# EC2 Fleet — "On-Demand as primary capacity" Walkthrough — Attack Research Plan

**Source of leads:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-on-demand-walkthrough.html` (the single target page) and the mechanism/reference pages it links or implies: `create-ec2-fleet`, `ec2-fleet-allocation-strategy`, `ec2-fleet-request-type`, `ec2-fleet-control-spending`, `manage-ec2-fleet`, `manage-launch-template-versions`, `delete-launch-template`, the API Reference (`API_CreateFleet`, `API_ModifyFleet`, `API_TargetCapacitySpecificationRequest`, `API_OnDemandOptionsRequest`, `API_SpotOptionsRequest`), the AWS CLI reference (`create-fleet`, `cli-usage-parameters-file`), and the IAM Service Authorization Reference `service-authorization/latest/reference/list_ec2.md` (offline mirror cross-checked against the online `.md` twins, 2026-10-15).
**Status:** Documentation-derived hypotheses only. **Nothing in this plan has been tested against a live AWS account.** It is the plan a hunter (`aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill — orchestrator pass on the target page + two parallel deep-analysis subagents (fleet-config mechanics/defaults, and the `CreateFleet`-vs-`RunInstances` IAM condition-key delta).

> **Scope note — what is NET-NEW here vs. the existing fleet plans.** This is a **page-level deep-dive child** of two existing plans and deliberately does **not** restate them:
> - `ec2-fleet-attack-research-plan.md` owns the core create path: launch-template `$Latest`/`$Default` late-binding → PassRole bypass, the AWS-authored "EC2 Fleet users" sample policy privesc, the SLR, KMS grants, `instant`-fleet overrides, the generic "RunInstances conditions don't propagate to the SLR launch" runtime fact, and `instant`-fleet audit gaps.
> - `fleet-tutorials-attack-research-plan.md` owns the Capacity-Reservation consumption + instance-weighting surface of the `fleet-tutorials.html` hub (of which this page is one of six children) — cross-account CR theft, interruptible-CR reclaim, billing transfer, CR resource groups, the CR condition-key gaps, and the Org-key absence.
>
> **This plan owns the one surface neither sibling develops: the On-Demand-primary MIXED-PURCHASING-OPTION configuration itself** — (a) the static IAM **guardrail-expressibility gap specific to the purchasing-mix / price / IMDS surface** (`ec2:InstanceMarketType` and the IMDS keys exist on `RunInstances` but are **absent from the `CreateFleet` action row**, and no price/strategy/capacity-count key exists at all); (b) the Lens-U "On-Demand capacity is always fulfilled" guarantee; (c) the capacity-split arithmetic; (d) the **defaults-when-omitted "forgotten self-healing fleet"** pattern that the published minimal tutorial config silently produces; (e) the numeric-version-pin safe-pattern delta + its latent availability break. It cross-references the two siblings wherever a lead touches their territory and does not re-derive their findings.

---

## 0. How to use this document
- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs.
- **Prefer the safe oracle first.** Every IAM lead in this plan is settleable *statically* with `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` and read-only reference reads — **no resource need be created** to prove the condition-key gaps (§5.1). Capacity/arithmetic/default-behavior leads (§5.2–§5.5) need a live canary fleet; use the cheapest instance type, a short `ValidUntil`, `Type=instant` where possible for synchronous error visibility, and tear down immediately.
- **HARD STOP:** EC2 Fleet runs entirely inside the caller's own account; the one AWS-service-plane identity in scope is the SLR `AWSServiceRoleForEC2Fleet` — treat it as read-only. The moment any evidence shows you have reached/assumed/extracted credentials or ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**
- **In-scope / reportable (Tier 2):** weak defaults in the **AWS-published, copy-verbatim tutorial `config.json`** (§5.4) are AWS-authored sample-config defaults, in scope under the Lens R/U carve-out. The static IAM gaps (§5.1) are AWS-owned structural facts of the EC2 authz model (Lens S/U) — reportable as a guardrail-expressibility defect, worth filing because a customer could build a compliance control on a guarantee IAM cannot enforce.
- **Out-of-scope / document-but-don't-report:** self-inflicted single-account cost footguns a customer sets on their *own* fleet with no privilege boundary crossed (see §7).

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)
1. **Prove the purchasing-option guardrail is unexpressible.** Show an admin *cannot* author an IAM/SCP policy that stops a `CreateFleet` caller from provisioning Spot (or On-Demand) capacity, because `ec2:InstanceMarketType` — the only EC2 key that filters by purchasing option — is absent from the `CreateFleet` action row (present on `RunInstances`).
2. **Prove the IMDSv2 guardrail is unexpressible at the `CreateFleet` boundary.** Show `ec2:MetadataHttpTokens`/`-Endpoint`/`-PutResponseHopLimit` cannot gate a fleet launch via the `CreateFleet` action's own IAM evaluation (keys present on `RunInstances`, absent on `CreateFleet`).
3. **Prove no IAM lever exists for price / spend / allocation-strategy / target-capacity count** on the fleet path — these keys do not exist anywhere in the EC2 condition-key universe.
4. **Falsify the "On-Demand capacity is always fulfilled" guarantee** — demonstrate it is pool-ordering within the On-Demand market only (no cross-market Spot→On-Demand substitution), and that a `maintain`/`request` fleet can sit silently below `OnDemandTargetCapacity` under ICE with no distinct alarmable state (contrast `instant`'s synchronous `errorSet`).
5. **Break the capacity-split validation** — submit `OnDemandTargetCapacity > TotalTargetCapacity` and redundant `DefaultTargetCapacityType` + explicit per-type capacity, and record whether the service rejects, clamps, or silently builds a fleet whose mix diverges from caller intent.
6. **Demonstrate the "forgotten self-healing fleet"** the published minimal config produces: `Type` omitted → `maintain`, `ValidUntil` omitted → never expires, Spot allocation omitted → AWS's self-described *not-recommended* `lowest-price`, no `MaxTotalPrice` cap → unbounded cost; a fleet that persists and self-replenishes indefinitely until explicitly deleted.
7. **Confirm the latent availability break** of the numeric version pin: delete the pinned launch-template version out from under a live `maintain` fleet and show future replenishment fails with no deletion-time cross-check warning.
8. Probe the undocumented **`Context` ("Reserved.")** parameter for any accepted-and-acted-upon side effect.

---

## 2. Components, Assets, and Design

**What the page does.** A CLI/API-only walkthrough: author a launch template, write a `config.json`, and call `aws ec2 create-fleet --cli-input-json file://config.json` to launch a **mixed On-Demand + Spot** fleet in the **caller's own account/VPC**. There is no multi-tenant service fleet and no customer-reachable data plane. The exact published config:

```json
{
  "LaunchTemplateConfigs": [
    { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-07b3bc7625cdab851", "Version": "2" } }
  ],
  "TargetCapacitySpecification": {
    "TotalTargetCapacity": 20,
    "OnDemandTargetCapacity": 15,
    "DefaultTargetCapacityType": "spot"
  }
}
```

Everything else — fleet `Type`, both allocation strategies, both `MaxTotalPrice` caps, `ValidFrom`/`ValidUntil`, `TerminateInstancesWithExpiration`, `ReplaceUnhealthyInstances`, `TagSpecification`, `Context` — is **omitted and inherits a default** (§5.4).

**Customer-facing interface.** SigV4 `ec2:CreateFleet` (+ `ModifyFleet`/`DeleteFleets`/`Describe*`). The `--cli-input-json file://…` form is resolved **client-side** by the CLI/botocore (local filesystem only; no `http(s)://` scheme on this generic parameter-loading path) and produces a wire-identical `CreateFleet` request — the service cannot distinguish it from discrete flags (so no server-side injection novelty — §8).

**Principals / roles.** Fleet caller (holds the AWS-authored sample policy — owned by `ec2-fleet-attack-research-plan.md` §5.2); the EC2 Fleet SLR `AWSServiceRoleForEC2Fleet` that issues the actual `RunInstances` for `maintain`/`request` fleets (owned by sibling). This page adds no new principal.

**Assets.** Provisioned On-Demand + Spot compute; the account's On-Demand service quota; cost/spend (no IAM-expressible cap — §5.1/§5.4); the **purchasing-option mix** itself as a compliance/cost property the walkthrough implies the operator controls.

**Identifiers.** Fleet ID; launch-template ID + a **pinned numeric version** (`"2"` — the integrity-safe counterpart to `$Latest`/`$Default`). No new opaque/guessable identifier is introduced.

```
 Caller (sample policy, no InstanceMarketType/IMDS/price IAM lever over the fleet path)
     │  create-fleet --cli-input-json file://config.json   (client-side JSON → wire-identical CreateFleet)
     ▼
 EC2 Fleet control plane ── reads ──► Launch Template version 2 (IMMUTABLE; pinned, not $Latest/$Default)
     │  Type defaults to MAINTAIN (self-replenishing, never-expiring)                     │ delete v2?
     │  Spot alloc defaults to LOWEST-PRICE (AWS: "not recommended, highest interruption") │ → latent
     ▼                                                                                     ▼ replenish break
 AWSServiceRoleForEC2Fleet (SLR) ── RunInstances ──► On-Demand pool  (TotalTargetCapacity − OnDemandTargetCapacity)
     │                                              └► Spot pool  (balance, best-effort)
     └─ "On-Demand always fulfilled" = pool-ordering WITHIN the On-Demand market, NOT a Spot→On-Demand fallback
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Admin authoring a guardrail SCP/identity policy | A `CreateFleet` caller's purchasing-option / IMDS / price / count choices | IAM `Condition` evaluation on the `CreateFleet` action | **A `Deny CreateFleet` keyed on `ec2:InstanceMarketType`/`ec2:MetadataHttpTokens`/(any price/strategy/count key) does not deny the matching fleet** → the guardrail is inert; the key is unsupported/undefined for the action (§5.1). |
| Workload owner relying on "On-Demand = guaranteed baseline" | Actual provisioned capacity | Fleet fulfillment under ICE | **A `maintain`/`request` fleet sits below `OnDemandTargetCapacity` with no distinct alarmable state** (only generic capacity events) → the "always fulfilled" guarantee is best-effort, not enforced (§5.2). |
| IaC generator / lower-priv caller computing the JSON | The provisioned OD/Spot mix | `CreateFleet` capacity-split validation | **A logically-inconsistent split (`OnDemand > Total`, or redundant default+explicit) is accepted and silently reshaped** → the fleet's mix diverges from the submitted intent (§5.3). |
| Operator who copies the published tutorial config verbatim | Long-run cost + fleet longevity | Default `Type=maintain` + `ValidUntil=∞` + `lowest-price` Spot + no `MaxTotalPrice` | **A fleet that self-replenishes and never expires with the highest-interruption Spot strategy and no cost cap** is created from an AWS-authored sample (§5.4, Tier-2). |
| Launch-template lifecycle/cleanup process | A live `maintain` fleet's future replenishment | Delete the pinned version `2` | **`delete-launch-template-versions` succeeds with no cross-check warning that a live fleet still references the version; later replenishment fails** (§5.5). |
| Any customer surface | AWS service plane (SLR live creds) | — | **Any AWS-owned identity/ARN/account reached = HARD STOP.** |

---

## 4. API / Interface Inventory

| Name | Mut? | Facing | Functionality | Authorized callers | Notes / net-new lead |
|---|---|---|---|---|---|
| `CreateFleet` | yes | external (SigV4) | Launch mixed OD+Spot fleet from a launch template | caller principal | **Required resource types `fleet*`,`instance*`; optional `capacity-reservation/image/launch-template/placement-group/subnet/volume`. 31-key condition-key union, but NO `ec2:InstanceMarketType`, NO IMDS keys, NO price/strategy/count key.** §5.1 |
| `RunInstances` (comparison baseline, not the target action) | yes | external | Direct launch | caller | 49-key union incl. `ec2:InstanceMarketType` + 3 IMDS keys — the delta vs `CreateFleet` is the finding (§5.1 table). |
| `ModifyFleet` | yes | external | Change `TargetCapacitySpecification` — **`maintain` type only** | caller | Scale-down narrative only mentions terminating **Spot**; On-Demand excess on scale-down is undocumented (§5.3). |
| `DeleteFleets` | yes | external | Delete fleet (± terminate) | caller | The only documented path to end the never-expiring default fleet (§5.4). |
| `DescribeFleets` / `DescribeFleetInstances` / `DescribeFleetHistory` | no | external | Read fleet state / instances / events | caller | The under-target / ICE oracle for §5.2; template-not-found replenishment oracle for §5.5. Account-scoped. |
| `create-fleet --cli-input-json file://…` | — | **client-side** | Load request body from a local file | — | Client-side only; no `http(s)` scheme; wire-identical to flags → **no server-side injection** (§8). Residual = local file-trust only. |
| `CreateLaunchTemplate` / `…Version` / `DeleteLaunchTemplateVersions` | yes | external | Author / delete template versions (immutable once created) | caller | Pinned-version deletion = §5.5. Template-authoring privesc owned by `ec2-fleet` sibling §5.1. |

**Doc-planted leads kept verbatim:**
- Target page: *"The allocation strategy determines that the On-Demand capacity is always fulfilled, while the balance of the target capacity is fulfilled as Spot if there is available capacity."* → Lens U (§5.2).
- `ec2-fleet-allocation-strategy.html` on the default Spot strategy: *"We don't recommend the lowest price allocation strategy because it has the highest risk of interruption … When using the AWS CLI, this is the default strategy. However, we recommend that you override the default …"* → §5.4 flagship.
- `API_CreateFleet` `Type`: *"The default value is `maintain`."*; `ValidUntil`: *"If no value is specified, the request remains until you cancel it."*; `Context`: *"Reserved."*; `SpotOptions.MaxTotalPrice`: *"If you do not specify this parameter, you will pay the current Spot price."* → §5.4 / §5.6.
- `list_ec2.md` `CreateFleet` row (lines 5113–5123) vs `RunInstances` row (9585–9609); `ec2:InstanceMarketType` definition line 10092 — *"Filters access by the market or purchasing option of an instance (capacity-block, on-demand, or spot)."* → §5.1.

---

## 5. Recommended Areas of Focus (priority order)

Priority = (static IAM guardrail-expressibility gap, safe to confirm, AWS-owned) > (documented-guarantee vs enforcement) > (capacity-split validation) > (AWS-authored sample-config insecure defaults) > (version-pin availability break / undocumented knob).

### 5.1 Purchasing-mix / IMDS / price guardrails are unexpressible on the `CreateFleet` action — **P0 (Lens S / U / X)** — Tier-2 reportable
**Background.** The walkthrough's whole feature is caller-chosen purchasing mix (`OnDemandTargetCapacity` vs Spot balance), allocation strategy, and (implicitly) price. The authoritative `list_ec2.md` `CreateFleet` row (lines 5113–5123) enumerates 8 resource types and a 31-key condition-key union. Critically, compared to `RunInstances` (lines 9585–9609, 49-key union), `CreateFleet` **lacks**:

| Absent key on `CreateFleet` | Role | On `RunInstances` at |
|---|---|---|
| `ec2:InstanceMarketType` | **purchasing option (on-demand / spot / capacity-block)** — the *only* EC2 key matching "purchasing option" (def. line 10092) | `instance*` line 9591 |
| `ec2:MetadataHttpTokens` | **IMDSv2 enforcement** | `instance*` line 9591 |
| `ec2:MetadataHttpEndpoint` / `ec2:MetadataHttpPutResponseHopLimit` | IMDS endpoint / hop limit | `instance*` |
| `ec2:InstanceMetadataTags` / `ec2:InstanceAutoRecovery` / `ec2:ProductCode` | IMDS tags / auto-recovery / marketplace code | `instance*` (±`image`) |

And a whole-document grep proves these keys **do not exist anywhere in EC2** (0 hits): `ec2:AllocationStrategy`, `ec2:MaxPrice`/`SpotPrice`-as-key, `ec2:DefaultTargetCapacityType`, `ec2:FleetType`, `ec2:CapacityType`. The count keys `ec2:InstanceCount`/`ec2:TargetInstanceCount` exist but are wired **only** to Capacity-Reservation actions (lines 4617/4728/5024/… , CR resource-type def 9924) — never `CreateFleet`. (`ec2:InstanceType`, `ec2:Tenancy`, `ec2:RootDeviceType` *are* present on `CreateFleet`'s `instance*`/`image` rows — instance-type guardrails DO work on the fleet path; do not over-claim.)

**Security Concern.** Four guardrails the walkthrough's own feature set implies an admin can set are **structurally impossible to express in IAM for the fleet entry point**:
- "This team may launch On-Demand only, never Spot" (or vice-versa) — no `ec2:InstanceMarketType` on `CreateFleet`.
- "Fleet-launched instances must enforce IMDSv2" — no IMDS keys on `CreateFleet`. (Distinct from the sibling's *runtime* SLR-non-propagation point — this is a **static action-row fact**: even a `Deny CreateFleet` written against the caller can't carry the IMDS condition at all.)
- "Cap the fleet's spend / max price" — no price key exists.
- "Cap `OnDemandTargetCapacity`/`TotalTargetCapacity`" — no fleet-capacity count key exists.
This is the Lens X twin-asymmetry (`RunInstances` checked, its fleet cousin not) **and** Lens U (a guarantee traceable only to orchestration, never to IAM). `DefaultTargetCapacityType:"spot"` is invisible to the action's IAM evaluation — Spot-ness triggers no `spot-instances-request` resource type (that's `RunInstances`/`RequestSpotInstances` only) and no condition.

**High-level Test Scenarios.** All settleable with `iam:SimulateCustomPolicy` — **no fleet created**:
- *Claim:* a `Deny CreateFleet` with `Condition {StringEquals {ec2:InstanceMarketType: spot}}` does not deny a Spot-provisioning fleet. → **Oracle:** simulate; the key is reported not-applicable / the Deny does not match → confirmed inert. **Severity:** High (defeats a no-Spot cost/compliance guardrail for the walkthrough's own feature).
- *Claim:* a `Deny CreateFleet` with `{StringNotEquals {ec2:MetadataHttpTokens: required}}` cannot block an IMDSv1-permitting fleet. → **Oracle:** simulate; key unsupported for the action → inert. **Severity:** Medium-High (SSRF/credential-theft hardening gap at the fleet entry point; chains to the sibling's IMDS-downgrade→IMDS-credential-theft kill chain).
- *Claim:* no policy can cap price/spend, allocation strategy, or target-capacity count on `CreateFleet`. → **Oracle:** simulate policies referencing `ec2:MaxPrice`/`ec2:AllocationStrategy`/`ec2:TargetInstanceCount` on `CreateFleet`; all ignored/unknown. **Severity:** High (price), Medium (strategy/count).
**Doc evidence:** `list_ec2.md` lines 5113–5123 (CreateFleet), 9585–9609 (RunInstances), 10092 (`ec2:InstanceMarketType` def), condition-key catalog 10036–10190 (zero-match grep). **Severity-if-true:** High, **in scope** — AWS-owned structural authz gap; a customer building "we can't launch Spot / we enforce IMDSv2 on all fleets" on IAM is relying on a non-enforceable claim.
**Stop condition:** this is a static-reference finding — Simulate confirms it with no resource touched; stop at the simulator verdict.

### 5.2 "On-Demand capacity is always fulfilled" — guarantee vs enforcement — **P1 (Lens U)**
**Background.** The page asserts *"the On-Demand capacity is always fulfilled, while the balance … is fulfilled as Spot if there is available capacity."* But `ec2-fleet-allocation-strategy.html` scopes the On-Demand allocation strategy to **pool ordering within the On-Demand market** ("lowest priced pool … next lowest priced pool"); nothing in `OnDemandOptionsRequest`, `SpotOptionsRequest`, `CreateFleet`, or `ModifyFleet` describes Spot capacity substituting for an unfulfilled On-Demand target. `errorSet` ("instances that could not be launched") is **"Supported only for fleets of type `instant`"** — and the walkthrough omits `Type`, so it is a `maintain` fleet with no synchronous error surface.
**Security Concern.** "Always fulfilled" is best-effort pool-ordering, not an enforced SLA across markets. A `maintain`/`request` fleet can sit **indefinitely below `OnDemandTargetCapacity`** under an ICE condition with only generic capacity events — a workload architected around "On-Demand = guaranteed baseline" silently runs under-provisioned, and there is no documented distinct alarmable "degraded/under-target" state to detect it. (Availability/trust-assumption mismatch, not a cross-boundary compromise.)
**High-level Test Scenarios.**
- *Claim:* a `maintain` fleet in a capacity-constrained type/AZ with `OnDemandTargetCapacity` above available capacity stays permanently under target with no first-class degraded state. → **Oracle:** create such a fleet (cheap type, constrained AZ), poll `DescribeFleets`/`DescribeFleetHistory`; confirmed if only generic "capacity-not-available" events appear and no alarmable health state distinguishes it from healthy. **Severity:** Medium.
- *Claim:* there is no cross-market substitution (Spot is never used to fill the On-Demand shortfall, nor vice-versa). → **Oracle:** inspect launched-instance `InstanceLifecycle`/market vs the requested split. **Severity:** Informational (confirms the guarantee's true scope).
**Doc evidence:** target page; `ec2-fleet-allocation-strategy.html`; `manage-ec2-fleet.html`; `API_CreateFleet` (`errorSet` instant-only). **Severity-if-true:** Medium (Lens U enforcement gap). **Stop condition:** once the under-target steady state + absent-signal are observed, record and tear down.

### 5.3 Capacity-split validation gaps (`OnDemand > Total`, redundant default+explicit, scale-down asymmetry) — **P1 (Lens U / business-logic)**
**Background.** `API_TargetCapacitySpecificationRequest`: `TotalTargetCapacity` (required) "filled using the default target capacity type"; `DefaultTargetCapacityType` (`spot|on-demand|capacity-block|reserved-capacity`, not required); `OnDemandTargetCapacity`/`SpotTargetCapacity` (not required). **No page documents** the validation behavior when `OnDemandTargetCapacity > TotalTargetCapacity`, nor the precedence when `DefaultTargetCapacityType=on-demand` is set *alongside* an explicit `OnDemandTargetCapacity`/`SpotTargetCapacity`. `API_ModifyFleet` scale-down prose mentions terminating **Spot** instances only — the fate of excess **On-Demand** on scale-down is undocumented.
**Security Concern.** The service may silently accept a logically-inconsistent split and build a fleet whose actual mix diverges from caller intent — a cost/configuration-integrity issue, most relevant to IaC generators computing this JSON programmatically and to a lower-priv caller operating under a budget/quota an operator sized on the submitted numbers.
**High-level Test Scenarios.**
- *Claim:* `CreateFleet` (type `instant`, cheapest type, `TotalTargetCapacity:1`, `OnDemandTargetCapacity:5`) is accepted/clamped rather than cleanly rejected. → **Oracle:** record exact `ValidationError`/`InvalidParameterValue` text or the actual provisioned count. **Severity:** Low-Medium.
- *Claim:* redundant `DefaultTargetCapacityType=on-demand` + explicit conflicting `SpotTargetCapacity` has no stated precedence and resolves surprisingly. → **Oracle:** submit, compare provisioned mix to each interpretation.
- *Claim:* `ModifyFleet` scale-down on a mixed fleet terminates only Spot, stranding paid On-Demand above the new target. → **Oracle:** scale a mixed `maintain` fleet down; inspect which lifecycle instances are terminated.
**Doc evidence:** `API_TargetCapacitySpecificationRequest`, `API_CreateFleet`, `API_ModifyFleet`. **Severity-if-true:** Low-Medium (cost/config integrity). **Stop condition:** use `instant` + `TotalTargetCapacity:1` to minimize spend; terminate on observation.

### 5.4 The published minimal `config.json` silently builds a "forgotten self-healing fleet" — **P1 (Lens R / U)** — Tier-2 reportable
**Background.** The tutorial's `config.json` omits every optional field, each inheriting a default (verbatim from `API_CreateFleet`/`…Options`/allocation-strategy):

| Omitted field | Inherited default | Security/cost relevance |
|---|---|---|
| `Type` | **`maintain`** | Self-replenishing, runs indefinitely |
| `ValidUntil` | **"remains until you cancel it"** (never expires) | No auto-termination path |
| `ValidFrom` | start immediately | — |
| `SpotOptions.AllocationStrategy` | **`lowest-price`** — AWS: *"not recommended … highest risk of interruption"* | **Flagship**: the published default *is* the strategy AWS tells you to override |
| `OnDemandOptions.AllocationStrategy` | `lowest-price` | benign for On-Demand |
| `SpotOptions.MaxTotalPrice` | **none → "you will pay the current Spot price"** (no cap) | Unbounded Spot cost |
| `OnDemandOptions.MaxTotalPrice` | none (no cap) | Unbounded On-Demand cost; a later `ModifyFleet` scale-up has no backstop |
| `SpotOptions.InstanceInterruptionBehavior` | **`terminate`** | Interrupted Spot destroyed, not paused |
| `SpotOptions.MaintenanceStrategies` | absent | No capacity-rebalance handling |
| `TerminateInstancesWithExpiration` / `ReplaceUnhealthyInstances` / `ExcessCapacityTerminationPolicy` | **unstated in `CreateFleet` text** | Flag empirically — termination-affecting flags with no documented default |
| `TagSpecification` | none | No cost-allocation/ownership tag → hampers later attribution & cleanup |

**Security Concern.** `Type=maintain` + `ValidUntil=∞` + no `MaxTotalPrice` + `lowest-price` Spot together produce exactly the "forgotten fleet that never dies" shape — an indefinitely-running, self-healing, uncapped-cost fleet with the highest-interruption Spot strategy, created by copying an **AWS-authored sample config verbatim**. Under the Lens R/U carve-out an insecure default in an AWS-published copy-verbatim artifact is in scope (Tier-2) — distinct from a customer-authored footgun. The flagship sub-finding is that the tutorial's silent default *is* the strategy AWS's own allocation-strategy page explicitly warns against.
**High-level Test Scenarios.**
- *Claim:* a verbatim-config fleet is `maintain`, has no `ValidUntil`, uses `lowest-price` Spot, and has no price cap. → **Oracle:** `DescribeFleets` on a fleet created from the exact published JSON; read back `Type`, `ValidUntil`, `SpotOptions.AllocationStrategy`, `MaxTotalPrice`. Confirmed if all match the defaults above. **Severity:** Medium (AWS-authored sample insecure/footgun defaults).
- *Claim:* the unstated-default flags (`TerminateInstancesWithExpiration`, `ReplaceUnhealthyInstances`, `ExcessCapacityTerminationPolicy`) resolve to values worth documenting. → **Oracle:** create and read back; record the empirical defaults (closes the doc gap).
**Doc evidence:** target `config.json`; `API_CreateFleet`; `API_OnDemandOptionsRequest`; `API_SpotOptionsRequest`; `ec2-fleet-allocation-strategy.html` lowest-price warning. **Severity-if-true:** Medium, in scope (Tier-2 AWS-authored sample). **Stop condition:** read-back via Describe is enough; delete immediately (it will not expire on its own).

### 5.5 Numeric version pin — safe-pattern delta + latent replenishment break — **P2 (Lens U / availability)**
**Background.** The walkthrough pins `"Version": "2"` (numeric) — the integrity-safe counterpart to the `$Latest`/`$Default` late-binding the `ec2-fleet` sibling (§5.1) treats as the PassRole-bypass risk. Launch-template versions are **immutable** (`manage-launch-template-versions.html`: "after you create a launch template, you can't modify it"), so a pinned version's *content* cannot be swapped under the fleet — the integrity property holds and this is correctly the mitigation. **But** `delete-launch-template.html`: "You can't replace the version number after you delete it" and "Deleting a launch template or launch template version doesn't affect any instances that you've launched." A `maintain` fleet **re-resolves the version reference at each replenishment launch**.
**Security Concern.** If the pinned version `2` is deleted after fleet creation (e.g. a cleanup process pruning "old" versions, unaware a live fleet still references it): already-running instances are unaffected, but any future Spot-replenishment or `ModifyFleet` scale-up permanently fails — and the docs state no deletion-time cross-check that warns a live fleet still depends on the version. A latent availability break of the exact "safe pattern" the sibling plans endorse.
**High-level Test Scenarios.**
- *Claim:* `delete-launch-template-versions` deletes a version still referenced by a live `maintain` fleet without warning/blocking. → **Oracle:** create `maintain` fleet pinned to vN; delete vN; confirm the delete is allowed with no live-fleet cross-check. **Severity:** Medium.
- *Claim:* subsequent replenishment/scale-up fails. → **Oracle:** force a Spot interruption or `ModifyFleet` scale-up; observe a template-version-not-found error in `DescribeFleetHistory`. **Severity:** Medium (availability/config-drift).
**Doc evidence:** `manage-launch-template-versions.html`, `delete-launch-template.html`, `API_CreateFleet`/`API_ModifyFleet` (launch-time-only version validation). **Stop condition:** observe the delete-allow + replenish-failure once; tear down.

### 5.6 `Context` ("Reserved.") undocumented parameter — **P3 (Step-3 undocumented-knob discipline)**
**Background.** `API_CreateFleet` and `API_ModifyFleet` both list a `Context` string parameter documented only as **"Reserved."** — no stated default, effect, or validation. Per the skill's Step-3 mandate to hunt console-hidden/undocumented knobs, an accepted string field with no stated behavior is exactly the shape to probe.
**Security Concern.** Unknown. Possible internal routing/metadata behavior; most likely inert. Record whether it is accepted, echoed in `DescribeFleets`, length/charset-validated, or produces any observable side effect.
**High-level Test Scenarios.** *Claim:* `Context` is accepted and acted on in some way. → **Oracle:** `CreateFleet` with a benign marker string in `Context`; read back via `DescribeFleets`; test oversize/injection-shaped values for differential validation. **Severity:** Informational unless a side effect appears. **Stop condition:** no side effect → close as inert; any surprising behavior → preserve and escalate.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| No-Spot / On-Demand-only guardrail bypass | `ec2:CreateFleet` IAM | `ec2:InstanceMarketType` — **absent from the action row** (present on `RunInstances`) |
| IMDSv2-enforcement guardrail bypass at the fleet boundary | `ec2:CreateFleet` IAM | `ec2:MetadataHttpTokens`/`-Endpoint`/`-HopLimit` — absent from `CreateFleet` |
| Price / spend / strategy / count cap | `ec2:CreateFleet` IAM | No such condition key exists anywhere in EC2 |
| "On-Demand always fulfilled" under ICE | fleet fulfillment / allocation strategy | Pool-ordering within On-Demand only; `errorSet` is `instant`-only — no `maintain` degraded-state signal |
| Inconsistent capacity split accepted | `CreateFleet`/`ModifyFleet` validation | Undocumented for `OnDemand>Total` & redundant default+explicit |
| Forgotten self-healing uncapped fleet | published `config.json` defaults | `Type=maintain`, `ValidUntil=∞`, `lowest-price` Spot, no `MaxTotalPrice` (AWS-authored sample) |
| Pinned-version deletion → replenishment break | launch-template version lifecycle | Immutability (holds for content); no deletion-time live-fleet cross-check |
| `Context` reserved-knob side effect | `CreateFleet`/`ModifyFleet` | Documented only as "Reserved." |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Launch-template `$Latest`/`$Default` late-binding → PassRole bypass, the AWS-authored sample user policy privesc, the SLR actual-policy audit, KMS grants, `instant`-fleet overrides, and the generic runtime "RunInstances conditions don't propagate to the SLR launch"** — all owned by `ec2-fleet-attack-research-plan.md`; cross-referenced, not re-derived.
- **Capacity-Reservation consumption, instance weighting, cross-account/Org trust, the CR condition-key gaps, and the EC2 Org-key absence** — owned by `fleet-tutorials-attack-research-plan.md` (this page's hub).
- **Pure single-account cost footguns a customer sets on their own fleet** (self-chosen `lowest-price`, no `MaxTotalPrice`) — out of scope **except** where (a) the weak value is the default inherited from the **AWS-published tutorial config** (§5.4, Tier-2), or (b) a lower-priv principal triggers them under a budget/SCP/quota the operator sized on the submitted split (§5.3).
- **`--cli-input-json` as a server-side injection vector** — N/A: client-side file load only, no `http(s)` scheme, wire-identical to flags (§8). Residual local-file-trust is a workstation/CI supply-chain concern, not an EC2 API issue.
- **Classic cross-tenant IDOR; SSRF; translation/wire-protocol injection; prompt injection; attestation; canonicalization/parser-differential; trusted-header; cache-key; token/JWT** — N/A for this surface (§8).
- **AWS service plane / SLR live credentials** — hard stop, read-only only.

## 8. Null Hypotheses / Doc Gaps (lenses checked, pages named)
- **Lens G (SSRF) — N/A.** Read the target page, `create-ec2-fleet`, `ec2-fleet-allocation-strategy`, `manage-ec2-fleet`, `cli-usage-parameters-file`: the only location-shaped input is `file://config.json`, resolved **client-side** by the CLI (no `http(s)` scheme on the generic parameter-file path). No field the *service* dereferences. **Confirmed N/A.**
- **Lens F / K / W / BB / CC / DD / FF — N/A.** No translator/parser/wire-protocol, no LLM/agent, no enclave/`kms:RecipientAttestation`, no authorizer/WAF/CDN/edge/cache layer, no JWT/OIDC in front of the SigV4 `CreateFleet` API. (Matches the sibling plans' verdicts for this service.)
- **Lens A (cross-tenant IDOR) — N/A.** The fleet, its instances, and the SLR all live in the caller's own account; no resource-by-foreign-ID path on this page. (Cross-account surface = shared CRs, owned by the hub plan.)
- **Lens EE (predictable-name land-grab) — N/A.** No global/predictable namespace resolved by this page; the launch template is referenced by caller-owned ID + pinned version.
- **Key doc-gaps for the hunter to settle live:**
  1. `maintain`/`request` fleet behavior under On-Demand ICE — is there any first-class degraded/under-target state, or only generic events? (gates §5.2)
  2. Validation of `OnDemandTargetCapacity > TotalTargetCapacity` and of redundant `DefaultTargetCapacityType` + explicit per-type capacity — reject / clamp / silent? (gates §5.3)
  3. Empirical defaults of `TerminateInstancesWithExpiration`, `ReplaceUnhealthyInstances`, `ExcessCapacityTerminationPolicy` (unstated in `CreateFleet` text). (gates §5.4)
  4. Does `delete-launch-template-versions` cross-check live-fleet references before allowing deletion of a pinned version? (gates §5.5)
  5. Any observable effect of `Context` ("Reserved."). (gates §5.6)

---

### Kill-chain candidates (rate at the end of the chain)
- **§5.1 IMDS-key gap** (no `ec2:MetadataHttpTokens` on `CreateFleet`) → fleet launches with `HttpTokens=optional` despite an org IMDSv2 Deny → IMDSv1 reachable on launched instances → **SSRF-to-IMDS credential theft** of the attached instance-profile role. End severity: High. (Joins the `ec2-fleet` sibling's §5.3 IMDS-downgrade kill chain from the static-IAM side.)
- **§5.1 purchasing-option-key gap** (no `ec2:InstanceMarketType`) → a caller an admin believes is restricted to On-Demand provisions Spot capacity at scale under `lowest-price` with no price cap (§5.4 defaults) → cost blast with the highest interruption rate. End severity: High (cost + availability).

---
*Page-level deep-dive child of `fleet-tutorials-attack-research-plan.md` (hub) and companion to `ec2-fleet-attack-research-plan.md` (core create path). Owns the On-Demand-primary mixed-purchasing-option configuration surface of `ec2-fleet-on-demand-walkthrough.html`: the static `CreateFleet` IAM guardrail-expressibility gap (`ec2:InstanceMarketType`/IMDS/price absent), the "On-Demand always fulfilled" Lens-U guarantee, capacity-split validation, the published-config "forgotten self-healing fleet" defaults, and the numeric-version-pin availability delta. Cross-references siblings for launch-template/PassRole/SLR/KMS and CR/weighting depth it deliberately does not restate.*
