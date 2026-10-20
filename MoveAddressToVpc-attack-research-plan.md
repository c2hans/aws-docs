# EC2 Elastic IP Address Lifecycle (`MoveAddressToVpc` & the EIP move/transfer/allocate family) — Attack Research Plan

**Source of leads:** target page `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_MoveAddressToVpc_section.html` and the surrounding EC2 Elastic-IP surface. Pages read (local mirror `/work/aws-docs/docs/…` cross-checked against live `docs.aws.amazon.com/*.md` and the machine-readable `servicereference.us-east-1.amazonaws.com/v1/ec2/ec2.json`, no sync gaps found):
API refs `API_MoveAddressToVpc`, `API_RestoreAddressToClassic`, `API_AllocateAddress`, `API_ReleaseAddress`, `API_AssociateAddress`, `API_DisassociateAddress`, `API_EnableAddressTransfer`, `API_AcceptAddressTransfer`, `API_DisableAddressTransfer`, `API_DescribeAddressTransfers`, `API_AddressTransfer`, `API_Address`, `API_ModifyAddressAttribute`, `API_ResetAddressAttribute`, `API_ProvisionByoipCidr`/`API_AdvertiseByoipCidr`/`API_WithdrawByoipCidr`/`API_DeprovisionByoipCidr`/`API_DescribeByoipCidrs`/`API_MoveByoipCidrToIpam`; user guide `transfer-EIPs-intro-ec2`, `using-instance-addressing-eips-releasing`, `elastic-ip-addresses-eip`, `working-with-eips`, `ec2-byoip`, `byoip-onboard`, `prepare-for-byoip`, `iam-policies-ec2-console`; IAM `service-authorization/.../list_ec2.md`.

**Status:** documentation-derived hypotheses only; nothing was tested against a live AWS account. The plan never claims a bug exists — it claims a boundary *might not hold* and says exactly how a hunter settles each one.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **DryRun is not an ownership oracle.** Every action here carries `DryRun`; `DryRunOperation` vs `UnauthorizedOperation` reflects *caller IAM only* and is evaluated *before* resource resolution. Never read it as proof of resource ownership — read the real (non-DryRun) business exception instead.
- **Two researcher-owned sandbox accounts + synthetic/non-production IPs settle every cross-account oracle here** without ever touching a third party's resource. Use canary data only.
- **HARD STOP:** the instant any evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. a carrier/Wavelength range that resolves to Amazon fleet infrastructure), stop, preserve evidence, flag for AWS-Security disclosure. No service-plane surface was found in the docs — this family is entirely customer↔customer / customer↔IAM-engine.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Cross-account EIP theft via the transfer handshake:** prove/refute that an account *other than* the designated `TransferAccountId` can call `AcceptAddressTransfer` for a pending transfer (accept side is keyed by the bare public IP, and no IAM key pins the accepting account).
2. **Dangling-EIP land-grab:** prove/refute that any account can re-allocate a victim's just-released Elastic IP (`AllocateAddress --address`) with no cooldown, no notification, and no prior-owner preference — inheriting DNS/allowlist/TLS/SMTP trust pointed at that IP.
3. **Legacy-twin authorization parity:** prove/refute that the deprecated `MoveAddressToVpc`/`RestoreAddressToClassic` (the only Write actions in the family with *no resource type*, `ec2:Region`-only, keyed by bare `PublicIp`) can be used as a free, un-scopeable cross-account EIP existence/ownership oracle.
4. **Transfer metadata disclosure to non-parties:** prove/refute that `DescribeAddressTransfers` (no resource-level IAM scoping) leaks a pending/accepted transfer's `publicIp`/`transferAccountId`/status to an account not party to it.
5. **Pool-ownership enforcement:** prove/refute that `AllocateAddress` binds `IpamPoolId`/`CustomerOwnedIpv4Pool` to a *validated share*, not mere pool existence.
6. **BYOIP blast radius:** prove/refute that advertise/withdraw of a BYOIP CIDR cannot be scoped to a specific CIDR (no resource type), letting one over-granted principal withdraw every BYOIP route in the account/region.
7. **AWS-authored sample-policy defect:** prove/refute that AWS's own EIP console sample IAM policy permits `AssociateAddress` onto an arbitrary network interface despite prose claiming it cannot.

---

## 2. Components, Assets, and Design

**Interface:** EC2 Query/JSON control-plane API, SigV4 IAM auth, region-scoped. No data plane for this family — every action is a control-plane mutation against a **shared regional IPv4-address inventory**. The target doc page is an SDK/CLI usage example (`aws ec2 move-address-to-vpc --public-ip <ip>`); the real surface is the Elastic-IP lifecycle it belongs to.

**Core resource — an Elastic IP — is nameable three ways, and that multiplicity is the crux of the family's authz questions:**
- **The dotted-quad public IP value** — *global and shared across all AWS accounts*; has **no owning-account field** once released (it re-enters the shared pool). Low-entropy, routable, scannable. It is the sole identifier accepted by `MoveAddressToVpc`, `RestoreAddressToClassic`, and `AcceptAddressTransfer`.
- **The `AllocationId`** (`eipalloc-…`) — account-scoped; the resource ARN is `arn:${Partition}:ec2:${Region}:${Account}:elastic-ip/${AllocationId}` (named by AllocationId only, **never by PublicIp**). Used by `Allocate`/`Release`/`Enable`/`Disable`-transfer, `Modify`/`Reset`-attribute.
- **The `AssociationId`** (once attached to an instance/ENI).

**Pools a caller can allocate from:** (1) Amazon's pool; (2) a BYOIP `PublicIpv4Pool` ("that you own"); (3) an `IpamPoolId` (IPAM pool, shareable cross-account via RAM+Organizations); (4) an Outposts `CustomerOwnedIpv4Pool` (CoIP).

**Platform migration (EC2-Classic → VPC):** `MoveAddressToVpc`/`RestoreAddressToClassic` move an EIP between the retired `standard` (EC2-Classic) platform and `vpc`. EC2-Classic was fully retired **August 2022**; the actions are marked "deprecated" but the IAM/control-plane layer **still recognizes and processes them** (confirmed in `ec2.json`, Oct 2026: both present, `IsWrite:true`, supported by Access-Analyzer policy generation and Action-Last-Accessed).

**Cross-account mutation points (the trust seams):**
- **EIP transfer** — a two-party, 7-day handshake: source `EnableAddressTransfer(AllocationId, TransferAccountId)` → recipient `AcceptAddressTransfer(Address, [TagSpecification])` → source `DisableAddressTransfer(AllocationId)`. **AWS does not notify the recipient** (out-of-band only). BYOIP/IPAM/CoIP EIPs cannot be transferred. Tags are reset on completion.
- **`MoveByoipCidrToIpam(IpamPoolId, IpamPoolOwner)`** — the one explicit cross-account param; scoped to the *destination* `ipam-pool`, not the source CIDR.
- **The shared IP pool** — a released EIP returns here with no account tag and no documented cooldown; whoever `AllocateAddress`es it first wins.

```
                 Amazon pool ─────────────────┐
 BYOIP CIDR (prov'd) ─ PublicIpv4Pool ─────────┤
 IPAM pool (x-acct via RAM) ─ IpamPoolId ──────┼─> AllocateAddress ─> Elastic IP (publicIp + eipalloc-id)
 Outposts CoIP ─ CustomerOwnedIpv4Pool ────────┘        │                        │
                                                        │              Associate/Disassociate (instance|ENI)
          [shared global IPv4 pool] <─ ReleaseAddress ──┘                        │
             ▲  no cooldown, no owner tag                         EnableAddressTransfer(allocId, acctB)
             │  (Objective 2 land-grab)                                           │  7-day pending, no recipient notify
    AllocateAddress --address X (any account races here)          AcceptAddressTransfer(publicIp)  ← keyed by IP, acct-pin = backend-only
                                                                                  │  (Objective 1 theft)
 EC2-Classic(standard) ⇄ VPC :  MoveAddressToVpc / RestoreAddressToClassic (publicIp-only, no resource type, Resource:"*")
```

---

## 3. Trust-Boundary Map
| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Account C (not the designated recipient) | A pending A→B EIP transfer | `AcceptAddressTransfer(Address=<A's EIP>)` from C | C's accept succeeds (or proceeds) → **cross-account theft of a live public IP**. Refuted iff C gets an account-mismatch/`Unauthorized`-class error. |
| Account C (non-party) | A→B transfer metadata | `DescribeAddressTransfers(AllocationId.N=<A's id>)` from C | Response leaks `publicIp`/`transferAccountId`/status → disclosure to a non-party. |
| Account B (any account) | A dotted-quad most recently owned by A | `AllocateAddress(Address=<A's former EIP>)` after A releases | B's allocate returns that exact IP before A reclaims → **shared pool has no prior-owner reservation**. |
| Account B | A BYOIP/IPAM/CoIP pool named by ID, not owned/shared to B | `AllocateAddress(IpamPoolId / CustomerOwnedIpv4Pool=<foreign>)` | 200 + an address drawn from a pool B was never shared. |
| Principal in A holding only `ec2:AdvertiseByoipCidr`/`WithdrawByoipCidr` | Every BYOIP CIDR in A/region | `WithdrawByoipCidr(Cidr=<any>)` | Succeeds against a CIDR outside the grantee's remit → **no resource-ARN exists to Deny/Allow by CIDR** (intra-account blast radius). |
| Any principal holding the two deprecated twins | Any public IPv4 (arbitrary account) | `MoveAddressToVpc(PublicIp=<any>)` real call | Error differs between nonexistent vs foreign-owned vs own IP → **cross-account existence/ownership oracle**, un-scopeable. |
| Holder of AWS's EIP-console sample policy | An arbitrary network interface | `AssociateAddress(... network-interface ...)` | Simulation returns `allowed` → AWS-authored artifact doesn't enforce its own prose restriction. |
| Any customer surface | AWS's own service plane | n/a | **Out of scope / HARD STOP** — not implicated anywhere in this family. |

---

## 4. API / Interface Inventory
| Action | Mutating | IAM resource type(s) | Key condition keys | Callable cross-acct? | Notes |
|---|---|---|---|---|---|
| **MoveAddressToVpc** (deprecated) | Write | **none (blank)** | `ec2:Region` **only** | n/a (`PublicIp` global) | `Resource:"*"`-only by construction; keyed by bare `PublicIp`; still IAM-processed. **Leads 3/4.** |
| **RestoreAddressToClassic** (deprecated) | Write | **none (blank)** | `ec2:Region` **only** | n/a | Twin of above. |
| AllocateAddress | Write | `elastic-ip*`,`ipam-pool`,`ipv4pool-ec2` | `aws:RequestTag`,`aws:TagKeys`,`ec2:Region`; pools: `ResourceTag` | — | **No `coip-pool` resource type.** No key binds the *value* of `Address`/pool params to caller ownership. **Leads 2/5.** |
| ReleaseAddress | Write | `elastic-ip` | `ec2:AllocationId`,`ec2:PublicIpAddress`,`ec2:Domain`,`ResourceTag`,`ec2:Region` | — | Well-scoped. `AuthFailure` if already allocated to another account = state oracle. |
| AssociateAddress | Write | `elastic-ip`/`instance`/`network-interface` | per-type (incl. `ec2:NetworkInterfaceID`,`ec2:Subnet`,`ec2:Vpc`) | — | Sample-policy defect — **Lead 7.** |
| DisassociateAddress | Write | `elastic-ip`/`network-interface` | same | — | Well-scoped. |
| **EnableAddressTransfer** | Write | `elastic-ip*` | `ec2:AllocationId`,`ec2:PublicIpAddress`,`ec2:Domain`,`ResourceTag`,`ec2:Region` | yes (names `TransferAccountId`) | **No condition key for the destination account.** **Leads 1/6.** |
| **AcceptAddressTransfer** | Write | `elastic-ip*` | `aws:RequestTag`,`aws:TagKeys`,`ec2:AllocationId`,`ec2:PublicIpAddress`,`ec2:Domain`,`ec2:Region` (no `ResourceTag`) | yes (recipient side) | Keyed by `Address`; no `ec2:TransferAccountId` key → acct-pin is backend-only. **Leads 3/8.** |
| DisableAddressTransfer | Write | `elastic-ip*` | as Enable | — | Revocation; race vs Accept undocumented. **Lead 2.** |
| **DescribeAddressTransfers** | List | **none** | `ec2:Region` only | callable w/ arbitrary `AllocationId.N` | No resource scoping; ownership filter (if any) is undocumented backend logic. **Lead 4.** |
| ModifyAddressAttribute / ResetAddressAttribute | Write | `elastic-ip*` | `ec2:Attribute`,`ec2:Attribute/${Name}`,+ full set | — | Well-scoped. |
| ProvisionByoipCidr / AdvertiseByoipCidr / WithdrawByoipCidr / DeprovisionByoipCidr / DescribeByoipCidrs | Write/List | **none** (no `byoip-cidr` type exists) | `ec2:Region` only | — | Cannot scope by CIDR. 10-sec global throttle. **Lead 9.** |
| MoveByoipCidrToIpam | Write | `ipam-pool*` (destination) | `ResourceTag`,`ec2:Region` | yes (`IpamPoolOwner`) | Scoped to dest pool, not source CIDR. **Lead 5.** |

---

## 5. Recommended Areas of Focus (ordered by severity-if-true × novelty)

### 5.1 Cross-account EIP theft via the transfer accept handshake — **PRIMARY (Lens A / CC / AA)** — Critical if true
**Background.** The transfer is a two-step handshake: source `EnableAddressTransfer(AllocationId, TransferAccountId)`; recipient `AcceptAddressTransfer(Address)`. The accept side is keyed **only by the public IP string** (`aws ec2 accept-address-transfer --address 100.21.184.216`). AWS *does not notify* the recipient — the source tells them out-of-band. The console "Multiple accounts" transfer type means more than one account may be a valid recipient of one enabled transfer.
**Security Concern.** `AcceptAddressTransfer`'s IAM condition-key set contains **no key that expresses "only the designated `TransferAccountId` may accept"** — there is no `ec2:TransferAccountId` key anywhere in the EC2 catalog. So the binding of *which account may accept* is **entirely backend business logic, with no IAM compensating control**, and the "secret" that gates acceptance is a low-entropy, routable, scannable public IP. If that backend check validates only "a pending transfer exists for this Address" rather than "…to *my* account," any account that learns the IP can accept a transfer meant for someone else.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* A third account C (not named `transferAccountId`) can accept an A→B transfer. **Oracle:** from C, `AcceptAddressTransfer(Address=<A's pending EIP>)`; success/partial-proceed = **Critical cross-account theft**; clean account-mismatch error = refuted.
- *Claim:* Re-`EnableAddressTransfer` on an already-`pending` AllocationId with a new `TransferAccountId=C` silently redirects the offer B still believes is valid. **Oracle:** enable A→B, then (no disable) enable A→C; observe reject vs silent-replace vs both-can-accept.
**Doc evidence:** `transfer-EIPs-intro-ec2.md` (accept uses `--address` only; "AWS does not notify transfer accounts…"); `API_AcceptAddressTransfer.md` (`Address` required, no AllocationId); `list_ec2.md` AcceptAddressTransfer condition keys (no account-pinning key).
**Preconditions / Cost:** 3 sandbox accounts, one in-flight transfer; reversible. **Severity-if-true:** **High–Critical** (interception/outage of a live public IP). **Stop condition:** refuted iff C's accept returns an account-mismatch/`Unauthorized`-class error.

### 5.2 Dangling-EIP land-grab after release — **PRIMARY (Lens EE / A)** — High–Critical if true
**Background.** `AllocateAddress`: *"After you release an Elastic IP address, it is released to the IP address pool and can be allocated to a different AWS account… To attempt to recover an Elastic IP address that you released, specify it in this operation."* `using-instance-addressing-eips-releasing.md`: *"You can't recover an Elastic IP address if it has been allocated to another AWS account."* **No grace period, reservation window, or prior-owner preference is documented anywhere** — "recover" is just ordinary first-come allocation against the same shared pool.
**Security Concern.** Textbook dangling-IP takeover precondition: the moment account A releases (voluntarily, or forced by EIP-quota pressure, instance teardown, or NAT-GW/ALB managed-EIP release) an IP still referenced by DNS records, allowlists, SPF/webhook config, or hardcoded clients, any other account can `AllocateAddress --address <ip>` and inherit all inbound trust — with zero notification to A and zero enforced delay.
**High-level Test Scenarios:**
- *Claim:* No cooldown/reservation protects a just-released IP. **Oracle:** release from A; immediately `AllocateAddress --address <ip>` from B; it succeeds → confirmed. (Also test whether A gets any same-account precedence window.)
- *Claim:* `AllocateAddress --address X` polling is a cheap race-window probe for a suspected release. **Oracle:** repeated allocate attempts transition from NotFound/unavailable → success at the release instant.
**Doc evidence:** `API_AllocateAddress.md` L8,L18; `API_ReleaseAddress.md` L14,L16; `using-instance-addressing-eips-releasing.md` L45-47.
**Preconditions / Cost:** victim release of a still-referenced IP; attacker needs only ordinary `ec2:AllocateAddress` in its own account; trivial cost. **Severity-if-true:** **High–Critical** cross-account (TLS-termination hijack, SMTP/SPF relay abuse, OAuth-redirect/allowlist bypass, inherited reverse-DNS/reputation). **Stop condition:** if the IP resolves into an AWS fleet/carrier range → HARD STOP + disclose; otherwise confirm with two sandbox accounts + synthetic IPs.

### 5.3 `DescribeAddressTransfers` / deprecated-twin enumeration oracles — **Lens A (oracle) / X** — Medium–High
**Background.** `DescribeAddressTransfers` has **no resource-level IAM scoping** (`ec2:Region` only) yet accepts an arbitrary `AllocationId.N` array. `MoveAddressToVpc`/`RestoreAddressToClassic` have **no resource type at all** (confirmed in `list_ec2.md` *and* `ec2.json`), are keyed by bare `PublicIp`, and can never succeed post-EC2-Classic-retirement — so their only remaining observable is the error they return.
**Security Concern.** Any non-party can call `DescribeAddressTransfers` with guessed/known allocation ids; if the server returns transfer metadata (publicIp, destination account, status) for transfers it is not a party to, that is disclosure feeding the 5.1 race. Separately, the deprecated twins are an un-scopeable (Lead 1: `Resource:"*"`-only) cross-account EIP existence/ownership oracle if their business exception differs for nonexistent vs foreign-owned vs own IPs.
**High-level Test Scenarios:**
- *Claim:* `DescribeAddressTransfers` from a non-party account leaks a pending transfer's metadata. **Oracle:** call from account C with A's `AllocationId`; non-empty result with `transferAccountId`/`publicIp` = confirmed; uniform empty/`NotFound` = refuted.
- *Claim:* `MoveAddressToVpc` error differential enumerates IP ownership across accounts. **Oracle:** three *real* (non-DryRun) calls — nonexistent IP / foreign-owned EIP / own EIP — record exact codes; distinguishable (a)-vs-(b) = confirmed. (DryRun explicitly *not* the oracle.)
**Doc evidence:** `list_ec2.md` DescribeAddressTransfers (blank resource type, `ec2:Region` only) + MoveAddressToVpc/RestoreAddressToClassic blocks; `ec2.json` (no `Resources` key for the twins); `API_MoveAddressToVpc.md` (prose-only preconditions, no documented ownership-check ordering).
**Severity-if-true:** Medium–High (transfer metadata disclosure) / Low–Medium (pure IP-ownership enumeration; capped because no state change is possible). **Stop condition:** refuted iff responses are uniform/`NotFound` regardless of id validity.

### 5.4 Destination-account guardrail gap + no IAM key for `TransferAccountId` — **Lens B/AA/U** — Medium
**Background & Concern.** `EnableAddressTransfer` targets *any* 12-digit account in-region with **no recipient consent gate** and **no IAM/SCP condition key to restrict the destination** (grep of `list_ec2.md` for `TransferAccountId` = zero hits). A role granted `ec2:EnableAddressTransfer` for "transfer within my org" can transfer to *any* account; an unsolicited-offer/griefing primitive, and the enabler for 5.1. Also test **Disable-vs-Accept race** (does `DisableAddressTransfer` atomically preclude an in-flight accept, or can both land → double-ownership / silent loss-of-control?) — the `addressTransferStatus` enum (`pending|disabled|accepted`) implies mutual exclusion the docs never guarantee under concurrency.
**Oracle:** author an SCP/IAM policy attempting to bound `TransferAccountId` (no key exists → provable statically); race `Disable` (A) against `Accept` (B) on one pending transfer and classify (both succeed / clean mutex error / accept silently wins). **Doc evidence:** `transfer-EIPs-intro-ec2.md`; `list_ec2.md`; `API_AddressTransfer.md` enum. **Severity:** Medium (guardrail gap); **High** if the race yields double-ownership or silent loss-of-control.

### 5.5 Pool-ownership binding on `AllocateAddress` / `MoveByoipCidrToIpam` — **Lens A/EE/AA** — Critical if non-shared pool is drainable
**Background.** `PublicIpv4Pool` says "that you own"; **`IpamPoolId` and `CustomerOwnedIpv4Pool` carry no ownership qualifier**, and `AllocateAddress` has **no `coip-pool` resource type** in IAM at all. IPAM pools are *intended* to be shared cross-account via RAM+Organizations. **Concern:** does `AllocateAddress` validate that access to a foreign `IpamPoolId` flows through an *active* share, or merely that the pool exists/has capacity (land-grab)? For CoIP, is EC2 IAM even in the enforcement path, or only the Outposts layer? For `MoveByoipCidrToIpam`, is the share granular to "this CIDR may move here," or is any org-shared pool sufficient regardless of CIDR?
**Oracle:** from a non-recipient sandbox account, `AllocateAddress --ipam-pool-id <foreign>` / `--public-ipv4-pool <foreign>` → immediate access-denied/not-found (safe) vs resolves (land-grab); test the **revocation-completeness** variant (pool previously shared, later unshared — still allocatable?); diff error shape for foreign-unshared vs nonexistent pool id (existence oracle). **Doc evidence:** `API_AllocateAddress.md` L32-35/L48-51/L59-62; `list_ec2.md` AllocateAddress row (no coip-pool); `ec2-byoip.md` (RAM+Orgs requirement); `API_MoveByoipCidrToIpam.md` (`IpamPoolOwner`). **Severity:** Critical (drain non-shared reputable space) / Medium (post-revocation only). **Preconditions:** multi-account IPAM / Outposts sandbox — otherwise a flagged **doc-gap** (Section 8).

### 5.6 BYOIP advertise/withdraw has zero per-CIDR IAM scoping — **Lens S** — Medium–High (intra-account blast radius)
**Background.** `AdvertiseByoipCidr`/`WithdrawByoipCidr`/`ProvisionByoipCidr`/`DeprovisionByoipCidr`/`DescribeByoipCidrs` each have **no resource type** (`ec2:Region` only); no `byoip-cidr` type exists. Any principal needing to advertise/withdraw *one* CIDR must be granted it for **every** BYOIP CIDR in the account/region. Combined with the documented 10-sec global advertise/withdraw throttle, one over-granted/compromised principal can serially withdraw every BYOIP route (route-withdrawal DoS) with no IAM way to limit blast radius.
**Oracle:** `iam:SimulatePrincipalPolicy` proves no per-CIDR Deny is expressible (static, zero resources); in a multi-CIDR account confirm a `ec2:Region`-scoped principal can withdraw an unrelated CIDR. **Also (Lens AA/U):** BYOIP ownership (X.509+ROA) is validated **only once at Provision**; nothing re-validates at advertise/withdraw — a point-in-time-vs-continuous trust gap (RIR/BGP-plane adjacent; treat as informational unless AWS's internal re-validation cadence is shown absent). **Doc evidence:** `list_ec2.md` BYOIP rows; `API_AdvertiseByoipCidr.md` L10; `prepare-for-byoip.md`; `byoip-onboard.md` L104. **Severity:** Medium–High least-privilege/blast-radius gap. Note: **not** routed to Lens R — no AWS sample IAM policy for BYOIP admin was found in the pages read, so this is a landscape gap, not an AWS-authored artifact defect.

### 5.7 AWS-authored EIP console sample policy vs its own prose — **Lens R / U (in scope, AWS-owned)** — Medium
**Background & Concern.** `iam-policies-ec2-console.md` prints a copy-verbatim sample granting `ec2:AllocateAddress`/`ec2:AssociateAddress` with `"Resource":"*"` and **no Condition**, immediately under prose claiming "Users cannot associate Elastic IP addresses with network interfaces…". `AssociateAddress` is one action with three conditionable resource types (`elastic-ip`/`instance`/`network-interface`); with `Resource:"*"` and no Deny, the **network-interface variant is not blocked** — the "restriction" is a console-UI omission, not an IAM boundary. Per the skill's carve-out, a weak default in an **AWS-authored, copy-verbatim** artifact is in scope and reportable (Tier 2, route `aws-security`), not a customer footgun.
**Oracle:** `iam:SimulatePrincipalPolicy` for `ec2:AssociateAddress` against an arbitrary `network-interface` ARN under a principal holding *exactly* the printed policy → `allowed` confirms; `implicitDeny` refutes. Escalate to a live scoped call with a canary ENI only if confirmed. **Doc evidence:** `iam-policies-ec2-console.md` (`ex-eip` JSON) vs `list_ec2.md` AssociateAddress (network-interface type with `ec2:NetworkInterfaceID`/`ec2:Subnet`/`ec2:Vpc`). **Severity:** Medium — lets an "instance-only EIP" role re-point a public EIP onto any ENI (traffic hijack/outage) for anyone who copied the sample trusting the console restriction was IAM-enforced.

### 5.8 Supporting / lower-priority leads
- **Tag-provenance / ABAC spoof (Lens I/U, Medium):** tags are reset on transfer and freely re-set by the recipient via `AcceptAddressTransfer` `TagSpecification.N`; a customer who builds ABAC on EIP tags per AWS's own "vetted for security compliance" use case can be spoofed (`tags are not provenance`). `aws:RequestTag`/`aws:TagKeys` *are* enforced on accept.
- **`ec2:Domain` enum case-sensitivity fail-open (Lens S, Medium):** `list_ec2.md` documents `ec2:Domain` as `String` with no enum/case guidance; runtime is lowercase `vpc|standard` (`API_Address.md`). A Deny written `"Standard"`/`"VPC"` is silently inert. **Oracle:** `iam:SimulateCustomPolicy` Deny on `"Standard"` vs a `vpc` resource.
- **NetworkBorderGroup "cannot move between groups" (Lens U, Info):** no `ec2:NetworkBorderGroup` condition key exists — enforced by API orchestration only, not IAM (completeness note, not a cross-tenant primitive).
- **Partial-`pending` TOCTOU (Lens AA, Low):** `EnableAddressTransfer` does no association pre-check (`InvalidTransfer.AddressAssociated` is deferred to accept); confirm source retains full associate/disassociate control during `pending` with no silent lock.
- **Doc self-contradiction (Lens U, Informational):** `API_AddressTransfer.md` says the recipient has **"seven hours"** to allocate; `transfer-EIPs-intro-ec2.md` and `API_DescribeAddressTransfers.md` say **"seven days"** (both confirmed on the live site). Security-relevant (bounds the 5.1/5.3 exposure window) — file to AWS docs owners.

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Non-recipient accepts a pending transfer | AcceptAddressTransfer (`Address`) | Backend-only account-pinning; **no IAM key** — attack whether the backend checks "to *my* account". |
| Dangling-IP takeover of a released EIP | AllocateAddress (`Address`) | **None** — first successful allocate wins; attack the absence of cooldown/reservation. |
| Transfer-metadata disclosure to a non-party | DescribeAddressTransfers | No resource-level IAM; undocumented backend ownership filter — attack by querying a foreign AllocationId. |
| Cross-account ownership oracle via legacy twin | MoveAddressToVpc / RestoreAddressToClassic | None (Resource:"*"-only, PublicIp-keyed) — attack the error differential (real call, not DryRun). |
| Allocate from a foreign/unshared pool | AllocateAddress (pool params) | Implicit account-scoped ARN + RAM/Orgs share (IPAM) — attack whether share-state vs mere existence is checked. |
| Withdraw a BYOIP CIDR outside remit | AdvertiseByoipCidr/WithdrawByoipCidr | **None** — no resource type/condition key; prove the gap statically via `SimulatePrincipalPolicy`. |
| Re-point public EIP onto arbitrary ENI under the sample policy | AssociateAddress | AWS console sample policy (`Resource:"*"`, no Condition) — attack via simulation; AWS-owned artifact. |
| Disable-vs-Accept race → double-ownership | Disable/AcceptAddressTransfer | `addressTransferStatus` enum implies exclusivity — attack the concurrency guarantee. |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **AWS's own service plane / fleet identity, and the account-provisioning/billing backend** that tracks which 12-digit ids are valid accounts — shared-responsibility line, HARD STOP on any hit.
- **RIR/BGP-plane mechanics** (ROA validity, RPKI relying-party behavior, real-world netblock transfer) — AWS-external, not an AWS API/IAM boundary.
- **Single-account self-DoS** (e.g. exhausting one's own 5-EIP/region quota) — out of scope per severity framing.
- **Customer-authored IAM policies** that over-grant BYOIP advertise/withdraw — a customer footgun, *except* 5.7 (the AWS-authored sample policy), which is in scope.
- **Cross-region transfer** — documented impossible; took AWS's statement as given (a hunter may spot-check but it is not prioritized).
- **Carrier/Wavelength allocation mechanics** — noted in docs, not analyzed; needs its own pass if in scope.
- **DryRun as an ownership signal** — explicitly a false-positive trap, not a lead.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked that did NOT fire — pages named per discipline)
- **Lens B/C — PassRole / confused-deputy / credential vending — NULL.** No action in the family accepts a role ARN; no address action pairs with `iam:PassRole`/`iam:PassedToService` (contrast `RequestSpotInstances`, which does). Checked: all 14 API Request-Parameters sections + their `list_ec2.md` blocks.
- **Lens G — SSRF — NULL.** No URL/URI/webhook/callback/logo-shaped field anywhere (params are IPs, allocation ids, account ids, CIDRs, pool ids — none dereferenced server-side). Checked: all API pages in scope.
- **Lens F — injection/translation — NULL.** Structured Query/JSON params only; no parser/translator reachable by a customer (the only parse is `CidrAuthorizationContext`'s signed X.509 message = RIR validation, out of scope).
- **Lens Q — upload — NULL.** No blob/attachment/image parameter.
- **Lens H — CMK/encryption-context — NULL.** EIPs are not an encrypted resource type; no `kms:*` key in the elastic-ip condition-key set.
- **Lens K — prompt injection — NULL.** No LLM/agent surface.
- **Lens W — attestation-conditioned auth — NULL.** No `kms:RecipientAttestation`/PCR keys near elastic-ip.
- **Lens FF — JWT/OIDC/Cognito — NULL.** SigV4 IAM is the sole documented auth mechanism.
- **Lens D/V — data-plane→control-plane / network segmentation — NULL.** No ENI/control-VPC/host component; pure control-plane account↔account.
- **Lens BB/CC/DD — canonicalization / trusted-header / cache-key — NULL for the direct EC2 Query API** (single-hop, no documented authorizer/CDN/cache in front). *Not* re-checked against the EC2 **console** stack, which sits behind more layers — a follow-up surface if console endpoints come into scope.
- **Lens O — audit-log evasion — DOC-GAP.** None of the transfer pages mention CloudTrail behavior for these actions; standard EC2 coverage likely applies but is unconfirmed here. Note also: `transfer-EIPs-intro-ec2.md` states IPAM audit history is *lost* when an EIP is transferred outside the organization — a documented audit-trail gap worth a hunter's attention. Needs the CloudTrail EC2 event reference (not in this pass).
- **Lens Y — transport/TLS/SigV4 — DOC-GAP.** Neither `aws:SecureTransport` nor `aws:SignatureVersion` appears anywhere in the EC2 service-authorization reference (not just this family); the doc is silent on TLS-floor/SigV2 enforcement — cannot be resolved from documentation alone.
- **Lens L — rate/pool exhaustion — DOC-GAP.** No documented per-account/global rate limit for `AllocateAddress`/`ReleaseAddress` (only the 5-EIP/region quota, a capacity not a rate limit); BYOIP advertise/withdraw has a 10-sec throttle (captured in 5.6). Throttling may exist undocumented at the service-limits layer.
- **Pool-ownership enforcement (5.5) & BYOIP ROA re-validation cadence (5.6) — DOC-GAP, not NULL:** documentation establishes the *absence of an explicit IAM ownership condition key* but cannot establish whether the API's own resource-resolution/backend logic closes the gap — flagged for a reviewer with a multi-account IPAM/Outposts sandbox.

---
*Deliverable prepared by the security-questionbuilder method (boundary-first question engine). All leads are documentation-derived falsifiable hypotheses; a hunter executes the oracles against an authorized test account, uses synthetic canary data, and HARD-STOPS on any AWS service-plane evidence.*
