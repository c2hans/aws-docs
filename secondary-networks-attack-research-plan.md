# Secondary Networks — Attack / Research Plan

> **Target:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/secondary-networks.html`
> (offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/secondary-networks.md`; online == offline, byte-identical as of 2026-10-15)
> **Service:** Amazon EC2 — Secondary Networks (NEW feature; multi-tenant east-west RDMA fabric for ML/GPU workloads)
> **Method:** `security-questionbuilder` skill (boundary-first question engine). Documentation-only; no live system touched. This file is the research plan a hunter executes later.
> **Authoritative sources used:** User Guide page (above), EC2 API Reference `API_*Secondary*` pages (23 pages, all present offline), IAM Service Authorization Reference `list_ec2.md`.
> **Relationship to existing plans:** This **complements and deepens** the Secondary-Networks summary leads already in `ec2-networking-attack-research-plan.md` (lead B9: "[MH] isolation asserted not mechanized", "[L] quota squatting"). It is the dedicated deep-dive. Cross-corpus RDMA/SRD framing is inherited from `efa-attack-research-plan.md`, `efa-acc-inst-types-attack-research-plan.md`, `efa-working-monitor-attack-research-plan.md`, `ena-nitro-perf-attack-research-plan.md`.

---

## 0. How to use this document

This is a **falsifiable-hypothesis research plan**, not a findings report. Each lead is written as:

> **Claim** (a thing the docs imply should be prevented, stated so it can be broken) → **Mechanism** (exact doc evidence) → **Confirm/Refute oracle** (the single observation that settles it) → **Preconditions / Cost / Severity-if-true**.

Execute leads in the priority order of §5. **Observe HARD STOPs** (§5 A1, A6, A7): the instant evidence shows RDMA traffic, an RDMA memory region/queue-pair, or any identifier/packet crossing into **another AWS account** or **AWS's own Nitro/fabric service plane**, stop immediately, preserve evidence, and flag for AWS-Security disclosure. Do not escalate beyond existence.

The headline is **not IAM** — the Secondary Networks IAM lifecycle (Create/Delete) is largely normally tag-scopable (see §4, §6-S). The headline is the **data-plane isolation model**: an explicitly multi-tenant RDMA fabric whose isolation is asserted as an adjective ("logically isolated", "physically partitioned") and **never attributed to a named enforcement control**, with **no SG / NACL / Flow Logs** to fall back on or to audit with. That is lenses **V / D / A / U / O**.

---

## 1. Components, Assets, and Design

### What the feature is (mechanism, not marketing)
Secondary Networks give an EC2 instance a **second, independent network stack** alongside its VPC ENI(s). The instance is **multi-homed**:
- **VPC side** (NetworkCardIndex 0, `InterfaceType=interface`): ordinary north-south TCP/IP to AWS services + internet. Full VPC controls (SG/NACL/Flow Logs) apply.
- **Secondary Network side** (NetworkCardIndex 1–8, `InterfaceType=secondary`): east-west **RDMA** (`--network-type rdma`, the only supported type) between "specialized" (GPU/ML) instances. **No SG, no NACL, no Flow Logs.**

### Resource model & identifier shapes
| Resource | ID prefix | Scope | ARN condition keys (from `list_ec2.md` resource table, l.9993-9995) |
|---|---|---|---|
| Secondary Network | `sn-` | Regional (L3 network, IPv4 CIDR /28–/12) | `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}` |
| Secondary Subnet | `ss-` | AZ-specific (CIDR /28–/12) within a network | `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}` |
| Secondary Interface | `si-` | Attached to an instance at launch (immutable) | `ec2:LaunchTemplate`, `ec2:IsLaunchTemplateResource`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `aws:ResourceTag/${TagKey}` |

- **ID format (doc-gap):** No formal grammar/length is documented. API-ref examples are consistently **standard 17-hex-char** (`sn-0123456789abcdef0`), **not** the short/low-entropy `ss-98765421yxz` shown in the User Guide CLI snippet (the UG example is uncorroborated and contradicted by every API-ref example). The real backend entropy must be confirmed before any enumeration claim — treat as 17-hex (high entropy) unless proven otherwise.
- **Association/attachment IDs:** `sn-cidr-assoc-…`, `ss-cidr-assoc-…`, `si-attach-…`.

### Identity & privilege
- SigV4 IAM only. No separate RBAC, no hidden admin identity surfaced in these docs, no RAM resource-share path (confirmed absent — see §4 and §6-AA).
- Capacity gating: instances come **only** via `--instance-market-options '{"MarketType":"capacity-block"}'` + a long-term `--capacity-reservation-specification`. "Select instance types" only (type list **not** in these docs → doc-gap, see §5 A7).

### Untrusted-data entry points
1. **Caller-chosen CIDR** (`--ipv4-cidr-block`, /28–/12) for networks and subnets — no cross-tenant uniqueness check documented.
2. **Caller-supplied `PrivateIpAddress.N`** at launch (explicit IP, not just auto-assign count) with **no ownership/account field** on the request object.
3. **DHCP-vended static routes** for cross-subnet reachability — advisory to the guest IP stack.
4. **The RDMA data plane itself** — raw east-west traffic between instances with no packet filter.

### ASCII pipeline

```
                    ┌─────────────────────── EC2 Instance (multi-homed) ──────────────────────┐
                    │                                                                          │
  AWS svcs/internet │   NIC0  InterfaceType=interface  ── VPC ENI ─┐                           │
  <── north-south ──┼── (SG / NACL / Flow Logs APPLY) ────────────┤                           │
                    │                                              │  guest OS route table     │
                    │   NIC1..NIC8  InterfaceType=secondary ───────┤  (DHCP-vended static      │
                    │   (NO SG / NO NACL / NO Flow Logs)           │   route = cross-subnet)   │
                    └──────────────────────────────────┬──────────┴───────────────────────────┘
                                                        │  RDMA (network-type=rdma)
                                                        ▼
          ┌───────────────────────── Secondary Network (sn-…) ────────────────────────────┐
          │  "physically partitioned network infrastructure" / "logically isolated"         │
          │  ┌── Secondary Subnet ss-A (AZ-a) ──┐   ┌── Secondary Subnet ss-B (AZ-a) ──┐    │
          │  │  instance group GPU 0-3           │◄─▶│  instance group GPU 4-7          │    │
          │  │  (direct routes)                  │   │  (reached via DHCP static route) │    │
          │  └───────────────────────────────────┘   └──────────────────────────────────┘    │
          │   ❓ enforcer for cross-SUBNET confinement: NONE NAMED (routing only)             │
          └─────────────────────────────────────────────────────────────────────────────────┘
             ❓ enforcer for cross-NETWORK / cross-ACCOUNT isolation: NONE NAMED  ◄── CROWN JEWEL
             "Multi-tenant support with logical isolation" + "Instances cannot communicate
              across different Secondary Networks"  — asserted, mechanism undisclosed
```

---

## 2. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| TB1 | Tenant A guest (secondary iface) | Tenant B instance on the **same shared RDMA fabric** (different Secondary Network / different account) | Shared "physically partitioned" fabric; no named enforcer | **Any** RDMA op, packet, or guest-counter delta on B caused by A — or vice versa — across the account/network line = **Critical HARD STOP** |
| TB2 | Guest in Secondary Subnet A | Instance in sibling Secondary Subnet B (**same** network) | DHCP-vended static route / direct route; no SG/NACL | Reaching a sibling subnet the operator intended segmented (by GPU-index/workload-type) — isolation is routing-only, not enforced |
| TB3 | Guest OS network stack | The fabric's source-address trust | "IP cannot be changed" (control-plane immutability) vs. on-the-wire source | Fabric accepts a **spoofed/duplicate source IP** transmitted from a secondary interface (no documented anti-spoofing; ifaces are explicitly *not* ENIs) |
| TB4 | Any IAM principal in the account | **All** secondary networks/subnets/interfaces in the account (incl. other teams') | `Describe*` actions with **blank resource type**, only `ec2:Region` | A read-only principal enumerates every `sn-/ss-/si-`, `ownerId`, CIDR, AZ, `instanceId`, `instanceOwnerId`, private IPs, MAC — account-wide, unscopable |
| TB5 | Caller request context | Secondary subnet named at launch | `SecondarySubnetId` string in RunInstances, **no owner/account field** | RunInstances attaches an interface in a subnet the caller does not own (existence-only check) |
| TB6 | Any customer surface | **AWS's own Nitro / fabric service plane** | The RDMA fabric substrate | Any identifier/credential/ARN/packet implicating AWS's own fleet = **hard-stop, preserve, disclose** |

---

## 3. API / Interface Inventory

| Name | Method | New? | Mutating | Facing | Functionality | From Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `CreateSecondaryNetwork` | SDK | **NEW** | Yes | External | Create `sn-` (regional, caller CIDR /28–/12) | Yes (SigV4) | IAM: `ec2:CreateSecondaryNetwork` | Resource `secondary-network*`; keys `aws:RequestTag`, `aws:TagKeys`, `ec2:Region` (**tag-on-create IS supported** — list_ec2 l.5434-5437). **No** CIDR/overlap condition key. |
| `CreateSecondarySubnet` | SDK | **NEW** | Yes | External | Create `ss-` in a network+AZ | Yes | `ec2:CreateSecondarySubnet` | `secondary-network*` (ResourceTag/Region/ResourceTag) + `secondary-subnet*` (RequestTag/TagKeys/Region), l.5440-5443. |
| `DeleteSecondaryNetwork` | SDK | **NEW** | Yes | External | Delete `sn-` (must be empty) | Yes | `ec2:DeleteSecondaryNetwork` | `*required` + `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag` — **deletion IS tag-scopable**, l.6148-6151. |
| `DeleteSecondarySubnet` | SDK | **NEW** | Yes | External | Delete `ss-` | Yes | `ec2:DeleteSecondarySubnet` | Same scoping as above, l.6154-6157. |
| `DescribeSecondaryNetworks` | SDK | **NEW** | No | External | List/read `sn-` + `ownerId`, CIDR, state | Yes | `ec2:DescribeSecondaryNetworks` | **BLANK resource type, only `ec2:Region`** (l.7326-7345) → account-wide read oracle. Filters incl. `owner-id`. MaxResults 5–1000. |
| `DescribeSecondarySubnets` | SDK | **NEW** | No | External | List/read `ss-` + `ownerId`, AZ, CIDR | Yes | `ec2:DescribeSecondarySubnets` | Same unscopable pattern. |
| `DescribeSecondaryInterfaces` | SDK | **NEW** | No | External | List/read `si-` + `ownerId`, **private IPs, MAC, `instanceId`, `instanceOwnerId`** | Yes | `ec2:DescribeSecondaryInterfaces` | Same unscopable pattern. Filters incl. `attachment.instance-id`, `attachment.instance-owner-id`, `private-ipv4-addresses.private-ip-address`. **Richest disclosure.** |
| `RunInstances` (secondary-interfaces) | SDK | existing+**NEW fields** | Yes | External | Launch multi-homed instance; attach up to 8 secondary ifaces | Yes | `ec2:RunInstances` | New rows: `secondary-interface` (RequestTag/TagKeys/Region, **no ResourceTag**) + `secondary-subnet` (ResourceTag/Region/ResourceTag), l.~9586-9598. `InstanceSecondaryInterfaceSpecificationRequest` accepts explicit `PrivateIpAddress.N` with **no owner field**. |
| `CreateTags` / `DeleteTags` | SDK | existing | Yes | External | Tag `si-/sn-/ss-` | Yes | `ec2:CreateTags`/`DeleteTags` | Full tag conditions, l.6250-6260. Relevant to any ABAC gate (§6-S). |

**Console-hidden / under-documented knobs flagged:**
- `DeleteOnTermination` — API ref: *"The only supported value for this field is `true`."* (cannot keep a secondary iface past instance termination — relevant to residual-resource lens, but currently constrained).
- Explicit `PrivateIpAddress.N` vs. `PrivateIpAddressCount` mutual-exclusivity is stated **only on the LaunchTemplate variant**, not restated on the RunInstances request object (doc-gap).
- **No action-specific error codes** on any of the 6 action pages (only generic `CommonErrors`) → cannot confirm/deny a NotFound-vs-AccessDenied enumeration oracle from docs alone (§6-A).

---

## 4. IAM scoping summary (why IAM is NOT the headline)

Confirmed against `list_ec2.md` (corrects two earlier misreads during analysis):
- **CreateSecondaryNetwork does support tag-on-create** (`aws:RequestTag`/`aws:TagKeys`/`ec2:Region`) — do **not** claim a creation-governance gap. (Earlier misread of the blank alphabetical-index row at l.685 was wrong; the full action row l.5434-5437 is authoritative.)
- **Both Deletes carry `aws:ResourceTag`/`ec2:ResourceTag`** — deletion **is** ABAC-scopable. Do **not** claim an ABAC-on-delete gap.
- **The one real IAM gap:** all three `Describe*` actions have a **blank resource type and only `ec2:Region`** → they are **unscopable account-wide read oracles** (TB4, §6-A/R). You cannot write a policy that lets a principal describe only *its own* / *its team's* secondary networks; any `Describe*` grant is account-wide.
- **No condition key for CIDR, overlap, network-type, instance-type, or capacity-reservation** on any Create/RunInstances action → the data-plane choices that matter for isolation (§5) are **not expressible in IAM**.

---

## 5. Recommended Areas of Focus (prioritized; NEW surface concentrated)

Ordered by value. **A1 is the crown jewel and a HARD STOP.** A2–A4 are same-account/lower-risk and should be run **first** as cheap confirmatory work that de-risks and instruments A1.

### A1 — Cross-tenant RDMA isolation has no named enforcer  — Lens V/D/U — **CRITICAL · HARD STOP**
- **Claim:** An instance in one Secondary Network (and especially one account) can send/receive RDMA to/from an instance in a *different* Secondary Network or *different account* on the shared fabric, despite "Instances cannot communicate across different Secondary Networks."
- **Mechanism (doc evidence):** Isolation is asserted only as adjectives — "**logically isolated** within partitions", "**physically partitioned** network infrastructure", "**Multi-tenant** support with logical isolation", "Instances cannot communicate across different Secondary Networks" — with **no attribution to any control** (no Nitro enforcement, no VLAN/VXLAN, no per-tenant encryption, no RDMA queue-pair/memory-region/address-handle scoping, no identity binding of a `si-` to an account). Weaker disclosure than EFA, which at least names SRD. **No SG/NACL/Flow Logs** exist as a fallback or audit channel. This is explicitly **multi-tenant by design**, so EFA's provisional "whole-host-only, therefore OOS" escape hatch (see `efa-acc-inst-types-attack-research-plan.md` Area 2) **cannot be assumed**.
- **Confirm/Refute oracle:** Two Secondary Networks (ideally two accounts) with secondary subnets in the same AZ. If a guest-readable RDMA counter analog (see A3 — must confirm one exists first) on instance A increments as a direct result of an **uncooperative** RDMA op from instance B in the *other* network/account — or any packet/segment from B is observed on A's secondary interface — the guarantee is **falsified**.
- **Preconditions:** Two Secondary-Network-eligible instances (capacity-block + CR; see A7); same AZ; ideally cross-account. **Cost:** high (capacity-block commitment). **Severity:** **Critical.** **HARD STOP** at the first sign of cross-account/cross-network delivery — preserve evidence, flag for disclosure, do **not** escalate (no data dumping, no QP reuse, no second record). Pre-live work should be **confirm-the-mechanism-first** via AWS inquiry, mirroring `efa-attack-research-plan.md` Area 4.

### A2 — Cross-subnet separation is routing-only, not a security boundary — Lens V — **Medium–High (same-account)**
- **Claim:** An operator who segmented sensitive workloads *by secondary subnet* (per the doc's own "segment traffic by GPU index / workload type" guidance) has **no enforcement** to rely on; a compromised guest reaches any sibling subnet in its own network.
- **Mechanism:** "Instances within the same secondary subnet are reachable through **direct routes**. Cross subnet communication is **available via a static route vended via DHCP**." + no SG/NACL exist. DHCP-vended routes are advisory to the guest IP stack; a guest with route-table/root access can add routes, or craft packets to a sibling subnet CIDR. Up to **200 subnets/network** — a large flat domain with no filtering primitive. Note the doc applies "security boundary" language to *Secondary Networks*, not to subnets — so sibling reachability is **intended**, and the finding is precisely that subnets are **unsafe to use as an isolation control**.
- **Oracle:** From a guest in subnet A (same account/network), reach an instance in sibling subnet B that the operator intended segmented; traffic succeeds with no filter available to stop it.
- **Preconditions:** one instance, two subnets, one network — **no cross-account line crossed.** **Cost:** low. **Severity:** Medium–High. Safe to test directly; run before A1.

### A3 — Audit blind spot: no Flow Logs, no documented telemetry — Lens O — **Low-as-enabler (multiplies A1/A2)**
- **Claim:** East-west RDMA in Secondary Networks has **zero AWS-side observability** and possibly no guest-side instrument either — a real cross-tenant breach would be **undetectable by any documented means**.
- **Mechanism:** "VPC features such as Security Groups, NACLs, **Flow Logs are not supported**." Stronger blind spot than EFA (where Flow Logs *are* supported, MAC-shaped — `efa-working-monitor-attack-research-plan.md`). The secondary-networks page documents **no** CloudWatch integration and **no** driver-counter family (no analog of EFA's `rdma_write_bytes` = "bytes written to it by other instances", the sole in-guest evidence of a non-cooperating peer).
- **Oracle / required pre-work for A1:** Determine whether **any** guest-readable counter/telemetry surface exists for secondary interfaces (sysfs `hw_counters`, `rdma -p statistic show`, or vendor driver equivalent). **A1 cannot be instrumented from inside the guest until this gap is resolved.** If none exists, A1's falsification degrades to AWS-side confirmation only.
- **Severity:** Low alone; **amplifier** for A1 and A2. **Doc-gap — confirm surface first.**

### A4 — Account-wide `Describe*` read oracle — Lens A/R — **Medium (intra-account), Low cross-account (pending)**
- **Claim:** Any principal granted `ec2:DescribeSecondary*` can enumerate **every** secondary network/subnet/interface in the account — including other teams' — with no resource-level scoping, harvesting `ownerId`, CIDRs, AZs, **`instanceId`, `instanceOwnerId`, private IPs, and MAC addresses**.
- **Mechanism:** All three `Describe*` have **blank resource type + only `ec2:Region`** (`list_ec2.md` l.7326-7345). API-ref confirms the response objects disclose `ownerId`/`instanceOwnerId`/`privateIpAddress`/`macAddress` **unconditionally** (no documented per-field redaction), and filters (`owner-id`, `attachment.instance-id`, `private-ipv4-addresses.private-ip-address`) allow targeted lookup. **Cross-account behavior when passing a non-owned ID is undocumented** (silent-empty vs. error vs. disclose) — test this: it is the difference between an intra-account footgun and a cross-tenant disclosure.
- **Oracle:** (intra) a scoped-down read-only role still lists resources it has no business seeing → confirmed unscopable. (cross) passing another account's `si-`/`sn-` ID returns the resource or a distinguishable NotFound/AccessDenied → disclosure oracle or enumeration oracle respectively. Note: no action-specific error codes are documented, so the NotFound-vs-AccessDenied distinction must be measured empirically.
- **Severity:** Medium intra-account (unscopable read + rich PII-ish network metadata); escalates if cross-account IDs resolve. **Safe to test (reads only).**

### A5 — Launch-time subnet ownership & explicit-IP injection — Lens A/C — **Medium–High (confirm ownership check)**
- **Claim:** `RunInstances` attaches a secondary interface into a `SecondarySubnetId` **without a documented ownership check**, and lets the caller pin an explicit `PrivateIpAddress` — potentially placing the caller's instance into another tenant's subnet or at a chosen address.
- **Mechanism:** `InstanceSecondaryInterfaceSpecificationRequest.SecondarySubnetId` is a bare string with **no owner/account field** anywhere in the request schema (ownership is response-side only). `PrivateIpAddress.N` lets the caller choose the exact IP (vs. auto-assign). The RunInstances `secondary-interface` IAM row carries **no `ResourceTag`** (only RequestTag/TagKeys/Region), so ABAC on the interface-to-be-created can't gate it; the `secondary-subnet` row does carry `ResourceTag` — so whether launch is gated depends on the subnet's tags, not the interface's.
- **Oracle:** Launch referencing a `ss-` owned by a different account/team; if the interface attaches, existence-only (not ownership) is checked. Combined with A2/A3, a chosen-IP interface in a foreign subnet is a lateral/impersonation primitive. **If the foreign subnet is in another account, this becomes a HARD STOP** (treat as A1).
- **Severity:** Medium–High same-account; Critical/HARD-STOP if cross-account attach succeeds. **Doc-gap on the ownership check — confirm first.**

### A6 — IP spoofing / duplicate-IP at the fabric — Lens V/D — **Doc-gap; High if absent · HARD STOP if cross-account**
- **Claim:** No fabric-level anti-spoofing exists for secondary interfaces; "IP cannot be changed" is a **control-plane (API) immutability** statement, not guest-OS-wire enforcement. Secondary interfaces are explicitly "**physically and logically separate from ENIs**" — so they may **not** inherit Nitro ENI source/dest-check anti-spoofing.
- **Mechanism:** "Secondary interfaces IP addresses cannot be changed once launched" (control-plane phrasing, mirrors `ModifyNetworkInterfaceAttribute`). No source/dest-check analog is mentioned. Duplicate-IP/ARP/ND behavior across tenants is undocumented, compounded by caller-controlled CIDRs (A7-adjacent) that can collide.
- **Oracle:** From a guest with driver access, transmit a packet with a source IP ≠ the launch-assigned IP (or duplicating a peer's) and observe whether the **fabric** (not just the local kernel) drops or forwards it. Silent forward = direct secondary finding feeding A1. **Stop immediately if the spoofed source lands in another account's instance.**
- **Severity:** High if anti-spoofing is genuinely absent; non-finding if silently inherited from Nitro. **Confirm surface first.**

### A7 — Capacity-reservation / instance-type physical-sharing precondition — Lens V — **Doc-gap; multiplier for A1/A6**
- **Claim:** Whether Secondary-Network-eligible instances are **whole-host-exclusive** or drawn from a **shared/pooled** substrate is undocumented here — and it determines whether A1's and A6's "shared physical substrate" reading (and any GPUDirect-RDMA cross-tenant GPU-memory reach) is even in scope.
- **Mechanism:** "available for select instance types and through capacity reservations with long term commitments"; launch uses `MarketType: capacity-block` + a CR. **No instance-type list** and **no host-exclusivity statement** in these docs (unlike `efa-acc-inst-types.md`, which at least names `.48xlarge`/metal). The GPU-index-to-subnet best practice (8 interfaces, NetworkCardIndex 1–8) mirrors the exact "shares an underlying physical NIC/GPU on host" ambiguity flagged in `efa-acc-inst-types-attack-research-plan.md` Area 2 — but here the context is **explicitly multi-tenant**, removing EFA's provisional de-risking.
- **Oracle:** Resolve from **instance-type + capacity-reservation documentation** (not this page): does a capacity-block/long-term CR guarantee dedicated, non-reused physical hosts for the reservation term, or only *capacity*? If pooled/non-exclusive → A1/A6 "(b) shared substrate" becomes architecturally likely → Critical. If strictly whole-host → narrows A1 risk to the fabric/network layer alone (still unresolved).
- **Severity:** Not independently exploitable; a **precondition multiplier.** Resolve before assuming physical sharing. If a shared substrate is confirmed, any GPUDirect-RDMA cross-tenant GPU-memory attempt is an immediate **HARD STOP**.

### A8 — CIDR overlap across tenants — Lens U/L — **Doc-gap; feeds A1 if misroute occurs**
- **Claim:** CIDR uniqueness across tenants/networks is **not enforced** — only a non-binding best practice (and it's about VPC-overlap for *routing simplicity*, not isolation). Two tenants can pick identical CIDRs (the doc's own example is `172.31.0.0/16`).
- **Mechanism:** `--ipv4-cidr-block` /28–/12, no documented uniqueness/registry; "Avoid Overlapping CIDRs ... **simplifies routing**" framing only; overlap check at CreateSecondarySubnet is scoped **only** to "an existing secondary subnet in the **same** secondary network" (API ref). No region/account-wide dedup.
- **Oracle:** Two networks (ideally two accounts) with identical CIDRs + identical subnet CIDRs; observe whether DHCP-vended/direct routes mis-resolve or deliver cross-network. A misroute/delivery is a **second, independent falsification path for A1** (orthogonal to the RDMA-counter oracle). If "partition" fully namespaces per `sn-` regardless of CIDR, overlap is harmless (Low, self-inflicted routing footgun).
- **Severity:** Low self-inflicted if namespaced; feeds Critical A1 if cross-delivery occurs. **Confirm first.**

### A9 — Quota / capacity squatting — Lens L — **Low–Medium (same-account mostly)**
- **Claim:** Shared-pool capacity + low adjustable quotas (5 networks/region, 200 subnets/network) enable intra-account denial or capacity hogging; cross-account capacity contention depends on A7.
- **Mechanism:** Quotas table; **no IAM condition key caps network/subnet/interface count per principal** (unscopable — see §4). Combined with capacity-block pooling (A7), capacity exhaustion of a scarce GPU pool is plausible.
- **Oracle:** Create to the quota ceiling and observe denial of a co-account team's create; or (pending A7) observe cross-account capacity starvation.
- **Severity:** Low–Medium. Complements `ec2-networking-attack-research-plan.md` "[L] quota squatting" lead.

---

## 6. Threat Model Test Objectives (lens-by-lens, incl. null hypotheses)

| Lens | Fires? | Lead / Null hypothesis (pages checked) |
|---|---|---|
| **A** — Cross-tenant IDOR / read oracle | **YES** | A4 (`Describe*` unscopable account-wide; rich disclosure), A5 (launch into foreign subnet). Pages: all 3 Describe API refs, `list_ec2.md` l.7326-7345, RunInstances spec. |
| **V** — Network segmentation / reachability | **YES (headline)** | A1 (cross-network), A2 (cross-subnet routing-only), A6 (spoofing). Pages: UG Architecture/Troubleshooting/best-practices. |
| **D** — Data→control plane | **PARTIAL** | A6 (fabric trust of guest-sourced packets); A1 (if fabric substrate reaches AWS service plane = TB6 HARD STOP). No control-ENI/host-service surface is *documented*, so marked doc-gap, not N/A. |
| **U** — Guarantee vs. enforcement | **YES** | A1/A2/A8 — every isolation guarantee ("logically isolated", "cannot communicate across networks") traced to **no named mechanism**. Pages: UG Overview/Key-concepts/best-practices. |
| **O** — Audit-log evasion | **YES** | A3 (no Flow Logs, no documented telemetry). Page: UG Additional considerations. |
| **L** — Resource exhaustion | **YES** | A9 (quota/capacity squatting). Page: UG Quotas; `list_ec2.md` (no count key). |
| **R** — IAM-artifact audit | **YES** | §4: Describe* unscopable; RunInstances `secondary-interface` row has no ResourceTag. No sample IAM-policy JSON is shipped on this page (only the two action names in Troubleshooting) → nothing to statement-audit beyond `list_ec2`. |
| **S** — Condition-key scoping semantics | **YES** | §4 — Create/Delete tag-scopable (corrects earlier misreads); Describe* unscopable; **no CIDR/network-type/instance-type/CR condition key** → the isolation-relevant choices are IAM-inexpressible. Page: `list_ec2.md`. |
| **AA** — Share/revoke lifecycle | **NULL** | **No RAM / resource-share / cross-account-share path exists** for secondary networks/subnets/interfaces. Pages checked: all 23 API refs (grep "RAM/share/cross-account/organization/multi-tenant" → only `ownerId` fields), UG (no share section). This **narrows** cross-tenant risk to the physical-fabric question (A1), not a sharing-misconfiguration question. |
| **B** — Confused deputy / PassRole | **NULL** | No role-ARN input on any Secondary* API; no "acts on your behalf" fetch. Pages: all Create/RunInstances request schemas. |
| **C** — Credential vending / session scope | **NULL** | No STS/session-policy/token-input surface. Pages: all API refs. |
| **E** — RBAC / priv-esc | **NULL** | No custom roles/hidden admin surfaced. Pages: UG, API refs. |
| **F** — Translation-layer / wire injection | **NULL (doc-gap)** | No documented customer-input→query/command transform; DHCP-route vending is the closest (covered under A2). RDMA wire-format parsing by the fabric is undocumented → doc-gap, not a confirmed surface. |
| **G** — SSRF (field service dereferences) | **NULL** | No URL/URI/endpoint/callback/webhook field in any Secondary* request. Pages: all Create/RunInstances schemas, UG getting-started. |
| **Q** — Uploaded blob / parser | **NULL** | No blob/file/image input; AMI driver support is the customer's own image, not a service-parsed upload. Pages: UG Troubleshooting, RunInstances. |
| **P** — Gate before privileged state change | **PARTIAL/doc-gap** | Capacity-reservation "active" state + instance-type eligibility are the only gates (A7). No OTP/consent/uniqueness gate. Pages: UG prerequisites/troubleshooting. |
| **T** — Generated secret storage | **NULL** | Service generates no persisted secret/key documented here. Pages: all API refs. |

---

## 7. Out of Scope

- **Live cross-account/cross-network RDMA probing beyond first-signal existence** — A1/A5/A6 become HARD STOPs the instant any cross-account delivery or AWS-service-plane identifier appears. No data dumping, no QP/MR reuse, no second-record retrieval, no escalation.
- **Anything implicating AWS's own Nitro/fabric service plane (TB6)** — hard stop, preserve evidence, disclose.
- **DNS enumeration, port scanning, subnet bruting** — HTTP/application + documented data-plane only.
- **Customer-side self-contention / self-DoS** (e.g., exhausting one's own quota, misconfiguring one's own guest routes) — a configuration footgun, not a service defect, unless it crosses to another tenant.
- **Instance-type/capacity-reservation internals** beyond confirming host-exclusivity (A7) — resolve via other AWS docs, not by probing.

---

## 8. Null hypotheses & doc-gaps to resolve before live testing

1. **Guest-side telemetry for secondary interfaces (A3)** — does any `rdma_write_bytes`-equivalent counter exist? **Blocks instrumentation of A1.** Resolve first.
2. **Describe\* on a non-owned ID (A4)** — silent-empty vs. error vs. disclose? Determines intra- vs. cross-tenant severity. Safe to test (reads).
3. **RunInstances subnet ownership check (A5)** — does it validate the `SecondarySubnetId` belongs to the caller? Undocumented.
4. **Fabric anti-spoofing (A6)** — inherited from Nitro or absent (ifaces are explicitly *not* ENIs)?
5. **Host-exclusivity of eligible instance types / capacity reservations (A7)** — whole-host vs. pooled. The pivotal multiplier for A1/A6.
6. **CIDR namespacing (A8)** — does the `sn-` partition fully namespace overlapping CIDRs, or can overlap cause cross-delivery?
7. **ID entropy (A1-adjacent)** — 17-hex (per API-ref examples) vs. the short `ss-98765421yxz` UG example. Confirm before any enumeration claim.
8. **Action-specific error codes** — none documented; the NotFound-vs-AccessDenied enumeration-oracle question (A4) must be measured empirically.
9. **RDMA wire-format parsing by the fabric (Lens F)** — undocumented; confirm whether the fabric parses any customer-controlled wire structure.

**Bottom line:** The IAM lifecycle is mostly well-scoped; the risk lives entirely in the **data plane**. The crown jewel (A1) is a cross-tenant RDMA-isolation guarantee asserted without a named enforcer, in an explicitly multi-tenant fabric with no SG/NACL/Flow-Logs backstop or audit trail. Treat it exactly as the EFA sibling plans treat their cross-tenant-SRD HARD STOP: confirm-the-mechanism-first, instrument only if a guest-side counter is confirmed to exist, and stop at the first byte of cross-account delivery.
