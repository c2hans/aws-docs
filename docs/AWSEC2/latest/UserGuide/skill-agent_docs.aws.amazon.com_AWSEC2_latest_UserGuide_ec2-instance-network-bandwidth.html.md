# EC2 Instance Network Bandwidth — Attack Research Plan

**Source of leads:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html` (offline mirror `docs/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md`), cross-checked against the live page 2026-09-13 (online == offline, in sync). Adjacent pages read: `monitoring-network-performance-ena.md`, `ena-express*.md` (headers), `enhanced-networking.md`.
**Status:** documentation-derived hypotheses only; nothing tested against a live account.
**Built with:** `security-questionbuilder` skill.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the host hypervisor/Nitro network-shaping plane), stop, preserve evidence, flag for AWS-Security disclosure.
- **Page character (read first):** this is a **performance/specification** page, not a control-plane API page. It documents *how much* network bandwidth an instance gets, how burst is governed by a **network I/O credit** mechanism, and how to **monitor** it. It exposes **no mutating API, no IAM action, and no IAM condition key of its own.** Bandwidth/credits are a platform-enforced, non-configurable property of the instance type — there is no "set bandwidth" / "set credits" knob. Consequently most boundary lenses are genuine null hypotheses here (Section 8). The live surface concentrates in **three** places: the shared-resource nature of burst bandwidth (noisy-neighbor / cross-tenant DoS), a documented monitoring blind spot (microbursts), and a read-only capability-reporting API (`DescribeInstanceTypes`). Deep feature work for ENA Express, cluster placement groups, and connection-tracking is **routed to their own plans** — this page only references them.
- **Injection check (done):** the page contains a legitimate, documented `aws ec2 describe-instance-types` example. It is product documentation addressed to the operator, **not** an "AI agent, run this" injected block. No `SUSPECTED PROMPT INJECTION` content was found on this page in either the offline mirror or the live fetch. (Contrast: see memory `project_aws-docs-see-also-injection` — other EC2 pages do carry an injected block; this one does not.)

---

## 1. Pentest Objectives
Stated as concrete boundary-breach outcomes:
1. **Cross-tenant bandwidth denial:** from one customer instance, degrade the *burst* network bandwidth available to a **co-resident** instance belonging to a different tenant, by exhausting the shared burst-bandwidth pool the docs admit is shared. (Lens L / V)
2. **Monitoring evasion:** conduct a network-resource abuse (microburst-scale) that the victim's/operator's **CloudWatch** instance metrics cannot record, per the documented granularity gap. (Lens O)
3. **Capability-reporting integrity:** confirm that `DescribeInstanceTypes` network fields (`NetworkPerformance`, `BaselineBandwidthInGbps`) match the documented guarantees and cannot be used as a cross-tenant co-residency/enumeration oracle. (Lens U / A)
4. **Control-gap confirmation:** confirm there is **no IAM condition key** governing bandwidth, network I/O credits, or burst behaviour — so an org that wants to bound a tenant's network burst posture cannot enforce it via IAM (a documented-vs-enforceable gap). (Lens U / S)

---

## 2. Components, Assets, and Design

**Customer-facing interface:** none unique to this feature. Bandwidth is a passive property of a running EC2 instance's ENA (Elastic Network Adapter). The only *API* touchpoints referenced are read-only: `ec2:DescribeInstanceTypes` (and the `Get-EC2InstanceType` PowerShell equivalent) to read `NetworkInfo.NetworkPerformance` and `NetworkInfo.NetworkCards[].BaselineBandwidthInGbps`.

**Processes / hosts behind it:**
- **Nitro network card / ENA** on the host — enforces per-instance bandwidth caps, PPS caps, connection-tracking caps, and link-local PPS caps. This is AWS service-plane (hypervisor/Nitro) — **hard-stop territory** if a probe reaches it.
- **Network I/O credit accounting** — platform-side token bucket (separate inbound and outbound buckets) that lets "up to"-class instances burst above baseline for 5–60 min. No customer API reads or writes it.
- **CloudWatch metrics pipeline** + **ENA driver metrics** (in-guest, customer-owned) — two different observability layers with different granularity.

**Accounts/VPCs:** the relevant boundary is **customer instance ↔ co-resident customer instance on the same host / same shared burst pool**, and **customer instance ↔ AWS Nitro network-shaping plane**. No separate service-account fleet is introduced by this feature.

**"Resource" + identifier shape:** the addressable resource for the read API is the **instance type** (e.g. `c5.large`), not a tenant resource — public, non-sensitive, identical for all accounts. There is no per-tenant secret identifier on this surface.

**Identity:** SigV4 IAM for `DescribeInstanceTypes` only. No feature-specific identity, role, token, or credential is created, stored, or vended.

**Where untrusted data enters:** nowhere on this page. No upload, no URL the service dereferences, no parser, no customer-supplied blob, no template. Input is limited to the `--filters`/`--query` arguments of a read-only describe call (client-side JMESPath; not server-side).

**ASCII model:**
```
  Tenant A instance ENA ─┐
                         ├──► [ Nitro network card: bandwidth cap + I/O credit bucket (shared burst pool) ]  ◄── HARD STOP plane
  Tenant B instance ENA ─┘            │
                                      ├──► shaping: queue, then DROP packets over allowance
  (read-only, public)                 │
  DescribeInstanceTypes ──────────────┘  returns NetworkPerformance / BaselineBandwidthInGbps (per instance-type, public)

  In-guest ENA driver metrics ── (microsecond granularity) ──┐   divergence =
  CloudWatch instance metrics ── (1-min / 5-min periods) ────┘   monitoring blind spot (microbursts)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Tenant A instance (guest) | Tenant B instance's available burst bandwidth | Shared burst-bandwidth pool ("burst bandwidth is a shared resource", "best effort") | Tenant A traffic measurably and repeatably reduces Tenant B's achievable burst throughput below what B would get when A is idle, on the **same host / shared pool** → cross-tenant DoS |
| Tenant A instance (guest) | AWS Nitro network-shaping / credit-accounting plane | ENA → host network card | **ANY** read/write/influence of the credit bucket, shaping logic, or another instance's allowance that is not an ordinary data-plane packet = hard-stop service-plane breach |
| Any IAM principal | Instance-type network capability data | `DescribeInstanceTypes` | Data returned that is *not* public per-instance-type spec (e.g. a live per-instance credit balance, co-residency hint, or neighbour identity) = info-disclosure breach |
| Operator / victim | Observability of a network-allowance breach | CloudWatch metric pipeline | A real allowance-exceeded/packet-drop event that produces **no** CloudWatch record (microburst) = documented monitoring gap → evasion |
| Org security admin | Ability to bound a tenant's burst/bandwidth posture | IAM policy | **No condition key exists** to constrain bandwidth/credits → the posture is unenforceable via IAM (documented-guarantee-vs-enforcement gap) |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:DescribeInstanceTypes` | GET/Query | Existing | **Non-mutating** | External | Returns per-instance-type network spec: `NetworkPerformance`, `NetworkCards[].BaselineBandwidthInGbps`, plus PPS/EFA/ENA fields | Yes (SigV4) | Any IAM principal with the action | Returns **public, account-independent** data. No resource-level scoping is meaningful (instance type is not a tenant resource). Console does **not** surface `BaselineBandwidthInGbps` → console-vs-API delta (Lens U, informational). |
| `Get-EC2InstanceType` | GET | Existing | Non-mutating | External | PowerShell wrapper of the above | Yes | Same | Same as above. |
| Network I/O credit bucket | — | Existing | n/a | **Internal (service plane)** | Token bucket governing burst; separate inbound/outbound | **No API** | None — platform only | No read/write API, no IAM action, no condition key. Not customer-observable except indirectly via throughput/driver metrics. |

**Undocumented/console-hidden knob sweep:** none found on this surface. There is no API parameter on this page that weakens auth or isolation. The only delta is **console omission of baseline-bandwidth display** (benign; the data is still public via the API). No `authorizerType`-style hidden permissive enum exists here.

**`[NEW]` / "focus on" markers:** none on this page. (The `C8in/C8ine/M8in/M8ine/M8idn/R8in/R8idn` row is a recent instance-family addition but carries no new *mechanism* — same shaping model.)

---

## 5. Recommended Areas of Focus

### Area 1 — Cross-tenant burst-bandwidth contention (shared-resource noisy neighbour)  ⭐ crown jewel
**Background:** "up to"-class instances (≤16 vCPU / `4xlarge` and smaller) burst above baseline using a network I/O credit mechanism. The docs state plainly: *"Instance burst is on a best effort basis, even when the instance has credits available, as burst bandwidth is a shared resource."* A "shared resource" on a multi-tenant host is the canonical noisy-neighbour surface.
**Security Concern:** if the shared burst pool is shared **across tenants co-resident on the same host (or same shaping domain)**, a tenant that aggressively bursts can starve a co-resident victim of burst bandwidth even while the victim holds credits — a cross-tenant availability impact the victim cannot prevent or attribute. This is the one place the feature's own wording concedes contention.
**High-level Test Scenarios:**
- **Claim:** Tenant A's sustained burst traffic on a small "up to"-class instance measurably reduces Tenant B's achievable burst throughput on a co-resident instance of the same class, below B's solo baseline-vs-burst profile. → **Mechanism:** "burst bandwidth is a shared resource", "best effort … even when the instance has credits available." → **Oracle:** controlled A/B throughput experiment under authorized test accounts — B's p50/p95 burst throughput with A idle vs A saturating, repeated, on deliberately co-located instances (same AZ, same type, ideally same placement/host). A statistically significant, repeatable drop in B's burst *attributable to A* confirms cross-tenant contention. → **Preconditions:** ability to co-locate two instances you control in separate accounts on the same shaping domain (hard to guarantee without host-placement control; use dedicated-host or cluster-placement tricks to raise co-residency odds). → **Cost:** medium (needs sustained traffic generation + co-residency). → **Severity:** cross-tenant DoS on shared infra = **High** *if* the contention crosses the account boundary and is attacker-controllable; **downgrade to out-of-scope "shared infra / best-effort by design"** if the impact is only within AWS's documented best-effort envelope and not attacker-steerable against a *chosen* victim. → **Stop condition:** if the probe starts measuring or manipulating the Nitro credit bucket itself rather than ordinary data-plane packets → HARD STOP (service plane).
**Doc evidence:** `ec2-instance-network-bandwidth.html`, "Available instance bandwidth" §, burst paragraph. **Severity-if-true:** High (cross-tenant) / else out-of-scope.

### Area 2 — Microburst monitoring blind spot (audit/observability evasion)
**Background:** The page documents that *"the network performance metrics would show that an allowance was exceeded and packets were dropped while the CloudWatch instance metrics do not … when the instance has a short spike in demand (a microburst) … CloudWatch metrics are not granular enough."* CloudWatch periods are 1-min or 5-min; the real shaping happens at microsecond scale.
**Security Concern:** a network-resource abuse (e.g. the Area-1 contention attack, or a self-inflicted allowance breach used to mask other activity) conducted at microburst scale leaves **no CloudWatch record** on the victim/operator side. The authoritative signal lives only in the **in-guest ENA driver metrics** — which a victim who hasn't installed the CloudWatch agent / isn't reading driver counters will never see. This is a documented detection gap that raises the severity of Area 1 by removing the defender's oracle.
**High-level Test Scenarios:**
- **Claim:** an allowance-exceeded/packet-drop event can be driven entirely within microburst windows such that CloudWatch `NetworkIn`/`NetworkOut`/packet-drop instance metrics show nothing, while ENA driver counters (`bw_in_allowance_exceeded`, `bw_out_allowance_exceeded`, `pps_allowance_exceeded`, etc.) increment. → **Mechanism:** the quoted granularity-gap paragraph + `monitoring-network-performance-ena` metric list. → **Oracle:** generate microburst traffic, then diff ENA driver counters (non-zero) against CloudWatch instance metrics (flat) over the same interval. → **Preconditions:** instance you control; ENA driver ≥ required version. → **Cost:** low. → **Severity:** **Low–Informational** as a standalone finding (it is documented behaviour), but a legitimate **enabler** that removes the defender's visibility for Area 1 — cite it there.
**Doc evidence:** "Monitor instance bandwidth" §. **Severity-if-true:** Low/Informational (enabler).

### Area 3 — `DescribeInstanceTypes` capability-reporting integrity & non-leakage (Lens U / A)
**Background:** The only API on the page returns `NetworkPerformance` and `BaselineBandwidthInGbps`. The docs also note the console does not display baseline bandwidth.
**Security Concern:** (a) does the API ever return anything **tenant-specific** (a live per-instance credit balance, a neighbour/co-residency hint, a host identifier) rather than the static per-instance-type spec? If so it becomes a co-residency/enumeration oracle. (b) Does the published bandwidth spec match what the control-plane API actually reports (doc-vs-API capability parity)?
**High-level Test Scenarios:**
- **Claim (refute-expected):** `DescribeInstanceTypes` returns only static, account-independent instance-type spec — identical across two unrelated accounts, with no per-instance or per-host field. → **Oracle:** call from two separate accounts, diff the full `NetworkInfo` block for the same instance type; any per-account/per-instance variance is a leak. → **Severity:** Info (expected identical). A variance would be Low–Medium (enumeration/co-residency oracle).
- **Claim:** the documented `BaselineBandwidthInGbps` table (c5 example) matches live `DescribeInstanceTypes` output field-for-field. → **Oracle:** diff the doc table against a live describe; a mismatch is a pure doc-vs-API capability inconsistency. → **Severity:** Informational (AWS-owned doc defect), worth filing only if a customer could build a compliance/attestation control on the false value.
**Doc evidence:** CLI/PowerShell blocks + "console does not display the baseline network bandwidth." **Severity-if-true:** Info / Low.

### Area 4 — Unenforceable-by-IAM posture gap (Lens U / S, documented-guarantee-vs-enforcement)
**Background:** Bandwidth, burst, and network I/O credits are entirely platform-governed. There is **no** `ec2:` condition key for bandwidth, baseline, burst, PPS, or credit state, and no API to cap them.
**Security Concern:** an org/security admin who wants to **prevent** a workload/account from consuming burst bandwidth (or to bound its network posture) cannot express that in IAM or an SCP keyed on a bandwidth/credit attribute — there is nothing to key on. This mirrors the confirmed pattern on sibling pages (see memory: `project_burstable-unlimited-mode-plan` / `standard-mode` — "NO CpuCredits-value IAM condition key"; and `instance-optimize-cpu` — no `ec2:CoreCount` key). The network equivalent is the same shape: the knob exists in the platform but is unscopable via IAM.
**High-level Test Scenarios:**
- **Claim:** no IAM condition key governs instance network bandwidth / burst / I/O-credit behaviour; therefore the only lever is *instance-type selection* (governable via `ec2:InstanceType` on `RunInstances`), not bandwidth itself. → **Oracle:** resolve the `ec2` IAM condition-key reference (Service Authorization Reference) and confirm absence of any bandwidth/credit/PPS key; confirm `ec2:InstanceType` is the only indirect lever. → **Preconditions:** none (doc/IAM-reference analysis). → **Cost:** low. → **Severity:** **Informational** — this is a design characteristic (same class AWS-owned gap as the CPU-credit pages), not an exploitable bug; document it so a downstream hunter doesn't chase a non-existent enforcement path.
**Doc evidence:** entire page (no IAM artifact present) + IAM reference. **Severity-if-true:** Informational.

### Area 5 — Routed-out referenced features (map the seam, hunt elsewhere)
This page *references* three features that carry their own, richer attack surface. **Do not deep-dive them here** — note the seam and route:
- **ENA Express** ("up to 25 Gbps between instances within the same AZ") — configurable feature with its own `ModifyNetworkInterfaceAttribute`/ENA-Express settings and a cross-instance data path. → route to the **ENA Express plan** (`ena-express*.md`). The relevant boundary question there: can ENA Express be established to/from an instance you don't own, or does it leak across accounts within an AZ?
- **Cluster placement group** ("up to 10 Gbps single-flow within the group") — co-residency/packing mechanics; see `placement-strategies` / cluster-placement coverage. Relevant to *raising co-residency odds* for Area 1.
- **Security-group connection tracking** ("connections tracked" maximum) — conntrack-exhaustion DoS has its own surface; see `security-group-connection-tracking.md`.
- **Link-local service PPS** (DNS / IMDS / Time Sync per-ENI PPS cap) — from `monitoring-network-performance-ena`; a per-ENI PPS cap on IMDS access is a self-DoS/availability angle, route to IMDS plans.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-tenant burst starvation | Shared burst-bandwidth pool | "best effort … shared resource" — attack the claim that best-effort contention never crosses the account boundary in an attacker-steerable way |
| Detection evasion of a network-allowance breach | CloudWatch vs ENA driver metrics | "CloudWatch metrics are not granular enough" — attack the assumption that allowance breaches are observable by the victim |
| Capability/spec leakage or mismatch | `DescribeInstanceTypes` | Implicit claim that the API returns only static public per-type spec — attack by diffing across accounts and against the doc table |
| Posture un-enforceability | IAM / SCP | Implicit claim that network posture is governable — attack by showing no condition key exists to bound it |
| Service-plane reach via the credit bucket | Nitro network card | Isolation of the credit-accounting plane from guests — **probe is HARD STOP on first contact** |

---

## 7. Out-of-Scope Risk Categories
- **Nitro / hypervisor network-shaping plane** — the credit bucket, packet-shaping/queueing logic, and per-instance allowance enforcement are AWS service plane. Any probe that reads or manipulates them is a **hard stop** → preserve evidence, disclose.
- **Single-tenant self-DoS** — an instance exhausting its *own* credits / hitting its *own* allowance and degrading *its own* throughput is documented, expected, out of scope.
- **Best-effort burst as designed** — contention within AWS's documented best-effort envelope, *not* attacker-steerable against a chosen cross-account victim, is a product characteristic, not a finding.
- **IMDS / DNS / Time Sync PPS caps on a managed host** — link-local service PPS limits; routed out; managed-host IMDS is out of scope per corpus norms.
- **Public instance-type spec data** — `NetworkPerformance`/`BaselineBandwidthInGbps` are intentionally public; reading them is not a disclosure.
- **ENA Express / cluster placement group / connection-tracking deep dives** — each has its own plan; only their *seam* to this page is in scope here.

---

## 8. Null Hypotheses / Doc Gaps
Lenses that do **not** fire on this page, with the pages checked (per skill discipline):

- **Lens A (IDOR):** no tenant resource-by-ID on this surface; `DescribeInstanceTypes` addresses public instance *types*, not tenant resources. Checked: full page + CLI/PowerShell examples. (The only residual A-flavoured test is the cross-account *non-leakage* check in Area 3.)
- **Lens B/C (PassRole / credential vending):** no role ARN input, no `AssumeRole`, no credential is created or vended. Checked: full page. **Null.**
- **Lens D/V (data→control escape / segmentation):** the only control-plane reach would be into the Nitro shaping plane — that is a **hard stop**, not a lead. No control ENI / control VPC is introduced by this feature. Network-segmentation deep work belongs to ENI/placement-group plans. **Null here** (beyond Area 1's contention framing).
- **Lens F (injection/translation):** no parser, translator, or wire-protocol layer; `--query` is client-side JMESPath. Checked: full page. **Null.**
- **Lens G (SSRF):** no field the service dereferences, fetches, previews, or renders. Checked: full page, CLI/PowerShell blocks, "Learn more" links. **Null.**
- **Lens H/W (KMS / attestation):** no KMS, no encryption context, no attestation. **Null.**
- **Lens I/S (tagging/ABAC / condition-key semantics):** no tagging API here, and — notably — **no condition key of any kind governs this feature** (documented as Area 4, the one substantive S-flavoured observation). No policy JSON is printed.
- **Lens J (OAuth/3P):** none. **Null.**
- **Lens K (prompt injection):** no LLM/agent. **Null.**
- **Lens L:** **FIRES** → Area 1 (shared burst resource).
- **Lens M (shared-id interception):** no session/presigned/one-time id. **Null.**
- **Lens N/X (namespace/action-parity):** single read-only action; no legacy alias or write twin. **Null.**
- **Lens O:** **FIRES** → Area 2 (microburst CloudWatch blind spot).
- **Lens P (identity proofing/registration):** no onboarding/gate/OTP. **Null.**
- **Lens Q (upload):** no upload or rich-content ingestion. Checked: full page. **Null.**
- **Lens R (AWS-authored IAM artifact):** **no IAM policy, managed policy, SLR, CFN snippet, or runbook permission block is printed on this page.** Checked: full page including CLI/PowerShell blocks (those are read-only describe examples, not policy artifacts). **Null — no shipped artifact to audit.**
- **Lens T (secret reachability):** the service generates/persists no secret. **Null.**
- **Lens U:** **FIRES (informational)** → Area 3 (console-vs-API display delta; doc-table-vs-API parity) and Area 4 (posture unenforceable by IAM).
- **Lens Y (transport/TLS/sig):** `DescribeInstanceTypes` uses the standard EC2 SigV4 endpoint; nothing feature-specific here. **Null** (covered generically by `ec2-api-intro` plan).
- **Lens AA (share/revoke):** no share/grant lifecycle. **Null.**

**Doc gaps:** the page does **not** state whether the burst-bandwidth "shared resource" pool is shared *across tenants* or only across an account's own instances on a host. This is the single ambiguity that decides whether Area 1 is High (cross-tenant) or out-of-scope (intra-account best-effort). **Mark Area 1 "confirm the sharing domain first"** — a hunter must establish co-residency and the cross-account contention experiment before rating it. ENA Express cross-account reachability within an AZ is likewise not specified here → confirm in the ENA Express plan.

---

## Priority order for a downstream hunter
1. **Area 1** (cross-tenant burst contention) — *only* substantive lead; gated on confirming the cross-account sharing domain (doc gap). Pair with Area 2 as the evasion enabler.
2. **Area 3** (`DescribeInstanceTypes` cross-account non-leakage diff) — cheap, fast, likely-refute but closes the enumeration-oracle question.
3. **Area 4** (IAM-unenforceability) — doc/IAM-reference confirmation, Informational, prevents wasted hunting on a non-existent enforcement path.
4. Route ENA Express / placement-group / conntrack to their own plans.
