# EC2 Instance Topology — Examples Page — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology-examples.html` (offline twin `docs/AWSEC2/latest/UserGuide/ec2-instance-topology-examples.md`, 704 lines, offline==online verbatim 2026-10-15). IAM facts cross-checked against `docs/service-authorization/latest/reference/list_ec2.md` (operation rows ~5133 `DescribeCapacityReservationTopology`, ~5805 `DescribeInstanceTopology`). Status: documentation-derived hypotheses only; nothing tested against a live account.

> **This is a PAGE-LEVEL CHILD / THIN COMPLEMENT** of the three existing topology plans. It is a CLI reference/demonstration page — **no new API, no new IAM artifact, no new trust boundary.** It exists to (a) make the parent plan's abstract read-oracle concrete by cataloguing the exact response fields and the request-filter targeting surface, and (b) supply the concrete demonstration evidence for the how-works plan's pre→post-launch node hypotheses. It **defers all core boundary leads** to its siblings and must not re-run them:
> - **`ec2-instance-topology-attack-research-plan.md`** (the feature/API PARENT) — owns A1 cross-account `nn-` co-residency oracle (HARD STOP), A2 RAM-shared-CR pre-launch leak, A3 foreign-ID/error-differential oracle, A4 no-IAM-scoping-grain, A5 twin-parity + partition availability, A6 observe→influence→confirm co-location kill chain, A7 NextToken replay.
> - **`how-ec2-instance-topology-works-attack-research-plan.md`** (mechanism child) — owns W1 published proximity-inference algorithm (co-residency confirmation oracle), W2 intra-account `nn-` stability/join-ability across both APIs + pre→post-launch, W3 bottom host node withheld pre-launch (launch = resolve step).
> - **`ec2-instance-topology-prerequisites-attack-research-plan.md`** (prereqs child) — owns P1 managed-policy over-grant (ReadOnlyAccess/SecurityAudit already grant both), P2 node-COUNT generation oracle, P3 state gate (`running`/`pending`/`active`), P4 GovCloud/Israel partition split.
>
> This plan cross-references those areas; it does **not** restate them.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows a `nn-` node string is comparable/stable **across two different AWS accounts** (i.e. the parent-A1 cross-tenant co-residency oracle is real), stop, preserve evidence, flag for AWS-Security disclosure. This page cannot settle that (its `nn-...example` IDs are placeholders) — it only sharpens the targeting that would exploit it.
- Everything in this plan is **intra-account read-only disclosure / targeting-refinement** unless chained into parent A1. On its own it is **Low–Informational**; it inherits parent severity when chained.

## 1. Pentest Objectives
1. Catalogue the **exact disclosure payload** a `DescribeInstanceTopology` / `DescribeCapacityReservationTopology` caller receives, so the parent plan's "read oracle" has a concrete field inventory to reason about (what physical-placement + metadata a read-only principal exfiltrates account-wide).
2. Map the **request-filter / parameter surface** (`--instance-ids`, `--group-names`, `--filters Name=instance-type`, `Name=zone-id`, `--capacity-reservation-id`, `--max-results`) and confirm that **none of these slicing dimensions has a corresponding IAM condition key** — i.e. rich *targeting* with zero *authorization grain* (deepens parent A4/A6).
3. Harvest the **concrete demonstration evidence** the page provides for how-works W2/W3: the pre-launch CR topology (2 nodes) vs post-launch instance topology (3 nodes) node-count delta, and the shared-`nn-` join pattern.

## 2. Components, Assets, and Design
- **Interface:** two read-only EC2 CLI/API calls (`describe-instance-topology` / `Get-EC2InstanceTopology`; `describe-capacity-reservation-topology` / `Get-EC2CapacityReservationTopology`). No mutation. Both support `--region` (or default region) and pagination.
- **Response field inventory (the disclosure payload — net-new concrete catalogue):**
  - **Instance topology** (`Instances[]`): `InstanceId`, `InstanceType`, `GroupName` (the customer's **placement-group name**, present only when the instance is in one — e.g. `ML-group`, `HPC-group`), `NetworkNodes[]` (the **ordered `nn-` physical-placement hierarchy**, leaf→spine), `CapacityBlockId` (`"null"` in every example; non-null links the node to a prepaid Capacity Block for ML), `ZoneId` (physical zone id, e.g. `usw2-az2`), `AvailabilityZone` (account-mapped AZ name, e.g. `us-west-2a`).
  - **CR topology** (`CapacityReservations[]`): `CapacityReservationId`, `CapacityBlockId`, `State` (`active` in examples), `InstanceType`, `NetworkNodes[]`, `AvailabilityZone`. **No `GroupName`, no `ZoneId`** on the CR shape.
  - `NextToken: "SomeEncryptedToken"` on every page.
- **Request-filter surface (the targeting knobs):** `--instance-ids`, `--group-names` (placement-group names), `--capacity-reservation-id`, `--filters Name=instance-type` (exact `trn1n.32xlarge` **or** wildcard family `trn1*`/`p4d*`), `--filters Name=zone-id` (AZ `use1-az1` **or** Local Zone `use1-atl2-az1`), combinable; `--max-results` (default 20, max 100).
- **Owners / boundary:** single-account. The read returns the **caller's own** account resources; the filters narrow *what is returned*, they do **not** widen *what is authorized*. No service-account/data-plane component is introduced by this page.

## 3. API / Interface Inventory
| Name | Method | Mutating | Ext-facing | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `DescribeInstanceTopology` | GET-style read | No | Yes (SDK/CLI) | Yes (SigV4) | any principal with `ec2:DescribeInstanceTopology` | **blank resource-type + only `ec2:Region`** (list_ec2 row ~5805) — unscopable account-wide (parent A4). Filters here are request params, NOT condition keys. |
| `DescribeCapacityReservationTopology` | read | No | Yes | Yes | `ec2:DescribeCapacityReservationTopology` | **blank resource-type + only `ec2:Region`** (row ~5133). Returns pre-launch (`pending`/`active`) placement (parent A2/A5). |

Both actions are **Access level: List**, no `aws:RequestTag`/`ResourceTag`/ARN/instance-id resource scoping (confirmed by the parent plan against list_ec2).

## 4. Recommended Areas of Focus

### Area E1 — [HEADLINE] Rich request-filter targeting over a zero-grain authz surface (Lens U / A / S)
**Background:** The page documents five independent ways to **slice** the topology read — by explicit instance/CR id, by placement-group name, by exact instance type, by instance-family wildcard (`trn1*`, `p4d*`), and by physical zone id (AZ or Local Zone) — all combinable in one call (Examples 1–7). This is a full targeting console.
**Security Concern:** Every one of these slicing dimensions is a **request filter, not an IAM condition key.** The parent plan already established the two actions carry **only `ec2:Region`** and a blank resource-type cell. So an administrator can neither (a) restrict *which* instances/zones/families a grantee may read, nor (b) deny reads of the high-value GPU/ML families specifically — yet the API *itself* hands the grantee a precise filter to isolate exactly those (`Name=instance-type,Values=p4d*` + `Name=zone-id,Values=use1-az1`). The filter surface converts the parent's "unscopable account-wide read" (A4) and "observe step" (A6) from a blunt dump into a **point-and-shoot physical-placement recon tool for the account's most sensitive clusters** (p4d/p5/trn1/trn2 = ML/HPC training fleets).
**High-level Test Scenarios:**
- Claim: *No IAM condition key exists that can restrict a `DescribeInstanceTopology` grantee to a subset of instance types, families, zones, or placement groups* → Oracle: `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` showing a Deny keyed on `ec2:InstanceType`/`ec2:AvailabilityZone`/`ec2:PlacementGroup` is **inert** against `DescribeInstanceTopology` (the keys are real for `RunInstances` but absent from the topology action's condition set — the Lens-S "condition-key that does not apply to this action" failure shape). No resources touched.
- Claim: *A read-only/auditor principal (ReadOnlyAccess, SecurityAudit — see prereqs P1) can single-call enumerate the physical `nn-` placement of only the account's GPU training instances in one AZ* → Oracle: with a scoped canary role holding exactly `ec2:DescribeInstanceTopology`, run `--filters "Name=instance-type,Values=p4d*,p5*,trn1*,trn2*" "Name=zone-id,Values=<az>"` and confirm it returns the `NetworkNodes[]` hierarchy for matching instances.
**Doc evidence:** Examples 3a/3b/3c (`instance-type` exact + `trn1*`/`p4d*` wildcard), 4a/4b/4c (`zone-id` AZ + Local Zone), 5 (combined); list_ec2 rows ~5133/~5805 (only `ec2:Region`).
**Severity-if-true:** Low–Medium intra-account (targeting amplifier); becomes the practical front-end of parent A6 → inherits A1 High–Critical the instant cross-account `nn-` comparability holds. **Reportable as an AWS-owned structural limitation** (no scoping grain for a placement-disclosing read) under Lens U/A4.

### Area E2 — Concrete response-field disclosure catalogue (Lens A — disclosure payload)
**Background:** The examples are the authoritative statement of **what fields the read returns.** Net-new beyond the hub's prose: the response discloses the customer's **placement-group name** (`GroupName`), the **`CapacityBlockId`** linkage to prepaid Capacity-Block (ML GPU) reservations, the full ordered **`NetworkNodes[]`** hierarchy, `ZoneId`, and (CR shape) `State`.
**Security Concern:** This is the exact data a principal denied every *other* EC2 describe might still read if granted only the topology action — it ties together: physical placement (`nn-`), logical grouping (`GroupName` placement group), capacity-commitment identity (`CapacityBlockId`), and zone. `GroupName` disclosure is itself a minor info-leak (reveals the account's cluster-naming / workload taxonomy to a read-only grantee); `CapacityBlockId` non-null would cross-link topology to the Capacity-Blocks-for-ML billing surface (cross-ref `fleet-tutorials` Capacity-Block area).
**High-level Test Scenarios:**
- Claim: *The response leaks `GroupName` (placement group) and `CapacityBlockId` to a principal holding only the topology action, even one denied `ec2:DescribePlacementGroups`/`ec2:DescribeCapacityReservations`* → Oracle: scoped canary role with only `ec2:DescribeInstanceTopology` (+ explicit Deny on the other describes) still receives populated `GroupName`/`CapacityBlockId` fields.
- Note the **inconsistency** (doc-only, not a bug): the same instance `i-2222...` is shown **with** `GroupName:"HPC-group"` in Ex1/Ex2 but **without** `GroupName` in Ex3a/3b/3c/4a/5 — i.e. the field is present only when the instance is actually in a placement group; do not read the omission as a security control.
**Doc evidence:** Ex1 lines 62/75 (`GroupName`), 68/81 (`CapacityBlockId`), 63–66 (`NetworkNodes`); Ex6 lines 616–633 (CR `State`/`CapacityReservationId`).
**Severity-if-true:** Low–Informational (intra-account read-only metadata disclosure); feeds parent A1/A2 payload definition.

### Area E3 — Demonstration evidence for how-works W2/W3 (pre→post-launch node delta + nn- join)  [SUPPLY, not a new boundary]
**Background:** The examples **concretely show** what the how-works plan could only hypothesize:
- **CR topology (pre-launch) returns 2 `NetworkNodes`** for `p5.48xlarge`/`p5en.48xlarge` (Ex6 lines 621–622/632–633; Ex7 683–684), while **instance topology (post-launch) returns 3 `NetworkNodes`** (Ex1/Ex3b/etc.). This is the documented, in-example demonstration of **how-works W3**: the bottom host-adjacent node is withheld until an instance launch resolves it (CR = 2 upper nodes; running instance = 3 nodes incl. the leaf). The exact precision gain from launching is now quantified: **+1 leaf node.**
- The same `nn-1111111111example` + `nn-2222222222example` pair is **shared** across `i-1111` (p4d, ML-group) and `i-2222` (trn1n, HPC-group) — different types, different placement groups, same upper spine (Ex1) — and the identical top pair recurs in the CR topology output (Ex6) and across regions in different examples. This is the in-example demonstration of **how-works W2** (`nn-` strings join across instances/types/groups/APIs within an account).
**Security Concern:** None net-new — these are placeholder (`...example`) IDs, so the page is **illustrative, not evidential**; it cannot settle whether real `nn-` strings are per-account-salted (parent A1 holds) or globally stable (parent A1 breaks). Its value is giving the hunter the **exact assertion to reproduce** against live canaries.
**High-level Test Scenarios (reproduce under how-works W2/W3, do not re-derive):**
- Launch a canary into a CR, read CR topology (expect N nodes), then read instance topology post-launch (expect N+1 nodes, with the first N byte-identical) → confirms W3 resolve-step + W2 intra-account stability. Negative control: re-read the same instance twice, assert byte-identical `NetworkNodes[]`.
**Doc evidence:** Ex6/Ex7 (2-node CR) vs Ex1/Ex3 (3-node instance); shared `nn-` across Ex1 instances and into Ex6.
**Severity-if-true:** N/A on its own (demonstration). Inherits parent A1 (HARD STOP) / how-works W2/W3.

### Area E4 — Pagination / NextToken  [THIN POINTER → parent A7]
`--max-results` default 20, max 100; `NextToken:"SomeEncryptedToken"` on every page. The opaque token's integrity/replay/cross-account-reuse question is **owned by parent A7** — do not re-open here. Only net-new note: the **100-per-page ceiling + NextToken paging** means a full-account placement sweep is a bounded, cheap loop (reinforces E1's "practical recon tool" framing; no rate/scoping control documented on the page).

### Area E5 — Local Zone topology exposure (Lens U — surface breadth)
**Background:** Ex4b/Ex4c show `zone-id` filtering on a **Local Zone** (`use1-atl2-az1` → `us-east-1-atl-2a`) returning full `NetworkNodes[]`. Topology disclosure therefore extends to Local Zone placements, not just standard AZs.
**Security Concern:** Minor breadth note — the physical-placement read oracle covers Local Zones too, which are smaller/more-isolated footprints where co-residency inference (parent A1/A6) is correspondingly higher-signal (fewer hosts). No new mechanism; sharpens parent A1 severity for Local-Zone workloads.
**Doc evidence:** Ex4b lines ~340–360 (`Values=use1-atl2-az1`), Ex4c.
**Severity-if-true:** Informational; parent-A1 severity amplifier for Local-Zone fleets.

## 5. Prioritization
E1 (filter-targeting over zero authz grain) is the one net-new, independently reportable lead (AWS-owned structural scoping gap, Lens U/A4). E2 (disclosure catalogue) and E3 (W2/W3 demonstration) are **supply/settle** inputs to the parent and how-works plans — valuable context, not new boundaries. E4/E5 are pointers/amplifiers. Nothing here outranks the parent's A1 cross-account HARD-STOP question, which remains the only Critical-tier lead in the cluster.

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Grantee isolates GPU/ML cluster placement by family+zone in one call | `DescribeInstanceTopology` filters | **No IAM condition key** for type/zone/group (only `ec2:Region`) — mitigation absent (E1) |
| Read-only auditor exfiltrates placement-group names + CapacityBlock linkage | response `GroupName`/`CapacityBlockId` | None at field level; relies on withholding the action entirely (E2, prereqs P1) |
| Pre-launch placement precision = 2 nodes; launch adds leaf (3 nodes) | CR vs instance topology | "Visibility of additional nodes requires an instance launch" (how-works W3) — advisory, not a control (E3) |
| Full-account placement sweep via 100/page + NextToken loop | pagination | No documented rate/scope control (E4 → parent A7) |

## 7. Out-of-Scope Risk Categories
- The cross-account `nn-` comparability question (parent A1) — referenced, not tested here (needs two-account canary; placeholder IDs on this page can't settle it).
- `nn-` entropy/stability mechanism, co-residency confirmation algorithm — how-works W1/W2.
- Managed-policy over-grant (ReadOnlyAccess/SecurityAudit grant both actions) — prereqs P1.
- `ZoneId`/`AvailabilityZone` disclosure as *such* — AZ granularity is publicly mappable via `DescribeAvailabilityZones`; the fine-grained signal is the `nn-` set, not the zone (how-works carve-out). The zone-id **filter** is in scope only as a *targeting* amplifier (E1/E5), not as a disclosure.
- Capacity-Block billing/consume surface — `fleet-tutorials` Capacity-Blocks plan (only the `CapacityBlockId` field *linkage* is noted here).
- NextToken opaque-token integrity/replay — parent A7.

## 8. Null hypotheses / doc gaps
- **Lenses B/C/D/E/F/G/H/J/K/M/N/O/Q/T/V/W/Y/AA/BB/CC/DD/EE/FF — NULL.** Pages checked: this examples page in full (704 lines) + the three sibling plans' coverage. Rationale: the page introduces **no role ARN / PassRole (B/C), no control-plane hop (D), no translation layer or parser (F), no server-side-dereferenced field (G — the filter values are matched internally, never fetched), no KMS/encryption context (H), no OAuth/3P (J), no LLM (K), no shared session id (M), no new/legacy namespace (N — the two actions are the only namespace), no upload/rich content (Q), no persisted secret (T), no network segmentation primitive (V), no attestation gate (W), no http:// endpoint or signature-version choice (Y), no share/revoke lifecycle (AA), no multi-parser request path (BB), no upstream-context header (CC), no caching layer (DD), no predictable-name resolution (EE), no token/claims validation (FF).**
- **Lens I (tagging/ABAC) — NULL-as-the-point:** the response surfaces no tags and the actions accept no tag condition key (parent A4) — the *absence* is the finding, already owned by parent A4 (and refined here as E1).
- **Lens L (DoS) — NULL / out-of-scope:** `--max-results` ≤100 + pagination is a self-paced read; no documented shared-fleet exhaustion vector from this read-only page.
- **Lens S partial-fire (E1):** the specific failure shape is "a condition key that *could* apply (`ec2:InstanceType`/`ec2:AvailabilityZone` exist for other EC2 actions) does **not** apply to this action," so a Deny written against it is inert — covered under E1.
- **Lens U primary-fire (E1/E5):** "the output includes only the instances that match…" prose is a statement about *response filtering*, not *authorization* — the guarantee the operator might read into the filter grammar (that they can constrain a grantee) does not exist. Confirmed.
- **Doc gaps carried for the hunter:** (1) non-null `CapacityBlockId` field format and whether it is readable to a topology-only principal denied the Capacity-Reservations describes (E2); (2) exact `NetworkNodes[]` ordering semantics (leaf-first vs spine-first) — examples imply shared *leading* nodes = shared spine, but the page does not state the order (defer to how-works node-hierarchy semantics); (3) whether `describe-capacity-reservation-topology` supports the `zone-id`/`group-names` filters (page only demonstrates `instance-type` + id for CRs — asymmetry with the instance call; untested whether the CR call rejects or silently ignores a `zone-id` filter).

---
*Child of the EC2 Instance Topology cluster. Siblings: `ec2-instance-topology-attack-research-plan.md` (parent), `how-ec2-instance-topology-works-attack-research-plan.md`, `ec2-instance-topology-prerequisites-attack-research-plan.md`. offline==online verified 2026-10-15.*
