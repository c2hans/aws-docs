# Create a Placement Group (`CreatePlacementGroup`) — Attack Research Plan (PAGE-LEVEL CHILD)

Source of leads: `AWSEC2/latest/UserGuide/create-placement-group.html` (the target page; offline `create-placement-group.md` == online byte-identical, verified 2026-10-15) + the authoritative API reference `AWSEC2/latest/APIReference/API_CreatePlacementGroup.html` (fetched online 2026-10-15) + the IAM Service Authorization Reference `list_ec2.md` (offline, targeted grep). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

## Relationship to the HUB plan — READ FIRST
This is the **page-level deep-dive child** of `placement-groups-attack-research-plan.md` (the HUB) for the single `create-placement-group` page + its `CreatePlacementGroup` API. It does **not** restate the hub's cross-cutting surface — it cross-references and **explicitly defers**:
- **Cross-account co-residency in a shared `cluster` PG + topology `nn-` side-channel (CROWN JEWEL / HARD STOP)** → **hub Area 1**. This child's Area 1 (parent-group-id) is a *create-time influence/precursor* that *feeds* that chain; it does not re-own the confirmation step.
- **Cross-account sharing lifecycle / org-leave orphan / unshare completeness** → **hub Area 2**.
- **`DescribePlacementGroups` unscopable read oracle + "can't view instances you don't own"** → **hub Area 3**.
- **The *existence* of `ec2:PlacementGroupStrategy` as a scopable key, and the fact that it's flagged on `--parent-group-id`** → **hub Area 4** (this child owns the *create-action-specific depth* of both).
- **`spread`/`partition` "physical isolation" is availability-not-security framing correction** → **hub Area 5**.
- **Predictable-name land-grab + name-only-condition footgun depth** → **hub Area 6** (this child owns only the *create-time* mechanics + the now-settled uniqueness fact).
- **`ModifyInstancePlacement` forced-downtime + shared-budget exhaustion depth** → **hub Area 7**.
- **Outpost placement groups (NULL/OOS, single-tenant)** → **hub Area 8** (this child adds the `SpreadLevel=host`→Outpost linkage only).

**Net-new surface this child OWNS** (none of it is in the hub, because the hub was built from the 6 UG pages + `list_ec2`/`list_ram`/`list_outposts` and never read `API_CreatePlacementGroup.html`): the four create-time request parameters the UG page under-documents (`ParentGroupId`, `PartitionCount`, `SpreadLevel`) **plus two reserved/console-hidden parameters the UG never mentions at all** (`LinkedGroupId` = "Reserved for future use", `Operator` = "Reserved for internal use"), the create-action's exact IAM condition-key coverage vs those parameters, the `precision-time` stale-enum fail-open *at create*, tag-on-create ABAC self-widening, and the create-time name/quota mechanics.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- `iam:SimulateCustomPolicy`/`SimulatePrincipalPolicy` is the safe first oracle for every condition-key claim (no resources touched). Escalate to a scoped live `create-placement-group` call only with synthetic canary data under a role holding exactly the artifact under test. **Treat `DryRun` as caller-IAM-only, NOT an ownership/parent-validation oracle** — it is evaluated before resource resolution (the API ref says `DryRun` returns `DryRunOperation`/`UnauthorizedOperation`, nothing about parent existence).
- **HARD STOP:** the moment create-time influence (a `--parent-group-id` or `cluster` PG) is shown to produce *confirmed cross-account physical adjacency* (a `nn-` topology node shared with a foreign account) — stop, preserve evidence, flag for AWS-Security disclosure, and hand the confirmation step to **hub Area 1**. Also HARD STOP on any identity/credential/ARN/account belonging to AWS's own placement engine / service plane.

## 1. Pentest Objectives (create-action-scoped)
1. Create a `cluster` placement group whose `--parent-group-id` references a **precision-time parent PG owned by another team/account**, with no IAM authorization checked against that parent — a create-time cross-resource reference (land-grab / co-residency precursor).
2. Determine what the **reserved/internal** parameters `LinkedGroupId` ("Reserved for future use") and `Operator` ("Reserved for internal use") actually do when supplied to the control-plane API, and whether either sets an ownership/management attribute that no `CreatePlacementGroup` condition key can scope.
3. Prove an admin **cannot** author an IAM policy that constrains the `precision-time` strategy at create (stale `ec2:PlacementGroupStrategy` enum fail-open), the partition count, the spread level, or that mandates a required tag.
4. Use tag-on-create (`aws:RequestTag`) to **self-set the very tag** that `DeletePlacementGroup`/`ModifyInstancePlacement`/launch ABAC later keys on — a create-time self-widening / deletion-protection / policy-evasion primitive.
5. Exhaust the 500-PG/Region ceiling by create, or squat a predictable name intra-account (uniqueness is per-account+Region → cross-account squat is refuted; see Area 5).

## 2. Components, Assets, and Design (create path only)

**The create action.** `CreatePlacementGroup` creates a Region+Account-scoped `placement-group` resource. ARN = `arn:${Partition}:ec2:${Region}:${Account}:placement-group/${PlacementGroupName}`; the response also returns an opaque `groupId` of the form `pg-0bea00ad0bexample` (`pg-` + 17 hex, confirmed in the API-ref sample responses). Both the ARN and the `ec2:PlacementGroupName` condition key key off the **operator-chosen name**, not the opaque id.

**The full accepted request-parameter set (API reference, verbatim 2026-10-15):**

| Parameter | Required | Type | Doc text / constraints | Surfaced in UG/CLI page? | IAM condition key? |
|---|---|---|---|---|---|
| `DryRun` | No | Boolean | permission precheck only | — | n/a |
| `GroupName` | **No** | String | "Must be unique within the scope of your account for the Region." Up to **255 ASCII** chars | yes | `ec2:PlacementGroupName` |
| `LinkedGroupId` | No | String | **"Reserved for future use."** | **NO — undocumented** | **none** |
| `Operator` | No | `OperatorRequest` object | **"Reserved for internal use."** | **NO — undocumented** | **none** (`ec2:ManagedResourceOperator` is NOT on CreatePlacementGroup) |
| `ParentGroupId` | No | String | "The ID of a parent placement group. Valid only when **Strategy** is `cluster`." (no ownership statement) | partially (CLI `--parent-group-id`, cluster example) | **none** |
| `PartitionCount` | No | Integer | "The number of partitions. Valid only when **Strategy** is `partition`." (no range stated) | yes (`--partition-count 5`) | **none** |
| `SpreadLevel` | No | String | `host \| rack`; **"Host — you can use `host` only with Outpost placement groups"**; Rack — no restrictions | console only (Host/Rack) | **none** |
| `Strategy` | **No** | String | Valid Values: **`cluster \| spread \| partition \| precision-time`** | yes | `ec2:PlacementGroupStrategy` (enum doc **omits** precision-time) |
| `TagSpecification.N` | No | Array | tags to apply to the new PG | yes | `aws:RequestTag`, `aws:TagKeys` |

**Authoritative IAM row** (`list_ec2.md` line 5370): `ec2:CreatePlacementGroup` → Resource type `placement-group*` (required) → Condition keys **exactly** `aws:RequestTag/${TagKey}`, `aws:TagKeys`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`. The dependent tagging action `ec2:CreateTags` is listed alongside (line 642). **Grep of the whole `list_ec2.md` for `ParentGroup`/`PartitionCount`/`PartitionNumber`/`SpreadLevel` = ZERO hits** — those three (plus `LinkedGroupId`, plus `Operator`→`ec2:ManagedResourceOperator`) have **no condition key anywhere on the create action**.

**Key definition texts (verbatim, `list_ec2.md` lines 10131-10133):**
- `ec2:PlacementGroup` — "Filters access by the ARN of the placement group" — **ARN**
- `ec2:PlacementGroupName` — "Filters access by the name of a placement group" — **String**
- `ec2:PlacementGroupStrategy` — "Filters access by the instance placement strategy used by the placement group **(cluster, spread, or partition)**" — **String** ← enum omits `precision-time`.

**Enforcement reality.** `CreatePlacementGroup` exposes a **single resource-type row** (the PG being created). Every *reference* the request makes to another resource — the `ParentGroupId` parent PG, whatever `LinkedGroupId`/`Operator` point at — is therefore **authz-invisible on the create action**: IAM evaluates the created-PG only, never the referenced parent. Co-location/isolation behaviour itself is decided by the EC2 placement engine (service plane), un-IAM-auditable.

```
  caller (CreatePlacementGroup)                      EC2 control plane / placement engine
  ┌──────────────────────────┐                       ┌───────────────────────────────────┐
  │ IAM eval scopes ONLY the  │  --parent-group-id    │ links new cluster PG to a parent  │
  │ created PG (name/strategy │ ────pg-xxxx──────────▶ │ PRECISION-TIME PG (another team?) │
  │ /tags/region)            │                        │  → places on precision-time HW    │
  │ parent ref = UNCHECKED    │  Operator/LinkedGroupId│  → shared high-precision-time rack│
  └──────────────────────────┘  (reserved, unscoped)  └───────────────────────────────────┘
                                                              │ co-residency observable
                                                              ▼ via DescribeInstanceTopology → HUB Area 1
```

## 3. Trust-Boundary Map (create-action rows; hub owns the rest)

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller creating a cluster PG | Another team's/account's precision-time **parent** PG | `--parent-group-id pg-xxxx` (no authz on parent, no condition key) | create succeeds referencing a parent the caller has no grant on; subsequent launches place on the parent's precision-time hardware |
| Caller | Undocumented control-plane behaviour | `LinkedGroupId` / `Operator` reserved params | API accepts the param and sets a state/ownership attribute the caller could not set via any documented, IAM-scopable path |
| Low-priv caller | `precision-time` strategy a Deny meant to forbid | stale `ec2:PlacementGroupStrategy` enum | a `Deny strategy=precision-time` (or `Deny strategy≠cluster`) is **inert** → precision-time PG created despite the policy |
| Caller with `CreatePlacementGroup` only | Resources protected by PG-tag ABAC | `aws:RequestTag` tag-on-create | caller self-sets the tag that `DeletePlacementGroup`/`RunInstances` ABAC keys on → self-widen / delete-protect / evade |
| Caller | Account PG namespace / 500-quota | create by name | intra-account name land-grab or 500/Region exhaustion (cross-account squat refuted — unique per-account) |

## 4. API / Interface Inventory

Single action in scope: `CreatePlacementGroup` (SDK + CLI `create-placement-group` + PowerShell `New-EC2PlacementGroup`). Mutating, external-facing, callable by any principal holding `ec2:CreatePlacementGroup`. Dependent action: `ec2:CreateTags` (fired when `TagSpecification` present). **Undocumented/console-hidden parameters flagged per skill Step 3:** `LinkedGroupId`, `Operator` (both accepted by the control-plane API + SDK model, absent from the console and the UG/CLI prose page — the exact "accepted by the API but not surfaced in the console or public documentation" shape). See the parameter table in §2.

## 5. Recommended Areas of Focus

### Area 1 — `--parent-group-id`: create-time cross-PG reference with NO authz on the referenced parent (HEADLINE; precursor to hub Area 1 HARD STOP)

**Background.** The create page's net-new feature: *"If you chose Cluster, you can optionally specify a parent precision time placement group to ensure that instances in the cluster placement group launch on precision time capable hardware."* The API reference confirms `ParentGroupId` ("The ID of a parent placement group. Valid only when Strategy is `cluster`") with **no statement that the parent must be owned by the caller**. `CreatePlacementGroup` has a **single resource-type row** (the created PG) and **no `ParentGroupId` condition key exists anywhere in `list_ec2.md`** (grep=0) — so the parent reference is evaluated by nothing in IAM.

**Security concern.** (a) **Parent land-grab / cross-team linkage** — can a caller create a `cluster` PG whose `--parent-group-id` points at a **precision-time parent PG they do not own** (another team's, or — if a precision-time PG is RAM-shared/resource-policy-shared — another account's)? If the control plane does not ownership-check the parent, this is a Lens A naming-asymmetry: authz checks the child, the operation binds to the parent. (b) **Co-residency precursor** — a precision-time parent "ensures instances launch on precision time capable hardware," i.e. a *specific, scarcer hardware pool*. Linking attacker capacity to a target's precision-time parent is a create-time **influence** step that narrows the host set before the `DescribeInstanceTopology` `nn-` confirmation — this is the `ec2-instance-topology` A6 / **hub Area 1** kill chain with a concrete create-time primitive. (c) **`pg-` id enumerability** — the parent is named by the opaque `pg-`+17hex id (not the name); assess whether the id is guessable/enumerable or must be learned (the shared-cluster-PG consumer already learns ids via the console bound-list).

**High-level test scenarios.**
- `iam:SimulateCustomPolicy` can't resolve the parent (DryRun/Simulate are caller-IAM only) → needs a scoped live create. Under a role holding only `ec2:CreatePlacementGroup` (scoped to its own PGs), `create-placement-group --strategy cluster --parent-group-id <foreign precision-time pg-id>`; confirm/refute whether the create is authorized against the parent's owner.
- If (a) holds, launch into the resulting cluster PG and inspect `DescribeInstanceTopology` `nn-` nodes for adjacency to the parent's instances → **HARD STOP + hand to hub Area 1** the moment a foreign-account `nn-` node is shared.
- Enumerate whether `--parent-group-id` accepts a cross-account `pg-` id at all (API-level), and whether a precision-time PG can even be shared (cross-ref `cr-cpg.md` / `share-placement-group.md`).

**Doc evidence.** `create-placement-group.md` console step 5.c + CLI "parent precision time placement group" example; `API_CreatePlacementGroup.html` `ParentGroupId` (cluster-only, no ownership text); `list_ec2.md` CreatePlacementGroup single-resource row + grep-confirmed absent `ParentGroupId` key.

**Severity.** Cross-account parent linkage confirming co-residency = **High–Critical + HARD STOP** (defer confirmation to hub Area 1). Cross-*team* intra-account parent land-grab = **Medium**. Precondition cap: cross-account requires the parent to be share-reachable first (consented-neighbour, same bound as hub Area 1); intra-account only needs the parent `pg-` id.

### Area 2 — Reserved / console-hidden parameters: `LinkedGroupId` ("future use") and `Operator` ("internal use")

**Background.** The API reference accepts two parameters the UG/CLI page and console never mention: `LinkedGroupId` — **"Reserved for future use"** (String) — and `Operator` — **"Reserved for internal use"** (an `OperatorRequest` object). The skill's Step-3 discipline flags exactly this: *a knob the reference accepts but the console/prose does not surface*. `Operator`/`OperatorRequest` is the EC2 "managed-resource operator" / Declarative-Services (DSP) construct; on **other** EC2 actions it correlates with the `ec2:ManagedResourceOperator` condition key (confirmed present on e.g. network-interface + instance rows at `list_ec2.md` 4697/4715) — but **`CreatePlacementGroup` carries no `ec2:ManagedResourceOperator` key** (not in its 5-key row). `LinkedGroupId` has no condition key either.

**Security concern.** (a) **`Operator` ownership/management attribute set with no IAM grain** — if the create action honours `Operator`, a caller may stamp the new PG as managed-by / operated-by a principal of their choice (or mark it AWS-managed), with no `ec2:ManagedResourceOperator` condition key available on the create action to deny or scope it → an authz-invisible ownership/attribution knob (Lens U doc-vs-enforcement + Step-3 permissive-value question: "what is the most permissive value the API accepts, and does anything warn the operator?"). (b) **`LinkedGroupId` latent/forward-compat parameter** — a "reserved" field accepted today may link the PG to another group (name mirrors `ParentGroupId`'s linkage shape); test whether it is silently accepted, validated, or ignored, and whether a value is persisted/returned. (c) Neither appears in CloudTrail-visible console flows → a value set via raw API is less likely to be noticed (Lens O enabler).

**High-level test scenarios.**
- Enumerate the `OperatorRequest` shape (`API_OperatorRequest.html`); send `create-placement-group` with a populated `Operator` under a non-privileged role; inspect the returned `PlacementGroup` / `DescribePlacementGroups` for an operator/managed attribute and whether `ec2:ManagedResourceOperator` (on any *other* action) can retroactively scope it. Does the service reject, honour, or ignore it? Any warning?
- Send `LinkedGroupId` with a syntactically valid `pg-` id and with garbage; record accept/validate/ignore + whether it is reflected in the response or a later Describe.
- Confirm these are genuinely absent from the console + CLI docs (Step-3 delta) and file the console/API documentation delta regardless of behaviour.

**Doc evidence.** `API_CreatePlacementGroup.html` `LinkedGroupId`/`Operator` verbatim; `list_ec2.md` CreatePlacementGroup 5-key row (no `ec2:ManagedResourceOperator`) vs 4697/4715 rows that do carry it.

**Severity.** If `Operator` sets an ownership/attribution attribute unscopable on create = **Medium–High** (Lens U, AWS-owned, reportable — an API-accepted auth/attribution-affecting field with no condition key + no console surface). If both are inert/ignored = **Informational doc-defect** (reserved params publicly documented but non-functional). Settleable with a single scoped live call each.

### Area 3 — `precision-time` strategy: stale `ec2:PlacementGroupStrategy` enum → create-time fail-open

**Background.** `Strategy` valid values are **`cluster | spread | partition | precision-time`** (API ref), and the create page offers `precision-time` as a first-class console/CLI choice. But the `ec2:PlacementGroupStrategy` **key definition** reads "…(cluster, spread, or partition)" — it **omits `precision-time`** (`list_ec2.md` 10133). Two possibilities: (i) the enum text is merely stale prose but the key *does* populate with the string `precision-time` at eval → a `StringEquals`/`StringNotEquals` Deny works; (ii) the key is genuinely not populated for `precision-time` creates → any `Deny` or `Allow` conditioned on `ec2:PlacementGroupStrategy` is **inert against precision-time**, i.e. a `Deny strategy ≠ cluster` fails *open* (precision-time slips through) and a `Deny strategy = precision-time` never matches.

**Security concern.** An admin who writes `"Deny": {"StringNotEquals": {"ec2:PlacementGroupStrategy": "cluster"}}` (intending "only cluster PGs") may silently allow `precision-time` PG creation if the key doesn't populate — and precision-time PGs are the ones that pull onto scarce precision-time hardware (Area 1 chain). Mirror risk for `RunInstances`/`DeletePlacementGroup`/`ModifyInstancePlacement`, which share the same key.

**High-level test scenarios.** `iam:SimulateCustomPolicy` with a policy keyed on `ec2:PlacementGroupStrategy` and a simulated `create-placement-group` context where `Strategy=precision-time`: does the key resolve to `precision-time` (match) or to *absent* (no match → fail-open)? Repeat for a live scoped create under both a `StringEquals cluster` Allow and a `StringNotEquals cluster` Deny.

**Doc evidence.** `API_CreatePlacementGroup.html` Strategy valid-values incl. `precision-time`; `list_ec2.md` 10133 key def omitting it.

**Severity.** Low–Medium (potential fail-open of a strategy-restriction policy). AWS-owned if the key genuinely cannot express a value the action accepts (Lens S "key that does not exist / is silently ignored" variant) — a reportable doc/enforcement defect even at Low.

### Area 4 — Create-time structural scoping gaps: `PartitionCount`, `SpreadLevel`, optional name, can't-mandate

**Background.** `PartitionCount` (Integer, partition-only) and `SpreadLevel` (`host|rack`) have **no condition key** (grep=0). `GroupName` and `Strategy` are both **Required: No** at the API — a create can omit the name (service-generated?) and omit strategy (defaults to `cluster`). `SpreadLevel=host` is "only with Outpost placement groups" (links to hub Area 8).

**Security concern.** (a) An admin **cannot** author "partition PGs must have ≥N partitions" or "no `host`-level spread" or "spread PGs only" by any `CreatePlacementGroup` condition — the only scopable create knobs are name/strategy/tags/region. (b) `PartitionCount` has no stated range on this action (UG elsewhere says ≤7/AZ); test clamp-vs-reject for 0 / 8 / huge / negative values (Lens L input validation). (c) `SpreadLevel=host` outside an Outpost — accept vs reject? (d) Optional `GroupName` → does the service auto-generate a name, and is an auto-generated name predictable (feeds hub Area 6)?

**High-level test scenarios.** Attempt IAM policies forcing partition count / spread level → show inexpressible via `iam:SimulateCustomPolicy`. Live scoped creates with boundary `PartitionCount` values and `SpreadLevel=host` off-Outpost; record validation. Create with no `GroupName`; inspect the generated name's shape.

**Doc evidence.** `API_CreatePlacementGroup.html` (PartitionCount/SpreadLevel no-range, GroupName/Strategy optional); `list_ec2.md` 5-key create row.

**Severity.** Medium (structural "least-priv is inexpressible" gaps; AWS-owned structural). Input-validation findings = Low unless a value crosses tenants.

### Area 5 — Tag-on-create ABAC self-widening + create-time name/quota mechanics

**Background.** `CreatePlacementGroup` supports `aws:RequestTag/${TagKey}` + `aws:TagKeys` (tag-on-create), firing dependent `ec2:CreateTags`. The downstream PG actions `DeletePlacementGroup`, `ModifyInstancePlacement`, and the `RunInstances` placement-group row are all **`aws:ResourceTag`-scopable**. So the tag a caller sets *at create* is the same tag ABAC later keys on. The AWS-authored sample on this page applies `purpose=production` (`--tag-specifications 'ResourceType=placement-group,Tags={Key=purpose,Value=production}'`). **`GroupName` is now confirmed "unique within the scope of your account for the Region" (255 ASCII)** — this **settles the hub's open doc-gap #7**: PG names are unique *per-account*, so there is **no cross-account name-collision squat** (hub Area 6's cross-account-satisfy footgun stands only via the name-only *condition* with `Resource:"*"`, not via a real collision). 500 PGs/Region is the only stated limit.

**Security concern.** (a) **Self-widening / delete-protection** — a caller holding `CreatePlacementGroup` with no required-tag condition can create a PG tagged `purpose=production` (or any value a protective `Deny DeletePlacementGroup where ResourceTag/purpose=production` keys on) → self-grant deletion immunity, or conversely create *untagged* to evade a tag-gated management policy (Lens I/S "can the holder set the very tag the grant keys on"). (b) **Tag-on-create not enforced** — is there anything forcing a required tag at create, or can `aws:RequestTag`/`aws:TagKeys` conditions be bypassed by omitting `TagSpecification` entirely (tag-gate fail-open)? (c) **255-ASCII name** → whitespace/case/trailing-dot variants for the hub Area 6 name-only-condition footgun (defer depth to hub; note ASCII-only kills unicode-homoglyph variants). (d) Create-side 500/Region exhaustion with no per-principal cap key (defer DoS depth to hub Area 7).

**High-level test scenarios.** Under a role with `CreatePlacementGroup` but no `aws:RequestTag` condition, create a PG with a protective tag value; then confirm a tag-gated `DeletePlacementGroup` Deny now shields it (self-protection) — `iam:SimulateCustomPolicy` first. Test whether an `aws:RequestTag`-required create policy is bypassable by omitting tags. Confirm per-account name uniqueness (collision → error) via two creates of the same name.

**Doc evidence.** `create-placement-group.md` tag example + 500/Region limit; `API_CreatePlacementGroup.html` GroupName uniqueness/255-ASCII; `list_ec2.md` CreatePlacementGroup `aws:RequestTag`/`aws:TagKeys` + Delete/Modify/Run `aws:ResourceTag` rows.

**Severity.** Tag self-widening / delete-protection = **Medium** (customer-authored-ABAC footgun unless an AWS sample policy conditions on these without a self-tag Deny — none shown; the `purpose=production` sample is illustrative, not a policy). Name-uniqueness finding = settles a doc-gap (Informational, feeds hub). Quota exhaustion = Low.

## 6. Threat Model Test Objectives
| # | Threat / Test Case | Area | Component | Documented mitigation to attack | Status |
|---|---|---|---|---|---|
| C1 | `--parent-group-id` references foreign/other-team precision-time parent, no authz on parent | 1 | `CreatePlacementGroup` single-resource row | none stated (parent authz-invisible) | **doc-gap — HARD STOP if co-residency confirmed → hub A1** |
| C2 | `pg-` parent id enumerable / guessable | 1 | `pg-`+17hex id | opaque id (console bound-list) | doc-gap |
| C3 | `Operator` sets management/ownership attr unscopable on create | 2 | reserved `OperatorRequest` | no `ec2:ManagedResourceOperator` key on create | doc-gap — Lens U, settleable live |
| C4 | `LinkedGroupId` accepted/validated/persisted | 2 | reserved param | "Reserved for future use" (prose only) | doc-gap |
| C5 | `precision-time` strategy slips a `ec2:PlacementGroupStrategy` Deny (fail-open) | 3 | stale key enum | key filters strategy on the action | enum stale (doc defect) — SimulateCustomPolicy |
| C6 | Cannot author "only partition N" / "no host-spread" / "spread only" | 4 | PartitionCount/SpreadLevel (no key) | — (inexpressible) | structural gap |
| C7 | PartitionCount / SpreadLevel=host-off-Outpost input validation | 4 | `CreatePlacementGroup` | ≤7/AZ (elsewhere); host⇒Outpost | input-validation test |
| C8 | Tag-on-create self-widen / delete-protect / evade | 5 | `aws:RequestTag` + downstream `aws:ResourceTag` | tag-on-create conditions | footgun — SimulateCustomPolicy |
| C9 | Cross-account name squat | 5 | name-based ARN | **unique per-account+Region (confirmed)** | **refuted — no collision** |
| C10 | 500-PG/Region create exhaustion, no per-principal cap | 5 | quota | 500/Region | Low (→ hub A7) |

## 7. Out-of-Scope Risk Categories
- The co-residency *confirmation* step (topology `nn-`) — owned by **hub Area 1**; this child only supplies the create-time influence primitive and HARD-STOPs on a foreign `nn-` hit.
- Cross-account sharing lifecycle, `DescribePlacementGroups` oracle, name-only-condition footgun depth, `ModifyInstancePlacement`/shared-budget DoS — **hub Areas 2/3/6/7**.
- `spread`/`partition` "isolation defeated" within one's own account = availability/self-DoS, not a security boundary (**hub Area 5** framing).
- Outpost single-tenant hardware (`SpreadLevel=host`) — **hub Area 8** (single-tenant, OOS as a cross-tenant finding).
- The EC2 placement engine's internal host-selection logic (service plane) — observe/confirm only, never exploit; HARD STOP on service-plane evidence.
- Customer-authored over-broad IAM (footgun). AWS-authored/managed-policy weak defaults remain in scope (Lens R/S) — **but this page prints no policy JSON**, so Lens R cannot run here (same gap as hub §R-gap).

## 8. Null hypotheses / doc gaps

**Lenses fired:** A (cross-resource parent reference / id enumerability — Area 1), U (doc-vs-enforcement: reserved-param & stale-enum — Areas 2/3), S (condition-key scoping: no-key params, silently-ignored enum, tag self-widen — Areas 3/4/5), I (tag-on-create ABAC — Area 5), EE/L (name/quota create mechanics — Area 5), V (precision-time hardware placement influence — Area 1, defers to hub A1), Step-3 undocumented-knob (Area 2).

**Explicit NULL hypotheses (pages checked per skill discipline):**
- **Lens B/C (PassRole / credential-vending):** N/A — `CreatePlacementGroup` takes no role-ARN input; no STS/session-policy/ProvidedContext seam. (`Operator` is an attribution object, not a role the service assumes — but confirm its shape in Area 2 before closing hard.) Pages: `create-placement-group.md`, `API_CreatePlacementGroup.html`, `API_OperatorRequest.md` (to read).
- **Lens G (SSRF):** N/A — no URL/URI/endpoint/webhook/callback field; `ParentGroupId`/`LinkedGroupId` are internal `pg-` ids the service resolves internally, not dereferenced locations. Pages: `create-placement-group.md`, `API_CreatePlacementGroup.html`.
- **Lens Q (upload/blob):** N/A — no file/image/attachment field.
- **Lens F (translation/injection):** N/A — no parser/translation layer; `GroupName` is a 255-ASCII string stored verbatim (test only for name-condition canonicalization, which is hub Area 6).
- **Lens D (data→control-plane), W (attestation/enclave), FF (JWT), J (OAuth), M (session), Y (transport), BB/CC/DD (parser/edge/cache):** N/A — a single SigV4-authenticated control-plane create call; no data-plane process, enclave, bearer token, OAuth, session id, edge/cache, or multi-parser path. Pages: `create-placement-group.md`, `API_CreatePlacementGroup.html`, `list_ec2.md` (PG rows).
- **Lens R (AWS IAM-artifact audit):** **could not run** — the create page prints no managed/sample policy JSON (only a tag CLI example). Same gap flagged at hub §R-gap; follow-up is the generic EC2 IAM-policy UG pages, not this page.

**Confirmed facts established by this child (reusable):**
1. `CreatePlacementGroup` IAM row = exactly 5 keys (`aws:RequestTag`, `aws:TagKeys`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`); resource `placement-group*`; dependent `ec2:CreateTags`. (`list_ec2.md` 5370)
2. **No condition key** for `ParentGroupId`, `PartitionCount`, `SpreadLevel`, `LinkedGroupId`, or `Operator`→`ec2:ManagedResourceOperator` on the create action (grep-confirmed; `ec2:ManagedResourceOperator` exists elsewhere but not here).
3. `Strategy` accepts `precision-time`; the `ec2:PlacementGroupStrategy` key definition omits it (stale enum). (`list_ec2.md` 10133 vs API ref)
4. `GroupName` is **unique per-account+Region**, up to 255 ASCII, and **optional** — settles hub doc-gap #7; **cross-account name squat refuted** (no collision possible across accounts).
5. **Two reserved/console-hidden parameters** exist on the public API: `LinkedGroupId` ("Reserved for future use") and `Operator` ("Reserved for internal use", `OperatorRequest` object) — net-new, absent from the hub.
6. `groupId` form = `pg-` + 17 hex (API-ref sample responses).

**Top open doc-gaps carried for the hunter (priority order):**
1. **(Area 1, HARD STOP precursor)** Is `--parent-group-id` ownership-checked against the referenced precision-time parent? Can it reference a cross-account (shared) or other-team parent? Needs a scoped/2-account live create.
2. **(Area 2)** What do `Operator` and `LinkedGroupId` actually do, and does `Operator` set an unscopable ownership/management attribute? (Settleable with one scoped live call each + reading `API_OperatorRequest.html`.)
3. **(Area 3)** Does `ec2:PlacementGroupStrategy` populate with `precision-time`, or is it inert (fail-open)? (`iam:SimulateCustomPolicy`.)
4. **(Area 4)** `PartitionCount` accepted range (clamp vs reject at 0/8/huge/negative); `SpreadLevel=host` off-Outpost accept/reject; optional-`GroupName` auto-generation shape.
5. **(Area 5)** Is an `aws:RequestTag`-required create policy bypassable by omitting `TagSpecification`? Does tag-on-create enable delete-protection self-widening?
