# EC2 Fleet / Spot Fleet — EventBridge Event Stream — Attack Research Plan

**Source of leads:** AWS EC2 User Guide page `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-ec2-fleet-using-eventbridge.html` (title *"Monitor and programmatically respond to the events emitted by your EC2 Fleet or Spot Fleet using Amazon EventBridge"*; markdown twin `monitor-ec2-fleet-using-eventbridge.md`, read in full — all 674 lines, every one of the 10 event-type examples and ~30 sub-types). Supporting pages: `describe-ec2-fleet.md#describe-ec2-fleet-event-history` (the symmetric pull channel, `describe-fleet-history`), EventBridge User Guide `eb-create-pattern.md` (anchor `eb-create-pattern-considerations`), `eb-event-patterns.md`, `eb-use-conditions.md`, `eb-event-bus-perms.md`, `eb-cross-account.md`, `logging-using-cloudtrail.md`, `eb-service-event-cloudtrail-management.md`, `API_PutRule.md`; IAM **Service Authorization Reference** `list_eventbridge.md` (service prefix `events`), `list_ec2.md`.

**Status:** documentation-derived hypotheses only; nothing tested against a live account. All offline `.md` cross-checked against the online `.md`/`.html` twin on **2026-10-14**. One drift observed: `eb-create-pattern.md` is truncated in the offline mirror (trailing "duplicate fields" bullet dropped) — not material to any lead here, but a reminder to diff tail sections online. No drift on any action/condition-key/event-schema cell cited here. Slug reminders reconfirmed: `list_eventbridge` (service prefix `events`; `list_amazoneventbridge`/`list_cloudwatchevents` 404), `list_ec2` (not `list_amazonec2`).

---

## Relationship to sibling plans (complement, do NOT duplicate)

This is the **dedicated page-level deep-dive for the single page `monitor-ec2-fleet-using-eventbridge.html`.** The **hub companion `fleet-monitor-attack-research-plan.md`** already owns the *mechanism-level* EventBridge analysis for this exact page as its net-new child, developing: Area 1 (default-bus capture / unscopable push vs tag-scoped pull + the `ForAllValues`/`events:source` **vacuous-truth IAM bypass**), Area 2 (cross-account exfil + `events:PutPermission` blank-resource/condition + no `detail` redaction on delivery), Area 3 (EventBridge-target **PassRole confused deputy**, `iam:PassedToService=events.amazonaws.com`), Area 6 (detection evasion: `instant` fleets, best-effort, `UnmonitorInstances`), Area 7 (the `detail.description` nested-JSON-string parsing differential).

**This plan does NOT restate those.** It cross-references them and owns the **granular, page-content-specific layer the hub plan necessarily left at summary level**:
- **Area A** — the exhaustive **per-detail-type / per-sub-type disclosure catalog** (10 detail-types, ~30 sub-types): exactly which field in which event leaks what, including the high-value fields the hub plan only alluded to (Spot **market price**, `PreviousState` **state-transition oracle**, load-balancer **topology** linkage, service-**quota** exhaustion, `iamFleetRoleInvalid` IAM-misconfig beacon).
- **Area B** — the EventBridge **matching-engine semantics** (not the IAM layer the hub owns): omitted pattern fields are a true `"*":"*"` wildcard, so a `detail.sub-type`-only rule is **cross-source by engine design**; and the page's third pattern field `detail.sub-type` has **no IAM condition key at all** → structurally unrestrictable. Resolves the hub plan's §8 doc-gap #2 (default-bus policy state).
- **Area C** — **`PutRule` name-clobber**: create-or-overwrite-by-name, destructive full-replace, no ownership check → cross-team monitoring-rule disable/hijack. **This upgrades the hub plan's `Lens EE = null` verdict** (which dismissed rule-name uniqueness as "collision/DoS at most") to an owned integrity/detection-evasion lead, and reconciles the contradiction explicitly (see Area C).
- **Area D** — the **CloudTrail defender-blindspot asymmetry** specific to this flow (control actions logged by default; the leaky event bodies off-by-default and `detail`-redacted even when on) — deepens hub Area 6.
- **Area E** — the **legacy-twin parity** (`aws.ec2fleet` vs `aws.ec2spotfleet`) as a monitoring/detection coverage gap (Lens X), with the exact per-family detail-type/sub-type diff.

**Explicitly defers** (thin pointers only, Area F/G): cross-account exfil + `PutPermission` → hub Area 2; EventBridge-target PassRole → hub Area 3; the whole CloudWatch `AWS/EC2Spot` metric plane → `ec2-fleet-cloudwatch-metrics-attack-research-plan.md`; the tag-scoped pull APIs' own scopability → `manage-spot-fleet` / `spot-fleet-states`; the 48 h event-history forensic decay (the page's "deleted/cancelled two days after" note) and SLR→human CloudTrail attribution break → `spot-fleet-states` (SF-11/15); the EC2-side fleet-SLR launch-time PassRole → `spot-fleet-prerequisites` / `create-spot-fleet`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This whole surface is **read / telemetry-shaped**: no new mutating EC2 API lives on this page. Leads are *information-disclosure*, *detection-evasion*, and *IAM-scopability* findings. Severity is **intra-account cross-team** unless a cross-account EventBridge target/bus policy is in play (that path is owned by hub Area 2).
- Start with the **static, no-touch** checks (read the Service Authorization Reference; `iam:SimulateCustomPolicy`) before any live call. Many leads here are settled by doc analysis alone (Area B's no-condition-key fact; Area C's `API_PutRule` overwrite semantics).
- Fleet / Spot Fleet ids are UUIDv4-shaped (`fleet-…` ~122-bit, `sfr-…`) → **not enumerable**; cross-account IDOR by guessing an id is a null (see §8). The pivot is the *channel*, not the id.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (the fleet control plane emitting on an AWS-owned bus, an SLR acting outside the authorized account), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to achieve:
1. **Read another team's fleet operational + launch-spec intelligence** — instance types, AMI IDs, AZ placement, Spot **market prices**, lifecycle **state transitions**, load-balancer wiring, IAM-misconfig beacons — using a principal that has **no** `ec2:Describe*Fleet*` rights and no fleet tag, by creating one EventBridge rule+target on the shared default bus (Area A + Area B). This bypasses the tag-scoped pull API (`DescribeFleetHistory`) the account relies on for team isolation.
2. **Capture every fleet's events with a single source-agnostic rule** — a `detail.sub-type`-only pattern (no `source`, no `detail-type`) that the matching engine wildcards across **both** fleet families and any other source (Area B).
3. **Silently disable or hijack another team's fleet-monitoring rule** by calling `PutRule` with the victim's rule name (create-or-overwrite, destructive full-replace, no ownership check) — a detective-control takedown or a race against an IaC/security-automation deploy (Area C).
4. **Operate under the account's CloudTrail blind spot** — the leaky event *bodies* are data events (off by default) and `detail`-redacted even when enabled, so a defender auditing the bus cannot see what an attacker's rule exfiltrated (Area D).
5. **Exploit a monitoring rule scoped to one fleet family** (`aws.ec2fleet` xor `aws.ec2spotfleet`) that silently misses its legacy twin (Area E).

---

## 2. Components, Assets, and Design

**What this page is.** The EventBridge **push channel** for EC2 Fleet (`source: aws.ec2fleet`) and the legacy Spot Fleet (`source: aws.ec2spotfleet`). When a fleet or an instance/Spot-request within it changes state, the control plane emits a JSON event to **the account's default event bus**. The page is verbatim: *"When an AWS service in your account generates an event, it always goes to your account's default event bus."* Customers write EventBridge **rules** (event-pattern match) wired to **targets** (SNS, Lambda, SQS, …) to react. The *same* lifecycle data is also readable via the tag-scoped pull API `ec2:DescribeFleetHistory` / `ec2:DescribeSpotFleetRequestHistory` (`describe-fleet-history` returns identical `EventDescription`/`EventSubType`/`InstanceId` records — confirmed, see Area A).

```
   Fleet / Spot Fleet control plane (AWS service plane)
   state machine: submitted→active→modify→deleted/cancelled→…
            │ (best-effort emit; maintain/request only — instant emits nothing)
            ▼
   ┌─────────────────────────────────────────────┐
   │ account DEFAULT event bus                     │  ← no per-team / per-source partition
   │ source: aws.ec2fleet | aws.ec2spotfleet       │
   │ 10 detail-types, ~30 sub-types, detail{...}   │
   └───────────────┬───────────────────────────────┘
    rule match (engine: present-fields AND; absent = "*":"*" wildcard)
                   │  ← identity-policy-gated only (no resource policy needed same-account)
                   ▼
     SNS / Lambda / SQS / Kinesis / Step Fn / API dest / another bus (same OR cross-acct)
                   │   detail NEVER redacted on delivery
                   ▼
            attacker-controlled target
   ───────────────────────────────────────────────
   Pull twin (tag-scoped): ec2:DescribeFleetHistory (fleet*) /
                           ec2:DescribeSpotFleetRequestHistory (spot-fleet-request*)
                           → identical EventDescription payload, aws:ResourceTag-scopable
```

**Assets at risk — the per-event payload (full catalog in Area A).** Every event carries `account`, `region`, `time`, the fleet **ARN** (`arn:aws:ec2:…:fleet/fleet-…` or `…:spot-fleet-request/sfr-…`), and a `detail` object whose fields depend on the detail-type: `sub-type` (lifecycle state), `instance-id` (`i-…`), `spot-instance-request-id` (`sir-…`), and a free-text / escaped-JSON **`description`** that embeds launch-spec (`instanceType`, `image`=AMI, `productDescription`, `availabilityZone`), **Spot market price** (`"… less than Spot market price $0.0619"`), **previous lifecycle state** (`"…, PreviousState: cancelled_running"`), load-balancer registration failures, and IAM-misconfiguration strings (`iamFleetRoleInvalid`).

**Identity establishment.** SigV4/IAM only; no separate data-plane credential. Rules invoke targets under either the EventBridge service principal (`events.amazonaws.com`) or a customer-supplied `RoleArn` (hub Area 3).

**Resource identifiers.** `fleet-`+UUIDv4 (~122-bit), `sfr-`+UUIDv4 — not enumerable. EventBridge **rule name** is the only *predictable/caller-chosen* identifier here, unique per Region+bus (Area C).

**Mandatory coverage sweep — pages checked for each lens trigger:** read `monitor-ec2-fleet-using-eventbridge.md` (full), `describe-ec2-fleet.md` (event-history), `eb-create-pattern.md`/`eb-event-patterns.md` (matching engine), `eb-use-conditions.md`/`eb-event-bus-perms.md`/`eb-cross-account.md` (authz/bus policy), `logging-using-cloudtrail.md`/`eb-service-event-cloudtrail-management.md` (audit), `API_PutRule.md`, `list_eventbridge.md`, `list_ec2.md`. **No field on this page is a server-side-dereferenced URL** (the rule *target* is a customer-chosen destination, not a service-side fetch → Lens G null); **no upload/blob** (Lens Q null); **no KMS/encryption context** (Lens H null); **no JWT/token/session** (SigV4 only → Lens FF/M null); **no proofing/registration gate** (Lens P null). Null hypotheses with checked pages in §8.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| In-account principal **without** `ec2:Describe*Fleet*` and without a fleet tag | Another team's fleet launch-spec / price / state / LB-wiring data | `events:PutRule` (default bus) matching `aws.ec2fleet`/`aws.ec2spotfleet` **or omitting `source`** + `PutTargets` to a destination it reads | A rule the principal owns delivers *another team's* `detail.description`/`sub-type`/`instance-id` to a target it controls, where `DescribeFleetHistory` on the same `fleet-…` returns `AccessDenied` → **intra-account observability-bypass breach** (Area A/B) |
| In-account principal with `events:PutRule` on a wildcard rule-name ARN | Another team's existing monitoring rule | `PutRule` with the victim's rule `Name` (create-or-replace, no ownership check) | The victim rule's `EventPattern`/`State` is silently overwritten / disabled → **cross-team detective-control takedown / integrity breach** (Area C) |
| Defender auditing the bus via CloudTrail | The exfiltrated event bodies | CloudTrail management vs data event split | Rule setup (`PutRule`/`PutTargets`) is logged, but the delivered `detail` is unobservable (data events off; `detail` = `HIDDEN_DUE_TO_SECURITY_REASONS`) → **audit-visibility gap** (Area D) |
| Operator writing a detection rule for one fleet family | The other (legacy) family | A rule scoped `source:["aws.ec2fleet"]` (or vice-versa) | Equivalent events from the untargeted `source` are not matched → **monitoring coverage gap** (Area E) |
| In-account attacker | **Another AWS account** | rule target = cross-account bus/SQS/SNS; `events:PutPermission` on default bus | Fleet events with leaky `description` arrive in a foreign account → **cross-account exfil** (owned by hub Area 2 — pointer) |
| Principal with `events:PutTargets` + loose `iam:PassRole` | Any EventBridge-trusting over-privileged role | pass `RoleArn`; EventBridge assumes it to invoke a target | Action runs under a role the caller could not assume directly → **confused deputy** (owned by hub Area 3 — pointer) |
| Any customer surface | AWS service plane (fleet control plane / AWS-owned bus / SLR) | — | Any AWS-owned identity/ARN/account observed → **HARD STOP, disclose** |

---

## 4. API / Interface Inventory

| Name | Method | Mut? | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `events:PutRule` | SDK | **Yes** | External | Create **or overwrite** a rule by name on an event bus | Yes | Any principal w/ action | Resource `rule-on-default-event-bus`/`rule-on-custom-event-bus` (ARN `…:rule/${RuleName}`). **Create-OR-update, destructive full-replace, no ownership check** (Area C). Condition keys incl. `events:source`, `events:detail-type`, `events:creatorAccount` (account-scoped), `events:detail.{eventTypeCode,service,userIdentity.principalId}` — **but NO key for `detail.sub-type`** (Area B). |
| `events:PutTargets` | SDK | **Yes** | External | Wire targets to a rule (additive by target id) | Yes | Any principal | `events:TargetArn` key; `iam:PassRole`(`PassedToService=events.amazonaws.com`) → hub Area 3. A `PutRule` overwrite does **not** wipe targets (Area C note). |
| `events:PutPermission` | SDK | **Yes** | External | Grant another account access to the default bus | Yes | Any principal | **Blank resource type, blank condition keys** → unconditioned cross-account grant (owned by hub Area 2). |
| `ec2:DescribeFleetHistory` | SDK | No | External | Pull EC2 Fleet event history | Yes | Owner (tag-scoped) | Resource `fleet*` **required**; `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region`. Returns **identical** `EventDescription`/`EventSubType`/`InstanceId` payload as the push channel (confirmed, Area A) → the **tag-scopable twin** of the unscopable push channel (Lens X). |
| `ec2:DescribeSpotFleetRequestHistory` | SDK | No | External | Pull Spot Fleet event history | Yes | Owner (tag-scoped) | Resource `spot-fleet-request*` **required** + same tag keys. (Owned by `manage-spot-fleet`/`spot-fleet-states`.) |

**Undocumented / console-hidden knob check.** The page is a console/SDK workflow over standard EventBridge APIs; no auth-weakening hidden knob. The one engine behavior the console *form* hides is that the "Event pattern form" always inserts `source` + `detail-type`, but the "Custom pattern (JSON editor)" lets a caller **omit `source`** — the permissive form the console template never shows (Area B). The page itself even prints a (JSON-malformed, missing a closing brace) `detail.sub-type` custom-pattern example, steering operators to the sub-type filter.

---

## 5. Recommended Areas of Focus

### Area A — Per-detail-type / per-sub-type disclosure catalog (headline; the owned granular layer under hub Area 1/2)
**Background.** The page documents **10 detail-types** (5 EC2 Fleet + 5 Spot Fleet) each with several sub-types (~30 total). Each lands on the default bus and is capturable by any `events:PutRule` principal (Area B) regardless of the tag-scoped pull API. The hub plan established *that* the stream leaks; this area catalogs **exactly what each event discloses**, because the per-field disclosure is the thing a hunter proves and rates.

**Security Concern — the disclosure catalog (all fields verbatim from the page examples):**

| Detail-type (both families) | `detail` fields | Sub-types | **What it discloses** |
|---|---|---|---|
| `EC2 Fleet State Change` / `EC2 Spot Fleet State Change` | `sub-type` + fleet ARN in `resources` | EC2 Fleet: `active, deleted, deleted_running, deleted_terminating, expired, modify_in_progress, modify_succeeded, submitted, progress` · Spot Fleet: `active, cancelled, cancelled_running, cancelled_terminating, expired, modify_in_progress, modify_succeeded, submitted, progress` | Fleet **lifecycle state** + account + fleet id. `modify_*` reveals config churn (someone is actively re-tuning the fleet); `deleted`/`cancelled` reveals teardown and (per the page) the **48 h delete-after-terminate window** (decay owned by `spot-fleet-states`). |
| `… Spot Instance Request Change` | `spot-instance-request-id` (`sir-…`), **`description`** = `"SpotInstanceRequestId sir-…, PreviousState: cancelled_running"`, `sub-type` (`active, cancelled, disabled, submitted`) | — | The `sir-` id **and the PREVIOUS lifecycle state** → a **state-transition oracle** (Area A-note). `disabled` = "You stopped the Spot Instance" reveals manual operator intervention. |
| `… Instance Change` | `instance-id` (`i-…`), **`description`** = escaped-JSON launch spec `{"instanceType":"c5.large","image":"ami-6057e21a","productDescription":"Linux/UNIX","availabilityZone":"us-east-1d"}`, `sub-type` (`launched, terminated, termination_notified`) | — | Instance id + **full launch spec** (type, **AMI id**, OS, **AZ placement**) + scale-down timing (`termination_notified`, page: "from a target capacity of 4 to … 3"). |
| `… Information` | **`description`** = free text w/ type, AMI, AZ, **Spot market price** (`"… less than Spot market price $0.0619"`), `sub-type` (`fleetProgressHalted, launchSpecTemporarilyBlacklisted, launchSpecUnusable, registerWithLoadBalancersFailed`) | — | **Spot market/bid intelligence** (the price the workload is bidding against); `registerWithLoadBalancersFailed` reveals the fleet is **wired to an ELB/ALB** (topology linkage to the target workload). |
| `… Error` | **`description`** = config-error strings (`"IPv6 is not supported for the instance type 'm3.large'"`, `"The associatePublicIPAddress parameter can only be specified for the network interface with DeviceIndex 0"`), `sub-type` (`iamFleetRoleInvalid, allLaunchSpecsTemporarilyBlacklisted, spotInstanceCountLimitExceeded, spotFleetRequestConfigurationInvalid`) | — | **`iamFleetRoleInvalid` = IAM-misconfiguration recon beacon** ("does not have the required permissions to either launch or terminate an instance"); `spotInstanceCountLimitExceeded` leaks **account service-quota exhaustion**; config errors leak network/launch-spec internals. |

**High-level Test Scenarios.**
- **Claim:** A principal holding only `events:PutRule`/`events:PutTargets` (no `ec2:Describe*Fleet*`, no fleet tag) obtains another team's launch spec, AMI id, AZ, and Spot price. **Oracle:** create a rule `{"detail-type":["EC2 Fleet Information","EC2 Fleet Instance Change"]}` (no `source`) + an SQS target it reads; observe a foreign fleet's `description`. Compare: `DescribeFleetHistory` on the same `fleet-…` returns `AccessDenied` under the same principal → the push channel bypasses the pull channel's tag scope. (Two scoped roles, one authorized account, self-owned canary fleet to generate the events.)
- **Claim (A-note, state oracle):** The `Spot Instance Request Change.description`'s `PreviousState` exposes a prior→current transition the owner never shared. **Oracle:** capture a `cancelled` event and read `PreviousState: cancelled_running` → a lifecycle history leak with no `ec2` rights.
- **Claim (recon beacon):** `iamFleetRoleInvalid` / `spotFleetRequestConfigurationInvalid` error events tell an attacker which fleets have broken/limited roles. **Oracle:** confirm the Error sub-types carry the misconfiguration `description` to any rule target (they do, per the examples).
- Look left/right: `registerWithLoadBalancersFailed` + the fleet ARN lets an attacker correlate a fleet to the LB/target-group it serves; `spotInstanceCountLimitExceeded` reveals the victim is at a quota ceiling (a DoS-timing signal).

**Doc evidence.** `monitor-ec2-fleet-using-eventbridge.md` (all 10 event examples + sub-type lists, lines 235–674); `describe-ec2-fleet.md` lines 154–194 (the pull twin returns identical `EventDescription`/`EventSubType`/`InstanceId`); `list_ec2.md` `DescribeFleetHistory` row (`fleet*` + tag keys). **Severity-if-true:** **Medium** intra-account cross-team info-disclosure, **raised toward High** where ABAC on fleets is the account's sole team-isolation mechanism (the price/AMI/LB intel is a strong recon primitive; not credentials → not Critical by itself). **Owner-to-fix:** shared — AWS owns the unscopable push channel and the un-redacted `description`; the customer owns not relying on fleet-tag ABAC as the only isolation. **Stop condition:** one foreign `description` captured + the paired `DescribeFleetHistory` AccessDenied; do not enumerate every detail-type.

### Area B — The matching engine is source-agnostic, and `detail.sub-type` has no IAM condition key (the structural root of "unscopable push channel")
**Background.** The hub plan's Area 1 attacks the *IAM layer* (the `events:source` condition's `ForAllValues` vacuous-truth bypass). This area attacks the layer underneath it — the EventBridge **matching engine** itself and the **absence of a condition key** — which makes the channel unscopable even with a *correctly written* IAM policy.

**Security Concern.**
1. **Omitted pattern fields are a true wildcard.** `eb-create-pattern.md` (anchor `eb-create-pattern-considerations`): *"For an event pattern to match an event, the event must contain all the field names listed in the event pattern … EventBridge ignores the fields in the event that aren't included in the event pattern. The effect is that there is a `"*": "*"` wildcard for fields that don't appear in the event pattern."* So a pattern `{"detail":{"sub-type":["launched"]}}` — naming only `detail.sub-type`, **omitting `source` and `detail-type`** — matches **any** event from **any** source carrying `detail.sub-type:"launched"`: both `aws.ec2fleet` and `aws.ec2spotfleet`, and any other AWS/partner source using that sub-type. This is cross-source capture **by engine design**, not merely via an IAM gap. (The page's own Lambda example steers operators to a `detail.sub-type` filter.) *Caveat the doc self-flags: "This describes current EventBridge behavior, and should not be relied on to not change."*
2. **`detail.sub-type` has no corresponding IAM condition key.** `list_eventbridge.md` `PutRule` condition keys: `events:source`, `events:detail-type`, `events:detail.eventTypeCode`, `events:detail.service`, `events:detail.userIdentity.principalId`, `events:creatorAccount`, tag keys — **and nothing for `detail.sub-type`.** So the page's *third* documented pattern field is **structurally unrestrictable at the IAM layer**: an admin cannot write a `PutRule` policy that allows building sub-type rules for only its own events, because the key does not exist. (`events:source`/`events:detail-type` *do* exist but are the keys the hub plan showed are vacuous-truth-bypassable.)
3. **Default-bus access is identity-policy-gated only (resolves hub §8 doc-gap #2).** `eb-use-conditions.md`: *"If an IAM user or role is authorized for the `events:PutRule` action, they can create a rule that matches certain events"* — no event-bus resource policy is required for same-account rule creation. `eb-event-bus-perms.md` scopes the resource policy to **cross-account** only. ⇒ any in-account principal whose identity policy grants `events:PutRule`/`PutTargets` reaches the whole stream with zero resource-policy gate; the only scoping is whatever `Resource`/condition the identity policy itself carries (and per (1)/(2), it cannot carry an effective one keyed on sub-type).

**High-level Test Scenarios.**
- **Claim:** a source-omitting `detail.sub-type`-only rule captures both fleet families with one rule. **Oracle:** `iam:SimulateCustomPolicy` is not needed for the engine fact — confirm by doc; live-confirm (authorized) by creating the rule and observing both `aws.ec2fleet` and `aws.ec2spotfleet` events arriving at the target.
- **Claim:** no IAM policy can restrict a principal to building rules for only its own fleet events via `detail.sub-type`. **Oracle:** show `list_eventbridge` has no `events:detail.sub-type` key → the restriction is unexpressible (static, settled by doc).
- **Claim:** the default bus needs no resource policy for an in-account `events:*` principal. **Oracle:** inspect the account's default-bus policy (commonly empty) and `iam:SimulatePrincipalPolicy` for `events:PutRule` → `allowed` with identity policy alone.

**Doc evidence.** `eb-create-pattern.md` (`eb-create-pattern-considerations`); `list_eventbridge.md` (`PutRule` condition-key column); `eb-use-conditions.md`, `eb-event-bus-perms.md`; `monitor-ec2-fleet-using-eventbridge.md` (the three pattern fields `source`/`detail-type`/`detail.sub-type`, Lambda example). **Severity-if-true:** **Medium–High** — this is the *structural* basis for the hub-headline "unscopable per-fleet push channel"; it elevates the IAM bypass (hub Area 1) from "bypassable sample policy" to "no correct policy exists for the sub-type field." **Owner-to-fix:** AWS (engine wildcard semantics + missing condition key). **Stop condition:** the two static doc facts (wildcard rule; no `detail.sub-type` key) + one live cross-source capture; do not enumerate sources.

### Area C — `PutRule` name-clobber: cross-team monitoring-rule disable / hijack (reconciles the hub plan's Lens EE null)
**Background & reconciliation.** The hub plan evaluated **Lens EE as null**, dismissing the page's rule-name uniqueness ("A rule can't have the same name as another rule in the same Region and on the same event bus") as "a naming-collision/DoS at most, not a trust-adoption land-grab." **This plan reaches a different, stronger verdict from `API_PutRule`:** `PutRule` is **create-OR-update keyed by `Name`, a destructive full-replace, with no documented ownership/creator check.** That makes rule-name uniqueness not just a collision nuisance but a **cross-team integrity + detective-control takedown primitive** — so EE *fires* here. The contradiction is reconciled: the hub's null stands for *land-grab of a trust-adopted name*; this plan owns the *overwrite/disable of an existing rule* shape the hub did not model.

**Security Concern.** `API_PutRule.md`: *"Creates or updates the specified rule. … If you are updating an existing rule, the rule is replaced with what you specify in this `PutRule` command. If you omit arguments in `PutRule`, the old values for those arguments are not kept. Instead, they are replaced with null values."* No statement conditions the overwrite on the original creator. The only scoping levers are (a) generic resource-ARN scope — but `rule-on-default-event-bus` is ARN `…:rule/${RuleName}`, so any principal with `events:PutRule` on `Resource:"*"` or a wildcard rule-name reaches any name; and (b) `events:creatorAccount`, which is **account-scoped** and therefore does nothing against **same-account cross-team** overwrite. Consequence: a principal holding broad `events:PutRule` can call `PutRule` with another team's rule `Name` and silently replace its `EventPattern`/`State`/`ScheduleExpression` — e.g. set the pattern to match nothing, or `State=DISABLED` — **blinding that team's fleet-security automation** while the rule still "exists." (Targets are separate: `PutTargets` is additive per target id and not wiped by `PutRule`, so a subtler variant leaves the targets but neuters the pattern.) A race variant: pre-create or overwrite a rule name an IaC/security-automation deploy is about to `PutRule`, winning or losing the race to control the final pattern.

**High-level Test Scenarios.**
- **Claim:** `PutRule` on an existing foreign-team rule name overwrites its pattern with no ownership error. **Oracle:** `iam:SimulatePrincipalPolicy` for `events:PutRule` on `arn:…:rule/<victimRuleName>` → `allowed` when `Resource` is `*`/wildcard; (authorized live) a scoped role overwrites a canary "security" rule's `EventPattern` to a non-matching pattern and the original pattern is gone (confirms destructive replace, not merge).
- **Claim:** the overwrite disables detection without deleting the rule (stealthier than `DeleteRule`). **Oracle:** overwrite with `State=DISABLED` or an impossible pattern; confirm the rule still lists but no longer fires.
- **Claim:** `events:creatorAccount` does not protect same-account teams. **Oracle:** show the key is account-scoped in `list_eventbridge` → inert for intra-account cross-team.
- Look left/right: chain with Area D — the overwrite itself *is* a logged management event, but a defender who only alarms on `DeleteRule` misses a `PutRule`-overwrite disable.

**Doc evidence.** `API_PutRule.md` (create-or-update, replace-with-null semantics, tags-ignored-on-update); `monitor-ec2-fleet-using-eventbridge.md` (rule-name uniqueness per Region+bus); `list_eventbridge.md` (`PutRule` ARN `…:rule/${RuleName}`, `events:creatorAccount` account-scoped). **Severity-if-true:** **Medium–High** — intra-account cross-team: disabling a victim team's fleet-security monitoring is a detective-control takedown (High as an enabler of a larger attack); pure overwrite without detection impact is Medium integrity/DoS. **Owner-to-fix:** customer (scope `events:PutRule` to a rule-name prefix per team) + AWS (no creator-pinned overwrite guard; `creatorAccount` is the only lever and it's account-grain). **Stop condition:** one simulated/observed overwrite of a canary rule's pattern; do not iterate rule names.

### Area D — CloudTrail defender-blindspot asymmetry (deepens hub Area 6)
**Background.** The hub plan noted (Area 6) that rule *setup* is auditable as management events. This area sharpens the exact asymmetry for *this* flow: the control actions are logged by default, but the leaky event **bodies** are not — and are redacted even when logging is turned on.

**Security Concern.** `logging-using-cloudtrail.md`: *"By default, CloudTrail logs management events,"* and *"All Amazon EventBridge API operations except `PutEvents` and `PutPartnerEvents` are control plane operations"* → `PutRule`/`PutTargets`/`PutPermission` are **management events, logged by default** (example at line 137 shows `"eventName":"PutRule"`). But *"By default, CloudTrail doesn't log data events,"* and the event delivery itself (`PutEvents`) is a **data event**; moreover *"The `detail` field in event entries is **redacted** in CloudTrail data event logs to protect sensitive data"* → the examples show `"detail": "HIDDEN_DUE_TO_SECURITY_REASONS"`. So: a defender who enables EventBridge **data events** to audit what crosses the bus **still cannot see the `detail`** (the launch-spec/price/beacon payload) — yet that same `detail` is delivered **verbatim** to an attacker's rule target (EventBridge never redacts on delivery; hub Area 2). The audit channel is strictly weaker than the exfil channel. Additional attribution gap for the cross-account path (Area 2): *"When an account that you granted permission to via a resource policy calls `PutEvents` to your bus, only the caller's account receives the CloudTrail data event. Your account (the bus owner) does not"* — the bus owner can be blind to a foreign principal publishing to its bus.

**High-level Test Scenarios.**
- **Claim:** enabling EventBridge data-event logging does not reveal what a capturing rule exfiltrated. **Oracle:** inspect a data-event log entry → `detail` is `HIDDEN_DUE_TO_SECURITY_REASONS` while the target (SQS) holds the full `detail` (doc-confirmable; one authorized round-trip corroborates).
- **Claim:** a `PutRule`-overwrite (Area C) is logged, so the setup stays auditable. **Oracle:** confirm the management-event default captures the overwrite → the evasion *setup* is detectable even though the data channel is blind (this bounds Areas A–C: a CloudTrail-management-event watcher sees the rule being created/overwritten).
- **Claim (cross-account attribution gap):** a foreign account `PutEvents` to the default bus leaves no data event in the bus owner's trail. **Oracle:** the doc table at lines 73–108 → bus-owner "does not" receive the data event.

**Doc evidence.** `logging-using-cloudtrail.md` lines 31/33/42/59/73/263/334/411; `eb-service-event-cloudtrail-management.md` (management-event rules). **Severity-if-true:** **Low–Informational** (detection-evasion enabler; raises the severity of any paired Area A/B/C action). **Owner-to-fix:** customer (watch `PutRule`/`PutTargets`/`PutPermission` management events; don't rely on data-event `detail`) + AWS (the redaction + off-by-default asymmetry). **Stop condition:** confirm the `detail` redaction + management-event default; no exploit needed.

### Area E — Legacy-twin parity: `aws.ec2fleet` vs `aws.ec2spotfleet` (Lens X — monitoring coverage gap)
**Background.** The page documents **two parallel families** with the Spot Fleet note: *"Spot Fleet uses a legacy API with no planned investment."* They are near-identical in shape but differ in `source`, resource-ARN type, and a handful of State-Change sub-type names.

**Security Concern — the diff.** Both families have the same five detail-types (prefix `EC2 Fleet …` vs `EC2 Spot Fleet …`), identical `… Instance Change` / `… Spot Instance Request Change` / `… Information` / `… Error` sub-type sets, and identically-shaped `description` fields. **The only divergences:** (a) `source` (`aws.ec2fleet` vs `aws.ec2spotfleet`); (b) resource ARN (`fleet/fleet-…` vs `spot-fleet-request/sfr-…`); (c) **State Change sub-types**: EC2 Fleet uses `deleted / deleted_running / deleted_terminating`, Spot Fleet uses `cancelled / cancelled_running / cancelled_terminating` (same semantics, different strings). Consequence: a detection/response rule written for one family (e.g. `source:["aws.ec2fleet"]`, or a pattern keyed on `sub-type:["deleted_terminating"]`) **silently misses the legacy twin's equivalent events** — a monitoring coverage gap, and the inverse of Area B's attacker benefit (the attacker's source-omitting rule *gains* both; the defender's source-pinned rule *loses* one). Because Spot Fleet is "no planned investment," defenders are likely to under-build the legacy path.

**High-level Test Scenarios.**
- **Claim:** a rule scoped to `aws.ec2fleet` does not fire on an equivalent `aws.ec2spotfleet` teardown. **Oracle:** doc-diff the two State-Change sub-type lists (`deleted*` vs `cancelled*`) → a `deleted_terminating`-keyed rule cannot match a Spot Fleet `cancelled_terminating` event. (Static; corroborate live with a canary of each type.)
- **Claim:** the two pull twins also diverge in resource type (`fleet*` vs `spot-fleet-request*`), so a tag-ABAC policy written for one does not cover the other. **Oracle:** `list_ec2` `DescribeFleetHistory` (`fleet*`) vs `DescribeSpotFleetRequestHistory` (`spot-fleet-request*`).

**Doc evidence.** `monitor-ec2-fleet-using-eventbridge.md` (both family sections, the legacy note at line 452, the `deleted*` vs `cancelled*` sub-type lists); `list_ec2.md` (the two Describe rows). **Severity-if-true:** **Low–Medium** (detection coverage gap / least-privilege-asymmetry; not a direct data breach). **Owner-to-fix:** customer (cover both sources) + AWS (divergent sub-type vocab for identical semantics). **Stop condition:** the sub-type diff is demonstrated; no further.

### Area F — [POINTER] Cross-account exfiltration + EventBridge-target PassRole
**Cross-references, not owned leads.** Cross-account forwarding of the leaky `description` via a rule target / `events:PutPermission` (blank resource+condition) is owned in full by **hub Area 2**. The EventBridge-target **PassRole confused deputy** (`events:PutTargets` + `iam:PassRole`/`PassedToService=events.amazonaws.com`) is owned by **hub Area 3**. Do not re-run them from this plan. **Net-new hook this plan contributes:** the Area A disclosure catalog is the *payload* those two channels carry out of the account — the cross-account severity of hub Area 2 is set by *which* detail-types the attacker's rule matches (an `… Information`/`… Error` rule exfiltrates price + IAM-beacon intel; an `… Instance Change` rule exfiltrates the launch spec). Rate hub Area 2 using Area A's field inventory.

### Area G — [POINTER + deepening] `detail.description` parse differential & indirect-injection provenance
**Mostly owned by hub Area 7** (the nested-JSON-string parsing differential). **Net-new deepening this plan contributes:** the `description` field is **not one shape but four**, so no single parser is safe and a consumer must branch on both detail-type *and* sub-type:
1. `… Instance Change`: an **escaped-JSON object inside a string** — `"{\"instanceType\":…}"` (needs `JSON.parse` of a string-in-string);
2. `… Spot Instance Request Change`: a **key-value free-text** — `"SpotInstanceRequestId sir-…, PreviousState: …"`;
3. `… Information`: **free text + a currency value** — `"…, Spot market price $0.0619"`;
4. `… Error`: **free-text config-error prose** — `"IPv6 is not supported for the instance type 'm3.large'"`.
**Provenance (resolves hub §8 doc-gap #4, partially):** the `describe-fleet-history` output (confirmed, `describe-ec2-fleet.md`) shows the launch-spec fields (`instanceType`, `image`/AMI, `availabilityZone`) are echoed into `EventDescription`/`description` **exactly as the fleet creator specified them in the launch template/spec** — so content that *influences* `description` is partly caller-controlled. **Still a doc-gap:** whether an *attacker-chosen free-text identifier* (an unusual AMI name, a tag, a crafted string) reaches `description` **un-sanitized** such that a downstream `eval`/shell/SQL consumer is injectable — the examples show only AWS-normalized values; confirm against a live canary before rating. **Severity:** Low standalone (consumer-owned); **inherits** the consumer's severity if a dangerous sink exists. **Stop condition:** the four-shape instability is demonstrated (static); do not build a consumer exploit without a real sink.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read another team's launch-spec / AMI / AZ / **Spot price** / **IAM-beacon** with no `ec2` rights | default bus + per-event `detail` (Area A) | None — push channel unscopable per-fleet; `description` never redacted on delivery |
| Capture both fleet families with one source-omitting rule | matching engine `"*":"*"` wildcard (Area B) | None — absent pattern fields are wildcarded; **no `detail.sub-type` condition key exists** |
| Default-bus reachable with identity policy alone | default event bus (Area B) | Same-account access needs no resource policy (resource policy is cross-account only) |
| Silently disable/overwrite a victim team's monitoring rule | `events:PutRule` create-or-replace (Area C) | None creator-pinned; `events:creatorAccount` is account-scoped (inert same-account) |
| Audit the bus but miss what leaked | CloudTrail data vs management events (Area D) | Mgmt events log rule setup by default; data-event `detail` = `HIDDEN_DUE_TO_SECURITY_REASONS`, off by default |
| Detection rule misses the legacy twin's events | `aws.ec2fleet` vs `aws.ec2spotfleet` (Area E) | Operator must cover both sources + the `deleted*`/`cancelled*` sub-type vocab divergence |
| Cross-account exfil of the `description` payload | rule target / `PutPermission` (hub Area 2 — pointer) | Receiver bus policy + target role (no source-scoping on delivery) |
| Confused-deputy privesc via EventBridge target | `PutTargets` + `iam:PassRole` (hub Area 3 — pointer) | `iam:PassedToService=events.amazonaws.com` scopes service not role |
| Unsafe parse of the 4-shape `description` | `detail.description` (Area G / hub Area 7) | None (unstructured, un-redacted); consumer's responsibility |

---

## 7. Out-of-Scope Risk Categories
- **The IAM-condition `ForAllValues`/`events:source` vacuous-truth bypass, cross-account exfil, `PutPermission`, EventBridge-target PassRole, and the `instant`-fleet/best-effort evasion** — owned by **`fleet-monitor-attack-research-plan.md`** (hub Areas 1/2/3/6). This plan cross-references them; it owns only the granular disclosure catalog (A), the engine-layer unscopability (B), the `PutRule`-overwrite (C), the CloudTrail asymmetry (D), and the legacy-twin coverage gap (E).
- **The entire CloudWatch `AWS/EC2Spot` metric plane** (unscopable metric reads, `PutMetricData` forgery, OAM, visibility decay) — owned by **`ec2-fleet-cloudwatch-metrics-attack-research-plan.md`**.
- **The tag-scoped pull APIs' own scopability** (`DescribeFleetHistory`, `DescribeSpotFleetRequest*`) — owned by `manage-spot-fleet` / `spot-fleet-states`. Used here only as the symmetric comparison.
- **48 h event-history forensic decay** (the page's "deleted/cancelled two days after terminate" note) and the **SLR→human CloudTrail attribution break** — owned by `spot-fleet-states` (SF-11/15).
- **The EC2-side fleet-SLR launch-time `iam:PassRole`/confused-deputy and SLR managed-policy over-grant** — owned by `spot-fleet-prerequisites` / `create-spot-fleet` / `spot-fleet-automatic-scaling`.
- **Cross-account IDOR by guessing a foreign `fleet-…`/`sfr-…`** — UUIDv4-shaped (~122-bit), not enumerable (§8).
- Shared AWS EventBridge/CloudWatch service infrastructure; bugs in a customer-written consumer Lambda; a customer steering their own account's monitoring; single-tenant self-DoS.
- **HARD STOP** on any AWS service-plane identity/account (fleet control plane, SLR acting outside the authorized account, AWS-owned event bus).

---

## 8. Null hypotheses / doc gaps

**Lenses that did not fire (pages checked named):**
- **Lens G (SSRF):** NULL — the rule *target* is a customer-chosen destination the customer configures, not a URL the EC2/EventBridge service dereferences server-side. Checked `monitor-ec2-fleet-using-eventbridge.md`, `eb-targets`-referenced flow. No service-side fetch.
- **Lens Q (upload):** NULL — no upload/blob/image field on this page.
- **Lens H (KMS/encryption context):** NULL — no key/encryption-context generated or named on this page (EventBridge/CloudWatch at-rest KMS is service-owned, out of scope).
- **Lens FF / M (token/JWT/session):** NULL — SigV4 only; no JWT/OIDC/session token in the event flow.
- **Lens P (proofing/registration):** NULL — no onboarding/verification/uniqueness gate (the rule-name uniqueness is handled as Area C integrity, not identity proofing).
- **Lens B/C (PassRole/vending), Lens R/S (IAM-artifact audit):** NULL **on this page** — the page prints no AWS-managed policy, SLR policy, or sample IAM JSON (it is a console/SDK runbook). The EventBridge-target PassRole is owned by hub Area 3; the condition-key *scoping-key-absence* finding is developed as Area B (not an artifact audit).
- **Lens EE (predictable-name land-grab):** **FIRES here as Area C** (reconciling the hub plan's EE-null) — but only in the *overwrite-existing-rule* shape, not a trust-adoption land-grab of a service-created name (that remains null — EventBridge creates no predictable-name resource the service later trusts).
- **Lens X (twin/legacy parity):** **FIRES as Area E** (`aws.ec2fleet` vs `aws.ec2spotfleet` coverage gap). The two families are otherwise identically-shaped (no divergent-validator bug beyond the sub-type vocab).
- **Lens BB/CC/DD (canonicalization / upstream-context / cache):** NULL — EventBridge pattern matching is content-filtering, not a security-decision parser split; no asserted-identity header or authz/response cache described on this page.

**Doc gaps to confirm surface first (do not rate until confirmed):**
1. **Whether an *attacker-chosen* free-text identifier reaches `detail.description` un-sanitized** (Area G indirect-injection vector). The examples show AWS-normalized launch-spec values echoed verbatim; whether a crafted string survives into `description` is unconfirmed — resolve with a self-owned canary fleet whose launch spec carries an unusual identifier, then read the emitted `description`.
2. **The engine wildcard rule's stability** — `eb-create-pattern.md` self-flags *"should not be relied on to not change."* Area B's cross-source capture is current behavior; re-verify online before a live test.
3. **`PutTargets` interaction with a `PutRule` overwrite** — confirmed additive-by-target-id and not wiped by `PutRule` per `API_PutRule`; verify live that an overwrite leaving the targets but neutering the pattern behaves as documented (Area C subtle variant).
4. **Best-effort drop rate** — "Events are emitted on a best effort basis" is unquantified; neither attacker nor defender can treat event absence as proof. Inherent limitation, not a testable bug (noted; owned framing in hub Area 6).

> **Downstream hunter note.** Priority order: **Area A + Area B** are the headline — the per-field disclosure catalog (A) delivered through the structurally-unscopable push channel (B: engine wildcard + no `detail.sub-type` condition key + identity-only default-bus gating). These are largely **static/doc-settled**; the only live step is one capture under a scoped role (no `ec2:Describe*Fleet*`) against a self-owned canary fleet, with the paired `DescribeFleetHistory` AccessDenied as the boundary proof. **Area C** (`PutRule` overwrite) is settled by `API_PutRule` + one `iam:SimulatePrincipalPolicy`; escalate to a canary-rule overwrite only in an authorized account. **Area D/E** are doc-confirmable detection-posture findings. Run all live confirmations with **two scoped roles in one authorized account + self-owned canary fleets of both `maintain` and `instant` type**, Simulate first, read-only, no foreign/production fleet ids. Defer cross-account (hub Area 2) and target-PassRole (hub Area 3) to the hub plan. **Hard stop** on any AWS service-plane identity.
