# EC2 Fleet — "Launch On-Demand Instances using *targeted* Capacity Reservations" Walkthrough — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-launch-on-demand-instances-using-targeted-capacity-reservations-walkthrough.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-fleet-launch-on-demand-instances-using-targeted-capacity-reservations-walkthrough.md`), plus supporting pages `ec2-fleet-on-demand-capacity-reservations.md`, `ec2-fleet-examples.md` (Examples 4–6, 12), `cr-groups-launch.md`, `capacity-reservation-sharing.md`; the IAM Service Authorization Reference `list_ec2.md` (CreateFleet detail block lines 5112–5123) and `list_resource-groups.md`; the API References `ARG/API_GroupResources`, `ARG/API_ListGroupResources`; RAM `shareable.md`. **Status: documentation-derived hypotheses only; nothing tested against a live account.** All offline==online cross-checks performed 2026-10-15 (online `.md` of `list_ec2` is summarizer-truncated before the CreateFleet rows — offline mirror read by targeted grep, confirmed exact sync).

**This is a page-level deep-dive CHILD of the `fleet-tutorials` hub.** It is scoped to the net-new surface *this* tutorial introduces and deliberately does **not** restate what the siblings already own. Cross-references:
- `fleet-tutorials-attack-research-plan.md` (hub) — the CR-consumption + cross-account/Org trust-boundary groundwork (hub Areas 1–8). This plan **deepens hub item 8** (CR Resource Group) and **hub item 2** (CreateFleet/RunInstances consume authz) to the page-content layer, and cross-refs hub items 1 (no Org IAM key), 3 (unscopable Describe oracles), 5 (interruptible reclaim), 6 (billing-ownership), 8 (shared-CR usage counts against owner quota).
- `ec2-fleet-on-demand-walkthrough-attack-research-plan.md` (sibling) — the On-Demand-primary mixed-purchasing config + the "forgotten self-healing fleet" default audit. **De-dup:** that plan's fleet is `maintain`/default; **this tutorial's fleet is `Type:instant`**, which flips a core assumption (see Area 0 note below).
- `ec2-fleet-instance-weighting-walkthrough-attack-research-plan.md` (sibling) — the launch-template `$Latest`/`$Default` late-binding + CreateFleet-has-no-`ec2:LaunchTemplate`-key headline. **This plan reuses that CreateFleet/LT-scoping finding and extends it to a *cross-service* late-bound target (the resource-groups group ARN).**
- `ec2-fleet-attack-research-plan.md` — core create/launch-template/PassRole/SLR/KMS depth (deferred).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Safe first oracle for every IAM lead is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resources touched). Escalate to a live scoped call only with synthetic canary data under a role holding *exactly* the artifact/grant being tested — never the over-privileged tester.
- **`DryRunOperation` is caller-IAM-only, evaluated BEFORE resource resolution — it is NOT an ownership oracle** (false-positive trap). The cross-account/foreign-group questions below cannot be settled by DryRun; they need a two-account canary.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

> **Area 0 — load-bearing distinction vs the maintain/Spot-Fleet siblings (read first).** The "fleet-services backbone finding" that governs every sibling plan — *instances are launched by the service-linked role, so the caller's identity-policy condition keys do not propagate to the launch* — **does NOT apply to this tutorial.** `ec2-fleet-prerequisites.md` (lines 33–34, confirmed): **"An `instant` EC2 Fleet does not require this role [`AWSServiceRoleForEC2Fleet`]."** This fleet is `Type:instant`, so the launch runs **directly under the caller's own IAM identity** — the caller must itself hold `ec2:CreateFleet` + `ec2:RunInstances`, and the caller's *expressible* `RunInstances` conditions **do** bind. Consequence for the hunter: the guardrail-bypass leads here are NOT "SLR strips my conditions"; they are "the specific control I need (which CR resource group / which prepaid capacity pool the fleet consumes) **has no condition key to express at all**, on either CreateFleet or RunInstances." Also confirmed irrelevant: `AWSEC2CapacityReservationFleetRolePolicy` (the `crf-*` SLR) governs the *Capacity Reservation Fleet* feature — a different feature from an EC2 Fleet consuming CRs via a resource group — and does not apply here.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Consume prepaid capacity you do not own/pay for:** make a `Type:instant` EC2 Fleet launch On-Demand Instances into `targeted` Capacity Reservations whose paying owner is another account/team, by routing through a Capacity Reservation resource group — proven by the victim's `AvailableInstanceCount` dropping while your instances run in their reserved capacity.
2. **Cross-service launch-placement influence without EC2 permissions:** holding only `resource-groups:GroupResources` (no `ec2:*`), change which CRs a referencing fleet consumes on its next invocation.
3. **Prove the CR-group target is IAM-unscopable:** show no identity policy on `CreateFleet` (or `RunInstances`) can pin/forbid the `CapacityReservationResourceGroupArn` a fleet targets, nor the CR id, nor the usage strategy.
4. **Read oracle:** enumerate another team's grouped Capacity Reservation ARNs (and the account ids they belong to) via an unscopable `ListGroupResources` / `DescribeCapacityReservations`.
5. **Revocation-completeness:** after a RAM-shared CR is unshared, show the group still references it and/or the fleet still consumes it (fail-open).
6. **Silent cost fallback:** force the documented "fall back to regular On-Demand" path to run billed capacity the operator did not intend.

---

## 2. Components, Assets, and Design

**Customer-facing interface:** AWS CLI/SDK (SigV4 IAM) across **two services** stitched together by this tutorial:
- `ec2`: `create-capacity-reservation` (Step 1), `create-launch-template` (Step 5), `create-fleet` (Step 7), `describe-capacity-reservations` (Step 8).
- `resource-groups`: `create-group` (Step 2), `group-resources` (Step 3), `list-group-resources` (Step 4).

**Assets / resource shapes:**
- **Capacity Reservation (CR)** — `arn:aws:ec2:${region}:${account}:capacity-reservation/cr-<hex>`. Prepaid On-Demand capacity. `instance-match-criteria`=`targeted` (this tutorial) means an instance must *explicitly target* it to use it. **RAM-shareable** cross-account/Org (`ec2:CapacityReservation`, `capacity-reservation-sharing.md`). A **cost/billing** asset — the owner pays whether or not it is used; a consumer's use counts against the **owner's** On-Demand quota (hub item 8).
- **Capacity Reservation resource group** — `arn:aws:resource-groups:${region}:${account}:group/${GroupName}`, configuration `{"Type":"AWS::EC2::CapacityReservationPool"}`. A layer of indirection the fleet targets instead of individual CRs. **Account-scoped ARN, but the account segment is the group OWNER's — not a constraint on member CRs.** NOT in the RAM shareable-resources catalog (only License-Manager `AWS::EC2::HostManagement` groups are shareable).
- **Launch template (LT)** — `lt-<hex>`; its `LaunchTemplateData.CapacityReservationSpecification.CapacityReservationTarget.CapacityReservationResourceGroupArn` names the group ARN. **The group ARN lives *inside the LT*, not in the create-fleet request.**
- **EC2 Fleet** — `Type:instant`; `TargetCapacitySpecification.DefaultTargetCapacityType:on-demand`; `OnDemandOptions.AllocationStrategy:lowest-price`; `OnDemandOptions.CapacityReservationOptions.UsageStrategy:use-capacity-reservations-first`.

**Identity:** SigV4 IAM. `instant` fleet launches **under the caller's own identity** (Area 0) — no SLR. Group operations are **account-level IAM** ("Resource Groups feature permissions are at the account level", `ARG/userguide/resource-groups.md`); Resource Groups **does not support resource-based policies** (`ARG/userguide/security_iam_service-with-iam.md`).

**Untrusted-data / cross-owner seam:** the CR ARNs added to a group (`group-resources`, Step 3) and the group ARN embedded in the LT (Step 5) are **caller-supplied strings naming resources that may belong to other accounts/teams**; the fleet dereferences the group → member CRs → prepaid capacity at launch time.

```
 caller IAM identity
   │  (1) ec2:CreateCapacityReservation  --instance-match-criteria targeted
   ▼
 CR cr-aaa, cr-bbb  (prepaid; owner pays; RAM-shareable) ─────────── other account's CR (RAM-shared in?) ??
   │  (3) resource-groups:GroupResources  ResourceArns=[cr-aaa, cr-bbb, <foreign cr?>]
   ▼
 CapacityReservationPool group  arn:...:resource-groups:...:group/my-cr-group
   │  (5) ec2:CreateLaunchTemplate  (CapacityReservationResourceGroupArn = group ARN)  ← group ARN is INSIDE the LT
   ▼
 Launch template lt-xxx
   │  (7) ec2:CreateFleet  Type=instant, UsageStrategy=use-capacity-reservations-first
   ▼
 instant Fleet → RunInstances (under CALLER identity) → resolves group → member CRs → launches into prepaid capacity
                                                              └─ runs out → SILENT fallback → regular (billed) On-Demand
```

---

## 3. API / Interface Inventory

| Name | Svc | Mutating | Ext | Functionality | Authorized callers | Notes / lead |
|---|---|---|---|---|---|---|
| CreateCapacityReservation | ec2 | yes | yes | create prepaid CR | holders of `ec2:CreateCapacityReservation` on `capacity-reservation*` | **`ec2:InstanceMatchCriteria` key EXISTS** (line 10093) → the ONE scopable control (Area 7) |
| GroupResources | resource-groups | yes | yes | add CR ARNs to a group | holders of ONLY `resource-groups:GroupResources` on `group*` | key = `aws:ResourceTag/${TagKey}` on the **group's own** tags only; `ResourceArns` regex permits any 12-digit account (Area 2) |
| UngroupResources | resource-groups | yes | yes | remove member | `group*` + group-tag key | membership mutation = launch-placement influence (Area 4) |
| ListGroupResources | resource-groups | no | yes | list members | `group*` | **"policy conditions… not currently supported"** → unscopable read oracle (Area 6) |
| CreateLaunchTemplate | ec2 | yes | yes | LT embedding group ARN | `ec2:CreateLaunchTemplate` | group ARN is LT content → escapes CreateFleet resource-perms (Area 1) |
| CreateFleet | ec2 | yes | yes | launch instant fleet | caller (holds RunInstances) | **no key for group/CR-id/UsageStrategy/FleetType** anywhere (Area 1) |
| RunInstances | ec2 | yes | yes | underlying launch (caller identity) | caller | `capacity-reservation` row has `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource`; `group` row only `ec2:Region` (Area 1) |
| DescribeCapacityReservations | ec2 | no | yes | remaining-capacity readout (Step 8) | caller | unscopable account-wide (hub item 3) — read oracle (Area 6) |

No `[NEW]` marker on this page, but the **`ReservedCapacityOptions` / `DefaultTargetCapacityType:reserved-capacity`** multi-CR-types path (`ec2-fleet-examples.md` Example 12 + sibling tutorial `ec2-fleet-launch-instances-multiple-cr-types-walkthrough.html`) is the newest adjacent surface and reuses the **same resource-group indirection** — every Area below applies to it with higher stakes (Capacity Blocks for ML / interruptible CRs); flag for the hub and that future sibling, do not own here.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| caller identity | another account's prepaid CR | `GroupResources` adds a foreign CR ARN → fleet launches into it | victim's `AvailableInstanceCount` drops / your instance runs in their reserved capacity = **cross-account breach** |
| `resource-groups:GroupResources`-only principal | EC2 launch placement of a fleet it has no `ec2:*` for | mutate group membership the LT points at | fleet's next instant invocation consumes a different CR set than its owner intended |
| CreateFleet identity policy (admin intent) | the CR resource group a fleet may target | group ARN sits inside LT; no condition key exists | an admin's attempted Deny/scope on the group ARN is **inert** (SimulatePolicy shows no key binds) |
| any caller | account-wide group membership + CR inventory | `ListGroupResources` (unscopable) / `DescribeCapacityReservations` | reading another team's grouped CR ARNs + owning account ids |
| RAM-share revoker | consumer still using the unshared CR | unshare after it was grouped | fleet still launches into / group still lists the revoked CR = fail-open revocation |
| **any customer surface** | **AWS service plane** | — | **hard stop** |

---

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE, Lens U / X / S] The targeted-CR consume target is specified inside the launch template → IAM-unscopable on the fleet path
**Background.** Step 5 puts `CapacityReservationResourceGroupArn` **inside the launch template**; Step 7's `create-fleet` only names the LT. The whole point of `targeted` CRs is isolation — `ec2-fleet-on-demand-capacity-reservations.md` (verbatim): *"If a Capacity Reservation is `targeted`, On-Demand Instances must specifically target it to run in the reserved capacity."* The resource group is **how** the fleet does that targeting.
**Security Concern.** `list_ec2.md` CreateFleet Description (line 5114, verbatim): *"Resource-level permissions for this action do not include the resources specified in a launch template. To specify resource-level permissions for resources specified in a launch template, you must include the resources in the RunInstances action statement."* And exhaustive grep confirms **no condition key exists anywhere in `list_ec2` for `CapacityReservationResourceGroupArn`, the resource-groups ARN, `CapacityReservationId` (exact), `UsageStrategy`, or `FleetType`.** CreateFleet's `capacity-reservation` row (line 5115) carries only `aws:ResourceTag`/`ec2:Region`/`ec2:ResourceTag` — no CR-id, no match-criteria, no `ec2:CapacityReservationFleet`. CreateFleet has **no `group` resource-type row at all**. Even RunInstances' `group` row (line 9589) carries only `ec2:Region`, and the `group` ARN's condition-key cell (line 9943) is **empty**. ⇒ an admin **cannot author an identity policy that pins which CR resource group — i.e. which pool of prepaid capacity — a fleet is allowed to consume**, nor forbid targeting a group at all, on either the fleet path or the underlying RunInstances. This is the same "un-LT-scopable launch path" shape as the instance-weighting sibling's Area 1, extended to a **cross-service, cost-bearing target**. (Note the asymmetry/Lens X: RunInstances' `capacity-reservation` row DOES get `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource` keys that CreateFleet's does not — a per-launch LT-provenance control available on the direct API but absent on the fleet path.)
**High-level Test Scenarios.**
- Author a policy that `Deny`s `CreateFleet`/`RunInstances` unless the targeted group ARN equals an approved value → `iam:SimulateCustomPolicy` should show **no key available to express it** (the Deny is structurally inauthorable). Confirm the only scoping available is the LT's own tag/id (which does not constrain the *group inside* it, since `$Latest`/a new LT version can swap the embedded group — chains to instance-weighting sibling Area 2).
- Confirm `use-capacity-reservations-first` and `Type=instant` are likewise unconditionable (no key) → the usage strategy cannot be mandated or forbidden by IAM.
**Doc evidence:** `list_ec2.md` lines 5114, 5115, 5119, 9589, 9943; walkthrough Steps 5 & 7. **Severity-if-true:** Lens U/S enforcement-gap = **Medium** (AWS-owned, uneditable action-row fact; reportable as the inability to express a least-privilege control over prepaid-capacity consumption); upgrades to **High** when it is the *enabling* precondition for Area 2's cross-account consume. **Stop:** once SimulatePolicy confirms no key binds the group ARN on either action.

### Area 2 — [Lens A / EE — cross-account & cross-team group membership] Can a foreign Capacity Reservation be grouped and consumed?
**Background.** Step 3 (`group-resources`) adds CR ARNs — strings carrying a 12-digit account id — to the pool group. Individual CRs are **RAM-shareable cross-account/Org** (`capacity-reservation-sharing.md`: *"share their reserved capacity with other AWS accounts or within an AWS organization"*).
**Security Concern.** `GroupResources` requires **only** `resource-groups:GroupResources` (API_GroupResources "Minimum permissions" — no `ec2:*`), its sole condition key is `aws:ResourceTag/${TagKey}` **on the group's own tags**, and the `ResourceArns` parameter regex `arn:aws(-[a-z]+)*:[a-z0-9\-]*:…:([0-9]{12})?:.+` **permits any 12-digit account segment with no documented comparison to the caller's own account**. No page (SAR, API Reference, ARG User Guide) states "only resources you own can be added to a group"; the only account language is "permissions are at the account level." ⇒ it is **undocumented whether `GroupResources` validates that the member CR ARNs are owned by (or RAM-shared to) the caller.** If it does not — or validates only RAM-share visibility, not ownership — a caller can group a **RAM-shared-in** (or, worst case, an arbitrary foreign) `targeted` CR, point an LT at that group, and launch an `instant` fleet that **consumes prepaid capacity the victim paid for**, decrementing the victim's `AvailableInstanceCount` and burning the victim's On-Demand quota (hub item 8).
**High-level Test Scenarios (two-account canary required — DryRun cannot answer; it is caller-IAM-only pre-resolution).**
- Account B shares a `targeted` CR to Account A via RAM. From A, `group-resources` it into A's pool group. Create an LT+instant fleet in A targeting the group. Oracle: does `describe-capacity-reservations` (run as B) show B's `AvailableInstanceCount` drop while A's instances run? = **cross-account prepaid-capacity theft**.
- Negative control: attempt to group a **non-shared** foreign CR ARN directly — does `GroupResources` return `NotFoundException` (owner-opaque), `ForbiddenException`, or **succeed**? Distinguish the three (Lens A error oracle). Success = the stronger breach.
- Intra-account cross-team: with ONLY `resource-groups:GroupResources` (no `ec2:*`), add Team-X's CR into a group Team-Y's fleet references → influence Team-Y's launch placement with zero EC2 rights.
**Doc evidence:** `API_GroupResources.md` (minimum perms; ResourceArns regex; Errors); `list_resource-groups.md` (GroupResources → `group*` + `aws:ResourceTag` only); `capacity-reservation-sharing.md`; RAM `shareable.md`. **Severity-if-true:** cross-account prepaid-capacity consumption / quota exhaustion = **High** (cross-account cost + resource impact); intra-account cross-team = Medium (least-priv footgun, but AWS-doc-silent on the ownership check so worth confirming). **Stop:** the instant evidence of a foreign/shared CR's count decrementing under your fleet — do not iterate records; one CR, one instance is the PoC.

### Area 3 — [Lens AA — share/revoke lifecycle & revocation completeness]
**Background.** The group can mix owned + shared CRs (hub item 8); member CRs are added once (Step 3) but RAM shares are revocable independently; the hub also flagged **interruptible** CRs that the owner can forcibly reclaim (hub item 5) and the multi-CR-types extension (Example 12) that puts interruptible/Capacity-Block CRs in the same group.
**Security Concern.** No page documents what happens to group membership or an in-flight fleet launch when a **shared CR is unshared/revoked after it was grouped**, or when a member CR is cancelled/expires. Does the group silently retain a dangling member? Does the next `instant` launch into the revoked CR **fail-open** (fall through to billed On-Demand) or fail-closed? For interruptible CRs reclaimed mid-use (hub item 5: 2-min warning, "org-leave = eventually terminated, no documented event") — does the group/fleet surface any signal?
**High-level Test Scenarios.** Group a shared CR → unshare it (as owner) → run the instant fleet in the consumer → observe whether it launches into the now-unshared CR, errors, or silently falls back (Area 5). Confirm `list-group-resources` still lists the revoked member (dangling-reference oracle).
**Doc evidence:** `capacity-reservation-sharing.md`; hub items 5/8; `ec2-fleet-examples.md` Example 12. **Severity-if-true:** surviving cross-account consumption after unshare = **High**; dangling member only = Low–Medium. **Stop:** first observation of post-revoke launch or dangling listing.

### Area 4 — [Lens B / EE — launch-template → group ARN late-binding; group-name land-grab]
**Background.** The LT references the group **by ARN**, resolved to member CRs **at launch time** (`cr-groups-launch.md` describes the resolution). `GroupResources`/`UngroupResources` mutate membership independently and asynchronously.
**Security Concern.** A principal holding **only `resource-groups:GroupResources`/`UngroupResources`** (no `ec2:RunInstances`, no `iam:PassRole`, no LT edit) controls **which prepaid CRs every future `instant` invocation of any fleet referencing that group consumes** — a cross-service launch-influence primitive with no EC2 permission. Distinct from the instance-weighting sibling's `$Latest`/`$Default` LT-version late-binding (Area 2 there): this is late-binding of **group membership**, a different, cross-service control plane. Additionally, group **names are account+region-scoped first-come** (`CreateGroup` has blank resource type; name is the identity) → an intra-account attacker can **pre-create `my-cr-group`** before an IaC deploy or victim-team references it (Lens EE land-grab), so the victim's LT (which may reference the group by a name resolved to ARN) resolves to the attacker's group of attacker-chosen CRs. (The tutorial's LT uses the full ARN incl. account id, which blocks *cross-account* by-name; confirm whether any console/by-name path resolves the group without pinning account.)
**High-level Test Scenarios.** Create a fleet+LT referencing group G. As a separate principal with only `resource-groups:*` on G, `UngroupResources` the owner's CRs and `GroupResources` your own (or a foreign/shared) CR. Re-invoke the instant fleet. Oracle: it consumes the swapped CR set. / Pre-create a predictable group name and see if a victim workflow adopts it.
**Doc evidence:** `cr-groups-launch.md`; `list_resource-groups.md` (CreateGroup blank resource type; GroupResources group-tag-only key); walkthrough Steps 2/3/5/7. **Severity-if-true:** EC2-less launch-placement control / prepaid-capacity redirection = **Medium–High**; name land-grab adopted by victim = High. **Stop:** first swapped-launch observation.

### Area 5 — [Lens U — documented guarantees: `instant`-only + silent On-Demand fallback]
**Background.** Two assertions: (a) *"On-Demand Capacity Reservations are available only for EC2 Fleet with the request type set to `instant`"* / *"You can't use Capacity Reservations for fleets of other types"*; (b) *"if it runs out of Capacity Reservations before the target On-Demand capacity is fulfilled, the fleet can launch the remaining target capacity into regular On-Demand capacity"* (`ec2-fleet-on-demand-capacity-reservations.md`), and the walkthrough's "4 additional On-Demand Instances are launched into regular On-Demand capacity."
**Security Concern.** (a) **What enforces `instant`-only?** No `FleetType` condition key exists (Area 1), so it is API-validation/orchestration only, not IAM. Does `CreateFleet` with `Type:maintain`/`request` + `CapacityReservationOptions.UsageStrategy:use-capacity-reservations-first` return a synchronous `ValidationException`, **silently ignore** the field (launch without CR targeting), or exhibit undefined behavior? A silently-ignored usage-strategy on a `maintain` fleet = a long-lived fleet that *looks* CR-pinned but launches billed On-Demand. (b) The **silent fallback** to regular (billed) On-Demand is cost-relevant: there is **no distinct alarmable fleet state** for "I exhausted my reservations and am now paying on-demand" on a `maintain`/`request` fleet (cross-ref on-demand sibling Area 2: `errorSet` is `instant`-only). For `instant` here, the fallback is immediate and visible in the response, but an operator who mis-sizes `TotalTargetCapacity` above the grouped CR count silently pays for the overflow.
**High-level Test Scenarios.** Submit `use-capacity-reservations-first` on a `maintain` fleet → classify the response (reject / ignore / accept). Confirm whether anything warns when `TotalTargetCapacity` > grouped unused CRs (the walkthrough's 10 vs 6 case is the documented norm — fallback is *expected*, which is itself the footgun). 
**Doc evidence:** `ec2-fleet-on-demand-capacity-reservations.md`; walkthrough Step 7 Note + outcome; `ec2-fleet-examples.md` Examples 4–6. **Severity-if-true:** silently-ignored strategy on a long-lived fleet = **Medium** (cost/intent integrity); pure cost-overflow footgun = Low. **Stop:** once the maintain-fleet acceptance behavior is classified.

### Area 6 — [Lens A — unscopable read oracles for recon]
**Background.** Step 4 (`list-group-resources`) and Step 8 (`describe-capacity-reservations`) are the readouts.
**Security Concern.** `ListGroupResources` carries a formal `aws:ResourceTag` cell in `list_resource-groups`, but `ARG/userguide/gettingstarted-prereqs-permissions.md` states verbatim: **"Using policy conditions with `resource-groups:ListGroupResources` is not currently supported."** ⇒ it is effectively **unscopable** — any principal with the action reads **every group's membership account-wide**, leaking the CR ARNs (and their owning account ids) inside each pool group. Combined with `DescribeCapacityReservations` being unscopable account-wide (hub item 3; `list_ec2` gives it blank resource-type + only `ec2:Region`), a low-priv caller can **enumerate which teams/accounts' CRs are in which groups** — the exact recon that makes Area 2/Area 4's membership-mutation practical (no prior id knowledge needed). This is the resource-groups twin of `manage-spot-fleet`'s unscopable `DescribeSpotFleetRequests` oracle (same inert-ABAC shape, different service).
**High-level Test Scenarios.** With a scoped role holding only `resource-groups:ListGroupResources`, enumerate groups and dump member CR ARNs; confirm an `aws:ResourceTag` Deny on the group is inert against this action (SimulatePolicy + live). Cross-reference leaked account ids to confirm cross-account members exist.
**Doc evidence:** `ARG/userguide/gettingstarted-prereqs-permissions.md`; `list_resource-groups.md`; `list_ec2` DescribeCapacityReservations row (hub item 3). **Severity-if-true:** account-wide membership/inventory disclosure = **Low–Medium** (recon enabler; raises Area 2/4 severity). **Stop:** confirm the condition-key inertness; do not enumerate beyond proof.

### Area 7 — [Lens S — the ONE scopable control, and its placement asymmetry]
**Background / net-positive finding.** Unlike the consume path, the **creation** of a `targeted` CR *is* scopable: `ec2:InstanceMatchCriteria` is a real condition key (`list_ec2` line 10093, present on `CreateCapacityReservation` line 5024). An admin **can** write `"StringEquals":{"ec2:InstanceMatchCriteria":"targeted"}` to force all CRs created in the account to be `targeted` (not `open`).
**Security Concern (the asymmetry).** The isolation primitive is enforceable **where the CR is born** but **not where it is consumed** (Area 1): there is no key to constrain which `targeted` CR / group a fleet then targets. So `ec2:InstanceMatchCriteria` protects against *open* CRs being auto-consumed by any matching instance, but does nothing about a fleet deliberately targeting a *group* of someone's `targeted` CRs (Area 2). Also test the case-sensitivity fail-open class (Lens S variant): is a Deny written against lowercase `"targeted"` inert if the request field is populated with a different casing? And confirm `ec2:InstanceMatchCriteria` is **absent** from `CreateFleet`/`RunInstances` (it is — grep-confirmed), i.e. you cannot require "only consume targeted CRs" at launch.
**High-level Test Scenarios.** SimulatePolicy an `ec2:InstanceMatchCriteria=targeted` Deny on `CreateCapacityReservation` (should bind) and the same key on `CreateFleet` (should be inert/absent). Test enum casing.
**Doc evidence:** `list_ec2` lines 5024, 10093; CreateFleet block 5112–5123. **Severity-if-true:** informational/hardening (documents the one place a control exists and its blind spot). **Stop:** after confirming the two Simulate results.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Fleet consumes another account's prepaid `targeted` CR via a group | `GroupResources` + instant fleet | *(none found)* — no ownership-check prose; `ResourceArns` regex permits foreign account |
| IAM cannot pin which CR group a fleet targets | CreateFleet / RunInstances | CreateFleet Description line 5114 (LT contents outside resource-perms); no group/CR-id/UsageStrategy key |
| `resource-groups`-only principal redirects a fleet's prepaid capacity | GroupResources/UngroupResources late-binding | *(none)* — membership key is group-tag only; EC2 not required |
| Post-unshare consumption / dangling member | RAM unshare + group | *(none documented)* — fail-open unknown |
| Silently-ignored `use-capacity-reservations-first` on non-instant fleet | CreateFleet validation | "instant only" prose; **no `FleetType` IAM key** enforcing it |
| Account-wide group-membership / CR-inventory disclosure | ListGroupResources / DescribeCapacityReservations | "policy conditions not supported" (ListGroupResources); blank resource type (Describe) |
| Force `targeted` at CR creation | CreateCapacityReservation | **`ec2:InstanceMatchCriteria`** (the one working control) |

---

## 7. Out-of-Scope Risk Categories
- The EC2 Fleet SLR / PassRole / confused-deputy depth — **and note it mostly does not even arise here** because `instant` fleets use no SLR (Area 0). PassRole/SLR surface for maintain/Spot fleets → `ec2-fleet-prerequisites`/`create-spot-fleet`/`ec2-fleet` plans.
- Launch-template `$Latest`/`$Default` version late-binding & CreateFleet-has-no-`ec2:LaunchTemplate`-key → owned by `ec2-fleet-instance-weighting-walkthrough` plan (this plan reuses, does not restate).
- The On-Demand-primary mixed-purchasing config, "forgotten self-healing fleet" defaults → `ec2-fleet-on-demand-walkthrough` plan (that fleet is maintain; this one is instant).
- CloudWatch/EventBridge monitoring, auto-scaling, cancel/terminate, modify-time mutation, tag-authz → the respective siblings.
- Org-boundary enforcement in EC2 IAM — confirmed **structurally absent** (zero `aws:PrincipalOrgID`/`ResourceOrgID` in `list_ec2`; hub item 1) — RAM/SCP-only; not re-tested here.
- `ReservedCapacityOptions`/`reserved-capacity` multi-CR-types + Capacity Blocks for ML + interruptible-reclaim depth → the hub + the `ec2-fleet-launch-instances-multiple-cr-types-walkthrough` sibling (flagged in §3; this plan's Areas apply but with higher stakes there).
- IMDS/instance-level config on managed hosts; single-tenant self-DoS; customer-authored-policy footguns.
- `--cli-input-json file://` — client-side botocore file load only, no `http(s)` scheme — confirmed N/A as SSRF by the on-demand sibling; not re-tested.

## 8. Null hypotheses / doc gaps (pages checked named)
- **Lens G (SSRF) — N/A.** Checked all 8 walkthrough steps + `ec2-fleet-on-demand-capacity-reservations.md` + `cr-groups-launch.md`: no field the service dereferences by URL/host; the only "dereferenced" inputs are ARNs resolved internally (covered by Lens A/EE, not SSRF). `CapacityReservationResourceGroupArn` is an ARN, not a fetched URL.
- **Lens Q (upload), F (translation/injection), K (prompt), W (attestation), FF (token/JWT), DD (cache), BB (canonicalization), CC (upstream-context), Y (TLS/sig) — N/A** for this documentation surface: it is a pure IAM/CLI control-plane workflow with no parser, blob upload, LLM, enclave gate, JWT, caching layer, multi-parser request path, upstream-identity header, or http endpoint on the pages read (walkthrough + examples + CR-usage + cr-groups-launch + the two SAR tables + RAM shareable + ARG user guide pages).
- **Lens J (OAuth) — N/A** (no 3P linking).
- **DOC GAP (highest-value open, gates Area 2 severity):** no page states whether `resource-groups:GroupResources` validates owner/account of the member `ResourceArns`, nor whether EC2-Fleet/RunInstances resolution of `CapacityReservationResourceGroupArn` enforces that the group's account matches the caller's. The API Reference's `NotFoundException` ("resources don't exist") is ambiguous for a resource that exists in another account. **Must be settled with a two-account canary before investing in the cross-account consume chain — do not infer from DryRun.**
- **DOC GAP:** `AWS::EC2::CapacityReservationPool` resource groups are **absent** from the RAM shareable catalog (only `AWS::EC2::HostManagement` groups appear), but no page states explicitly that CapacityReservationPool groups *cannot* be RAM-shared — confirm the group itself is non-shareable (so cross-account must go via sharing the individual CRs, per Area 2/3), vs. an undocumented share path.
- **DOC GAP:** behavior of `use-capacity-reservations-first` submitted on a `maintain`/`request` fleet (reject vs silent-ignore vs accept) is undocumented (Area 5).
- **DOC GAP:** whether `targeted`-CR isolation ("must specifically target it") is enforced server-side at launch against the *group membership* or merely trusts the group resolution (Area 2 refute path).

---
*Companion to the `fleet-tutorials` hub and the two walkthrough siblings. The net-new surface this page contributes to the EC2-Fleet corpus is the **`resource-groups` cross-service indirection as an IAM-unscopable, cost-bearing consume target** (Areas 1/2/4/6) — the first sibling where the launch target lives in a *different service* with its own (weaker, tag-and-account-level, no-resource-policy) authorization model.*
