# Delete a Network Interface (`DeleteNetworkInterface`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete_eni.html` (offline twin `AWSEC2/latest/UserGuide/delete_eni.md` — **verified byte-identical online==offline 2026-10-15**), `API_DeleteNetworkInterface.html` (verified online 2026-10-15), and the IAM Service Authorization Reference `list_ec2.md` (read by offline grep; `DeleteNetworkInterface` @ L6088–6092). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

---

> **Relationship to siblings (READ FIRST — this is a COMPLEMENT, not a standalone).** `delete_eni.html` is the page-level how-to for the single mutating action `ec2:DeleteNetworkInterface`. It is a 2-sentence intro + console/CLI/PowerShell steps, and it is already cited as a lead-source by two existing plans, which remain **authoritative** for the surfaces they own — do NOT restate them:
> - **`requester-managed-eni-attack-research-plan.md`** OWNS the **AWS-service-plane delete-detached race** (its Area 2 / claim @122–125, **HARD STOP**): a customer with `ec2:DeleteNetworkInterface` racing a transiently-detached RDS/NAT/VPCE/resource-gateway ENI, and the fact that **no `requesterManaged` IAM condition key exists** so service-ENI deletes cannot be denied. That plan already cites this page's release sentence as its mechanism.
> - **`using-eni-attack-research-plan.md`** is authoritative for the ENI-resource lifecycle/grant surface (Create/Modify/Reset/Describe/`DeleteNetworkInterfacePermission`, the Describe oracles, requester-managed/managed hard-stop) and nominally lists `Delete` among them.
> - **`network-interface-attachments-attack-research-plan.md`** OWNS the **detach** action (`DetachNetworkInterface`, force-detach, relocation) — the *required precondition* this page links to (`network-interface-attachments.md#detach_eni`).
> - **`managing-network-interface-ip-addresses-attack-research-plan.md`** OWNS the one-ENI-identity-grant / generic-8-key / inert-ABAC framing across the ENI IP ops.
>
> **This plan owns ONLY what is net-new to the `DeleteNetworkInterface` action itself and not owned above:** (A1) the UserGuide-only **collateral EIP-disassociation + private-IP release** on whole-ENI delete, and its IAM-unscopability; (A2) the **managed-vs-requesterManaged delete-scopability asymmetry**; (A3) the **in-use/detached gate as a service-enforced, IAM-inexpressible precondition** and its *self-managed* (non-service-plane) race window; (A4) delete-side detection (Lens O); (A5) the cross-account-IDOR null + DryRun-not-an-oracle trap. See [[reference-aws-iam-service-auth-ref-url]].

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Settle every IAM-scopability question with `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` FIRST (no resource touched). Escalate to a live scoped call only with canary ENIs you provisioned.
- **`DryRunOperation` is caller-IAM-only, evaluated before resource resolution — it is NOT an ownership oracle.** `DeleteNetworkInterface` exposes `DryRun`; do not treat a `DryRunOperation` response as proof the delete would succeed against a given ENI.
- **HARD STOP:** the moment evidence shows the ENI is `requesterManaged=true` (RDS/NAT/VPCE/resource-gateway) or `Managed=true` with an AWS `Operator` (EKS Auto Mode) — i.e. the AWS service plane — stop, preserve evidence, flag for AWS-Security disclosure. Prove the non-deny of the *acceptance*; never complete a delete that damages a real service resource. The service-plane race itself is owned/developed by `requester-managed-eni` — route confirmations there.

## 1. Pentest Objectives
Concrete breach outcomes to pursue, in priority order:
1. **Strip an Elastic IP / private IPs off a victim resource via a path that bypasses the EIP-scoped controls** — delete the ENI the EIP rides on, using a principal that is denied/scoped on `DisassociateAddress` and `ReleaseAddress`, and observe the EIP disassociate and the private IPs return to the pool. (A1)
2. **Recycle a freed address into a cross-tenant pre-emption / dangling-DNS primitive** — show the released private IP (shared subnet) or disassociated EIP becomes grabbable by another principal. (A1 → chains to EIP cluster + `working-with-ip-addresses`)
3. **Prove `DeleteNetworkInterface` cannot be IAM-denied for service-managed ENIs** while it *can* for operator-managed ENIs (asymmetry). (A2 — service-plane half deferred to `requester-managed-eni`)
4. **Win the delete-detached race against a self-managed ENI mid-relocation** (failover automation window), not just a service ENI. (A3)

## 2. Components, Assets, and Design
- **Action:** `ec2:DeleteNetworkInterface`. **Interface:** EC2 query/SDK API (`DeleteNetworkInterface`), CLI `aws ec2 delete-network-interface`, PowerShell `Remove-EC2NetworkInterface`, console (Network Interfaces → Actions → Delete).
- **Request params (API ref, verified):** `NetworkInterfaceId` (String, **Required: Yes**), `DryRun` (Boolean, Required: No). **No other params.** Response: `requestId` + `return` (Boolean). **Errors: Common Error Types only** (no action-specific error enumerated — so no documented distinct "in-use" vs "not-found" vs "access-denied" error string; see A3/A5 oracle note).
- **Resource:** a **detached** ENI (`eni-<17 hex>`), identified by ARN `arn:aws:ec2:<region>:<acct>:network-interface/<id>`. ID entropy is high (17 hex) and non-fabricable → see A5.
- **Documented side effects (UserGuide, the net-new asset):** *"Deleting a network interface releases all attributes associated with the interface and releases any private IP addresses or Elastic IP addresses to be used by another instance."* — i.e. delete is a **collateral address-release** operation, not just an object delete.
- **Precondition:** *"You can't delete a network interface that is in use. First, you must detach the network interface."* The IAM action Description reinforces this: *"Grants permission to delete a **detached** network interface."* The "detached" state is a **server-side attachment-state check**, not an IAM condition (no `ec2:AttachmentId` / attachment-state key exists — confirmed 0-hit by the attachments sibling).

```
                        ec2:DeleteNetworkInterface (NetworkInterfaceId)
                                      │  (server-side: must be DETACHED)
          ┌───────────────────────────┼───────────────────────────────┐
          ▼                           ▼                                 ▼
  ENI object destroyed      private IPv4/IPv6 released          associated EIP disassociated
  (attributes released)     back to SUBNET pool  ──┐            (returns to account pool) ──┐
                                                   ▼                                        ▼
                                     cross-tenant pre-emption /              EIP re-association by another
                                     dangling-DNS reuse (shared subnet)      principal / released-EIP squat
                                     [working-with-ip-addresses A4]          [EIP cluster plans]
```

## 3. API / Interface Inventory
| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `DeleteNetworkInterface` | SDK/CLI/PS/console | Existing | **Mutating (destroy + collateral release)** | External | Delete a **detached** ENI; release its IPs/EIP | Yes (signed) | Any principal with `ec2:DeleteNetworkInterface` on the ENI (same account; `network-interface*` required) | DryRun available (IAM-only). No cross-account naming. |

**IAM row (verified `list_ec2.md` L6088–6092):**
- Description: "Grants permission to **delete a detached network interface**." Access level: **Write**.
- Resource type (**\*required**): `network-interface*`.
- Condition keys (the generic 8-key ENI set, nothing more): `aws:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:Subnet`, `ec2:Vpc`.
- **Absent and load-bearing (grep-confirmed 0 hits on this action / in corpus):** no `elastic-ip` resource row; no `ec2:AllocationId`, `ec2:PublicIpAddress`, `ec2:PrivateIpAddress`, `ec2:Ipv6Address`; no `requesterManaged`/`RequesterId` key (none exists anywhere); no attachment-state/`ec2:AttachmentId` key.

## 4. Recommended Areas of Focus

### Area 1 (HEADLINE) — Collateral EIP-disassociation + private-IP release is a whole-ENI, IAM-unscopable address-stripping primitive (Lens S/U/X/AA; also L/A chain)
**Background.** The UserGuide states delete "releases all attributes … and releases any private IP addresses or **Elastic IP addresses** to be used by another instance." So deleting the ENI an EIP is associated to **disassociates that EIP** and **frees the ENI's private IPv4/IPv6** back to the subnet pool. The `DeleteNetworkInterface` IAM row has **no `elastic-ip` resource type and no `ec2:AllocationId`/`ec2:PublicIpAddress`/`ec2:PrivateIpAddress`/`ec2:Ipv6Address` condition key** — only `network-interface*` identity + the generic 8 keys.

**Security Concern.** This is the **whole-ENI superset of the confirmed `UnassignPrivateIpAddresses → EIP collateral-disassociation` twin** owned by `instance-secondary-ip-addresses` (its Area 1): there, unassigning a secondary private IP also disassociates its EIP via an action with no `elastic-ip` row. Here, **deleting the whole ENI does the same for the primary + every secondary IP and every associated EIP at once.** `DisassociateAddress` (list_ec2 L7885–7889) and `ReleaseAddress` carry `ec2:AllocationId`/`ec2:PublicIpAddress` and are therefore scopable, but **a principal explicitly denied/scoped on `DisassociateAddress` and `ReleaseAddress` can still strip the EIP by deleting the ENI it rides on** — an EIP-control bypass identical in shape to the sibling, one trust-level up.
- **Two downstream effects:**
  - **(a) Availability/integrity collateral:** the service/instance behind that EIP loses its public address with one call; no EIP-scoped guardrail stops it.
  - **(b) Pool-recycling → cross-tenant pre-emption / dangling-DNS:** the freed private IP (in a **RAM-shared subnet**) becomes available for a co-tenant to grab (chains to `working-with-ip-addresses` Area 4 cross-tenant private-IP pre-emption and the ephemeral-pool/dangling-DNS reuse in `using-instance-addressing` Area 3); the disassociated EIP becomes re-associable (chains to the EIP-cluster released-EIP squatting leads).

**High-level Test Scenarios.**
- *Claim:* a role scoped so that `ec2:DisassociateAddress` and `ec2:ReleaseAddress` are **Denied** (or tag/AllocationId-scoped away) but `ec2:DeleteNetworkInterface` is **Allowed** on a target ENI can still disassociate that ENI's EIP. → *Oracle:* `iam:SimulateCustomPolicy` to show the deny on Disassociate/Release and allow on Delete; then on a **canary** ENI with a canary EIP, detach + delete and observe the EIP disassociate (`DescribeAddresses` shows it unassociated) and the private IPs released (`DescribeNetworkInterfaces` no longer lists them). → *Severity-if-true:* **Medium–High** (EIP-control bypass + availability); **High** if the recycled address is grabbed cross-tenant on a shared subnet.
- *Open doc-gap (settle first):* the exact **disposition of the EIP** — does delete only **disassociate** it (EIP remains allocated to the owner account, re-associable only by the owner) or does "to be used by another instance" imply it returns to a **public pool** (cross-account squattable)? The UG wording is ambiguous; `DescribeAddresses` on the canary after delete settles it. This decides whether effect (b) is intra-account recycling or a genuine cross-account squatting feeder.
- *Lens-U precision guard:* "releases … to be used by another instance" is the only doc sentence; nothing promises atomicity or ordering, and the **API ref does NOT repeat the release language at all** (UserGuide-only) → a hunter must confirm the behavior empirically, not from the API contract.

**Doc evidence:** `delete_eni.md` intro sentence; `list_ec2.md` L6088–6091 (no elastic-ip row / no IP-value keys); contrast L7885–7889 (`DisassociateAddress` has `ec2:AllocationId`/`ec2:PublicIpAddress`). **Severity-if-true:** Medium–High (High on shared subnet).

### Area 2 — managed-vs-requesterManaged delete-scopability asymmetry (Lens S/X)
**Background.** `DeleteNetworkInterface`'s condition keys include **`ec2:ManagedResourceOperator`** but **no `requesterManaged` key** (none exists in `list_ec2`).

**Security Concern.** The two "AWS put this ENI here" concepts diverge on this action:
- **Operator-managed** ENIs (EKS Auto Mode `Managed=true`, `Operator` set) → `ec2:ManagedResourceOperator` **can** be used to deny delete, so an admin *can* fence those.
- **Requester-managed** ENIs (RDS/NAT/VPCE/resource-gateway, `requesterManaged=true`) → **no key**, so `ec2:DeleteNetworkInterface` **cannot be denied only for service ENIs**; any broad network-admin role covers them. This is the IAM gap behind the service-plane delete-detached race.

**High-level Test Scenarios.**
- *Claim:* an admin can write a policy that denies deleting operator-managed ENIs but **cannot** write one that denies deleting requester-managed (RDS/NAT/VPCE) ENIs. → *Oracle:* `iam:SimulateCustomPolicy` with a `Deny` keyed on `ec2:ManagedResourceOperator` (effective) vs the absence of any `requesterManaged` key to key a Deny on (inert — no such key). → *Severity:* Informational–Medium as a scoping-gap finding; **the exploit half (racing a service ENI mid-detach) is owned/developed by `requester-managed-eni` Area 2 — route there, do not restate. HARD STOP on any service-plane ENI.**

**Doc evidence:** `list_ec2.md` L6091 (`ec2:ManagedResourceOperator` present); `requester-managed-eni-attack-research-plan.md` (no `requesterManaged` key, grep 0-hit). **Severity-if-true:** Informational–Medium (asymmetry); service-plane exploit = **High**, deferred.

### Area 3 — The "in-use / detached" gate is service-enforced and IAM-inexpressible; the delete-detached race generalizes to self-managed ENIs mid-relocation (Lens U/AA/L)
**Background.** Delete requires the ENI be **detached** — a **server-side attachment-state check** (UG + the IAM Description "delete a **detached** network interface"). There is **no attachment-state / `ec2:AttachmentId` condition key** (0-hit, per the attachments sibling), so this precondition **cannot be expressed, tightened, or relaxed in IAM**; it is purely a runtime state gate.

**Security Concern.** `requester-managed-eni` owns the race against a *service* ENI's transient detach. The net-new generalization here: **any ENI that is transiently detached by customer-owned automation** is race-deletable by a holder of `ec2:DeleteNetworkInterface`. The clearest case is the **failover/relocation automation** in `scenarios-enis` Scenario 5 (an ENI detached from a failed instance before re-attach to a standby) — a competing principal (or a buggy/over-broad automation role) that deletes the ENI in that window strands the standby and **collaterally releases the ENI's IPs/EIP** (Area 1), turning a transient failover into a permanent address loss + pool recycle. No IAM key gates on "is this ENI mid-relocation."

**High-level Test Scenarios.**
- *Claim:* during a self-managed detach→reattach window, `DeleteNetworkInterface` is accepted and the relocation automation is left referencing a destroyed ENI (+ its IPs/EIP freed). → *Oracle:* on a canary, detach an ENI and, before reattach, delete it; confirm acceptance and the Area-1 collateral release. → *Preconditions:* a principal holding `ec2:DeleteNetworkInterface` scoped by ENI-identity/tag only; a window where the ENI is detached. → *Severity:* **Medium–High** (availability + address loss); intra-account cross-team if the deleting role differs from the relocation role.
- *Enumeration sub-oracle (Lens A/O):* the API ref enumerates **no action-specific error** (Common Errors only), so test whether a delete attempt on a **still-attached** ENI returns a distinct error/latency vs a detached-but-foreign ENI vs a nonexistent ENI — a weak existence/state oracle. (Keep in mind cross-account naming is foreclosed — see A5.)

**Doc evidence:** `delete_eni.md` ("can't delete … in use. First, you must detach"); `list_ec2.md` L6089 Description; `scenarios-enis-attack-research-plan.md` S5 (relocation carries IPs/EIP/MAC/SG). **Severity-if-true:** Medium–High.

### Area 4 — Delete-side detection posture (Lens O)
**Background/Concern.** The native EC2 EventBridge event catalog (`automating_with_eventbridge.md`) has **no ENI create or delete event** (grep 0-hit; consistent with `create-network-interface` Area 7). So an ENI delete — and its collateral EIP/IP release — produces **no push signal**; only a CloudTrail **management event** (`DeleteNetworkInterface`, logged by default) records it. There is no purpose-built "your EIP was disassociated / your IP was released" event. Detection of Area 1's collateral effect relies on polling the unscopable `DescribeNetworkInterfaces`/`DescribeAddresses` (both blank-resource-type, `ec2:Region`-only). Note: in a shared VPC, a participant-created ENI is **participant-owned** and only the participant can delete it, so its `DeleteNetworkInterface` CloudTrail record lands in the **participant's** trail — the subnet owner (who can only Describe) gets no delete record in their own trail.
- *Severity:* **Low/Informational** (detection enabler; raises Area 1/3 severity by delaying discovery).

## 5. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| EIP stripped off victim via ENI delete despite Disassociate/Release deny | `DeleteNetworkInterface` collateral release | EIP actions scoped by `ec2:AllocationId`/`ec2:PublicIpAddress` — but **not inherited** by the Delete path (no elastic-ip row) |
| Freed private IP grabbed cross-tenant on shared subnet | released-IP → subnet pool | "available … to be used by another instance" — no documented cross-account cooldown/anti-targeting |
| Cannot deny delete on service ENIs | `ec2:DeleteNetworkInterface` scoping | `ec2:ManagedResourceOperator` (operator-managed only); **no `requesterManaged` key** |
| Delete-detached race on self-managed relocation ENI | detached-state gate | server-side attachment-state check; **no IAM attachment-state key** |

## 6. Out-of-Scope Risk Categories
- **The AWS-service-plane delete-detached race itself** — owned/developed by `requester-managed-eni` (HARD STOP; route confirmations there).
- Shared RDS/NAT-GW/PrivateLink service infrastructure internals.
- `DetachNetworkInterface` / force-detach mechanics — owned by `network-interface-attachments`.
- IP-reassignment/takeover primitives (`AssignPrivateIpAddresses … AllowReassignment`, EIP ride-along) — owned by `using-instance-addressing` / `instance-secondary-ip-addresses` / `working-with-ip-addresses`.
- Single-tenant self-DoS (deleting your own ENI).
- Customer-authored IAM footguns (no AWS-authored IAM artifact ships on this page).

## 7. Null hypotheses / doc gaps (pages checked)
- **Lens A (cross-account IDOR): NULL.** `DeleteNetworkInterface` requires `network-interface*` and takes only a `NetworkInterfaceId` the caller must own (same account); `eni-<17 hex>` IDs are non-fabricable; no body-vs-path dual-naming. Checked: `delete_eni.md`, `API_DeleteNetworkInterface.html`, `list_ec2.md` L6088–6091. The only cross-trust-boundary reach is the **service plane** (Area 2/3), deferred to `requester-managed-eni`.
- **DryRun oracle: NULL (false-positive trap).** `DryRun` is caller-IAM-only, pre-resource-resolution — not an ownership/state oracle.
- **Lens B/C/E (PassRole/vending/privesc): N/A** — no role ARN, STS, SLR, or vending on this action; runs under caller identity. Checked `API_DeleteNetworkInterface.html` (params: `NetworkInterfaceId`, `DryRun` only).
- **Lens G (SSRF): N/A** — no server-dereferenced URL field. **Lens Q (upload): N/A** — no blob. **Lens F/K: N/A** — no parser/LLM. **Lens H/T/W/Y/J/FF/N/BB/CC/DD/EE: N/A** — no KMS/secret/attestation/transport/token/namespace/cache/predictable-name surface on this single destroy action. **Lens R/S (IAM artifact): no policy JSON printed on this page** (the condition-key analysis in A1/A2 is Lens-S static reasoning over `list_ec2`, not an artifact audit).
- **Lens I (tagging): N/A on delete itself** (tags are read for ABAC scoping, not mutated); but note the `requester-managed-eni` plan's observation that unconditioned `CreateTags`/`DeleteTags` on an ENI could **self-widen** a tag-scoped Delete allow — cross-ref, don't restate.
- **Doc gaps to settle live (priority order):** (1) **EIP disposition on delete** — disassociate-and-retain vs release-to-pool (decides Area 1(b) cross-account severity); (2) whether released **private IPs** in a RAM-shared subnet are immediately grabbable by a co-tenant; (3) distinct error/latency on still-attached vs detached vs nonexistent ENI (Area 3 oracle); (4) whether the self-managed relocation race is practically winnable (window length).

---
*Verified 2026-10-15: `delete_eni.md` online==offline byte-identical; `API_DeleteNetworkInterface.html` fetched online (params `NetworkInterfaceId`+`DryRun`, Errors=Common only, no release language in API ref — UserGuide-only); `list_ec2.md` `DeleteNetworkInterface` @L6088–6092 (network-interface\* required; 8 generic keys incl. `ec2:ManagedResourceOperator`; no elastic-ip row / no IP-value / no requesterManaged key). Cross-refs: [[requester-managed-eni]] (service-plane race, authoritative), [[using-eni]], [[network-interface-attachments]] (detach precondition), [[instance-secondary-ip-addresses]] (UnassignPrivateIpAddresses→EIP twin), [[working-with-ip-addresses]] / [[using-instance-addressing]] (pool recycling / dangling-DNS), [[scenarios-enis]] (relocation window). See [[reference-aws-iam-service-auth-ref-url]].*
