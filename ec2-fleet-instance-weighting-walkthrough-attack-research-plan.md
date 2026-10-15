# EC2 Fleet Instance-Weighting Walkthrough — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/ec2-fleet-instance-weighting-walkthrough.html` (the target
tutorial page) and the mechanism/API pages its `config.json` dereferences —
`ec2-fleet-instance-weighting.html`, `ec2-fleet-allocation-strategy.html`,
`ec2-fleet-control-spending.html`, `create-ec2-fleet.html`, `ec2-fleet-request-type.html`,
`ec2-fleet-attribute-based-instance-type-selection.html`, the EC2 **API Reference**
(`API_CreateFleet`, `API_FleetLaunchTemplateOverridesRequest`,
`API_FleetLaunchTemplateSpecificationRequest`, `API_TargetCapacitySpecificationRequest`,
`API_InstanceRequirements`), and the IAM **Service Authorization Reference**
`service-authorization/latest/reference/list_ec2.md`. Online `.md` twins cross-checked against the
offline mirror 2026-10-15 (API Reference + walkthrough + weighting/allocation/spending pages
byte-for-byte identical offline==online; `list_ec2.md` read offline by targeted grep — the online
`.md` fetch is summarizer-truncated before the CreateFleet detail rows, so the offline grep is
authoritative here, not drift).

Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope note — what is NEW here vs. the hub plan `fleet-tutorials-attack-research-plan.md`.** This
> is the **page-level deep-dive child** of the `fleet-tutorials.html` hub for the single tutorial
> `ec2-fleet-instance-weighting-walkthrough.html`. The hub plan already owns the **Capacity-Reservation
> consumption** cross-account surface (its Areas 1–8) and touches instance-weighting cost math and the
> `ec2-fleet-prerequisites` sample policy only at **summary level** (hub Area 9 + Objective 7). This
> plan **does NOT restate the CR-consumption surface** — it cross-references the hub for all of it — and
> instead owns the granular surface this specific walkthrough's `config.json` and `create-fleet` CLI
> introduce: the **launch-template-config construction surface** (`$Latest`/`$Default` late-binding,
> the `instant`-type override expansion of `IamInstanceProfile`/`UserData`/`MetadataOptions`/SSM-AMI,
> `InstanceRequirements` instance-type broadening), the **CreateFleet-vs-RunInstances IAM
> condition-key asymmetry**, the **default `Type=maintain`** the tutorial silently inherits, and the
> **deep** weighting-overshoot / `MaxTotalPrice` / per-override-`MaxPrice` math (hub Area 9 at depth).
> SLR launch condition-key non-propagation, PassRole/confused-deputy depth, cancel/terminate internals,
> auto-scaling, monitoring/EventBridge, and tag-authz are all **deferred to the siblings** and
> cross-referenced where they touch.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 is ordered). Look left and right for adjacent bugs.
- **In-scope / reportable:** (a) AWS-owned **guarantee-vs-enforcement / twin-authorization-parity gaps** where the IAM reference itself makes a control inexpressible (CreateFleet's missing `ec2:LaunchTemplate`/version keys — Area 1) — Lens U/X, Informational→Medium, AWS-owned; (b) a **confirmed intra-account privilege-escalation** where a lower-privileged principal reaches a role/userData/AMI it could not use directly via the fleet's launch path (Areas 2, 3) — Medium–High; (c) weak defaults in **AWS-authored copy-verbatim artifacts** (the `ec2-fleet-prerequisites` sample user policy — deferred to hub Area 9, cross-ref only).
- **Out-of-scope / document-but-don't-report:** self-inflicted single-account cost footguns (weighting overshoot, price-protection-off, `MaxTotalPrice` edges) **unless** a lower-priv principal triggers them under a budget/SCP/quota the operator sized on a false 1:1 capacity-to-instance assumption (§7). The customer's own fleet IAM policy is their footgun; only AWS-authored artifacts and AWS-owned expressibility gaps are reportable.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. the EC2 Fleet SLR `AWSServiceRoleForEC2Fleet` reaching outside the caller's account, or any AWS-owned fleet host), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Late-rebind a running fleet's launch spec you don't fully control** — get a `maintain`-type fleet that references `Version:"$Latest"`/`$Default` to launch, on its next replenishment, an instance carrying an `IamInstanceProfile` / `UserData` / AMI / security group a principal who holds only `ec2:ModifyLaunchTemplate`+`ec2:CreateLaunchTemplateVersion` (not `iam:PassRole`, not `ec2:RunInstances`) placed into the template — launched by the EC2 Fleet SLR, not the planter.
2. **Inject a launch spec at create time via `instant` overrides** — on an `instant` fleet, set `IamInstanceProfile`, `LaunchTemplateSpecificationUserData` (16 KB raw user-data bypassing the launch template), `MetadataOptions` (IMDSv1 / high hop-limit), or an SSM-parameter-resolved `ImageId` directly in the `create-fleet` request, and determine whether `iam:PassRole` / IMDS / AMI-owner controls are enforced on that override path.
3. **Prove the LT-pinning / version controls are inexpressible in a CreateFleet policy** — demonstrate `CreateFleet` exposes **no** `ec2:LaunchTemplate`, `ec2:IsLaunchTemplateResource`, or any version condition key, so an admin cannot author a CreateFleet-scoped policy that pins *which* launch template (or forbids `$Latest`/`$Default`) a fleet may reference — while `RunInstances` can.
4. **Amplify spend/instance-type blast radius within one account** — combine weighting round-up overshoot (no documented ceiling), `diversified` per-pool compounding, `InstanceRequirements` with price-protection off (`999999`), and the `MaxTotalPrice`-vs-weighting documented silence, to launch materially more / larger / costlier capacity than a budget/quota sized on the walkthrough's 1:1 assumption would predict.
5. **Characterize the default `Type=maintain` surface the tutorial hides** — confirm the config's omitted `Type` yields a long-lived, auto-replenishing, event-emitting fleet (re-resolving its launch template over time), not the one-shot the reader may assume.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** SigV4 EC2 API + AWS CLI only — **there is no console support for creating an EC2 Fleet** (`create-ec2-fleet.md`: *"There is currently no console support for creating an EC2 Fleet"*). The entire create surface is API/CLI/CloudFormation, so every lead below is on a path **no console review would surface** (satisfies the skill's "hunt the undocumented/console-hidden knob" discipline — the whole action is console-hidden). Relevant action: `CreateFleet` (`aws ec2 create-fleet --cli-input-json file://config.json`).

**The tutorial's `config.json` (ground truth for this page):**
```
{ "LaunchTemplateConfigs":[{
    "LaunchTemplateSpecification":{ "LaunchTemplateId":"lt-07b3bc7625cdab851", "Version":"1" },
    "Overrides":[
      {"InstanceType":"r3.2xlarge","SubnetId":"subnet-482e4972","WeightedCapacity":1},
      {"InstanceType":"r3.4xlarge","SubnetId":"subnet-482e4972","WeightedCapacity":2},
      {"InstanceType":"r3.8xlarge","MaxPrice":"0.90","SubnetId":"subnet-482e4972","WeightedCapacity":4}
    ] }],
  "TargetCapacitySpecification":{ "TotalTargetCapacity":20, "DefaultTargetCapacityType":"spot" } }
```
Note what the config **omits** and therefore inherits as defaults: **`Type` → `maintain`** (API Reference: *"The fleet type. The default value is `maintain`"*), no `SpotOptions.AllocationStrategy` (CLI default = **lowest-price**, which the strategy page labels *"(not recommended)"* for highest interruption risk), no `MaxTotalPrice`, no `ValidUntil`, no `TerminateInstancesWithExpiration`, no `Context`.

**Principals / trust zones.**
- **Fleet caller** — the identity invoking `CreateFleet`. Instances are launched by the EC2 Fleet **service-linked role `AWSServiceRoleForEC2Fleet`**, not re-authenticated per instance as the caller (established by the sibling plans; the backbone finding is that a customer's *identity-policy* `RunInstances` condition keys do **not** propagate to SLR-initiated launches).
- **Launch-template author / mutator** — a principal holding `ec2:CreateLaunchTemplateVersion` / `ec2:ModifyLaunchTemplate` on the `launch-template*` resource. **Distinct from the fleet caller.** Under `$Latest`/`$Default` this principal controls what the fleet actually launches at each replenishment (Area 2).
- **EC2 Fleet SLR** — `AWSServiceRoleForEC2Fleet`. Performs the launch. **AWS service plane for its own identity = hard stop; the launch *into the caller's account* is in scope.**
- **AWS service plane** — hard stop.

**Assets.** The `IamInstanceProfile` an instance receives (→ its live STS creds via IMDS); `UserData` (root-run boot script); the AMI (`ImageId` / SSM-resolved); the account's On-Demand/Spot spend and Service-Quota headroom; the launch template and its version pointer (`$Default`).

**Identifiers.** Launch template `lt-` + 17 hex (ARN `arn:…:launch-template/lt-…`); fleet `fleet-<uuid>`; template **version** is a monotonic integer or the symbolic `$Latest`/`$Default`. Subnet `subnet-…` (one AZ; EC2 Fleet *"can't span different subnets from the same Availability Zone"* and *"can't span AWS Regions"*).

```
 LT author ──ModifyLaunchTemplate / CreateLaunchTemplateVersion──► launch-template lt-xxxx
   (holds ec2:ModifyLaunchTemplate, NOT PassRole/RunInstances)       │  version pointer $Latest/$Default
                                                                      │  (IamInstanceProfile, UserData, AMI, SG)
 Fleet caller ──CreateFleet (Version:"$Latest")──► EC2 Fleet SLR ─────┘ resolves version AT LAUNCH TIME
   (holds ec2:CreateFleet; NO ec2:LaunchTemplate key available)       │  (maintain → re-resolves on every replenish)
                                                                      ▼
                                                   instance launched by SLR into caller's account
                                                     carrying whatever the resolved version says
```

---

## 3. API / Interface Inventory (create / launch-template-config surface)

| Name | Mut? | Int/Ext | Authorized callers | `list_ec2` resource types / condition keys | Notes / lead |
|---|---|---|---|---|---|
| `CreateFleet` | Mut | Ext (API/CLI/CFN only, **no console**) | fleet callers | req: `fleet*`,`instance*`,`image`,`subnet`,`launch-template`,`placement-group`,`volume`,`capacity-reservation`. **`launch-template` row keys = only `aws:ResourceTag`/`ec2:Region`/`ec2:ResourceTag`** | **No `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource`/version key anywhere in the row.** Doc: *"Resource-level permissions for this action do not include the resources specified in a launch template."* Area 1 |
| `RunInstances` | Mut | Ext | all | every resource-type row carries `ec2:IsLaunchTemplateResource` **and** `ec2:LaunchTemplate` | The twin that **can** be LT-pinned → CreateFleet/RunInstances authz-parity gap. Area 1 |
| `ModifyLaunchTemplate` | Mut | Ext | LT owner/mutator | `launch-template*` + `ec2:Attribute`/`ec2:Attribute/${AttributeName}`/`ec2:ManagedResourceOperator`/`ec2:Region`/`ec2:ResourceTag` | Moves `$Default`. **No key restricts which version becomes default / no `DefaultVersion` key.** Area 2 |
| `CreateLaunchTemplateVersion` | Mut | Ext | LT mutator | `launch-template*` (+tag/region) | Adds a version → moves what `$Latest` resolves to. Area 2 |
| `CreateFleet` override `IamInstanceProfile` | Mut | Ext | fleet caller (**`instant` only**) | — (not a distinct `list_ec2` row; see `instance*` key `ec2:InstanceProfile`) | Caller sets the instance profile in the request, bypassing the LT. PassRole enforcement? Area 3 |
| `CreateFleet` `LaunchTemplateSpecificationUserData` | Mut | Ext | fleet caller (**`instant` only**) | — | 16 KB raw base64 user-data **bypassing the launch template entirely**. Root-run boot script injection. Area 3 |
| `CreateFleet` override `MetadataOptions` | Mut | Ext | fleet caller (**`instant` only**) | — | Set `HttpTokens=optional` (IMDSv1) / high `HttpPutResponseHopLimit`. Area 3 |
| `CreateFleet` override `ImageId` / SSM param | Mut | Ext | fleet caller (**`instant` only**) | — | AMI by id or `resolve:ssm` parameter instead of AMI id. AMI-owner / param-trust. Area 3 |
| `CreateFleet` override `InstanceRequirements` | Mut | Ext | fleet caller | — (mutually exclusive w/ `InstanceType`) | Attribute-based type selection; price-protection off = `999999`. Instance-type broadening. Area 4 |
| `CreateFleet` `Context` | Mut | Ext | fleet caller | — | API Reference: *"Reserved."* — undocumented opaque knob (same as modify-spot-fleet). §8 |

**Doc-flagged leads to keep verbatim:**
- `API_FleetLaunchTemplateSpecificationRequest`: *"The launch template version number, `$Latest`, or `$Default`. … If the value is `$Latest`, Amazon EC2 uses the latest version of the launch template. If the value is `$Default`, Amazon EC2 uses the default version."* (no create-time-pinning caveat).
- `API_FleetLaunchTemplateOverridesRequest` `ImageId`: *"This parameter is only available for fleets of type `instant`. For fleets of type `maintain` and `request`, you must specify the AMI ID in the launch template."*
- `list_ec2` CreateFleet Description: *"Resource-level permissions for this action do not include the resources specified in a launch template. To specify resource-level permissions for resources specified in a launch template, you must include the resources in the RunInstances action statement."*
- `ec2-fleet-instance-weighting`: *"If the result isn't an integer, the fleet rounds it up to the next integer … The fleet can select any pool … even if the capacity of the instances launched exceeds the requested target capacity."* (the only overshoot sentence; **no ceiling stated**).
- `ec2-fleet-attribute-based-instance-type-selection`: *"You can also turn off price protection. To indicate no price protection threshold, specify a high percentage value, such as `999999`."*

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| LT mutator (no PassRole/RunInstances) | A role's live creds / root boot / AMI on a fleet instance | `CreateLaunchTemplateVersion`/`ModifyLaunchTemplate` + fleet's `$Latest`/`$Default` late-bind | **An instance launched by the SLR carries an `IamInstanceProfile`/`UserData`/AMI the mutator placed, which the mutator could not have passed via `RunInstances` directly = intra-account privesc** (Area 2). |
| Fleet caller (`instant`) | A role's creds / root boot / IMDS posture | `create-fleet` override `IamInstanceProfile`/`UserData`/`MetadataOptions`/SSM-AMI | **A caller lacking `iam:PassRole` for the profile (or a `RunInstances` IMDS/AMI condition) gets an instance carrying it anyway = create-time launch-spec injection** (Area 3). |
| Admin authoring a CreateFleet policy | Intended "only LT `lt-X` / no `$Latest`" control | `list_ec2` CreateFleet row | **The control is inexpressible — no `ec2:LaunchTemplate`/version key on CreateFleet; the RunInstances twin has it = authz-parity / guarantee-expressibility gap** (Area 1). |
| Lower-priv principal under a budget/SCP/quota | Account spend / quota headroom | weighting round-up + diversified compounding + price-protection-off | **Capacity/cost materially exceeding a 1:1-sized budget without an SCP/quota violation = cost-amplification footgun** (Area 4; in-scope only under a mis-sized guardrail). |
| Any customer surface | AWS service plane / another account | — | **Any AWS-owned identity/ARN, or any launch landing in an account you don't control = HARD STOP.** |

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — CreateFleet exposes no launch-template-pinning / version condition key, while RunInstances does  [Lens U / X / S] — AWS-owned, reportable
**Background.** `list_ec2.md` CreateFleet row: the `launch-template` resource type carries **only** `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`. **Neither `ec2:LaunchTemplate` (ARN) nor `ec2:IsLaunchTemplateResource` (Bool) appears anywhere in the CreateFleet action row.** RunInstances, by contrast, carries both on every resource-type row. AWS states the gap in its own CreateFleet Description: *"Resource-level permissions for this action do not include the resources specified in a launch template. To specify resource-level permissions for resources specified in a launch template, you must include the resources in the RunInstances action statement."*
**Security Concern.** Two controls a careful admin would expect to write are **inexpressible on the CreateFleet action**:
1. "This principal may create fleets referencing **only** launch template `lt-X`" — impossible (`ec2:LaunchTemplate` absent on CreateFleet).
2. "This principal may **not** use `$Latest`/`$Default`, only a pinned version" — impossible (no `ec2:LaunchTemplateVersion`-class key exists anywhere in `list_ec2`, grepped exhaustively; only `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource` exist).
This is the twin-authorization-parity shape (Lens X): one action in a family (RunInstances) is LT-scopable, its sibling (CreateFleet, which *results in* RunInstances-equivalent launches by the SLR) is not — and the SLR launch does not re-apply the caller's identity-policy conditions (backbone finding). So a fleet becomes an **un-LT-scopable launch path**: the control an admin builds on RunInstances is bypassed by routing the launch through CreateFleet.
**High-level Test Scenarios.**
- *Claim:* a Deny/Allow `Condition` using `ec2:LaunchTemplate` on `ec2:CreateFleet` is **inert** (the key is not evaluated for that action). → **Oracle:** `iam:SimulateCustomPolicy` with an `ec2:CreateFleet` statement conditioned on `ec2:LaunchTemplate = arn:…:launch-template/lt-ALLOWED`; call for a *different* `lt-OTHER`. If the condition does not deny (key absent → unmatched → the policy behaves as if unconditioned, matching the `ec2:InterfaceType`-doesn't-exist / inert-key class catalogued for modify-spot-fleet), the control is confirmed inexpressible. Confirm symmetrically that the **same** key *does* gate `ec2:RunInstances`.
- *Claim:* no condition key forbids `$Latest`/`$Default` on CreateFleet or RunInstances. → **Oracle:** grep `list_ec2` for any `LaunchTemplateVersion`/`DefaultVersion` key (zero hits = confirmed), then Simulate.
**Doc evidence:** `list_ec2` CreateFleet vs RunInstances rows; CreateFleet Description sentence. **Severity-if-true:** Informational→Medium — AWS-owned guarantee/expressibility gap (a customer building an attestation/compliance control on "fleet callers can only use approved launch templates" via CreateFleet permissions is relying on a non-enforceable claim). Chains directly into Area 2.
**Stop condition:** once Simulate confirms the key is inert on CreateFleet and live on RunInstances, record and stop (no resources touched).

### Area 2 — `$Latest`/`$Default` late-binding: launch-template mutation as an intra-account launch-spec privesc  [Lens B/E variant + EE pointer late-binding]
**Background.** `Version` accepts the symbolic `$Latest`/`$Default` (API Reference, quoted §3); AWS's own `instant-fleet.md` examples use `"Version":"$Latest"` in all 12 configs (the idiomatic pattern — the tutorial's pinned `"1"` is the exception, not the norm). The resolution is **unconditional and at launch time**: *"Amazon EC2 uses the latest version of the launch template."* For a `maintain`-type fleet (the tutorial's default — Area 5), launches recur over the fleet's lifetime (replenishment, health-check replacement, Capacity-Rebalance), so **each** re-launch re-resolves the pointer. Whoever can `CreateLaunchTemplateVersion` (adds a version → moves `$Latest`) or `ModifyLaunchTemplate` (moves `$Default`) thereby controls the `IamInstanceProfile`, `UserData`, AMI (`ImageId`), security groups, and network interfaces of every future SLR-launched instance — and the launch is performed by `AWSServiceRoleForEC2Fleet`, **not** by the template mutator, so the mutator never needed `iam:PassRole` or `ec2:RunInstances`.
**Security Concern.** This is the launch-spec/late-binding variant of Lens B/E ("non-PassRole actions that reach a role's live credentials … `$Latest`/`$Default` late-binding"). `ModifyLaunchTemplate`'s only `list_ec2` condition keys are `ec2:Attribute`/`ec2:Attribute/${AttributeName}`/`ec2:ManagedResourceOperator`/`ec2:Region`/`ec2:ResourceTag` — **none restricts which version becomes default**. So in an account where launch-template mutation and fleet creation are held by *different, lower-privileged* principals (a common CI/CD split — one team owns templates, platform owns fleets), the template-owner can inject an instance profile they do not hold `PassRole` for and have the fleet's SLR attach it to a running instance, then read that role's creds via IMDS.
**High-level Test Scenarios.**
- *Claim:* a principal holding only `ec2:CreateLaunchTemplateVersion`/`ec2:ModifyLaunchTemplate` on `lt-X` (no `iam:PassRole`, no `ec2:RunInstances`) can cause a `maintain` fleet referencing `lt-X:$Latest`/`$Default` to launch an instance carrying an arbitrary `IamInstanceProfile`. → **Oracle:** under a scoped principal, add a new LT version whose `IamInstanceProfile` is a higher-priv role; trigger/await a replenishment; `DescribeInstances` shows the SLR-launched instance carrying that profile. Confirmed = intra-account privesc with no PassRole. (Live test needs a canary fleet + canary role; `SimulatePrincipalPolicy` first to confirm the mutator principal is *not* denied by any PassRole/LT condition.)
- *Claim:* no IAM condition can pin the version a fleet resolves (combine with Area 1). → **Oracle:** Area-1 Simulate.
- *Claim (adjacent):* the same late-bind lets a template-owner swap the **AMI** (`ImageId`) to one the fleet caller never approved (chains to Lens EE if the AMI is name/SSM-resolved — see Area 3). → **Oracle:** version-bump the AMI, observe the next launch's AMI.
**Doc evidence:** `API_FleetLaunchTemplateSpecificationRequest` (Version semantics); `instant-fleet.md` (`$Latest` idiom); `list_ec2` ModifyLaunchTemplate/CreateLaunchTemplateVersion rows; `create-ec2-fleet.md` `maintain` replenishment. **Preconditions:** a fleet configured with `$Latest`/`$Default` (idiomatic) + a split where the template-mutator is lower-priv than the roles the template can reference. **Severity-if-true:** Medium–High (intra-account privesc; High if the reached role is materially higher-priv). **In scope** as a privesc; the "customer split their own duties" framing does **not** out-of-scope it, because the SLR-launch bypass of the caller's conditions is AWS mechanism, not the customer's policy error.
**Stop condition:** canary role creds observed via IMDS on the SLR-launched instance = confirmed; stop, do not use the creds further.

### Area 3 — `instant`-type override expansion: create-time launch-spec injection (IamInstanceProfile / UserData / MetadataOptions / SSM-AMI)  [Lens B/E/R + G/EE chains]
**Background.** `create-ec2-fleet.md`: *"For EC2 Fleets of type `instant`, you can also override the following launch template parameters: `IamInstanceProfile` … `KeyName` … `MetadataOptions`."* Plus *"For EC2 Fleets of type `instant`, you can specify a Systems Manager parameter instead of the AMI ID"* and *"you can also specify user data at the launch template specification level using the `LaunchTemplateSpecificationUserData` parameter … provide base64-encoded user data without including it in the launch template itself. User data must not exceed 16 KB."* `API_FleetLaunchTemplateOverridesRequest` confirms `IamInstanceProfile`, `ImageId`, `MetadataOptions`, `BlockDeviceMapping.N` are **`instant`-only** override fields. The tutorial omits `Type` (defaults `maintain`, where these are *not* overridable), but a reader switching to `instant` for synchronous launches — the common pattern for one-shot batch jobs like Example Corp's compute run — immediately opens all of these.
**Security Concern.** For `instant` fleets the **caller** supplies the launch spec in the `create-fleet` request, not (only) the launch template. The questions, each a documented gap:
1. **PassRole on `IamInstanceProfile` override** — does `CreateFleet` enforce `iam:PassRole` for a caller-supplied override instance profile? The CreateFleet `list_ec2` row has **no `iam-passed-role`/`instance-profile` resource type** of its own (instance-profile scoping appears only as the `ec2:InstanceProfile` key on the `instance*` row, which keys on the profile ARN, not a PassRole grant). If PassRole is not enforced on the override path, a caller passes a role they could not pass via `RunInstances`.
2. **`LaunchTemplateSpecificationUserData`** — 16 KB raw root-run boot script that **bypasses the launch template entirely** (so it is invisible to any review that only inspects the referenced template, and to any `ec2:ModifyInstanceAttribute(userData)`-style control). Classic privesc if combined with (1)'s instance profile.
3. **`MetadataOptions` override** — set `HttpTokens=optional` (re-enable IMDSv1) or a high `HttpPutResponseHopLimit`; the backbone finding is that the caller's identity-policy `ec2:MetadataHttpTokens` condition does **not** propagate to SLR launches, and here the caller can *also* positively weaken IMDS in the override → chains to SSRF-to-IMDS credential theft (Lens G).
4. **SSM-parameter `ImageId`** — `resolve:ssm`-style AMI resolution; if the parameter is attacker-influenceable or resolves to an attacker-published AMI by name, this is the whoAMI/shadow-resource shape (Lens EE).
**High-level Test Scenarios.**
- *Claim:* an `instant` `create-fleet` with an override `IamInstanceProfile` the caller lacks `iam:PassRole` for still launches. → **Oracle:** scoped principal with `ec2:CreateFleet` but **no** `iam:PassRole` for role R; `create-fleet --type instant` overriding `IamInstanceProfile=R`; `DescribeInstances` shows R attached = PassRole-bypass (Critical-class privesc if R is higher-priv). `DryRun` first (IAM-only; note DryRun is caller-IAM only, not an ownership oracle).
- *Claim:* `LaunchTemplateSpecificationUserData` executes without appearing in the referenced LT. → **Oracle:** launch an `instant` fleet with a benign canary user-data (e.g. a timestamped tag write by the instance), confirm it ran though the LT has no user-data.
- *Claim:* the `MetadataOptions` override can set IMDSv1 regardless of an identity-policy `ec2:MetadataHttpTokens=required` Deny. → **Oracle:** Simulate + canary launch; inspect `DescribeInstances` `MetadataOptions.HttpTokens`.
**Doc evidence:** `create-ec2-fleet.md` `instant`-override list + `LaunchTemplateSpecificationUserData`; `API_FleetLaunchTemplateOverridesRequest`; `list_ec2` CreateFleet row (no PassRole/instance-profile resource). **Preconditions:** `--type instant`; a canary role/profile; a canary AMI/SSM param for (4). **Severity-if-true:** PassRole bypass = High–Critical (privesc); userData/IMDS/AMI injection = Medium–High. **In scope** (SLR-launch mechanism + create-path authz, not a customer policy error).
**Stop condition:** canary profile/role observed on the instance, or canary user-data executed = confirmed; stop.

### Area 4 — Weighting overshoot × InstanceRequirements × MaxTotalPrice: cost/instance-type blast radius (deep layer under hub Area 9)  [Lens L / business-logic]
**Background (owns the *depth* the hub summarizes).** `ec2-fleet-instance-weighting`: round-up with **no stated ceiling** — *"even if the capacity of the instances launched exceeds the requested target capacity"* (the only overshoot sentence; the page's own worked example delivers 16 units against a request for 10 = 60% overshoot). `diversified` **compounds** overshoot because each selected pool independently `ceil(share/weight)`-rounds (`ec2-fleet-allocation-strategy` + the weighting page's 3-pools-of-8-for-30 → 32-units example). `ec2-fleet-control-spending`: `MaxTotalPrice` *"the fleet stops launching instances"* — a **pre-launch block**, demonstrated **only on unweighted whole-instance arithmetic**; there is **zero documented text** on how the "stop before the next launch" gate behaves when the next weighted launch jumps total capacity/cost in a large discrete step (weight-sized, not unit-sized). Per-override `MaxPrice` (the tutorial's `"0.90"` on `r3.8xlarge`) vs the global/implied price has **no documented precedence rule** anywhere in the corpus. `InstanceRequirements` (attribute-based, mutually exclusive with `InstanceType`) selects a *"wide range of instance types"* incl. future generations; price protection is on by default (`OnDemandMaxPricePercentageOverLowestPrice` default 20%) but **explicitly defeatable** with `999999`.
**Security Concern.** A lower-privileged principal who can set `WeightedCapacity`, choose `diversified`, swap `InstanceType`→`InstanceRequirements` with loose bounds, and set price-protection `999999`, can launch materially more / larger / costlier capacity than a budget/SCP/quota sized on the walkthrough's clean 1:1 (20 units = 20 small instances) assumption would predict — while every value is spec-compliant. This is a self-inflicted footgun **except** where it crosses a trust boundary: a junior role bounded by a cost SCP / Service-Quota / a `MaxTotalPrice` the operator believed was a hard cap.
**High-level Test Scenarios.**
- *Claim:* small `TotalTargetCapacity` + large mutually-prime `WeightedCapacity` under `diversified` yields overshoot ratio ≫1 while spec-valid. → **Oracle:** `DescribeFleetInstances` unit-sum vs target.
- *Claim:* a weighted next-launch step overshoots `MaxTotalPrice` (the gate blocks on unit granularity, not weight granularity). → **Oracle:** set `SpotOptions.MaxTotalPrice` just below a single weighted instance's hourly cost; observe whether 0, 1 (overshoot), or an error results. Documented silence makes any of the three plausible.
- *Claim:* `InstanceRequirements` + price-protection `999999` launches an instance type far costlier than the walkthrough's r3 family. → **Oracle:** loose `VCpuCount`/`MemoryMiB` + `999999`; inspect launched types.
- *Claim:* per-override `MaxPrice` vs global precedence is as the operator assumes. → **Oracle:** conflicting global vs override `MaxPrice`; observe which binds.
**Doc evidence:** the five quotes in §3. **Severity-if-true:** Low–Medium; **in scope only** when a lower-priv principal triggers it under a budget/SCP/quota sized on the false 1:1 assumption (otherwise §7 out-of-scope self-footgun).

### Area 5 — The tutorial's hidden default `Type=maintain`: long-lived, auto-replenishing, event-emitting  [Lens U / context-setter]
**Background.** The config omits `Type`; the API default is `maintain` (quoted §2). The tutorial text never tells the reader this — a reader may assume a one-shot provisioning of 20 units. `maintain` means: asynchronous, **auto-replenishes interrupted Spot** (re-resolving the launch template each time → Area 2's recurrence), supports `ReplaceUnhealthyInstances`, and **emits EventBridge events** (`request`/`maintain` emit; `instant` does not — cross-ref `monitor-ec2-fleet-using-eventbridge` / `fleet-monitor` plans).
**Security Concern.** This is a context-correcting lead, not a standalone bug: it establishes that this walkthrough's fleet is **persistent**, which is the precondition that upgrades Area 2 from "one launch" to "every future replenishment" and ties the fleet to the EventBridge push-channel surface owned by the monitoring siblings. It also means `ExcessCapacityTerminationPolicy` (default `termination` per the CLI skeleton) governs what happens on a capacity reduction — cross-ref the modify/terminate-primitive siblings.
**High-level Test Scenarios.**
- *Claim:* a config with no `Type` produces a `maintain` fleet that persists and re-launches. → **Oracle:** `DescribeFleets` on the tutorial config shows `Type=maintain`, `ActivityStatus` ongoing; interrupt an instance, observe replenishment re-resolving the LT.
**Doc evidence:** `API_CreateFleet` Type default; `create-ec2-fleet.md`; `ec2-fleet-request-type.md`. **Severity-if-true:** Informational (enables Area 2 + monitoring-sibling leads). **Defers:** EventBridge event-stream analysis to `monitor-ec2-fleet-using-eventbridge` / `fleet-monitor` plans; terminate-on-excess to the modify/delete plans.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Pin which LT / forbid `$Latest` on a fleet caller | CreateFleet IAM | **No `ec2:LaunchTemplate`/version key on CreateFleet** (present only on RunInstances) — Area 1 |
| Inject an instance profile/userData/AMI via a template a fleet late-binds | `$Latest`/`$Default` + ModifyLaunchTemplate | Launch performed by SLR; no PassRole needed by mutator; no version-pinning key — Area 2 |
| Inject launch spec at create time on an `instant` fleet | `create-fleet` `instant` overrides | PassRole/IMDS/AMI-owner enforcement on the override path (unknown — test) — Area 3 |
| Weaken IMDS to v1 on fleet instances | `MetadataOptions` override (instant) | Identity-policy `ec2:MetadataHttpTokens` does not propagate to SLR launch — Area 3 |
| Overshoot a 1:1-sized budget/quota | weighting + diversified + 999999 price-protection | round-up by design (no ceiling); `MaxTotalPrice` only demoed unweighted — Area 4 |
| Reader assumes one-shot; gets persistent fleet | omitted `Type` | API default `maintain` (tutorial never states it) — Area 5 |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Capacity-Reservation consumption, cross-account/cross-Org CR trust, CR-Fleet SLR policy, billing transfer, CR groups, Capacity Blocks, interruptible reclaim** — entirely owned by the **hub plan `fleet-tutorials-attack-research-plan.md`** (its Areas 1–8). Not restated here.
- **SLR launch condition-key non-propagation (general), PassRole/confused-deputy depth, cancel/terminate internals, auto-scaling control loop, EventBridge/CloudWatch monitoring, tag-authz** — owned by the sibling plans (`ec2-fleet`, `spot-fleet-prerequisites`, `create-spot-fleet`, `modify-*`, `delete-fleet`, scaling + monitoring families). Cross-referenced where they touch (Areas 2/3/5).
- **The `ec2-fleet-prerequisites` sample user policy (`ec2:*` on `*` + `iam:PassRole` role-name-prefix `DevTeam*`)** — owned by **hub Area 9**; cross-ref only, do not re-audit.
- **Self-inflicted single-account cost footguns** (weighting overshoot, price-protection-off, `MaxTotalPrice` edges, shared `Priority`) — in scope **only** under a mis-sized budget/SCP/quota crossed by a lower-priv principal (Area 4); otherwise documented design.
- **The customer's own fleet IAM policy** — a customer footgun, not reportable. Only AWS-authored artifacts and AWS-owned expressibility/parity gaps (Area 1) are reportable.
- **`file://` CLI local-file read, `--generate-cli-skeleton`** — client-side CLI behavior, out of scope.
- **CR brute-force / `lt-`/`fleet-` ID enumeration at 17-hex entropy** — not feasible; assume IDs leak via CloudTrail/tags/config.
- **AWS service plane** (the SLR's own identity, AWS-owned fleet hosts) — hard stop, not a target.

## 8. Null hypotheses / doc gaps (lenses checked, pages named)
- **No `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource`/version condition key on `CreateFleet`** — confirmed by grepping the full CreateFleet row in `list_ec2.md`; present on `RunInstances`. *Confirmed — it's the Area 1 finding, not a gap.*
- **`$Latest`/`$Default` late-binding is unconditional and at launch time** — confirmed from `API_FleetLaunchTemplateSpecificationRequest`. *Confirmed.*
- **PassRole enforcement on an `instant` override `IamInstanceProfile`** — **doc gap**; neither the UserGuide nor `list_ec2` states whether `iam:PassRole` is checked for a caller-supplied override instance profile on CreateFleet. Area 3 needs a live scoped test to settle (highest-value open question on this page).
- **`MaxTotalPrice` behavior with weighted step-jumps** — **doc gap**; `ec2-fleet-control-spending` documents only unweighted arithmetic and never addresses weight-sized discrete overshoot of the stop-gate (Area 4).
- **Per-override `MaxPrice` vs global precedence** — **doc gap**; no page in the corpus states the precedence rule (Area 4).
- **`WeightedCapacity` bounds** — min/max/decimals/zero/negative are **absent** from the weighting UserGuide page; the CLI skeleton shows `WeightedCapacity: 0.0` (float). Confirm bounds against `API_FleetLaunchTemplateOverridesRequest` before modelling an extreme-weight overshoot.
- **`Context` parameter = "Reserved."** (`API_CreateFleet`) — undocumented opaque knob, same as the modify-spot-fleet `Context`. Flag; no documented semantics to test from docs alone.
- **API Reference `request`-type bullet typo** ("does submit" vs the UserGuide's "does not submit") — a documentation inconsistency, not a security finding; do not silently rely on either phrasing for a `request`-type behavioral claim.
- **Lenses that did not fire (pages read):** SSRF/G (no server-side-fetch field in the walkthrough, create-fleet, weighting, allocation, spending, or attribute-selection pages — except the Area-3 `MetadataOptions`/SSM chains, carried as chains not standalone); Q upload (none); K prompt-injection (no LLM/agent); H/W/Y/FF/DD/CC/BB (no KMS-context, attestation, transport, token, cache, upstream-context, or multi-parser HTTP router surface in these pages) — N/A for this documentation set; re-open if a console/API path with those shapes is found.

---
*Page-level deep-dive child of the `fleet-tutorials.html` hub (`fleet-tutorials-attack-research-plan.md`)
for `ec2-fleet-instance-weighting-walkthrough.html`. Owns the launch-template-config construction surface
($Latest/$Default late-binding, instant-override injection, CreateFleet-vs-RunInstances IAM parity) and
the deep weighting/spending math; defers the entire Capacity-Reservation consumption surface to the hub
and SLR/PassRole/scaling/monitoring/tag depth to the siblings. Companion to the 20 existing fleet/spot-fleet
plans in this directory.*
