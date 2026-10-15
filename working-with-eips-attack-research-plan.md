# Working with Elastic IP addresses (Allocate / Associate / Disassociate) — Attack / Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-eips.html
(offline mirror: `docs/AWSEC2/latest/UserGuide/working-with-eips.md`; page H1 is *"Associate an Elastic IP address with an instance"*, topics = **Allocate / Associate / Disassociate an Elastic IP address**).
**Service / surface:** Amazon EC2 — the **operational mechanics** of the EIP lifecycle: `AllocateAddress`, `AssociateAddress`, `DisassociateAddress`, and the four *allocation sources* the page exposes (Amazon pool, BYOIP `ipv4pool-ec2`, Outpost customer-owned pool, **IPAM pool** with `--address` targeting) and the two *association targets* (instance vs network-interface, with a `--private-ip-address` sub-target).

**Position in corpus:** This is the **procedural child / complement** of `elastic-ip-addresses-eip-attack-research-plan.md` (the EIP overview plan, itself a page-level child of the `ec2-networking` hub). The two plans share the same four actions; to avoid duplication:
- **This plan OWNS the *operation-mechanics* net-new surface** that the overview page did not reach because it is only exposed on this procedural page: **IPAM-pool targeted/sequential allocation** (`--ipam-pool-id` + `--address`), the **allocation-source selection** matrix (`--public-ipv4-pool` / customer-owned / IPAM), and the **associate `--private-ip-address` sub-target** (bind an EIP onto a *secondary* private IP).
- **This plan DEFERS** to the overview plan: cross-account **transfer** hijack (overview T1–T5), **released-EIP shared-pool squatting** (overview L1–L3), **reverse-DNS** (overview D1–D2), the **base forced-reassociation steal** (overview S1), **unscopable read oracles** (overview O1–O2), **NetworkBorderGroup zero-IAM-key** (overview B1), and the **7-day/7-hour** doc contradiction (overview X1). Where this page sharpens one of those, it is noted inline as "sharpens overview-<id>", not re-derived.
- **Sibling cross-refs:** `using-instance-addressing-attack-research-plan.md` (secondary private-IPv4 cross-ENI/cross-account takeover + "EIP rides along"), `ec2-byoip-attack-research-plan.md` + `byoip-working-with-attack-research-plan.md` (BYOIP `ipv4pool-ec2` pool ownership/consume), `working-with-ip-addresses-attack-research-plan.md` (launch-time public-IP). IPAM-pool RAM-share mechanics live in the VPC-IPAM docset (out of this page's folder but pulled in here because this page is the first EC2 surface that *consumes* an IPAM pool for EIPs).

**Method:** `security-questionbuilder` (boundary-first). Documentation-only; no live AWS calls. Every lead is a falsifiable claim + confirm/refute oracle for a downstream hunter. Online `.md` cross-checked against the offline mirror (byte-identical here). IAM reality read from `list_ec2.md` offline (online truncates condition-key tables), per [[reference-aws-iam-service-auth-ref-url]].

---

## §0 — Executive summary (what *this page* adds over the overview)

The overview plan established that EIP security is structurally under-governed by IAM. This procedural page adds **four allocation sources** and a **private-IP association sub-target**, and the IAM reference shows the *new* knobs are also largely unscopable:

1. **IPAM-pool EIP allocation is scopable by tag only — the natural ID key is absent.** `AllocateAddress` on the `ipam-pool` resource type supports **only** `aws:ResourceTag` / `ec2:Region` / `ec2:ResourceTag` (list_ec2 L4671). The dedicated key **`ec2:Ipv4IpamPoolId` exists but is attached to `CreateVpc` / `CreateSubnet` / `CreatePublicIpv4Pool` (L4836/4804/5480), NOT to `AllocateAddress`** → you cannot write a policy restricting *which IPAM pool ID* a principal pulls an EIP from unless every pool is correctly tagged. Classic Lens-S "the obvious key exists elsewhere but not here" asymmetry (Lead **N1**).
2. **The `--address` parameter lets a caller demand a *specific* IP from an IPAM pool, and nothing scopes the IP value.** `AllocateAddress` has **no `ec2:PublicIpAddress` key on any of its three resource rows** (L4670–4672). The page explicitly markets *"Allocating sequential Elastic IP addresses"* from a contiguous IPAM block. In a **RAM-shared / org-shared public-IPv4 IPAM pool** (confirmed shareable to accounts/OUs/org; the `AWSRAMDefaultPermissionsIpamPool` permission bundles allocate+release+view-all), a consumer who calls `allocate-address --ipam-pool-id <shared> --address <chosen>` can **land-grab a specific, predictable address** a peer account expects next (and read every account's allocations via `GetIpamPoolAllocations` first) — a cross-account targeting primitive the overview's shared-*Amazon*-pool squatting (overview L1) does not cover (Leads **N2 / N2a**, Lens EE/AA/A).
3. **`AssociateAddress --private-ip-address` can bind an EIP onto a *secondary* private IP, and the private IP is unscopable.** API ref: *"The primary **or secondary** private IP address to associate with the Elastic IP address"* (`API_AssociateAddress.md` L50-52). `AssociateAddress` has **no `ec2:PrivateIpAddress` key** (L4714-4716). Chained with the secondary-private-IP cross-ENI/cross-account takeover in `using-instance-addressing`, this is the step that *attaches public reachability* to a hijacked secondary IP — the public-side half of that steal (Lead **N3**, Lens A/S).
4. **Allocation-source selection (`--public-ipv4-pool` BYOIP / customer-owned Outpost pool) is likewise tag-only.** The BYOIP `ipv4pool-ec2` row supports only tag/Region keys (L4672); no key for the pool CIDR or the specific address (Lead **N4**, Lens S/U — defers BYOIP pool ownership to `ec2-byoip`).

**Highest-value leads here:** **N2 (+N2a)** (IPAM shared-pool targeted/sequential land-grab + cross-account allocation oracle — the one genuinely new cross-account primitive on this page, documentation-confirmed), **N3** (secondary-private-IP EIP binding, the public-reachability half of the secondary-IP steal), **N1** (IPAM-pool-ID unscopable on AllocateAddress).

---

## §1 — Components, Assets, and Design (delta over overview §1)

### Customer-facing interface
Same as overview: EC2 public API (SigV4 IAM), console **Elastic IPs** pane, CLI/PowerShell. This page adds no non-SDK endpoints. The *new* request parameters this page surfaces:
- `allocate-address`: `--network-border-group`, `--public-ipv4-pool <ipv4pool-ec2-…>` (BYOIP), `--customer-owned-ipv4-pool` (Outpost), `--ipam-pool-id <ipam-pool-…>` **+ `--address <specific IPv4>`** (IPAM sequential), `--tag-specifications`.
- `associate-address`: `--instance-id` **xor** `--network-interface-id`, `--allocation-id`, **`--private-ip-address`**, `--allow-reassociation`.
- `disassociate-address`: `--association-id`.

### Assets (new relative to overview)
- **The IPAM pool** (`ipam-pool-…`) and the **contiguous public-IPv4 CIDR** it manages — a *shared, cross-account* inventory asset when RAM-shared. An individual *address* inside it is targetable by value.
- **The specific private IP on an ENI** (`--private-ip-address`) — selecting a secondary private IP routes a public EIP onto a *particular* workload binding, not just "the instance".

### Ownership / trust zones (new seam)
- **IPAM-pool owner account ↔ consumer accounts of a RAM-shared pool.** When a public-IPv4 IPAM pool is shared across an Organization, every consumer draws EIPs from one contiguous block the owner provisioned. One consumer's `--address` choice reaches into inventory the owner (and peer consumers) also see — a **cross-account land-grab + inventory seam** this page is the first to open. *(Exact RAM mechanics pending sub-research — see N2.)*
- **Caller's `AssociateAddress` request ↔ a specific private-IP binding on a (possibly multi-tenant / shared-VPC) ENI** — the private-IP sub-target reaches *inside* an ENI's address set.

### Untrusted-data entry points (new)
- `AllocateAddress.Address` as a **targeting** value against an IPAM pool (not just the overview's "recover" use).
- `AllocateAddress.IpamPoolId` / `PublicIpv4Pool` / `CustomerOwnedIpv4Pool` — pool-source selectors, existence-validated.
- `AssociateAddress.PrivateIpAddress` — free IPv4 string resolved against the target ENI's private-IP set.

### Connection sketch (this page's slice)
```
  [ Amazon pool ]  [ BYOIP ipv4pool-ec2 ]  [ Outpost customer-owned ]  [ IPAM pool (maybe RAM-shared across org) ]
          \_______________\___________________________\__________________________/
                                         |  allocate-address  (--address targets a SPECIFIC ip; NO ec2:PublicIpAddress key;
                                         |                      ipam-pool row: NO ec2:Ipv4IpamPoolId key -> tag-only)
                                         v
                                  elastic-ip / eipalloc-...
                                         |  associate-address  --private-ip-address <primary OR secondary>
                                         |                      (NO ec2:PrivateIpAddress key -> binding target unscopable)
                                         v
                            instance  |  network-interface  --(a chosen private IP, maybe a secondary belonging to another workload)
```

---

## §2 — Trust-boundary map (rows unique to this page)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Consumer account C of a RAM-shared public-IPv4 IPAM pool | A *specific* address in the owner's contiguous block | `allocate-address --ipam-pool-id <shared> --address <chosen/next-sequential>` | C obtains the *exact* address a peer/owner expected → predictable-name land-grab; **no `ec2:PublicIpAddress` key** can forbid the value (N2) |
| Principal P with `ec2:AllocateAddress` (tags not enforced) | Any IPAM pool reachable to the account | `allocate-address --ipam-pool-id <any>` | P pulls from a pool a policy "intended" to exclude — **`ec2:Ipv4IpamPoolId` is not an AllocateAddress key**, so only a tag Condition (if present) stands (N1) |
| Principal P with `ec2:AssociateAddress` on an EIP | A *secondary* private IP on a target ENI | `associate-address --allocation-id X --network-interface-id N --private-ip-address <secondary>` | Public EIP is bound to a chosen private IP, not just "the primary" — **no `ec2:PrivateIpAddress` key**; chains to secondary-IP takeover (N3) |
| Principal with `ec2:AllocateAddress` on `ipv4pool-ec2`/customer-owned | A specific BYOIP/Outpost address | source-selector + `--address` | Pulls a chosen address from a bring-your-own block; scopable by tag only (N4; BYOIP ownership → `ec2-byoip`) |
| **Any customer surface** | **AWS's own BGP / IPAM service plane** | — | **HARD STOP** — any AWS-fleet credential/identity/ARN or control-plane reach ⇒ preserve evidence, flag for disclosure |

---

## §3 — API / interface surface (this page's actions, with the net-new columns)

| Name | Mut? | Resource rows (list_ec2) | Condition keys of interest | This-page note |
|---|---|---|---|---|
| `AllocateAddress` | ✓ | `elastic-ip*` (L4670); `ipam-pool` (L4671); `ipv4pool-ec2` (L4672) | `elastic-ip*`: `aws:RequestTag`,`aws:TagKeys`,`ec2:Region`. `ipam-pool`/`ipv4pool-ec2`: `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag` | **NO `ec2:PublicIpAddress`** on any row (IP value unscopable); **NO `ec2:Ipv4IpamPoolId`** (pool ID unscopable — present on CreateVpc/CreateSubnet/CreatePublicIpv4Pool). `--address` targets a specific IP (N1/N2/N4). |
| `AssociateAddress` | ✓ | `elastic-ip` (L4714); `instance` (L4715); `network-interface` (L4716) — **all alternates, none `*`-required** | `elastic-ip`: `ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,tags,Region. `instance`: `ec2:InstanceID`+metadata keys. `network-interface`: `ec2:NetworkInterfaceID`,`ec2:Subnet`,`ec2:Vpc`. | **NO `ec2:PrivateIpAddress`** → `--private-ip-address` (primary **or secondary**) unscopable (N3). `AllowReassociation` default-auto, **not** an IAM key (sharpens overview-S1). |
| `DisassociateAddress` | ✓ | `elastic-ip`,`network-interface` (L7885+) | `ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,tags,Region | Collateral behavior defers to overview-S2 / `instance-secondary-ip-addresses`. |

(Full transfer/release/modify/describe inventory lives in the overview plan §3; not repeated here.)

---

## §4 — Leads (falsifiable, with oracle) — net-new to this page

### N1 — IPAM-pool allocation is scopable by tag only; `ec2:Ipv4IpamPoolId` absent from AllocateAddress (Lens S)
*Claim:* An IAM policy **cannot** restrict *which IPAM pool ID* a principal allocates an EIP from, because `AllocateAddress`'s `ipam-pool` resource row (list_ec2 L4671) supports only `aws:ResourceTag`/`ec2:Region`/`ec2:ResourceTag` — the dedicated `ec2:Ipv4IpamPoolId` key exists in EC2 but is wired to `CreateVpc`/`CreateSubnet`/`CreatePublicIpv4Pool` (L4836/4804/5480), **not** here. The only lever is an `aws:ResourceTag` Condition on the pool, which silently fails open for any pool missing the required tag.
*Mechanism:* list_ec2 L4671 vs L4836/4804/5480; key definition L10102 ("Filters access by the ID of an IPAM pool provided for IPv4 CIDR block allocation").
*Oracle:* craft a policy denying `ec2:AllocateAddress` unless `ec2:Ipv4IpamPoolId` equals an allowed pool → confirm the Condition is **inert** (key never populated for this action, so a Deny never matches / an Allow is vacuous). Then confirm a `ResourceTag`-based scope is the only thing that works and only when the pool is tagged.
*Preconditions/cost:* 1 account, ≥2 IPAM pools. Free, single-call.
*Severity:* **Medium** — least-privilege / blast-radius gap on multi-pool accounts; the enabler for N2 when pools are shared.

### N2 — Targeted / sequential IP land-grab from a RAM-shared IPAM pool (Lens EE + AA) — **headline, cross-account confirmed by docs**
*Claim:* A consumer principal of a RAM-shared **public-IPv4** IPAM pool can allocate a **specific, predictable `/32`** (`--address <X>`, or the next sequential address) that a *peer account* in the same org/share expected to receive next, because (a) AWS explicitly markets *"Allocate **sequential** Elastic IP addresses … from a contiguous public IPv4 block"* with worked `192.0.2.0 … .3` / `18.97.0.41` (next-in-block) examples, (b) `--address` lets a caller choose *"a specific `/32` in your IPAM pool"*, and (c) `AllocateAddress` has **no `ec2:PublicIpAddress` key** to forbid a value and the shared-pool allocation rules only gate by **netmask / tags / locale**, never by a specific excluded address. The single RAM managed permission **`AWSRAMDefaultPermissionsIpamPool`** bundles *allocate + release + view-all-allocations*, so any shared principal gets the full primitive. This is a cross-account dangling-trust + targeted-DoS primitive the overview's *Amazon*-pool squatting (overview L1) does not cover (that path cannot target a value and is same-pool-only).
*Mechanism (doc-confirmed):*
  - RAM-shareability: `vpc/latest/ipam/share-pool-ipam.html` — *"principals can allocate CIDRs from the pool … A principal … means any AWS account, IAM role or organizational unit"*; the `AWSRAMDefaultPermissionsIpamPool` permission *"allow[s] principals to view the CIDRs and allocations in the shared IPAM pool and allocate/release CIDRs in the pool."*
  - Exact-address + sequential: `vpc/latest/ipam/tutorials-eip-pool.html` — *"you can also choose a specific `/32` … by using the `--address` option"*; *"allocate **sequential** Elastic IP addresses"* with contiguous `192.0.2.0/30` → `.0 .1 .2 .3` example; tutorial walks the block (`18.97.0.41` = next in `18.97.0.40/29`). Target page `working-with-eips.html` carries `allocate-address --ipam-pool-id … --address 192.0.2.0`.
  - No IP/pool-ID key: list_ec2 L4670-4672 (no `ec2:PublicIpAddress`, no `ec2:Ipv4IpamPoolId`); allocation rules per `create-top-ipam.html` gate only netmask/tags/locale.
  - Ownership + recycle: `API_AllocateAddress.md` — EIP is allocated *"to **your** account"* (consumer owns it, not the pool owner); on release it *"can be allocated to a **different** AWS account"*; `release-alloc-ipam.html` — recycled CIDR becomes reclaimable after **a few minutes (Advanced Tier)** or **up to 48 h (Free Tier)**, then grabbable by *any* consumer. No sanctioned alternative: *"You **cannot transfer** sequential Elastic IP addresses allocated from an IPAM pool to other AWS accounts"* — pool-sharing is the only cross-account path.
*Oracle:* in a 2-account org with a RAM-shared public-IPv4 IPAM pool (consumer C holds `AWSRAMDefaultPermissionsIpamPool`): (1) C runs `get-ipam-pool-allocations` to read peer allocations and pick the next-sequential/high-value target; (2) C calls `allocate-address --ipam-pool-id <shared> --address <that address>`; confirm it succeeds and the EIP lands in C's account. **The one doc-gap is whether `--address <already-allocated>` fails fast, waits, or is silently refused — the pre-emptive-squat-before-peer-allocates case needs live confirmation.** Also time the release→reclaim window (minutes vs 48 h) to size the recycle-squat race.
*Preconditions/cost:* org + IPAM (Organizations-integrated) + RAM-shared public-IPv4 pool + 2 consumer accounts; `AWSRAMDefaultPermissionsIpamPool` on the consumer. Low cost (EIP hourly charge only).
*Severity:* **High** — cross-account targeted address acquisition (dangling-trust takeover of an address a peer's allowlists/DNS/reputation point at, **and** targeted denial of a peer's expected sequential address) with no per-address ownership/exclusion control; the sanctioned sharing model *is* the attack surface.
*Stop condition:* allocating the one target address (or reading the allocation inventory) is the PoC — do not weaponize inherited trust.

### N2a — Shared-pool allocation inventory is a built-in cross-account oracle (Lens A, feeder for N2)
*Claim:* `GetIpamPoolAllocations` returns **every** allocation in a shared pool — *including other accounts' allocations* — with each entry carrying `resourceOwner` (the allocating account ID) and `cidr`, and this view is bundled into the same `AWSRAMDefaultPermissionsIpamPool` RAM permission that grants allocate. So any consumer can enumerate which account holds which `/32` and predict the next sequential address to target in N2.
*Mechanism:* `vpc/latest/ipam/view-alloc-ipam.html` — *"get-ipam-pool-allocations … view all allocations in a specific pool that you own or that has been shared with you … This includes allocations that are not directly owned by you … including allocations owned by other accounts."* Contrast `API_DescribeIpamPoolAllocations.md` — *"returns **only** allocations directly owned by you"* (the owner-scoped twin; a Lens-X parity note — two APIs, divergent cross-account exposure). `API_IpamPoolAllocation.md` field `resourceOwner` = *"The owner of the resource."*
*Oracle:* as a consumer, `get-ipam-pool-allocations --ipam-pool-id <shared>` → confirm peer accounts' `resourceOwner`+`cidr` are returned; confirm `describe-ipam-pool-allocations` does **not** show them (parity divergence).
*Severity:* **Medium** (cross-account recon / timing oracle; raises N2 feasibility).

### N3 — EIP binding onto a *secondary* private IP is unscopable; public-reachability half of the secondary-IP steal (Lens A/S)
*Claim:* `AssociateAddress --private-ip-address` can bind an EIP onto a **secondary** private IP (not just the primary), and there is **no `ec2:PrivateIpAddress` condition key** on `AssociateAddress`, so a policy cannot restrict *which* private IP a public address lands on. Combined with the cross-ENI/cross-account secondary-private-IP takeover in `using-instance-addressing`, this is the step that attaches *public* reachability to a hijacked/attacker-chosen secondary IP — turning an internal reassignment into internet-facing exposure.
*Mechanism:* `API_AssociateAddress.md` L50-52 ("primary **or secondary** private IP address to associate … If no private IP address is specified, [it] is associated with the primary"); list_ec2 L4714-4716 — no `ec2:PrivateIpAddress` key on any AssociateAddress row.
*Oracle:* on an ENI with a primary + a secondary private IP, with a principal scoped to `ec2:AssociateAddress` on the EIP (and whatever ENI grant), call `associate-address --allocation-id X --network-interface-id N --private-ip-address <secondary>`; confirm the EIP binds to the chosen secondary and that no Condition could have restricted the private-IP value. Then chain: does the secondary IP's current user lose/retain reachability? (Reassociation default-auto per overview-S1.)
*Preconditions/cost:* 1 account, 1 ENI with a secondary IP. Free.
*Severity:* **Medium–High** — on a shared-VPC / multi-workload ENI, selectively exposing or redirecting a specific private binding; High when chained with the cross-account secondary-IP takeover.

### N4 — BYOIP / Outpost pool-source selection is tag-only; address value unscopable (Lens S/U)
*Claim:* Choosing the allocation source (`--public-ipv4-pool <ipv4pool-ec2-…>` for BYOIP, customer-owned Outpost pool) and the specific address within it is governed only by `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region` (list_ec2 L4672) — no key for the pool CIDR or the requested IP — so the same "cannot scope the value" gap applies to bring-your-own ranges.
*Mechanism:* target page Allocate section (BYOIP / customer-owned bullets); list_ec2 L4672.
*Oracle:* confirm no `ec2:PublicIpAddress`/pool-CIDR Condition is evaluable on `AllocateAddress` for the `ipv4pool-ec2` row; defer **BYOIP pool ownership / within-pool squatting** to `ec2-byoip` + `byoip-working-with` (those plans own whether a BYOIP pool is single-account and thus NOT cross-account squattable).
*Severity:* **Low–Medium** (least-privilege gap; the cross-account dimension lives in the BYOIP siblings).

### N5 — Allocation-source confusion / console-vs-API default (Lens U, doc-completeness)
*Claim:* The page lists four allocation sources but does not state the API default or whether omitting a source silently falls back to the Amazon pool; a policy intending "BYOIP only" may be bypassable by simply omitting the pool selector (reverting to Amazon pool), which the tag-only scoping cannot prevent.
*Mechanism:* target page Allocate section (four sources, no stated precedence/default); N1/N4 (no pool-ID/IP key).
*Oracle:* call `allocate-address` with no source → confirm it draws from the Amazon pool regardless of any pool-scoped tag Condition (which only gates the pool resource, not the no-pool path).
*Severity:* **Low** (hardening / policy-evasion footgun).

---

## §5 — Null hypotheses (checked, pages named)

- **ec2:Ipv4IpamPoolId usable on AllocateAddress:** Refuted — L4671 lists it absent; key is defined (L10102) and used only on CreateVpc/CreateSubnet/CreatePublicIpv4Pool. (N1.)
- **ec2:PublicIpAddress usable on AllocateAddress:** Refuted — none of L4670-4672 carry it (consistent with overview L1). (N2/N4.)
- **ec2:PrivateIpAddress key on AssociateAddress:** Refuted — zero on all three rows L4714-4716; `--private-ip-address` is unscopable. (N3.)
- **This page introduces a new mutating transfer/release path:** N/A — the page covers only Allocate/Associate/Disassociate; transfer/release/reverse-DNS are on the overview page and owned there. Confirmed by reading the full target `.md` (3 topics only).
- **Lens B PassRole / confused-deputy on this page:** N/A — read the full Allocate/Associate/Disassociate page + `API_AssociateAddress`/`API_AllocateAddress`; no action accepts a role ARN or acts "on your behalf". (Consistent with overview H0-8.)
- **IPAM cross-account allocation ownership / RAM-consume governance:** Resolved (N2) — public-IPv4 IPAM pools ARE RAM-shareable to accounts/OUs/org; `AWSRAMDefaultPermissionsIpamPool` bundles allocate+release+view; consumer owns the resulting EIP; release recycles to the shared pool (minutes–48 h).
- **`--address <already-allocated>` behavior in a shared pool:** **doc-gap — not stated on any page** (the one place requiring live confirmation; see N2 oracle). The sequential/exact-address + shared-pool + no-per-address-key combination is otherwise fully documentation-confirmed.

---

## §6 — Priority & NEW/changed surface

1. **N2 (+N2a)** — IPAM shared-pool targeted/sequential land-grab + cross-account allocation oracle: the one genuinely new cross-account primitive this page exposes, **documentation-confirmed** (RAM-shareable, exact `--address`, sequential marketing, `GetIpamPoolAllocations` cross-account view, consumer-owns + recycle). Needs org + RAM-shared public-IPv4 IPAM pool + 2 consumer accounts. Only live-gap: `--address <already-allocated>` behavior.
2. **N3** — secondary-private-IP EIP binding: single-account testable; chains to the `using-instance-addressing` secondary-IP takeover for cross-account impact.
3. **N1** — IPAM-pool-ID unscopable on AllocateAddress: single-call policy-inertness confirmation; enables N2.
4. **N4 / N5** — BYOIP/Outpost source selection + no-source fallback: cheap least-privilege/evasion confirmations.

**NEW/notable surface flags:** the **IPAM-pool EIP consume path** (and its `--address` targeting) is the newest capability on this page and the least IAM-governed (tag-only, no pool-ID key, no IP-value key). The **cross-account** question for a RAM-shared pool (N2) is the highest-impact unknown and is not answered on this page — it is being resolved against the VPC-IPAM docset.

---

## §7 — Hunter preconditions & hard stops

- **Accounts:** 2 (org, with a RAM-shared public-IPv4 IPAM pool: 1 owner + 1–2 consumers) for N2; 1 for N1/N3/N4/N5.
- **Perms:** default `ec2:AllocateAddress/AssociateAddress/DisassociateAddress`, plus `ec2:GetIpamPoolAllocations`/`DescribeIpamPools` for the N2 oracle; a scoped test role holding *only* a tag/pool Condition to prove inertness (N1).
- **Canaries only:** throwaway EIPs/pools; for N2 target an address *you* placed as the "peer" canary — never a real third party's expected address; release every allocation to avoid leaving a squatter-exposed address.
- **Hard stop:** any AWS-fleet credential/identity/ARN, BGP/IPAM control-plane reach, or ability to affect another real tenant's live routing ⇒ stop, preserve evidence, flag for disclosure. **Confirm existence, never exploit beyond it** — for N2, allocating the one target address is the PoC.

## §8 — Online-vs-offline drift

Target page (`working-with-eips.md`) and `API_AssociateAddress.md` read online `.md` and compared to the offline mirror: **byte-identical** modulo cosmetic wrap. The `AllowReassociation` (param) vs `AllowReassignment` (example prose, `API_AssociateAddress.md` L84) inconsistency is present **identically in both copies** → upstream AWS authoring issue (already logged in overview-S1), not mirror drift. `list_ec2.md` read offline only (online truncates condition-key tables), per [[reference-aws-iam-service-auth-ref-url]].

---

*Procedural child/complement of `elastic-ip-addresses-eip-attack-research-plan.md`. OWNS: IPAM-pool targeted/sequential EIP allocation (N2), IPAM-pool-ID unscopability on AllocateAddress (N1), secondary-private-IP EIP binding (N3), BYOIP/Outpost source-selection scoping gap (N4), no-source fallback (N5). DEFERS to the overview plan: transfer hijack, released-EIP shared-Amazon-pool squatting, reverse-DNS, base forced-reassociation, read oracles, NetworkBorderGroup, 7-day/7-hour contradiction. Cross-refs: `using-instance-addressing` (secondary-IP takeover), `ec2-byoip`/`byoip-working-with` (BYOIP pool ownership), VPC-IPAM docset (RAM-share mechanics for N2).*
