# EC2 Fleet — Launch Instances into Interruptible Capacity Reservations (walkthrough) — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/ec2-fleet-launch-instances-interruptible-cr-walkthrough.html` (the target page) + its doc neighborhood: `interruptible-capacity-reservations.html`, `capacity-owner-procedures.html`, `capacity-consumer-procedures.html`, `monitor-interruptible-cr.html`, `cr-groups.html`, `capacity-reservation-sharing.html`, `ec2-fleet-prerequisites.html`, API refs `API_CreateInterruptibleCapacityReservationAllocation`/`API_UpdateInterruptibleCapacityReservationAllocation`/`API_InterruptibleCapacityAllocation`, and the IAM Service Authorization Reference `list_ec2` (offline `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`, 10190 lines — the ONLY usable source; online `list_ec2.html` truncates before the condition-key table). Status: **documentation-derived hypotheses only; nothing tested against a live account.** Offline==online verified 2026-10-15 for every UserGuide/APIReference page except the ASG page (see §8 drift).

This is the **page-level deep-dive child of the `fleet-tutorials.html` hub** for walkthrough tutorial #5. It is the sibling of:
`ec2-fleet-instance-weighting-walkthrough-attack-research-plan.md`, `ec2-fleet-on-demand-walkthrough-attack-research-plan.md`, `ec2-fleet-targeted-capacity-reservations-walkthrough-attack-research-plan.md`, and `ec2-fleet-launch-instances-capacity-blocks-walkthrough-attack-research-plan.md`. It **defers** to and cross-refs those for shared groundwork and owns only the net-new **Interruptible Capacity Reservation (ICR) consume path** (new `MarketType=interruptible-capacity-reservation`, `DefaultTargetCapacityType=reserved-capacity`, `ReservedCapacityOptions.ReservationType=["interruptible-capacity-reservation"]`, the owner-reclaim forced-termination primitive, and the RAM-org trust boundary). This plan is also the one that **resolves the open CR-group contradiction** carried unresolved by the hub plan.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.
- **Safe first oracle for every IAM lead is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resources touched).** Escalate to a live scoped call only with synthetic/canary data under a role holding *exactly* the artifact under test, never the over-privileged tester. **`DryRun` is caller-IAM-only (evaluated before resource resolution) — NOT an ownership/existence oracle.** Teardown every resource created.

### Load-bearing distinction (Area 0 — read before any lead; mirrors the targeted-CR sibling)
This tutorial's fleet is **`Type: instant` (REQUIRED** — "Only EC2 Fleet requests of type `instant` are supported for launching instances into Interruptible Capacity Reservations"). Per `ec2-fleet-prerequisites.md` ("An `instant` EC2 Fleet does not require this role [`AWSServiceRoleForEC2Fleet`]"), an instant fleet launches **directly under the CALLER's own identity** — the caller must hold `ec2:RunInstances`, and the caller's *expressible* identity-policy conditions **do** bind. Therefore:
- **The SLR-non-propagation BACKBONE FINDING does NOT apply here** (it is a `maintain`/`request`-fleet fact). The leads here are shaped **"the control I need has no IAM key / no enum value,"** not "the SLR strips my conditions." Do not import the backbone framing.
- `AWSEC2CapacityReservationFleetRolePolicy` (crf-*) is a *different* feature (Capacity Reservation **Fleet**) and does NOT govern this path.
- The consumer path is **also reachable via plain `run-instances`** (same `--instance-market-options '{"MarketType":"interruptible-capacity-reservation"}'` + `CapacityReservationTarget`) and via **Auto Scaling Groups** (`capacity-consumer-procedures.md`) — so every consume-side lead below must be re-asked against RunInstances and ASG, not only CreateFleet.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Consume an ICR cr-id you were not shared** (or shared outside your org) — launch into it, or get an existence/capacity oracle from a foreign cr-id — via `create-fleet`/`run-instances` targeting (Area 3 / Lens A). Critical if cross-account.
2. **Author an identity policy that forbids interruptible launches or pins which ICR a fleet consumes** — prove it is *impossible* on both CreateFleet and RunInstances (Area 1 / Lens U/S/X). Reportable AWS-owned enforcement gap.
3. **Burn another account's On-Demand quota / shift cost** by launching your interruptible instances against an owner's shared ICR (Area 3 / Lens A). Cross-account.
4. **Resolve the CR-group contradiction** — does `group-resources` accept an ICR ARN, and does a group-targeting fleet ever auto-match into an ICR against the "can't add to groups" rule (Area 4 / Lens U)?
5. **Silently terminate / disrupt a consumer's workload across the account boundary** beyond the by-design reclaim — specifically via the org-leave "eventually terminated, no documented warning" path (Area 2 / Lens AA/U).
6. **Redirect which ICR future launches target** by editing the launch template with no CreateFleet/PassRole (Area 5 / Lens B/E).

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** An **Interruptible Capacity Reservation (ICR)** is spare capacity an On-Demand Capacity Reservation (ODCR) **owner** carves out of a *source* CR and lends to other teams, retaining the right to reclaim it. Two roles:
- **Capacity owner** — owns the source ODCR; creates/updates/reclaims/cancels the interruptible allocation; **can only view, launch, tag, share, and assign billing** for the ICR; cannot directly modify/cancel it (all count changes go through the source CR).
- **Capacity consumer** — launches instances into the shared ICR, understanding they can be terminated on reclaim.

**Owner-side control plane (two net-new EC2 actions, operate on the *source* `capacity-reservation`):**
- `CreateInterruptibleCapacityReservationAllocation` — `CapacityReservationId` (source, required; must be active, no end date, available capacity), `InstanceCount` (required, ≤1000, available only), `ClientToken`, `DryRun`, `TagSpecification.N`, `ZeroSizePreference`(`retain|default`, default `default`). One allocation per source CR.
- `UpdateInterruptibleCapacityReservationAllocation` — `CapacityReservationId` (source, required), `TargetInstanceCount` (**optional**; higher=add, lower=reclaim; ≤1000 delta/call; floor 0), `ZeroSizePreference`, `DryRun`. Lowering → reclaim; `0` → cancel (unless `retain`).
- Response/embedded `InterruptibleCapacityAllocation`: `instanceCount`, `interruptibleCapacityReservationId`, `interruptionType`(only value: `adhoc`), `status`(`pending|active|updating|canceling|canceled|failed`), `targetInstanceCount`, `zeroSizePreference`. **No consumer-account field anywhere** — the owner API objects do not reveal who is consuming.

**Consumer-side consume plane (this tutorial):**
- **Launch template**: `InstanceMarketOptions.MarketType = "interruptible-capacity-reservation"` + `CapacityReservationSpecification.CapacityReservationTarget.CapacityReservationId = cr-...`.
- **Fleet config.json**: `TargetCapacitySpecification.{TotalTargetCapacity:10, DefaultTargetCapacityType:"reserved-capacity"}`, `ReservedCapacityOptions.ReservationType:["interruptible-capacity-reservation"]`, `Type:"instant"`. Output `Lifecycle: "interruptible-capacity-reservation"`.
- Also: plain `run-instances --instance-market-options ... --capacity-reservation-specification ...` and ASG via launch template.
- ICRs are **targeted** CRs by default ("will not automatically cover matching instances — you must explicitly specify the reservation ID"). **No fallback** to On-Demand/Spot.

**Identifiers.** `cr-<~17 hex>` (CR id). Fleet id `fleet-<uuid>`. No consumer id in owner objects; no owner id in the consumer EventBridge event.

**Identity / trust.** Instant fleet → caller's own IAM identity (needs `RunInstances`). Cross-account/cross-org sharing of the ICR is via **AWS RAM, restricted to "within your AWS organization"** (`capacity-owner-procedures.md`). **No consumer-side RAM accept step is documented** (org-internal auto-association). The KMS-grant-to-SLR prerequisite (`ec2-fleet-prerequisites.md`) is printed but is a `maintain`-fleet concern (instant fleets don't use the SLR).

```
 OWNER account (ODCR owner)                         CONSUMER account (same AWS Org)
 ┌───────────────────────────────┐                 ┌───────────────────────────────────┐
 │ source ODCR (active, no end)   │                 │ create-fleet (instant) / run-      │
 │  └─ CreateInterruptible...     │   RAM share     │ instances / ASG                     │
 │     Allocation (InstanceCount) │  (org-scoped)   │   LT: MarketType=interruptible-     │
 │  ICR (interruptible) ──────────┼───────────────▶ │        capacity-reservation         │
 │   TargetInstanceCount          │                 │        CapacityReservationId=cr-... │
 │  UpdateInterruptible...Alloc   │                 │   config: reserved-capacity +       │
 │   (lower → RECLAIM) ───────────┼──2-min EventBridge warning──▶ consumer instances      │
 │                                │                 │   TERMINATED on reclaim (no OD/Spot │
 │  billed for the reservation;   │                 │   fallback). Consumer billed for    │
 │  consumer usage counts vs      │                 │   its running instances only.       │
 │  OWNER's On-Demand quota ◀─────┼─────────────────┘                                     │
 └───────────────────────────────┘                 └───────────────────────────────────┘
   EventBridge: owner gets "Reclamation Completed" (aggregate counts, no consumer id)
                consumer gets "Instance Interruption Warning" (instance-id, no cr/owner id)
   instant fleet itself emits NO aws.ec2fleet EventBridge events; CloudTrail logs CreateFleet (mgmt)
```

---

## 3. API / Interface Inventory

| Name | Mutating | Facing | Functionality | Authorized callers | Notes / lead |
|---|---|---|---|---|---|
| `ec2:CreateFleet` | yes | external | instant fleet, launches into ICR | caller w/ RunInstances | **no interruptible/CR-id/market-type condition key** (Area 1). `ReservedCapacityOptions`/`ReservationType`/`DefaultTargetCapacityType`/`Type` = request params, **0 IAM keys** |
| `ec2:RunInstances` | yes | external | direct consume path | caller | has `ec2:InstanceMarketType` (3-value enum, no interruptible value) on `instance*`; capacity-reservation row = tag/region/LT keys only, **no CR-id** (Area 1) |
| `ec2:CreateInterruptibleCapacityReservationAllocation` | yes | external | owner carves ICR from source CR | source-CR owner | acts on `capacity-reservation*`; **tag/ARN-scopable** owner-side; keys incl. `ec2:IsInterruptible`,`ec2:InterruptibleCapacityReservationId`,`ec2:SourceCapacityReservationId`,`ec2:TargetInstanceCount`,`ec2:InstanceMatchCriteria`,`ec2:InterruptionType` |
| `ec2:UpdateInterruptibleCapacityReservationAllocation` | yes | external | **reclaim / forced-terminate** | source-CR owner | lower `TargetInstanceCount` → terminate consumer running instances (Area 2) |
| `ec2:DescribeCapacityReservations` | no | external | lists CRs incl. `Interruptible:true` + embedded `InterruptibleCapacityAllocation` | caller | **blank resource type, only `ec2:Region`** → unscopable account-wide ICR enumeration oracle (recon for Area 3). No dedicated interruptible Describe action exists |
| RAM share of ICR | yes | external | org-scoped sharing | owner | enforced by RAM, **not EC2 IAM** (no org condition key in EC2) |
| `resource-groups:GroupResources` (ICR ARN?) | yes | external | **contested** — can ICR join a CR group? | caller | Area 4 contradiction |

**Undocumented/console-hidden knobs & params the IAM layer can't see:** `MarketType=interruptible-capacity-reservation` (a 4th market value the request accepts but `ec2:InstanceMarketType`'s enum does **not** list); `ReservedCapacityOptions.ReservationType` (a **list** — "when you specify multiple launch templates, each targeting a different ICR, EC2 Fleet provisions instances across all matching reservations"); `ZeroSizePreference=retain` (keeps an allocation alive at 0). `UpdateInterruptible...` `TargetInstanceCount` is **optional** — a call with only `ZeroSizePreference` is valid.

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Consumer account | Owner's ICR (shared) | `create-fleet`/`run-instances` targeting `cr-id` | Launching into / getting a capacity-or-existence signal from an ICR **not RAM-shared to the caller (or shared outside the org)** = breach |
| Consumer identity | Consumer's own quota vs **owner's** | ICR consume counts vs owner's On-Demand limit | Consumer launches burn the **owner account's** On-Demand quota → cross-account quota exhaustion |
| Owner account | Consumer's running workload | `UpdateInterruptible...Allocation` lower count + 2-min EventBridge | Owner unilaterally terminating a consumer's instances is **by design**; the breach-shaped variant = org-leave "eventually terminated, no documented warning" |
| Admin (policy author) | Fleet/instance launch | identity policy on CreateFleet/RunInstances | **Any** attempt to deny "interruptible market" or pin "only this ICR" that cannot be expressed = AWS-owned enforcement gap (Area 1) |
| LT editor (no CreateFleet/PassRole) | Which ICR future launches hit | LT version holding `MarketType`+`CapacityReservationId` | A principal with only LT-edit redirecting the consumed ICR = launch-placement primitive (Area 5) |
| Any caller surface | AWS's own service plane | — | **HARD STOP** — ICR allocation is intra-account/org EC2; any AWS-fleet identity/ARN surfacing = disclosure |

---

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE, Lens U/S/X — AWS-owned, Tier-2 reportable] The interruptible-CR consume path is IAM-unscopable, and the new MarketType has no IAM enum value
**Background.** The tutorial introduces a brand-new instance market, `MarketType=interruptible-capacity-reservation`, selected inside the launch template, plus fleet-level `DefaultTargetCapacityType=reserved-capacity` and `ReservedCapacityOptions.ReservationType=["interruptible-capacity-reservation"]`.

**Security Concern.** An admin cannot write an identity policy that (a) **forbids** a team from launching interruptible instances, (b) **pins which ICR** a fleet/instance may consume, or (c) **denies the reserved-capacity target type** — on either CreateFleet or RunInstances. Confirmed from `list_ec2.md`:
- `ec2:InstanceMarketType` (def **line 10092**) enumerates **only `capacity-block`, `on-demand`, `spot`** — **no `interruptible-capacity-reservation` value**. So even where the key exists (RunInstances `instance*`, line 9591) it cannot discriminate an interruptible launch. The request accepts a 4th market value the IAM condition key does not model — a **doc-vs-IAM integrity gap**.
- `ec2:InstanceMarketType` is **ABSENT from all 8 CreateFleet resource rows (5113–5123)**; CreateFleet's `capacity-reservation` row (line 5115) carries only `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`.
- The four interruptible keys — `ec2:IsInterruptible` (10104), `ec2:InterruptibleCapacityReservationId` (10099), `ec2:SourceCapacityReservationId` (10159), `ec2:TargetInstanceCount` (10164) — appear **only on `CreateInterruptibleCapacityReservationAllocation` (5183) and `UpdateInterruptibleCapacityReservationAllocation` (9735)** (owner-side), never on CreateFleet/RunInstances. **0 hits on the consume path.**
- **No `ec2:CapacityReservationId` key exists anywhere** (exact-string grep = **0 hits**); `ec2:InstanceMatchCriteria` (10093) is owner/CR-management-side only, never on CreateFleet/RunInstances CR rows.
- `ReservedCapacity`/`ReservationType`/`reserved-capacity`/`DefaultTargetCapacityType`/`FleetType` → **0 IAM-key hits** — pure request params, unconditionable.
- CreateFleet Description (line 5114) verbatim: *"Resource-level permissions for this action do not include the resources specified in a launch template … you must include the resources in the RunInstances action statement"* — and the market/CR-id knobs live **inside the launch template**, which CreateFleet cannot scope, and CreateFleet has **no `ec2:LaunchTemplate` key** either (Lens-X asymmetry vs RunInstances, which carries `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource`).

**High-level Test Scenarios (falsifiable).**
- *Claim:* `iam:SimulateCustomPolicy` with a Deny on `ec2:CreateFleet` conditioned on `ec2:InstanceMarketType StringEquals interruptible-capacity-reservation` **has no effect** (key absent + value not in enum) → the interruptible fleet still simulates ALLOW. → **Confirm/Refute:** simulate; key inert.
- *Claim:* No policy on CreateFleet/RunInstances can restrict launches to a specific `cr-id` (no CR-id condition key) — only tag/region on the CR *resource*, which the caller may not even be able to set on a foreign shared CR. → simulate + inspect.
- *Claim:* `ec2:InstanceMarketType` on RunInstances cannot deny interruptible launches because the enum lacks the value → a Deny keyed on it is vacuous for this market.
- **Oracle:** `iam:Simulate*` shows the intended Deny is inert; no resource created. **Doc evidence:** list_ec2 lines 10092/10099/10104/10159/10164/5113-5123/5115/9591/9735/5183/5114. **Severity-if-true:** Medium (AWS-owned, uneditable-surface enforcement gap; **High** where an org relies on IAM — not SCP/RAM — to bound which teams/pools can consume reclaimable capacity). **Reportable Tier-2** (AWS-authored IAM surface). **Stop condition:** both knobs confirmed inert on both actions.

### Area 2 — [Lens AA/U/A — cross-account availability dependency; org-leave gap is the sharp lead] Owner-reclaim forced-termination
**Background.** The owner reclaims via `UpdateInterruptibleCapacityReservationAllocation` with a lower `TargetInstanceCount`: "we first reclaim available instances, then running instances … 2-minute interruption warning through EventBridge … then terminated" (`capacity-owner-procedures.md`). There is **no fallback to On-Demand or Spot** and **no consumer veto, cooldown, rate-limit, or SLA beyond the 2 minutes** documented.

**Security Concern.** The consumer's workload availability is unilaterally controllable by a *different account* (the owner), across the org boundary. Owner-initiated reclaim of lent capacity is **by design** (lower novelty), but two shapes are breach-adjacent:
1. **Org-leave path is weaker and less observable:** "If a consumer account leaves your organization, the interruptible reservation is automatically unshared … Any instances running in the unshared reservation are **eventually terminated**" — the word *eventually*, with **no documented 2-minute EventBridge warning** for this path (only the reclaim and reclamation-completed events are documented). A consumer migrated out of an org can lose workloads with no interruption notice.
2. **No cooldown/rate-limit** → an owner can thrash allocate/reclaim (≤1000/call) to repeatedly disrupt a consumer; the consumer has no release/veto action.

**High-level Test Scenarios.**
- *Claim:* reducing `TargetInstanceCount` below the running count terminates consumer running instances within ~2 min, with the documented EventBridge warning. → **Confirm:** two-account canary (owner reclaims, consumer observes the `EC2 Capacity Reservation Instance Interruption Warning` + termination). **Severity:** by-design availability dependency — Low/Informational unless the notice/termination deviates from docs.
- *Claim (sharp):* the **org-leave** termination fires **without** the 2-minute `Instance Interruption Warning` (or with a materially longer/absent notice than owner-initiated reclaim). → **Confirm:** move the consumer account out of the org while instances run; capture whether any interruption event is emitted and the actual time-to-terminate. **Severity:** Medium (undocumented silent cross-account termination; detection/availability gap). **doc-gap — not stated** which event, if any, fires here.
- **Oracle:** termination occurs with a notice path differing from the documented 2-min warning. **Doc evidence:** `capacity-owner-procedures.md` (Modifying note, Reclamation process, Sharing considerations), `monitor-interruptible-cr.md`, `interruptible-capacity-reservations.md`.

### Area 3 — [Lens A/U — cross-account consume authz & quota theft; HIGHEST-VALUE OPEN DOC-GAP] Targeting a shared/foreign ICR cr-id
**Background.** ICRs are **targeted** — "you must explicitly specify the reservation ID when launching." Consume is gated **entirely upstream by the RAM share scope** ("within your AWS organization"); Area 1 proves **no EC2 IAM backstop** at launch. The consumer tells apart ICRs with the unscopable `DescribeCapacityReservations` (blank resource type, only `ec2:Region` — line 6696) filtering `Interruptible==true` — an account-wide enumeration oracle (the consumer-procedures page literally instructs this). **Usage counts against the OWNER's On-Demand quota** (`capacity-reservation-sharing.md`: "Instances launched into the shared capacity by consumers count towards the Capacity Reservation owner's On-Demand Instance limit"), and the **consumer pays only for its own running instances** while the **owner pays the reservation** — a cost/quota asymmetry.

**Security Concern.** With no launch-time IAM check beyond "is this cr-id RAM-shared to me," the questions are: (a) does the server enforce the RAM share at `create-fleet`/`run-instances`, or does an **un-shared / wrong-org** foreign `cr-id` leak an existence/capacity oracle (or launch)? (b) can a shared-to consumer **over-consume** or **race** other org consumers down a shrinking shared pool? (c) can a consumer deliberately **exhaust the owner's On-Demand quota** by launching into the shared ICR?

**High-level Test Scenarios.**
- *Claim:* targeting a `cr-id` **not shared to the caller** returns a distinct error (existence oracle) rather than a generic AccessDenied; targeting a `cr-id` **shared to the caller** launches with no secondary identity check. → **Confirm/Refute:** two-account canary — one shared ICR, one un-shared foreign ICR; compare `create-fleet`/`run-instances` responses (and `DescribeCapacityReservations` visibility). **cr-id entropy** (`cr-<~17 hex>`) makes blind cross-account IDOR a **partial-null** (not fabricable), so the real residual is **within-org shared ids + the enumeration oracle**, not guessing. **Severity:** cross-account consume of un-shared capacity = **Critical**; existence oracle on foreign id = Low–Medium.
- *Claim:* a consumer launch burns the **owner's** On-Demand limit → a malicious/greedy consumer can push the owner to quota exhaustion (cross-account DoS on the owner's launch capacity). → **Confirm:** canary, observe owner quota counters. **Severity:** High (cross-account quota/cost).
- *Claim:* multiple org consumers racing the same ICR pool have **no documented contention resolution** → first-come occupy / partial-fulfill ("EC2 Fleet launches as many instances as it can and reports … in the API response"). → observe race outcome. **Severity:** Medium (noisy-neighbor within org).
- **Oracle:** launch/visibility of capacity the caller was not shared, or owner-quota movement attributable to a consumer. **Doc evidence:** `capacity-consumer-procedures.md`, `capacity-reservation-sharing.md` (Instance limits / Billing and metering), target page ("launches as many as it can"), list_ec2 line 6696. **Preconditions:** two accounts in one org, a RAM-shared ICR + an un-shared ICR. **Stop condition:** share-enforcement behavior settled in both directions. **Note:** the quota-counts-to-owner and consumer-pays-instances facts are **inferred** from the general sharing page + the ICR "all other sharing works the same" cross-reference — the ICR-specific pages do **not** restate them verbatim; confirm live.

### Area 4 — [Lens U — CONFIRMED doc-vs-doc contradiction, OWNED by this plan] Can an ICR join a Capacity Reservation group?
**Background.** The hub plan carried this as an unresolved open item. It is now **confirmed still contradictory**, both statements verbatim-present online with no drift (2026-10-15):
- `interruptible-capacity-reservations.md` (Considerations → consumers): **"You can't add interruptible Capacity Reservations to capacity reservation groups."**
- `cr-groups.md`: **"A group supports all reservation types, including … interruptible Capacity Reservations … You can add any combination of reservation types to a single group."** (the phrase links directly to `interruptible-capacity-reservations.html` — unambiguously the same feature).
- `cr-groups-add.md` carves out no exception either.

**Security Concern.** CR-group membership **auto-matches** instances by attributes (unlike ICR's mandatory explicit targeting). If `resource-groups:GroupResources` in fact **accepts** an ICR ARN, then (i) the targeted-CR sibling's **IAM-unscopable, cost-bearing cross-service group-consume path** (`CapacityReservationResourceGroupArn` inside the LT, no condition keys anywhere) **extends to reclaimable interruptible capacity**, and (ii) a launch could silently land in — or be denied-of — reclaimable capacity it never explicitly targeted. If `GroupResources` **rejects** the ARN, `cr-groups.md` is overbroad copy and the attack surface narrows.

**High-level Test Scenarios.**
- *Claim:* `aws resource-groups group-resources` (or the EC2 CR-group add path) **accepts** an interruptible `cr-id`/ARN against the "can't add" rule. → **Confirm/Refute:** attempt the add with a canary ICR; record accept vs reject.
- *Claim:* a `create-fleet`/`run-instances` targeting a **group ARN** that (per the above) contains an ICR ever **matches an instance into the ICR** without the required explicit cr-id. → observe `Lifecycle`/placement in the response. **If true, chains into the targeted-CR sibling's Area 1/2 (group-consume unscopable + foreign-CR grouping).**
- **Oracle:** group-add accept/reject; an instance landing in an ICR via group auto-match. **Doc evidence:** the two contradicting pages above + `cr-groups-add.md`. **Severity:** if ICRs *can* be grouped and auto-matched → Medium–High (unexpected reclaimable placement + extends the cross-service unscopable consume path); pure doc inconsistency if rejected → Informational (AWS-owned, file it). **Stop condition:** add accepted-or-rejected settled; if accepted, pivot to the targeted-CR sibling plan.

### Area 5 — [Lens B/E — late-binding launch-template redirect] Who controls which ICR gets consumed
**Background.** The ICR target (`MarketType=interruptible-capacity-reservation` + `CapacityReservationId`) lives **inside the launch template**. The fleet config references the LT by name + `Version:"1"`.
**Security Concern.** A principal holding only `ec2:CreateLaunchTemplateVersion`/`ec2:ModifyLaunchTemplate` (no CreateFleet, no `iam:PassRole`, no RunInstances) can rewrite `MarketType`/`CapacityReservationId`/`IamInstanceProfile`/UserData — redirecting which ICR (or market) every *future* launch targets. **But instant fleets do not self-replenish** (no `maintain` loop), so the redirect fires only on the next `create-fleet`/`run-instances`/ASG scale-out — **weaker than the instance-weighting sibling's Area 2** (which has maintain-replenishment amplification). Worst with `$Latest`/`$Default` version pins (the tutorial pins `"1"`, the integrity-safe counterpart — cross-ref on-demand sibling Area 5).
**High-level Test Scenarios.** *Claim:* `ModifyLaunchTemplate` has no condition key restricting which version becomes default and `CreateLaunchTemplateVersion` has no `ec2:Attribute`-class key (confirmed pattern in capacity-blocks sibling §5.3) → LT-editor controls the consumed ICR. → simulate + canary scale-out. **Severity:** Medium (intra-account launch-placement/privesc enabler). **Cross-ref** instance-weighting Area 2, capacity-blocks §5.3 — do not re-derive LT-key depth here.

### Area 6 — [Lens O — detection blind spots & EventBridge disclosure] instant fleet + ICR event model
**Background.** `instant` fleets emit **no `aws.ec2fleet` EventBridge events** (fleet-monitor finding; corroborated here by omission). The only ICR events (`monitor-interruptible-cr.md`, both `source: aws.ec2`):
- **Consumer** — `EC2 Capacity Reservation Instance Interruption Warning`: `detail.instance-id`, `instance-action:terminate`, `instance-termination-time`, `azId`; `account` = consumer. **No cr-id, no owner account** leak.
- **Owner** — `EC2 Interruptible Capacity Reservation Allocation Reclamation Completed`: `detail.sourceCapacityReservationId`, `instanceType`, `availabilityZoneId`, `TotalInstanceCount`, `ReclaimedInstanceCount`, `targetInstanceCount`; aggregate only. **No consumer account/instance ids** leak.
- CloudTrail: `InterruptibleCapacityReservationCreated/AllocationUpdated/Cancelled`, `CapacityReservationModified`, `InterruptibleCapacityReservationInstancesTerminated`; plus `CreateFleet`/`RunInstances` as management events (logged by default).
**Security Concern.** An interruptible launch via an instant fleet produces **no fleet-level EventBridge signal** — only the CloudTrail management event. The org-leave termination (Area 2) has **no documented event**. Neither EventBridge event crosses the owner↔consumer identity gap (good for isolation, but also means neither party can observe the other's attribution via EventBridge).
**High-level Test Scenarios.** *Claim:* a create-fleet into an ICR emits zero `aws.ec2fleet` events (only CloudTrail). *Claim:* org-leave termination emits no interruption warning. → canary + EventBridge/CloudTrail capture. **Severity:** Low–Informational (detection enabler; raises severity of Area 2/3 as a stealth multiplier).

### Area 7 — [Lens U — fail-open on unsupported combinations] Considerations as enforcement points
**Background.** The tutorial's Considerations: (i) **instant-only**; (ii) `OnDemandTargetCapacity`/`SpotTargetCapacity` with `reserved-capacity` default is **unsupported**; (iii) multiple LTs each targeting a different ICR → "**EC2 Fleet provisions instances across all matching reservations**"; (iv) **no OD/Spot fallback**. ASG (online, consolidated page) adds: **warm pools not supported** with ICR, and a **launch template can target only one CR type** (ICR vs Capacity Block vs standard — mutually exclusive).
**Security Concern.** Each "unsupported" is an enforcement point that may **fail open** (silently ignore) rather than reject — the fleet could fall back to billed regular capacity, or the multi-LT "provisions across all matching reservations" could over-provision across more ICRs than intended (cost/placement). An LT that violates the one-CR-type rule may be accepted with undefined precedence.
**High-level Test Scenarios.** *Claim:* submitting `Type:maintain`/`request` (or OD/Spot target capacity) with `reserved-capacity` default **rejects synchronously** rather than silently ignoring. *Claim:* multiple LTs targeting different ICRs provision across all with no documented ceiling → over-provision/cost. *Claim:* an LT with two CR types is rejected (per ASG rule) consistently on the fleet path. → canary each; observe reject-vs-silent-accept. **Severity:** Medium (cost/intent footgun; fail-open availability). **doc-gap** — enforcement point (orchestration vs API validation) unstated.

### Area 8 — [Lens R — AWS-authored sample IAM artifact; thin POINTER] prerequisites user policy
**Background.** `ec2-fleet-prerequisites.md` prints a sample EC2 Fleet user policy: `{"Action":["ec2:*"],"Resource":"*"}` + `{"Action":["iam:ListRoles","iam:PassRole","iam:ListInstanceProfiles"],"Resource":"arn:aws:iam::123456789012:role/DevTeam*"}` (PassRole scoped by **role-name prefix** `DevTeam*`, not `iam:PassedToService`). Plus a KMS `create-grant` to `AWSServiceRoleForEC2Fleet` (a `maintain`-fleet concern; **instant fleets don't use the SLR**, so moot for this tutorial).
**Security Concern / Pointer.** `ec2:*` on `*` trivially includes every action in Areas 1–7 (CreateFleet, RunInstances, the two allocation actions, DescribeCapacityReservations) with no scoping — the sample artifact *is* the over-grant. `DevTeam*` prefix PassRole = self-escalation if a `DevTeam*`-named admin role exists. **This is shared verbatim with all four walkthrough siblings** — do not re-audit; cross-ref the on-demand/instance-weighting/targeted-CR/capacity-blocks plans and the `ec2-fleet` core plan for the full PassRole/privesc depth. **Severity:** least-priv footgun as printed; the PassRole-prefix shape is the reportable piece (shared finding).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Admin cannot deny interruptible market / pin ICR on fleet path | CreateFleet/RunInstances IAM | "resource-level permissions … do not include launch-template resources" (line 5114); `ec2:InstanceMarketType` 3-value enum (10092) |
| Consume an un-shared / cross-org ICR cr-id | RunInstances/CreateFleet targeting | RAM share scope ("within your AWS organization") — **the only** gate; no EC2 IAM backstop |
| Burn owner's On-Demand quota via consumer launches | shared ICR | "consumer usage counts toward the owner's On-Demand Instance limit" (sharing page) |
| Silent cross-account workload termination | org-leave path | "automatically unshared … eventually terminated" — **no documented warning** |
| ICR joins a CR group & auto-matches | resource-groups / cr-groups | "You can't add interruptible CRs to groups" vs cr-groups "all reservation types" — **contradiction** |
| LT edit redirects consumed ICR | ModifyLaunchTemplate/CreateLaunchTemplateVersion | no condition key restricting default version / attribute |
| Fail-open on unsupported Type/target-capacity combo | CreateFleet orchestration | Considerations list "not supported" (prose only) |
| Over-provision across multiple ICRs | multi-LT fleet | "provisions instances across all matching reservations" — no ceiling stated |

---

## 7. Out-of-Scope Risk Categories
- **Owner reclaiming its own lent capacity within the documented 2-min notice** = by design (availability dependency, not a vuln) — only the org-leave/undocumented-notice deviation is in scope.
- Shared ODCR / underlying EC2 capacity infrastructure; IMDS on managed hosts.
- Single-tenant self-DoS (owner thrashing *their own* consumers within one account).
- **Customer-authored** least-privilege gaps (the prerequisites sample is AWS-authored → Area 8 in scope *only* for its PassRole-prefix / `ec2:*` shape, as a shared Tier-2 note).
- `iam:PassRole`/SLR/KMS-grant depth, `$Latest` late-binding depth, EventBridge mechanism depth, auto-scaling, tag-authz — owned by the siblings; cross-referenced, not re-derived here.
- Anything implicating AWS's own service plane → **HARD STOP + disclosure**.

## 8. Null hypotheses / doc gaps / drift
- **Lens G (SSRF):** N/A — read target page, both procedure pages, prerequisites, monitor page; no field the service dereferences server-side (cr-id/market-type/count are not fetched URLs). `--cli-input-json file://` is client-side load only (confirmed in on-demand sibling), not SSRF.
- **Lens F / K / W / BB / CC / DD / FF / Y:** N/A — no translation layer, LLM, attestation gate, multi-parser request path, upstream-asserted-identity header, cache layer, JWT, or transport-floor claim on these pages.
- **Lens Q (16KB user-data via instant override):** low; cross-ref instance-weighting sibling Area 3 (not re-derived).
- **Lens H (KMS):** the prerequisites KMS-grant-to-SLR is a `maintain`-fleet concern; **instant fleets don't use the SLR**, so N/A for this tutorial. Core KMS-grant surface deferred to `ec2-fleet` core plan.
- **Lens A blind cross-account IDOR:** partial-null — `cr-<~17 hex>` is not fabricable; residual is within-org shared ids + the `DescribeCapacityReservations` enumeration oracle (Area 3), not guessing.
- **Reconfirmed:** ZERO `aws:PrincipalOrgID`/`aws:ResourceOrgID`/`aws:ResourceOrgPaths`/`aws:PrincipalOrgPaths` in `list_ec2` → the "within your AWS organization" ICR guarantee has **no EC2 resource-level IAM enforcement** (RAM/SCP only).
- **Open doc-gaps for the hunter:** (1) is the RAM share server-side-enforced at launch, or does a foreign cr-id leak an oracle/launch (Area 3)? (2) org-leave termination event/notice (Area 2)? (3) CR-group accept/reject for ICR ARN (Area 4)? (4) owner-quota-counts + consumer-pays facts are inferred from the general sharing page, not restated on ICR pages — confirm live. (5) `status:failed` cause + orphaned-instance behavior unstated. (6) no documented consumer-side early-release action. (7) multi-consumer contention/race resolution on one ICR pool unstated. (8) whether non-owner `DryRun` on the allocation actions probes source-CR existence (enumeration angle).
- **DRIFT (confirmed):** `autoscaling/ec2/userguide/asg-interruptible-capacity-reservations.html` now **301-redirects** to `capacity-reservation-create-asg-procedure.html#target-capacity-blocks-or-interruptible-capacity-reservations-from-a-launch-template` (offline mirror still has the standalone page). New online-only facts: **warm pools unsupported** with ICR; **one CR type per launch template**. All other UserGuide/APIReference pages: offline==online, no substantive drift (2026-10-15).
- **CONTRADICTION (confirmed, unresolved in docs):** CR-group membership of ICRs (Area 4) — both statements verbatim-present, both verified online.
