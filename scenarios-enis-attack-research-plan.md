# Multiple Network Interfaces (scenarios-enis) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/scenarios-enis.html` (offline mirror `docs/AWSEC2/latest/UserGuide/scenarios-enis.md`), cross-read against `using-eni.md`, `network-interface-attachments.md`, `modify-network-interface-attributes.md`, and `list_ec2.md` (IAM Service Authorization Reference). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **What this page is.** A conceptual *scenarios / best-practices* page ("Multiple network interfaces for your Amazon EC2 instances"). It introduces **no new API, no new parameter, no IAM policy JSON, no URL/upload/token field.** It describes 5 use-cases for attaching multiple ENIs to one instance:
> 1. **Management network** — primary ENI = public (80/443 from 0.0.0.0/0), secondary ENI = SSH-only from a restricted range/subnet/VGW, on a "separate subnet that has more restrictive access controls," same AZ.
> 2. **Network and security appliances** — NAT / proxy / LB with multiple ENIs "with their own public and private IP addresses, security groups, and source/destination checking."
> 3. **Dual-homed instances across subnets** — web→mid-tier→DB, each instance multi-homed into the next zone's subnet.
> 4. **Dual-homed instances across VPCs in the same account** — attach a secondary ENI from a *different VPC* (same AZ); explicitly marketed to **"overcome CIDR overlaps between two VPCs that can't be peered"** and "connect multiple VPCs within a single account." States: **"You can't create multi-homed instances across VPCs in different AWS accounts."**
> 5. **Low-budget, high-availability** — on instance failure, attach the ENI to a hot-standby; **"the interface maintains its private IP addresses, Elastic IP addresses, and MAC address"** so traffic begins flowing with no route-table/DNS change.
>
> **Therefore this plan is a SCENARIOS-LEVEL COMPLEMENT, not a new-mechanism plan.** It cross-references the per-action siblings and OWNS only the net-new framings this page uniquely contributes: (i) the Scenario-4 **cross-account multi-homing prohibition as a documented guarantee** + the cross-VPC attach-as-VPC-isolation-bypass that AWS *markets as a feature*; (ii) the **dual-homed instance as an OS-level bridge between two security zones** that no SG/NACL sees; (iii) **MAC-address portability on ENI failover** as an identity/license-binding transfer primitive (net-new attribute detail). Everything else is a POINTER to the owning sibling — do not re-derive.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Most of this page's mechanisms are already owned by siblings. **Read the POINTERS in §5 first** and do not duplicate the owning plan's work. This plan's genuinely net-new leads are **S4-U1, S4-V1, S5-AA1** (the three bolded owned leads).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (a requester-managed / `Operator`-attributed / EKS-Auto-Mode `Managed=true` ENI, or any AWS-fleet-owned instance), stop, preserve evidence, flag for AWS-Security disclosure. ENI scenarios run entirely under the customer's own identity — there is no SLR / service-fleet launch path on this page.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Cross-VPC isolation bypass by design:** confirm whether a principal that can `AttachNetworkInterface` can bridge two VPCs (or two subnets with asymmetric SGs) that security architecture assumed were isolated, and whether an admin can IAM-fence the attach to same-VPC. **Breach oracle:** an ENI from VPC-B successfully attached to an instance in VPC-A under a policy intended to confine the principal to VPC-A.
2. **Cross-account multi-homing:** confirm the documented "can't … across VPCs in different AWS accounts" guarantee is actually enforced by the API/service, not just prose/console. **Breach oracle:** a cross-account ENI attach that the doc says is impossible returns success (or a weaker-than-expected error that leaks a different enforcement layer).
3. **Security-zone bridge:** confirm that a multi-homed instance (Scenario 1/3) silently forwards/routes between the public zone and the "more restrictive" management/backend zone at the OS level, defeating the per-ENI SG model. **Breach oracle:** traffic reaching the restricted-subnet resource via the dual-homed host from a source the restricted SG would reject.
4. **Failover-relocation identity transfer:** confirm that moving an ENI to a standby carries the victim's **private IPs + EIPs + MAC + SGs + source/dest-check** to the new host, and that this is authorizable without `iam:PassRole` or any IP/MAC-value condition key. **Breach oracle:** a standby instance inheriting a victim ENI's full L2/L3 identity (incl. MAC-bound license) via Attach/Detach.
5. **source/destination-check MITM enablement** (Scenario 2): confirm an admin cannot forbid turning an instance into an unchecked NAT/router/firewall via `ModifyNetworkInterfaceAttribute`. **Breach oracle:** `sourceDestCheck=false` set under a policy intended to prevent it.

---

## 2. Components, Assets, and Design
- **Customer-facing interface:** EC2 control-plane API (SigV4 / console) — `AttachNetworkInterface`, `DetachNetworkInterface`, `CreateNetworkInterface`, `ModifyNetworkInterfaceAttribute`, `AssociateAddress`/`DisassociateAddress`, `AssignPrivateIpAddresses`. **No API is unique to this page.**
- **Resources & identifiers:** `eni-<17hex>` (network interface), `eni-attach-<id>` (attachment, no IAM ARN — authz rides on the ENI), `i-<17hex>` (instance), `subnet-…`, `vpc-…`, EIP `eipalloc-…`. Identity carried by the ENI: primary + secondary private IPv4, one EIP per private IPv4, one public IPv4, secondary IPv6, **security groups, a MAC address, a source/destination-check flag**, description (`using-eni.md:14-24`).
- **Accounts / VPCs:** everything on this page is **single-account**. The only cross-account statement is a *prohibition* (Scenario 4). The real cross-tenant surface for ENIs (RAM-shared subnets, cross-account `CreateNetworkInterfacePermission`) lives on the sibling pages, not here.
- **Identity model:** direct caller identity (IAM principal). No service-linked role, no PassRole on this page's actions, no credential vending. "the code running on your behalf" (Scenario 5) implies an **automation principal holding `ec2:AttachNetworkInterface`/`DetachNetworkInterface`** — a relocation role, audited below.
- **Untrusted-data transforms:** none on this page (no parser, no fetch, no upload).

ASCII — the multi-homed-instance bridge (Scenario 1/3/4):
```
                 ┌──────────── EC2 instance (one OS kernel) ────────────┐
  internet  ───► eth0 (SG: 80/443 from 0.0.0.0/0)                        │
  (public subnet, VPC-A)                                                 │
                 │   ← the OS can forward/route between the two NICs →   │
  mgmt/DB    ───► eth1 (SG: SSH-only / DB-only; "more restrictive")      │
  (restricted subnet, same AZ — or a DIFFERENT VPC-B in same account)    │
                 └──────────────────────────────────────────────────────┘
   SG/NACL evaluate each ENI independently; NEITHER sees the in-OS hop between eth0 and eth1.
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal scoped to VPC-A | ENI in VPC-B (same acct) | `AttachNetworkInterface` (same AZ) | Attach succeeds under a policy meant to confine to VPC-A → cross-VPC bridge (there is no `ec2:Vpc` on the instance row to fence it) |
| Caller in account X | ENI/instance in account Y | cross-account attach | Doc says impossible — any success, or an error that reveals the enforcement is console/orchestration-only, is a finding |
| Public zone (eth0) | restricted mgmt/DB subnet (eth1) | OS-level forwarding on the dual-homed host | A packet reaching the restricted resource via the host that the restricted SG would have dropped |
| Attacker automation role (`ec2:AttachNetworkInterface`) | victim ENI's full identity (IPs/EIP/MAC/SG) | Detach-from-victim + Attach-to-standby | Standby inherits the victim's MAC/EIP/private-IPs → traffic + MAC-bound license follow |
| Any customer surface | AWS service plane | — (none on this page) | **Hard stop** if a requester-managed / `Managed=true` / `Operator`-attributed ENI appears |

---

## 4. API / Interface Inventory
All actions below are **existing**, SDK, external-facing, callable from the Internet, authorized to any IAM principal granted them. None is unique to this page — each is owned by a sibling plan (see §5 pointers).

| Name | Mutating | Functionality on this page | Owning sibling plan |
|---|---|---|---|
| `AttachNetworkInterface` | yes | attach secondary ENI (Scenario 1-5), cross-VPC (S4) | `network-interface-attachments`, `using-eni` (lead #2) |
| `DetachNetworkInterface` | yes | detach for failover (S5) | `network-interface-attachments` |
| `CreateNetworkInterface` | yes | create the secondary ENI with chosen SG/IP | `create-network-interface` |
| `ModifyNetworkInterfaceAttribute` | yes | set `sourceDestCheck=false` for NAT/router (S2), swap SGs | `modify-network-interface-attributes`, `using-eni` (lead #3) |
| `AssociateAddress`/`DisassociateAddress` | yes | EIP that rides along on failover (S5) | `elastic-ip-addresses-eip`, `working-with-eips` |
| `AssignPrivateIpAddresses` | yes | secondary private IPv4 for failover (S1 Note) | `using-instance-addressing` |

No undocumented/console-hidden knob is introduced on this prose page (the hidden-knob audit belongs to the per-action siblings — `create-network-interface` Area 4 `trunk`/`Operator`, `modify-network-interface-attributes` 5 console-hidden params).

---

## 5. Recommended Areas of Focus

### Area S4-U1 — [NET-NEW, OWNED] Cross-account multi-homing prohibition is a documented guarantee with no stated enforcement mechanism (Lens U)
**Background.** Scenario 4 asserts, verbatim: *"You can't create multi-homed instances across VPCs in different AWS accounts."* It simultaneously markets same-account cross-VPC multi-homing as a deliberate feature to *"overcome CIDR overlaps between two VPCs that can't be peered"* and *"connect multiple VPCs within a single account."*
**Security Concern.** The page states a cross-account **negative capability** (a security guarantee) but names no mechanism that enforces it. Per the Lens-U method, trace the promise to the enforcer: is "different AWS account" rejected by `AttachNetworkInterface` server-side, or only unreachable because you can't normally *name* a foreign ENI? The sibling `using-eni` lead #2 already establishes that the `AttachNetworkInterface` **`instance` resource row carries no `ec2:Vpc`/`ec2:Subnet` key** — the join between the ENI's VPC and the instance's VPC is service-enforced, not IAM-expressible. The open question this page raises: *is the cross-account boundary enforced at the same service layer, and does it hold if a foreign ENI becomes nameable* (e.g. via a RAM-shared subnet where a participant created the ENI, or a cross-account `CreateNetworkInterfacePermission` grant)?
**High-level Test Scenarios.**
- Claim: `AttachNetworkInterface(eni owned by account Y, instance owned by account X)` returns success → cross-account multi-homing despite the doc. → Oracle: a successful attach, or a non-`AccessDenied` error (e.g. `InvalidParameterValue`) that shows the check is a parameter/orchestration guard rather than an ownership gate. Needs a 2-account canary; the ENI must be nameable (RAM-shared subnet participant ENI, or a cross-account ENI permission). **DryRun is caller-IAM-only — it will NOT answer this; it short-circuits before resource/ownership resolution.**
- Claim: the guarantee is only "you can't normally reference a foreign ENI," so once a foreign ENI *is* referenceable (shared-subnet participant ENI), the attach is not independently account-checked. → Oracle: attach a participant-created ENI (account Y) to the subnet-owner's instance (account X) in the same shared subnet/AZ.
**Doc evidence:** `scenarios-enis.md:48` (prohibition + same-AZ requirement). **Severity-if-true:** cross-account L2 adjacency / data-plane bridge = **High–Critical**; if merely a confusing doc guarantee that *is* enforced, Informational (file the doc-vs-enforcement note). **Stop:** if the foreign resource turns out to be AWS-owned, hard stop.

### Area S4-V1 — [NET-NEW, OWNED] The dual-homed instance is an OS-level bridge the SG/NACL model cannot see (Lens V/U)
**Background.** Scenarios 1, 3, and 4 all describe one instance straddling two security zones: a public ENI and a "more restrictive" management/backend ENI (S1), or web↔mid-tier↔DB tiers (S3), or two non-peered VPCs (S4). AWS presents this as isolation ("more restrictive access controls" on the secondary subnet) while the whole value proposition is that one host sits in both zones.
**Security Concern.** Security groups and NACLs evaluate **each ENI independently** (per-ENI SG model — see `using-instance-addressing`/`using-eni`). Neither control sees the **in-kernel hop** between eth0 and eth1. A dual-homed host is therefore a standing bridge: anything that compromises the public-facing process (eth0) is already L3-adjacent to the restricted subnet (eth1) with no SG/NACL in the path — the "more restrictive access controls" protect against *direct* reach to eth1 but not against reach *through the host*. Scenario 4 makes this explicit for VPC isolation: it is sold as a way to defeat the absence of VPC peering. This is a documented-guarantee-vs-mechanism gap (Lens U) layered on a network-segmentation reality (Lens V): the segmentation the architecture assumes (subnet/VPC isolation) is defeated by design the moment multi-homing is used, and no per-ENI control expresses "this host may not forward between its NICs."
**High-level Test Scenarios.**
- Claim: a source permitted only to eth0 (public SG) can reach a service in the restricted subnet by pivoting through the dual-homed host's OS (IP forwarding, a proxy/appliance process, or an app that "initiates a connection to the backend"). → Oracle: a connection landing on the restricted-subnet resource whose source, if sent directly, the restricted SG would drop. (Scenario 2/3 literally describe the host "initiates a connection to the backend" and NAT/proxy appliances — the forwarding is the intended behavior; the finding is that it is **ungoverned by any AWS control** and invisible to flow-based detection on the restricted subnet, which sees only the host's eth1 as source.)
- Claim: VPC Flow Logs / GuardDuty on the restricted subnet attribute all bridged traffic to the dual-homed host's eth1, masking the true external origin (detection/attribution gap, Lens O). → Oracle: flow-log entries show only eth1→target, never the real client.
**Doc evidence:** `scenarios-enis.md:19-28` (mgmt network, "more restrictive access controls"), `:43` ("initiates a connection to the backend"), `:38` (NAT/proxy appliances), `:51-52` (cross-VPC bridge). **Severity-if-true:** this is **architecture-inherent, largely a customer-design footgun** when the customer builds it — but it is **AWS-documented guidance that presents multi-homing as compatible with "more restrictive" isolation without warning that the host defeats it**, so the reportable artifact is the **doc guidance gap (Lens U/R-adjacent, Low–Informational)**. The *exploitation* of a specific customer's bridge is out of scope here (customer-authored topology). **Stop:** do not pivot into any resource you don't own.

### Area S5-AA1 — [NET-NEW DETAIL, OWNED] ENI failover carries private IPs + EIPs + **MAC address** + SGs + source/dest-check to the standby (Lens AA / X)
**Background.** Scenario 5 ("low-budget, high-availability"): on instance failure, *"the code running on your behalf … attach the network interface to a hot standby,"* and *"the interface maintains its private IP addresses, Elastic IP addresses, and MAC address, [so] network traffic begins flowing to the standby instance as soon as you attach the network interface."* `using-eni.md:8` confirms *"The attributes of a network interface follow it as it's attached or detached …"* and `:14-24` lists the full carried attribute set: private IPv4s, one EIP per private IPv4, public IPv4, secondary IPv6, **security groups, a MAC address, a source/destination-check flag**, description.
**Security Concern.** This is the **ENI-relocation primitive owned by `network-interface-attachments`** (its HEADLINE: "detach from one instance attach to another = IP/EIP/SG/MAC relocation"), framed here as a *supported, encouraged automation*. Two net-new angles this scenario adds beyond the attachments plan:
  1. **MAC-address portability as an identity/license transfer.** MAC is explicitly in the carried set. Software licensing, in-guest allow-lists, and some AWS-adjacent identity schemes bind to MAC. A principal holding only `ec2:DetachNetworkInterface` + `ec2:AttachNetworkInterface` (no `iam:PassRole`, no `RunInstances`, no IP/EIP action) can move a victim ENI onto an attacker-controlled standby and **inherit the victim's MAC-bound identity + all EIPs + all private IPs** in one step. The attachments plan owns the IP/EIP ride-along; **this plan flags the MAC specifically** as the under-considered carried attribute.
  2. **No condition key governs the carried values.** There is no `ec2:PrivateIpAddress`, `ec2:Ipv6Address`, EIP-value, or MAC condition key on the assign/attach actions (confirmed across siblings) — so an admin can scope *which ENIs* a relocation role may attach/detach (by tag/ENI-id) but cannot scope *what identity rides along*. The "code running on your behalf" automation role is thus a full-identity-transfer capability if over-broad.
**High-level Test Scenarios.**
- Claim: a role with only `ec2:AttachNetworkInterface`+`ec2:DetachNetworkInterface` (ENI scoped by tag) can relocate a victim ENI (its EIPs/private-IPs/MAC/SGs intact) to an attacker standby without any IP/EIP/PassRole permission. → Oracle: attach succeeds; standby's `ip link`/metadata shows the victim MAC + the EIP now routing to the standby. Settle the IAM shape first with `iam:SimulateCustomPolicy` (no resources); then a single-account canary with two instances + one tagged ENI.
- Claim: the source/destination-check flag rides along too (`using-eni.md:23`), so relocating an ENI that had `sourceDestCheck=false` lands a NAT/router-enabled NIC on the standby without a separate `ModifyNetworkInterfaceAttribute` call. → Oracle: standby ENI reports `sourceDestCheck=false` immediately post-attach. (Chains to Area S2 below.)
**Doc evidence:** `scenarios-enis.md:57`, `using-eni.md:8,14-24`. **Severity-if-true:** intra-account cross-team full-identity hijack via a mis-scoped relocation role = **Medium–High** (the IAM scoping gap is the AWS-relevant part; the capability is by-design). **Cross-ref — do not re-derive the base relocation/force-detach/no-EventBridge facts:** `network-interface-attachments` plan.

### Area S2 — [POINTER] source/destination-check disable = ungoverned MITM/NAT/router enablement (Lens S/U/D)
Scenario 2 ("configure the additional interfaces with their own … source/destination checking") is the scenario that motivates disabling src/dest check to build NAT/proxy/firewall appliances. **Owned by `using-eni` (lead #3) and `modify-network-interface-attributes`:** value-level condition keys `ec2:SourceDestCheck`/`DeleteOnTermination`/`DeviceIndex`/`NetworkCardIndex`/`InterfaceType` are **0-hit in `list_ec2`**, so `ModifyNetworkInterfaceAttribute` scopes only the attribute *name* (`ec2:Attribute`), never its *value* → granting the ability to modify `sourceDestCheck` = granting MITM/transit-node enablement with no guardrail, plus case-sensitivity fail-open on any Deny written against the lowercase enum. **Do not re-run; chains into S4-V1 (bridge) and S5-AA1 (flag rides along).**

### Area S1/S4 cross-VPC attach IAM-unfenceability — [POINTER]
**Owned by `using-eni` lead #2:** `AttachNetworkInterface` @list_ec2 ≈4858 — the `instance` row has **no `ec2:Vpc`/`ec2:Subnet` key**, so the same-account cross-VPC attach this page markets (S4) **cannot be IAM-fenced to same-VPC**; the NI-row `ec2:Vpc` binds the ENI's *own* VPC, not the target instance's. This plan's S4-U1 extends that to the **cross-account** boundary question; the same-account cross-VPC unfenceability itself is already owned. Do not re-derive.

### Area S1 secondary-private-IPv4 failover + EIP ride-along — [POINTER]
The S1 **Note** ("consider using a secondary private IPv4 … move the interface and/or secondary private IPv4 address to a standby") is the `AssignPrivateIpAddresses … AllowReassignment` + collateral-EIP-move surface. **Owned by `using-instance-addressing` (Area 1: no source-ENI/owner check, no `AllowReassignment`/`ec2:PrivateIpAddress` key, EIP rides along) and `instance-secondary-ip-addresses` (UnassignPrivate collateral EIP disassociation).** Do not re-derive — the scenario here is just the HA framing of that primitive.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account ENI attach despite the doc prohibition | `AttachNetworkInterface` | "You can't create multi-homed instances across VPCs in different AWS accounts" (`:48`) — trace to the enforcing layer |
| Same-account cross-VPC attach under a VPC-confined policy | `AttachNetworkInterface` | per `using-eni` #2: no `ec2:Vpc` on instance row (confirmed-unfenceable) |
| Public→restricted-subnet pivot via dual-homed host | OS of multi-homed instance | per-ENI SG "more restrictive access controls" (`:21,25`) — does not govern in-OS forwarding |
| Full-identity (MAC/EIP/IP/SG) hijack via relocation role | `Detach`+`AttachNetworkInterface` | ENI-id/tag scoping only; no value-level key for carried attributes |
| `sourceDestCheck=false` under a policy meant to forbid it | `ModifyNetworkInterfaceAttribute` | per `using-eni` #3 / modify sibling: no `ec2:SourceDestCheck` value key |
| Flow-log/attribution masking of bridged traffic | VPC Flow Logs on restricted subnet | source attributed to host eth1, not real client (Lens O) |

---

## 7. Out-of-Scope Risk Categories
- **Customer-authored topology.** A customer that *chooses* to multi-home a host across zones owns that design decision; exploiting a *specific customer's* bridge is their footgun, not an AWS defect. The in-scope artifact is only the **AWS doc guidance** that presents multi-homing as compatible with "more restrictive" isolation without warning of the OS-bridge (Lens U, Low–Informational).
- **The ENI-relocation primitive itself** (Attach/Detach moving IPs/EIP/MAC) — by-design; owned by `network-interface-attachments`. Only the **IAM-scoping gap** on a relocation role is reportable here (and it is a customer-authored-policy footgun unless it appears in an AWS-published sample policy — none on this page).
- **Requester-managed / `Managed=true` / `Operator`-attributed ENIs** = AWS service plane — hard stop, never a target.
- **Shared RDS/Grover/host infra, IMDS on managed hosts, DNS rebinding against private-only endpoints** — standard exclusions.
- **IPv6 reassignment** (safer — no `AllowReassignment` force-move) — deferred to `working-with-ipv6-addresses`.

## 8. Null hypotheses / doc gaps (lenses checked, pages named)
Pages read for triggers: `scenarios-enis.md` (full), `using-eni.md:1-47`, cross-ref sibling plan summaries.
- **A (IDOR):** N/A on this prose page — no resource-by-ID API is introduced; `eni-`/`i-` ids are 17-hex (non-fabricable, checksum-bearing) → cross-tenant IDOR is a genuine null here. The nameability question is folded into S4-U1.
- **B/C (PassRole / vending):** **null** — no role-ARN input, no PassRole on any action, no SLR, no credential vending on this page. ("the code running on your behalf" is an automation *principal* the customer builds, audited as S5-AA1's scoping gap, not a PassRole.)
- **F (injection), K (prompt), FF (JWT):** N/A — no parser/translator/LLM/token on this page.
- **G (SSRF), Q (upload):** **null** — read the full page; there is **no field the service dereferences** (no `*Url`/`*Uri`/webhook/import) and **no upload/blob** anywhere in the 5 scenarios. The only "fetches" are the customer's own network traffic between NICs (data plane, not a server-side fetch).
- **H (KMS), T (secret reachability), W (attestation):** N/A — no key/secret/attestation on this page.
- **P (proofing), J (OAuth), M (session), N (migration), DD (cache), BB (canonicalization), CC (upstream-context), EE (land-grab):** N/A — no registration gate, 3P link, session id, namespace migration, caching layer, multi-parser request path, upstream-asserted identity, or predictable global name on this page.
- **Y (transport):** N/A — control-plane SigV4 only; no `http://` endpoint or internal-hop cert claim on this page.
- **Doc gaps to settle live (carried for the hunter):**
  1. **S4-U1 central gap:** the enforcement layer of the cross-account multi-homing prohibition is undocumented — needs a 2-account canary (DryRun cannot answer).
  2. Whether a RAM-shared-subnet *participant* ENI (account Y) is nameable+attachable to the owner's (account X) instance in the same AZ — the practical path to S4-U1.
  3. Whether `sourceDestCheck=false` reliably rides along on ENI relocation (S5-AA1 scenario 2 chain).
  4. Whether VPC Flow Logs emit any signal distinguishing bridged-through-host traffic from host-originated (S4-V1 Lens-O detection gap).

---
*Cross-referenced siblings (owning plans — read before executing any pointer):* `using-eni-attack-research-plan.md` (lead #2 cross-VPC attach, #3 sourceDestCheck MITM), `network-interface-attachments-attack-research-plan.md` (Attach/Detach relocation, force-detach, no-EventBridge), `modify-network-interface-attributes-attack-research-plan.md` (value-key audit), `using-instance-addressing-attack-research-plan.md` (secondary-IP takeover + EIP ride-along), `instance-secondary-ip-addresses-attack-research-plan.md` (UnassignPrivate collateral EIP), `create-network-interface-attack-research-plan.md` (create-time attributes), `ec2-networking-attack-research-plan.md` (hub). See [[reference-aws-iam-service-auth-ref-url]].
```
