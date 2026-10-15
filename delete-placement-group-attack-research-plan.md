# Delete a Placement Group (`DeletePlacementGroup`) — Attack Research Plan (PAGE-LEVEL CHILD / TEARDOWN COMPLEMENT)

Source of leads: `AWSEC2/latest/UserGuide/delete-placement-group.html` (the target page; offline `delete-placement-group.md` == online byte-identical, verified 2026-10-15) + `API_DeletePlacementGroup.html` (fetched online 2026-10-15) + `change-instance-placement-group.md` (the "empty the PG" prerequisite) + the IAM Service Authorization Reference `list_ec2.md` (offline detailed table line 6100 **and** online `list_ec2.md`, both verified 2026-10-15). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

## Relationship to the HUB and sibling plans — READ FIRST
This is the **page-level teardown child** of `placement-groups-attack-research-plan.md` (the HUB) for the single `delete-placement-group` page + its `DeletePlacementGroup` API. It is the **teardown counterpart** of `create-placement-group-attack-research-plan.md` (the create child). It does **not** restate cross-cutting surface — it cross-references and **explicitly defers**:
- **Cross-account co-residency in a shared `cluster` PG + topology `nn-` side-channel (CROWN JEWEL / HARD STOP)** → **hub Area 1**.
- **Cross-account sharing *lifecycle* / org-leave orphan / unshare completeness / the RAM-revoke-vs-launch TOCTOU (T6)** → **hub Area 2**. (This child owns only the *delete-action*'s own empty-check TOCTOU, Area 2 below.)
- **`DescribePlacementGroups` unscopable read oracle + "can't view instances you don't own"** → **hub Area 3** (the Describe you use to *find* a PG to delete is unscopable; that is the hub's, not this page's).
- **Existence/scopability of `ec2:PlacementGroupStrategy`, `--parent-group-id` as a *create-time* primitive, tag-on-create ABAC self-widening, reserved `Operator`/`LinkedGroupId` params, stale `precision-time` enum** → **create child Areas 1/2/3/5**. This teardown child owns the *delete-side consequence* of two of those (the parent-link teardown-block, Area 1; the stale-enum + tag applied to a Deny-on-delete, Area 3) and defers their create-time depth.
- **`spread`/`partition` isolation = availability-not-security framing** → **hub Area 5**.
- **Predictable-name land-grab core** → **hub Area 6** (this child owns only the *delete→reclaim* window, Area 4, and defers).
- **`ModifyInstancePlacement` forced-downtime + shared-budget exhaustion** → **hub Area 7** (invoked here only as the mechanism to *empty* a PG before delete).

**Net-new surface this child OWNS** (not in the hub or the create child):
1. The **"cannot delete a parent of a cluster placement group"** teardown-ordering constraint as a **cross-team / cross-account denial-of-teardown + forced-persistence lever**, chained with the create child's unauthorized `--parent-group-id` parent-link (Area 1 — HEADLINE).
2. The **"must contain no instances"** precondition as an **IAM-unexpressible guarantee** (no `ec2:InstanceCount`-style key on `DeletePlacementGroup`) + the **add-instance-during-delete TOCTOU** race (Area 2).
3. **Settlement of the delete-scopability discrepancy** (delete **is** scopable — refutes any "delete is unscoped like Describe" prior) and the delete-side angles of tag/strategy scoping: **untag-to-unprotect** against a tag-gated delete-Deny, and the **stale `precision-time` enum applied to a Deny-on-delete** (Area 3).
4. **Delete is `GroupName`-only** (no `GroupId`, no reserved params) → **cross-account delete-by-id is refuted**; delete-authz on a *shared* PG is owner-scoped (Area 4, mostly deferred/negative).

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- `iam:SimulateCustomPolicy`/`SimulatePrincipalPolicy` is the safe first oracle for every condition-key claim (no resources touched). Escalate to a scoped live `delete-placement-group` call only with synthetic canary data under a role holding exactly the artifact under test. **Treat `DryRun` as caller-IAM-only, NOT an ownership/precondition oracle** — the API ref says `DryRun` returns `DryRunOperation`/`UnauthorizedOperation`, i.e. it is evaluated before the empty-check / parent-check resource resolution.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's own placement engine / service plane, or a *confirmed* cross-**account** physical co-residency (`nn-` node shared with a foreign account) surfaced while probing a shared PG's teardown — stop, preserve evidence, flag for AWS-Security disclosure, hand the confirmation to **hub Area 1**.

## 1. Pentest Objectives (delete-action-scoped)
1. **Lock a victim's placement group open:** create a `cluster` child PG that references a victim/other-team precision-time **parent** PG (create child Area 1), then prove the victim **cannot delete that parent** until the attacker-owned child — which the victim can neither see nor delete — is removed (denial-of-teardown / forced-persistence).
2. Delete a placement group that is **not actually empty**, or make a delete land such that a running instance is left referencing a deleted PG id (precondition-bypass / dangling membership via TOCTOU).
3. Prove an admin's intended **deletion-protection** policy is defeated — either because the holder can strip the gating tag (`UntagResource`), or because a `Deny DeletePlacementGroup where strategy≠X` is **inert against `precision-time`** (stale-enum fail-open), so a protected PG is deletable anyway.
4. Confirm/refute whether a **consumer of a shared PG** (RAM share or `PutResourcePolicy`) can `DeletePlacementGroup` on the owner's PG, or only the owner can.
5. Use the delete→free-name window to **reclaim a predictable PG name** before the owner recreates it (intra-account; cross-account refuted).

## 2. Components, Assets, and Design (delete path only)

**The delete action.** `DeletePlacementGroup` is a Region+Account-scoped mutating control-plane Write that destroys one `placement-group` resource. The API accepts **exactly one specific parameter — `GroupName` (Required: Yes)** — plus `DryRun`. **No `GroupId`, no `TagSpecification`, and (unlike `CreatePlacementGroup`) NO reserved/console-hidden parameters** (`LinkedGroupId`/`Operator` do not exist on delete). Because the resource is named by its **account-unique name** (create child confirmed names are unique per-account+Region), a `--group-name` delete can only ever target a PG **in the caller's own account** — there is no name-collision or id path to another account's PG.

**Two documented preconditions, both enforced server-side (no IAM grain):**
1. *"Before you can delete a placement group, it must contain no instances."* (UG + API ref: "You must terminate all instances in the placement group before you can delete the placement group.") Emptying is done via terminate, or `ModifyInstancePlacement`/`modify-instance-placement --group-name ""` to remove an instance (`change-instance-placement-group.md`), which itself requires the instance be **`stopped`**.
2. *"You can't delete a placement group that is a parent of a cluster placement group. Delete the cluster placement groups first."* — a **teardown-ordering / relationship constraint** that is the mirror image of the create child's `--parent-group-id` link.

**Authoritative IAM row** (`list_ec2.md` detailed table line 6100, offline **and** online, verified 2026-10-15):
`ec2:DeletePlacementGroup` → Resource type **`placement-group*`** (required) → Condition keys **exactly** `aws:ResourceTag/${TagKey}`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`, `ec2:ResourceTag/${TagKey}` → Access level **Write** → no dependent actions.
> **Discrepancy settled:** the *summary* action-list at `list_ec2.md` line 1154 renders `DeletePlacementGroup` with a **blank** condition-key/resource cell — this is a lossy rendering of the summary list, **not** authoritative. The detailed table (line 6100) and the online source both show the full scopable row above. **Delete IS scopable** by ARN, name, tag, and strategy — it is **not** a blank-resource unscoped action (that is `DescribePlacementGroups`: blank resource + `ec2:Region` only, List).

**What delete can and cannot be scoped by (vs the empty-check / parent-check):** delete can be gated by *which* PG (name/ARN/tag) and *which strategy*. It **cannot** be gated by "is it empty" or "is it a parent" — those are control-plane preconditions with **no condition key** (grep of `list_ec2.md` = 0 for `InstanceCount`/`ParentGroup`/parent-linkage keys on any PG action). So the two preconditions are prose+engine guarantees, un-IAM-authorable (Lens U).

```
  attacker acct A (create child Area 1)        victim acct/team B
  ┌───────────────────────────────┐            ┌──────────────────────────────┐
  │ CreatePlacementGroup           │            │ owns precision-time PARENT PG │
  │  --strategy cluster            │ parent ref │  pg-VICTIM (no authz on ref)  │
  │  --parent-group-id pg-VICTIM   │ ─────────▶ │                              │
  └───────────────────────────────┘            │ DeletePlacementGroup(pg-VICTIM)│
         child PG lives in A, invisible to B    │   → BLOCKED: "is a parent of  │
                                                │     a cluster PG" (child in A)│
                                                │   = cannot tear down own PG   │
                                                └──────────────────────────────┘
```

## 3. API / Interface Inventory

| Name | Method | Mutating | Resource type (req) | Condition keys | Callable by | Notes |
|---|---|---|---|---|---|---|
| `DeletePlacementGroup` | SDK + CLI `delete-placement-group` + PS `Remove-EC2PlacementGroup` | **Yes (Write, destructive)** | `placement-group*` | `aws:ResourceTag`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`, `ec2:ResourceTag` | any principal holding `ec2:DeletePlacementGroup` | **`GroupName` only** (Required:Yes); `DryRun` optional; no `GroupId`; no reserved params; no response beyond `return:true` |
| `ModifyInstancePlacement` (empty step) | CLI `modify-instance-placement --group-name ""` | Yes | `instance*` / `placement-group` / `dedicated-host` | PG row: `ec2:PlacementGroupName`/`Strategy` | holder on target instance | removes instance from PG; **instance must be `stopped`** — defer depth → hub Area 7 |
| `DescribePlacementGroups` (find step) | CLI `describe-placement-groups` | No (List) | **(blank)** | `ec2:Region` only | any holder | **unscopable** account-wide read oracle — defer → hub Area 3 |

Error surface (API ref `Errors` section lists only common errors): the **"not empty"** and **"parent of a cluster PG"** failures are **not** documented as named, individually-coded errors → the error *content* (does it name/enumerate the blocking child PG's id or the owning account?) is an **undocumented info-leak oracle** worth capturing (Area 1).

## 4. Trust-Boundary Map (delete-action rows; hub/create own the rest)

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Attacker (owns a child cluster PG) | Victim's parent PG lifecycle | "can't delete a parent of a cluster PG" + create child's unauthorized `--parent-group-id` | victim's `DeletePlacementGroup(parent)` fails citing a child the victim cannot see/delete → forced-persistence / denial-of-teardown |
| Caller racing a launch | The "must be empty" precondition | TOCTOU between engine empty-check and delete vs concurrent `RunInstances`/`ModifyInstancePlacement` | delete succeeds on a now-non-empty PG, or a running instance ends up referencing a deleted PG id |
| Holder of a tag/strategy-scoped delete grant | A PG a Deny meant to protect | `UntagResource` on the gating tag; stale `precision-time` enum | delete succeeds on a PG the admin's `Deny` intended to shield |
| Shared-PG consumer | Owner's shared PG | `DeletePlacementGroup --group-name` / resource-policy grant | consumer deletes/tears down the owner's PG (expected owner-only — confirm) |
| Caller | Freed PG name after delete | delete → name released → recreate | attacker reclaims the predictable name before owner recreates (intra-account) |

## 5. Recommended Areas of Focus

### Area 1 — "Cannot delete a parent of a cluster PG": cross-team/cross-account denial-of-teardown + forced-persistence (HEADLINE; chains create child Area 1)

**Background.** The page and API ref both state: *"You can't delete a placement group that is a parent of a cluster placement group. Delete the cluster placement groups first."* The **create child Area 1** established (as an open, un-refuted doc-gap) that `CreatePlacementGroup --strategy cluster --parent-group-id pg-xxxx` references a parent PG with **no IAM authorization checked against that parent** (`CreatePlacementGroup` exposes a single resource-type row = the created child; no `ParentGroupId` condition key exists anywhere). Composing the two: if the create-time parent reference can point at a parent the caller does not own, then an attacker's child cluster PG becomes a **lifecycle lock** on the victim's parent — the victim's own `DeletePlacementGroup(parent)` is blocked by a child that lives in the **attacker's** scope and is therefore invisible to and un-deletable by the victim.

**Security concern.** (a) **Denial-of-teardown / forced-persistence (Lens A relationship-isolation + Lens AA teardown-completeness):** can an attacker (or a buggy other team) indefinitely prevent a victim from deleting a precision-time parent PG by keeping a child cluster PG linked to it? This also *pins* the victim's precision-time hardware allocation open (the parent keeps influencing placement), which is the co-residency-precursor state the create child + hub Area 1 care about — teardown-block = persistence of the co-residency primitive. (b) **Info-leak oracle (Lens A error-differential):** does the delete failure message enumerate the blocking child PG — its `pg-` id, strategy, or owning account? If so, the victim's failed delete becomes a cross-account existence/identity oracle for the attacker's child. (c) **Does the block even cross accounts?** This hinges on the create child's open Q1 — whether `--parent-group-id` accepts a *foreign/shared* parent at all. If parent-linkage is intra-account-only, the lever degrades to **cross-team within one account** (still a real griefing/persistence primitive); if it spans a RAM/resource-policy-shared precision-time parent, it is cross-account.

**High-level test scenarios.**
- Two scopes (teams or accounts): scope A creates a `cluster` PG with `--parent-group-id` = scope B's precision-time parent (per create child Area 1). Then as B, attempt `delete-placement-group --group-name <parent>`; confirm it is **blocked**, and capture the **exact error text** — does it reveal A's child id/account? (`DryRun` will NOT reveal this — needs the real call; it fails at the precondition, not IAM.)
- Determine whether B has **any** path to clear the block without A's cooperation (force-delete flag? support? none documented → that is the finding).
- Chain to **hub Area 1 / create child Area 1**: while the parent is pinned open, launch into the parent's precision-time pool and inspect `DescribeInstanceTopology` `nn-` nodes — **HARD STOP** on a foreign-account `nn-` hit.

**Doc evidence.** `delete-placement-group.md` / `API_DeletePlacementGroup.html` "cannot delete a parent of a cluster placement group"; create child Area 1 (`--parent-group-id`, no authz on parent, no condition key); `list_ec2.md` DeletePlacementGroup row (no parent/linkage condition key to express or override the block).

**Severity.** Cross-account denial-of-teardown / forced-persistence = **High if the parent-link crosses accounts**; cross-team intra-account = **Medium**. Error-enumeration info-leak = Low–Medium (enabler). **Precondition cap:** depends on create child Q1 (can `--parent-group-id` reference a non-owned parent); if parent-linkage is strictly owner-validated, this whole area collapses to a self-inflicted ordering nuisance (document as refuted).

### Area 2 — "Must contain no instances" is an IAM-unexpressible guarantee + add-instance TOCTOU

**Background.** Delete requires the PG be empty; the only documented way to satisfy it is terminate / move / remove instances (`change-instance-placement-group.md`: `modify-instance-placement --group-name ""`, instance must be `stopped`). `DeletePlacementGroup`'s condition keys are **only** `ResourceTag`/`PlacementGroupName`/`PlacementGroupStrategy`/`Region` — there is **no `ec2:InstanceCount`** (or any membership) condition key on the action (grep `list_ec2.md` = 0). So "it must be empty" is a **pure control-plane precondition**, not something an admin can author, attest, or tighten in IAM (Lens U: documented guarantee with no customer-authorable enforcement mechanism).

**Security concern.** (a) **TOCTOU / precondition race (Lens P gate-skip + Lens AA):** between the engine's empty-check and the actual destroy, can a concurrent `RunInstances` (launch into the PG) or `ModifyInstancePlacement` (add a stopped instance → start) land, so that either (i) the delete destroys a PG that just became non-empty, or (ii) a freshly-launched/started instance ends up a member of a PG that no longer exists (dangling PG membership / orphaned placement reference)? (b) **Consistency of the empty-check across populate paths:** the hub notes multiple ways a PG gets populated — `RunInstances`, `ModifyInstancePlacement`, `AttachResourcesToPlacementGroup`, Spot/Fleet launches, Capacity Reservations in a cluster PG (`cr-cpg.md`). Does the empty-check count **all** of these — e.g. does an **empty-but-CR-backed** cluster PG (a Capacity Reservation reserving capacity but zero running instances) count as "empty" and delete out from under the reservation, stranding or silently releasing reserved capacity? (c) This is largely **intra-account self-consistency**; it rises to **cross-account** only inside a *consented share* where a consumer's in-flight launch races the owner's delete — that specific RAM-revoke/launch TOCTOU is **hub Area 2 T6**; here own the *delete-action's own* empty-check race and the CR-backed-but-empty question.

**High-level test scenarios.**
- Fire `delete-placement-group` concurrently with a `RunInstances --placement-group-name <same>` (and separately with a `modify-instance-placement` add). Repeat under contention; inspect for a surviving instance whose `DescribeInstances` placement references a PG that `DescribePlacementGroups` says is gone.
- Create a cluster PG, place a **Capacity Reservation** in it (`cr-cpg.md`) with zero running instances; attempt delete — does it treat CR-reserved-but-instance-empty as deletable, and what happens to the CR? (Lens AA cascade/stranding.)
- Confirm via `iam:SimulateCustomPolicy` that **no** condition key lets an admin express "only delete empty PGs" or "deny delete if InstanceCount>0" (structural inexpressibility = the finding).

**Doc evidence.** `delete-placement-group.md` + `API_DeletePlacementGroup.html` "must terminate all instances"; `change-instance-placement-group.md` empty-string removal + `stopped` requirement; `cr-cpg.md` CR-in-cluster-PG; `list_ec2.md` DeletePlacementGroup 5-key row (no membership key).

**Severity.** TOCTOU dangling-membership = **Medium** (intra-account consistency; High only if it crosses a consented-share account boundary → hand to hub Area 2). CR-backed-empty strand/silent-release = **Medium** if confirmed. IAM-inexpressibility = Low (structural, AWS-owned, reportable Lens U).

### Area 3 — Delete IS scopable: delete-side tag/strategy scoping — untag-to-unprotect + stale `precision-time` enum on a Deny

**Background.** Settled fact (online+offline 2026-10-15): `DeletePlacementGroup` is scopable by `placement-group*` ARN, `ec2:PlacementGroupName`, `ec2:ResourceTag`, and `ec2:PlacementGroupStrategy`. So an admin **can** author deletion-protection — e.g. `Deny DeletePlacementGroup where ec2:ResourceTag/protected = true`, or `Deny DeletePlacementGroup where ec2:PlacementGroupStrategy = precision-time`. Two delete-side bypass shapes, both inheriting mechanisms the create child owns but applying them to the **destroy** operation:

**Security concern.** (a) **Untag-to-unprotect (Lens I/S):** a tag-gated delete-Deny is only as strong as the tag's immutability. If the same principal (or a collaborator) holds `ec2:DeleteTags`/`UntagResource` on the PG with no condition pinning the `protected` key, they can **strip the tag, then delete** — defeating the protection. Combined with the **create child Area 5** finding that a `CreatePlacementGroup` holder can *self-set* arbitrary tags at create, the full lifecycle is: create untagged (or create tagged then untag) → never subject to the tag-gated delete-Deny. (b) **Stale `precision-time` enum fail-open (Lens S "silently-ignored enum" variant; create child Area 3):** the `ec2:PlacementGroupStrategy` key *definition* reads "(cluster, spread, or partition)" — **omitting `precision-time`**. If the key does not populate for a precision-time PG, then a `Deny DeletePlacementGroup where StringNotEquals strategy = cluster` is **inert against precision-time** → the precision-time PG (exactly the one tied to Area 1's co-residency pool) is **deletable despite the Deny**, and conversely a `Deny strategy = precision-time`-to-protect never matches. (c) **No `aws:RequestTag` on delete** (there is no tag-on-delete) — so request-tag conditions are inapplicable; only `ResourceTag`/name/strategy gate delete (confirms the scoping grain, nothing to self-set at delete time).

**High-level test scenarios.**
- `iam:SimulateCustomPolicy` first: under a `Deny DeletePlacementGroup if ResourceTag/protected=true`, simulate delete on a protected PG (expect Deny), then simulate after an `UntagResource` (expect Allow) — prove the protection is only as strong as tag-mutability. Confirm whether a `Condition` can pin the tag against untag (it cannot gate `DeleteTags` by the *value being removed* cleanly — note the structural gap).
- `iam:SimulateCustomPolicy` with `ec2:PlacementGroupStrategy` context = `precision-time` against a `StringNotEquals cluster` Deny on `DeletePlacementGroup`: does the key resolve (match → protected) or come back absent (no match → fail-open, deletable)? Mirror the create child Area 3 test on the delete action.
- Live scoped delete under a strategy-scoped role on a `precision-time` PG with canary data.

**Doc evidence.** `list_ec2.md` DeletePlacementGroup row (ResourceTag + PlacementGroupName + PlacementGroupStrategy scopable) line 6100; key-definition text omitting `precision-time` (create child §2, `list_ec2.md` key defs); create child Area 3/Area 5 (stale enum + tag self-widen, deferred-to for create-side depth).

**Severity.** Untag-to-unprotect = **Medium** (defeats an AWS-recommendable protection pattern; customer-authored-ABAC footgun unless an AWS sample policy ships this gate without pinning untag — none found). Stale-enum fail-open on delete = **Low–Medium**, AWS-owned (reportable Lens S/U doc-vs-enforcement defect — a strategy a Deny cannot express).

### Area 4 — `GroupName`-only delete: cross-account delete-by-id refuted; shared-PG delete authz; delete→name-reclaim window

**Background.** `DeletePlacementGroup` accepts **only `GroupName`** (API ref, Required:Yes), **not** a `GroupId`. PG names are **unique per-account+Region** (create child confirmed). Therefore a delete is intrinsically scoped to the caller's own account's namespace — there is **no name-collision or id path** to reach another account's PG by delete.

**Security concern.** (a) **Cross-account delete-by-id — REFUTED:** unlike launching into a *shared* PG (hub notes that uses the PG **id**), delete offers no id parameter, so a consumer cannot `delete-placement-group` another account's PG by naming its id. Clean negative. (b) **Shared-PG delete authz (defer → hub Area 2):** can a RAM-share or a native `ec2:PutResourcePolicy` resource-based policy on a `placement-group` (hub §3 notes PG carries `PutResourcePolicy`/`GetResourcePolicy`/`DeleteResourcePolicy`) ever grant `ec2:DeletePlacementGroup` to a **consumer**, letting them tear down the owner's PG? Expected owner-only (share grants launch/use, not destroy) — **confirm** whether the resource-policy action set can include delete; if yes, that is a cross-account teardown path (High). (c) **Delete→reclaim window (Lens EE, defer core → hub Area 6):** on successful delete the name is released; an intra-account actor who can `CreatePlacementGroup` and who observes the deletion (via the unscopable `DescribePlacementGroups`, hub Area 3) can **immediately recreate the freed name** with attacker-chosen strategy/tags before the legitimate owner recreates it — a name-rebind/squat race. Cross-account reclaim is **refuted** (names per-account). Thin; depth → hub Area 6.

**High-level test scenarios.**
- Confirm (docs/API) there is no `GroupId` delete path (done — refuted). File the clean negative.
- Inspect whether a `placement-group` resource-based policy (`PutResourcePolicy`) can enumerate `ec2:DeletePlacementGroup` as a shareable action to a foreign principal → `iam:SimulateCustomPolicy` / read `API_PutResourcePolicy` constraints; if delete is shareable, escalate to hub Area 2 as a cross-account teardown lead.
- Intra-account: delete a PG, then race a `CreatePlacementGroup` of the same name from a second principal; measure whether an attacker can win the reclaim and rebind strategy/tags.

**Doc evidence.** `API_DeletePlacementGroup.html` `GroupName`-only; create child C9 (names unique per-account → cross-account squat refuted); hub §3 (`PutResourcePolicy` on `placement-group`), hub Areas 2/6.

**Severity.** Cross-account delete-by-id = **NULL/refuted**. Shared-PG delete-grant = **High if resource-policy can grant delete** (else refuted; → hub Area 2). Delete→reclaim intra-account = **Low–Medium** (→ hub Area 6).

### Area 5 — Irreversibility + console confirm-gate (framing / informational)

**Background.** Delete is **permanent** — no documented soft-delete, recovery window, or undo; the console requires typing **"Delete"** to confirm (`delete-placement-group.md` console step 4), and the API returns only `return:true`.

**Security concern.** The confirm-gate is a **UI anti-footgun, not an API security control** — a programmatic `delete-placement-group` has no equivalent typed confirmation, so any automation/role holding the action deletes without friction. Irreversibility makes the Area 1 (persistence) and Area 2 (TOCTOU)/Area 3 (protection-bypass) levers **one-shot destructive**: there is no rollback once a PG is destroyed, and recreating the same-named PG does **not** restore the original `groupId` (opaque `pg-…` id changes), breaking any id-based references/automation that pinned the old id. No CloudTrail-evasion specifics are documented; delete is a normal mutating management event (Lens O: ordinary, logged).

**High-level test scenarios.** None cross-tenant. Note for the hunter: do **not** rely on the console confirm as a control when modelling blast radius; confirm the recreated-PG `groupId` differs (id-reference breakage) if any downstream automation pins ids.

**Doc evidence.** `delete-placement-group.md` console confirm step; `API_DeletePlacementGroup.html` single boolean response; create child (groupId = `pg-`+17hex, regenerated on recreate).

**Severity.** Informational (framing — prevents over/under-rating; amplifies Areas 1–3 by removing rollback).

## 6. Threat Model Test Objectives
| # | Threat / Test Case | Area | Component | Documented mitigation to attack | Status |
|---|---|---|---|---|---|
| D1 | Attacker child cluster PG blocks victim's delete of a (precision-time) parent → forced-persistence | 1 | "can't delete a parent of a cluster PG" + unauthorized `--parent-group-id` | parent-link ownership (create child Q1: unstated) | **doc-gap — HEADLINE; HARD STOP if co-residency confirmed → hub A1** |
| D2 | Delete-failure error enumerates the blocking foreign child PG id/account | 1 | API error content | Errors section lists only common errors | doc-gap — info-leak oracle |
| D3 | TOCTOU: delete lands on a now-non-empty PG, or instance left referencing deleted PG | 2 | empty-check vs concurrent `RunInstances`/`ModifyInstancePlacement` | "must contain no instances" (engine-only, no IAM key) | doc-gap |
| D4 | CR-backed but instance-empty cluster PG deletes, stranding/releasing the reservation | 2 | `cr-cpg.md` CR-in-PG + delete | empty = no instances (CR status unstated) | doc-gap |
| D5 | Admin cannot author "only delete empty PGs" | 2 | DeletePlacementGroup keys | — (inexpressible, no InstanceCount key) | structural gap (Lens U) |
| D6 | Untag the gating tag, then delete a tag-protected PG | 3 | `UntagResource` + tag-gated delete-Deny | `ec2:ResourceTag` delete scoping | footgun — SimulateCustomPolicy |
| D7 | `Deny delete where strategy≠cluster` inert against `precision-time` (fail-open) | 3 | stale `ec2:PlacementGroupStrategy` enum | key filters strategy on the action | enum stale (doc defect) — SimulateCustomPolicy |
| D8 | Cross-account delete another account's PG by id | 4 | `DeletePlacementGroup` params | **`GroupName`-only, no `GroupId`; names unique per-account** | **refuted** |
| D9 | Shared-PG consumer deletes owner's PG via resource-policy grant | 4 | `PutResourcePolicy` on `placement-group` | expected owner-only (confirm) | doc-gap → hub A2 |
| D10 | Reclaim freed PG name after owner's delete (intra-account) | 4 | delete→recreate race | names per-account; opaque id regenerated | Low–Med → hub A6 |
| D11 | Console confirm-gate relied on as a control; recreated PG id differs | 5 | console vs API; `groupId` | typed "Delete" confirm (UI only) | informational |

## 7. Out-of-Scope Risk Categories
- The **co-residency confirmation** step (topology `nn-`) and the **cross-account sharing lifecycle / RAM-revoke-vs-launch TOCTOU** — **hub Areas 1/2**; this page only supplies the teardown-block persistence lever (Area 1) and the delete-action's own empty-check race (Area 2), and HARD-STOPs on a foreign `nn-` hit.
- The **unscopable `DescribePlacementGroups`** read oracle used to find a PG to delete — **hub Area 3**.
- `--parent-group-id` **create-time** mechanics, reserved `Operator`/`LinkedGroupId`, tag-on-create self-widening, stale-enum **at create** — **create child Areas 1/2/3/5** (this page owns only the delete-side consequences).
- `spread`/`partition` "isolation defeated" within one's own account = availability/self-DoS, not a security boundary — **hub Area 5**.
- Single-tenant self-DoS by deleting one's own PGs; exhausting/emptying one's own fleet to satisfy the precondition.
- The EC2 placement engine's internal host-selection and the empty-check/parent-check logic itself (service plane) — observe/confirm only, never exploit; HARD STOP on service-plane evidence.
- Customer-authored over-broad IAM (footgun). AWS-authored/managed-policy weak defaults remain in scope (Lens R/S) — **but this page prints no policy JSON**, so Lens R cannot run here (same gap as hub §R-gap / create child §8).

## 8. Null hypotheses / doc gaps

**Lenses fired:** A (relationship/sibling-isolation of parent-child teardown + error-differential info-leak — Area 1), AA (teardown-completeness / stranded-reservation / forced-persistence — Areas 1/2), U (documented-guarantee-vs-IAM-enforcement: empty-check & parent-check un-authorable, stale enum — Areas 2/3), S/I (condition-key scoping: delete scopable, untag-to-unprotect, silently-ignored `precision-time` enum — Area 3), P (precondition-gate skip / TOCTOU — Area 2), EE (delete→name-reclaim window — Area 4, deferred), O (confirm-gate / logging — Area 5).

**Explicit NULL hypotheses (pages checked per skill discipline):**
- **Lens G (SSRF):** N/A — `DeletePlacementGroup` takes a single `GroupName` string the service resolves internally; no URL/URI/endpoint/webhook/callback field it dereferences. Pages: `delete-placement-group.md`, `API_DeletePlacementGroup.html`.
- **Lens Q (upload/blob):** N/A — no file/image/attachment field.
- **Lens F (translation/injection):** N/A — no parser/translation layer; `GroupName` is an account-unique string looked up, not interpreted. (Name canonicalization for a name-only IAM *condition* is a create/launch concern → hub Area 6, not delete.)
- **Lens B/C (PassRole / credential-vending):** N/A — delete takes no role-ARN input; no STS/session-policy/ProvidedContext seam. (Delete has **no** reserved `Operator`/`LinkedGroupId` params — unlike create — so even the create child's Area 2 attribution question does not arise here.) Pages: `API_DeletePlacementGroup.html`, `list_ec2.md` DeletePlacementGroup row.
- **Lens D (data→control-plane), W (attestation/enclave), FF (JWT), J (OAuth), M (session), Y (transport), BB/CC/DD (parser/edge/cache), K (prompt-injection), H (KMS):** N/A — a single SigV4-authenticated control-plane destroy call; no data-plane process, enclave, bearer token, OAuth, session id, edge/cache, LLM, or KMS key in the delete path. Pages: `delete-placement-group.md`, `API_DeletePlacementGroup.html`, `list_ec2.md` (PG rows).
- **Lens N (namespace migration):** N/A — no dual/legacy ARN namespace for placement groups.
- **Lens V (network segmentation):** N/A at the delete API layer — relevant only to the placement engine's host-selection (service plane, OOS/HARD-STOP) → hub Area 1.
- **Lens R (AWS IAM-artifact audit):** **could not run** — the delete page prints no managed/sample policy JSON (only CLI/PowerShell one-liners). Same gap as hub §R-gap and create child §8.

**Confirmed facts established by this child (reusable):**
1. `DeletePlacementGroup` IAM row (online+offline 2026-10-15, `list_ec2.md` detailed table line 6100) = Resource `placement-group*` (required); Condition keys **exactly** `aws:ResourceTag/${TagKey}`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`; Access **Write**; no dependent actions. **Delete IS scopable** by ARN/name/tag/strategy — **not** blank-resource like `DescribePlacementGroups`.
2. The `list_ec2.md` *summary* list (line 1154) renders delete with a blank cell — **lossy, not authoritative**; use the detailed table (6100). (Discrepancy with the hub §3 table **resolved in favour of scopable**.)
3. `DeletePlacementGroup` accepts **only `GroupName` (Required:Yes)** + `DryRun`; **no `GroupId`, no `TagSpecification`, no reserved/console-hidden params** (contrast create's `LinkedGroupId`/`Operator`). → **cross-account delete-by-id refuted**.
4. The two preconditions ("must be empty"; "can't delete a parent of a cluster PG") have **no condition key** on the action — un-IAM-authorable, pure control-plane (grep `list_ec2.md` = 0 for InstanceCount/parent-linkage keys).
5. The API `Errors` section documents **only common errors** — the not-empty / parent-of-cluster failures are not individually coded; their message *content* is an undocumented potential info-leak (Area 1 D2).

**Top open doc-gaps carried for the hunter (priority order):**
1. **(Area 1, HEADLINE)** Does an attacker-owned child cluster PG referencing a victim's parent (create child Q1) **block the victim's `DeletePlacementGroup(parent)`**, and does the error enumerate the foreign child? (Needs the create child's parent-link cross-scope question answered first; a 2-scope live test.)
2. **(Area 2)** Empty-check TOCTOU — can a concurrent launch/add leave a running instance referencing a deleted PG id? Does a CR-backed-but-instance-empty cluster PG delete and strand the reservation?
3. **(Area 3)** On the **delete** action, does `ec2:PlacementGroupStrategy` populate with `precision-time` (so a strategy Deny works) or is it inert (fail-open)? And can a tag-gated delete-Deny be defeated by `UntagResource`? (`iam:SimulateCustomPolicy`.)
4. **(Area 4)** Can a `placement-group` resource-based policy (`PutResourcePolicy`) grant `ec2:DeletePlacementGroup` to a foreign consumer (cross-account teardown)? → hub Area 2.

**Confirmed negative results (do not re-chase):** cross-account **delete-by-id** — refuted (`GroupName`-only, names unique per-account). No reserved/hidden parameters on delete (contrast create). `DeletePlacementGroup` is **scopable** (refutes any "delete is unscoped like Describe" prior). Delete has **no** `aws:RequestTag` (no tag-on-delete). Offline `delete-placement-group.md` == online byte-identical; `API_DeletePlacementGroup.html` and `list_ec2.md` (both renderings) verified 2026-10-15.
