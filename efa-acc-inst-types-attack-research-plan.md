# efa-acc-inst-types — Attack / Research Plan

> **Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-acc-inst-types.html`
> ("Maximize network bandwidth on Amazon EC2 instances with multiple network cards" — EFA
> accelerated instance-types **network-card topology / multi-NIC configuration** page.)
> Offline twin: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/efa-acc-inst-types.md`.
> **Drift check (2026-10-15):** online `.html`/`.md` fetched and compared to offline mirror —
> **byte-for-byte identical, no drift.** IAM ground truth from
> `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (authoritative over
> User-Guide prose on any conflict). Status: **documentation-derived falsifiable hypotheses only;
> nothing tested against a live account.** No claim below asserts a confirmed bug.

---

## §0 — How to use this document (orientation for the next agent)

This page is one leaf of the **EFA documentation cluster**. Four sibling plans already exist in
`/work/aws-docs/` and **own** large parts of the EFA surface. To avoid duplicate work, this plan
is deliberately scoped to what is **specific to the multi-network-card topology** that this page —
and essentially only this page — describes. **Read the cross-references before executing any lead.**

**What the siblings already own (do NOT re-derive here):**

| Sibling plan | Owns |
|---|---|
| `efa-attack-research-plan.md` | **HEADLINE: `InterfaceType=efa\|efa-only` is IAM-unscopable** (its Area 1 — no `ec2:InterfaceType` key); SG-on-`efa-only`-may-be-vestigial (its Area 7); mandatory self-ref SG; installer supply chain; intra-customer bandwidth contention explicitly scoped **out** as self-DoS. |
| `efa-start-attack-research-plan.md` (MPI) | **Area C: cross-tenant RDMA/GDR memory reach over SRD**; QP↔ENI binding gap; fabric isolation enforcement (`efa.md:506` "can't cross AZ/VPC"); Area A IAM-expressiveness ceiling. |
| `efa-start-nccl-attack-research-plan.md` | GPUDirect-RDMA GPU-HBM cross-tenant reach deepening MPI Area C; NCCL supply chain; `NCCL_TOPO_FILE`. |
| `efa-start-nixl-attack-research-plan.md` | NIXL/inference KV-cache-as-RDMA-prize; ETCD coord-plane. |

**What THIS plan owns (net-new to the topology page):**
1. The **NetworkCardIndex (NCI) / DeviceIndex** multi-NIC placement knobs — accepted by
   `RunInstances`/`CreateNetworkInterface`/launch-templates, **also 0-hit in `list_ec2.md`** (Lens S/X,
   a *second* unscopable-knob family alongside `InterfaceType`).
2. The page's own **"NCIs … share an underlying physical NIC on the host"** / **"each underlying GPU
   on the host can send traffic directly"** wording — a **tenant-boundary doc-gap** (Lens L/U/V):
   does "on the host" mean *within one customer's whole-host instance* (self-contention, OOS) or a
   *shared physical substrate* (cross-tenant, Critical)? This page is where that ambiguity lives.
3. The page's **copy-paste launch-template JSON** (up to 32 EFA devices, `AssociatePublicIpAddress:false`,
   `DeleteOnTermination:true`, `Groups:[{{security_group_id}}]`) as a **shipped artifact** (Lens R/B/E).
4. "**You can't use an EFA-only network interface as the primary network interface**" — enforcement
   point (Lens U/X).

If a lead here restates a sibling, it is marked **[CROSS-REF — see <plan>]** and not re-expanded.

---

## §1 — Components, Assets, and Design

**What the page actually is.** A configuration/topology reference for EFA-capable *accelerated*
instance types (`p5.48xlarge`, `p5e.48xlarge`, `p5en.48xlarge`, `P6-B200`, `P6e-GB200`, `P6-B300`).
It tells the operator **how many network cards each type has**, **which NetworkCardIndex values map to
which physical NIC/GPU**, and **how to lay out multiple EFA interfaces across those cards** to maximize
aggregate bandwidth. It is not an API; it is a **placement recipe** expressed through existing EC2
request parameters.

**Customer-facing interface / selection knobs (the whole security-relevant surface of this page):**
- `InterfaceType` ∈ {`interface`, `efa`, `efa-only`} — *which kind of device.* **[CROSS-REF — owned by
  `efa-attack-research-plan.md` Area 1.]**
- **`NetworkCardIndex` (NCI)** — *which physical network card the ENI binds to.* The topology
  knob this page is built around.
- **`DeviceIndex`** — *the OS-level device ordering on the instance* (DeviceIndex 0 on NCI 0 = primary).
- Count of EFA interfaces — up to **32 EFA devices** on the largest types (page's own JSON).
- These are set on `RunInstances --network-interfaces`, `CreateNetworkInterface`, and
  **launch templates** (the page's examples are launch-template `LaunchTemplateData` JSON).

**Processes / planes behind it.** No new fleet or service account is introduced by this page. The
relevant planes are the ones the EFA cluster already names: customer instance (guest, Libfabric
user-space) → **EFA Nitro device** (OS-bypass) → **SRD fabric** → peer instances. The *new* physical
objects this page names are **the underlying physical NIC(s)** and **the underlying GPU(s)** "on the
host" that NCIs map onto — see §2, because "the host" is a trust-boundary statement.

**Identity / roles.** SigV4 IAM on the EC2 control plane only. No page-specific identity.

**Resource / identifier shapes.** `eni-*` (ENI IDs), launch-template IDs/versions, instance IDs.
NCI/DeviceIndex are **small integers** (0..N), not identifiers — but see Lens S: they are
request-field integers with **no condition-key backstop**.

**Untrusted-data transforms.** None introduced by this page (no parser/URL/blob field). The page's
only ingested artifacts are the **launch-template JSON** the operator copies (Lens R) and the GPUDirect
topology that NCCL/NIXL consume (**[CROSS-REF — NCCL `NCCL_TOPO_FILE`]**).

**ASCII topology (what the page describes):**

```
          customer instance (e.g. p5.48xlarge — whole-host sized)
   ┌─────────────────────────────────────────────────────────────┐
   │  DeviceIndex 0 / NCI 0  ── ENI (interface|efa) ── primary IP  │
   │  NCI 1 ── EFA ─┐                                              │
   │  NCI 2 ── EFA ─┤  up to 32 EFA devices across N network cards │
   │   ...          │                                              │
   │  NCI k ── EFA ─┘                                              │
   └───────┬───────────────────┬───────────────────┬──────────────┘
           │                   │                    │
     "share an underlying physical NIC on the host" ◀── §2 DOC-GAP:
           │                   │                    │   is "the host" one
     ┌─────▼─────┐       ┌──────▼─────┐       ┌──────▼─────┐  customer's, or
     │ phys NIC  │       │ phys NIC   │  ...  │   GPU      │  shared substrate?
     └───────────┘       └────────────┘       └── "sends traffic directly" (GDR)
```

---

## §2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller w/ `ec2:RunInstances`/`CreateNetworkInterface` for ordinary ENIs | An `efa`/`efa-only` OS-bypass device on a chosen NCI | `InterfaceType=efa` + `NetworkCardIndex=k` | **[CROSS-REF — `efa-attack-research-plan.md` Area 1.]** No `ec2:InterfaceType` **and** no `ec2:NetworkCardIndex`/`ec2:DeviceIndex` key → neither the device type nor its NIC placement can be constrained by policy. |
| Customer instance A (EFA on NCI k) | **The "underlying physical NIC/GPU on the host"** | SRD/RDMA/GDR over the shared physical substrate the page names | **If "the host" is a substrate shared across tenants:** any SRD/GDR frame or memory read reaching another account's buffer via the shared NIC/GPU = **Critical cross-tenant breach.** **If "the host" = one customer's whole-host instance:** self-contention only (OOS). *This page is the sole doc source for the ambiguity — §4 Lens L/V resolves it.* |
| Customer instance A EFA endpoint | Customer B EFA endpoint, same AZ / shared cluster placement group | SRD send between two accounts' EFA ENIs | **[CROSS-REF — `efa-start` MPI Area C owns the SRD cross-tenant reach oracle.]** This plan only adds: *multi-NIC multiplies the attach points* (up to 32 per instance). |
| Launch-template editor (lower-priv) | Instances later launched by a fleet/ASG SLR | `$Latest`/`$Default` LT version adds/removes/relocates EFA interfaces | **[CROSS-REF — `ec2-fleet-*` SLR-non-propagation + `$Latest` late-binding.]** This plan adds: the *topology JSON* is the thing edited. |
| EFA-only ENI | IP network / primary-NIC role | "can't be primary network interface" rule | Attach `efa-only` as DeviceIndex 0 / primary and observe accept-vs-reject (§4 Lens U). |

**Hard stop.** Any observation that an SRD/GDR frame crosses into **AWS's own service plane**, or that
"the host" substrate is genuinely shared across tenants and a cross-account memory read succeeds — stop
immediately, preserve evidence, flag for disclosure. Do not iterate or dump.

---

## §3 — API / interface surface

| Name | Method | Mut? | Face | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `RunInstances` (`--network-interfaces` w/ `NetworkCardIndex`,`DeviceIndex`,`InterfaceType`) | SigV4 | Mut | Ext | Launch instance w/ multi-NIC EFA topology inline | Yes | IAM principals w/ action | **No condition key for `NetworkCardIndex`/`DeviceIndex`/`InterfaceType`** (grep-confirmed, §4 Lens S). |
| `CreateNetworkInterface` (`--interface-type`, placed via attach `NetworkCardIndex`) | SigV4 | Mut | Ext | Create standalone EFA ENI | Yes | IAM principals | Same key gap. |
| `AttachNetworkInterface` (`--network-card-index`, `--device-index`) | SigV4 | Mut | Ext | Bind ENI to a specific physical card | Yes | IAM principals | **The NCI-placement action.** No `ec2:NetworkCardIndex` key → placement unconstrainable. |
| `CreateLaunchTemplate` / `CreateLaunchTemplateVersion` | SigV4 | Mut | Ext | Store the page's topology JSON as reusable `LaunchTemplateData` | Yes | IAM principals | The page's examples ARE this payload. Late-binding → §4 Lens B/E **[CROSS-REF fleet plans].** |
| `ModifyNetworkInterfaceAttribute` | SigV4 | Mut | Ext | Only post-hoc lever (name-not-value `ec2:Attribute`) | Yes | IAM principals | **[CROSS-REF — Area 1.]** Cannot retrofit a device-type/NCI constraint. |

**Console-hidden / parameter-only knobs flagged by this page:** `NetworkCardIndex` and `DeviceIndex`
are plain request integers surfaced in the CLI/API and in "Advanced network configuration," but there
is **no IAM surface for either value** — the exact "most-permissive value accepted by the API with
nothing to warn the operator" shape the skill's §3 asks for, now extended from `InterfaceType` to the
*placement* knobs. Nothing warns an operator that pinning an EFA device onto a particular physical NIC
is unauthorizable.

**Verbatim lead the page plants:** *"The NCIs in the following groups share an underlying physical NIC
on the host"* and *"Each underlying GPU on the host can send traffic directly over the network."* Keep
these two sentences — they are the entire basis of §4 Lens L/V/U.

---

## §4 — Boundary-lens catalog

### Area 1 — [NET-NEW, Lens S/X] NIC-placement knobs `NetworkCardIndex`/`DeviceIndex` are *also* IAM-unscopable
**Background.** This page's whole purpose is to tell operators to pin EFA devices onto specific physical
network cards (NCI 1..k) to maximize bandwidth. Placement onto a physical NIC is a *capability-shaping*
act: it determines how much of the host's aggregate fabric a workload can command and (if "the host" is
shared, §Area 2) which physical substrate it touches.
**Security Concern.** Just like `InterfaceType`, the placement knobs have **no condition key.** Full grep
of `list_ec2.md`: `NetworkCardIndex` = **0 hits**, `DeviceIndex` = **0 hits**, `efa`/`efa-only` = 0 hits.
`AttachNetworkInterface`/`RunInstances` carry no key constraining which card an ENI binds to or how many
EFA devices (up to 32) a principal may place. An admin cannot write "this principal may attach at most N
EFA interfaces" or "may not pin to NCI 0." This is a **second** unscopable-knob family on the same page,
distinct from (and additive to) `efa-attack-research-plan.md` Area 1's `InterfaceType` gap.
**Leads (falsifiable):**
- *Claim:* a principal allowed `AttachNetworkInterface` for one ordinary ENI can attach the full 32-EFA
  multi-card topology this page describes, and no IAM/SCP condition could cap the count or the card.
  → *Oracle:* `iam:SimulateCustomPolicy` with every plausible `NetworkCardIndex`/count condition returns
  Allow (there is no key to name); a scoped live `attach-network-interface --network-card-index k` on an
  `efa` ENI succeeds. *Severity:* **Medium**, Tier-2 reportable (AWS-owned IAM-schema gap).
**Doc evidence:** `list_ec2.md` (grep=0 for both knobs); efa-acc-inst-types.md topology tables + 32-device
JSON. **Severity-if-true:** Medium.

### Area 2 — [NET-NEW HEADLINE, Lens L/V/U] "share an underlying physical NIC / GPU on the host" — tenant-boundary doc-gap
**Background.** The page states NCIs in certain groups **share an underlying physical NIC on the host**,
that **EFA and IP traffic share the same underlying resources** (one reduces the other), and that **each
underlying GPU on the host can send traffic directly over the network** (GPUDirect). These are physical,
sub-instance resources.
**Security Concern — the ambiguity this page uniquely creates.** "The host" is undefined with respect to
*tenancy*. Two readings:
- **(a) Single-tenant reading (most likely):** the accelerated types named are `.48xlarge` / `GB200` /
  metal-class, i.e. **whole-host sized** — one customer gets the entire physical host, so "shares a NIC on
  the host" means *the customer's own interfaces contend with each other.* → **self-DoS / self-contention,
  OUT OF SCOPE** (consistent with `efa-attack-research-plan.md`'s scope exclusion).
- **(b) Shared-substrate reading (must be refuted, not assumed):** if any of these types can be
  **partitioned** (sub-host sizing, future smaller SKUs, a GB200 NVL domain spanning tenants, or a
  Nitro-managed partition), then a physical NIC or a GPU "on the host" is a **cross-tenant shared
  resource**, and the page is documenting a shared data substrate without naming its isolation layer.
**Leads (falsifiable):**
- *Claim (refute (b)):* every instance type on this page is strictly whole-host single-tenant, so NIC/GPU
  sharing is intra-tenant only. → *Oracle:* confirm from the instance-type spec (vCPU/host ratio; is there
  any sub-host variant?) that no sub-host partition exists; if any type is sub-host, escalate to a
  cross-tenant SRD/GDR reach test **[CROSS-REF — `efa-start` MPI Area C oracle]**. *Severity:* **Critical
  if (b) holds**, else self-DoS/OOS.
- *Claim (Lens L, bounded):* the EFA↔IP shared-NIC contention lets a *co-resident* workload (if any
  co-residency exists) starve another's IP bandwidth below any floor. → *Oracle:* only meaningful if (b);
  otherwise self-contention. *Severity:* Medium-if-(b), else OOS.
- *Claim (Lens U):* the "can't cross AZ/VPC" EFA isolation guarantee (`efa.md:506`) is enforced by a named
  mechanism at the physical-NIC/GPU layer this page introduces. → *Oracle:* **[CROSS-REF — `efa-start` MPI
  Area C]**; this plan only flags that the *physical-substrate* layer is where that guarantee must bite and
  the page never names the enforcer. *Severity:* doc-gap → High-if-unenforced.
**Doc evidence:** efa-acc-inst-types.md ("share an underlying physical NIC on the host", "each underlying
GPU … can send traffic directly", "bandwidth used by one will reduce the bandwidth available to the
other"); efa.md:506. **Severity-if-true:** Critical only under reading (b); otherwise OOS self-DoS.
**Priority:** resolve reading (a) vs (b) **first** — it gates whether anything on this page is in scope
beyond the IAM gaps.

### Area 3 — [NET-NEW, Lens U/X] "EFA-only interface can't be the primary network interface"
**Background.** The page asserts `efa-only` interfaces (no IP) cannot occupy the primary NIC role
(DeviceIndex 0 / NCI 0).
**Security Concern.** This is a stated constraint → test the enforcement shape. If the API **silently
accepts** an `efa-only` primary and the instance comes up IP-less (or with the EFA device mispromoted),
that is a documented-guarantee-vs-enforcement gap (Lens U) and a possible availability/footgun primitive.
If it hard-rejects at request validation, the guarantee holds.
**Lead:** *Claim:* `RunInstances`/`AttachNetworkInterface` placing an `efa-only` ENI at DeviceIndex 0 is
rejected at validation, not silently accepted. → *Oracle:* attempt the placement in a scoped account;
observe reject-with-error vs accept-then-degrade. *Severity:* Low–Medium (self-inflicted availability).
**Doc evidence:** efa-acc-inst-types.md ("You can't use an EFA-only network interface as the primary
network interface"). **Severity-if-true:** Low–Medium.

### Area 4 — [NET-NEW, Lens R] The page's copy-paste launch-template JSON is a shipped artifact
**Background.** The page ships `LaunchTemplateData` JSON the operator copies verbatim to build the
multi-NIC topology (up to 32 EFA devices, `AssociatePublicIpAddress:false`, `DeleteOnTermination:true`,
`Groups:[{{security_group_id}}]`).
**Security Concern (statement-by-statement, per skill §Step-1 artifact rule):**
- `AssociatePublicIpAddress:false` — **safe default** (good; note the contrast with the Spot/other EFA
  samples that set it true — see `working-with-ip-addresses` Area 1 **[CROSS-REF]**).
- `Groups:[{{security_group_id}}]` — reuses the **single self-referencing SG** across all 32 EFA devices.
  **[CROSS-REF — `efa-attack-research-plan.md` Area 2/7: whether that SG actually confines SRD traffic is
  the open question; this plan adds that the topology multiplies the SG's attach surface by up to 32.]**
- `DeleteOnTermination:true` — correct hygiene; no residual-ENI concern from the sample itself.
- No IMDS/`HttpTokens` field in the snippet → the template neither enforces nor forbids IMDSv2 for these
  high-value GPU instances (Lens R omission). *Lead:* does the sample's silence leave IMDSv1 reachable on
  instances that hold GPUDirect-capable fabric creds? *Oracle:* launch from the verbatim template, query
  IMDS without a token. *Severity:* Medium (sample-omission hardening gap).
**Doc evidence:** efa-acc-inst-types.md launch-template JSON block. **Severity-if-true:** Low–Medium.

### Area 5 — [CROSS-REF, Lens B/E] Launch-template late-binding of the topology
**Background.** Because the topology lives in a launch template, the fleet/ASG `$Latest`/`$Default`
late-binding privesc applies: an editor who can bump a LT version can add/remove/relocate EFA interfaces
that a fleet SLR will then launch under identity that doesn't propagate the editor's conditions.
**This plan does not re-expand it** — **[CROSS-REF — `ec2-fleet-*` SLR-non-propagation + `$Latest`
late-binding plans].** It only records that the *object being late-bound here is the EFA NIC topology*,
so the blast radius of that known class now includes "silently attach OS-bypass/RDMA devices to
fleet-launched instances." *Severity:* inherits High from the fleet class.

### Area 6 — [CROSS-REF] `InterfaceType` unscopability + SG-on-`efa-only` vestigiality
**[CROSS-REF — fully owned by `efa-attack-research-plan.md` Areas 1 and 7, and `efa-start` MPI Area A.]**
Recorded here only so this page's reader is routed correctly: the `efa`/`efa-only` device-type gap and
the "is the SG on an `efa-only` ENI real or dead config" question are **not** re-tested from this page.

---

## §5 — Prioritized NEW / changed surface

Fire in this order:

1. **Area 2 (resolve single-tenant vs shared-substrate).** Gates whether the physical NIC/GPU story is a
   Critical cross-tenant surface or an OOS self-DoS. Cheapest first move: confirm every listed type is
   whole-host. Do this before touching anything data-plane.
2. **Area 1 (NCI/DeviceIndex IAM-unscopability).** Highest-confidence net-new finding; pure
   `SimulateCustomPolicy` + grep already supports it; AWS-owned, reportable Medium.
3. **Area 4 (launch-template artifact audit — IMDS omission, 32× SG reuse).** Static, cheap.
4. **Area 3 (`efa-only`-as-primary enforcement shape).** Single scoped API attempt.
5. **Areas 5 & 6 (cross-refs).** Execute via the sibling plans, not here.

**Concentration note:** everything genuinely new on this page is either (a) a *second* instance of the
EFA cluster's unscopable-knob theme (now the placement knobs), or (b) the tenant-boundary ambiguity in
the "on the host" wording. Spend fire there; route the rest to siblings.

---

## §6 — Falsifiable-hypothesis summary (oracle table)

| # | Claim (as breakable) | Confirm/refute oracle | Sev-if-true |
|---|---|---|---|
| A1 | `NetworkCardIndex`/`DeviceIndex`/EFA-count cannot be constrained by any IAM/SCP condition | `SimulateCustomPolicy` all-Allow (no key exists) + scoped `attach --network-card-index` succeeds | Medium (AWS-owned) |
| A2a | Every listed type is whole-host single-tenant → NIC/GPU sharing intra-tenant only | Instance-type spec shows no sub-host variant | OOS (good outcome) |
| A2b | A physical NIC/GPU "on the host" is shared across tenants → cross-tenant SRD/GDR reach | **[CROSS-REF MPI Area C oracle]** cross-account SRD send/GDR read same host | **Critical** |
| A2c | `efa.md:506` AZ/VPC isolation has a named enforcer at the physical-NIC layer | **[CROSS-REF MPI Area C]** | High-if-unenforced |
| A3 | `efa-only` at DeviceIndex 0 is rejected at validation, not silently degraded | Scoped `RunInstances` placement attempt | Low–Medium |
| A4 | Verbatim LT leaves IMDSv1 reachable on GPUDirect instances | Launch from template, query IMDS tokenless | Medium |
| A5 | Topology late-binds via `$Latest` so a fleet SLR attaches EFA devices an LT editor chose | **[CROSS-REF fleet plans]** | High |

---

## §7 — Scope exclusions (explicit)

- **Intra-customer bandwidth contention** (EFA↔ENA share a NIC; NCIs share NIC/GPU **on the customer's own
  whole-host instance**) → self-contention, **OOS** unless Area 2 reading (b) is confirmed. Consistent with
  `efa-attack-research-plan.md`.
- **Installer / software supply chain** (efa-installer, NCCL/NIXL/MPI stacks) → **[CROSS-REF efa-start*
  plans].** Not on this topology page.
- **Generic ENI IDOR / cross-VPC attach / detach-collateral** → owned by the ENI cluster plans
  (`using-eni`, `network-interface-attachments`, `delete-eni`).
- **Live-account execution** — out of scope for this skill; this is a plan only.

---

## §8 — Null hypotheses (lenses checked and not fired, with pages read)

Pages read for this sweep: `efa-acc-inst-types.md` (full), `efa.md` (limits/isolation table + l.506),
`create-efa.md` / `detach-efa.md` (referenced), `list_ec2.md` (grep sweep), and the four sibling plans.

- **Lens A (cross-tenant IDOR):** NULL for this page — NCI/DeviceIndex are small integers, not
  tenant-scoped resource identifiers; no resource-by-ID API introduced here. (Cross-tenant *fabric* reach
  is Lens V, routed to MPI Area C.)
- **Lens B/E:** fires only as **[CROSS-REF]** (launch-template late-binding) — no new PassRole/role-ARN
  field on this page.
- **Lens C (credential vending):** NULL — no STS/session-policy/token surface on this page.
- **Lens D (data→control escape):** NULL — no control ENI / host-agent surface described here; the only
  "control" angle is the LT late-binding (Lens E cross-ref).
- **Lens F (translation/injection):** NULL — no parser/wire-protocol/query layer on this page.
- **Lens G (SSRF / server-dereferenced location field):** NULL — read the full page + launch-template JSON;
  **no field the service fetches/renders** (`Groups`, `NetworkCardIndex`, `DeviceIndex`, `InterfaceType`,
  `AssociatePublicIpAddress`, `DeleteOnTermination` are all local config, none dereferenced).
- **Lens H (crypto/signing):** NULL — no crypto material on this page.
- **Lens J (multi-tenant metadata/logging):** NULL for this page.
- **Lens K (rate/quota as security control):** partial — EFA-device count (≤32) is uncapped by IAM
  (folded into Area 1); no other quota lever here.
- **Lens L (resource exhaustion / noisy neighbor):** fires **conditionally** (Area 2) — OOS self-DoS under
  single-tenant reading, Medium under shared-substrate reading.
- **Lens M, N, O, P, Q, T, W, Y:** NULL — read the full page; no OTP/gate, no uploaded blob, no secret
  persisted, no profile/branding field, no business-proofing step on this topology page.
- **Lens R (shipped-artifact audit):** FIRES — Area 4 (launch-template JSON).
- **Lens S (condition-key scoping; "key that doesn't exist" variant):** FIRES — Area 1 (NCI/DeviceIndex),
  and **[CROSS-REF]** Area 6 (`InterfaceType`). This is the page's dominant lens.
- **Lens U (documented-guarantee vs enforcement):** FIRES — Area 2c (AZ/VPC isolation at physical layer,
  cross-ref) and Area 3 (`efa-only`-not-primary).
- **Lens V/D (network segmentation / data-plane reach):** FIRES as **[CROSS-REF MPI Area C]** — multi-NIC
  multiplies attach points (this plan's only additive note).
- **Lens X (action-family parity):** FIRES — Area 1 (same key gap across `RunInstances` /
  `CreateNetworkInterface` / `AttachNetworkInterface`).
- **Lens AA, BB, CC, DD, EE, FF:** NULL for this page — no deletion-collateral, tag-based-authz,
  pagination-leak, versioning, cross-region, or event-blindspot surface specific to the topology config
  (deletion-collateral is owned by `delete-eni`; event blind-spots by the fleet plans).

**Bottom line.** This page's security content reduces to **two net-new facts** — (1) the NIC-*placement*
knobs are IAM-unscopable just like the device-type (Lens S/X, reportable Medium), and (2) the page is the
sole doc source of the **"on the host" tenant-boundary ambiguity** (Lens L/V/U) that must be refuted
before any physical-substrate sharing is assumed in scope — plus cross-references to the EFA cluster for
everything else. A clean refutation of Area 2 reading (b) leaves Area 1 as the only standing finding, which
is itself a correct and complete result.
