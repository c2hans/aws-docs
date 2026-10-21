# EC2 CreateLaunchTemplateVersion — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html ; API_RequestLaunchTemplateData.html ; UserGuide/permissions-for-launch-templates.md ; UserGuide/ExamplePolicies_EC2.md ; UserGuide/manage-launch-template-versions.html ; mirror `docs/service-authorization/latest/reference/list_ec2.md` (lines 5119, 5253–5263, 8940–8944, 9593, 9967). Verified 2026-10-21 against the live docs + offline IAM reference. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

Sibling/companion plans (read together): `CreateLaunchTemplate-attack-research-plan.md` (the authoring half — v1 creation), `ec2-CreateFleet-attack-research-plan.md` (one of the consumers of the drifted version). This action is the **mutation half** of the RunInstances launch family and the action where version-drift is actually *injected*.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **Primary safe oracle for almost everything here is `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`** — CreateLaunchTemplateVersion is a pure data-staging action; you can prove the authz gap without ever launching an instance. `DryRun` is caller-IAM-only and is evaluated **before** resource resolution — **treat it as NOT an ownership oracle** (false-positive trap).
- **HARD STOP:** the fleet/ASG launcher is an AWS **service-linked role** (`AWSServiceRoleForAutoScaling`, `AWSServiceRoleForEC2Fleet`, Spot Fleet SLR). The moment evidence touches that SLR's identity/credentials, or any AWS-service-plane ARN/account, **stop, preserve evidence, flag for AWS-Security disclosure.** Do not drive the SLR to launch to "prove" privesc on a live account — prove it with Simulate + the AWS-verbatim doc statement instead.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Privilege escalation via version drift:** holding only `ec2:CreateLaunchTemplateVersion` on one template (no `iam:PassRole`, no `ec2:RunInstances`), cause an EC2 instance to boot carrying an IAM instance profile the principal could not legitimately pass. (AWS-acknowledged as PassRole-equivalent — see Area 1.)
2. **Guardrail inertness:** demonstrate that an admin's Deny/guardrail written on `ec2:Attribute`, on `aws:RequestTag`, or pinned by launch-template ID *fails to constrain* a new version's embedded content.
3. **Content-ungoverned staging:** stage a version with IMDSv1-enabled, root-level UserData, 0.0.0.0/0 SG, admin instance profile, and a `resolve:ssm` AMI alias, proving **no embedded-resource condition key** gates any of it at version-create.
4. **Cross-account / cross-tenant reach:** base a version on an SSM alias / AMI resolving to an attacker-owned image (whoAMI shape); confirm nothing pins owner/account.
5. **Recon & secret exposure:** read every launch-template version's full `LaunchTemplateData` (UserData bootstrap secrets, profiles, SGs, snapshot IDs) account-wide via `DescribeLaunchTemplateVersions`.
6. **Resilience/DoS:** delete or churn the specific version a pinned fleet/ASG depends on.

---

## 2. Components, Assets, and Design

**What the action is.** `CreateLaunchTemplateVersion` adds an immutable, auto-numbered new *version* to an existing launch template (named by `LaunchTemplateId` or `LaunchTemplateName`). Launch templates themselves are immutable; a "modification" is always a new version. A version is a frozen blob of `RequestLaunchTemplateData` — the full instance launch spec.

**`RequestLaunchTemplateData` (the version body) carries, among ~30 fields:**
- `IamInstanceProfile` (role container attached to the instance → IMDS creds) — **the privesc payload.**
- `UserData` (base64 boot script, runs as root on first boot) — **code-exec + secret-staging payload.**
- `MetadataOptions.HttpTokens` (`optional` = IMDSv1 reachable; `required` = IMDSv2) and `HttpPutResponseHopLimit`, `InstanceMetadataTags`.
- `NetworkInterfaces` / `SecurityGroupIds` / `SecurityGroups` (can place 0.0.0.0/0-permissive SGs).
- `ImageId` — accepts an AMI id **or** an SSM parameter reference / `resolve:ssm` alias (late-bound at launch).
- `BlockDeviceMappings` (snapshot IDs, `Encrypted`, `DeleteOnTermination`), `KeyName`, `InstanceType`, `Placement` (tenancy/host/affinity), `CapacityReservationSpecification`, `Operator` ("Reserved for internal use").

**Version-specific inputs (not on the parent Create):**
- `SourceVersion` — new version inherits all params from a chosen source version; any field you also supply **overwrites** the inherited one. BDM snapshots are *dropped* unless re-specified. → lets an attacker clone a trusted/reviewed version and overwrite exactly one dangerous field (minimal diff → review evasion).
- `ResolveAlias` (default `false`) — whether the response echoes the resolved AMI id for an SSM-alias `ImageId`. With `false`, the version stores the alias and resolution happens **at launch time**, later and elsewhere.
- `VersionDescription`, `ClientToken`.

**Version numbering & pointers.** Versions are numbered sequentially (cannot be chosen). Two logical pointers exist on the template: **`$Default`** (changed only by `ModifyLaunchTemplate`) and **`$Latest`** (auto-tracks the newest version — moves on *every* `CreateLaunchTemplateVersion`, with no additional action). Consumers (ASG, EC2 Fleet, Spot Fleet, RunInstances) reference a template by a **specific version number, `$Default`, or `$Latest`**.

**Identity / authz.** SigV4 IAM. Action access-level **Write**; required resource type `launch-template*`.

**Resource identifier shape.** `arn:${Partition}:ec2:${Region}:${Account}:launch-template/${LaunchTemplateId}` — **no version segment.** IAM cannot name a version; `ec2:LaunchTemplate` / `ec2:IsLaunchTemplateResource` pin the template, never a version.

### ASCII pipeline (where drift bites)
```
 low-priv principal (only ec2:CreateLaunchTemplateVersion on lt-X)
        │  stages v-next:  IamInstanceProfile=admin, UserData=root, HttpTokens=optional,
        │                  ImageId=resolve:ssm/attacker, SG=0.0.0.0/0
        ▼
   launch-template lt-X   ──$Latest auto-advances to v-next──┐   ($Default needs ModifyLaunchTemplate)
        │                                                    │
        ▼                                                    ▼
   ASG / EC2 Fleet / Spot Fleet configured to track $Latest or $Default
        │   scale-out / replacement launch to meet target capacity
        ▼
   AWSServiceRoleForAutoScaling / ...ForEC2Fleet  (SLR = the launcher)   ◄── HARD STOP (service plane)
        │   "EC2 does not re-check user permissions ... no user interaction"  (AWS verbatim)
        ▼
   EC2 instance boots → instance profile creds at 169.254.169.254  → attacker-controlled role
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv principal (version-create only) | IAM role / instance profile it lacks `PassRole` for | Embed `IamInstanceProfile` in v-next of a $Latest/$Default-tracked template | An instance boots with that profile while the principal cannot `RunInstances` with it directly → **PassRole bypass = High** |
| Low-priv principal | AWS ASG/Fleet **SLR** (service plane) | SLR launches the drifted version with no re-check | Any observation of the SLR launching attacker content — **do not drive this on a live acct; HARD STOP** |
| Caller's version body | Admin's `ec2:Attribute` Deny guardrail | CreateLaunchTemplateVersion has no `ec2:Attribute` key | A Deny on `ec2:Attribute`/`DefaultVersion` denies `ModifyLaunchTemplate` but **allows** version-create → guardrail inert |
| Caller's version body | Admin's `aws:RequestTag` tag-gate | Version action has no `aws:RequestTag`/`aws:TagKeys` key | A "must tag on create" policy that constrains `CreateLaunchTemplate` does **not** constrain versions → version inherits parent's existing tag |
| Caller (`resolve:ssm` ImageId) | Attacker-published AMI (another account) | SSM-alias / name resolution deferred to launch time | Fleet launches an AMI resolving to a non-owned image id (whoAMI) → cross-account code exec |
| Read-only principal | Every template's full version body account-wide | `DescribeLaunchTemplateVersions` Resource `"*"`, no conditions | UserData secrets / profiles / SGs / snapshot IDs of templates the principal doesn't own are returned → info-disclosure / Lens T secret recovery |
| Principal with delete-version | A fleet/ASG pinned to a specific version | `DeleteLaunchTemplateVersion` | Launch failure on scale-out of a resource relying on that version → DoS |

Canonical lines named: **caller request context ↔ PassRole/credential-vending** (the headline); **any customer surface ↔ AWS service plane (ASG/Fleet SLR = hard stop)**; **untrusted staged content ↔ generated launch action** (no re-check).

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| CreateLaunchTemplateVersion | POST (Query) | Existing | **Yes** | External (SDK/API) | Add immutable numbered version; $Latest auto-advances | Yes | `ec2:CreateLaunchTemplateVersion` on `launch-template*` | **Keys: `aws:ResourceTag`, `ec2:ManagedResourceOperator`, `ec2:Region`, `ec2:ResourceTag` only — NO `ec2:Attribute`, NO `aws:RequestTag`/`TagKeys`, NO embedded-resource key.** |
| ModifyLaunchTemplate | POST | Existing | Yes | External | Set `$Default` version | Yes | `ec2:ModifyLaunchTemplate` | **Has `ec2:Attribute`/`ec2:Attribute/${AttributeName}` → Lens-X asymmetry vs version-create.** Needed to move $Default (not needed for $Latest). |
| DeleteLaunchTemplateVersion | POST | Existing | Yes | External | Delete a version (not $Default) | Yes | `ec2:DeleteLaunchTemplateVersion` | tag-scopable; DoS a pinned consumer. |
| DescribeLaunchTemplateVersions | GET | Existing | No | External | Read full version bodies | Yes | `ec2:DescribeLaunchTemplateVersions` | **Resource `"*"`, no conditions → account-wide read of all version bodies.** Recon + Lens-T secret exposure. |
| RunInstances / CreateFleet / Spot Fleet / ASG Create/Update | — | Existing | Yes | External + SLR | Consume template by `$Default`/`$Latest`/#N | — | varies | The re-check gap lives here; see Area 1. |

Undocumented/console-hidden knob: **`Operator` / `OperatorRequest`** in `RequestLaunchTemplateData` is "Reserved for internal use" — accepted by API, not surfaced in console. Probe its interaction with the `ec2:ManagedResourceOperator` condition key (doc-gap).

---

## 5. Recommended Areas of Focus

### Area 1 — Version-drift privilege escalation (PassRole-equivalence) — CROWN JEWEL, Severity High (Critical if SLR/service-plane touched)
**Background.** A launch template version is content-ungoverned, and fleets/ASGs tracking `$Latest`/`$Default` re-launch instances to meet capacity **without any user in the loop**.

**Security Concern (AWS-verbatim, permissions-for-launch-templates "Control versioning permissions" Important box):**
> "When a different launch template version is used for `Latest` or `Default`, Amazon EC2 does not re-check user permissions for actions to be completed when launching new instances to fulfil the fleet's target capacity because there is no user interaction with the AWS resource. **By granting a user permission to call the `CreateLaunchTemplateVersion` and `ModifyLaunchTemplate` APIs, the user is effectively also granted the `iam:PassRole` permission if they point the fleet to a different launch template version that contains an instance profile** ... a user can potentially update a launch template to pass an IAM role to an instance even if they don't have the `iam:PassRole` permission."

And ExamplePolicies_EC2.md (verbatim): *"For an Auto Scaling group that is configured to use the `Latest` or `Default` launch template, the permissions are not checked when a new version of the launch template is created. For permissions to be checked, you must configure the Auto Scaling group to use a specific version."* + *"Restrictions on the use of IMDSv1 on IAM principals for RunInstances are only checked when an ASG … is created or updated."*

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A principal holding only `ec2:CreateLaunchTemplateVersion` on template `lt-X` (no `iam:PassRole`, no `ec2:RunInstances`) can cause an admin instance profile to be attached to a running instance. → **Mechanism:** embed `IamInstanceProfile=<admin>` in v-next; a pre-existing ASG/Fleet tracks `$Latest`; scale-out launches it via the SLR with no re-check. → **Oracle:** `iam:SimulatePrincipalPolicy` shows the principal denied `iam:PassRole`/`RunInstances`, while the doc guarantees the SLR launch proceeds. Confirm the ASG config references `$Latest`/`$Default` (not a pinned #). **Do NOT trigger a live launch to confirm — the launcher is an AWS SLR (hard stop).**
- **Claim:** `$Latest` alone removes even the need for `ModifyLaunchTemplate`. → **Mechanism:** `$Latest` auto-advances on every `CreateLaunchTemplateVersion`; only `$Default` requires Modify. → **Oracle:** a template whose consumers reference `$Latest` → version-create-only is sufficient for the full chain; the AWS note's "`CreateLaunchTemplateVersion` *and* `ModifyLaunchTemplate`" overstates the requirement for the $Latest case.
- **Preconditions:** a consumer (ASG/Fleet) already tracking `$Latest`/`$Default` exists in the account; attacker can create a version on its template.
- **Cost:** one API call. **Severity-if-true:** High (non-PassRole→role-attach); escalates to Critical if the drifted role is itself privileged (admin) → full account takeover.
- **Stop condition:** proof-by-Simulate + doc. Never observe the SLR launch on a live account.

**Chain:** Area 1 → UserData (Area 3) root boot script reads the attached role creds from IMDS and exfils them → persistent cross-service access at the role's privilege.

### Area 2 — Guardrail inertness: `ec2:Attribute` and `aws:RequestTag` asymmetry (Lens X + Lens S) — Severity High
**Background.** Admins commonly try to lock down launch templates with a Deny.

**Security Concern.** `list_ec2.md` L5262 vs L8943: **`CreateLaunchTemplateVersion` has NO `ec2:Attribute` key; `ModifyLaunchTemplate` does.** And L5262 vs L5256: version-create has **no `aws:RequestTag`/`aws:TagKeys`** (the parent `CreateLaunchTemplate` does).

**High-level Test Scenarios:**
- **Claim:** `Deny ec2:ModifyLaunchTemplate when ec2:Attribute=DefaultVersion` (an attempt to freeze the default version) does **not** stop an attacker from injecting a malicious new version. → **Mechanism:** the Deny matches only `ModifyLaunchTemplate`; `CreateLaunchTemplateVersion` carries no `ec2:Attribute` key so the Deny never evaluates against it; and if the consumer tracks `$Latest`, no Modify is needed anyway. → **Oracle:** `SimulateCustomPolicy` with that Deny → `CreateLaunchTemplateVersion` = **allowed**.
- **Claim:** An admin policy that constrains template creation to `aws:RequestTag/env=test` fails to constrain versions. → **Mechanism:** version-create only reads `aws:ResourceTag` on the already-existing template, which the attacker (or anyone) set at create time (self-widen). → **Oracle:** Simulate: a version-create on a template tagged `env=test` is allowed under a `ResourceTag` policy regardless of version content; `RequestTag` conditions are vacuous for this action. Also test case-sensitivity / `…IfExists` fail-open on the `ResourceTag` condition.
- **Severity-if-true:** High (the only documented guardrails are advisory for this action).

### Area 3 — Content-ungoverned version body (Lens U / R / S) — Severity High
**Background.** The version body is the full launch spec.

**Security Concern (AWS-verbatim, permissions-for-launch-templates Important box):**
> "You can't use resource-level permissions to restrict the resources that users can specify in a launch template when they create a launch template **or launch template version**. Therefore, make sure that only trusted administrators are granted permission to create launch templates and launch template versions."

The sole mitigation is prose. **No condition key exists for any embedded resource.** Absent keys that exist on *RunInstances* legs but **not** on CreateLaunchTemplateVersion: `ec2:InstanceProfile`, `ec2:NewInstanceProfile`, `ec2:ImageID`, `ec2:Owner`, `ec2:Public`, `ec2:MetadataHttpTokens` (IMDS enforcement), `ec2:Vpc`, `ec2:SecurityGroupID`, and there is no `ec2:UserData*` key anywhere.

**High-level Test Scenarios:**
- **Claim:** A version can set `MetadataOptions.HttpTokens=optional` (IMDSv1 on) with no IAM obstacle. → **Oracle:** Simulate shows no `ec2:MetadataHttpTokens`-equivalent gate on the action; IMDSv1-restriction is "only checked when an ASG is created or updated" (ExamplePolicies) — not at version-create. → combines with Area 1 to make IMDS creds trivially stealable via SSRF.
- **Claim:** `UserData` carrying a root boot script is accepted with no content key. → **Oracle:** no `ec2:UserData` key exists in `list_ec2.md`.
- **Claim:** `SourceVersion` minimal-diff evasion — base v-next on reviewed v2, overwrite **only** `IamInstanceProfile` (snapshots dropped silently). → **Mechanism:** SourceVersion inheritance + field overwrite; "Snapshots ... are ignored ... unless explicitly included." → **Oracle:** the resulting version differs from the trusted base by one line, defeating diff-based review.
- **Severity-if-true:** High (feeds Areas 1/4).

### Area 4 — `resolve:ssm` / AMI-name late-binding (Lens EE + Lens U authenticity-filter omission) — Severity High
**Background.** `ImageId` accepts an SSM parameter reference; `ResolveAlias=false` (default) stores the alias and resolves it **at launch time**.

**Security Concern.** Nothing in the version-create authz pins AMI **owner/account**. An SSM alias can be pointed at an attacker-published image; resolution deferral means the review of the version body shows an alias, not the eventual image.

**High-level Test Scenarios:**
- **Claim:** A version with `ImageId=resolve:ssm:/path` resolving to a non-owned AMI (whoAMI shape) is accepted and later launched by the fleet SLR. → **Oracle:** confirm no `ec2:Owner`/`ec2:ImageID` key on the action; confirm `ResolveAlias=false` defers resolution. **Refute** if an org/account SCP or the consumer's RunInstances statement pins owner (check the consumer policy, per ExamplePolicies). → chains with Area 1 (cross-account code exec via the drifted, SLR-launched instance).
- **Severity-if-true:** High → Critical if combined with a privileged drifted role.

### Area 5 — Account-wide version-body disclosure & secret recovery (Lens A recon + Lens T) — Severity Medium–High
**Background.** `DescribeLaunchTemplateVersions` is `Resource:"*"`, no resource-level perms, no conditions (permissions-for-launch-templates, verbatim).

**Security Concern.** A read-only principal retrieves the **full `LaunchTemplateData` of every version of every template** in the account — including `UserData` (frequently contains bootstrap secrets/tokens/registration keys), `IamInstanceProfile`, security-group IDs, and `BlockDeviceMappings` snapshot IDs.

**High-level Test Scenarios:**
- **Claim:** `DescribeLaunchTemplateVersions` returns base64 `UserData` containing a secret for a template the caller doesn't own. → **Oracle:** read any version body across the account; decode UserData; a credential/token present = Lens-T secret wall bypass (the secret's intended IAM wall is irrelevant because it's inlined into a world-readable launch spec). → feeds Area 1/3 targeting.
- **Severity-if-true:** Medium (recon) → High where UserData holds live credentials.

### Area 6 — Version-delete / churn DoS (Lens L / resilience) — Severity Medium (High if cross-tenant/shared pipeline)
- **Claim:** Deleting the specific version an ASG/Fleet is pinned to causes scale-out launch failures. → **Mechanism:** `DeleteLaunchTemplateVersion` (tag-scopable, but a `Resource:"*"` grant allows any); a pinned consumer references a now-missing #. → **Oracle:** consumer launch fails / stalls at next scaling event. (`$Default` cannot be deleted; pinned specific-version consumers are the target.)
- **Severity-if-true:** Medium; High if the pipeline is shared/production-critical.

### Area 7 — `Operator`/`ec2:ManagedResourceOperator` console-hidden knob (doc-gap probe) — Severity Informational→?
- **Claim:** The `Operator` field (RequestLaunchTemplateData, "Reserved for internal use") interacts with the `ec2:ManagedResourceOperator` condition key present on this action (L5262). → **Oracle:** probe whether setting `Operator` lets a caller assert a managed/operator context that flips the `ec2:ManagedResourceOperator` key value, potentially satisfying an operator-scoped Allow or dodging a caller-scoped Deny. **Doc-gap — confirm surface first.**

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Version-drift PassRole bypass | $Latest/$Default fleet + SLR | Prose only ("grant only to trusted admins"); "pin a specific version" (ASG) |
| `ec2:Attribute` Deny bypass | CreateLaunchTemplateVersion vs ModifyLaunchTemplate | Deny assumed to cover both — it does not |
| `aws:RequestTag` tag-gate bypass | version-create inherits parent ResourceTag | Admin's create-time tag gate |
| IMDSv1 re-enable via version | MetadataOptions.HttpTokens | "checked only at ASG create/update" (ExamplePolicies) |
| Cross-account AMI via resolve:ssm | ImageId late-binding | consumer-side RunInstances `ec2:Owner`/`ec2:ImageID` (if present) |
| Account-wide version-body read | DescribeLaunchTemplateVersions | none (Resource `"*"`, no conditions) |
| Pinned-version delete DoS | DeleteLaunchTemplateVersion | tag-based condition keys (optional) |

---

## 7. Out-of-Scope Risk Categories
- **IMDS on fully managed hosts** (not this surface).
- **Customer-authored IAM policies** that are over-broad (`Resource:"*"` on version-create) — that's a customer least-privilege footgun, **out of scope** — *unless* it appears in an **AWS-published sample policy / managed policy / CFN / runbook the customer copies verbatim** (then Tier-2 reportable; audit ExamplePolicies_EC2 and any AWS-managed policy granting `ec2:CreateLaunchTemplateVersion`).
- **Single-tenant self-DoS** (deleting your own versions).
- **A principal steering resources entirely within its own account that it already fully controls** with no privilege gain.
- **Driving the ASG/Fleet SLR to launch** on a live account to "prove" Area 1 — **hard stop**; prove via Simulate + the AWS-verbatim statements instead.
- Product/feature-parity gaps; DNS-rebinding against private-only endpoints.

## 8. Null hypotheses / doc gaps
- **SSRF (Lens G) — null.** Read API_RequestLaunchTemplateData, the action page, and permissions page: no field the *CreateLaunchTemplateVersion* action dereferences server-side at create (SigV4, no fetch/preview/unfurl). `resolve:ssm` is name-resolution (Area 4), not an HTTP fetch, and resolution happens at launch, not here.
- **Translation/injection (F), prompt-injection (K), attestation (W), JWT/token (FF), cache (DD), canonicalization (BB), upstream-context (CC), transport/TLS (Y) — null** for this action (no parser/LLM/enclave/token/edge/proxy/custom-transport at this control-plane action).
- **Lens N (namespace migration) — null:** single ARN namespace; the ARN's *missing version segment* is captured under Lens S/X (Area 2), not a migration window.
- **Doc-gaps to confirm on a live surface first:** (a) whether **EC2 Fleet / Spot Fleet** (vs ASG) re-check RunInstances perms on `$Latest` — ExamplePolicies states the ASG behavior explicitly but Fleet is only implied by the permissions-page Important box; (b) the `Operator`/`ec2:ManagedResourceOperator` interaction (Area 7); (c) exact `ResolveAlias`-at-create vs at-launch resolution timing for a cross-account alias.

---
*Plan authored 2026-10-21 from documentation only. Companion: `CreateLaunchTemplate-attack-research-plan.md`, `ec2-CreateFleet-attack-research-plan.md`. The headline finding (Area 1) is AWS-acknowledged in the docs verbatim — the research value is quantifying the blast radius and confirming the `$Latest`-only (no-Modify) and `ec2:Attribute`-Deny-inert variants.*
