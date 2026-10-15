---
source_page: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html
offline_mirror: /work/aws-docs/docs/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.md
generated: 2026-10-15
skill: security-questionbuilder
plan_type: page-level COMPLEMENT (sits beside enhanced-networking-ena hub + ec2-instance-network-bandwidth + ena-express)
drift_check: online .md == offline .md, byte-identical (both subagents confirmed; only offline source_url front-matter differs)
---

# Monitor network performance for ENA — Attack / Research Plan

> **Scope note (read first).** This page (`monitoring-network-performance-ena.html`) is the **observability
> contract** for EC2 network governors: it defines the six ENA-driver allowance counters, the NEW fragment-proxy
> mode, the metric-persistence/reset semantics, and every retrieval surface (Linux `ethtool`, CloudWatch agent,
> Windows `EnaPerfCounters.man`, DPDK `dpdk-testpmd`, FreeBSD `sysctl`). It is **already referenced** by three
> existing sibling plans. This plan is deliberately a **COMPLEMENT**, not a duplicate. It owns the net-new,
> currently-unowned surface and **defers** everything the siblings already own, with explicit cross-references.
>
> **Ownership split (settled before writing):**
> - **This plan OWNS:** (1) the fragment-proxy-mode allowance-bypass [Lens U/L — NEW feature]; (2) the
>   conntrack *governor depth* via `security-group-connection-tracking` (idle-timeout attack-budget asymmetry,
>   exhaustion-behavior ambiguity, untracked-flow footgun) [Lens L]; (3) the link-local/IMDS/DNS/Time-Sync PPS
>   ceiling as an ungoverned single-ENI chokepoint + the IMDS-credential-refresh erosion chain [Lens U]; (4) the
>   `CloudWatchAgentServerPolicy` AWS-managed IAM-artifact audit [Lens R/S]; (5) metric-reset-as-evidence-destruction
>   + guest-only-telemetry blind spot [Lens O]; (6) the DPDK/FreeBSD/Windows retrieval supply-chain surface [Lens Q,
>   informational].
> - **DEFER to `ec2-instance-network-bandwidth-attack-research-plan.md`:** bandwidth/PPS shared-pool noisy-neighbor
>   mechanics, burst-credit bucket behavior, `ec2:InstanceBandwidthWeighting` key audit, and the headline
>   "every bandwidth signal is guest-OS-only" Lens-O finding. This plan's conntrack/link-local Lens-O findings are
>   the *same pattern extended* to those two governors — stated as a page-family-wide confirmation, not a restatement.
> - **DEFER to `ena-express-attack-research-plan.md`:** all `ena_srd_*` metrics and any SRD-transport
>   SG/NACL-bypass / cross-tenant segmentation question. (The only verbatim "Persistence" sentence on the entire
>   page physically lives inside the ENA-Express metrics section — a load-bearing scoping detail, see §5 Lens O.)
> - **DEFER to `enhanced-networking-ena-attack-research-plan.md` (hub):** ENA driver install/upgrade trust path,
>   `RegisterImage`/`enaSupport` AMI write-path, Windows driver-package supply chain (hub Area 4). This plan only
>   adds the *monitoring-specific* retrieval artifacts the hub does not enumerate.
> - **DEFER to `using-instance-addressing` / IMDS plans:** IMDSv2 hop-limit/token auth-bypass. This plan touches
>   IMDS **only** as an *availability* target of link-local PPS exhaustion (U2), never its authentication model.

---

## 0. Target & Method

- **Target page:** EC2 User Guide → "Monitor network performance for the ENA settings on your EC2 instance."
- **Doc provenance:** offline mirror + online `.md` twin both read by two independent subagents; **byte-identical,
  no drift** (both confirmed; the lone diff is the mirror's injected `source_url` front-matter, not page content).
- **Method:** security-questionbuilder boundary-lens pass. Documentation-only; every lead below is a **falsifiable
  hypothesis with a confirm/refute oracle a hunter executes later** against an authorized account. No live testing
  was performed here.
- **Supporting pages read:** `security-group-connection-tracking.md`, `ec2-instance-network-bandwidth.md`,
  `CloudWatch-Agent-network-performance.md`, `CloudWatchAgentServerPolicy.md` (AWS-managed policy JSON),
  `instance-metadata-security-credentials.md`, `enhanced-networking-ena.md`, `list_cloudwatch.md` (service-auth ref).

---

## 1. Components, Assets, and Design

**What the page actually is.** A read-only telemetry/observability contract. It does not expose a mutating API; its
security interest is almost entirely in **(a)** what the counters *mean* about the underlying governors (which the
page is the authoritative definition for), **(b)** the one *behavioral* toggle it documents (fragment proxy mode),
and **(c)** the trust/supply-chain properties of the retrieval surfaces.

**The six ENA-driver counters (base metrics, read in-guest via `ethtool -S eth0`):**

| Counter | Governor it reflects | Scope |
|---|---|---|
| `bw_in_allowance_exceeded` / `bw_out_allowance_exceeded` | inbound/outbound aggregate bandwidth ceiling | per-instance *(defer to bandwidth plan)* |
| `pps_allowance_exceeded` | aggregate packets-per-second ceiling | per-instance *(defer to bandwidth plan)* |
| `conntrack_allowance_exceeded` | security-group connection-tracking table | **per-instance (this plan)** |
| `conntrack_allowance_available` | remaining tracked-connection headroom (Nitro only) | **per-instance, point-in-time gauge (this plan)** |
| `linklocal_allowance_exceeded` | PPS to local proxy services (Amazon DNS + IMDS + Time Sync) | **per-ENI (this plan)** |

> Doc defines base counters as *"the cumulative number of packets queued or dropped on each network interface
> **since the last driver reset**."* Enforcement is described only as AWS *"shapes the traffic ... by queueing and
> then dropping network packets"* — token-bucket parameters and whether shaping is in the Nitro card vs hypervisor
> are **undocumented** (genuine doc gap, not an assertable finding).

**The NEW behavioral toggle — fragment proxy mode (verbatim):**
> *"If fragment proxy mode is enabled for the Linux driver, egress fragment drops bypass the 1024 PPS limit that
> usually applies and are counted within standard PPS allowances. Fragment proxy mode is disabled by default."*
> Requirements: *"To override the egress fragment PPS limit of 1024, install ENA driver version 2.13.3 or later."*
> DPDK equivalent: *"DPDK driver v25.03 or later supports fragment proxy mode."*

**Retrieval surfaces (each a distinct interface / potential supply-chain seam):**
- **Linux:** `ethtool -S eth0` (kernel/driver pull, requires in-guest privilege).
- **CloudWatch agent:** optional push exporter; `ethtool` plugin must explicitly list each counter in
  `metrics_include` — *"This metric is collected only if you have listed it in the `ethtool` subsection..."*
- **Windows:** copy `EnaPerfCounters.man` from the driver package into `%SystemRoot%\System32\drivers`, register via
  `lodctr /m:EnaPerfCounters.man` (unregister `unlodctr`).
- **DPDK:** `dpdk-testpmd` example app.
- **FreeBSD:** `sysctl dev.ena.*.eni_metrics`.

**Assets at stake:** instance/ENI network availability (DoS target); the integrity of the *only* abuse-signal the
customer is pointed to; the CloudWatch namespace/log-group integrity reachable via the shipped agent role; the
in-guest-vs-AWS-side durability gap of the telemetry itself.

**Connection sketch:**
```
   [governors, enforced in Nitro/ENA shaping layer]           [AWS-side durable logs]
   bandwidth / pps / conntrack / link-local-PPS                 CloudTrail  VPC Flow Logs
            │  (drops increment kernel counters)                   ▲  (NEITHER records a
            ▼                                                      │   governor-drop event)
   ENA driver counters  ──ethtool -S──►  in-guest only  ──opt-in CloudWatch agent──►  CloudWatch
   (reset on reboot/terminate/detach)      (ephemeral)        (PutMetricData via CloudWatchAgentServerPolicy)
            ▲
   fragment proxy mode (guest driver v2.13.3+ / DPDK 25.03+) flips a host-side shaping ceiling, NO AWS API
```

---

## 2. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| In-guest process (any tenant, own instance) | host-side egress-fragment shaper (1024 PPS ceiling) | install ENA driver ≥2.13.3 + enable fragment proxy mode | **Egress-fragment throughput materially exceeds 1024 PPS with no AWS-side API call, event, or operator warning** → an ungoverned, undetectable self-service ceiling raise |
| In-guest process (own instance) | conntrack table of the same instance | open many tracked connections until table full | New connections dropped (expected); **if *existing* established connections also drop, the self-DoS budget is far smaller than documented** |
| In-guest process (own instance) | link-local proxy services (Amazon DNS / IMDS / Time Sync) on own ENI | sustained PPS flood to 169.254.169.x | **SDK/CLI calls begin failing with `ExpiredToken` because link-local drops starved IMDS credential refresh past the 5-min buffer** — a data-plane flood degrading a control-plane credential |
| Operator (defender) | link-local PPS ceiling | attempt SG/NACL rule on 169.254.169.254 / .123 | **No SG/NACL/IAM lever exists to contain or throttle it** (control-surface absence = the breach) |
| EC2 instance role carrying `CloudWatchAgentServerPolicy` | *any* CloudWatch namespace / *any* Logs log-group in the account | `PutMetricData` / `logs:CreateLogGroup` with no `cloudwatch:namespace` / no log-group-ARN condition | **Writing a metric into `AWS/EC2` or a victim team's custom namespace, or a log group the agent should never touch** → cross-team telemetry poisoning |
| Attacker who generated abuse traffic on a compromised instance | the only in-guest record of that abuse | reboot / terminate / detach ENI | **Counters reset to 0; if no CloudWatch agent was pre-installed, no AWS-side record of the abuse window exists at all** → self-service evidence destruction |
| Any customer surface | AWS Nitro / host shaping plane | — | **HARD STOP.** The shaping/enforcement layer is AWS's service plane. Confirm existence of a *guest-observable* effect only; never probe or reach the host enforcement mechanism itself. Preserve evidence, flag for disclosure. |

---

## 3. API / Interface Surface

This page is **non-mutating / read-only**; it names no customer-facing EC2 control-plane API. The surface is
retrieval interfaces + one guest-driver toggle + one adjacent IAM artifact.

| Name | Type | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ethtool -S eth0` | in-guest syscall/driver | No (read) | No | in-guest root/privileged | Primary surface; suppressible/observable only by in-guest actor |
| CloudWatch agent `ethtool` plugin | guest daemon → `PutMetricData` | push | No (egress to CW) | instance role | Opt-in; each counter must be listed in `metrics_include` |
| **fragment proxy mode** | ENA driver (Linux ≥2.13.3) / DPDK ≥25.03 config | **Yes — flips a shaping ceiling** | No | in-guest root | **No AWS API field, no `describe-*`/`modify-network-interface-attribute` surface, no IAM/SCP lever** — console-hidden-knob delta is total |
| `lodctr /m:EnaPerfCounters.man` | Windows perf-counter registration | writes to `System32\drivers` | No | in-guest admin | Manifest copied from "the driver installation package"; no checksum step documented |
| `dpdk-testpmd` | DPDK example app | read | No | in-guest, built from DPDK | diagnostic only |
| `sysctl dev.ena.*.eni_metrics` | FreeBSD sysctl | read | No | in-guest | diagnostic only |
| `CloudWatchAgentServerPolicy` | **AWS-managed IAM policy (shipped artifact)** | n/a | n/a | attached to EC2 instance roles fleet-wide | Audited statement-by-statement in §5 Lens R/S |

**Undocumented/console-hidden knob (per skill's Step-3 hunt):** fragment proxy mode is accepted and effective at
the ENA driver layer but surfaced **nowhere** in the EC2 console, the EC2 API reference, or any instance/ENI
attribute. The most-permissive state ("enabled") raises a host-side anti-abuse ceiling with **zero operator
warning and zero AWS-side footprint.** This is the sharpest console-vs-mechanism delta on the page.

---

## 4. Mandatory Coverage Sweep (lens-trigger enumeration)

- **URL/host fields the service dereferences (Lens G):** none on this page. The counters reference 169.254.169.x
  link-local destinations but the page does not accept a caller-supplied URL. **NULL — page read in full.**
- **Uploaded/parsed blobs (Lens Q):** `EnaPerfCounters.man` (XML manifest copied into `System32\drivers`); DPDK
  app binary; driver packages. Covered §5 Lens Q (informational).
- **Gates before privileged state change (Lens P):** none — no proofing/OTP/uniqueness workflow on this page. **NULL.**
- **"Revealed only after <step>" (Lens A disclosure-timing):** none. **NULL.**
- **IAM policy JSON / named managed policy (Lens R/S):** `CloudWatchAgentServerPolicy` — **present, audited in full.**
- **Secrets/keys the service persists (Lens T):** none generated by this page. **NULL.**
- **Security *guarantees* asserted (Lens U):** (a) 1024-PPS egress-fragment ceiling "usually applies"; (b)
  link-local PPS "does not impact traffic to custom DNS resolvers"; (c) counters are "per instance" / "per network
  interface" (isolation claim); (d) IMDS credentials made available "at least five minutes before" expiry. All four
  traced to mechanism in §5.

---

## 5. Boundary-Lens Catalog (the questions)

### Lens U — Documented guarantee vs. enforcement  *(primary lens for this page)*

**U-FRAG [HEADLINE / NEW feature] — Fragment proxy mode is an ungoverned, undetectable, guest-side raise of a host anti-abuse ceiling.**
- **Claim:** A tenant can unilaterally remove the 1024-PPS egress-fragment ceiling for its own ENI by installing ENA
  Linux driver ≥2.13.3 (or DPDK ≥25.03) and enabling fragment proxy mode — with **no** control-plane API, IAM action,
  SCP, or operator warning anywhere in the documentation set, and **no** AWS-side (CloudTrail/API) footprint.
- **Mechanism (doc):** fragment-proxy footnote + requirements sentence (quoted §1). Confirmed absent from the EC2 API
  reference, `enhanced-networking-ena.md`, and any `modify-network-interface-attribute`/`describe-instance-attribute`
  surface — the only documented levers are "install driver version X" (kernel) and "install DPDK version X" (userspace),
  both internal to the guest OS.
- **What changes OFF→ON:** OFF (default) a host-side shaper enforces a hard 1024-PPS ceiling specifically on *egress
  fragments*, separate from the instance's normal PPS allowance; ON folds that traffic into the regular
  `pps_allowance_exceeded` budget, i.e. the *fragment-specific* sub-limit disappears (the overall instance PPS max
  still applies underneath).
- **Confirm/Refute oracle:** on an authorized Nitro instance, pin ENA driver below vs at/above 2.13.3 (same instance
  type/size), flood egress UDP fragments >1024 PPS, and compare observed egress-fragment throughput + `pps_allowance_exceeded`
  deltas across both driver versions and both mode states. Material increase in sustained egress-fragment throughput
  past 1024 PPS once enabled (with non-fragment PPS allowance unaffected) **confirms** "guest-controlled, ungoverned
  ceiling raise." Independently grep the full EC2 API reference for any `FragmentProxyMode`-shaped field — absence
  **corroborates** "no IAM/SCP lever."
- **Severity if true:** Medium. Legitimate AWS capability, not a bug — but a per-guest, driver-version-gated expansion
  of egress-fragment throughput that bypasses a specific anti-abuse shaping ceiling, is invisible to the account
  owner/security team unless they inspect `ethtool -i` driver versions in-guest, and has zero API/CloudTrail footprint.
  Relevant to **fragmentation-based IDS evasion and fragmented-UDP reflection/amplification** research: a tenant can
  locally raise its own egress-fragment ceiling with no AWS-side visibility or governance.
- **HARD STOP boundary:** confirm the *guest-observable* throughput change only. Do **not** attempt to probe or map the
  host-side shaper itself.

**U-LINKLOCAL-1 — Single per-ENI link-local PPS ceiling for IMDS + Amazon DNS + Time Sync, with no SG/NACL/IAM control surface.**
- **Claim:** `linklocal_allowance_exceeded` reflects one shared PPS ceiling governing Amazon DNS, IMDS, and Time Sync
  together, and no security-group, NACL, or IAM condition key exists to throttle, contain, or scope it.
- **Mechanism (doc):** metrics table — *"...the PPS of the traffic to local proxy services exceeded the maximum for
  the network interface. This impacts traffic to the Amazon DNS service, the Instance Metadata Service, and the Amazon
  Time Sync Service, but does not impact traffic to custom DNS resolvers."* Grep across
  `configuring-instance-metadata-options.md`, `instance-metadata-limiting-access.md`,
  `security-group-connection-tracking.md` found **zero** SG/NACL/firewall control over link-local traffic (the only
  IMDS control is hop-limit/IMDSv2 token = a *consumer-side authN* control, not a rate/reachability control).
  Consistent with the documented fact that SGs have no effect on Route 53 Resolver / AmazonProvidedDNS traffic.
- **Confirm/Refute oracle:** attempt an SG/NACL rule targeting 169.254.169.254 (IMDS) / 169.254.169.123 (Time Sync),
  confirm no effect (matching the documented DNS baseline); grep the EC2 service-authorization reference for any
  link-local-PPS condition key (expect none).
- **Severity if true:** Medium-High — a single ENI-wide ceiling that an in-guest actor (compromised sidecar/container,
  malicious co-process, or the instance's own workload) can exhaust with **no operator-available guardrail** to contain it.

**U-LINKLOCAL-2 — Sustained link-local PPS exhaustion can erode the IMDS credential-refresh 5-minute safety margin.**
- **Claim:** A sustained (not microburst) link-local PPS flood that repeatedly fails the IMDS credential-refresh poll
  can push a dependent SDK/CLI past the documented 5-minute pre-expiry buffer into real credential expiration — a
  silent availability failure whose root cause is invisible unless `linklocal_allowance_exceeded` is already exported.
- **Mechanism (doc, chained):** `instance-metadata-security-credentials.md` — *"We make new credentials available at
  least five minutes before the expiration of the old credentials."* (the only documented slack) × the page's statement
  that link-local PPS loss manifests as dropped packets to IMDS specifically.
- **Confirm/Refute oracle:** sustain a link-local-PPS-saturating load for >5 min against an instance actively polling
  IMDS for role credentials; observe whether SDK calls begin failing with `ExpiredToken`/`InvalidClientTokenId`.
- **Severity if true:** High (turns a cosmetic-sounding "packets dropped" metric into a control-plane-credential outage)
  — **but** the actor must already be able to generate sustained traffic to the instance's own link-local destinations,
  which in practice means code already running on the instance (self-DoS), since 169.254.169.x is not internet-routable.
- **Confidence:** Medium — both the buffer and the drop mechanism are independently documented; the causal chain is a
  plausible but untested inference, flagged as such.

**U-LINKLOCAL-3 — "Does not impact custom DNS resolvers" carve-out: verify it just *moves* the traffic to a different governor.**
- **Claim:** custom-resolver traffic is exempt from the link-local ceiling but presumably rides the general
  `pps_allowance_exceeded`/`bw_*` ceilings instead — i.e. the carve-out relocates rather than removes governance.
- **Oracle:** during a link-local exhaustion event, confirm custom-resolver queries keep resolving while
  AmazonProvidedDNS/IMDS/Time-Sync drop, and confirm custom-resolver traffic instead increments `pps_allowance_exceeded`.
- **Severity:** Low if carve-out holds (confirms doc; yields a defender mitigation for U2 — move to a custom resolver);
  Medium if refuted (doc inaccuracy with operational impact).

### Lens L — Resource exhaustion / noisy-neighbor (conntrack governor depth)

**L-CT-1 — Conntrack is a strictly per-instance self-DoS governor (negative cross-tenant finding, stated explicitly).**
- **Claim:** Unlike the burst-*bandwidth* pool (which the sibling bandwidth plan confirms is a *shared, cross-tenant*
  resource), the conntrack table is per-instance; exhausting one instance's table should not affect a co-resident one.
- **Mechanism (doc):** `security-group-connection-tracking.md` — *"Amazon EC2 defines the maximum number of
  connections that can be tracked **per instance**."* No shared-pool language anywhere.
- **Oracle:** saturate one owned instance's conntrack table; observe whether a second co-resident instance's
  `conntrack_allowance_available` moves. **Expect refute (no cross-tenant effect).**
- **Severity:** negative result if refuted (expected) — but a *valuable* one: it draws the sharp line that
  bandwidth/PPS governors are shared-pool while conntrack is per-instance-isolated. High only if a cross-tenant effect
  is unexpectedly found (would contradict documented isolation).

**L-CT-2 — Exhaustion behavior on *existing* connections is doc-ambiguous.**
- **Claim:** at table-full, the doc says *"any packets that are sent or received are dropped because a new connection
  cannot be established"* — conflating "new connection" with "any packets," which may mean established flows also drop.
- **Oracle:** hold several long-lived tracked connections open on a victim while flooding new-connection attempts until
  `conntrack_allowance_exceeded` increments; check whether the pre-existing established connections survive.
- **Severity if existing connections also break:** Medium — turns a new-connection-only limit into a full instance
  network outage reachable from a smaller attack budget.

**L-CT-3 — Idle-timeout default asymmetry: non-Nitro-v6 (432000s) is a far cheaper low-and-slow conntrack-DoS target than Nitro v6 (350s).**
- **Claim:** the 5-day (432000s) default idle timeout on non-Nitro-v6 instances lets a slow trickle of idle
  half-open/established connections accumulate against the ceiling for days, making low-and-slow exhaustion cheap;
  Nitro v6's 350s default sharply reduces that budget.
- **Mechanism (doc):** *"Default: 350 seconds for Nitro v6 ... 432000 seconds for all other instance types."* +
  AWS's own warning to *"test your applications on Nitro v6 ... with the reduced 350 second default ... before
  deploying to production."* — AWS itself recognizing the old default as DoS-friendly.
- **Oracle:** compare time-to-exhaustion for an identical connection-opening rate against a Nitro-v6 vs non-v6 instance.
- **Severity if true:** Medium (self-DoS, but quantifies the asymmetry and anchors it to AWS's own change rationale).

**L-CT-4 — Untracked-flow footgun (owner-side availability, not an attacker primitive).**
- **Claim:** a 0.0.0.0/0 ⇄ 0.0.0.0/0 all-traffic rule pair makes a flow *untracked*, and *"an untracked flow of
  traffic is immediately interrupted if the rule that enables the flow is removed or modified"* — so an SG edit instantly
  kills in-flight untracked sessions (tracked ones survive narrowing).
- **Oracle:** confirm an SG narrowing on an untracked (all-traffic-both-directions) rule set instantly drops in-flight
  sessions vs the tracked case surviving.
- **Severity:** Low — self-inflicted operational surprise, already stated as fact in docs; useful as defender guidance,
  not an attacker-controlled primitive (controlling the SG implies full compromise).

### Lens R/S — AWS-authored IAM artifact audit: `CloudWatchAgentServerPolicy`

Shipped policy JSON (fetched online+offline, byte-identical, v3/default, edited 2024-02-06). The CloudWatch-agent
retrieval path on this page points customers to attach exactly this policy fleet-wide.

**R1 [sharpest, fully evidence-backed] — `cloudwatch:PutMetricData` granted with `Resource:"*"` and NO `Condition`, despite a scoping key existing.**
- **Mechanism (doc):** policy statement `CWACloudWatchServerPermissions` grants `cloudwatch:PutMetricData` on
  `Resource:"*"` with no condition. `list_cloudwatch.md` (service-auth ref) documents `PutMetricData` supports the
  `cloudwatch:namespace` condition key. The shipped policy does not use it → any principal with this policy can
  `PutMetricData` into **any** namespace (incl. `AWS/EC2`, `AWS/EBS`, or a victim team's custom namespace), not just
  the agent's own `CWAgent`.
- **Oracle:** attach the managed policy to a test role; `PutMetricData` into an arbitrary namespace and confirm success;
  then confirm a `StringEquals {"cloudwatch:namespace":"CWAgent"}` condition would have blocked it (proving the key
  works and the shipped policy simply omits it).
- **Severity:** Medium — cross-team **metric injection/poisoning**: fabricate low values to mask a real incident in a
  victim's alarm namespace, or high values to trip false alarms / drive auto-scaling. Present on essentially every
  fleet that follows the documented CloudWatch-agent setup.

**R3 — `logs:*` (`CreateLogGroup`/`CreateLogStream`/`PutLogEvents`/`PutRetentionPolicy`/`Describe*`) with `Resource:"*"`, no log-group-ARN scoping.**
- **Mechanism:** Logs ARNs *do* support resource-level scoping, but the statement uses `Resource:"*"` with no condition
  → the role can create/write to **any** log group in the account/region.
- **Oracle:** `logs:CreateLogGroup` on an unrelated name; confirm success.
- **Severity:** Medium — same over-broad fleet-wide shape as R1, extended to log-group namespace collision/pollution.

**R2 (not a finding) — `ec2:DescribeVolumes` + `ec2:DescribeTags` only; narrow, and these actions don't support
resource-level permissions anyway. No `ec2:Describe*` wildcard.**

**R4 (contrast, not a finding) — `ssm:GetParameter` IS correctly scoped to
`arn:aws:ssm:*:*:parameter/AmazonCloudWatch-*`.** The authors clearly know how to scope — they simply didn't apply it
to `PutMetricData`/`logs:*`. X-Ray `Resource:"*"` is unavoidable (no resource-level support), not a finding.

> **Net R/S verdict:** copy-verbatim, broadly-granted artifact for the metrics/logs statement; correctly-scoped for
> SSM. R1 is the single most concrete, evidence-backed lead in the whole plan (JSON + condition-key existence are both
> directly fetched facts, not inferences).

### Lens O — Audit / detection / evidence-destruction

**O1 — Metric-reset-as-evidence-destruction.** Base counters are *"cumulative ... since the last driver reset"*; the
only verbatim "Persistence" sentence on the page (*"Metrics reset if the instance reboots or is terminated, or if the
network interface is detached"*) is physically located **inside the ENA-Express section** (owned by the `ena-express`
plan), and is **not restated** for the base allowance counters.
- **Claim:** an attacker who generated abuse traffic (conntrack churn, PPS/link-local flood) on a compromised instance
  can erase the only in-guest telemetry of it by reboot / terminate / ENI detach; if no CloudWatch agent was
  pre-installed, there is **no AWS-side durable record** of the abuse window at all (unlike CloudTrail / VPC Flow Logs).
- **Doc gap (itself a finding):** that the *base* counters also reset on reboot/terminate/detach is a *reasonable
  inference* (reboot reinitializes the driver; detach removes the netdev) but is **not a verbatim guarantee** on this
  page — flag the doc gap, don't assert it as fact.
- **Oracle:** generate `pps_/conntrack_allowance_exceeded`, confirm nonzero via `ethtool -S`, then (a) reboot and
  recheck → 0; (b) detach/reattach ENI and recheck; (c) confirm no CloudWatch datapoint exists for the window if the
  agent was never installed; (d) ask whether AWS Support / Nitro-side telemetry retains these independently of the guest.
- **Severity:** Medium-High for IR/forensics — a trivially triggerable (guest-privileged, no special permission)
  evidence-destruction mechanic for the primary abuse signal AWS points customers to. Likely by-design (ephemeral
  per-attachment counters), but worth stating plainly as a gap vs VPC Flow Logs / CloudTrail durability.

**O2 — Guest-only-telemetry blind spot (page-family-wide confirmation).** Conntrack and link-local breaches, like the
bandwidth/PPS breaches the sibling bandwidth plan already owns, produce **zero AWS-side telemetry by default** — read
only via in-guest `ethtool`, exported only if the CloudWatch agent is installed *and* the specific counter is listed
in `metrics_include`. CloudTrail never records a governor-drop (it is a kernel/NIC counter, not an API call). This
confirms the pattern is **page-family-wide**, not bandwidth-specific — a force-multiplier making L-CT-2/L-CT-3/U-LINKLOCAL
DoS both effective and silent against a non-instrumented instance. *(Severity: High as a multiplier; defers the base
framing to the bandwidth plan.)*

### Lens Q — Supply-chain / untrusted artifact (informational)

- **Windows `EnaPerfCounters.man`:** copied from "the driver installation package" into `%SystemRoot%\System32\drivers`
  and registered via `lodctr` with **no checksum/signature-verification step documented**. The manifest is XML
  (perf-counter schema, not executable), and writing to `System32\drivers` already requires admin — so low/informational.
  Note only: `lodctr` has a history of Windows CVEs around manifest loading; the omission of a verification step is the
  defect-shaped observation, not a confirmed vector.
- **Linux / DPDK / FreeBSD:** `enhanced-networking-ena.md` points Linux users to GitHub (`amzn/amzn-drivers`) for
  release notes + build/install — a standard clone-and-build pattern, **not** a curl-pipe-to-shell embedded in AWS docs,
  structurally lower-risk than the `ena-express` sibling's `check-ena-express-settings.sh` download-run concern.
  `dpdk-testpmd` and FreeBSD `sysctl` are read-only local diagnostics for someone who already has guest shell. **No
  concrete AWS-doc-embedded code-exec vector found.**
- Driver-package / AMI `enaSupport` trust path is **deferred to the hub plan (Area 4)**.

### Lens V / L (cross-tenant side-channel) — NULL (explicit)

- All six base counters are per-instance/per-ENI by documented wording (*"for the instance" / "for the network
  interface"*; `conntrack_allowance_available` *"by the instance ... of that instance type"*). No counter is described
  as reflecting shared host/NIC aggregate or neighbor activity. **Lens L side-channel NULL; Lens V cross-tenant
  reachability/sniffing NULL** for this page family — any cross-tenant segmentation lead belongs to the ENA-Express /
  `ec2-networking` hub (hub lead #3), not here. Pages checked: `monitoring-network-performance-ena.md`,
  `security-group-connection-tracking.md`. *(Confirm/refute oracle for completeness: drive exhaustion on instance A on
  a shared host, check whether any counter on co-located instance B moves — expect no correlation.)*

### Other lenses — NULL (pages checked named above)

A (IDOR), B (PassRole), C (credential vending), D (data→control escape via API), E (RBAC escalation), F (injection),
G (SSRF), P (proofing gate), T (secret storage): **no triggers on this read-only telemetry page** — no resource-by-ID
API, no role-ARN input, no caller-supplied URL/blob the service dereferences, no proofing workflow, no secret
generated. (U-LINKLOCAL-2 is the closest thing to a data→control effect, but via *availability* degradation, not an
API escape — kept under Lens U.)

---

## 6. Prioritized NEW / changed surface

1. **U-FRAG (NEW feature, HEADLINE)** — fragment proxy mode: ungoverned, undetectable, guest-side raise of a host
   anti-abuse ceiling. The genuinely new, unowned surface this page introduces. *Medium, novel.*
2. **R1 — `CloudWatchAgentServerPolicy` `PutMetricData` unscoped-by-namespace** — most concrete, fully doc-evidenced,
   fleet-wide, falsifiable in one API call. *Medium.*
3. **U-LINKLOCAL-2 — link-local PPS exhaustion → IMDS credential-refresh erosion** — highest *impact* if confirmed
   (data-plane flood → control-plane credential outage); Medium confidence, untested chain. *High-if-true.*
4. **L-CT-3 — conntrack idle-timeout attack-budget asymmetry (432000s vs 350s)** — new mechanism-level claim not in the
   bandwidth sibling; AWS's own warning corroborates. *Medium.*
5. **O1 — metric-reset evidence-destruction + base-counter persistence doc gap.** *Medium-High for IR.*
6. **U-LINKLOCAL-1 — no SG/NACL/IAM lever over the link-local ceiling.** *Medium-High (control-surface absence).*
7. **L-CT-2 — conntrack exhaustion behavior on existing connections (doc-ambiguous).** *Medium-if-true.*
8. **R3 — `logs:*` unscoped.** *Medium.* • **U-LINKLOCAL-3 / L-CT-1 — negative/confirmation leads.** *Low but worth stating.*
9. **Lens Q — Windows `lodctr` manifest no-checksum.** *Informational.*

---

## 7. Falsifiable-Hypothesis Lead Sheet (hunter-executable)

| # | Lens | Claim (one line) | Oracle | Severity |
|---|---|---|---|---|
| 1 | U | fragment proxy mode raises egress-fragment ceiling with no API/IAM/SCP lever or footprint | pin driver <2.13.3 vs ≥, flood egress UDP fragments, compare throughput + grep API ref for the field | Med (novel) |
| 2 | R/S | `CloudWatchAgentServerPolicy` lets `PutMetricData` write any namespace | attach policy, PutMetricData into `AWS/EC2`/victim namespace, confirm success; confirm `cloudwatch:namespace` condition blocks | Med |
| 3 | U | sustained link-local PPS flood expires IMDS role credentials past the 5-min buffer | flood 169.254.169.254 >5 min while polling IMDS; watch for `ExpiredToken` | High-if-true (Med conf) |
| 4 | L | 432000s idle-timeout default makes non-Nitro-v6 a cheap low-and-slow conntrack-DoS target | compare time-to-exhaustion v6 (350s) vs non-v6 (432000s) at equal rate | Med |
| 5 | O | base counters reset on reboot/terminate/detach (doc only guarantees this for ENA-Express) → evidence destruction | trigger counters, reboot + detach/reattach, confirm reset; confirm no CW datapoint if agent absent | Med-High (IR) |
| 6 | U | no SG/NACL/IAM control over the link-local PPS ceiling | attempt SG/NACL on 169.254.169.254/.123, confirm no effect; grep EC2 auth ref for link-local key | Med-High |
| 7 | L | conntrack exhaustion drops *existing* established connections, not just new ones | hold long-lived tracked conns, flood new until `conntrack_allowance_exceeded`, check survivors | Med-if-true |
| 8 | R/S | `logs:*` unscoped → create/write any log group | `logs:CreateLogGroup` on unrelated name, confirm success | Med |
| 9 | U | custom-DNS-resolver carve-out just moves traffic to `pps_allowance_exceeded` | during link-local exhaustion, confirm custom resolver survives + increments general PPS | Low |
| 10 | L | conntrack is per-instance isolated (NOT a shared pool like burst bandwidth) | saturate instance A table, check co-resident B's `conntrack_allowance_available` — expect no change | Negative/confirmation |
| 11 | Q | Windows `EnaPerfCounters.man` copied into `System32\drivers` with no documented checksum | confirm doc omits any integrity-verification step before `lodctr` | Info |

---

## 8. HARD STOP / Scope Discipline

- The governor **enforcement/shaping layer is AWS's Nitro/host service plane.** Every oracle above confirms a
  *guest-observable* effect only (a counter value, a throughput number, a credential error, an API success/denial in the
  *tester's own* account). **Never probe, map, or attempt to reach the host-side shaper, Nitro card telemetry, or any
  neighbor instance's data.** If any probe begins returning another tenant's data or an AWS-fleet identity/credential/ARN,
  **stop immediately, preserve evidence, flag for disclosure.**
- All IAM-artifact oracles (R1/R3/R8) are run **against the hunter's own authorized account** with the managed policy
  attached to a *test* role — they confirm the *grant breadth*, never write into a real victim's namespace/log group.
- DoS oracles (U-FRAG, L-CT-*, U-LINKLOCAL-*) run **against the hunter's own instances only**; link-local/conntrack
  exhaustion is self-inflicted on an owned target, never aimed at a shared or third-party resource.
- Documentation-only plan: nothing here has been tested. Every lead is a hypothesis for a downstream `aws-vuln-hunter`
  to confirm or refute with observed API evidence.

---

### Cross-reference index (for the next agent)

- `ec2-instance-network-bandwidth-attack-research-plan.md` — bandwidth/PPS shared-pool, burst credits,
  `ec2:InstanceBandwidthWeighting`, headline guest-only-telemetry Lens-O. **This plan extends its Lens-O to
  conntrack+link-local and adds L-CT-3 / U-LINKLOCAL-2 as net-new mechanisms.**
- `ena-express-attack-research-plan.md` — all `ena_srd_*` metrics + SRD-transport segmentation. **Owns the only
  verbatim Persistence sentence on this page.**
- `enhanced-networking-ena-attack-research-plan.md` (hub) — ENA driver install/upgrade trust, `enaSupport` AMI
  write-path, Windows driver-package supply chain (Area 4).
- `ec2-networking` hub — cross-tenant segmentation (hub lead #3) is the correct home for any SRD/co-tenancy lead.
