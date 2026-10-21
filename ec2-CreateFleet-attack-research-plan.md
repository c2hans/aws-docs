# EC2 CreateFleet — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html (+ API_FleetLaunchTemplateConfigRequest / API_FleetLaunchTemplateOverridesRequest / API_FleetInstanceMetadataOptionsRequest) and offline IAM authorization reference `docs/service-authorization/latest/reference/list_ec2.md` L5113-5123 (CreateFleet row). Cross-referenced against RunInstances / CreateImage rows in the same file. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

Related prior plans (reuse their primitives): `ec2-RunInstances-attack-research-plan.md`, `ec2-AssociateIamInstanceProfile-attack-research-plan.md`. CreateFleet is a **composite launch action** in the same family as RunInstances/CreateLaunchTemplate/RequestSpotInstances — the multi-resource fail-open move applies, PLUS a documented CreateFleet↔RunInstances cross-action authorization coupling that is unique to this action.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Preferred resource-free oracle for every authorization lead: **`iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`** — no instance launched, no cost. Escalate to a live `instant`-type CreateFleet call with a `--dry-run` or canary launch template only to confirm a simulate-positive.
- **`DryRunOperation` is caller-IAM only, NOT an ownership oracle** — it short-circuits before resource resolution. Do not use DryRun to probe cross-account resource reach.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the EC2 Fleet service-linked role `AWSServiceRoleForEC2Fleet`, Spot SLR, or any AWS-owned fleet identity), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Launch an instance that a RunInstances-scoped policy would forbid** — prove CreateFleet is a parallel launch path that bypasses resource-level controls written only on `ec2:RunInstances`.
2. **Attach an IAM role to a fleet-launched instance the caller could not attach directly** → read role creds from IMDS → privesc (the RunInstances/PassRole terminus, reached via CreateFleet).
3. **Launch on an attacker-chosen AMI** despite an image allow-list, via (a) `instant`-fleet `ImageId` override, or (b) `resolve:ssm` parameter resolution (whoAMI / SSM-alias poisoning).
4. **Launch with IMDSv1 reachable (`HttpTokens=optional`)** despite an org Deny intended to force IMDSv2 — prove the hardening condition keys do not exist on the CreateFleet authorization path.
5. **Consume a shared (cross-account, RAM) Capacity Reservation** via the `capacity-reservation` target leg without a key that pins the owner.
6. **Self-widen ABAC** by tag-on-create on a resource type whose leg omits `aws:RequestTag`.

---

## 2. Components, Assets, and Design

**Interface:** EC2 Query/JSON API action `ec2:CreateFleet` (SigV4, public regional endpoint `ec2.<region>.amazonaws.com`). Mutating, external-facing, callable by any principal holding `ec2:CreateFleet`.

**What it does:** Creates an "EC2 Fleet" — a declarative request for On-Demand + Spot capacity that **launches EC2 instances**. It is a *second launch path* alongside `RunInstances`/`RequestSpotFleet`. Three fleet `Type`s with materially different authz surface:
- `instant` — synchronous one-shot. **Unlocks per-override `ImageId`, `SubnetId`, `KeyName`, `IamInstanceProfile`, `MetadataOptions`, `BlockDeviceMapping`** (all documented "Supported only for fleets of type `instant`").
- `maintain` / `request` — asynchronous, self-healing (replenishes interrupted Spot, `ReplaceUnhealthyInstances`). These forbid per-override ImageId/profile/metadata — those come from the **launch template**.

**Assets / resources touched (from the IAM row, 8 resource-type legs):**
`fleet*` (the fleet request, tagged on create), `instance*` (the launched instances), `image`, `subnet`, `volume`, `launch-template`, `placement-group`, `capacity-reservation`.

**Identity / privilege:**
- Caller SigV4 principal needs `ec2:CreateFleet`.
- If a launch spec carries an instance profile → **`iam:PassRole`** on the contained role.
- **Service-linked role** `AWSServiceRoleForEC2Fleet` (and the Spot SLR) performs the actual asynchronous launch/replenish for `maintain`/`request` fleets — a service-plane identity (HARD STOP target).

**Where untrusted input is transformed:**
- `ImageId` override → **`resolve:ssm:…` resolver** (public param / same-account param / cross-account param-ARN) → AMI ID at launch. A name/alias-resolution seam.
- Launch template reference (ID/name + **version**, incl. `$Default`/`$Latest`) → full launch spec → RunInstances-equivalent launch.
- `Context` parameter = documented only as **"Reserved."** — an undocumented knob (flag it).

**ASCII pipeline:**
```
caller (ec2:CreateFleet)
   │  CreateFleet(LaunchTemplateConfigs[{ LT ref + Overrides[] }], Type)
   ▼
CreateFleet authz  ── 8 resource-type legs, EACH authorized independently ──┐
   │  (per doc: launch-template-EMBEDDED resources authorized via ec2:RunInstances statement, NOT CreateFleet)
   ▼                                                                         │
 instant → launch now           maintain/request → AWSServiceRoleForEC2Fleet (SLR) launches async
   ▼                                                                         ▼
 EC2 instances (profile→IMDS creds, userData root-exec, chosen AMI, subnet/VPC, volumes)
```

---

## 3. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller principal | `ec2:RunInstances`-scoped resource controls | CreateFleet is a separate action authorizing the same launch | A launch (instance running) that the RunInstances policy statements forbid = **the RunInstances resource wall was bypassed via CreateFleet** |
| Caller principal | IAM role (via instance profile → IMDS) | `IamInstanceProfile` override (instant) or profile embedded in launch template | Reading, from a fleet-launched instance's IMDS, creds of a role the caller could not `AssociateIamInstanceProfile`/`RunInstances`-pass directly |
| Caller principal | Attacker/foreign AMI | `instant` `ImageId` override OR `resolve:ssm` resolution | Fleet launches an instance from an AMI the image allow-list/`ec2:Owner`/`ec2:ImageID` Deny was meant to block |
| Caller principal | Cross-account Capacity Reservation (RAM-shared) | `capacity-reservation` target leg | Fleet instances land in / bill against a CR owned by another account with no owner-pinning condition key |
| Caller (low-priv) | IMDSv2-enforcement org guardrail | CreateFleet launch with `MetadataOptions`/template metadata | An instance launched via CreateFleet with `HttpTokens=optional` while the org Deny (keyed on `ec2:MetadataHttpTokens`) was presumed to cover all launch paths |
| Any CreateFleet holder | AWS service plane (`AWSServiceRoleForEC2Fleet`) | async launch/replenish by SLR | **HARD STOP** — any SLR credential/ARN/account surfacing = service-plane breach, disclose |

---

## 4. API / Interface Inventory

| Name | Mutating | External | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|
| `CreateFleet` | Yes | Yes | Launch On-Demand+Spot capacity | any `ec2:CreateFleet` holder | 8 resource legs; `instant` unlocks ImageId/profile/metadata overrides |
| `ModifyFleet` | Yes | Yes | Change target capacity of `maintain`/`request` fleet | holder | re-triggers SLR launches; check key parity vs CreateFleet |
| `DeleteFleets` | Yes | Yes | Delete fleet (+optionally terminate instances) | holder | revocation/teardown completeness (Lens AA) |
| `DescribeFleets` / `DescribeFleetInstances` / `DescribeFleetHistory` | No | Yes | Enumerate fleets + launched instances | holder | recon; check resource-type scoping / region-only |
| `CreateLaunchTemplate` / `CreateLaunchTemplateVersion` / `ModifyLaunchTemplate` | Yes | Yes | Author/mutate the launch spec CreateFleet consumes | holder | **late-binding `$Default`/`$Latest` pivot** |

**Undocumented / console-hidden knobs (Step-3 hunt):**
- `Context` — "Reserved." Accepted by the API, no documented semantics. Probe: does it accept arbitrary strings, reach a downstream, or appear in CloudTrail?
- `instant`-only overrides (`ImageId`, `SubnetId`, `KeyName`, `IamInstanceProfile`, `MetadataOptions`) are reference-documented but **thinly surfaced in console** — the most permissive values (foreign AMI, `resolve:ssm` cross-account ARN, `HttpTokens=optional`) warrant the undocumented-knob treatment.

---

## 5. Recommended Areas of Focus

### AREA 1 — CreateFleet as a RunInstances-bypass launch path *(CROWN JEWEL — Lens X / U / S, High–Critical)*
**Background:** The IAM reference states verbatim (list_ec2.md L5114): *"Resource-level permissions for this action do not include the resources specified in a launch template. To specify resource-level permissions for resources specified in a launch template, you must include the resources in the RunInstances action statement."* CreateFleet launches instances but its own resource legs do **not** cover launch-template-embedded resources — those are governed by the separate `ec2:RunInstances` statement.

**Security Concern:** A policy author who scopes the launch surface on **`ec2:RunInstances`** (the obvious action) but grants **`ec2:CreateFleet`** broadly has two decoupled actions purporting to control one capability. Conversely, an org that *Denies* `ec2:RunInstances` for certain AMIs/subnets/SGs but leaves `ec2:CreateFleet` allowed may still permit those launches through the fleet path, depending on whether the engine evaluates the RunInstances statement for template-embedded resources at fleet-launch time. This is the action-family/twin parity shape (Lens X), applied to a *write twin of a launch*, not a read.

**High-level Test Scenarios:**
- **Claim:** A principal with `ec2:CreateFleet` + `ec2:RunInstances` (Resource:\* on RunInstances) but an org Deny on `ec2:RunInstances` for `image/ami-FORBIDDEN` can still launch that AMI via a launch template referenced by CreateFleet. → **Oracle:** `SimulatePrincipalPolicy` for `ec2:CreateFleet` returns allowed while `ec2:RunInstances` on the same AMI returns denied; confirm with an `instant` fleet launch. Severity: **High** (resource-wall bypass), **Critical** if the forbidden AMI/subnet reaches a cross-account resource.
- **Claim:** A principal holding ONLY `ec2:CreateFleet` (no `ec2:RunInstances` statement at all) can still launch instances via a launch template. → tests whether the "must include RunInstances statement" is a *requirement* (fail-closed, good) or merely *advisory for resource-scoping* (the instances launch with no RunInstances authz at all = bypass).
- **Adjacent (Lens X sibling):** check `ModifyFleet` target-capacity increase re-launches through the SLR — does it re-authorize the launch spec, or only check `ec2:ModifyFleet`? A `maintain` fleet created once then grown via ModifyFleet may launch unauthorized capacity.

**Doc evidence:** list_ec2.md L5113-5123; API_CreateFleet request params (`LaunchTemplateConfigs` required). **Severity-if-true:** High–Critical.

---

### AREA 2 — IMDSv2-hardening condition keys absent on the CreateFleet path *(Lens S / U, High)*
**Background:** CreateFleet's `instance*` leg (L5118) carries: AvailabilityZone(Id), CpuOptionsAmdSevSnp, EbsOptimized, InstanceBandwidthWeighting, InstanceID, **InstanceProfile**, InstanceType, PlacementGroup, Region, RootDeviceType, Tenancy. It **lacks** `ec2:MetadataHttpTokens`, `ec2:MetadataHttpEndpoint`, `ec2:MetadataHttpPutResponseHopLimit`, `ec2:InstanceMetadataTags`, `ec2:InstanceAutoRecovery`, `ec2:InstanceMarketType`, `ec2:ProductCode`, `ec2:ManagedResourceOperator` — **all of which are present on the `CreateImage`/`RunInstances` instance\* leg** (compare L5145). Yet the `instant` fleet supports a full `MetadataOptions` (`FleetInstanceMetadataOptionsRequest`) override.

**Security Concern:** An org that enforces IMDSv2 with a Deny on `ec2:MetadataHttpTokens != required` believes it covers all instance launches. That Deny is **inert on the CreateFleet path** because the key is not populated for `ec2:CreateFleet`. A caller launches a fleet instance with `HttpTokens=optional` (IMDSv1 reachable by plain SSRF), and the guardrail never fires. Same logic for `MetadataHttpPutResponseHopLimit` (hop-limit >1 lets containers reach IMDS) and `InstanceMetadataTags`.

**High-level Test Scenarios:**
- **Claim:** `SimulatePrincipalPolicy` for `ec2:CreateFleet` with context `ec2:MetadataHttpTokens=optional` returns **allowed** even under a Deny that blocks the same context on `ec2:RunInstances`. → Oracle: simulate both actions; the delta proves the key is not evaluated for CreateFleet.
- **Claim:** An `instant` fleet with `MetadataOptions.HttpTokens=optional` launches successfully in an account whose SCP forbids IMDSv1 launches. Severity: **High** (re-opens the IMDSv1 SSRF→credential primitive org-wide).
- **Refute condition:** if AWS evaluates the embedded-launch via the RunInstances statement (Area 1), these keys *might* be enforced through that path — test both.

**Doc evidence:** L5118 vs L5145; `FleetInstanceMetadataOptionsRequest`. **Severity-if-true:** High.

---

### AREA 3 — Role attach → IMDS cred privesc via fleet-launched instance *(Lens B / E, Critical)*
**Background:** `FleetLaunchTemplateOverridesRequest.IamInstanceProfile` (instant) and launch-template-embedded instance profiles let CreateFleet attach an IAM role to the launched instance. The `instance*` leg carries `ec2:InstanceProfile`, but **not** `ec2:NewInstanceProfile` (that key exists only on Associate/ReplaceIamInstanceProfile — see `ec2-associate-iam-instance-profile-surface`). Passing a profile requires `iam:PassRole`, which binds the **role** ARN, not the profile; profile/role names are decoupled and profile membership is mutable.

**Security Concern:** CreateFleet is a *third* path (after RunInstances and AssociateIamInstanceProfile) to get a role's creds onto an instance you control → read from IMDS → act as the role. Any org Deny keyed on `ec2:NewInstanceProfile` (to forbid attaching profile X) is **inert** on CreateFleet (key not present). The `iam:PassRole` prefix-wildcard footgun from AWS sample policies (`role/DevTeam*`) applies identically.

**High-level Test Scenarios:**
- **Claim:** With `iam:PassRole` scoped to `role/TestRole-*` and `ec2:CreateFleet` on Resource:\*, a caller launches an instant fleet attaching `TestRole-admin` → IMDS creds = admin. Oracle: `SimulatePrincipalPolicy(iam:PassRole, ec2:CreateFleet)`; confirm with instant launch + IMDS GET. Severity: **Critical** (scales with passed role).
- **Claim:** An org Deny on `ec2:NewInstanceProfile=profile/forbidden` does not block CreateFleet attaching that profile. Oracle: simulate — key absent → allowed.
- **Chain:** CreateFleet (attach role) → `maintain` fleet → SLR keeps replenishing instances with that role even after the caller's session ends (persistence). HARD STOP if SLR creds surface.

**Doc evidence:** `FleetLaunchTemplateOverridesRequest.IamInstanceProfile`; L5118 (`ec2:InstanceProfile` present, `ec2:NewInstanceProfile` absent); UG permission-to-pass-iam-roles. **Severity-if-true:** Critical.

---

### AREA 4 — AMI selection: `instant` ImageId override + `resolve:ssm` authenticity omission *(Lens U authenticity-filter / Lens EE / Lens A, High)*
**Background:** `ImageId` (instant override) accepts a literal `ami-…` **or** `resolve:ssm:public-parameter`, `resolve:ssm:parameter-name[:version|:label]`, or a **cross-account** `resolve:ssm:parameter-ARN`. The resolver maps the name/ARN to an AMI ID at launch. The `image` resource leg has `ec2:Owner`, `ec2:Public`, `ec2:ImageID`, `ec2:ImageType`, `ec2:RootDeviceType` keys.

**Security Concern:** Two selection seams:
1. **whoAMI / name-resolution:** does the `image`-leg condition key (`ec2:Owner`/`ec2:ImageID`) evaluate against the **resolved** AMI, or is resolution done *after* authz so a `resolve:ssm` reference bypasses an `ec2:ImageID` allow-list? If authz sees the SSM string and not the resolved ami-id, an `ec2:ImageID=ami-TRUSTED` allow-list is defeated.
2. **SSM-alias poisoning (Lens EE):** a cross-account `resolve:ssm:parameter-ARN` resolves a parameter the caller doesn't own → attacker-controlled parameter points at an attacker AMI. Does the fleet pin the parameter owner? Combined with the Area-1 launch-template-resource gap, the AMI in a template may dodge CreateFleet's `image` leg entirely.

**High-level Test Scenarios:**
- **Claim:** An `instant` fleet with `ImageId=resolve:ssm:/attacker/param` launches a non-allow-listed AMI despite an `ec2:ImageID`-scoped policy. Oracle: simulate with the resolved vs unresolved value; confirm with a canary parameter → own AMI.
- **Claim:** `ImageId` override on an instant fleet overrides a launch-template AMI pin that a template-scoped grant assumed was fixed. Severity: **High** (launch arbitrary/backdoored AMI as caller).

**Doc evidence:** `FleetLaunchTemplateOverridesRequest.ImageId` (resolve:ssm formats incl. cross-account ARN); L5117 image leg keys. **Severity-if-true:** High.

---

### AREA 5 — Launch-template late-binding / version drift *(Lens S / X, Medium–High)*
**Background:** The `launch-template` resource leg (L5119) has only `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag` — **no version segment** in the scoping. CreateFleet references a template by ID/name and a version that can be `$Default` or `$Latest`.

**Security Concern:** A grant scoped to `launch-template/lt-ABC` does not pin a **version**. A lower-privileged principal with `ec2:ModifyLaunchTemplate` (change `$Default`) or `CreateLaunchTemplateVersion` can mutate what `lt-ABC` launches — AMI, instance profile, userData, SGs — *after* the CreateFleet grant was written. The CreateFleet caller then launches the mutated spec. "Reference template lt-ABC" is an illusory pin.

**High-level Test Scenarios:**
- **Claim:** Changing a launch template's `$Default` version (or adding a `$Latest`) causes a `launch-template/lt-ABC`-scoped CreateFleet grant to launch a spec with a different AMI/profile/userData than when the grant was authored. Oracle: create fleet referencing `$Default`, flip default to a version with an admin instance profile, re-create fleet. Severity: **High** (pivot to Area 3 privesc).
- **Adjacent:** whoever holds `CreateLaunchTemplateVersion` but not `CreateFleet` can still weaponize the template that a CreateFleet holder will consume (split-privilege gadget).

**Doc evidence:** L5119 (no version in scoping); `FleetLaunchTemplateSpecificationRequest` (version incl. $Default/$Latest). **Severity-if-true:** Medium–High.

---

### AREA 6 — Cross-account Capacity Reservation targeting *(Lens A / AA, Medium–High)*
**Background:** CreateFleet has a `capacity-reservation` resource leg (L5115) with keys `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag` only — no owner/account/sharing key. Capacity Reservations are RAM-shareable across accounts/orgs.

**Security Concern:** A fleet can target a shared CR. Nothing in the CreateFleet authorization pins *which account's* CR, nor whether the caller is an authorized consumer beyond server-side RAM state. A consumer could land instances into (and bill against) a foreign CR, or a CR revoked/unshared mid-flight (Lens AA) may still back a `maintain` fleet's replenishment.

**High-level Test Scenarios:**
- **Claim:** A `maintain` fleet targeting a RAM-shared CR keeps consuming it after the owner unshares (revocation incompleteness). Oracle: share CR → create maintain fleet → unshare → observe continued replenishment. Severity: **Medium–High** (cross-account capacity/billing).
- **Claim:** No condition key lets the CR *owner* restrict which consumer accounts' fleets target it. Confirm absence in list_ec2.md CR leg + capacity-reservation resource keys.

**Doc evidence:** L5115. **Severity-if-true:** Medium–High.

---

### AREA 7 — Tag-on-create ABAC self-widening *(Lens I / S, Medium)*
**Background:** `aws:RequestTag`/`aws:TagKeys` appear only on the `fleet*`, `instance*`, and `volume` legs — **not** on image/launch-template/subnet/placement-group/capacity-reservation. `TagSpecification` tags fleet + (instant) instance/volume/network-interface.

**Security Concern:** A caller can self-assign (via TagSpecification) the tag that a downstream `aws:ResourceTag`-gated lifecycle policy (Stop/Terminate/Modify) keys on — self-widening ABAC. And an ABAC Deny that assumes `aws:RequestTag` covers "the launch" does not constrain the image/subnet/LT choice (those legs lack the key).

**High-level Test Scenarios:**
- **Claim:** `CreateFleet` with `TagSpecification[instance]{Owner=victim-team}` mints instances pre-tagged to satisfy a `aws:ResourceTag/Owner=victim-team`-gated grant the caller otherwise lacks. Oracle: simulate the downstream action post-tag. Severity: **Medium** (High if ABAC is the sole access control).

**Doc evidence:** L5116/5118/5122 (RequestTag present) vs L5115/5117/5119/5120/5121 (absent). **Severity-if-true:** Medium.

---

### AREA 8 — SubnetId override / VPC targeting *(Lens S, Medium)*
**Background:** `SubnetId` is an instant override; the `subnet` leg (L5121) carries `ec2:SubnetID`, `ec2:Vpc`, `ec2:AvailabilityZone`. Note `ec2:Vpc` historically binds the resource's home VPC — confirm it constrains the *target* subnet's VPC here, not something else (the `ec2:Vpc`-binds-wrong-resource failure shape from Lens S).

**Security Concern:** Launching into a subnet/VPC the caller shouldn't use (e.g. a shared-VPC subnet, or a subnet with privileged SG/route posture). Confirm the subnet leg actually gates the override and isn't bypassed through the launch-template path (Area 1).

**Doc evidence:** L5121; `FleetLaunchTemplateOverridesRequest.SubnetId`. **Severity-if-true:** Medium.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| CreateFleet launches resources a RunInstances policy forbids | authz engine, 8-leg row | "must include resources in the RunInstances action statement" (advisory, not enforced?) |
| IMDSv1 launch under an IMDSv2 org Deny | instance\* leg | `ec2:MetadataHttpTokens` — **absent** on CreateFleet |
| Attach admin role → IMDS privesc | IamInstanceProfile override / template | `iam:PassRole` (binds role not profile); `ec2:NewInstanceProfile` **absent** |
| Launch attacker/foreign AMI | ImageId override + resolve:ssm | `ec2:Owner`/`ec2:ImageID`/`ec2:Public` (resolution-order dependent) |
| Version-drift template hijack | launch-template leg | `ec2:ResourceTag` scoping — **no version segment** |
| Cross-account CR consumption | capacity-reservation leg | RAM state only; no owner condition key |
| ABAC self-widen via tag-on-create | TagSpecification | `aws:RequestTag` present on some legs, absent on others |

---

## 7. Out-of-Scope Risk Categories
- IMDS reachability *on a fully-managed AWS host* (not applicable — fleet instances are customer-owned).
- Single-tenant self-DoS (launching too much of your own capacity / hitting your own quotas).
- The `AWSServiceRoleForEC2Fleet` / Spot SLR internals — **HARD STOP**, service-plane; do not probe, disclose if surfaced.
- Spot pricing/interruption behavior (product behavior, not a boundary).
- Customer-authored launch templates / policies that are over-broad by the customer's own choice (least-priv footgun) — **except** any AWS-published sample policy/CFN that ships these (Tier-2, in scope, route aws-security).
- DNS rebinding against private-only endpoints.

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF):** No server-side-fetch URL field on CreateFleet itself. `resolve:ssm` is a name-resolution seam (Area 4), not an HTTP fetch — not SSRF. Checked: API_CreateFleet + both override structs. **Null (SSRF).**
- **Lens F (injection/wire-protocol):** no translation layer / parser of attacker blobs in CreateFleet; inputs are typed enums/IDs. Checked request params. **Null.**
- **Lens K (prompt injection):** no LLM/agent in path. **Null.**
- **Lens FF/J (JWT/OAuth):** SigV4 only; no token/OAuth surface. **Null.**
- **Lens Y (transport/sig):** standard SigV4 EC2 endpoint; no CreateFleet-specific transport claim. Generic EC2 Query-API SigV2/HTTP concerns tracked in `ec2-devguide-monitor-apimetrics-surface` / `ec2-api-reference-wide-surface`, not re-opened here. **Deferred.**
- **`Context` parameter ("Reserved."):** **doc-gap — confirm surface first.** Undocumented semantics; probe whether it accepts arbitrary values, reaches a downstream, or logs.
- **Area 1 enforcement direction:** whether the "RunInstances statement governs template-embedded resources" is fail-closed (requirement) or advisory is **the single most important thing to settle live** — it determines whether Areas 2/3/4 are enforced through the RunInstances path or genuinely open on CreateFleet. doc-gap — confirm with `SimulatePrincipalPolicy` on both actions.

---
*Plan authored 2026-10-20 from AWS public documentation. No live testing performed.*
