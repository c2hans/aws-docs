# Spot Fleet Target Tracking Scaling — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/spot-fleet-target-tracking.html` (target page: "Target tracking scaling: Scale Spot Fleet by targeting a value for a specific metric") and its referenced siblings `spot-fleet-automatic-scaling.html` (Considerations), `spot-fleet-auto-scaling-IAM.html`; the Application Auto Scaling User Guide pages `application-auto-scaling-target-tracking.html`, `target-tracking-scaling-policy-overview.html` ("How target tracking works"), `monitoring-cloudwatch.html` (predefined metrics + metric table), `create-target-tracking-policy-cli.html` (worked CLI + alarm-name output), `security_iam_permission_validation.html`, `security_iam_service-with-iam.html`; the AAS API Reference `API_PutScalingPolicy.html`, `API_TargetTrackingScalingPolicyConfiguration.html`, `API_PredefinedMetricSpecification.html`, `API_CustomizedMetricSpecification.html`, `API_RegisterScalableTarget.html`; and the IAM Service Authorization References `list_ec2` and **`list_application-autoscaling`** (hyphenated slug — the non-hyphen form 404s; mirror path `/work/aws-docs/docs/service-authorization/latest/reference/list_application-autoscaling.md`). Online + offline mirror cross-checked. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope note / relationship to siblings — READ FIRST.** This is the **target-tracking-policy-specific deep-dive companion** to `spot-fleet-automatic-scaling-attack-research-plan.md`. The automatic-scaling plan owns the *broad* second-control-plane surface (Application Auto Scaling + CloudWatch driving `ec2:ModifySpotFleetRequest`) and already fully owns these leads — **this plan does NOT restate them, it cross-references:**
> - **AWS-authored IAM-artifact audit** (the `spot-fleet-auto-scaling-IAM.html` operator sample policy with `application-autoscaling:*` + `cloudwatch:PutMetricAlarm/DeleteAlarms/Disable/EnableAlarmActions` + `iam:CreateServiceLinkedRole` + `sns:*` **all on `Resource:"*"`**, and the SLR policy `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` left un-hardened vs its scoped `alarm:TargetTracking*` siblings) → **auto-scaling plan Areas R1 / S1**.
> - **Confused-deputy via caller-suppliable `RoleARN`** → **auto-scaling plan Area B1**.
> - **Register a foreign-owned `sfr-` and scale it (ownership is IAM-unscopable; no `resource-id` condition key)** → **auto-scaling plan Area A1**.
> - **min/max guarantee enforced only by AAS orchestration, bypassable via direct `ec2:ModifySpotFleetRequest`** → **auto-scaling plan Area U1**.
> - **Legacy managed policy `AmazonEC2SpotFleetAutoscaleRole`** → **auto-scaling plan Area X1**; **revocation completeness on deregister** → **Area AA1**; **`cloudwatch:PutMetricData`-only metric steering (generic)** → **Area L2**.
>
> **What THIS plan uniquely owns** — the mechanisms that exist *only* for the target-tracking policy type (step/scheduled scaling do not have them) and that the sibling only touches shallowly:
> 1. **Multi-policy MAX-capacity-wins arbitration** with the **"scale-out if ANY ready / scale-in only if ALL ready"** asymmetry — a *per-added-policy* capacity-override and scale-in-lockout primitive the sibling does not model at all (TT1).
> 2. **The auto-created `AlarmHigh`/`AlarmLow` managed-alarm pair** — predictable name grammar, selective High-vs-Low deletion asymmetry, `INSUFFICIENT_DATA` scaling-freeze, and alarm pre-creation/collision (TT2 — far deeper than the sibling's generic "edit the managed alarm").
> 3. **`CustomizedMetricSpecification` as the metric-*selection* point of the policy itself**, the **scale-in-to-0** path, and the **`DisableScaleIn` capacity-pin** (TT3 — deeper than the sibling's generic custom-metric note).
> 4. **The documented scale-out-aggressive / scale-in-conservative asymmetry** and the near-**unbounded `TargetValue` range** as cost-amplification primitives (TT4).
> 5. The **`request` vs `maintain` prerequisite** and the **ALB `ResourceLabel`** caller-supplied input (TT5).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This is a **single-account / delegation-centric** surface (per the fleet-services memory). The highest-value leads here are **intra-account cross-team / cross-workload capacity & cost manipulation and monitoring-integrity breaks** driven through AWS-managed delegation (the AAS SLR) — **not** cross-tenant IDOR (`sfr-<UUID>` is 128-bit, scalable targets/alarms are account-scoped; see §8).
- Trust the **IAM Service Authorization Reference (`list_ec2`, `list_application-autoscaling`)** over User-Guide prose when they disagree.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the AAS SLR acting outside the account, or an alarm/metric owned by AWS's fleet), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives
1. Show that a principal who can call `PutScalingPolicy` for a fleet (its own, or — chaining to auto-scaling Area A1 — a foreign-owned one) can **add a second target-tracking policy** whose metric/target forces the fleet to a capacity the owner never intended, and that the owner's own scale-in policy is **structurally unable to bring it back down** because of the "any-out / all-in" + "largest-capacity-wins" arbitration (TT1).
2. Show that the **AWS-managed `AlarmHigh`/`AlarmLow` alarm pair** can be selectively tampered with (delete/disable one side) to produce an **asymmetric, silent** failure — scale-in disabled → runaway cost; scale-out disabled → availability loss — while `describe-scaling-policies` still reports the policy healthy (TT2).
3. Show that the policy's **`CustomizedMetricSpecification`** lets a caller point the fleet's capacity at an **arbitrary, self-controlled CloudWatch metric**, and that a `0`-emitting metric with `MinCapacity=0` can be used to **terminate the entire fleet** via the two SLR hops (TT3).
4. Show that the documented **scale-out-aggressive/scale-in-conservative** asymmetry plus the near-unbounded **`TargetValue`** can be weaponized into **monotonic cost growth** that the conservative scale-in logic will not reverse (TT4).
5. Determine whether the **`maintain`-type prerequisite** and the **ALB `ResourceLabel`** are validated at policy-creation time or fail open (TT5).
6. Confirm whether target-tracking-initiated capacity changes are **attributable in CloudTrail** to the human who authored the policy, or only to the AAS SLR (shared with auto-scaling Area L1/O — cross-ref).

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** Target tracking is one of three Spot Fleet automatic-scaling policy types, and the **only one in which AWS auto-creates and manages the CloudWatch alarms**. "With target tracking scaling, you create a target tracking scaling policy by selecting a metric and setting a target value. Spot Fleet then creates and manages the CloudWatch alarms that trigger the scaling policy" (`spot-fleet-target-tracking.html`); the authoritative AAS page attributes the same to Application Auto Scaling: "Application Auto Scaling creates and manages the CloudWatch alarms that trigger scaling events" (`application-auto-scaling-target-tracking.html`). (The attribution discrepancy is resolved in favor of AAS by the SLR policy — see §8; cross-ref auto-scaling Area S1.)

- **Customer-facing interface:** SigV4 IAM. Create via console ("Spot Requests → Auto Scaling tab → Configure") or CLI: `application-autoscaling register-scalable-target` then `application-autoscaling put-scaling-policy --policy-type TargetTrackingScaling --target-tracking-scaling-policy-configuration <json>`.
- **The scalable resource / addressing:** a Spot Fleet request, `sfr-<UUID>`, addressed as the AAS 3-tuple `ServiceNamespace=ec2`, `ResourceId=spot-fleet-request/sfr-xxxx`, `ScalableDimension=ec2:spot-fleet-request:TargetCapacity` — **all caller-supplied strings** (central to TT1/TT3 and auto-scaling Area A1).
- **The policy object (`TargetTrackingScalingPolicyConfiguration`)** — the new attack surface this page introduces, fields (verbatim from `API_TargetTrackingScalingPolicyConfiguration.md`):
  - `TargetValue` (Double, **Required**) — "Values must be in the range of -2^360 to 2^360." (TT4)
  - `PredefinedMetricSpecification` **or** `CustomizedMetricSpecification` (choose one).
    - Predefined (Spot Fleet): `EC2SpotFleetRequestAverageCPUUtilization`, `EC2SpotFleetRequestAverageNetworkIn`, `EC2SpotFleetRequestAverageNetworkOut`, `ALBRequestCountPerTarget` (CloudWatch namespace `AWS/EC2Spot`, dimension `FleetRequestId`; ALB → `AWS/ApplicationELB`).
    - Customized: `MetricName`, `Namespace`, `Dimensions[]`, `Statistic`, `Unit` — **all unconstrained free strings, no whitelist** (TT3).
  - `DisableScaleIn` (Boolean, default `false`) (TT3).
  - `ScaleInCooldown` / `ScaleOutCooldown` (Integer seconds; Spot Fleet default 300) (TT4).
  - `ResourceLabel` (on `ALBRequestCountPerTarget` only): `app/<lb-name>/<lb-id>/targetgroup/<tg-name>/<tg-id>` — caller-supplied (TT5).
- **The managed alarm pair:** `AlarmHigh` (scale-out) + `AlarmLow` (scale-in). Confirmed name grammar from the Spot Fleet CLI worked example: `TargetTracking-spot-fleet-request/sfr-73fbd2ce-...EXAMPLE-AlarmHigh-<uuid>` and `...-AlarmLow-<uuid>` — **the entire name except the trailing per-alarm UUID is derived from the resource-id string the caller already knows** (TT2).
- **Processes / identities:**
  - *Application Auto Scaling control loop* — reads the alarm state, computes the adjustment, calls `ec2:ModifySpotFleetRequest` under the SLR `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest` (service principal `ec2.application-autoscaling.amazonaws.com`). SLR policy = 5 actions all `Resource:"*"` (auto-scaling Area S1).
  - *EC2 Spot Fleet* — scale-out launches via the Spot Fleet SLR (identity-policy `RunInstances` conditions do NOT propagate — `create-spot-fleet` plan); scale-in terminates ("the instance receives a Spot Instance interruption notice").
- **Untrusted-data entry points unique to this page:** the **metric selection** (`CustomizedMetricSpecification`), the **target value**, the **`DisableScaleIn` flag**, the **ALB `ResourceLabel`**, and — because policies compose — the **number and content of additional target-tracking policies** (TT1).
- **KMS / secrets:** none generated by this surface (null — §8).

```
      ┌───────────────────────── customer AWS account ─────────────────────────┐
 author (holds application-autoscaling:PutScalingPolicy [+ RegisterScalableTarget])
      │   put-scaling-policy --policy-type TargetTrackingScaling                 │
      │     TargetTrackingScalingPolicyConfiguration{                            │
      │       TargetValue, (Predefined|Customized)MetricSpec,                    │
      │       DisableScaleIn, ScaleIn/OutCooldown }                              │
      └──────────────────────────────┬───────────────────────────────────────────┘
                                     │ AAS AUTO-CREATES two alarms:
                                     ▼
   CloudWatch  ◄── AlarmHigh (scale-out)  "TargetTracking-<ResourceId>-AlarmHigh-<uuid>"
   (metric      ── AlarmLow  (scale-in)   "TargetTracking-<ResourceId>-AlarmLow-<uuid>"
    value only,          │                      ▲ predictable prefix; only <uuid> is random
    not publisher) ──────┤                      │ caller holds cloudwatch:* on "*" (sample policy)
                         ▼
      Application Auto Scaling control loop  (SLR, Resource:"*")
         • scale-out if ANY policy ready;  scale-in only if ALL policies ready
         • when multiple policies fire: pick the one giving the LARGEST capacity
                         │ ec2:ModifySpotFleetRequest (set TargetCapacity)  ◄─ Resource:"*", no Condition
                         ▼
                   EC2 Spot Fleet  ──► scale-out: RunInstances (launch primitive)
                                    └─► scale-in : terminate Spot Instances (terminate primitive)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Policy author (can `PutScalingPolicy`) | The fleet owner's *intended capacity envelope* | Add a 2nd target-tracking policy (different metric); "largest-capacity-wins" + "any-out/all-in" | Fleet pinned at a capacity the owner's own policy cannot reduce → **intra-account control override / scale-in lockout** |
| Holder of the operator sample policy (`cloudwatch:*` on `"*"`) | The AWS-managed `AlarmHigh`/`AlarmLow` pair | `DeleteAlarms`/`PutMetricAlarm`/`DisableAlarmActions` on the predictable `TargetTracking-<sfr>-Alarm*` name | One side of the pair silently removed/disabled while the policy still reports healthy → **asymmetric monitoring-integrity break** |
| Any workload with `cloudwatch:PutMetricData` | A fleet's capacity decision | A TT policy's `CustomizedMetricSpecification` watches a self-published metric value | Fleet scales (or scales to 0 → terminates) on a value the fleet owner does not control |
| AAS control loop (SLR) | EC2 Spot Fleet capacity | SLR `ec2:ModifySpotFleetRequest` on `Resource:"*"`, no Condition | Capacity change on a fleet outside the scalable target the author legitimately registered (chains to auto-scaling A1/S1) |
| Target-tracking orchestration (soft) | EC2 fleet target capacity (hard) | scale-out "as fast as it can" / scale-in only >10% below target | Monotonic cost growth the conservative scale-in logic will not reverse |
| Any customer surface | **AWS's own service plane** | — | **HARD STOP** — any AWS-fleet identity/ARN/account = disclosure, preserve evidence |

---

## 4. API / Interface Inventory

| Name | Service | Mutating | Facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `RegisterScalableTarget` | application-autoscaling | ✔ | External | Register `sfr-xxxx`; set min/max; optional `RoleARN` | `application-autoscaling:*` (sample) | Deferred/absent EC2-ownership check → auto-scaling A1. `RoleARN` → auto-scaling B1 |
| `PutScalingPolicy` (`--policy-type TargetTrackingScaling`) | application-autoscaling | ✔ | External | Create/modify a TT policy; **auto-creates the AlarmHigh/AlarmLow pair** | same | **The core API of this page.** Multi-policy arbitration = TT1; metric spec = TT3 |
| `DeleteScalingPolicy` | application-autoscaling | ✔ | External | Delete a TT policy; deletes its managed alarms | same | Orphan check → cross-ref auto-scaling AA1 |
| `DescribeScalingPolicies` | application-autoscaling | ✘ | External | Read policies | same | **No resource type, no condition keys** (list_application-autoscaling) → fully account-wide read; a tamper-detection source if un-blocked |
| `cloudwatch:PutMetricAlarm` / `DeleteAlarms` / `Disable/EnableAlarmActions` | cloudwatch | ✔ | External | Touch any alarm incl. the managed pair | caller + SLR | Sample policy grants on `"*"` → TT2 |
| `cloudwatch:PutMetricData` | cloudwatch | ✔ | External | Publish the metric a TT policy watches | any holder | TT3 (metric-value steering; generic form in auto-scaling L2) |
| `ec2:ModifySpotFleetRequest` | ec2 | ✔ | External | Set `TargetCapacity` (launch/terminate primitive) | SLR + artifact holder | see `modify-spot-fleet-attack-research-plan.md` |

**Console-hidden / API-only knobs (relative to the console "Configure" flow on this page):** `DisableScaleIn` *is* surfaced in the console, but `CustomizedMetricSpecification` (arbitrary `Namespace`/`MetricName`/`Dimensions`), metric-math customized metrics, the `-2^360…2^360` `TargetValue` range, and multi-policy composition are all driven from the API/CLI and are the lead-rich delta.

---

## 5. Recommended Areas of Focus

### TT1 — Multi-policy "largest-capacity-wins" + "any-out / all-in" arbitration = capacity-override & scale-in-lockout primitive (business-logic / Lens L / A) — PRIORITY
**Background.** Target tracking is the only policy type with this composition rule. Verbatim: "You can have multiple target tracking scaling policies for a scalable target, provided that each of them uses a different metric … It will scale out the scalable target if **any** of the target tracking policies are ready for scale out, but will scale in only if **all** of the target tracking policies (with the scale-in portion enabled) are ready to scale in." and "If multiple scaling policies instruct the scalable target to scale out or in at the same time, Application Auto Scaling scales based on the policy that provides the **largest capacity** for both scale in and scale out." (`target-tracking-scaling-policy-overview.html` → Multiple scaling policies). The EC2 page states the same: "The fleet scales based on the policy that specifies the largest fleet capacity."

**Security Concern.** The composition rule is *additive and attacker-favorable for growth*: a principal who can `PutScalingPolicy` against a fleet (the fleet's own owner-delegate, a different team sharing the account, or — chained via auto-scaling Area A1, where ownership is IAM-unscopable — a **foreign-owned** `sfr-`) can **add one more** target-tracking policy on any **unused metric** (e.g. `EC2SpotFleetRequestAverageNetworkIn` if the owner only used CPU). Because scale-out fires if *any* policy is ready and the *largest-capacity* policy wins, the attacker's aggressive policy dictates the floor; because scale-in requires *all* policies ready, the **owner's own scale-in can never complete** while the attacker's metric stays above its target. The "different metric" uniqueness constraint does not protect the owner — it simply forces the attacker onto a *second* metric, which they then drive (TT3). Net primitive: **persistent capacity inflation the legitimate owner cannot reverse by policy**, only by discovering and deleting the rogue policy.

**High-level Test Scenarios.**
- **Claim:** adding a second TT policy with a high effective target overrides a conservative owner policy and locks out the owner's scale-in. **Mechanism:** "any-out / all-in" + "largest-capacity-wins". **Oracle:** on an authorized canary fleet, create owner policy P1 (CPU, target 50, scale-in enabled); add attacker policy P2 (NetworkIn, target set so its computed capacity is high); drive P2's metric up; observe capacity rises to P2's figure and P1-driven scale-in produces **no** `FulfilledCapacity` decrease while P2 stays hot (`describe-scaling-activities`). **Preconditions:** `application-autoscaling:PutScalingPolicy` on the target (own, same-account other team, or foreign via A1). **Cost:** low. **Severity:** Medium–High intra-account (cost inflation + owner cannot self-remediate via policy); escalates when combined with A1 (foreign fleet) to **High**.
- **Claim:** the "different metric required" rule is enforced only by AAS and does not stop a second author. **Oracle:** attempt a 2nd policy on a distinct metric → accepted; attempt on the same metric → rejected (confirm the rule is a uniqueness constraint on metric, not on author/ownership). **Severity:** feeds the above.
- **Claim (chain):** combined with `DisableScaleIn` on the rogue policy (TT3) the owner's scale-in is doubly defeated — the rogue policy never contributes a scale-in "ready" vote at all. **Severity:** Medium–High.

**Doc evidence:** `target-tracking-scaling-policy-overview.html` (Multiple scaling policies); `spot-fleet-target-tracking.html` ("largest fleet capacity"). **Severity-if-true:** Medium–High (intra-account availability/cost; owner self-remediation blocked).

### TT2 — The auto-managed AlarmHigh/AlarmLow pair: predictable names, selective-side tamper asymmetry, INSUFFICIENT_DATA freeze, pre-creation/collision (Lens L / O / U / EE / AA) — PRIORITY
**Background.** Target tracking is the only policy type where AWS owns the alarms. "Spot Fleet then creates and manages the CloudWatch alarms" / "Application Auto Scaling creates and manages the CloudWatch alarms … and deletes them when no longer needed." The UG warns: "**Do not edit or delete the CloudWatch alarms that Spot Fleet manages**" and "Do not create, edit, or delete the CloudWatch alarms that are used with a target tracking scaling policy." Confirmed name grammar (from the Spot Fleet CLI worked example): `TargetTracking-spot-fleet-request/sfr-...EXAMPLE-AlarmHigh-<uuid>` and `...-AlarmLow-<uuid>` — **the whole name except the trailing per-alarm UUID is derived from the resource-id string the author already supplies.**

**Security Concern.** The "do not edit/delete" guarantee is **advisory prose, not an IAM control** — the operator sample policy on `spot-fleet-auto-scaling-IAM.html` grants `cloudwatch:DeleteAlarms`, `cloudwatch:PutMetricAlarm`, `cloudwatch:DisableAlarmActions`, `cloudwatch:EnableAlarmActions` on **`Resource:"*"`**, and the SLR policy itself leaves `PutMetricAlarm`/`DeleteAlarms` on `"*"` (un-hardened vs the `alarm:TargetTracking*`-scoped siblings — auto-scaling Area S1). So any holder can touch the managed pair. Three distinct, target-tracking-only breach shapes the sibling's generic "edit the alarm" lead does not model:
1. **Selective-side asymmetry.** The pair is two alarms with opposite effects. Deleting/`DisableAlarmActions` **only `AlarmLow`** removes the scale-in trigger → the fleet can grow but **never shrink** (runaway cost), while `describe-scaling-policies` still reports the policy present and enabled (no `DisableScaleIn` flag was set, so the console shows a healthy, scale-in-capable policy — a false signal). Disabling **only `AlarmHigh`** removes scale-out → availability loss under load with the same false "healthy" signal.
2. **Predictable-prefix targeting.** An attacker who knows the fleet's `sfr-` id (intra-account, or any party with `cloudwatch:DescribeAlarms`) can locate the pair by `--alarm-name-prefix "TargetTracking-spot-fleet-request/sfr-xxxx"` without knowing the UUID, then tamper — no enumeration of the random UUID is needed.
3. **INSUFFICIENT_DATA freeze (availability + stealth).** "If the metric is missing data points, this causes the CloudWatch alarm state to change to `INSUFFICIENT_DATA`. When this happens, Application Auto Scaling cannot scale your scalable target until new data points are found." For a `CustomizedMetricSpecification` the attacker (or an outage of the metric source) controls, simply **stopping the metric publish** freezes scaling at the current capacity — a no-tamper-on-the-alarm way to pin capacity (combines with TT1/TT3/TT4 to lock in an inflated capacity).

Also note (EE/AA): the name is deterministic from the resource id — worth testing whether an attacker **pre-creating** an alarm with the exact `TargetTracking-<ResourceId>-AlarmHigh-<...>` name causes AAS to collide/adopt/skip-create (the UUID suffix likely defeats a pure name collision, so rate this a lower-confidence probe), and whether `DeleteScalingPolicy` reliably **deletes both** alarms or can orphan one (cross-ref auto-scaling AA1).

**High-level Test Scenarios.**
- **Claim:** `DisableAlarmActions`/`DeleteAlarms` on **only `AlarmLow`** yields unbounded scale-out while the policy reports healthy. **Oracle:** on a canary fleet, locate the pair by prefix, disable `AlarmLow`, drive the metric to force scale-out, let it drop; confirm `FulfilledCapacity` never decreases and `describe-scaling-policies` still shows the policy scale-in-enabled. **Severity:** Medium–High (cost + false monitoring signal).
- **Claim:** stopping the custom metric publish freezes scaling (INSUFFICIENT_DATA) at the current (possibly inflated) capacity. **Oracle:** stop publishing; observe alarm → INSUFFICIENT_DATA and no further scaling activities. **Severity:** Medium.
- **Claim (O):** the "do not edit the alarms" property has no enforcement mechanism (pure prose). **Oracle:** diff the sample/SLR policy's `cloudwatch:*` resource (`"*"`) against the warning — no `Deny`, no scoped resource protects the managed alarm. **Severity:** Informational→enabler (raises TT1/TT4 effective severity).
- **Claim (EE/AA, lower-confidence):** pre-created same-prefix alarm collides, or `DeleteScalingPolicy` orphans one alarm. **Oracle:** pre-create; and after policy delete enumerate residual `TargetTracking-*` alarms. **Severity:** Low–Medium.

**Doc evidence:** `spot-fleet-target-tracking.html` (managed-alarm note); `target-tracking-scaling-policy-overview.html` (Considerations: do-not-edit + INSUFFICIENT_DATA); `create-target-tracking-policy-cli.html` (AlarmHigh/AlarmLow name output); `spot-fleet-auto-scaling-IAM.html` (`cloudwatch:*` on `"*"`); auto-scaling Area S1. **Severity-if-true:** Medium–High.

### TT3 — `CustomizedMetricSpecification` as the metric-selection point: arbitrary metric, scale-in-to-0 terminate, DisableScaleIn capacity-pin (Lens K / U / A) — PRIORITY
**Background.** A TT policy watches whatever metric its spec names. Predefined is a fixed enum, but `CustomizedMetricSpecification` fields `MetricName`, `Namespace`, `Dimensions[]`, `Statistic`, `Unit` are **unconstrained free strings — no whitelist, no binding to the fleet** (confirmed from `API_CustomizedMetricSpecification.md`; the docs only *recommend* "a metric that changes inversely proportional to capacity"). Supporting facts: "use your own custom metrics published to CloudWatch"; `DisableScaleIn` default `false`; and the ALB-specific scale-in-to-0: "When a metric emits real 0 values to CloudWatch … Application Auto Scaling can scale in to 0 … the scalable target's minimum capacity must be set to 0."

**Security Concern.** Three distinct uses of the metric-selection point, all target-tracking-specific:
1. **Capacity steered by whoever controls the metric.** Because the alarm reacts to metric *values*, not the publishing *principal*, a TT policy pointed at a custom metric lets any holder of `cloudwatch:PutMetricData` for that `Namespace`/`MetricName`/`Dimensions` drive the fleet's capacity — no `ec2:*`, no `application-autoscaling:*`, no SLR relationship. (Generic form is auto-scaling Area L2; the *target-tracking-specific* amplifier is that the attacker can also be the one who **chose** the metric when they created the rogue TT1 policy — they pick a metric they already control.)
2. **Scale-in-to-0 = whole-fleet terminate via metric.** With `MinCapacity=0` (or a scheduled min of 0) and a custom metric emitting sustained `0`, target tracking scales the fleet to **0** → every Spot Instance terminated, through the AAS SLR → EC2 SLR hops, reachable by a caller who holds **no** `ec2:TerminateInstances` and no `ec2:ModifySpotFleetRequest`. This is a metric-driven variant of the terminate primitive in `modify-spot-fleet-attack-research-plan.md`.
3. **`DisableScaleIn` capacity-pin.** A policy created with `DisableScaleIn=true` only ever scales out; it never contributes a scale-in. Set on a (rogue, TT1) policy for a fleet, it pins capacity at the high-water mark and — via the "all-in" rule — poisons the whole fleet's ability to scale in regardless of the owner's other policies.

**High-level Test Scenarios.**
- **Claim:** a role with only `cloudwatch:PutMetricData` for the custom metric a TT policy watches can force fleet scale-out (and, with min=0 and a 0-metric, scale the fleet to 0 → terminate all instances). **Oracle:** create a TT policy on `Namespace=MyNamespace/MetricName=MyUtilizationMetric`; from a separate role holding *only* `PutMetricData`, publish values to drive scale-out, then publish sustained `0` with min=0 and observe termination. `SimulatePrincipalPolicy` to confirm the publishing role lacks EC2/AAS rights first. **Severity:** Medium–High intra-account (capacity/cost steering with no EC2/AAS rights); **High** when it reaches full-fleet termination.
- **Claim:** `CustomizedMetricSpecification` accepts a metric in any namespace with no ownership tie. **Oracle:** create a policy citing an arbitrary namespace/metric → accepted. **Severity:** confirms (1)/(2).
- **Claim:** `DisableScaleIn=true` pins capacity and (via all-in) blocks fleet-wide scale-in. **Oracle:** policy with `DisableScaleIn=true`; drive up; confirm no scale-in ever occurs. **Severity:** Medium–High.
- **Cross-account caveat:** no documented cross-account custom-metric path except CloudWatch cross-account observability (OAM) — **un-examined doc-gap**, treat as open follow-up, not a confirmed null (see §8; same caveat as auto-scaling L2).

**Doc evidence:** `API_CustomizedMetricSpecification.md` (free-string fields); `application-auto-scaling-target-tracking.html` ("your own custom metrics"); `target-tracking-scaling-policy-overview.html` (scale-in-to-0, DisableScaleIn, Multiple policies all-in rule); `API_TargetTrackingScalingPolicyConfiguration.md` (`DisableScaleIn` default false). **Severity-if-true:** Medium–High (High at full-fleet terminate).

### TT4 — Scale-out-aggressive / scale-in-conservative asymmetry + near-unbounded TargetValue (Lens L / U)
**Background.** Verbatim: "a target tracking scaling policy is more aggressive in adding capacity … than it is in removing capacity … it responds by adding capacity proportional to the metric value **as fast as it can**. The higher the metric, the more capacity is added." And on scale-in: "the policy won't scale-in if it calculates that removing a minimum unit of capacity would likely bring the metric back above the target value … removing capacity only when utilization passes a threshold that is far enough below the target value (usually **more than 10% lower**)." `TargetValue` range is `-2^360 to 2^360`.

**Security Concern.** The asymmetry is a built-in cost amplifier: an attacker (or an attacker-chosen metric) that holds the metric just above target produces fast, proportional scale-out, while the conservative scale-in refuses to act until utilization falls >10% below target — so a sawtooth that repeatedly touches "above target" grows the fleet and rarely shrinks it. The near-unbounded `TargetValue` compounds this: a pathological target (very small, so any real metric is "far above"; or a nonsensical/negative value) can make the proportional "add as fast as it can" logic request extreme capacity. The documented worked examples ("add two instances" rounding up; "choose not to scale-in until the metric lowers enough") confirm scale-in is deliberately sticky. Note the fleet owner cannot tune this away — the aggressiveness is AWS orchestration, not a customer knob.

**High-level Test Scenarios.**
- **Claim:** a sustained just-above-target metric drives monotonic growth that scale-in will not reverse within the >10% band. **Oracle:** hold the (custom) metric ~5% above target; observe repeated scale-out and no scale-in; cost grows. **Severity:** Medium (cost; availability is protected by design, cost is not).
- **Claim:** a pathological `TargetValue` (e.g. extremely small, or outside sane range but within `±2^360`) yields extreme capacity requests bounded only by `MaxCapacity`/account limits. **Oracle:** create a policy with a tiny target; observe the computed adjustment. Confirm whether any server-side sanity bound exists below `2^360`. **Severity:** Medium (bounded by MaxCapacity — unless MaxCapacity itself was set high, chaining to auto-scaling U1).
**Doc evidence:** `target-tracking-scaling-policy-overview.html` (How it works — aggressiveness + >10% scale-in band + rounding examples); `spot-fleet-target-tracking.html` ("scales out … as fast as it can, but scales in more gradually"); `API_TargetTrackingScalingPolicyConfiguration.md` (`TargetValue` range). **Severity-if-true:** Medium (cost).

### TT5 — `maintain`-type prerequisite + ALB `ResourceLabel` caller input (Lens P / U / A)
**Background.** Prerequisites on `spot-fleet-target-tracking.html`: "The Spot Fleet request must have a request type of `maintain`. Automatic scaling is not supported for requests of type `request`." And `ALBRequestCountPerTarget` requires a caller-supplied `ResourceLabel` of the form `app/<lb-name>/<lb-id>/targetgroup/<tg-name>/<tg-id>` ("You can't specify a resource label unless the metric type is `ALBRequestCountPerTarget` and there is a target group attached to the Spot Fleet").
**Security Concern.** (a) Is the `maintain`-type precondition enforced at `RegisterScalableTarget`/`PutScalingPolicy` time, or does registration succeed and silently no-op (consistent with "If the specified resource is not active … this operation does not change the resource's current capacity" — auto-scaling A1)? A fail-open here means a scaling policy can be attached to a `request`-type fleet and sit dormant (confusing posture; low direct impact). (b) The `ResourceLabel` is a caller-supplied ARN-like string naming an ALB target group — is it validated to belong to the caller's fleet/account, or merely parsed? If a policy can cite a target group it does not own, the fleet's capacity is driven by another resource's request count (an input-trust question analogous to TT3's metric selection).
**High-level Test Scenarios.**
- **Claim:** a TT policy is accepted against a `request`-type (non-maintain) fleet and silently never scales. **Oracle:** register a `request`-type fleet, put a TT policy, observe accept + no scaling. **Severity:** Low (posture confusion / doc-vs-enforcement).
- **Claim:** `ResourceLabel` accepts a target group not attached to the caller's fleet (or in another account). **Oracle:** create an `ALBRequestCountPerTarget` policy with a foreign/arbitrary `ResourceLabel`; observe whether it is validated. **Severity:** Low–Medium (metric-source confusion; cross-account only if the label resolves cross-account — likely rejected).
**Doc evidence:** `spot-fleet-target-tracking.html` (Prerequisites — maintain-only); `API_PredefinedMetricSpecification.md` (`ResourceLabel` format + constraint); `API_RegisterScalableTarget.md` (deferred-activation sentence). **Severity-if-true:** Low–Medium.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Override owner capacity + lock out scale-in by adding a 2nd TT policy | multi-policy "largest-wins / any-out / all-in" | "provided that each uses a different metric" (uniqueness is the only stated bound) |
| Silent asymmetric monitoring break (delete/disable one alarm of the pair) | managed `AlarmHigh`/`AlarmLow`, `cloudwatch:*` on `"*"` | "Do not create, edit, or delete the CloudWatch alarms …" (advisory only) |
| Freeze scaling at inflated capacity via INSUFFICIENT_DATA | custom metric publish + managed alarm | "Application Auto Scaling cannot scale … until new data points are found" |
| Steer / terminate a fleet via a self-controlled custom metric | `CustomizedMetricSpecification` free-string + scale-in-to-0 | "Choose a metric that changes inversely proportional to … capacity" (recommendation, not enforcement) |
| Pin capacity high via `DisableScaleIn` | policy flag + all-in rule | `DisableScaleIn` default false (opt-in) |
| Monotonic cost growth via scale-out/scale-in asymmetry | AAS orchestration | ">10% below target" conservative scale-in (protects availability, not cost) |
| Policy attached to a `request`-type fleet / foreign ALB `ResourceLabel` | prerequisite + ResourceLabel validation | "request type must be `maintain`"; label-must-be-attached rule |
| Capacity change not attributable to policy author | CloudTrail + SLR | — (cross-ref auto-scaling L1/O) |

---

## 7. Out-of-Scope Risk Categories
- **AWS-authored IAM-artifact over-grant** (sample policy + SLR policy on `"*"`, un-hardened `cloudwatch:*`, over-broad `iam:CreateServiceLinkedRole`/`sns:*`) — **owned by `spot-fleet-automatic-scaling-attack-research-plan.md` Areas R1/S1**; this plan only *uses* those grants as the precondition for TT1/TT2/TT3, it does not re-audit them.
- **Confused-deputy via caller-suppliable `RoleARN`** — auto-scaling **B1**.
- **Register-a-foreign-fleet / ownership-is-IAM-unscopable (no `resource-id` condition key)** — auto-scaling **A1** (TT1/TT3 *chain* onto it for a cross-team target but do not restate the authz analysis).
- **min/max guarantee bypass via direct `ec2:ModifySpotFleetRequest`** — auto-scaling **U1**.
- **Legacy managed policy parity** — auto-scaling **X1**; **generic `PutMetricData` steering** — auto-scaling **L2**; **deregister/revocation completeness** — auto-scaling **AA1**.
- **`ec2:ModifySpotFleetRequest` internals** (`LaunchTemplateConfig.N`, `ExcessCapacityTerminationPolicy`, case-sensitivity) — `modify-spot-fleet-attack-research-plan.md`.
- **Cross-account / cross-tenant IDOR on `sfr-<UUID>`** — 128-bit, not fabricable (genuine null); scalable targets, policies, and the managed alarm pair are all account-scoped.
- **Spot Fleet SLR launch guardrail-bypass** (identity-policy `RunInstances` conditions not propagating) — `create-spot-fleet-attack-research-plan.md`; here only the downstream effect of a scale-out.
- **CloudWatch's own multi-tenant metric/alarm isolation**, Application Auto Scaling control-plane internals — AWS-shared infra / shared-responsibility line.
- **Single-tenant self-DoS** from an owner's own flapping/misconfigured policy where no privilege or ownership boundary is crossed; **step scaling / scheduled scaling** policy types (different pages/plans).
- **A customer who authors their own over-broad scaling IAM policy** — least-privilege footgun (in scope only when the artifact is AWS-authored/uneditable/copy-verbatim — see auto-scaling R1).

---

## 8. Null hypotheses / doc gaps
- **Lens A (cross-account / cross-tenant):** null for this surface — the TT policy, the scalable target (`scalable-target/${ResourceId}` ARN lives in the *caller's* account), and the `AlarmHigh`/`AlarmLow` pair are all account-scoped; `sfr-<UUID>` is 128-bit. Pages checked: `spot-fleet-target-tracking.html`, `target-tracking-scaling-policy-overview.html`, `API_RegisterScalableTarget.html`, `list_application-autoscaling`. In-scope realization is intra-account cross-team/cross-workload (TT1/TT3), reached via auto-scaling A1.
- **Lens H (KMS / encryption context):** null — TT policy, metric spec, and alarms generate/store no key, secret, or encryption context. Pages checked: all four TT pages + `API_PutScalingPolicy.md`.
- **Lens G (SSRF):** null — no field the TT control plane dereferences/fetches server-side. `CustomizedMetricSpecification.Namespace/MetricName/Dimensions` and `ResourceLabel` are matched against CloudWatch metadata, not fetched as URLs. Pages checked: `API_CustomizedMetricSpecification.md`, `API_PredefinedMetricSpecification.md`, `target-tracking-scaling-policy-overview.html`.
- **Lens Q (upload) / F (translation injection):** null — no file upload, no query/wire-protocol translation. (Lens K fires only in the limited intra-account "metric-value steering" form — TT3 — not classic LLM prompt injection.)
- **Lens V/D (network segmentation / data→control):** null for the scaling control loop (control-plane-to-control-plane API traffic, no customer-reachable ENI). The data-plane angle lives on the launched instances (out of scope here).
- **Lens EE (predictable-name pre-registration):** **partial / low-confidence.** The managed alarm names are deterministic *except* for a per-alarm random UUID suffix, which likely defeats a pure name-collision pre-creation attack — rate the TT2 pre-creation probe low-confidence and confirm empirically whether AAS matches by exact name (defeated by UUID) or by name-prefix/tag (potentially collidable).
- **Cross-account custom-metric path (gates TT3 cross-account severity):** **doc-gap, not a confirmed null.** CloudWatch cross-account observability (OAM) interacting with a `CustomizedMetricSpecification` was not examined — it could in principle let a TT policy reference a consent-shared cross-account metric. Treat as an open follow-up before closing the cross-account question (same caveat as auto-scaling L2).
- **`maintain`-type precondition enforcement point (TT5):** **doc-gap** — the docs state the prerequisite but not whether it is enforced at register/put time or silently deferred. Confirm before relying on either reading.
- **Spot Fleet CloudWatch metric namespace/dimension strings:** confirmed this pass — namespace `AWS/EC2Spot`, dimension `FleetRequestId`, metric names `CPUUtilization`/`NetworkIn`/`NetworkOut` (predefined), plus `AWS/ApplicationELB` `RequestCountPerTarget`/`TargetGroup` for ALB (`monitoring-cloudwatch.html`). (This resolves the auto-scaling plan's §8 "metrics page unverified" gap for the target-tracking context.)
- **Doc-vs-doc attribution (Informational, file-worthy):** `spot-fleet-target-tracking.html` says "**Spot Fleet** then creates and manages the CloudWatch alarms"; the AAS pages say "**Application Auto Scaling** creates and manages the CloudWatch alarms." The SLR policy (`cloudwatch:PutMetricAlarm` held by `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`) resolves it in favor of Application Auto Scaling — the EC2 UG wording is imprecise. (Same finding noted in auto-scaling §8.)

---

> **Downstream hunter note.** This plan is the *target-tracking-specific* layer on top of `spot-fleet-automatic-scaling-attack-research-plan.md` — **read that plan's Areas R1/S1/A1/B1/U1 first** for the IAM-artifact and ownership groundwork; they are the preconditions this plan builds on and are deliberately not restated here. Start the live work with **TT2** (static: diff the sample/SLR `cloudwatch:*` resource vs the "do not edit the alarms" prose — confirmable with `GetPolicyVersion`/`SimulatePrincipalPolicy` before any touch; then the selective-side alarm tamper on a canary). The headline chains are **TT1** (add a 2nd TT policy → largest-wins override + all-in scale-in lockout) and **TT3** (unconstrained custom metric → steer/terminate via scale-in-to-0 with only `cloudwatch:PutMetricData`), both run against a **canary fleet with two scoped roles in one authorized account**, `Simulate` first. **TT4/TT5** are lower-severity cost/posture confirmations. Resolve the §8 doc-gaps (OAM cross-account metric path; `maintain` enforcement point; EE UUID-vs-prefix matching) before escalating severity. Tear down every fleet/alarm/scalable-target/metric created. **Hard stop** on any AWS service-plane identity.
