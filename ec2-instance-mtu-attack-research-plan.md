# EC2 Instance MTU — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-mtu.html` (= "Set the MTU for your Amazon EC2 instances"); offline mirror `./docs/AWSEC2/latest/UserGuide/ec2-instance-mtu.md` (offline==online byte-identical, verified 2026-10-15). Authoritative IAM cross-check: `./docs/service-authorization/latest/reference/list_ec2.md`. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Verdict up front:** This is a **guest-OS network-configuration page** (jumbo frames / path-MTU discovery), not a control-plane surface. It is a child of the `ec2-networking` hub. The page carries **exactly one net-new, in-scope, reportable lead** for the whole corpus — the **AWS-documented instruction to download and run an unsigned third-party Windows binary (`mturoute.exe`) from an individual's personal domain with no AWS-side integrity verification** (Area 1, Lens R/Y/EE). Everything else is NULL or a self-inflicted operational pitfall, and is deferred to siblings. There is **no cross-tenant primitive and no AWS service-plane reach** on this page — the supply-chain lead compromises only the instance of whoever follows the doc.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. **(No lead on this page is expected to reach the service plane — the subagent recon confirmed none exists.)**
- **De-dup contract (read first):** the sibling plan `enhanced-networking-os-attack-research-plan.md` (Area 5) already performed a dedicated NULL analysis of the *VPC-guide* MTU page `network_mtu.html` (fabric MTU caps, PMTUD/ICMP self-DoS). This plan owns the two things that page does **not** contain: the **`mturoute.exe` third-party download** and the **per-Windows-driver MTU registry commands**. Jumbo-frame/PMTUD fabric behavior is **cross-referenced, not restated** (Area 3). Driver-acquisition supply chain for NIC drivers is owned by `sriov-networking-attack-research-plan.md` (SourceForge `ixgbevf` / Intel.com); this plan's `mturoute.exe` is a **distinct, net-new third-party artifact** (a diagnostic tool, not a driver) — grep of the corpus confirms no existing plan mentions `elifulkerson`/`mturoute`.

---

## 1. Pentest Objectives
Stated as concrete breach outcomes a hunter would try to produce:
1. **Supply-chain:** Prove that an operator who follows the page's Windows path-MTU instructions executes code whose integrity AWS never vouched for — i.e. the AWS doc link (`elifulkerson.com`) can resolve to attacker-controlled bytes with no AWS-side hash/signature gate, yielding code execution (as the downloading operator, typically Administrator) on the EC2 instance. **Owner-to-fix = AWS (doc defect), reportable Tier-2.**
2. **Cross-tenant falsification (expected NEGATIVE):** Prove the MTU/jumbo/PMTUD surface offers **no** vector by which one tenant influences another instance's effective MTU, blackholes a neighbor's traffic, injects/forges PMTUD ICMP, or crosses the documented 1500/8500 fabric caps. (Documented as a null to keep the hunter off deterministic fabric behavior.)
3. **Control-plane falsification (expected NEGATIVE):** Prove there is no `ec2:*` action / condition key / ENI attribute that sets or reads MTU, so IAM/ABAC lenses do not apply.
4. **Recon characterization:** Bound the information disclosed by `tracepath`/`mturoute` output (AWS egress-path topology) and the SG-inbound-UDP/ICMP requirement for probing another instance — confirm it is self-path recon, not arbitrary-tenant recon.

---

## 2. Components, Assets, and Design

**Customer-facing interface of this page:** none at the AWS API layer. Every operation is a **guest-OS command** the operator runs *inside their own instance* over their own SSH/RDP session:

| Operation | Linux | Windows (per driver) |
|---|---|---|
| Check path MTU | `tracepath <dns|ip>` (iputils, UDP probes) | **download `mturoute.exe` from `elifulkerson.com`**, then `.\mturoute.exe <dns|ip>` (ICMP probes) |
| Check instance MTU | `ip link show eth0` | `Get-NetAdapterAdvancedProperty` (ENA `*JumboPacket`=9015 / ENA 1.5− `MTU`=9001 / Intel SRIOV `*JumboPacket`=9014 / PV `netsh … show subinterface`=9001) |
| Set instance MTU | `sudo ip link set dev eth0 mtu {1500|9001}` + persist (AL2023 `MTUBytes=`, AL2 `ifcfg`/`dhclient.conf`) | `Set-NetAdapterAdvancedProperty … -RegistryValue {9015/9014/9001 enable, 1514/1500 disable}` / `netsh interface ipv4 set subinterface … mtu=` |

**Assets:** (a) the integrity of the `mturoute.exe` artifact fetched from a third-party domain and run on the instance; (b) the instance's own network connectivity (an MTU misconfig degrades it); (c) the AWS egress-path topology disclosed by trace output. **No tenant data, no credential, no ARN, no role, no secret, no uploaded blob, no URL the AWS service dereferences** appears anywhere on the page.

**Trust zones touched:** operator ↔ their own guest OS (same owner); guest OS ↔ third-party internet host (`elifulkerson.com`, `download.elifulkerson.com`); guest OS ↔ AWS network fabric (MTU caps enforced below the guest). There is **no AWS service account / control plane / shared fleet** in this page's pipeline.

```
operator SSH/RDP ─► own EC2 guest OS ──(HTTPS)──► elifulkerson.com (3rd-party personal domain)
                         │                              └─► download.elifulkerson.com/files/mturoute/2.5/mturoute.exe  (unsigned .exe, run as Admin)
                         ├─ ip link / netsh / Set-NetAdapterAdvancedProperty   (guest-only MTU knob — invisible to EC2 control plane)
                         └─ tracepath/mturoute <dest> ──► AWS fabric (CGNAT 100.64/10, edge 72.21/205.251) ──► destination
                                                           ▲ MTU hard-clamped by fabric: IGW/VPN 1500, inter-region peering/TGW 8500 (deterministic, per-tenant uniform)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Operator's own guest OS | `elifulkerson.com` / `download.elifulkerson.com` (3rd-party) | AWS-doc-instructed HTTPS download of `mturoute.exe`, then execute | **Attacker-controlled bytes execute on the instance** because AWS pins no hash/signature → the compromised-domain / future-build-compromise path yields code exec as the downloading operator. (The in-scope boundary breach here is AWS's doc instruction, not a runtime AWS flaw.) |
| Tenant A's instance | Tenant B's instance (effective MTU / path) | MTU setting + PMTUD ICMP | **NEGATIVE expected** — every lever (interface MTU, SG/NACL ICMP rules) is the victim's own config; anti-spoofing is enforced per-ENI at the fabric; no cross-tenant MTU/ICMP injection seam. A packet-drop a *neighbor* caused on B's traffic would be the breach — none is documented or plausible. |
| Guest data path | EC2 control plane | (none) | **NEGATIVE** — no `ec2:*` MTU action/attribute exists; the guest MTU knob never reaches the control plane. |
| Any instance owner | AWS network architecture | `tracepath`/`mturoute` output | Discloses the owner's **own** egress path (CGNAT + AWS edge IPs) — self-path recon, not another tenant's. Low/informational. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | **No AWS API appears on this page.** All operations are guest-OS CLI/PowerShell. | — | instance operator (OS-level) | `ModifyNetworkInterfaceAttribute` has **no `mtu` parameter** (API ref confirmed); `list_ec2.md` grep for `mtu|jumbo|tracepath|transmissionunit` = **0 hits**. MTU is 100% guest-controlled. |

**Undocumented/console-hidden knob sweep:** N/A — there is no control-plane API or SDK model for MTU to diff against the console. The only "knob" is the guest driver registry value, which the page documents openly per driver.

---

## 5. Recommended Areas of Focus

### Area 1 — `mturoute.exe` third-party supply chain (Lens R / Y / EE) — **PRIMARY, net-new, reportable**
**Background.** The Windows "Check path MTU" procedure (page L58–L67) instructs verbatim: *"Download **mturoute.exe** to your EC2 instance from https://elifulkerson.com/projects/mturoute.php,"* then run `.\mturoute.exe <dest>`. The linked page is a **PHP landing page**, not a stable artifact URL; the actual binary resolves (one hop removed) to `https://download.elifulkerson.com/files/mturoute/2.5/mturoute.exe` — a **version-numbered path** that has changed across the project's history (2008–2011+), so the bytes a reader fetches today need not match anything AWS's doc reviewers ever vetted. The AWS page prints **no checksum, no hash, no PGP key, no code-signing publisher** and does not instruct the reader to verify anything.

**Security Concern (net-new; distinct from `sriov-networking`'s NIC-driver supply chain).** AWS's **authoritative** documentation funnels Windows EC2 operators — including enterprise/regulated users — into downloading and executing (typically with Administrator rights) an **unsigned executable from a single individual's personal domain**, with **zero AWS-side integrity gate**:
- The upstream site *does* publish MD5/SHA1/SHA256/SHA512 checksum files and PGP `.asc` detached signatures for the exe and source — **but AWS surfaces none of them**, so a reader following only the AWS steps has no prompt to verify. (Detached PGP ≠ a trusted Windows Authenticode chain — the binary presents as "unknown publisher.")
- It is a one-person project ("© Eli Fulkerson"), with no visible company, maintained org, or contact channel, and no evidence of post-~2011 updates — plausibly unmaintained.
- **Vectors this opens (all moderate-probability, high-blast-radius, no active compromise observed):**
  - **Domain lapse / compromise / resale** — if `elifulkerson.com` expires or is taken over, AWS's official docs keep pointing operators at attacker-controlled content, with no AWS-side hash to catch the swap.
  - **Future build-pipeline / hosting compromise** of the author — AWS pins no version/hash, so a trojanized future release is undetectable to anyone following the AWS steps.
  - **MITM** — largely mitigated today (landing page and download subdomain both HTTPS), but depends entirely on a hobby site's continuing TLS/cert hygiene, not AWS infrastructure.
  - Typosquat risk is *lower* (the doc hyperlinks directly) but survives copy-paste/search re-lookup by operators who don't recall the exact URL. The page also uses the **same third-party domain as the example trace *destination*** (`www.elifulkerson.com`, L64) — reinforcing operator trust in the domain.

**High-level Test Scenarios (falsifiable claims):**
- *Claim:* the AWS page prescribes download→execute of `mturoute.exe` with **no verification step and no pinned hash/signature**, so compromise or lapse of `elifulkerson.com` (or a trojanized future build) yields code execution as the downloading operator on every instance that follows the doc. → *Oracle (static / OSINT, NO live download):* exhibit the exact page text (L58–L67) showing a bare third-party link with no checksum/signature; confirm the real artifact lives at a version-numbered subdomain path AWS never pins; confirm the AWS page references none of the upstream checksums/PGP that the site itself publishes; confirm absence of Authenticode publisher. All already captured in recon — this is a documentation/threat-model lead, not a live exploit.
- *Severity-if-true:* **Medium** — instance-level code execution bounded to the operator who follows the doc; **in scope and reportable as an AWS-authored doc defect** (Lens R carve-out: AWS owns the uneditable/copy-verbatim instruction, so this is **not** a customer footgun), route `aws-security`, Tier-2. **Not Critical** — no cross-tenant reach, no AWS service plane. **Recommended fix framing for the report:** AWS should host/mirror the tool, or at minimum pin a SHA-256 and instruct verification, or replace it with a first-party/`tracert`-based procedure.
- *Stop condition:* finding is fully established from docs/OSINT; **do not download or run the binary**, and do not probe `elifulkerson.com`.

**Doc evidence:** `ec2-instance-mtu.md` L58–L67 (+ L64 destination reuse). **Cross-ref:** `sriov-networking-attack-research-plan.md` §4 Area A (same *shape* — AWS-documented unverified third-party fetch — different artifact; cite for the reusable supply-chain framing, don't restate).

### Area 2 — Per-driver MTU registry value inconsistency (Lens U, doc-consistency) — Low / Informational
**Background.** The "set/check" steps give **different "jumbo" and "standard" numbers per Windows driver**: ENA 2.1.0+ `*JumboPacket` enable **9015** / disable **1514**; ENA 1.5− `MTU` enable **9001** / disable **1500**; Intel SRIOV 82599 `*JumboPacket` enable **9014** / disable **1514** (page note: *"the MTU size includes the header and the payload"*); AWS PV / `netsh` **9001/1500**; Linux `ip link` **9001/1500**.
**Security Concern.** The `*JumboPacket` registry value is the full **L2 frame** size (payload + 14-byte Ethernet header → 1500+14=1514, 9001+14=9015), while `MTU`/`netsh`/`ip link` express the **IP MTU** (1500/9001). The page states both families as "standard"/"jumbo" without reconciling the +14 offset, so an operator can set a value appropriate for the wrong driver → an **MTU mismatch** → feeds the self-DoS blackhole in Area 3.
**Test Scenario:** *Claim:* the page's mixed 1514/1500 and 9015/9014/9001 "jumbo"/"standard" values, undocumented as L2-vs-IP framing, induce operator MTU-mismatch misconfiguration. → *Oracle:* static doc read (values already captured). *Severity:* **Informational** (doc-clarity; no boundary crossed). AWS-owned, worth a one-line note in the report, not a standalone finding.

### Area 3 — Jumbo-frame / PMTUD fabric behavior & blackhole self-DoS (Lens L / V) — **CROSS-REFERENCE, NULL for this plan**
Deferred to `enhanced-networking-os-attack-research-plan.md` Area 5 (dedicated `network_mtu.html` NULL analysis) and the `ec2-networking` hub (L374–375). Subagent recon reconfirmed, with exact quotes, that nothing here is net-new:
- **Fabric caps are deterministic, per-tenant-uniform AWS enforcement, not guest-violable:** IGW/VPN **1500**, inter-region VPC peering / TGW **8500** (`network_mtu.html`: *"An internet gateway in your VPC will forward packets up to 1500 bytes only"*; TGW quotas: 8500 between VPCs/DX/peering, 1500 over VPN; TGW does **not** support PMTUD on VPN/DX/peering). **No documented case of jumbo frames crossing a boundary AWS claims is 1500-only.**
- **PMTUD blackhole is purely self-inflicted:** victim's own oversized MTU + victim's own SG/NACL dropping ICMP type-3-code-4 (`path_mtu_discovery.html` explicitly tells the operator to permit it). Small packets pass, large transfers hang.
- **No cross-tenant vector:** a shared-subnet neighbor cannot set another ENI's MTU, cannot inject/forge PMTUD ICMP (per-ENI anti-spoofing at the fabric), cannot alter the fabric caps. **Breach oracle NEGATIVE.**
*Severity:* out-of-scope single-tenant self-DoS; **Lens V isolation NULL** (MTU boundary is a capacity boundary, not a tenant-isolation boundary).

### Area 4 — `tracepath`/`mturoute` recon + SG-inbound requirement (Lens O / A-adjacent) — Low / Informational
**Background.** Sample trace output (L38–L52) discloses the owner's **own** egress path: `*.compute.internal` first hop, CGNAT `100.64.x.x` (RFC 6598), AWS edge `72.21.x.x` / `205.251.x.x`. The page notes: *"If the destination is another EC2 instance, verify that its security group allows inbound UDP traffic"* (Linux `tracepath` = UDP probes; Windows `mturoute`/`tracert` = ICMP — would need inbound ICMP).
**Security Concern / Test Scenario:** *Claim:* path-MTU probing is a cross-tenant recon primitive. → *Oracle:* **REFUTED by design** — output reveals only the prober's own egress architecture pattern (AWS network, not another tenant); probing *another* instance requires **that instance's SG to already allow inbound UDP/ICMP from your source**, which is a looser-than-default SG the target owner chose, not an AWS-plane gap. *Severity:* **Informational** (AWS-network-pattern disclosure to the instance owner; minor SG-hardening note: opening inbound UDP/ICMP for diagnostics widens the target's surface).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Operator runs trojanized `mturoute.exe` after domain compromise/lapse or build-pipeline compromise | AWS doc instruction (Windows path-MTU step) | **None on the AWS side** — no pinned hash/signature, no mirror; upstream checksums/PGP exist but are not surfaced or required (Area 1) |
| Tenant B influences Tenant A's effective MTU / blackholes A's large transfers | VPC fabric + guest MTU + SG/NACL ICMP | Per-ENI anti-spoofing; MTU & ICMP rules are the victim's own config; fabric caps uniform (Area 3) — expected to hold |
| Jumbo frames escape a 1500/8500-clamped boundary | IGW / VPN / peering / TGW | Deterministic fabric clamp "up to 1500/8500 bytes only" (Area 3) — expected to hold |
| MTU set/read via IAM-scopable control-plane action | EC2 control plane | No such action/attribute exists (`list_ec2` grep = 0; `ModifyNetworkInterfaceAttribute` has no mtu param) — IAM lenses N/A |
| Operator mis-sets MTU due to driver value confusion (1514 vs 1500 / 9015 vs 9001) | Windows driver registry values | Page states values but not L2-vs-IP framing (Area 2) → feeds self-DoS (Area 3) |

---

## 7. Out-of-Scope Risk Categories (stated as confidently as in-scope)
- **Single-tenant MTU/PMTUD self-DoS** — the operator's own misconfig degrading their own connectivity (Area 3). Deterministic AWS fabric caps (IGW/VPN 1500, peering/TGW 8500) are intended behavior, not a falsifiable isolation claim.
- **The guest MTU knob itself** — it never reaches the AWS control plane; no IAM/ABAC/condition-key surface to test.
- **Vulnerabilities inside the third-party `mturoute.exe` tool** or inside `elifulkerson.com`'s hosting — out of scope as *third-party* software; the *in-scope* finding is strictly AWS's doc instruction to fetch it without verification (Area 1).
- **IMDS / egress / general guest hardening** on a managed instance.
- Any attempt to actually download, execute, or MITM the binary, or to probe/attack `elifulkerson.com` — **do not do this**; the Area-1 finding is complete from docs/OSINT.

---

## 8. Null Hypotheses / Doc Gaps (pages checked named per discipline)
Pages read for triggers: `ec2-instance-mtu.md` (full), `list_ec2.md` (grepped), `ModifyNetworkInterfaceAttribute` API ref, cross-ref `network_mtu.md` / `path_mtu_discovery.html` / TGW quotas (via sibling + subagent).

- **Lens A (IDOR / cross-tenant):** NULL — no resource-by-ID API, no tenant/resource identifier, no shared service account; everything is the operator's own guest OS. (Recon disclosure-timing / sub-resource shapes N/A — no resource.)
- **Lens B / C (PassRole / credential vending):** NULL — no role ARN, `PassRole`, STS, session policy, or credential-provider field on the page.
- **Lens D / V (data→control / network segmentation):** NULL for isolation — no control ENI/VPC reachable; MTU boundary is a capacity boundary (Area 3).
- **Lens E (RBAC privesc):** NULL — no role model; guest OS only.
- **Lens F (translation/injection):** NULL — no wire-protocol translator/parser owned by an AWS service in this page's flow.
- **Lens G (SSRF):** NULL — the `tracepath`/`mturoute` destination (DNS name/IP) is dereferenced by **the operator's own guest OS egressing from a box they control**, not by any AWS service on the caller's behalf; no `*Url`/`*Uri`/webhook/fetch field the service dereferences. (Named explicitly: the destination field was checked and plays an operator-egress role, not a server-side-fetch role.)
- **Lens H (KMS):** NULL — no key/encryption-context.
- **Lens I / S (tagging / condition-key semantics):** NULL — no IAM policy, no condition key, nothing taggable; `list_ec2` has no MTU action to scope.
- **Lens J (OAuth/3P linking):** NULL — no 3P integration/OAuth.
- **Lens K (prompt injection):** NULL — no LLM/agent.
- **Lens L (DoS):** fires only as single-tenant self-DoS → out of scope (Area 3).
- **Lens M (session/id interception):** NULL — no session id / presigned URL / one-time token.
- **Lens N (ARN/namespace migration):** NULL — no ARN/namespace.
- **Lens O (audit evasion / recon):** fires at Informational (Area 4 recon); no security-relevant AWS operation to evade logging on (control-plane NULL).
- **Lens P (proofing/registration):** NULL — no registration/gate/code/uniqueness constraint.
- **Lens Q (file upload):** NULL — the only "download" is the operator fetching `mturoute.exe` (covered as supply chain, Area 1); no upload the AWS service parses/renders.
- **Lens R / Y / EE:** **FIRE** → Area 1 (AWS-documented unverified third-party binary fetch — the one net-new in-scope lead; EE = trust of a predictable third-party domain name AWS pins no owner/hash to).
- **Lens T (cross-service secret reachability):** NULL — no secret generated/persisted.
- **Lens U (doc-vs-enforcement):** fires at Informational (Area 2 driver-value inconsistency; Area 3 confirms fabric guarantees are mechanism-enforced, not merely prose — holds).
- **Lens W (attestation):** NULL — no Nitro/enclave/PCR gate.
- **Lens X (action-family parity):** NULL — no control-plane action family.
- **Lens AA (share/revoke):** NULL — no share/grant.
- **Lens BB / CC / DD (parser-differential / upstream-context / cache-key):** NULL — single component (guest OS), no multi-parser request path, no authorizer/cache.
- **Lens FF (JWT/token):** NULL — no token validation.

**Doc gaps:** none blocking — the page is small, fully captured, offline==online. The sole live-confirmable items (HTTP/HTTPS of the download hops, upstream checksum/PGP existence, absence of Authenticode) were resolved via OSINT during recon; Area 1 is report-ready as a documentation defect without any live-account testing.
