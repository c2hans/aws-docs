# Attack / Research Plan — EC2 Security Group **Connection Tracking**

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html`
(markdown twin: `.../security-group-connection-tracking.md`)
**Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/security-group-connection-tracking.md` (125 lines)
**Online == offline:** verified **word-for-word identical** on 2026-10-15 (subagent fetch of both). No sync drift.
**Built by:** `security-questionbuilder` skill + 2 subagents (IAM condition-key audit of `list_ec2.md`; adjacent-doc primitive verification).
**Method:** AWS "Researcher Training Material" style — boundary-first, falsifiable-hypothesis leads. Documentation-only; a hunter executes later.

---

## §0 — How to use this plan (READ FIRST — scope & de-duplication)

This page is the **authoritative source document** for EC2 Security-Group connection tracking. Three existing sibling plans already cite its mechanism and OWN specific angles. **This plan OWNS the connection-tracking mechanism itself and the net-new primitives below; it must NOT re-litigate what the siblings own.** Route accordingly:

| Angle | Owner plan | What they own |
|---|---|---|
| Nitro **flow-cache** mechanism (per-5-tuple decision cache), tracked-flow-**survives-SG-revoke** timing, conntrack-exhaustion-as-DoS, `ConnectionTrackingSpecification` IAM-unscopable | **`ena-nitro-perf-attack-research-plan.md`** (Leads #1/#3/#4). Its Lead #2 **explicitly hands off** the "untracked degrades stateful→stateless" *consequence* to THIS plan. | the hardware substrate + revoke-timing + exhaustion |
| **Incident-response / containment-efficacy inversion** (narrower least-privilege rules are *more* likely tracked → slower revoke, up to 5 days; session-survival test scenarios; untracked-immediate-drop asymmetry) | **`ec2-security-groups-privatelink-attack-research-plan.md`** (Area 6) | the IR/containment framing |
| Stateful **response-channel egress-filter bypass / exfil** landing-page framing (H1); most-permissive-wins (H3) | **`ec2-security-groups-attack-research-plan.md`** (SG chapter HUB) | the chapter-level framing |

**What THIS plan owns (net-new, nothing above covers it):**
1. **U-1 — The 600-second non-TCP/UDP/ICMP "response window" as an inbound-SG-filter bypass primitive** (the headline net-new finding on this page). Covers GRE/ESP/AH/etc. by inference; hardcoded, no knob, **no security callout in the doc**.
2. **U-2 — Stateful bypass mechanism itself** (the TCP/UDP/ICMP case) as the SOURCE-of-truth write-up; cross-ref hub H1 for landing framing.
3. **U-3 — The 8 "automatically-tracked" device types force tracking "even if the SG config does not otherwise require tracking"** → silently *removes* the untracked "immediate-interruption-on-rule-change" property for flows through NAT GW / NLB / PrivateLink / Lambda-Hyperplane / Network-Firewall / egress-only-IGW / Global-Accelerator / DynamoDB-gateway. **DynamoDB = 2 conntrack entries** → exhaustion amplifier.
4. **V/O-1 — Route 53 Resolver DNS SG-ineffectiveness** → SG-based DNS egress filtering silently no-ops → DNS-exfil blind spot (DNS Firewall is the only lever).
5. **S-1 — IAM cannot scope ANY of it** (confirmed, see §4): no condition key for tracking timeouts on the 4 config call sites, and no rule-content key (protocol/port/CIDR) on the 5 SG-rule actions — so neither "untracked rule shape" nor timeout values can be forbidden by policy. Sharpened by the **`vpn-connection` asymmetry** (AWS *does* model timing as condition keys there — deliberate omission here).

If a lead here duplicates a sibling, it is cross-referenced, not re-scored.

---

## §1 — Components, Assets, and Design

**What the page describes.** Connection tracking is the **stateful-firewall layer** of EC2 Security Groups, implemented on the **Nitro card (service plane)**. For most flows the Nitro card records connection metadata (the 5-tuple + state) so that *responses* to an allowed flow are permitted automatically, without a matching reverse rule. The page defines: (a) when a flow is *tracked* vs *untracked* vs *automatically tracked*; (b) the stateful response behavior; (c) a per-instance maximum number of tracked connections; (d) three configurable idle timeouts.

**Mechanism, not marketing:**

- **Tracked (default) flow** — most flows. Nitro stores 5-tuple + state; response traffic is allowed "regardless of outbound security group rules, and vice versa." Changing an SG rule does **not** immediately drop a tracked flow — it keeps flowing until the idle timeout (TCP established up to **432000s = 5 days**).
- **Untracked flow** — a flow is untracked only when a rule allows **all traffic (0.0.0.0/0) in both directions on all ports** for the relevant protocol. Untracked flows are **immediately interrupted** when the governing rule is removed (≤ a few minutes to converge). Untracked is the *fast-revoke* optimization — but see U-3, it is defeated by auto-tracking.
- **Automatically-tracked flow** — 8 device types (listed below) force tracking **even if the SG config would otherwise make the flow untracked**.
- **Non-TCP/UDP/ICMP flow** — only **IP address + protocol number** is tracked (no ports). A "response" of the **same protocol** from the same host within **600 seconds** is accepted **regardless of inbound SG rules** (U-1).

**Assets & identifiers on this page:**
- No ARNs or resource IDs are the *subject* of this page — the "resource" is the **flow** (5-tuple), an ephemeral kernel/Nitro object the customer never names via API.
- Configuration surface: `ConnectionTrackingSpecification { TcpEstablishedTimeout, UdpTimeout, UdpStreamTimeout }` attached to a **network interface**.
- Observability: guest-OS ENA metrics `conntrack_allowance_available`, `conntrack_allowance_exceeded` — **no CloudWatch/control-plane equivalent on this page.**

**Runtimes / planes behind the interface:**
- **Nitro card** — enforces SG/NACL/route decisions and holds the flow table + flow cache. **Service plane. HARD STOP if a probe would read or manipulate another tenant's flow table / Nitro state — preserve evidence, flag for disclosure, do not continue.**
- **Guest OS** — the only place the customer sees conntrack metrics.
- **Route 53 Resolver (VPC+2 / AmazonProvidedDNS)** — an AWS-owned data-plane endpoint explicitly outside SG enforcement.

**ASCII — where enforcement lives:**
```
                 [customer guest OS]  <-- only place conntrack_allowance_* metrics are visible
                        |
   ================ Nitro card (SERVICE PLANE — HARD STOP) ================
     flow table (5-tuple + state)        flow cache (ena-nitro-perf OWNS)
     SG eval / NACL eval / route eval     idle timeouts (60s..432000s)
   ========================================================================
        |                    |                         |
   [tracked flow]     [untracked flow]        [auto-tracked flow]
   survives rule      dropped immediately     survives rule change EVEN
   change until       on rule removal         IF SG would be untracked
   idle timeout                               (8 device types; DynamoDB=2 entries)
        |
   non-TCP/UDP/ICMP: IP+proto only; 600s same-proto "response" bypasses INBOUND rules
        |
   [Route 53 Resolver / VPC+2]  <-- SGs have NO effect here (DNS Firewall only)
```

---

## §2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| External host attacker ↔ victim instance | Victim's **inbound** SG filter | Non-TCP/UDP/ICMP (GRE/ESP/AH/…) "response window" | **If a packet of protocol P from an external IP is accepted inbound within 600s of the victim emitting protocol P to that IP — despite NO inbound rule allowing P — the inbound filter was bypassed.** (data-plane behavior; confirm in a lab the hunter controls, never cross-tenant) |
| Compromised/insider workload ↔ outbound SG filter | Victim's **outbound** SG filter | Stateful response channel (U-2 / hub H1) | Response traffic exits even though outbound rules forbid it → egress-filter is not a reliable exfil control for *response* traffic |
| Workload with revoked SG rule ↔ old peer | Containment / revoke | Tracked flow survives revoke up to 5 days; auto-tracked flows survive even when "untracked-shaped" | **A connection still carries data after the authorizing rule is revoked** → *(timing OWNED by `ena-nitro-perf`; auto-tracking twist U-3 owned here)* |
| Workload with SG-based DNS egress deny ↔ Route 53 Resolver | DNS exfil channel | SGs have no effect on VPC+2 DNS | **DNS query/response to the resolver succeeds despite an SG rule that should block it** → SG DNS-egress control is a silent no-op |
| Multi-tenant Nitro host | Another tenant's flow table / flow cache | — | **ANY read/influence of another tenant's connection state = HARD STOP, service-plane breach, disclosure.** This plan asserts it is a null hypothesis (no customer-testable primitive) — see §8 |
| IAM policy author ↔ connection-tracking config | Governance / least-privilege | `ConnectionTrackingSpecification` + SG-rule content | **No condition key exists to cap timeouts or forbid an untracked/wide-open rule shape** → governance gap (confirmed §4) |

---

## §3 — Interface / configuration surface

This is a **data-plane concept page**; its "API surface" is the set of control-plane calls that *set* connection-tracking config, plus the SG-rule actions whose content determines tracked-vs-untracked. (IAM facts confirmed by subagent against `list_ec2.md`, line refs in §4.)

| Name | Mutating? | Facing | Sets what | Scopable by IAM? | Notes |
|---|---|---|---|---|---|
| `CreateNetworkInterface` | yes | ext | `ConnectionTrackingSpecification` at NIC create | **No tracking/timeout key** (tag/Region/NICID/SG/subnet/Vpc only) | line 5357 |
| `ModifyNetworkInterfaceAttribute` | yes | ext | mutate `ConnectionTrackingSpecification` on existing NIC | only generic `ec2:Attribute` / `ec2:Attribute/${AttributeName}` (untyped String) + tag/AZ/Region/Subnet/Vpc | line 8966; **case-sensitivity fail-open risk** (§4) |
| `RunInstances` | yes | ext | NIC-row `ConnectionTrackingSpecification` at launch | **No tracking/timeout key** anywhere in the long per-resource block | line 9585 |
| `CreateLaunchTemplate` / `…Version` | yes | ext | bake `ConnectionTrackingSpecification` into LT (indirect, authored once, applied at every launch) | **No tracking/timeout key** (tag/Region/ResourceTag/ManagedResourceOperator only) | lines 5253 / 5259 |
| `AuthorizeSecurityGroupIngress`/`Egress` | yes | ext | rule content that decides tracked vs untracked (0.0.0.0/0 both-dir all-port) | **No protocol/port/CIDR key** (tag/Region/SGID/Vpc only; rule-tag key only enforced when `TagSpecifications` present) | lines 4894/4888 |
| `RevokeSecurityGroupIngress`/`Egress` | yes | ext | rule removal (triggers immediate drop for untracked only) | **No rule-content key** | lines 9579/9573 |
| `ModifySecurityGroupRules` | yes | ext | edit rule content | **No rule-content key** | line 8998 |
| `conntrack_allowance_available` / `_exceeded` | no (read) | guest-OS metric | the ONLY exhaustion visibility | n/a — not a control-plane API | lines 42–44 of target |

**Console-hidden / under-tested knobs:** `ConnectionTrackingSpecification` timeouts are an API/launch-template field that most operators never set; the **600s non-TCP/UDP window and the auto-tracking list have NO knob at all** (hardcoded service behavior). The Launch-Template path (`CreateLaunchTemplateVersion`) is the quietest write path — timeouts baked into `$Latest`/`$Default` apply to every future launch with no per-launch re-review and no IAM lever.

---

## §4 — Boundary-lens catalog (findings)

### Lens U — Documented-guarantee-vs-enforcement (DOMINANT lens for this page)

**U-1 — [HEADLINE / NET-NEW] The 600-second non-TCP/UDP/ICMP "response window" is an inbound-SG-filter bypass primitive.**
- **Claim:** For any IP protocol other than TCP/UDP/ICMP (e.g. GRE/47, ESP/50, AH/51), if a victim instance first emits protocol P to host H, then H can send protocol P *back* to the victim within **600 seconds** and the packet is **accepted inbound regardless of the victim's inbound SG rules** — because Nitro regards it as "response traffic." No ports are matched (only IP + protocol number), so H's packet need not correspond to any real session.
- **Mechanism (doc evidence, verbatim, target line 12):** *"For protocols other than TCP, UDP, or ICMP, only the IP address and protocol number is tracked. If your instance sends traffic to another host, and the host sends the same type of traffic to your instance within 600 seconds, the security group for your instance accepts it regardless of inbound security group rules."*
- **Confirm/Refute oracle (lab the hunter owns — NOT cross-tenant):** In a controlled VPC, give an instance an inbound SG with **no** rule for protocol 47. From the instance, send one GRE packet to a controlled external IP. Within 600s, send a GRE packet from that external IP back to the instance. **Confirm** if the inbound GRE packet is delivered to the guest (tcpdump on the instance) despite the absent inbound rule; **refute** if dropped. Then test the window edge (send at ~601s → expect drop) and the no-prior-egress case (send GRE inbound with no prior egress → expect drop) to prove the behavior is response-gated.
- **Why it matters:** The behavior is **hardcoded (no knob)** and carries **no warning/Note in the doc** (unlike the DNS paragraph, which is boxed). An attacker who can induce a victim to emit a non-TCP/UDP/ICMP packet toward an attacker-controlled IP (misconfig, SSRF-to-raw-socket, a chatty tunnel/VPN daemon, a monitoring agent) opens a 600-second **inbound channel that bypasses the inbound SG entirely** for that protocol. The port-less matching makes it coarse: *any* protocol-P packet from that IP is accepted.
- **Preconditions:** victim emits protocol P to attacker IP first; attacker can source protocol P from that IP; 600s window. **Cost:** low. **Severity-if-true: Medium** (inbound-filter bypass, narrow protocol class, requires victim-initiated egress; situational escalation to High if the protocol carries a tunnel the attacker can ride into the VPC).
- **Status:** NET-NEW to this plan. Not covered by any sibling (they focus on TCP/UDP revoke-timing and stateful egress). **Primary deliverable of this plan.**

**U-2 — Stateful response channel defeats egress filtering (SOURCE write-up; landing framing in hub H1).**
- **Claim:** Outbound SG rules do not constrain *response* traffic to an allowed inbound flow (and vice versa) — so an outbound "deny" is not a reliable exfil control for response bytes.
- **Mechanism (verbatim, target lines 8/10):** *"responses to inbound traffic are allowed to flow out of the instance regardless of outbound security group rules, and vice versa"*; ICMP/netcat worked example (line 10) — response ICMP exits "even if your outbound security group rules restrict outbound ICMP traffic."
- **Oracle:** allow inbound ICMP, deny outbound ICMP, ping the instance → echo-replies exit despite the egress deny.
- **Severity:** Low/Info as a standalone (documented intended behavior) but **load-bearing for exfil threat models** — note it so IR teams don't assume egress rules bound response data. **Cross-ref hub H1.**

**U-3 — [NET-NEW] Auto-tracking silently voids the untracked "fast-revoke" guarantee for 8 device classes.**
- **Claim:** Flows through any of the 8 "automatically tracked" device types are tracked **even when the SG is 0.0.0.0/0 both-directions all-ports** (which would otherwise make them *untracked* and therefore immediately killable on rule change). An operator relying on "wide-open rule ⇒ untracked ⇒ instant revoke" is wrong for traffic traversing NAT GW / NLB / PrivateLink / Lambda-Hyperplane ENIs / Network-Firewall endpoints / egress-only-IGW / Global-Accelerator / DynamoDB-gateway.
- **Mechanism (verbatim, target line 29):** *"Connections made through the following are automatically tracked, even if the security group configuration does not otherwise require tracking"* + the 8-item list. Combined with line 14 ("tracked connections are not immediately interrupted … continues to allow packets until existing connections time out") and line 24 (only *untracked* flows are immediately interrupted).
- **Oracle:** route a wide-open (0/0 both ways) flow through a NAT gateway; revoke the rule; observe the flow **survives** past the revoke until idle timeout (vs. a non-NAT 0/0 flow which drops immediately). Confirms the untracked optimization is void behind these devices.
- **DynamoDB amplifier (verbatim, target line 37):** *"Each connection to DynamoDB consumes 2 conntrack entries."* → halves the effective per-instance tracked-connection budget for DynamoDB-heavy workloads → **conntrack-exhaustion DoS reached at half the expected connection count.** *(Exhaustion-as-DoS mechanism OWNED by `ena-nitro-perf` Lead #3; the 2×-DynamoDB amplifier is net-new here.)*
- **Severity:** Medium (containment-correctness defect — a documented fast-revoke optimization that silently does not apply; directly worsens IR, extends sibling privatelink Area 6). The 2× amplifier: single-tenant Medium DoS acceleration.

**U-4 — Idle-timeout limits are documented but ungoverned.**
- **Claim:** TCP-established timeout defaults differ by platform and can be set as high as 5 days; nothing caps it.
- **Mechanism (verbatim, target lines 72–75):** Min `60`s / Max `432000`s / Default `350`s for Nitro v6 (excluding P6e-GB200), `432000`s for all other instance types (incl. P6e-GB200). UDP 30–60s; UDP-stream 60–180s.
- **Oracle:** confirm (lab) that a tracked TCP flow authorized by a since-revoked rule remains usable for up to the configured timeout (worst case 5 days on non-Nitro-v6). **Timing/survival OWNED by `ena-nitro-perf` Lead #1 + privatelink Area 6**; recorded here only to anchor the exact numbers and the Nitro-v6 350s default change. **Cross-ref, do not re-score.**

### Lens S — IAM condition-key scoping (STRONG — confirmed by subagent)

**S-1 — No condition key can scope connection tracking at all.** (All confirmed against `list_ec2.md`, 0 hits.)
- **Timeouts:** `ConnectionTracking`, `IdleTimeout`, `TcpEstablishedTimeout`, `UdpTimeout`, `UdpStreamTimeout`, `TcpTimeout`, `conntrack` → **0 hits anywhere** in the 10,190-line reference. None of the 4 config call sites (`CreateNetworkInterface` 5357, `ModifyNetworkInterfaceAttribute` 8966, `RunInstances` 9585, `CreateLaunchTemplate[Version]` 5253/5259) carries any tracking/timeout key. **An org cannot write a policy that caps the idle timeout or forbids a 5-day timeout.**
- **Rule content:** `AuthorizeSecurityGroupIngress/Egress` (4894/4888), `RevokeSecurityGroupIngress/Egress` (9579/9573), `ModifySecurityGroupRules` (8998) carry only tag/Region/`ec2:SecurityGroupID`/`ec2:Vpc`. **No `ec2:Protocol`, port-range, or CIDR key exists (0 hits).** → **IAM cannot forbid authoring the exact 0.0.0.0/0-both-directions-all-ports rule shape that creates untracked flows, nor restrict rule authorship by protocol/port.** *(This is the SG-rule-content gap also noted by privatelink Area 3 / hub H3 — cross-ref; the connection-tracking consequence is net-new framing here.)*
- **Sharpening asymmetry (NET-NEW):** the `vpn-connection` resource type **does** expose numeric timing condition keys (`ec2:DPDTimeoutSeconds`, `ec2:Phase1LifetimeSeconds`, `ec2:Phase2LifetimeSeconds`, `ec2:RekeyMarginTimeSeconds`, `ec2:RekeyFuzzPercentage`, `ec2:ReplayWindowSizePackets`). AWS **does** model timing-as-condition-key when it chooses — so the total absence for connection-tracking timeouts is a **deliberate/notable governance gap**, not an IAM-platform limitation. Good evidence line for the write-up.
- **Severity:** governance/least-privilege gap (Info→Low for a hunter; High-value *narrative* for a defender audience). Confirm-oracle: `iam:SimulateCustomPolicy` with a Deny on a fabricated `ec2:TcpEstablishedTimeout` condition → the condition is inert (never matches), i.e. the Deny does not constrain the call. **Safe read-only oracle.**

**S-2 — `ModifyNetworkInterfaceAttribute` ConnectionTracking Deny may fail open on case.**
- **Claim:** The only lever over mutating a NIC's `ConnectionTrackingSpecification` is the generic `ec2:Attribute` / `ec2:Attribute/${AttributeName}` (untyped **String**, no documented enum, no normalization guarantee — reference lines 10051–10052). A Deny written against a guessed literal (e.g. lowercase `connectiontracking`) using `StringEquals` is **case-sensitive by default** and silently fails to match if the API's actual attribute token differs in case → **fail-open**.
- **Oracle:** `iam:SimulateCustomPolicy` — Deny `ModifyNetworkInterfaceAttribute` when `ec2:Attribute StringEquals connectiontracking`, then simulate the call; if the Deny does not fire (because the real token is cased differently / is a different string), the control is inert. Doc is **silent** on the correct literal → operators cannot write a reliable Deny.
- **Severity:** Low (hardening footgun; depends on operator attempting this control at all).

### Lens V / O — Service-ENI / resolver bypass (DNS blind spot)

**V-1 — [NET-NEW framing] Security groups have NO effect on Route 53 Resolver DNS → SG-based DNS egress filtering is a silent no-op → DNS-exfil blind spot.**
- **Claim:** An operator who adds an SG egress rule intending to block/limit DNS to the VPC resolver achieves nothing; DNS to VPC+2 / AmazonProvidedDNS flows regardless. The only lever is Route 53 Resolver **DNS Firewall**.
- **Mechanism (verbatim, target line 17, boxed Note):** *"Security groups have no effect on DNS traffic to or from the Route 53 Resolver … If you wish to filter DNS requests through the Route 53 Resolver, you can enable Route 53 Resolver DNS Firewall."*
- **Oracle:** add an SG egress deny for UDP/53 to VPC+2; issue a DNS query from the instance → it still resolves. Confirms SG non-enforcement. (DNS-exfil as a channel is a known class; the net-new point is that **operators mistakenly treat SG egress as a DNS control**.) *(Link-local/VPC+2 reachability also noted by `using-instance-addressing` Area 4 — cross-ref; the SG-ineffectiveness-as-defensive-gap is this plan's.)*
- **Severity:** Medium as a defensive blind spot (data-exfil channel survives a plausible-looking SG control); Info as a pure behavior.

### Lens L — Resource-exhaustion / DoS

**L-1 — conntrack allowance exhaustion (single-tenant DoS).** *(Mechanism OWNED by `ena-nitro-perf` Lead #3 and `ec2-instance-network-bandwidth`.)* Recorded here for the DynamoDB-2× amplifier (U-3) and because this page is the source of the metric names.
- **Mechanism (verbatim, target lines 42–44):** per-instance max tracked connections; beyond it *"any packets that are sent or received are dropped because a new connection cannot be established"*; visibility only via guest-OS `conntrack_allowance_available` / `conntrack_allowance_exceeded`.
- **Blind-spot note:** no CloudWatch/control-plane metric on this page → a defender without ENA/guest telemetry **cannot see** conntrack exhaustion. **Severity:** Medium single-tenant DoS; **cross-ref, do not re-score.**

### Lens AA — Revoke / lifecycle (tracked-flow-survives-revoke)

**AA-1 — Rule revoke does not break tracked flows; NACL is the only immediate kill-switch.** *(OWNED by `ena-nitro-perf` Lead #1 + privatelink Area 6.)* Source text here (verbatim, target line 14): *"When you change a security group rule, its tracked connections are not immediately interrupted … To ensure that traffic is immediately interrupted … you can use a network ACL … Adding a network ACL that blocks traffic in either direction breaks existing connections."* **Cross-ref, do not re-score.** The net-new wrinkle is U-3 (auto-tracked devices extend this survival even to otherwise-untracked flows).

---

## §5 — Prioritized leads (NEW / highest-value first)

1. **U-1 — 600s non-TCP/UDP/ICMP inbound-filter bypass.** *(NET-NEW, headline.)* Medium (situational High). Lab-confirmable with GRE/ESP + tcpdump. **No doc warning, no knob.** Prime deliverable.
2. **U-3 — Auto-tracking voids the untracked fast-revoke guarantee for 8 device classes + DynamoDB 2× conntrack amplifier.** *(NET-NEW.)* Medium. Directly worsens IR containment; extends privatelink Area 6.
3. **V-1 — Route 53 Resolver SG-ineffectiveness = DNS-exfil blind spot.** *(NET-NEW framing.)* Medium (defensive). Trivially confirmable.
4. **S-1 — No IAM condition key caps timeouts or forbids untracked/wide-open rule shape; sharpened by `vpn-connection` timing-key asymmetry.** *(Confirmed.)* Governance gap. Safe `iam:SimulateCustomPolicy` oracle.
5. **S-2 — `ec2:Attribute` ConnectionTracking Deny case-sensitivity fail-open.** Low. SimulateCustomPolicy oracle.
6. **U-2 — Stateful egress bypass of response traffic.** Low/Info (source write-up; hub H1 owns framing).
7. *(Cross-ref only — do not re-score:)* U-4 timeout numbers; AA-1 revoke-survival timing; L-1 conntrack exhaustion → owned by `ena-nitro-perf` / privatelink Area 6.

---

## §6 — Confirm/refute oracles summary (all documentation-derived; lab or read-only)

- **U-1:** controlled VPC, instance with no inbound GRE rule; emit GRE outbound to a controlled IP; send GRE back within/after 600s; tcpdump the instance. In-window delivered + out-of-window dropped + no-prior-egress dropped = confirmed response-gated inbound bypass. **Hunter-owned lab only. Never cross-tenant.**
- **U-3:** 0/0-both-ways flow via NAT GW vs via plain ENI; revoke rule; measure survival. NAT flow survives (tracked) while plain flow drops (untracked) = confirmed. DynamoDB: observe 2 conntrack entries per connection against `conntrack_allowance_available`.
- **V-1:** SG egress deny UDP/53 to VPC+2; `dig @VPC+2` still resolves = confirmed no-op.
- **S-1 / S-2:** `iam:SimulateCustomPolicy` with a fabricated timeout/attribute condition in a Deny → condition inert / Deny fails to fire = confirmed unscopable / fail-open. **Read-only, no mutation.**

**HARD STOPS:** Any probe that would read or alter another tenant's Nitro flow table / flow cache, or that surfaces an AWS service-plane identity/credential/ARN, is a service-plane breach — **stop immediately, preserve evidence, flag for disclosure.** The Nitro flow machinery is NOT a test target. All active confirmation is confined to a VPC/account the hunter owns, with synthetic/canary data.

---

## §7 — Severity rationale

- Cross-tenant on this page = **null** (no customer-testable primitive; flow table is per-instance service-plane state). Highest realistic severities are **Medium**, all single-tenant/defensive:
  - U-1 inbound-filter bypass = Medium (narrow protocol class, victim-egress precondition; situational High if it tunnels into the VPC).
  - U-3 containment-correctness + DynamoDB 2× = Medium.
  - V-1 DNS-exfil blind spot = Medium (defensive).
  - S-1/S-2 governance/hardening = Low/Info (High-value narrative, not an exploit).
  - U-2 egress-response bypass = Low/Info.

---

## §8 — Null hypotheses (lenses checked, no customer-testable primitive — pages read: the full `security-group-connection-tracking.md`, `ena-nitro-perf.md`, and `list_ec2.md` SG/NIC/RunInstances/LaunchTemplate rows)

- **Lens A (cross-tenant IDOR):** NULL — no resource-by-ID API on this page; the "resource" is an ephemeral per-instance flow with no customer-nameable identifier. No disclosure-timing or sub-resource surface.
- **Lens B/C (confused-deputy / PassRole / credential vending):** NULL — no role ARN, token, or STS interaction on this page.
- **Lens D (data→control-plane escape):** NULL *as a documentation lead* — the Nitro flow table is control/service-plane but there is **no documented customer-reachable path** to it; reaching it would itself be the HARD STOP, not a planned test.
- **Lens E (RBAC privesc):** NULL — no roles/identities on this page.
- **Lens F (injection/translation):** NULL — no parser/translation layer; connection tracking is packet-metadata state, not customer-string transformation.
- **Lens G/Q (SSRF / blob-parse):** NULL — no URL/host field the service dereferences, no uploaded blob. (U-1 is a raw-protocol reachability primitive, not SSRF.)
- **Lens R/T (shipped IAM artifact / secret storage):** NULL — this page ships no policy JSON, SLR, or generated secret.
- **Cross-tenant Nitro flow-table read/influence:** asserted NULL + **HARD STOP** — any success here is a service-plane breach to disclose, not a finding to pursue.

---

### Cross-reference index
- `ena-nitro-perf-attack-research-plan.md` — flow-cache mechanism, tracked-flow-survives-revoke timing (Lead #1), conntrack-exhaustion DoS (#3), `ConnectionTrackingSpecification` IAM-unscopable (#4); its Lead #2 hands off the untracked→stateless consequence to THIS plan.
- `ec2-security-groups-privatelink-attack-research-plan.md` Area 6 — IR/containment-efficacy inversion (narrower rules → tracked → slower revoke).
- `ec2-security-groups-attack-research-plan.md` (HUB) — H1 stateful egress-exfil landing framing; H3 most-permissive-wins; SG-rule-content condition-key gap.
- `using-instance-addressing-attack-research-plan.md` Area 4 — VPC+2 / link-local resolver reachability.

*End of plan.*
