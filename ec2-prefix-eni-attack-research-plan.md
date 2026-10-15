# EC2 Prefix Delegation for Network Interfaces — Attack Research Plan

Source of leads: `ec2-prefix-eni.html` (overview) + its procedural child `work-with-prefixes.html` (`.md` twins in `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`), cross-checked against the IAM Service Authorization Reference `docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines, read by targeted offline grep). Status: **documentation-derived hypotheses only; nothing tested against a live account.** Online/offline verified byte-consistent 2026-10-15 (overview page via WebFetch; `list_ec2` rows read directly).

This is a **page-level deep-dive child of the [`ec2-networking` hub plan](ec2-networking-attack-research-plan.md)** covering the **prefix-delegation** feature specifically. It is a sibling of the IP-addressing cluster plans and **deliberately does NOT restate** mechanisms those siblings own — it cross-references them and owns only the net-new prefix surface. See **§7 / §8** for the exact deferral map.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The three primary leads here are **Lens S/U (IAM-unscopability)**, **Lens P/A/EE (the manual-prefix "already-assigned" verification gate across tenants)**, and **Lens L (16×-amplified subnet exhaustion)**. None is a classic cross-tenant data IDOR; this feature's value is control-plane scoping gaps + a shared-subnet address-namespace boundary.
- The two highest-value questions are **doc-gaps that `iam:SimulateCustomPolicy` / `DescribeNetworkInterfaces` can only partly settle** — the overlap-check scope and the AllowReassignment-on-prefix behavior **need a 2-account shared-VPC canary**. `DryRunOperation` is caller-IAM-only (evaluated before resource resolution) → **NOT an ownership/overlap oracle** (false-positive trap).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. a requester-managed / `Managed=true` ENI), stop, preserve evidence, flag for AWS-Security disclosure. Never exploit a confirmed cross-tenant primitive beyond existence — one prefix proves it.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Claim a prefix (/28 IPv4 or /80 IPv6) that overlaps IP space in use by another account** sharing the same VPC subnet (RAM-shared) — i.e. defeat the documented "AWS verifies that it is not already assigned to other resources before assigning it" check across the tenant boundary.
2. **Force-move a prefix off another ENI** (own-account cross-team, or cross-account via a shared subnet) using the assign-prefix path, mirroring the `AssignPrivateIpAddresses … AllowReassignment` secondary-IP takeover.
3. **Exhaust a shared subnet's address space** using the prefix-count knob at 16× the per-ENI-limit accounting rate, denying launches to co-tenants.
4. **Demonstrate that no IAM policy can forbid prefix delegation, cap prefix count, or pin/forbid a specific prefix CIDR** on any of the five prefix-capable actions (control-plane guardrail gap).
5. **Pre-empt / squat a subnet CIDR reservation of type `prefix`** so that another principal's *automatic* prefix assignment is steered into or blocked by an attacker-chosen range.

---

## 2. Components, Assets, and Design

**Feature.** Prefix delegation assigns a *block* of private IPv4 (`/28` = 16 addresses) or IPv6 (`/80`) addresses to an ENI in one operation, instead of individual secondary IPs. Primary use: container density (one prefix per instance → many pod IPs without per-IP API calls). **Nitro-based instances only.**

**Two assignment modes (overview page, verbatim):**
- **Automatic** — "AWS chooses the prefix and assigns it to your network interface. If the subnet for the network interface has a subnet CIDR reservation of type `prefix`, we select the prefixes from the subnet CIDR reservation. Otherwise, we select them from the subnet CIDR range."
- **Manual** — "You specify the prefix and AWS verifies that it is not already assigned to other resources before assigning it to your network interface." ← **the enforcement gate this plan centers on.**

**Resource / identifier shapes.**
- ENI id `eni-<17 hex>` (non-fabricable, ~68-bit → blind cross-account IDOR is a partial-null; residual = *known/shared-subnet* ENIs).
- IPv4 prefix must be a `/28` **within the subnet CIDR, not overlapping other prefixes or IPs of existing resources in the subnet**; IPv6 prefix `/80`.
- Subnet CIDR reservation `scr-<hex>` (resource type `subnet-cidr-reservation`), type `prefix` or `explicit`.
- A prefix counts as **1 IP** toward the per-ENI maximum (e.g. `c5.large` = 10 IPv4/ENI → up to 9 prefixes = 144 real IPv4) — see [`AvailableIpPerENI`](AvailableIpPerENI-attack-research-plan.md).
- An **EIP can be associated to the whole-prefix IP or to the IP-address part of a prefix** (overview: "You can also assign an Elastic IP address to the IP address part of the assigned prefix") → chains the prefix path into the EIP-association surface.
- "Prefixes are **included in source/destination checks**."

**API / interface surface (five prefix-capable actions).**

| Action | Mode | Prefix params (CLI) | IAM resource row | Prefix condition key? |
|---|---|---|---|---|
| `CreateNetworkInterface` | create-time | `--ipv4-prefix-count` / `--ipv4-prefixes` / `--ipv6-prefix-count` / `--ipv6-prefixes` | `network-interface*`, `security-group`, `subnet*` | **none** |
| `AssignPrivateIpAddresses` | existing ENI (IPv4) | `--ipv4-prefix-count` / `--ipv4-prefixes` (+ `--allow-reassignment`) | `network-interface*` only | **none** |
| `AssignIpv6Addresses` | existing ENI (IPv6) | `--ipv6-prefix-count` / `--ipv6-prefixes` | `network-interface*` only | **none** |
| `UnassignPrivateIpAddresses` | remove (IPv4) | `--ipv4-prefixes` | `network-interface*` only | **none** |
| `UnassignIpv6Addresses` | remove (IPv6) | `--ipv6-prefix` | `network-interface*` only | **none** |
| *(supporting)* `CreateSubnetCidrReservation` | auto-assign source | `--reservation-type prefix --cidr <block>` | `subnet*` | tag/AZ/Region/SubnetID/Vpc only — **no type/CIDR key** |

```
                 subnet CIDR range  ──┐
                                      ├─(auto)──► AWS picks prefix ─┐
  subnet-cidr-reservation(type=prefix)┘                            │
                                                                   ▼
  caller ──(manual: --ipv4-prefixes 10.0.0.208/28)──► [overlap-verify gate] ──► ENI gets /28 block
                                                        (scope = ? per-acct / whole-subnet)
  shared VPC: owner-subnet + participant ENIs all draw from the SAME subnet address namespace
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Participant account (RAM-shared subnet) | Owner's / co-tenant's in-use IP space | manual `--ipv4-prefixes <overlapping /28>` | AWS **assigns** an overlapping/adjacent prefix, or returns an error that **leaks** which IPs are in use (existence oracle) |
| Caller / cross-team principal | Another ENI's prefix | `AssignPrivateIpAddresses --ipv4-prefixes … --allow-reassignment` | the prefix (and any EIP on it) **moves** to the caller's target ENI without the losing owner's consent |
| Any principal with prefix action | Shared subnet address pool | `--ipv4-prefix-count N` (uncapped by IAM) | subnet address exhaustion visible to co-tenants (launch failures) |
| Admin writing an identity policy | The prefix feature | (absence of) `ec2:Ipv4Prefix`/`Ipv6Prefix`/count keys | `SimulateCustomPolicy` shows a Deny on those keys is **silently inert**; prefix request still allowed |
| Caller | Other principal's *automatic* prefix selection | `CreateSubnetCidrReservation --reservation-type prefix` | attacker's reservation steers/blocks a victim's auto-assigned prefixes |
| Any customer surface | AWS service plane | — | **hard stop** on any requester-managed/`Managed=true` ENI |

---

## 4. Boundary-lens catalog — firing lenses

### Area 1 — HEADLINE (Lens S/U, AWS-owned Tier-2 reportable): the entire prefix-delegation feature is IAM-unscopable
**Background.** All five prefix-capable actions take prefix selectors (`Ipv4Prefix`/`Ipv4PrefixCount`/`Ipv6Prefix`/`Ipv6PrefixCount`) that choose *how many* and *which* address blocks land on an ENI.

**Security Concern.** Whole-corpus grep of `list_ec2.md` (10,190 lines) returns **ZERO hits** for `ec2:Ipv4Prefix`, `ec2:Ipv6Prefix`, `ec2:Ipv4PrefixCount`, `ec2:Ipv6PrefixCount`, or any `*Prefix*` / `PrefixCount` condition key (confirms the [`create-network-interface`](create-network-interface-attack-research-plan.md) Area-3 grep). The two mutating existing-ENI actions carry **only** `network-interface*` with the generic 8-key set `{aws:ResourceTag, ec2:AvailabilityZone, ec2:ManagedResourceOperator, ec2:NetworkInterfaceID, ec2:Region, ec2:ResourceTag, ec2:Subnet, ec2:Vpc}`. `CreateNetworkInterface` adds `security-group`/`subnet*` rows but still no prefix key. ⇒ an admin **cannot** write a policy that (a) forbids prefix delegation, (b) caps the number of prefixes (the 16×-exhaustion amplifier of Area 3), or (c) pins/forbids a specific prefix CIDR. This is the confirmed `ec2:InterfaceType`-is-not-a-real-key failure shape (Variant-coverage Lens-S item (a)) applied to prefixes. Because `CreateNetworkInterface` / `AssignPrivateIpAddresses` run under the **caller's own identity** (no Fleet SLR here), the gap is a *static action-row* fact, not SLR-non-propagation.

**High-level Test Scenarios.**
- Claim: *A policy that `Deny`s `ec2:AssignPrivateIpAddresses` when a hypothetical `ec2:Ipv4PrefixCount > 1` has no effect.* Oracle: `iam:SimulateCustomPolicy` with a context entry for that key — the simulate shows the key **unrecognized / not evaluated**, action still `allowed`. No resource created.
- Claim: *No policy can restrict a tenant to a specific prefix CIDR range.* Oracle: same, with `ec2:Ipv4Prefix` context — inert.
- The ONLY live levers confirmed: ENI identity (`ec2:NetworkInterfaceID`/tag), subnet/VPC (`ec2:Subnet`/`ec2:Vpc`), AZ, Region. Count and CIDR value are ungoverned.

**Doc evidence.** `list_ec2.md` AssignPrivateIpAddresses rows (≈4700–4704), AssignIpv6Addresses (≈4694–4698), CreateNetworkInterface (5357–5362). **Severity-if-true:** Low–Medium as a pure scoping gap, but it is the **enabler** that raises Areas 2–3 (there is no policy backstop to the exhaustion/takeover primitives). Reportable as an AWS-owned control-expressibility gap.

---

### Area 2 — Prefix force-move via AllowReassignment (Lens A/X/S/U) — cross-ENI / shared-subnet cross-account takeover
**Background.** The existing-ENI IPv4 path is `AssignPrivateIpAddresses`, the same action whose secondary-IP `AllowReassignment=true` the [`using-instance-addressing`](using-instance-addressing-attack-research-plan.md) Area 1 proved is a **cross-ENI / RAM-shared-subnet cross-account takeover** with no documented source-ENI/owner consent check (the gaining caller sets `AllowReassignment`, not the losing owner).

**Security Concern.** Does `AllowReassignment` extend to **prefixes**? If `--ipv4-prefixes <P>` names a `/28` already assigned to ENI-A (another ENI, possibly another account's ENI in a shared subnet) and the caller sets `--allow-reassignment`, does AWS **move the whole /28** to the caller's ENI-B? The overview states an EIP can ride on a prefix IP, so a prefix force-move may **also relocate any EIP** on that prefix (the "any Elastic IP associated with the IP is also moved" amplifier the sibling documented for single IPs). IAM gives no `AllowReassignment` condition key (0 hits, confirmed) and no prefix-value key, so this cannot be fenced. **API-ref confirmed (2026-10-15):** `AssignPrivateIpAddresses` accepts `AllowReassignment` *and* `Ipv4Prefix.N`/`Ipv4PrefixCount` **in the same call**, but the `AllowReassignment` parameter description reads only *"Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned…"* — it says **"IP address," never "prefix."** So the flag's effect on a prefix already assigned elsewhere is **undocumented, not denied** — the two params coexist but the semantics are silent. This is the live question, not whether the knob exists. **[OPEN — needs 2-account canary; see §8 doc-gap D1.]**

**High-level Test Scenarios.**
- Claim: *`AssignPrivateIpAddresses --ipv4-prefixes <P-on-foreign-ENI> --allow-reassignment` moves P to my ENI across a shared-subnet account boundary.* Oracle: `DescribeNetworkInterfaces` on the victim ENI shows P gone, caller's ENI shows P present; victim loses the block (and any EIP). Prove existence on a self-owned canary pair first, then one cross-account canary move, then **STOP**.
- Refute path: if the API rejects prefix reassignment, or requires the prefix be unassigned first (the safer IPv6-style behavior), Area 2 collapses to the IPv6 shape (Area 2b).

**Area 2b (IPv6, confirmed safer).** `AssignIpv6Addresses` has **no `AllowReassignment`-equivalent parameter at all** (full param list = `Ipv6AddressCount`, `Ipv6Addresses.N`, `Ipv6Prefix.N`, `Ipv6PrefixCount`, `NetworkInterfaceId`; API-ref confirmed 2026-10-15), matching the sibling's IPv6 "must unassign first" finding. ⇒ an IPv6-prefix takeover needs `UnassignIpv6Addresses` authz on the **victim** ENI first, not just assign on the attacker ENI. Do not over-claim Area 2 onto IPv6.

**Doc evidence.** overview "assign an Elastic IP address to the IP address part of the assigned prefix"; `work-with-prefixes.md` assign-to-existing uses `assign-private-ip-addresses`; sibling `using-instance-addressing` Area 1/2. **Severity-if-true:** cross-account prefix+EIP relocation on a shared subnet = **High**; intra-account cross-team = Medium–High.

---

### Area 3 — 16×-amplified shared-subnet address exhaustion (Lens L) — cross-tenant DoS
**Background.** Each prefix counts as **one** IP toward the per-ENI limit but a `/28` is **16 real IPv4 addresses** drawn from the subnet. `--ipv4-prefix-count` is uncapped by IAM (Area 1).

**Security Concern.** In a RAM-shared subnet, co-tenants share one address namespace. A participant assigning the maximum prefixes per ENI across several ENIs/instances consumes subnet addresses at up to **16× the rate** the per-ENI accounting suggests, and no IAM key caps it → **cross-tenant subnet exhaustion** (co-tenant launches / auto-assign fail). This deepens the amplifier flagged by [`AvailableIpPerENI`](AvailableIpPerENI-attack-research-plan.md) (which owns the per-ENI maxima) and [`create-network-interface`](create-network-interface-attack-research-plan.md) Area 3 (which owns create-time `Ipv4PrefixCount`); **this plan owns the assign-to-existing + the cross-tenant-DoS framing of the knob.**

**High-level Test Scenarios.**
- Claim: *One participant can drain a shared /24 subnet's free addresses via prefix-count, denying co-tenant launches.* Oracle: assign prefixes until `DescribeSubnets AvailableIpAddressCount` → low / co-tenant `RunInstances`/auto-assign returns `InsufficientFreeAddressesInSubnet`. Use a self-owned 2-account canary subnet; measure, do not weaponize.
- Adjacent: does automatic assignment from the **subnet CIDR range** (no reservation) compete with the owner's reservations → silent starvation?

**Doc evidence.** overview Considerations ("Each prefix … counts as one IP address", `/28`); `AvailableIpPerENI.md`. **Severity-if-true:** cross-tenant DoS on a shared subnet = **High**; single-account self-DoS = Low/out-of-scope.

---

### Area 4 — The manual-prefix "already-assigned" verification gate across the tenant boundary (Lens P/A/EE/U) — HIGHEST-VALUE OPEN LEAD
**Background.** Manual assignment, verbatim: *"You specify the prefix and AWS verifies that it is not already assigned to other resources before assigning it to your network interface."* Requirement: *"The prefix is in the subnet CIDR of the network interface, and does not overlap with other prefixes or IP addresses assigned to existing resources in the subnet."* This is a **uniqueness/overlap gate** (Lens P) over a **shared address namespace** (Lens A).

**Important wording nuance (API-ref re-read 2026-10-15).** The requirement is phrased *"does not overlap with other prefixes or IP addresses assigned to existing resources **in the subnet**"* — i.e. **subnet-scoped on its face, not account-scoped.** The docs never use the words "account," "tenant," or "shared VPC" here, so the plain reading actually **favors whole-subnet enforcement across all tenants** — which would make Area 4a (account-scoped bypass) *refute* and promote **Area 4b (the enumeration oracle)** as the more likely live outcome: if the check sees all tenants' IPs, an overlap rejection is itself a cross-tenant usage probe. But "in the subnet" is an *inference about enforcement scope*, not a stated guarantee that the check is cross-account-aware — a canary must still settle whether it fails open across the account boundary. Treat 4b as the primary hypothesis, 4a as the high-severity tail.

**Security Concern.** In a RAM-shared subnet the "existing resources in the subnet" belong to **multiple accounts**. Two questions no page answers:
1. **Enforcement scope** — is the overlap check performed over the **whole subnet (all tenants)** or only the **caller's own resources**? If only own-account, a participant can claim a `/28` **overlapping another account's in-use IPs** → duplicate-address / traffic-blackhole / interception condition against a co-tenant (and prefixes are *included in source/dest checks*, so a crafted prefix on a forwarding ENI could draw a co-tenant's traffic). If whole-subnet, the gate instead becomes an **existence oracle** (Area 4b).
2. **Pre-emption (Lens EE/L)** — can a participant *first-claim* a `/28` covering a co-tenant's known/hardcoded internal-service IP, so the victim's later individual-IP assignment or launch is blocked? (Parallels the [`create-network-interface`](create-network-interface-attack-research-plan.md) Area-2 cross-account IP-collision question, extended to a 16-address block.)

**Area 4b — overlap error as an enumeration oracle (Lens A).** If manual assignment of an overlapping `/28` returns a distinct error ("already assigned / overlaps") vs success, the gate becomes a **cross-tenant IP-usage probe**: sweep candidate `/28`s to map which address ranges a co-tenant occupies, without any read permission on their resources. Distinct error strings / codes / latencies = the oracle.

**High-level Test Scenarios.**
- Claim: *The overlap verification is account-scoped, so a participant can assign a `/28` overlapping an owner/co-tenant IP.* Oracle: 2-account shared-VPC canary — account B assigns `--ipv4-prefixes <range containing a B-visible A-owned IP>`; success = breach. **DryRun will NOT answer this** (caller-IAM-only, pre-resolution). Prove the duplicate assignment exists via `DescribeNetworkInterfaces` on both sides, then STOP.
- Claim: *A participant can pre-empt a co-tenant's planned IP by covering it with a prefix.* Oracle: B claims the `/28`, A's attempt to use an address inside it fails.
- Claim (4b): *Overlap rejection leaks co-tenant IP usage.* Oracle: differential error between a free `/28` and one covering an A-owned IP, from B's credentials only.

**Doc evidence.** `ec2-prefix-eni.md` "Manual assignment" + Basics bullet (overlap requirement) + Considerations ("included in source/destination checks"); shared-VPC isolation is documented **control-plane-only** (`vpc-share-limitations.md`), silent on the address namespace. **Severity-if-true:** account-scoped overlap check enabling cross-tenant duplicate-address/interception = **High–Critical**; pre-emption DoS = High; enumeration oracle = Low–Medium.

---

### Area 5 — Subnet CIDR reservation (type `prefix`) as a steering/squat primitive (Lens EE/A/S)
**Background.** Automatic assignment, verbatim: if the subnet has a reservation of **type `prefix`**, "we select the prefixes from the subnet CIDR reservation." `CreateSubnetCidrReservation` requires the `subnet*` resource type and is scopable by `aws:ResourceTag`/`ec2:AvailabilityZone(Id)`/`ec2:Region`/`ec2:SubnetID`/`ec2:Vpc` — **but there is NO condition key for the reservation `type` (prefix vs explicit) nor for the reserved CIDR value** (confirmed from the row; `GetSubnetCidrReservations` is the read side).

**Security Concern.** Whoever can create a reservation on a subnet controls the pool that *everyone's* automatic prefix assignment in that subnet draws from. In a **shared VPC the subnet owner** holds `CreateSubnetCidrReservation` (participants cannot modify the subnet), so this is largely an **owner→participant steering** question + an **intra-account cross-team** land-grab: a team with `ec2:CreateSubnetCidrReservation` scoped to a subnet (but no CIDR-value key) can reserve a `prefix` block that boxes in or redirects auto-assignment for other teams' ENIs in that subnet, and no policy can constrain *which* CIDR they reserve or forbid the `prefix` type. Also test whether a `prefix`-type reservation sized to cover most of the subnet is a lower-effort variant of the Area-3 exhaustion. **Reservation-page facts (API-ref 2026-10-15):** a reservation object carries an **`OwnerId`** field (reservations are account-scoped objects); *"When you reserve multiple CIDR ranges within the same VPC, the CIDR ranges can't overlap"* (so a squatted reservation **blocks** other principals from reserving the same range — a land-grab primitive); and *"When you reserve more than one range in a subnet for Prefix Delegation, and Prefix Delegation is configured for automatic assignment, we choose the IP addresses to assign to network interfaces **at random**"* (so a reservation an attacker injects does feed others' auto-assign, non-deterministically). The page says **nothing** about who may create a reservation in a shared-VPC participant context, nor about cross-account auto-assign effects → pure doc-gap (D4).

**High-level Test Scenarios.**
- Claim: *A principal with subnet-scoped `CreateSubnetCidrReservation` can reserve a `prefix` block of an arbitrary CIDR; no policy can restrict the CIDR or the type.* Oracle: `SimulateCustomPolicy` shows no key to express it; live create of a reservation with a chosen `--cidr` succeeds under a subnet-scoped role.
- Claim: *Auto-assign for other principals' ENIs in the subnet is thereafter drawn from (or blocked by) the attacker's reservation.* Oracle: create a `prefix` reservation, then auto-assign a prefix on a second ENI → observe the prefix comes from the reserved block / is denied when the block is full.

**Doc evidence.** overview "subnet CIDR reservation of type `prefix`"; `list_ec2.md` CreateSubnetCidrReservation (5484–5490) + DeleteSubnetCidrReservation (6184+) + GetSubnetCidrReservations (3486+); VPC UG `subnet-cidr-reservation` page. **Severity-if-true:** intra-account cross-team steering/DoS = Medium; owner-side feature behaving as designed in shared VPC = Informational (document, don't chase).

---

### Area 6 — EIP-on-prefix and source/dest-check interactions (Lens A/V, chaining)
**Background.** overview: "You can assign an Elastic IP address to a network interface that has a prefix assigned to it" and "to the IP address part of the assigned prefix"; "Prefixes are included in source/destination checks."

**Security Concern.** Two chaining seams, both **owned by siblings for their core mechanism** — logged here as the prefix-specific entry points, not re-derived:
- Associating an EIP to a prefix IP routes into the EIP-association surface; a prefix force-move (Area 2) that **relocates the EIP** chains to the released-EIP squatting / forced-reassociation leads in the [`ec2-networking` hub](ec2-networking-attack-research-plan.md) and the EIP cluster plans.
- "Included in source/destination checks" + the keyless `sourceDestCheck` modify primitive ([`using-eni`](using-eni-attack-research-plan.md) lead #3, [`modify-network-interface-attributes`](modify-network-interface-attributes-attack-research-plan.md)) means a prefix on a forwarding/NAT-enabled ENI is a traffic-draw vector — the MITM-enablement question is owned there; the prefix is just a larger address target.

**High-level Test Scenarios.** Deferred — see §7 pointers. Only test here: does an EIP associated to a prefix IP survive / move with a prefix reassignment (Area 2 amplifier)?

**Severity-if-true:** inherits the chained end (EIP hijack High; MITM High) — rate at the chain end, not here.

---

## 5. Recommended Areas of Focus (priority order)
1. **Area 4** — manual-prefix overlap-check scope across tenants (cross-tenant duplicate-address / pre-emption / enumeration). Highest novel impact; needs 2-account canary.
2. **Area 2** — prefix force-move via `AllowReassignment` (+ EIP ride-along). High; confirm API behavior first (§8 D1).
3. **Area 3** — 16×-amplified shared-subnet exhaustion. High (cross-tenant DoS).
4. **Area 1** — IAM-unscopability (the enabler; settle cheaply with SimulateCustomPolicy, no resources).
5. **Area 5** — subnet-CIDR-reservation steering/squat. Medium.
6. **Area 6** — EIP/source-dest chaining entry points (defer mechanism to siblings).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component / Action | Documented mitigation to attack |
|---|---|---|
| Cross-tenant overlapping-prefix assignment | `AssignPrivateIpAddresses`/`CreateNetworkInterface` manual `--ipv4-prefixes` | "AWS verifies that it is not already assigned to other resources" — **scope unstated** |
| Prefix force-move off a foreign ENI | `AssignPrivateIpAddresses --allow-reassignment` | no documented source-ENI/owner consent; no IAM key |
| Shared-subnet exhaustion via prefix count | `--ipv4-prefix-count` | per-ENI limit (accounts prefix as 1 IP → understates 16×); no per-principal cap |
| Guardrail: forbid/cap prefix delegation | all 5 actions | **no condition key exists** (`ec2:Ipv4Prefix`/`Ipv6Prefix`/count = 0 hits) |
| Steer/squat auto-assign pool | `CreateSubnetCidrReservation --reservation-type prefix` | subnet-scopable, but **no type/CIDR-value key** |
| EIP relocation via prefix reassignment | EIP-on-prefix + Area 2 | "EIP associated with the IP is also moved" (single-IP doc; prefix untested) |

---

## 7. Out-of-Scope / Deferred (do NOT duplicate — cross-reference)
- **The `AssignPrivateIpAddresses … AllowReassignment` secondary-IP takeover primitive, the no-source-owner-consent model, and the no-`AllowReassignment`/`ec2:PrivateIpAddress` key facts** → owned by [`using-instance-addressing`](using-instance-addressing-attack-research-plan.md) (Areas 1/2) and [`instance-secondary-ip-addresses`](instance-secondary-ip-addresses-attack-research-plan.md). This plan only extends them to the **prefix** variant (Area 2).
- **Per-ENI IP-capacity maxima and the general 16×-understatement arithmetic** → [`AvailableIpPerENI`](AvailableIpPerENI-attack-research-plan.md).
- **Create-time ENI attribute unscopability (incl. `Ipv4PrefixCount` at create) and the shared-VPC participant-creates-ENI-with-chosen-IP collision question** → [`create-network-interface`](create-network-interface-attack-research-plan.md) (Areas 2/3).
- **IPv6 bulk-prefix knob under-surfacing and IPv6 being safer (no force-move)** → [`working-with-ipv6-addresses`](working-with-ipv6-addresses-attack-research-plan.md).
- **EIP transfer / released-EIP squatting / forced reassociation / reverse-DNS** → [`ec2-networking` hub](ec2-networking-attack-research-plan.md) + the EIP cluster plans.
- **`sourceDestCheck` MITM-enablement, keyless value-level ENI attribute modify, Reset-on-requester-managed** → [`using-eni`](using-eni-attack-research-plan.md), [`modify-network-interface-attributes`](modify-network-interface-attributes-attack-research-plan.md), [`requester-managed-eni`](requester-managed-eni-attack-research-plan.md).
- **Launch-time public/private IPv4 and shared-VPC forced exposure** → [`working-with-ip-addresses`](working-with-ip-addresses-attack-research-plan.md).
- Guest-OS static-binding split-brain → [`config-windows-multiple-ip`](config-windows-multiple-ip-attack-research-plan.md).
- Single-account self-DoS; IMDS on managed hosts; DNS-rebinding against private endpoints; a customer's own over-broad policy (customer footgun). **Hard stop** on any requester-managed/`Managed=true` ENI.

---

## 8. Null hypotheses / doc-gaps (confirm before investing)
- **D1 (gates Area 2) — PARTIALLY RESOLVED (2026-10-15):** `AssignPrivateIpAddresses` accepts `AllowReassignment` together with the prefix params, but its description is written only for an "IP address," never a prefix → **behavior on a prefix is undocumented, not forbidden.** `AssignIpv6Addresses` has no `AllowReassignment` at all → IPv6 is the unassign-first (safer) shape. **Still open:** does `--allow-reassignment` actually move a `/28` off a foreign ENI, and does any EIP on the prefix relocate with it? Needs a self-canary then one 2-account canary move.
- **D2 (gates Area 4 — the central question) — SHARPENED (2026-10-15):** the overlap requirement is phrased *"existing resources **in the subnet**"* (subnet-scoped on its face), so the plain reading **favors whole-subnet / all-tenant enforcement** → promotes Area 4b (enumeration oracle) over 4a (account-scoped bypass). But the docs never state the check is cross-account-aware; whether it *fails open* across the account boundary is still only a 2-account shared-VPC canary question. DryRun cannot answer (caller-IAM-only, pre-resolution).
- **D3 (Area 4b):** does an overlap rejection produce a **distinct, co-tenant-revealing** error vs a non-overlap success (enumeration oracle)? Given D2's whole-subnet reading, this is now the **leading** live outcome to test first.
- **D4 (Area 5) — CONFIRMED DOC-GAP (2026-10-15):** the subnet-CIDR-reservation page is **silent** on who may create a reservation in a shared-VPC participant context and on cross-account auto-assign effects; the only ownership signal is the reservation's `OwnerId` field. Confirmed facts: reservations can't overlap within a VPC (block primitive) and multi-range `prefix` auto-assign picks addresses at random. The owner-only vs any-subnet-writer boundary is unverifiable from docs → canary.
- **D5:** no EventBridge event is known for IP/prefix assign/unassign (consistent with the sibling finding) → assign/unassign are CloudTrail **management** events only; a cross-account reassign onto an attacker ENI logs in the attacker/ENI-owner trail, giving the victim no push signal (Lens O detection gap). Confirm against the native event catalog.
- **Null lenses (pages read: `ec2-prefix-eni.md`, `work-with-prefixes.md`, relevant `list_ec2` rows):** B/C (no PassRole/role-ARN/SLR/STS — all five actions run under caller identity), G (no server-dereferenced URL — prefix CIDR/subnet/ENI are identifiers/values, not fetched), F/K (no translation layer or LLM), Q (no upload), H/W (no KMS/attestation), Y/FF (no transport/token surface), T (no generated secret), J/M/N/BB/CC/DD all N/A for this control-plane feature. P fires via Area 4 (uniqueness/overlap gate), not a human-proofing flow.

---
*Cross-refs: [[reference-aws-iam-service-auth-ref-url]] — use `list_ec2.html`/`.md`, not the dead `list_amazonec2.html`. All grep line numbers from `docs/service-authorization/latest/reference/list_ec2.md` as of 2026-10-15.*
