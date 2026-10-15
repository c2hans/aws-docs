# EC2 Fleet / Spot Fleet — Monitoring Surface — Attack Research Plan

**Source of leads:** AWS EC2 User Guide hub page `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-monitor.html` (title *"Monitor your EC2 Fleet or Spot Fleet"*; markdown twin `fleet-monitor.md`) and its two child topics — `ec2-fleet-cloudwatch-metrics.html` (*"Monitor your EC2 Fleet or Spot Fleet using CloudWatch"*) and `monitor-ec2-fleet-using-eventbridge.html` (*"Monitor and programmatically respond to the events emitted by your EC2 Fleet or Spot Fleet using Amazon EventBridge"*). Supporting pages: `manage-detailed-monitoring.html`, `describe-ec2-fleet.html#describe-ec2-fleet-event-history`, API Reference `API_SpotFleetMonitoring`, CloudFormation `aws-properties-ec2-spotfleet-spotfleetmonitoring`. IAM **Service Authorization Reference** `list_ec2.md`, `list_cloudwatch.md`, `list_eventbridge.md` (service prefix `events`); EventBridge User Guide `eb-use-conditions`, `eb-event-bus-perms`, `eb-cross-account`, `eb-targets`, `logging-using-cloudtrail`; CloudWatch `iam-cw-condition-keys-namespace`, `cloudwatch_concepts`, `publishingMetrics`.

**Status:** documentation-derived hypotheses only; nothing tested against a live account. All offline `.md` cross-checked against the online `.md`/`.html` twin on **2026-10-14**; no online-vs-offline drift observed on any action/condition-key cell cited here. Slug pitfalls confirmed this run: use `list_cloudwatch` (not `list_amazoncloudwatch` → 404) and `list_eventbridge` (not `list_amazoneventbridge`/`list_cloudwatchevents` → absent).

**Relationship to sibling plans (complement, do not duplicate):** This is the **hub + EventBridge-channel companion** for the EC2 Fleet & Spot Fleet family. The `fleet-monitor.html` hub has two children; one of them (`ec2-fleet-cloudwatch-metrics.html`) **already has its own dedicated plan**, so this plan owns the **net-new child: the EventBridge event stream** (`monitor-ec2-fleet-using-eventbridge.html`) plus the hub-level **two-channels integration view** and the **detection-evasion** surface. It explicitly **defers**:
- **the entire CloudWatch `AWS/EC2Spot` metric plane** — unscopable metric reads, `PutMetricData` forged-telemetry into the reserved namespace, OAM cross-account metric sharing, and the 2-week-visibility/15-month-retention detection decay — to **`ec2-fleet-cloudwatch-metrics-attack-research-plan.md`** (its M-READ / M-FORGE / M-OAM / M-DETECT). Areas 4 and 5 below are **thin pointers** that state only the *hub-integration* angle (the metric channel as the unscopable twin of the EventBridge push channel) and route all depth, oracles, and severity there — do NOT re-run them from this plan;
- the pull-side read-API scopability asymmetry of `DescribeSpotFleetRequests`/`...Instances`/`...RequestHistory` to **`manage-spot-fleet-attack-research-plan.md`** (that plan owns the describe-surface; this plan cross-references it as the *symmetric pull channel* to the push channel it owns here);
- the 48 h event-history **forensic decay** and the **SLR→human CloudTrail attribution break** (`spotFleetRequestId` purge) to **`spot-fleet-states-attack-research-plan.md`** (SF-8/11/15);
- the auto-scaling control-loop metric *consumers* (target-tracking / step / scheduled) to the three auto-scaling plans — **but this plan (via the already-confirmed cloudwatch-metrics sibling) RESOLVES their open §8 doc-gap**: Spot-Fleet metric namespace `AWS/EC2Spot` / dimension `FleetRequestId` / metric names are confirmed verbatim (see Area 4 pointer);
- the EC2-side `iam:PassRole`/SLR launch-time confused-deputy to **`spot-fleet-prerequisites`/`create-spot-fleet`** (this plan owns only the *EventBridge-target* PassRole, Area 3, which is a different deputy).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Start with the **static, no-touch** checks (`iam:SimulatePrincipalPolicy`, reading the Service Authorization Reference) before any live call. The whole monitoring surface is **read/telemetry-shaped**: there is no new mutating EC2 API here, so most leads are *information-disclosure*, *detection-evasion*, and *IAM-scopability* findings whose severity is **intra-account** unless a cross-account EventBridge target or bus policy is in play (Area 2).
- These are single-account/delegation-centric services. The classic cross-tenant IDOR path is bounded by the UUID-shaped `fleet-…` / `sfr-…` identifiers (not enumerable — see §2); do not chase cross-account reads of foreign fleet IDs you have not obtained out-of-band.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. the fleet SLR acting outside the authorized account, an AWS-owned event bus), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to achieve:
1. **Read another team's fleet operational telemetry** (target/fulfilled capacity, bid behavior, instance churn) using a principal that has *no* `ec2:Describe*Fleet*` rights, via CloudWatch metric reads or an EventBridge rule — i.e., bypass the tag-scoped pull API through an unscopable push/metric channel (Area 1, Area 4).
2. **Exfiltrate fleet launch-spec intelligence** (AMI IDs, instance types, AZs, Spot market prices, `iamFleetRoleInvalid` recon) out of the account by wiring an EventBridge rule+target on the shared default bus to an attacker-controlled destination, including **cross-account** (Area 2).
3. **Escalate privilege** by passing an over-privileged role to EventBridge through `events:PutTargets` + loosely-scoped `iam:PassRole` (Area 3).
4. **Poison / forge fleet telemetry** — publish fake `AWS/EC2Spot` metric points for a victim `FleetRequestId`, or mislead an operator/alarm (Area 5).
5. **Blind the account's fleet monitoring** — operate a fleet in a mode that emits no events, exploit best-effort delivery, or coarsen the metric fidelity an alarm depends on (Area 6).

---

## 2. Components, Assets, and Design

**What this surface is.** A read-only observability layer over EC2 Fleet (`aws.ec2fleet`) and the legacy Spot Fleet (`aws.ec2spotfleet`). It has **two delivery channels** and **one pull API**, carrying the *same* underlying fleet lifecycle data:

```
                     ┌─────────────────────────────────────────────┐
   Fleet lifecycle   │  EC2 Fleet / Spot Fleet control plane (AWS)  │
   (launch/terminate,│  state machine: submitted→active→modify→...  │
    modify, errors)  └───────┬───────────────┬──────────────┬───────┘
                             │ (metrics)      │ (events)     │ (pull)
                             ▼                ▼              ▼
                   ┌──────────────┐  ┌──────────────────┐  ┌──────────────────────┐
   CHANNEL A        │ CloudWatch   │  │ EventBridge       │  │ ec2:DescribeFleetHistory
   (metrics)        │ AWS/EC2Spot  │  │ DEFAULT event bus │  │ ec2:DescribeSpotFleet-
                    │ namespace    │  │ source=aws.ec2*   │  │   RequestHistory      │
                    └──────┬───────┘  └────────┬──────────┘  └──────────┬───────────┘
   read: GetMetric*       │ rule match        │ PutRule/PutTargets      │ (owned by
   (NO namespace/dim      │                   ▼                         │ manage-spot-fleet
    scoping — acct-wide)  │          SNS / Lambda / SQS / Kinesis /     │ + spot-fleet-states;
                          │          Step Fn / API dest / ANOTHER       │ tag-scopable:
                          ▼          event bus (same OR cross-account)   │ fleet*/spot-fleet-request*
                   operator / alarm        │ (NO detail redaction)       │ + aws:ResourceTag)
                                           ▼
                                   attacker-controlled target
```

**Assets at risk (what the channels disclose).**
- **CloudWatch metrics** (namespace **`AWS/EC2Spot`**): `AvailableInstancePoolsCount`, `BidsSubmittedForCapacity`, `EligibleInstancePoolCount`, `FulfilledCapacity`, `MaxPercentCapacityAllocation`, `PendingCapacity`, `PercentCapacityAllocation`, `TargetCapacity`, `TerminatingCapacity`. **Dimensions: `AvailabilityZone`, `FleetRequestId`, `InstanceType`.** → operational intelligence: how big a workload is, where it runs, its bidding posture, when it scales. *(This verbatim confirmation resolves the `spot-fleet-automatic-scaling` plan §8 "metrics unverified" doc-gap: namespace `AWS/EC2Spot`, dimension `FleetRequestId`, metric names as listed.)*
- **EventBridge events** (`detail-type` set: `EC2 Fleet State Change`, `EC2 Fleet Spot Instance Request Change`, `EC2 Fleet Instance Change`, `EC2 Fleet Information`, `EC2 Fleet Error`, plus the `EC2 Spot Fleet …` quintet): each event carries `account`, `region`, the **fleet ARN** (`arn:aws:ec2:…:fleet/fleet-…` or `…:spot-fleet-request/sfr-…`), `instance-id` (`i-…`), `spot-instance-request-id` (`sir-…`), and a free-text **`detail.description`** that embeds launch-spec JSON — e.g. `"{\"instanceType\":\"c5.large\",\"image\":\"ami-6057e21a\",\"productDescription\":\"Linux/UNIX\",\"availabilityZone\":\"us-east-1d\"}"` — plus **Spot market prices** and error strings including **`iamFleetRoleInvalid`** ("does not have the required permissions to either launch or terminate an instance" → a direct IAM-misconfiguration recon beacon).
- **`SpotFleetMonitoring.Enabled`** (`API_SpotFleetMonitoring`, CFN `AWS::EC2::SpotFleet SpotFleetMonitoring`): Boolean, **default `false`**, toggles per-instance detailed (1-min) monitoring. Not an IAM-scopable field of its own (see §3).

**Identity establishment.** All three channels are IAM/SigV4. There is no separate data-plane credential here. The EventBridge rules invoke targets under either the EventBridge service principal (`events.amazonaws.com`) or a customer-supplied `RoleArn` (Area 3).

**Resource identifiers.** EC2 Fleet: `fleet-` + UUIDv4-shaped (`fleet-598fb973-87b7-422d-be4d-6b0809bfff0a`) → ~122-bit, **not enumerable**. Spot Fleet: `sfr-` + UUIDv4-shaped → not enumerable. `FleetRequestId` dimension value = the `fleet-…`/`sfr-…` id. These high-entropy ids are the *reason* cross-account IDOR is near-null here (§8) and *also* the pivot a hunter needs: anyone who obtains a foreign fleet id out-of-band (shared config, a leaked event, a dashboard screenshot) can then read its CloudWatch metrics with no further authz (Area 4).

**Trust zones.** Customer account (operator identities, the default event bus, the account's CloudWatch metric store) ↔ **another AWS account** (cross-account EventBridge target / bus — the only cross-tenant seam this surface opens) ↔ AWS service plane (the fleet control plane and SLR — hard stop).

**Mandatory coverage sweep — pages checked for each lens trigger:** read `fleet-monitor.md`, `ec2-fleet-cloudwatch-metrics.md`, `monitor-ec2-fleet-using-eventbridge.md` (all 674 lines incl. every event example + sub-type), `manage-detailed-monitoring.md`, `describe-ec2-fleet.md` (event-history section), `API_SpotFleetMonitoring.md`, the CFN `SpotFleetMonitoring` property, and the three Service Authorization Reference files. **No field on this surface is a server-side-dereferenced URL** (→ Lens G null), **no upload/blob field** (→ Lens Q null), **no KMS/encryption-context** (→ Lens H null), **no JWT/token validation** (→ Lens FF null), **no registration/proofing gate** (→ Lens P null). Enumerated null hypotheses with their checked pages in §8.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| In-account principal **without** `ec2:Describe*Fleet*` on a fleet's tag | Another team's fleet lifecycle data | `events:PutRule` on the **default** bus matching `aws.ec2fleet`/`aws.ec2spotfleet` (or omitting `source`) + `PutTargets` to a target it reads | A rule the principal owns delivers *another team's* fleet events to a destination it controls, where the tag-scoped `DescribeFleetHistory` would have denied it → **boundary breach (intra-account observability bypass)** |
| In-account principal without fleet-describe rights | Another team's fleet capacity/bid metrics | `cloudwatch:GetMetricStatistics`/`GetMetricData`/`ListMetrics` on `AWS/EC2Spot` filtered by a known `FleetRequestId` | Metric datapoints returned for a `FleetRequestId` the caller has no `ec2` rights over → **boundary breach (unscopable metric read)** |
| In-account attacker | **Another AWS account** | `events:PutPermission` on default bus / rule target = cross-account SQS/SNS/event-bus | Fleet events (with leaky `description`) arrive in a foreign account → **cross-account exfiltration breach** |
| Principal with `events:PutTargets` + loose `iam:PassRole` | Any EC2-trusting/over-privileged role | Pass `RoleArn` to EventBridge; EventBridge assumes it to invoke target | EventBridge performs an action under a role the caller could not assume directly → **confused-deputy / privesc breach** |
| Attacker publishing custom metrics | A victim fleet's dashboards/alarms | `cloudwatch:PutMetricData` into `AWS/EC2Spot` with a victim `FleetRequestId` dimension | A forged datapoint appears under the victim's fleet dimension / an alarm or operator is misled → **telemetry-integrity breach** |
| Attacker wanting to avoid detection | The account's security automation | Run `instant`-type fleet (no events) / exploit best-effort drop / `UnmonitorInstances` | A fleet lifecycle action that produces **no** EventBridge event or coarsened metrics → **monitoring-evasion breach** |
| Any customer surface | AWS service plane (fleet control plane, SLR, AWS-owned bus) | — | Any AWS-owned identity/ARN/account observed → **HARD STOP, disclose** |

---

## 4. API / Interface Inventory

| Name | Method | Mut? | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `cloudwatch:GetMetricStatistics` | SDK | No | External | Read `AWS/EC2Spot` datapoints | Yes | Any principal w/ the action | **Blank resource type, NO condition keys** → cannot scope to namespace/`FleetRequestId`. Account/region-wide. |
| `cloudwatch:GetMetricData` / `ListMetrics` | SDK | No | External | Read/enumerate metrics | Yes | Any principal | Optional `dataset` resource (CW-Omni, unrelated) + `aws:ResourceTag`/`cloudwatch:HasAccessGrant`; **no namespace/dimension key**. |
| `cloudwatch:PutMetricData` | SDK | **Yes** | External | Publish custom metric points | Yes | Any principal | Scopable only by `cloudwatch:namespace` (write). `AWS/EC2Spot` **not documented as API-blocked** (naming convention only) → Area 5. |
| `cloudwatch:PutMetricAlarm` / `DeleteAlarms` / `SetAlarmState` / `Disable/EnableAlarmActions` | SDK | Yes | External | Manage alarms over the metrics | Yes | Any principal | Scopable by `alarm*` ARN + `aws:ResourceTag` **only** — *not* by which metric/namespace the alarm watches. `cloudwatch:AlarmActions` on `PutMetricAlarm`. |
| `events:PutRule` | SDK | Yes | External | Create a rule on an event bus | Yes | Any principal | Resource `rule-on-default-event-bus`/`rule-on-custom-event-bus`. Keys incl. `events:source`, `events:detail-type` — **source-scoping bypassable** (Area 1). |
| `events:PutTargets` | SDK | Yes | External | Wire targets to a rule | Yes | Any principal | `events:TargetArn` (unrestricted by default) + `iam:PassRole`(`PassedToService=events.amazonaws.com`) → Area 3. |
| `events:PutPermission` | SDK | Yes | External | Grant another account access to default bus | Yes | Any principal | **Blank resource type, blank condition keys** → unconditioned cross-account grant (Area 2). |
| `ec2:DescribeFleetHistory` | SDK | No | External | Pull EC2 Fleet event history | Yes | Owner (tag-scoped) | Resource `fleet*` **required**; keys `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region` → **tag-scopable** (the symmetric pull channel vs the unscopable push channel). |
| `ec2:DescribeSpotFleetRequestHistory` | SDK | No | External | Pull Spot Fleet event history | Yes | Owner (tag-scoped) | Resource `spot-fleet-request*` **required** + same tag keys. (Owned by `manage-spot-fleet`/`spot-fleet-states`.) |
| `ec2:MonitorInstances` / `ec2:UnmonitorInstances` | SDK | **Yes** | External | Toggle detailed (1-min) monitoring per instance | Yes | Any principal w/ action | Resource `instance*` + `aws:ResourceTag`/`ec2:ResourceTag` + rich instance-attr keys. **Tag-scopable** footgun → Area 6. No fleet-level/`SpotFleetRequestId` key. |
| `SpotFleetMonitoring.Enabled` (field on `RequestSpotFleet`/CFN) | field | — | — | Enable detailed monitoring on fleet-launched instances | — | — | Boolean, default `false`; **no dedicated IAM action/condition key** (grep of `list_ec2` for "monitoring" finds only Monitor/Unmonitor + unrelated Capacity Manager). |

**Undocumented / console-hidden knob check.** No `authorizerType:"NONE"`-class hidden auth-weakening knob on this read surface. The one notable console-vs-API delta: the CloudWatch console only surfaces the `EC2 Spot` namespace groupings and will *hide the namespace entirely* if the account hasn't used a fleet in the Region for two weeks (`ec2-fleet-cloudwatch-metrics.md` note) — but the **API** (`GetMetricStatistics`/`ListMetrics`) has no such Region/recency gate and no owner filter, so the SDK path is the superset. The `SpotFleetMonitoring.Enabled` Boolean is API/CFN-exposed; the console exposes it only as the launch-time "Detailed CloudWatch monitoring" checkbox.

---

## 5. Recommended Areas of Focus

### Area 1 — EventBridge default-bus capture: the unscopable push channel vs the tag-scoped pull channel (headline)
**Background.** Fleet lifecycle data is readable two ways: the **pull API** `ec2:DescribeFleetHistory` (requires resource `fleet*`, supports `aws:ResourceTag`/`ec2:ResourceTag` → an admin *can* ABAC-restrict a team to its own fleets) and the **push channel** — the same events land on the account's **default event bus** with `source: aws.ec2fleet` / `aws.ec2spotfleet`. Any principal that can create a rule+target on the default bus can siphon that stream.

**Security Concern.** The default bus has **no per-team / per-source partitioning**. IAM *can* restrict which `source`/`detail-type` a principal may build a rule for via the `events:source` / `events:detail-type` condition keys on `events:PutRule` — **but the naive policy form is bypassable.** The EventBridge guide's own example `"ForAllValues:StringEquals": {"events:source": "aws.ec2"}` is a **vacuous-truth allow**: `ForAllValues` returns `true` over an empty set, so a principal who simply **omits `source` from the rule's event pattern** (keying only on `detail-type` or `detail.*`) skips the condition entirely — unless the policy *also* carries `"Null": {"events:source": "false"}` to force the key present. Most sample/managed policies omit the `Null` guard. This is the Lens S "`ForAllValues:*` vacuous-truth" variant, confirmed live in the EventBridge docs.

**High-level Test Scenarios.**
- **Claim:** A principal holding only `events:PutRule`/`events:PutTargets` (no `ec2:Describe*Fleet*`, no fleet tag) can capture another team's `EC2 Fleet Instance Change` / `State Change` events on the default bus. **Oracle:** create a rule with pattern `{"detail-type":["EC2 Fleet Instance Change"]}` (no `source`) + a target (an SQS queue the principal reads); observe a foreign fleet's `instance-id`/launch-spec `description` arriving. Compare to `DescribeFleetHistory` on the same `fleet-…` returning `AccessDenied` under the same principal → proves the push channel bypasses the pull channel's tag scope.
- **Claim:** An `events:source="aws.ec2fleet"`-scoped `PutRule` policy *without* the `Null` guard is bypassable. **Oracle:** `iam:SimulateCustomPolicy` (no resources touched) with a candidate rule that omits `source` → `allowed`; then with `source` present → still `allowed`; demonstrating the restriction is inert against the source-omitting pattern.
- Look left/right: a rule keyed on `detail.sub-type` (`launched`/`terminated`) alone gives an attacker a per-instance churn feed of every fleet in the account.

**Doc evidence.** `monitor-ec2-fleet-using-eventbridge.md` (default bus, `source`/`detail-type` fields, full event examples); `list_eventbridge.md` `events:PutRule` row (`events:source`/`events:detail-type` keys); `eb-use-conditions.html` (the `ForAllValues` example + the `Null`-guard caveat); `list_ec2.md` `DescribeFleetHistory` row (resource `fleet*` + tag keys). **Severity-if-true:** **Medium–High** intra-account (cross-team observability / least-privilege-ceiling bypass; High where ABAC on fleets is the account's sole team-isolation mechanism). **Owner-to-fix:** shared — AWS owns the vacuous-truth condition-evaluation semantics and the bypassable sample policy; the customer owns adding the `Null` guard. **Stop condition:** once the simulate delta (source-omitting pattern allowed; pull-API denied) is shown, the boundary verdict is settled — do not enumerate every detail-type.

### Area 2 — Cross-account exfiltration of fleet launch-spec intelligence via rule target / bus policy
**Background.** EventBridge rule targets include **another event bus in a different account**, and cross-account SQS/SNS/Lambda. `events:PutPermission` grants another account access to your **default** bus (and, if written broadly, lets that account `PutRule`/`PutTargets` directly on your bus). EventBridge **never redacts `detail`** — the fleet `description` (AMI IDs, instance types, AZs, Spot market prices, `iamFleetRoleInvalid`) flows verbatim to whatever target a rule points at.

**Security Concern.** No condition key scopes cross-account *delivery* by event `source`. `events:creatorAccount` only scopes which rules a principal may *manage*, not where events go. So an in-account attacker (or an over-broad `PutPermission` grant) can forward the account's entire fleet event stream — including launch-spec and IAM-misconfig recon — into a foreign account, gated only by the receiver's bus resource policy + (post-2023-03) a target IAM role.

**High-level Test Scenarios.**
- **Claim:** Fleet events can be forwarded to an attacker-controlled account. **Oracle:** rule on default bus (pattern matching `aws.ec2fleet`) → target = cross-account event bus / SQS the attacker controls; confirm the leaky `description` arrives in the foreign account. (In an authorized two-account test only.)
- **Claim:** `events:PutPermission` with no condition lets an external account operate on the default bus. **Oracle:** inspect/simulate a default-bus resource policy that names an external principal with `events:PutRule`/`PutTargets` → external account creates a capturing rule directly.
- **Claim:** The `iamFleetRoleInvalid` / `spotFleetRequestConfigurationInvalid` error events are a usable IAM-recon beacon. **Oracle:** confirm these sub-types carry the misconfiguration description to any rule target (they do, per the event examples) → an attacker learns which fleets have broken/limited roles.

**Doc evidence.** `eb-cross-account.html`, `eb-event-bus-perms.html` (`PutPermission` scope), `list_eventbridge.md` (`events:PutPermission` blank resource/condition), `monitor-ec2-fleet-using-eventbridge.md` (the five event examples with `description`), `logging-using-cloudtrail.md` (confirms redaction is CloudTrail-data-event-only, **not** delivery). **Severity-if-true:** **Medium–High** (cross-account exfiltration of workload intelligence; not credentials, so not Critical by itself, but a strong recon primitive — raise if `description` ever carries a secret). **Owner-to-fix:** customer (bus policy / target) + AWS (the unconditioned `PutPermission` default and the no-source-scoping on delivery). **Stop condition:** one confirmed cross-account arrival of a `description` field; do not iterate targets.

### Area 3 — EventBridge-target PassRole confused deputy
**Background.** `events:PutTargets` is paired with `iam:PassRole` gated only by `iam:PassedToService=events.amazonaws.com` — which constrains the *service* the role is passed to, **not which role**. Targets that assume a role (event bus, SQS, Kinesis, Step Functions, API destinations, ECS, SSM Run Command) run under that passed role.

**Security Concern.** If the operator's `iam:PassRole` is not scoped to specific role ARNs, a principal with `events:PutTargets` can pass an **over-privileged** EC2/EventBridge-trusting role and have EventBridge assume it to invoke a target of the attacker's choosing → privilege escalation / lateral action under a role the caller could not assume directly. This is distinct from the EC2-side fleet-SLR PassRole owned by `spot-fleet-prerequisites`/`create-spot-fleet`; here the deputy is **EventBridge**, reached through the monitoring workflow this page tells operators to build.

**High-level Test Scenarios.**
- **Claim:** `events:PutTargets` + `iam:PassRole` on `*` lets a low-priv principal make EventBridge act as a high-priv role. **Oracle:** `iam:SimulatePrincipalPolicy` for `events:PutTargets` + `iam:PassRole` on a privileged role ARN with `iam:PassedToService=events.amazonaws.com` → `allowed`; then (authorized live) wire a rule→SSM-Run-Command/Step-Functions target under that role and observe the action execute under the passed role's identity.
- Chain into Area 2: the passed role could be the target that forwards events cross-account.

**Doc evidence.** `list_eventbridge.md` `PutTargets` API-operations row (`iam:PassRole` / `iam:PassedToService=events.amazonaws.com`), `eb-targets.html` (role-assuming targets + the `events.amazonaws.com` trust policy). **Severity-if-true:** **High** (non-admin → broader action via confused deputy) if `PassRole` is unscoped; else N/A. **Owner-to-fix:** customer (scope `PassRole` to specific role ARNs) — a footgun unless AWS sample policy over-grants it (check the monitoring runbook/sample policies). **Stop condition:** the simulate `allowed` + one observed action under the passed role.

### Area 4 — [POINTER] CloudWatch `AWS/EC2Spot` metric read is structurally unscopable
**This is a cross-reference, not an owned lead.** The CloudWatch metric channel — the *second* child of the `fleet-monitor` hub — is owned in full by **`ec2-fleet-cloudwatch-metrics-attack-research-plan.md` (lead M-READ)**. That plan already confirmed: the CloudWatch read actions (`GetMetricStatistics`/`DescribeAlarmsForMetric` blank resource+condition cells; `ListMetrics`/`GetMetricData` only `dataset`+`cloudwatch:HasAccessGrant`) carry **no namespace/dimension condition key**, so any principal with a read action can pull **every** fleet's `TargetCapacity`/`FulfilledCapacity`/`BidsSubmittedForCapacity`/pool-counts account/region-wide filtered by any known `FleetRequestId`, even with `ec2:DescribeSpotFleetRequests` denied — the CloudWatch twin of `manage-spot-fleet`'s unscopable Describe oracle.

**Hub-integration angle this plan contributes (the only net-new framing):** the metric channel is the **unscopable READ twin of the EventBridge push channel (Area 1)**. A hunter working the hub should run them *together* — a principal denied the tag-scoped pull API (`DescribeFleetHistory`) can reach the *same* fleet's lifecycle+capacity picture through **two** independent unscopable channels (EventBridge default-bus capture **and** CloudWatch metric read). That dual-bypass is the hub-level headline; the per-channel depth, oracles, and severity live in Area 1 (here) and M-READ (cloudwatch-metrics plan) respectively.

**Also:** this confirms the Spot-Fleet metric strings (`AWS/EC2Spot`, dim `FleetRequestId`) that resolve the `spot-fleet-automatic-scaling` §8 gap — see the cloudwatch-metrics plan for the verbatim table. **Do not re-run M-READ from this plan.**

### Area 5 — [POINTER] Forged `AWS/EC2Spot` telemetry via `PutMetricData`
**This is a cross-reference, not an owned lead.** Owned in full by **`ec2-fleet-cloudwatch-metrics-attack-research-plan.md` (lead M-FORGE)**, including the pivotal doc-gap (no AWS doc states customers are blocked from writing into the `AWS/`-reserved namespace; `AWS/{service}` is only a convention per `cloudwatch_concepts`/`publishingMetrics`) and the canary round-trip test (`put-metric-data --namespace AWS/EC2Spot` on a self-owned `FleetRequestId`, then read back) as that plan's step-1.

**Hub-integration angle this plan contributes:** a forged-metric write chains into **Area 6** here — if an attacker both suppresses the genuine EventBridge/metric signal (instant fleets, best-effort drop, `UnmonitorInstances`) *and* publishes a plausible forged `AWS/EC2Spot` point, the account's dashboards show a fabricated-but-healthy picture while the real fleet activity is invisible. The write primitive is M-FORGE's; the detection-blinding half is Area 6's; the combination is the hub-level deception scenario. **Do not re-run M-FORGE from this plan.**

### Area 6 — Monitoring / detection evasion (coverage gaps the docs state outright)
**Background.** The EventBridge page states three evasion-relevant facts verbatim: (1) **"Events are emitted on a best effort basis"** → silent drops are expected, not errors. (2) **"Only fleets of type `maintain` and `request` emit events. Fleets of type `instant` do not emit events"** → an `instant` fleet performs its launch/terminate with **zero** EventBridge signal. (3) Detailed monitoring is **off by default** (`SpotFleetMonitoring.Enabled=false`; basic = 5-min periods), and `ec2:UnmonitorInstances` turns it off per instance.

**Security Concern.** Security automation built on the fleet EventBridge stream has documented blind spots an attacker can live inside: run workloads as **`instant`** fleets to avoid lifecycle events entirely; rely on **best-effort** drops; or call **`UnmonitorInstances`** (tag-scopable, but if the attacker's instances carry a tag it's granted on) to coarsen the metric fidelity the account's `AWS/EC2Spot` alarms depend on. None of these produce a fleet event; the detective control simply doesn't fire.

**High-level Test Scenarios.**
- **Claim:** An `instant`-type fleet's launches/terminations generate no `EC2 Fleet Instance Change` events. **Oracle:** create an `instant` fleet (self-owned canary), subscribe a catch-all rule → confirm no `aws.ec2fleet` events emitted (vs a `maintain` fleet that does). Read-only wrt other tenants.
- **Claim:** `UnmonitorInstances` degrades alarm fidelity. **Oracle:** confirm `list_ec2` scoping (`instance*` + `aws:ResourceTag`) and that toggling off drops `AWS/EC2Spot`/instance metrics from 1-min to 5-min → an alarm with a short evaluation period loses resolution. Enabler, not a standalone breach.
- **Claim:** The control actions are logged even when the data channel is blind. **Oracle:** confirm `PutRule`/`PutTargets`/`PutPermission`/`MonitorInstances`/`UnmonitorInstances` are CloudTrail **management** events (logged by default) → the *setup* of an evasion/exfil rule is auditable even though `PutEvents` data events (the event bodies, `detail` redacted) are off by default. This bounds the evasion: a defender watching CloudTrail management events still sees the rule being created.

**Doc evidence.** `monitor-ec2-fleet-using-eventbridge.md` ("best effort", the `instant`/`maintain`/`request` note); `manage-detailed-monitoring.md` (basic vs detailed periods, `Monitor/UnmonitorInstances` permissions); `ec2-fleet-cloudwatch-metrics.md` ("recommend you enable detailed monitoring … to ensure accuracy"); `logging-using-cloudtrail.md` (management vs data events; `detail` redacted in data events as `HIDDEN_DUE_TO_SECURITY_REASONS`). **Severity-if-true:** **Low–Informational** (detection-evasion enabler; raises the severity of any paired action). **Owner-to-fix:** customer (don't depend solely on fleet events; monitor CloudTrail management events). **Stop condition:** confirm the `instant`-no-event behavior and the management-event logging of rule setup.

### Area 7 — Event `detail.description` parsing differential (nested-JSON-string / free-text)
**Background.** The `EC2 Fleet Instance Change` event serializes the launch spec as a **JSON string nested inside the `description` string field**: `"description": "{\"instanceType\":\"c5.large\",\"image\":\"ami-6057e21a\",...}"`. Other sub-types put **free text** (with embedded Spot prices and AMI IDs) in the same `description` field.

**Security Concern.** A downstream consumer (the Lambda the page tells operators to wire up) that naively parses `description` — `JSON.parse` on a string-in-string, regex-extracts a price, or string-concatenates it into a query/command — hits a parsing-differential / injection seam. Content that *influences* `description` is partly caller-controlled (instance types, AMI IDs chosen in the launch spec); if an attacker can get crafted bytes into a field that lands in `description`, and a privileged consumer interprets it, that is indirect injection into the automation. The consumer is customer-owned (so mostly a customer footgun), but the **AWS-shaped quirk** — AWS emitting a structured object as an escaped string inside a string, with no schema/redaction — is worth flagging because it predictably induces unsafe parsing.

**High-level Test Scenarios.**
- **Claim:** `description` is unstructured/escaped and not schema-stable across sub-types. **Oracle:** diff the `description` shape across `launched` (nested JSON), `launchSpecUnusable` (free text + price), `spotFleetRequestConfigurationInvalid` (free text) → confirm no single parse is safe; a consumer must branch on sub-type. (Pure doc analysis.)
- **Claim (indirect-injection, consumer-dependent):** attacker-chosen launch-spec strings reach `description` verbatim. **Oracle:** inspect whether any caller-settable launch-spec string (e.g. an unusual instance-type/AMI identifier) appears un-sanitized in the emitted `description` → if a downstream `eval`/shell/query consumer exists, this is the delivery vector (chain to Lens F/K on the consumer). Severity = the consumer's, not this field's.

**Doc evidence.** `monitor-ec2-fleet-using-eventbridge.md` (the `description` examples across all five sub-types); subagent-confirmed: EventBridge does not sanitize/redact `detail`. **Severity-if-true:** **Low** standalone (customer-owned consumer); **inherits** the consumer's severity if a dangerous sink exists. **Owner-to-fix:** customer (parse defensively) + AWS (doc the field as untyped/escaped). **Stop condition:** the schema-instability demonstration; do not build a consumer exploit without a real sink.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Capture another team's fleet events on the shared default bus | EventBridge `PutRule`/default bus | `events:source`/`events:detail-type` conditions — **bypassable without the `Null` guard** (vacuous-truth) |
| Read any fleet's capacity metrics with no EC2 rights | CloudWatch `AWS/EC2Spot` reads | None — read actions have no namespace/dimension condition key |
| Cross-account exfil of launch-spec intel via rule target / `PutPermission` | EventBridge targets / bus policy | Receiver bus resource policy + target IAM role (no source-scoping condition on delivery; `detail` never redacted in delivery) |
| Confused-deputy privesc via EventBridge target | `PutTargets` + `iam:PassRole` | `iam:PassedToService=events.amazonaws.com` (scopes service, not role) + optional `events:TargetArn` |
| Forge `AWS/EC2Spot` datapoints for a victim fleet | CloudWatch `PutMetricData` | `cloudwatch:namespace` (write); `AWS/*` reservation is convention-only — **confirm runtime block** |
| Evade fleet-event detection | `instant` fleet / best-effort / `UnmonitorInstances` | CloudTrail management-event logging of rule/monitor setup (data-event bodies off by default, `detail` redacted) |
| Unsafe parse of `description` nested-JSON-string | EventBridge `detail.description` | None (unstructured, un-redacted); consumer's responsibility |

---

## 7. Out-of-Scope Risk Categories
- **The tag-scoped pull APIs themselves** (`DescribeFleetHistory`, `DescribeSpotFleetRequests/Instances/RequestHistory`) — owned by `manage-spot-fleet-attack-research-plan.md` and `spot-fleet-states-attack-research-plan.md`. This plan only uses them as the *symmetric comparison* for the push/metric channels.
- **48 h event-history forensic decay and the SLR→human CloudTrail attribution break** — owned by `spot-fleet-states` (SF-11/15).
- **The fleet SLR launch-time `iam:PassRole`/confused-deputy and the SLR managed-policy over-grant** — owned by `spot-fleet-prerequisites`/`create-spot-fleet`/`spot-fleet-automatic-scaling`. (This plan owns only the *EventBridge-target* PassRole, Area 3.)
- **Auto-scaling control-loop consumers** of these metrics (target-tracking / step / scheduled alarms) — owned by the three auto-scaling plans. This plan supplies the confirmed metric strings they needed.
- **Cross-account IDOR by guessing a foreign `fleet-…`/`sfr-…`** — the ids are UUIDv4-shaped (~122-bit), not enumerable; not a practical path (see §8). A hunter who obtains a foreign id out-of-band should pivot it into Area 4 (metric read), not brute-force it.
- Shared AWS CloudWatch/EventBridge service infrastructure; IMDS on managed hosts; single-tenant self-DoS; a customer steering their own monitoring automation; bugs in customer-written consumer Lambdas.
- **HARD STOP** on any AWS service-plane identity/account (fleet control plane, SLR acting outside the authorized account, AWS-owned event bus).

---

## 8. Null hypotheses / doc gaps

**Lenses that did not fire (pages checked named):**
- **Lens G (SSRF):** NULL — checked `fleet-monitor.md`, both child pages, `manage-detailed-monitoring.md`, `API_SpotFleetMonitoring`. No field on this surface is a URL/host the service dereferences; the only "fetch" is CloudWatch reading its own metric store. (The EventBridge *target* is a destination the customer configures, not a service-side SSRF.)
- **Lens Q (upload):** NULL — no upload/blob/image/attachment field anywhere on the monitoring surface.
- **Lens H (KMS/encryption-context):** NULL — this surface generates/stores no key or encryption context. (CloudWatch/EventBridge data-at-rest KMS is out of scope and service-owned.)
- **Lens FF / M (token/JWT/session):** NULL — all three channels are SigV4; no JWT/OIDC/session token in the monitoring flow.
- **Lens P (proofing/registration):** NULL — no onboarding/verification/uniqueness gate.
- **Lens W (attestation):** NULL — no attestation condition.
- **Lens BB/CC/DD (canonicalization / upstream-context / cache):** NULL for the EC2 docs themselves — no multi-parser request path, asserted-identity header, or authz/response caching described on this surface. (EventBridge rule-pattern matching is content-filtering, not a security-decision/execution parser split.)
- **Lens EE (predictable-name land-grab):** NULL on the EC2 side — no service-created predictable-name resource here. (EventBridge *rule names* must be unique per Region/bus, but that is a naming-collision/DoS at most, not a trust-adoption land-grab; the attacker-rule in Area 1 is a *capture*, not a name-squat.)
- **Lens X (twin/legacy parity):** PARTIAL/covered — the push-vs-pull parity gap (unscopable EventBridge delivery vs tag-scoped `DescribeFleetHistory`) is developed as Area 1; `aws.ec2spotfleet` is the legacy twin of `aws.ec2fleet` and emits an identically-shaped (separately-named) event set, so no divergent-validator parity bug between them beyond the shared Area 1 gap.

**Doc gaps to confirm surface first (do not rate until confirmed):**
1. **Does CloudWatch reject `PutMetricData` into the `AWS/EC2Spot` namespace at runtime?** The docs call `AWS/` a convention with only syntactic validation; whether a runtime guard blocks customer writes to AWS-reserved namespaces is undocumented. Area 5 is gated on this — resolve with a self-owned canary round-trip before rating.
2. **Default-bus resource policy default state.** Whether the account's default bus already permits any in-account principal to `PutRule`/`PutTargets` without an explicit grant (the common case) vs requiring one — determines how much of Area 1/2 is reachable with a bare `events:*` identity policy. Confirm against the account's actual bus policy.
3. **Cross-account event-bus-to-bus delivery of a `scalingPolicy`/fleet event** post-2023-03 role requirement — confirmed supported in docs; the *exact* receiver-side controls (resource policy + role) should be verified in a two-account authorized test before rating Area 2 severity.
4. **Whether any caller-settable launch-spec string reaches `detail.description` un-sanitized** (Area 7 indirect-injection vector) — the examples show AWS-chosen fields; confirm whether an unusual instance-type/AMI identifier is echoed verbatim.
5. **Best-effort drop rate / conditions** — "best effort" is unquantified; a hunter cannot rely on event absence as proof, and a defender cannot rely on event presence. Noted as an inherent limitation, not a testable bug.

> **Downstream hunter note.** Start with the **static, no-touch** checks: Area 1 (`iam:SimulateCustomPolicy` on the source-omitting `PutRule` pattern — the vacuous-truth bypass), Area 3 (`iam:SimulatePrincipalPolicy` on `PutTargets`+`PassRole`), and Area 4 (confirm no `cloudwatch:namespace`/dimension key on the read actions → inert-ABAC) — all confirmable before any live call. The headline is **Area 1 + Area 4**: the push channel (EventBridge default bus) and the metric channel (CloudWatch reads) are both **unscopable per-fleet**, so a principal with no `ec2:Describe*Fleet*` and no fleet tag can still read any team's fleet lifecycle + capacity data — bypassing the tag-scoped pull API the account relies on for team isolation. Run the live confirmations with **two scoped roles in one authorized account + a self-owned canary fleet**, Simulate first, read-only, no foreign/production dimensions. Resolve the §8 doc-gaps (AWS-namespace writability; default-bus policy; cross-account target controls) before escalating severity. **Hard stop** on any AWS service-plane identity.
