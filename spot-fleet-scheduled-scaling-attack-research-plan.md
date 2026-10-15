# Spot Fleet Scheduled Scaling — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/spot-fleet-scheduled-scaling.html` (the target page — "Scheduled scaling: Scale Spot Fleet on a schedule") plus the Application Auto Scaling (AAS) surfaces it drives: `API_PutScheduledAction.html`, `API_DescribeScheduledActions.html`, `API_DeleteScheduledAction.html`, `API_RegisterScalableTarget.html`; AAS User Guide `scheduled-scaling-policy-overview.html`, `scheduled-scaling-using-cron-expressions.html`; the EC2 prerequisite pages `spot-fleet-auto-scaling-IAM.html` and `spot-fleet-automatic-scaling.html#considerations`; and the IAM Service Authorization Reference **`list_application-autoscaling`** (hyphenated slug — the non-hyphen variant 404s; mirrored at `/work/aws-docs/docs/service-authorization/latest/reference/list_application-autoscaling.md`) and `list_ec2`. Online + offline mirror (`/work/aws-docs`) cross-checked; the offline `list_application-autoscaling.md` was confirmed byte-equivalent to the live fetch. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope note / relationship to siblings.** This is the **scheduled-scaling (time-deferred capacity-change) companion** to the Spot Fleet plan family. It is the *third* layer of the auto-scaling triad and is deliberately scoped to what exists **only** for scheduled actions — the `PutScheduledAction`/`DescribeScheduledActions`/`DeleteScheduledAction` surface and the *time dimension* it introduces. It does **not** restate the groundwork already owned by its siblings; it cross-references them:
> - **`spot-fleet-automatic-scaling-attack-research-plan.md`** owns the shared control-loop IAM groundwork — the AWS-authored IAM-artifact audit (**R1**), the AAS SLR policy audit `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` unconditioned on `"*"` (**S1**), the **ownership-is-IAM-unscopable** foreign-fleet register-and-terminate chain (**A1**), the caller-`RoleARN` confused-deputy (**B1**), the min/max-guarantee-vs-enforcement question (**U1**), managed-alarm/custom-metric tampering (**L1/L2**), and the legacy `AmazonEC2SpotFleetAutoscaleRole` parity (**X1**). Read it first — those are preconditions this plan builds on.
> - **`spot-fleet-target-tracking-attack-research-plan.md`** owns the `maintain`-type prerequisite enforcement-point question (**TT5**), the alarm-pair tamper and `CustomizedMetricSpecification` steer-to-0 (**TT2/TT3**).
> - **`modify-spot-fleet-attack-research-plan.md`** owns the EC2-side `ec2:ModifySpotFleetRequest` terminate/launch primitive (`ExcessCapacityTerminationPolicy=default`, `LaunchTemplateConfig.N`, `ec2:Attribute` case-sensitivity) and the `sfr-<UUID>` 128-bit cross-tenant-IDOR null.
> - **`spot-fleet-auto-scaling-IAM-attack-research-plan.md`** owns the printed sample identity policy (SNS/CloudWatch/IAM over-grants).
>
> **The new, under-reviewed primitive this plan owns:** capacity (and therefore instance *launch* and *termination*) can now be mutated **at an attacker-chosen future time, on a recurring schedule, under the SLR's identity** — temporally and attributionally decoupled from the principal who planted it. A1 proves a caller with only `application-autoscaling:*` can scale a foreign-owned fleet *now*; this plan proves the same primitive **persists, defers, recurs, and permanently rewrites the owner's bounds** — a time-bomb / persistence shape that no sibling models.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Like all Spot-Fleet plans these are **single-account / delegation-centric** surfaces: the highest-value leads are **intra-account cross-team privilege / blast-radius escalation** and **documented-guarantee-vs-enforcement** gaps — **not** classic cross-tenant IDOR (scalable targets, scheduled actions, and the SLR are per-account; `sfr-<UUID>` is 128-bit → cross-*tenant* fabrication is a genuine null, see §8).
- Trust the **IAM Service Authorization Reference** (`list_application-autoscaling`, `list_ec2`) over User-Guide prose when they disagree (the reusable doc-vs-reference contradiction established across the sibling plans).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives
1. Show that a principal who can `PutScheduledAction` on a Spot Fleet scalable target can **plant a deferred or recurring capacity change** (scale-in-to-0 = whole-fleet termination; scale-out-to-max = cost blow-up) that fires **later, under the AAS SLR identity**, decoupled in time and CloudTrail attribution from the planter.
2. Show that the scheduled-action namespace is **IAM-indistinguishable per action** — no `scheduled-action` resource type and no `resource-id` condition key exist — so a principal who can reach a scalable target can **create, overwrite (create-or-update by name, no version/etag), or delete *any* named scheduled action on it**, including an owner's.
3. Show that a scheduled action **permanently rewrites** the scalable target's `MinCapacity`/`MaxCapacity` — AAS does **not** revert after `EndTime` — so a single call leaves a persistent floor-pin or ceiling-collapse that outlives the schedule and the planter's access.
4. Determine whether `PutScheduledAction` is bound by any **synchronous ownership / `maintain`-type / min>max** check, or whether all validation is deferred to execution time (fail-permissive-at-create).
5. Show that `DescribeScheduledActions` is **completely unscopable** (no resource type, no condition keys) → an account-wide read oracle enumerating every fleet's future capacity plan, and that `SuspendedState=ScheduledScalingSuspended` is a scalable-target-level **kill switch** reachable via `RegisterScalableTarget`.
6. Confirm whether scheduled-action-initiated capacity changes are **attributable in CloudTrail** to the human who planted them or obscured behind the SLR and separated in time.

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** Scheduled scaling instructs Spot Fleet to "perform scaling activities at specific times" by creating *scheduled actions* on an Application Auto Scaling **scalable target**. The customer does not call EC2 directly for the capacity change; a scheduled action is a timer attached to the scalable target, and when it fires **Application Auto Scaling** (not the planter) calls `ec2:ModifySpotFleetRequest` under its SLR.

- **Customer-facing interface:** SigV4 IAM — `application-autoscaling:PutScheduledAction` / `DescribeScheduledActions` / `DeleteScheduledAction` (AWS CLI `put-scheduled-action` / `describe-scheduled-actions` / `delete-scheduled-action`), plus `RegisterScalableTarget` (prerequisite). EC2 console "Spot Requests → Scheduled Scaling" tab. No EC2 API is called by the customer for the schedule itself.
- **The scheduled action (the new asset):** addressed by **`ScheduledActionName`** (String 1–256, pattern forbids control chars / `:` `/` `|` / leading-trailing spaces) which is **unique only among scheduled actions on the specified scalable target** — scoped by the triple, not globally. Carries `Schedule` (`at(...)` | `rate(...)` | `cron(...)`, 1–1600 chars), `ScalableTargetAction` (`MinCapacity`/`MaxCapacity`, integers), `StartTime`/`EndTime` (UTC timestamps), `Timezone` (IANA/Joda name).
- **The scalable target (prerequisite):** triple **`ServiceNamespace=ec2`, `ResourceId=spot-fleet-request/sfr-<UUID>`, `ScalableDimension=ec2:spot-fleet-request:TargetCapacity`** — all caller-supplied strings. ARN `arn:${Partition}:application-autoscaling:${Region}:${Account}:scalable-target/${ResourceId}`. **"You cannot create a scheduled action until you have registered the resource as a scalable target."** (So the A1 register step is always a precondition here.)
- **Processes / identities:**
  - *AAS scheduler* — evaluates `at`/`rate`/`cron` + `Timezone`, and at trigger time "scales based on the new capacity values, by comparing current capacity to the specified minimum and maximum." The exact runtime identity that evaluates the schedule is not named (doc-gap; see §8).
  - *AAS control loop* — issues the actual `ec2:ModifySpotFleetRequest` under SLR **`AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`** (policy audited in sibling S1 — `ec2:ModifySpotFleetRequest` on `Resource:"*"`, no Condition).
  - *EC2 Spot Fleet* — executes: scale-out launches Spot Instances via the Spot Fleet SLR (identity-policy `RunInstances` conditions do NOT propagate — see `create-spot-fleet` plan); scale-in terminates them (the terminate primitive — see `modify-spot-fleet` plan).
- **Prerequisites (gates):** fleet must be type **`maintain`** ("Automatic scaling is not supported for requests of type `request`"); scheduled actions "can only be created for existing Spot Fleets."
- **KMS / secrets / uploads / URLs:** none on this surface (nulls — §8).

```
                 ┌───────────────────────── customer AWS account ──────────────────────────┐
   planter ──────┤ application-autoscaling: RegisterScalableTarget (sfr-xxxx)               │
 (holds AAS      │                          PutScheduledAction (name, cron/at, Min/Max,      │
  write actions) │                                            StartTime/EndTime/Timezone)   │
                 └──────────────┬────────────────────────────────────────────────────────────┘
                                │  timer persists on the scalable target
                                ▼
            ┌────────── AAS scheduler (fires at future/recurring time; runtime identity undocumented) ──────────┐
            │  compares current capacity to the action's Min/Max                                                  │
            └──────────────┬──────────────────────────────────────────────────────────────────────────────────────┘
                           │ ec2:ModifySpotFleetRequest  ◄── runs as SLR, Resource:"*", no Condition
                           ▼                                   (NOT as the planter; separated in time)
                     EC2 Spot Fleet  ──► Min=0/Max=0 : terminate whole fleet (no ec2:TerminateInstances held by anyone)
                                      └─► Max=huge   : scale-out / cost blow-up
                                   (bounds set by the action PERSIST after EndTime — never reverted)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Planter (holds AAS write actions) | A fleet they do **not** own, **at a future time** | `RegisterScalableTarget` + `PutScheduledAction` on a scalable target whose IAM scoping cannot name one fleet | A deferred/recurring capacity change executes against another team's fleet, firing under the SLR after the planter is gone → **intra-account time-delayed privilege escalation** |
| Planter | Another principal's scheduled action on the same scalable target | `PutScheduledAction` create-or-update by name (no version/etag); `DeleteScheduledAction` — both at `ScalableTarget` IAM granularity | Overwriting / deleting an owner's scheduled action, or planting one the owner did not author → **scheduled-action clobber (no per-action authz)** |
| Scheduled action (soft config) | The scalable target's standing Min/Max bounds | AAS "does not revert" after `EndTime` | Bounds left permanently rewritten after the schedule ends → **persistent floor-pin / ceiling-collapse outliving the schedule** |
| Low-priv reader | Every fleet's future capacity plan | `DescribeScheduledActions` (no resource type, no condition keys) | Enumerating all scheduled actions account-wide with no scoping → **config/recon info-disclosure** |
| Any caller with `RegisterScalableTarget` | Owner's scheduled-scaling availability | `SuspendedState=ScheduledScalingSuspended` | Owner's scheduled scale-in/out frozen while console still shows actions configured → **silent availability/cost pin** |
| AAS SLR | EC2 Spot Fleet capacity | SLR `ec2:ModifySpotFleetRequest` on `"*"` (sibling S1) | Any fleet modified at trigger time, attributed to the SLR not the planter → **attribution decoupling (Lens O)** |
| Any customer surface | **AWS's own service plane** | — | **HARD STOP** — any AWS-fleet identity/ARN/account = disclosure, preserve evidence |

---

## 4. API / Interface Inventory

| Name | Service | Mutating | Facing | Functionality | Resource type / scopability (per `list_application-autoscaling`) | Notes |
|---|---|---|---|---|---|---|
| `PutScheduledAction` | application-autoscaling | ✔ | External | **Create-or-update** a scheduled action (name, `at`/`rate`/`cron`, Min/Max, Start/End, Timezone) | `ScalableTarget*` **required**; cond keys = `scalable-dimension`, `service-namespace`, `aws:ResourceTag` **only — no `resource-id`, no `aws:RequestTag`/`TagKeys`** | SS1/SS2/SS3/SS4. Overwrite by name, no version check |
| `DeleteScheduledAction` | application-autoscaling | ✔ | External | Delete a scheduled action by name | `ScalableTarget*` required; same 3 cond keys | SS2 — delete any action on a reachable target |
| `DescribeScheduledActions` | application-autoscaling | ✘ | External | List scheduled actions in a namespace | **blank resource type, blank condition keys → fully unscopable** | SS5 — account/namespace-wide read oracle |
| `RegisterScalableTarget` | application-autoscaling | ✔ | External | Register `sfr-xxxx` as scalable target (prereq); set Min/Max; `SuspendedState` | `ScalableTarget*`; adds `aws:RequestTag`/`TagKeys` | A1 (sibling) + SS5 `ScheduledScalingSuspended` kill switch |
| `DeregisterScalableTarget` | application-autoscaling | ✔ | External | Remove target → **cascades: deletes all its scheduled actions** | `ScalableTarget*` | SS6 revocation-completeness |
| `ec2:ModifySpotFleetRequest` | ec2 | ✔ | Internal (via SLR) | The capacity change executed at trigger time | SLR policy `"*"`, no Condition (sibling S1) | **see `modify-spot-fleet` plan**; not called by the planter |

**Undocumented / console-hidden knobs (API accepts, console does not surface):**
- **`Timezone`** — console offers predefined recurrences + a "Custom" cron box; the full IANA/Joda timezone set (`Etc/GMT+9`, `Pacific/Tahiti`, …) and DST auto-adjust are API/CLI-only (SS4).
- **`StartTime`/`EndTime` as UTC timestamps** combined with a non-UTC `Timezone` on the recurrence — a mixed-reference-frame window the console flow does not expose (SS4).
- **`rate(value unit)`** expressions and raw six-field `cron(... Year)` grammar — richer than the console's predefined list (SS4).
- **`MinCapacity:0` / unbounded `MaxCapacity`** in `ScalableTargetAction` — the API doc does not restate the "0 allowed for Spot Fleets" rule on the scheduled-action param (it lives on `RegisterScalableTarget`), nor any numeric `MaxCapacity` ceiling (SS1).

---

## 5. Recommended Areas of Focus

### SS1 — Deferred / recurring destruction & cost **time-bomb** (Lens U / O / A) — PRIORITY
**Background.** A scheduled action sets `MinCapacity`/`MaxCapacity` at a future or recurring time; at trigger time AAS scales current capacity into that band and the SLR issues `ec2:ModifySpotFleetRequest`. For Spot Fleets **`MinCapacity:0` is explicitly allowed** (`RegisterScalableTarget`: "the minimum value allowed is 0 … Spot Fleets"), and `MaxCapacity` has **no documented upper bound** ("Although you can specify a large maximum capacity …"). Scale-in-to-0 is the whole-fleet terminate primitive (`modify-spot-fleet` plan) reached here **without the planter holding `ec2:ModifySpotFleetRequest` or `ec2:TerminateInstances`** — the SLR performs it.
**Security Concern.** `PutScheduledAction` turns the A1 "scale a foreign fleet now" primitive into a **timer**: `cron(...)` / `at(...)` with `ScalableTargetAction{MinCapacity:0,MaxCapacity:0}` plants a whole-fleet termination that fires at an attacker-chosen moment (e.g. a weekend, a known maintenance window) or **recurs** so every manual recovery is undone on the next tick. `MaxCapacity:<huge>` plants a scheduled cost blow-up. Because the change executes under the SLR, the planter can **delete the scalable target's registration, revoke their own session, or lose access** and the bomb still fires — temporal + attribution decoupling the IR team must reconstruct via `DescribeScheduledActions`/`DescribeScalingActivities`, not CloudTrail `userIdentity`.
**High-level Test Scenarios.**
- **Claim:** a principal holding only `application-autoscaling:RegisterScalableTarget`+`PutScheduledAction` (no `ec2:*`) can schedule the termination of a Spot Fleet at a future time via `MinCapacity:0,MaxCapacity:0`. **Mechanism:** `MinCapacity:0` allowed for Spot Fleets; SLR holds the unconditioned `ModifySpotFleetRequest`; trigger-time behavior "if current capacity is greater than the specified maximum capacity, Application Auto Scaling scales in to the maximum capacity." **Oracle:** two scoped roles in one authorized account — role A owns a `maintain` canary fleet; role B holds only the two AAS write actions; B registers A's `sfr`, puts an `at(<T+2min>)` action with Min/Max=0; observe A's instances terminate at T, with the `ModifySpotFleetRequest` CloudTrail event attributed to the SLR, not B. `iam:SimulatePrincipalPolicy` first (confirm no `Deny` fires on B). **Severity:** High (intra-account, time-delayed, cross-ownership destruction; attribution-obscured).
- **Claim (recurrence as anti-recovery):** a `cron(...)` action re-asserts Min/Max every tick, so an owner raising capacity back is overridden on the next fire. **Oracle:** plant `cron(0/5 * * * ? *)` Min=0; owner raises TargetCapacity; observe it collapse again within 5 min. **Severity:** High (persistent availability/cost control defeated).
- **Claim (cost):** `MaxCapacity:<very large>` scheduled action forces a mass scale-out at a chosen time. **Oracle:** `at(...)` with Max=10000 against a canary fleet; observe launch surge; tear down immediately. **Severity:** Medium–High (cost DoS).
**Doc evidence:** `API_PutScheduledAction.md` (`ScalableTargetAction`, `Schedule` formats); `API_RegisterScalableTarget.md` (`MinCapacity:0` for Spot Fleets; no `MaxCapacity` ceiling); `scheduled-scaling-policy-overview.md` (trigger-time scale-in/out); sibling S1 (SLR `ModifySpotFleetRequest` on `"*"`). **Severity-if-true:** High. **Stop condition:** confirm the chain reaches EC2 instance termination once on a canary; do not iterate across real fleets.

### SS2 — Scheduled-action namespace is IAM-indistinguishable; create-or-update **clobber** (Lens A / S / EE) — PRIORITY
**Background.** `list_application-autoscaling` defines **no `scheduled-action` resource type** — `PutScheduledAction` and `DeleteScheduledAction` both require resource type **`ScalableTarget*`** and expose only `scalable-dimension` + `service-namespace` + `aws:ResourceTag` as condition keys (**no `resource-id`, and no `aws:RequestTag`/`aws:TagKeys` on `PutScheduledAction`**). The API is **create-or-update by name** ("Creates or updates a scheduled action … This name must be unique among all other scheduled actions on **the specified scalable target**"), with **no version/etag/if-not-exists guard** documented.
**Security Concern.** Two compounding gaps:
1. **No per-action authz granularity.** IAM cannot distinguish one scheduled action from another on the same scalable target — the finest grain expressible is the `scalable-target/spot-fleet-request/sfr-…` ARN in the `Resource` element (and the sibling-A1 fact that even *that* cannot be pinned by condition key, only by literal ARN, and `scalable-dimension` is identical for every Spot Fleet). So any principal who can `PutScheduledAction`/`DeleteScheduledAction` on a target can **create, silently overwrite, or delete *every* named scheduled action on it** — including the owner's recovery/scale-up actions.
2. **Silent overwrite.** Because `Put` is create-or-update with no concurrency guard, an attacker who knows (or reads via SS5) the owner's `ScheduledActionName` can **replace its Min/Max/schedule in place** — the owner's console still shows an action by that name, now carrying the attacker's capacity values (an "edit in disguise"). `PutScheduledAction` also carries **no `aws:RequestTag` key**, so a defender cannot even require a tag at scheduled-action-create to segregate ownership.
**High-level Test Scenarios.**
- **Claim:** a principal scoped (by literal `Resource` ARN) to a scalable target can delete an owner's scheduled action on it. **Oracle:** owner creates action `nightly-scaledown`; attacker role (same ARN scope) calls `DeleteScheduledAction nightly-scaledown`; observe it gone. **Severity:** Medium–High (scheduling-integrity loss; chains to SS3 persistence).
- **Claim:** silent in-place overwrite — attacker replaces the owner's action payload keeping the name. **Oracle:** `PutScheduledAction` with the owner's existing name + attacker Min/Max; `DescribeScheduledActions` shows the same name, new values; no new-vs-update signal. **Severity:** Medium–High (stealthy; owner audits by name).
- **Claim (S):** no customer-authored policy can grant "manage only *my* scheduled action" — the only discriminators are the shared `scalable-dimension` and a per-target (not per-action) ARN. **Oracle:** attempt to author such a scoping policy; show it is structurally impossible with the published key set (same impossibility A1 found, now at scheduled-action grain). **Severity:** Medium–High (ABAC structurally impossible, not merely inert).
**Doc evidence:** `list_application-autoscaling.md` (PutScheduledAction/DeleteScheduledAction resource type `ScalableTarget*`, 3 condition keys, no `resource-id`; no `scheduled-action` resource type); `API_PutScheduledAction.md` ("Creates or updates", name unique per scalable target, no etag). **Severity-if-true:** Medium–High.

### SS3 — Scheduled action **permanently rewrites** the bounds — AAS does not revert after `EndTime` (Lens U / AA) — PRIORITY
**Background.** AAS User Guide, verbatim: **"If you specify an end time, the action stops repeating after this time. Application Auto Scaling does not keep track of previous values and revert back to those previous values after the end time."** A scheduled action's `MinCapacity`/`MaxCapacity` is written onto the scalable target and **left there**.
**Security Concern.** A customer (and an auditor) naturally reads a time-bounded scheduled action as *temporary* — "scale up for Black Friday, then back to normal." The docs confirm it is **not** temporary: after `EndTime` (or after a one-time `at(...)` fires) the rewritten Min/Max **persists indefinitely**. So a single `PutScheduledAction` is a **standing-state mutation disguised as a transient event**:
- `MinCapacity:<high>` with a past/short window pins a permanent capacity *floor* (cost) that survives the schedule and the planter's access, and overrides target-tracking scale-in (which "does not scale below the minimum").
- `MaxCapacity:0`/low with a short window permanently caps the fleet (availability) even after the action is deleted — deleting the *action* does not restore the *bounds*.
This is also a **revocation-incompleteness** shape (Lens AA): tearing down the attacker's scheduled action does not undo its effect; the owner must independently `RegisterScalableTarget` to reset Min/Max. Compounds SS1 (recurrence) and SS2 (clobber): an attacker can plant a one-shot `at(<now>)` Min=high action, let it fire, then delete it — leaving a permanent floor with no surviving scheduled-action artifact to find.
**High-level Test Scenarios.**
- **Claim:** a one-time scheduled action's Min/Max persists on the scalable target after it fires / after `EndTime`, and is not restored. **Oracle:** note target Min/Max; put `at(<T+1min>)` Min=50; after it fires, `DescribeScalableTargets` shows Min=50 standing; delete the action; Min stays 50. **Severity:** Medium–High (persistent cost/availability state mutation; survives action deletion and planter access).
- **Claim (AA):** deleting the scheduled action does not revert the bound. **Oracle:** as above — the delete leaves the rewritten bound. **Severity:** feeds the above.
- **Claim (U):** the owner's expectation of "temporary" is doc-contradicted — flag the UI/mental-model gap. **Oracle:** doc citation. **Severity:** Informational (enabler, raises SS1/SS2 effective severity).
**Doc evidence:** `scheduled-scaling-policy-overview.md` ("does not … revert back"); `API_RegisterScalableTarget.md` (updating the target re-clamps current capacity into Min/Max — the only reset path). **Severity-if-true:** Medium–High.

### SS4 — Schedule expression, `Timezone`/DST, and `StartTime`/`EndTime` reference-frame semantics (Lens F / P / O)
**Background.** `Schedule` accepts `at(yyyy-mm-ddThh:mm:ss)`, `rate(value unit)`, `cron(6-field incl. Year)` (1–1600 chars); `Timezone` is any IANA/Joda name and **auto-adjusts for DST**; but `StartTime`/`EndTime` are documented as **always UTC** even when `Timezone` is set. There is **no documented synchronous `ValidationException` for `MinCapacity>MaxCapacity`** — the guidance is phrased as caller responsibility, implying execution-time (deferred) resolution.
**Security Concern.** Three sub-surfaces:
1. **Reference-frame mismatch (stealth/mis-timing).** A recurring `cron` evaluated in an obscure `Timezone` (e.g. `Pacific/Tahiti`, or a DST-observing zone) fires at a wall-clock time the UTC-reasoning owner/auditor does not expect — and the `StartTime`/`EndTime` guard rails stay in UTC, so a window the planter *thinks* bounds the action may not align with when it actually fires. Weaponizable to make a destructive SS1 action fire "off-schedule" relative to monitoring, or to survive a DST transition twice.
2. **min>max deferred resolution (fail-permissive-at-create).** If `Put` accepts `Min>Max` and resolves it only at trigger time (undocumented which wins), the created action is a latent inconsistent state; test whether trigger-time resolution clamps to Min (floor wins → cost) or Max (ceiling wins → termination) — the choice decides blast direction.
3. **Expression parsing (Lens F — low-confidence).** `cron`/`at`/`rate` strings up to 1600 chars are parsed server-side; classic injection is unlikely (bounded grammar, no downstream shell named), but confirm the parser rejects malformed/oversized/overlapping-field expressions cleanly rather than fail-open scheduling or crashing the per-target scheduler (noisy-neighbor on the shared scalable target). **This resolves the auto-scaling plan's §8 "schedule-expression injection — doc-gap null" by scoping it here.**
**High-level Test Scenarios.**
- **Claim:** a non-UTC `Timezone` makes a recurring action fire at a time inconsistent with the owner's UTC view and with the UTC `StartTime`/`EndTime` bounds. **Oracle:** `cron` in `Pacific/Tahiti` + UTC `EndTime`; observe actual fire times vs the window. **Severity:** Low–Medium (stealth enabler for SS1).
- **Claim:** `PutScheduledAction` accepts `MinCapacity>MaxCapacity`; trigger-time resolution picks one deterministically. **Oracle:** put Min=10,Max=2; observe accept (no sync error) and which bound wins at fire. **Severity:** Low–Medium (latent-state + blast-direction).
- **Claim (F):** malformed/oversized `Schedule` is rejected cleanly, not fail-open or crash. **Oracle:** submit a 1600-char / malformed cron; expect `ValidationException`, no scheduler disruption. **Severity:** Low (null-leaning; confirm not fail-open).
**Doc evidence:** `API_PutScheduledAction.md` (`Schedule`, `Timezone`, `StartTime`/`EndTime` UTC); `scheduled-scaling-using-cron-expressions.md` (DST auto-adjust); min>max guidance phrased as caller responsibility. **Severity-if-true:** Low–Medium.

### SS5 — `DescribeScheduledActions` unscopable read oracle + `ScheduledScalingSuspended` kill switch (Lens A / U / L)
**Background.** `DescribeScheduledActions` has **blank resource type and blank condition keys** in `list_application-autoscaling` → it cannot be resource- or tag-scoped; a grant is namespace-wide. `RegisterScalableTarget` accepts `SuspendedState` including **`ScheduledScalingSuspended`** — "while a suspension is in effect, all scaling activities that involve scheduled actions are suspended" — a scalable-target-level toggle (not per-action, not independently IAM-gated beyond `RegisterScalableTarget`).
**Security Concern.**
1. **Read oracle / recon.** A low-priv principal with only `application-autoscaling:DescribeScheduledActions` can enumerate **every scheduled action across the `ec2` namespace** — every fleet's `sfr-` id, future capacity plans, Min/Max, cron windows, and the exact `ScheduledActionName`s an SS2 overwrite needs. No ownership scoping is possible. This is the same read-side scopability asymmetry the sibling `manage-spot-fleet` plan found for `DescribeSpotFleetRequests` (blank resource cell), now on the scheduling surface, and it is the discovery primitive that makes SS2's name-overwrite practical.
2. **Suspension as a pin.** A principal who can `RegisterScalableTarget` (A1 shows this is unscopable to one fleet) can set `ScheduledScalingSuspended` on an owner's target → the owner's legitimate scheduled scale-down (cost control) or scale-up (availability) silently stops firing while `DescribeScheduledActions` still lists the actions as present → a stealthy, reversible-by-attacker availability/cost pin with no "disabled" artifact on the actions themselves.
**High-level Test Scenarios.**
- **Claim:** `DescribeScheduledActions` returns actions on fleets the caller does not own. **Oracle:** role with only that read action lists another team's scheduled actions in the account. **Severity:** Low–Medium (config disclosure; recon enabler for SS1/SS2).
- **Claim:** `ScheduledScalingSuspended` freezes an owner's scheduled scaling without a per-action signal. **Oracle:** suspend via `RegisterScalableTarget SuspendedState`; owner's scheduled scale-down does not fire; actions still listed. **Severity:** Medium (silent availability/cost pin).
**Doc evidence:** `list_application-autoscaling.md` (DescribeScheduledActions blank resource type + no condition keys); `API_RegisterScalableTarget.md` / `scheduled-scaling-policy-overview.md` (`SuspendedState=ScheduledScalingSuspended`). **Severity-if-true:** Low–Medium.

### SS6 — `maintain`-type prerequisite gate + deregister cascade (Lens P / AA)
**Background.** Prerequisites (target page): fleet type must be **`maintain`** ("Automatic scaling is not supported for requests of type `request`"); scheduled actions "can only be created for existing Spot Fleets." Cascade: "If a scalable target is deregistered … Any scheduled actions that were specified for the scalable target are deleted."
**Security Concern.** (a) **Gate enforcement point (fail-open?).** Is the `maintain`-type requirement checked synchronously at `RegisterScalableTarget`/`PutScheduledAction`, or does registration/scheduling succeed against a `request`-type fleet and silently no-op (consistent with `RegisterScalableTarget`'s "If the specified resource is not active … this operation does not change the resource's current capacity")? A fail-open leaves a dormant scheduled action that activates if the fleet later becomes `maintain` — a latent, confusing posture. **This question is co-owned with target-tracking TT5** (same prerequisite sentence); defer the general enforcement-point determination there and record here only the scheduled-action-specific instance (a planted scheduled action on a `request`-type fleet). (b) **Revocation symmetry.** The deregister cascade deletes scheduled actions but — per SS3 — does **not** revert the Min/Max those actions last wrote; confirm the cascade is complete for the action objects yet still leaves the standing-bound residue.
**High-level Test Scenarios.**
- **Claim:** a scheduled action is accepted against a `request`-type fleet and sits dormant. **Oracle:** register a `request`-type fleet (if registration is even allowed), put an action, observe accept + no fire. **Severity:** Low (posture confusion). *(Cross-ref TT5 for the authoritative enforcement-point test.)*
- **Claim:** `DeregisterScalableTarget` deletes scheduled actions but leaves the rewritten bound. **Oracle:** chains to SS3 — deregister, confirm actions gone, bound residue remains (or capacity state persists). **Severity:** Low–Medium.
**Doc evidence:** `spot-fleet-scheduled-scaling.html` (prerequisites); `API_PutScheduledAction.md` (deregister cascade); `API_RegisterScalableTarget.md` (deferred-activation sentence). **Severity-if-true:** Low–Medium.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Schedule a foreign fleet's termination/cost blow-up to fire later under the SLR | `PutScheduledAction` Min/Max + `at`/`cron`; SLR `ModifySpotFleetRequest` `"*"` | prerequisites imply scheduling only *your* fleet; "service-linked role … to modify the capacity of **the** fleet" |
| Overwrite / delete an owner's scheduled action (no per-action authz) | `PutScheduledAction` create-or-update by name; `DeleteScheduledAction`; `ScalableTarget`-grain IAM | `ScheduledActionName` "unique … on the specified scalable target" (implies isolation) |
| Permanent bound rewrite surviving the schedule | scheduled action Min/Max vs scalable-target standing bounds | time-bounded action *appears* temporary |
| Mis-time / stealth a destructive action via `Timezone`/DST | `Schedule` + `Timezone` vs UTC `StartTime`/`EndTime` | DST "automatically adjusts" (implies correctness) |
| Enumerate every fleet's future capacity plan | `DescribeScheduledActions` (no resource type/condition keys) | — (no scoping available) |
| Freeze an owner's scheduled scaling silently | `RegisterScalableTarget SuspendedState=ScheduledScalingSuspended` | suspension is a stated feature (not framed as an attack toggle) |
| Capacity change not attributable to the planter | CloudTrail + SLR + time separation | — |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account / cross-tenant IDOR on `sfr-<UUID>`** — 128-bit id is not fabricable (owned by `modify-spot-fleet` plan); only intra-account cross-team (known/enumerated-via-SS5 id) is in scope.
- **The shared control-loop IAM groundwork** — AWS-authored artifact / SLR-policy audit, the base foreign-fleet register-and-scale chain, caller-`RoleARN`, min/max-vs-`ModifySpotFleetRequest`, managed-alarm/custom-metric tampering, legacy-role parity — all owned by **`spot-fleet-automatic-scaling-attack-research-plan.md`** (R1/S1/A1/B1/U1/L1/L2/X1). This plan cross-references, never restates them.
- **Target-tracking policy specifics** (alarm pair, `CustomizedMetricSpecification`, `maintain`-gate enforcement-point determination, ALB `ResourceLabel`) — owned by **`spot-fleet-target-tracking-attack-research-plan.md`** (TT1–TT5).
- **EC2-side `ModifySpotFleetRequest` internals** (`ExcessCapacityTerminationPolicy`, `LaunchTemplateConfig.N`, `ec2:Attribute` case-sensitivity) and the Spot Fleet SLR launch guardrail-bypass — owned by `modify-spot-fleet` / `create-spot-fleet` plans; here only the downstream effect of a scheduled fire.
- **The printed sample identity policy over-grants** (SNS/CloudWatch/IAM) — owned by `spot-fleet-auto-scaling-IAM-attack-research-plan.md`.
- **A customer who writes their own over-broad `application-autoscaling` policy** — least-privilege footgun (out of scope). In scope only where the weak default is an **AWS-authored/uneditable/copy-verbatim artifact** (that audit lives in sibling R1/S1).
- **AAS/EventBridge scheduler internals, shared AAS control-plane multi-tenancy, CloudWatch metric isolation** — AWS-shared infra / shared-responsibility line.
- **Single-tenant self-DoS** from your own flapping/mis-scheduled action where no ownership boundary is crossed; IMDS on the managed scaling control plane.

---

## 8. Null hypotheses / doc gaps
- **Lens B (confused deputy / caller `RoleARN`):** null **for scheduled scaling** — Spot Fleet supports an SLR, so `RegisterScalableTarget.RoleARN` is not required and the capacity change runs under `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`; the caller-`RoleARN`-honored question is owned by sibling **B1**. Pages checked: `API_RegisterScalableTarget.md`, `spot-fleet-auto-scaling-IAM.md`.
- **Lens G (SSRF) / Q (upload) / F-classic (translation injection):** null — the scheduled-scaling surface dereferences/fetches no URL and parses no uploaded blob; the only parsed input is the bounded `at`/`rate`/`cron` grammar (handled as a low-confidence sub-lead in SS4, not classic injection). Pages checked: `spot-fleet-scheduled-scaling.md`, `API_PutScheduledAction.md`, `scheduled-scaling-using-cron-expressions.md`.
- **Lens H (KMS / encryption context):** null — this surface generates/stores no key, secret, or encryption context. Pages checked: all four scheduling pages.
- **Lens K (prompt injection):** null — no LLM/agent in the scheduling path.
- **Lens V/D (network segmentation / data→control):** null — control-plane-to-control-plane API traffic (AAS scheduler → `ModifySpotFleetRequest`) with no customer-reachable ENI; the data-plane angle lives on launched instances (out of scope here).
- **DOC GAP — synchronous ownership check:** no doc states `PutScheduledAction` (or `RegisterScalableTarget`) synchronously re-validates EC2-side **ownership** of the `sfr-` fleet; `ObjectNotFoundException` is scoped to the *scalable target* record, not the EC2 resource, and the only published permission-validation worked example is RDS/Aurora — the exact synthetic EC2 IAM probes AAS issues for a Spot Fleet target are undocumented. **Confirm empirically before escalating SS1 beyond "deferred/execution-time check."**
- **DOC GAP — scheduler runtime identity:** the page links EventBridge cron docs but does **not** state that EventBridge Scheduler literally evaluates the schedule, nor name the identity that fires the action; only the downstream `ModifySpotFleetRequest`-under-SLR is confirmed. Confirm before reasoning about the scheduler's own trust boundary.
- **DOC GAP — min>max synchronous validation:** no documented hard `ValidationException` for `Min>Max` at `Put` time; resolution is implied deferred to execution. Determines SS4 blast direction — confirm which bound wins.
- **DOC GAP — `MinCapacity:0`/`MaxCapacity` ceiling on the scheduled-action param:** the "0 allowed for Spot Fleets" rule and the absence of a `MaxCapacity` ceiling are documented on `RegisterScalableTarget`, **not** restated on `PutScheduledAction`'s `ScalableTargetAction`; confirm they apply identically when set via a scheduled action (SS1 assumes they do).
- **DOC GAP — `maintain`-type gate enforcement point (SS6):** stated as a prerequisite but not whether enforced synchronously at register/put or silently deferred; co-owned with TT5. Confirm before relying on either reading.
- **DOC GAP — CloudTrail attribution of scheduled fires:** whether the scheduled `ModifySpotFleetRequest` carries any reference back to the planting principal/`ScheduledActionName`, or only the SLR `userIdentity`, is undocumented (gates SS1's attribution-decoupling severity).
- **`list_application-autoscaling` slug pitfall (reusable):** the authoritative resource-type/condition-key cells here were resolved from the **hyphenated** slug `list_application-autoscaling` (non-hyphen 404s / JS shell); mirror confirmed byte-equivalent to live. No `application-autoscaling:resource-id` condition key exists; `DescribeScheduledActions` has blank resource type + blank condition keys.

---

> **Downstream hunter note.** This is the *scheduled-scaling* layer of the Spot Fleet auto-scaling triad — **read `spot-fleet-automatic-scaling-attack-research-plan.md` Areas A1/S1/R1 first** (the ownership-unscopable + SLR-unconditioned groundwork this plan's time-deferral rides on; not restated here). Start with the **static, no-touch** confirmations: SS2's IAM-granularity claim (`list_application-autoscaling` — no `scheduled-action` resource type, no `resource-id` key, create-or-update by name) and SS3's "does not revert" doc fact + SS5's blank-scoped `DescribeScheduledActions` — all confirmable from the reference/API docs and `iam:SimulatePrincipalPolicy`/`GetPolicyVersion` before any live call. The headline chain is **SS1** (plant a deferred/recurring `MinCapacity:0,MaxCapacity:0` scheduled action → whole-fleet termination fires later under the SLR, no `ec2:*` held) → run with **two scoped roles in one authorized account + a `maintain` canary fleet**, `at(<T+2min>)`, `Simulate` first; verify the `ModifySpotFleetRequest` CloudTrail event is SLR-attributed (Lens O). Then **SS3** (confirm the bound persists after the action fires and after you delete it), **SS2** (overwrite/delete an owner's action by name after discovering it via SS5), **SS4** (Timezone/DST mis-timing + min>max deferred resolution), **SS5** (`ScheduledScalingSuspended` pin). Resolve the §8 doc-gaps (synchronous ownership check; scheduler identity; min>max winner; CloudTrail attribution) before escalating severity. **Tear down every scheduled action, scalable target, and canary fleet created** — and remember SS3: deleting the action does *not* reset the bounds, so also `RegisterScalableTarget` the canary back to baseline. **Hard stop** on any AWS service-plane identity.
