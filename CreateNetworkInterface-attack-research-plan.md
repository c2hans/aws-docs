# EC2 CreateNetworkInterface — Attack Research Plan

Source of leads:
- API: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html (+ API_CreateNetworkInterfacePermission, API_NetworkInterface, API_OperatorRequest, API_ConnectionTrackingSpecificationRequest) — local mirror `/work/aws-docs/docs/AWSEC2/latest/APIReference/`.
- IAM: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (Service Authorization Reference for Amazon EC2).
- ENI User Guide: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html.

Status: **documentation-derived hypotheses only; nothing tested against a live account.** Produced with the `security-questionbuilder` skill (boundary-first lens catalog).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5). Look left and right for adjacent bugs.
- These are **IAM-policy-enforcement / tenant-isolation** hypotheses. The oracle is almost always: *provision a deliberately-scoped IAM role holding exactly the grant under test, then observe whether an action the policy author believes is denied is in fact allowed.* Use `iam:SimulateCustomPolicy` / `SimulatePrincipalPolicy` as the safe first oracle (no resources touched); escalate to a live scoped call only with synthetic/canary resources in an account you own.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. a `requesterManaged`/service-owned ENI, a service-linked identity, an ENI in an AWS-managed VPC), stop, preserve evidence, flag for AWS-Security disclosure. Do **not** attach to, mutate, or pivot through service-owned ENIs.

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Create an ENI that a scoping IAM policy intended to forbid** — wrong subnet/VPC, wrong IP, wrong security groups, or a privileged `InterfaceType` (`trunk`/`efa`) the policy author could not express a Deny for.
2. **ENI-attach hijack / cross-account leasing** — use `CreateNetworkInterfacePermission` to grant another account (or a service) `INSTANCE-ATTACH`/`EIP-ASSOCIATE` on an ENI, enabling a cross-account attach that the owning account's instance-side IAM never authorized.
3. **Spoof a service-managed ENI** — set the `Operator.Principal` / induce `requesterManaged=true` so the ENI masquerades as AWS-managed and evades customer tag/operator-based controls or detection.
4. **Tag-at-birth self-widening** — create the ENI with attacker-chosen tags to later pass `ec2:ResourceTag`-gated Attach/Modify/Delete ABAC.
5. **Default-SG fail-open** — create an ENI without supplying `SecurityGroupId.N` so the VPC default SG is attached, side-stepping a Deny written against specific security-group resources.
6. **IP squatting / collision inside a shared subnet** — pin `PrivateIpAddress`/prefixes to a victim's address or exhaust the subnet, with no condition key able to constrain the chosen IP.

---

## 2. Components, Assets, and Design

**What the action is.** `CreateNetworkInterface` creates an Elastic Network Interface (ENI) — a virtual NIC with its own MAC, one or more private IPv4/IPv6 addresses (or prefixes), a set of security groups, source/dest-check state, and connection-tracking timeouts — inside a **subnet** (required `SubnetId`). The ENI is an independently-addressable, independently-attachable identity object: once created it can be attached to an EC2 instance (`AttachNetworkInterface`), shared to another account (`CreateNetworkInterfacePermission`), or have an EIP associated. Detaching/re-attaching an ENI moves its IPs, MAC, and SGs — i.e. its network identity — onto a different instance.

**Request surface (the knobs that matter):**
- `SubnetId` **(required)** — placement; determines VPC + AZ.
- `SecurityGroupId.N` (optional) — firewall posture. **If omitted, the VPC default SG is attached.**
- `PrivateIpAddress`, `PrivateIpAddresses.N`, `SecondaryPrivateIpAddressCount`, `Ipv4Prefix.N`, `Ipv4PrefixCount`, `Ipv6Addresses.N`, `Ipv6AddressCount`, `Ipv6Prefix.N`, `Ipv6PrefixCount`, `EnablePrimaryIpv6` — fully attacker-choosable IP assignment.
- `InterfaceType` = `interface | efa | efa-only | trunk`. **`trunk`** is the ECS/branch-ENI multiplexing type; **`efa`** is the HPC kernel-bypass fabric adapter.
- `Operator` → `OperatorRequest.Principal` = *"The service provider that manages the resource."* Doc elsewhere labels `Operator` **"Reserved for internal use."**
- `ConnectionTrackingSpecification` — TCP/UDP idle timeouts (min/max bounds).
- `TagSpecification.N` — tags applied at creation.
- `ClientToken`, `DryRun`.

**Response / resource object (`NetworkInterface`):** `networkInterfaceId` (ARN `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}`, account-scoped), `ownerId`, `requesterId`, **`requesterManaged`** (managed-by-AWS flag), `operator`, `sourceDestCheck`, `denyAllIgwTraffic`, `status` (`available|associated|attaching|in-use|detaching`), and the full IP/SG/tag set. Note the **request** `InterfaceType` enum (4 values) is far narrower than the **response** `interfaceType` enum (~22 values incl. `nat_gateway`, `transit_gateway`, `vpc_endpoint`, `lambda`, `branch`, `*_managed`) — service-created ENIs carry types a customer cannot request.

**Ownership / zones.**
- **Customer account/VPC** owns self-created ENIs (`requesterManaged=false`).
- **AWS service plane** owns `requesterManaged=true` ENIs (created by ELB, NAT GW, RDS, Lambda, VPC endpoints, etc.) living in the customer VPC but managed by a service — the shared-responsibility line.
- **Another AWS account** can be granted attach/associate rights via `CreateNetworkInterfacePermission` (the cross-account seam).

```
            CreateNetworkInterface (SubnetId req; SG optional; IPs free; InterfaceType free; Operator free; tags)
                    │  creates
                    ▼
   ┌───────────────────────────────┐        CreateNetworkInterfacePermission (AwsAccountId | AwsService, INSTANCE-ATTACH|EIP-ASSOCIATE)
   │  ENI (eni-...) in subnet/VPC   │ ───────────────────────────────────────────────────────────────────────►  other AWS account / service
   │  MAC + IPs + SGs + tags        │
   │  requesterManaged? operator?   │
   └───────────────────────────────┘
                    │  AttachNetworkInterface (instance leg + ENI leg)      → instance inherits ENI's IPs/MAC/SGs (network identity move)
                    │  ModifyNetworkInterfaceAttribute                      → change SGs / sourceDestCheck / attachment
                    ▼
            attached to an EC2 instance  (traffic / identity surface)
```

---

## 3. API / Interface Inventory (ENI family)

| Name | Mutating | Access level | Req. resource legs | Key condition keys | Notes |
|---|---|---|---|---|---|
| **CreateNetworkInterface** | yes | Write | `network-interface*`, `subnet*`, `security-group` (NOT `*`) | NI leg: `aws:RequestTag`,`aws:TagKeys`,`ec2:NetworkInterfaceID`,`ec2:Region`. Subnet leg: `ec2:SubnetID`,`ec2:Vpc`,`ec2:AvailabilityZone(Id)`,`ec2:ResourceTag`. SG leg: `ec2:SecurityGroupID`,`ec2:Vpc`,`ec2:ResourceTag`. | **Target.** No key for `InterfaceType`, IPs, `Operator`, `AssociatePublicIpAddress`, connection-tracking. SG leg optional → fail-open. `ec2:NetworkInterfaceID` inert at create. |
| **CreateNetworkInterfacePermission** | yes | **Permissions management**, Write | `network-interface*` | `ec2:AuthorizedUser`, `ec2:AuthorizedService`, `ec2:Permission`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`,`ec2:Subnet`,`ec2:Vpc`,`ec2:ResourceTag` | Cross-account/ service attach-leasing primitive. `AwsService` param "Currently not supported" but accepted (console-hidden knob). |
| DeleteNetworkInterfacePermission | yes | Permissions management, Write | `network-interface` (NOT `*`) | `ec2:ManagedResourceOperator`,`ec2:NetworkInterfaceID`,`ec2:Subnet`,`ec2:Vpc`,`ec2:ResourceTag`,`ec2:AvailabilityZone` | Revoke side — no `ec2:AuthorizedUser`/`ec2:Permission` key (can't scope *which* grant you delete). |
| AttachNetworkInterface | yes | Write | `instance*`, `network-interface*` | instance: full instance key set incl. `ec2:InstanceProfile`,`ec2:Tenancy`. NI: `ec2:NetworkInterfaceID`,`ec2:Subnet`,`ec2:Vpc`,`ec2:ResourceTag`,`ec2:ManagedResourceOperator` | No key binding *which ENI* to *which instance* beyond per-resource scoping → attach any permitted ENI to any permitted instance. |
| DetachNetworkInterface | yes | Write | `instance*`, `network-interface*` | same families as Attach | — |
| ModifyNetworkInterfaceAttribute | yes | Write | `instance`, `network-interface*`, `security-group`, `subnet` | NI leg adds `ec2:Attribute`,`ec2:Attribute/${AttributeName}` | Can swap SGs / toggle sourceDestCheck post-create. |
| DescribeNetworkInterfaces / …Attribute / …Permissions | no | List/Read | — (region-only typically) | — | Enumeration surface. |

Undocumented / console-hidden knobs to probe: `Operator.Principal`, `AwsService` ("Currently not supported"), `InterfaceType=trunk`, `EnablePrimaryIpv6` (irreversible once set).

---

## 4–5. Recommended Areas of Focus (firing lenses, priority order)

### AREA 1 — [HIGH] `InterfaceType` has no condition key: `trunk`/`efa` creation is un-denyable (Lens S var-a, Lens X, Lens U)
**Background.** The request accepts `InterfaceType ∈ {interface, efa, efa-only, trunk}`. `trunk` ENIs underpin branch-ENI multiplexing (ECS `awsvpc` trunking — many branch ENIs/tenants behind one trunk); `efa`/`efa-only` are kernel-bypass HPC fabric adapters with distinct driver/placement semantics.
**Security Concern.** Grep of `list_ec2.md` returns **zero** occurrences of any `ec2:InterfaceType` condition key. There is therefore **no way to author an IAM policy that allows `CreateNetworkInterface` but denies `InterfaceType=trunk` (or `efa`)**. A role scoped to "create normal ENIs in subnet X" can silently create trunk/EFA interfaces, changing the networking/isolation primitives available (branch-ENI fan-out, EFA fabric reachability) inside that subnet.
**High-level Test Scenarios.**
- *Claim:* a policy `Allow ec2:CreateNetworkInterface on subnet-X` cannot be narrowed to exclude `trunk`. → *Oracle:* author the policy; `SimulateCustomPolicy` for the action with and without an `InterfaceType` condition — the condition key is unknown/ignored → simulation still ALLOWs. Confirm live by creating a `trunk` ENI under the scoped role.
- *Claim:* same for `efa`/`efa-only`.
**Doc evidence:** API_CreateNetworkInterface `InterfaceType` field; `list_ec2.md` CreateNetworkInterface row (no InterfaceType key). **Severity-if-true:** Medium–High (least-expressible-policy; enables branch-ENI/EFA primitives an operator believed blocked).

### AREA 2 — [HIGH] Cross-account / cross-service ENI attach-leasing via CreateNetworkInterfacePermission (Lens A, Lens AA, Lens B)
**Background.** `CreateNetworkInterfacePermission` *"Grants an AWS-authorized account permission to attach the specified network interface to an instance in their account"* — `AwsAccountId` + `Permission ∈ {INSTANCE-ATTACH, EIP-ASSOCIATE}`. It is access-level **Permissions management**. An `AwsService` param also exists, documented *"Currently not supported."*
**Security Concern.** This is a first-party cross-account grant. The action **does** expose scoping keys (`ec2:AuthorizedUser`, `ec2:AuthorizedService`, `ec2:Permission`) — but a default/typical `Allow ec2:CreateNetworkInterfacePermission on <eni>` with no condition lets the holder grant **any** account `INSTANCE-ATTACH`. Grantee validation (Lens AA): does the API verify the target `AwsAccountId` exists / is in-org, or accept an arbitrary 12-digit account (dangling-grant / typo-squat)? Revocation completeness: `DeleteNetworkInterfacePermission` **lacks** `ec2:AuthorizedUser`/`ec2:Permission` keys, so a policy can't scope *which* grant may be revoked, and the revoke leg's `network-interface` resource is not `*`-required.
**High-level Test Scenarios.**
- *Claim:* a holder of `CreateNetworkInterfacePermission` (no `ec2:AuthorizedUser` condition) can lease attach rights to an arbitrary external account. → *Oracle:* call with `AwsAccountId` = an account you control but that is unrelated/out-of-org; grantee account then `AttachNetworkInterface` succeeds. Breach = cross-account attach the owner's instance-side IAM never authorized.
- *Claim:* `AwsService` ("Currently not supported") is accepted by the control plane and sets `ec2:AuthorizedService` — can a service principal be named to make the ENI service-attachable? → *Oracle:* submit a service string; inspect `DescribeNetworkInterfacePermissions`/error.
- *Claim:* grantee account is not existence/ membership-validated. → *Oracle:* grant to a non-existent/foreign account id; observe acceptance.
**Doc evidence:** API_CreateNetworkInterfacePermission (AwsAccountId/AwsService/Permission); list_ec2.md rows for Create/DeleteNetworkInterfacePermission. **Severity-if-true:** cross-account attach = High (Critical if the ENI carries a privileged instance identity / reaches another tenant).

### AREA 3 — [HIGH] ENI = movable network identity; attach key-gap enables traffic/identity hijack (Lens X var B/E, Lens V)
**Background.** An ENI bundles IPs + MAC + SGs + source/dest-check. `AttachNetworkInterface` moves that bundle onto an instance. There is **no condition key that binds a specific ENI to a specific instance** — Attach scopes the ENI leg (`ec2:NetworkInterfaceID`/`Subnet`/`Vpc`/`ResourceTag`) and the instance leg independently.
**Security Concern.** A principal permitted to create an ENI (this action) and attach ENIs can: (a) place an ENI holding a *victim's* reserved private IP or an EIP-associated identity, then attach it to an attacker instance to intercept traffic destined to that IP; (b) create an ENI with permissive SGs and attach it to an instance to widen its reachability; (c) toggle `sourceDestCheck=false` (via Modify) to turn an instance into a traffic router/MITM. CreateNetworkInterface is the **supply step** of this chain.
**High-level Test Scenarios.**
- *Claim:* CreateNetworkInterface + AttachNetworkInterface lets an attacker move a chosen private IP / SG posture onto an instance of their choice within scope. → *Oracle:* create ENI pinned to a specific `PrivateIpAddress` in a shared subnet; attach to attacker instance; confirm traffic to that IP now lands on the attacker ENI.
- *Claim:* no key prevents attaching an ENI created in subnet A to an instance whose policy was only meant to use subnet B's ENIs. → *Oracle:* simulate/attach across the intended split.
**Doc evidence:** API_NetworkInterface (`sourceDestCheck`, IP/MAC/SG fields); list_ec2.md Attach/Detach/Modify rows. **Severity-if-true:** High (intra-account lateral/MITM; cross-tenant if subnet is shared).

### AREA 4 — [HIGH] Default-security-group fail-open: SG leg is NOT required (Lens S var-b, multi-resource fail-open)
**Background.** In `list_ec2.md`, CreateNetworkInterface's `security-group` resource leg is listed **without** the `*` (required) marker, unlike `network-interface*` and `subnet*`. The API makes `SecurityGroupId.N` optional; **omitting it attaches the VPC default security group.**
**Security Concern.** A Deny or scoping condition written against *security-group* resources (e.g. "only SG sg-approved may be used", or `ec2:ResourceTag` on SGs) is **inert when no SG is supplied** — the SG leg is simply not evaluated, and the default SG (often permissive / self-referential, sometimes widened by other principals) is silently attached. This is the recurring EC2 fail-open-scoping pattern.
**High-level Test Scenarios.**
- *Claim:* a policy that constrains which security groups an ENI may use is bypassed by omitting `SecurityGroupId.N`. → *Oracle:* under a role whose CreateNetworkInterface Allow is conditioned on `ec2:ResourceTag/approved` on the SG, create an ENI with **no** SG; if it succeeds (default SG attached) the SG constraint failed open.
- *Claim:* the default SG's posture is attacker-influenceable (AuthorizeSecurityGroupIngress on default SG). → chain to SG-ingress leads.
**Doc evidence:** list_ec2.md CreateNetworkInterface (security-group leg sans `*`); API field `SecurityGroupId.N Required: No`. **Severity-if-true:** Medium–High.

### AREA 5 — [HIGH] `Operator.Principal` / `requesterManaged` spoofing of a service-managed ENI (Lens U, Lens S var-b, Lens M)
**Background.** `OperatorRequest.Principal` = *"The service provider that manages the resource"*; the field group is *"Reserved for internal use."* The response object carries `operator` and `requesterManaged`. CreateNetworkInterface's condition-key list **does not include `ec2:ManagedResourceOperator`** even though sibling actions (Attach/Modify/Delete/CreateNetworkInterfacePermission) and the network-interface *resource type* do.
**Security Concern.** If the control plane accepts a customer-supplied `Operator.Principal` at create (the field is in the public request shape), the resulting ENI could be labelled as managed by a service provider — potentially (a) evading customer governance that keys on operator/`requesterManaged` to distinguish "our ENIs" from "AWS's", (b) evading detection/inventory tooling, or (c) causing downstream Modify/Delete/Permission calls — which *do* gate on `ec2:ManagedResourceOperator` — to mis-evaluate because the operator value was attacker-set at a step that had no such key. Governance guarantee ("operator identifies the managing service") traced to its enforcement mechanism (Lens U).
**High-level Test Scenarios.**
- *Claim:* a non-service caller can set `Operator.Principal` to an arbitrary string and it persists on the ENI. → *Oracle:* create with `Operator.Principal=<arbitrary>`; read back `operator`/`requesterManaged` via Describe.
- *Claim:* because CreateNetworkInterface lacks `ec2:ManagedResourceOperator`, a Deny intended to stop setting a managed operator is inert. → *Oracle:* SimulateCustomPolicy with a `ec2:ManagedResourceOperator` condition on Create — key ignored.
- *Claim:* a spoofed operator value changes how a later `ModifyNetworkInterfaceAttribute`/`DeleteNetworkInterfacePermission` ABAC-on-operator evaluates. → *Oracle:* set operator at create, then test the operator-gated sibling.
**Doc evidence:** API_OperatorRequest ("Reserved for internal use"); API_NetworkInterface `operator`/`requesterManaged`; list_ec2.md (Create lacks ManagedResourceOperator; siblings have it). **Severity-if-true:** Medium–High (governance/detection evasion; High if it reaches the service-plane — **HARD STOP if a real service identity is impersonated**).

### AREA 6 — [MEDIUM] No IP-value condition key: IP squatting / collision / subnet exhaustion (Lens S var-a, Lens L)
**Background.** Seven IP-assignment parameters are attacker-choosable; **no `ec2:Cidr`-equivalent or per-IP/prefix/count condition key exists** for CreateNetworkInterface.
**Security Concern.** A policy cannot restrict *which* private IPs, prefixes, or how many a principal assigns. In a shared/hijack-prone subnet this permits: pinning an ENI to a specific private IP to collide with / pre-claim a victim address; allocating `/28` IPv4 prefixes or large `SecondaryPrivateIpAddressCount` to exhaust the subnet (noisy-neighbor DoS); `EnablePrimaryIpv6` (irreversible) to pin a GUA.
**High-level Test Scenarios.**
- *Claim:* a scoped CreateNetworkInterface role can assign any private IP in the subnet, including one targeted for a victim resource. → *Oracle:* create ENI with `PrivateIpAddress=<target>`; observe success/collision behavior.
- *Claim:* prefix/count parameters allow subnet IP exhaustion. → *Oracle:* request large `Ipv4PrefixCount`/`SecondaryPrivateIpAddressCount`; measure free-IP depletion (own subnet only).
**Doc evidence:** API IP fields; list_ec2.md (no IP/cidr key). **Severity-if-true:** Medium (cross-tenant IP collision/DoS on a *shared* subnet = High).

### AREA 7 — [MEDIUM] Tag-at-birth self-widening into downstream ABAC (Lens I, Lens S)
**Background.** `TagSpecification.N` + `aws:RequestTag/${TagKey}`/`aws:TagKeys` on the NI leg let the creator set tags atomically at creation. Attach/Modify/Delete/Permission siblings all gate on `ec2:ResourceTag/${TagKey}`.
**Security Concern.** If the environment uses ABAC (`ec2:ResourceTag/team=X` to govern who may Attach/Modify an ENI), the creator can **self-assign the gating tag at birth**, pre-satisfying the downstream ABAC check — unless a matching `aws:RequestTag` Deny is present at create. Classic tag self-widen.
**High-level Test Scenarios.**
- *Claim:* create an ENI with `team=victim` tag and thereby gain Attach/Modify rights ABAC-scoped to that tag. → *Oracle:* SimulateCustomPolicy / live: create with the tag, then confirm the ABAC-gated sibling now allows.
- *Claim:* `aws:RequestTag`/`aws:TagKeys` are not enforced to prevent setting reserved/`aws:` keys at create. → *Oracle:* attempt reserved key tagging.
**Doc evidence:** API TagSpecification; list_ec2.md NI leg (RequestTag/TagKeys). **Severity-if-true:** Medium (High where ABAC *is* the access control).

### AREA 8 — [LOW] `ec2:NetworkInterfaceID` is inert at create; `DryRun` is not an ownership oracle (Lens S var-a, Lens A var)
**Background.** The NI leg lists `ec2:NetworkInterfaceID` — but the ENI ID is generated server-side **after** authorization, so a Deny/condition keyed on a specific `ec2:NetworkInterfaceID` cannot match at create time. `DryRun` is also present.
**Security Concern.** Operators may believe they scoped creation to specific ENI IDs; that condition is vacuous at create (only meaningful on post-create actions). `DryRun` reflects caller IAM only (pre-resource-resolution) and must **not** be used as an ownership/existence oracle.
**High-level Test Scenarios.**
- *Claim:* `ec2:NetworkInterfaceID` condition on CreateNetworkInterface never constrains creation. → *Oracle:* SimulateCustomPolicy with such a condition; creation still allowed regardless of value.
**Doc evidence:** list_ec2.md NI leg; API `DryRun`. **Severity-if-true:** Low (policy-author footgun / false sense of scoping).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Create `trunk`/`efa` ENI under a "normal ENI only" policy | InterfaceType param | (none — no `ec2:InterfaceType` key) |
| Lease attach rights to arbitrary external account | CreateNetworkInterfacePermission | `ec2:AuthorizedUser`/`ec2:AuthorizedService`/`ec2:Permission` (only if operator adds them) |
| Grant to non-existent / out-of-org account (dangling) | CreateNetworkInterfacePermission | grantee validation (unverified) |
| Scope-which-grant-to-revoke | DeleteNetworkInterfacePermission | (none — lacks AuthorizedUser/Permission keys) |
| ENI identity hijack via create+attach | AttachNetworkInterface | per-resource ec2:NetworkInterfaceID/Subnet/Vpc (no ENI↔instance binding) |
| Default-SG fail-open | SecurityGroupId.N optional / SG leg not required | ec2:SecurityGroupID/ResourceTag on SG (inert when SG omitted) |
| Operator/requesterManaged spoof | Operator.Principal | ec2:ManagedResourceOperator (absent on Create) |
| IP squat / subnet exhaustion | IP params | (none — no per-IP/cidr/count key) |
| Tag-at-birth ABAC self-widen | TagSpecification | aws:RequestTag/aws:TagKeys Deny at create (if present) |

---

## 7. Out-of-Scope Risk Categories
- Attacks requiring attachment to / mutation of an **AWS service-managed (`requesterManaged=true`) ENI** or an ENI in an AWS-owned VPC → **HARD STOP, disclose.** Do not pivot through the service plane.
- Customer-authored least-privilege footguns where the customer wrote the weak policy themselves (in scope only as advisory).
- IMDS / instance-internal attacks on fully-managed hosts.
- DNS rebinding against private-only endpoints; L2 sniffing claims unsupported by docs.
- Single-tenant self-DoS (subnet exhaustion in your own subnet) — Low/informational unless it degrades a *shared* subnet.

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF):** N/A — no field in CreateNetworkInterface/Permission is a URL/host the service dereferences (read API_CreateNetworkInterface, API_OperatorRequest, API_ConnectionTrackingSpecificationRequest — no `*Url`/`*Uri`/fetch field).
- **Lens K / Q (injection / upload):** N/A — no LLM, no blob/file upload, no parsed document (same pages checked).
- **Lens H / W (KMS / attestation):** N/A — no KMS key or attestation parameter on these actions.
- **Lens F (translation-layer):** N/A — Query/JSON API only; no customer-language translation layer on this action.
- **Doc gap — `Operator`:** "Reserved for internal use" but present in the public request shape; docs do not state whether the control plane *accepts* a customer-set value or silently drops it. Mark AREA 5 **"doc-gap — confirm acceptance first."**
- **Doc gap — `AwsService`:** documented "Currently not supported" yet accepted as a parameter; behavior on a supplied value is unspecified (AREA 2).
- **Doc gap — cross-AZ/subnet ENI reachability** in shared (RAM-shared) subnets: the ENI hijack blast radius across a shared subnet depends on VPC-sharing semantics not fully specified on these pages → confirm shared-subnet surface before AREA 3/6 cross-tenant claims.

---

### Kill-chain summary (rate at end-of-chain severity)
**ENI identity-hijack lease:** AREA 1 (create a `trunk`/permissive ENI, un-denyable type) **+** AREA 4 (omit SG → default SG) **+** AREA 6 (pin victim IP) **→** AREA 2 (`CreateNetworkInterfacePermission` lease to attacker account) **→** attacker `AttachNetworkInterface` in their own account → intercept traffic / inherit network identity destined for the pinned IP. End severity: **High → Critical** if the pinned IP/EIP or shared subnet crosses a tenant/account boundary.
