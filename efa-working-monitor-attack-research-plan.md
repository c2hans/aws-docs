# EFA Monitoring (`efa-working-monitor.html`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-working-monitor.html` (offline mirror `./docs/AWSEC2/latest/UserGuide/efa-working-monitor.md`, 206 lines, **offline == online verified 2026-10-15**). IAM cross-checks from `./docs/service-authorization/latest/reference/list_ec2.md`. Status: documentation-derived hypotheses only; nothing tested against a live account.

**Relationship to the EFA plan family (READ FIRST — this is a page-level deep-dive child, not a standalone):**
This plan is the **page-level deep-dive CHILD of `efa-attack-research-plan.md` (the EFA hub)** for the dedicated monitoring page `efa-working-monitor.html`. It **deepens the hub's Area 6** ("OS-bypass monitoring & forensic blind spots", Lens O), which already summarizes this page at the paragraph level. This plan does **not** restate the hub's area-level analysis — it cross-references it and owns the granular, net-new observability surface the hub left at summary level. Hard de-dup against siblings:
- **SRD/RDMA cross-tenant memory-isolation mechanism itself** (whether cross-tenant RDMA reach *exists*) → **hub Area 4 (HARD STOP)** and `efa-start-attack-research-plan.md` Area C. This plan owns the *observability/confirmation instrument* for that hypothesis, not the hypothesis.
- **Whether an SG actually filters SRD/RDMA payload traffic** → **hub Area 7** (Lens X/AA). This plan owns only the flow-log *shape* consequence for detection.
- **EFA software supply chain** (installer TOFU, unpinned deps) → **hub Area 5**; `check-ena-express-settings.sh`-style guest scripts → `ena-express-attack-research-plan.md`.
- **`CloudWatchAgentServerPolicy` over-broad / unscoped IAM audit** → `monitoring-network-performance-ena-attack-research-plan.md` (already owns the CloudWatch-agent managed-policy critique). This plan cross-refs it and does not re-audit the policy.
- **Nitro flow-cache / tracked-flow-survives-SG-revoke** detection mechanism → `ena-nitro-perf-attack-research-plan.md`.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **This page describes NO AWS API.** Every surface is one of three guest/VPC-side read paths: (a) in-guest EFA driver counters via `rdma-tool` / sysfs, (b) VPC Flow Logs, (c) the CloudWatch agent / Container Insights. So the classic cross-tenant-API lenses (A/B/C/E/H/I/T/…) do not fire on the page's *own* content; they are recorded as explicit nulls in §8 with the pages checked. The live leads are concentrated in **Lens O (audit/detection evasion)** and **Lens U/A (metrics as a cross-instance observability oracle & side-channel)**.
- **HARD STOP:** the moment a *live* test using these counters produces evidence of cross-tenant RDMA reach (another account's bytes landing in / being read from your instance, or your bytes reaching another account) — stop, preserve the counter evidence, flag for AWS-Security disclosure. That is hub Area 4 territory; this plan's role ends at "the counter proves it."

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Confirm or refute hub Area 4 using the driver counters as the instrument.** Prove whether `rdma_write_bytes` ("bytes written to it by *other instances*") / `rdma_read_bytes` / `rdma_read_resp_bytes` increment on instance **A** as a direct result of RDMA issued from a non-cooperating instance **B** — and whether B can be in a different account/tenant on the same cluster/fabric. A non-zero cross-tenant increment is the breach oracle for the HARD STOP.
2. **Establish the EFA/SRD traffic detection blind-spot.** Show that a VPC-Flow-Log-based detection pipeline built for IP 5-tuples cannot match EFA rows (MAC-formatted `srcAddress`/`destAddress`, `sourcePort`/`destPort`/`protocol` = `-`), so an EFA lateral pivot is invisible to such rules.
3. **Establish the EKS/Container-Insights SRD-anomaly blind-spot.** Show that the five SRD-health counters most useful for spotting adversarial fabric behavior are exactly the ones Container Insights omits.
4. **Establish the counter-reset anti-forensics primitive.** Show that a driver reset zeroes cumulative counters an operator alarms on.
5. **Assess the SRD metrics as a cross-tenant fabric side-channel** (does one tenant's traffic measurably move another tenant's `impaired_remote_conn_events` / `unresponsive_remote_events` / `retrans_*`).

## 2. Components, Assets, and Design

**What the page actually describes (mechanism, not marketing).** Three monitoring channels for an EFA-attached instance:

1. **EFA driver counters (guest-local, real-time).** The EFA kernel driver publishes 22 cumulative counters per EFA device "since instance launch or the last driver reset." Read two ways, both requiring **in-guest shell** on the instance:
   - `rdma -p statistic show` (the `rdma-tool` from `rdma-core`; man page `man7.org/linux/man-pages/man8/rdma.8.html` — an upstream Linux tool, not an AWS-shipped artifact).
   - `more /sys/class/infiniband/{device}/ports/{port}/hw_counters/* | cat` — raw sysfs, e.g. device `rdmap0s31`, port `1`.
   - Counter families (verbatim semantics from the table):
     - **Local tx/rx:** `tx_bytes`, `rx_bytes`, `tx_pkts`, `rx_pkts`, `rx_drops` (all EFA instance types).
     - **Send/recv (two-sided):** `send_bytes`, `recv_bytes`, `send_wrs`, `recv_wrs`.
     - **RDMA one-sided (cross-instance memory):** `rdma_write_wrs`, `rdma_read_wrs`, **`rdma_write_bytes` = "The number of bytes written to it by *other instances* using rdma write operations"**, `rdma_read_bytes` = "bytes received using rdma read operations", `rdma_write_wr_err`, `rdma_read_wr_err`, `rdma_read_resp_bytes` = "bytes sent in response to rdma read operations", `rdma_write_recv_bytes` = "bytes received by rdma write operations".
     - **SRD fabric health (Nitro v4+ only):** `retrans_bytes`, `retrans_pkts`, `retrans_timeout_events` ("times EFA SRD traffic timed out and resulted in a network path change"), `impaired_remote_conn_events` ("times EFA SRD connections entered an impaired state, resulting in a reduced throughput rate limit"), `unresponsive_remote_events` ("times an EFA SRD remote connection was unresponsive").
2. **VPC Flow Logs.** EFA traffic can be captured in a flow log and published to **CloudWatch Logs or S3**. EFA rows are identified by `srcAddress`/`destAddress` **formatted as MAC addresses**, with `sourcePort`/`destPort`/`protocol` rendered as `-`. Documented example row shows `action = ACCEPT`, `log-status = OK`.
3. **CloudWatch.** The **CloudWatch agent** collects the driver counters and publishes them to CloudWatch (external page `AmazonCloudWatch/.../CloudWatch-Agent-EFA.html`). For EKS, **Container Insights** supports all driver metrics **except** `retrans_bytes`, `retrans_pkts`, `retrans_timeout_events`, `unresponsive_remote_events`, `impaired_remote_conn_events`.

**Ownership / trust framing.** The driver counters and sysfs are **guest-OS-local** — the customer owns the guest; reading your own counters crosses no boundary. The *interesting* property is that `rdma_write_bytes` and the RDMA-recv counters are **populated by remote peers' actions on your memory region**, i.e. they are the one place a tenant can *observe the effect of another instance's one-sided RDMA on itself*. VPC Flow Logs and CloudWatch are AWS data-plane services with their own IAM/delivery roles (generic, deferred). No per-EFA / per-counter IAM action or condition key exists.

```
  Instance A (tenant X)                         Instance B (tenant Y?)
  guest OS                                       guest OS
   ├─ rdma-tool / sysfs hw_counters              ├─ issues RDMA write/read over SRD
   │    rdma_write_bytes  <── incremented by ────┘   (one-sided; A's kernel NOT in path)
   │    rdma_read_resp_bytes
   │    impaired_remote_conn_events  <── reflects fabric/peer state (shared SRD substrate)
   │
   ├─ (OS-bypass: EFA frames never hit guest netstack)
   │
   └─ CloudWatch agent ──► CloudWatch metrics        VPC Flow Log ──► CWL / S3
                                                       srcAddress/destAddress = MAC
                                                       ports/protocol = "-"   (not a 5-tuple)
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Remote instance B (same cluster; possibly another tenant) | Instance A's memory region | one-sided RDMA write/read over SRD | **`rdma_write_bytes` / `rdma_read_resp_bytes` on A increments due to B's action** = cross-instance memory touch observed; if B is another account → HARD STOP (hub Area 4). |
| Co-resident tenant on shared SRD fabric | Instance A's SRD-health counters | shared fabric substrate state leaks into `impaired_remote_conn_events` / `unresponsive_remote_events` / `retrans_*` | A's SRD-health counter moves measurably in response to B's traffic = cross-tenant fabric **side-channel** (topology/neighbor inference). |
| Attacker with in-guest access on a compromised instance | historical SRD anomaly record | driver reset zeroes cumulative counters | post-reset counters read 0 while operator's alarm baseline is destroyed = anti-forensics. |
| EFA lateral-mover | defender's flow-log detection pipeline | EFA rows carry MAC addrs + `-` ports/proto | a flow-log rule written for IPv4/IPv6 5-tuples does not match EFA rows = detection evasion. |
| EKS/container workload operator | SRD anomaly visibility | Container Insights omits 5 SRD counters | adversarial fabric behavior produces no Container-Insights signal = EKS detection gap. |
| Any customer surface | AWS service plane | — | not reachable from this page's content; §8 null. |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `rdma -p statistic show` | guest CLI (`rdma-core`) | existing | No (read) | guest-local | read EFA driver counters | No | in-guest shell | upstream Linux tool; not AWS-shipped. No supply-chain surface on *this* page. |
| `more /sys/class/infiniband/.../hw_counters/*` | sysfs read | existing | No | guest-local | read raw counters | No | in-guest shell | counters populated partly by **remote** peers (RDMA recv family). |
| VPC Flow Log (create / read) | VPC API + CWL/S3 | existing | create = mutating | external (data-plane) | capture EFA traffic metadata | via console/API | flow-log role / log-destination IAM | generic VPC feature; delivery role & S3/CWL authz are **out of this plan's scope** (generic VPC Flow Logs). Page only documents the EFA-specific *row shape*. |
| CloudWatch agent (EFA plugin) | agent → `cloudwatch:PutMetricData` | existing | mutating (publishes metrics) | external | ship driver counters to CloudWatch | — | instance role w/ `CloudWatchAgentServerPolicy` | **IAM audit deferred** to `monitoring-network-performance-ena` sibling. |
| Container Insights (EKS) | CW agent / addon | existing | — | external | container metric collection | — | cluster/instance role | omits the 5 SRD counters (§Area M4). |
| `ec2:MonitorInstances` / `ec2:UnmonitorInstances` | EC2 API | existing | mutating | external | toggle *EC2 detailed monitoring* (1-min CW), **unrelated to EFA driver counters** | yes | `instance*`-scoped (no fleet/EFA key) | tangential; EFA driver metrics do NOT flow through this. Recorded to prevent a false lead. |

**No `[NEW]` marker on this page.** No non-SDK/console-hidden knob (the page exposes no API parameters at all).

## 5. Recommended Areas of Focus (ranked)

### Area M1 — [HEADLINE] The RDMA-recv driver counters are the cross-instance-memory observability oracle — the live instrument for hub Area 4's HARD STOP (Lens U / A)
**Background.** The driver table documents, verbatim, that `rdma_write_bytes` is *"The number of bytes written to it **by other instances** using rdma write operations"*, alongside `rdma_read_bytes`, `rdma_read_resp_bytes`, and `rdma_write_recv_bytes`. These are the only guest-readable signals whose value is produced by **another instance's one-sided RDMA against this instance's memory region** — the EFA data path explicitly bypasses the guest kernel, so these counters are the *sole* in-guest evidence that a remote peer touched local memory.
**Security Concern.** Hub Area 4 and `efa-start` Area C pose the Critical-if-true hypothesis that cross-tenant RDMA reach exists on the shared SRD fabric. That hypothesis is *un-observable from any AWS API* — but it is **directly measurable** from these counters. This page therefore supplies the confirmation instrument that makes the hub's HARD-STOP question falsifiable in a lab:
- **Attacker-side confirmation:** instance B issues an RDMA write/read against a target address/rkey; B's own `rdma_write_wrs`/`rdma_read_wrs` + bytes confirm the op was accepted by the fabric (did not error locally) — distinguishing "QP connect refused" from "op delivered."
- **Victim-side confirmation (the breach oracle):** instance A's `rdma_write_bytes` / `rdma_write_recv_bytes` / `rdma_read_resp_bytes` **increment** when and only when a remote peer actually wrote-to / read-from A's registered memory. A non-zero increment on A caused by a peer A never authorized at the application layer = proof the memory region was reachable; if that peer is in **another account**, HARD STOP.
- **Defender value (dual-use):** because these counters are cumulative and guest-local, they are *also* the only way a victim could ever notice they were RDMA-read by a neighbor — and there is **no API equivalent**, so a defender without in-guest access is blind.
**High-level Test Scenarios.**
- *Claim:* A's `rdma_write_bytes` increments by exactly the payload B wrote, with A's application never having initiated the transfer → *Oracle:* two-instance canary (same account first), pre-read A's `rdma_write_bytes`, have B perform a known-size `ibv_post_send(RDMA_WRITE)` to A's registered buffer, re-read; delta == payload confirms observability. Then repeat with B in a **second account** sharing the cluster/placement-group/RAM-shared SG — a non-zero delta is the HARD-STOP breach. *Preconditions:* two EFA instances, ability to register MRs and exchange rkeys (or to brute an rkey — see hub Area 4). *Cost:* low (lab). *Severity:* **the instrument is Informational; a non-zero cross-account delta is Critical + HARD STOP** (reported under hub Area 4).
- *Adjacent:* does `rdma_read_resp_bytes` on A reveal that a peer *read* A's memory (exfil direction), giving the victim an exfil-detection signal the API lacks?
**Doc evidence:** efa-working-monitor.md (driver-metrics table, `rdma_write_bytes` "by other instances"). **Severity-if-true:** instrument Informational; realized cross-tenant RDMA = Critical.

### Area M2 — [in-scope, Low–Medium] SRD-health counters as a cross-tenant fabric side-channel + the counter-reset anti-forensics primitive (Lens A side-channel / O)
**Background.** `retrans_bytes`, `retrans_pkts`, `retrans_timeout_events`, `impaired_remote_conn_events`, `unresponsive_remote_events` (Nitro v4+) describe the state of the **remote** side of SRD connections and the shared network path: timeouts "resulted in a network path change", impaired state "reduced throughput rate limit", remote "unresponsive". These values are a function of the shared SRD substrate, not purely of local behavior.
**Security Concern.**
- **Side-channel:** on a shared fabric, one tenant's traffic volume/pattern can plausibly move a co-resident tenant's `impaired_remote_conn_events` / `retrans_timeout_events` (path contention, rate-limit events). If measurable, these counters leak coarse neighbor-activity / topology signal across the tenant boundary with no API and no log — a classic noisy-neighbor side-channel turned into an inference primitive.
- **Anti-forensics (deepens hub Area 6):** counters are cumulative "since instance launch or **the last driver reset**." An attacker with in-guest root who can reload/reset the EFA driver (module reload, interface bounce) zeroes `retrans_*` and the `*_remote_*` anomaly counters — exactly the signals an operator alarms on for adversarial fabric behavior — while the instance keeps running. There is no documented tamper-evident record of the reset in the counter channel itself.
**High-level Test Scenarios.**
- *Claim:* instance A's `impaired_remote_conn_events` / `retrans_timeout_events` respond measurably to co-resident instance B's traffic burst → *Oracle:* hold A idle, baseline counters, drive heavy SRD traffic from B (same placement group), observe whether A's SRD-health counters move; a repeatable correlation = cross-tenant side-channel. *Severity:* **Low–Medium** (coarse inference; higher if it discriminates specific neighbors).
- *Claim:* a driver reset zeroes SRD anomaly counters mid-run → *Oracle:* generate `retrans_*`/`impaired_*` events, reset the EFA driver, confirm counters read 0 while the instance stays up. *Severity:* **Low–Medium** (detection enabler; raises severity of hub Areas 2–4 by erasing their evidence trail).
**Doc evidence:** efa-working-monitor.md (SRD counter semantics; "since instance launch or the last driver reset"). **Severity-if-true:** Low–Medium.

### Area M3 — [in-scope, Low–Medium] VPC-Flow-Log MAC-address shape = EFA/SRD traffic is invisible to IP-5-tuple detection (Lens O, deep layer under hub Area 6)
**Background.** The page states EFA flow-log rows carry `srcAddress`/`destAddress` **formatted as MAC addresses**, with `sourcePort`/`destPort`/`protocol` shown as `-`. The single documented example is `action = ACCEPT`, `log-status = OK`; the doc **never shows a REJECT row and never discusses whether SGs filter SRD payload at all** (open silence shared with hub Area 7).
**Security Concern.** Nearly all VPC-Flow-Log detection content (GuardDuty-style analytics, SIEM parsers, allow/deny-list rules, exfil-volume alerts) is written against **IPv4/IPv6 5-tuples**. An EFA row has no IP addresses, no ports, and no protocol — so:
- A detection rule keyed on `srcaddr`/`dstaddr` as IPs **silently fails to match** every EFA row → a lateral pivot or data movement conducted over EFA/RDMA produces flow-log entries that existing rules skip. The data is captured but un-actionable by standard tooling.
- MAC-address identifiers are **per-ENI**, not per-account/per-identity, giving defenders a far weaker correlation key than an IP (no reverse DNS, no SG/subnet inference, no WHOIS). Attribution of an EFA flow across a fleet is materially harder.
- Because `protocol`/`ports` are blank, **volume-based exfil alarms that threshold on a (proto,port) tuple never fire** for EFA traffic; only the raw `bytes`/`packets` columns remain, and only if a rule was built to read EFA-shaped rows.
- The ACCEPT-only example + the SG-vs-SRD silence means a defender cannot tell from the docs whether a REJECT would ever appear for SRD traffic (i.e. whether SGs even gate it) — if SGs don't filter SRD (hub Area 7), there is no DENY row to detect on, closing the last flow-log-based control.
**High-level Test Scenarios.**
- *Claim:* a flow-log alerting pipeline built for IP 5-tuples does not match EFA rows → *Oracle:* enable a flow log on an EFA ENI, generate EFA traffic, confirm rows carry MAC `srcAddress`/`destAddress` and `-` ports/protocol; run a representative IP-5-tuple detection rule and confirm zero matches. *Severity:* **Low–Medium** (detection enabler; raises severity of any EFA lateral-movement finding).
- *Claim:* no REJECT row is ever emitted for SRD traffic (SG does not gate it) → *Oracle:* with a self-ref SG narrowed, generate EFA traffic and inspect flow log for a REJECT row; absence corroborates hub Area 7's "SG may be vestigial for SRD." *Severity:* Low (confirms hub Area 7 framing).
**Doc evidence:** efa-working-monitor.md (flow-log section, example row). **Severity-if-true:** Low–Medium. Cross-ref hub Area 6 (summary) and Area 7 (SG-vs-SRD).

### Area M4 — [in-scope, Low] EKS Container Insights omits exactly the five SRD-anomaly counters (Lens O)
**Background.** The page states Container Insights "supports all of the EFA driver metrics, **except**: `retrans_bytes`, `retrans_pkts`, `retrans_timeout_events`, `unresponsive_remote_events`, and `impaired_remote_conn_events`."
**Security Concern.** The excluded five are precisely the SRD-health/anomaly counters most useful for spotting adversarial or anomalous fabric behavior (retransmission storms, impaired/unresponsive remote connections, path changes). A containerized / EKS workload therefore has a **structural blind-spot**: an operator relying on Container Insights for EFA observability sees throughput but not the anomaly signals that would flag a fabric-level attack or a noisy/hostile neighbor. This narrows the already-thin detection surface (M2/M3) further for the EKS population specifically.
**High-level Test Scenarios.** *Claim:* generating `retrans_*`/`impaired_*`/`unresponsive_*` events in an EKS pod produces no corresponding Container Insights metric while the same events are visible via in-pod `rdma-tool` → *Oracle:* run the canary in EKS, drive SRD anomalies, diff Container Insights metrics vs guest counters. *Severity:* **Low** (detection gap scoped to EKS; enabler, not a primitive).
**Doc evidence:** efa-working-monitor.md (CloudWatch section, Container Insights exclusion list). **Severity-if-true:** Low.

### Area M5 — [POINTER, no new analysis] CloudWatch agent IAM & supply chain
The CloudWatch agent that ships these counters runs under an instance role with `CloudWatchAgentServerPolicy`. **The over-broad/unscoped critique of that managed policy is already owned by `monitoring-network-performance-ena-attack-research-plan.md`** (Lens R/S) and is not re-audited here. The agent install/config supply chain is generic CloudWatch-agent (external page `CloudWatch-Agent-EFA.html`), not an EFA-specific artifact; EFA installer supply chain → hub Area 5. No net-new work on this page.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-instance RDMA write/read observed via `rdma_write_bytes` / `rdma_read_resp_bytes` increment | EFA driver counters (guest) | none on this page — counters are *descriptive*; isolation claimed elsewhere (hub Area 4). The counter *confirms* a breach rather than preventing it. |
| Cross-tenant fabric side-channel via SRD-health counters | `impaired_remote_conn_events` etc. | none documented; shared-fabric contention is unaddressed. |
| Anti-forensic counter reset | EFA driver | none — doc states counters reset on driver reset with no tamper-evidence. |
| EFA lateral movement invisible to flow-log detection | VPC Flow Logs | none — MAC-shaped rows with `-` ports/proto; ACCEPT-only example; SG-vs-SRD unspecified. |
| EKS SRD-anomaly blind-spot | Container Insights | none — five SRD counters explicitly excluded. |

## 7. Out-of-Scope Risk Categories
- **The SRD/RDMA memory-isolation mechanism itself** (whether cross-tenant reach exists) — owned by **hub Area 4 (HARD STOP)** / `efa-start` Area C. This plan ends at "the counter proves it"; it does not pursue the fabric exploit.
- **`CloudWatchAgentServerPolicy` / CloudWatch-agent IAM audit** — owned by `monitoring-network-performance-ena-attack-research-plan.md`.
- **Generic VPC Flow Logs delivery role, S3/CWL destination authz, log-tampering** — generic VPC feature, not EFA-specific; only the EFA *row shape* is in scope here.
- **EFA installer / `rdma-core` / CloudWatch-agent install supply chain** — hub Area 5; `rdma-tool` is upstream Linux (`man7.org`), not an AWS-shipped artifact.
- **Single-tenant self-DoS, IMDS on managed hosts, in-guest root already assumed** — out of scope per standard framing (reading your own counters crosses no boundary).
- **SG-vs-SRD enforcement** (is a self-ref SG vestigial for SRD payload) — owned by **hub Area 7**; this plan only notes the flow-log REJECT-silence corroboration.

## 8. Null hypotheses / doc gaps (lenses checked, with pages)
- **Lens A (cross-tenant resource-by-ID IDOR):** NULL for the page's own content — efa-working-monitor.md exposes **no AWS API, no resource ID, no tenant field**; all reads are guest-local or your-own-account flow logs/metrics. The *side-channel/observability* variant of A fires instead (Area M1/M2). Pages checked: the full target page.
- **Lens B / C (PassRole / credential vending):** NULL — no role ARN, no AssumeRole, no credential input anywhere on the page. (CloudWatch agent role → deferred to ENA sibling, not a page lead.) Pages checked: target page.
- **Lens D / V (data→control plane / network reachability):** deferred — the page is observability-only; the actual SRD/control-plane reachability question is hub Area 4/Area V. No new reachability content here.
- **Lens E (RBAC privesc):** NULL — no roles defined on the page.
- **Lens F (parser / injection):** NULL-dominant — `rdma-tool` and sysfs are read-only numeric counters; flow-log rows are AWS-generated. Theoretical: a downstream SIEM that regex-parses the MAC-shaped flow-log row could mis-parse (consumer-owned, inherits consumer severity) — recorded as a thin indirect note under M3, not a page primitive. Pages checked: target page (counter output format, flow-log example).
- **Lens G (SSRF):** NULL — no field the service dereferences; `rdma-tool` man-page URL and the CloudWatch/VPC doc links are static documentation references, not server-side-fetched inputs. Pages checked: target page (all URLs are doc hyperlinks).
- **Lens H (KMS / encryption context):** NULL — no KMS, no encryption context on the page (flow-log destination encryption is generic VPC/S3, deferred).
- **Lens I / S (tagging / condition-key):** NULL on the page — **no EC2 IAM action or condition key governs EFA driver counters** (confirmed: `list_ec2.md` has no EFA/rdma/counter/`InterfaceType` key; apparent grep hits were "Def**efa**ult" substring false-positives). `ec2:MonitorInstances`/`UnmonitorInstances` are `instance*`-scoped and unrelated to EFA driver counters (recorded in §4 to kill a false lead).
- **Lens K (prompt injection):** NULL — no LLM/agent on the page.
- **Lens L (resource exhaustion):** NULL on the page — counters are fixed-cardinality (22 metrics); no parser/upload/limit surface. Metric cardinality in CloudWatch is a cost concern, not a cross-tenant DoS.
- **Lens M (shared-identifier interception):** NULL — no session/token/presigned-URL on the page.
- **Lens N (ARN/namespace migration):** NULL — no ARN or dual-namespace on the page.
- **Lens O (audit/detection evasion):** **FIRES** — Areas M2 (counter-reset anti-forensics), M3 (flow-log MAC blind-spot), M4 (EKS gap). This is the page's primary live surface.
- **Lens P (proofing/registration):** NULL — no registration/verification workflow.
- **Lens Q (upload):** NULL — no upload/blob field.
- **Lens R (AWS-authored IAM artifact):** deferred — only artifact in reach is `CloudWatchAgentServerPolicy`, owned by the ENA-monitoring sibling.
- **Lens T (secret reachability):** NULL — the page generates/persists no secret.
- **Lens U (doc-guarantee vs enforcement):** **FIRES weakly** — the page makes no explicit security *guarantee* to violate, but the metric semantics ("bytes written to it by other instances") *document* the cross-instance-RDMA capability whose isolation is only asserted elsewhere; Area M1 uses this as the confirmation instrument. Also the ACCEPT-only flow-log example + SG-vs-SRD silence (M3) is a doc-gap feeding hub Area 7.
- **Lens W (attestation):** NULL — no attestation/enclave content.
- **Lens X / AA (action-family parity / revoke lifecycle):** deferred to hub Area 7 (SG-revoke-vs-SRD) and `ena-nitro-perf` (tracked-flow-survives-SG-revoke); nothing net-new on this page.
- **Lens Y (transport/TLS/sig):** NULL — no endpoint, no signature on the page; flow-log/CloudWatch transport is generic AWS data-plane.
- **Lenses BB/CC/DD/EE/FF:** NULL — no multi-parser request path, no asserted-identity header, no caching layer, no predictable-name resolution, no token validation on the page. Pages checked: target page in full.

**Carried doc-gaps for the hunter:**
1. **Does `rdma_write_bytes` on the victim actually increment for a non-cooperating remote write, and can the remote be cross-account?** (M1 — the load-bearing live question; also the hub Area 4 oracle.)
2. **Do SRD-health counters measurably respond to a co-resident tenant's traffic?** (M2 side-channel — unquantified; needs a two-instance correlation test.)
3. **Is any REJECT row ever emitted for SRD traffic, or do SGs not gate it at all?** (M3 ↔ hub Area 7.)
4. **Is a driver reset itself recorded anywhere tamper-evidently** (CloudTrail/console), or is the counter-reset fully silent? (M2 anti-forensics completeness.)
5. **Exact `/sys/class/infiniband` device/port enumeration under multi-EFA (`efa-acc-inst-types`) instances** — whether per-NetworkCard counters are separable (cross-ref `efa-acc-inst-types-attack-research-plan.md`).

---
*Cross-references: [[efa-attack-research-plan]] (hub — Areas 4, 6, 7), [[efa-start-attack-research-plan]] (Area C cross-tenant RDMA), [[monitoring-network-performance-ena-attack-research-plan]] (CloudWatchAgentServerPolicy audit, fragment-proxy detection blind-spot), [[ena-nitro-perf-attack-research-plan]] (tracked-flow-survives-SG-revoke), [[efa-acc-inst-types-attack-research-plan]] (multi-NIC counter separability). See [[reference-aws-iam-service-auth-ref-url]].*
