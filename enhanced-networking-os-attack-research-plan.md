# Optimize network performance on EC2 Windows instances — Attack / Research Plan

> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-os.html
> (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/enhanced-networking-os.md`; online `.md` twin fetched — **byte-identical to offline, verified 2026-10-15**).
> **Method:** `security-questionbuilder` skill — boundary-first, documentation-only. Nothing tested against a live account.
> **Status:** documentation-derived hypotheses only. **Honest headline: this page is NULL-dominant** — it is the **Windows counterpart** of `ena-improve-network-latency-linux-attack-research-plan.md` (a deliberately low-yield guest-OS tuning page). It is kept as a sibling so a downstream hunter does not re-open it from zero.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the Nitro card / host managing the ENA device), stop, preserve evidence, flag for AWS-Security disclosure. (No such surface is *reachable from this page* — the page is pure in-guest Administrator config — but the Nitro ENA device boundary is named here as a disclosure line, not a test target.)
- **Bottom line for a hunter in a hurry:** this page introduces **no AWS API, IAM action/condition key, role/ARN, server-dereferenced URL, uploaded blob, secret, or tenant/resource identifier.** Every action it describes is a Windows-guest Administrator PowerShell operation on the operator's *own* instance (self-only blast radius). Do not spend a live budget here. The only non-null residue is a **Low** supply-chain-adjacent note (Area 1) and self-DoS/doc-currency notes (Areas 2–3), plus two **cross-references** (Areas 4–5) whose depth is owned elsewhere.

---

## 1. Pentest Objectives
Stated as concrete breach outcomes, so a hunter can confirm there is nothing to break:
1. **Cross-tenant via RSS/affinity config:** show that a Windows guest's `Set-NetAdapterRss` CPU-affinity configuration can affect the network performance, CPU scheduling, or ENA queue allocation of **another tenant** on the same host. *(Expected: refuted — Nitro virtualizes ENA RSS queues per-ENI/per-instance.)*
2. **Control-plane reach:** show that any knob on this page corresponds to an **EC2 API action or IAM condition key** an admin could allow/deny, or that it reaches the Nitro ENA device management plane. *(Expected: refuted — zero IAM surface.)*
3. **Supply-chain:** show that following the page's instructions causes the operator to execute attacker-controlled code. *(Expected: Low — only human-facing hyperlinks to Microsoft first-party docs; no `curl|iex`/script fetch.)*

---

## 2. Components, Assets, and Design

**What the page actually is.** A guest-OS **performance-tuning** page for **Windows** EC2 instances using enhanced networking (ENA). It recommends in-guest configuration changes an Administrator applies locally. There is no AWS request/response flow on this page.

**Mechanism inventory (verbatim from the page):**
- **RSS (Receive Side Scaling) CPU affinity** via the Windows **PowerShell cmdlet `Set-NetAdapterRss`** — knobs `BaseProcessorGroup`, `BaseProcessorNumber`, `MaxProcessingGroup`, `MaxProcessorNumber`, `NumaNode`. "ENA elastic network interfaces provide up to eight RSS queues." Recommendation to exclude boot processor (logical 0/1) on >16-vCPU instances. Example cmdlets for a 72-vCPU, 2-NUMA-node, 3-ENI instance.
- **TCP chimney offloading** — "should be disabled in most use cases, and has been deprecated as of Windows Server 2016."
- **MTU** — a pointer to `network_mtu.html` ("adjust according to your workload and network architecture").
- **Cluster placement group latency** — published characteristic: "average round trip latencies … of 50us and tail latencies of 200us at the 99.9 percentile"; recommends latest ENA drivers on Nitro fixed-performance instances.
- **Checksum offloading / RSS enabled** — "already configured on official Windows AMIs" (default state, not an action).

**Owners / zones.** Exactly one trust zone is in play: the **customer's own Windows guest OS** (Administrator). The Nitro **ENA device** (hardware/host) that exposes the "up to eight RSS queues" is AWS-owned, but the page never gives the guest a channel to it beyond the standard virtualized NIC — the guest only *partitions its own vCPUs* across queues the device already presents to that one instance.

**Assets.** None sensitive. No ARNs, IDs, secrets, tokens, URLs-that-get-fetched, or tenant identifiers appear anywhere on the page.

**Connection diagram (there is no pipeline):**
```
[Customer Windows guest OS / Administrator]
        │  PowerShell: Set-NetAdapterRss (local, in-guest)
        ▼
[Guest NIC driver (ENA) — vCPU→RSS-queue affinity map]   ← all state is per-instance
        │  (device presents ≤8 RSS queues to THIS instance)
        ▼
[Nitro ENA device / host]  ← AWS-owned; NOT reachable/configurable from this page (disclosure line, not a target)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Windows guest Administrator | Its own ENA NIC's RSS→vCPU map | `Set-NetAdapterRss` (local) | None — stays inside the one instance. A breach would be the config affecting **another instance's** performance/queues; expected impossible (per-instance virtualization). |
| Windows guest Administrator | Nitro ENA device / host | (none exposed by this page) | Any guest-reachable channel that configures the device beyond this instance's presented queues, or returns device/host identity → **HARD STOP + disclosure**. Page provides no such channel. |
| Operator reading the page | Microsoft `learn.microsoft.com` docs | Human-facing hyperlink (Area 1) | Operator transcribes a harmful command from tampered third-party docs. Microsoft's supply chain, not AWS's; no automated fetch/exec. |

No customer↔service-account boundary, no data-plane↔control-plane boundary, no cross-tenant shared-fleet boundary is crossed by anything on this page.

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `Set-NetAdapterRss` | **Windows PowerShell cmdlet (local, in-guest)** | Yes (local NIC config) | **No** | Local Windows Administrator | Microsoft cmdlet, not an AWS API. No SigV4, no endpoint, no IAM. |
| *(none — AWS)* | — | — | — | — | **The page references zero AWS API actions.** |

**Control-plane NULL confirmed by reference grep:** `grep -niE "netadapter|rss|cpuaffinity|chimney|receiveside|processorgroup|jumbo|\bmtu\b"` over the authoritative `list_ec2.md` (Service Authorization Reference) → **zero hits**. There is **no `ec2:*` action or condition key** that corresponds to RSS CPU affinity, TCP chimney offload, RSS queue count, or MTU. An admin **cannot** allow/deny or scope any knob on this page via IAM — because none is a control-plane operation. (This matches the Linux sibling's finding; `enaSupport` is a *different* surface — a value-blind generic `ec2:Attribute` on `ModifyInstanceAttribute`, owned by `troubleshooting-ena`/`enhanced-networking-ena`, and not touched by this page.)

---

## 5. Recommended Areas of Focus

### Area 1 — External third-party documentation links (Lens R / Q — PRIMARY actionable, **Low**, bounded null)
**Background.** The page ends two of its three "see more" pointers at **`learn.microsoft.com`**: the `Set-NetAdapterRss` cmdlet reference (line 32) and the SQL Server "affinity mask" option (line 34). The third pointer is an *internal* AWS doc link (`network_mtu.html`, Area 5).

**Security Concern.** A tuning page that steers an operator to run privileged commands is, in the abstract, a supply-chain seam (the Linux sibling's PRIMARY lead is exactly this shape). **But the Windows instance is materially *weaker* as a lead and must not be over-rated:**
- The links point to **Microsoft first-party documentation**, not to an **AWS-owned mutable artifact**. This is the key distinction from the Linux sibling, whose lead is `github.com/amzn/amzn-drivers/blob/**master**/...` — AWS-owned content pinned to a *mutable* branch with no checksum ceremony. Microsoft's docs are a different vendor's supply chain; a defect there is not AWS's defect.
- The links are **human-facing prose hyperlinks to a cmdlet reference**, not a copy-paste script and **not** a `curl … | iex` / `Invoke-WebRequest | Invoke-Expression` / `sudo bash` one-liner. There is **no network callback and no binary execution** triggered by following the page.
- The AWS page itself ships **safe, self-contained example cmdlets inline** (the three `Set-NetAdapterRss` lines) — the operator does not *need* to leave the page to apply the recommendation.

**High-level Test Scenarios (falsifiable):**
- **Claim:** following this page causes the operator to execute attacker-controlled code. → **Mechanism:** two `https://learn.microsoft.com/...` hyperlinks + three inline example cmdlets. → **Oracle:** inspect whether any link is an executable payload fetch rather than a doc hyperlink, and whether the inline cmdlets are safe as written. → **Refuted** by inspection: both links are HTTPS doc references to Microsoft; inline cmdlets are benign RSS-affinity sets. **Residual** risk is only "Microsoft's doc portal is compromised AND the operator transcribes a malicious command" — Microsoft's supply chain, self-instance blast radius, **Low**.
- **Severity-if-true:** Low (and owner-to-fix would be Microsoft, not AWS). **RE-FLAG only** if AWS ever converts this page to a `curl|iex`-style one-liner or links a *mutable AWS-owned* script (as some driver pages do).

### Area 2 — RSS CPU-affinity misconfiguration = single-tenant self-DoS (Lens L / U — bounded NULL, **out of scope**)
**Background.** `Set-NetAdapterRss` lets the Administrator pin each ENA NIC's RSS queues to a range of logical processors (`BaseProcessorNumber`/`MaxProcessorNumber`/`BaseProcessorGroup`). The page warns of "contention," overlapping ranges, and the need to re-evaluate after an instance resize ("these settings are persistent for each network adapter").

**Security Concern.** A wrong affinity mask (overlapping ranges, using core 0, too few processors, or a stale mask after a vCPU-count change on resize) degrades the operator's **own** network throughput / causes inter-NIC CPU contention. This is a latent **availability/performance** footgun confined to the one instance.

**High-level Test Scenarios:**
- **Claim:** a guest's RSS affinity config can degrade **another tenant's** network performance or steal/starve another instance's ENA RSS queues on the same host. → **Mechanism:** "ENA elastic network interfaces provide up to eight RSS queues" — but these are the queues the Nitro ENA device presents to **this** instance's ENIs; the cmdlet only maps them onto **this** guest's vCPUs. → **Oracle:** two co-resident instances; attempt to make instance A's `Set-NetAdapterRss` change instance B's observed throughput or queue count. → **Expected refuted** — Nitro virtualizes ENA queues and vCPUs per-instance; no shared RSS/queue/interrupt surface (consistent with the Linux sibling's Area 5.2 conclusion that interrupt-moderation disable is single-tenant self-DoS only).
- **Severity-if-true:** cross-tenant performance interference would be High — but it is **expected impossible**; the self-DoS reading is **out of scope** (single-tenant self-inflicted).

### Area 3 — Doc-currency / published-characteristic notes (Lens U / O — Informational)
- **TCP chimney offloading** "deprecated as of Windows Server 2016" — a currency note; no boundary. (If anything, disabling a deprecated offload is security-neutral-to-positive.)
- **Cluster-placement-group latency** "50us … 200us at the 99.9 percentile" — a **published performance characteristic**, not a disclosure of any other tenant's data. Not an info-leak lead.
- **"already configured on official Windows AMIs"** (RSS, checksum offload) — a statement about AMI defaults; no caller-controllable surface. (Lens U: the "guarantee" here is just a default state, enforced by AMI build, with no IAM claim to contradict.)

### Area 4 — Cluster placement group → co-residency / topology (CROSS-REFERENCE ONLY — do NOT restate)
The page's cluster-placement-group sentence (line 15) touches the same co-residency/topology surface the Linux sibling cross-refers. The real control-plane keys (`ec2:PlacementGroupStrategy`, `ec2:PlacementGroupName`) and the `DescribeInstanceTopology` co-residency oracle are **OWNED BY `ec2-networking-attack-research-plan.md` (Cluster 3)**. Nothing to add here; do not re-derive. (Nitro/Dedicated-Host *tenancy* — `ec2:Tenancy` + host actions — remains a flagged **CORPUS GAP** per the Linux sibling; no `*dedicated-host*` plan exists yet.)

### Area 5 — MTU (`network_mtu.html`) — CROSS-REFERENCE, **NULL** (dedicated sub-analysis done 2026-10-15)
The page links MTU tuning to `network_mtu.html` (line 13). A dedicated boundary analysis of `network_mtu.md` (offline==online byte-identical) returns **NULL** — no net-new attack surface for this plan to own:
- **No control-plane surface:** `grep -ni "mtu\|jumbo" list_ec2.md` → **zero hits**; MTU is set via guest-OS tooling (`netsh interface ipv4 set subinterface` on Windows / `ip link` on Linux), not an EC2 API. No `ModifyNetworkInterfaceAttribute`/`Describe*`/ARN/role/URL/secret/tenant-id on the page.
- **Jumbo frames are boundary-crossing *by design*, but AWS's fabric enforces the caps, not the guest:** documented hard caps — "**MTU limit 1500 bytes** — Traffic over an internet gateway / VPN / between AWS Regions (unless a transit gateway is used)"; "**MTU limit 8500 bytes** — Traffic over an inter-region VPC peering connection"; oversized packets are "fragmented … or dropped if the `Don't Fragment` flag is set." This is a **capacity/throughput boundary**, not a tenant-isolation boundary a guest can violate — one tenant's MTU setting does not reach another tenant's packets/bandwidth. Blast radius of misconfig = self (connectivity/perf).
- **PMTUD / ICMP = classic self-DoS black-hole, not a cross-tenant primitive:** the page warns ICMP "Type 3, Code 4 (Fragmentation Needed)" can be filtered by the operator's **own** SG/NACL → sender never shrinks packets → connection hangs. Every actor is "the originating/receiving host" in the reader's own topology; no documented cross-tenant ICMP injection/spoof seam.
- **Guarantee words:** the only absolute is "An internet gateway … will forward packets **up to 1500 bytes only**" (an AWS-fabric performance cap, not an access-control claim); "PMTUD **does not guarantee** jumbo frames won't be dropped" is a disclaimer, not a control.

**Verdict:** cross-reference only; **no dedicated workstream warranted.** If a hunter wants a one-line residual, the only Windows-specific thing worth a glance (not a lead — no Claim/Mechanism/Oracle exists) is whether the Windows MTU-setting path (`netsh`) differs from Linux in any enforcement detail; the page itself furnishes nothing security-relevant.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| RSS affinity config crosses to another tenant | ENA RSS queues / vCPU map | Per-instance Nitro virtualization (implicit — not an IAM control) |
| Knob corresponds to an IAM-scopable control-plane action | (none) | N/A — confirmed zero `ec2:*` surface via `list_ec2.md` grep |
| Operator runs attacker code by following the page | learn.microsoft.com links | HTTPS doc hyperlinks (not script fetch); safe inline example cmdlets |
| Jumbo-frame / MTU change affects a shared fabric or peer | MTU (network_mtu) | See Area 5 cross-ref verdict |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Single-tenant self-DoS / self-performance-degradation** from a wrong RSS affinity mask or a stale mask after resize — the operator harming their own instance. Explicitly out of scope.
- **IMDS / Nitro / host plane on a fully-managed device** — the Nitro ENA device is AWS-owned; the page gives the guest no channel to it. Not a test target; a disclosure line only.
- **Microsoft's documentation supply chain** — a compromise of `learn.microsoft.com` is Microsoft's defect, not AWS's.
- **Product/feature-parity gaps** (e.g. "Windows AMI defaults differ from Linux") — not a vulnerability.
- **Guest-OS CPU-scheduling microarchitecture side-channels** from vCPU pinning — a theoretical class, bounded-null, not elevated absent a Nitro-specific lead (same stance as the Linux sibling's C-state note).

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire, with pages checked)
Pages checked for triggers: the **full target page** (35 lines, every heading/table/command/link read verbatim) + `list_ec2.md` (Service Authorization Reference, grepped) + the Linux sibling plan for parity.

- **A (IDOR):** N/A — no resource-by-ID API, no tenant/resource identifier anywhere on the page.
- **B / C (PassRole / credential vending):** N/A — no role/ARN, no `AssumeRole`, no credential field.
- **D / V (data→control / network segmentation):** N/A — no control ENI/VPC, no PrivateLink; the only "interface" is the guest's own NIC. (RSS queues are per-instance, not a shared segment.)
- **E (RBAC/privesc):** N/A — the only privilege is local Windows Administrator (customer-owned); no AWS role model on this page.
- **F (injection/translation):** N/A — no parser/translator; cmdlet args are integers (processor numbers), applied locally.
- **G (SSRF):** N/A — the two `learn.microsoft.com` links and the `network_mtu.html` link are **human-facing prose hyperlinks**, not fields the service dereferences/fetches/renders. No server-side fetch seam. (This is the explicit disposition the Step-1 discipline requires: triggers checked on every line; none is a server-dereferenced location.)
- **H (KMS/encryption context):** N/A — no keys/encryption on the page.
- **I (tagging/ABAC):** N/A — no tags.
- **J (OAuth/3P):** N/A.
- **K (prompt injection):** N/A — no LLM/agent.
- **L (DoS):** fires only as single-tenant self-DoS (Area 2) → out of scope.
- **M (shared-identifier interception):** N/A — no session/token/presigned-URL.
- **N (namespace migration):** N/A.
- **P (proofing/registration):** N/A — no gate/OTP/uniqueness workflow.
- **Q (upload):** N/A — no uploaded blob; the supply-chain-*adjacent* residue is captured under Area 1 (R/Q) as a doc-link, not an upload.
- **R / S (IAM-artifact / condition-key audit):** N/A — the page prints **no IAM policy JSON, no managed-policy ARN, no sample policy, no CFN/runbook permissions block**. (The one supply-chain-adjacent artifact is a *third-party doc link*, Area 1 — not an AWS-authored permissions artifact.)
- **T (cross-service secret reachability):** N/A — nothing generated/persisted.
- **U (doc-vs-enforcement):** fires only as Informational (Area 3) — no IAM/API claim to contradict.
- **W (attestation):** N/A.
- **X (action-family parity):** N/A — no AWS action, so no twin/legacy variant.
- **Y (transport/TLS/sig):** N/A — no AWS endpoint; the doc hyperlinks are HTTPS.
- **AA (share/revoke):** N/A — no share.
- **BB / CC / DD (canonicalization / upstream-context / cache):** N/A — no multi-parser request path, no authorizer, no cache.
- **EE (predictable-name land-grab):** N/A — no name the service resolves/creates.
- **FF (JWT/token validation):** N/A — no token.

**Doc gaps:** none material. The page is complete and self-consistent; offline==online byte-identical (verified 2026-10-15). The only pointer whose depth lives elsewhere is MTU (Area 5, cross-ref) and cluster placement groups (Area 4, owned by `ec2-networking`).

---

*Sibling cross-references: `ena-improve-network-latency-linux-attack-research-plan.md` (the Linux twin of this page — same NULL-dominant guest-OS-tuning shape); `ec2-networking-attack-research-plan.md` Cluster 3 (cluster-placement-group co-residency/topology); `enhanced-networking-ena` / `troubleshooting-ena` (the `enaSupport` `ec2:Attribute` surface, distinct from anything on this page). See `reference-aws-iam-service-auth-ref-url` for the `list_ec2` slug used in the control-plane grep.*
