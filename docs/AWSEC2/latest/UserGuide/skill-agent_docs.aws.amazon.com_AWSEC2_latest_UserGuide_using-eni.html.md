# Elastic Network Interfaces (ENI) — Attack Research Plan

**Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html (+ child pages)
**Source of leads:** Offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` — `using-eni.md`, `create-network-interface.md`, `network-interface-attachments.md`, `modify-network-interface-attributes.md`, `managing-network-interface-ip-addresses.md`, `requester-managed-eni.md`, `scenarios-enis.md`, `ec2-prefix-eni.md`, `AvailableIpPerENI.md`, `delete_eni.md`; plus `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (IAM condition keys) and `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_*NetworkInterface*.md`. Cross-check against the live pages (`.html` / `.md`) before executing — the offline mirror can be stale.
**Status:** Documentation-derived hypotheses only. Nothing has been tested against a live account. Method: `security-questionbuilder`.
**Date:** 2026-09-13.

---

## 0. How to use this document

- Each lead is stated as **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity → Stop condition.** Work in priority order (Section 5); look left and right for adjacent bugs.
- **HARD STOP:** an ENI is a *customer VPC resource* — the whole surface sits inside the customer's own account/VPC except for the one deliberate cross-account primitive (`CreateNetworkInterfacePermission`, §5 Area 1) and `RequesterManaged` ENIs created by AWS services. The moment evidence shows an identity / credential / ARN / account belonging to **AWS's own service plane** (e.g. reaching a requester-managed ENI's backing service, or the ENI fleet's control plane), stop, preserve evidence, and flag for AWS-Security disclosure.
- **Prime scope discipline for this service:** most cross-*tenant* lenses (A cross-account, D control-plane, V shared-fleet) are *null or out-of-scope* here because there is no multi-tenant service fleet in the ENI data path — the ENI lives in the customer VPC. The real yield is in **IAM enforceability gaps** (Lens U / S / X), the **cross-account attach grant** (Lens AA / B), and **cross-VPC / source-dest-check network-boundary defeats** (Lens V / U) that are *customer-account* lateral-movement and defense-evasion primitives, plus AWS-authored-artifact audits (Lens R). Rate honestly: an intra-account footgun the customer inflicts on themselves is Low; an AWS-owned enforceability gap (no condition key exists to express a documented guarantee) is a reportable Tier-2 hardening defect.

---

## 1. Pentest Objectives

Concrete boundary-breach outcomes a hunter should try to produce:

1. **Cross-account ENI attach without a valid grant / with a stale grant** — attach an ENI you own into another account's instance (or vice-versa) where `CreateNetworkInterfacePermission` was never issued, or *after* `DeleteNetworkInterfacePermission` should have revoked it. (Lens AA / B)
2. **Enforceability gap: disable Source/Destination check under a policy meant to forbid it** — prove there is *no IAM condition key* that scopes the *value* of `SourceDestCheck`, so a role allowed to `ModifyNetworkInterfaceAttribute` at all can turn the instance into a NAT/router/interceptor and reach the IMDS (`169.254.169.254`) from outside the VPC. (Lens U / S / D-adjacent)
3. **`ec2:Attribute` case-sensitivity / multiplex fail-open** on `ModifyNetworkInterfaceAttribute` — a Deny keyed on a lowercase/mis-cased attribute name is inert, letting a caller change `groups`, `sourceDestCheck`, `deleteOnTermination`, or `description` that the policy author believed were locked. (Lens S variant, corpus-confirmed for `ec2:Attribute`)
4. **Cross-VPC network bridging inside one account** — attach an ENI from VPC-A to an instance in VPC-B (documented feature) and prove there is *no condition key* binding the instance's VPC to the ENI's VPC, defeating VPC isolation / CIDR-overlap segmentation without peering. (Lens V / U)
5. **Rogue-ENI disguise / requester-managed impersonation** — set an attacker-controlled `Description` (e.g. `"VPC Endpoint Interface vpce-0..."`) on a customer-created ENI to masquerade as an AWS-service (requester-managed) ENI and evade responder triage; test whether `RequesterManaged`/`RequesterId` are forgeable. (Lens O / M / U)
6. **Grant-target validation & undocumented knob** — does `CreateNetworkInterfacePermission` accept a nonexistent/foreign `AwsAccountId`, or the doc-flagged-"currently not supported" `AwsService` value? (Lens P / Step-3 hidden knob)
7. **Prefix manual-assignment race** — defeat the "AWS verifies the prefix is not already assigned" uniqueness gate via a TOCTOU race between two `AssignPrivateIpAddresses`/prefix assignments. (Lens P / L)
8. **AWS-authored IAM-artifact audit** — resolve any AWS-managed policy / sample policy the ENI docs reference and audit for over-broad ENI grants (`Resource:"*"`, unconditioned `ModifyNetworkInterfaceAttribute`/`AttachNetworkInterface`). (Lens R)

---

## 2. Components, Assets, and Design

**What it is.** An *elastic network interface (ENI / "network interface")* is a logical virtual NIC that lives in a VPC subnet and can be attached to / detached from EC2 instances **in the same Availability Zone**. Its attributes travel with it: primary + secondary private IPv4, primary + secondary IPv6, one EIP per private IPv4, one public IPv4, **security groups**, a **MAC address**, a **source/destination-check flag**, a description, and a delete-on-termination flag.

**Customer-facing interface.** EC2 Query/JSON API (SigV4), AWS CLI (`aws ec2 …`), PowerShell cmdlets, and the EC2 console (`Network & Security → Network Interfaces`). No non-SDK/wire protocol here — this is a pure control-plane resource. The *data plane* is ordinary VPC packet forwarding, governed by security groups / NACLs / route tables (out of this page's scope, but the ENI's SG membership is set here).

**Resource identifiers.**
- `eni-<17 hex>` — network interface id.
- `eni-attach-<17 hex>` — **attachment** id (note: `DetachNetworkInterface` and delete-on-termination modification key on the *attachment* id, not the eni id — a two-names-for-one-relationship shape, Lens A).
- Interface types: `ENA` (default), `EFA with ENA`, `EFA-only` (no IP addresses; can't be primary), plus `interface` / `vpc_endpoint` / `trunk` / `branch` for managed/requester types.
- `NetworkCardIndex` (0..N; primary must be card 0), `DeviceIndex`.

**Ownership / accounts.**
- **Customer account + VPC** owns the ENI, its subnet, its SGs. This is where 95% of the surface lives.
- **AWS service accounts** own *requester-managed ENIs* — created *in the customer's VPC on the customer's behalf* by RDS, NAT Gateway, PrivateLink/interface-endpoint, ELB, Lambda, WorkSpaces, EKS Auto Mode ("managed network interface"), etc. The customer can view + tag but **cannot** modify/attach/detach/associate-EIP/assign-IP or specify it at launch (can still `Reset…Attribute`). Identified by `RequesterManaged=true`, `RequesterId` (service alias / account id), and a service-supplied `Description`.
- **A second AWS account** can be granted `INSTANCE-ATTACH` or `EIP-ASSOCIATE` permission on a *specific* ENI via `CreateNetworkInterfacePermission` — the only first-class cross-account primitive on this surface.

**Where untrusted / caller-controlled data enters.** ENI `Description` (free text, later rendered in console + returned by `Describe*` — evasion/impersonation vector), tag keys/values, the `AwsAccountId`/`AwsService`/`Permission` grant inputs, manually-specified private IP / IPv6 / prefix CIDR values (verified for uniqueness by AWS), and SG-id lists on create/modify.

**Documented security guarantees to turn back on the docs (Lens U seeds):**
- *"You can't detach a **primary** network interface."*
- *"You **can't** create multi-homed instances across VPCs in **different AWS accounts**."* (scenarios-enis) — tension vs `CreateNetworkInterfacePermission INSTANCE-ATTACH` which grants a cross-account attach.
- *"Source/destination checks are enabled by default… You must disable [them] if the instance runs NAT, routing, or firewalls."* (the disable primitive) + IMDS doc: disabling src/dest check on a Nitro instance lets a network appliance forward packets to `169.254.169.254` — an IMDS-reach-from-outside-the-VPC enabler.
- *"AWS verifies that the prefix is not already assigned to other resources before assigning it"* (manual prefix — a uniqueness/verification gate).
- *"You can't manage [requester-managed] network interfaces yourself."*

**ASCII — ownership & the seams that matter**

```
        Customer Account A (VPC-A)                 Customer Account A (VPC-B, same acct)
   ┌──────────────────────────────┐            ┌──────────────────────────────┐
   │  ENI (SGs, MAC, IPs, EIP)     │  Attach    │  Instance i-B                │
   │  source/dest-check flag ──────┼──(same AZ)─┼─▶ *cross-VPC bridge*          │  ← Lens V/U (#4)
   └───────────┬──────────────────┘            └──────────────────────────────┘
               │ ModifyNetworkInterfaceAttribute (multiplexed: groups /        ← Lens S/X (#2,#3)
               │   sourceDestCheck / deleteOnTermination / description / ...)
               ▼
   ┌──────────────────────────────┐   CreateNetworkInterfacePermission
   │  RequesterManaged ENI         │   (INSTANCE-ATTACH | EIP-ASSOCIATE)
   │  (RDS / NATGW / VPCE / ELB /  │            │  AwsAccountId = 2222...
   │   Lambda / EKS AutoMode)      │            ▼
   │  RequesterId, Description ─────┼──▶ evasion  Account B  ── attach A's ENI into B's instance  ← Lens AA/B (#1)
   └──────────────────────────────┘   (Lens O/M/U #5)                                (revoke completeness)
                                             ▲
                            AWS service plane (backing service of the requester-managed ENI)  ── HARD STOP
```

---

## 3. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (what proves it broke) |
|---|---|---|---|---|
| B1 | Account A caller | Account B's instance | `CreateNetworkInterfacePermission INSTANCE-ATTACH` → cross-account attach | An ENI attached across accounts **without** a live, matching permission grant, or **after** its `DeleteNetworkInterfacePermission` — i.e. a cross-account attach the grant model says is impossible. |
| B2 | Role scoped "may modify ENI attrs but must not weaken network posture" | The ENI's `SourceDestCheck` / `groups` | `ModifyNetworkInterfaceAttribute` (multiplexed) | The scoped role **disables source/dest check** or **swaps in a permissive SG** despite a policy the author believed prevented it → routing/NAT/interception + IMDS reach. No `ec2:`*value* key exists to deny it. |
| B3 | Instance in VPC-B | Network in VPC-A (same account) | `AttachNetworkInterface` of a VPC-A ENI to a VPC-B instance | Packets flow between two VPCs that were never peered; no condition key binds instance-VPC == eni-VPC → VPC segmentation defeated intra-account. |
| B4 | Incident responder / detection | A rogue attacker ENI | Attacker sets `Description` mimicking a service ENI | An ENI that a responder classifies as AWS-managed (by description) but is attacker-owned; or `RequesterManaged`/`RequesterId` proven forgeable. |
| B5 | Customer caller | An AWS-service-plane resource behind a requester-managed ENI | Reset/attach/route manipulation of a requester-managed ENI | Any packet/response from the backing service plane reached via the requester-managed ENI = **HARD STOP** disclosure. |
| B6 | Two concurrent callers (same account) | Same subnet prefix / IP | `AssignPrivateIpAddresses` / prefix manual assign race | Two ENIs each accept the *same* private IPv4/prefix the "verify not already assigned" gate should have made unique. |

---

## 4. API / Interface Inventory

Condition keys below are **verbatim from `list_ec2.md`** (Service Authorization Reference). Absences are the leads.

| Name | Method | Mut. | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes / condition keys |
|---|---|---|---|---|---|---|---|
| `CreateNetworkInterface` | Query | Yes | Yes | Create ENI in a subnet, with SGs/IPs/prefixes/interface-type | Yes | IAM principals w/ action | Resources: `network-interface*` (`aws:RequestTag`,`aws:TagKeys`,`ec2:NetworkInterfaceID`,`ec2:Region`), `security-group` (`ec2:Vpc`,`ec2:SecurityGroupID`,tag), `subnet*` (`ec2:Vpc`,`ec2:SubnetID`,AZ,tag). **No key for interface-type value** (Lens S "key that doesn't exist"). |
| `AttachNetworkInterface` | Query | Yes | Yes | Attach ENI to instance (hot/warm/cold); pick `NetworkCardIndex`/`DeviceIndex`; `EnaSrdSpecification`,`EnaQueueCount` | Yes | IAM principals | Resources: `instance*` (tag,AZ,type,profile,metadata… — **no `ec2:Vpc`**), `network-interface*` (`ec2:Subnet`,`ec2:Vpc`,`ec2:NetworkInterfaceID`,AZ,tag). **No key links instance-VPC to eni-VPC → cross-VPC attach unscopable (B3).** |
| `DetachNetworkInterface` | Query | Yes | Yes | Detach by `attachment-id`; `Force` flag | Yes | IAM principals | Keys on the ENI. `Force` detach: docs warn it can leave instance metadata not reflecting the detach until restart (Lens O state/audit confusion). Detaching a *service-attached* ENI → "no permission to access the resource". |
| `ModifyNetworkInterfaceAttribute` | Query | Yes | Yes | **Multiplexed**: `Groups`, `SourceDestCheck`, `Attachment.DeleteOnTermination`, `Description`, `EnaSrdSpecification`, `ConnectionTrackingSpecification`, `EnablePrimaryIpv6`, `AssociatePublicIpAddress` (one at a time) | Yes | IAM principals | **`ec2:Attribute` + `ec2:Attribute/${AttributeName}`** on `network-interface*` (Lens S case fail-open); `security-group` resource (`ec2:Vpc`,`ec2:SecurityGroupID`). **No value-level key for `SourceDestCheck` (B2).** Prime Lens S/X/U target. |
| `ResetNetworkInterfaceAttribute` | Query | Yes | Yes | Reset attribute to default (allowed even on requester-managed ENIs) | Yes | IAM principals | Requester-managed ENIs: modify denied but **reset allowed** — asymmetry to probe. |
| `CreateNetworkInterfacePermission` | Query | Yes | Yes | **Grant another AWS account** `INSTANCE-ATTACH`/`EIP-ASSOCIATE` on a specific ENI | Yes | IAM principals (**Permissions-management** access level) | Inputs: `AwsAccountId`, `AwsService` (*"Currently not supported"* — undocumented/rejected knob to probe), `Permission ∈ {INSTANCE-ATTACH, EIP-ASSOCIATE}`. Keys: `ec2:AuthorizedUser`,`ec2:AuthorizedService`,`ec2:Permission`. **Only cross-account primitive (B1).** |
| `DeleteNetworkInterfacePermission` | Query | Yes | Yes | Revoke a permission grant; `Force` flag | Yes | IAM principals | Revoke-completeness target (Lens AA): does it sever an ENI *already attached* cross-account? |
| `DescribeNetworkInterfacePermissions` | Query | No | Yes | List grants | Yes | IAM principals | Enumeration of who-can-attach-what. |
| `AssignPrivateIpAddresses` / `UnassignPrivateIpAddresses` | Query | Yes | Yes | Add/remove secondary private IPv4 / prefixes; `AllowReassignment` | Yes | IAM principals | Keys: `ec2:Subnet`,`ec2:Vpc`,`ec2:NetworkInterfaceID`,tag. **No key on the IP/prefix value.** `AllowReassignment` = steal a secondary IP from another ENI (B6 adjacent). |
| `AssignIpv6Addresses` / `UnassignIpv6Addresses` | Query | Yes | Yes | Add/remove IPv6 / IPv6 prefixes | Yes | IAM principals | Same shape as IPv4. Primary IPv6 (`EnablePrimaryIpv6`) is **irreversible** once set. |
| `AssociateAddress` / `DisassociateAddress` | Query | Yes | Yes | Bind/unbind EIP to ENI/instance | Yes | IAM principals | Ties to existing **EIP-addresses** plans in memory (recover-by-value, transfer-accept). `elastic-ip` keys: `ec2:AllocationId`,`ec2:PublicIpAddress`,`ec2:Domain`. |
| `DeleteNetworkInterface` | Query | Yes | Yes | Delete a detached ENI; releases IPs/EIPs | Yes | IAM principals | Can delete an AWS-service ENI *if* the service detached-but-didn't-delete it → cleanup-race / dangling-resource. |
| `DescribeNetworkInterfaces` | Query | No | Yes | List/inspect ENIs incl. `requester-managed` filter, `Description`, `RequesterId` | Yes | IAM principals | Read oracle for B4 disguise + inventory. |

**Undocumented / console-hidden knobs to enumerate (Step-3 discipline):** `AwsService` on `CreateNetworkInterfacePermission` (API accepts, docs say unsupported — what does the control plane actually do?); `EnaSrdSpecification` / `EnaQueueCount` on attach/modify (perf knobs, low sec value but under-tested); `AllowReassignment` on `AssignPrivateIpAddresses`; `Force` on detach/delete-permission; `AssociatePublicIpAddress` as a *modify* attribute (not just launch-time). Diff the API/SDK model against the console-exposed set and treat the delta as leads.

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Cross-account ENI-attach grant: target validation & revocation completeness  ⭐ (Lens AA / B / P)
**Background.** `CreateNetworkInterfacePermission` "grants an AWS-authorized **account** permission to attach the specified network interface to an instance **in their account**" — `AwsAccountId` + `Permission ∈ {INSTANCE-ATTACH, EIP-ASSOCIATE}`. This is the *only* documented cross-account primitive on the ENI surface, and it directly contradicts the scenarios-enis guarantee that "you can't create multi-homed instances across VPCs in **different AWS accounts**."
**Security Concern.** Grant creation is a Write + **Permissions-management** action whose grantee is a caller-supplied account id. Revocation is a *separate* API (`DeleteNetworkInterfacePermission`), which is the classic grant-checked-at-grant-time / revoke-side-unchecked shape (Lens AA).
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* `CreateNetworkInterfacePermission` accepts a **nonexistent or unrelated `AwsAccountId`** with no existence/opt-in check. → *Oracle:* grant to a canary/never-consented account id returns success and appears in `DescribeNetworkInterfacePermissions`. → Sev: Low alone (grantee must still act), but a griefing / pre-positioning primitive.
- *Claim:* After `DeleteNetworkInterfacePermission`, an ENI **already attached** cross-account (or an in-flight `AttachNetworkInterface`) **survives** — revoke does not sever the live attachment. → *Oracle:* attach under a grant, revoke, confirm the attachment (and its packet flow / EIP association) persists. → Sev: **High** (surviving cross-account reach after revoke).
- *Claim:* The doc-flagged `AwsService` value ("Currently not supported") is **silently accepted** by the control plane and grants a service-principal attach right the console never surfaces. → *Oracle:* call with `AwsService=<some>.amazonaws.com`; compare `DryRunOperation` vs a real call's error/accept. → Sev: Medium (hidden knob / confused-deputy enabler).
- *Claim:* `ec2:AuthorizedUser` / `ec2:AuthorizedService` / `ec2:Permission` condition keys **do not actually constrain** the grant (key ignored / wrong binding). → *Oracle:* under a role Denied unless `ec2:AuthorizedUser` = self, issue a grant to a different account and see it succeed. → Sev: Medium–High.
- **Kill-chain:** cross-account attach of *your* ENI (carrying your SGs + EIP) into *their* instance, or *their* ENI into *your* instance, is a bidirectional network-bridge / data-exfil path across the account boundary. Rate at the end of the chain.
**Doc evidence:** `API_CreateNetworkInterfacePermission.md` (AwsAccountId / AwsService / Permission), `list_ec2.md` line ~5339 (Permissions-management, `ec2:AuthorizedUser/Service/Permission`), `scenarios-enis.md` (cross-account multi-homing "can't"). **Severity-if-true:** High.
**Stop condition:** if attach reaches an AWS-service-owned instance/account → HARD STOP.

### Area 2 — Source/Destination-check disable has no value-level IAM lever  ⭐ (Lens U / S)
**Background.** Source/dest check is on by default and "ensures the instance is either the source or destination of any traffic it receives"; disabling it is *required* for NAT/routing/firewall instances. The IMDS-access doc explicitly warns that on Nitro instances, disabling src/dest check lets a VPC network appliance forward packets to the IMDS (`169.254.169.254`), i.e. reach instance credentials from outside the VPC.
**Security Concern.** `SourceDestCheck` is set via `ModifyNetworkInterfaceAttribute`. The Service Authorization Reference exposes `ec2:Attribute` / `ec2:Attribute/${AttributeName}` (which attribute) but **no condition key on the *value*** (`true`/`false`). So a policy can allow or forbid *touching* the attribute, but **cannot express "may modify the ENI but must never set SourceDestCheck=false."**
**High-level Test Scenarios:**
- *Claim:* There is no IAM mechanism to prevent disabling src/dest check while still permitting other ENI attribute edits → the documented default-on protection is **advisory, not enforceable**. → *Oracle:* enumerate every `ec2:` key on `ModifyNetworkInterfaceAttribute`/`network-interface` in `list_ec2.md`; confirm none binds the src/dest boolean; then under a role granted the action, set `SourceDestCheck.Value=false` and observe success. → Sev: **Medium (High as an enabler)** — turns an instance into a router/interceptor + IMDS-from-outside-VPC.
- *Claim:* `ec2:Attribute` **case-sensitivity fail-open** — a Deny written as `ec2:Attribute: "sourceDestCheck"` (or `groups`) is inert if the request populates the key with a different casing than the author assumed. → *Oracle:* replicate the corpus-confirmed `ec2:Attribute` casing test (see instance-resize / stop-start plans): craft a Deny on one casing, send the other, observe fail-open. → Sev: Medium–High.
**Doc evidence:** `using-eni.md` ("Source/destination checking"), `instance-metadata-limiting-access.md` (IMDS + src/dest check), `list_ec2.md` line ~8941 (`ec2:Attribute` present, no value key). **Severity-if-true:** Medium–High (AWS-owned enforceability gap → reportable Tier-2).

### Area 3 — `ModifyNetworkInterfaceAttribute` multiplex: SG swap & delete-on-termination  (Lens S / X / A)
**Background.** One multiplexed action mutates `Groups`, `Description`, `Attachment.DeleteOnTermination`, `EnablePrimaryIpv6`, `AssociatePublicIpAddress`, connection-tracking, ENA-SRD. "You can use this action to attach and detach security groups from an existing EC2 instance." Delete-on-termination is keyed on the **attachment id**, not the eni id.
**Security Concern.** Changing SGs replaces the *entire* set ("new set replaces the current set") — a single call can strip all inbound restrictions or add a permissive SG. The `security-group` resource type *is* scopable (`ec2:Vpc`, `ec2:SecurityGroupID`, tag) — but only if the operator writes those conditions; by default any SG in the VPC is attachable.
**High-level Test Scenarios:**
- *Claim:* A role allowed `ModifyNetworkInterfaceAttribute` with no `security-group`-scoped condition can attach an over-permissive SG (e.g. `0.0.0.0/0:22`) to any ENI it can name, bypassing intended network posture. → *Oracle:* modify groups to a permissive SG under a scoped role; confirm accept. → Sev: Medium (intra-account footgun unless the SG condition was the control).
- *Claim:* Toggling `DeleteOnTermination` via `Attachment.AttachmentId` lets a caller who can name the *attachment* (but perhaps not the eni by tag) flip data-remanence/teardown behavior — a two-names-for-one-resource authz gap. → *Oracle:* compare whether ENI-id tag conditions gate the attachment-id-keyed modify. → Sev: Low–Medium.
- *Claim:* `AssociatePublicIpAddress` / `EnablePrimaryIpv6` as *modify* attributes expose launch-only behaviors post-launch with weaker scoping. → *Oracle:* enumerate which of these are gated by any condition key. → Sev: Low.
**Doc evidence:** `API_ModifyNetworkInterfaceAttribute.md`, `modify-network-interface-attributes.md`, `list_ec2.md` line ~8941. **Severity-if-true:** Medium.

### Area 4 — Cross-VPC attach defeats VPC segmentation intra-account  (Lens V / U)
**Background.** "The network interface can reside in the same VPC as your instance **or in a different VPC that you own**, as long as [same AZ]. This enables you to create multi-homed instances across VPCs with different networking and security configurations." Documented use cases: "overcome CIDR overlaps between two VPCs that can't be peered" and "connect multiple VPCs within a single account."
**Security Concern.** This is a *feature*, but it is also a lateral-movement / segmentation-defeat primitive: an instance in a locked-down VPC-B can be bridged to a sensitive VPC-A without peering, TGW, or a route-table change — invisibly to network-topology-based controls. `AttachNetworkInterface`'s `instance` resource type carries **no `ec2:Vpc` condition key**, and nothing binds instance-VPC to eni-VPC, so a customer *cannot* write "only attach ENIs from the same VPC as the instance."
**High-level Test Scenarios:**
- *Claim:* No IAM condition key can restrict cross-VPC attach → the segmentation boundary is unenforceable via IAM. → *Oracle:* enumerate `AttachNetworkInterface` keys (confirmed: `instance*` has no `ec2:Vpc`); attempt an SCP/identity policy expressing "same-VPC only" and show it can't be written. → Sev: Medium (AWS-owned enforceability gap).
- *Claim:* Cross-VPC attach silently *works* even when the two VPCs have overlapping CIDRs / conflicting NACLs, producing asymmetric-routing or a covert channel. → *Oracle:* attach and test bidirectional reachability across the two VPCs. → Sev: Medium.
- **Boundary check:** confirm the "**different AWS accounts** = not allowed" guarantee actually holds at the API (attempt an attach of an ENI whose VPC is in another account without a permission grant → expect refuse). If it *doesn't* hold, that escalates to Area 1 / **High**.
**Doc evidence:** `network-interface-attachments.md` (console step "different VPC that you own"), `scenarios-enis.md` (cross-VPC use cases + cross-account "can't"), `list_ec2.md` line ~4834. **Severity-if-true:** Medium (intra-account); High if the cross-account guard fails.

### Area 5 — Rogue-ENI disguise / requester-managed impersonation  (Lens O / M / U)
**Background.** Requester-managed ENIs are identified in the console/`Describe*` by `RequesterManaged=true`, a `RequesterId`, and a service-supplied `Description` like `"VPC Endpoint Interface vpce-089f..."`. The customer sets `Description` on their *own* ENIs freely.
**Security Concern.** A responder or automated control that trusts `Description` (or a naive "looks like a VPC endpoint" heuristic) can be fooled by an attacker-created ENI wearing a service-like description — an evasion/persistence disguise. The real question is whether the trustworthy markers (`RequesterManaged`, `RequesterId`) are attacker-forgeable.
**High-level Test Scenarios:**
- *Claim:* `Description` on a customer ENI can be set to an arbitrary service-mimicking string and is returned verbatim by `DescribeNetworkInterfaces` → disguise. → *Oracle:* create ENI with `Description="VPC Endpoint Interface vpce-0deadbeef"`; confirm it renders identically to a real one in list views. → Sev: Low (evasion; raises severity as an enabler).
- *Claim:* `RequesterManaged`/`RequesterId` are **server-set and NOT forgeable** by the customer (expected null hypothesis) — confirm this so responders can rely on them, not on `Description`. → *Oracle:* attempt to set `RequesterManaged=true` / a foreign `RequesterId` at create/modify; expect rejection/ignore. → Sev: refuting = Informational; if forgeable = High.
- *Claim (Lens O):* `Force` detach leaving instance metadata not reflecting the detach until restart creates a detection blind spot. → *Oracle:* force-detach, read IMDS/console attachment state, look for divergence window. → Sev: Low–Informational.
**Doc evidence:** `requester-managed-eni.md` (Description/RequesterId/RequesterManaged fields), `network-interface-attachments.md` (Force detach warning). **Severity-if-true:** Low (evasion enabler); High only if markers are forgeable.

### Area 6 — Prefix / secondary-IP uniqueness gate & reassignment  (Lens P / L / A)
**Background.** Manual prefix assignment: "AWS **verifies that the prefix is not already assigned** to other resources before assigning it." IPv4 prefix `/28`, IPv6 `/80`, must be within the subnet CIDR and not overlap. `AssignPrivateIpAddresses` has an `AllowReassignment` flag.
**Security Concern.** A verify-then-assign gate is a TOCTOU candidate; `AllowReassignment` explicitly permits moving a secondary IP that is already on another ENI.
**High-level Test Scenarios:**
- *Claim:* Two concurrent manual prefix/IP assignments **race** the uniqueness check and both succeed, producing a duplicated in-subnet address/prefix (traffic blackhole / hijack of another ENI's IP). → *Oracle:* fire N parallel `AssignPrivateIpAddresses`/prefix calls for the same value across two ENIs; observe two accepts. → Sev: Medium (intra-account; High if it steals a *requester-managed* ENI's IP).
- *Claim:* `AllowReassignment=true` lets a caller **steal a secondary private IP** off another ENI they can name, redirecting that IP's traffic. → *Oracle:* reassign a victim ENI's secondary IP; confirm traffic follows. → Sev: Medium.
- *Claim:* Manual assignment of an IP inside a **requester-managed** ENI's range is (not) blocked. → *Oracle:* attempt; expect refuse. If it succeeds → HARD STOP (touching service-plane addressing).
**Doc evidence:** `ec2-prefix-eni.md` ("verifies not already assigned"), `create-network-interface.md` (Custom prefix), `managing-network-interface-ip-addresses.md`, `list_ec2.md` `AssignPrivateIpAddresses`. **Severity-if-true:** Medium.

### Area 7 — AWS-authored IAM-artifact audit  (Lens R / S)
**Background.** The Step-1 discipline requires resolving any AWS-managed / sample policy the docs reference.
**Security Concern.** The ENI UserGuide pages themselves print **no** IAM policy JSON, no CFN, no named managed policy, no SLR — so there is no page-local artifact to audit *here*. But ENI actions (`CreateNetworkInterface`, `AttachNetworkInterface`, `ModifyNetworkInterfaceAttribute`, `AssignPrivateIpAddresses`) appear in many **AWS-managed policies elsewhere** (`AmazonEC2FullAccess`, EKS/ELB/Lambda/RDS SLR policies that manage ENIs on the customer's behalf).
**High-level Test Scenarios:**
- *Claim:* An AWS-managed policy grants ENI mutating actions with `Resource:"*"` and no `ec2:Vpc`/tag condition → a holder can attach/modify/attach-SG on **any** ENI in the account (intra-account over-grant baked into an uneditable artifact). → *Oracle:* `iam:GetPolicyVersion` on the candidate managed policies; audit the ENI statements; `iam:SimulatePrincipalPolicy` as the safe first oracle. → Sev: Medium–High (AWS-owned, Tier-2 reportable) if a *non-admin* managed policy over-grants; Low if only in `*FullAccess`.
- *Claim:* An SLR that creates ENIs "on your behalf" holds `DeleteNetworkInterface`/`ModifyNetworkInterfaceAttribute` broader than its purpose. → *Oracle:* resolve the SLR's attached policy; compare to stated purpose. → Sev: Medium.
**Doc evidence:** none page-local (state this); route to `list_ec2.md` + managed-policy resolution. **Severity-if-true:** Medium–High only if the artifact is AWS-authored/uneditable.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account attach without/after grant | `CreateNetworkInterfacePermission` / `DeleteNetworkInterfacePermission` | "grant to a single account only"; separate delete API; scenarios "can't multi-home across accounts" |
| Disable source/dest check under a restrictive policy | `ModifyNetworkInterfaceAttribute(SourceDestCheck)` | "checks enabled by default"; **no value-level condition key** |
| `ec2:Attribute` case / multiplex fail-open | `ModifyNetworkInterfaceAttribute` | `ec2:Attribute` + `ec2:Attribute/${AttributeName}` condition keys |
| Attach over-permissive SG | `ModifyNetworkInterfaceAttribute(Groups)` / `CreateNetworkInterface` | `security-group` resource keys (`ec2:Vpc`,`ec2:SecurityGroupID`) — only if authored |
| Cross-VPC segmentation bridge (same account) | `AttachNetworkInterface` | "different VPC that you own" feature; **no instance-VPC↔eni-VPC binding key** |
| Rogue ENI disguised as service ENI | `CreateNetworkInterface(Description)` / `DescribeNetworkInterfaces` | `RequesterManaged`/`RequesterId` server-set markers |
| Prefix/IP uniqueness race; IP theft via reassignment | `AssignPrivateIpAddresses` (`AllowReassignment`), prefix manual assign | "AWS verifies the prefix is not already assigned" |
| Reach service plane via requester-managed ENI | `ResetNetworkInterfaceAttribute` / attach / route | "you can't manage these yourself" (+ reset allowed) — HARD STOP if breached |
| Delete a service-detached ENI (dangling) | `DeleteNetworkInterface` | "if the service detached but didn't delete it, you can delete it" |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Multi-tenant service-fleet compromise / cross-*account* IDOR on the ENI object itself** — there is no shared AWS fleet in the ENI data path; the ENI is a customer VPC resource. Lens A cross-account and Lens D control-plane-escape are **null here** (the exception is the requester-managed ENI's backing service = HARD STOP, not a test target).
- **Intra-account least-privilege footguns in a *customer-authored* policy** (e.g. the customer grants `ec2:*` and complains ENIs are reachable) — the customer's own defect, out of scope. In-scope only when the over-grant ships in an AWS-managed/uneditable artifact (Area 7).
- **VPC data-plane packet security** (NACL/route-table/security-group *rule* efficacy, packet sniffing on the wire, ENA/EFA driver internals, SRD transport) — governed by other guides; this page only sets SG *membership*.
- **Single-tenant self-DoS** — exhausting your own ENI-per-instance or IP-per-ENI limits.
- **IMDS on the managed instance** beyond the src/dest-check reachability enabler noted in Area 2.
- **EIP transfer / recover-by-value / BYOIP** deep dives — already covered by the existing EIP-addresses, instance-addressing, and BYOIP plans in memory; only the `AssociateAddress`→ENI seam is referenced here.

---

## 8. Null Hypotheses / Doc Gaps

- **Lens F (translation/injection), K (prompt/LLM), H (KMS/encryption-context), W (attestation), Y (TLS/SigV2):** N/A. Read all ten ENI UserGuide pages + the ENI API references; the ENI surface has no parser/translator, no LLM, no customer-KMS integration on the ENI object, no attestation gate, and no ENI-specific transport/signature knob. No triggers.
- **Lens G (SSRF):** N/A for the ENI control plane — read create/modify/attachments/requester-managed/prefix pages; no field the ENI service dereferences server-side (Description is stored/rendered, not fetched). *Adjacent:* disabling src/dest check (Area 2) is an SSRF-*enabler* for reaching IMDS from a VPC appliance, tracked there, not as an ENI-service SSRF.
- **Lens I (tagging/ABAC):** partially fires — `aws:RequestTag`/`aws:TagKeys` on `CreateNetworkInterface`, `aws:ResourceTag` on most actions; folded into the condition-key analysis of Areas 1–4 rather than a standalone area. Worth a dedicated ABAC-bypass pass only if the customer uses tag-based ENI access control.
- **Lens N (namespace migration):** N/A — no dual-live ARN/namespace migration documented for ENIs.
- **Lens T (cross-service secret reachability):** N/A — the ENI generates no persisted secret/credential (MAC/IPs are not secrets).
- **Doc gaps to confirm on the live system first:**
  - Exact behavior of `AwsService` on `CreateNetworkInterfacePermission` (docs say "currently not supported" — control-plane response unverified). *doc-gap — confirm surface first.*
  - Whether `DeleteNetworkInterfacePermission` severs an already-live cross-account attachment (Area 1) — not documented. *doc-gap.*
  - Whether the manual-prefix "verify not already assigned" check is transactional (Area 6 race) — not documented. *doc-gap.*
  - Whether `RequesterManaged`/`RequesterId` are truly immutable/customer-unsettable (Area 5) — implied by "you can't manage these yourself" but not stated as a forgery guarantee. *doc-gap.*

---

### Appendix — verified condition-key facts (from `list_ec2.md`, offline mirror 2026-09-13; re-verify live)
- `ModifyNetworkInterfaceAttribute` → `network-interface*` exposes **`ec2:Attribute`** and **`ec2:Attribute/${AttributeName}`** (attribute-name scoping, subject to case fail-open) but **no value-level key** for `SourceDestCheck`/`Groups` values.
- `AttachNetworkInterface` → `instance*` resource has **no `ec2:Vpc`** key; `network-interface*` has `ec2:Vpc`/`ec2:Subnet` — so **no way to require instance-VPC == eni-VPC**.
- `CreateNetworkInterfacePermission` → access level **Permissions management, Write**; keys `ec2:AuthorizedUser`, `ec2:AuthorizedService`, `ec2:Permission`.
- `CreateNetworkInterface` → `security-group` and `subnet*` scopable by `ec2:Vpc`/`ec2:SecurityGroupID`/`ec2:SubnetID`; **no interface-type value key**.
- `AssignPrivateIpAddresses` → keys `ec2:Subnet`,`ec2:Vpc`,`ec2:NetworkInterfaceID`,tag; **no key on the assigned IP/prefix value**; `AllowReassignment` request flag is uncondition-able.
