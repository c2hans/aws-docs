# How EC2 Instance Topology Works — Attack Research Plan
Source of leads: `how-ec2-instance-topology-works.html` (offline twin `./docs/AWSEC2/latest/UserGuide/how-ec2-instance-topology-works.md`; offline == online 2026-10-15). Parent hub `ec2-instance-topology.html`, prereqs `ec2-instance-topology-prerequisites.html`, examples `ec2-instance-topology-examples.html`, API ref `API_DescribeInstanceTopology` / `API_DescribeCapacityReservationTopology`. Status: documentation-derived hypotheses only; nothing tested against a live account.

> **This is a page-level CHILD / MECHANISM-COMPLEMENT of [[ec2-instance-topology-attack-research-plan]]** (`ec2-instance-topology-attack-research-plan.md`), which owns the feature-/API-level surface. That parent already owns, and this plan does **NOT** restate (cross-refs only):
> - Parent **Area 1** [HEADLINE/HARD-STOP] — the "**Each topology view is unique per AWS account**" guarantee (hub `ec2-instance-topology.md` line 31) and whether `nn-` IDs are **cross-account comparable / low-entropy** (the load-bearing unknown, needs a 2-account canary).
> - Parent **Area 2** — cross-account placement disclosure via RAM-shared / foreign Capacity Reservations.
> - Parent **Area 3** — foreign-ID ownership scoping + error-differential enumeration oracle on `InstanceId.N` / `GroupName.N` / `CapacityReservationId.N` (incl. placement-group **name**-collision).
> - Parent **Area 4** — structurally unscopable account-wide placement read (blank resource type, only `ec2:Region`; no tag/ARN/AZ condition key).
> - Parent **Area 5** — twin-parity between the two APIs + the pre-launch window.
> - Parent **Area 6** — observe + influence (`cr-cpg`) + confirm co-location kill chain.
> - Parent **Area 7** — `NextToken` ("SomeEncryptedToken") integrity/scoping.
>
> This child owns only what the **mechanism page itself newly introduces**: the fully-documented **proximity-inference algorithm** (W1), the **intra-account node-ID stability** the differences table confirms (W2), and the **partial-CR-topology → "launch to resolve the bottom node"** influence mechanic (W3). Each **supplies/settles** a parent area rather than opening a new boundary.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right.
- **HARD STOP:** the moment evidence shows cross-account `nn-` comparability (parent Area 1) or any identity/credential/ARN belonging to AWS's own service plane — stop, preserve evidence, flag for AWS-Security disclosure. This page's leads are **confirmation-oracle / mechanism** depth that make the parent's HARD-STOP leads *mechanical*; treat a cross-account match surfaced while exercising W1 as the parent-Area-1 HARD STOP.

## 1. Pentest Objectives (boundary-breach goals)
1. **Prove the proximity verdict is mechanical, not interpretive** — show that two parties applying the page's own documented rule ("same bottom node ⇒ physically close") to two topology responses derive the *same* adjacency verdict, i.e. the response alone (no AWS tooling) is a push-button co-residency oracle. (This is the engine behind parent Areas 1/6; here it is the deliverable.)
2. **Bound the entropy question from the intra-account side** — demonstrate (from docs + single-account reads) that `nn-` IDs are **stable and comparable within an account across both APIs and across the pre-launch→post-launch transition**, narrowing the parent's open HARD-STOP question to *purely cross-account comparability*.
3. **Map the influence lever precisely** — show that the CR topology deliberately **withholds the bottom (host-adjacent) node pre-launch** and that an **instance launch is the documented act that resolves it**, i.e. launching is the "influence/confirm" step of the parent Area 6 loop.

## 2. Components, Assets, and Design (net-new mechanism detail only)

**Asset.** Same `NetworkNodes[]` node set as the parent (ordered `nn-…` IDs, top→bottom; last = host-adjacent bottom node). The *net-new* asset this page documents is the **interpretation function** that maps raw node sets to a physical-adjacency verdict — AWS publishes the algorithm in prose and worked examples:
- *"if the network node connected to any two instances is the same, these instances are physically close to each other"* (shared **bottom** node ⇒ adjacent).
- *"the fewer the number of hops between network nodes, the closer the instances are"* (shared **upper** node + hop-count ⇒ graded proximity).
- Worked verdicts: instances 1&2 (share `nn-4…`) are closest; 1,2,3 (share `nn-2…` at layer ii) closer to each other than to 4 (shares only `nn-1…` at layer i).

**Response fields re-confirmed (owned by parent §2 — listed here only to anchor W-leads):** `NetworkNodes[]`, `InstanceId`/`CapacityReservationId`, `InstanceType`, `GroupName` (placement group, e.g. `ML-group`), `CapacityBlockId`, `ZoneId` (e.g. `usw2-az2`), `AvailabilityZone` (e.g. `us-west-2a`), `State` (CR only), `NextToken`.

**Design facts the differences table newly pins down:**
- *"If the instance is in a Capacity Reservation, the first nodes will match the corresponding Capacity Reservation topology, followed by additional nodes to connect to the instance."* ⇒ **the same physical node yields the same `nn-` string across the two APIs and across the pre-launch→post-launch transition, within one account** (W2).
- CR topology returns a **partial** set (1–2 upper nodes); inline code comment: *"Visibility of additional nodes requires an instance launch and the DescribeInstanceTopology API."* ⇒ the **bottom/host-adjacent node is hidden until an instance launches** (W3).
- Footnote: *"For Capacity Blocks for Ultraservers, the network node set is the same when describing the topology for an `active` Capacity Reservation or its running instance."* ⇒ for Ultraservers the **pre-launch** leak is byte-for-byte as precise as the post-launch one (no bottom-node gap) — corroborates parent Area 5.

```
Caller (ec2:DescribeInstanceTopology / ...CapacityReservationTopology)
      │  SigV4, regional EC2 endpoint, no resource grain (parent Area 4)
      ▼
NetworkNodes[]  (nn-… IDs, top→bottom)  ──┐
   + InstanceType / ZoneId / GroupName ...│
      │                                   │  apply DOCUMENTED rule (this page):
      ▼                                   │   shared bottom node  ⇒ adjacent
  [W1] Proximity-inference function ◄─────┘   fewer hops to common ⇒ closer
      │
      ├─ W2: nn- stable across both APIs + pre→post launch (intra-account)  → narrows parent Area 1/5
      └─ W3: bottom node hidden pre-launch; LAUNCH resolves it            → mechanizes parent Area 6
```

## 3. API / Interface Inventory
No new API, parameter, console route, or non-SDK endpoint is introduced on this page — it is the explanatory/mechanism page for the two actions inventoried in the parent (`DescribeInstanceTopology`, `DescribeCapacityReservationTopology`). See parent §3. The only "interface" this page adds is **documentation**: the adjacency-interpretation algorithm (W1) and the response-field schema shown in the examples.

## 4. Recommended Areas of Focus (net-new / mechanism depth; priority order)

### Area W1 — [HEADLINE] The proximity-inference algorithm IS the co-residency confirmation oracle (Lens U — guarantee-vs-mechanism; supplies parent Area 1/6)
**Background.** AWS's own words turn a raw node set into a physical-adjacency verdict with a deterministic rule — no AWS tooling, no heuristics required: *"As a general rule, if the network node connected to any two instances is the same, these instances are physically close to each other … the fewer the number of hops between network nodes, the closer the instances are."* The page even hands you worked verdicts.
**Security Concern.** The parent's HARD-STOP (Area 1) hinges on whether `nn-` IDs are **cross-account comparable**. If they are, *this page supplies the push-button scoring function that converts the comparison into a graded co-residency verdict* — i.e. the attack is not "stare at opaque strings and guess", it is "string-equality on the bottom node ⇒ same host-adjacent node ⇒ CONFIRMED adjacent", with a documented fallback to upper-layer hop-count for graded proximity. The feature's co-location **disclaimer** ("you can't use it to launch a new instance physically close to an existing instance") is advisory about the *launch* path only; it does **nothing** to blunt the *inference* path this algorithm defines. The guarantee that matters ("unique per AWS account") is enforced — *if at all* — by per-account salting of the `nn-` token, **not** by the interpretation rule, which is identical for everyone.
**High-level Test Scenarios.**
- **Claim:** given two topology responses, applying only the page's documented rule yields a deterministic, repeatable adjacency ranking (bottom-node equality = adjacent; shared-upper-node hop-count = graded). → **Mechanism:** the "general rule" + worked examples (instances 1&2 closest via shared `nn-4…`; 1,2,3 share `nn-2…`). → **Oracle:** in a **single account** (benign), launch ≥4 supported-type instances, call `DescribeInstanceTopology`, and show the rule reproduces AWS's own ordering and matches an independent latency/`FulfilledCapacity` proximity signal. Confirms the scoring function works end-to-end. → **Preconditions:** one account, ≥2 supported instance types; **Cost:** low (minutes of a `p4d`/`trn1`-class or `g6e` instance). → **Severity:** mechanism-enabler on its own (**Informational**); **inherits parent Area 1 severity (High→Critical, HARD STOP) the instant the same rule is applied across two accounts and a bottom-node `nn-` matches.**
- **Claim (settle-the-disclaimer):** the "can't launch close" disclaimer is not a technical control over inference. → **Oracle:** confirm from docs/behavior that nothing in the response is withheld or perturbed to defeat the published rule (no coarsening, no per-query noise). → **Severity:** Informational (Lens U doc-vs-mechanism).
**Doc evidence:** `how-ec2-instance-topology-works.md` — "As a general rule…"/"fewer the number of hops…"; hub considerations "you can't use it to launch a new instance physically close". **Stop condition:** cross-account bottom-node match → HARD STOP, hand to parent Area 1.

### Area W2 — Intra-account node-ID STABILITY across both APIs & the pre→post-launch transition (Lens X / Lens U; settles half of parent Area 1/5)
**Background.** The differences table states that for an instance inside a Capacity Reservation, *"the first nodes will match the corresponding Capacity Reservation topology, followed by additional nodes to connect to the instance,"* and the Ultraserver footnote says the CR and running-instance node sets are **identical**.
**Security Concern.** This is a **documented admission that the same physical node emits the same `nn-` string across (a) the two different APIs and (b) the pre-launch→post-launch lifecycle, within one account.** It therefore **settles the intra-account half** of the parent's open entropy question: `nn-` is not re-randomized per-call, per-API, or per-lifecycle-stage — it is at least **account-stable and join-able**. The remaining unknown collapses to a single crisp question: *is the salt per-account (parent Area 1 holds) or global (parent Area 1 breaks)?* It also means an attacker can **correlate a pre-launch CR topology with the later running-instance topology** of the same capacity by `nn-` equality — a within-account join the docs guarantee works.
**High-level Test Scenarios.**
- **Claim:** `DescribeCapacityReservationTopology` for a CR and `DescribeInstanceTopology` for an instance launched into that CR share identical leading `nn-` IDs. → **Oracle:** one account: create a supported-type CR, read its topology, launch an instance into it, read instance topology; assert prefix-equality of `nn-` lists (full equality for Ultraservers). → **Preconditions:** single account; **Cost:** low. → **Severity:** Informational intra-account (confirms stability); **the result is the precondition that makes parent Area 2's shared-CR leak and Area 5's pre-launch window dangerous** — if a RAM-shared-in CR's `nn-` set (parent Area 2) is join-able to the owner's later instance topology, pre-launch disclosure becomes a durable tracker.
- **Claim (negative-control for parent Area 1):** `nn-` IDs are **not** perturbed between two reads of the same unchanged instance. → **Oracle:** re-read the same instance's topology minutes/hours apart; assert byte-identical `nn-`. Any per-read noise would *strengthen* the "unique per account" defense and must be recorded. → **Severity:** Informational (bounds parent Area 1).
**Doc evidence:** differences table "the first nodes will match the corresponding Capacity Reservation topology"; Ultraserver footnote. **Stop condition:** none intra-account; escalate only via parent Area 1/2.

### Area W3 — Pre-launch bottom-node is withheld; an instance LAUNCH is the documented resolve step (Lens U + kill-chain; mechanizes parent Area 6)
**Background.** CR topology returns a **partial** node set and the example code comment is explicit: *"Visibility of additional nodes requires an instance launch and the DescribeInstanceTopology API."* The differences table echoes it ("Shows a partial set of nodes").
**Security Concern.** This precisely defines the **influence→confirm** half of the parent Area 6 co-location loop: the host-adjacent *bottom* node (the finest-grained physical signal) is deliberately **not** disclosed until a tenant **launches** into the capacity. So the documented workflow for resolving the bottom node *is itself the launch action* an attacker would use to drive capacity toward a target — the "observe (partial CR topology) → influence (launch into/near it) → confirm (now the bottom `nn-` is visible)" sequence is spelled out as normal usage. For **Ultraservers** the gap is zero (W2 footnote), so even the *pre-launch* CR topology already carries the bottom-equivalent node — removing the launch step entirely for those types.
**High-level Test Scenarios.**
- **Claim:** a CR's topology omits the bottom node until an instance is launched, then `DescribeInstanceTopology` reveals it. → **Oracle:** single account: read CR topology (observe partial set), launch, re-read via instance API (bottom node now present); diff the node counts. → **Preconditions:** single account, supported type; **Cost:** low. → **Severity:** Informational self-use; **feeds parent Area 6 — rated at the chain end: Critical iff cross-account co-location is confirmed (then HARD STOP), otherwise in-scope only as self-placement (out of scope).**
- **Claim (Ultraserver no-gap):** for Capacity Blocks for Ultraservers the pre-launch CR topology already equals the running-instance node set, so no launch is needed to obtain the fine-grained signal. → **Oracle:** compare active-CR vs running-instance node sets for an Ultraserver type; assert equality. → **Severity:** raises parent Area 2/5 severity for Ultraservers specifically (pre-launch leak == post-launch precision).
**Doc evidence:** CR example comment "Visibility of additional nodes requires an instance launch…"; differences table "Shows a partial set of nodes"; Ultraserver footnote. **Stop condition:** cross-account confirm → parent Area 6 HARD STOP.

## 5. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Deterministic adjacency scoring from a raw node set (W1) | Published proximity rule | "unique per AWS account" salting of `nn-` (parent Area 1) — the ONLY barrier; the rule itself is public & unmitigated |
| Join pre-launch CR topology to post-launch instance topology by `nn-` (W2) | Both APIs, one account | None documented — stability is an explicit guarantee ("first nodes will match") |
| Re-read noise / per-call perturbation of `nn-` (W2 negative control) | Response generator | Unknown — if present it strengthens parent Area 1; if absent it confirms join-ability |
| Launch-to-resolve-bottom-node as the influence step (W3) | CR topology → instance topology | "can't use it to launch close" disclaimer (advisory only, not a technical control) |
| Ultraserver pre-launch == post-launch precision (W2/W3) | Capacity Blocks for Ultraservers | None — documented equivalence removes the pre-launch coarsening |

## 6. Out-of-Scope Risk Categories
- **Single-account self-placement / self-optimization** — the feature's intended use; in scope only when it crosses to another account (parent Area 1/2/6).
- **The IAM/condition-key unscopability, foreign-ID/error-differential oracle, RAM-shared-CR disclosure, and `NextToken` surface** — owned by the parent (Areas 2/3/4/7); not re-opened here.
- **The cross-account `nn-` comparability HARD-STOP itself** — owned by parent Area 1; this plan only supplies the scoring function (W1) and the intra-account stability bound (W2) that make it mechanical.
- **General Capacity Reservation / cluster-placement-group lifecycle** (`cr-cpg`, RAM share/consume/billing) — owned by `fleet-tutorials-attack-research-plan.md` and the CR siblings; touched here only via the topology-influence mechanic (W3).
- **AZ-ID (`ZoneId`) as a standalone locator** — AZ-granular and already publicly mappable (`DescribeAvailabilityZones`); not a net-new fine-grained leak. The fine-grained signal remains the `nn-` set (parent Area 1).

## 7. Null hypotheses / doc gaps (pages checked: `how-ec2-instance-topology-works.md`, hub `ec2-instance-topology.md`, prereqs `ec2-instance-topology-prerequisites.md`)
This is a **conceptual/mechanism page**: no new API, parameter, IAM/CFN JSON, URL/host field, uploaded blob, token/JWT, OAuth flow, KMS/attestation key, network interface, or caching/authorizer layer is introduced. Accordingly the following lenses are **N/A for this page** (their triggers are owned, where present at all, by the parent):
- **Lens A (IDOR), B (PassRole), C (vending), E (RBAC)** — no new resource-by-ID API or role here; parent Areas 2/3/4 own the read-side IDOR shape. **NULL (page named).**
- **Lens G (SSRF)** — no field the service dereferences; the page contains only `nn-`/`i-`/`cr-` identifiers and example JSON. **NULL.**
- **Lens Q (upload), J (OAuth), M (session-id), FF (JWT)** — no upload/blob, no 3P link, no session/token except the parent-owned `NextToken` (parent Area 7). **NULL.**
- **Lens F (translation/injection), BB (canonicalization), CC (upstream-context), DD (cache-key)** — single read API, no multi-parser/authorizer/cache path. **NULL.**
- **Lens H (KMS/enc-context), W (attestation), Y (transport/sig)** — no CMK/attestation/transport claim on this page. **NULL.**
- **Lens I (tagging/ABAC), S (condition-key semantics), R (IAM-artifact)** — no policy JSON on this page; the *absence* of condition keys is owned as parent Area 4. **NULL here / deferred to parent.**
- **Lens N (namespace migration), T (secret reachability), L (DoS), EE (predictable-name land-grab)** — no dual namespace, no persisted secret, no new parser/limit, no name the service resolves-and-trusts. **NULL.**
- **Lens V (network segmentation)** — the page *describes* network topology but exposes no ENI/segment the caller can reach; the co-residency angle is **information disclosure** (W1/parent Area 1), not L3/L4 reachability. **NULL as a reachability surface.**
- **Lens O (audit)** — both actions are CloudTrail management events (parent Area 4/§8); W1/W3 recon looks like ordinary `Describe*`/`RunInstances` traffic → detection blind spot, enabler-only. **Informational, deferred to parent.**
- **Firing lenses: U (primary — documented guarantee/mechanism, W1/W3), X (twin/stability parity, W2), + kill-chain composition (W3→parent Area 6), A disclosure-timing (W2 join feeds parent Area 2).**

**Open doc-gaps carried (all resolve into parent leads):**
1. **`nn-` cross-account comparability + salt scope** — the single load-bearing unknown; W1 supplies the oracle, parent Area 1 is the HARD-STOP test (2-account canary).
2. **Per-read / per-call `nn-` perturbation** — W2 negative control; absence confirms join-ability, presence strengthens the per-account guarantee.
3. **Does a RAM-shared-in CR's `nn-` set join to the owner's later running-instance topology** — W2 stability × parent Area 2 shared-CR disclosure = durable cross-account tracker (resolve parent Area 2 first).
