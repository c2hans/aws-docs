# Spot Fleet — *Example CLI Configurations* — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-examples.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/spot-fleet-examples.md`; the two are **byte-identical**, verified 2026-10-15). Authoritative IAM facts from `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (the online `list_ec2.html` summarizer-truncates and **drops the `RequestSpotFleet` entry entirely** — trust the offline grep; see [[reference-aws-iam-service-auth-ref-url]]). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **What this page is, and what this plan therefore owns.** `spot-fleet-examples.html` is a pure *example-configuration* reference: 12 AWS-authored JSON configs a customer copies and feeds to `aws ec2 request-spot-fleet --spot-fleet-request-config file://…`. It introduces **no new API** — every config is an input to `RequestSpotFleet`, already covered mechanism-by-mechanism by the siblings below. This plan is therefore the **copy-verbatim-artifact companion**: it treats the 12 configs as *shipped AWS artifacts* (skill Lens R — "AWS-published sample CODE insecure defaults") and owns (a) the insecure defaults the samples *instantiate* as copy-paste code, and (b) the three net-new mechanisms the samples surface that no sibling develops — **Capacity Rebalancing auto-replace+terminate (Ex 8)**, **attribute-based Min-only selection (Ex 12)**, and the **cross-account IamFleetRole (Ex 11)**.
>
> **Deliberate de-duplication — this plan complements, does not restate:**
> - **`create-spot-fleet-attack-research-plan.md`** owns the *mechanism* layer: §5.1 SLR-launch guardrail non-propagation (backbone), §5.2 inline-launch-spec weaker-twin / `MetadataOptions` parity gap, §5.3 inline instance-profile + user-data injection / request-time PassRole unverified, §5.5 cross-resource LB/target-group registration, §5.7 "does RequestSpotFleet resource-level scoping gate launch-spec *content* or only the request object", §5.8 network exposure at create. **This plan cites those and provides the artifact-level *evidence* that upgrades them from "mechanism exists" to "AWS ships the vulnerable default in copy-paste configs."**
> - **`spot-fleet-prerequisites-attack-research-plan.md`** owns the IAM-artifact audit of the sample *identity/role* policies, PassRole scoping, confused-deputy prevention, KMS-grant.
> - **`ec2-fleet-instance-weighting-walkthrough-…`** owns weighting overshoot (Ex 6); **`modify-spot-fleet-…`** / **`cancel-spot-fleet-…`** own the terminate primitives Ex 8/Ex 11 chain into; **`spot-fleet-states-…`** owns `maintain`/`request` lifecycle & 48h decay.

---

## §0 — How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **Safe first oracle for every IAM lead is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** (no resource created). Escalate to a live `request-spot-fleet` call **only** with a synthetic canary fleet, canary AMI, and synthetic account; tear everything down.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the `spotfleet.amazonaws.com` SLR's own credentials, not your fleet's), stop, preserve evidence, flag for AWS-Security disclosure.
- **Reportability carve-out:** findings here are against *AWS-authored, copy-verbatim example configs*. Per the skill's Lens-R carve-out, an insecure default in an AWS-published sample the customer is told to copy is **in scope and reportable (Tier 2 → `aws-security`)**, NOT a customer footgun — the footgun exclusion applies only to policies/templates the *customer* authored.

---

## §1 — Pentest Objectives (concrete breach outcomes to attempt)
1. Show that a principal who follows an AWS-published example literally launches **IMDSv1-capable** instances with **no in-request lever** to prevent it (Ex 1–6), i.e. the shipped artifact bakes in the SSRF→credential-theft precondition. *(Area 1)*
2. Show that the **inline `LaunchSpecifications` path (Ex 1–6)** is **less IAM-scopable** than both its launch-template cousin and its single-instance twin `RequestSpotInstances` — specifically that `AssociatePublicIpAddress`, the network-interface resource, and launch-template-resource distinction have **no condition key** on `RequestSpotFleet`. *(Area 2)*
3. Show that a caller can embed an **arbitrary `IamInstanceProfile.Arn`** in an inline launch spec whenever the admin copied the base example `iam:PassRole` statement (scoped only to the IamFleetRole) and did not add the separate instance-profile PassRole statement the "Important" callout requires. *(Area 3)*
4. Show that **Capacity Rebalancing `launch-before-terminate` (Ex 8)** is a bounded-but-material **cost-doubling + SLR-driven auto-terminate** primitive (fulfilled capacity → 2× target), and that `launch` mode is an **unbounded-cost** footgun. *(Area 4)*
5. Show that **attribute-based Min-only selection (Ex 12)** yields an effectively unbounded instance-type set bounded only by a **disable-able** price-protection heuristic. *(Area 5)*
6. Resolve whether `RequestSpotFleet` accepts a **cross-account `IamFleetRole`** (Ex 11's `111111111111`) → confused-deputy. *(Area 6)*
7. Resolve whether a `NetworkInterfaceId` placed in a launch spec/template is **rejected or silently dropped** (provisioning-integrity confusion). *(Area 7)*

---

## §2 — Components, Assets, and Design

**What the page is.** A set of 12 copy-paste JSON configs for `aws ec2 request-spot-fleet --spot-fleet-request-config file://{{file_name.json}}`. Two mutually-exclusive launch-spec styles appear:

- **Inline `LaunchSpecifications[]` (legacy)** — Examples **1–6**. Embeds, *directly in the request body*: `ImageId`, `KeyName`, `SecurityGroups[].GroupId`, `InstanceType`, `SubnetId`, `Placement.AvailabilityZone`, inline `NetworkInterfaces[]` (incl. `AssociatePublicIpAddress`), and **`IamInstanceProfile.Arn`**. Backed by the API struct `SpotFleetLaunchSpecification`.
- **`LaunchTemplateConfigs[]` (modern)** — Examples **7–12**. References an external `LaunchTemplateName`/`LaunchTemplateId` + `Version`, with per-pool `Overrides[]`.

**Identity / principals in play (unchanged from the create siblings, restated for the hunter):**
- **Caller** — holds `ec2:RequestSpotFleet` (+ dependent `ec2:CreateTags`, `iam:PassRole`). The caller does **not** launch instances directly.
- **IamFleetRole** (`aws-ec2-spot-fleet-tagging-role`, trusted by `spotfleet.amazonaws.com`) / the **AWSServiceRoleForEC2SpotFleet** SLR — the identity that actually performs `RunInstances`/`TerminateInstances` on the backend. This is the backbone fact: caller identity-policy conditions do **not** propagate to these launches (owned by `create-spot-fleet §5.1`).
- **Inline instance profile** (`my-iam-role`) — attached to the *resulting instances*; caller-supplied; the IMDS-reachable workload identity.

**ASCII pipeline (where the trust lines are):**
```
 operator's laptop                 caller IAM identity              service plane (AWS-owned)
 ┌───────────────┐  file://cfg.json ┌───────────────────┐  assume   ┌──────────────────────────┐
 │ aws ec2       │ ───────────────► │ ec2:RequestSpotFleet│ ───────► │ IamFleetRole / SLR        │
 │ request-spot- │ (client reads    │  +iam:PassRole      │ PassedTo │ (spotfleet.amazonaws.com) │
 │ fleet         │  the file; NOT   │  (service-scoped)   │ Service= │  RunInstances  Resource:* │
 └───────────────┘  an SSRF)        └─────────┬───────────┘ ec2.*    │  TerminateInstances  *    │
   ▲ 12 AWS sample                              │ inline spec carries   └───────────┬──────────────┘
   │ configs = the                              │ ImageId/SG/subnet/       launches  │
   │ copy-verbatim                              │ IamInstanceProfile.Arn/            ▼
   │ artifact set                               │ NetworkInterfaces              ┌──────────────┐
   └── insecure defaults ───────────────────────┘ (NONE set MetadataOptions)     │ EC2 instances│
                                                                                 │ IMDS reachable│
                                                                                 └──────────────┘
```

**Assets at risk:** the workload-identity creds reachable via IMDS on launched instances (Area 1); the account's EC2 spend/quota (Areas 4,5); the IamFleetRole / inline instance-profile trust (Areas 3,6); provisioning integrity (Area 7).

---

## §3 — API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `ec2:RequestSpotFleet` | SigV4 API / CLI `request-spot-fleet` | Existing | **Yes** | Yes | holder of `ec2:RequestSpotFleet` + dependent `ec2:CreateTags`, `iam:PassRole` | The *only* action this page exercises. 8 resource types; see §4. |
| `--spot-fleet-request-config file://…` | CLI arg | Existing | n/a | n/a | local operator | **Client-side file load only — NOT a server-side fetch** (no `http(s)` scheme; wire-identical to inline JSON). Null for SSRF. |

**Dependent-action table (list_ec2.md:4354–4357, verbatim shape):** `RequestSpotFleet` ⇒ `ec2:CreateTags` (Tagging,Write) + `ec2:RequestSpotFleet` (Write) + `iam:PassRole` with **`iam:PassedToService = ec2.amazonaws.com`** (service-scoped, not role-scoped).

**`RequestSpotFleet` resource types + condition keys (list_ec2.md:9465–9474, verbatim):**
| Resource type | Condition keys (exact) |
|---|---|
| `image` | `aws:ResourceTag/*`, `ec2:ImageID`, `ec2:ImageType`, `ec2:Owner`, `ec2:Public`, `ec2:Region`, `ec2:ResourceTag/*`, `ec2:RootDeviceType` |
| `key-pair` | `aws:ResourceTag/*`, `ec2:KeyPairName`, `ec2:KeyPairType`, `ec2:Region`, `ec2:ResourceTag/*` |
| `launch-template` | `aws:ResourceTag/*`, `ec2:ManagedResourceOperator`, `ec2:Region`, `ec2:ResourceTag/*` |
| `placement-group` | `aws:ResourceTag/*`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`, `ec2:ResourceTag/*` |
| `security-group` | `aws:ResourceTag/*`, `ec2:Region`, `ec2:ResourceTag/*`, `ec2:SecurityGroupID`, `ec2:Vpc` |
| `snapshot` | `aws:ResourceTag/*`, `ec2:OutpostArn`, `ec2:Owner`, `ec2:ParentVolume`, `ec2:Region`, `ec2:ResourceTag/*`, `ec2:SnapshotID`, `ec2:SnapshotTime`, `ec2:SourceOutpostArn`, `ec2:VolumeSize` |
| **`spot-fleet-request*`** (only `*`required) | `aws:RequestTag/*`, `aws:TagKeys`, `ec2:Region` |
| `subnet` | `aws:ResourceTag/*`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:Region`, `ec2:ResourceTag/*`, `ec2:SubnetID`, `ec2:Vpc` |

**Absent-by-design (the leads):** NO `instance-profile` resource type; NO `network-interface` resource type (its single-instance twin `RequestSpotInstances` at 9477–9486 **does** carry one, with `ec2:NetworkInterfaceID`/`ec2:Subnet`/`ec2:Vpc`); NO `ec2:AssociatePublicIpAddress` (key *exists* at 10050 but only on `network-interface`-bearing actions); NO `ec2:MetadataHttpTokens`/`-Endpoint`/`-PutResponseHopLimit` (58 occurrences in list_ec2, all on `instance`-keyed actions, none here); NO `ec2:IsLaunchTemplateResource`/`ec2:LaunchTemplate` on any row (RunInstances/CreateFleet rows are riddled with them).

---

## §4 — Trust-Boundary Map

| From (actor) | To (resource) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller | Launched instance's IMDS creds | inline spec with no `MetadataOptions` → IMDSv1 | Any launched instance answers IMDSv1 (`curl 169.254.169.254/latest/meta-data/iam/...` with no token) — the sample *shipped* the precondition |
| Caller | Arbitrary instance-profile role | inline `IamInstanceProfile.Arn` under service-scoped `iam:PassRole` | `RequestSpotFleet` accepts a profile ARN the caller could not `PassRole` directly (admin copied base policy only) |
| Caller | Another account's IamFleetRole | `IamFleetRole` ARN field (Ex 11 shows `111111111111`) | `RequestSpotFleet` accepts a cross-account role ARN / the SLR assumes it = confused deputy |
| Caller | Account EC2 spend/quota | Ex 8 rebalance 2× target; Ex 12 Min-only unbounded types; `launch` mode | Fulfilled capacity reaches 2× target, or instance types far outside intent, under the SLR with no caller `TerminateInstances`/type condition |
| Caller's stated intent | Actual provisioning | `NetworkInterfaceId` in spec (doc says "omit") | Request neither rejects nor honors it → silent-drop launches a different ENI than operator believes |
| **any caller surface** | **AWS service plane** | SLR's own creds | **HARD STOP** |

---

## §5 — Recommended Areas of Focus (priority order)

### §5.1 — Area 1 [HEADLINE · Lens R / U — AWS-authored sample artifact ships insecure defaults] — IMDSv1 + public-IP + SSH-key defaults baked into the copy-paste configs
**Background.** All 12 configs are AWS-authored copy-verbatim artifacts. A grep of the page confirms: **0** occurrences of `MetadataOptions`/`HttpTokens` across all 12; exactly **1** `AssociatePublicIpAddress: true` (Ex 2); `KeyName: my-key-pair` present in Ex 1–2.

**Security Concern.**
- (a) **IMDSv1 by default, with no in-request lever for Ex 1–6.** The inline `SpotFleetLaunchSpecification` struct **has no `MetadataOptions` field at all** (API_SpotFleetLaunchSpecification.md field list: AddressingType, BlockDeviceMapping, EbsOptimized, GroupSet, IamInstanceProfile, ImageId, InstanceRequirements, InstanceType, KernelId, KeyName, Monitoring, NetworkInterfaceSet, Placement, RamdiskId, SpotPrice, SubnetId, TagSpecificationSet, UserData, WeightedCapacity) — so Examples 1–6 **cannot** request IMDSv2 at all from the fleet request. Combined with the IAM fact (no `ec2:MetadataHttpTokens` on `RequestSpotFleet`, §3), **there is no identity-policy or request-body mechanism to force IMDSv2 on the Spot Fleet inline path** — the only backstops are the AMI's `ImdsSupport: v2.0` or an **opt-in** account-level IMDS default (AWS does *not* pre-set it; absent AMI/account setting the default is `HttpTokens=optional` = IMDSv1-and-v2, per `configuring-instance-metadata-options.md`). For Ex 7–12 (launch-template path) `MetadataOptions` lives in `RequestLaunchTemplateData` inside the referenced template, which the page never shows — so the omission is *forced* for 1–6 and *invisible* for 7–12.
- (b) **Public IP baked in** (Ex 2 `AssociatePublicIpAddress:true`) with **no `ec2:AssociatePublicIpAddress` condition key on `RequestSpotFleet`** → an admin cannot deny public-IP assignment on the fleet path even though they can on `RunInstances`/`CreateFleet` (§3; chains to Area 1a — a public, IMDSv1 instance is directly reachable).
- (c) SSH `KeyName` present in samples (minor; a key-pair backstop is scopable via `ec2:KeyPairName`).

**High-level Test Scenarios (falsifiable claims).**
- *Claim:* a fleet created from Ex 1 verbatim launches instances that answer IMDSv1 (token-less `GET 169.254.169.254/latest/meta-data/iam/security-credentials/`). → *Oracle:* token-less IMDS call returns the instance-profile creds on a canary fleet built from the verbatim config with a stock AMI and no account IMDS default. *Severity-if-true:* the artifact ships the SSRF→creds precondition = **Medium (High in combination with (b)'s public IP)**; AWS-owned, Tier-2 reportable.
- *Claim:* no `ec2:MetadataHttpTokens` Deny can be written for `RequestSpotFleet`. → *Oracle:* `iam:SimulateCustomPolicy` with a Deny on `ec2:MetadataHttpTokens` for `ec2:RequestSpotFleet` is **inert** (no such key on the action), while the same Deny bites `ec2:RunInstances`. *Severity:* Informational-but-AWS-owned enforcement gap.
- *Claim:* `AssociatePublicIpAddress:true` cannot be IAM-denied on the fleet path. → *Oracle:* a Deny keyed on `ec2:AssociatePublicIpAddress` is inert for `ec2:RequestSpotFleet` in SimulateCustomPolicy. *Severity:* Low–Medium (enforcement gap).

**Doc evidence:** `spot-fleet-examples.md` (grep counts above); `API_SpotFleetLaunchSpecification.md` (no MetadataOptions field); `configuring-instance-metadata-options.md` / `configuring-IMDS-new-instances.md` (opt-in default); `list_ec2.md` §3 (no keys). **Stop:** once Simulate shows the keys inert and one canary confirms token-less IMDS — do not enumerate every example.
**Precision guard (do not over-claim):** frame (a) as "the inline struct has no field + no IAM key" — NOT "AWS forgot a field it could have used"; for Ex 7–12 the IMDS posture is a *referenced-template* question, out of scope for this page.

### §5.2 — Area 2 [Lens X — twin / family authorization-parity gap] — the inline `LaunchSpecifications` path is structurally the least-scopable of three cousins
**Background.** Three request-construction cousins launch the same kind of instance: `RequestSpotFleet` inline spec (Ex 1–6), `RequestSpotFleet` launch-template (Ex 7–12), and single-instance `RequestSpotInstances`.

**Security Concern.** `RequestSpotFleet` is missing scoping machinery its cousins have:
- Its **Description carries no launch-template caveat**, unlike `CreateFleet` (list_ec2.md:5114 verbatim: *"Resource-level permissions for this action do not include the resources specified in a launch template. … you must include the resources in the RunInstances action statement"*). `RequestSpotFleet`'s Description (9466) is just *"Grants permission to create a Spot Fleet request."* `grep "do not include the resources specified in a launch template" docs/AWSEC2/` = **0 hits** — the caveat is **never published for Spot Fleet** despite the identical architecture (Ex 7–12 use `LaunchTemplateConfigs`). → whether launch-template-named resources are scoped at all on this action is undocumented.
- Its 8 rows carry **no `ec2:IsLaunchTemplateResource`/`ec2:LaunchTemplate`** keys (RunInstances/CreateFleet rows do) → no way to write a policy that distinguishes "resource named inline" from "resource pulled via template."
- It has **no `network-interface` resource row**, whereas `RequestSpotInstances` (9481) does (`ec2:NetworkInterfaceID`/`ec2:Subnet`/`ec2:Vpc`) → the inline `NetworkInterfaces[]` in Ex 2 cannot be scoped by any NIC condition key on the fleet action.

**High-level Test Scenarios.**
- *Claim:* a Deny on `ec2:Vpc`/`ec2:SubnetID` written to confine a Spot Fleet to one subnet binds the inline `SubnetId`/`NetworkInterfaces[].SubnetId` the same as the launch-template `SubnetId` override. → *Oracle:* SimulateCustomPolicy / canary request shows the condition either binds the inline value, binds only the request object, or is inert against the template path — three distinct outcomes, each a finding of its own severity. (This is the concrete, examples-page instance of **create-spot-fleet §5.7**; cite it, do not re-derive.)
- *Claim:* the NIC in Ex 2 is unscopable on the fleet path but scopable on `RequestSpotInstances`. → *Oracle:* a Deny on `ec2:NetworkInterfaceID` bites `RequestSpotInstances` and is inert for `RequestSpotFleet` in Simulate.

**Doc evidence:** list_ec2.md:5114 (CreateFleet caveat), 9466 (no caveat), 9465–9474 vs 9477–9486. **Severity-if-true:** scoping gap on a launch action = **Medium–High** (an admin believes a subnet/VPC/NIC confinement holds that doesn't). **Stop:** once the three-way Simulate outcome is settled for one key. **Cross-ref:** create-spot-fleet §5.2/§5.7.

### §5.3 — Area 3 [Lens B / R — inline instance-profile PassRole, artifact instance] — base example policy lets a caller pass *any* instance profile inline
**Background.** Examples 1–2 embed `"IamInstanceProfile": {"Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"}` directly in the inline spec.

**Security Concern.** `spot-fleet-prerequisites.md:86–91` states verbatim: *"If you specify a role for the IAM instance profile in the launch specification or launch template, you must grant the user the permission to pass the role to the service. … include `arn:aws:iam::*:role/{{IamInstanceProfile-role}}` as a resource for the `iam:PassRole` action."* — i.e. the inline instance-profile role **is** subject to `iam:PassRole`, but **the base example policy earlier in the same doc (lines 59–63) scopes `iam:PassRole` only to `arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role`** (the IamFleetRole) and relies entirely on the admin noticing the "Important" callout to add a *second* PassRole statement for instance-profile roles. There is **no `ec2:InstanceProfile`/`ec2:NewInstanceProfile` condition key on any `RequestSpotFleet` row** (RunInstances has them) to backstop it. So an admin who copies the base example literally — or who uses the common `iam:PassRole` with `Resource:"*"` — lets a caller embed **any** instance-profile ARN in `LaunchSpecifications[].IamInstanceProfile.Arn`, attaching an arbitrary (possibly higher-privileged) role to the launched instances.

**High-level Test Scenarios.**
- *Claim:* a principal holding `ec2:RequestSpotFleet` + the base-example `iam:PassRole` (IamFleetRole-only) can request a fleet whose inline spec names a *different*, more-privileged instance-profile role, and the request is authorized. → *Oracle:* under a scoped role holding exactly the base example policy, SimulateCustomPolicy for `ec2:RequestSpotFleet` + `iam:PassRole` on the foreign instance-profile ARN returns `allowed` only if PassRole is `*`/mis-scoped, `implicitDeny` if the second statement is correctly absent — settles whether the artifact fails open. Escalate to a canary fleet with a canary high-priv profile only after Simulate. *Severity-if-true:* instance-profile privesc = **High** (intra-account); AWS-authored-artifact-induced, Tier-2 reportable **iff** the base example itself is the thing a reasonable admin copies.
**Doc evidence:** prerequisites.md:59–63 (base policy) + 86–91 ("Important"); list_ec2.md:9465–9474 (no instance-profile key). **Stop:** once Simulate settles allow-vs-deny under the verbatim base policy. **Cross-ref:** create-spot-fleet §5.3 (mechanism, user-data injection), prerequisites §Lens R/P.

### §5.4 — Area 4 [NET-NEW · Lens L / U / AA — Capacity Rebalancing auto-replace + SLR terminate] — Ex 8 `launch-before-terminate`
**Background.** Ex 8 sets `SpotMaintenanceStrategies.CapacityRebalance.ReplacementStrategy = launch-before-terminate`, `TerminationDelay = 720`, with the page note *"You are charged for all instances while they are running."* No sibling develops the rebalance mechanism.

**Security Concern (from `ec2-fleet-capacity-rebalance.md`).**
- **Documented double-charge window:** `termination-delay` min **120 s**, max **7200 s** (2 h); both old and new instances bill for the overlap.
- **Service-driven termination under the SLR:** EC2 waits `termination-delay` then terminates the old instances via **`AWSServiceRoleForEC2SpotFleet` → `ec2:TerminateInstances`** — the caller needs no `TerminateInstances`. (Same SLR-terminate-without-caller-permission shape as `cancel-spot-fleet`/`modify-spot-fleet`; cross-ref those for the primitive.)
- **Documented cost-amplification ceiling:** *"Amazon EC2 can launch new replacement Spot Instances until fulfilled capacity is double target capacity … then it stops launching."* Worked example: target 100 → up to 100 replacements → fulfilled 200 before launches stop.
- **Unbounded-cost sibling mode:** with `ReplacementStrategy = launch` (not `launch-before-terminate`), EC2 does **not** auto-terminate the at-risk instances — *"you continue paying for them while they are running"* — so a config that chooses `launch` leaks instances indefinitely absent customer-wired termination.

**High-level Test Scenarios.**
- *Claim:* a rebalance event doubles fulfilled capacity (to 2× target) and bills the overlap, driven entirely by the service with no caller terminate permission. → *Oracle:* on a canary `maintain` fleet with `launch-before-terminate` + a forced/awaited rebalance recommendation, observe fulfilled capacity transiently reach 2× target and the old-instance termination appear in CloudTrail attributed to the SLR, not the caller. *Severity-if-true:* bounded cost amplification + SLR terminate = **Medium** (cost/availability; High only if combined with a mis-sized budget/SCP). 
- *Claim:* `TerminationDelay` outside [120,7200] is rejected (bounds enforced). → *Oracle:* request with `TerminationDelay:0`/`99999` returns a validation error (or silently clamps — the interesting case).
**Doc evidence:** `ec2-fleet-capacity-rebalance.md` (bounds, 2×-target, SLR terminate, `launch`-mode cost); examples note. **Stop:** once the 2×-target + SLR-attribution is observed once. **Cross-ref:** modify/cancel terminate primitives; spot-fleet-states (replacement lifecycle).

### §5.5 — Area 5 [NET-NEW · Lens L / U — attribute-based Min-only unbounded type set] — Ex 12
**Background.** Ex 12 `InstanceRequirements` sets `VCpuCount.Min:2`, `MemoryMiB.Min:4`, **no `Max`**. The page states *"Because no maximum is specified, there is no maximum limit."*

**Security Concern.** The candidate instance-type set is effectively unbounded (any type ≥2 vCPU and ≥4 MiB RAM — a trivially low floor). The *only* documented backstop is **price protection**, which `ec2-fleet-attribute-based-instance-type-selection.md` confirms is a **cost heuristic, not a type-breadth cap**, is **on by default** (OD threshold 20% over lowest-priced; Spot auto), and is **user-disable-able** (*"To indicate no price protection threshold, specify a high percentage value, such as `999999`"*). So a copy of Ex 12 with price protection widened/disabled can select arbitrarily large/expensive types.

**High-level Test Scenarios.**
- *Claim:* Ex 12 with price protection set to `999999` provisions instance types far larger than any stated intent. → *Oracle:* canary fleet; observe selected instance types unbounded above. *Severity-if-true:* cost amplification = **Low–Medium** (in scope only under a mis-sized budget/SCP/quota). **Cross-ref:** `ec2-fleet-instance-weighting-walkthrough` (overshoot) — complementary cost lead, do not restate weighting round-up here.
**Doc evidence:** examples.md:707–710; ABS page price-protection section. **Stop:** once unbounded-type selection is shown once.

### §5.6 — Area 6 [DOC-GAP · Lens B / U — cross-account IamFleetRole] — Ex 11's `111111111111`
**Background.** Every config uses account `123456789012` **except Ex 11**, whose `IamFleetRole = arn:aws:iam::111111111111:role/aws-ec2-spot-fleet-tagging-role` — a *different* account id (grep confirms 1× `111111111111`, 19× `123456789012`).

**Security Concern.** No AWS doc states the `IamFleetRole` must be in the **same account** as the caller/fleet (`API_RequestSpotFleet.md` only says "an IAM role that grants the Spot Fleet permission … on your behalf", no account scoping). Meanwhile `spot-fleet-prerequisites.md#cross-service-confused-deputy-prevention` **recommends** adding `aws:SourceArn`/`aws:SourceAccount` to the role's trust policy *"to limit the permissions that Spot Fleet gives another service"* — a recommendation that only makes sense if the **default trust (Principal `spotfleet.amazonaws.com`, no account condition) is NOT account-scoped**. The Ex 11 cross-account id + the dedicated confused-deputy section in the same doc family are suggestive but **not confirmed by prose** → live-test candidate (likely a doc typo, but the confused-deputy question is real).

**High-level Test Scenarios.**
- *Claim:* `RequestSpotFleet` accepts an `IamFleetRole` ARN in a different account than the caller and the SLR/service assumes it. → *Oracle:* two synthetic accounts; account A calls `RequestSpotFleet` naming account B's `aws-ec2-spot-fleet-tagging-role` (whose trust omits `aws:SourceAccount`); observe accept + whether B's role is assumed to launch in whose account. **HARD STOP** if the assumption implicates the service plane. *Severity-if-true:* cross-account confused deputy = **High–Critical**; if the role's trust *does* require same-account, this is a clean negative. **Precondition:** needs two canary accounts; DryRun is caller-IAM only (won't resolve the trust).
**Doc evidence:** examples.md Ex 11; API_RequestSpotFleet.md; prerequisites confused-deputy section. **Stop:** on first clear accept/deny.

### §5.7 — Area 7 [Lens U — documented validation claim] — `NetworkInterfaceID` "you can't specify it"
**Background.** Page note (examples.md:16–17): *"For Spot Fleet, you can't specify a network interface ID in a launch template or launch specification. Make sure you omit the `NetworkInterfaceID` parameter …"*

**Security Concern.** No page in the mirror states **what happens** if the parameter is present — API-level rejection vs **silent drop/ignore**. The second case is the interesting one: an operator who believes they pinned a specific ENI would actually get a fresh ENI — a provisioning-integrity/confusion bug.

**High-level Test Scenarios.**
- *Claim:* a `request-spot-fleet` with `NetworkInterfaceId` set in a launch spec/template is silently accepted and the field ignored (not rejected). → *Oracle:* DryRun / canary request with `NetworkInterfaceId` populated — observe `InvalidParameterCombination`-class rejection (safe) vs 200/silent-strip (finding). *Severity-if-true:* silent-drop = **Low–Medium** (integrity confusion; higher if the "pinned" ENI carried a security group the operator relied on).
**Doc evidence:** examples.md:16–17; no enforcement prose anywhere in mirror. **Stop:** on first reject-vs-ignore observation.

### §5.8 — Area 8 [Lens S — per-launch-spec `SpotPrice` override granularity] — Ex 4 (low)
**Background.** Ex 4 sets a fleet-level `SpotPrice:"1.00"` and per-launch-spec overrides (`0.10`/`0.20`), with one spec inheriting the fleet max. Ex 5/6 set `SpotPrice:"0.70"`.
**Security Concern.** `SpotPrice`/`MaxPrice` is a cost ceiling only; there is **no `ec2:` condition key for a price cap** (whole-doc grep for a price/`MaxPrice`/`SpotPrice` key = 0 — consistent with the on-demand-walkthrough sibling's finding). An admin cannot IAM-bound the max price a fleet request sets. **Severity:** Low (cost footgun, enforcement gap). **Cross-ref:** on-demand/instance-weighting walkthroughs for the price/strategy no-key fact — do not restate.

---

## §6 — Threat-Model Test Objectives (ranked)

| # | Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|---|
| 1 | Verbatim sample ⇒ IMDSv1 instance; no in-request lever | inline `SpotFleetLaunchSpecification` (Ex 1–6) | "secure by default" expectation; AMI/account IMDS default is the *only* backstop |
| 2 | Public IP + IMDSv1 unscopable on fleet path | `AssociatePublicIpAddress` (Ex 2) | `ec2:AssociatePublicIpAddress` (absent on `RequestSpotFleet`) |
| 3 | Arbitrary inline instance-profile via base PassRole policy | `IamInstanceProfile.Arn` (Ex 1–2) | prerequisites "Important" 2nd PassRole statement (easy to miss) |
| 4 | Launch-template-named resources unscoped (no caveat, no `IsLaunchTemplateResource` key) | `RequestSpotFleet` (Ex 7–12) | CreateFleet-style caveat — **never published for Spot Fleet** |
| 5 | Rebalance 2× target cost + SLR terminate; `launch` unbounded | `CapacityRebalance` (Ex 8) | 2×-target ceiling; `termination-delay` 120–7200 s |
| 6 | Min-only unbounded instance types | `InstanceRequirements` (Ex 12) | price protection (disable-able via `999999`) |
| 7 | Cross-account IamFleetRole confused deputy | `IamFleetRole` (Ex 11) | `aws:SourceArn`/`aws:SourceAccount` on role trust (opt-in) |
| 8 | `NetworkInterfaceId` reject-vs-silent-drop | launch spec/template | page note "omit it" (no enforcement prose) |

---

## §7 — Out-of-Scope Risk Categories (state confidently)
- **Shared/managed EC2 host infrastructure, the Spot service's own fleet, IMDS *on AWS-managed hosts*** — out of scope; IMDS concern here is on the *customer's own launched instances*, which is in scope.
- **A customer steering their own fleet / their own account's spend** where no AWS-authored artifact induced it — the cost leads (Areas 4,5,8) are in scope **only** as properties of the AWS-published sample configs or as IAM enforcement gaps, not as "the customer can spend money."
- **Customer-authored policies** — least-privilege footguns the customer wrote are out of scope; the carve-out applies to the **AWS-authored example configs and the prerequisites base policy** only.
- **`file://` as SSRF** — client-side CLI file load, no network fetch; null.
- **Cross-tenant IDOR on `sfr-<UUID>` ids** — 128-bit, not fabricable; owned by `manage-spot-fleet`/`modify-spot-fleet` as a partial-null; not re-opened here.
- **The terminate/cancel/modify primitives, lifecycle/48h decay, auto-scaling control loop, EventBridge, tag-authz** — owned by the named siblings; cross-referenced, not restated.

## §8 — Null Hypotheses, Doc Gaps, and Contradictions to Resolve
- **Lens G (SSRF) — N/A.** Pages checked: all 12 configs on `spot-fleet-examples.md`. No field the service dereferences server-side — `ImageId`/`SubnetId`/`SecurityGroups.GroupId`/`IamInstanceProfile.Arn`/`LaunchTemplateId` are identifiers the control plane resolves, not URLs/hosts it fetches; `file://` is client-side. No `*Url`/`*Uri`/webhook/discovery field exists on the page.
- **Lens Q (upload) — N/A for this page.** `UserData` is a base64 blob but is not shown populated in any example here; the user-data injection seam is owned by `create-spot-fleet §5.3`.
- **Lens A (cross-tenant IDOR) — N/A at this page.** No resource-by-id read/mutate API is exercised; `RequestSpotFleet` only creates.
- **Lens K (prompt injection) — N/A.** No LLM/agent in the pipeline.
- **Doc-gap 1 (test first):** `RequestSpotFleet` has **no published launch-template-scoping caveat** (CreateFleet does, list_ec2.md:5114) and **no `ec2:IsLaunchTemplateResource`/`LaunchTemplate` keys** — whether launch-template-named resources are scoped at all on this action is undocumented (Area 2). 
- **Doc-gap 2 (test first):** cross-account `IamFleetRole` accept/reject is undocumented (Area 6).
- **Doc-gap 3 (test first):** `NetworkInterfaceId`-present behavior (reject vs silent-drop) is undocumented (Area 7).
- **Doc-gap 4:** whether the inline instance-profile PassRole fails open under the verbatim base example policy depends on whether a reasonable admin copies the base statement without the "Important" 2nd statement — settle via Simulate before asserting (Area 3).
- **Not a contradiction, a precision note:** the `MetadataOptions` omission is **structurally forced** for Ex 1–6 (field absent from `SpotFleetLaunchSpecification`) and a **referenced-template question** for Ex 7–12 — do not over-claim it as "AWS forgot a field it could have inlined."

---
*Companion to: `create-spot-fleet-attack-research-plan.md` (mechanism layer), `spot-fleet-prerequisites-attack-research-plan.md` (IAM-artifact/PassRole/confused-deputy), `spot-fleet-attack-research-plan.md`, `modify-spot-fleet-…`/`cancel-spot-fleet-…` (terminate primitives), `ec2-fleet-instance-weighting-walkthrough-…` (overshoot), `ec2-fleet-on-demand-walkthrough-…` (price/strategy no-key), `spot-fleet-states-…` (lifecycle). See [[project-aws-research-plans]], [[reference-aws-iam-service-auth-ref-url]].*
