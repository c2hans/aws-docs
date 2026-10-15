# EC2 Fleet / Spot Fleet CloudWatch Metrics — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-cloudwatch-metrics.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-fleet-cloudwatch-metrics.md`, confirmed byte-equivalent to online). Supporting pages: `viewing_metrics_with_cloudwatch.html` (EC2 instance metrics / `AWS/EC2` namespace), the IAM **Service Authorization Reference** `list_cloudwatch.html` + `list_oam.html`, CloudWatch User Guide `cloudwatch_concepts.html` / `publishingMetrics.html` / `iam-cw-condition-keys-namespace.html` / `CloudWatch-Unified-Cross-Account.html`. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **This is the observability/metrics-plane companion** in the EC2-Fleet / Spot-Fleet plan family. It owns exactly one surface the control-plane siblings deliberately left open: the `AWS/EC2Spot` fleet-published CloudWatch metrics as (a) a **read/info-disclosure oracle** and (b) a **forgeable integrity sink**, plus the **cross-account OAM** metric-sharing path and the **detection blind-spots** of CloudWatch metric visibility. It defers the entire auto-scaling *control loop* (alarm→policy→`ModifySpotFleetRequest`) and all EC2-side IAM to its siblings and cross-references them precisely (see "Relationship to sibling plans" at the end of §0).

---

## 0. How to use this document

- Each lead below is: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs the plan did not anticipate.
- Every oracle is runnable **intra-account with two scoped IAM roles in a single authorized test account** (a reader role and a publisher role), plus — for the cross-account lead only — a second authorized account to stand up the OAM link. Use `iam:SimulatePrincipalPolicy` as the first (resource-touchless) oracle wherever a lead is about what a scoped principal is *allowed* to do.
- Use **synthetic canary fleets** you create and tear down. Never read, publish against, or enumerate a fleet you do not own in an account you are not authorized to test.
- **HARD STOP:** the moment any evidence shows an identity / credential / ARN / account belonging to **AWS's own service plane** (e.g. the metric-publishing identity behind `AWS/EC2Spot` turns out to be an AWS-fleet principal you can reach or impersonate), stop, preserve evidence, and flag for AWS-Security disclosure. Do not escalate.
- **Time budget:** this is a thin, well-bounded surface. The two headline leads (M-READ, M-FORGE) are confirmable in a short session. If runtime approaches the hard limit, emit findings collected so far and stop.

**Relationship to sibling plans (read these for the parts this plan defers):**
- Auto-scaling control loop (alarm→policy→terminate), SLR `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy`, foreign-fleet terminate → `spot-fleet-automatic-scaling-attack-research-plan.md` (A1/S1/L2) and `spot-fleet-target-tracking-attack-research-plan.md` (**TT3** = unconstrained-custom-metric capacity steering).
- The Describe-side read oracle (config/`iamFleetRole`/launch-spec disclosure) → `manage-spot-fleet-attack-research-plan.md`. **This plan is the metrics twin of that read oracle** — same "unscopable account-wide read" shape, different data plane (CloudWatch time-series vs the EC2 Describe API).
- Operator sample policy granting `cloudwatch:*` on `"*"` → `spot-fleet-auto-scaling-IAM-attack-research-plan.md` (R2) and `spot-fleet-step-scaling-attack-research-plan.md` (SS1, the `SetAlarmState`/alarm-action trust chain). This plan does **not** re-audit those alarm/policy artifacts; it covers only the metric-data plane feeding them.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Read fleet operational posture you were never granted on the EC2 side.** From a principal holding only account-wide CloudWatch read (`cloudwatch:GetMetricStatistics`/`GetMetricData`/`ListMetrics`) and **explicitly denied `ec2:DescribeSpotFleetRequests`/`DescribeFleets`**, recover another team's fleet request IDs and their `TargetCapacity` / `FulfilledCapacity` / `PendingCapacity` / `TerminatingCapacity` / `BidsSubmittedForCapacity` / pool-count time-series — proving the metrics plane leaks fleet inventory and scaling/bidding strategy that the EC2 control-plane read was supposed to gate.
2. **Forge the fleet's own signal.** From a principal holding only `cloudwatch:PutMetricData` with no namespace condition, publish fabricated data points into `AWS/EC2Spot` with a victim fleet's `FleetRequestId` dimension — corrupting the owner's dashboards, alarms, and any auto-scaling policy that reads that namespace, with **no `ec2:*` and no `application-autoscaling:*`**.
3. **Cross-account metric exposure via OAM.** Prove whether a CloudWatch Observability-Access-Manager link configured to share "all namespaces" (or a namespace set that includes `AWS/EC2Spot`) exposes a source account's fleet posture to a monitoring account, and whether the IAM layer can scope that to exclude `AWS/EC2Spot`.
4. **Detection blind-spot.** Demonstrate the gap between 15-month metric *retention* and 2-week *ListMetrics/console visibility* so a defender who enumerates via `ListMetrics` or watches namespace presence silently misses idle/terminated fleets.

---

## 2. Components, Assets, and Design

**What this page describes.** A read-only observability view: the AWS-published CloudWatch metrics that an EC2 Fleet or Spot Fleet emits, how to filter them by dimension, and how to view them in the CloudWatch console. It is not an API page — it introduces no new mutating action — but it defines a **data plane** (CloudWatch time-series) that mirrors control-plane state and is reachable through a *different* IAM surface (`cloudwatch:*`) than the EC2 control plane (`ec2:*`).

**Assets.**
- **Namespace `AWS/EC2Spot`** — the fleet metric namespace. Doc: *"The `AWS/EC2Spot` namespace includes the following metrics for your fleet, plus the CloudWatch metrics for the Spot Instances in your fleet."*
- **Fleet metrics (9), all `Count` or `Percent`:** `AvailableInstancePoolsCount`, `BidsSubmittedForCapacity`, `EligibleInstancePoolCount`, `FulfilledCapacity`, `MaxPercentCapacityAllocation`, `PendingCapacity` (= `TargetCapacity − FulfilledCapacity`), `PercentCapacityAllocation`, `TargetCapacity`, `TerminatingCapacity` (capacity being terminated because provisioned > target). These are **operational-intelligence assets**: together they expose a fleet's target size, fulfilment gap, pool-diversification strategy, bidding activity, and active scale-in events.
- **Dimensions (3):** `AvailabilityZone`, `FleetRequestId`, `InstanceType`. `FleetRequestId` carries the fleet request identifier (Spot Fleet `sfr-<UUID>`, e.g. documented `sfr-123f8fc2-cb31-425e-abcd-example2710`; EC2 Fleet `fleet-<UUID>`). It is a **query filter**, not an access-control boundary (see Lens U / M-READ).
- **The publishing identity.** The 9 fleet metrics are published by the **fleet service**, not by the customer's instances or the caller — the customer never calls `PutMetricData` for them. This is the trust-boundary of interest for M-FORGE (does the consumer distinguish service-published points from customer-published points carrying the same namespace+dimensions?).

**Data pipeline (who writes, who reads):**
```
          ┌─────────────────────────────────────── AWS service plane ──┐
 Fleet    │  Spot Fleet / EC2 Fleet service  ──PutMetricData(service)──▶ │
 request  │  (publishes the 9 AWS/EC2Spot fleet metrics + per-instance) │
          └──────────────────────────────────────────────┬─────────────┘
                                                           ▼
   ┌──────────────────────── customer account: CloudWatch metric store ────────────────────────┐
   │  namespace AWS/EC2Spot {dim FleetRequestId, AvailabilityZone, InstanceType}                 │
   │  retained 15 months; visible in ListMetrics/console only if written in last 2 weeks        │
   └───────▲───────────────────────────────▲────────────────────────────────┬──────────────────┘
           │ GetMetricStatistics/GetMetricData/ListMetrics (NO resource/      │ PutMetricData
           │ namespace/dimension IAM scoping — account-wide)                  │ (cloudwatch:namespace
           │                                                                  │  condition is OPT-IN only)
   ┌───────┴───────────┐   ┌──────────────────────────────┐          ┌───────┴───────────────┐
   │ reader principal  │   │ auto-scaling policy / alarm / │          │ publisher principal   │
   │ (cross-team,      │   │ dashboard that READS          │◀─forged──│ (cloudwatch:PutMetric │
   │  M-READ)          │   │ AWS/EC2Spot (M-FORGE sink)    │   points  │  Data, M-FORGE)       │
   └───────────────────┘   └──────────────────────────────┘          └───────────────────────┘
           ▲
           │ oam link (consent-gated; shares all-namespaces OR a namespace subset)
   ┌───────┴───────────┐
   │ monitoring account │  (M-OAM, cross-account read)
   └────────────────────┘
```

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | Functionality | Notes / lead |
|---|---|---|---|---|---|---|
| `cloudwatch:ListMetrics` | SigV4 | No | Yes | any holder (classic metrics: no resource type / no condition — `dataset` resource is OTLP-only, N/A here) | Enumerate metric name + dimension tuples, incl. **all `FleetRequestId` values** published to `AWS/EC2Spot` | **M-READ** (enumeration oracle; misses idle >2wk) |
| `cloudwatch:GetMetricStatistics` | SigV4 | No | Yes | any holder (**blank resource type, blank condition keys** — fully unscopable) | Read aggregated time-series for a metric+dimensions | **M-READ** (posture read); works even on >2wk-idle metrics if combo known |
| `cloudwatch:GetMetricData` | SigV4 | No | Yes | any holder (classic: unscopable; `dataset`/`HasAccessGrant` is OTLP-only) | Bulk/metric-math read | **M-READ** |
| `cloudwatch:DescribeAlarmsForMetric` | SigV4 | No | Yes | any holder (blank/blank) | List alarms watching a given metric | Lens O recon (find which fleet metrics are alarmed) |
| `cloudwatch:PutMetricData` | SigV4 | **Yes** (writes data points) | Yes | holder; scopable **only if** policy adds `cloudwatch:namespace` condition (opt-in) | Publish arbitrary data points to any namespace incl. `AWS/EC2Spot` with any dimensions | **M-FORGE** (integrity sink) |
| `oam:CreateLink` + `cloudwatch:Link` | SigV4 | Yes (monitoring acct) | Yes | holder in monitoring acct; `Sink*` resource + `oam:ResourceTypes` (telemetry-category, **not** namespace) | Establish cross-account metric sharing | **M-OAM** |
| console metric browser | HTTPS | No | Yes | console user | View graphs grouped by dimension | Namespace hidden if unused ≥2wk (Lens O) |

**No new mutating EC2 action on this page.** The entire lead-bearing surface is CloudWatch's generic metric plane viewed through the fleet lens. The sharp facts are in the **condition-key asymmetry**: `PutMetricData` *can* be namespace-scoped (`cloudwatch:namespace`) but the four read actions *cannot* be scoped by namespace, dimension, or resource at all for classic metrics.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Intra-account principal with CloudWatch read, **no EC2 fleet read** | Another team's fleet inventory + scaling/bidding posture | `ListMetrics`/`GetMetricStatistics` on `AWS/EC2Spot` (no resource/namespace/dimension IAM scoping) | Recovering a `FleetRequestId` and its `TargetCapacity`/`TerminatingCapacity`/`Bids…` series the caller cannot `Describe` on the EC2 side = **intra-account over-exposure / inert-ABAC** |
| Intra-account principal with `PutMetricData`, no `ec2:*`/`application-autoscaling:*` | A fleet owner's dashboards / alarms / auto-scaling signal | `PutMetricData` into `AWS/EC2Spot` with victim `FleetRequestId` (no namespace condition on default grant) | A fabricated data point accepted and reflected in the owner's `GetMetricStatistics`/alarm state = **monitoring-integrity breach**; capacity change if a policy reads it = escalation |
| Source account (fleet owner) | Monitoring account | OAM link sharing all-namespaces / a set incl. `AWS/EC2Spot` | Monitoring account reads source fleet posture; **and** whether IAM alone (no link-config change) can exclude `AWS/EC2Spot` = scoping-mechanism question |
| Any customer surface | **AWS service plane** (the `AWS/EC2Spot` publishing identity) | — | **HARD STOP** if the publisher identity is reachable/impersonable |

---

## 5. Recommended Areas of Focus

### M-READ — Fleet posture disclosure via unscopable CloudWatch metric read  *(PRIORITY 1 — confirmed-shape, intra-account)*
**Background.** The four CloudWatch read actions are account/region-wide once granted: per `list_cloudwatch.html`, `GetMetricStatistics` and `DescribeAlarmsForMetric` have a **blank resource-type column and a blank condition-key column**, and `ListMetrics`/`GetMetricData` only acquire a resource type/condition (`dataset`, `cloudwatch:HasAccessGrant`) for the newer OTLP-ingestion feature — irrelevant to classic namespace+dimension metrics like `AWS/EC2Spot`. **No read action has a `cloudwatch:namespace` or dimension condition key.** Meanwhile the EC2 control-plane read `DescribeSpotFleetRequests` is itself only region-scopable (see `manage-spot-fleet` plan), so even that wall is weak — but a principal can be denied it entirely and still read the metrics.

**Security Concern.** The page says *"To filter the data for your fleet, use the following dimensions"* — presenting `FleetRequestId` as a per-fleet selector. It is a **query filter, not an authorization boundary**: there is no IAM mechanism to restrict a reader to *their* `FleetRequestId`, namespace, or dimension. So any principal with generic CloudWatch read (extremely common — it is in default read-only/observability grants) can enumerate every fleet in the account and read each fleet's `TargetCapacity`, `FulfilledCapacity`, `PendingCapacity`, `TerminatingCapacity`, `BidsSubmittedForCapacity`, `AvailableInstancePoolsCount`, `EligibleInstancePoolCount`, and `PercentCapacityAllocation` time-series — i.e. the fleet's size, fulfilment gap, active scale-in, bidding activity, and capacity-pool diversification strategy — across team/workload boundaries inside one account, bypassing any attempt to compartmentalise fleets via `ec2:*` scoping.

**High-level Test Scenarios.**
- **Claim:** a role holding only `cloudwatch:ListMetrics`+`GetMetricStatistics` and an explicit `Deny` on `ec2:DescribeSpotFleetRequests`/`ec2:DescribeFleets` can recover a foreign-team fleet's ID and capacity series. **Oracle:** create canary fleet A under role-A; from role-R (CloudWatch-read + EC2-fleet-read Deny), `aws cloudwatch list-metrics --namespace AWS/EC2Spot` → recover A's `FleetRequestId`; `get-metric-statistics --namespace AWS/EC2Spot --metric-name TargetCapacity --dimensions Name=FleetRequestId,Value=<A>` → non-empty series. `SimulatePrincipalPolicy` first to prove role-R is denied the EC2 read. **Refute if** CloudWatch read somehow enforces an ownership/tag check not in the reference (it does not per the tables).
- **Claim:** `ListMetrics` enumerates `FleetRequestId` dimension values with **no prior knowledge** of any fleet ID. **Oracle:** `list-metrics --namespace AWS/EC2Spot --dimensions Name=FleetRequestId` returns the set of active fleet IDs. **Adjacent:** correlate `AvailabilityZone`/`InstanceType` dimensions to map a competitor team's capacity-pool footprint.

**Doc evidence:** `ec2-fleet-cloudwatch-metrics.html` (dimension table + metric table); `list_cloudwatch.html` (blank/blank rows for `GetMetricStatistics`/`DescribeAlarmsForMetric`). **Severity-if-true:** **Medium** — intra-account cross-team information disclosure / least-privilege compartmentalisation failure (an **inert-ABAC** shape: no namespace/dimension condition key exists to write the Deny). Not cross-account by itself. **Stop condition:** one fleet's posture read from the deny-scoped reader role.

---

### M-FORGE — Forging data into the `AWS/EC2Spot` namespace (monitoring-integrity sink)  *(PRIORITY 1 — one confirmed doc-gap at the core)*
**Background.** `cloudwatch:PutMetricData` writes data points into the **caller's own account** CloudWatch. Per `list_cloudwatch.html` it supports a `cloudwatch:namespace` condition key — but that is **opt-in**: the dedicated page `iam-cw-condition-keys-namespace.html` shows it must be *added* by the customer, and AWS's own published console/observability grants (`security_iam_id-based-policy-examples.html`) grant `cloudwatch:PutMetricData` on `Resource:"*"` with **no namespace condition**. Crucially, **no CloudWatch documentation states that customers are blocked from publishing into `AWS/`-prefixed (reserved) namespaces** — `cloudwatch_concepts.html` only *describes* `AWS/{service}` as AWS's naming *convention*, and `publishingMetrics.html` imposes no namespace restriction. The 9 fleet metrics are published by the **service**, but the consumer (dashboard / alarm / auto-scaling policy) keys on namespace+metric+dimensions, not on the publishing principal.

**Security Concern.** If writes into `AWS/EC2Spot` are not blocked at the API (the documentation is consistent with "not blocked"), then any intra-account principal with the common unscoped `cloudwatch:PutMetricData` can publish fabricated `TargetCapacity`/`FulfilledCapacity`/`CPUUtilization`-style data points carrying a victim fleet's `FleetRequestId` — with **no `ec2:*` and no `application-autoscaling:*`**. Downstream impact ladder: (a) corrupt the owner's dashboards/graphs (integrity/decision-corruption); (b) drive the owner's **own CloudWatch alarms** on fleet metrics to `ALARM`/`OK` on demand; (c) if a target-tracking/step policy's metric spec reads a metric in `AWS/EC2Spot` for this fleet, steer capacity — the **confirmed** generic form of this is `spot-fleet-target-tracking` **TT3** (custom namespace); M-FORGE is the sharper variant where the attacker poisons the **service's own** namespace that *predefined* specs and the owner's hand-built alarms trust.

**High-level Test Scenarios.**
- **Claim (the pivotal doc-gap):** `PutMetricData --namespace AWS/EC2Spot` is accepted (AWS does not reserve the namespace at the API). **Oracle:** from a publisher role holding only `cloudwatch:PutMetricData` (no namespace condition, no `ec2:*`), `aws cloudwatch put-metric-data --namespace AWS/EC2Spot --metric-data MetricName=TargetCapacity,Dimensions=[{Name=FleetRequestId,Value=<canary-fleet>}],Value=9999` → then `get-metric-statistics` on that metric/dimension shows the injected value interleaved with the service's real points. **Refute if** the API returns `AccessDenied`/`InvalidParameterValue` for an `AWS/`-prefixed namespace (would convert this lead to a null and is itself worth documenting as the enforcing mechanism). This single call settles the whole lead — run it first.
- **Claim:** a namespace-forged point flips the fleet owner's alarm. **Oracle:** owner creates an alarm on `AWS/EC2Spot TargetCapacity` for the canary fleet; publisher role forges a breaching value; observe `DescribeAlarmHistory` state change — proving a principal with no fleet rights can trigger the owner's alarm actions (chains into `spot-fleet-step-scaling` **SS1** force-trigger).
- **Claim (scoping escape-hatch exists but is off by default):** adding `Condition:{StringEquals:{cloudwatch:namespace:"AWS/EC2Spot"}}` as a `Deny` blocks the forge; absent it, nothing does. **Oracle:** `SimulatePrincipalPolicy` with and without the Deny — demonstrates the mitigation is customer-opt-in and absent from AWS's sample grants.

**Doc evidence:** `list_cloudwatch.html` (`PutMetricData` → condition key `cloudwatch:namespace`, resource `dataset` non-required); `iam-cw-condition-keys-namespace.html` (opt-in JSON); `cloudwatch_concepts.html` / `publishingMetrics.html` (no reservation statement — **doc-gap**); `security_iam_id-based-policy-examples.html` (sample grants `PutMetricData` on `*` unconditioned). **Severity-if-true:** **Medium** intra-account (monitoring-integrity / decision corruption, no fleet rights required); **High** if it reaches auto-scaling capacity steering or forces alarm actions with impact. **Stop condition:** one forged `AWS/EC2Spot` point read back from the owner's query, or an `AccessDenied` that refutes the lead.

---

### M-OAM — Cross-account fleet-posture exposure via Observability Access Manager  *(PRIORITY 2 — resolves a doc-gap carried by two sibling plans)*
**Background.** `spot-fleet-automatic-scaling` (L2) and `spot-fleet-target-tracking` (§8, TT3 cross-account caveat) both left "CloudWatch cross-account observability (OAM)" as an **un-examined doc-gap**. This plan owns it. Per `list_oam.html`, `oam:CreateLink` requires a `Sink*` resource in the monitoring account and companion `cloudwatch:Link`; its `oam:ResourceTypes` condition key filters by **telemetry category** (`AWS::CloudWatch::Metric` vs `::Logs::LogGroup`), **not by metric namespace**. `CloudWatch-Unified-Cross-Account.html` states: *"You can choose to share the metrics from all namespaces with the monitoring account, or filter to a subset of namespaces."* — so namespace scoping of a link **exists but is a `CreateLink`/`PutSinkPolicy` configuration parameter, not an IAM condition key**.

**Security Concern.** The IAM layer gates *whether a link/sink can be created at all*, not *which namespaces flow through it*. A source account that establishes an OAM link sharing "all namespaces" (the broadest and simplest option) silently exposes its entire `AWS/EC2Spot` fleet posture (all 9 metrics × `FleetRequestId`/`AZ`/`InstanceType`) to the monitoring account — the cross-account amplification of M-READ. Because the scoping lives in link config rather than IAM, a least-privilege reviewer auditing IAM policies alone cannot see that `AWS/EC2Spot` is being shared, and cannot write an IAM Deny to exclude it.

**High-level Test Scenarios.**
- **Claim:** an all-namespaces OAM link exposes source-account fleet metrics to the monitoring account. **Oracle:** two authorized accounts; source creates a canary fleet; monitoring account (via the link) runs `get-metric-statistics --namespace AWS/EC2Spot` and reads the source fleet's `TargetCapacity`. **Refute if** `AWS/EC2Spot` is excluded by default from OAM sharing (undocumented — would be a useful finding).
- **Claim:** IAM alone cannot restrict a link to exclude `AWS/EC2Spot`. **Oracle:** attempt an IAM policy/condition on the link principal that would drop `AWS/EC2Spot`; confirm (per `list_oam.html`) there is no namespace condition key — the only lever is the link's `MetricConfiguration.Filter`, a config value. **Severity-if-true:** **Medium–High** cross-account read of operational posture, **consent-gated** (both accounts must agree to the link — this is a mis-scoping / least-visibility footgun, not an unconsented breach). **Stop condition:** source fleet posture read from the monitoring account, or confirmation the namespace is excluded.

---

### M-DETECT — Metric visibility decay as a detection blind-spot  *(PRIORITY 3 — Lens O, enabler)*
**Background.** Two different lifetimes, confirmed: **retention** — `cloudwatch_concepts.html`: *"Data points … are available for 455 days (15 months)"* and *"Metrics cannot be deleted, but they automatically expire after 15 months if no new data is published"*; **visibility** — the same page: *"Metrics that have not had any new data points in the past two weeks do not appear in the console … They are not returned in the results of a list-metrics command. The best way to retrieve these metrics is with the get-metric-data or get-metric-statistics commands."* The target page confirms the namespace-level effect specifically for fleets: *"if you have used EC2 Fleet or Spot Fleet in the Region, but not for the past two weeks, the [EC2 Spot] namespace does not appear."*

**Security Concern.** A defender who hunts fleets by `ListMetrics` enumeration (M-READ's own method) or who watches for the `EC2 Spot` namespace's *presence* in the console has a **two-week blind window**: an attacker who spins up a fleet, acts, and terminates it (or an idle/abandoned rogue fleet) drops out of `ListMetrics` and the console namespace list after 14 days even though the evidence is still retained for 15 months. The data is only recoverable by a `GetMetricData`/`GetMetricStatistics` query that already knows the exact namespace+metric+`FleetRequestId` — which the defender no longer has, because the enumeration path that would have given them the ID is the one that went blind.

**High-level Test Scenarios.**
- **Claim:** a terminated canary fleet's metrics vanish from `ListMetrics`/console within ~2 weeks but remain fetchable via `GetMetricStatistics` with the known ID. **Oracle:** record the canary `FleetRequestId`; after >14 days idle, confirm `list-metrics --namespace AWS/EC2Spot` omits it while `get-metric-statistics` with the saved ID still returns points. **Severity:** **Low / Informational** (detection-evasion enabler; raises the practicality of M-READ/M-FORGE by narrowing the window defenders can observe). **Stop condition:** the ListMetrics-omission / GetMetricData-still-present split demonstrated (or reasoned from the doc if the 2-week wait is out of budget — the behavior is explicitly documented).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-team fleet posture read with EC2 read denied | `cloudwatch:GetMetricStatistics`/`ListMetrics` on `AWS/EC2Spot` | **None** — reads have blank resource/condition columns; `FleetRequestId` is a filter not an ACL (M-READ) |
| Forge `AWS/EC2Spot` points into a victim fleet's dimension | `cloudwatch:PutMetricData` | `cloudwatch:namespace` condition — but **opt-in**, absent from AWS sample grants; namespace-reservation at API is a **doc-gap** (M-FORGE) |
| Force an owner's fleet-metric alarm to ALARM/OK | forged metric → alarm | Owner alarm trusts namespace+dimensions, not publisher identity (M-FORGE → `spot-fleet-step-scaling` SS1) |
| Cross-account posture leak via OAM all-namespaces link | `oam:CreateLink` / sink | Namespace filter exists only as link **config**, not IAM condition; `oam:ResourceTypes` is category-level (M-OAM) |
| Terminated/idle rogue fleet evades metric-based detection | ListMetrics / console namespace presence | 2-week visibility decay vs 15-month retention — documented behavior, no mitigation (M-DETECT) |

---

## 7. Out-of-Scope Risk Categories

- **The auto-scaling control loop itself** (alarm→policy→`ec2:ModifySpotFleetRequest`→terminate), the SLR policy audit, and foreign-fleet terminate — owned by `spot-fleet-automatic-scaling` / `-target-tracking` / `-step-scaling` / `-scheduled-scaling`. This plan touches them only as the *downstream sink* of M-FORGE and cross-references, never re-derives, them.
- **The EC2 Describe-side read oracle** (`DescribeSpotFleetRequests` config/launch-spec/`iamFleetRole` disclosure) — owned by `manage-spot-fleet`. M-READ is its CloudWatch twin, not a duplicate.
- **The operator sample policy `cloudwatch:*` on `"*"`** — audited in `spot-fleet-auto-scaling-IAM` (R2) and `spot-fleet-step-scaling` (SS1). Not re-audited here.
- **Per-instance `AWS/EC2` metrics / IMDS on managed hosts / detailed-monitoring billing** — product behavior, not a boundary.
- **CloudWatch as a whole service** — only the `AWS/EC2Spot` fleet-metric slice is in scope; generic CloudWatch bugs are a different target.
- **A customer who writes their own over-broad `cloudwatch:PutMetricData` grant** is a self-inflicted footgun **except** where AWS's *published sample* grant is the source of the unconditioned permission (then it is the sample-policy finding tracked in the IAM siblings, not this plan).
- **DNS rebinding / network-layer attacks on CloudWatch endpoints**, and **single-tenant self-DoS** via metric-flooding.

---

## 8. Null Hypotheses / Doc Gaps

- **Lens A (cross-account IDOR), direct form: NULL within one account's native API.** `PutMetricData` writes only to the caller's own account; the read APIs read only the caller's account. There is no documented API to read/write another account's CloudWatch metrics *except* the consent-gated OAM link (M-OAM). `FleetRequestId` is a 128-bit `sfr-`/`fleet-` UUID → **not fabricable/enumerable cross-account** (genuine null, not a lazy one). Pages checked: `list_cloudwatch.html`, `publishingMetrics.html`, `API_CancelSpotFleetRequests.md` (ID format).
- **Lens G (SSRF): NULL.** No field on this page or in the metric/dimension model is a URL/host the service dereferences. Pages checked: `ec2-fleet-cloudwatch-metrics.html`, `viewing_metrics_with_cloudwatch.html`, `publishingMetrics.html`.
- **Lens B/C (PassRole / credential vending): NULL on this surface.** No role ARN is passed and no credential vended by the metrics plane. (The fleet's *publishing* identity is AWS's — a HARD STOP target if ever reachable, not a customer lead.)
- **Lens Q (upload), K (prompt-injection), W (attestation), FF (JWT): NULL** — no upload, no LLM, no attestation gate, no token validation on this surface.
- **DOC-GAP 1 (pivotal, gates M-FORGE severity):** No AWS doc states whether the `PutMetricData` API **rejects writes to `AWS/`-reserved namespaces**. The documentation is *consistent with* "not blocked" (no reservation statement anywhere; `cloudwatch:namespace` is opt-in), but this is **not a confirmed null** — a single live `put-metric-data --namespace AWS/EC2Spot` call settles it and must be the first action of the M-FORGE test.
- **DOC-GAP 2 (gates M-FORGE escalation):** Whether any **predefined** Spot-Fleet auto-scaling metric spec reads a metric *in `AWS/EC2Spot`* (vs the per-instance `AWS/EC2` namespace) is not cleanly documented; the recalled `EC2SpotFleetRequestAverage*` strings are **PredefinedMetricType enum values, not CloudWatch metric names**, and the underlying namespace they read was not confirmed. Confirm before claiming M-FORGE → capacity-steering via a *predefined* (as opposed to custom, = TT3) policy.
- **DOC-GAP 3 (gates M-OAM):** Whether `AWS/EC2Spot` is included by default in an "all namespaces" OAM share, and whether any default OAM behavior excludes AWS-published namespaces, is not documented — resolve with the two-account test before escalating M-OAM severity.
- **DOC-GAP 4 (minor, M-READ cosmetics):** No verbatim documented EC2 Fleet `fleet-<...>` ID example was located (only the Spot Fleet `sfr-<UUID>` example). Does not affect the lead (ListMetrics returns whatever IDs exist).

---

*Downstream hunter note.* Start with **M-FORGE's first scenario** — a single `put-metric-data --namespace AWS/EC2Spot` from a `PutMetricData`-only role: it resolves DOC-GAP 1, the hinge of this whole plan, in one call. Then **M-READ** (deny-scoped reader role → `list-metrics`/`get-metric-statistics`), both runnable in one authorized account with two scoped roles and `SimulatePrincipalPolicy` as the pre-check. **M-OAM** needs a second account; **M-DETECT** is doc-confirmed and only needs a live demo if the 2-week wait fits the budget. Read the four sibling cross-refs in §0 before escalating any forged-metric lead into the auto-scaling control loop. Tear down every canary fleet, alarm, metric, and OAM link created. **HARD STOP** on any sign the `AWS/EC2Spot` publishing identity is an AWS service-plane principal.
