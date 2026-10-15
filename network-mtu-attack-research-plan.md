# Network MTU (EC2) — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/network_mtu.html` (target) + its config child `ec2-instance-mtu.html`; corroborated by `security-group-connection-tracking.html` and `service-authorization/.../list_ec2.md`. Offline mirror == online (WebFetch) 2026-10-15, no security-relevant drift. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Honest headline up front.** This is a *thin, guest-OS / data-plane network-primitive* page. MTU on EC2 is set **entirely inside the guest** (`ip link set … mtu`, `Set-NetAdapterAdvancedProperty`, `netsh … set subinterface mtu=`) — **there is NO EC2 control-plane API, NO IAM action, and NO condition key for MTU/jumbo frames anywhere in `list_ec2.md`** (grep `mtu|jumbo` = 0 hits). Consequently the classic high-yield lenses for this corpus (A cross-tenant IDOR, B/C PassRole/vending, R/S IAM-artifact audit) **do not fire** — there is no API surface, no shipped policy, no multi-tenant service account on this page. The surface that *does* exist is **Lens V (network segmentation / ICMP reachability)**, **Lens L (fragmentation / PMTUD availability)**, **Lens O (ICMP as an out-of-band delivery path through the conntrack carve-out)**, and **one genuinely AWS-owned reportable: Lens R/Q — the doc steers Windows users to download and run an unverified third-party executable.** Most of the rest is customer self-configuration = out of scope (same class as "a user tuning their own instance"). The plan below concentrates fire on the four in-scope items and states the large out-of-scope set as confidently as the in-scope one.

This plan is a **child/complement in the EC2-networking corpus**. It cross-references and does **not** restate:
- `ena-nitro-perf-attack-research-plan.md` — owns the conntrack flow-cache "tracked flow survives SG revoke until 5-day timeout; only a NACL interrupts immediately" finding + conntrack-exhaustion DoS + `ConnTrackSpec` IAM-value-unscopable. **PMTUD here depends on exactly that conntrack machinery** → cross-ref, don't re-derive the conntrack internals.
- `ec2-networking-attack-research-plan.md` — the hub; MTU is one of its 14 child topics.
- `placement-groups-attack-research-plan.md` / the EFA cluster — jumbo frames are "recommended inside a cluster placement group"; no new boundary here, cross-ref.
- `sriov-networking-attack-research-plan.md` / `troubleshoot-ena-driver` — the Windows driver registry knobs (`*JumboPacket`, Intel 82599 vs ENA vs AWS PV) and driver supply chain.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. a PMTUD ICMP that reaches or originates from a Nitro/control-plane host, or a path-MTU manipulation that affects another tenant), stop, preserve evidence, flag for AWS-Security disclosure.
- **Caller/vantage reminder:** every in-guest MTU command runs as the *instance owner on their own instance*. A finding is only in scope when the effect **crosses a tenant/trust boundary** (reaches/affects another account's instance, the control plane, or is an AWS-authored defect). "I set my own MTU and broke my own throughput" is out of scope.

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Cross-tenant path-MTU manipulation:** cause a *victim* instance (another account/tenant) to shrink its path MTU or black-hole traffic by injecting a spoofed ICMP "Fragmentation Needed" (IPv4 Type 3/Code 4) or ICMPv6 "Packet Too Big" (Type 2) — i.e. a remote, low-cost throughput-DoS / connection-stall against a resource I do not own. **Breach oracle:** victim's measured path MTU drops (or large flows stall) in response to packets I injected while off-path/on a shared segment.
2. **ICMP delivery through the stateful carve-out:** reach a victim instance with ICMP that its *inbound* SG rules do not explicitly allow, by riding the "automatically tracked / response traffic" exception. **Breach oracle:** an ICMP PTB/FragNeeded accepted by an instance whose SG has no inbound ICMP allow.
3. **AWS-authored unverified-binary execution:** confirm the official doc instructs the operator to fetch and run an unsigned/unverified third-party `.exe` over a path with no integrity pin. **Breach oracle:** the documented command downloads `mturoute.exe` from a third-party origin with no checksum/signature verification step anywhere in the page.
4. **Availability guarantee gaps (lower priority):** confirm the documented "internet gateway forwards ≤1500 bytes only" / inter-region 8500 / DF-set-drop behavior creates silent black holes a mis-sized MTU can fall into.

## 2. Components, Assets, and Design

**What this page actually describes (mechanism, not marketing):**
- **MTU is a per-interface guest-OS setting.** Standard 1500 (all instance types); jumbo 9001 (all current-gen + previous-gen A1/C3/I2/M3/R3). Windows jumbo values are driver-specific: ENA ≥2.1.0 = `*JumboPacket` 9015, ENA ≤1.5 = `MTU` 9001, Intel 82599 = `*JumboPacket` 9014, AWS PV = `netsh` 9001. **Jumbo disabled by default on Windows.**
- **No control-plane knob.** Setting MTU is `sudo ip link set dev eth0 mtu N` (Linux) or `Set-NetAdapterAdvancedProperty`/`netsh` (Windows). Persistence is editing `/usr/lib/systemd/network/80-ec2.network` (AL2023), `ifcfg-eth0`+`dhclient.conf` (AL2), or distro-specific. **All owner-local, in-guest.**
- **PMTUD is an ICMP-dependent control loop in the data plane.** IPv4: oversize-with-DF → router/host drops + returns ICMP Type 3 Code 4 → sender re-sizes. IPv6: no in-network fragmentation → drop + ICMPv6 Type 2 (PTB) → sender re-sizes. **Delivery of that ICMP back to the sender depends on SG connection-tracking state** (tracked / automatically-tracked / untracked) and can be independently blocked by a **NACL** even when the SG allows ICMP.
- **Cross-boundary payload ceilings (fragmentation triggers):** IGW / VPN / inter-Region (non-TGW) = 1500; inter-Region VPC peering = 8500; packets over the ceiling are fragmented, or **dropped if DF is set**.
- **Diagnostic tools the page tells you to run:** Linux `tracepath` (from `iputils`, OS-packaged — benign) uses UDP probes (doc: "verify that its security group allows inbound UDP"); Windows `mturoute.exe` **downloaded from `https://elifulkerson.com/projects/mturoute.php`** (third-party, non-AWS origin).

**Identity / roles / resources:** none introduced by this page. No ARN, no resource-by-ID API, no role, no token, no secret, no upload field. The "resource" is a network interface's MTU attribute, mutated only from inside the guest.

**ASCII — where MTU/PMTUD lives in the stack:**
```
[Customer guest OS]  ip link / netsh  → sets interface MTU (1500 | 9001)   ← no AWS API in this path
        │ egress packet (maybe DF-set, maybe >path-MTU)
        ▼
[Nitro data plane: SG conntrack + anti-spoof] ──(tracked/auto-tracked/untracked)──┐
        │                                                                          │ ICMP PTB / FragNeeded
        ▼                                                                          │ (must be delivered back)
[VPC router] → [IGW ≤1500 | TGW | inter-region peering ≤8500 | VPN ≤1500] ────────┘
        │                                   ▲
        │ DF set + oversize → DROP (silent black hole)   NACL can block ICMP even if SG allows
        ▼
[Remote host / another tenant's instance]  ← PMTUD / spoofed-ICMP target
```

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ip link set … mtu` (Linux) | guest shell | existing | mutates **own** NIC | guest-local | set interface MTU | no | instance root | no AWS API; no IAM |
| `Set-NetAdapterAdvancedProperty` / `netsh … set subinterface mtu` (Win) | guest shell | existing | mutates **own** NIC | guest-local | set jumbo/standard | no | instance admin | driver-registry knob |
| `tracepath` (Linux) | guest shell | existing | non-mutating | guest→dest | UDP-probe path MTU | n/a | instance user | needs dest inbound UDP |
| `mturoute.exe` (Win) | **downloaded 3P exe** | existing | non-mutating | guest→dest | ICMP-probe path MTU | n/a | instance user | **fetched from elifulkerson.com — Lens R/Q** |
| PMTUD ICMP (Type 3/4, ICMPv6 Type 2) | data-plane packet | existing | n/a | **cross-host** | path-MTU signaling | yes (routable) | any host that can route to target | **the only cross-boundary surface** |

**No `[NEW]` markers, no non-SDK API, no console-hidden parameter** — because there is no API at all. The entire control surface is the guest OS. This is itself the key structural fact (see Lens S/U below).

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Attacker host (off-path / shared segment / another tenant) | Victim instance's TCP/IP stack (another account) | spoofed ICMP FragNeeded / ICMPv6 PTB shrinking victim path MTU | victim's path MTU drops / large flows stall from packets attacker injected = **cross-tenant availability breach** |
| Attacker host w/o inbound-ICMP SG allow on victim | Victim instance | "automatically tracked / response traffic" conntrack carve-out delivering ICMP | ICMP PTB accepted by a victim whose SG lacks an inbound ICMP allow = reachability-model breach |
| AWS doc (published artifact) | Operator's Windows instance | doc instructs download+run of unsigned 3P `mturoute.exe`, no integrity check | the page's own command fetches a non-AWS binary with no checksum/signature step = **AWS-authored supply-chain defect** |
| Customer guest (own instance) | Own NIC MTU | `ip link` / `netsh` | *in scope only if it affects another tenant* — otherwise **out of scope (self-config)** |
| Oversize+DF packet | IGW / peering / VPN ceiling | silent drop | large flows black-hole with no error = availability (mostly single-tenant → OOS) |

Canonical boundary that is **absent** here and worth stating: there is **no customer↔service-account boundary on this page** (no shared fleet, no translation layer, no credential vending). Do not invent one.

## 5. Recommended Areas of Focus (one block per firing lens)

### Area 1 — Lens R/Q: AWS-authored doc steers to an unverified third-party binary (the one clean reportable)
**Background.** `ec2-instance-mtu.html` → "Check path MTU … Windows" instructs: *"Download **mturoute.exe** to your EC2 instance from https://elifulkerson.com/projects/mturoute.php"* and then run it. This is an AWS-published runbook step the operator follows verbatim. (Contrast the Linux path, which uses `tracepath` from the OS-packaged `iputils` — acceptable.)
**Security Concern.** The page provides **no checksum, no signature, no publisher-verification, and no HTTPS-pinning guidance** for a native Windows executable it tells the user to run. `elifulkerson.com` is a personal/third-party site outside AWS's control; a future domain lapse, site compromise, or TLS-strip on the download turns the AWS-recommended diagnostic step into attacker code execution on the instance. This matches the Lens R variant *"AWS-published sample CODE / runbook with an insecure default the customer copies verbatim"* and Lens Q *"untrusted blob the service tells you to fetch and execute."*
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* the documented procedure results in execution of an unsigned binary from a non-AWS origin with zero integrity verification. **Oracle:** read the full page section — confirm (a) the download URL is third-party, (b) no `Get-FileHash`/signature/`certutil` step exists, (c) the file is run directly. (Pure doc audit — settles immediately; **this is already confirmed from the doc text**, so the only open part is the disclosure framing.)
- *Claim:* the download can be served over a downgradable/interceptable path. **Oracle:** attempt the fetch, observe whether HTTP is accepted / whether redirects to HTTP occur; check whether the binary is code-signed by inspecting the Authenticode signature. (Low-cost; no AWS resource touched.)
**Doc evidence:** `ec2-instance-mtu.html` Windows "Check path MTU" step 1. **Severity-if-true:** Medium (AWS-authored artifact → reportable Tier-2; not a customer footgun because AWS authored and ships the instruction). **Stop condition:** doc text confirmed; recommend AWS fix (host a verified copy / add a checksum / use a signed first-party tool). Do not actually exploit a live download.

### Area 2 — Lens V/O: ICMP PMTUD delivery through the stateful conntrack carve-out
**Background.** `network_mtu.html` (Path MTU Discovery) states PMTUD depends on receiving an ICMP control message, and that delivery hinges on SG connection-tracking: *"If connections are automatically tracked, are untracked, or if your security group rules allow inbound ICMP traffic, you can receive PMTUD responses."* `security-group-connection-tracking.html` enumerates the auto-tracked front-ends (NAT GW, NLB, PrivateLink, Lambda Hyperplane ENIs, egress-only IGW, Network Firewall, GA, DynamoDB GW endpoint) and the "response traffic within 600s is accepted regardless of inbound rules" rule.
**Security Concern.** The stateful carve-out is a **delivery channel for inbound ICMP that the instance's inbound SG rules never explicitly authorized** — ICMP PTB/FragNeeded rides in as "response traffic." Combined with the already-owned finding that **a tracked flow survives an SG-rule revoke until the (up to 5-day) conntrack timeout and only a NACL interrupts it immediately** (`ena-nitro-perf` headline), the reachability an operator *believes* they revoked for ICMP may persist. The net-new MTU angle: this is the exact path a spoofed ICMP PTB would use to reach a victim (feeds Area 3), and a defender who "allowed ICMP at the SG" may still have it silently NACL-dropped → PMTUD black hole (Lens U caveat the page itself flags: *"ICMP traffic can be blocked even if allowed at the security group level … a network ACL that denies ICMP"*).
**High-level Test Scenarios:**
- *Claim:* an instance with NO inbound ICMP SG allow still receives ICMP PTB for its own outbound auto-tracked connections (e.g. via NAT GW). **Oracle:** from a no-inbound-ICMP instance, open an outbound flow through a NAT GW to a reduced-MTU path; confirm PTB is delivered and the stack re-sizes. In scope only as a mechanism check; stays within own account.
- *Claim:* after revoking the SG rule that permitted a flow, PMTUD ICMP for that still-tracked flow continues to be delivered until conntrack expiry. **Oracle:** cross-ref `ena-nitro-perf`; measure delivery post-revoke with and without a NACL deny. **Severity:** Low–Medium (reachability-model / availability; single-account unless chained to Area 3).
**Doc evidence:** `network_mtu.html` PMTUD §; `security-group-connection-tracking.html`. **Stop condition:** mechanism characterized; defer conntrack-timeout depth to `ena-nitro-perf`.

### Area 3 — Lens V/L: spoofed ICMP "Packet Too Big" path-MTU-shrink DoS against another tenant
**Background.** PMTUD trusts an *unauthenticated* ICMP control message to lower the sender's path MTU. Classic off-path attack class: forge an ICMPv6 PTB (or IPv4 Type 3/Code 4) claiming a tiny next-hop MTU to collapse a victim's throughput or force pathological fragmentation / connection stalls. The page confirms the receiver "uses the lowest MTU size along the network path and resends," i.e. it will act on the control message.
**Security Concern.** If an attacker on a **shared VPC segment** (shared subnet / shared-VPC participant) or any position able to spoof a plausible on-path source IP can inject a PTB toward a victim instance, it is a remote, near-zero-cost availability-degradation primitive against a resource the attacker does not own — the in-scope cross-tenant shape. **The load-bearing open question is whether Nitro's anti-spoofing / source-dest-check prevents injecting a packet with a forged source into another tenant's flow.** AWS's data plane generally enforces per-ENI source-MAC/IP anti-spoofing, which would **refute** the arbitrary cross-tenant variant — so this is likely-mitigated and must be tested, not assumed.
**High-level Test Scenarios:**
- *Claim:* an instance can emit an IP packet with a spoofed source address of an on-path device toward a peer instance (precondition for the attack). **Oracle:** attempt to send a crafted ICMPv6 PTB with a forged source from attacker instance A to victim instance B in a **shared subnet both accounts' canaries occupy**; observe at B whether the PTB is received and whether B's path MTU to its real peer drops. If Nitro drops the spoofed-source packet at the source ENI → **refuted (expected)**; if it is delivered and B re-sizes → **cross-tenant availability breach, escalate + HARD STOP** (it implicates the shared data plane).
- *Claim:* even without source spoofing, a legitimately-addressed PTB from attacker A to a flow A shares with B (e.g. A is a hop/relay the victim routes through, or a shared NAT GW) can shrink B's MTU. **Oracle:** measure. **Severity-if-true:** High (cross-tenant throughput DoS on shared fabric); the spoofing variant reaching the service plane = Critical + hard stop.
**Doc evidence:** `network_mtu.html` PMTUD IPv4/IPv6 ICMP behavior. **Preconditions:** two in-scope canary accounts, co-resident in a shared subnet / shared path. **Cost:** low. **Stop condition:** the moment a packet affects another tenant or originates/terminates on an AWS fleet host, preserve evidence and flag. **Expectation:** most likely **refuted** by Nitro anti-spoofing — document the refutation as a positive result.

### Area 4 — Lens L/U: cross-boundary silent black-hole & the IGW ≤1500 guarantee
**Background.** `network_mtu.html`: IGW/VPN/inter-Region(non-TGW) cap payload at 1500; inter-Region VPC peering at 8500; over-ceiling packets are fragmented or **dropped if DF is set**; *"An internet gateway in your VPC will forward packets up to 1500 bytes only. 1500 MTU packets are recommended for internet traffic."* and *"Path MTU Discovery does not guarantee that jumbo frames will not be dropped by some routers."*
**Security Concern.** A jumbo-configured instance whose traffic egresses to the internet with DF set hits a **silent black hole** (drop, no useful error if PMTUD ICMP is also blocked by NACL per Area 2) — a self-inflicted availability break, but worth noting as a reliability trap AWS documents but cannot enforce (there is no IAM/control-plane way to prevent a tenant from mis-sizing). This is predominantly **single-tenant self-DoS = out of scope**; the only in-scope framing is Lens U: the "IGW forwards ≤1500 only" is a *guarantee* with no enforcement knob exposed to the operator, and the interaction with Area 2's NACL-blocked-ICMP turns a recoverable fragmentation into an unrecoverable black hole.
**High-level Test Scenarios:** *Claim:* a 9001-MTU + DF flow to an internet host black-holes with no delivered ICMP when the subnet NACL denies ICMP. **Oracle:** reproduce in own account; confirm no PTB received, flow stalls. **Severity:** Low (single-tenant availability / documentation-reliability). **Doc evidence:** PMTUD "Important" callout.

### Area 5 — Lens S/U: the absence of any MTU control-plane knob (structural null, stated as a lead)
**Background.** Grep of `list_ec2.md` for `mtu|jumbo` = **0 hits**; the config child sets MTU only in-guest.
**Security Concern.** An administrator **cannot** author an IAM policy, SCP, or launch-template constraint that *mandates* or *forbids* jumbo frames / a given MTU — the attribute is invisible to the control plane. If an org has a compliance expectation ("all instances use 1500 for internet egress" or "jumbo required in the HPC cluster PG"), it is enforceable only by guest-config tooling, never by AWS IAM. This is the MTU instance of the recurring corpus theme *"an isolation/config guarantee with no IAM mechanism behind it"* (Lens U) and *"a control the admin expects to express has no condition key"* (Lens S failure-shape (a): the key does not exist). Settles via `iam:SimulateCustomPolicy` showing no MTU-related key is evaluable, or simply by the grep. **Severity:** Informational (governance gap, AWS-owned by design, not a vuln) — recorded so a downstream agent does not waste time hunting a nonexistent IAM lever.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-tenant path-MTU shrink via spoofed ICMPv6 PTB | VPC data plane (shared subnet) | Nitro per-ENI source-IP/MAC anti-spoofing + source/dest check (expected to refute) |
| ICMP reaching instance w/o inbound-ICMP SG allow | SG connection tracking | stateful "response traffic" carve-out is intended behavior; NACL is the stateless backstop |
| Persisted ICMP delivery after SG revoke | conntrack flow cache | up-to-5-day timeout; NACL for immediate cut (owned by `ena-nitro-perf`) |
| Unverified `mturoute.exe` execution | AWS doc runbook | **none in the doc** — no checksum/signature/first-party host (the finding) |
| Jumbo-frame black hole on internet egress | IGW 1500 ceiling + DF | PMTUD (fails if NACL blocks ICMP); doc "recommends 1500 for internet" |
| Admin cannot enforce MTU policy | IAM / control plane | **none** — no MTU key exists (governance gap by design) |

## 7. Out-of-Scope Risk Categories (stated as confidently as in-scope)
- **Customer tuning the MTU of their own instance** (`ip link set`, `netsh`, driver registry) — self-config on an owned resource; no boundary crossed. Out of scope (same class as IMDS on a managed host / a user steering their own instance).
- **Single-tenant self-DoS** from a mis-sized MTU / jumbo-to-internet black hole — availability impact confined to the owner. Out of scope.
- **Reliability/performance** of jumbo frames in a placement group / over Direct Connect / NAT GW / TGW — product behavior, cross-ref `placement-groups` + VPC docs, not a security boundary.
- **Guest-OS driver internals** (ENA/Intel 82599/AWS PV jumbo registry values) — belongs to `sriov-networking` / `troubleshoot-ena-driver`; this page only reads/sets the knob.
- **Nitro data-plane anti-spoofing itself** — if a test shows spoofing is prevented, that is the expected shared-responsibility control; do not probe the Nitro host beyond the one anti-spoof confirmation (HARD STOP if any packet originates/terminates on an AWS fleet host).
- **DNS / Route 53 Resolver conntrack carve-out** (noted in the conntrack page) — unrelated to MTU; defer.

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire + why, pages named)
- **Lens A (cross-tenant IDOR):** N/A — read `network_mtu.html` + `ec2-instance-mtu.html`; **no resource-by-ID API, no tenant/customer id field, no shared service account** on either page. No disclosure-timing or sub-resource relationship exists.
- **Lens B/C (PassRole / credential vending):** N/A — no role ARN, no AssumeRole, no token input on either page.
- **Lens D (data→control escape):** partially folded into Area 3's HARD STOP — PMTUD ICMP that reached a control/storage ENI would be a breach, but the page documents no such path; flagged as the stop condition, not an active lead.
- **Lens F (translation/injection):** N/A — no parser/translator/wire-protocol conversion on this page (ICMP/MTU are not customer-input-to-backend-language seams).
- **Lens G (SSRF):** N/A — read both pages; the only URL is the `mturoute.exe` *download* (a client-side guest fetch, routed to Lens R/Q as a supply-chain concern, **not** a server-side fetch the service dereferences). `tracepath`/`mturoute` take a user-supplied destination but that is the user's own diagnostic egress, not a service-side fetch with fleet identity.
- **Lens H/W (KMS / attestation):** N/A — no encryption/KMS/enclave surface.
- **Lens I (tagging/ABAC):** N/A — MTU is not a taggable/condition-keyed attribute.
- **Lens K (prompt injection):** N/A — no LLM/agent.
- **Lens M (shared-identifier interception):** N/A — no session/token id.
- **Lens N (namespace migration):** N/A — no dual ARN/namespace.
- **Lens P (proofing/registration):** N/A — no onboarding/verification/uniqueness gate.
- **Lens R/S (IAM-artifact audit / condition-key semantics):** **fires only negatively** — there is NO IAM artifact and NO MTU condition key (Area 5); the single positive R/Q hit is the unverified-binary doc-steer (Area 1), which is an AWS-published *runbook* artifact rather than a policy JSON.
- **Lens T (cross-service secret reachability):** N/A — no secret generated/persisted.
- **Lens U (doc-vs-enforcement):** fires at Areas 4 & 5 (IGW ≤1500 guarantee with no operator knob; MTU unenforceable via IAM).
- **Lens X/AA/BB/CC/DD/EE/FF:** N/A — no action twins/legacy aliases, no share/revoke lifecycle (beyond the conntrack-revoke cross-ref to `ena-nitro-perf`), no multi-parser request path, no upstream-asserted identity, no caching layer, no predictable-name resolution, no JWT/token validation on these pages.
- **Lens Y (transport/TLS/sig):** fires weakly only via Area 1 (the `mturoute.exe` download could be served over downgradable HTTP — folded into Area 1 scenario 2); no AWS API transport on this page.
- **Lens O (audit evasion):** ICMP PMTUD control messages are data-plane packets not individually CloudTrail-logged; relevant only as the Area 2/3 delivery path, not a standalone finding.

**Doc gaps to confirm before investing:**
1. Whether Nitro anti-spoofing blocks a crafted spoofed-source ICMPv6 PTB from one tenant to a co-resident tenant (Area 3 — the single highest-value live test; likely refutes the cross-tenant variant).
2. Whether `mturoute.exe` is code-signed and whether its download enforces HTTPS (Area 1 scenario 2).
3. Interaction of conntrack 5-day survival with PMTUD ICMP delivery after SG revoke (Area 2 — defer depth to `ena-nitro-perf`).

---
*Cross-refs: [[project-aws-research-plans]], ena-nitro-perf-attack-research-plan.md, ec2-networking-attack-research-plan.md, placement-groups-attack-research-plan.md, sriov-networking-attack-research-plan.md, reference-aws-iam-service-auth-ref-url.*
