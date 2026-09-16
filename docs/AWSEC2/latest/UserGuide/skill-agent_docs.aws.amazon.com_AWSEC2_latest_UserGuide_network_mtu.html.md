# EC2 Network MTU — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network_mtu.html` (+ its `.md` twin) and its child page `ec2-instance-mtu.html` (`Set the MTU for your Amazon EC2 instances`). Offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/network_mtu.md`, `.../ec2-instance-mtu.md`. Cross-refs: `ec2launch-v2-task-definitions.md` (`enableJumboFrames` task), `enhanced-networking-os.md`, `ec2-networking.md`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**
Verified 2026-09-13: **live page == offline mirror** (byte-for-byte on the substantive text). **NO injected AI-agent "See also"/"run this aws CLI" block** on either MTU page (grep clean) — contrast `[[aws-docs-see-also-injection]]`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right.
- **HARD STOP:** the moment evidence touches the shared network *fabric* (SRD/substrate packet handling, per-instance MTU enforcement in the Nitro data plane, cross-tenant fragment handling) — that is AWS's own service plane. Stop, preserve evidence, flag for AWS-Security. This page describes an in-guest OS knob riding on that fabric; the fabric itself is out of scope.
- **Read this first — the shape of this target:** MTU on EC2 is **not a control-plane resource.** It is set entirely **inside the guest OS** (`ip link set … mtu`, `Set-NetAdapterAdvancedProperty`, `netsh interface … set subinterface … mtu=`). **There is no `ec2:` API and no IAM condition key that reads, sets, or constrains an instance's MTU** (confirmed: corpus grep for MTU-related IAM/API returns only `directconnect:update-virtual-interface-attributes` and Snowball `update-mtu-size` — neither is EC2; Mechanical Turk hits are false "mtu" matches). Consequently most boundary lenses are **genuine nulls**, and the two real leads are (1) an AWS-published runbook that tells the customer to fetch and run an **unsigned third-party binary**, and (2) the **complete absence of any IAM lever** over MTU/jumbo-frame posture. Do not re-scope the whole instance/ENI/enhanced-networking surface here — route those to the sibling plans named in §7.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. Determine whether following AWS's own MTU runbook verbatim can lead to **code execution on the customer instance from a non-AWS supply-chain vector** (the `mturoute.exe` third-party download).
2. Determine whether an org/account can **enforce or even observe** MTU / jumbo-frame posture through any AWS control (IAM, SCP, Config, an `ec2:` condition key, a `Describe*`), or whether the posture is **entirely unenforceable by design**.
3. Confirm that the in-guest MTU tools (`tracepath`, `mturoute`, `ip link`) create **no server-side-fetch (SSRF) surface implicating AWS's fleet identity** (customer-initiated, in-guest — expected null).
4. Characterise PMTUD's ICMP dependency as a **self-inflicted blackhole/DoS and a monitoring blind-spot enabler**, and bound it as single-tenant / out-of-scope-as-a-boundary.

---

## 2. Components, Assets, and Design

**What the customer touches (all in-guest, customer-owned):**
- **Guest network stack** — MTU is a property of the guest's network interface, set with OS commands. Values in docs: standard **1500** (all instance types), jumbo **9001** (all current-gen + prev-gen A1/C3/I2/M3/R3). Windows driver register values differ: ENA `*JumboPacket`=9015 / legacy `MTU`=9001, Intel 82599 `*JumboPacket`=9014, AWS PV `netsh … mtu=9001`.
- **In-guest diagnostic tools:** Linux `tracepath` (from `iputils`, preinstalled), `ip link show/set`; Windows `mturoute.exe` (**third-party, must be downloaded**), `Get-/Set-NetAdapterAdvancedProperty`, `netsh`.
- **Persistence files (Linux):** `/usr/lib/systemd/network/80-ec2.network` (`[Link] MTUBytes=`), `/etc/sysconfig/network-scripts/ifcfg-eth0` (`MTU=`), `/etc/dhcp/dhclient.conf`. Editing these needs root; they are the customer's own files.
- **EC2Launch v2 `enableJumboFrames` task** (Windows) — a **boolean toggle, no inputs**, `AllowedStages [PostReady, UserData]`, runs inside the EC2Launch v2 agent (SYSTEM). Referenced from this page but owned by the launch-agent surface.

**What sits behind it (AWS-owned, out of scope / hard stop):**
- The **Nitro/SRD network fabric** that actually forwards, fragments, or drops frames; the **1500-byte cap enforced at the internet gateway**; the **8500-byte inter-region VPC-peering cap**; NAT-gateway / transit-gateway MTU handling. These are shared infrastructure — HARD STOP.

**Trust posture:** every action on this page executes **as the customer, inside the customer's own instance/OS.** There is no service account, no multi-tenant fleet process, no resource-by-id API, no role assumption, and no data-plane→control-plane bridge exposed by this page. The single crossing that leaves the customer's trust zone is the **outbound download of `mturoute.exe` from `elifulkerson.com`** (a third-party, non-AWS origin) that AWS's runbook tells the customer to execute.

```
Customer instance (guest OS, customer-owned)
  ├─ ip link / Set-NetAdapterAdvancedProperty / netsh  → sets MTU on the vNIC  (no AWS API involved)
  ├─ tracepath <dest> / mturoute.exe <dest>            → customer-initiated PMTUD probe (egress from THIS instance)
  │        │
  │        └── mturoute.exe fetched from  https://elifulkerson.com  ← ⭐ third-party supply-chain seam (Area 1)
  └─ EC2Launch v2 enableJumboFrames (SYSTEM, boolean)  → toggles jumbo frames  (route to launch-agent plans)
             │
             ▼
   Nitro / SRD network fabric  ──  IGW caps 1500 · inter-region peering caps 8500 · fragments/drops  (AWS-owned = HARD STOP)
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| *(none — no EC2 API sets/reads MTU)* | — | — | — | — | MTU is guest-OS-only | — | — | **Confirmed null.** No `ec2:` action, no condition key. |
| `ip link set dev … mtu …` | in-guest CLI | existing | in-guest state | in-guest | set MTU (Linux) | no | root on the instance | Not an AWS API. |
| `Set-NetAdapterAdvancedProperty` / `netsh … set subinterface mtu=` | in-guest CLI | existing | in-guest state | in-guest | set MTU (Windows) | no | admin on the instance | Not an AWS API. |
| `tracepath` / `mturoute.exe` | in-guest CLI | existing | non-mutating | in-guest | PMTUD probe from this instance | no | any user on the instance | `mturoute.exe` is a **third-party download** (see Area 1). |
| EC2Launch v2 `enableJumboFrames` | config task | existing | in-guest state | in-guest (agent) | enable jumbo frames | no | whoever supplies the EC2Launch v2 config / user-data | No inputs; boolean. Deep surface → `[[ec2launch-v2-plan]]`, `[[ec2-windows-instances-plan]]`. |
| Direct Connect `update-virtual-interface-attributes` (MTU) | API | existing | mutating | external | VIF MTU | yes | DX VIF owner | **Different service — out of scope for this page.** |

**Undocumented/console-hidden knob sweep:** none applicable — there is no API/parameter surface to have a hidden field on. The relevant "hidden" fact is the *absence* of any control-plane MTU knob (Area 2).

---

## 4. Boundary-lens catalog results

### FIRING LENSES

**Lens R/U (AWS-published insecure runbook / supply chain / TOFU) — Area 1 ⭐ crown jewel.**
The child page instructs, verbatim: *"Download **mturoute.exe** to your EC2 instance from https://elifulkerson.com/projects/mturoute.php"* then *".\mturoute.exe www.elifulkerson.com"*. AWS's own documentation directs the customer to fetch an **unsigned third-party binary from a personal non-AWS domain** and execute it on a production instance, with **no integrity guidance** — no checksum, no signature verification, no vendored/first-party alternative. This is an AWS-authored artifact (Lens R extends to AWS-published guidance/sample steps), so it is reportable rather than a customer footgun. See Area 1.

**Lens S/U (no condition-key / documented-guarantee-vs-enforcement) — Area 2 ⭐.**
No `ec2:` IAM action or condition key governs MTU (grep-confirmed). Same *class* as `[[network-bandwidth-plan]]`, `[[burstable-unlimited-mode-plan]]`, `[[instance-optimize-cpu-plan]]` (no `CpuCredits`/`CoreCount` key) and `[[enhanced-networking-plan]]` (no `enaSupport`-value key) — but **stronger**: for MTU there is *no attribute at all*, not merely a missing condition key on an existing attribute, so there is **nothing for IAM/SCP/Config to bind to**. See Area 2.

**Lens L/O (resilience / audit blind-spot) — Area 3 (informational enabler).**
The doc states PMTUD relies on ICMP and that ICMP "can be blocked even if allowed at the security-group level" (e.g. a NACL denying ICMP). A blocked ICMP path silently **blackholes** oversized packets (large flows hang; classic PMTUD blackhole). Single-tenant, self-inflicted; also a monitoring/evasion enabler. See Area 3.

### NULL HYPOTHESES (pages checked: `network_mtu.md`, `ec2-instance-mtu.md`, plus the EC2Launch v2 task/settings pages)
- **Lens A (IDOR):** no resource-by-id, no tenant/account field, no shared-fleet process on either page. **Null.**
- **Lens B / C (PassRole / credential vending):** no role ARN input, no STS/session, no credential-provider field. **Null.**
- **Lens D / V / W (data→control escape / network segmentation / attestation):** the only "behind" component is the shared network fabric = **HARD STOP**, not a testable boundary from this page. Route co-residency/fabric questions to `[[instance-topology-plan]]`. **Null here.**
- **Lens G (SSRF via server-side fetch):** `tracepath`/`mturoute`/`ip link` are **customer-initiated, in-guest**, egressing from the customer's own instance with the customer's own identity — **not** an AWS fleet-identity server-side fetch. No `*Url`/`*Uri` field the *service* dereferences. **Null** (the `mturoute.exe` download is a supply-chain issue → Area 1, not fleet SSRF).
- **Lens H (KMS):** none. **Null.**
- **Lens Q (upload):** no upload to any service; the `.exe` download is covered under Area 1. **Null.**
- **Lens Y (TLS/SigV2):** no service endpoint on this page; the third-party download URL is HTTPS (integrity concern is *provenance*, in Area 1, not transport downgrade). **Null.**
- **Lens I/J/K/M/N/P/X/AA:** no triggers (no tags-as-authz, no OAuth, no LLM, no session id, no namespace migration, no identity-proofing gate, no action-family twin, no share/revoke lifecycle). **Null.**

---

## 5. Recommended Areas of Focus

### Area 1 ⭐ — AWS runbook fetches & executes an unsigned third-party binary (`mturoute.exe`)  [Lens R / U — supply chain / TOFU]
**Background.** `ec2-instance-mtu.html` → "Check the path MTU … Windows instances" tells the operator to **download `mturoute.exe` from `https://elifulkerson.com/projects/mturoute.php`** and run it. `elifulkerson.com` is a personal third-party site, not an AWS-controlled or code-signed distribution. AWS provides **no hash, no signature check, no vendored copy**.
**Security Concern.** A customer who follows official AWS guidance runs attacker-influenceable code on a production instance if: the third-party site/domain is compromised, expires and is re-registered, or the HTTPS endpoint is otherwise substituted. There is no trust-on-first-use verification step. This is AWS-authored guidance (uneditable/copy-verbatim), so per the Lens R carve-out it is in scope and reportable — **Tier 2 hardening**, not a customer footgun.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** the doc provides no integrity control for `mturoute.exe`. → **Mechanism:** the download step lists a URL and an execute step with no checksum/signature. → **Confirm/Refute:** re-read the page; confirm absence of any hash/sig/first-party mirror. → *(documentation-confirmable now: CONFIRMED — no integrity guidance present).*
- **Claim:** the binary's provenance is not AWS-controlled. → **Mechanism:** host is `elifulkerson.com`, not `*.amazonaws.com`/`*.aws.amazon.com`/`*.aws.dev`. → **Confirm/Refute:** WHOIS/host ownership; confirm it is a third-party personal site. → CONFIRMED by inspection.
- **Adjacent:** does AWS elsewhere ship a first-party path-MTU tool for Windows (so the third-party dep is avoidable)? If yes, the third-party instruction is a gratuitous supply-chain exposure.
**Doc evidence:** `ec2-instance-mtu.md` lines 60/64/67. **Severity-if-true:** Low–Medium (single-tenant, in-guest, customer-initiated execution; no AWS fleet identity involved) — but AWS-authored, so file as a documentation/supply-chain hardening item. **Stop condition:** documentation finding; do **not** fetch, download, or execute the binary — this is a doc-analysis result, and doing so would be pointless active work. Recommendation for AWS: host a signed first-party tool or publish a checksum.

### Area 2 ⭐ — No IAM/SCP lever exists over MTU or jumbo-frame posture  [Lens S / U — enforceability gap]
**Background.** MTU is set purely in-guest; there is no `ec2:` attribute, action, or condition key for it. The `enableJumboFrames` EC2Launch v2 task and the raw OS commands both act inside the guest, invisible to the control plane.
**Security Concern.** An organisation **cannot enforce, prevent, or even observe** an instance's MTU/jumbo-frame configuration through any AWS-native control (IAM, SCP, a condition key, or a `Describe*`). Any compliance/attestation requirement that assumes MTU can be governed centrally (e.g. "mandate 1500 to avoid jumbo-frame black-holing on internet-bound paths", or "prevent unapproved MTU changes") has **no enforcement mechanism** — the only lever is guest-side configuration management the customer builds themselves.
**High-level Test Scenarios:**
- **Claim:** no `ec2:` condition key/attribute reads or constrains MTU. → **Mechanism:** Service Authorization Reference for EC2 has no MTU action/key; `ModifyInstanceAttribute`/`ModifyNetworkInterfaceAttribute` expose no MTU field. → **Confirm/Refute:** enumerate EC2 actions/condition keys for any MTU/jumbo string; enumerate `Modify*Attribute` attribute names. **Expected: none** (corpus grep already returned only Direct Connect + Snowball). → CONFIRMED (documentation); re-verify against live Service Authorization Reference at hunt time.
- **Claim:** no `Describe*` returns per-instance MTU. → **Confirm/Refute:** `DescribeInstances`/`DescribeNetworkInterfaces` field list — confirm no MTU field. → Refute only if a live API surfaces one.
**Doc evidence:** absence across `network_mtu.md`, `ec2-instance-mtu.md`, and the EC2 IAM reference. **Severity-if-true:** Informational/Low (governance/enforceability gap; there is no direct exploit — jumbo-frame misuse is a performance/reliability problem, not a privilege boundary). File as a doc-vs-enforcement observation à la `[[network-bandwidth-plan]]`. **Stop condition:** once the null API/condition-key set is confirmed, done.

### Area 3 — PMTUD ICMP dependency: blackhole DoS + monitoring blind spot  [Lens L / O — informational enabler]
**Background.** The page states PMTUD depends on ICMP (IPv4 Type 3/Code 4; IPv6 PTB Type 2), that ICMP may be delivered only when connections are tracked/untracked or SG rules allow inbound ICMP, and that "ICMP traffic can be blocked even if allowed at the security-group level" (e.g. a NACL deny). It also warns that an internet gateway forwards only ≤1500 bytes regardless of PMTUD.
**Security Concern.** A misconfiguration (NACL/SG denying ICMP) silently **blackholes** oversized packets — large transfers hang with no clean error — a self-inflicted availability problem. As an *enabler*, jumbo-frame/PMTUD behaviour can also interact with instance-level monitoring blind spots (cf. `[[network-bandwidth-plan]]` microburst note) where guest-side counters diverge from CloudWatch. Both are **single-tenant, customer-owned config**.
**High-level Test Scenarios:**
- **Claim:** denying ICMP at the NACL blackholes >1500-byte flows to a jumbo-configured peer without a control-plane signal. → **Confirm/Refute:** in a lab account, set MTU 9001, deny ICMP via NACL, send >1500-byte DF traffic; observe silent stall. → Reliability finding only.
**Doc evidence:** `network_mtu.md` "Path MTU Discovery" + "Important" note. **Severity-if-true:** Informational / out-of-scope as a boundary (self-DoS, single-tenant). Do **not** escalate into the shared fabric. **Stop condition:** confirm it is self-inflicted and single-tenant, then stop.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Supply-chain: run tampered `mturoute.exe` by following the runbook | AWS-published child page | *None* — no checksum/signature/first-party mirror (Area 1) |
| Enforce/observe MTU posture org-wide | EC2 control plane / IAM | *None exists* — MTU is guest-only, no `ec2:` key/attribute/Describe (Area 2) |
| Server-side fetch (SSRF) via a path-MTU tool with fleet identity | in-guest tools | N/A — customer-initiated, in-guest, customer identity (null) |
| PMTUD blackhole / large-flow stall | guest MTU + SG/NACL/ICMP | PMTUD (ICMP) — but ICMP itself may be blocked by NACL (Area 3) |
| Jumbo-frame cross-boundary drop/fragmentation | Nitro/SRD fabric, IGW, TGW | IGW hard-caps 1500; inter-region peering 8500 — **AWS-owned = HARD STOP** |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **The shared network fabric** (SRD/substrate frame forwarding, per-instance MTU/DF handling, cross-tenant fragment processing, IGW 1500 cap, inter-region 8500 cap) — AWS-owned service plane. **HARD STOP.**
- **Single-tenant self-DoS / reliability** from the customer's own MTU/ICMP misconfiguration (Area 3) — not a boundary.
- **Generic IP-fragmentation attacks** (tiny-fragment firewall evasion, overlapping fragments) — general networking, not exposed by this page's surface; handled by the VPC fabric.
- **Deep EC2Launch v2 / user-data-as-SYSTEM surface** — the `enableJumboFrames` task is a boolean with no inputs; the real launch-agent privesc/user-data surface lives in `[[ec2launch-v2-plan]]`, `[[ec2-windows-instances-plan]]`, `[[configure-launch-agents-plan]]`. Route there; do not re-scope here.
- **Enhanced-networking / ENA driver TOFU, SR-IOV, ENA Express/SRD** — `[[enhanced-networking-plan]]`, `[[enhanced-networking-ena-plan]]`.
- **Instance-type network bandwidth / burst / co-residency** — `[[network-bandwidth-plan]]`, `[[instance-topology-plan]]`.
- **Direct Connect / Snowball MTU APIs** — different services.

---

## 8. Null hypotheses / doc gaps
- **Lenses A, B, C, D, H, I, J, K, M, N, P, Q, V, W, X, Y, AA — null**, triggers absent from both MTU pages (checked `network_mtu.md`, `ec2-instance-mtu.md`, `ec2launch-v2-task-definitions.md`, `ec2launch-v2-settings.md`).
- **Lens G — null** on this page (tools are in-guest customer-initiated, not fleet-identity server-side fetch); the `mturoute.exe` download is reclassified to Area 1 (supply chain).
- **No injected AI-agent "See also"/CLI block** on the live or offline MTU pages (grep clean) — contrast `[[aws-docs-see-also-injection]]`. Nothing to treat as untrusted instructions here.
- **Doc-gap to close at hunt time (cheap, doc-only):** re-confirm against the *live* EC2 Service Authorization Reference that no MTU/jumbo condition key or attribute has been added since the mirror snapshot (Area 2 depends on this null holding). Also confirm no `Describe*` field surfaces MTU.
- **Verdict on this page overall:** thin spec/concept + in-guest runbook. Two reportable-but-low leads (Area 1 supply chain ⭐, Area 2 enforceability gap ⭐) and one informational reliability note (Area 3). No cross-tenant, no service-plane, no control-plane API surface of its own. Reuse this plan; do not re-scope the broader networking surface.

---
### Completion metadata
- **Assigned skill:** `security-questionbuilder` (`/work/.claude/skills/security-questionbuilder`)
- **Target:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network_mtu.html` (+ child `ec2-instance-mtu.html`)
- **Inputs read:** offline mirror `network_mtu.md`, `ec2-instance-mtu.md`; live `network_mtu.md` (WebFetch, confirmed == offline); EC2Launch v2 task/settings pages; corpus grep for any MTU IAM/API/condition key.
- **Result:** plan produced; two ⭐ low-severity reportable leads + one informational note; all high-value lenses either fire-low or are evidenced nulls.
- **Could not fully test (recommend hunter follow-up):** live re-confirmation of the no-condition-key null (Area 2) against the current Service Authorization Reference; live confirmation `mturoute.exe` is still third-party-hosted (Area 1). Neither requires touching a live account beyond read-only doc/API-metadata checks.
