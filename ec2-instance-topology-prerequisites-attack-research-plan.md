# EC2 Instance Topology — PREREQUISITES — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/ec2-instance-topology-prerequisites.html` (the single target page) + its IAM-permissions / instance-type / state / region sections; cross-referenced to `service-authorization/.../list_ec2.md` (both topology action rows) and the AWS-managed-policy reference (`aws-managed-policy/latest/reference/*`). Offline mirror `docs/AWSEC2/latest/UserGuide/ec2-instance-topology-prerequisites.md` == online verified byte-for-byte (modulo frontmatter) 2026-10-15. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

## Relationship to the hub plan (READ FIRST — this is a COMPLEMENT, not a duplicate)
This page is one of the children of `ec2-instance-topology.html`, whose hub plan is **`ec2-instance-topology-attack-research-plan.md`** (same directory). That hub plan already OWNS and fully develops the feature's crown-jewel surface:
- **Hub Area 1** — the `nn-` "unique per AWS account" guarantee vs cross-account physical **co-residency oracle** (HARD STOP trigger).
- **Hub Area 2** — cross-account placement disclosure via **RAM-shared / foreign Capacity Reservations**.
- **Hub Area 3** — foreign-ID ownership scoping & **error-differential IDOR** on `InstanceId.N` / `GroupName.N` / `CapacityReservationId.N`.
- **Hub Area 4** — the structurally **unscopable account-wide read** (blank resource type, only `ec2:Region`) as a `list_ec2` fact.
- **Hub Area 5** — twin-parity between the two topology APIs.
- **Hub Area 6** — the observe+influence (topology + CR-in-CPG) **co-location kill chain**.
- **Hub Area 7** — `NextToken` ("SomeEncryptedToken") integrity/scoping.

**This prerequisites plan DEFERS all of the above to the hub** and owns ONLY the net-new surface that the *prerequisites page itself* introduces as a document — the **eligibility matrix** (region / instance-type / state) and the **"Required IAM permissions" instruction block**, analysed as attacker-usable recon oracles and as an AWS-authored permissions artifact. Where a lead here touches a hub area, it is marked `→ hub Area N` and only the prerequisites-page-specific *delta* is developed.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **DryRun is IAM-only** — evaluated before resource resolution; NOT an ownership oracle (reusable corpus caveat). Any "foreign ID leaks" test needs a real two-account canary call.
- **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` is the safe first oracle** for every IAM lead here (no resources touched, no placement data read).
- **HARD STOP (inherited from the hub):** the moment any evidence shows a `nn-` node identifier is stable/comparable across two different AWS accounts, or any node ID / ARN / account identifier belonging to AWS's own fleet is observed — stop, preserve the evidence pair, flag for AWS-Security disclosure. This plan's recon oracles (P2/P3) are *enablers* for that hub finding; treat a confirmed cross-account placement byte the same way.

---

## 1. Pentest Objectives (concrete outcomes specific to the prerequisites surface)
1. **Show the "Required IAM permissions" instruction understates reach** — demonstrate that account-wide physical-host-placement disclosure is already granted to principals the page never mentions (any holder of a common read-only / security-audit managed policy), and that no least-privilege scoping of the two actions is possible beyond a region Deny or a named-action Deny.
2. **Weaponize the eligibility matrix as recon** — show that the documented instance-type→network-node-**count** map (3 vs 4 nodes) and the supported-type fence turn a topology response (self or, if the hub leaks fire, foreign) into an **instance-generation oracle** (is this top-tier `p6-b200/b300` Blackwell capacity?).
3. **Sharpen the state/phase oracle** — use the documented state gating (`running` / `pending`|`active`) to refine the hub's foreign-ID error-differential and to pin the **earliest pre-launch placement disclosure window** (a `pending` CR).
4. **Expose the regional-parity governance gap** — show that a CR-topology-based placement-monitoring control is silently absent in Israel (Tel Aviv) and GovCloud (US-West), and that the surface extends into sovereign/government partitions (ESC Germany, GovCloud).

---

## 2. Components, Assets, and Design (delta over the hub)
This page adds no new component, interface, host, network path, parser, upload, token, or role. It is a **static eligibility + permissions reference** for the two read-only topology APIs the hub plan already modelled. The only "assets" it introduces to an attacker are **four pieces of documented ground truth**:

- **The required-permissions set** = exactly `ec2:DescribeInstanceTopology` + `ec2:DescribeCapacityReservationTopology`, stated with **no sample policy, no `Resource`/`Condition` guidance, no warning** about account-wide scope or physical-placement sensitivity.
- **The supported-type → node-count map** (the eligibility fence AND a type oracle):
  - **3 network nodes:** all supported `g6e.*`, `g7e.*`, `hpc6a/6id/7g/7a/8a.*`, `p3dn/p4d/p4de/p5/p5e/p5en.*`, `p6e-gb200.36xlarge`, `trn1/trn1n/trn2/trn2u.*` (~38 types).
  - **4 network nodes:** `p6-b200.48xlarge` | `p6-b300.48xlarge` (the only two) — so **4 nodes = Blackwell B200/B300**.
  - CR-topology node count "**varies depending on the type and state** of the Capacity Reservation" (not fixed).
- **The state gate:** instances must be `running`; CRs must be `pending` or `active`; "**You can't get topology information for instances or Capacity Reservations in any other state.**"
- **The region fence:** ~30 regions incl. **AWS GovCloud (US-West)** and **AWS European Sovereign Cloud (Germany)**; **`DescribeCapacityReservationTopology` is NOT supported in Israel (Tel Aviv) and GovCloud (US-West)**; instance-type availability "varies by Region."

`list_ec2.md` confirmed verbatim 2026-10-15 for BOTH actions: **Resource types (\*required): (blank)**, **Condition keys: `ec2:Region`** (sole key), **Access level: List** (DescribeCapacityReservationTopology ≈ offline line 6690/1640; DescribeInstanceTopology ≈ 6978/1928). No `aws:ResourceTag`, no ARN key, no instance-type/AZ/state key.

```
Prerequisites page  ─────────────────────────────────────────────┐
  ├─ "Required IAM permissions"  = 2 bare actions, no scoping      │  (Area P1: AWS-authored
  │        │ reachable ALSO via ReadOnlyAccess / SecurityAudit /   │   permissions artifact,
  │        │ AmazonEC2ReadOnlyAccess / ViewOnlyAccess / EC2FullAccess / Admin — all Resource:"*")
  ├─ Instance-type list → 3 vs 4 node-count ───────► type/generation oracle   (Area P2)
  ├─ State gate (running / pending|active) ────────► existence+phase oracle   (Area P3)
  └─ Region fence (incl. GovCloud-W, ESC-Germany; CR-topo absent in IL/GovCloud-W)  (Area P4)
                                   │
                                   ▼  (all feed the hub's co-residency core)
            ec2-instance-topology-attack-research-plan.md  (Areas 1/2/3/5/6/7)
```

---

## 3. API / Interface Inventory
No new API. The two actions are inventoried in the hub plan §3. The prerequisites page contributes only the **preconditions** on those two actions (region/type/state) and the **permissions instruction** — see Areas below. No console surface, no non-SDK/hidden knob (the console does not support topology at all).

---

## 4. Recommended Areas of Focus (priority order; all net-new to this page)

### Area P1 — [HEADLINE] The "Required IAM permissions" block as an AWS-authored instruction that grants an unscopable, account-wide physical-placement read — and badly understates who already holds it (Lens R / Lens U / Lens S)
**Background.** The prerequisites page's **IAM permissions** section is the canonical "what you must grant" artifact for this feature. It says, in full: *"Your IAM identity (user, user group, or role) requires the following permissions: `ec2:DescribeInstanceTopology`, `ec2:DescribeCapacityReservationTopology`."* There is **no sample policy, no `Resource` line, no `Condition`, and no note** that these actions return physical host placement (`nn-` node IDs) for **every** supported-type instance/CR in the account, or that they cannot be scoped below the region level. The sibling `how-ec2-instance-topology-works.md` is where the "physical host placement" sensitivity is spelled out — this page omits it entirely.

**Security Concern.** Two AWS-owned defects compound:
1. **Reach is far wider than the page implies.** Confirmed by managed-policy audit (2026-10-15): **all of `ReadOnlyAccess`, `AmazonEC2ReadOnlyAccess`, `AmazonEC2FullAccess`, `SecurityAudit`, `ViewOnlyAccess`(=`job-function/ViewOnlyAccess`), `AdministratorAccess`** grant **both** topology actions on `Resource:"*"` — five via `ec2:Describe*`/`ec2:*`/`*` wildcards, and `ViewOnlyAccess` v46 (edited 2026-09-30) **explicitly adds `ec2:DescribeCapacityReservationTopology` by name** plus sweeps `DescribeInstanceTopology` via its `ec2:DescribeInstance*` sub-wildcard. So a **read-only auditor, a `SecurityAudit` role, or any `ec2:Describe*` monitoring principal already has account-wide physical-placement disclosure** — none of which the prerequisites page lists as a holder, and the account owner may never have intended placement to be in that blast radius.
2. **No least-privilege path exists.** Because both actions have a **blank resource-type cell and only `ec2:Region`**, an admin **cannot** restrict them to a subset of instances/CRs by tag, ARN, AZ, or OU. The *only* ways to contain the exposure are (a) an SCP/Deny on `StringNotEquals ec2:Region` (blanket region restriction), or (b) an **explicit named-action `Deny`** (`"Action":["ec2:DescribeInstanceTopology","ec2:DescribeCapacityReservationTopology"],"Effect":"Deny"`). The page offers neither, so a customer following it verbatim grants the maximal, uncontainable form.

This is a **Lens R / U artifact defect** (AWS-authored permissions guidance the customer copies verbatim; the omission of scope/sensitivity and of any least-privilege example is AWS's, not the customer's) layered on a **Lens S structural gap** (no condition key binds anything but region).

**High-level Test Scenarios (falsifiable).**
- **Claim:** a principal holding ONLY `SecurityAudit` (or `ReadOnlyAccess`, or `AmazonEC2ReadOnlyAccess`, or `ViewOnlyAccess`) can call `describe-instance-topology` / `describe-capacity-reservation-topology` and receive `nn-` node sets for instances/CRs owned by *other teams* in the account. → **Mechanism:** managed-policy JSON grants both actions on `Resource:"*"`; no resource grain. → **Oracle:** `iam:SimulatePrincipalPolicy` on a role carrying exactly the managed policy, action=each topology action, resource=`*` → **Allowed**; then a live scoped read returns placement for instances the role's team does not own. → **Preconditions:** one account, ≥2 teams/workloads, the managed policy attached. → **Cost:** trivial. → **Severity:** **Low–Medium** (intra-account over-exposure of placement to a read-only/audit grant; AWS-owned because the reach is baked into AWS-managed policies + the page's silence).
- **Claim:** a tag-conditioned Deny intended to protect one team's placement is **inert** (the key is never evaluated). → **Oracle:** `iam:SimulateCustomPolicy` with `Allow topology` + `Deny ... Condition StringNotEquals aws:ResourceTag/team: mine` → the Deny does not apply (unknown key) → still Allowed. → **Severity:** Low–Medium (confirms no partial scoping; matches hub Area 4). → **Classification:** structural AWS-owned limitation, not a customer footgun.
- **Claim:** the only working carve-outs are region-Deny and named-action-Deny. → **Oracle:** simulate both; confirm `ec2:Region` is the sole key that changes the decision and that a named-action Deny flips it to Denied. → **Severity:** Informational (hardening guidance for defenders; AWS doc gap for not stating it).
- **Adjacent (Lens U doc-vs-sibling):** the prerequisites page omits the "physical host placement" sensitivity that `how-ec2-instance-topology-works.md` states → a customer scoping IAM off *this* page cannot know the data is placement. → **Oracle:** doc diff; file as the enabling documentation defect. → **Severity:** Informational.

**Doc evidence:** `ec2-instance-topology-prerequisites.md` IAM-permissions section (two bare actions, no policy); `list_ec2.md` rows (blank resource type, only `ec2:Region`); managed policies `ReadOnlyAccess`/`AmazonEC2ReadOnlyAccess`/`AmazonEC2FullAccess`/`SecurityAudit`/`ViewOnlyAccess`(v46, `DescribeCapacityReservationTopology` named)/`AdministratorAccess`. **Severity-if-true:** Low–Medium (intra-account), **reportable as an AWS-authored artifact/doc defect (Tier-2 / Informational-to-Low)**. **Stop condition:** none here (intra-account); if a read-only grant is shown to leak *cross-account* placement, that is hub Area 1/2/3 → HARD STOP.

### Area P2 — Instance-type → network-node-COUNT disclosure oracle; supported-type fence as a value filter (Lens A variant / Lens U)
**Background.** The page publishes an exact, closed map: every supported type returns **3** network nodes, EXCEPT `p6-b200.48xlarge` and `p6-b300.48xlarge`, which return **4**. Unsupported types return no topology at all. For CR topology the node count "varies depending on the type and state of the Capacity Reservation."

**Security Concern.** The node-**count** in any topology response is a **documented 1-bit instance-generation oracle**: a 4-node response can only be a Blackwell `p6-b200`/`p6-b300` (the highest-value GPU capacity); a 3-node response is "some other supported HPC/ML/GPU/Trainium type"; an empty/absent response is "unsupported type / not the capacity you care about." Even without reading the `nn-` values, the shape of the response classifies the target's hardware class. This is only a self-inventory curiosity **within one account** — but it is a **force-multiplier for the hub's cross-account leaks**: if any of hub Area 1/2/3 returns a foreign node set, the node-count alone tells the attacker *what kind of capacity the victim holds* (prioritize Blackwell), and the CR-topology "count varies by type/state" turns the count into a **CR type+state inference** before any instance launches.

**High-level Test Scenarios.**
- **Claim:** response node-count deterministically distinguishes `p6-b200/b300` (4) from all other supported types (3). → **Oracle:** launch one of each class (self-owned), diff `len(NetworkNodes)`; confirm the 3-vs-4 split matches the page. → **Severity:** Informational self-oracle; **upgrades to High as a selector** only when chained to a confirmed hub cross-account leak. → **Preconditions:** self-owned instances of each class.
- **Claim:** CR-topology node-count varies with CR type/state in a way that infers the reservation's instance class/phase pre-launch. → **Oracle:** create CRs of differing supported types/states; record node-count per (type,state). A stable mapping = pre-launch type/phase oracle. → **Severity:** Low (self); force-multiplier for hub Area 2.
- **Claim:** an empty topology response reliably means "unsupported type," usable to fingerprint the supported-type footprint of a (self or leaked) fleet. → **Oracle:** call against a mix of supported/unsupported running instances; empty-vs-populated differential. → **Severity:** Low.

**Doc evidence:** `ec2-instance-topology-prerequisites.md` Instance-types section (3-node list; 4-node = `p6-b200.48xlarge`/`p6-b300.48xlarge`; CR-count-varies footnote). **Severity:** Informational→High-as-chained-selector. **Stop condition:** inherits hub Area 1/2/3 (foreign node bytes → HARD STOP).

### Area P3 — State-gating as an existence/phase oracle refinement; the pending-CR pre-launch window (Lens A error-differential / Lens X phase)
**Background.** The page states the gate precisely: `DescribeInstanceTopology` → instances must be `running`; `DescribeCapacityReservationTopology` → CRs must be `pending` or `active`; and "**You can't get topology information for instances or Capacity Reservations in any other state.**"

**Security Concern.** This adds a documented **state dimension** to the hub's foreign-ID error-differential (hub Area 3). For a known-or-guessed resource ID, the response now potentially distinguishes **owned-running (topology)** vs **owned-wrong-state (documented refusal/empty)** vs **foreign-running** vs **nonexistent** — a richer enumeration/oracle than existence alone, and a possible **instance-state oracle** (is i-… running right now?) if the wrong-state refusal differs from the not-found error. Separately, the **`pending`** CR state is the **earliest possible placement-disclosure window**: `DescribeCapacityReservationTopology` returns a node set for a CR that is reserved-but-not-yet-active, i.e. *before any instance exists* — the most dangerous phase for the hub's Area 2 cross-account leak and Area 6 co-location loop, because no running-instance side channel is needed to confirm placement.

**High-level Test Scenarios.**
- **Claim:** owned-stopped vs owned-running vs nonexistent instance IDs yield distinguishable responses (error code / empty-set / 200), forming a **state + existence oracle**. → **Oracle:** compare responses for (owned-running), (owned-stopped), (owned-terminated), (nonexistent), (unsupported-type) — a stable differential = oracle. → **Severity:** Low–Medium (sharpens hub Area 3). → **Preconditions:** self-owned instances in each state.
- **Claim:** a `pending` CR returns a usable node set (pre-launch placement). → **Oracle:** create a supported-type CR, call `describe-capacity-reservation-topology` while `pending`; non-empty `NetworkNodes` = pre-launch disclosure confirmed. → **Severity:** Low self; **High–Critical if chained to hub Area 2 cross-account shared-CR leak** (pre-launch cross-account placement). → **Stop condition:** foreign pending-CR node set → HARD STOP.
- **Claim (parity, → hub Area 5):** the two APIs treat state transitions / cross-fed IDs with divergent validators. → defer depth to hub Area 5; this plan only pins the exact state preconditions above as the test inputs.

**Doc evidence:** `ec2-instance-topology-prerequisites.md` State section. **Severity:** Low–Medium; High-if-chained. **Stop condition:** foreign node bytes → HARD STOP (hub).

### Area P4 — Regional-parity / sovereign-partition governance gap (Lens U / Lens X)
**Background.** Supported in ~30 commercial regions **plus AWS GovCloud (US-West) and AWS European Sovereign Cloud (Germany)**. Critically: "**The `DescribeCapacityReservationTopology` API is not supported in Israel (Tel Aviv) and AWS GovCloud (US-West).**" Instance-type availability also "varies by Region."

**Security Concern.** Two angles, both AWS-owned:
1. **Detective-control blind spot by region.** A defender who builds placement-anomaly or co-residency-monitoring on `DescribeCapacityReservationTopology` has that control **silently absent in Israel (Tel Aviv) and GovCloud (US-West)** — and asymmetrically, `DescribeInstanceTopology` *is* available in GovCloud-W, so the two halves of the detection diverge exactly in a high-compliance partition. A monitoring assumption that "topology APIs exist everywhere I run" fails open there with no error until invoked.
2. **Surface reaches sovereign/government partitions.** Physical-placement disclosure (the hub's whole concern) is **present in GovCloud (US-West) and the European Sovereign Cloud (Germany)** — partitions where co-residency / data-sovereignty concerns are heightened and where the Area P1 managed-policy reach (SecurityAudit/ReadOnlyAccess) applies identically. The hub's Area 1 "unique per account" guarantee and Area 2 shared-CR tests should be re-run per partition, since cross-partition ID semantics are undocumented.

**High-level Test Scenarios.**
- **Claim:** `DescribeCapacityReservationTopology` returns `UnsupportedOperation`/region-unsupported in IL(Tel Aviv) and GovCloud(US-West) while `DescribeInstanceTopology` succeeds in GovCloud(US-West) → documented control-coverage divergence. → **Oracle:** doc-confirmed; a live `aws ... --region` call pair confirms the error vs success. → **Severity:** Informational (defender guidance). 
- **Claim:** the P1 managed-policy reach and the hub's `nn-` comparability behave identically (or differently) in GovCloud/ESC vs commercial. → **Oracle:** repeat P1 simulate + hub Area-1 two-account test within each partition. → **Severity:** inherits hub Area 1 (High–Critical if comparable); governance-relevant in sovereign partitions. → **Stop condition:** cross-account `nn-` match in any partition → HARD STOP.

**Doc evidence:** `ec2-instance-topology-prerequisites.md` AWS Regions section (region list; CR-topology-not-in-IL/GovCloud-W sentence; ESC-Germany entry). **Severity:** Informational→inherits-hub.

---

## 5. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read-only / `SecurityAudit` / `ViewOnlyAccess` principal reads account-wide physical placement the prerequisites page never lists them as holding | IAM permissions section + 6 managed policies | **none** below region — only a named-action Deny or `ec2:Region` SCP (page states neither) |
| Prerequisites page omits placement-sensitivity + any least-privilege sample → customer grants the maximal uncontainable form | IAM permissions section (vs `how-...-works.md`) | prose only; no sample policy, no `Resource`/`Condition`, no sensitivity note |
| Node-count (3 vs 4) classifies instance generation (Blackwell `p6-b200/b300`) from a topology response | Instance-types section / `NetworkNodes[]` | none — the count map is documented and deterministic |
| Pending-CR topology = earliest pre-launch placement disclosure window | State section / DescribeCapacityReservationTopology | implicit "pending/active" gate (no redaction stated for pending) |
| Owned-state vs foreign vs nonexistent response differential = state+existence oracle | State section / both APIs | documented "can't get topology in any other state" (behavior of the refusal unspecified) |
| CR-topology detective control silently absent in IL(Tel Aviv) / GovCloud(US-West); surface present in GovCloud / ESC-Germany | AWS Regions section | explicit "not supported in Israel (Tel Aviv) and GovCloud (US-West)" |

---

## 6. Out-of-Scope Risk Categories
- **The entire co-residency / `nn-` comparability / cross-account IDOR / co-location-chain / NextToken core** — OWNED by `ec2-instance-topology-attack-research-plan.md` (hub Areas 1/2/3/5/6/7). This plan contributes only recon oracles (P2/P3) and the permissions/region framing (P1/P4) that feed those.
- **Single-account self-inventory / self-optimization** — observing your own fleet's placement/type/state is the feature's intended use (in-scope only when it crosses an account per the hub).
- **Customer-authored IAM** — a customer who writes an over-broad topology grant is a footgun; in scope here only to the extent AWS's *managed policies* and the *prerequisites page's own instruction* produce the exposure (P1).
- **The general Capacity Reservation / RAM-share lifecycle** — owned by `fleet-tutorials-attack-research-plan.md` and the CR siblings.
- **Standard EC2 endpoint TLS/SigV4, IMDS, host-level side channels, the shared Nitro substrate** — no feature-specific transport/data path; the microarchitectural side channel itself is shared-infra (out of scope); this plan covers only the metadata disclosure that would make such targeting easier.

---

## 7. Null hypotheses / doc gaps (pages checked)
Pages read for trigger sweeps: `ec2-instance-topology-prerequisites.md` (full, offline==online), the three sibling UG pages and both API refs (via the hub plan), both `list_ec2.md` topology rows (verbatim), and six AWS-managed policies (`ReadOnlyAccess`, `AmazonEC2ReadOnlyAccess`, `AmazonEC2FullAccess`, `SecurityAudit`, `ViewOnlyAccess`/`job-function/ViewOnlyAccess`, `AdministratorAccess`).

- **Lens B / C (PassRole / credential vending) — NULL.** The prerequisites page names only two read-only `List` actions; no role ARN, PassRole, STS/session, or credential field.
- **Lens G (SSRF) — NULL.** No field the service dereferences/fetches/renders; no `*Url`/`*Uri`/webhook/import on this page.
- **Lens F (injection) — NULL.** No parser/translator/wire protocol; the page is a static matrix.
- **Lens Q (upload) — NULL.** No upload/blob/image/attachment.
- **Lens K (prompt injection) — NULL.** No LLM/agent/GenAI.
- **Lens P (proofing/registration) — NULL.** No registration/verification/OTP/uniqueness gate; the "prerequisites" here are resource *eligibility* (region/type/state), not an anti-abuse workflow.
- **Lens H / W (KMS / attestation) — NULL.** No CMK/encryption-context/attestation key on these actions.
- **Lens J / FF (OAuth / JWT) — NULL.** SigV4 only.
- **Lens T (cross-service secret) — NULL.** No secret generated/persisted.
- **Lens I (tagging/ABAC) — NULL and it IS the point** — the actions carry no tag condition key at all; covered as the *absence* lead in P1 (Lens S), not a tagging-mutation surface.
- **Lens Y (transport/sig) — NULL.** Standard regional EC2 HTTPS/SigV4; no `http://`, internal hop, or SigV2 specific to this page.
- **Lens V / D (network segmentation / control-plane escape) — NULL.** The feature *describes* network topology but the prerequisites page introduces no reachable ENI/listener/segment; disclosure, not reachability.
- **Lens N / BB / CC / DD / EE — NULL.** No namespace migration/dual-ARN; no multi-parser/authorizer/cache/CDN layer; no predictable-name resource created/resolved by this page.
- **Lens AA — deferred.** CR-share revocation completeness is a hub Area 2 / fleet-tutorials concern; the prerequisites page adds only the `pending`/`active` state gate (P3) and the region fence (P4) as inputs.
- **Lens O (audit) — Informational.** Both actions are CloudTrail management events logged by default; there is no distinct signal separating legitimate eligibility/topology use from placement reconnaissance (P2/P3 probing looks like ordinary `Describe*`). Enabler only.
- **Lens X — partial.** Twin-parity depth is hub Area 5; this plan contributes the exact state (P3) and region (P4) divergences as test inputs.

**Primary doc gaps the hunter must close live (ranked, prerequisites-specific):**
1. **Does a bare read-only / `SecurityAudit` grant actually return cross-team placement, and is a named-action Deny the only carve-out?** (P1 — simulate first, then scoped live read.)
2. **Node-count 3-vs-4 determinism and the CR-topology count-varies mapping** (P2 — self-owned, cheap; big force-multiplier for hub leaks).
3. **Owned-state-vs-foreign-vs-nonexistent response differential, and whether a `pending` CR discloses placement pre-launch** (P3).
4. **Per-partition behavior in GovCloud(US-West) and ESC(Germany), and the IL/GovCloud-W CR-topology absence** (P4 — governance-relevant; re-run hub Area 1 per partition).
