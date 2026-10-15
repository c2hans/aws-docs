# EC2 Instance Topology — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/ec2-instance-topology.html` (+ children `how-ec2-instance-topology-works.html`, `ec2-instance-topology-prerequisites.html`, `ec2-instance-topology-examples.html`), API refs `API_DescribeInstanceTopology.html` / `API_DescribeCapacityReservationTopology.html`, and `service-authorization/.../list_ec2.md` (rows for both actions). Offline mirror == online verified on the load-bearing phrases ("unique per AWS account", "physical host placement", "you can't use it to launch … close") 2026-10-15. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

This is a **read-only observability feature** (two `List`-level `Describe*` APIs). It mints and returns **physical-host-placement node identifiers** (`nn-…`). Its highest-value surface is therefore NOT the usual EC2 mutate/IDOR/PassRole set — it is an **information-disclosure / physical-co-residency-oracle** question layered on top of a **structurally unscopable account-wide read**. Those two facts drive the whole plan.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **DryRun is IAM-only** — it is evaluated *before* resource resolution and is **not** an ownership oracle (reusable corpus caveat). Any "does a foreign ID leak" test must use a real (non-DryRun) call with a synthetic two-account canary.
- **HARD STOP:** the moment any evidence shows a `nn-` node identifier is **stable/comparable across two different AWS accounts** (i.e. the "unique per account" guarantee is defeated and cross-account physical co-residency can be inferred), stop, preserve the two-account evidence pair, and flag for AWS-Security disclosure — that is a cloud-isolation/side-channel-precursor finding, not an ordinary bug. Likewise stop if any node ID, ARN, or account identifier belonging to AWS's own fleet is observed.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Defeat the "unique per AWS account" guarantee** — demonstrate that two accounts observing physically-adjacent capacity can derive the *same* or *correlatable* `nn-` node value, enabling cross-account/cross-tenant physical co-residency detection (side-channel targeting precursor).
2. **Cross-account placement disclosure via RAM-shared Capacity Reservations** — show `DescribeCapacityReservationTopology` on a shared-in CR reveals the *owner's* physical placement (pre-launch).
3. **Ownership-scoping break on `InstanceId.N` / `GroupName.N` / `CapacityReservationId.N`** — show a foreign resource ID returns its topology (or an existence/type/AZ enumeration oracle) rather than being filtered or denied.
4. **Confirm the unscopable-read posture** — show an admin cannot restrict `ec2:DescribeInstanceTopology` to a subset of instances (by tag/ARN), so any grant exposes **all** instances' physical placement account-wide.
5. **Twin-parity** — show the two topology APIs enforce identical ownership and that neither leaks what the other refuses.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** Two SigV4 EC2 query APIs over the standard regional EC2 endpoint (HTTPS). Both are in the public SDK/CLI/PowerShell (`describe-instance-topology` / `Get-EC2InstanceTopology`; `describe-capacity-reservation-topology` / `Get-EC2CapacityReservationTopology`). No console surface ("The AWS Management Console does not support viewing topology"). No data plane, no fleet host, no network listener introduced by this feature — it is a control-plane read of placement metadata.

**The asset being disclosed.** A per-instance / per-CR **network node set**: an ordered list of `nn-XXXXXXXXXXexample` identifiers, one per network-hierarchy layer (3 nodes for most supported types; 4 for `p6-b200.48xlarge`/`p6-b300.48xlarge`; 1–2 partial for CR topology). The *bottom* node = the physical host-adjacent node; shared bottom nodes ⇒ instances are physically close. Also returned: `InstanceId`/`CapacityReservationId`, `InstanceType`, `GroupName` (placement group), `CapacityBlockId`, `ZoneId`, `AvailabilityZone`, `State` (CR only). **The `nn-` value is the crown jewel** — it is a direct, documented proxy for physical location in AWS's network fabric ("physical host placement of your EC2 instances").

**Identifier shape.** `nn-` + opaque body (examples masked as `…example`); real entropy/structure **undocumented — doc-gap, must observe live**. `i-…`/`cr-…` are standard EC2 IDs (checksummed → a *foreign* ID generally cannot be fabricated blind; see Lens A null caveat). `NextToken` is documented only as `"SomeEncryptedToken"` (opaque, server-encrypted).

**Identity / authz.** SigV4 IAM only. Both actions are `Access level: List`, **blank resource-type cell** (no `*required` resource), **sole condition key `ec2:Region`** (confirmed in `list_ec2.md` lines 6978–6982 and 6690–6694; action-index corroboration lines 1928–1932 / 1640–1644). No tag, no ARN, no AZ, no instance-type condition key. Ownership ("your instances" / "your Capacity Reservations", per both API-ref `Default:` sentences) is enforced **only** server-side and implicitly — there is no IAM lever and no resource identifier the caller can scope.

**Supported surface (recon).** Running instances only (DescribeInstanceTopology) / `pending`|`active` CRs only (DescribeCapacityReservationTopology). ~40 HPC/ML/GPU/Trainium instance types. ~30 regions; **CR topology NOT supported in Israel (Tel Aviv) or GovCloud (US-West)** (regional parity gap). Pagination: ≤100/page instances (default 20), ≤10/page CRs (default 10); `MaxResults` mutually exclusive with the IDs parameter.

```
Caller (IAM principal, region R)
   │  ec2:DescribeInstanceTopology / DescribeCapacityReservationTopology  (SigV4, HTTPS)
   ▼
EC2 control plane ── implicit "your instances/CRs" ownership filter (server-side only; NO IAM resource/condition grain beyond ec2:Region)
   │
   ▼
Placement-metadata store ──► returns NetworkNodes[] (nn-… physical-host-placement IDs) + InstanceType + Zone + GroupName + CapacityBlockId
                                           ▲
                            "Each topology view is unique per AWS account"  ← the guarantee under test (Area 1)
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `DescribeInstanceTopology` | SigV4 query | Existing-ish (modern) | **Non-mutating** | External | Return `nn-` node set + placement metadata for *running* instances | Yes (regional EC2 endpoint) | Any principal holding `ec2:DescribeInstanceTopology` (no resource grain) | Blank resource type; only `ec2:Region`. `InstanceId.N` default = "all your instances". `Filter`: availability-zone, instance-type (wildcard `*`/`?`), zone-id. `GroupName.N`. `MaxResults` 1–100. **DryRun = IAM-only.** |
| `DescribeCapacityReservationTopology` | SigV4 query | Modern | **Non-mutating** | External | Return `nn-` node set for *pending/active* CRs (pre-launch placement) | Yes | `ec2:DescribeCapacityReservationTopology` (no resource grain) | Blank resource type; only `ec2:Region`. `CapacityReservationId.N` default = "all your CRs" (max 10). `Filter`: availability-zone, instance-type. `MaxResults` 1–10. Not in IL/GovCloud-W. |

Both are **SDK-public** (so not the "non-SDK under-tested" shape), but both **take resource IDs in the request body with no corresponding IAM resource ARN** — the exact "authz scopes nothing, only server-side existence/ownership guards the ID" shape that Lens A targets. No undocumented/console-hidden auth-weakening knob found (console is unsupported entirely).

---

## 4. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — [HEADLINE] "Unique per AWS account" node IDs vs cross-account physical co-residency oracle (Lens U + Lens A disclosure)
**Background.** The feature's entire purpose is to expose *physical host placement* as `nn-` node identifiers; shared bottom nodes = physically adjacent instances. The docs assert a security property verbatim: **"Each topology view is unique per AWS account."** (`ec2-instance-topology.md` line 31.) The natural reading is that `nn-` IDs are **per-account randomized/salted tokens** so that the *same* physical node yields *different* `nn-` strings in two different accounts — precisely to stop cross-account co-residency inference (the classic "Hey You, Get Off of My Cloud" side-channel precursor).

**Security Concern.** If the guarantee is only *descriptive* ("your view only shows your resources") and the underlying `nn-` values are in fact **globally stable / deterministically derived from physical location**, then two cooperating accounts — or an attacker account vs. a victim account whose instance IDs/placement-group names the attacker can guess or observe — can **compare node sets and detect when their instances land on the same host/rack/spine**. That converts a planning convenience into a **cross-tenant physical-adjacency detector**: the enabling signal for cache/row-hammer/noisy-neighbor side-channel targeting, and for confirming successful co-location after repeated launches.

**High-level Test Scenarios (falsifiable).**
- **Claim:** The same physical node produces the *same* `nn-` value across two accounts. → **Mechanism:** `NetworkNodes[]` are documented as physical-placement identifiers; "unique per account" is prose with no stated salting mechanism. → **Oracle:** In two controlled accounts in the same AZ/region, launch supported-type instances until (via another signal — EFA/SRD latency, placement group, Capacity Block, or simply many launches) two instances are plausibly co-resident; compare their `nn-` bottom-node strings. **Identical (or trivially correlatable) `nn-` across accounts = guarantee defeated = HARD STOP + disclosure.** Distinct, uncorrelated strings for known-adjacent capacity = guarantee holds (genuine null). → **Preconditions:** two accounts, supported instance types, same AZ. → **Cost:** moderate (GPU/HPC instance-hours). → **Severity if true:** **High–Critical** (cross-tenant physical co-residency oracle / isolation-guarantee break).
- **Claim:** `nn-` entropy/structure leaks absolute physical location even within one account (e.g. embeds rack/row, is sequential, or is low-entropy). → **Oracle:** collect many `nn-` values across AZs/zones/types; test for structure, monotonicity, short length, or cross-AZ collisions. Structured/low-entropy IDs weaken Area 1 even without a second account. → **Severity:** Low–Medium (recon enabler) rising to High if it enables cross-account correlation.

**Doc evidence:** `ec2-instance-topology.md` l.31; `how-ec2-instance-topology-works.md` ("physical host placement", NN diagram, shared-node = closeness rule). **Severity-if-true:** **High–Critical.** **Stop condition:** any cross-account `nn-` match → HARD STOP.

### Area 2 — Cross-account placement disclosure via RAM-shared / foreign Capacity Reservations (Lens A + Lens AA)
**Background.** `DescribeCapacityReservationTopology` returns the physical node set for `pending`/`active` CRs **before any instance launches** ("placement of reserved capacity before launching"), and operates on CRs by ID (`CapacityReservationId.N`, default "all your Capacity Reservations"). Capacity Reservations are **RAM-shareable cross-account and cross-Organization** (see `fleet-tutorials-attack-research-plan.md` / `ec2-fleet-on-demand-capacity-reservations.md`; individual CRs are first-class RAM share resources).

**Security Concern.** The API-ref says "your … Capacity Reservations" but **nowhere states whether a RAM-shared-in CR counts as "yours" for topology** nor whether the *owner's* physical placement is redacted when a consumer describes a shared CR. If a shared-in (or otherwise foreign-reachable) CR's topology is returned, a **consumer learns the owner's pre-launch physical placement** — and combined with Area 1 (if node IDs are comparable) this is a direct cross-account co-location primitive against the capacity *owner*, not just a peer.

**High-level Test Scenarios.**
- **Claim:** `DescribeCapacityReservationTopology --capacity-reservation-id <foreign-but-RAM-shared cr-…>` returns the owner's `nn-` set. → **Oracle:** Account A creates a supported-type CR and RAM-shares it to Account B; B calls the API with A's `cr-id`. Non-empty `NetworkNodes` for a CR B does not own = cross-account placement disclosure. → **Severity:** **High** (cross-account), **Critical** if it chains to Area 1 adjacency inference.
- **Claim:** revocation incompleteness — after A **unshares** the CR, B can still describe its topology (stale reference) or a cached/paginated `NextToken` still resolves it. → **Oracle:** unshare, then re-call + replay a prior `NextToken`. → **Severity:** High (surviving cross-account read after revoke; defer the general CR-share lifecycle to the fleet-tutorials plan — this owns only the *topology* leak).

**Doc evidence:** `API_DescribeCapacityReservationTopology` ("your pending or active Capacity Reservations", `Default: Describes all your Capacity Reservations"); CR-sharing surface per `fleet-tutorials-attack-research-plan.md`. **Severity:** High–Critical. **Stop condition:** foreign node set returned → record pair, continue only to confirm, then stop.

### Area 3 — Foreign-ID ownership scoping & enumeration oracle on `InstanceId.N` / `GroupName.N` / `CapacityReservationId.N` (Lens A + Lens A variant: error-differential)
**Background.** All three selectors take caller-supplied identifiers with **no IAM resource grain** (blank resource type). Ownership is enforced only by the implicit server-side "your instances/CRs" filter. `GroupName.N` matches **placement-group names** — human-chosen strings, often low-entropy/guessable (`ML-group`, `HPC-group` in AWS's own examples).

**Security Concern.** Classic "validate existence, not ownership" / differential-error IDOR shape. Even if topology bytes are withheld for foreign resources, the **way** they are withheld can leak: foreign-owned `i-…` vs nonexistent `i-…` vs owned-but-wrong-state may yield different error codes / `InternalError`(500) vs `InvalidInstanceID.NotFound`(400) vs silent-omission(200-empty), forming a **cross-account existence / instance-type / AZ oracle**. `GroupName` matching on a *name* (not ARN) raises the question of whether a name collision across accounts can surface another account's instances.

**High-level Test Scenarios.**
- **Claim:** supplying a *foreign* running `i-…` (supported type) returns its topology. → **Oracle:** B calls `describe-instance-topology --instance-ids <A's i-…>`; non-empty = cross-account disclosure. (Note: real EC2 instance IDs are checksummed → B generally cannot *fabricate* A's ID blind; this test needs A's real ID, which is itself often obtainable — flow logs, shared VPC, logs, prior recon. Treat the checksum as a mitigating factor, not a wall — Lens A embedded-checksum caveat.) → **Severity:** High (cross-account) / informational if cleanly filtered.
- **Claim:** foreign vs nonexistent vs wrong-state IDs are distinguishable (error/latency/empty-set differential) → existence oracle. → **Oracle:** compare responses for (owned-running), (owned-stopped), (foreign-running), (nonexistent), (unsupported-type) IDs; a stable differential = enumeration oracle. → **Severity:** Low–Medium.
- **Claim:** a placement-group **name** collision surfaces another account's instances, or `GroupName` is matched before the ownership filter. → **Oracle:** B creates a placement group with the same name A uses, calls `--group-names`; verify only B's instances appear. → **Severity:** Medium if cross-account leak.

**Doc evidence:** `API_DescribeInstanceTopology` (`InstanceId.N Default: Describes all your instances`, `GroupName.N`), examples 1/2/6. **Severity:** High if cross-account; else Low–Medium oracle. **Stop condition:** any foreign topology byte returned → HARD STOP + disclosure.

### Area 4 — Structurally unscopable account-wide placement read (Lens S + Lens U; intra-account over-exposure)
**Background.** Confirmed in `list_ec2.md`: both actions have a **blank resource-type cell** and **only `ec2:Region`** as a condition key — identical inert-ABAC shape to `DescribeSpotFleetRequests` / `DescribeCapacityReservations` (prior plans). `Access level: List`.

**Security Concern.** An admin **cannot** author a least-privilege policy that restricts topology reads to a *subset* of instances (by `aws:ResourceTag`, instance ARN, AZ, or OU) — the grant is **all-or-nothing per region**. Any principal granted `ec2:DescribeInstanceTopology` (e.g. a monitoring/scheduler role, a read-only "SecurityAudit"-style grant, or anyone with `ec2:Describe*`) can read the **physical placement of every supported-type instance in the account**, across all teams/workloads. For HPC/ML tenants running sensitive co-tenant-sensitive jobs, that is an intra-account information-exposure the account owner has no IAM mechanism to contain. There is no `ec2:ResourceTag`/`ec2:AvailabilityZone` key to even partially scope it.

**High-level Test Scenarios.**
- **Claim:** a scoped role `Allow ec2:DescribeInstanceTopology` + `Deny` on `aws:ResourceTag/team != mine` cannot block foreign-team topology because the key is never evaluated (inert Deny). → **Oracle:** `iam:SimulateCustomPolicy` (safe first oracle, no resources) showing the tag-conditioned Deny does not apply to the action; then a live scoped read returns all teams' instances. → **Severity:** **Low–Medium** (intra-account least-priv footgun). **Classification note:** this is a *structural API limitation AWS owns* (no scoping key exists), reportable as a **Lens-U documented-posture / Informational-to-Low** gap — NOT a customer-authored footgun — but it is only in-scope-reportable to the degree it reflects an AWS design choice; it is NOT cross-account. Keep severity honest.
- **Claim:** `ec2:Region` is the only containment, so SCP/region-deny is the sole governor. → confirm no other key via full `list_ec2` grep. (Done: only `ec2:Region`.)

**Doc evidence:** `list_ec2.md` 6978–6982 / 6690–6694; `ec2-instance-topology-prerequisites.md` IAM-permissions section (lists only the two bare actions, no scoping guidance). **Severity:** Low–Medium.

### Area 5 — Twin-parity between the two topology APIs & the pre-launch window (Lens X)
**Background.** Two sibling actions share the **same `nn-` namespace** and the same unscopable posture, but differ in *phase*: DescribeInstanceTopology (post-launch, running instances, full node set) vs DescribeCapacityReservationTopology (**pre-launch**, pending/active CRs, partial node set). For Capacity Blocks for Ultraservers the CR node set is documented to **match the launched-instance node set exactly**.

**Security Concern.** Divergent-validator / twin-parity: does either API accept a resource ID or reach a node set the other refuses? E.g. does DescribeInstanceTopology enforce ownership identically to DescribeCapacityReservationTopology, or does one have a looser server-side filter? The **pre-launch** CR API is the more dangerous twin for Area 1/2 because it reveals placement *before* any instance exists (no running-instance side-channel needed to confirm). And the Ultraserver "CR node set == instance node set" equivalence means a *pre-launch* leak is as precise as a post-launch one for those types.

**High-level Test Scenarios.**
- **Claim:** one API returns a node set for a resource/state the other denies (validator divergence). → **Oracle:** cross-feed IDs and states (e.g. a CR in a state each treats differently) and diff the ownership/error behavior. → **Severity:** Low–Medium (parity gap), High if the looser twin crosses an account boundary.
- **Claim:** the CR-topology regional gap (not in IL/GovCloud-W) means a detection/governance control built on topology reads is silently absent there. → **Oracle:** doc-confirmed; note for defenders. → **Severity:** Informational.

**Doc evidence:** `how-ec2-instance-topology-works.md` differences table; prerequisites regional list. **Severity:** Low–Medium.

### Area 6 — Chained primitive: observe (topology) + influence (CR-in-CPG) → iterative co-location (Lens U guarantee-vs-mechanism + kill-chain)
**Background.** The docs explicitly disclaim: **"you can't use it to launch a new instance physically close to an existing instance. To influence instance placement, you can create Capacity Reservations in cluster placement groups"** (`ec2-instance-topology.md` l.33, linking `cr-cpg.md`).

**Security Concern.** The disclaimer is advisory about *this feature in isolation*, but the **feature set as a whole supplies both halves of a co-location loop**: (observe) topology reveals where capacity/instances sit; (influence) CR-in-CPG + repeated launches push new capacity toward a target node; (confirm) topology re-read detects a shared bottom node. Within one account this is benign self-optimization. **Across accounts, chained with Area 1 (if `nn-` is comparable) and Area 2 (shared-CR placement leak), it becomes a guided cross-tenant co-residency attack**: read victim-adjacent placement → launch/reserve toward it → confirm co-location via matching `nn-`.

**High-level Test Scenarios.**
- **Claim:** iterating {describe-topology → create CR in CPG / launch → re-describe} measurably increases the rate of landing on a *target* node. → **Oracle:** in-account first (benign), measuring convergence to a chosen `nn-`; only escalate cross-account if Area 1 shows comparable IDs (and then it is HARD STOP). → **Severity:** rated at the **end** of the chain: Critical if cross-account co-location is confirmed; otherwise out-of-scope self-placement.

**Doc evidence:** `ec2-instance-topology.md` l.33 + `cr-cpg.md`. **Severity:** Critical-if-cross-account; else out of scope. **Stop condition:** cross-account convergence → HARD STOP.

### Area 7 — `NextToken` ("SomeEncryptedToken") integrity & scoping (Lens M, lower priority)
**Background.** Pagination token documented only as an opaque server-encrypted string; `MaxResults` is mutually exclusive with the IDs parameter.
**Security Concern.** If the token encodes caller/account/filter scope and is not integrity-bound to the principal, a token issued in one context might be replayed to continue enumeration across a boundary or to resume a query whose filter the server would now reject.
**Test Scenarios.** **Claim:** a `NextToken` from principal/account A, replayed by B (or after a filter/scope change), continues A's result stream. → **Oracle:** capture a `NextToken`, replay under a different principal/account/filter; any cross-context continuation = scoping break. → **Severity:** Medium if it crosses a tenant boundary; otherwise Informational. **Likely a genuine null** (AWS pagination tokens are typically principal-bound and integrity-protected) — doc-gap, confirm cheaply.

---

## 5. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account physical co-residency inference via comparable `nn-` IDs | DescribeInstanceTopology / `NetworkNodes` | "Each topology view is unique per AWS account" (prose only — trace to the salting/randomization mechanism) |
| Owner's pre-launch placement leaked to a RAM-shared-CR consumer | DescribeCapacityReservationTopology | "your … Capacity Reservations" implicit ownership filter (no stated shared-CR behavior) |
| Foreign `i-…`/`cr-…`/placement-group-name returns topology or an existence oracle | both APIs, ID selectors | implicit server-side "your instances/CRs"; EC2 ID checksum (mitigating, not a wall) |
| Admin cannot scope topology reads to a subset of instances → account-wide placement exposure | IAM `list_ec2` rows | **none** — blank resource type, only `ec2:Region` |
| Validator/ownership divergence between the two topology twins | both APIs | shared `nn-` namespace; different phase/state preconditions |
| Observe+influence co-location loop (topology + CR-in-CPG) | feature set | "you can't use it to launch close to an existing instance" (advisory disclaimer) |
| `NextToken` replay across principal/account/filter | pagination | opaque "SomeEncryptedToken" (assumed principal-bound) |

---

## 6. Out-of-Scope Risk Categories
- **Single-account self-placement / self-optimization** — a tenant observing and optimizing *its own* workload proximity is the feature's intended use (in-scope only when it crosses to another account per Area 1/2/6).
- **IMDS, host-level side channels, and the shared Nitro/host substrate itself** — the *mechanism* of a cache/rowhammer side-channel is shared-infra and out of scope; this plan covers only the **topology-metadata disclosure that would make such targeting possible**, not the microarchitectural exploit.
- **Pagination/`MaxResults` resource-exhaustion / self-DoS** — single-tenant, Low/out-of-scope.
- **Standard EC2 endpoint TLS/SigV4** — no feature-specific transport surface introduced (Lens Y null, below).
- The general **Capacity Reservation RAM-share lifecycle** (grant/consume/billing/org-leave) — owned by `fleet-tutorials-attack-research-plan.md` and the CR siblings; this plan touches it only through the *topology* leak (Area 2).

---

## 7. Null hypotheses / doc gaps (pages checked)

Pages read for trigger sweeps: `ec2-instance-topology.md`, `how-ec2-instance-topology-works.md`, `ec2-instance-topology-prerequisites.md`, `ec2-instance-topology-examples.md`, both API-ref pages, and the two `list_ec2.md` action rows.

- **Lens B / C (PassRole / credential vending) — NULL.** No role ARN, no `PassRole`, no STS/session, no credential field anywhere; both actions are read-only `List`.
- **Lens G (SSRF) — NULL.** No field the service dereferences/fetches/renders; no `*Url`/`*Uri`/webhook/import. Checked all three UG pages + API refs.
- **Lens F (translation/injection) — NULL.** No parser/translator/wire-protocol/query-builder; filters are fixed enums (availability-zone/instance-type/zone-id) with `*`/`?` wildcard matching only (server-side glob, not a query language).
- **Lens Q (upload) — NULL.** No upload/blob/image/attachment field.
- **Lens K (prompt injection) — NULL.** No LLM/agent/GenAI in the path.
- **Lens P (proofing/registration) — NULL.** No registration/verification/OTP/uniqueness gate; read-only feature.
- **Lens H / W (KMS / attestation) — NULL.** No CMK, encryption context, or attestation condition keys for these actions (`NextToken` is server-encrypted but opaque to the caller — see Area 7).
- **Lens J / FF (OAuth / JWT) — NULL.** SigV4 only; no token validation surface.
- **Lens T (cross-service secret) — NULL.** Feature generates/persists no secret.
- **Lens I (tagging/ABAC) — NULL (and it's the point).** These actions carry **no tag condition key at all** — covered as the *absence* lead in Area 4, not as a tagging-mutation surface.
- **Lens Y (transport/sig) — NULL.** Standard regional EC2 HTTPS/SigV4; no `http://`, no documented internal hop, no SigV2 acceptance specific to this feature.
- **Lens V (network segmentation) — NULL as a reachability surface.** The feature *describes* network topology but introduces no ENI/listener/segment the caller can reach; the co-residency angle is information-disclosure (Area 1), not L3/L4 reachability.
- **Lens D / N / BB / CC / DD / EE — NULL.** No control-plane host reachable from a data path (no data path); no namespace migration/dual-ARN; no multi-parser/authorizer/cache/CDN layer; no predictable-name resource the service creates/resolves (read-only).
- **Lens AA — partial, deferred.** CR-share revocation completeness touched only via Area 2; the general share lifecycle is owned by the fleet-tutorials/CR plans.
- **Lens O (audit) — Informational.** Both actions are CloudTrail management events logged by default, so topology *reads* are auditable; but there is **no distinct signal** separating legitimate topology use from co-residency reconnaissance (Area 1/6 probing looks like ordinary `Describe*` traffic) — a detection blind spot, enabler-only.

**Primary doc gaps the hunter must close live (ranked):**
1. **`nn-` cross-account comparability + entropy/structure** — the load-bearing unknown for Area 1 (and thus 2/6). The docs assert "unique per account" but never describe the salting/randomization mechanism. *This is the single most important thing to resolve, and the HARD-STOP trigger.*
2. **Shared-in / foreign CR topology behavior** — is a RAM-shared CR "yours" for `DescribeCapacityReservationTopology`, and is the owner's placement redacted? (Area 2.)
3. **Foreign-instance-ID / placement-group-name handling** — filtered vs denied vs error-differential (Area 3).
4. **`NextToken` principal/account/filter binding** (Area 7) — likely null, confirm cheaply.
5. **Twin ownership-validator parity** between the two APIs (Area 5).
