# EC2 Prefix Delegation (`work-with-prefixes`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-prefixes.html` ("Manage prefixes for your network interfaces" — IPv4/IPv6 **prefix delegation** on network interfaces; **NOT** managed prefix lists). Supporting pages: `ec2-prefix-eni.html` (concept/limits), `subnet-cidr-reservation.html` (VPC UG), `vpc-share-limitations.html`, `prefix-mode-linux.html` (EKS), the five `API_*` references, and the authoritative IAM table `service-authorization/.../list_ec2.md`. Status: **documentation-derived hypotheses only; nothing tested against a live account.** Online twins verified byte-identical to the offline mirror on 2026-10-15 for `work-with-prefixes.md`, `ec2-prefix-eni.md`, `subnet-cidr-reservation.md`.

> **Position in the EC2-Networking plan set.** This is a page-level child of the **ec2-networking hub** and a **convergence complement** of `managing-network-interface-ip-addresses-attack-research-plan.md`. Prefix delegation introduces **no new API** — it rides the same ENI IP-management actions. This plan therefore owns ONLY the prefix-specific surface and cross-references, without restating, the siblings that already own the base actions:
> - **`managing-network-interface-ip-addresses`** — the 6-action convergence: a single `network-interface*` grant authorizes all IP ops; 0 per-IP-value/safety condition keys. (Prefix delegation uses 4 of those 6 actions.)
> - **`AvailableIpPerENI`** — per-ENI IP capacity maxima; already notes `/28` prefix = 16 real addrs → up-to-16× understated. This plan owns the **action-level** unscopability that `AvailableIpPerENI` left to the addressing siblings.
> - **`create-network-interface`** — create-time ENI attributes unscopable (prefix is one of them).
> - **`working-with-ipv6-addresses`** — IPv6 prefix bulk knob (`Ipv6Prefix`/`Count`) under-surfaced.
> - **`using-instance-addressing`** — `AssignPrivateIpAddresses` + `AllowReassignment` secondary-IP cross-ENI takeover.
> - **`instance-secondary-ip-addresses`** — `UnassignPrivateIpAddresses` → EIP auto-disassociation collateral (single secondary IP).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **Backbone note (load-bearing):** all 5 prefix APIs and all 3 subnet-CIDR-reservation APIs run under the **caller's own identity** — there is no service-linked role in the ENI IP path (unlike Fleet). So the caller's expressible IAM conditions DO bind. The force of this plan's headline is **not** "an SLR strips my conditions" — it is "**the conditions I would need to write do not exist as IAM keys.**"
- **`DryRunOperation` is caller-IAM-only** (evaluated before resource resolution) → it can prove a condition key is inert, but it is **not** an ownership/overlap oracle. The custom-prefix overlap and cross-account tests need a two-account canary, not DryRun.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, stated as outcomes)
1. **Shared-subnet IPv4 exhaustion / cost DoS** against co-tenant accounts, amplified ~16× per `/28` prefix, that **no IAM policy on the subnet owner's side can cap** (no prefix-count or prefix-size condition key).
2. **Cross-account subnet-CIDR-reservation pre-emption/griefing:** claim or delete a block of a RAM-shared subnet's IP space (`CreateSubnetCidrReservation` type `prefix`, or `DeleteSubnetCidrReservation`) so that another participant's / the owner's auto-prefix allocation is starved or silently re-steered.
3. **Account/region-wide prefix recon** via the unscopable `DescribeNetworkInterfaces` / `GetSubnetCidrReservations` oracles (enumerate every ENI's prefixes and every reservation's owning account).
4. **Cross-ENI / cross-account prefix takeover** via a custom `--ipv4-prefixes` CIDR that overlaps a victim's block (likely refuted by documented overlap-rejection — settle it) and the `AllowReassignment`-on-prefix question.
5. **Orphaned-EIP / collateral** from unassigning a prefix that contains an EIP-mapped address (doc-gap).

---

## 2. Components, Assets, and Design

**What the feature is.** Prefix delegation assigns a *CIDR block* (not a single address) to a network interface. IPv4 prefixes are fixed at **`/28` (16 addresses)**; IPv6 prefixes at **`/80` (2^48 addresses)** (`ec2-prefix-eni.html`: *"The IPv4 prefix that you can specify is `/28`." / "The IPv6 prefix that you can specify is `/80`."*). Supported on **Nitro-based instances only**. Primary consumer is EKS/VPC-CNI "prefix mode" for pod density (`prefix-mode-linux.html`: *"Prefix mode is enabled by default on IPv6 clusters and is the only option supported."*).

**The amplification mechanic (the asset at risk).** `ec2-prefix-eni.html` Considerations, verbatim: *"The maximum number of IP addresses that you can assign to a network interface depends on the instance type. **Each prefix that you assign to a network interface counts as one IP address.** … you can assign up to 9 prefixes to the network interface."* → a prefix consumes **1 unit** of the per-ENI IP quota but delivers **16** (IPv4) or **2^48** (IPv6) real addresses out of the subnet's shared pool. One `AssignPrivateIpAddresses --ipv4-prefixes 10.0.0.208/28` call removes 16 real addresses from the subnet in a single operation.

**The five actions (identical to the IP-management set, with prefix params layered on):**

```
            ┌─────────────────────────── caller identity (no SLR) ───────────────────────────┐
            │                                                                                 │
  create ─► CreateNetworkInterface ──┐                                                        │
                                      ├─►  ENI  ◄── AssignPrivateIpAddresses (--ipv4-prefix*)  │
  manage ─► AssignIpv6Addresses ──────┘           AssignIpv6Addresses       (--ipv6-prefix*)  │
  remove ─► UnassignPrivateIpAddresses / UnassignIpv6Addresses (--ipv4-prefixes/--ipv6-prefixes)
            │                                                                                 │
            │   auto-assign source selection:                                                 │
            │     if subnet has a CIDR reservation of type `prefix`  →  draw from reservation  │
            │     else                                               →  draw from subnet CIDR  │
            └── CreateSubnetCidrReservation / DeleteSubnetCidrReservation / GetSubnetCidrReservations
                (VPC-level, separate IAM actions — steer where auto-prefixes come from)
```

**Identifiers / assets:** `eni-…` (ENI ID), subnet ID, the prefix CIDR itself (caller-chosen or auto), `SubnetCidrReservation` object (`cidr`, `reservationType ∈ {prefix,explicit}`, `ownerId`, `subnetId`). EIPs may be mapped onto an address inside a delegated prefix (`ec2-prefix-eni.html`: *"You can also assign an Elastic IP address to the IP address part of the assigned prefix."*).

**Identity / trust model:** SigV4 IAM, caller identity throughout. The cross-tenant surface appears only in a **RAM-shared VPC subnet**, where a participant account creates/manages its own ENIs (and can create subnet CIDR reservations) in the owner's subnet (`vpc-share-limitations.md`).

---

## 3. API / Interface Inventory

| Name | Mutating | Facing | Functionality | Authorized callers | IAM resource type / key surface (from `list_ec2.md`) | Notes |
|---|---|---|---|---|---|---|
| CreateNetworkInterface | yes | ext | create ENI, optionally with prefixes | any `ec2:CreateNetworkInterface` holder | `network-interface*`(aws:RequestTag/TagKeys/ec2:NetworkInterfaceID/Region) + `subnet*`(AZ/AZId/Region/ResourceTag/SubnetID/Vpc) + `security-group` | **No prefix/count/CIDR key.** Params `Ipv4Prefix.N`/`Ipv4PrefixCount`/`Ipv6Prefix.N`/`Ipv6PrefixCount`, mutually exclusive w/ each other and w/ specific IPs. |
| AssignPrivateIpAddresses | yes | ext | add secondary IPv4 **or IPv4 prefixes** to existing ENI | ENI owner / shared-subnet participant on own ENI | `network-interface*` only: aws:ResourceTag, ec2:AvailabilityZone, ManagedResourceOperator, NetworkInterfaceID, Region, ResourceTag, Subnet, Vpc | **8 generic keys, 0 prefix/count/AllowReassignment key.** `AllowReassignment` is a request param defined only for "an IP address". |
| AssignIpv6Addresses | yes | ext | add IPv6 addrs **or IPv6 prefixes** | same | identical 8-key set | **No `AllowReassignment` param at all.** |
| UnassignPrivateIpAddresses | yes | ext | remove secondary IPv4 / **IPv4 prefixes** | same | identical 8-key set | EIP-inside-prefix fate undocumented. |
| UnassignIpv6Addresses | yes | ext | remove IPv6 / **IPv6 prefixes** | same | identical 8-key set | — |
| CreateSubnetCidrReservation | yes | ext | reserve a CIDR block in a subnet (`prefix` steers auto-assign) | `ec2:CreateSubnetCidrReservation` holder | `subnet*`: AZ/AZId/Region/ResourceTag/SubnetID/Vpc | **No `Cidr`-value key, no `ReservationType` key.** `prefix`-type reservation reduces available-IP count **immediately** on create. |
| DeleteSubnetCidrReservation | yes | ext | delete a reservation | `ec2:DeleteSubnetCidrReservation` holder | **blank resource type**, only `ec2:Region` | **Resource:"*" account/region-wide; cannot be scoped to a subnet or owner.** |
| GetSubnetCidrReservations | no | ext | list reservations (incl. `ownerId`) | `ec2:GetSubnetCidrReservations` holder | **blank resource type**, only `ec2:Region` | Discloses foreign-account `ownerId`. Unscopable read oracle. |
| DescribeNetworkInterfaces | no | ext | list ENIs incl. `Ipv4PrefixSet`/`Ipv6PrefixSet` | List-level holder | **blank resource type**, only `ec2:Region` | Account/region-wide prefix recon oracle. |

Console surfaces only a binary **Auto-assign / Custom** radio per address family — it never exposes the parameter names, the mutual-exclusivity rules, or any count ceiling (Lens U delta).

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Shared-subnet **participant account** | **Owner's / co-participant's** usable IP space in the shared subnet | `AssignPrivateIpAddresses --ipv4-prefix-count N` / `--ipv4-prefixes` (16 addrs each), or `CreateSubnetCidrReservation` type `prefix` | Co-tenant `RunInstances`/ENI create fails `InsufficientFreeAddressesInSubnet` / CNI `InsufficientCidrBlocks` while attacker holds the blocks — **and no owner IAM policy could have capped the attacker's prefix count/size.** |
| Any grantee of `ec2:DeleteSubnetCidrReservation` | **Another account's** subnet CIDR reservation | `DeleteSubnetCidrReservation` (Resource:"*") | A reservation with a foreign `ownerId` is deleted / auto-assignment re-steers to the raw subnet CIDR; victim EKS CNI loses reserved space. |
| Any `DescribeNetworkInterfaces` / `GetSubnetCidrReservations` holder | Every ENI's prefixes + every reservation's owner, account/region-wide | unscopable List/Get | Reading `Ipv4PrefixSet`/`ownerId` for resources the caller cannot tag- or ARN-scope. |
| Caller supplying a custom `--ipv4-prefixes` CIDR | A block already assigned to **another ENI** (possibly another account) | overlap handling in Assign/Create | A custom prefix overlapping a victim block is **accepted** (takeover/breach) vs **rejected** (existence oracle only). |
| Caller unassigning a prefix | An **EIP** mapped to an address inside that prefix | `UnassignPrivateIpAddresses --ipv4-prefixes` | EIP silently disassociates / orphans, or the call is rejected (doc-silent). |
| any customer surface | AWS service plane | — | hard stop. |

---

## 5. Recommended Areas of Focus

### Area 1 — HEADLINE (Lens S/U/L, AWS-owned reportable): prefix *size* and *count* are structurally IAM-unscopable; prefix delegation is a documented ~16× amplifier of the per-ENI IP primitive
**Background.** Prefix delegation layers `Ipv4Prefix.N`/`Ipv4PrefixCount`/`Ipv6Prefix.N`/`Ipv6PrefixCount` onto `CreateNetworkInterface` and the two `Assign*` actions. `ec2-prefix-eni.html` states each prefix "counts as one IP address" against the per-ENI maximum while delivering 16 (IPv4 `/28`) or 2^48 (IPv6 `/80`) real addresses.
**Security Concern.** An exhaustive sweep of all 941 unique `ec2:*` identifiers in `list_ec2.md` found **no condition key — none — that can gate a prefix value, a prefix count, or an IPv4/IPv6 address count on any of the 5 actions** (`ec2:Ipv4Prefix`/`Ipv6Prefix`/`*PrefixCount`/`ec2:Cidr` do not exist; the only `*Count` keys — `ec2:InstanceCount`/`ec2:TargetInstanceCount` — are Capacity-Reservation/Fleet-only; `ec2:InsideTunnelCidr` is VPN-only; `ec2:Ipv4IpamPoolId`/`Ipv6IpamPoolId` are IPAM-only and not on these rows). The gating surface available to a policy author is strictly **identity-based** (`ec2:NetworkInterfaceID`, `ec2:SubnetID`, `ec2:Vpc`, `ec2:AvailabilityZone`, tags) — never **content-based**. Therefore there is no IAM dial between "may create/manage an ENI in this subnet" and "may delegate a 16-address block, or 9 of them, in one call." This **sharpens `AvailableIpPerENI`'s capacity finding at the action level**: `AvailableIpPerENI` owns the per-ENI maxima; this plan owns the fact that the *amplifier* (prefix size/count) is unexpressible in policy.
**High-level Test Scenarios.**
- **Claim:** A principal granted only `ec2:AssignPrivateIpAddresses` scoped to a subnet (`ec2:SubnetID`) can assign the maximum prefixes the ENI/instance-type allows and no policy on that grant can reduce the count or forbid `/28`-size blocks. → **Mechanism:** 8-key `network-interface*` row (`list_ec2.md` ~4700-4707); no prefix key anywhere. → **Oracle:** `iam:SimulateCustomPolicy` with a hypothetical `Deny` on `ec2:Ipv4PrefixCount`/`ec2:Ipv4Prefix` shows the key is **inert** (unknown key, never matches) while the `Assign` still simulates `allowed`; no resource touched. → **Severity-if-true:** Medium (customer-least-priv control gap; **AWS-owned reportable** because it is a structural absence in the IAM reference, not a customer artifact).
- **Claim:** A shared-subnet participant can exhaust the subnet's usable IPv4 for all co-tenants ~16× faster per API call than with single-IP assignment, undetected by any count-based IAM guard. → **Mechanism:** "each prefix counts as one IP" + `vpc-share-limitations.md` line 43 (participants "can associate or disassociate IP addresses with the network interfaces that they created"). → **Oracle:** two-account canary in a RAM-shared subnet — participant assigns prefixes up to its ENI limit; measure co-tenant `RunInstances` failing `InsufficientFreeAddressesInSubnet`. → **Severity-if-true:** High (cross-tenant DoS on shared infra).
**Doc evidence:** `ec2-prefix-eni.html` Considerations; `list_ec2.md` action rows; condition-key sweep. **Stop condition:** once SimulateCustomPolicy confirms key inertness, the IAM gap is settled; the exhaustion magnitude needs a canary.

### Area 2 — Subnet CIDR Reservation as a cross-tenant pre-emption / steering / griefing primitive (NET-NEW; no sibling owns these 3 actions)
**Background.** `work-with-prefixes.html` line 8: *"If you let us automatically assign prefixes and the subnet … has a subnet CIDR reservation of type `prefix`, we select the prefixes from the subnet CIDR reservation. Otherwise, we select them from the subnet CIDR range."* `subnet-cidr-reservation.html`: a `prefix`-type reservation lets AWS auto-assign from it; `explicit` lets you manually assign. Reservation = `{cidr, reservationType, ownerId, subnetId}`.
**Security Concern — three distinct sub-primitives:**
- **(2a) Immediate capacity claim / starvation.** `subnet-cidr-reservation.html`, verbatim: *"The reservation type affects the count of available IP addresses for the subnet. If you create a prefix reservation, the count decreases immediately."* → a reservation **locks a block of the shared subnet's IP pool the instant it is created, before any ENI exists**. `CreateSubnetCidrReservation`'s IAM row scopes only `subnet*` (ARN/tag/AZ/VPC/region) — there is **no `Cidr`-value key and no `ReservationType` key** — so a policy can allow a principal to reserve *in* a subnet but cannot cap *how much* or *which* range, nor forbid the `prefix` type. A participant in a RAM-shared subnet can thereby pre-emptively starve co-tenants and the subnet owner.
- **(2b) Auto-assignment hijack/steering.** Whoever can `CreateSubnetCidrReservation` on a subnet controls where every subsequent **auto-assigned** prefix is drawn from. Multiple prefix reservations → *"we choose the IP addresses to assign … at random"* (not caller-controlled), but the *source pool* is attacker-defined.
- **(2c) Cross-account reservation deletion (griefing).** `DeleteSubnetCidrReservation` has a **blank resource-type cell and only `ec2:Region`** → it is effectively `Resource:"*"` account/region-wide; **IAM cannot restrict which subnet's or which owner's reservation a grantee may delete.** A principal granted it for any reason can delete another account's reservation, collapsing the EKS CNI's reserved prefix space (the exact mitigation `prefix-mode-linux.html` recommends) and re-steering auto-assignment back to the raw (possibly contended) subnet CIDR.
**High-level Test Scenarios.**
- **Claim:** A shared-subnet participant with `ec2:CreateSubnetCidrReservation` on the shared subnet can reserve a large `prefix`-type block and immediately reduce the owner's available-IP count, with no owner IAM lever over the CIDR or type. → **Oracle:** two-account canary; `GetSubnetCidrReservations` shows the participant-owned reservation with a foreign `ownerId`; owner's available count drops. → **Severity:** High (cross-tenant DoS / resource squatting).
- **Claim:** A grantee of `ec2:DeleteSubnetCidrReservation` can delete a reservation owned by a different account/subnet. → **Mechanism:** blank resource type (`list_ec2.md` ~6184-6188). → **Oracle:** SimulateCustomPolicy shows no resource-level constraint is expressible; two-account canary confirms the delete of a foreign-`ownerId` reservation succeeds. → **Severity:** High (cross-tenant integrity/availability).
**Doc evidence:** `work-with-prefixes.md` L8; `subnet-cidr-reservation.md`; `API_CreateSubnetCidrReservation.md` (`Cidr`, `ReservationType ∈ {prefix,explicit}` both required request params, un-gatable); `list_ec2.md` reservation rows. **Stop condition:** stop at the first confirmed cross-account reservation create/delete; do not enumerate further.

### Area 3 — Unscopable prefix/reservation read oracles (Lens A / U)
**Background & Concern.** `DescribeNetworkInterfaces`, `GetSubnetCidrReservations`, and `DescribeSubnets` each have a **blank resource-type cell and only `ec2:Region`** in `list_ec2.md` — unscopable account/region-wide. `DescribeNetworkInterfaces` returns `Ipv4PrefixSet.N`/`Ipv6PrefixSet.N` per ENI (`API_NetworkInterface.md`); `GetSubnetCidrReservations` returns `cidr`/`reservationType`/`ownerId` (including **foreign-account** owners). Request-side `Filter.N` (subnet-id/vpc-id/tag) are caller query filters, **not** IAM restrictions — they limit what a call asks for, not what the oracle *can* see. This is the prefix-specific instance of the same inert-ABAC Describe-oracle shape documented for `manage-spot-fleet`'s `DescribeSpotFleetRequests`.
**High-level Test Scenarios.**
- **Claim:** A principal with only `ec2:DescribeNetworkInterfaces` (no tag/ARN scoping possible) can enumerate every ENI's delegated prefixes account/region-wide → the recon that makes the Area-2/Area-4 custom-prefix and pre-emption plays practical. → **Oracle:** the IAM row (blank resource type) + the `Ipv4PrefixSet` response field; confirm an attempted `Deny` keyed on tag/subnet is inert for this action. → **Severity:** Low–Medium (intra-account over-exposure; enabler for the higher-severity areas).
- **Claim:** `GetSubnetCidrReservations` discloses the owning account of every reservation in a shared subnet. → **Severity:** Low (info-leak; enables targeting in Area 2).

### Area 4 — Custom-prefix overlap: takeover (likely refuted) vs existence oracle vs `AllowReassignment` (Lens A / X)
**Background.** Custom assignment lets the caller name the exact CIDR (`--ipv4-prefixes 10.0.0.208/28`). `ec2-prefix-eni.html` Basics states, for manual assignment: *"The prefix is in the subnet CIDR … and does not overlap with other prefixes or IP addresses assigned to existing resources in the subnet"* and *"Manual assignment — You specify the prefix and AWS verifies that it is not already assigned to other resources before assigning it to your network interface."*
**Security Concern.** The documented overlap-**rejection** makes direct cross-ENI/cross-account prefix *takeover* via a colliding custom prefix **likely refuted** (lean-null) — but it simultaneously creates an **existence oracle** (reject = block in use by *some* resource, possibly another account's ENI), and it leaves two questions open:
- **(4a)** Does `AllowReassignment=true` on `AssignPrivateIpAddresses` apply to a **prefix** (force-move a /28 off another ENI), or only to a single secondary IP? The param is defined only as "an IP address … already assigned to another network interface or instance"; `AssignIpv6Addresses` has **no `AllowReassignment` param at all**. Prefix force-move is **inferred-no from omission**, never stated — a lead to settle. (Cross-ref `using-instance-addressing`, which owns the single-secondary-IP `AllowReassignment` takeover; this plan asks whether that primitive extends to whole blocks.)
- **(4b)** Overlap-rejection semantics across accounts in a shared subnet: does the "existing resources in the subnet" check span the owner + all participants (so rejection reveals cross-account usage)?
**High-level Test Scenarios.**
- **Claim:** A custom `--ipv4-prefixes` overlapping a co-tenant's assigned block is **rejected**, not assigned (refutes takeover; confirms oracle). → **Oracle:** two-account canary; expect `InvalidParameterValue`/overlap error, not a successful move. → **Severity:** takeover-if-accepted = High–Critical (treat as hard-stop candidate for cross-account); oracle-only = Low–Medium.
- **Claim:** `AllowReassignment=true` does **not** move a prefix off a foreign ENI. → **Oracle:** canary with `AllowReassignment=true` + a prefix overlapping another ENI; expect rejection. **DryRun will not answer this** (IAM-only, pre-resolution). → **Severity:** if it *does* move = High (cross-ENI/cross-account block theft).
**Stop condition:** stop at the first evidence of acceptance against a foreign-owned block (preserve, flag); otherwise record the refutation.

### Area 5 — Unassign-prefix collateral: EIP-inside-prefix fate (Lens A/U doc-gap)
**Background.** `ec2-prefix-eni.html`: *"You can also assign an Elastic IP address to the IP address part of the assigned prefix."* Both `API_UnassignPrivateIpAddresses.md` and `API_UnassignIpv6Addresses.md` are **silent** on what happens to an EIP mapped to an address inside a prefix when that prefix is unassigned (contrast: the *Assign* API documents EIP-follows-IP for a single-IP move). This complements `instance-secondary-ip-addresses` (which owns `UnassignPrivateIpAddresses` → EIP auto-disassociation for a *single secondary IP*); here the collateral is an EIP buried inside a /28 block torn out in one call.
**High-level Test Scenarios.**
- **Claim:** Unassigning a prefix that contains an EIP-mapped address silently disassociates/orphans the EIP (or is rejected). → **Oracle:** canary — map an EIP into a delegated prefix, `unassign-private-ip-addresses --ipv4-prefixes <that /28>`, observe EIP association state. → **Severity:** Medium (availability/dangling-IP; low if cleanly rejected). **Stop condition:** record the observed behavior; this is a doc-gap settle, not an exploit.

### Area 6 — No EventBridge signal for any prefix/reservation action (Lens O)
**Background & Concern.** An exhaustive read of the EC2 EventBridge event-type list (`automating_with_eventbridge.md`) shows **no event type** for network-interface IP/prefix assign/unassign or for subnet CIDR reservation create/delete. The five prefix APIs and the three reservation APIs leave **only a CloudTrail management-event trail** — no near-real-time signal. A shared-subnet starvation/pre-emption (Areas 1–2) is therefore detectable only by after-the-fact CloudTrail review, not by an EventBridge-driven alarm.
**Test Scenario.** **Claim:** No EventBridge rule can be written to fire on prefix assignment or reservation creation. → **Oracle:** the event-type catalog omission (doc-confirmed). → **Severity:** Low/Informational (detection-latency enabler that raises the practical severity of Areas 1–2).

### Area 7 — Count-ceiling / schema-integrity doc-gaps (Lens U / L)
- **(7a)** No `Ipv4PrefixCount`/`Ipv6PrefixCount` **numeric ceiling** is stated in any of the 5 API reference pages (only the generic per-ENI/instance-type limit). The effective cap is the per-ENI IP maximum (`AvailableIpPerENI`) × subnet CIDR size — but the API docs never say so. Confirm whether an oversized count returns a clean error or over-allocates. **Severity:** Low (doc-gap; feeds Area 1).
- **(7b)** No published **per-subnet / per-account quota** for prefixes or subnet CIDR reservations (`amazon-vpc-limits.md` documents only the unrelated managed-prefix-list quota). The only bounds are the subnet CIDR size and per-ENI IP count. **Severity:** Low (doc-gap; relevant to Area 2 squatting).
- **(7c)** **Schema inconsistency:** `CreateNetworkInterface` types `Ipv4Prefix.N`/`Ipv6Prefix.N` as structured `Ipv4PrefixSpecificationRequest`/`Ipv6PrefixSpecificationRequest` objects, while the four `Assign*/Unassign*` actions type the equivalent params as bare "Array of strings." Also a prose typo ("Ipv4 Prefixes") in `AssignPrivateIpAddresses`. **Severity:** Informational (relevant only to request-validation/allow-list builders). **Nitro-only** prerequisite is a scope note, not a lead.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Shared-subnet IPv4 exhaustion ×16 per `/28`, uncappable by IAM | AssignPrivateIpAddresses prefix path | None — no prefix-count/size condition key; relies on per-ENI limit + subnet size only |
| Cross-account reservation pre-emption (immediate capacity claim) | CreateSubnetCidrReservation (type `prefix`) | `subnet*` ARN/tag scoping only — no `Cidr`/`ReservationType` key |
| Cross-account reservation deletion / auto-assign re-steer | DeleteSubnetCidrReservation | None expressible — blank resource type, `ec2:Region` only |
| Account/region-wide prefix + reservation-owner recon | DescribeNetworkInterfaces / GetSubnetCidrReservations | None — unscopable List/Get (`ec2:Region` only) |
| Custom-prefix cross-ENI/cross-account takeover | AssignPrivateIpAddresses / CreateNetworkInterface | "AWS verifies not already assigned to other resources" (overlap-reject) — settle whether it spans accounts; AllowReassignment-on-prefix undocumented |
| Orphaned EIP on prefix unassign | UnassignPrivateIpAddresses | Undocumented (doc-gap) |
| No near-real-time detection of the above | all 8 actions | CloudTrail management events only; no EventBridge event |

---

## 7. Out-of-Scope Risk Categories
- **Managed prefix lists / IPAM / BYOIP** (`CreateManagedPrefixList`, `AllocateIpamPoolCidr`, etc.) — different feature set; this page is **network-interface prefix delegation** only.
- Single-tenant self-exhaustion (a customer filling their own private subnet) — least-priv footgun, not cross-tenant.
- IMDS / in-guest behavior of delegated prefixes — managed-host surface.
- The base ENI-IP takeover/collateral primitives already owned by `using-instance-addressing` and `instance-secondary-ip-addresses` — cross-referenced, not re-tested here except for the prefix-specific extension questions (Areas 4–5).
- Per-ENI IP maxima enumeration — owned by `AvailableIpPerENI`.
- Shared RDS/Grover/storage infra; AWS service-plane; DNS rebinding against private endpoints.

## 8. Null hypotheses / lenses that did not fire (pages checked)
- **Lens B/C (PassRole / credential vending):** N/A — none of the 8 actions accept a role ARN or vend credentials; all run under caller identity (checked `list_ec2.md` rows + all 5 API refs; no `roleArn`/PassRole param).
- **Lens G (SSRF):** N/A — no field is dereferenced/fetched server-side; prefix values are CIDRs, not URLs (checked `work-with-prefixes`, `ec2-prefix-eni`, all 5 API refs).
- **Lens F / K / Q (injection / LLM / upload):** N/A — no translation layer, no agent/LLM, no file/blob upload; inputs are CIDR strings and integers.
- **Lens H (KMS), J (OAuth), W (attestation), Y (transport), FF (JWT), DD/CC/BB (cache / upstream-context / canonicalization):** N/A — no KMS key, 3P link, attestation gate, custom transport, token, cache layer, authorizer, or multi-parser request path in this surface (checked the 5 API refs + the IAM rows).
- **Lens A direct cross-tenant *takeover* via custom prefix:** **lean-null** — documented overlap-rejection ("AWS verifies that it is not already assigned to other resources") blocks the direct steal; retained as **Area 4** because the cross-account span of that check and the `AllowReassignment`-on-prefix question are doc-silent and need a canary.
- **Doc-gaps carried as leads (confirm surface before deep investment):** (a) `AllowReassignment` applicability to prefixes; (b) EIP-inside-unassigned-prefix fate; (c) cross-account span of overlap-rejection; (d) `Ipv4PrefixCount`/`Ipv6PrefixCount` numeric ceiling; (e) per-subnet/account prefix & reservation quotas; (f) participant→participant/owner `DescribeNetworkInterfaces` visibility in a shared subnet (`vpc-share-limitations.md` documents only owner→participant).

---

*Cross-references:* `managing-network-interface-ip-addresses` (6-action convergence, 0 per-IP-value keys), `AvailableIpPerENI` (per-ENI maxima + /28 16× note), `create-network-interface` (create-time attributes), `working-with-ipv6-addresses` (IPv6 prefix bulk knob), `using-instance-addressing` (AllowReassignment secondary-IP takeover), `instance-secondary-ip-addresses` (Unassign→EIP collateral), `ec2-networking` hub. IAM authority: `service-authorization/.../list_ec2.md` — see `reference_aws-iam-service-auth-ref-url`.
