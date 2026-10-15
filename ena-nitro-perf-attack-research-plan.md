# ena-nitro-perf — Attack / Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-nitro-perf.html`
("Nitro system considerations for performance tuning")
**Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ena-nitro-perf.md` (176 lines)
**IAM authority consulted:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines)
**Plan type:** **COMPLEMENT / HUB** — this page is a synthesizing performance-tuning hub whose every
mechanism-shaped item is already owned by an existing sibling plan. This plan does **not** re-derive
those; it (a) owns the one genuinely net-new security *framing* on the page — the Nitro flow-cache +
security-group connection-tracking teardown-timing guarantee — and (b) acts as the index that maps
each surface back to its owning sibling and reconciles the cross-references.

**Online == offline:** CONFIRMED byte-identical for `ena-nitro-perf.md` (both subagents verified via
live WebFetch + diff). The only delta is a WebFetch HTML→MD rendering artifact (trailing hard-break
double-spaces after bold inline headers) — not a content change. No prose, numbers, commands, or links
differ. Adjacent `security-group-connection-tracking.md` also byte-identical online/offline;
`monitoring-network-performance-ena.md` differs only in trailing-whitespace formatting.

**Headline (one sentence):** This page documents the Nitro hardware **flow cache** — a per-5-tuple cache
of the SG/ACL/route-table decision made on a flow's first packet — and in doing so exposes the mechanism
behind a documented-guarantee-vs-enforcement gap that other EC2 networking pages quietly rely on:
tightening a security group does **not** tear down an already-established *tracked* flow (it keeps
flowing until the connection-tracking idle timeout, as long as **5 days / 432000 s** by default on all
non-Nitro-v6 instance types) — only a stateless NACL deny interrupts it immediately.

---

## 0. TL;DR — what to actually test, ranked

| # | Lead | Lens | Severity ceiling | Owner |
|---|---|---|---|---|
| 1 | **SG rule revoke does not immediately kill a *tracked* flow** — flows survive until the TCP-established idle timeout (default up to 432000 s / 5 days on non-Nitro-v6). Only a NACL deny is immediate. This is the enforcement mechanism behind the "SG/NACL still evaluated" reassurance the `enhanced-networking-ena` hub leans on. | U | Medium (IR/runbook correctness) | **THIS PLAN** |
| 2 | **"Use Untracked connections" perf tip silently degrades a stateful firewall to stateless** for that flow — the perf page recommends it for PPS with no inline caveat that it requires an already-fully-open 0.0.0.0/0-both-directions rule and forfeits per-connection reply validation. | U (doc-gap) | Low/Info (doc clarity) | **THIS PLAN** (consequence owned by `security-group-connection-tracking`) |
| 3 | **Conntrack-table exhaustion DoS**, amplified by the 432000 s default idle-TCP timeout on non-Nitro-v6; absolute ceiling undocumented; guest-OS-only visibility. Per-instance only — no documented cross-tenant bleed. | L + O | Medium (single-tenant DoS) | cross-ref `ec2-instance-network-bandwidth` + `create-network-interface`; detailed here |
| 4 | **`ConnectionTrackingSpecification` idle-timeout values are IAM-unscopable** — no condition key caps/floors `TcpEstablishedTimeout`/`UdpTimeout`/`UdpStreamTimeout` on any of 4 call sites. | S | Info/Low (capability gap) | confirms `create-network-interface` + `ena-queues` |
| 5 | **Fragment proxy mode = 1024-PPS egress bypass** (`insmod ena.ko enable_frag_bypass=1`), no API lever, zero CloudTrail. | L + O | — | **OWNED by `monitoring-network-performance-ena`** — cross-ref only |
| 6 | **ENA queue allocation (`EnaQueueCount`) IAM-unscopable.** | S | — | **OWNED by `ena-queues`** — cross-ref only |
| 7 | **GitHub supply-chain** (`ENA_Linux_Best_Practices.rst` + driver-compilation README on unpinned `master`, no checksum). | R/Q | — | **OWNED by `ena-improve-network-latency-linux`** — cross-ref only |
| 8 | **NitroV3-vs-NitroV4 asymmetric-L2 hardware-acceleration delta** = a documented platform-generation fingerprint; performance behavior, not a filtering/spoofing control. | O/U (info) | Info | **THIS PLAN** (null control-plane) |
| 9 | **Nitro v6 default-timeout reduction** (432000 s → 350 s) = quiet cross-generation behavioral change; availability/correctness, not a boundary break. | N (changed surface) | Info | cross-ref `security-group-connection-tracking` |

**Honest bottom line:** `ena-nitro-perf.html` introduces **zero new EC2 API actions, zero new IAM
condition keys, and zero new control-plane surface.** It is a guest-OS / data-plane performance-tuning
page. Its research value is almost entirely **Lens U** (one documented-guarantee-vs-enforcement finding
worth a live timing test) plus confirming/indexing surfaces owned by four sibling plans. A clean result
here is a correct result.

---

## 1. Components, Assets, and Design

**What the page describes (mechanism, not marketing):**

- **Nitro flow cache (the core asset).** The Nitro card does packet processing in hardware. On a flow's
  **first packet** it evaluates security groups, network ACLs, and route-table entries, then **caches
  that decision per 5-tuple** (src IP, dst IP, src port, dst port, protocol). Subsequent packets of the
  same flow hit the cache (the "accelerated" / hardware path) rather than being re-evaluated.
- **Ingress/egress packet flow.** Documented end to end; the security decision point is first-packet
  evaluation + cache insertion.
- **VPC mutation = cache reevaluation.** *"Updates to security groups, route tables, and access control
  lists all need to be reevaluated in the processing path to ensure that route entries and security group
  rules still apply as expected."* — forces reevaluation **of packets in the processing path**, i.e. new
  / exception-path packets; the doc never states this retroactively tears down an already-permitted
  tracked flow.
- **Tracked / untracked / automatically-tracked connections.** Connection-tracking state table lives on
  the Nitro card, scoped **per instance** (not per-ENI, not cross-tenant). (Full mechanics on the adjacent
  `security-group-connection-tracking.md`.)
- **Packets NOT accelerated** (exception / "full flow" path): fragments, idle connections, VPC mutation,
  ICMP, and asymmetric L2 flows on NitroV3-and-earlier platforms.
- **Guest-OS tuning knobs:** PPS tuning, **fragment proxy mode** (`sudo insmod ena.ko
  enable_frag_bypass=1` / `=0`), ENA queue allocation, driver requirements (ENA Linux ≥ 2.2.9 / Windows
  ≥ 2.0.0), BQL (Byte Queue Limit, disabled by default), jumbo frames (9001 B), micro-bursting, number of
  flows (single = 5 Gbps / cluster placement group = 10 Gbps / ENA Express = 25 Gbps).

**Customer-facing interface:** none introduced by this page. All knobs are either (a) guest-OS/kernel
(`insmod`, `ethtool`, driver install) or (b) existing EC2 APIs owned by siblings
(`CreateNetworkInterface`, `ModifyNetworkInterfaceAttribute`, `RunInstances`, `CreateLaunchTemplate` for
`ConnectionTrackingSpecification`; `EnaQueueCount` for queues).

**Accounts / VPCs / tenancy:** Single-tenant framing throughout. Conntrack table and allowance counters
are consistently scoped "per instance" / "for that instance type." No shared-fleet / multi-tenant
language. No service-account vs data-plane-account split is described on this page.

**Processes bound to customer-reachable interface:** The Nitro card (hardware packet processor) sits
between the customer ENI and the VPC fabric. The customer reaches only its own guest OS + ENA driver;
the Nitro flow-cache/conntrack machinery is service-plane and **not** customer-addressable as an API.
Any field or response that would implicate the Nitro service-plane internals is a **HARD STOP** —
preserve evidence, flag for disclosure, do not probe.

**Untrusted-data entry → transform:** None on this page in the injection sense. Conntrack is an L3/L4
state table, not an input-transforming parser. The only "artifacts" are two human-facing GitHub links
and local shell commands (see §5).

```
                    customer account / guest OS
   +-----------------------------------------------------+
   |  app  ->  ENA driver (ethtool, insmod ena.ko)       |   guest-OS knobs:
   |            |     ^                                   |   frag_bypass, BQL,
   |            v     | allowance counters (guest-only)   |   queue count, MTU
   +------------|-----|-----------------------------------+
                |     |   <-- customer ENI (the only reachable interface)
   =============|=====|===================================  trust boundary
                v     |
   +-----------------------------------------------------+
   |   NITRO CARD  (service plane — NOT customer API)    |
   |   - 1st-packet SG/ACL/route eval -> FLOW CACHE      |   per-5-tuple decision cache
   |   - connection-tracking state table (per instance)  |   tracked/untracked/auto
   |   - fragment proxy / PPS governor / acceleration    |   HARD STOP if reached as a host
   +-----------------------------------------------------+
                |
                v   VPC fabric
```

---

## 2. Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Remote network peer | Customer instance (own account) | New/forwarded packets evaluated at Nitro first-packet, then cached | A packet admitted/denied **inconsistently with the current SG/ACL** after a rule change proves stale-cache mis-enforcement (expected: tracked flows persist until timeout — documented, Area 1) |
| Operator (SG-write) | Own live sessions | Revoke/narrow an SG rule | Established **tracked** session keeps flowing after revoke = documented residual-access window (Area 1); established **untracked** session dies immediately (Area 1 inverse) |
| Remote peer (reachable tracked port) | Instance conntrack table | Flood new/idle connections | `conntrack_allowance_exceeded` increments → new legit connections dropped = single-tenant DoS (Area 3). **Cross-tenant bleed = HARD STOP breach** (not documented; would implicate shared Nitro card) |
| Guest root | Nitro egress PPS governor | `insmod ena.ko enable_frag_bypass=1` | Egress exceeds the documented 1024-PPS fragment limit with no control-plane event = governor bypass (**owned by `monitoring-network-performance-ena`**) |
| Customer guest OS | Nitro service-plane internals | Any attempt to address the Nitro card as a host / read its state beyond published ethtool counters | **HARD STOP** — any response from Nitro service-plane internals = disclosure-grade breach; preserve evidence, stop |

Canonical boundaries explicitly **absent** here: customer↔service account (no multi-tenant surface),
data↔control plane (no control ENI/API on this page), credential-vending/STS, OAuth/confused-deputy.
Recorded as null in §6.

---

## 3. API / interface surface inventory

**No API is introduced by this page.** The page references guest-OS commands and defers all control-plane
configuration to existing, sibling-owned APIs. For completeness:

| Name | Method | New? | Mutating | Internet-callable | Authorized callers | Notes / owner |
|---|---|---|---|---|---|---|
| `sudo insmod ena.ko enable_frag_bypass=1/0` | guest shell | — | guest-local | No (local root) | guest root | kernel module load; no network fetch; owner = `monitoring-network-performance-ena` (frag-proxy) |
| `ethtool -S eth0` | guest shell | — | read | No | guest root | allowance counters guest-only; owner = `ec2-instance-network-bandwidth` + `monitoring-network-performance-ena` |
| `ConnectionTrackingSpecification` (`--connection-tracking-specification TcpEstablishedTimeout=,UdpTimeout=,UdpStreamTimeout=`) | param on `CreateNetworkInterface` / `ModifyNetworkInterfaceAttribute` / `RunInstances` / `CreateLaunchTemplate` | — | mutating | Yes (control plane) | any principal with the action | **IAM value-unscopable** (§4.4); owner = `create-network-interface` |
| `EnaQueueCount` / `DefaultEnaQueueCount` | param on Run/Attach/Modify | — | mutating | Yes | any principal with the action | **IAM-unscopable**; owner = `ena-queues` |

**Undocumented/console-hidden knob sweep:** None found that weakens auth/isolation on this page. The
`enable_frag_bypass` kernel param is guest-local, not a control-plane field. The driver-version gating
of fragment proxy mode (the page says "depending on your driver version"; `monitoring-network-performance-ena`
pins it to v2.13.3+) is a capability detail, not an isolation toggle.

---

## 4. Boundary-lens findings (areas)

### Area 1 — Lens U (HEADLINE, OWNED HERE): flow-cache + tracked-connection teardown timing

**Claim 1 (confirmed documented behavior, not hypothetical):** Tightening/revoking a security-group rule
does **not** immediately interrupt an already-established **tracked** connection; it keeps flowing until
the connection-tracking idle timeout elapses.
- **Mechanism (exact text, `security-group-connection-tracking.md` line 14):** *"When you change a
  security group rule, its tracked connections are not immediately interrupted. The security group
  continues to allow packets until existing connections time out."*
- **Corroborated by this page's "VPC mutation" text:** reevaluation applies to packets *in the processing
  path*, and the page never states it retroactively kills a permitted tracked flow — teardown is governed
  by timeout.
- **The actionable guarantee gap:** only a **stateless NACL deny** interrupts immediately — *"Adding a
  network ACL that blocks traffic in either direction breaks existing connections."* SGs promise filtering
  but **not** immediate teardown.
- **Why this plan owns it:** `enhanced-networking-ena-attack-research-plan.md` leans on
  `ena-nitro-perf.md` as the security reassurance that "SG/NACL are still evaluated" for ENA Express SRD
  traffic. This page is the enforcement mechanism behind that reassurance — and it reveals the reassurance
  is about *first-packet evaluation*, not *continuous* re-enforcement. The flow-cache is exactly why
  evaluation is first-packet-only.
- **Confirm/Refute oracle (live timing test):** establish a tracked TCP connection under a narrow-source
  inbound rule; revoke/narrow the rule so a *new* connection would be denied; observe whether the existing
  connection keeps flowing until the TCP-established idle timeout vs. dropping immediately. Expected: flows
  until timeout.
- **Severity:** Medium — incident-response/runbook correctness. An admin who revokes SSH/DB access to
  contain an incident does **not** cut a live attacker session established under a tracked rule; on
  non-Nitro-v6 instances the default TCP-established timeout is **432000 s (5 days)**.
- **Residual ambiguity worth a live test:** does a **route-table** or **NACL** change force faster
  reevaluation of an *established* flow than an **SG** change does? The "VPC mutation" text lumps all three
  together as "reevaluated in the processing path" but the connection-tracking page only resolves the SG
  case explicitly. Test whether route/ACL mutation behaves identically to the SG case for an established
  tracked flow.

**Claim 2 (the inverse — do NOT confuse):** **Untracked** flows die **immediately** when the enabling
rule is removed/modified. *"An untracked flow of traffic is immediately interrupted if the rule that
enables the flow is removed or modified."* (worked SSH example, lines 22–24). This asymmetry is a
training/runbook trap: "revoke = immediate" is true **only** for the (less common, fully-open) untracked
config, not the hardened tracked config.

**Lens-U capability-table sub-check:** N/A — no per-instance-type security-capability table exists on the
page to diff against `Describe*` output (only prose Nitro-v6-vs-other timeout defaults).

### Area 2 — Lens U doc-gap (OWNED HERE): "Use Untracked connections" degrades stateful → stateless

**Claim 3:** For an untracked flow, response traffic is admitted *"based on the inbound or outbound rule
that permits the response traffic, not based on tracking information"* (`security-group-connection-tracking.md`
line 22) — i.e. the per-connection reply-validation guarantee of a stateful firewall is **forfeited**;
any packet matching the broad rule shape passes as "response," whether or not a real connection preceded
it.
- **The doc-gap:** `ena-nitro-perf.md` line 151 lists **"Use Untracked connections"** as a PPS-tuning
  action with a forward link but **no inline caveat** that (a) it requires an already-fully-open
  `0.0.0.0/0`-both-directions-all-ports rule, and (b) it loses per-connection reply validation. An operator
  chasing PPS might **broaden a narrower rule** specifically to make a flow untracked, inadvertently
  widening real access control.
- **Severity:** Low/Info — this is a **documentation clarity** finding, not a code vulnerability. The
  untracked rule is already maximally permissive by construction, so losing conntrack reply-filtering has
  small practical blast radius; the risk is the operator-misunderstanding path. **(SUSPECTED NOTHING —
  honest doc-improvement lead.)**
- **Scoping limit (falsifiable):** flows through egress-only IGWs, Global Accelerator, NAT gateways,
  Network Firewall endpoints, NLBs, PrivateLink interface VPCEs, Lambda Hyperplane ENIs, and DynamoDB
  gateway endpoints are **automatically tracked** regardless of SG shape — "Use Untracked connections" is
  simply unavailable for those paths.

### Area 3 — Lens L + O: conntrack-table exhaustion DoS (cross-ref, detailed here)

**Claim 5 (scope-bounding):** The conntrack table is **per-instance**, not per-ENI and not cross-tenant.
*"Amazon EC2 defines the maximum number of connections that can be tracked per instance."* No doc text
implies cross-tenant sharing on the physical Nitro card. **This caps severity at single-tenant DoS.** A
live test showing a co-resident different-tenant instance affected by one instance's exhaustion would be
a **HARD-STOP** cross-tenant breach — stop and flag for disclosure.

**Claim 6 (remote-driven DoS):** *"After the maximum is reached, any packets that are sent or received
are dropped because a new connection cannot be established."* AWS's own ELB-scaling guidance ("scale
instances/size if you exceed the maximum") is a tacit admission that externally-driven connection volume
hits this ceiling. Oracle: flood new connections to a reachable tracked port faster than they time out →
`conntrack_allowance_exceeded` increments → legit new connections dropped. **Severity: Medium**
(single-tenant), and it's an acknowledged operational risk, not a hidden bug.

**Claim 7 (doc-gap):** The absolute per-instance maximum is **never printed** and **no `Describe*` API**
returns it; the only signal is the derived gauge `conntrack_allowance_available` via ethtool/CloudWatch
agent. Capacity planning for >100k-connection workloads is impossible from public docs alone. Lens-U
doc-vs-API gap, Info severity.

**Claim 8 (exhaustion amplifier — cross-refs `create-network-interface`):** The **432000 s (5-day) default
TCP-established timeout on all non-Nitro-v6 instance types** means idle-but-established connections hold
conntrack slots for up to 5 days each by default, massively lowering the new-connections/sec needed to
keep the table saturated (vs. Nitro-v6's 350 s default). AWS itself advises shortening it (*"configure the
shortest idle connection tracking timeout possible"*). This independently corroborates the
`create-network-interface` plan's "idle-timeout amplifier" flag from primary-source text.

**Claim 9 (Lens O — visibility):** `conntrack_allowance_exceeded` / `conntrack_allowance_available` are
**guest-OS-only** (ethtool, ENA driver ≥ 2.8.1); CloudWatch requires an explicitly-installed agent; **no
CloudTrail/EventBridge path exists** (packet drops are a data-plane phenomenon, no control-plane mutation
to log — structurally inapplicable, not merely undocumented). An account owner on default CloudWatch EC2
metrics has **zero visibility** into the Area-3 DoS. Cross-confirms `ec2-instance-network-bandwidth`.

**Consolidated conntrack timeout reference:**

| Timeout | Min | Max | Default (Nitro v6, excl. P6e-GB200) | Default (all other, incl. P6e-GB200) |
|---|---|---|---|---|
| TCP established | 60 s | 432000 s (5 d) | **350 s** | **432000 s (5 d)** |
| UDP (single transaction) | 30 s | 60 s | 30 s | 30 s |
| UDP stream (multi-transaction) | 60 s | 180 s | 180 s | 180 s |
| Other protocols (IP+proto, fixed) | — | — | 600 s response window (not `ConnectionTrackingSpecification`-tunable) | same |

NLB-fronted connections are always tracked with independent LB-side idle timeouts (350 s TCP / 120 s UDP)
that do **not** follow the ENI-level `ConnectionTrackingSpecification` — a two-layer timeout mismatch worth
noting when tuning one layer.

### Area 4 — Lens S (CONFIRMED NULL): `ConnectionTrackingSpecification` values IAM-unscopable

Grep of `list_ec2.md` (10,190 lines, case-insensitive) returned **0 hits** for
`ConnectionTrackingSpecification`, `TcpEstablishedTimeout`, `UdpTimeout`, `UdpStreamTimeout`,
`IdleTimeout`, bare `Tracking`. Verified directly on the action rows:
- `CreateNetworkInterface` (L5357–5361): keys = `aws:RequestTag`, `aws:TagKeys`,
  `ec2:NetworkInterfaceID`, `ec2:Region` (+ SG/subnet/vpc rows) — nothing connection-tracking-related.
- `ModifyNetworkInterfaceAttribute` (L8966–8971): generic `ec2:Attribute` / `ec2:Attribute/${AttributeName}`
  + tag/region/subnet/vpc — and per the `ena-queues` sibling's documented restriction, that generic key
  only reaches single-`Value`-shaped attributes, **not** a multi-property nested object like
  `ConnectionTrackingSpecification`, so it cannot reach the field values either.
- `RunInstances`: no connection-tracking-specific key.

**Verdict:** IAM can gate *who may call* these actions, but **no policy can cap, floor, or forbid a
specific idle-timeout value.** This is a capability gap (consistent with `EnaQueueCount` in `ena-queues`,
and with `create-network-interface`), not a bug. It directly bounds the Area-3 amplifier: an org cannot
use IAM to enforce "max TcpEstablishedTimeout = 60 s" as a hardening control.

### Area 5 — fragment proxy mode (CROSS-REF, owned by `monitoring-network-performance-ena`)

The page documents `sudo insmod ena.ko enable_frag_bypass=1` as a way of *"overcoming the egress PPS
limit of 1024."* This is the **1024-PPS egress governor bypass** already fully owned (with the specific
driver v2.13.3+/DPDK v25.03+ requirement, the "no API lever," and the "zero CloudTrail" conclusions) by
`monitoring-network-performance-ena-attack-research-plan.md`. This page is **less specific** (says only
"depending on your driver version") — a scoping difference, not a contradiction. **Net-new here:** the
BQL interaction only — *"If BQL and the fragment proxy override are both enabled, it can result in
performance limitations by restricting the number of bytes passed to Nitro before all fragments are
processed."* — a performance footgun, not a security delta. **Do not open a new finding; defer to the
monitoring sibling.**

### Area 6 — ENA queue allocation (CROSS-REF, owned by `ena-queues`)

One-paragraph pointer to `ena-queues.md`; `EnaQueueCount` is IAM-unscopable across Run/Attach/Modify.
Confirmed null (0 hits for `EnaQueue`/`QueueCount` in `list_ec2.md`). **Defer to `ena-queues`;** no new
field introduced here.

### Area 7 — Lens R/Q supply chain (CROSS-REF, owned by `ena-improve-network-latency-linux`)

Two human-facing GitHub links on **unpinned `master`** with no checksum/signature:
- `https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst` —
  **identical artifact** already catalogued (Low severity) by `ena-improve-network-latency-linux` Area 5.1.
- `https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#driver-compilation` ("Driver
  compilation") — same supply-chain shape, newly *mentioned* on this page but same `master`/no-checksum
  pattern, same self-instance blast radius.
- **Lens G (SSRF): NULL** — neither link is server-dereferenced; both are prose links a human clicks.
  `insmod` is purely local. Internal cross-refs (`ena-queues.md`, `security-group-connection-tracking.md`,
  `monitoring-network-performance-ena.md`, `ena-adapter-driver-install-upgrade-win.md`) are same-domain
  doc links. No caller-supplied URL anywhere. **Defer to the latency-linux sibling;** no incremental
  severity.

### Area 8 — Lens O/U (info, OWNED HERE): NitroV3-vs-NitroV4 asymmetric-L2 fingerprint

*"NitroV3 and earlier platforms do not use hardware acceleration for traffic between two ENIs in the same
subnet where one ENI is using the default gateway router and the other is not. NitroV4 and later platforms
use hardware acceleration in this scenario."*
- This is a **documented performance behavior**, not a filtering/spoofing control — the packet is subject
  to the same SG/ACL decision on either platform; only the code path (accelerated vs. "full flow"
  exception) differs.
- **Research value:** it is a **platform-generation fingerprint** observable by an in-guest tenant (via
  performance differential on an asymmetric-L2 topology) — Lens O information disclosure of the underlying
  Nitro hardware generation. Info severity; no control-plane key gates or exposes platform generation
  (`list_ec2.md`: `platform` hits are only `ec2:InstancePlatform` OS-platform, unrelated; `Nitro` hits
  only NitroTPM, unrelated).
- **Explicit non-claim:** the docs do **not** connect asymmetric routing or the V3/V4 delta to any
  filtering bypass or spoofing vector. Treat any such claim as **unsupported by these docs** — the
  asymmetric-routing discussion is scoped entirely to performance and hardware-acceleration eligibility.
  Automatic tracking exists partly *to enforce symmetric routing* for multi-path flows (a reliability
  mechanism), which if anything argues tracking is protective, not weakened, under asymmetry.

### Area 9 — Lens N (changed surface): Nitro v6 default-timeout reduction

The TCP-established default dropped **432000 s → 350 s** on Nitro v6 (excl. P6e-GB200). AWS flags it:
*"You should test your applications on Nitrov6 generation instances with the reduced 350 second default
connection tracking timeout before deploying to production."* This is the page-cluster's one genuine
version-delta: Nitro-v6 adopters inherit a materially shorter idle-eviction default with no customer code
change — primarily an **availability/correctness** risk (long-lived idle connections silently dropped),
not a security boundary break. Cross-ref `security-group-connection-tracking`.

---

## 5. Prioritization — NEW / changed surface

- **Genuinely net-new control-plane surface on this page: NONE.** Zero new APIs, zero new IAM actions,
  zero new condition keys (confirmed by full `list_ec2.md` grep — every non-zero hit traced to an
  unrelated homonym: VPC Flow Logs, Capacity-Reservation OS platform, NitroTPM, VPN DPD timeout, VPC/VPN
  "connection" resources).
- **Highest-value lead:** Area 1 (Lens U, tracked-flow teardown timing) — the one finding this plan owns
  outright and the mechanism other EC2 networking plans implicitly depend on. Worth a live timing test
  (including the route-table/NACL-vs-SG reevaluation-timing ambiguity).
- **Changed surface:** Area 9 (Nitro v6 350 s default) — the only version-delta the docs call out.
- Everything else is **confirm-and-index** against four sibling plans.

---

## 6. Explicit NULL hypotheses (pages checked)

Pages read in full for this plan: `ena-nitro-perf.md`, `security-group-connection-tracking.md`,
`monitoring-network-performance-ena.md`, `create-network-interface.md`,
`modify-network-interface-attributes.md`, `ec2-instance-network-bandwidth.md`; IAM authority
`list_ec2.md` (full grep sweep).

- **Lens A (cross-tenant IDOR):** NULL — no resource-by-ID API, no tenant identifier, no shared-fleet
  language; conntrack is per-instance.
- **Lens B/C (PassRole / credential vending):** NULL — no role ARN, AssumeRole, or credential chaining;
  `ConnectionTrackingSpecification` is a plain numeric parameter.
- **Lens D (data→control-plane escape):** NULL on this page — no control ENI/control API described. (The
  Nitro service-plane boundary is a HARD STOP, §2, not a documented customer surface.)
- **Lens E (RBAC/priv-esc):** NULL — no roles/admin identities on this page.
- **Lens F (translation-layer injection):** NULL — conntrack is a state table, not an input-transforming
  parser.
- **Lens G (SSRF):** NULL — no server-dereferenced field; both GitHub links are human-clicked prose, all
  other links same-domain doc cross-refs, `insmod` is local. (Pages checked: all six above.)
- **Lens H (KMS/encryption):** NULL — no key material.
- **Lens J/K/P/Q-uploads/W (OAuth/prompt-injection/proofing/upload-blob/attestation):** NULL — none appear.
- **Lens R/S (shipped IAM artifact / condition-key audit):** No IAM policy JSON or managed-policy name is
  printed on the page; condition-key audit performed against `list_ec2.md` directly — see Area 4 (confirmed
  value-unscopable). The earlier connection-tracking subagent's inconclusive live fetch of the
  Service-Authorization-Reference was **resolved** here against the offline mirror (`list_ec2.md`), which
  is the authoritative source per repo convention — not a residual doc-gap.
- **Lens Y (TLS/transport/signature):** NULL — conntrack operates at L3/L4, below TLS.
- **Lens AA (share/revoke lifecycle):** NULL in the cross-account-share sense; the SG-rule "revoke"
  analog is fully analyzed under Lens U (Area 1).
- **Lens BB/CC/DD/EE/FF (canonicalization / trusted-header / cache-key divergence / land-grab / JWT):**
  NULL — no parser/authorizer-header/HTTP-cache/predictable-namespace/bearer-token layer on these pages.

---

## 7. Hard-stop / disclosure reminders for the downstream hunter

- The Nitro flow-cache, conntrack table, and PPS governor are **AWS service-plane internals.** Testing is
  limited to **observing documented guest-OS counters** (`ethtool`) and **documented SG/ACL/timeout
  behavior** from the customer's own instance.
- **Any** observation implicating another tenant (cross-tenant conntrack bleed, co-resident instance
  effect, reaching the Nitro card as an addressable host, or reading Nitro state beyond published ethtool
  counters) is a **HARD STOP** — stop immediately, preserve evidence, flag for AWS disclosure. Do not
  escalate or iterate.
- All live tests in Areas 1/3 must use the hunter's **own** authorized instances with synthetic traffic;
  tear down created resources.

## 8. Sibling cross-reference index

| Surface | Owning plan |
|---|---|
| Fragment proxy mode / 1024-PPS egress bypass / guest-only allowance counters | `monitoring-network-performance-ena-attack-research-plan.md` |
| ENA queue allocation (`EnaQueueCount` IAM-unscopable) | `ena-queues-attack-research-plan.md` |
| `ENA_Linux_Best_Practices.rst` + driver GitHub supply chain | `ena-improve-network-latency-linux-attack-research-plan.md` |
| Burst-is-shared best-effort DoS / guest-only ethtool allowance telemetry | `ec2-instance-network-bandwidth-attack-research-plan.md` |
| `ConnectionTrackingSpecification` idle-timeout amplifier (IAM angle) | `create-network-interface-attack-research-plan.md` |
| ENA Express SRD "SG/NACL still evaluated" reassurance (depends on THIS page's flow-cache mechanism) | `enhanced-networking-ena-attack-research-plan.md` |
| Full connection-tracking mechanics (tracked/untracked/auto, timeout table) | `security-group-connection-tracking.md` (no standalone plan; analyzed inline here) |

**This plan OWNS:** Area 1 (Lens-U tracked-flow teardown timing — the headline), Area 2 (untracked-perf-tip
doc-gap), Area 8 (NitroV3/V4 fingerprint), and the hub/index role reconciling the above.
