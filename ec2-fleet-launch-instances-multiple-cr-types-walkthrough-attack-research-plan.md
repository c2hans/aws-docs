# EC2 Fleet — "Launch instances into multiple Capacity Reservation types" (`ReservedCapacityOptions`) — Attack / Research Plan

> **Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-launch-instances-multiple-cr-types-walkthrough.html`
> (offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-fleet-launch-instances-multiple-cr-types-walkthrough.md`)
> **Service:** Amazon EC2 — EC2 Fleet (`CreateFleet`), Capacity Reservations, Capacity Reservation Resource Groups
> **Produced by:** `security-questionbuilder` skill (documentation-only; no live AWS contact)
> **Date:** 2026-10-15
> **Status of surface:** NET-NEW. This walkthrough documents the brand-new `ReservedCapacityOptions` request structure and the `DefaultTargetCapacityType: "reserved-capacity"` enum value for `CreateFleet`. Both are API-documented but barely integrated into the rest of the docs (absent from the CLI JSON skeleton page and `create-ec2-fleet` examples). High-value because it is new, mixes three capacity-reservation ownership models in one request, and — per the IAM audit below — ships with **zero service-specific condition keys**.

---

## §0 — How to use this plan (reader orientation)

This plan is written so a hunter with a two-account (ideally three-account, cross-Organization) AWS test harness can pick it up cold. Read in this order:

1. **§1 Components / Assets / Design** — what the feature actually is and the exact request shape.
2. **§2 Trust-boundary map** — the ownership seams and the breach oracle for each.
3. **§3 API / interface inventory** — what you can call, what's new, what's internal.
4. **§4 Boundary-lens leads** — the falsifiable hypotheses, each with a confirm/refute oracle. This is the executable core.
5. **§5 Priority ordering** — where to spend the first day.
6. **§6 Canary / harness requirements** — what you must stand up before testing.
7. **§7 Cross-references** — what this plan deliberately does NOT re-derive (owned by sibling plans).
8. **§8 Null hypotheses** — lenses checked and found not to fire, with pages read.

**Scope discipline (inherited, non-negotiable):** documentation-only reasoning here; a hunter executes later against authorized accounts only. Every lead claims a boundary *might not hold* — none asserts a confirmed bug. Read-only / minimum-PoC payloads only. **Hard stop:** the instant any evidence surfaces an identity / credential / ARN / account belonging to AWS's own service plane (not a customer tenant), preserve evidence and flag for AWS-Security disclosure — do not probe further.

**Oracle hygiene reminders for the executing hunter:**
- `DryRunOperation` is **caller-IAM-only**, evaluated *before* resource resolution — it is NOT an ownership oracle. Never settle a cross-account/foreign-resource claim with DryRun.
- `iam:SimulateCustomPolicy` / `SimulatePrincipalPolicy` is the safe *first* oracle for "does this policy even have a lever."
- Any cross-account / foreign-CR claim requires a genuine **two-account (or cross-Org) canary** — it cannot be settled from one account.

---

## §1 — Components, Assets, and Design

### 1.1 What the feature is

A single `CreateFleet` call of **`Type: "instant"`** that fills a target capacity by drawing from a **mix of Capacity Reservation (CR) types** — On-Demand Capacity Reservations (ODCRs), Capacity Blocks for ML, and interruptible Capacity Reservations — reached indirectly through a **Capacity Reservation Resource Group** named only by its group ARN in the launch template, with per-type priority arbitration and an on-demand fallback.

### 1.2 The exact request shape (from the walkthrough `config.json` + API refs)

```
CreateFleet (Type: "instant")
├─ LaunchTemplateConfigs
│   ├─ LaunchTemplateSpecification: {LaunchTemplateName: "my-cr-resource-group-template", Version: "1"}
│   │     └─ (LT embeds CapacityReservationSpecification.CapacityReservationTarget
│   │          .CapacityReservationResourceGroupArn = arn:aws:resource-groups:...:group/...)
│   └─ Overrides:
│        • p5.48xlarge / us-east-1a / Priority 1
│        • p4d.24xlarge / us-east-1b / Priority 2
├─ TargetCapacitySpecification
│   ├─ TotalTargetCapacity: 100
│   └─ DefaultTargetCapacityType: "reserved-capacity"      ← NEW enum value
└─ ReservedCapacityOptions                                  ← NEW structure
    ├─ AllocationStrategy: "prioritized"                    (only "prioritized"; omit = random)
    ├─ ReservationTypes (ORDERED): ["on-demand-capacity-reservation",
    │                               "capacity-block",
    │                               "interruptible-capacity-reservation"]
    └─ ReservedCapacityFallbackOptions.MarketTypes: ["on-demand"]   (only "on-demand"; omit = no fallback)
```

**Prerequisite CRs placed in the group (from the walkthrough):**

| CR ID | Type | Instance / AZ | Ownership |
|---|---|---|---|
| `cr-1234567890abcdef1` | ODCR | p5.48xlarge / us-east-1a | yours |
| `cr-abcdef1234567890a` | ODCR | p4d.24xlarge / us-east-1b | yours |
| `cr-0123456789abcdef0` | Capacity Block | p5.48xlarge / us-east-1a | yours |
| `cr-9876543210fedcba9` | interruptible CR | p5.48xlarge / us-east-1a | **"shared with you by another account in your organization"** |

### 1.3 The alternate, under-documented targeting path (net-new vector)

`API_FleetCapacityReservationTargetRequest.md` shows the fleet can name CRs **two ways**:
- `CapacityReservationResourceGroupArn.N` — the group-ARN indirection the tutorial uses, OR
- `CapacityReservationId.N` — **an explicit array of CR IDs supplied directly in the `CreateFleet` request body.**

The walkthrough only demonstrates the group-ARN path. The direct-CR-ID-array path is API-reachable but not walked, not in the CLI skeleton, and is the sharpest IDOR surface in §4 Lens A.

### 1.4 Assets & identifiers

- **Capacity Reservation ID** shape: `cr-` + 17 hex (`cr-0123456789abcdef0`) — structured, 17-char; enumerability must be assessed (Lens A).
- **CR group ARN**: `arn:aws:resource-groups:<region>:<account>:group/<name>` — a **`resource-groups` service ARN**, i.e. a cross-service pointer; EC2 dereferences it.
- **The capacity itself** is the asset: compute hours someone paid for, counting against someone's On-Demand service quota.
- **Identity:** SigV4 IAM. `instant` fleet runs **under the CALLER's identity** (no service-linked role — see §2.3), so caller IAM conditions bind — but see §4 Lens S: there are no conditions to bind.

### 1.5 ASCII pipeline

```
                 Consumer account (CALLER)
                        │  CreateFleet(instant, ReservedCapacityOptions, group ARN)
                        ▼
   ┌─────────────────────────────────────────────────────────┐
   │ EC2 Fleet (instant → runs under caller identity, no SLR) │
   └─────────────────────────────────────────────────────────┘
                        │ dereferences group ARN  (cross-service → resource-groups)
                        ▼
   ┌───────────────────────────── CR Resource Group ──────────────────────────────┐
   │  ODCR (you)   ODCR (you)   Capacity Block (you)   interruptible CR (ANOTHER    │
   │                                                   ACCOUNT, shared via RAM)      │
   └────────────────────────────────────────────────────────────────────────────────┘
         │                                   │                         │
         ▼                                   ▼                         ▼
   capacity you paid for             capacity you paid for      capacity OWNER paid for;
                                     owner-set end time         owner reclaims at will (2-min notice);
                                     (40/10-min notice)         counts vs OWNER's On-Demand quota
```

---

## §2 — Trust-boundary map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| B1 | Consumer account (fleet caller) | A CR **owned by a different account** | `ReservedCapacityOptions.CapacityReservationTarget` naming a group that contains a shared-in CR, or a CR ID directly | Fleet launches into / consumes a CR the caller does **not** own and that was **not shared** to the caller = cross-account breach. (If only *shared* CRs are reachable, that is by-design, not a breach — the test is reaching an UN-shared one.) |
| B2 | Consumer account | Another account's **On-Demand service quota** | Owner-pays / owner-quota attribution model (`capacity-reservation-sharing.md`) | Consumer fleet exhausts the **owner's** On-Demand instance limit via launches the owner never authorized per-call = cross-account quota/DoS. |
| B3 | CR **owner** account | Consumer account's **running instances** | `update-interruptible-capacity-reservation-allocation` (reclaim) / Capacity-Block end-time | Owner unilaterally force-terminates consumer compute with ≤2-min (interruptible) or ~30-min (block) notice, no consumer veto = cross-account forced-termination primitive. |
| B4 | EC2 (service) | `resource-groups` service | Group-ARN dereference during fleet fulfilment | EC2 resolves/consumes group members with an authorization check that does **not** re-verify the caller's rights to each member CR = confused-deputy / cross-service authz gap. |
| B5 | IAM policy author (defender) | The whole `ReservedCapacityOptions` feature | IAM condition keys on `CreateFleet` | **No condition key exists** to scope *which* CRs / CR types / groups / fallbacks a principal may use = unscopable surface (the central finding). |
| B6 | Doc reader (defender building the config) | Actual API behaviour | The walkthrough's prose guarantees | A documented guarantee ("instant-only", "mutually exclusive with OnDemandOptions", "can't add interruptible to groups") is contradicted elsewhere or not enforced = doc-vs-doc / doc-vs-enforcement gap. |
| B7 | Any customer surface | **AWS's own service plane** | — | **HARD STOP** — any AWS-fleet identity/credential/ARN/account surfaced ⇒ preserve + disclose. |

### 2.3 Backbone note (instant fleet identity)

`ec2-fleet-prerequisites.md` line 34: *"An instant EC2 Fleet does not require this role"* (the SLR `AWSServiceRoleForEC2Fleet`). So the `instant` fleet in this walkthrough acts under the **caller's** identity — meaning any caller IAM condition *would* bind at fulfilment time. The force of §4 Lens S is precisely that **there are no conditions to bind for this feature** — the one place the backbone would help, the keys don't exist.

---

## §3 — API / interface inventory

| Name | Mutating? | New/Existing | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `CreateFleet` (`Type:instant`, `DefaultTargetCapacityType:reserved-capacity`, `ReservedCapacityOptions`) | **Yes** | **NEW parameters on existing API** | Yes (SigV4) | any principal with `ec2:CreateFleet` | Prime target. Params below are the net-new surface. |
| ↳ `ReservedCapacityOptions.ReservationTypes.N` | — | NEW | — | — | Ordered list → priority/exhaustion arbitration across CR types (Lens U/arbitration). |
| ↳ `ReservedCapacityOptions.CapacityReservationTarget.CapacityReservationId.N` | — | NEW | — | — | **Direct CR-ID array in request body** — not walked by tutorial. Lens A prime. |
| ↳ `ReservedCapacityOptions.CapacityReservationTarget.CapacityReservationResourceGroupArn.N` | — | NEW | — | — | Cross-service pointer to `resource-groups`. Lens B4. |
| ↳ `ReservedCapacityOptions.ReservedCapacityFallbackOptions.MarketTypes.N` | — | NEW | — | — | Only `on-demand`. Lens U (can't be IAM-forbidden). |
| ↳ `ReservedCapacityOptions.AllocationStrategy` | — | NEW | — | — | `prioritized` only; omit = random. |
| `CreateCapacityReservation` / `CreateCapacityReservationBySplitting` | Yes | Existing | Yes | any w/ perm | Owner-side; interruptible via allocation action. |
| `create-interruptible-capacity-reservation-allocation` | Yes | Existing (interruptible) | Yes | CR owner | Owner creates the lent capacity. |
| `update-interruptible-capacity-reservation-allocation --target-instance-count N` | **Yes** | Existing | Yes | **CR owner only** | **Cross-account forced-termination primitive** (B3). 2-min EventBridge warning. |
| `resource-groups:GroupResources` / `ListGroupResources` | Yes / No | Existing (cross-service) | Yes | per `resource-groups` IAM | **Zero condition keys** (Subagent 2 §5/§6). Grouping + enumeration path. |
| RAM `create-resource-share` / `associate-resource-share` | Yes | Existing | Yes | CR owner | The ACTUAL org-scoping enforcement point — not EC2 IAM (B5/Lens S). |
| `DescribeFleets` / `DescribeFleetInstances` / `DescribeInstances` | No | Existing | Yes | caller | Post-hoc: reveals per-instance `CapacityReservationId` (ownership only visible *after* launch, not in config). |

**Doc-flagged leads kept verbatim:**
- `API_CreateFleet.md` lines 58–62: `ReservedCapacityOptions` *"Supported only for fleets of type `instant`."* Context field: *"Reserved."*
- `API_ReservedCapacityOptionsRequest.md`: *"only used if EC2 Fleet is of type instant"* + must set `DefaultTargetCapacityType=reserved-capacity`; `CapacityReservationTarget` = CR IDs **or** group ARN, not both.
- Walkthrough Considerations: instant-only; must **explicitly** specify `ReservationTypes`; `ReservedCapacityOptions` **mutually exclusive** with `OnDemandOptions.CapacityReservationOptions`.
- `API_CreateFleetError.md`: `lifecycle` valid values = spot | on-demand | interruptible-capacity-reservation | capacity-block.

**Console-hidden / under-surfaced knobs (the delta is the lead):**
- The entire `ReservedCapacityOptions` structure and the `reserved-capacity` default type are **absent from the `create-ec2-fleet.md` JSON config/CLI skeleton page** and from `ec2-fleet-examples.md` (Subagent 1). API-reachable, prose-invisible — classic under-tested surface.
- The `CapacityReservationId.N` direct-targeting array (vs. the group-ARN path the tutorial walks).

---

## §4 — Boundary-lens leads (the executable core)

### Lens A — Cross-tenant / cross-account resource access (IDOR) — **PRIMARY**

**A1 — Direct CR-ID targeting of a CR you neither own nor were shared.**
- **Claim:** `CreateFleet` with `ReservedCapacityOptions.CapacityReservationTarget.CapacityReservationId=["cr-<foreign>"]` consumes a CR owned by another account that was never shared to the caller, because fulfilment checks CR **existence/active-state** but not caller **entitlement**.
- **Mechanism (doc evidence):** `API_FleetCapacityReservationTargetRequest.md` accepts a raw CR-ID array in the request body; `cr-groups-add.md` states a CR must be "active" and "owned or shared with you" to be *grouped* — but the direct-ID path bypasses the group entirely, and no doc states the fleet re-checks entitlement on a directly-named CR ID. `cr-` IDs are structured 17-hex (enumerability candidate).
- **Confirm/Refute oracle:** From account B, name account A's un-shared `cr-…`. **Breach** = instances launch into A's reservation. **Refuted** = `UnauthorizedOperation`/`InvalidCapacityReservationId.NotFound` for the un-shared CR but success for a shared one. (Requires two-account canary; DryRun will NOT settle this — it's IAM-only, pre-resolution.)
- **Preconditions / Cost / Severity:** 2 accounts, one real CR each; a handful of instance-minutes. **Severity: Critical if true (cross-account capacity theft).**

**A2 — CR-ID enumeration oracle.**
- **Claim:** Error differentiation (NotFound vs AccessDenied vs AlreadyExists-in-use) across directly-named CR IDs forms an existence/ownership oracle over the 17-hex `cr-` space.
- **Oracle:** distinct error codes/latencies per class of CR ID = enumeration signal. **Severity: Medium** (enables A1 targeting; 17-hex is large but regional/account-correlated patterns worth checking).

**A3 — Group-member ownership masking (reach via group vs. direct).**
- **Claim:** A group that *silently* contains a shared-in (cross-account) CR means the fleet consumes foreign capacity while the fleet/LT config shows only a group ARN — a reviewer cannot see whose capacity is in scope.
- **Mechanism:** Subagent 2 §5 — fleet/LT reference **only** `CapacityReservationResourceGroupArn`; per-instance `CapacityReservationId` is visible only post-hoc via `DescribeInstances`. `cr-groups.md`: a group mixes owned + shared cross-account CRs.
- **Oracle:** This is a confirmed *masking* property (documented), not itself a breach; it is the **enabler** for A1/B2/B3 and a stated auditability gap. **Severity: High (contributes to cross-account blast-radius opacity).**

**A4 — Disclosure-timing on shared CR / group membership.**
- **Claim:** `ListGroupResources` / `DescribeCapacityReservations` on a group reveals member CR ARNs (which embed the owner account ID) before/without the owner intending that disclosure.
- **Mechanism:** Subagent 2 §5 — `resource-groups:ListGroupResources` has **zero condition keys**; EC2 ARNs embed owner account → structural info-disclosure side-channel (inferred from ARN shape, not documented). **Severity: Low–Medium** (account-ID disclosure); flag as *undocumented* side-channel to confirm live.

### Lens S — Condition-key scoping semantics — **CENTRAL FINDING**

**S1 — The entire `ReservedCapacityOptions` feature is IAM-unscopable.**
- **Claim:** No IAM condition key lets a defender restrict *which* CRs, CR types, groups, or fallback market types a principal may drive through `CreateFleet` — so a policy can only allow or deny `ec2:CreateFleet` wholesale.
- **Mechanism (doc evidence):** Subagent 1 audit of `list_ec2.md` CreateFleet rows (5113–5123): no key for CR ID, CR type, group ARN, reservation-type list, or fallback market type. `grep orgid list_ec2.md` → **0 hits** (Subagent 2 §6): no `aws:PrincipalOrgID`/`aws:ResourceOrgID` on any EC2 action. The interruptible condition keys that *do* exist (`ec2:IsInterruptible`, `ec2:InterruptibleCapacityReservationId`, lines ~10099/10104/10164) are bound **only to owner-side allocation actions** (lines 515–516, 4573–4574, 5180–5183, 9732–9735) and the capacity-reservation resource row (9924) — **they do NOT apply to the fleet consume path.**
- **Confirm/Refute oracle:** `iam:SimulateCustomPolicy` — attempt to author a policy that permits `CreateFleet` only for a specific CR type / group / CR-ID and show the simulator provides no lever (keys ignored). **Refuted** if any undocumented key is honoured. **Severity: High** (defensive-control gap; AWS-side — a shipped feature with no scoping surface).

**S2 — "Plausible-but-inert" interruptible keys (sharper Lens-U/S).**
- **Claim:** A defender who finds `ec2:IsInterruptible` / `ec2:InterruptibleCapacityReservationId` in the reference will reasonably believe they can gate interruptible-CR *consumption* by a fleet — but these keys only exist on the owner's allocation actions, so a policy attaching them to `CreateFleet` silently no-ops.
- **Oracle:** Simulate a `CreateFleet` policy with a `Condition` on `ec2:InterruptibleCapacityReservationId` → the condition is ignored (action doesn't support the key). **Severity: High** (false sense of control — the most review-defeating shape here).

### Lens U — Doc-guarantee vs. enforcement, incl. doc-vs-doc contradiction — **HIGH**

**U1 — THE CONTRADICTION: interruptible CRs "can't be added to groups" vs. four pages that group them.**
- **Claim:** `interruptible-capacity-reservations.md` ("Capacity consumers") states *"You can't add interruptible Capacity Reservations to capacity reservation groups,"* while `cr-groups.md`, `cr-groups-launch.md`, `cr-groups-lifecycle.md`, and this very walkthrough all give detailed, mutually-consistent instructions for doing exactly that (and the walkthrough's `cr-9876543210fedcba9` IS a grouped interruptible CR).
- **Online-vs-offline:** Subagent 2 fetched the live `.md` twins of all three source pages — **byte-identical** to the mirror. This is a **live doc defect, not sync lag.**
- **Oracle:** Live `GroupResources` with an interruptible CR + `CreateFleet` targeting it: either (a) grouping is silently rejected (prohibition is current, tutorial is wrong) or (b) it works (prohibition is stale). Either way the docs cannot be followed safely. **Severity: High** (AWS-authored contradiction — Tier-2 reportable doc defect; a reader cannot determine whether their config is supported). Flag for AWS clarification; do not assume either statement authoritative without live confirmation.

**U2 — "Mutually exclusive with `OnDemandOptions.CapacityReservationOptions`" — enforced?**
- **Claim:** Supplying both `ReservedCapacityOptions` and `OnDemandOptions.CapacityReservationOptions` in one `CreateFleet` is documented as not allowed, but `API_CreateFleet.md`'s Errors section names **no** mutual-exclusivity exception.
- **Oracle:** Live canary sending both — does the API reject, or silently honour one (and which)? A silent-honour is a config-confusion / policy-bypass seed. **Severity: Medium** (doc-gap; needs live canary).

**U3 — "Supported only for fleets of type `instant`" — enforced?**
- **Claim:** `ReservedCapacityOptions` on a `maintain`/`request` fleet is documented unsupported but default `Type` is `maintain`; is it rejected or ignored?
- **Oracle:** Canary `CreateFleet` with `ReservedCapacityOptions` and `Type:maintain` → reject vs silent-ignore. Silent-ignore on a maintain fleet would be a far more dangerous primitive (persistent self-healing fleet drawing on CRs). **Severity: Medium–High if silently honoured.**

**U4 — Fallback cannot be forbidden.**
- **Claim:** `ReservedCapacityFallbackOptions.MarketTypes=["on-demand"]` lets a fleet silently fall back to paid on-demand capacity when reservations are exhausted, and no IAM key can forbid it (ties to S1).
- **Oracle:** Simulate / canary — confirm no key gates fallback; confirm fallback launches bill the caller at on-demand rates. **Severity: Medium** (cost/DoS footgun; unscopable).

### Lens B — Confused deputy & cross-service dereference — **HIGH**

**B4-lead — EC2→resource-groups dereference entitlement check.**
- **Claim:** When EC2 fulfils a fleet by resolving a group ARN, it enumerates/consumes the group's member CRs with the service's resolution logic; if it does not re-evaluate the *caller's* entitlement to each member at consume time, a caller who can name a group ARN (even one containing CRs shared to the *group owner* but not to the caller) consumes capacity it couldn't name directly.
- **Mechanism:** `resource-groups:GroupResources`/`ListGroupResources` carry **zero condition keys** (Subagent 2 §6); group ARN is a cross-service pointer EC2 dereferences; no doc states a per-member caller-entitlement re-check at fleet fulfilment.
- **Oracle:** Account B names a group ARN (owned by/ shared from A) whose members include CRs not individually shared to B → do those members get consumed? **Breach** = yes. (Two/three-account canary; the group-sharing semantics via RAM must be set up.) **Severity: High–Critical if true (cross-account via indirection).**

**B-note — `aws:SourceArn`/`aws:SourceAccount` absent.** Because the instant fleet runs under the caller (no SLR deputy), the classic confused-deputy condition keys don't apply here; the deputy risk is instead the **cross-service group dereference** (B4) rather than a service-principal signing oracle. Record as the reason the standard confused-deputy keys are N/A (null, pages read: `list_ec2.md`, `ec2-fleet-prerequisites.md`).

### Lens AA — Share / revoke lifecycle & cross-account forced termination — **HIGH**

**AA1 — Interruptible reclaim = cross-account forced-termination with ≤2-min notice, no veto.**
- **Claim:** The CR **owner** (account A) can force-terminate the consumer (account B) fleet's running `p5.48xlarge` instances at will via `update-interruptible-capacity-reservation-allocation`, with only a 2-min EventBridge warning and no consumer override.
- **Mechanism:** Subagent 2 §3 — `capacity-owner-procedures.md` ("Reclaim capacity at any time"; 2-min warning); `capacity-consumer-procedures.md` ("interruption notice 2 minutes before termination"); CloudTrail `InterruptibleCapacityReservationInstancesTerminated`. No documented consumer veto/cooldown/rate-limit.
- **Oracle:** This is a *documented, by-design* primitive — the research question is whether a consumer fleet can be made to depend on interruptible capacity **without the operator realizing** (because the group ARN masks that `cr-9876…` is interruptible and foreign — ties to A3). **Severity: High (cross-account availability).** Document as design-risk + masking combo, not a "bug" by itself.

**AA2 — Org-leave auto-unshare termination has NO documented warning SLA.**
- **Claim:** When a consumer account leaves the Organization, its interruptible-CR instances are "eventually terminated" with no documented 2-min warning / EventBridge event — a looser, undocumented termination path than the standard reclaim.
- **Mechanism:** Subagent 2 §3 — `capacity-owner-procedures.md`: *"If a consumer account leaves your organization, the interruptible reservation is automatically unshared… Any instances running in the unshared reservation are eventually terminated."* Contrast with the explicit 2-min reclaim window.
- **Oracle:** Live: trigger org-leave, observe whether the 2-min interruption event fires or termination is abrupt. **Severity: Medium** (doc-gap / availability ambiguity).

**AA3 — Capacity-Block owner controls consumer instance lifetime.**
- **Claim:** For a *shared* standard Capacity Block in the group, the owner's extend/don't-extend decision unilaterally determines whether the consumer's fleet instances survive past the original expiry; FCFS "regardless of ownership."
- **Mechanism:** Subagent 2 §4 — `capacity-blocks-share.md` FCFS quote; owner-only extension; 40-min notice / 10-min-to-terminate EventBridge. (UltraServer blocks N/A — cannot be shared.)
- **Oracle:** Design-risk, documented. Research angle = combined with A3 masking: a fleet silently drawing on a foreign shared block inherits the owner's schedule. **Severity: High (cross-account availability).**

**AA4 — Shared-CR auto-removal race.**
- **Claim:** `cr-groups-add.md` — "If a shared Capacity Reservation is later unshared by its owner, EC2 automatically removes it from your group." Is there a TOCTOU window where a fleet targeting the group consumes a CR mid-unshare, or where removal does/doesn't terminate already-launched instances?
- **Oracle:** Live: unshare during fleet fulfilment; observe. **Severity: Medium** (race/lifecycle).

### Lens EE — Predictable-name / land-grab — **MEDIUM**

**EE1 — Capacity-Block FCFS occupy (cross-ref, see §7).**
- **Claim:** Being first to launch into a shared block occupies it regardless of ownership.
- **Owned by the capacity-blocks sibling plan** — do not re-derive here; this plan only notes it compounds with the multi-type group (a fleet can win the FCFS race *as a side effect* of targeting a mixed group it didn't realize contained a shared block). **Severity: see sibling.**

### Lens X — Action-family parity (`InstanceMarketType` asymmetry) — **MEDIUM**

**X1 — `InstanceMarketType` gate exists on `RunInstances` but not `CreateFleet`.**
- **Claim:** `list_ec2.md` shows `ec2:InstanceMarketType` as a supported condition key on `RunInstances` (row ~9591) but **not** on `CreateFleet` (row ~5118) — so a defender can constrain market type on direct launches but not on the fleet path that reaches the same capacity.
- **Mechanism:** Subagent 1 audit (asymmetry at those rows).
- **Oracle:** Simulate — confirm the key is honoured on `RunInstances` and ignored/absent on `CreateFleet`. **Severity: Medium** (parity/scoping gap enabling fallback-to-on-demand that couldn't be stopped at the fleet layer; ties S1/U4).

### Lens — arbitration / exhaustion (ordered `ReservationTypes`)

**ARB1 — Priority/exhaustion arbitration across CR types.**
- **Claim:** The ordered `ReservationTypes` list plus `AllocationStrategy:prioritized` plus `Priority` overrides creates a deterministic draw order; a caller can engineer which *owner's* capacity is consumed first (e.g. foreign interruptible before own ODCR, or vice-versa) by reordering — potentially draining a specific account's shared capacity preferentially.
- **Oracle:** Live: vary `ReservationTypes` order + overrides, observe which CR (ownership) is consumed first via post-hoc `DescribeInstances`. **Severity: Medium** (lets a consumer preferentially burn a chosen owner's reclaimable/paid capacity — compounds B2/AA).

---

## §5 — Priority ordering (where to spend the first day)

1. **S1 + S2 (unscopability + inert interruptible keys)** — pure `SimulateCustomPolicy`, no live launches, settles the central defensive-control claim fastest and safely. **Do this first.**
2. **A1 (direct foreign CR-ID targeting)** — the highest-severity *active* claim; needs the two-account canary but is the whole point of the feature's new request shape.
3. **B4 (group-ARN cross-service dereference entitlement)** — the cross-account escalation of A1 via indirection; needs 3-account/Org canary.
4. **U1 (the live doc contradiction)** — cheap live `GroupResources` + `CreateFleet`; resolves a Tier-2 doc defect.
5. **U2/U3 (mutual-exclusivity / instant-only enforcement)** — cheap single-account canaries; silent-honour findings are dangerous.
6. **AA1/AA3 + A3 masking combo**, then **ARB1**, then **X1/U4**, then **A2/A4/AA2/AA4** (enumeration/lifecycle edges).

---

## §6 — Canary / harness requirements

- **Three accounts** ideally, two minimum, in a test **AWS Organization** (interruptible + org-leave + group-sharing all need Org membership):
  - **Account A (owner):** creates ODCR, interruptible CR (via `create-interruptible-capacity-reservation-allocation`), and a standard Capacity Block; shares the interruptible CR to B via RAM; builds a CR group.
  - **Account B (consumer/attacker):** runs `CreateFleet` with `ReservedCapacityOptions`.
  - **Account C (out-of-org / un-shared):** source of a CR that is *never* shared to B — the clean negative for A1/B4.
- **Synthetic/canary data only**; smallest viable instance types where the feature permits (note: p5/p4d in the tutorial are expensive — use the smallest instance type that supports CRs for the canary, not the tutorial's p5.48xlarge, unless a type-specific behaviour is under test).
- **Tear down** every CR, group, RAM share, and fleet after each test.
- **Oracles:** `SimulateCustomPolicy` first; `DescribeInstances`/`DescribeFleetInstances` for post-hoc per-instance `CapacityReservationId`; CloudTrail (`InterruptibleCapacityReservationInstancesTerminated`, `CreateFleet`) and EventBridge interruption events for the lifecycle leads.
- **Hard stop** if any surfaced CR/instance/ARN belongs to AWS's own fleet rather than a test tenant.

---

## §7 — Cross-references (owned elsewhere — do NOT re-derive)

This capstone plan deliberately cross-references rather than restates:

- **`resource-groups` cross-service IAM-unscopability of CR-group targets, foreign-CR grouping, `ListGroupResources` unscopable oracle** → owned by **`ec2-fleet-targeted-capacity-reservations-walkthrough-attack-research-plan.md`**. This plan extends it only to the *mixed-type / direct-CR-ID* request shape.
- **Capacity-Block FCFS race-and-occupy, cross-account prepaid-block consumption, RAM-shared block mechanics** → owned by **`ec2-fleet-launch-instances-capacity-blocks-walkthrough-attack-research-plan.md`** (§5.2). This plan notes only the compounding effect of a block hidden inside a mixed group.
- **`instant`-fleet-under-caller-identity / SLR-not-required backbone** → established in the hub + targeted-CR sibling. This plan uses it (§2.3) but doesn't re-prove it.
- **LaunchTemplate late-binding / `CapacityReservationResourceGroupArn` inside `CapacityReservationSpecification`** → instance-weighting / targeted-CR siblings own the LT late-binding redirect angle.
- **No `aws:PrincipalOrgID` on EC2 (general fact)** → the fleet-tutorials hub owns the general statement; this plan confirms it specifically for the reserved-capacity path (S1/B5).

**What THIS plan uniquely owns:** (a) the net-new `ReservedCapacityOptions` structure + `DefaultTargetCapacityType:reserved-capacity` and its total IAM-unscopability (S1); (b) the "plausible-but-inert interruptible keys on the consume path" sharpening (S2); (c) the three-CR-type-in-one-group mix including a cross-ORG shared interruptible CR; (d) the ordered-`ReservationTypes` arbitration vector (ARB1); (e) `ReservedCapacityFallbackOptions` unscopable on-demand fallback (U4); (f) the `CapacityReservationTarget.CapacityReservationId.N` **direct-CR-ID request-body targeting vector** (A1); (g) the interruptible-reclaim + capacity-block-end **dual** cross-account forced-termination vectors mixed invisibly in one group (AA1/AA3 + A3 masking); (h) the live, confirmed-not-sync-lag **doc-vs-doc contradiction** on grouping interruptible CRs (U1); (i) the `InstanceMarketType` action-family-parity gap on `CreateFleet` vs `RunInstances` (X1).

---

## §8 — Null hypotheses (lenses checked, found not to fire — with pages read)

- **Lens F (translation-layer / wire-protocol / query injection):** N/A. Pages read: the walkthrough, `API_CreateFleet.md`, `API_ReservedCapacityOptionsRequest.md`, `API_FleetCapacityReservationTargetRequest.md`. Inputs are structured enums / ARNs / CR-IDs; no customer free-text transformed into a downstream query or wire protocol on this surface. (Injection risk, if any, lives in LT user-data — out of scope for this feature page.)
- **Lens G (SSRF / server-side dereference of a caller URL):** N/A. Pages read: walkthrough + all four API-ref types. No field is a URL/host the service fetches; the only dereferenced pointer is an ARN (`resource-groups` group), handled under Lens B4 as cross-service authz, not SSRF.
- **Lens Q (uploaded-blob parsing):** N/A — no blob/upload field on this surface (pages: walkthrough, API refs).
- **Lens D (data-plane → control-plane escape):** N/A for the fleet *request* surface — this is a control-plane API, not a running data path; no customer-reachable data interface introduced by this feature. (Launched instances' own escape surface is generic EC2, out of scope.)
- **Lens C (credential vending / session scope), Lens E (RBAC priv-esc within account):** no STS session-policy / role-vending construct and no built-in-role model introduced by this feature; the privilege question collapses to Lens S (there's just `ec2:CreateFleet`, unscopable). Pages read: `list_ec2.md` CreateFleet rows, `ec2-fleet-prerequisites.md`.
- **Lens B confused-deputy *signing-oracle* variant:** N/A because the instant fleet runs under the caller (no service-principal deputy / SLR); recorded under §4 Lens B-note. The surviving deputy risk is the cross-service group dereference (B4), which IS carried as an open lead.

---

*End of plan. Executable leads are in §4; start with §5's ordering. All cross-account claims require the §6 multi-account/Org canary and cannot be settled by `DryRunOperation`.*
