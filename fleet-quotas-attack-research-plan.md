# EC2 Fleet & Spot Fleet Quotas — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-quotas.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/fleet-quotas.md`, verified **byte-identical** online==offline 2026-10-15). Supporting evidence from `create-ec2-fleet.md`, `monitor-ec2-fleet-using-eventbridge.md`, `delete-fleet.md`, `cancel-spot-fleet.md`, `spot-fleet-states.md`, the API reference (`API_CreateFleet.md`, `API_TargetCapacitySpecificationRequest.md`, `API_FleetLaunchTemplateSpecificationRequest.md`, `API_FleetCapacityReservationTargetRequest.md`, `API_ReservedCapacityOptionsRequest.md`, `API_RequestServiceQuotaIncrease.md`), and the IAM Service Authorization Reference (`list_ec2.md`, `list_support.md`, `list_servicequotas` [online — not in mirror]). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

**This plan's place in the corpus.** `fleet-quotas.html` is the **account-limits / resilience-governor page** for the whole EC2-Fleet + Spot-Fleet feature set. It is the FIRST sibling whose primary surface is **Lens L (resource exhaustion / availability / cost)** and **Lens U (documented-guarantee-vs-enforcement)** rather than cross-tenant data access — the page defines no resource-by-ID API and crosses no cross-account trust boundary of its own. Its value is (a) it names the exact numeric governors that bound every launch primitive the siblings describe, and (b) it documents two first-class **blind spots** — the `instant` fleet type (unlimited count/pools, zero telemetry) and the shared EC2-Fleet/Spot-Fleet quota pool (intra-account cross-team DoS). It cross-references but does not restate the launch-injection / SLR / cross-account-CR-consume mechanics owned by `ec2-fleet`, `create-spot-fleet`, `ec2-fleet-instance-weighting-walkthrough`, `ec2-fleet-launch-instances-multiple-cr-types-walkthrough`, `ec2-fleet-targeted-capacity-reservations-walkthrough`, `fleet-monitor`/`monitor-ec2-fleet-using-eventbridge`, `delete-fleet`, and `cancel-spot-fleet`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Most leads here are **availability/cost (Lens L)** or **control-expressibility (Lens S/U)** — their severity ceiling intra-account is a *least-privilege/footgun or AWS-owned control-gap*, NOT cross-tenant compromise. The one place real cross-account impact enters is where a quota **amplifies** a cross-account primitive another sibling owns (Area 7's 5,000-CR-per-request × un-shared-CR-consume open question). Rate chained leads at the end of the chain.
- `DryRunOperation` is **caller-IAM only, evaluated before resource resolution** — it is NOT a quota-enforcement or ownership oracle. Quota-enforcement questions (Areas 2/3/6/7) require a **synthetic canary fleet in an account you are authorized to test**, with teardown. `iam:SimulateCustomPolicy` is the safe first oracle for every "is there a condition key" claim (Areas 2/5/7-nuance) — it touches no resources.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Cross-team / cross-fleet-type DoS inside one account:** prove that a principal operating one fleet type (or team) can exhaust a quota the quotas page says is *shared* (1,000 fleets, 300 Spot pools, 100,000 Region units) and thereby **block another team's fleet creations** in the same account/Region.
2. **Control-expressibility gap:** prove an administrator **cannot** author an IAM policy that caps a principal's per-fleet or per-Region target capacity below the default quota (no condition key exists), so the only governor is the account-wide quota itself.
3. **Quota-overshoot cost amplification:** prove that fulfilled/launched capacity can exceed the *requested* `TotalTargetCapacity` that the quota gates (instance-weighting round-up), with no documented ex-post reconciliation against the quota and no mandatory `MaxTotalPrice` backstop.
4. **`instant`-type quota-and-telemetry blind spot:** demonstrate that unbounded parallel `instant` CreateFleet calls launch capacity while (a) consuming no fleet-count/pool quota and (b) emitting zero EventBridge events — a documented detection blind spot.
5. **Self-raise of a cost ceiling / IAM-unscopable increase path:** determine whether a low-privilege principal can submit (and possibly auto-approve) a target-capacity quota increase, and whether the `support:CreateCase` increase path is IAM-restrictable at all.
6. **Fail-open on stated constraints:** determine whether "can't span Regions" and "can't span subnets in the same AZ" are synchronous API rejects or unenforced prose.
7. **5,000-CR-per-request amplifier of a cross-account consume primitive:** quantify and (via the sibling plans' open question) chain the up-to-5,000 Capacity-Reservation references per `instant` CreateFleet into cross-account prepaid-capacity theft / victim On-Demand-quota burn.

---

## 2. Components, Assets, and Design

**What the page governs.** Per-account, **Region-specific** numeric quotas on the EC2 Fleet (`CreateFleet`) and Spot Fleet (`RequestSpotFleet`) control planes, plus a Support-Center quota-increase workflow. No data plane, no resource-by-ID read API, no network interface, no identity vended here. The "resource" is a *fleet request* and the *target capacity* it declares.

**The quota table (verbatim values, with footnote decoding):**

| # | Quota description | Value | Hard? | Shared EC2+Spot? | Applies to `instant`? |
|---|---|---|---|---|---|
| 1 | EC2 Fleets **and** Spot Fleets of type `maintain`/`request` in `active`/`deleted_running`/`cancelled_running` | **1,000** | **Yes (²)** | **Yes (¹)** | No (instant excluded from this row) |
| 2 | EC2 Fleets of type `instant` | **Unlimited** | n/a | n/a | — |
| 3 | Spot capacity pools (instance-type × subnet) for `maintain`/`request` | **300** | No | **Yes (¹)** | No |
| 4 | Spot capacity pools for `instant` | **Unlimited** | n/a | n/a | — |
| 5 | User data in a launch specification | **16 KB** | **Yes (²)** | implicit | yes (incl. the `instant`-only override field) |
| 6 | Target capacity per EC2 Fleet or Spot Fleet | **10,000** | No (increasable; **no footnote**) | n/a | **Yes** (no carve-out) |
| 7 | Capacity Reservations per EC2 Fleet request using `ReservedCapacityOptions` | **5,000** | **Yes (²)** | n/a | `instant`-only feature |
| 8 | Target capacity across all EC2 Fleets and Spot Fleets in a Region | **100,000** | No (increasable; ¹ only) | **Yes (¹)** | **Yes** (inferred — see Area 4 doc-gap) |
| 9 | A fleet request can't span Regions | constraint | — | — | — |
| 10 | A fleet request can't span different subnets from the same AZ | constraint | — | — | — |

Footnotes (verbatim): **¹** "These quotas apply to both your EC2 Fleets and your Spot Fleets." **²** "These are hard quotas. You can't request an increase for these quotas." **³** `deleted_running`/`cancelled_running` fleets (instances left running on delete/cancel) **still count** toward quota #1 until the instances are terminated and the fleet reaches `deleted_terminating`/`cancelled_terminating`, at which point it stops counting.

**Increase workflow (asset):** `## Request a quota increase for target capacity` → Support Center **Create case** console form (`issueType=service-limit-increase&limitType=service-code-ec2-fleet`), Limit type "EC2 Fleet", choice of **"Target Fleet Capacity per Fleet (in units)"** or **"Target Fleet Capacity per Region (in units)"**. Confirms (a) both #6 and #8 are increasable, (b) the quota is measured in **units** (weighted), not instances.

```
                 ┌─────────────────────────────────────────────────────────┐
   Caller IAM ──▶│  CreateFleet / RequestSpotFleet  (control plane)         │
 (CreateFleet /  │   • validates requested TotalTargetCapacity (units)      │
  RequestSpot-   │     against #6 (10,000/fleet) and #8 (100,000/Region)    │──┐
  Fleet)         │   • counts active fleet toward #1 (1,000) unless instant │  │ weighting round-UP
                 └─────────────────────────────────────────────────────────┘  │ (no overshoot ceiling)
                              │ maintain/request → SLR          │ instant      ▼
                              ▼  (AWSServiceRoleForEC2Fleet)     ▼ (caller id)  FULFILLED capacity
                       EventBridge events                 NO EventBridge        may EXCEED requested
                       (telemetry present)                events (blind)        (not re-checked vs quota?)

   Increase path:  Support Center case  ──(support:CreateCase, IAM-UNSCOPABLE)──▶  AWS review
                   (or servicequotas:RequestServiceQuotaIncrease, per-quota-ARN scopable)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Team/principal A (one fleet type) | Team/principal B's ability to create fleets, **same account/Region** | Shared quota pool #1/#3/#8 (footnote ¹) | B's `CreateFleet`/`RequestSpotFleet` fails with a limit-exceeded error **solely because A consumed the shared pool** — intra-account cross-team availability denial |
| Low-priv caller | Account cost ceiling | `TotalTargetCapacity` request-time gate (#6/#8) + weighting round-up + opt-in `MaxTotalPrice` | Fulfilled instance count / spend exceeds the requested-units quota with no backstop |
| `instant`-fleet caller | Detection / quota accounting | `instant` excluded from #1/#3 and emits no EventBridge events | Capacity launched that appears in **neither** the fleet-count quota **nor** the EventBridge stream |
| Caller with `support:CreateCase` **or** `servicequotas:RequestServiceQuotaIncrease` | Own account's quota ceiling | Increase workflow | A principal the admin did not intend raises (or auto-approves) a capacity/cost ceiling; `support:CreateCase` cannot be IAM-scoped to EC2-Fleet only |
| `instant`-fleet caller | Up to 5,000 Capacity Reservations (possibly cross-account/RAM-shared) in one call | `ReservedCapacityOptions` / `CapacityReservationId.N` / group ARN (#7) | One request consumes/occupies prepaid capacity across many CRs, including (open) foreign/un-shared CRs → cross-account capacity theft + victim On-Demand-quota burn **[chain — see Area 7 + sibling plans]** |
| Caller | "can't span Regions" / "can't span subnets same AZ" guarantees | API validation (unspecified) | A fleet request that spans is **accepted** rather than rejected (fail-open) |

**Service-plane boundary (hard stop):** none of this page's primitives should ever reach AWS's own fleet/service-plane identity. If a quota-exhaustion or increase probe surfaces an AWS-owned account/credential/ARN, STOP and flag for disclosure.

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:CreateFleet` | POST (SigV4) | Existing | **Yes** | External | Create a fleet; gated by #1/#6/#8/#5/#7 | Yes | caller IAM | `capacity-reservation` resource row IS tag/Region-scopable; **no capacity/CR-ID/fleet-type condition key** (Areas 2/7) |
| `ec2:RequestSpotFleet` | POST (SigV4) | Existing | **Yes** | External | Create a Spot Fleet; gated by #1/#6/#8/#5 | Yes | caller IAM | same no-capacity-key gap |
| `ec2:ModifyFleet` / `ec2:ModifySpotFleetRequest` | POST | Existing | Yes | External | Resize target capacity of a live fleet | Yes | caller IAM | re-hits #6/#8 at modify time (cross-ref `modify-ec2-fleet`/`modify-spot-fleet` plans) |
| `servicequotas:RequestServiceQuotaIncrease` | POST | Existing | Yes | External | Programmatic quota-increase request | Yes | caller IAM | **IS** per-quota-ARN scopable (`{service-code}/{quota-code}`); `servicequotas:service` key scopes by service only. `SupportCaseAllowed` flag — some quotas auto-approved w/o human review (unknown for EC2 Fleet — doc-gap) |
| `support:CreateCase` | POST | Existing | Yes | External | Support-case increase path the page documents | Yes | caller IAM | **IAM-UNSCOPABLE** — no resource types, no condition keys (`list_support.md`). All-or-nothing (Area 5) |
| Support Center "Create case" console form | HTTPS (browser) | Existing | Yes | External | Human increase workflow (page links it) | Yes (console) | console user | `limitType` is a URL query param, **not** an IAM-enforceable scope |

No resource-by-ID read API, no non-SDK/console-hidden knob, and no `[NEW]` marker on this page. The quota *values* are the leads, not new endpoints.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — Shared EC2-Fleet/Spot-Fleet quota pool → intra-account cross-team DoS  **[Lens L, HEADLINE]**
**Background:** Quotas #1 (1,000 fleets), #3 (300 Spot pools), and #8 (100,000 Region target-capacity units) are explicitly ONE shared pool per account/Region across **both** fleet types (footnote ¹: *"These quotas apply to both your EC2 Fleets and your Spot Fleets."*).
**Security Concern:** In a multi-team account, a principal operating EC2 Fleets can exhaust a pool that Spot-Fleet-operating principals depend on, and vice versa — a documented, not hypothetical, cross-team availability denial. #1 is additionally a **hard** quota (²) — it **cannot be raised** to relieve the contention.
**High-level Test Scenarios:**
- *Claim:* Creating 1,000 `maintain`/`request` fleets (any mix of EC2 Fleet + Spot Fleet) blocks ALL further `maintain`/`request` fleet creation account-wide-per-Region, for every team, until some fleet reaches a `_terminating` state. → *Oracle:* the 1,001st `CreateFleet`/`RequestSpotFleet` returns a limit-exceeded error attributable to the shared count. → *Preconditions:* `ec2:CreateFleet`/`ec2:RequestSpotFleet`; canary account. → *Cost:* instances need not actually launch (count is on the fleet request). → *Severity:* **Medium** (intra-account cross-team DoS; High only if the account is a shared-tenancy boundary the org treats as isolation).
- *Claim:* The same holds for the 300 Spot-pool pool (#3) — one team specifying many instance-type×subnet pools starves another's pool diversity. → *Oracle:* a fleet requesting a new (type,subnet) pool fails once 300 are in use across both services.
- *Stop condition:* once limit-exceeded is reproduced from the shared counter, the boundary question is answered; do not launch real capacity.
**Doc evidence:** `fleet-quotas.md:16,18,23,27`. **Severity-if-true:** Medium (cross-team availability footgun; AWS-owned insofar as the shared-pool design is undocumented as an isolation risk).

### Area 2 — No IAM condition key caps per-fleet / per-Region target capacity  **[Lens S / U, AWS-owned control-gap]**
**Background:** The 10,000-per-fleet (#6) and 100,000-Region (#8) quotas are enforced **server-side only**.
**Security Concern:** An administrator **cannot** write an identity/SCP policy that tightens a principal below the default — there is no capacity/count condition key on `CreateFleet` or `RequestSpotFleet`. Confirmed: grep of `list_ec2.md` finds `ec2:InstanceCount` ("number of instances", line 10090) and `ec2:TargetInstanceCount` (interruptible-CR-only, line 10164) but **neither appears in the `CreateFleet` (5113–5123) or `RequestSpotFleet` (9465–9474) action blocks**, and `TotalTargetCapacity`/`TargetCapacity`/`MaxTotalPrice` are **not condition keys at all** (zero hits). So the quota is the *only* governor; least-privilege cannot pre-shrink it.
**High-level Test Scenarios:**
- *Claim:* `iam:SimulateCustomPolicy` with a hypothetical `Condition` on `ec2:TotalTargetCapacity`/`ec2:InstanceCount` applied to `ec2:CreateFleet` is **inert** (key not recognized / not populated) → the Deny never fires; a request for `TotalTargetCapacity:10000` is Allowed. → *Oracle:* SimulateCustomPolicy shows the condition has no effect on the CreateFleet decision. → *Cost:* zero (simulation only, no resources). → *Severity:* **Medium** (AWS-owned expressibility gap; the admin's only lever is denying `CreateFleet` wholesale or an account-level quota decrease via Service Quotas template).
**Doc evidence:** `list_ec2.md` CreateFleet/RequestSpotFleet action blocks; `fleet-quotas.md:21,23`. **Severity-if-true:** Medium.

### Area 3 — Weighting round-up overshoots the *requested-units* quota → cost amplification  **[Lens L / U; chains to instance-weighting Area 4]**
**Background:** The #6/#8 quotas gate the **requested** `TotalTargetCapacity` integer ("The number of units to request", `API_TargetCapacitySpecificationRequest.md:15`) measured in **units**, validated at CreateFleet time. Instance weighting then "rounds it up to the next integer … The fleet can select any pool … **even if the capacity of the instances launched exceeds the requested target capacity**" (`ec2-fleet-instance-weighting.md:31`) with **no documented overshoot ceiling** and no documented ex-post re-check of fulfilled capacity against the quota.
**Security Concern:** A request nominally **under** the quota can fulfil **over** it. `WeightedCapacity` is a `Double` with **no documented minimum** (`API_FleetLaunchTemplateOverridesRequest.md:110-115`); a tiny weight (e.g. `0.0001`) against `TotalTargetCapacity:9999` rounds up to a very large instance count while passing the request-time units check. `MaxTotalPrice` is **opt-in with no default** (empty in the CLI skeleton, `create-ec2-fleet.md:253,263`) → absent any backstop, capacity is the only spend governor.
**High-level Test Scenarios:**
- *Claim:* Fulfilled instance count / vCPU for a weighted fleet exceeds the requested `TotalTargetCapacity` units with no quota rejection. → *Oracle (canary):* submit a small-`TotalTargetCapacity`, tiny-`WeightedCapacity` fleet and observe fulfilled capacity > requested units and > any naive quota expectation; confirm no limit-exceeded error. → *Preconditions:* canary account; **set `MaxTotalPrice` low to bound real spend during the test.** → *Cost:* controllable via `MaxTotalPrice`. → *Severity:* **Medium** (single-account cost/availability amplification; the per-Region 100,000 is the only hard-ish ceiling and it too is a units count).
- *Doc-gap to resolve first:* does the service re-check *fulfilled* weighted capacity against #6/#8, or only the requested integer? No page states a re-check — treat as open.
**Doc evidence:** `API_TargetCapacitySpecificationRequest.md:15-17`; `ec2-fleet-instance-weighting.md:31`; `API_FleetLaunchTemplateOverridesRequest.md:110-115`. **Severity-if-true:** Medium. **Cross-ref:** `ec2-fleet-instance-weighting-walkthrough-attack-research-plan.md` Area 4 (overshoot deep layer) — do not re-derive; this plan owns only the quota-interaction angle.

### Area 4 — `instant` fleet type = quota + telemetry blind spot  **[Lens L / O / U]**
**Background:** `instant` fleets are **Unlimited** in count (#2) and Spot pools (#4), and emit **zero** EventBridge events (`monitor-ec2-fleet-using-eventbridge.md:13`: *"Only fleets of type `maintain` and `request` emit events. Fleets of type `instant` do not emit events…"*) — structurally absent, not best-effort-dropped. The capacity quotas #6/#8 carry **no `instant` carve-out** in their row text, so each `instant` call is still capped at 10,000 units and (inferred) accumulates toward the 100,000 Region pool.
**Security Concern:** An insider or compromised credential can launch large capacity via **unlimited parallel `instant` CreateFleet calls**, each (a) consuming no fleet-count/pool quota slot a defender might alarm on and (b) producing no EventBridge signal — defeating both quota-telemetry and event-based detection. CloudTrail still logs the `CreateFleet` management event (the surviving audit signal — note it).
**High-level Test Scenarios:**
- *Claim:* N parallel `instant` fleets launch capacity while quota #1's count stays at 0 and no `aws.ec2fleet` EventBridge event fires. → *Oracle (canary):* create ≥2 `instant` fleets; confirm fleet-count quota usage unchanged and no EventBridge delivery to a test rule; confirm the CreateFleet CloudTrail event IS present. → *Cost:* bound with small `TotalTargetCapacity`/`MaxTotalPrice`. → *Severity:* **Medium** (detection-evasion enabler; raises severity of any launch-based abuse).
- *Doc-gap to resolve:* does `instant` target capacity count toward the 100,000 Region aggregate (#8)? The row's silence on type is the only basis for "yes." If `instant` is **excluded** from #8, instant becomes an effectively unbounded capacity path — a materially higher-severity finding. **Settle this first (canary).**
**Doc evidence:** `fleet-quotas.md:17,19,21,23`; `monitor-ec2-fleet-using-eventbridge.md:13`. **Severity-if-true:** Medium (High if #8 excludes instant). **Cross-ref:** `fleet-monitor` / `monitor-ec2-fleet-using-eventbridge` plans (instant = no events), `ec2-fleet-examples` (instant examples).

### Area 5 — Quota-increase authorization: IAM-unscopable Support path + programmatic self-raise  **[Lens R / U / B]**
**Background:** The page routes increases through the Support Center case form. Two code paths exist: `support:CreateCase` and `servicequotas:RequestServiceQuotaIncrease`.
**Security Concern:**
- `support:CreateCase` is **IAM-unscopable** — `list_support.md:148,188,193`: no resource types, no condition keys, *"AWS Support does not support specifying a resource ARN"* / *"has no service-specific condition keys."* A principal granted `support:CreateCase` can request **any** limit increase for **any** service; the console form's `limitType=service-code-ec2-fleet` is a URL param, **not** an IAM-enforceable scope. A least-privilege policy cannot say "may raise EC2-Fleet limits only."
- `servicequotas:RequestServiceQuotaIncrease` **is** per-quota-ARN scopable (`arn:…:servicequotas:…:{service-code}/{quota-code}`), but the `servicequotas:service` condition key scopes only by **service** (coarse). `API_RequestServiceQuotaIncrease.md` `SupportCaseAllowed` flag implies **some** quotas auto-approve without human review.
**High-level Test Scenarios:**
- *Claim:* A principal with only `support:CreateCase` can submit a fleet (or arbitrary-service) limit-increase case despite an admin intending otherwise. → *Oracle:* `iam:SimulateCustomPolicy` shows no condition can narrow `support:CreateCase`; a scoped canary role with just that action can open a case. → *Severity:* **Low–Medium** (self-raise of a cost/availability ceiling; capped by whatever human/async approval the quota actually requires).
- *Doc-gap to resolve:* is the EC2-Fleet target-capacity quota (`#6/#8`) adjustable/auto-approvable via `RequestServiceQuotaIncrease` (no human review), or Support-review-only? The EC2 UG documents only the manual path; Service Quotas docs never list EC2 Fleet as an API-adjustable example (zero hits). If auto-approvable, a low-priv principal could self-raise the ceiling programmatically — settle before investing.
**Doc evidence:** `fleet-quotas.md:36-58`; `list_support.md:148,188,193`; `API_RequestServiceQuotaIncrease.md` (`SupportCaseAllowed`). **Severity-if-true:** Low–Medium.

### Area 6 — "Can't span Regions / subnets-in-same-AZ": enforcement unverified (fail-open?)  **[Lens U]**
**Background:** Quota rows #9/#10 and `create-ec2-fleet.md:19-20` ("EC2 Fleet limitations") state these as prose constraints.
**Security Concern:** Neither `API_CreateFleet.md` nor `API_RequestSpotFleet.md` names a `ValidationException` subtype or error code for a spanning request (zero hits for `span`/"same Availability Zone"/"different subnets" in the API error sections — only generic `CommonErrors.md`). The docs do not say whether these are synchronous rejects or guidance → potential fail-open.
**High-level Test Scenarios:**
- *Claim:* A fleet request listing two subnets in the same AZ (or spanning Regions where expressible) is **accepted/partially-honored** rather than rejected. → *Oracle (canary):* submit the spanning config; a 2xx / partial launch instead of a clean `ValidationException` is the breach. → *Severity:* **Low–Informational** (provisioning-integrity confusion; no isolation break).
**Doc evidence:** `fleet-quotas.md:24-25`; `create-ec2-fleet.md:19-20`; `API_CreateFleet.md`/`API_RequestSpotFleet.md` Errors. **Severity-if-true:** Low–Info.

### Area 7 — 5,000-CR-per-request amplifier of the cross-account CR-consume primitive  **[Lens L × A/AA chain]**
**Background:** `ReservedCapacityOptions` (an **`instant`-only** feature, `API_ReservedCapacityOptionsRequest.md:11`) lets one `CreateFleet` name up to **5,000** Capacity Reservations (#7, **hard**) — either as a `CapacityReservationId.N` array or a `CapacityReservationResourceGroupArn.N` whose group has **no documented member cap** (`API_FleetCapacityReservationTargetRequest.md:13-20`).
**Security Concern:** The quota is a **blast-radius multiplier** on a primitive the sibling plans flag as an open cross-account question: whether a fleet can name a **foreign / RAM-shared / un-shared** `cr-…` id and consume it (prepaid-capacity theft + the **owner's** On-Demand-quota burn). The multiple-CR-types walkthrough explicitly allows a CR "shared with you by another account in your organization" as a group member, and **no doc bounds how many of the 5,000 may be cross-account**. **Correction to a tempting over-claim:** `CreateFleet`'s `capacity-reservation` resource row **IS** scopable by `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region` (`list_ec2.md:5113-5123`); the real gap is the **absence of an `ec2:CapacityReservationId` condition key** (so you can tag/Region-scope but not pin a specific CR id) — route the scoping question to Lens S, not "fully unscopable."
**High-level Test Scenarios:**
- *Claim:* A single `instant` CreateFleet referencing up to 5,000 CRs (array or group) consumes capacity across all of them, including CRs the caller was never granted. → *Oracle (TWO/THREE-account canary — DryRun is caller-IAM-only, cannot settle):* name an un-shared foreign `cr-…`; `AccessDenied` = enforced; `Insufficient Capacity`-style existence oracle or a successful launch = breach. → *Severity:* **High–Critical if cross-account consume succeeds** (rate at the chain end); Low if purely intra-account amplification.
- *Stop condition:* the moment a foreign CR's capacity is consumed, that is the PoC — do not iterate the 5,000 list or escalate.
**Doc evidence:** `fleet-quotas.md:22`; `API_FleetCapacityReservationTargetRequest.md:13-20`; `API_ReservedCapacityOptionsRequest.md:11`; `ec2-fleet-launch-instances-multiple-cr-types-walkthrough.md:22`; `list_ec2.md:5113-5123`. **Severity-if-true:** High–Critical (chained). **Cross-ref (owns the base cross-account question — do not restate):** `ec2-fleet-launch-instances-multiple-cr-types-walkthrough-attack-research-plan.md` (A1 direct CR-ID targeting, B4 EC2→resource-groups dereference), `ec2-fleet-targeted-capacity-reservations-walkthrough-attack-research-plan.md` (foreign-CR grouping, `ListGroupResources` oracle), `fleet-tutorials-attack-research-plan.md` (RAM/Org trust boundary).

### Area 8 — Orphaned `deleted_running`/`cancelled_running` instances consume ordinary EC2 quotas  **[Lens L, low]**
**Background:** Footnote ³ + `delete-fleet.md:17` / `cancel-spot-fleet.md:20`: delete/cancel **without** terminate leaves instances running in `deleted_running`/`cancelled_running`; the fleet still counts toward #1 until `_terminating`. Separately, `fleet-quotas.md:10` says "the usual Amazon EC2 quotas apply to instances launched by a fleet" — so orphaned instances keep consuming ordinary instance/vCPU/volume quotas indefinitely.
**Security Concern:** A fleet deleted/cancelled "cleanly" can leave running capacity (and spend) behind that is easy to miss, and that still occupies a fleet-count slot — a cost/availability footgun, not a quota-accounting *gap* (docs state it still counts).
**High-level Test Scenarios:**
- *Claim:* After delete-without-terminate, instances keep running and keep consuming vCPU/volume quota while the fleet occupies a #1 slot. → *Oracle:* observe `deleted_running` state + running instances post-delete. → *Severity:* **Low** (self-inflicted cost/availability; cross-ref the cancel/delete siblings for the orphan/KMS-grant-survival depth this plan does not restate).
**Doc evidence:** `fleet-quotas.md:10,31`; `delete-fleet.md:17`; `cancel-spot-fleet.md:20`; `spot-fleet-states.md:24-28`. **Severity-if-true:** Low. **Cross-ref:** `delete-fleet-attack-research-plan.md`, `cancel-spot-fleet-attack-research-plan.md`, `spot-fleet-states-attack-research-plan.md`.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-team DoS via shared quota pool | `CreateFleet`/`RequestSpotFleet` count/pool quotas #1/#3/#8 | Footnote ¹ shared-pool design (no per-team/per-type isolation; #1 is hard, not raisable) |
| Admin cannot cap per-fleet capacity | IAM policy on `CreateFleet`/`RequestSpotFleet` | Absence of any capacity/count condition key (server-side quota only) |
| Fulfilled capacity > requested quota | Instance weighting round-up vs #6/#8 | "size of your fleet is not below its target capacity" + no overshoot ceiling; `MaxTotalPrice` opt-in only |
| `instant` quota/telemetry evasion | `instant` fleet type vs #1/#3 + EventBridge | Unlimited count/pools (#2/#4) + "instant fleets do not emit events" (CloudTrail mgmt event is the only surviving signal) |
| Self-raise cost ceiling / unscopable increase | `support:CreateCase`, `servicequotas:RequestServiceQuotaIncrease` | Support path IAM-unscopable; Service Quotas per-quota-ARN scopable but `service` key coarse; `SupportCaseAllowed` auto-approve |
| Spanning-constraint fail-open | `CreateFleet`/`RequestSpotFleet` validation | Prose "limitations" with no documented `ValidationException` |
| 5,000-CR cross-account consume amplifier | `ReservedCapacityOptions` / `CapacityReservationId.N` / group ARN | 5,000 hard cap; no documented cross-account member bound; no `ec2:CapacityReservationId` key |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Cross-account/cross-tenant data access on this page itself** — every quota is per-account, Region-specific; the page exposes no resource-by-ID read API. The only cross-account exposure is the *chained* Area 7 CR-consume question, whose base primitive is owned by the CR-walkthrough siblings. (Lens A null — see §8.)
- **Shared underlying EC2/Spot capacity-pool infrastructure** and the global Spot market — AWS-operated, shared-responsibility line.
- **Single-tenant self-DoS / self-inflicted cost** from one's own fleets (Areas 3/8 intra-account) is a least-privilege/footgun, in-scope only as an availability/cost *primitive*, not a vulnerability per se — EXCEPT where the control is AWS-owned and uneditable (Area 2's missing condition key, Area 5's unscopable `support:CreateCase`), which ARE reportable.
- **IMDS / userData *content* execution** on launched instances — owned by `ec2-fleet` / instance-weighting siblings; this page owns only the 16 KB *size* governor.
- **DryRun as an ownership/quota oracle** — explicitly out (caller-IAM only, pre-resolution).
- **Modifying logging/CloudTrail** — the quota page provides no such control.

---

## 8. Null hypotheses / doc gaps

**Lenses that did not fire (pages checked named):**
- **A (cross-tenant IDOR):** N/A — read `fleet-quotas.md` fully; all quotas are per-account/Region, no resource-by-ID API, no tenant/customer id field, no opaque id to enumerate. (The one adjacent cross-account thread is Area 7, which is a *consume-amplifier chain*, not an IDOR on this page.)
- **G (SSRF):** N/A — read the whole page incl. the increase procedure; the only URL is the **Support Center console link** (`console.aws.amazon.com/support/home#…`) which is a browser hyperlink, not a server-dereferenced field. No `*Url`/`*Uri`/webhook/import field the service fetches.
- **Q (upload):** N/A — no upload/image/attachment field; the 16 KB userData is a size governor, not an upload-parse surface (parse surface owned by launch-spec siblings).
- **B/C (PassRole/vending):** N/A on this page — no role-ARN input, no STS/session scope here (the SLR launch path is owned by `ec2-fleet`/`create-spot-fleet`/`spot-fleet-prerequisites`). Area 5's increase-path is a Lens-R/U artifact angle, not PassRole.
- **D/V (network segmentation), F (injection), H (KMS), I (tagging-as-ACL), J (OAuth), K (prompt), M (session), N (namespace migration), P (proofing), T (secret reachability), W (attestation), X (twin-action), Y (transport), BB/CC/DD (parser/upstream/cache), EE (predictable-name), FF (token):** N/A — read `fleet-quotas.md`, `create-ec2-fleet.md`, and the increase procedure; none of their triggers (parsers, ENIs, KMS keys, tokens, authorizers, caches, predictable namespaces, migration windows) appear on the quotas surface. Each is owned (where relevant to the broader feature) by a named sibling plan.
- **O (audit-log):** partially fires as the *detection* half of Area 4 (instant = no EventBridge; CloudTrail CreateFleet mgmt event survives). Not developed as a standalone area.

**Open doc-gaps for the hunter to settle first (ordered by leverage):**
1. **(Area 4) Does `instant` target capacity count toward the 100,000 Region quota (#8)?** If excluded, instant is an unbounded capacity path (upgrades Area 4 to High). Settle with a canary before investing.
2. **(Area 7) How many of the 5,000 referenced CRs may be cross-account/RAM-shared, and does fulfilment re-check caller entitlement per CR?** Owned (base question) by the multiple-CR-types + targeted-CR siblings; the 5,000 ceiling is this plan's amplification contribution. Two/three-account canary.
3. **(Area 3) Is *fulfilled* weighted capacity re-checked against #6/#8, or only the requested integer?** No doc states a re-check. Canary with low `MaxTotalPrice`.
4. **(Area 5) Is the EC2-Fleet target-capacity quota API-adjustable/auto-approvable (`RequestServiceQuotaIncrease` + `SupportCaseAllowed`), or Support-review-only?** EC2 UG documents only the manual path; Service Quotas docs never list EC2 Fleet as API-adjustable.
5. **(Area 6) Are the "span Regions / span subnets-in-AZ" constraints synchronous `ValidationException`s or unenforced prose?** No error code documented.

**Corrections carried into the corpus memory (reusable):**
- The **1,000-fleet count quota (#1) is HARD (²)** — not raisable (prior framing missed this).
- **`ec2:CreateFleet` is NOT "fully IAM-unscopable"** — its `capacity-reservation` resource row carries `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region`; the real gap is the absence of an `ec2:CapacityReservationId` condition key and of any capacity/count key.
- **`LaunchTemplateSpecificationUserData`** (the `instant`-only create-time userData override) lives on `FleetLaunchTemplateSpecificationRequest` (one value per `LaunchTemplateConfigs` entry), **not** on the per-override `FleetLaunchTemplateOverridesRequest`; its 16 KB bound is explicitly stated (not a doc-gap).
- Both the **per-fleet 10,000 (#6, no footnote) and per-Region 100,000 (#8, ¹ only) are increasable** via Support case; capacity is measured in **units** (weighted), not instances.

See [[reference-aws-iam-service-auth-ref-url]] and [[project-aws-research-plans]].
