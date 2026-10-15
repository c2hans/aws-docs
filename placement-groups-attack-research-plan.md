# EC2 Placement Groups — Attack Research Plan (HUB)

Source of leads: `AWSEC2/latest/UserGuide/placement-groups.html` (hub) + its 6 child pages
(`placement-strategies`, `create-placement-group`, `change-instance-placement-group`,
`delete-placement-group`, `share-placement-group`, `placement-groups-outpost`) + the
`cr-cpg` (Capacity Reservations in cluster placement groups) page + the IAM Service
Authorization Reference `list_ec2.md`. Status: **documentation-derived hypotheses only; nothing tested against a live account.** Offline mirror == online `.md` for `placement-groups.md` verified 2026-10-15.

This is the **HUB** plan. It owns the hub-level surface (the rules/limitations list, the
physical-isolation guarantees of the strategies, the IAM-backbone condition-key map, the
cross-account sharing seam, and the co-residency kill-chain cross-reference). Per-page
granular deep-dives belong in page-level child plans (`share-placement-group-*`,
`placement-strategies-*`, `create-placement-group-*`, etc.); where a child plan does not yet
exist, the relevant Area below is self-contained enough for a hunter to execute directly.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- `iam:SimulateCustomPolicy`/`SimulatePrincipalPolicy` is the safe first oracle for every condition-key claim (no resources touched). Escalate to a scoped live call only with synthetic canary data under a role holding exactly the artifact under test.
- **HARD STOP:** the moment evidence shows cross-**account** physical co-residency being *confirmed* (a `nn-` topology node shared with a foreign account), or any identity/credential/ARN/account belonging to AWS's own service plane / placement engine, stop, preserve evidence, flag for AWS-Security disclosure. Co-residency confirmation is the hub's single highest-severity trigger.

## 1. Pentest Objectives
1. Launch an instance into, or read the membership/placement of, a placement group **owned by another account** without a valid share — or **after** a share was revoked.
2. Defeat the **physical-isolation guarantee** of `spread`/`partition` ("do not share the underlying hardware") — i.e. cause two instances the model says are isolated to land on the same host, or prove the guarantee is advisory only.
3. Use a `cluster` placement group (optionally + a Capacity Reservation, optionally RAM/resource-policy-shared) as a **sanctioned cross-account co-residency primitive** — deliberately co-locate attacker capacity next to a target, then confirm co-residency via EC2 instance topology (`nn-` nodes). (Chains to the `ec2-instance-topology` plan A6.)
4. Establish or keep **cross-account access to a shared placement group** that the owner's `PutResourcePolicy`/RAM share did not intend, or that survives `DeleteResourcePolicy`/unshare.
5. Prove an admin **cannot** author an IAM policy that forces a given placement strategy / forbids `cluster` / scopes to one PG — i.e. find where the `ec2:PlacementGroupStrategy`/`PlacementGroupName` keys are *inert* on the action that actually matters.
6. Pre-register / squat a **predictable placement-group name** so a victim or service resolves/targets the attacker's PG (name-based ARN, no entropy).
7. Enumerate every placement group in the account via the unscopable `DescribePlacementGroups` read oracle despite a tag/ARN Deny.

## 2. Components, Assets, and Design

**What a placement group is.** A named, Region+Account-scoped EC2 resource that *influences
physical placement* of interdependent instances. Four strategies:
- **Cluster** — packs instances close together inside one AZ for low-latency HPC (→ *same rack / adjacent hardware* = intentional co-residency).
- **Partition** — spreads instances across logical partitions; "groups of instances in one partition **do not share the underlying hardware** with groups in different partitions" (≤7 partitions/AZ). *Isolation guarantee.*
- **Spread** — "**Strictly places** a small group of instances across **distinct underlying hardware**" to reduce correlated failure (≤7 instances/AZ for a rack-spread; host-level spread limits apply). *Isolation guarantee.*
- **Precision time** — places on hardware with direct access to high-precision time sources.

**Resource identity.** ARN = `arn:${Partition}:ec2:${Region}:${Account}:placement-group/${PlacementGroupName}`.
The identifier is the **operator-chosen name** — no opaque high-entropy id, no checksum. Also carries a `${PlacementGroupId}` form in some APIs, but the ARN and the `ec2:PlacementGroupName` key key off the **name**.

**Ownership / trust zones.** A PG belongs to the account that created it. Two cross-account
exposure mechanisms exist:
1. **AWS RAM share** (`share-placement-group.html`) — share the PG to another account/OU/Org; consumers launch instances into it.
2. **Native EC2 resource-based policy** — `ec2:PutResourcePolicy`/`GetResourcePolicy`/`DeleteResourcePolicy` carry a `placement-group` resource type ("attach an IAM policy that enables cross-account sharing to a resource"). This is a *second, API-level* sharing path distinct from RAM.
When shared and used for `cluster`, the owner's and consumer's instances become **co-resident on shared physical hardware across an account boundary** — this is the asset of highest interest.

**Enforcement reality.** The physical-isolation / co-location behavior is enforced by the
**EC2 placement engine** (service plane), not by any customer-visible mechanism. IAM can
scope *which* PG/strategy you may target (`ec2:PlacementGroupStrategy`/`Name`) but cannot
attest that the hardware isolation actually held. "within your organization" sharing bounds
are RAM/SCP only — **EC2 has zero `aws:PrincipalOrgID`/`ResourceOrgID` condition keys** (grep of full `list_ec2.md` = 0).

```
  caller account A                         AWS placement engine (service plane)
  ┌───────────────┐   RunInstances(PG)     ┌───────────────────────────────┐
  │ IAM: can scope│ ────────────────────▶  │ decides host/rack/partition   │
  │ Strategy/Name │                        │  (cluster=pack, spread=split) │
  └───────────────┘                        └───────────────────────────────┘
        │ PutResourcePolicy / RAM share            ▲ co-residency observable
        ▼                                          │ via DescribeInstanceTopology (nn-)
  account B consumer ── RunInstances(sharedPG) ────┘   = cross-acct co-residency
```

## 3. API / Interface Inventory (from `list_ec2.md`, confirmed 2026-10-15)

| Action | Resource type (required) | Condition keys (PG-relevant) | Access | Notes |
|---|---|---|---|---|
| `CreatePlacementGroup` | `placement-group*` | `aws:RequestTag`, `aws:TagKeys`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region` | Write | strategy+name **scopable at create**; tag-on-create supported |
| `DeletePlacementGroup` | `placement-group` | `aws:ResourceTag`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`, `ec2:ResourceTag` | Write | |
| `ModifyInstancePlacement` | `dedicated-host` / `instance*` / `placement-group` | instance row: `ec2:Attribute` +tags; PG row: `ec2:PlacementGroupName`/`Strategy` | Write | moves instance in/out of PG, changes partition # |
| `DescribePlacementGroups` | **(blank)** | **`ec2:Region` only** | List | **unscopable account-wide read oracle** |
| `RunInstances` (placement-group row) | `placement-group` | `ec2:IsLaunchTemplateResource`, `ec2:LaunchTemplate`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`, tags | Write | launch into PG, strategy/name scopable |
| `AttachResourcesToPlacementGroup` | `placement-group*` | `aws:ResourceTag`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, ... | **Permissions management, Write** | **2nd populate path**; doc link is a broken placeholder (`docs.aws.amazon.com/UserGuide/placement-groups.html`) = doc-defect |
| `PutResourcePolicy` | `placement-group` (+ipam-pool, verified-access-group) | `aws:ResourceTag`, `ec2:PlacementGroupName`, ... | **Permissions management, Write** | **native cross-account sharing**; doc link mis-points at IPAM page |
| `GetResourcePolicy` | `placement-group` (+...) | `aws:ResourceTag`, `ec2:PlacementGroupName`, ... | Read | read the share policy |
| `DeleteResourcePolicy` | `placement-group` (+...) | `aws:ResourceTag`, `ec2:PlacementGroupName`, ... | **Permissions management, Write** | revoke the share |
| `CreateCapacityReservation` | `capacity-reservation*` | incl. `ec2:PlacementGroup`, `ec2:InstanceMatchCriteria`, `ec2:Tenancy`, `ec2:OutpostArn`, ... | Write | CR into a cluster PG → co-residency "influence" step |
| `RequestSpotFleet` / `RequestSpotInstances` | `placement-group` | `ec2:PlacementGroupName`/`Strategy` | Write | fleet launch into PG |

Condition-key definitions (verbatim):
- `ec2:PlacementGroup` — "Filters access by the ARN of the placement group" — **ARN**
- `ec2:PlacementGroupName` — "Filters access by the name of a placement group" — **String**
- `ec2:PlacementGroupStrategy` — "Filters access by the instance placement strategy used by the placement group (cluster, spread, or partition)" — **String** (note: enum omits `precision time` in the doc text — possible gap)

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Consumer account B | Owner A's placement group | RAM share / `PutResourcePolicy` | B launches into / reads / mutates A's PG beyond the grant, or after `DeleteResourcePolicy`/unshare |
| Attacker account | Target account hardware | `cluster` PG (shared) + CR | `DescribeInstanceTopology` shows a `nn-` node shared across the account boundary = **HARD STOP** |
| Low-priv caller | A specific strategy/PG | `ec2:PlacementGroupStrategy`/`Name` Deny | caller launches `cluster` where policy intended only `spread`, because the key is inert on the acting API |
| Any caller | Every PG in account | `DescribePlacementGroups` | enumerate all PGs despite tag/ARN Deny (blank resource row) |
| Attacker | Predictable PG name | name-based ARN, first-come namespace | attacker pre-creates the name a victim/service resolves |
| Caller | AWS placement engine | `spread`/`partition` guarantee | two "isolated" instances land on the same host (guarantee is advisory) |

## 5. Recommended Areas of Focus

Eight areas, prioritised. **Area 1 is the crown-jewel / HARD-STOP lead.** Each area: Background → Security concern → High-level test scenarios → Doc evidence → Severity. Confirmed facts are tagged `[F#]` to the sub-analysis that established them (SG1 = shared-PG/RAM, SG2 = strategies+CRUD, SG3 = Outpost+CR); all offline==online verified 2026-10-15.

---

### Area 1 — Cross-account co-residency in a shared `cluster` PG + the topology side-channel (CROWN JEWEL / HARD STOP)

**Background.** A `cluster` placement group is AWS's *sanctioned* mechanism for packing instances onto the same low-latency rack/segment. When a cluster PG is RAM-shared (or a CR inside it is shared), the owner's and a consumer's instances become **co-resident on shared physical hardware across an account boundary** — co-residency is the feature, not a bug. The only documented control against one party *learning the other's physical placement* is one prose sentence: "Each topology view is unique per AWS account" (`ec2-instance-topology.md`). `DescribeInstanceTopology`/`DescribeCapacityReservationTopology` return `nn-xxxxxxxxxx` network-node IDs where a shared node ⇒ physical adjacency, and both actions have **no resource type and only `ec2:Region`** as a condition key — so the per-account scoping is 100% server-side, un-IAM-auditable. Separately, CR-only sharing promises the consumer gets "**no visibility or access to the placement group... including its ARN**" (`cr-cpg.md`) — yet `DescribeInstanceTopology`'s worked example populates a `GroupName` field for PG-member instances.

**Security concern.** (a) Can a consumer of a shared cluster PG (or a shared CR inside one) use topology `nn-` nodes / `GroupName` to confirm cross-account co-residency with the owner, or with a *second, mutually-untrusted* consumer of the same share — a guided co-location → confirm loop (the `ec2-instance-topology` plan's A6 kill-chain, now with a concrete sharing primitive)? (b) Does the `GroupName`/topology surface violate CR-only sharing's explicit "no PG visibility, including ARN" guarantee (Lens U enforcement-gap feeding a Lens A disclosure)?

**High-level test scenarios.**
- Two-account shared cluster PG: as consumer B, launch matching instances, call `DescribeInstanceTopology` on *your own* instances, inspect `GroupName` + `nn-` node set for any value that correlates to / discloses A's instances or the PG ARN that CR-only sharing said is hidden.
- Two mutually-untrusted consumers (B, C) of the *same* owner-A CR inside a cluster PG: do repeated `open` launches + topology polling let B detect `nn-` overlap with C's instances (co-residency oracle between parties whose only link is A)?
- Chain to `ec2-instance-topology` A6: observe (topology) → influence (`CreateCapacityReservation` with `ec2:PlacementGroup` into a cluster PG, `open` match-criteria auto-pulls matching instances) → confirm (re-read `nn-`).

**Doc evidence.** `ec2-instance-topology.md` "unique per AWS account" + "console does not support viewing topology" (API-only) [SG1 F15/F16]; `cr-cpg.md` auto-match + "Consumer accounts have no visibility or access to the placement group... including its ARN" + `GroupName:"ML-group"` in the topology worked example [SG3 Lead 2]; `list_ec2.md` `DescribeInstanceTopology`/`DescribeCapacityReservationTopology` = blank resource type + `ec2:Region` only [SG1 F15 / SG3 Lead 1]; `CreateCapacityReservation` carries `ec2:PlacementGroup`/`ec2:InstanceMatchCriteria` [SG3 Lead 4].

**Severity.** **High–Critical if confirmed. HARD STOP** the moment a `nn-` node is observed shared with a *foreign account*, or `GroupName`/ARN leaks across the CR-only-sharing boundary — preserve evidence, flag for AWS-Security disclosure, do not escalate. **Precondition caps blast radius:** every cross-account path requires the *owner* to have initiated a RAM/CR share to the attacking account/OU/org first (SG3 confirmed no unconsented path exists in `cr-cpg.md`/`capacity-reservation-sharing.md`/`list_ec2.md`) — this is a *consented-neighbour* co-residency oracle, not an arbitrary-victim reach.

---

### Area 2 — Cross-account sharing lifecycle: grantee validation, org-leave orphaning, unshare completeness, native-vs-RAM path

**Background.** A PG is shared via **AWS RAM** (invitation+accept for non-org accounts; automatic for org members if org-sharing is toggled on). The EC2 `*ResourcePolicy`/`*ResourcesToPlacementGroup` actions are **"Permission-only"** — the SAR header states they are *"not directly invocable through any API operation; they can only be used in IAM policy statements"* — i.e. they are the dependent-action gates RAM fires internally, **not** a standalone customer sharing API [SG1 F12/AA3]. EC2 and RAM both expose **zero `aws:PrincipalOrgID`/`aws:ResourceOrgID`** keys (grep = 0 in both `list_ec2.md` and `list_ram.md`) [SG1 F21]; RAM's `ram:Principal` key filters principal **format only, not membership** [SG1 F19].

**Security concern.** (a) **Org-leave orphaned grant** — RAM's `ram:RetainSharingOnAccountLeaveOrganization` Boolean implies a share *can* be configured to survive an account leaving the org; neither page states the **default** or the auto-revoke behaviour → a stale cross-trust-boundary grant surviving divestiture (classic Lens AA stranded grant). (b) **Grantee validation** — does RAM service-side validate an OU/Org-ARN principal exists and is the caller's own org, or only the syntactic `ram:Principal` format IAM sees? (c) **Unshare completeness** (Lens AA, *answered*): running instances **survive** unshare — disassociated from the PG, kept running in their owner account; new launches/reservations blocked going forward — a clean design, not a bug. Residual: **TOCTOU** between `DeleteResourceShare` and an in-flight consumer `RunInstances`/`ModifyInstancePlacement`. (d) No org-ID pinning condition key means org-restriction is a coarse RAM toggle (`ram:AllowsExternalPrincipals` all-or-nothing), not an SCP-authorable boundary.

**High-level test scenarios.**
- Org-wide PG share with `RetainSharingOnAccountLeaveOrganization` at default (or =true); remove the consumer account from the org; check whether it can still launch into / read the PG.
- `CreateResourceShare`/`AssociateResourceShare` with a syntactically-valid but non-existent / foreign OU/Org ARN principal; does the API reject it (service-side membership check) even though `ram:Principal` only checked format?
- Fire `DeleteResourceShare` concurrently with a consumer `RunInstances` referencing the shared PG by ID — can the launch land after the share is gone?
- Desk-check (already confirmed as a gap): try to author an SCP denying `ram:CreateResourceShare` unless principal ∈ `o-xxxx` using only documented keys — no such key exists.
- Sanity-check that no EC2 SDK `put-resource-policy` method exists (confirms AA3 refutation; else the invitation-accept gate has a direct-call bypass).

**Doc evidence.** `share-placement-group.md` share targets / unshare semantics / "can't re-share" [SG1 F1/F2/F10/F11]; `list_ram.md` `ram:RetainSharingOnAccountLeaveOrganization`, `ram:Principal` "format", `ram:AllowsExternalPrincipals` [SG1 F19]; `list_ec2.md` Permission-only header + the 5 entries [SG1 F12]; zero org-ID keys both files [SG1 F21].

**Severity.** Org-leave orphaning = **High if confirmed**. Grantee-validation gap = Med–High if service-side check is absent. TOCTOU = Medium (one extra instance). No-org-key = Low/Informational (defence-in-depth gap, amplifies the above). AA3 (direct `PutResourcePolicy` bypass) = **refuted by docs** — keep as a closed negative result.

---

### Area 3 — "Can't view instances you don't own" is prose-only; the Describe read-oracle is unscopable

**Background.** `share-placement-group.md` guarantees a consumer "can't view or modify instances and capacity reservations... not owned by you" [SG1 F7]. But `DescribePlacementGroups` has **no resource type and no condition keys** (fully unscoped List) [SG1 F14 / SG2 F4], and `DescribeInstances` likewise cannot be resource-scoped — so this guarantee can only be enforced by server-side ownership filtering inside the EC2 control plane, with **no `Condition`/`Resource` a customer could author** to back it.

**Security concern.** Does any field — instance IDs, counts, strategy, even error-code / latency / throttling differentials — disclose the owner's co-resident instances to the consumer, despite the F7 promise? And independently: an unscopable `DescribePlacementGroups` means any principal granted it reads **every PG in the account+Region** regardless of a tag/ARN Deny (intra-account enumeration oracle; twin of the `DescribeInstanceTopology` shape and of other blank-resource EC2 Describes catalogued across the ENI/topology plans).

**High-level test scenarios.** From a consumer account in a two-account shared cluster PG, call `DescribePlacementGroups` / `DescribeInstances`; diff responses & error behaviour for any owner-side leak. Intra-account: with a tag/ARN Deny on PGs, confirm `DescribePlacementGroups` still returns all of them.

**Doc evidence.** `share-placement-group.md` F7; `list_ec2.md` `DescribePlacementGroups` blank-resource + `ec2:Region` only [SG1 F14 / SG2 F4].

**Severity.** Cross-account instance disclosure = **Critical if confirmed** (currently doc-gap, *not refuted*). Intra-account unscopable enumeration = Low–Medium (least-priv structural gap, AWS-owned).

---

### Area 4 — Placement-knob IAM scoping gaps: can scope *strategy*, cannot *mandate a PG*, cannot scope partition/spread/parent

**Background.** Contrary to the "unscopable like `ec2:InterfaceType`" prior, `ec2:PlacementGroupStrategy` **is** a real, scopable key on `CreatePlacementGroup`/`RunInstances`/`DeletePlacementGroup`/`ModifyInstancePlacement` [SG2 F1]. But three gaps: (a) the `RunInstances` placement-group row is **conditional, not required** — no key can **mandate** that a launch *use* a PG at all (you can forbid `cluster`, you cannot force membership) [SG2 F1]; (b) **no IAM key** exists for partition count, spread level, or parent-group linkage — grep-confirmed absent `PartitionNumber`/`PartitionCount`/`SpreadLevel`/`ParentGroupId` [SG2 F2]; (c) the `ec2:PlacementGroupStrategy` doc enum is **stale** — lists only cluster/spread/partition, omitting `precision-time` [SG2 F1, plan §3]. Plus: `CreatePlacementGroup` offers **zero condition keys for Outpost scoping** — no `ec2:OutpostArn` even though that key exists on `CreateCapacityReservation` — so you cannot restrict *which Outpost* a role creates PGs on [SG3 Surface 1].

**Security concern.** (a) `--parent-group-id` on `CreatePlacementGroup` links a new PG to a `precision-time` parent in **another team's** scope with **no IAM check on the referenced parent** — `CreatePlacementGroup` exposes a single resource-type row (the created PG), so the parent reference is authz-invisible (Lens A asymmetry, parent-link land-grab) [SG2 F3]. (b) A stale strategy enum could mean a `Deny strategy≠X` policy fails open against `precision-time`. (c) Admin cannot author "every launch must be in a PG" or "only partition N" — enforcement gaps a least-priv design would assume exist.

**High-level test scenarios.** `iam:SimulateCustomPolicy` first: prove a `Deny PlacementGroupStrategy=cluster` is bypassable via a path where the key is inert; prove `precision-time` slips a stale-enum Deny. Create a PG with `--parent-group-id` pointing at a foreign/precision-time parent; confirm no authz on the parent. Attempt an IAM policy to force PG membership on `RunInstances` → show it's inexpressible.

**Doc evidence.** `list_ec2.md` per-action condition-key rows [SG2 F1/F2], `CreatePlacementGroup` no-Outpost-key [SG3]; `placement-strategies.md`/`create-placement-group.md` `--parent-group-id` [SG2 F3]; key definition text omitting precision-time (plan §3).

**Severity.** `--parent-group-id` cross-link = **Med–High**. Can't-mandate-PG / can't-scope-partition = Medium (structural). Stale enum = Low–Med (potential fail-open). Outpost-scoping gap = Low (intra-account least-priv footgun; single-tenant hardware).

---

### Area 5 — Framing correction: `spread`/`partition` "physical isolation" is an availability guarantee, NOT a tenant-security boundary

**Background.** The docs say partition groups "do not share the underlying hardware" and spread "strictly places across distinct underlying hardware" — language that *reads* like a security isolation claim. It is a **correlated-failure / availability** guarantee, enforced best-effort by the EC2 placement engine (service plane) [SG2 F6].

**Security concern.** This area exists to **prevent severity inflation**, not to assert a bug. "Two instances landed on the same host despite spread" is a *self-account availability* concern (your own fleet's blast-radius assumption), **not** a cross-tenant isolation break — there is no second tenant being isolated *from* by spread/partition. Treat any "isolation defeated" lead here as self-DoS/OOS unless it crosses an account boundary (in which case it belongs in Area 1). Flag the doc wording as a clarity gap worth reporting to AWS, since it invites exactly this mis-rating.

**High-level test scenarios.** None that produce a cross-tenant finding. If testing resilience assumptions: launch a spread PG at its limit, correlate `nn-`/host placement, confirm distinctness — but file results as availability, not security.

**Doc evidence.** `placement-groups.md`/`placement-strategies.md` strategy descriptions [SG2 F6].

**Severity.** N/A as a security finding (framing/doc-clarity note). Prevents mis-scoring Objective 2.

---

### Area 6 — Predictable PG-name land-grab + name-only IAM-condition footgun

**Background.** PG ARN = `…:${Account}:placement-group/${PlacementGroupName}` — the identifier is the **operator-chosen name**, no entropy, scoped under `${Account}` so two accounts can hold identically-named PGs [SG1 F8 / SG2 F5]. `ec2:PlacementGroupName` matches the **bare string** with **no account-binding key** — only pinning `Resource` (vs `Resource:"*"`) ties a grant to one account [SG1 F18].

**Security concern.** A policy that gates `RunInstances` on `Condition:{StringEquals:{ec2:PlacementGroupName:"shared-name"}}` with `Resource:"*"` is also satisfied by an **attacker-owned, identically-named PG in a different account** — a name-only-condition footgun. **AWS's own documented mitigations** (confirmed): CLI launch into a non-owned PG **requires the PG ID, not the name** [SG1 F5]; console uses a bound RAM-derived list, not free-text [SG1 F6] — strongly implying AWS considered this shape. PG name uniqueness-per-account behaviour was **not confirmed** by the four pages (doc-gap).

**High-level test scenarios.** Author the anti-pattern policy; create an attacker-owned PG with the leaked/guessed name in a second account; show the condition is satisfied cross-account. Confirm the console's enumeration source is strictly RAM-association-derived, not a name search.

**Doc evidence.** ARN format + name-based condition [SG1 F8/F18/F5/F6, SG2 F5]; **no sample policy JSON** is printed on `share-placement-group.md` — it names only two bare action strings (unusual; Lens R could not run) [SG1 F9/§R-gap].

**Severity.** Medium **as a customer-authored footgun** (Lens S/EE) — **not an AWS-owned defect** unless an AWS-shipped sample policy conditions on `ec2:PlacementGroupName` without `Resource` pinning (none found; doc-gap).

---

### Area 7 — Resource exhaustion / forced-downtime sabotage levers (lower severity, intra-account)

**Background.** 500 PGs/Region quota; partition max 7/AZ; spread max 7 running instances/AZ; **sharing does NOT multiply these — limits are shared across all consumers** [SG1 F3 / SG2 F7]. `ModifyInstancePlacement` (move an instance in/out of a PG or change its partition) requires the instance be **`stopped`**, is strategy-scopable but the **partition target is not scopable**, and can fail on capacity [SG2 F8].

**Security concern.** (a) A malicious/greedy consumer of a *shared* partition/spread PG can consume the shared 7/AZ budget, denying the owner or co-consumers placement (cross-account *availability* grief within a consented share). (b) `ModifyInstancePlacement` forces a stop→modify→start cycle = a forced-downtime + capacity-reacquisition-failure sabotage lever against instances a principal can modify. (c) 500/Region PG quota as a self/shared-DoS exhaustion ceiling with no IAM key to cap per-principal PG count.

**High-level test scenarios.** As a shared-PG consumer, fill the 7/AZ spread/partition budget; confirm the owner is then denied. Trigger `ModifyInstancePlacement` on a target instance; measure the forced-stop window + capacity-fail. Exhaust the 500 PG/Region ceiling; confirm no per-principal cap key.

**Doc evidence.** `placement-groups.md`/`share-placement-group.md` limits + "shared, not multiplied" [SG1 F3]; `list_ec2.md` `ModifyInstancePlacement` resource/condition rows [SG2 F8].

**Severity.** Low–Medium. Shared-budget denial = Medium within a consented share; forced-downtime = Medium; quota exhaustion = Low.

---

### Area 8 — Outpost placement groups: NULL / out-of-scope (documented negative result)

**Background.** PGs on an AWS Outpost "work in the same way as in regular AZs," but an Outpost is provisioned and billed to a **single owning account** (`outpost` ARN has one `${Account}` segment; `list_outposts.md` has **no sharing action at all** — grep "share"/"RAM"/"cross-account" = 0 hits). CR-sharing *on* an Outpost shares consumption of the owner's own capacity (identical to regional CR sharing → folds into Area 1), not the Outpost resource itself [SG3 Surface 1].

**Security concern.** None cross-tenant: placement groups there spread instances across the **one customer's own** hosts/racks — self-co-residency only, which is not a security boundary. Recorded as a NULL so a downstream hunter does not re-spend time, with the one residual (Area 4) that `CreatePlacementGroup` can't be scoped by `ec2:OutpostArn`.

**Doc evidence.** `placement-groups-outpost.md`, `capacity-reservations-outposts.md`, `list_outposts.md` (full action/resource/condition-key listing) [SG3 Surface 1]. Offline==online byte-identical 2026-10-15.

**Severity.** NULL (out of scope — single-tenant customer-owned hardware, no sharing primitive).

## 6. Threat Model Test Objectives
| # | Threat / Test Case | Area | Component | Documented mitigation to attack | Status |
|---|---|---|---|---|---|
| T1 | Confirm cross-account co-residency via topology `nn-`/`GroupName` in shared cluster PG | 1 | topology API + shared `cluster` PG/CR | "topology view unique per account" (prose only, no IAM) | **doc-gap — HARD STOP if confirmed** |
| T2 | CR-only share leaks PG ARN/`GroupName` despite "no PG visibility" promise | 1 | `cr-cpg.md` share + `DescribeInstanceTopology` | "consumer has no visibility... including its ARN" | doc-gap — Lens U enforcement test |
| T3 | Grant survives org-leave (`RetainSharingOnAccountLeaveOrganization`) | 2 | RAM share | default/auto-revoke unstated | doc-gap |
| T4 | Grantee OU/Org-ARN validated service-side (not just `ram:Principal` format) | 2 | `CreateResourceShare` | `ram:Principal` = format check only | doc-gap |
| T5 | Access survives unshare (running instances) | 2 | `DeleteResourceShare` | **confirmed: instances survive, disassociated; new launches blocked** | answered — clean |
| T6 | TOCTOU: launch lands after concurrent unshare | 2 | RAM revoke vs `RunInstances` | revoke "at any time" (admission-time unclear) | doc-gap |
| T7 | Consumer reads owner's instances despite "can't view" promise | 3 | `DescribePlacementGroups`/`DescribeInstances` | server-side ownership filter (no IAM scoping possible) | doc-gap — Critical if true |
| T8 | Enumerate all PGs despite tag/ARN Deny | 3 | `DescribePlacementGroups` | — (blank resource; no scoping possible) | structural gap |
| T9 | `--parent-group-id` links foreign/precision-time parent w/o authz | 4 | `CreatePlacementGroup` | single resource-type row (parent unchecked) | doc-gap |
| T10 | Strategy Deny bypass / stale `precision-time` enum fail-open | 4 | `ec2:PlacementGroupStrategy` | key filters strategy on the acting action | enum stale (doc defect) |
| T11 | Cannot author "launch must use a PG" / "only partition N" | 4 | `RunInstances` PG row (conditional) | — (inexpressible) | structural gap |
| T12 | PG name squat / name-only condition cross-account satisfy | 6 | name-based ARN, `ec2:PlacementGroupName` | CLI requires PG **ID** not name; console bound-list | AWS-mitigated; footgun if `Resource:"*"` |
| T13 | Shared partition/spread 7-per-AZ budget denial | 7 | shared PG limits | limits shared not multiplied | availability (consented share) |
| T14 | `ModifyInstancePlacement` forced stop→modify→start sabotage | 7 | `ModifyInstancePlacement` | requires `stopped`; partition target unscopable | Medium |
| T15 | Outpost cross-tenant co-residency | 8 | Outpost PG | single-tenant owned hardware; no share action | **NULL — refuted** |

## 7. Out-of-Scope Risk Categories
- Single-tenant self-DoS from exhausting one's own spread (≤7/AZ) or partition (≤7) limits.
- Co-residency *within the attacker's own account* (no cross-tenant boundary).
- Outpost placement groups where the Outpost is **customer-owned single-tenant hardware** (self co-residency = OOS) — confirm single vs shared Outpost first.
- Shared responsibility: the EC2 placement engine's internal host-selection logic itself (service plane) — observe/confirm only, never exploit; HARD STOP on service-plane evidence.
- Customer-authored over-broad IAM (footgun). AWS-authored/managed policy weak defaults remain in scope (Lens R/S).

## 8. Null hypotheses / doc gaps (refined after merge)

**Lenses fired:** A (cross-tenant/disclosure-timing — Areas 1/3/4 parent-link), AA (share/revoke completeness — Area 2), U (guarantee-vs-enforcement — Areas 1/2/3), EE (predictable-name land-grab — Area 6), S/X (condition-key scoping / action-family parity — Areas 4/7), V (physical/network segmentation — Area 1), L (resource exhaustion — Area 7), R (sample-policy audit — *could not run*, see below).

**Explicit NULL hypotheses (pages named per skill discipline):**
- **Lens F (translation/injection):** N/A — no parser/translation layer in PG create/share/launch. Pages: `placement-groups.md`, `placement-strategies.md`, `share-placement-group.md`, `cr-cpg.md`.
- **Lens G (SSRF):** N/A — no URL/webhook/callback/endpoint field the service dereferences anywhere in the PG or RAM-sharing flow. Pages: all 6 child pages + `share-placement-group.md` + `list_ram.md`.
- **Lens Q (upload/blob):** N/A — no file/blob/attachment surface.
- **Lens B/C (PassRole / credential-vending):** N/A — PG actions take no role-ARN input; no STS/session-policy/ProvidedContext seam. (CR-sharing uses RAM, not a role the service assumes on the caller's behalf.)
- **Lens D (data→control-plane):** N/A at the API layer — no data-plane process is customer-reachable from a PG; the only control-plane reach of interest is the *placement engine* itself (service plane — observe/HARD-STOP only, Area 1).
- **Lens W (attestation/enclave), FF (JWT):** N/A — no `kms:RecipientAttestation`/PCR/enclave or bearer-JWT scheme; RAM invitation uses native IAM. Pages: `share-placement-group.md`, `list_ec2.md` (PG actions), `list_ram.md`.
- **Lens Outpost cross-tenant (Area 8):** **NULL/refuted** — single-tenant owned hardware, no sharing action in `list_outposts.md`.

**Lens R could NOT run (doc-gap, worth reporting):** `share-placement-group.md`'s "Required permissions" prints only two bare action strings (`ec2:PutResourcePolicy`, `ec2:DeleteResourcePolicy`) with **no sample policy JSON** to audit statement-by-statement — unusual for a RAM-integrated resource. Follow-up: fetch the RAM User Guide generic sharing pages (`working-with-sharing-create.html`) for a generic sample policy that might apply.

**Top open doc-gaps carried for the hunter (priority order):**
1. **(Area 1, HARD STOP)** Is cross-account co-residency in a shared `cluster` PG / CR *confirmable* via topology `nn-` nodes, and does `GroupName`/ARN leak across the CR-only-sharing "no visibility" boundary? Needs a 2-account canary.
2. **(Area 2)** Default of `ram:RetainSharingOnAccountLeaveOrganization` + whether an org-leave auto-revokes a PG share (stranded-grant risk).
3. **(Area 2)** Does RAM validate OU/Org-ARN grantee existence + caller-org-membership service-side (beyond `ram:Principal` format)?
4. **(Area 3)** Does `DescribePlacementGroups`/`DescribeInstances` leak owner-side instances to a consumer despite the "can't view" promise (unscopable → prose-only enforcement)?
5. **(Area 4)** Is `--parent-group-id` on `CreatePlacementGroup` authz-checked against the referenced parent PG's owner?
6. **(Area 2)** TOCTOU: can a consumer `RunInstances` land after a concurrent `DeleteResourceShare`?
7. **(Area 6)** PG name uniqueness-per-account semantics (unconfirmed by the four pages).

**Confirmed negative results (do not re-chase):** `ec2:PlacementGroupStrategy` IS scopable (not an `ec2:InterfaceType`-style inert key) — refuted; `PutResourcePolicy`/`DeleteResourcePolicy` are **Permission-only** (not a directly-callable bypass of RAM's invitation-accept gate) — refuted; unshare is non-destructive (running instances survive) — answered clean; Outpost cross-tenant co-residency — NULL. EC2 and RAM both carry **zero `aws:PrincipalOrgID`/`ResourceOrgID`** keys — confirmed structural (consistent with all prior EC2 plans in this corpus).
