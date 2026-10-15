# CreateNetworkInterface (EC2 ENI creation) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-network-interface.html` (+ `.md` twin, offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/create-network-interface.md`); authoritative IAM from `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10190 lines, read by offline grep — online `.md` truncates before the CreateNetworkInterface rows); adjacent pages `efa.md`, `create-efa.md`, `efa-start.md`, `ec2-prefix-eni.md`, `security-group-connection-tracking.md`, `managing-network-interface-ip-addresses.md`, `modify-network-interface-attributes.md`, VPC UG `vpc-share-limitations.md`/`using-vpc.md`; API `API_CreateNetworkInterface.md`. **Status: documentation-derived hypotheses only; nothing tested against a live account.** All pages verified offline==online byte-identical 2026-10-15 (two parallel subagents + direct Opus grep); no drift.

This is the **page-level deep-dive child of the `ec2-networking` hub for the `CreateNetworkInterface` action**, i.e. the *create-time* ENI surface. It is a sibling/complement of:
- **`using-eni-attack-research-plan.md`** — owns ENI *lifecycle/attribute/grant* (Attach / Modify / Reset / Delete / Describe / Create+DeleteNetworkInterfacePermission). That plan **explicitly deferred ENI creation**; this plan owns it. Cross-ref, do not restate.
- **`using-instance-addressing` / `working-with-ip-addresses` / `instance-secondary-ip-addresses` / `working-with-ipv6-addresses`** — own IP *assignment/reassignment* post-create (`AssignPrivateIpAddresses … AllowReassignment` takeover, launch-time public IP, EIP ride-along). This plan owns only create-time IP *value selection* and cross-refs the rest.
- **`AvailableIpPerENI`** plan — owns per-ENI IP-capacity / subnet-exhaustion depth; this plan feeds it the prefix-delegation create vector.
- **`ec2-networking` hub** — owns the EFA/SRD cross-tenant frame-injection mechanism (hub lead #3) and shared-VPC isolation (hub lead #5); this plan owns the create-time *EFA-interface-type-is-unscopable* and *participant-creates-ENI-in-owner-subnet* angles and cross-refs the mechanism.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The safe first oracle for every IAM-scoping lead is **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — it settles "is this key inert on this action" with **zero resources created**. `DryRunOperation` is caller-IAM-only and evaluated *before* resource resolution — **not** an ownership/scoping oracle (false-positive trap).
- Cross-account leads (Area 2, Area 6) need a **2-account canary** (owner O + RAM-share participant P). Use synthetic subnets/IPs only.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — **requester-managed / `Managed=true` ENIs, Hyperplane/Lambda ENIs, the EFA SRD fabric host side, any `Operator`-marked service ENI** — stop, preserve evidence, flag for AWS-Security disclosure. Do not probe the host/Nitro side of the SRD path.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. Create a network interface whose **security-relevant attribute an admin policy was written to forbid** — an EFA/EFA-only/`trunk` interface, a prefix-delegated ENI, a specific private IP, a max-timeout connection-tracking spec — proving the guardrail is unexpressible (Area 1, 3, 4).
2. As a **RAM-share participant**, create an ENI in the **owner's** subnet bearing a **specific private IPv4** the owner's workload expects (a hardcoded internal-service address), pre-empting or colliding with the owner's launch, and leave an ENI the owner **cannot delete** (Area 2).
3. Exhaust an owner's **shared subnet IP space** or an instance's **connection-tracking table** via create-time knobs with no IAM cap (Area 3).
4. Reach a **console-hidden** CreateNetworkInterface state (`InterfaceType=trunk`, `Operator=…`) that changes isolation/manageability of the ENI (Area 4).
5. Pin an ENI's **primary IPv6** irreversibly as a transient create-time actor (Area 5).
6. Confirm no **EventBridge** signal reaches the subnet owner when a foreign ENI is created in their subnet (Area 7).

---

## 2. Components, Assets, and Design

**Interface:** `ec2:CreateNetworkInterface` (SigV4 IAM; console "Network Interfaces → Create", CLI `create-network-interface`, PS `New-EC2NetworkInterface`). Runs under the **caller's own identity** — there is **no service-linked role and no PassRole** on this action (no credential-vending or confused-deputy surface here; contrast the Fleet corpus).

**What a "resource" is:** a **network interface** `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}` (`eni-…`). Created in the **available (unattached)** state; attachment is a *separate* later action (`AttachNetworkInterface` / launch-time `NetworkInterfaces`) owned by the `using-eni` plan.

**Request parameters** (API_CreateNetworkInterface, all `Required: No` except `SubnetId`):
`ClientToken`, `ConnectionTrackingSpecification` (obj), `Description`, `DryRun`, `EnablePrimaryIpv6` (bool), `InterfaceType` (`interface|efa|efa-only|trunk`, default `interface`), `Ipv4Prefix.N`, `Ipv4PrefixCount`, `Ipv6AddressCount`, `Ipv6Addresses.N`, `Ipv6Prefix.N`, `Ipv6PrefixCount`, `Operator` (obj — **"Reserved for internal use."**), `PrivateIpAddress`, `PrivateIpAddresses.N`, `SecondaryPrivateIpAddressCount`, `SecurityGroupId.N`, **`SubnetId` (Required: Yes)**, `TagSpecification.N`.

**Trust zones:** customer account (caller) ↔ **shared-VPC owner account** (when the subnet is RAM-shared to the caller) ↔ the EFA/SRD data-plane fabric (host side = AWS service plane, hard stop). No separate service/control account on this action.

```
caller (participant or owner)
   │  ec2:CreateNetworkInterface  (SubnetId required)
   ▼
 [subnet*]  ← scopable: ec2:Vpc / ec2:SubnetID / ec2:AvailabilityZone(Id) / tag
 [security-group] ← scopable: ec2:Vpc / ec2:SecurityGroupID / tag   (SG-VPC==subnet-VPC enforced SERVICE-side only)
   │
   ▼  creates
 eni-… (state: available)   ← NOT scopable at create: InterfaceType, Private/IPv6 IP value,
   │                           Ipv4/Ipv6 prefixes, EnablePrimaryIpv6, ConnectionTracking timeouts
   │                           (ENI OWNED BY CALLER even inside owner's shared subnet)
   ▼ later (separate actions, other plans)
 Attach → instance │ AssignPrivateIpAddresses(AllowReassignment) │ Modify/Reset attr
```

---

## 3. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller holding scoped `CreateNetworkInterface` | the ENI's own attributes (type/IP/prefix/conntrack) | create request body fields with **no condition key** | ENI created with the forbidden attribute while policy "denies" it → scoping gap (SimulateCustomPolicy shows key inert) |
| RAM-share **participant** | **owner's** shared subnet | `--subnet-id <owner's subnet> --private-ip-address <chosen>` | participant-owned ENI appears in owner's subnet at a chosen IP; owner can only Describe, cannot delete |
| Participant / team | shared subnet IP pool / instance conntrack table | prefix delegation / max conntrack timeout at create | owner launch fails for lack of addresses, or conntrack table exhaustion drops packets, with no IAM lever to prevent |
| Caller | console-hidden ENI state | `InterfaceType=trunk` / `Operator=…` | an ENI created in a state the console never offers that changes isolation/manageability |
| Any customer surface | EFA SRD fabric host side / managed ENI plane | — | **HARD STOP** — AWS service plane |

---

## 4. API / Interface Inventory

| Name | Mut? | Ext? | Internet? | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ec2:CreateNetworkInterface` | **Mutating** | External | Yes | anyone with the IAM action (incl. shared-VPC participant) | 3 req resource types; ENI's own attrs unscopable |
| `ec2:CreateNetworkInterfacePermission` | Mutating (Perms mgmt) | External | Yes | ENI owner | cross-account grant — **owned by `using-eni`** |
| `ec2:ValidateSecurityGroupQuotasForInterface` | Non-mut | External | Yes | caller | SG-quota precheck; low signal |
| `ec2:DescribeNetworkInterfaces` | Non-mut | External | Yes | all (unscopable) | account-wide read oracle; **owner's only visibility into participant ENIs** |
| `AttachNetworkInterface` / `ModifyNetworkInterfaceAttribute` / `ResetNetworkInterfaceAttribute` / `DeleteNetworkInterface` | Mutating | External | Yes | ENI owner | **owned by `using-eni`** — cross-ref only |

**Console-hidden knobs (Step-3 delta):** `InterfaceType=trunk` and `Operator` ("Reserved for internal use") are accepted by the API/SDK but **absent from the console "Create network interface" flow and all UserGuide prose** (grep of `create-network-interface.md` for `trunk` = 0). → Area 4.

---

## 5. Recommended Areas of Focus

### Area 1 — HEADLINE (Lens S/U, AWS-owned, Tier-2 reportable): the ENI's own security-relevant attributes are UNSCOPABLE at create
**Background.** `ec2:CreateNetworkInterface` (list_ec2 L5357–5362) requires exactly three resource rows and scopes only **where** the ENI is born and **which SG** rides on it:
- `network-interface*` → keys: `aws:RequestTag`, `aws:TagKeys`, `ec2:NetworkInterfaceID`, `ec2:Region` (note: **no `aws:ResourceTag`** — the ENI doesn't exist yet; tag-on-create via RequestTag is the only tag lever).
- `security-group` (non-`*`) → `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`, `ec2:SecurityGroupID`, `ec2:Vpc`.
- `subnet*` → `aws:ResourceTag`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:Region`, `ec2:ResourceTag`, `ec2:SubnetID`, `ec2:Vpc`.

**Security Concern.** None of the ENI's **own** future attributes is expressible as a condition key. Whole-corpus grep of `list_ec2.md` (10190 lines): `ec2:InterfaceType` = **0**, `ec2:Ipv4Prefix`/`ec2:Ipv6Prefix` = **0**, `ec2:PrivateIpAddress`/`ec2:Ipv6Address` = **0**, `ec2:PrimaryIpv6`/`ec2:EnablePrimaryIpv6` = **0**, `ec2:ConnectionTracking`/`ec2:IdleTimeout` = **0**, `ec2:NetworkCardIndex` = **0**. So an admin **cannot** write a CreateNetworkInterface-scoped policy that: forbids EFA/EFA-only/`trunk` interfaces, forbids or caps IP prefix delegation, pins/forbids a specific private or IPv6 address, forbids the irreversible primary-IPv6 toggle, or forces a short connection-tracking timeout. This is the **confirmed `ec2:InterfaceType`-is-not-a-real-key** variant of Lens S ("a condition key that does not exist → cannot deny by it") applied across five attributes at once.

**High-level Test Scenarios.**
- *Claim:* a policy that `Deny`s `ec2:CreateNetworkInterface` with `Condition {StringEquals ec2:InterfaceType: efa}` is **inert** → **Mechanism:** key undefined on the action → **Oracle:** `iam:SimulateCustomPolicy` returns Allow for an `efa` create under that policy (and the key simply does not resolve). Repeat for a prefix/IP/EnablePrimaryIpv6/conntrack-timeout condition. **No resource created.**
- *Claim:* the ONLY create-time guardrails that hold are subnet-identity (`ec2:SubnetID`/`ec2:Vpc`), SG-identity (`ec2:SecurityGroupID`/`ec2:Vpc`), region, and tag-on-create (`aws:RequestTag`/`aws:TagKeys`) → Simulate to confirm these *do* bind (positive control).

**Doc evidence:** list_ec2 L5357–5362; API_CreateNetworkInterface param list. **Severity-if-true:** Medium (Lens-S control-gap; **High** where an org relies on an inert Deny believing EFA/prefix/IP are governed) — AWS-owned/uneditable semantics, **Tier-2 reportable**. **Stop condition:** Simulate confirms the five keys inert and the three identity levers live.

---

### Area 2 — Cross-account shared-VPC (Lens A / L / EE): participant creates an ENI with a CHOSEN private IP in the OWNER's subnet; pre-emption + un-cleanable residue
**Background.** `vpc-share-limitations.md` (Network interfaces): *"Participants can create network interfaces in a shared VPC subnet. … Participants can modify or delete the network interfaces in a shared VPC that they created. … VPC owners can describe network interfaces owned by participants in a shared VPC subnet. VPC owners cannot work with network interfaces owned by participants in any other way, such as attaching, detaching, or modifying…"* `using-vpc.md` L49: participants must own ENIs they specify. The create page CLI Examples 2 & 4 show `--private-ip-address`/`--private-ip-addresses PrivateIpAddress=10.0.1.30,Primary=true` with **no shared-subnet caveat**. There is **no documented cross-account IP-collision/uniqueness check or error anywhere** in the EC2 or VPC UserGuide (doc silence, not confirmed-absent enforcement).

**Security Concern.** A RAM-share participant P, given only `ec2:CreateNetworkInterface` scoped to the owner O's shared `subnet*`, can:
1. **Pre-empt / collide on a specific private IPv4** O's workload depends on (a hardcoded internal-service address, a well-known `.5`, a Kubernetes/service-mesh fixed IP). If subnet-wide IP uniqueness is enforced regardless of account, P's create **DoSes** O's later launch at that address (address-confusion / "available"-vs-taken); if it is *not* cross-account enforced, two ENIs could claim one IP (routing ambiguity). Either outcome is a cross-account integrity/availability break; which one happens is the live question.
2. **Leave an ENI O cannot remove.** The ENI is **owned by P**; O can only `Describe` it — O cannot detach/modify/delete it, and after O **unshares** the subnet, *"Existing participant resources continue to run,"* O *"cannot delete the shared subnet or the shared-subnet VPC"* until P deletes its ENI (`vpc-sharing-share-subnet-working-with.md`). So P can **pin a persistent, un-cleanable foreign ENI** inside O's subnet (land-grab / subnet-pollution; EE-flavoured — occupying a name/address in a namespace O controls).

**High-level Test Scenarios (2-account canary O+P).**
- *Claim:* P creates `eni` in O's shared subnet at `--private-ip-address <IP O expects>` → **Oracle:** `aws ec2 describe-network-interfaces` from O shows a participant-owned ENI holding that IP; O's attempt to launch/create at the same IP returns an in-use/collision error (DoS) — **or** both succeed (ambiguity). Record the exact error/behavior (currently undocumented).
- *Claim:* O cannot reclaim the IP/ENI → **Oracle:** O's `delete-network-interface`/`detach` on P's ENI returns AccessDenied; after O unshares, O's `delete-subnet` is blocked until P deletes.
- *Adjacent:* does P creating the ENI require any tag O's RequestTag policy could gate? (Only `aws:RequestTag` is available — O can require a tag, but cannot stop the IP choice.)

**Doc evidence:** `vpc-share-limitations.md` Network-interfaces bullets; `vpc-sharing-share-subnet-working-with.md`; create page CLI Ex2/Ex4; Area-1 proof that no IP-value key exists. **Severity-if-true:** cross-account subnet IP pre-emption/DoS = **High**; persistent un-cleanable foreign ENI = **Medium–High**. **Preconditions:** O shares a subnet to P via RAM; P scoped to that subnet only. **Cost:** low. **Stop condition:** collision behavior + reclaim-impossibility observed, or refuted (cross-account uniqueness cleanly rejects with a clear error and no ambiguity).

---

### Area 3 — Create-time exhaustion amplifiers with no IAM cap (Lens L / U)
**Background & Concern.** Two create-time knobs scale resource consumption and have **no condition key** (Area 1) to cap them:

**(a) IP prefix delegation.** `ec2-prefix-eni.md`: IPv4 prefix = **`/28` (16 addresses)**, IPv6 = `/80`; *"Each prefix that you assign to a network interface counts as one IP address"* against the per-ENI limit; *"Manual assignment — You specify the prefix and AWS verifies that it is not already assigned to other resources before assigning it."* `Ipv4Prefix.N`/`Ipv4PrefixCount`/`Ipv6Prefix.N`/`Ipv6PrefixCount` are create params. A participant/team can therefore allocate **16× the subnet space per prefix** at create with no IAM lever to forbid prefixes or cap the count → amplified **shared-subnet IPv4 exhaustion** (chains to Area 2's cross-account subnet and to the **`AvailableIpPerENI`** plan's per-ENI-maxima exhaustion depth). Manual-prefix selection also lets a caller **target** a specific /28 of the subnet (pre-empt a CIDR O expects).

**(b) Connection-tracking spec.** `security-group-connection-tracking.md`: the conntrack table is **per-instance and bounded** — *"Connections that remain idle can lead to connection tracking exhaustion and cause connections not to be tracked and packets to be dropped"*; *"After the maximum is reached, any packets … are dropped."* `ConnectionTrackingSpecification` sets per-ENI idle timeouts: **TCP established up to 432000 s (5 days)**, UDP up to 60 s, UDP-stream up to 180 s. AWS's own guidance is *"configure the shortest idle connection tracking timeout possible"* — but there is **no IAM key** to enforce it, so an ENI can be created with the **maximum** timeout, keeping idle flows pinned in the table far longer → faster table exhaustion / packet drops on the instance it attaches to. Interacts with the documented **untracked-flow bypass** (a wide-open bidirectional 0.0.0.0/0 rule makes flows untracked by design, and *"an untracked flow … is immediately interrupted if the rule … is removed or modified"*).

**High-level Test Scenarios.**
- *Claim:* no policy can forbid/limit prefix delegation at create → **Oracle:** `SimulateCustomPolicy` with a prefix-targeting Deny is inert (Area 1). Live: a scoped principal creates an ENI with `--ipv4-prefix-count 9` and consumes 144 subnet addresses.
- *Claim:* an admin cannot force a short conntrack timeout → **Oracle:** Simulate a conntrack Deny inert; live create an ENI with TCP timeout 432000 and confirm it attaches.
- *Chain:* Area 2 (participant in O's subnet) + prefix delegation → **cross-account subnet exhaustion DoS** of O's launches.

**Doc evidence:** `ec2-prefix-eni.md` (Basics/Considerations), `security-group-connection-tracking.md` (timeouts/exhaustion/untracked), API param list. **Severity-if-true:** cross-tenant shared-subnet exhaustion = **High**; single-instance conntrack self-exhaustion = Low–Medium (High if it degrades a co-tenant on a shared host, which the docs do not claim). **Stop condition:** keys confirmed inert and consumption reproduced, or a per-account/subnet governor is found that caps it.

---

### Area 4 — Console-hidden InterfaceType `trunk` + `Operator` "Reserved for internal use" (Lens U — undocumented knob; Step-3 delta)
**Background.** `InterfaceType` valid values are `interface | efa | efa-only | trunk`, but the console "Create network interface" flow and all `create-network-interface.md` prose surface only **ENA / EFA-with-ENA / EFA-only** — `trunk` is **never mentioned** (grep = 0). `Operator` is an `OperatorRequest` object documented verbatim as **"Reserved for internal use."** (API_CreateNetworkInterface L89). The `network-interface` resource type carries `ec2:ManagedResourceOperator` and the `using-eni` plan established that **requester-managed / `Managed=true` ENIs are the AWS service plane** and that `ResetNetworkInterfaceAttribute` works on requester-managed ENIs where `Modify` is blocked.

**Security Concern.** The delta between the API-accepted surface and the console surface is a lead:
- **`trunk`:** ENI trunking (branch ENIs; `AssociateTrunkInterface`) is used by ECS/EKS to multiplex many ENIs. Can a general caller create an `InterfaceType=trunk` ENI, and does doing so change isolation, attachment limits, or the branch-ENI relationship in a way the console-only operator never anticipated? Is `trunk` creation gated by anything beyond the (unscopable, Area 1) `InterfaceType` param?
- **`Operator`:** can a caller set `Operator` to mark the ENI as **managed / operated by a principal** (populating `ec2:ManagedResourceOperator`), thereby minting an ENI that the `using-eni` guardrails treat as service/requester-managed — e.g. one that resists `Modify` but is still `Reset`-able, or that mis-attributes ownership? If `Operator` is caller-settable despite "reserved," that is a declared-managed spoof.

**High-level Test Scenarios.** `SimulateCustomPolicy` + a careful DryRun (DryRun is IAM-only — it will NOT reveal whether `Operator`/`trunk` are honored, so a live canary create is needed): submit `--interface-type trunk` and an `Operator` object; observe whether the API accepts them, what `DescribeNetworkInterfaces` reports for `InterfaceType`/`RequesterManaged`/`Operator`, and whether the resulting ENI evades `Modify` while remaining `Reset`-able. **HARD STOP** if the created ENI appears under an AWS-owned operator/managed identity — preserve and disclose.

**Doc evidence:** API_CreateNetworkInterface (`InterfaceType` enum, `Operator` "Reserved for internal use"); create page prose omission; `using-eni` requester-managed findings. **Severity-if-true:** if `Operator`/`trunk` yields a managed-ENI spoof or service-plane attribution = **High + possible hard stop**; if merely an accepted-but-benign hidden state = Low (doc-gap/Informational). **Stop condition:** API accept/reject + resulting attribute state observed on a synthetic ENI.

---

### Area 5 — Irreversible `EnablePrimaryIpv6` set at create (Lens U / AA)
**Background.** Create page: *"After you enable an IPv6 GUA address to be a primary IPv6, you can't disable it. … until the instance is terminated or the network interface is detached."* Confirmed identically on `managing-network-interface-ip-addresses.md` (*"you can't change it"*) and framed in `using-instance-addressing.md`. `modify-network-interface-attributes.md` lists the modifiable attributes (Description, Security groups, Delete-on-termination, Source/dest check, Idle connection tracking timeout) and **does not include a primary-IPv6 disable** — the only "off" is terminate/detach. The API has `ModifyNetworkInterfaceAttribute EnablePrimaryIpv6` (set-only, surfaced via the "Manage IP addresses" flow, reachable by assign-IP perms).

**Security Concern.** A **one-way, revocation-incomplete** state change (Lens AA revoke-side): a transient create-time actor (or anyone who can reach the manage-IP flow) can **permanently pin** the ENI's primary IPv6 for the life of the ENI/instance. The documented rationale is pure availability ("avoid disrupting traffic"); no security caveat (persistent-identity trackability of a fixed GUA) is documented. There is no IAM key to forbid it (Area 1).

**High-level Test Scenarios.** *Claim:* `EnablePrimaryIpv6=true` at create cannot be undone except by terminate/detach, and cannot be IAM-forbidden → **Oracle:** create with the flag, confirm no API path disables it; `SimulateCustomPolicy` with an `EnablePrimaryIpv6` Deny is inert. **Severity-if-true:** Low–Medium (availability/standing-state footgun; trackable fixed-identity concern). **Stop condition:** irreversibility + inert-Deny confirmed.

---

### Area 6 — EFA/EFA-only create is a permissive-SG, unscopable interface (Lens V / D cross-ref hub #3; Lens R sample)
**Background.** Creating an EFA interface is **purely the `InterfaceType` param** — no special IAM permission or condition key (subagent grep of `efa.md`/`create-efa.md`/`efa-start.md` for permission/condition-key = 0; Area 1 proves `ec2:InterfaceType` doesn't exist). EFA **requires** an SG that *"allows all inbound and outbound traffic to and from the security group itself"* (`create-efa.md`), and the `efa-start.md` getting-started walkthrough **ships an SSH-from-anywhere `0.0.0.0/0` rule flagged "testing purposes only"** alongside the all-traffic self-rule. EFA/SRD isolation is bounded by `efa.md`: *"EFA traffic can't cross Availability Zones or VPCs"* and *"EFA traffic is not routable"* (ENA-side IP traffic remains routable).

**Security Concern.** (a) An org cannot forbid EFA-interface creation via IAM (Area 1), so any principal with `CreateNetworkInterface` can introduce the OS-bypass/SRD path and its mandatory permissive SG. (b) The AWS-published getting-started **sample SG** is an insecure-default artifact (all-traffic self-rule + SSH `0.0.0.0/0`) a customer may copy verbatim (Lens R). (c) The SRD/OS-bypass fabric's enforcement layer for the "can't cross AZ/VPC" guarantee is **never named** — the cross-tenant frame-injection question (same AZ, shared cluster placement group, 2 accounts' EFA endpoints) is the hub's lead #3; **this plan defers the mechanism to the hub** and owns only the create-time "no IAM lever + permissive-SG sample" framing.

**High-level Test Scenarios.** *Claim:* EFA creation is ungoverned by IAM → Simulate (Area 1). *Claim:* the getting-started SG sample is over-permissive as shipped → read `efa-start.md` SG steps, audit the printed rules. *(Defer SRD cross-tenant injection to the hub; HARD STOP at the fabric host side.)* **Severity-if-true:** EFA-ungovernable = Medium (control-gap); SRD cross-tenant (hub) = High–Critical. **Stop condition:** here, confirm the IAM gap + sample audit; hand the SRD mechanism to the hub.

---

### Area 7 — No EventBridge signal for ENI creation; cross-account detection asymmetry (Lens O)
**Background.** The native EC2 EventBridge catalog (`automating_with_eventbridge.md`) has **no network-interface create/delete event** (grep = 0). `CreateNetworkInterface` is an Access-level **Write** → a **CloudTrail management event** (logged by default) is the only signal.

**Security Concern.** Because a participant's ENI created in the owner's subnet (Area 2) is **owned by the participant**, the CloudTrail `CreateNetworkInterface` record lands in the **participant's** trail — the **owner has no event-driven signal** that a foreign ENI appeared in their subnet, only a pollable, unscopable `DescribeNetworkInterfaces` (blank resource type + `ec2:Region` only). So the Area-2 squat/exhaustion is **detectable only by the owner actively polling Describe**, never pushed. Pairs with the Area-5/Area-4 silent state changes.

**High-level Test Scenarios.** *Claim:* no EventBridge event fires on ENI create and the owner sees nothing in their own trail for a participant-created ENI → confirm the event-catalog absence; confirm (2-account) the Create event is only in P's trail. **Severity:** Low–Informational (detection enabler that raises Area-2/3 severity).

---

### Area 8 — The working controls + a VPC-match that IAM can't express (Lens S, completeness)
**Background.** The *positive* controls that DO bind at create: `ec2:SubnetID`/`ec2:Vpc`/`ec2:AvailabilityZone(Id)` on the subnet row, `ec2:SecurityGroupID`/`ec2:Vpc`/tag on the SG row, `ec2:Region`, and `aws:RequestTag`/`aws:TagKeys` (tag-on-create). An admin **can** pin "create ENIs only in subnet X with SG Y, Region Z, carrying tag T."

**Security Concern (narrow).** The service requires the SG and subnet to be in the **same VPC** (`ec2-instance-launch-parameters.md`: *"You must choose a security group from the same VPC as the subnet"*; `modify-network-interface-attributes.md`: *"The security group and network interface must be created for the same VPC"*) — but the **create page itself is silent** on this rule, and **IAM cannot express it**: `ec2:Vpc` on the SG row evaluates the *SG's home VPC*, nothing binds it to the subnet's VPC (Lens-S "key binds the wrong resource" shape). Because the service enforces matching, this is **not exploitable** — it is an IAM-expressiveness/doc-completeness note, logged so a hunter does not chase a cross-VPC-SG attach that the service already blocks. Also note the **absence of `aws:ResourceTag` on the `network-interface*` create row** (only `aws:RequestTag`) → ABAC on the ENI itself only begins to apply *after* creation.

**Severity:** Informational. **Oracle:** Simulate confirms the identity/tag levers bind and that a cross-VPC SG+subnet pair is rejected service-side (DryRun), not by IAM.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Create forbidden interface type / prefix / IP / conntrack-spec under a policy meant to deny it | `CreateNetworkInterface` IAM | the five attribute condition keys **do not exist** (list_ec2) — mitigation is absent |
| Participant pre-empts owner's internal-service IP in shared subnet | shared-VPC create | no documented cross-account IP-collision check (`vpc-share-limitations`) |
| Participant leaves un-cleanable ENI in owner subnet, blocks unshare/subnet-delete | shared-VPC ownership model | owner "cannot work with" participant ENIs; unshare leaves resources running |
| Shared-subnet IP exhaustion via prefix delegation | `Ipv4Prefix*` | per-ENI limit only; no per-principal/subnet IAM cap |
| Conntrack table exhaustion via max idle timeout | `ConnectionTrackingSpecification` | "configure shortest timeout" is prose guidance, no IAM enforcement |
| Hidden `trunk`/`Operator` state spoofs managed/isolated ENI | `InterfaceType`/`Operator` | "Reserved for internal use" is prose only; no documented authz |
| Irreversible primary-IPv6 pin | `EnablePrimaryIpv6` | documented one-way; no disable path; no IAM key |

---

## 7. Out-of-Scope Risk Categories
- The **EFA/SRD fabric host side**, requester-managed / `Managed=true` / Hyperplane / Lambda ENIs — **AWS service plane, hard stop** (hand SRD cross-tenant mechanism to the `ec2-networking` hub lead #3).
- ENI **Attach/Modify/Reset/Delete** and the **CreateNetworkInterfacePermission** cross-account grant — owned by **`using-eni`**; not re-tested here.
- Post-create **IP reassignment/takeover** (`AssignPrivateIpAddresses … AllowReassignment`), launch-time public IP, EIP ride-along — owned by **`using-instance-addressing`/`working-with-ip-addresses`/`instance-secondary-ip-addresses`**.
- Per-ENI IP-capacity maxima depth — owned by **`AvailableIpPerENI`**.
- Single-tenant self-DoS (own conntrack table, own subnet) absent cross-tenant blast = Low/out-of-scope.
- Customer-authored over-broad `CreateNetworkInterface` grants = customer footgun (out of scope); the **inert-condition-key semantics (Area 1)** and the **AWS getting-started EFA SG sample (Area 6)** are AWS-authored and **in scope / Tier-2**.

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens B / C (PassRole / credential vending) — N/A.** `CreateNetworkInterface` has no role-ARN/token param, no SLR, runs under caller identity (API param list read in full). No confused-deputy/STS surface.
- **Lens G (SSRF) — N/A.** No field the service dereferences: `SubnetId`/`SecurityGroupId`/`PrivateIpAddress`/`Ipv6Addresses`/prefixes are identifiers/addresses, not fetched URLs (full param list + create page + API ref read).
- **Lens F (translation/parser) — N/A.** No wire-protocol/query translation; IDs are not parsed into a backend language.
- **Lens Q (upload) — N/A.** No blob/file field (param list read).
- **Lens K (prompt injection) — N/A.** No LLM/agent in path.
- **Lens H (KMS/encryption-context) — N/A.** No KMS key param on ENI create.
- **Lens W (attestation) / Y (transport-sig) / J (OAuth) / FF (JWT) / N (namespace migration) / BB / CC / DD (multi-parser/authorizer/cache) / T (secret storage) / P (proofing) / M (session id) — N/A** for this single mutating control-plane action (create page + API ref read; none of their triggers present).
- **Doc gaps to confirm live first:** (1) cross-account **IP-uniqueness/collision behavior** in a shared subnet (Area 2 — undocumented; the central open question); (2) whether `Operator`/`InterfaceType=trunk` are **honored** for a non-service caller and what attribute state results (Area 4 — DryRun can't answer, needs synthetic canary); (3) whether EFA SRD "can't cross AZ/VPC" is enforced below SG — deferred to the hub.

See [[reference-aws-iam-service-auth-ref-url]] and [[project-aws-research-plans]].
