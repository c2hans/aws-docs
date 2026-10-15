# EC2 Fleet — Example CLI Configurations — Attack Research Plan
Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-examples.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-fleet-examples.md`, confirmed offline==online 2026-10-15). Supporting pages read: `ec2-fleet-capacity-rebalance.md`, `rebalance-recommendations.md`, `ec2-fleet-request-type.md`, `ec2-fleet-prerequisites.md`, `modify-ec2-fleet.md`, `create-ec2-fleet.md`, `monitor-ec2-fleet-using-eventbridge.md`, API refs `API_CreateFleet` / `API_SpotOptionsRequest`, and the IAM Service Authorization Reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`.
Status: documentation-derived hypotheses only; nothing tested against a live account.

> **What this page is, and what this plan owns.** `ec2-fleet-examples.html` is a **catalog of 12 copy-verbatim `create-fleet --cli-input-json` example configs**. Eleven of the twelve examples re-use mechanisms already deep-dived by sibling plans (CR-consumption, instance-weighting, on-demand-primary, multi-CR-types, the `instant`-vs-`maintain` backbone). This plan therefore does **not** restate those — it **cross-references** them (§5 Areas P1–P5 are thin pointers) and develops only the **two surfaces this page uniquely introduces into the fleet corpus**:
> 1. **Capacity Rebalancing** (Example 7 — `MaintenanceStrategies.CapacityRebalance`, `launch-before-terminate`, `TerminationDelay`, `ExcessCapacityTerminationPolicy`). **No prior sibling plan covers this mechanism.** This is the headline (Area 1).
> 2. The **Spot allocation-strategy & capacity-sizing knobs** surfaced by Examples 8/9/10 (`capacity-optimized` / `-prioritized` / `price-capacity-optimized`, `Priority`, `MinTargetCapacity`, `SingleInstanceType`, `MaxTotalPrice`) and their total IAM-unscopability (Area 2).
> Plus the **examples-page-as-AWS-authored-artifact** doc-integrity surface (Area 3), where this plan is the natural owner because the page's entire purpose is "copy this JSON verbatim."

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **Backbone fact (load-bearing for which lens applies).** `API_CreateFleet` `Type` **default = `maintain`** (verbatim "The default value is `maintain`."; `ec2-fleet-request-type.md:21` "`maintain` (default)"). So the examples that **omit `Type`** — **Examples 1, 2, 3, 7, 8, 9** — are **`maintain`** fleets, launched/terminated by the **service-linked role `AWSServiceRoleForEC2Fleet`**, NOT the caller. The **SLR-non-propagation backbone finding** (the caller's identity-policy `RunInstances`/`TerminateInstances` condition keys do NOT bind the SLR's launches/terminations — see `ec2-fleet-attack-research-plan.md`) **APPLIES to those six**. Examples **4, 5, 6, 10, 11, 12** set `Type:instant` → run under the **caller's own identity** (SLR N/A; caller conditions WOULD bind — cross-ref the targeted-CR / capacity-blocks / multi-CR-types siblings' "Area 0").
- `AWSServiceRoleForEC2Fleet` grants (verbatim `ec2-fleet-prerequisites.md:22-29`): `ec2:RunInstances`, `ec2:RequestSpotInstances`, `ec2:TerminateInstances`, `ec2:DescribeImages`/`DescribeInstanceStatus`/`DescribeSubnets`/`CreateTags`. Line 33-34: "An `instant` EC2 Fleet does not require this role."
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives
Concrete breach outcomes a hunter should try to produce from the surfaces this page uniquely introduces:
1. Demonstrate that **no IAM policy an admin can write on `CreateFleet` can forbid, require, or bound Capacity Rebalancing** — in particular cannot cap `TerminationDelay`, cannot forbid `ReplacementStrategy=launch`, cannot forbid `ExcessCapacityTerminationPolicy=termination` — proving these are governance-blind footguns in an AWS-authored copy-verbatim example.
2. Demonstrate the **cost-amplification / dual-billing primitive**: a `maintain`+CapacityRebalance fleet that can concurrently bill up to **2× target capacity** for up to **2 hours** per rebalance (`launch-before-terminate`), or **indefinitely** (`launch`), under the SLR, with the caller holding only `ec2:CreateFleet`.
3. Demonstrate (or refute via live canary) the **launch-template-version redirect** on rebalance replacement: whether a `maintain`+CapacityRebalance fleet re-resolves `$Latest`/`$Default` on every rebalance-driven replacement, letting an LT-editor (no `CreateFleet`/`PassRole`) steer the IAM-profile/UserData/AMI/SG of every future replacement instance.
4. Settle whether the page's **AWS-authored example JSON is copy-safe** (Example 5 is syntactically invalid; several examples ship AWS's own "not recommended" `lowest-price` default and the `lowest-price`+`launch-before-terminate` combination AWS "strongly recommends against").
5. Confirm the **detection blind spot**: rebalancing produces no single correlatable EventBridge event (no `rebalanced` sub-type; two uncorrelated best-effort streams).

## 2. Components, Assets, and Design
- **Interface.** `aws ec2 create-fleet --cli-input-json file://{{file.json}}` (page top). The `file://` is a **client-side botocore file load, not a server fetch** → NOT an SSRF vector (resolved by `ec2-fleet-on-demand-walkthrough-attack-research-plan.md`; wire-identical to inline flags). Underlying API: `CreateFleet` (SigV4 IAM).
- **Actors / identities.**
  - *Caller* — holds `ec2:CreateFleet` (sample user policy `ec2-fleet-prerequisites.md:85-130` grants `ec2:*` on `*` + `iam:PassRole`/`ListRoles`/`ListInstanceProfiles`).
  - *SLR* `AWSServiceRoleForEC2Fleet` — executes `RunInstances`/`RequestSpotInstances`/`TerminateInstances` for **maintain/request** fleets (Examples 1,2,3,7,8,9).
  - *Amazon EC2 Spot* — emitter of the **rebalance recommendation** (`source: aws.ec2`, `detail-type: EC2 Instance Rebalance Recommendation`), the external trigger for Capacity Rebalancing.
- **The 12 example configs (asset inventory).**

  | # | Anchor | Type (resolved) | Runs under | Net-new to this page? | Owner plan |
  |---|---|---|---|---|---|
  | 1 | config1 | maintain (default) | SLR | no | on-demand / ec2-fleet |
  | 2 | config2 | maintain (default) | SLR | no | on-demand |
  | 3 | config3 | maintain (default) | SLR | no | **on-demand walkthrough** |
  | 4 | config5 | instant | caller | no | targeted-CR / hub |
  | 5 | config6 | instant | caller | no (+**broken JSON**, Area 3) | targeted-CR / hub |
  | 6 | config7 | instant | caller | no | **targeted-CR walkthrough** |
  | **7** | **config8** | **maintain (default)** | **SLR** | **YES — Capacity Rebalancing (Area 1)** | **this plan** |
  | **8** | **config9** | **maintain (default)** | **SLR** | **YES — allocation strategy (Area 2)** | **this plan** |
  | **9** | **config10** | **maintain (default)** | **SLR** | **YES — `Priority` (Area 2)** | **this plan** |
  | **10** | **config11** | **instant** | **caller** | **YES — `MinTargetCapacity`/`SingleInstanceType` (Area 2)** | **this plan** |
  | 11 | config12 | instant | caller | partly (InstanceRequirements) | **instance-weighting walkthrough** |
  | 12 | config13 | instant | caller | no (ReservedCapacityOptions) | **multiple-cr-types walkthrough** |

- **DRIFT NOTE (memory correction).** Prior corpus memory recorded `ReservedCapacityOptions` / `DefaultTargetCapacityType:reserved-capacity` as **absent from `ec2-fleet-examples.md`**. As of 2026-10-15 it is **present** (Example 12, offline line 767, offline==online). The page was updated to add Example 12. The multiple-cr-types capstone sibling still owns that structure's analysis.

## 3. API / Interface Inventory
| Name | Method | Mutating | Ext-facing | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `CreateFleet` | SigV4 | **yes** | yes | yes | `ec2:CreateFleet` holders | the one mutating action every example calls; carries the nested `SpotOptions.MaintenanceStrategies.CapacityRebalance`, `ExcessCapacityTerminationPolicy`, `SpotOptions.AllocationStrategy`/`MinTargetCapacity`/`SingleInstanceType`/`MaxTotalPrice`, `OnDemandOptions`, `ReservedCapacityOptions` |
| `ModifyFleet` | SigV4 | yes | yes | yes | `ec2:ModifyFleet` holders | **maintain-only**; `ExcessCapacityTerminationPolicy` governs scale-down termination here — owned by `modify-ec2-fleet-attack-research-plan.md` |
| `DescribeCapacityReservations` | SigV4 | no | yes | yes | `ec2:DescribeCapacityReservations` | the CR-remaining-count read-back shown in Examples 4/5/6 — unscopable oracle, owned by hub/targeted-CR siblings |
| rebalance recommendation (EventBridge) | push | n/a | n/a | n/a | account default bus | `source: aws.ec2`, instance-level, best-effort (`rebalance-recommendations.md`) |
| fleet events (EventBridge) | push | n/a | n/a | n/a | account default bus | maintain/request only; **no `rebalanced` sub-type** (`monitor-ec2-fleet-using-eventbridge.md`) |

**Console-hidden / undocumented knob sweep:** `Context` param on `CreateFleet` = "Reserved." (undocumented; carried open across the corpus). `TerminationDelay` is passed as a **JSON string** (`"720"`) not an int — a type-coercion edge worth a glance but low value. No auth/isolation-weakening enum found that the console hides for this page's fields.

## 4. Trust-Boundary Map
| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller (`ec2:CreateFleet` only) | SLR-driven `RunInstances`/`TerminateInstances` | maintain fleet + CapacityRebalance | Caller causes instance **termination + relaunch** (and up to 2× billing) **without holding `ec2:TerminateInstances`/`RunInstances`** — the SLR's permission, not the caller's, is exercised. In-scope as a **customer least-priv footgun amplified by an AWS-authored example**; the SLR policy itself is AWS-authored (Lens R/S) |
| LT-editor (`ec2:ModifyLaunchTemplate`/`CreateLaunchTemplateVersion`, no `CreateFleet`) | every future replacement instance of a live rebalancing fleet | `$Latest`/`$Default` re-resolution on rebalance replacement (**doc-gap**) | A replacement instance launched after an LT default-version swap runs the attacker's IAM-profile/UserData/AMI → intra-account privesc. Oracle = live canary (see Area 1 §E1) |
| Admin authoring an IAM policy | `CreateFleet` rebalance/strategy/termination knobs | IAM condition-key evaluation | Admin **cannot** author any `Deny`/`Condition` that forbids rebalance, caps `TerminationDelay`, or forbids `ExcessCapacityTerminationPolicy=termination` — `SimulateCustomPolicy` shows every candidate key is inert/absent (Area 1 §D, Area 2) |
| Defender (EventBridge/CloudTrail) | rebalance churn visibility | event correlation | No single event attributes a replacement to a rebalance; two best-effort streams, no shared correlation id; CloudTrail SLR-attribution undocumented (Area 1 §F) |
| Any customer surface | AWS service plane | — | **HARD STOP** if any SLR/service-plane credential or ARN is reachable |

---

## 5. Recommended Areas of Focus

### Area 1 — Capacity Rebalancing: governance-blind SLR-driven churn + dual-billing primitive (Example 7) — **HEADLINE, net-new to the corpus**
**Lenses:** S (condition-key absence) · U (doc-guarantee vs enforcement) · B/E (LT late-binding privesc) · L (cost/resource) · O (audit evasion) · R (AWS-authored SLR artifact).

**Background.** Example 7 (`ec2-fleet-config8`) is the only example that configures `SpotOptions.MaintenanceStrategies.CapacityRebalance`. It sets `ReplacementStrategy: "launch-before-terminate"`, `TerminationDelay: "720"`, and top-level `ExcessCapacityTerminationPolicy: "termination"`, and **omits `Type`** → inherits **`maintain`** (the *only* type Capacity Rebalancing supports — `ec2-fleet-capacity-rebalance.md:29` "Capacity Rebalancing is available only for fleets of type `maintain`"). A rebalance recommendation from Amazon EC2 Spot (`ec2-fleet-capacity-rebalance.md:8`) triggers the SLR to **launch a replacement and terminate the at-risk instance**.

**Security Concern.** For a maintain fleet, both the replacement **launch** and the old-instance **termination** are executed by `AWSServiceRoleForEC2Fleet`, not the caller (`ec2-fleet-prerequisites.md:22-34`). A principal holding **only `ec2:CreateFleet`** (no `ec2:TerminateInstances`, no `ec2:RunInstances`) thereby arms an automatic, SLR-driven terminate-and-relaunch loop and a dual-billing amplifier — and **no IAM mechanism exists to govern any of it**.

**High-level Test Scenarios (falsifiable claims):**

- **§D (Lens S/U) — Claim: no condition key can forbid/require/bound Capacity Rebalancing.**
  Mechanism: grep of all 10,190 lines of `list_ec2.md` for `rebalance|replacementstrategy|terminationdelay|excesscapacity|maintenancestrateg` = **ZERO matches** (confirmed). `CreateFleet`'s rows (list_ec2 5113-5124) carry only generic per-resource keys (`aws:ResourceTag`, `ec2:Region`, `ec2:InstanceType`, `ec2:AvailabilityZone`, …) — none reference the rebalance/termination structures.
  Confirm/Refute oracle: `iam:SimulateCustomPolicy` with a `Deny CreateFleet` conditioned on any candidate key (e.g. a hypothetical `ec2:ReplacementStrategy`) → the key is **inert/unrecognized**, the `CreateFleet` still simulates `allowed`, proving the guardrail is unexpressible. No resource created.
  Severity-if-true: Low–Medium (governance gap in an AWS-authored copy-verbatim example — Tier-2 reportable as a doc/enforcement gap, not a customer footgun, because the example ships the shape).

- **§E-cost (Lens L) — Claim: a `CreateFleet`-only principal can concurrently bill up to 2× target capacity for up to 2 hours per rebalance, or indefinitely.**
  Mechanism: `launch-before-terminate` holds old+new simultaneously for `TerminationDelay` (**min 120s, max 7200s**, `ec2-fleet-capacity-rebalance.md:38`); the fleet "can launch new replacement Spot Instances until fulfilled capacity is **double target capacity**" (lines 70-74). `launch` strategy **never auto-terminates** the old instance ("you continue paying for them while they are running", lines 43/78) → unbounded double-billing until a human acts. "You are charged for all instances while they are running" (Example 7 note, line 477).
  Confirm/Refute oracle: live canary maintain fleet (synthetic, cheap instance types), induce/await a rebalance (or inspect metering) → observe concurrent billed count exceeding target by up to the replacement set, persisting for the delay (or indefinitely under `launch`).
  Preconditions: `ec2:CreateFleet`; SLR pre-exists. Cost: real $ (small with t-class canaries). Severity: Medium (single-tenant cost-DoS / self-inflicted; **not** cross-tenant). In scope specifically because the AWS example ships `launch-before-terminate` with no `MaxTotalPrice` cap.

- **§E1 (Lens B/E) — Claim: an LT-editor with no `CreateFleet`/`PassRole` can redirect every future rebalance replacement.**
  Mechanism: `CreateFleet` resource-level IAM "do not include the resources specified in a launch template" (list_ec2 5114) → LT contents are un-scopable on the fleet path; replacement launches are SLR `RunInstances`. If the fleet references `$Latest`/`$Default` (the idiomatic pattern — see `ec2-fleet-instance-weighting-walkthrough-attack-research-plan.md` Area 2), each rebalance replacement may re-resolve the LT default version. **Doc-gap:** docs do not state whether rebalance replacements pin the CreateFleet-time version or re-resolve.
  Confirm/Refute oracle: live canary — create a `maintain`+CapacityRebalance fleet referencing `$Default`; after launch, `ModifyLaunchTemplate` the default to a new version with an attacker IamInstanceProfile/UserData; induce a rebalance; inspect whether the replacement instance carries the new version's profile. (`DryRun` is caller-IAM-only, cannot answer.)
  Severity-if-true: Medium–High (intra-account privesc; same shape as instance-weighting Area 2 but fired automatically and repeatedly by rebalancing). **Cross-ref, do not re-derive, the $Latest/$Default late-binding analysis in the instance-weighting sibling.**

- **§E2 (Lens U) — Claim: `lowest-price` (AWS's own default allocation strategy) + `launch-before-terminate` is the combination AWS "strongly recommends against", yet nothing prevents it.**
  Mechanism: `API_SpotOptionsRequest` `AllocationStrategy` **Default: `lowest-price`** labelled "**(not recommended) … highest risk of interruption**"; `ec2-fleet-capacity-rebalance.md:40` "We **strongly recommend against** using the `lowest-price` … allocation strategy in combination with `launch-before-terminate` to avoid having replacement Spot Instances that are also at an elevated risk of interruption." A fleet that omits `SpotOptions.AllocationStrategy` but sets `launch-before-terminate` lands in exactly the recommended-against state by default.
  Oracle: documentation-confirmed; a hunter demonstrates the default-into-antipattern by omitting `AllocationStrategy`. Severity: Low (doc/UX hazard; AWS-owned).

- **§F (Lens O) — Claim: rebalance-driven churn is not correlatably observable.**
  Mechanism: maintain fleets emit EventBridge events, but `EC2 Fleet Instance Change` has sub-types only `launched`/`terminated`/`termination_notified` — **no `rebalanced` sub-type** (`monitor-ec2-fleet-using-eventbridge.md:223-446`); the rebalance signal itself is a separate instance-level `aws.ec2` stream, both "best effort" (delivery not guaranteed). No shared correlation id ties a replacement launch to the recommendation that caused it. CloudTrail attribution of the SLR's `RunInstances`/`TerminateInstances` (userIdentity = SLR vs fleet) is undocumented.
  Oracle: subscribe both streams on a canary; confirm no field correlates a `terminated`/`launched` pair to a specific recommendation. Severity: Low–Informational (detection enabler).

**Doc evidence:** `ec2-fleet-examples.md:471-510`; `ec2-fleet-capacity-rebalance.md:8,29,35-43,70-78`; `ec2-fleet-prerequisites.md:22-34`; `API_CreateFleet` (Type default, ExcessCapacityTerminationPolicy maintain-only); `list_ec2.md` (zero rebalance keys). **Severity-if-true (area):** Medium (cost + intra-account privesc), with a Tier-2 governance-gap reportable (§D).

### Area 2 — Allocation-strategy & capacity-sizing knobs are entirely IAM-unscopable (Examples 8, 9, 10)
**Lenses:** S · U · L.

**Background.** Examples 8/9/10 introduce `SpotOptions.AllocationStrategy` = `capacity-optimized` / `capacity-optimized-prioritized` / `price-capacity-optimized`, the per-override `Priority` field (Example 9), and (Example 10) `MinTargetCapacity: 2` + `SingleInstanceType: true` plus explicit `OnDemandTargetCapacity:0`/`SpotTargetCapacity:50`.

**Security Concern.** None of these knobs — nor `lowest-price`, `MaxTotalPrice`, `InstancePoolsToUseCount`, `MinTargetCapacity`, `SingleInstanceType`, `SingleAvailabilityZone` — has **any** IAM condition key. Grep of `list_ec2.md` for `allocationstrategy|mintargetcapacity|singleinstancetype|ec2:priority` = **ZERO** (confirmed; consistent with `ec2-fleet-on-demand-walkthrough-attack-research-plan.md` Area 1 "no price/strategy key exists anywhere"). An admin cannot pin a fleet to a safe strategy, forbid `lowest-price`, cap `MaxTotalPrice`, or require a minimum/maximum sizing.

**High-level Test Scenarios:**
- **Claim (Lens U): `MaxTotalPrice` is a cap that is not a cap.** `API_SpotOptionsRequest` `MaxTotalPrice`: "does **not** account for surplus credits, and, if you use surplus credits, your final cost **might be higher than what you specified for `MaxTotalPrice`**" (T-unlimited instances). A compliance/budget control built on `MaxTotalPrice` can be silently exceeded. Oracle: documentation-confirmed; live canary with a T-unlimited type over baseline shows billing > cap. Severity: Low–Medium (AWS-owned doc/enforcement gap; cost).
- **Claim (Lens L): `MinTargetCapacity` is an all-or-nothing availability switch.** `API_SpotOptionsRequest`: "If this minimum capacity isn't reached, **no instances are launched**." (instant-only; max 1000; requires `SingleAvailabilityZone` or `SingleInstanceType`). An adversarial or mis-copied `MinTargetCapacity` set high → the fleet silently launches **zero**. Oracle: `create-fleet` with a `MinTargetCapacity` above available pool capacity → empty `fleetInstanceSet`, no error beyond `errorSet`. Severity: Low (self-inflicted availability footgun).
- **Claim (Lens S): no key can forbid `lowest-price`.** As above. Oracle: `SimulateCustomPolicy` — a `Deny` on a hypothetical strategy key is inert. Severity: Low.

**Doc evidence:** `ec2-fleet-examples.md` Examples 8-10 (lines ~531-660); `API_SpotOptionsRequest` (defaults, MinTargetCapacity, MaxTotalPrice surplus-credit caveat); `list_ec2.md` (zero keys). **Severity-if-true:** Low–Medium, cost/availability, single-tenant. Mostly out-of-scope as self-config EXCEPT the AWS-owned Lens-U facts (`lowest-price` default, `MaxTotalPrice`-isn't-a-cap) which are reportable.

### Area 3 — The examples page as an AWS-authored copy-verbatim artifact (doc-integrity)
**Lenses:** U (doc-vs-reality) · R (AWS-authored artifact).

**Background.** The entire page instructs the reader to copy JSON verbatim into `create-fleet --cli-input-json`. Weak or broken defaults here are **AWS's defect**, not the customer's, because the customer copies as-is.

**High-level Test Scenarios:**
- **Claim: Example 5 is invalid JSON and fails on copy-verbatim.** `ec2-fleet-examples.md:328` `"AllocationStrategy": "lowest-price"` has **no trailing comma** before line 329 `"CapacityReservationOptions"`, and line 333 `"Type": "instant",` has a **trailing comma** before the closing brace (line 334). Two syntax errors; offline==online. A reader copying Example 5 gets a parse error. Oracle: `python -c 'import json,sys; json.load(...)'` on the block → `JSONDecodeError`. Severity: **Informational** (fail-closed; AWS-owned doc defect; worth filing).
- **Claim: multiple examples ship AWS's own "not recommended" `lowest-price`** (Examples 4, 5, 6 On-Demand `lowest-price`; the implicit Spot default) and the recommended-against `lowest-price`+`launch-before-terminate` pairing (Area 1 §E2). Severity: Low (hazardous default in a copy-verbatim artifact).
- **Claim: `{{placeholder}}` templating is inconsistent and copy-unsafe.** Examples 6, 11, 12 wrap values in `{{...}}` (e.g. `"TotalTargetCapacity": {{10}}`, `"Version": "{{1}}"`), which is **not valid JSON** and will fail unless the reader strips the braces — unlike Examples 1-5/7-10 which use literal values. A reader copying Example 11/12 verbatim hits a parse error. Oracle: JSON-parse the blocks. Severity: Informational (doc-consistency; AWS-owned).

**Doc evidence:** `ec2-fleet-examples.md:327-334` (broken JSON), Examples 6/11/12 (`{{}}` placeholders), Examples 4/5/6 (`lowest-price`). **Severity-if-true:** Informational–Low; **in scope as AWS-authored artifact defects (Tier-2)**, not customer footguns.

### Area P1–P5 — Pointers (DO NOT re-run; owned by siblings)
These examples re-use mechanisms already deep-dived. Cross-reference only.
- **P1 — Examples 1/2/3 (Spot/On-Demand default & On-Demand-primary mix):** → `ec2-fleet-on-demand-walkthrough-attack-research-plan.md` (maintain-default self-healing fleet, `OnDemandTargetCapacity` split, lowest-price risky default, capacity-split validation gap). Also `ec2-fleet-attack-research-plan.md` for LT/PassRole/SLR/KMS core-create depth.
- **P2 — Examples 4/5 (multiple ODCRs, `use-capacity-reservations-first`):** → `fleet-tutorials-attack-research-plan.md` (hub CR-consumption Areas 1-8) + `ec2-fleet-targeted-capacity-reservations-walkthrough-attack-research-plan.md` (IAM-unscopable CR consume path, `DescribeCapacityReservations` unscopable read-back oracle shown in the examples).
- **P3 — Example 6 (targeted CRs):** → `ec2-fleet-targeted-capacity-reservations-walkthrough-attack-research-plan.md` (owns `InstanceMatchCriteria` birth-vs-consume asymmetry, resource-groups cross-service unscopable target, foreign-CR grouping, `ListGroupResources` oracle).
- **P4 — Example 11 (`InstanceRequirements` attribute-based selection):** → `ec2-fleet-instance-weighting-walkthrough-attack-research-plan.md` Area 4 (open-ended `Min` with no `Max` + price-protection-off broadens instance-type pool). Also owns the `$Latest`/`$Default` late-binding referenced by Area 1 §E1.
- **P5 — Example 12 (`ReservedCapacityOptions`, multiple CR types, resource group):** → `ec2-fleet-launch-instances-multiple-cr-types-walkthrough-attack-research-plan.md` (owns the net-new `ReservedCapacityOptions` structure, `DefaultTargetCapacityType:reserved-capacity`, ordered `ReservationTypes` arbitration, direct `CapacityReservationId.N` body targeting, dual cross-account forced-termination, the live cr-groups contradiction). **Note the drift (§2): Example 12 is newly present on this page.**
- **ModifyFleet / `ExcessCapacityTerminationPolicy` on scale-down:** → `modify-ec2-fleet-attack-research-plan.md`.
- **EventBridge mechanism depth:** → `monitor-ec2-fleet-using-eventbridge-attack-research-plan.md` + `fleet-monitor-attack-research-plan.md`.

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| `CreateFleet`-only principal arms SLR terminate+relaunch loop | CapacityRebalance / SLR | None — SLR holds `TerminateInstances`/`RunInstances`; no caller-side check (Area 1) |
| Cap/forbid `TerminationDelay`, `ReplacementStrategy`, `ExcessCapacityTerminationPolicy` via IAM | `CreateFleet` condition keys | **No condition key exists** (Area 1 §D) |
| 2× target-capacity dual-billing for ≤2h or indefinitely | CapacityRebalance | Only prose "we recommend"; no enforceable cap, no `MaxTotalPrice` in example (Area 1 §E-cost) |
| Redirect replacement launches via LT default-version swap | LT `$Latest`/`$Default` + SLR RunInstances | CreateFleet IAM "do not include launch-template resources" → unscopable; **doc-gap on re-resolution** (Area 1 §E1) |
| Default allocation strategy = recommended-against combo | `SpotOptions.AllocationStrategy` default `lowest-price` | Prose "strongly recommend against" only (Area 1 §E2 / Area 2) |
| `MaxTotalPrice` exceeded via surplus credits | SpotOptions | Documented caveat; cap not enforced for T-unlimited (Area 2) |
| Copy-verbatim example fails / ships hazardous default | page JSON | None — AWS-authored defect (Area 3) |
| Rebalance churn un-correlatable in audit | EventBridge/CloudTrail | No `rebalanced` sub-type; best-effort streams; SLR CloudTrail attribution undocumented (Area 1 §F) |

## 7. Out-of-Scope Risk Categories
- Shared EC2/Spot capacity-pool infrastructure and the Spot market itself (AWS-owned).
- Single-tenant self-inflicted cost/availability from one's own fleet config (Areas 1 §E-cost, 2) **except** where the hazard is baked into the AWS-authored example / managed SLR (then Tier-2 reportable).
- IMDS on fully-managed instances; product/feature-parity gaps.
- `--cli-input-json file://` as SSRF — **resolved N/A** (client-side botocore load; on-demand sibling).
- All CR-consumption, instance-weighting, on-demand-primary, multi-CR-types, ModifyFleet, EventBridge-mechanism, PassRole/KMS depth — owned by the siblings in §5 P1-P5; re-analysis here would be duplication.
- Cross-tenant / cross-account: **no cross-account boundary is introduced by this page's net-new surface** (Capacity Rebalancing and allocation strategies are all single-account). The cross-account CR surface lives in the CR siblings, not here.

## 8. Null hypotheses / doc gaps
- **Lens A (IDOR):** N/A — no resource-by-id read/mutate introduced beyond `fleetId` creation; checked the full examples page + `API_CreateFleet` response elements. `fleetId`/`cr-…` ids not fabricable; no cross-tenant naming.
- **Lens G (SSRF):** N/A — only `file://` (client-side) and launch-template/AMI references (no server-side fetch of a caller URL). Checked page top + create-ec2-fleet.
- **Lens Q (upload), K (prompt-injection), FF (JWT), DD (cache), BB/CC (parser/upstream-context), W (attestation), Y (transport):** N/A for a JSON-config catalog page — no upload, LLM, token, cache, multi-parser, enclave, or transport surface. Pages checked: the full examples page + `ec2-fleet-capacity-rebalance.md`.
- **Lens H (KMS):** deferred to `ec2-fleet-attack-research-plan.md` (no KMS field on this page; EBS encryption rides the LT/AMI, not the fleet config).
- **Doc-gaps needing a live canary (hunter must confirm):**
  1. Whether rebalance replacement launches **re-resolve `$Latest`/`$Default`** or pin the CreateFleet-time LT version (Area 1 §E1 — the highest-value open).
  2. **CloudTrail attribution** of the SLR's rebalance `RunInstances`/`TerminateInstances` (userIdentity = SLR ARN vs fleet) and whether `CreateFleet`/`ModifyFleet` log full nested `MaintenanceStrategies`/`TerminationDelay` params (Area 1 §F).
  3. Whether `ModifyFleet`'s generic `ec2:Attribute`/`ec2:Attribute/${AttributeName}` keys can actually gate `excess-capacity-termination-policy` — no doc enumerates valid `AttributeName` values (Area 1 §D; carried as unlikely).
  4. **Actual default of `ExcessCapacityTerminationPolicy`** when omitted (prose silent; only inferred from the CLI skeleton showing `termination`).
  5. Exact billing/metering granularity during the `TerminationDelay` dual-billing window (no cost model documented).
```
