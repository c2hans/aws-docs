# BYOIP "Use your address range in Amazon EC2" (byoip-working-with) — Attack / Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/byoip-working-with.html`
(offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/byoip-working-with.md`, 51 lines) + the
authoritative IAM reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`
(10,190 lines) + `/work/aws-docs/docs/ram/latest/userguide/shareable.md`.
Status: documentation-derived hypotheses only; nothing tested against a live account.
Drift check 2026-10-15: online `.md` == offline `.md`, byte-identical, no drift.

> **This is a page-level deep-dive COMPLEMENT of `ec2-byoip-attack-research-plan.md`** (the BYOIP
> service plan, itself a child of the `ec2-networking` hub). `byoip-working-with.html` is the **CONSUME /
> use-your-range page** — the step-by-step of pulling addresses *out* of an already-provisioned BYOIP pool.
> The parent plan already owns the lifecycle actions (Provision/Advertise/Withdraw/Deprovision), the full
> X.509/RDAP/ROA crypto ownership chain, and summarized the consume APIs in its §3 table + Lead 7 (IPv4
> within-pool squatting) and Lead 10 (RAM). **This plan does not restate those** — it develops the consume
> surface at mechanism level and OWNS the net-new granular findings the parent only table-rowed: the
> read-oracle scopability **asymmetry** (W1), the **IPv6-pool→VPC consume path** the parent's IPv4-only Lead 7
> never covered (W2), the systematic **create-vs-operate condition-key gap** (W3, sharpening Lead 7),
> **targeted-value selection** as a reputation/dangling primitive (W4), **release-to-pool recycling** (W5),
> and the **cross-account negative** closed for the direct-pool path (W6). Sibling complements:
> `byoip-onboard-attack-research-plan.md` (onboarding/advertise flow) and
> `prepare-for-byoip-attack-research-plan.md` (preparation artifacts).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity →
  Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The highest-value oracle for every lead here is **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`**
  — it settles "is this condition key / resource-ARN scoping actually enforceable?" with **no resources
  touched**. Escalate to a live scoped call only with canary data in an authorized account.
- **DryRun is caller-IAM-only, NOT an ownership oracle** (evaluated before resource resolution) — do not use
  it to answer "did the pool get consumed."
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service
  plane** (e.g. the BGP advertiser fleet, ASNs 16509/14618/8987/214101), stop, preserve evidence, flag for
  AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. Prove that a principal scoped to "consume pool A only" can nonetheless **enumerate the account's entire
   BYOIP inventory** (every provisioned IPv4/IPv6 pool + CIDR) via an unscopable `Describe*` oracle. (W1)
2. Prove that an admin writing the **natural, documented** CreateVpc/AssociateVpcCidrBlock policy (scoped on
   the required `vpc*` resource) gets **no enforcement** over *which* BYOIP IPv6 pool a caller drains. (W2)
3. Prove that `AllocateAddress --address <chosen-ip>` and `create-vpc --ipv6-cidr-block <chosen-cidr>` let a
   caller claim a **specific, high-value address/sub-range** of a shared BYOIP range that IAM cannot deny by
   value — including re-claiming a just-released reputation IP with live downstream DNS. (W3/W4)
4. Confirm (or refute) that the direct `ipv4pool-ec2` / `ipv6pool-ec2` resources are **not RAM-shareable**, so
   this page's surface is intra-account and the cross-account path runs only through VPC IPAM. (W6)

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane APIs over SigV4 (CLI shown): the IPv4 consume path
(`describe-public-ipv4-pools`, `allocate-address --public-ipv4-pool|--address`) and the IPv6 consume path
(`describe-ipv6-pools`, `create-vpc --ipv6-pool|--ipv6-cidr-block`, `associate-vpc-cidr-block --ipv6-pool`,
`get-associated-ipv6-pool-cidrs`, `describe-vpcs`, and disassociate→release-to-pool). No new service process,
network interface, or data-plane component is introduced by this page — it is a thin orchestration layer over
existing EC2 control APIs that read from / allocate out of the account's provisioned BYOIP pools.

**Assets.**
- **Provisioned BYOIP IPv4 pool** — resource type `ipv4pool-ec2`, ARN
  `arn:${Partition}:ec2:${Region}:${Account}:ipv4pool-ec2/${Ipv4PoolEc2Id}` (list_ec2 L9964). Holds the
  customer's advertised, reputation-bearing public IPv4 addresses.
- **Provisioned BYOIP IPv6 pool** — resource type `ipv6pool-ec2`, ARN
  `arn:${Partition}:ec2:${Region}:${Account}:ipv6pool-ec2/${Ipv6PoolEc2Id}` (list_ec2 L9965).
- **Elastic IP (`elastic-ip`)** minted *from* the IPv4 pool; **VPC IPv6 CIDR association** minted *from* the
  IPv6 pool. These are the consumed artifacts that then feed instances / NAT GWs / NLBs.
- The addresses themselves are the high-value asset: a BYOIP range is a **globally known, attacker-owned-by-the-
  customer, reputation-bearing** CIDR — unlike Amazon's ephemeral public-IPv4 pool, the whole range is public
  and enumerable, so "which specific address did I get" is security-relevant.

**Identity / trust.** Single-account: the caller consumes from pools their own account provisioned. There is
**no cross-tenant trust boundary on this page** — see W6 (direct pools are not RAM-shareable; cross-account
BYOIP consumption only exists via a *different* path, VPC IPAM pools, which this page's flags do not engage).

**ASCII (consume pipeline):**
```
                 provisioned BYOIP pools (account-scoped)
                 ┌───────────────────────────────────────┐
   describe-public-ipv4-pools ─▶ ipv4pool-ec2 ──allocate-address──▶ elastic-ip ──▶ EC2 / NATGW / NLB
   describe-ipv6-pools        ─▶ ipv6pool-ec2 ──create-vpc / ─────▶ VPC IPv6 CIDR ─▶ subnets / ENIs
   describe-byoip-cidrs       ─▶ (both)          associate-vpc-cidr-block
                 └───────────────────────────────────────┘
   get-associated-ipv6-pool-cidrs / describe-vpcs  = read-back
   disassociate-vpc-cidr-block / release-address   = return to shared pool
```

**Mandatory coverage sweep (pages checked for lens triggers):** read the full target page, the parent
`ec2-byoip.md`, `byoip-onboard.md`, `prepare-for-byoip.md`, the `list_ec2.md` rows for all 9 actions on this
page, the `ipv4pool-ec2`/`ipv6pool-ec2` resource-type definitions, the `ec2:PublicIpAddress`/`AllocationId`/
`Domain`/`Ipv4IpamPoolId`/`Ipv6IpamPoolId` condition-key definitions, and `ram/.../shareable.md`.
No URL/host field the service dereferences (SSRF N/A — §8); no upload/blob (Q N/A); no identity-proofing gate on
this page (P deferred to onboard/prepare siblings); no IAM policy JSON printed on this page (R N/A — the artifact
audit is the parent's); no KMS/attestation/token/transport mechanism (H/W/FF/Y N/A).

---

## 3. API / interface surface (IAM-anchored)

All rows from `list_ec2.md` **Actions** table (detailed, lines 4603–9762), re-verified 2026-10-15.
★ = required resource type (the one named in the policy `Resource` element). Line numbers are current.

| API | L | Mut. | Access | Resource types | Condition keys | Scopable to pool / address? |
|---|---|---|---|---|---|---|
| `AllocateAddress` | 4668 | yes | Write | `elastic-ip★`; `ipam-pool`; `ipv4pool-ec2` | elastic-ip: `aws:RequestTag`,`aws:TagKeys`,`ec2:Region`; pools: `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag` | pool: **tag/ARN only, no id-value key**; **address: NO (no `ec2:PublicIpAddress`)** |
| `DescribePublicIpv4Pools` | 7248 | no | List | **(blank)** | `ec2:Region` | **No — unscopable account-wide oracle** |
| `DescribeByoipCidrs` | 6630 | no | List | **(blank)** | `ec2:Region` | **No — unscopable account-wide oracle** |
| `CreateVpc` | 5749 | yes | Write | `ipam-pool`; `ipv6pool-ec2`; `vpc★` | pools: `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag`; vpc: `aws:RequestTag`,`aws:TagKeys`,`ec2:Ipv4IpamPoolId`,`ec2:Ipv6IpamPoolId`,`ec2:Region`,`ec2:VpcID` | VPC: yes; **IPv6 pool: ARN only on the contextual row, no `ec2:Ipv6Pool` value key, no CIDR key** |
| `AssociateVpcCidrBlock` | 4832 | yes | Write | `ipam-pool`; `ipv6pool-ec2`; `vpc★` | pools: tag/region; vpc: `aws:ResourceTag`,`ec2:Ipv4IpamPoolId`,`ec2:Ipv6IpamPoolId`,`ec2:Region`,`ec2:ResourceTag`,`ec2:Tenancy`,`ec2:VpcID` | VPC: yes; **IPv6 pool: same gap as CreateVpc** |
| `GetAssociatedIpv6PoolCidrs` | 8204 | no | Read | `ipv6pool-ec2★` | `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag` | **Yes — by pool ARN/tag (the lone scopable read)** |
| `DescribeIpv6Pools` | 7080 | no | List | **(blank)** | `ec2:Region` | **No — unscopable account-wide oracle** |
| `DescribeVpcs` | 7686 | no | List | **(blank)** | `ec2:Region` | **No — unscopable account-wide oracle** |
| `DisassociateVpcCidrBlock` | 7999 | yes | Write | `vpc` (no ★ — doc inconsistency) | `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag`,`ec2:Tenancy`,`ec2:VpcID` | VPC: yes; **destination pool: NO (no `ipv6pool-ec2` row)** |

**Condition-key ground truth (definitions):** `ec2:PublicIpAddress` (L10136), `ec2:AllocationId` (L10049),
`ec2:Domain` (L10072) — the EIP triple, carried on **all 11 operate-on-existing-EIP actions**
(AcceptAddressTransfer 4611, AssociateAddress 4714, AssociateNatGatewayAddress 4776, CreateNatGateway 5320,
DisableAddressTransfer 7755, DisassociateAddress 7887, DisassociateNatGatewayAddress 7941, EnableAddressTransfer
8008, ModifyAddressAttribute 8720, ReleaseAddress 9386, ResetAddressAttribute 9492) — and **absent from
`AllocateAddress`** (the only EIP-creating action). `ec2:Ipv4IpamPoolId`/`ec2:Ipv6IpamPoolId` are the ONLY
pool-id-shaped keys and are **IPAM-specific** (a different allocation path than this page's `--ipv6-pool`/
`--public-ipv4-pool`). **0 hits** anywhere for `ec2:PublicIpv4Pool`, `ec2:Ipv4PoolEc2`, `ec2:Ipv6Pool`,
`ec2:Ipv6PoolEc2`, `ec2:Address`, or any CIDR-value key.

---

## 4. Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Intra-account principal scoped to consume pool A | The account's **entire** BYOIP inventory (all pools + CIDRs) | `Describe{PublicIpv4Pools,Ipv6Pools,ByoipCidrs,Vpcs}` are unscopable | A principal that can only `AllocateAddress` on pool A still lists every provisioned pool/CIDR in the account/region → **recon boundary breach** (the grant implied pool-A-only visibility) |
| Team B principal (shared BYOIP pool) | A **specific** address / sub-range of the shared range | `AllocateAddress --address` / `create-vpc --ipv6-cidr-block` lack any value condition key | Team B claims a chosen (reputation-sensitive / recently-released) address from the shared pool that IAM could not deny = **within-pool squatting** |
| Any consumer | Which BYOIP pool a VPC drains | CreateVpc/AssociateVpcCidrBlock only `vpc*`-scopable in the documented pattern | A consumer drains pool A's IPv6 space through a policy the admin believed only authorized "create VPCs" = **pool-selection control gap** |
| Caller's account | **Another account** | — | **No boundary exists on this page** — direct pools are not RAM-shareable (W6); any cross-account reach would be the VPC-IPAM path (out of scope here) |

---

## 5. Recommended Areas of Focus (one block per firing lens)

### W1 — Consume-path read-oracle scopability ASYMMETRY (HEADLINE) — Lens S / X / A
**Background.** The page's four read/list actions expose the BYOIP inventory; the mutating consume actions pull
from it. In the IAM reference the two groups are scoped *inconsistently*.
**Security Concern.** `DescribePublicIpv4Pools` (L7248), `DescribeByoipCidrs` (L6630), `DescribeIpv6Pools`
(L7080) and `DescribeVpcs` (L7686) all have a **blank resource-type cell and only `ec2:Region`** → they are
**fully unscopable account-wide oracles**: a principal cannot be restricted to "see only pool A." Yet the
*mutating* consumers (`AllocateAddress`, `CreateVpc`, `AssociateVpcCidrBlock`) and the one Read action
`GetAssociatedIpv6PoolCidrs` (L8204, `ipv6pool-ec2★`) **are** pool-ARN/tag-scopable. So an admin who scopes
*consumption* to one pool cannot scope *enumeration* of the whole inventory. This is the same inert-ABAC /
unscopable-Describe shape confirmed on `manage-spot-fleet`'s `DescribeSpotFleetRequests` and the
`capacity-reservation` Describe oracles — applied to BYOIP consume.
**High-level Test Scenarios.**
- **Claim:** a role with `ec2:AllocateAddress` scoped to `ipv4pool-ec2/<poolA>` + `ec2:DescribePublicIpv4Pools`
  can enumerate *every* IPv4 pool (incl. pool B it has no allocate rights on) and every provisioned CIDR.
  → **Oracle:** `iam:SimulateCustomPolicy` on `DescribePublicIpv4Pools` with any `Resource`/`Condition`
  narrower than `*` returns the key as **inert** (no resource type to bind); the simulate shows allow
  regardless of pool. No live resource touched.
- **Claim:** the asymmetry means recon always precedes (and is never gated by) the consumption control.
**Doc evidence:** list_ec2 L7248/6630/7080/7686 (blank resource type) vs L8204 (`ipv6pool-ec2★`).
**Severity-if-true:** Medium (intra-account cross-team recon of the org's full reputation-IP inventory;
force-multiplier for W4 targeting). CONFIRMED structural from the reference.

### W2 — IPv6-pool consume is unscopable in the documented pattern (the IPv4-squatting twin) — Lens S / U
**Background.** Parent Lead 7 covered IPv4 within-pool squatting only. This page introduces the **IPv6** consume
path (`create-vpc --ipv6-pool`, `associate-vpc-cidr-block --ipv6-pool`) that no sibling has analyzed.
**Security Concern.** On both `CreateVpc` (L5749) and `AssociateVpcCidrBlock` (L4832), the only **required** (★)
resource type is `vpc`, scopable by `ec2:VpcID`/tags. `ipv6pool-ec2` appears only as a **contextual
(non-required) resource row** carrying nothing but `aws:ResourceTag`/`ec2:Region`/`ec2:ResourceTag`. There is
**no `ec2:Ipv6Pool` value key and no CIDR-value key** (`ec2:Ipv6IpamPoolId` is IPAM-only, a *different* flag). So
the natural, documented policy — scoped on the `vpc*` resource the admin is thinking about — grants **zero
enforcement over which BYOIP IPv6 pool is drained**. Pool-ARN scoping on the contextual row *is* technically
possible but is coarse, undocumented as the pattern, and trivially omitted.
**High-level Test Scenarios.**
- **Claim:** a role allowed `ec2:CreateVpc` scoped to a tag/VPC condition (no `ipv6pool-ec2` Resource clause)
  can create a VPC that pulls an IPv6 CIDR from **any** provisioned BYOIP IPv6 pool in the account.
  → **Oracle:** `iam:SimulateCustomPolicy` showing CreateVpc allowed with the pool unbound; confirm no
  `ec2:Ipv6Pool`-class key exists to add. Live: in a lab account, a `vpc*`-only-scoped role runs
  `create-vpc --ipv6-pool <poolB>` and succeeds.
- **Claim:** an admin cannot express "this team may create VPCs but never consume BYOIP pool B" without
  resorting to an explicit `Deny` on `Resource: ...ipv6pool-ec2/<poolB>` — not the shape the docs lead them to.
**Doc evidence:** list_ec2 L5749/5752/5753, L4832/4835/4836; byoip-working-with.md L32–42.
**Severity-if-true:** Medium (intra-account pool-selection control gap; the IPv6 analogue of Lead 7).

### W3 — Create-vs-operate condition-key gap: the control to pin an address exists everywhere except where it is chosen — Lens X / S / U
**Background.** Sharpens parent Lead 7 from "AllocateAddress lacks `ec2:PublicIpAddress`" into a **systematic
family asymmetry** across the whole EIP action set.
**Security Concern.** The triple `ec2:PublicIpAddress`/`ec2:AllocationId`/`ec2:Domain` is carried on **all 11
actions that operate on an *existing* EIP** (Associate/Disassociate/Release/Modify/Reset/Accept/Enable/Disable-
transfer, NAT-gw assoc) — but is **absent from `AllocateAddress`**, the one action that *mints* the EIP and
*chooses* its value via `--address`. The admin can therefore restrict *which EIP a principal may release or
move* (by IP/allocation-id), but **cannot restrict which IP a principal may claim at allocation**. The control
arrives one step too late: the value is bound at create, where no key gates it.
**High-level Test Scenarios.**
- **Claim:** no policy can express "allow AllocateAddress from pool A but deny `--address 203.0.113.7`."
  → **Oracle:** `iam:SimulateCustomPolicy` — a `Deny` keyed on `ec2:PublicIpAddress` for `AllocateAddress`
  evaluates **inert** (key not present on the action), while the same Deny on `ReleaseAddress` is honored.
  The simulate divergence between the two actions *is* the finding; no resource touched.
**Doc evidence:** list_ec2 L4668–4673 (AllocateAddress, triple absent) vs L9386 (ReleaseAddress, triple present)
+ the 11-action carrier list in §3; `ec2:PublicIpAddress` def L10136.
**Severity-if-true:** Medium (least-priv footgun, CONFIRMED structural). Elevates to the severity of W4 when the
chosen address is reputation-/DNS-sensitive.

### W4 — Targeted-value selection as a reputation / dangling-DNS primitive — Lens A / EE-flavored
**Background.** A BYOIP range is a **globally known, customer-owned, reputation-bearing** CIDR — every address
in it is public and enumerable (unlike Amazon's opaque ephemeral pool). The page explicitly offers value-pick:
`allocate-address --address <ip>` and `create-vpc --ipv6-cidr-block <cidr>` / `associate-vpc-cidr-block`.
**Security Concern.** Because no value condition key exists (W2/W3), a caller sharing the pool can claim a
**specific** address or sub-range: (a) re-claim a reputation IP a sibling just released (allow/deny-list value);
(b) **re-bind a recently-released address that still has live downstream DNS / allow-listing pointing at it** —
a BYOIP-specific dangling-takeover that is *sharper* than the ephemeral-public-IPv4 case because the attacker
already knows and co-owns the whole range and can target the exact freed address; (c) race a sibling for a
chosen value. The predictable-namespace flavor of Lens EE: the "namespace" is the known BYOIP CIDR, selection is
first-come, and nothing pins the value to an owner.
**High-level Test Scenarios.**
- **Claim:** after team A runs `release-address` on a reputation IP, team B can immediately
  `allocate-address --address <that-ip> --public-ipv4-pool <poolA>` and bind it to its own resource.
  → **Oracle:** two-role lab in one account; confirm the chosen `--address` is granted with no cooldown.
- **Claim:** the IPv6 twin — pick a specific `--ipv6-cidr-block` sub-range of the pool on `create-vpc`.
**Doc evidence:** byoip-working-with.md L21 (`--address`), L32–42 (`--ipv6-cidr-block`); the no-value-key facts
of W2/W3.
**Severity-if-true:** intra-account Medium on its own; **inherits High** when chained to a live dangling-DNS /
allow-list takeover. **Cross-reference** `using-instance-addressing-attack-research-plan.md` and
`working-with-ip-addresses-attack-research-plan.md` for the EIP-takeover + ephemeral-pool-reuse + dangling-DNS
mechanisms — **this plan owns only the "BYOIP pool feeds that primitive with attacker-chosen precision" slice.**

### W5 — Release-to-pool recycling is unscopable by destination pool — Lens S / U
**Background.** Disassociating an IPv6 CIDR "releases it back into your IPv6 address pool" (page L50); releasing
an EIP returns the address to the IPv4 pool. These returns re-stock the shared pool that W4 then re-picks from.
**Security Concern.** `DisassociateVpcCidrBlock` (L7999) lists **only the `vpc` resource type — no
`ipv6pool-ec2` row at all** → an admin cannot scope *which pool* a CIDR is returned to (only which VPC/
association is torn down). Combined with no documented re-use cooldown on this page, release feeds the W4 recycle
loop. Minor Lens-U doc-integrity note: the `vpc` row on DisassociateVpcCidrBlock lacks the `*required` marker
its CreateVpc/AssociateVpcCidrBlock twins carry — an inconsistency to confirm is cosmetic, not a semantic
difference.
**High-level Test Scenarios.**
- **Claim:** no policy can gate the pool a disassociation returns a CIDR to.
  → **Oracle:** list_ec2 L7999–8003 shows no `ipv6pool-ec2` resource row; `iam:SimulateCustomPolicy` confirms
  no pool-scoping clause binds.
**Doc evidence:** list_ec2 L7999–8003; byoip-working-with.md L50.
**Severity-if-true:** Low–Medium (enabler for W4).

### W6 — Cross-account negative: direct pools are NOT RAM-shareable (closes parent Lead 10 for this path) — Lens AA / U
**Background.** Parent Lead 10 asked whether BYOIP pools cross an account boundary via RAM.
**Security Concern (resolved as a negative).** `ram/.../shareable.md` lists `ec2:IpamPool` (L420, shareable with
any account) and `ec2:CoipPool` (L419, Org-only) — but **no entry for `ipv4pool-ec2` or `ipv6pool-ec2`**; a
corpus-wide grep for `ipv6pool-ec2` hits only EC2 docs, CFN tag-specs, and examples, never a RAM-sharing page.
So the **direct** BYOIP pools this page consumes are **not RAM-shareable**: cross-account BYOIP consumption
exists only by onboarding the CIDR into a **VPC IPAM pool** (RAM-shareable, uses `ec2:Ipv4IpamPoolId`/
`ec2:Ipv6IpamPoolId` — keys this page's `--public-ipv4-pool`/`--ipv6-pool` flags do **not** engage).
**Consequence for scope:** every lead on this page (W1–W5) is **intra-account** (cross-team least-priv /
recon). The cross-account surface is a *different* path (IPAM) and belongs to the VPC-IPAM docs, outside this
mirror.
**High-level Test Scenario.** Confirm no `create-resource-share` accepts an `ipv4pool-ec2`/`ipv6pool-ec2` ARN.
**Doc evidence:** `ram/.../shareable.md` L419–421; list_ram.md (RAM's own resource types only).
**Severity:** Informational (scope-bounding; prevents the hunter chasing a nonexistent cross-tenant boundary).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Scoped consumer enumerates full BYOIP inventory | `Describe{PublicIpv4Pools,Ipv6Pools,ByoipCidrs,Vpcs}` | "unscopable, `ec2:Region` only" — mitigation is **absent** (W1) |
| Drain any IPv6 pool via a `vpc*`-scoped policy | `CreateVpc`/`AssociateVpcCidrBlock` | ARN-scope the `ipv6pool-ec2` contextual row (undocumented, easily omitted) (W2) |
| Claim a chosen reputation / dangling address | `AllocateAddress --address`, `CreateVpc --ipv6-cidr-block` | no value condition key — mitigation **not expressible** (W3/W4) |
| Return a CIDR to a pool the admin meant to fence | `DisassociateVpcCidrBlock` | no `ipv6pool-ec2` resource row — **not scopable** (W5) |
| Reach another account's BYOIP range | (none on this page) | direct pools not RAM-shareable → **no boundary to breach here** (W6) |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account / cross-tenant BYOIP consumption** — does not exist on this page's surface; rides VPC IPAM
  pools (`ec2:IpamPool`), covered by VPC-IPAM docs outside this mirror (W6).
- **The BYOIP lifecycle, crypto ownership chain, and advertise/withdraw DoS** — owned by the parent
  `ec2-byoip` plan and `byoip-onboard`/`prepare-for-byoip` siblings.
- **EIP-transfer, ephemeral-public-IPv4 reuse, generic dangling-DNS takeover mechanism** — owned by
  `using-instance-addressing` / `working-with-ip-addresses` plans; W4 here is only the BYOIP-pool feed-in slice.
- **IMDS / shared managed-host / service-plane infra** — not reached by this page.
- **Customer-authored least-privilege footguns** — W1–W5 are reported as *structural reference gaps* (AWS cannot
  express the control), not as customer mis-writes; the customer cannot fix an absent condition key. Still only
  intra-account Medium at most, so Tier-3 informational unless chained to W4 takeover.

---

## 8. Null hypotheses / doc gaps
- **SSRF (G): N/A** — read all page actions + flags; no field the service dereferences (fetches/validates/
  renders) server-side. `--address`/`--ipv6-cidr-block`/`--ipv6-pool` are value selectors, not URLs.
- **Upload / rich content (Q): N/A** — no blob/file/image input on this page.
- **Identity proofing (P): N/A here** — the ownership-proofing gate lives at provision time (parent + onboard);
  consume assumes an already-provisioned pool.
- **IAM-artifact audit (R): N/A here** — no managed/sample policy JSON is printed on this page; the artifact
  audit belongs to the parent.
- **KMS (H), Attestation (W), Token/JWT (FF), Transport/TLS (Y), Translation-injection (F), Prompt (K): N/A** —
  none of those mechanisms appear on this page.
- **Doc gaps for the next agent:** (1) Is there a **re-use cooldown** on release-to-pool before an address/CIDR
  can be re-allocated? Not stated on this page — the key open question gating W4's dangling-takeover timing;
  needs live confirm. (2) Does `allocate-address --address` enforce that the IP is **within** the named pool, or
  can it pull any address the account provisioned regardless of `--public-ipv4-pool`? (3) Confirm the
  DisassociateVpcCidrBlock missing-`*` is cosmetic. (4) VPC IPAM pool sharing (`ec2:IpamPool` + the
  `ec2:Ipv4IpamPoolId`/`ec2:Ipv6IpamPoolId` consume path) — the *only* cross-account BYOIP surface — needs the
  VPC-IPAM docs pulled into the mirror to analyze.

### Drift check result (online vs offline)
`byoip-working-with.md`: online == offline, **byte-identical**, no material drift (2026-10-15). All `list_ec2.md`
line numbers re-verified against the current offline mirror.

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)
