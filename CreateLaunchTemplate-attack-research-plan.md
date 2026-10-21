# EC2 CreateLaunchTemplate — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html + API_RequestLaunchTemplateData.html (online, fetched 2026-10-21); offline mirror `./aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (CreateLaunchTemplate rows L5253-5257, CreateLaunchTemplateVersion L5259-5262, ModifyLaunchTemplate L8940-8942, launch-template resource L9967, key defs L10105/10109/10111); `./aws-docs/docs/AWSEC2/latest/UserGuide/permissions-for-launch-templates.md`; `ExamplePolicies_EC2.md` (L757/855/882/912/954 sample policies, L1692-1693 ASG recheck gap). Status: **documentation-derived hypotheses only; nothing tested against a live account.** Cross-references existing memory `[[ec2-multiresource-action-failopen-scoping]]`, `[[ec2-createfleet-surface]]`, `[[ec2-startinstances-lifecycle-bootprimitive]]`, `[[ec2-associate-iam-instance-profile-surface]]`.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **The resource-free oracle for almost every lead here is `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`** — CreateLaunchTemplate is a pure data-staging action, so you can prove the authz gap without launching anything. Escalate to a live `CreateLaunchTemplate` + scoped `RunInstances` only with synthetic/canary profiles, AMIs, and user data.
- **`DryRun` is caller-IAM only, NOT an ownership/content oracle** — it is evaluated before resource resolution. Do not treat `DryRunOperation` as proof the embedded AMI/profile/SG was validated.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. an SLR such as `AWSServiceRoleForAutoScaling` / `AWSServiceRoleForEC2Fleet` launching a drifted template), stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Stage a privileged launch spec with no content authz:** create a launch template (LT) containing an admin IAM instance profile, root-executing UserData, IMDSv1-enabled MetadataOptions, a cross-account/`resolve:ssm` AMI, and `0.0.0.0/0` security groups using **only `ec2:CreateLaunchTemplate`** (no `ec2:RunInstances`, no `iam:PassRole`, no resource-level grant on any embedded resource). Objective proven if the LT is created with all of the above and SimulatePolicy shows the embedded references were never authorized at create time.
2. **Version-drift / late-binding escalation:** given a `RunInstances` grant pinned to `ec2:LaunchTemplate=lt-X` (the intended guardrail), mutate the template's content after the grant — via `CreateLaunchTemplateVersion` + `$Latest`/`$Default` — so a consuming principal (or an Auto Scaling group / EC2 Fleet) launches the attacker's spec. Proven if the consumer launches the mutated spec with **no re-check** of the original resource-level/IMDSv2 restrictions.
3. **ABAC self-widening:** create an LT tagged with the exact key/value that a downstream `aws:ResourceTag`-gated `CreateLaunchTemplateVersion`/`ModifyLaunchTemplate`/`RunInstances` policy keys on, defeating the tag gate from inside one call.
4. **Confirm the documented mitigation is prose-only:** AWS says "only trusted administrators" should hold `ec2:CreateLaunchTemplate` because resource-level permissions *cannot* restrict embedded content. Prove there is no IAM condition key that enforces this, so a least-privilege reviewer who grants `CreateLaunchTemplate` has unknowingly granted the staging primitive.

## 2. Components, Assets, and Design

**What it is.** `CreateLaunchTemplate` creates a *launch template* — a stored, versioned data container of instance-launch parameters (`RequestLaunchTemplateData`). It **does not launch anything**. The template is later *consumed* by `RunInstances`, `CreateFleet`/EC2 Fleet, Spot Fleet, and EC2 Auto Scaling groups. CreateLaunchTemplate is the **authoring half** of the RunInstances-family launch chain; all compute/privilege effects are deferred to a separate consumption action.

**Resource & identifier shape.** `arn:${Partition}:ec2:${Region}:${Account}:launch-template/${LaunchTemplateId}` (`lt-0a20c965061f64abc`, 17 hex chars). Owned intra-account. **No version segment in the ARN** (L9967) — the ARN names the template, never a specific version. Versions are integers; `$Default` and `$Latest` are late-binding aliases.

**Identity.** SigV4 IAM only. No tokens, no 3P OAuth, no JWT, no OIDC, no SCRAM.

**Embedded resource references carried in `RequestLaunchTemplateData` (all optional, none authorized at create):**
- `ImageId` — AMI id **or** `resolve:ssm:<public-param | parameter-name | parameter-ARN>` (SSM alias, incl. **cross-account parameter-ARN**). Resolves to an AMI only at launch.
- `IamInstanceProfile` — name or ARN of an IAM instance profile (the privilege-escalation leg).
- `UserData` — base64, 16 KB; executed as root at boot. **No `ec2:UserData*` condition key exists anywhere in EC2.**
- `MetadataOptions` — `HttpTokens` (IMDSv1 vs IMDSv2), `HttpEndpoint`, `HttpPutResponseHopLimit`, `InstanceMetadataTags`.
- `SecurityGroup.N` / `SecurityGroupId.N` — names/IDs; or inside `NetworkInterface.N`.
- `NetworkInterface.N` / `SecondaryInterface.N` — subnet, public-IP association, ENI id.
- `BlockDeviceMapping.N` — EBS from snapshot ids, `KmsKeyId`, `Encrypted`, `DeleteOnTermination`.
- `KeyName`, `CapacityReservationSpecification`, `Placement` (Tenancy/host/affinity), `InstanceMarketOptions`, `DisableApiStop`, `DisableApiTermination`, `LicenseSpecification`.
- `TagSpecification.N` (inside the data) — tags applied to the **launched resources**, not the template.
- `Operator` (`OperatorRequest`) — on both the action and the data; "Reserved for internal use" / "the entity that manages the launch template" (console-hidden knob → Step 3 undocumented-knob hunt).

**Top-level request params:** `LaunchTemplateName` (required), `LaunchTemplateData` (required), `TagSpecification.N` (tags on the LT itself), `VersionDescription`, `ClientToken`, `DryRun`, `Operator`.

**ASCII pipeline:**
```
 [principal w/ ec2:CreateLaunchTemplate ONLY]
        │  CreateLaunchTemplate(LaunchTemplateData = {admin profile, root userData,
        │                        IMDSv1, resolve:ssm AMI, 0.0.0.0/0 SG, foreign snapshot})
        ▼
 ┌─────────────────────────────┐   authz check here = launch-template* + {RequestTag,TagKeys,Region} ONLY
 │  launch-template  lt-X  v1   │   ← embedded resource refs are NEVER authorized at create
 │  (versioned data container)  │
 └─────────────┬───────────────┘
   CreateLaunchTemplateVersion → v2 (mutated)    ModifyLaunchTemplate → set $Default
        │  ($Latest / $Default late-binding; ARN has no version segment)
        ▼
 [consumer]  RunInstances / CreateFleet / Spot Fleet / Auto Scaling group
        │  ← ec2:RunInstances resource-level perms + ec2:IsLaunchTemplateResource
        │     enforced HERE (if the consumer policy was written to) — and NOT re-checked
        │     on new version for ASG using $Latest/$Default (AWS-acknowledged)
        ▼
 EC2 instance boots: root UserData runs, admin instance-profile creds vended via IMDS
```

## 3. API / Interface Inventory

| Name | Method | New/Exist | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| CreateLaunchTemplate | SigV4 Query/SDK | Existing | **Mutating** | External | Create LT v1 (data container) | Yes (ec2 endpoint) | anyone w/ `ec2:CreateLaunchTemplate` | **Authz = `launch-template*` + `aws:RequestTag`,`aws:TagKeys`,`ec2:Region` ONLY.** No key references any embedded resource. |
| CreateLaunchTemplateVersion | SigV4 | Existing | **Mutating** | External | Add a new content version | Yes | `ec2:CreateLaunchTemplateVersion` | Keys: `aws:ResourceTag`,`ec2:ManagedResourceOperator`,`ec2:Region`,`ec2:ResourceTag`. **No `ec2:Attribute`** (ModifyLaunchTemplate has it → Lens X asymmetry). Content still un-authorized. |
| ModifyLaunchTemplate | SigV4 | Existing | Mutating | External | Set `$Default` version | Yes | `ec2:ModifyLaunchTemplate` | Keys add `ec2:Attribute`/`ec2:Attribute/${AttributeName}`. Does not change content, only which version is default. |
| DeleteLaunchTemplate / DeleteLaunchTemplateVersions | SigV4 | Existing | Mutating | External | Delete LT/versions | Yes | `ec2:Delete…` | `launch-template*` only. Deleting a LT an ASG/Fleet depends on → availability impact (doc "Important" warning). |
| DescribeLaunchTemplates / DescribeLaunchTemplateVersions | SigV4 | Existing | Non-mutating | External | List/read LT + full data | Yes | `ec2:Describe…` — **Resource `"*"`, no resource-level perms, no conditions** (doc-stated) | Read side: exposes every LT's full launch spec account-wide incl. UserData, profiles, SG, snapshot ids. Recon + see Lens A intra-account. |

**Undocumented-knob hunt:** `Operator`/`OperatorRequest` on both the action and the data is "Reserved for internal use" and not surfaced in the console or prose — probe what values the control-plane API accepts and whether setting it influences `ec2:ManagedResourceOperator` evaluation on downstream `CreateLaunchTemplateVersion`/`RunInstances` (that key = "presence of an EC2 operator provisioning a managed resource"). A caller-settable `Operator` that flips `ec2:ManagedResourceOperator` could satisfy/评 a managed-resource condition. Doc-gap — confirm the field's accepted values live.

## 4. Boundary-lens catalog

### Area 1 — Content-ungoverned staging primitive (Lens U + R/S + multi-resource fail-open) — **PRIMARY**
Background: `CreateLaunchTemplate` authorizes against exactly one resource type (`launch-template*`) and three condition keys (`aws:RequestTag`, `aws:TagKeys`, `ec2:Region`). Every embedded reference in `RequestLaunchTemplateData` — AMI, IAM instance profile, security groups, snapshots, key pair, network interfaces, UserData, MetadataOptions — is **not an authorization input at all**.

Security Concern: AWS states this verbatim (`permissions-for-launch-templates.md`, **Important**): *"You can't use resource-level permissions to restrict the resources that users can specify in a launch template when they create a launch template or launch template version. Therefore, make sure that only trusted administrators are granted permission to create launch templates and launch template versions."* The sole documented mitigation is prose ("trust only admins") — there is no IAM mechanism. A least-privilege policy author who grants `ec2:CreateLaunchTemplate` (e.g. to a CI role or a developer) has unknowingly granted the ability to stage a fully weaponized launch spec.

High-level Test Scenarios (falsifiable claims):
- **Claim:** A principal holding only `ec2:CreateLaunchTemplate` can create an LT whose `LaunchTemplateData.IamInstanceProfile` names an admin profile they have no `iam:PassRole` for, whose `UserData` is a root reverse shell, whose `MetadataOptions.HttpTokens=optional` (IMDSv1), and whose `ImageId=resolve:ssm:<cross-account-ARN>`. → **Mechanism:** action row L5255-5256 (keys = RequestTag/TagKeys/Region only); `RequestLaunchTemplateData` fields all `Required: No` and un-keyed. → **Oracle:** `SimulatePrincipalPolicy` for `ec2:CreateLaunchTemplate` returns `allowed` with those values present; live `CreateLaunchTemplate` succeeds and `DescribeLaunchTemplateVersions` echoes the spec. **No `iam:PassRole` is evaluated at create.** → **Preconditions:** `ec2:CreateLaunchTemplate` only. → **Cost:** one API call. → **Severity:** the staging call itself = Medium (no compute yet); escalates to the terminus in Area 2.
- **Claim:** There is no condition key by which a policy author *could* restrict the embedded profile/AMI/SG/userdata at create time even if they wanted to. → **Oracle:** enumerate the action's keys — absent are `ec2:InstanceProfile`, `ec2:ImageID`, `ec2:Owner`, `ec2:Public`, `ec2:MetadataHttpTokens`, `ec2:NewInstanceProfile`, any `ec2:UserData*`, `ec2:Vpc`/`ec2:SecurityGroupID`. All of these exist on `RunInstances`'s per-resource legs (L9949 instance leg, L9945 image leg, L9996 SG leg) but **none attach to `CreateLaunchTemplate`**. → **Severity:** Low/Informational as a pure doc-vs-enforcement finding, but it is the root cause that makes Area 2 Critical; AWS-owned, worth filing as the enforcement-gap behind the prose guarantee.

Doc evidence: `permissions-for-launch-templates.md` Important block; `list_ec2.md` L5253-5257. Severity-if-true: Medium at the staging boundary; the gap is the enabler for Critical.

### Area 2 — Version-drift / `$Latest`-`$Default` late-binding escalation (Lens X + Lens B/E PassRole-adjacent + Lens AA) — **CROWN JEWEL, kill chain**
Background: the launch-template ARN has no version segment (L9967). The intended guardrail for deferring content governance is a `RunInstances` policy that pins `ec2:LaunchTemplate=lt-X` and/or `ec2:IsLaunchTemplateResource=true` ("Filters access by whether users are able to override resources that are specified in the launch template", L10105) — forcing consumers to use the admin-reviewed template. But the *content* of `lt-X` is mutable after the grant, and the pin does not name a version.

Security Concern: AWS acknowledges the re-check gap for Auto Scaling, verbatim (`ExamplePolicies_EC2.md` L1693): *"For an Auto Scaling group that is configured to use the `Latest` or `Default` launch template, the permissions are not checked when a new version of the launch template is created. For permissions to be checked, you must configure the Auto Scaling group to use a specific version of the launch template."* And L1693: *"Restrictions on the use of IMDSv1 on IAM principals for RunInstances are only checked when an Auto Scaling group … is created or updated."* So a lower-privileged principal who can only add a version can swap in IMDSv1 + an admin profile + root UserData, and the next scale-out launches it with the SLR's identity and **no RunInstances/IMDSv2 re-authorization**.

High-level Test Scenarios:
- **Claim (ASG / Fleet drift — HARD-STOP terminus):** An ASG or EC2 Fleet references `lt-X` at `$Latest`/`$Default`. A principal with `ec2:CreateLaunchTemplateVersion` on `lt-X` (and nothing else of value) creates v2 with an admin `IamInstanceProfile`, `HttpTokens=optional`, and root `UserData`. On the next scale-out, `AWSServiceRoleForAutoScaling`/`AWSServiceRoleForEC2Fleet` launches v2; the original `ec2:RunInstances` resource-level + IMDSv2 restrictions are **not re-evaluated**. → **Mechanism:** L1692-1693; version-less ARN L9967; `IsLaunchTemplateResource` pin does not pin a version. → **Oracle:** confirm the ASG/Fleet uses `$Latest`/`$Default`; create v2; observe the new instance boots with the admin profile and IMDSv1 reachable. **If the launching identity is an AWS SLR, STOP and flag for disclosure** — this is the shared-responsibility line. → **Preconditions:** `ec2:CreateLaunchTemplateVersion` on the target LT; an existing `$Latest`/`$Default`-referencing ASG/Fleet. → **Cost:** one version-create + wait for scale. → **Severity:** Critical (privesc to an admin role + IMDSv1, un-rechecked, via a service-plane launcher).
- **Claim (RunInstances consumer drift):** A consumer holds `ec2:RunInstances` + `iam:PassRole`-free policy pinned to `ec2:LaunchTemplate=lt-X` + `ec2:IsLaunchTemplateResource=true`. A separate low-priv principal sets `lt-X` `$Default` to a malicious version (needs `ec2:ModifyLaunchTemplate`) or adds a `$Latest` version (needs only `ec2:CreateLaunchTemplateVersion`). The consumer's next launch uses the mutated content. → **Oracle:** `SimulatePrincipalPolicy` shows the consumer's RunInstances pin still "allowed" after content change (the ARN condition can't see the version); live launch materializes the drifted profile/userdata. → **Severity:** High–Critical depending on the profile reachable.
- **Claim (Lens X asymmetry — bypass a ModifyLaunchTemplate Deny):** A guardrail Denies `ec2:ModifyLaunchTemplate` (keyed on `ec2:Attribute`, which `ModifyLaunchTemplate` has but `CreateLaunchTemplateVersion` does **not** — L5262 vs L8942) to stop default-version changes. For any consumer referencing `$Latest`, that Deny is inert: `CreateLaunchTemplateVersion` alone makes the new version live without ever touching `ModifyLaunchTemplate`. → **Oracle:** Simulate both actions; show the Deny matches ModifyLaunchTemplate but not CreateLaunchTemplateVersion, and `$Latest` consumers pick up the new version. → **Severity:** High (guardrail-bypass enabling Area 2 terminus).

Doc evidence: `ExamplePolicies_EC2.md` L1692-1693; `list_ec2.md` L9967, L5259-5262, L8940-8942, L10105. Severity-if-true: **Critical**.

### Area 3 — Tag-on-create ABAC self-widening (Lens I / S)
Background: `CreateLaunchTemplate` carries `aws:RequestTag`/`aws:TagKeys` (tag the LT at create). `CreateLaunchTemplateVersion`, `ModifyLaunchTemplate`, `DeleteLaunchTemplate`, and tag-gated `RunInstances` policies gate on `aws:ResourceTag`/`ec2:ResourceTag` of the LT.
Security Concern: a caller who can create an LT with an arbitrary tag can self-assign the exact tag that a downstream `aws:ResourceTag`-gated policy keys on (e.g. the sample `aws:ResourceTag/purpose=testing` gate in `permissions-for-launch-templates.md`, or the `Purpose=Webservers` RunInstances gate at `ExamplePolicies_EC2.md` L954), defeating the intended scoping within the lifecycle of one resource they created.
High-level Test Scenarios:
- **Claim:** `CreateLaunchTemplate` with `TagSpecification{launch-template, purpose=testing}` then `CreateLaunchTemplateVersion`/`RunInstances` succeeds against a policy that gates those actions on `aws:ResourceTag/purpose=testing`. → **Oracle:** Simulate the create (RequestTag allowed) then the version/launch (ResourceTag now satisfied). Check whether `ec2:CreateTags` with `ec2:CreateAction=CreateLaunchTemplate` is additionally required and whether that itself is scoped. → **Severity:** Medium (High where the tag *is* the access-control mechanism for the downstream launch).
- **Claim:** `aws:TagKeys` enforcement is bypassable by omitting the tag at create when the gate is phrased as "require tag" but not "deny create without tag" (fail-open-on-omit shape seen on other EC2 tag-gated creates). → **Oracle:** Simulate create with no TagSpecification against the tag-requiring policy; expect allowed = fail-open. → **Severity:** Medium.

Doc evidence: `list_ec2.md` L5256 vs L5262; `permissions-for-launch-templates.md` sample policies. Severity-if-true: Medium–High.

### Area 4 — AWS-published sample-policy audit (Lens R / S)
Background: `permissions-for-launch-templates.md` and `ExamplePolicies_EC2.md` (L757, L855, L882, L912, L954) ship copy-verbatim IAM samples that customers attach as-is.
Security Concern: audit each statement-by-statement for a weak default the customer inherits (AWS-owned, Tier-2, in scope).
High-level Test Scenarios:
- **Claim:** The `CreateLaunchTemplate` sample grants `Resource:"*"` gated only on `aws:ResourceTag/purpose=testing` — but tag conditions on a *create* action evaluate `aws:RequestTag` semantics; verify whether the sample's `aws:ResourceTag` key is even effective at create (an ineffective condition = `Resource:"*"` unconditioned create). → **Oracle:** `SimulateCustomPolicy` with the printed JSON, a create call carrying no matching tag; if allowed, the sample's guard is vacuous. → **Severity:** Medium (AWS-authored, uneditable sample inducing over-broad grant).
- **Claim:** The `IsLaunchTemplateResource` sample policies (L757/882/912) genuinely pin the template but do **not** pin a version (they cannot — no version ARN segment), so they are defeated by Area 2 drift. Confirm the sample's own promise ("prevents users from overriding any of the resources specified in the launch template") holds only against call-time override, not against template mutation. → **Oracle:** read the sample; note it has no version condition; cross-reference L1693. → **Severity:** Informational→High as the documented-guarantee-vs-enforcement root for Area 2.

Doc evidence: `ExamplePolicies_EC2.md` L757/855/882/912/954; `permissions-for-launch-templates.md`. Severity-if-true: Medium–High.

### Area 5 — `resolve:ssm` AMI indirection staged in the template (Lens EE / U — whoAMI / SSM-alias poisoning)
Background: `ImageId` accepts `resolve:ssm:public-parameter`, same-account `parameter-name`, and **cross-account `parameter-ARN`**; the SSM parameter resolves to an AMI id only at launch, inside the consumer's context.
Security Concern: the AMI is chosen by *name/parameter resolution*, not pinned to an owner, and the resolution happens at a later time than the review of the template. An attacker who controls (or can poison) the referenced SSM parameter — or who publishes an AMI matching a name/owner-less lookup the parameter points at — redirects every launch from the template to an attacker AMI. Create-time authz never sees the AMI (Area 1).
High-level Test Scenarios:
- **Claim:** An LT with `ImageId=resolve:ssm:<attacker-controlled-param-ARN>` is created with no image-leg authz; at launch the consumer's `ec2:ImageID`/`ec2:Owner`/`ec2:Public` RunInstances conditions evaluate **the resolved AMI**, but if the consumer policy omits `ec2:Owner=amazon`/self, an attacker-registered AMI is selected. → **Oracle:** confirm which value the image-leg condition evaluates (the SSM string vs the resolved AMI) and whether a cross-account parameter-ARN is accepted; Simulate the RunInstances image leg against an attacker AMI id. → **Severity:** High–Critical (victim executes attacker AMI = code exec on victim instance). → **Preconditions:** control of, or write access to, the referenced parameter; consumer policy lacking an owner pin.
- **Claim:** `resolve:ssm` late binding + Area 2 version drift compose: add a version that switches `ImageId` to a poisoned SSM alias on a `$Latest` ASG. → **Severity:** Critical.

Doc evidence: `API_RequestLaunchTemplateData` ImageId `resolve:ssm` block; `create-launch-template.md` L455 (`resolve:ssm:{{golden-ami}}` sample). Severity-if-true: High–Critical. Note: `resolve:ssm` is name-resolution, not an HTTP fetch → this is Lens EE, **not** SSRF.

### Area 6 — Snapshot / KMS references staged without authz (Lens H + T + A, consumption-deferred)
Background: `BlockDeviceMapping.N` carries snapshot ids, `KmsKeyId`, `Encrypted`, `DeleteOnTermination`. None are authorized at create (Area 1).
Security Concern: a template can reference a foreign/cross-account snapshot id or a specific KMS key; whether that reference is read/decryptable is deferred to the consumer's `RunInstances` volume leg (`ec2:ParentSnapshot`, `ec2:Encrypted`, `ec2:KmsKeyId` on the volume resource, L10021). Also `DeleteOnTermination=false` baked into the template can strand disks (data-remanence) after instances die.
High-level Test Scenarios:
- **Claim:** An LT referencing a snapshot the creator cannot read is created anyway (no snapshot authz at create); the breach, if any, materializes only if the consumer has snapshot read. → **Oracle:** create with a foreign snapshot id; confirm acceptance; then test consumer RunInstances volume-leg authz separately. → **Severity:** Medium (the real cross-account read is a RunInstances-leg question; see `[[ec2-copysnapshot-surface]]`).
- **Claim:** `MetadataOptions`/encryption hardening SCPs keyed on `ec2:Encrypted`/`ec2:MetadataHttpTokens` are inert at the CreateLaunchTemplate boundary — the insecure value is stored unchallenged and only (maybe) caught at launch. → **Severity:** Medium (encryption/IMDS downgrade staged).

Doc evidence: `API_RequestLaunchTemplateData` BlockDeviceMapping/MetadataOptions; `list_ec2.md` L10021 volume leg, L9949 instance leg. Severity-if-true: Medium.

### Area 7 — Describe read-side exposure (Lens A intra-account / Lens O)
Background: `DescribeLaunchTemplates`/`DescribeLaunchTemplateVersions` are documented as **Resource `"*"`, no resource-level permissions, no conditions**. Any principal with the Describe permission reads **every** LT's full launch spec account-wide — UserData (base64, may embed secrets), instance-profile ARNs, SG ids, subnet/ENI ids, snapshot ids, SSM AMI aliases.
Security Concern: intra-account over-share and a recon oracle; UserData routinely contains bootstrap secrets. Combined with Area 2, a reader learns exactly which `$Latest`/`$Default` templates feed which ASGs to target.
High-level Test Scenarios:
- **Claim:** `ec2:DescribeLaunchTemplateVersions` cannot be scoped to a subset of templates (Describe ignores resource-level perms per doc) → a read-only role sees all templates' UserData. → **Oracle:** the doc statement itself + Simulate shows no condition support; confirm UserData is returned in cleartext-base64. → **Severity:** Low–Medium (info disclosure / recon; High if UserData holds live credentials).

Doc evidence: `permissions-for-launch-templates.md` Describe sections ("Describe actions do not support resource-level permissions … must be `"*"`"). Severity-if-true: Low–Medium.

## 5. Prioritized order
1. **Area 2 — version-drift / `$Latest`-`$Default` ASG/Fleet escalation** (Critical, AWS-acknowledged, service-plane terminus → HARD STOP on SLR).
2. **Area 1 — content-ungoverned staging** (the root enabler; prove with SimulatePolicy first, zero cost).
3. **Area 5 — `resolve:ssm` AMI redirection** (High–Critical, composes with Area 2).
4. **Area 4 — AWS sample-policy audit** (Tier-2, reportable).
5. **Area 3 — tag-on-create ABAC self-widening** (Medium–High).
6. **Area 6 — snapshot/KMS/encryption staging** (Medium, mostly a RunInstances-leg question).
7. **Area 7 — Describe over-share** (Low–Medium recon).

**Kill chain (rate at the terminus = Critical):** `ec2:CreateLaunchTemplate`/`CreateLaunchTemplateVersion` (Area 1/2, no content authz, no PassRole) → stage/inject admin `IamInstanceProfile` + root `UserData` + `HttpTokens=optional` + poisoned `resolve:ssm` AMI (Area 5) into a `$Latest`/`$Default` template consumed by an ASG/Fleet → service-linked role launches it with **no RunInstances/IMDSv2 re-check** (Area 2) → instance boots, root UserData runs, admin creds vended over IMDSv1 → act as the passed role. **Stop and flag the moment the launching identity resolves to an AWS SLR.**

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Stage admin profile + root UserData with only CreateLaunchTemplate | action authz | prose-only "trust only admins" (`permissions-for-launch-templates.md` Important) — no IAM key |
| Mutate pinned template so consumer launches attacker spec | version late-binding | `ec2:LaunchTemplate` ARN pin (has no version segment, L9967) |
| ASG/Fleet $Latest new-version not re-authorized | consumption re-check | "use a specific version" guidance (L1693) — opt-in, default is $Latest/$Default |
| Bypass ModifyLaunchTemplate Deny via CreateLaunchTemplateVersion | Lens X key asymmetry | `ec2:Attribute` on Modify but absent on version-create (L5262 vs L8942) |
| Redirect launches to attacker AMI via resolve:ssm | ImageId indirection | `ec2:Owner`/`ec2:ImageID` on RunInstances image leg (not at create) |
| Self-widen ABAC via tag-on-create | tag gate | `aws:RequestTag`/`aws:ResourceTag` split across create vs version/modify |
| Read all templates' UserData/profiles | Describe | none — Describe is Resource `"*"`, no conditions (doc-stated) |

## 7. Out-of-Scope Risk Categories
- The **RunInstances / CreateFleet consumption-side** resource-level enforcement itself is a separate action with its own plan (`[[ec2-multiresource-action-failopen-scoping]]`, `[[ec2-createfleet-surface]]`); here, only the *staging* and *drift* boundaries are in scope. The whoAMI/PassRole/UserData terminus mechanics live in those plans.
- Customer-authored IAM policies that grant `ec2:CreateLaunchTemplate` too broadly = customer footgun, **except** the AWS-published samples in Area 4 (in scope, Tier-2).
- IMDS on fully-managed hosts; single-tenant self-DoS (deleting your own LT that an ASG needs — the doc's "Important" warning is a reliability note, not cross-tenant).
- Shared RDS/Grover/storage infra; DNS rebinding; third-party reference repos.

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF): NULL.** Read `API_CreateLaunchTemplate`, `API_RequestLaunchTemplateData`, `create-launch-template.md`, `permissions-for-launch-templates.md`. No field is dereferenced server-side by CreateLaunchTemplate — `resolve:ssm` is name-resolution at launch (Area 5, Lens EE), not an HTTP fetch; no `*Url`/`*Uri`/webhook/logo field exists. (UserData *could* contain a fetch, but that executes on the customer's own instance at boot, not on an AWS fleet → out of scope.)
- **Lens F (injection/parser): NULL.** No translation layer, wire protocol, BSON, or query builder; UserData is opaque base64 stored, not parsed by the service.
- **Lens K (prompt injection): NULL.** No LLM/agent in the pipeline.
- **Lens J / FF (OAuth / JWT): NULL.** SigV4 IAM only; no tokens, 3P linking, or JWT.
- **Lens M (session interception): NULL.** No session ids / presigned URLs / one-time tokens.
- **Lens W (attestation): NULL at this action.** `EnclaveOptions` is a boolean staged in the template; attestation-gating is a KMS-key-policy concern, not CreateLaunchTemplate.
- **Lens Y (transport/sig): NULL-specific** — standard EC2 SigV4/HTTPS endpoint; no action-specific transport knob. (Generic EC2 SigV4-coverage questions belong to the service, not this action.)
- **Doc-gap — `Operator`/`OperatorRequest`:** "Reserved for internal use"; accepted values and interaction with `ec2:ManagedResourceOperator` undocumented. **Confirm surface live before drawing conclusions** (Step 3 undocumented-knob hunt).
- **Doc-gap — exact re-check behavior for EC2 Fleet / Spot Fleet (vs Auto Scaling):** L1692-1693 is explicit for Auto Scaling groups; whether `maintain`/`request` Fleets re-authorize on new `$Latest` version is not stated for Fleet the same way. Mark "confirm surface first" — test both consumer types.
```
