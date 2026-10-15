# EC2 Instance Network Bandwidth — Attack Research Plan

> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html
> **Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md`
> **IAM authority:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`
> **Scope note:** single-account EC2, HTTP/application + control-plane layer only. This is a **concepts / capacity-governor page** (the shape of `fleet-quotas` and `AvailableIpPerENI`), not a CRUD-API page. The primary firing lenses are **L** (resource exhaustion / noisy neighbour), **U** (performance *guarantee* vs *enforcement*), **O** (detection/telemetry gap), and **S** (condition-key scoping). **V/D** (SRD cross-tenant) fires but is a **corroboration of the existing `ec2-networking` hub lead #3 (EFA/SRD)**, not net-new.
> **Drift check:** online == offline, byte-identical, for the target page **and** for the two child pages analysed (`monitoring-network-performance-ena.html`, `ena-express.html`). Verified 2026-10-15.

---

## 0. TL;DR — where the boundaries might not hold

1. **[L / U — HEADLINE] Burst bandwidth is a documented *shared, best-effort* resource with no per-tenant floor and no IAM lever.** The page states verbatim: *"Instance burst is on a best effort basis, even when the instance has credits available, as burst bandwidth is a shared resource."* A co-resident tenant that sustains burst-level egress can degrade a victim's burst throughput below what the victim's own credit balance would otherwise allow. **No condition key, quota, or API caps a principal's bandwidth consumption** — the only scoping that exists (`ec2:InstanceBandwidthWeighting`) governs the *EBS-vs-network split*, not the absolute rate. This is the strongest confirmed lead.

2. **[O — HEADLINE] Every bandwidth-exhaustion signal is guest-OS-only.** `bw_in/out_allowance_exceeded`, `pps_allowance_exceeded`, `conntrack_allowance_exceeded`, `linklocal_allowance_exceeded` are ENA driver counters read with `ethtool` **inside the guest**. They are **not** emitted to CloudWatch, EventBridge, or CloudTrail by default. An attacker throttling a victim (lead #1) produces **zero AWS-side telemetry** unless the victim has pre-wired a guest-side exporter → the victim cannot attribute, and the operator cannot detect, the degradation.

3. **[U — baseline is a floor-claim with no enforcement doc] "An instance receives the maximum number of network I/O credits at launch"** and the baseline is described as sustainable "indefinitely" — but the page never states what *enforces* the baseline against a noisy host. Baseline is presented as a guarantee; test whether it degrades under host contention (if it does, the "baseline" is itself best-effort and the guarantee is nominal).

4. **[S — condition-key gap, carefully framed] `ec2:InstanceBandwidthWeighting` is a REAL key** (String, *"Filters access by the bandwidth weighting of an instance"*) carried on the `instance` resource row of essentially every instance-targeting action, and is a meaningful *request* input on **RunInstances**, **ModifyInstanceNetworkPerformanceOptions**, and **ModifyInstancePlacement**. **Do not over-claim "no bandwidth key exists."** The accurate gap: this key governs only the `default | vpc-1 | ebs-1` weighting choice; **no** key governs baseline/burst *rate*, network-I/O-credit balance, or single-vs-multi-flow caps.

5. **[S / O — resource-less infra-performance actions] The four `*AwsNetworkPerformance*` actions are resource-less and scopable only by `ec2:Region`.** `Enable/DisableAwsNetworkPerformanceMetricSubscription`, `DescribeAwsNetworkPerformanceMetricSubscriptions`, `GetAwsNetworkPerformanceData` carry **no resource type and only `ec2:Region`** — any principal granted them toggles and reads **account-wide** inter-AZ/inter-Region infrastructure performance subscriptions; cannot be scoped to a tag, ARN, or team.

6. **[V/D — DEFER to hub lead #3] ENA Express/SRD routes packets across "different AWS network paths" with zero stated SG/NACL/VPC isolation mechanism.** Corroborating evidence (second product surface — EFA + ENA Express — on the identical unexplained-isolation SRD transport), **not a new lead**. Merge into `ec2-networking` hub lead #3.

---

## 1. Components, Assets, and Design

### What the page actually describes
A **capacity model**, not an API. The customer-facing "interface" is the set of bandwidth limits the EC2 data plane imposes on an instance's ENA network path, plus the read-only knobs that expose them.

- **Baseline bandwidth** — the rate an instance can sustain *indefinitely*. Property of instance type (`DescribeInstanceTypes` → `NetworkInfo.NetworkCards[0].BaselineBandwidthInGbps`).
- **Burst bandwidth** — a higher rate, available for a limited time, funded by the **network I/O credit** mechanism. Explicitly **best-effort and shared** ("burst bandwidth is a shared resource").
- **Network I/O credits** — bucket model. *"An instance receives the maximum number of network I/O credits at launch."* *"A stopped instance does not earn network I/O credits."* **Separate inbound and outbound buckets.**
- **Flow classification** — a "flow" is a 5-tuple:
  - **Multi-flow aggregate:** `< 32 vCPU` → 5 Gbps; `> 32 vCPU` → 50 % of aggregate; a named set of 8th-gen instances (C8in/C8ine, M8in/M8ine/M8idn, R8in/R8idn) are baseline-only for multi-flow.
  - **Single-flow (one 5-tuple):** limited to **5 Gbps** unless both endpoints are in the **same cluster placement group** → **10 Gbps**; or **ENA Express** → **25 Gbps** (same-AZ per the bullet; SRD transport itself is intra-Region).
  - **MPTCP** noted as a way to spread one logical connection across multiple sub-flows.
- **Microburst** paragraph — sub-second spikes can exceed the measured average and hit the limit invisibly to coarse monitoring.

### Assets at stake
- A tenant's **effective throughput** (availability/QoS asset) — degradable by a co-tenant via the shared burst pool.
- The **network-I/O-credit balance** — an availability asset with no API to read it from the control plane (guest-side `ena` counters only).
- The **inter-AZ/inter-Region infrastructure-performance subscription + data** (account-wide config asset) — toggled/read by resource-less IAM actions.

### Identity / control surface
- SigV4 IAM. The only *mutating* control-plane knobs this page implies:
  - `RunInstances` (launch with a chosen `InstanceBandwidthWeighting` + placement group + instance type).
  - `ModifyInstanceNetworkPerformanceOptions` (change the weighting post-launch; `instance*` resource).
  - `ModifyInstancePlacement` (move an instance into/out of a placement group; `instance*` + `placement-group` + `dedicated-host` rows).
  - `Enable/DisableAwsNetworkPerformanceMetricSubscription` (resource-less).
- Read-only: `DescribeInstanceTypes`, `GetAwsNetworkPerformanceData`, `DescribeAwsNetworkPerformanceMetricSubscriptions`.

### ASCII — where contention and blindness live
```
   Tenant A instance ─┐
   Tenant B instance ─┼──► shared host NIC / network segment ──► AWS backbone
   Victim instance   ─┘        ▲                    ▲
                                │                    │
              "burst = shared resource,       SRD spreads flows across
               best effort" (Lens L/U)        "different AWS network paths"
                                                     (Lens V/D → hub #3)
   Guest OS: ethtool -S  ◄── bw_*/pps_/conntrack_ allowance counters
             (Lens O: guest-only; no CloudWatch/CloudTrail by default)
```

---

## 2. Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Co-tenant instance (same host/segment) | Victim's effective burst throughput | Shared, best-effort burst pool ("burst bandwidth is a shared resource") | Victim's sustained throughput measurably drops **below its own credit-funded burst rate** while a co-tenant saturates the shared pool |
| Co-tenant instance | Victim's **baseline** throughput | Host NIC contention | Victim cannot sustain the documented **baseline** rate (baseline is claimed sustainable "indefinitely") — proves baseline is itself best-effort |
| Any IAM principal with the action | Account-wide infra-performance subscription | Resource-less `Enable/Disable/Describe/GetAwsNetworkPerformanceData`, only `ec2:Region` | A principal the operator expected to be scoped to one tag/team toggles or reads subscriptions for the **whole account/region** |
| IAM principal | Instance bandwidth-vs-EBS weighting | `ModifyInstanceNetworkPerformanceOptions` / `ModifyInstancePlacement` + `ec2:InstanceBandwidthWeighting` | Weighting changed on an instance the policy author believed scoped — **test what the key actually gates vs. what the UG implies** |
| SRD-routed flow (ENA Express/EFA) | VPC/SG/NACL isolation | SRD "distributes packets across different AWS network paths" | **DEFER:** any evidence SRD transport bypasses SG/NACL enforcement → `ec2-networking` hub lead #3 |
| Guest workload | AWS-side detection | ENA allowance counters are guest-OS-only | A throttling event leaves **no** CloudWatch metric / CloudTrail event by default |

---

## 3. API / interface surface (bandwidth-relevant subset of `list_ec2`)

| Name | Mutating | Resource row(s) | Bandwidth-relevant condition keys | Notes |
|---|---|---|---|---|
| `RunInstances` | yes | `instance*` (+ many) | `ec2:InstanceBandwidthWeighting`, `ec2:InstanceType`, `ec2:PlacementGroup`, `ec2:Tenancy` | Launch-time choice of weighting, type, and CPG — the only point all three bandwidth-shaping inputs co-occur |
| `ModifyInstanceNetworkPerformanceOptions` | yes | `instance*` | `ec2:InstanceBandwidthWeighting` (+ generic instance set) | Post-launch weighting change. **The page's named "modify the weighting" action.** |
| `ModifyInstancePlacement` | yes | `instance*`, `placement-group`, `dedicated-host` | `ec2:InstanceBandwidthWeighting`, `ec2:PlacementGroup`, `ec2:Tenancy` | Move in/out of a CPG → changes the single-flow 5→10 Gbps bump; weighting key present but inert to placement |
| `DescribeInstanceTypes` | no | *(resource-less)* | region/generic | Read oracle for Baseline/Burst/NetworkPerformance — **public spec data → Lens A NULL** |
| `EnableAwsNetworkPerformanceMetricSubscription` | yes | **none** | **`ec2:Region` only** | Resource-less; account-wide infra-perf subscription toggle |
| `DisableAwsNetworkPerformanceMetricSubscription` | yes | **none** | **`ec2:Region` only** | Resource-less |
| `DescribeAwsNetworkPerformanceMetricSubscriptions` | no | **none** | **`ec2:Region` only** | Resource-less list oracle |
| `GetAwsNetworkPerformanceData` | no | **none** | **`ec2:Region` only** | Resource-less read of inter-AZ/Region performance |

**`ec2:InstanceBandwidthWeighting` — exact definition (from `list_ec2.md` L10089):** `| ec2:InstanceBandwidthWeighting | Filters access by the bandwidth weighting of an instance | String |`. Possible values are the weighting enum (`default`, `vpc-1`, `ebs-1`) per the UG. It appears on the generic `instance`-resource condition-key set, so it is *listed* on dozens of instance actions (AssociateAddress → RunInstances), but only functions as a request-shaping control on the three mutating actions above; elsewhere it is a resource-attribute match on the instance's current weighting.

**Console-hidden / under-surfaced knob check:** `ModifyInstanceNetworkPerformanceOptions` is reference-documented but barely surfaced in the UG prose; the weighting enum values are the "undocumented knob" to enumerate against the console. No value weakens isolation per se, but the asymmetry (API accepts weighting change; UG under-describes it) is a Lens-S/U audit item.

---

## 4. Boundary-lens catalogue (fired + null, with pages named)

### Lens L — Resource exhaustion / noisy neighbour  **[PRIMARY — FIRES]**
- **Trigger:** page states burst is a *shared resource*, best-effort, with separate finite inbound/outbound credit buckets; single-flow and aggregate caps.
- **Claim 1:** A co-resident tenant sustaining high egress degrades a victim's *burst* throughput below the rate the victim's own credit balance would fund. → **Mechanism:** *"Instance burst is on a best effort basis, even when the instance has credits available, as burst bandwidth is a shared resource."* → **Oracle:** victim's measured throughput falls while victim still shows positive credits and a co-tenant saturates the segment. → **Severity:** Medium–High (cross-tenant QoS DoS, availability only). *Requires co-residency — hard to force in single-account scope; frame as "the doc concedes the shared-pool contention; quantify the achievable degradation."*
- **Claim 2 (credit-starvation):** An attacker who controls a victim's *inbound* flow (e.g. a public service on the victim) can drain the victim's **inbound** credit bucket independently of outbound, since buckets are separate. → **Oracle:** `bw_in_allowance_exceeded` climbs under attacker-driven ingress while outbound is unaffected. → **Severity:** Medium (remote, no co-residency needed if victim exposes an ingress endpoint).
- **Claim 3 (pps / conntrack, not just bytes):** `pps_allowance_exceeded` and `conntrack_allowance_exceeded` are separate ceilings — a high-pps/low-byte or many-connection flood exhausts an allowance the byte-rate caps never show. → **Oracle:** small-packet or many-flow flood trips pps/conntrack counters while bw counters stay green. → **Severity:** Medium.
- **No IAM/quota mitigation exists:** confirmed — no condition key or Service Quota caps per-principal bandwidth/pps/credit consumption (only `ec2:InstanceCount`/`TargetInstanceCount` exist, instance-count not rate; same conclusion as `AvailableIpPerENI` and `fleet-quotas`).

### Lens U — Guarantee vs enforcement  **[PRIMARY — FIRES]**
- **Trigger:** words "baseline … sustain … indefinitely", "maximum number of credits at launch", "best effort", "shared resource".
- **Claim:** The **baseline** is presented as a dependable floor, but no sentence names the mechanism that enforces it against host contention. If baseline degrades under a noisy host, the floor is nominal. → **Oracle:** under heavy co-tenant load, victim cannot hold documented baseline. → **Severity:** High-if-true (undermines the one stated guarantee). → **Preconditions:** co-residency; measurement.
- **Secondary claim (launch-credit reset):** "maximum credits at launch" + "stopped instance earns no credits" implies **stop/start resets the credit bucket to full**. A workload that stop/starts frequently gets repeated full burst allocations — a possible fairness/abuse pattern worth confirming (does a rapid stop/start loop farm burst credits?). → **Severity:** Low–Medium.

### Lens O — Detection / audit evasion  **[PRIMARY — FIRES]**
- **Trigger:** monitoring page (`monitoring-network-performance-ena.md`, 320 lines, subagent-analysed) exposes all allowance counters **only via the guest ENA driver (`ethtool -S`)**.
- **Claim:** A bandwidth/pps/conntrack-exhaustion attack (Lens L) generates **no** CloudWatch metric, EventBridge event, or CloudTrail entry by default; detection requires the victim to have pre-deployed a guest-side exporter (CloudWatch agent custom metrics). → **Oracle:** reproduce an allowance-exceeded event; confirm nothing appears in the victim's CloudWatch/CloudTrail without guest instrumentation. → **Severity:** High as a force-multiplier on Lens L (the attack is both effective *and* invisible/unattributable).
- **Corollary:** `conntrack_allowance_available` is a *point-in-time* gauge only; there is no historical/aggregated AWS-side record — post-incident forensics are impossible without prior guest logging.

### Lens S — Condition-key scoping  **[FIRES — framed precisely]**
- **Fired finding A:** `ec2:InstanceBandwidthWeighting` exists and is real; it scopes the **weighting** input on Run/Modify actions. **The genuine gap is the absence of any key for the *rate* dimension** (baseline, burst, credit balance, flow caps). An operator cannot write "deny launching instance types above N Gbps baseline" except indirectly via `ec2:InstanceType` allow-lists.
- **Fired finding B (resource-less infra-perf actions):** the four `*AwsNetworkPerformance*` actions carry **no resource type and only `ec2:Region`** → cannot be scoped by tag/ARN/team. A least-privilege policy for "view network performance" necessarily grants account-wide reach within the region. **Oracle:** a principal intended to be tag-scoped successfully calls `GetAwsNetworkPerformanceData` / toggles subscriptions for resources it doesn't "own". → Severity: Low–Medium (config/visibility, not data exfil).
- **Audit item:** does `ec2:InstanceBandwidthWeighting` behave as a `RequestTag`-style request key on Modify (gates the *new* value) or a resource key (gates the *current* value), or both? The reference lists it on the resource row; confirm whether a `Condition` on the *desired* new weighting is actually enforced at `ModifyInstanceNetworkPerformanceOptions` call time.

### Lens V / D — Network segmentation / SRD cross-tenant  **[FIRES → DEFER to hub lead #3]**
- **Trigger:** single-flow 10 Gbps requires same cluster placement group; 25 Gbps requires ENA Express/SRD; SRD "distributes packets for each network flow across different AWS network paths."
- **Finding (from subagent):** across `ena-express*.md` there is **zero** mention of security groups, NACLs, VPC, or any isolation mechanism for SRD-routed traffic — in contrast to AWS's usual "SGs/NACLs still apply" framing. SRD adds its own header (lower MTU ⇒ encapsulation). CPG "can span peered VPCs in the same Region"; **silence on whether a CPG can span accounts.**
- **Disposition:** **This is the same SRD transport as EFA — corroborating evidence for the existing `ec2-networking` hub lead #3, not a new lead.** Add ENA Express as a second affected product surface under that lead. Open sub-question kept there: *does SG/NACL enforcement apply to SRD-routed packets, and can a CPG span accounts?*
- **Doc-vs-doc inconsistency to record:** the target page scopes ENA Express benefit to "same AZ"; `ena-express.md` says SRD communication is same-AZ **or** cross-AZ intra-Region. Minor scoping error in the parent page's framing.

### Lens A — Read oracle / information disclosure  **[NULL — pages named]**
- Pages checked: target page's `DescribeInstanceTypes` reference (`NetworkInfo.NetworkPerformance`, `NetworkCards[0].BaselineBandwidthInGbps`) and `GetAwsNetworkPerformanceData`.
- Verdict: **NULL.** `DescribeInstanceTypes` returns **public instance-type spec data** (identical for every account; published on the EC2 instance-types site) — no tenant-specific disclosure. Same conclusion the `AvailableIpPerENI` plan reached. `GetAwsNetworkPerformanceData` returns aggregate AWS *infrastructure* latency/loss between AZs/Regions, not other-tenant data — moved to Lens S (scoping) rather than A (disclosure).

### Lenses explicitly NULL (triggers absent on this page and its two children)
- **B (confused deputy / PassRole):** no role-ARN input on any bandwidth action. NULL — checked `RunInstances`/`Modify*` rows (no `iam:PassRole` seam specific to bandwidth).
- **C (credential vending / session scope):** no STS/token surface. NULL.
- **E (RBAC/privilege-escalation across roles):** no role model on this page. NULL.
- **F (translation-layer / injection):** no customer-input→downstream-language transform. NULL.
- **G (SSRF):** no field the service dereferences. NULL — target + monitoring + ena-express pages read; no URL/URI/endpoint input.
- **Q (blob parsing):** no upload/attachment. NULL.
- **P (gate before privileged state change):** no identity/OTP/uniqueness gate. NULL.
- **R (shipped IAM/CFN sample policy):** none printed on these pages. NULL (but see `monitoring-network-performance-ena` for CloudWatch-agent config snippets — operational, not an IAM artifact).
- **T (generated secret storage):** none. NULL.

---

## 5. Prioritised leads (NEW / highest-signal first)

| # | Lens | Lead | Confirm/refute oracle | Severity-if-true | Confidence |
|---|---|---|---|---|---|
| 1 | L+O | Co-tenant burst-pool contention degrades a victim below its credited burst rate, **invisibly** (no AWS-side telemetry) | Co-resident load test; victim throughput drops with positive credits; nothing in victim CloudWatch/CloudTrail | High (cross-tenant QoS DoS, unattributable) | Med (doc concedes shared pool; co-residency hard to force) |
| 2 | L | Separate inbound/outbound + pps + conntrack ceilings each exhaustible independently; remote ingress flood drains victim inbound credits without co-residency | Attacker-driven ingress trips `bw_in_allowance_exceeded`/`pps`/`conntrack` while byte-rate caps stay green | Medium (remote, no co-residency) | Med-High |
| 3 | U | "Baseline sustainable indefinitely" is best-effort in practice — degrades under host contention | Baseline unachievable under heavy co-tenant load | High (nominal guarantee) | Low-Med |
| 4 | S | Resource-less `*AwsNetworkPerformance*` actions grant account-wide reach, scopable only by region | Tag-scoped principal successfully toggles/reads account-wide subscription | Low-Med (config/visibility) | **High (confirmed from `list_ec2`)** |
| 5 | U | Stop/start resets credit bucket to full ("max credits at launch", "stopped earns none") → burst-credit farming via rapid cycle | Rapid stop/start loop repeatedly restores full burst allowance | Low-Med | Med |
| 6 | S | `ec2:InstanceBandwidthWeighting` request-time enforcement semantics on `ModifyInstanceNetworkPerformanceOptions` (gates new value? current value? both?) | Policy denying a target weighting value either blocks or fails to block the Modify call | Low (hardening) | Med |
| 7 | V/D | **DEFER** — SRD (ENA Express) rides the same unexplained-isolation transport as EFA | — | — | **Merge into hub lead #3** |

**Doc-gaps to resolve before hunting:** (a) whether `ena-express` SRD traffic is subject to SG/NACL (hub #3); (b) whether a cluster placement group can span accounts (page silent); (c) exact `InstanceBandwidthWeighting` enum values and their rate effect (UG under-documents).

---

## 6. Hunter preconditions & scope guardrails
- All of leads #1–#3 require **two instances the researcher owns** (synthetic, canary workloads) and ideally forced co-residency (cluster placement group in one account) — single-account, no cross-tenant target. Measure with `iperf3` + guest `ethtool -S` ENA counters.
- Lead #4 is confirmable **from IAM alone** (policy simulator) — no data-plane action needed.
- **Hard stops:** do not attempt to force co-residency with a *foreign* tenant; do not probe AWS infrastructure endpoints via `GetAwsNetworkPerformanceData` beyond reading one's own account's subscription. Any SRD-isolation test that touches another account = stop, preserve evidence, route to hub lead #3 owner.

## 7. What could not be fully tested from docs
- Actual achievable co-tenant degradation magnitude (requires live measurement).
- Whether baseline is enforced or best-effort (doc does not say; empirical only).
- SRD↔SG/NACL interaction (doc-silent; deferred to hub #3).
- `InstanceBandwidthWeighting` request-vs-resource enforcement semantics (reference lists the key; behaviour needs a live policy test).

## 8. Cross-references
- Parent hub: `ec2-networking` hub plan — add ENA Express under **hub lead #3 (EFA/SRD cross-tenant isolation)** as a second product surface.
- Sibling capacity-governor plans (same L/U/O shape, same "no IAM key caps capacity" conclusion): `fleet-quotas`, `AvailableIpPerENI`.
- IAM authority: `list_ec2.md` — `ec2:InstanceBandwidthWeighting` @L10089 (def), @L8867 `ModifyInstanceNetworkPerformanceOptions`, @L8873 `ModifyInstancePlacement`, @L9585 `RunInstances`; `*AwsNetworkPerformance*` @L6618/7770/8023/8210 (all resource-less, `ec2:Region`-only).

---
*Online == offline verified 2026-10-15 for target + `monitoring-network-performance-ena` + `ena-express`. No sync drift.*
