# Spot Fleet Automatic Scaling — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/spot-fleet-automatic-scaling.html` and its children `spot-fleet-target-tracking.html`, `spot-fleet-step-scaling.html`, `spot-fleet-scheduled-scaling.html`, `spot-fleet-auto-scaling-IAM.html`; the AWS-managed policies `AmazonEC2SpotFleetAutoscaleRole` (legacy) and `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` (the current SLR policy, ARN `arn:aws:iam::aws:policy/aws-service-role/AWSApplicationAutoscalingEC2SpotFleetRequestPolicy`); Application Auto Scaling UG `application-auto-scaling-service-linked-roles.html`, `auth-and-access-control.html`, `security_iam_service-with-iam.html`, `security-iam-awsmanpol.html`; `API_RegisterScalableTarget.html`; and the IAM Service Authorization References `list_ec2` and **`list_application-autoscaling`** (note the hyphenated slug — the non-hyphen `list_applicationautoscaling` 404s; the hyphenated page is also in the mirror). Online + offline mirror (`/work/aws-docs`) cross-checked. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope note / relationship to siblings.** This is the **automatic-scaling / cross-service-control-loop companion** to the existing Spot Fleet plans. It is deliberately distinct: the six prior plans (`spot-fleet`, `create-spot-fleet`, `modify-spot-fleet`, `tag-spot-fleet`, `manage-spot-fleet`, `spot-fleet-states`, `delete-fleet`) own the *EC2-side* IAM, launch-spec, lifecycle, tagging and read surfaces. **This plan owns the second control plane that none of them cover: Application Auto Scaling + CloudWatch driving `ec2:ModifySpotFleetRequest` on the customer's behalf.** The new, under-reviewed primitive here is that capacity (and therefore instance *launch* and *termination*) is now mutated by a *second AWS service's* service-linked role and by *AWS-managed/AWS-published IAM artifacts*, not by the fleet owner directly. Where a lead reaches the EC2-side `ModifySpotFleetRequest` terminate/launch primitive, it **cross-references `modify-spot-fleet-attack-research-plan.md`** rather than restating it.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- These are **single-account / delegation-centric** services (per the fleet-services memory): the highest-value leads are **intra-account privilege / blast-radius escalation via AWS-authored (managed / uneditable / copy-verbatim) IAM artifacts**, confused-deputy via a caller-suppliable `RoleARN`, and documented-guarantee-vs-enforcement gaps in the scaling control loop — **not** classic cross-tenant IDOR (scalable targets and alarms are per-account).
- Trust the **IAM Service Authorization Reference (`list_ec2`, `list_applicationautoscaling`)** over User-Guide prose when they disagree (see the reusable doc-vs-reference contradiction established in the sibling plans).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives
1. Show that a principal holding **only an AWS-authored auto-scaling IAM artifact** (the `AmazonEC2SpotFleetAutoscaleRole` managed policy, or the EC2 UG's published sample policy) can perform a fleet action its description implies it cannot — specifically modify/terminate the capacity of a Spot Fleet it does not own, or create an unrelated service-linked role.
2. Show that the **Application Auto Scaling SLR** (`AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`) can be made to modify a fleet's capacity the registering caller does not own, or that its attached policy exceeds its stated purpose.
3. Show that a **caller-suppliable `RoleARN`** on the scalable target lets a principal make Application Auto Scaling act with a role the caller could not use directly (confused deputy).
4. Show that a **documented scaling guarantee** ("does not scale below minimum / above maximum capacity") is enforced only by orchestration and can be bypassed (direct `ModifySpotFleetRequest`, a second policy, or a scheduled action) → cost/availability impact.
5. Show that the scaling control loop can be driven to **runaway scale-out (cost DoS)** or **suppressed scale-in** by tampering with the Spot-Fleet-managed CloudWatch alarm, the trigger metric, or the cooldown/weighting rounding behavior.
6. Confirm whether scaling-initiated capacity changes are **attributable in CloudTrail** to the human who configured them, or obscured behind the SLR.

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** "Automatic scaling for Spot Fleet is made possible by a combination of the Amazon EC2, Amazon CloudWatch, and Application Auto Scaling APIs." Three control planes cooperate to mutate one EC2 resource:

- **Customer-facing interface:** SigV4 IAM APIs across three services — `ec2:*SpotFleet*` (EC2), `application-autoscaling:*` (register scalable target, put scaling policy, put scheduled action), `cloudwatch:PutMetricAlarm`/`DeleteAlarms`/etc. Plus the EC2 console "Auto Scaling" / "Scheduled Scaling" tabs. AWS CLI uses the `application-autoscaling` command set. (Legacy API — "no planned investment"; AWS recommends EC2 Fleet / ASG instead.)
- **The scalable resource:** a **Spot Fleet request**, id shape `sfr-<UUID>` (128-bit → not enumerable; see sibling IDOR null). As an Application Auto Scaling scalable target it is addressed by the triple **`ServiceNamespace=ec2`, `ResourceId=spot-fleet-request/sfr-xxxx`, `ScalableDimension=ec2:spot-fleet-request:TargetCapacity`** — all **caller-supplied strings** (critical for Lens S/A below).
- **Processes / identities behind the interface:**
  - *Application Auto Scaling control loop* — polls CloudWatch, computes the capacity adjustment, calls `ec2:ModifySpotFleetRequest` to set `TargetCapacity`. Runs under the **SLR `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`** (service principal `ec2.application-autoscaling.amazonaws.com`).
  - *CloudWatch alarms* — for **target tracking**, "Spot Fleet then creates and manages the CloudWatch alarms"; for **step scaling**, the *customer* supplies the alarm/metric.
  - *EC2 Spot Fleet* — executes the capacity change: scale-out launches Spot Instances (via the **Spot Fleet SLR** — see `create-spot-fleet` plan; identity-policy `RunInstances` conditions do NOT propagate), scale-in terminates them ("the instance receives a Spot Instance interruption notice").
- **Roles / privilege levels:**
  - `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest` — the current default SLR; attached policy `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` resolved in Area S1 (5 actions — `ec2:DescribeSpotFleetRequests`, `ec2:ModifySpotFleetRequest`, `cloudwatch:PutMetricAlarm/DescribeAlarms/DeleteAlarms` — all `Resource:"*"`, no Condition).
  - **Legacy managed policy `AmazonEC2SpotFleetAutoscaleRole`** (service-role policy, ARN `arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetAutoscaleRole`, v3, created 2016 / edited 2019) — the pre-SLR `aws-ec2-spot-fleet-autoscale-role`. Docs say it "is no longer required" but **the managed policy is still published and attachable**. (Lead X1.)
  - The **human caller** who configures scaling, holding either `application-autoscaling:*` + the EC2/CloudWatch actions (the UG sample) or a fine-grained custom policy.
- **Untrusted-data entry points:** the trigger **metric** (step scaling can use *custom* metrics the customer publishes), the **cooldown**/**min-max bound** parameters, the **cron/at schedule expression** (scheduled scaling), and the **`RoleARN`** on the scalable target.
- **KMS / secrets:** none generated by this surface (null — see §8).

```
                 ┌─────────────────────────── customer AWS account ────────────────────────────┐
   human caller ─┤ application-autoscaling: RegisterScalableTarget / PutScalingPolicy /         │
 (UG sample pol. │                          PutScheduledAction  [+ optional RoleARN]            │
  or custom)     │ cloudwatch: PutMetricAlarm / DeleteAlarms                                     │
                 │ iam: CreateServiceLinkedRole                                                  │
                 └───────────────┬──────────────────────────────────────────────────────────────┘
                                 │ registers sfr-xxxx as scalable target
                                 ▼
   CloudWatch  ──metric/alarm──►  Application Auto Scaling control loop
   (TargetCapacity, CPUUtil,     (runs as SLR AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest)
    custom metrics)              │
                                 │ ec2:ModifySpotFleetRequest  (set TargetCapacity)   ◄── Resource:"*", no Condition
                                 ▼
                           EC2 Spot Fleet  ──► scale-out: RunInstances via Spot Fleet SLR (launch primitive)
                                            └─► scale-in : terminate Spot Instances   (terminate primitive)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Human caller (holds scaling policy only) | A Spot Fleet request they do **not** own | `RegisterScalableTarget` + `PutScalingPolicy`/`ModifySpotFleetRequest` on `Resource:"*"` | Registering/scaling/terminating a fleet owned by another team/role in the account where the owner intended an ownership scope → **intra-account authz gap** |
| Human caller | Application Auto Scaling (acts via SLR) | `RegisterScalableTarget` with a `RoleARN` the caller chooses | App Auto Scaling performs `ModifySpotFleetRequest` using a role the caller could not assume/pass directly → **confused deputy** |
| App Auto Scaling SLR | EC2 Spot Fleet capacity | SLR policy `ec2:ModifySpotFleetRequest` on `Resource:"*"` with no Condition | SLR modifies/terminates a fleet outside the scalable target the caller legitimately registered |
| Scaling *orchestration* (soft bound) | EC2 fleet target capacity (hard state) | min/max enforced in App Auto Scaling, not in `ModifySpotFleetRequest` | Capacity set below min / above max via a path that skips the orchestration → **documented-guarantee bypass** |
| CloudWatch metric publisher | Another principal's scaling decision | step-scaling trigger metric (incl. custom metrics) | A metric value the owner does not control drives scale-out/in of their fleet (cost/availability) |
| Any customer surface | **AWS's own service plane** | — | **HARD STOP** — any AWS-fleet identity/ARN/account = disclosure, preserve evidence |

---

## 4. API / Interface Inventory

| Name | Service | Mutating | Facing | Functionality | Authorized callers (per UG sample) | Notes |
|---|---|---|---|---|---|---|
| `RegisterScalableTarget` | application-autoscaling | ✔ | External | Register `sfr-xxxx` as scalable target; set min/max; **optional `RoleARN`** | anyone with `application-autoscaling:*` | Triggers SLR auto-create via `iam:CreateServiceLinkedRole`. `RoleARN` → Lens B |
| `DeregisterScalableTarget` | application-autoscaling | ✔ | External | Remove scalable target | same | revocation-completeness → Lens AA |
| `PutScalingPolicy` | application-autoscaling | ✔ | External | Target-tracking / step policy; for target-tracking **creates+manages CW alarms** | same | metric/threshold = control input |
| `PutScheduledAction` | application-autoscaling | ✔ | External | Cron/at capacity change; min/max at a time | same | schedule expression input → Lens P/U |
| `DescribeScalableTargets` / `DescribeScalingPolicies` / `DescribeScheduledActions` / `DescribeScalingActivities` | application-autoscaling | ✘ | External | Read scaling config/history | same | read-side scopability → Lens S |
| `ec2:ModifySpotFleetRequest` | ec2 | ✔ | External | Set `TargetCapacity` (launch/terminate primitive) | SLR + any holder of the artifact | **see `modify-spot-fleet` plan**; `list_ec2` requires `spot-fleet-request*` + accepts `launch-template` |
| `ec2:DescribeSpotFleetRequests` | ec2 | ✘ | External | Read fleet config | SLR + caller | sibling `manage-spot-fleet`: BLANK resource cell, `ec2:Region` only → unscopable |
| `cloudwatch:PutMetricAlarm` / `DeleteAlarms` | cloudwatch | ✔ | External | Create/delete trigger alarms (incl. the ones Spot Fleet manages) | caller + SLR | Lens L/O — tamper managed alarm |
| `iam:CreateServiceLinkedRole` | iam | ✔ | External | Create the App Auto Scaling SLR | caller | UG sample = `Resource:"*"` **no condition** → Lens R |
| `sns:CreateTopic`/`Subscribe`/`Get*`/`List*` | sns | ✔/✘ | External | Scaling notifications | caller | `Resource:"*"` in UG sample |

**Undocumented/hidden knob:** the `RoleARN` property of `AWS::ApplicationAutoScaling::ScalableTarget` is accepted **"even if the specified service-linked role doesn't yet exist"** (SLR doc, note after the ARN table) — a caller-supplied role field that the console flow (which uses the default SLR) does not surface. Enumerate what else `RegisterScalableTarget`/`PutScalingPolicy` accept beyond the console (custom-metric spec, `Cooldown`, `DisableScaleIn`, step bounds to `±infinity`).

---

## 5. Recommended Areas of Focus

### Area R1 — AWS-authored IAM artifacts: unconditioned `ModifySpotFleetRequest` + over-broad `CreateServiceLinkedRole` (Lens R / S / U) — PRIORITY
**Background.** Two AWS-authored artifacts ship for this surface and the customer attaches/copies them verbatim: (a) the AWS-**managed** policy `AmazonEC2SpotFleetAutoscaleRole` (uneditable), and (b) the EC2 UG's printed **sample** policy on `spot-fleet-auto-scaling-IAM.html`.

**Security Concern.** Both grant the launch/terminate primitive `ec2:ModifySpotFleetRequest` (and `ec2:DescribeSpotFleetRequests`, `cloudwatch:PutMetricAlarm`/`DeleteAlarms`) on **`Resource:"*"` with no Condition** — so a principal holding only the artifact can modify/terminate the capacity of **any** Spot Fleet in the account, not just one it owns. The sibling `modify-spot-fleet` plan establishes `ModifySpotFleetRequest` + `ExcessCapacityTerminationPolicy=default` is a terminate primitive and `TargetCapacity`-increase is a launch primitive. **Additionally**, the EC2 UG sample grants `iam:CreateServiceLinkedRole` on **`Resource:"*"` with no `iam:AWSServiceName` condition** — strictly broader than AWS's *own* Application Auto Scaling UG example and the legacy managed policy, both of which scope that action to the single SLR ARN with the `iam:AWSServiceName = ec2.application-autoscaling.amazonaws.com` condition. The UG sample therefore lets its holder create **any** service-linked role.

**High-level Test Scenarios.**
- **Claim:** A role holding *only* `AmazonEC2SpotFleetAutoscaleRole` can `ModifySpotFleetRequest` on a fleet it does not own → terminate it. **Mechanism:** policy JSON lines 40–46 — `ec2:ModifySpotFleetRequest` on `"*"`, no Condition. **Oracle:** `iam:SimulatePrincipalPolicy` for the action against a foreign `sfr-*` ARN returns `allowed` (safe first oracle); escalate only with a scoped role + canary fleet. **Severity:** High (intra-account, AWS-managed uneditable artifact → Tier 2 report).
- **Claim:** A principal holding the UG sample policy can create a service-linked role unrelated to auto-scaling. **Mechanism:** `iam:CreateServiceLinkedRole` on `"*"` with no `iam:AWSServiceName` condition in the sample vs the scoped version AWS itself recommends. **Oracle:** diff the two published JSON blocks; `SimulateCustomPolicy` of the sample against `CreateServiceLinkedRole` for an arbitrary `AWSServiceName`. **Severity:** Medium (over-broad AWS-published sample → report; customer who copies it inherits the defect).
- **Claim (U):** The UG sample's `application-autoscaling:*` wildcard exceeds what the console scaling workflow needs. **Oracle:** map the console flow's actual calls vs the wildcard; any action in the wildcard not on the path = over-grant. **Severity:** Low–Medium.

**Doc evidence:** `AmazonEC2SpotFleetAutoscaleRole.html` JSON; `spot-fleet-auto-scaling-IAM.html` sample policy + "it creates a service-linked role named …"; `application-auto-scaling-service-linked-roles.html` scoped example. **Severity-if-true:** High (artifact is AWS-authored + uneditable/copy-verbatim).

### Area S1 — Application Auto Scaling SLR policy: unconditioned, and left un-hardened where AWS hardened its siblings (Lens R / S / E) — PRIORITY
**Background.** Enabling auto-scaling auto-creates `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest` (trust `ec2.application-autoscaling.amazonaws.com`), attached policy **`AWSApplicationAutoscalingEC2SpotFleetRequestPolicy`** (`arn:aws:iam::aws:policy/aws-service-role/…`; type = service-linked-role policy, "you cannot attach … and an IAM admin can view, but not edit the permissions"). **Resolved verbatim**, it is a single statement granting exactly five actions, **all on `Resource:"*"` with no Condition:**

| Action | Resource | Condition |
|---|---|---|
| `ec2:DescribeSpotFleetRequests` | `*` | none |
| `ec2:ModifySpotFleetRequest` | `*` | none |
| `cloudwatch:PutMetricAlarm` | `*` | none |
| `cloudwatch:DescribeAlarms` | `*` | none |
| `cloudwatch:DeleteAlarms` | `*` | none |

**Security Concern.** (1) `ec2:ModifySpotFleetRequest` is unconditioned `"*"` even though `list_ec2` confirms the action **supports** `spot-fleet-request*` ARN + `aws:ResourceTag`/`ec2:ResourceTag` scoping — so the control loop's IAM blast radius is *every* fleet in the account, not the one target the caller registered. (2) **Comparative tell (strong Lens R signal):** on the *same* `security-iam-awsmanpol.html` page, AWS has deliberately scoped the sibling SLR policies' alarm actions — ElastiCache / Neptune / SageMaker AI / WorkSpaces restrict `cloudwatch:PutMetricAlarm`/`DeleteAlarms` to `arn:aws:cloudwatch:*:*:alarm:TargetTracking*` — and the page's changelog records AWS *retrofitting* exactly this ("[SageMaker policy] now restricts … `PutMetricAlarm` and `DeleteAlarms` … to CloudWatch alarms that are used with target tracking scaling policies," **November 13, 2023**). **No equivalent hardening changelog ever appears for the Spot Fleet policy** — its `PutMetricAlarm`/`DeleteAlarms` remain on `"*"`, so the SLR can create/delete *any* alarm in the account, not only its own `TargetTracking*` alarms. The gap is AWS-authored and uneditable → in scope, Tier-2.
**High-level Test Scenarios.**
- **Claim:** the Spot Fleet SLR policy permits `ec2:ModifySpotFleetRequest` / `cloudwatch:DeleteAlarms` against a fleet/alarm the registration never named. **Oracle:** `iam:GetPolicyVersion` on `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` → read statement (done, above); `iam:SimulatePrincipalPolicy` for the action against an unrelated fleet/alarm ARN → `allowed`. The service's internal targeting is then the *only* control, not IAM. **Severity:** Medium–High (AWS-authored over-grant; blast radius exceeds one-fleet/one-policy purpose).
- **Claim:** the SLR can delete/overwrite an *unrelated* customer alarm (not `TargetTracking*`) because `DeleteAlarms`/`PutMetricAlarm` are on `"*"`. **Oracle:** compare the Spot Fleet policy's alarm resource (`"*"`) to the siblings' `alarm:TargetTracking*`. **Severity:** Medium.
**Doc evidence:** `security-iam-awsmanpol.html` (policy JSON + sibling-scoping + changelog); `spot-fleet-auto-scaling-IAM.html` SLR paragraph; `list_ec2` `ModifySpotFleetRequest` scopability. **Severity-if-true:** Medium–High. **Pending empirical confirm:** whether AAS's backend *compensates* by internally filtering the unscoped calls to the registered resource is undocumented — must be confirmed before escalating beyond "IAM artifact over-grants."

### Area B1 — Caller-suppliable `RoleARN` on the scalable target (Lens B / C — confused deputy)
**Background.** The SLR is "the default role," but `RegisterScalableTarget` / `AWS::ApplicationAutoScaling::ScalableTarget` accept a **`RoleARN`** property, and the legacy custom role `aws-ec2-spot-fleet-autoscale-role` predates the SLR.
**Security Concern.** If a caller can register a scalable target with a `RoleARN` of their choosing, Application Auto Scaling will later assume that role and call `ModifySpotFleetRequest` under it — making the service act with a role the caller may not be able to use directly, with no `iam:PassRole` gate documented on this path.
**High-level Test Scenarios.**
- **Claim:** `RegisterScalableTarget` lets a caller pass a role whose downstream use they could not perform directly. **Mechanism:** `RoleARN` is `Required: No` and documented as "required for services that do **not** support service-linked roles … If the service supports service-linked roles, Application Auto Scaling uses a service-linked role." The AAS API model lists `iam:PassRole` with condition `iam:PassedToService: application-autoscaling.amazonaws.com` for `RegisterScalableTarget` — but that **pins only the target service principal, not which role**, so any role the caller already holds `PassRole` for can be passed. **Doc-gap (flag, don't assume):** the docs do **not** state what happens if a caller supplies a `RoleARN` anyway for the `ec2` namespace (which *does* support an SLR) — ignored? honored and preferred over the SLR? The SLR doc even notes the `RoleARN` property is accepted "even if the specified service-linked role doesn't yet exist." **Oracle:** register a Spot Fleet scalable target with a caller-chosen `RoleARN` and observe whether AAS honors it over the SLR for the subsequent `ModifySpotFleetRequest`. **Severity:** High if a non-SLR caller-role is honored; Critical only if a cross-account target is accepted (no doc evidence it is).
- **Claim:** the role's trust policy only requires `application-autoscaling.amazonaws.com`, enabling a confused-deputy if `aws:SourceArn`/`aws:SourceAccount` is absent. **Oracle:** read the SLR/custom-role trust policy for a scoping condition key. **Severity:** Medium–High.
**Doc evidence:** SLR doc `RoleARN` note; `spot-fleet-auto-scaling-IAM.html` "original managed Spot Fleet role … was `aws-ec2-spot-fleet-autoscale-role`". **Severity-if-true:** High.

### Area A1 — Scalable-target registration: ownership of the fleet is IAM-unscopable, so the control loop is a cross-ownership terminate/launch primitive (Lens A / S / R) — PRIORITY
**Background.** The scalable target is addressed by a **caller-supplied string triple** (`ServiceNamespace=ec2`, `ResourceId=spot-fleet-request/sfr-xxxx`, `ScalableDimension=ec2:spot-fleet-request:TargetCapacity`). Resolved from `list_application-autoscaling`: the write actions (`RegisterScalableTarget`, `PutScalingPolicy`, `PutScheduledAction`, `DeregisterScalableTarget`) take resource type `ScalableTarget*` but their **only** non-tag condition keys are **`application-autoscaling:service-namespace`** and **`application-autoscaling:scalable-dimension`** — and both are *fixed enum-like strings shared by every Spot Fleet in the account* (`ec2` / `ec2:spot-fleet-request:TargetCapacity`). **There is NO `application-autoscaling:resource-id` (or equivalent) condition key** — contrary to a tempting assumption. The `ScalableTarget` ARN *does* carry a per-target id, but it is an **AAS-minted opaque id assigned at registration** (e.g. `scalable-target/1234abcd…`), *different from* the EC2 `sfr-` id, doesn't exist until after registration, and is taggable only via `aws:ResourceTag`.
**Security Concern.** Therefore a policy author **cannot** write "this principal may only register/scale *my* fleet" — the only IAM-enforceable discriminator (`scalable-dimension`) is identical for every Spot Fleet. Combined with (a) the SLR's unconditioned `ec2:ModifySpotFleetRequest` (Area S1) and (b) no documented EC2-side ownership check at `RegisterScalableTarget` time (the API only pattern-validates `ResourceId`; its own text says "If the specified resource is not active … this operation does not change the resource's current capacity," implying registration succeeds and the check is *deferred* to the first scaling action), the ownership check may exist in **neither** layer. `sfr-<UUID>` is 128-bit so cross-*tenant* fabrication is a genuine null; the realistic target is **intra-account cross-team** (a known `sfr-` id another team owns). This is the two-hop chain: a caller with only `application-autoscaling:*` (no `ec2:ModifySpotFleetRequest`, no `ec2:TerminateInstances`) reaches, via the AAS SLR → the EC2 Spot Fleet SLR, the terminate primitive documented in `modify-spot-fleet-attack-research-plan.md`.
**High-level Test Scenarios.**
- **Claim:** a principal holding only `application-autoscaling:RegisterScalableTarget`+`PutScalingPolicy` can register a *foreign-owned* `sfr-xxxx` and drive capacity to 0 (terminate) via the SLR. **Oracle:** two scoped roles in one account — role A owns the fleet; role B holds only AAS write actions; B registers A's `sfr`, attaches a scale-in-to-0 policy (`ExcessCapacityTerminationPolicy=default`), observe A's instances terminate. `SimulatePrincipalPolicy` first (no `Deny` fires); live only with canaries. **Severity:** High (intra-account destructive privilege escalation across an ownership boundary, enabled by an AWS-authored condition-key omission + unconditioned SLR).
- **Claim (S):** no customer-authored Deny can pin registration to owned fleets, because the only key available (`scalable-dimension`) is shared. **Oracle:** attempt to author such a scoping policy — show it is impossible with the published key set. **Severity:** Medium–High (ABAC structurally impossible, not merely inert).
- **Claim (U, doc-gap):** `RegisterScalableTarget` performs no EC2 ownership/existence check at call time. **Oracle:** register a nonexistent/foreign `sfr` → observe success. **Severity:** feeds the above.
**Doc evidence:** `list_application-autoscaling` (resource type `ScalableTarget`, condition keys = service-namespace + scalable-dimension + tags only, **no resource-id**); `security_iam_service-with-iam.html` (AAS-minted opaque ARN id); `API_RegisterScalableTarget.html` (`ResourceId` pattern-only validation; deferred-activation sentence); Area S1 SLR policy. **Severity-if-true:** High.

### Area U1 — Min/max capacity bound: documented guarantee vs enforcement (Lens U) — PRIORITY
**Background.** "Automatic scaling does not scale your fleet below the minimum capacity or above the maximum capacity." The bound is set on the **scalable target** (App Auto Scaling), while the actual capacity lives on the **Spot Fleet request** (EC2).
**Security Concern.** The guarantee is enforced by Application Auto Scaling orchestration, **not** by `ec2:ModifySpotFleetRequest` — the enforcement language lives entirely in the AAS API (`API_RegisterScalableTarget.html`: "**Application Auto Scaling scaling policies** will not scale capacity to values that are outside of the minimum and maximum range"), and EC2 itself has no concept of the registered min/max (`modify-spot-fleet` plan §5.5: `TargetCapacity` is an unbounded integer with no documented per-call ceiling). Any path that sets `TargetCapacity` outside the AAS loop — a direct `ModifySpotFleetRequest`, a `PutScheduledAction` with its own min/max, a second scaling policy, or the SLR itself — is not bound by the registered min/max. Note the artifact that *configures* the ceiling (the UG sample) also grants the caller plain `ec2:ModifySpotFleetRequest` on `"*"` — the same principal who sets the guardrail already holds the key that bypasses it. A holder can therefore push capacity above the "maximum" (cost blow-up) or to 0 (availability), defeating a control the owner believed was a ceiling.
**High-level Test Scenarios.**
- **Claim:** `ec2:ModifySpotFleetRequest` ignores the App Auto Scaling min/max. **Oracle:** register target with max=2, then direct `ModifySpotFleetRequest TargetCapacity=50` — observe 50 launched. **Severity:** Medium–High (cost DoS / guardrail bypass).
- **Claim:** a `PutScheduledAction` or second policy overrides the min/max bound. **Oracle:** scheduled action min=100 vs target max=2. **Severity:** Medium.
**Doc evidence:** `spot-fleet-target-tracking.html` / `-step-scaling.html` "does not scale … below the minimum … or above the maximum"; `spot-fleet-scheduled-scaling.html` min/max per action. **Severity-if-true:** Medium–High (cost/availability).

### Area L1 — Managed-alarm & control-loop tampering → runaway scale-out / suppressed scale-in (Lens L / O)
**Background.** For target tracking, "Spot Fleet then creates and manages the CloudWatch alarms"; the UG warns "Do not edit or delete the CloudWatch alarms that Spot Fleet manages." For step scaling the customer supplies the alarm, which may use **custom metrics**.
**Security Concern.** The managed alarms sit in the customer's CloudWatch and are mutable with `cloudwatch:PutMetricAlarm` (granted on `"*"` by the artifact). Editing the managed alarm's threshold/metric, or publishing a crafted value to a step-scaling **custom metric**, can force continuous scale-out (cost DoS, "Spot Fleet can exceed the target capacity") or suppress scale-in. The weighting-rounding examples in Considerations (fulfilled 30.1, subtract 1 → 29.1 → rounds to 30, no action) show scale actions can be made to **no-op**, which can also be weaponized to pin capacity.
**High-level Test Scenarios.**
- **Claim:** the "do not edit the managed alarm" guarantee is advisory prose, not an IAM control — the UG sample grants `cloudwatch:PutMetricAlarm`/`DisableAlarmActions`/`EnableAlarmActions` on `"*"`, so the configuring principal can overwrite the managed alarm's threshold (force runaway scale-out) or `DisableAlarmActions` on it (silently suppress scale-in/out while the console still shows the policy as "configured" — no tamper signal). **Oracle:** as a holder of only the UG sample policy, `DisableAlarmActions` the Spot-Fleet-created `TargetTracking*` alarm; confirm scaling stops firing while `describe-scaling-policies` still reports it enabled. **Severity:** Medium.
- **Claim (weighting-rounding scale-in no-op):** the documented float-rounds-up behavior makes scale-in silently no-op while fulfilled capacity stays above target (cost). **Mechanism:** Considerations worked examples — target 30 / fulfilled 30.1 / subtract-1 → 29.1 → rounds up to 30 → "no scaling action is taken"; and weights 2/4/8 → fulfilled 12 (20% over target 10), 20%-decrease still rounds back to 10. Compounds with AAS's own independent rounding layer. **Oracle:** reproduce the doc's own example; trigger scale-in; observe `FulfilledCapacity` does not decrease despite a "successful" scaling activity. **Severity:** Medium–High (scale-in guardrail defeated; uncontrolled spend; AWS-acknowledged, undermitigated).
- **Claim (cooldown asymmetry + "any-scales-out"):** cooldown blocks scale-in but never scale-out, and with multiple policies AAS scales out if *any* policy is ready but scales in only if *all* are — so one noisy/attacker-influenced signal keeps forcing growth with nothing throttling cost. **Mechanism:** "if another alarm triggers a scale-out policy during the cooldown period after a scale-in, automatic scaling scales out immediately … the scale-in cooldown period stops and doesn't complete"; "scale out … if **any** … scale in only if **all**." **Oracle:** two policies; drive scale-out metric into alarm while scale-in is mid-cooldown; observe uninterrupted growth. **Severity:** Medium (availability protected by design; cost is not — chains with Area L2).
- **Claim (O):** SLR-initiated `ModifySpotFleetRequest` / alarm calls are CloudTrail-attributed to `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`, not the metric/alarm/human that triggered them → no linkage without a manual `DescribeScalingActivities` correlation. **Oracle:** trigger a scaling activity; inspect the `ModifySpotFleetRequest` event `userIdentity`. **Severity:** Low–Informational (enabler; raises effective severity of U1/L1/L2 by hindering IR attribution).
**Doc evidence:** `spot-fleet-target-tracking.html` managed-alarm note; `spot-fleet-automatic-scaling.html` Considerations (weighting rounding, cooldown); `spot-fleet-auto-scaling-IAM.html` (`DisableAlarmActions` in sample); AAS `target-tracking-scaling-policy-overview.html` / `step-scaling-policy-overview.html` (rounding, flapping warning). **Severity-if-true:** Medium.

### Area L2 — Custom-metric trust gap: `cloudwatch:PutMetricData` alone steers a fleet's capacity (Lens K / U — intra-account)
**Background.** Step scaling and target tracking can be driven by **customer custom metrics** ("You can create CloudWatch alarms based on metrics provided by AWS **or your own custom metrics**"; target tracking: "use your own custom metrics published to CloudWatch"). The alarm watches metric *values*, not the publishing *principal*.
**Security Concern.** No documented binding ties the metric-publishing principal to fleet ownership beyond generic CloudWatch IAM. A low-privileged or compromised workload holding only `cloudwatch:PutMetricData` — no `ec2:*`, no `application-autoscaling:*`, no SLR relationship — can publish data points to the metric+dimension a scaling policy is bound to and thereby force fleet-wide scale-out (cost DoS) or suppress scale-in.
**High-level Test Scenarios.**
- **Claim:** a role with only `cloudwatch:PutMetricData` can scale another workload's fleet. **Oracle:** publish points matching the exact custom metric+dimension a step/target-tracking policy watches; observe capacity change attributable to that publish. **Severity:** Medium–High intra-account (a workload with no autoscaling/EC2 rights steers a production fleet's capacity and cost); **Critical only if a cross-account metric path existed — none found (see §8 null; CloudWatch OAM cross-account is an un-examined doc-gap).**
**Doc evidence:** `spot-fleet-step-scaling.html` ("your own custom metrics"); AAS `application-auto-scaling-target-tracking.html` ("your own custom metrics published to CloudWatch"). **Severity-if-true:** Medium–High (intra-account).

### Area X1 — Legacy role / action parity (Lens X / N)
**Background.** The pre-SLR path (`aws-ec2-spot-fleet-autoscale-role` + the still-published `AmazonEC2SpotFleetAutoscaleRole` managed policy) and the new SLR path both reach the same `ModifySpotFleetRequest` capability. Docs say the legacy role "is no longer required" — but it is not stated to be removed/deprecated-enforced.
**Security Concern.** During/after migration, does the legacy role still function as a usable `ModifySpotFleetRequest` path that bypasses whatever ownership/condition posture the SLR path might (eventually) enforce? Two live artifacts for one capability with potentially divergent authz coverage.
**High-level Test Scenarios.**
- **Claim:** the legacy managed policy still grants a working `ModifySpotFleetRequest` path equivalent to the SLR. **Oracle:** confirm `AmazonEC2SpotFleetAutoscaleRole` is still attachable (it is, per the published reference) and simulate the action. **Severity:** Medium (parity/least-priv; AWS-managed artifact → report).
**Doc evidence:** `spot-fleet-auto-scaling-IAM.html` "original managed … role … no longer required"; `AmazonEC2SpotFleetAutoscaleRole.html` still live (v3). **Severity-if-true:** Medium.

### Area AA1 — Revocation completeness on deregister / policy delete (Lens AA)
**Background.** "After you delete a service-linked role, Application Auto Scaling creates the role again when you call `RegisterScalableTarget`." Target-tracking deletes its managed alarms "automatically when you delete the … policy."
**Security Concern.** Does `DeregisterScalableTarget` / policy delete sever **all** downstream references — the managed CloudWatch alarms, any scheduled actions, and the SLR's ability to keep driving the fleet — or can a stale alarm / scheduled action keep mutating capacity after the operator believes scaling is off?
**High-level Test Scenarios.**
- **Claim:** a managed alarm or scheduled action survives policy/target deletion and still triggers capacity change. **Oracle:** delete the policy, enumerate residual alarms/scheduled actions, observe whether capacity still changes. **Severity:** Low–Medium.
**Doc evidence:** `spot-fleet-target-tracking.html` alarm-cleanup note; SLR delete/recreate note. **Severity-if-true:** Low–Medium.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Terminate/launch a fleet via auto-scale artifact without owning it | `ModifySpotFleetRequest` on `"*"` (managed policy + sample) | "service-linked role … to modify the capacity of the fleet" — implies scope to *your* fleet |
| Create an unrelated SLR | `iam:CreateServiceLinkedRole` `"*"` in UG sample | AWS's own example scopes it with `iam:AWSServiceName` |
| Confused deputy via caller `RoleARN` | `RegisterScalableTarget` / `ScalableTarget.RoleARN` | "The service-linked role is the default role" (implies the SLR, not an arbitrary role) |
| Register & scale a fleet owned by another team | App Auto Scaling condition keys bind to caller-supplied `ResourceId` | `application-autoscaling:resource-id` condition key (claims resource scoping) |
| Push capacity past the documented max / to 0 | min/max on scalable target vs `ModifySpotFleetRequest` | "does not scale … above the maximum capacity" |
| Runaway scale-out via managed-alarm edit | CloudWatch managed alarm + `PutMetricAlarm` `"*"` | "Do not edit or delete the CloudWatch alarms that Spot Fleet manages" (advisory only) |
| SLR capacity change not attributable to author | CloudTrail + SLR | — |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account / cross-tenant IDOR on `sfr-<UUID>`** — 128-bit id is not fabricable; genuine null. Only intra-account cross-team (known id) is in scope.
- **The Spot Fleet SLR launch guardrail-bypass** (identity-policy `RunInstances` conditions not propagating to fleet launches) — owned by `create-spot-fleet-attack-research-plan.md`; here it is only the *downstream effect* of a scale-out.
- **`ModifySpotFleetRequest` internals** (console-hidden `LaunchTemplateConfig.N`, `ExcessCapacityTerminationPolicy`, case-sensitivity fail-open) — owned by `modify-spot-fleet-attack-research-plan.md`; cross-referenced, not restated.
- **Tag-based ABAC on the fleet** — owned by `tag-spot-fleet-attack-research-plan.md`.
- **A customer who writes their own over-broad scaling policy** — least-privilege footgun (out of scope). In-scope only when the artifact is AWS-authored/uneditable/copy-verbatim.
- **CloudWatch's own multi-tenant metric isolation**, EventBridge Scheduler internals, shared CloudWatch/App-Auto-Scaling control-plane infra — AWS-shared infra / shared-responsibility line.
- **Single-tenant self-DoS** from your own flapping policy where no privilege boundary is crossed.
- IMDS on the managed scaling control plane; product/feature-parity gaps of the legacy Spot Fleet API.

---

## 8. Null hypotheses / doc gaps
- **Lens A (cross-account / cross-tenant):** null — scalable targets (`spot-fleet-request/sfr-…`), scaling policies, and the SLR are all account-scoped (`API_RegisterScalableTarget.html` `ResourceId` = same-account fleet id; one SLR per account, trust limited to the account's own `ec2.application-autoscaling.amazonaws.com`). Pages checked: all four scaling pages + `API_RegisterScalableTarget.html` + `application-auto-scaling-service-linked-roles.html`. **Caveat / doc-gap:** CloudWatch cross-account observability (OAM links) interacting with a custom-metric-driven policy (Area L2) was **not** examined — it could in principle let an alarm reference a consent-shared cross-account metric. Treat as an open follow-up, not a confirmed null, before fully closing the cross-account question.
- **Lens H (KMS / encryption context):** null — all seven scaling/AAS pages checked; this surface generates/stores no key, secret, or encryption context. (Scale-out launches may use encrypted EBS, but that is the launch-spec surface, not scaling.)
- **Lens G (SSRF):** null — read the four scaling pages; no field the scaling control plane dereferences/fetches server-side (metric names and ARNs are not fetched URLs).
- **Lens Q (upload) / F (translation injection):** null — no file upload, no query/wire-protocol translation on this surface (pages checked: all four scaling pages + IAM page). *(Lens K fires in a limited intra-account form — see Area L2 custom-metric trust — not as classic LLM prompt injection.)*
- **Lens V/D (network segmentation / data→control):** null for the scaling control loop itself — control-plane-to-control-plane API traffic (CloudWatch → AAS → `ModifySpotFleetRequest`) with no customer-reachable ENI; the data-plane angle lives on the launched instances (out of scope here). Pages checked: all four scaling pages.
- **Lens P (schedule-expression injection):** **doc-gap / low-confidence null** — scheduled scaling restricts the expression to EventBridge's documented cron grammar (linked, not reproduced) and the action is executed by AAS's backend via the SLR; no customer-controlled executor/shell path is named. The exact runtime identity that evaluates the cron and issues the capacity change is not spelled out — not confirmed to be literally EventBridge Scheduler. Confirm before testing.
- **Lens U doc-vs-doc inconsistency (file-worthy, Informational):** `spot-fleet-target-tracking.html` says "**Spot Fleet** then creates and manages the CloudWatch alarms," while AAS `application-auto-scaling-target-tracking.html` says "**Application Auto Scaling** creates and manages the CloudWatch alarms." The SLR policy (Area S1) resolves it in favor of Application Auto Scaling (its SLR holds `cloudwatch:PutMetricAlarm`), so the EC2 UG wording is imprecise.
- **`list_application-autoscaling` reference:** the authoritative resource-type/condition-key cells in Area A1/S1 were resolved from the **hyphenated slug `list_application-autoscaling`** (the non-hyphen `list_applicationautoscaling` 404s / is a JS shell WebFetch cannot render — same pitfall class as the dead `list_amazonec2` slug); the hyphenated page is mirrored at `/work/aws-docs/docs/service-authorization/latest/reference/list_application-autoscaling.md`. Facts there (no `resource-id` condition key; `ScalableTarget` ARN with AAS-opaque id) are confirmed against the mirror.
- **CloudWatch Spot Fleet metrics page unverified:** only `TargetCapacity` is verbatim-confirmed (from the step-scaling console walkthrough, breadcrumb "EC2 Spot → Fleet Request Metrics"); the namespace (`AWS/EC2Spot`) and other metric names (`FulfilledCapacity`, `PercentageOfDesiredCapacity…`, dimension `FleetRequestId`) are **inferred, not confirmed** — the metrics doc page could not be fetched. Confirm metric/namespace/dimension strings before building a metric-publish PoC (Area L2).
- **Compensating-control doc-gap (gates Area S1 escalation):** whether AAS's backend internally filters the SLR's unscoped `ModifySpotFleetRequest`/`PutMetricAlarm`/`DeleteAlarms` calls to the registered resource is undocumented. Confirm empirically before escalating Area S1 beyond "IAM artifact over-grants."

---

> **Downstream hunter note.** Start with the **static, no-touch** checks: **R1, S1, U1** (AWS-authored artifact over-grant + SLR policy audit incl. the un-hardened `cloudwatch:*` on `"*"` vs the siblings' `alarm:TargetTracking*` + guarantee-vs-enforcement) — all confirmable with `iam:SimulatePrincipalPolicy` / `GetPolicyVersion` before any live call. The headline chain is **A1** (ownership is IAM-unscopable → a caller with only `application-autoscaling:*` terminates a foreign-owned fleet via the two SLR hops) — run it with **two scoped roles in one authorized account + a canary fleet**, `Simulate` first. Then **B1** (does a caller-supplied `RoleARN` get honored for the `ec2` namespace), **L2** (publish to a custom metric with only `cloudwatch:PutMetricData` → steer capacity), and **L1** (managed-alarm `DisableAlarmActions` / weighting-rounding scale-in no-op). Resolve the §8 doc-gaps (compensating backend filter; metric namespace/dimension strings; RoleARN-for-ec2 behavior) before escalating severity. Tear down every fleet/alarm/scalable-target created. **Hard stop** on any AWS service-plane identity.
