# Troubleshoot the ENA Windows Driver (`troubleshoot-ena-driver.html`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-ena-driver.html`
(offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/troubleshoot-ena-driver.md`, 459 lines),
cross-read against `troubleshooting-ena.md` (the Linux counterpart), `ena-driver-releases-windows.md`
(the Windows driver changelog/version table), `monitoring-network-performance-ena.md`, and the
IAM Service Authorization Reference `list_ec2.md`. **Status: documentation-derived hypotheses only;
nothing tested against a live account.** Target page re-verified **offline==online byte-identical
2026-10-15** (WebFetch of the `.md` twin == offline mirror; section anchors `ts-ena-drv-reset`,
`ts-ena-win-sub-opt-config-notification`, `ts-ena-diagnostics-event-messages`, `ts-ena-drv-sc-conn`,
`ts-ena-drv-sc-unexpected-vsn`, `ts-ena-drv-perf-adj` all present in both).

> **What this page is.** A **guest-OS troubleshooting/diagnostics runbook** for the kernel-mode
> **NDIS Windows driver** of the Elastic Network Adapter (ENA). It documents: how to read ENA driver
> events in Device Manager / Event Viewer / Performance Monitor; a table of driver event-message IDs
> (`5001`–`5210`); a **device-pushed "sub-optimal configuration notification"** (event ID `59000`
> carrying a numeric *code* in a Binary-Data word); the **ENA adapter-reset mechanism** (device
> keep-alive → driver watchdog → reset; stuck-Tx detection; MMIO read-timeout → "surprise removal");
> five troubleshooting scenarios (unexpected driver version from Driver-Store ranking, device warning,
> timeout+reset error pair `5007/5205`, 6th-gen migration minimum-version table, sub-optimal interface
> performance); driver install via `ena.inf` / "Have Disk" / `PnPUtil`; and advanced-property tuning
> knobs (Receive Buffers, RSS, Max RSS Queues, Jumbo packets, LLQ Header Size Policy, Transmit Buffers,
> Metrics Refresh Interval). It introduces **no AWS control-plane API, no IAM policy JSON, no condition
> key, no cross-account surface, no server-side-fetched URL, no upload, no token/role field.**

## Relationship to existing plans (read first — this is a page-level deep-dive child)

This page is listed as a **lead source** by two existing hub plans, both of which already own the
control-plane / IAM / supply-chain surface around ENA:

- **`enhanced-networking-attack-research-plan.md`** (SR-IOV / ENA / ENA-Express hub) owns **Area 6 —
  AWS-authored driver-install insecure defaults** (`ena-adapter-driver-install-upgrade-win.md` Step-2
  mutable `…/ENA/Latest/AwsEnaNetworkDriver.zip` fetch, no SHA256/Authenticode verification, run as
  Administrator) [Lens R] and **Area 7 — ENA/ENA-Express metrics as a side-channel/oracle** [Lens O/L],
  plus the `enaSupport`/`sriovNetSupport` write surface and the `EnaSrdSpecification` unscopability.
- **`enhanced-networking-ena-attack-research-plan.md`** sharpens hub Area 6 (**Area N2** — the Windows
  enable runbook disables script-signing to run a checksum-free fetched installer) and declares
  **Lens G (SSRF) NULL** for the whole driver family (every fetch is dereferenced by the customer's own
  guest OS, not a control-plane fetch identity).
- **`enabling-enhanced-networking-attack-research-plan.md`** / **`test-enhanced-networking-ena-attack-research-plan.md`**
  own the `ModifyInstanceAttribute enaSupport` enable/verify surface and the bulk `DescribeInstances`
  read oracle.
- **`ena-queues-attack-research-plan.md`** owns `EnaQueueCount`/`DefaultEnaQueueCount` on
  `RunInstances`/`AttachNetworkInterface`/`ModifyNetworkInterfaceAttribute`.

**This plan therefore DOES NOT RESTATE** the driver-download Lens-R audit, the metrics side-channel,
the `enaSupport`/SRD write surface, or the SSRF-null reasoning — it **cross-references** them. It
**owns the one surface no sibling develops: the Nitro ENA device → guest kernel-driver notification /
reset / completion channel** documented *only* on this troubleshooting page (event-ID table, code
`59000`, keep-alive/watchdog/MMIO/surprise-removal reset mechanics), plus the Driver-Store
version-selection footgun and the single-tenant reset/jumbo-frame availability surface.

> **The honest headline:** this is overwhelmingly a **guest-OS, customer-owned, single-tenant** page.
> The AWS boundary-breach model finds **no cross-tenant, no cross-account, and no attacker-reachable
> control-plane boundary that originates on this page.** Its net-new value is (1) it is the clearest
> doc-level description of the **device↔guest-driver wire interface**, which *is* a real trust boundary
> (customer guest ↔ AWS Nitro service plane) — but one whose exploitable mechanism lives in the
> open-source driver + undocumented device spec, **not** in this page (doc-gap + hard-stop pointer);
> and (2) AWS's own driver changelog provides **confirmed historical memory-safety evidence** that this
> code class has shipped corruption bugs. Everything else is correctly out of scope and is stated as
> confidently as the in-scope leads.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost →
  Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP (applies to the only Critical-shaped lead here):** the device↔guest ENA interface is the
  customer-guest ↔ **AWS Nitro service-plane** boundary. The moment any evidence shows a guest→device
  path reaching the host, the hypervisor, Nitro firmware, or another tenant, **stop immediately,
  preserve evidence, and flag for AWS-Security disclosure.** Do not attempt to characterize or widen
  such a path. The ENA device, Nitro card, and host fleet are AWS's own service plane.
- Most leads below resolve to **out-of-scope / null** with pages named. That is the correct result for a
  guest-OS troubleshooting page and is what keeps a hunter off the shared-responsibility line.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Device→guest parser integrity:** demonstrate that a malformed / out-of-spec device notification
   (a crafted `59000` code word, an unexpected admin-queue completion req-id/offset, an oversized or
   mis-lengthed event payload) causes memory corruption, a hang, or a UAF **in the guest kernel driver**
   — i.e. the driver trusts a device-supplied length/offset/code before bounds-checking. *(Lens F. In
   practice only reachable by a Nitro-side defect → hard stop; here it is a doc-gap pointer to the
   open-source driver.)*
2. **Guest→device escape (HARD STOP):** demonstrate that admin-queue commands / Tx descriptors / MMIO
   writes a **malicious guest** emits reach the host, another tenant, or Nitro firmware. *(Not
   documented on this page; the real surface is the device spec + `amzn-drivers`. If pursued, it is a
   service-plane target — authorization required, hard stop on any hit.)*
3. **Driver-selection integrity:** show that Windows selects an **attacker-planted** driver package over
   the intended ENA package via Driver-Store ranking. *(Lens EE/R — requires local admin; local-privesc
   flavored, out of scope but documented.)*
4. **Availability:** show a reset / surprise-removal / jumbo-frame drop condition that is **cross-tenant**
   (not single-instance). *(Lens L — expected null: all documented reset causes are single-instance.)*

## 2. Components, Assets, and Design

**Customer-facing interface (this page).** None that is network-callable. The entire page is in-guest
Windows tooling: `devmgmt.msc`, `eventvwr.msc`, `resmon`, Performance Monitor, PowerShell
(`Set-NetAdapterRss`, `Restart-Computer`), `PnPUtil`, and the Device-Manager "Advanced" property tabs.

**Processes / hosts behind it.**
- **ENA Windows driver** — a **kernel-mode NDIS miniport driver** (C/C++), customer-owned, running in the
  customer's guest kernel. It parses device-pushed events, runs the keep-alive **watchdog**, handles
  resets and NDIS "surprise removal", and exposes advanced properties. *Native memory-safety code.*
- **ENA device** — PCI-attached, **Nitro-card-resident** (AWS host/service plane). Posts keep-alive
  (~1/sec), driver events, the `59000` sub-optimal-config notification, admin-queue completions, and MMIO
  register state. Can **device-initiate** a reset (driver v2.9.0 "support for asynchronous reset requests
  initiated by the device", per `ena-driver-releases-windows.md`).
- **CloudWatch agent** (optional, in-guest) — collects ENA Performance-Monitor counters into the
  account's **own** CloudWatch namespace (intra-account telemetry; see parent Area 7).

**Accounts / VPCs.** Only the **customer account / guest OS** appears on this page. The ENA device sits
on the **AWS Nitro host** (service plane). No data-plane/control-plane split, service account, or
multi-tenant fleet is documented or implied for the driver surface.

**Network interfaces / sockets.** The ENA adapter is the customer's own ENI. There is no documented
control ENI, storage ENI, or peer-tenant reachability from the driver.

**"Resource" & identifier shape.** No service resource, ARN, or opaque ID is defined on this page.
Identifiers present are **Windows-local**: driver event IDs (`5001`–`5210`, `59000`), the `ena.inf`
package, and advanced-property names. None is a cross-tenant handle.

**Identity.** None established on this page (no SigV4, no token, no session). The only IAM-adjacent action
reachable *near* this surface (not on this page) is `ec2:ModifyInstanceAttribute enaSupport` — owned by
the enabling/enhanced-networking plans.

**Untrusted-data entry → transform.** The one genuine transform seam: **device-pushed notifications →
guest kernel-driver parser → driver action** (log an event, open a config dialog, mark the adapter
unhealthy, initiate a reset, perform NDIS surprise-removal). This is the Lens-F surface.

```
AWS Nitro host / service plane          |   Customer guest OS (customer-owned)
                                        |
  ENA device (Nitro card) ──PCI/MMIO──┐ |
   • keep-alive (~1/s)                 | |   ┌──────────────────────────────────────┐
   • driver events 5001-5210           ├─┼──▶│ ENA Windows kernel driver (NDIS, C/C++)│
   • sub-optimal cfg event 59000(code) | |   │  • watchdog (keep-alive miss → reset)  │
   • admin-queue completions (req-id)  | |   │  • event parse → Event Viewer / 59000  │
   • device-initiated reset (v2.9.0+)  ─┘ |   │  • NBL egress completion (v2.8.0 fix) │
         ▲  guest→device: admin-queue /    │   │  • surprise-removal recovery          │
         │  Tx descriptors / MMIO writes    │   └───────────────┬──────────────────────┘
         └── HARD STOP boundary ────────────┘                   │ Perf-Mon counters
   (customer guest ↔ Nitro service plane)                       ▼
                                        |   CloudWatch agent → account's own CW namespace
```

## 3. API / Interface Inventory

No AWS SDK/API, console route, or non-SDK endpoint is introduced by this page. For completeness, the
only machine interfaces touched are **in-guest** and **device-local**:

| Name | Type | Mutating | Internet-callable | Authorized caller | Notes |
|---|---|---|---|---|---|
| Device-Manager advanced properties (RSS, Jumbo, buffers, LLQ, Metrics Refresh) | Guest config | yes (local) | no | local admin | §`ts-ena-drv-perf-adj`; no IAM, no boundary |
| `Set-NetAdapterRss` (exclude CPU 0) | Guest PowerShell | yes (local) | no | local admin | §`ts-ena-drv-sc-conn` reset mitigation |
| `PnPUtil` / "Have Disk" `ena.inf` install | Guest driver install | yes (local) | no | local admin | §`ts-ena-drv-sc-unexpected-vsn`; Driver-Store ranking |
| ENA device notification/reset channel | PCI/MMIO + admin queue | n/a (device-pushed) | no | the Nitro device | **Lens F / hard-stop boundary**; wire format undocumented here |
| `ec2:ModifyInstanceAttribute enaSupport` *(off-page)* | Control-plane API | yes | yes | IAM principal | **Owned by enabling/enhanced-networking plans — not this one** |

No `[NEW]` marker, no "testing should focus on…" sentence, and no undocumented/console-hidden
auth-weakening parameter appears on this page.

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| **AWS Nitro ENA device** (service plane) | **Customer guest kernel driver** | device-pushed keep-alive / events / `59000` code / admin-queue completions parsed by the driver | **Memory corruption, UAF, OOB, or hang in the guest driver from a device-supplied length/offset/code** = a parser defect (AWS-owned driver). Source is AWS-controlled → not a customer-reachable attack primitive; relevant only as driver robustness / a Nitro-firmware-defect amplifier. |
| **Customer guest** (malicious) | **ENA device / Nitro host** | guest→device admin-queue commands, Tx descriptors, MMIO writes | **Any guest-emitted request reaching the host, hypervisor, Nitro firmware, or another tenant = HARD-STOP service-plane breach.** Not documented on this page; mechanism lives in the device spec + `amzn-drivers`. |
| **Local attacker (admin) in guest** | **Which driver package Windows loads** | Driver-Store package ranking; `ena.inf`/"Have Disk" | **Windows loads an attacker-planted package instead of the intended ENA driver.** Requires local admin → local-privesc/persistence, single-tenant, customer-owned. |
| **Any guest workload** | **This instance's network availability** | keep-alive-miss / stuck-Tx / MMIO-timeout reset; CPU-0 starvation false-positive; jumbo+DF drops | **Instance network impaired.** Single-instance only; no documented cross-tenant effect. |
| **CloudWatch agent** | **Account CloudWatch** | Perf-Mon counter collection | Intra-account telemetry; no boundary crossing (see parent Area 7). |

## 5. Recommended Areas of Focus (one block per firing lens)

### Area 1 — Device→guest driver notification/completion parsing [Lens F — native memory-safety] — PRIMARY net-new
**Background.** The ENA device **pushes** structured data into the guest kernel driver through three
documented channels (§`ts-ena-drv-reset`, §`ts-ena-win-sub-opt-config-notification`,
§`ts-ena-diagnostics-event-messages`): (1) **keep-alive** events (~1/sec) consumed by the driver
watchdog; (2) a **sub-optimal-configuration notification, event ID `59000`,** whose action **code is a
device-supplied word** the driver reads from "Binary Data: In words … the last word is the code"
(troubleshoot-ena-driver.md:156); (3) **admin-queue completions / MMIO register reads** with
device-chosen req-ids and offsets (the Linux twin logs `expected: req id[1] … actual: req id[57006]`).
Driver v2.9.0 added "**asynchronous reset requests initiated by the device**", so the device can drive a
guest reset path directly.
**Security Concern.** A kernel-mode NDIS driver that parses device-supplied codes, lengths, req-ids, and
completion descriptors is classic native-memory-safety surface. **AWS's own changelog confirms this code
class has shipped corruption bugs:** ENA Windows driver **v2.8.0** "**Fixed a race condition in the
complete flow of egress network buffer list (NBL) processing, which could lead to memory corruption
caused by attempting to release an NBL that was already released**" (`ena-driver-releases-windows.md`) —
a double-free in the egress completion path. This is documentary proof the device↔driver completion
handling is a live memory-safety area, not a hypothetical.
**High-level Test Scenarios (falsifiable claims).**
- *Claim:* the driver trusts the device-supplied `59000` code word (and admin-queue req-id/offset) before
  bounds/range-checking → a malformed value yields OOB/UAF/hang. *Mechanism:* code-word read at
  troubleshoot-ena-driver.md:156; completion-handling double-free (v2.8.0). *Oracle:* in the open-source
  `amzn-drivers` Windows ENA source (and the ENA device spec), trace the `59000` code and NBL/admin-queue
  completion handlers; confirm whether a device-controlled length/offset/req-id indexes a buffer or frees
  a descriptor without validation. *This is a code/spec review, not a live test.*
- *Claim:* a device-initiated async reset (v2.9.0+) during in-flight egress can re-enter the
  already-fixed completion path. *Oracle:* diff the v2.8.0 fix against the v2.9.0 async-reset change for a
  re-introduced race.
**Preconditions / Cost / Severity.** Precondition to *trigger* from the attacker side: control of the
**device** source — i.e. a Nitro-firmware/service-plane position (**hard stop**) — so this is **not a
customer-reachable primitive**. Value is as **AWS-owned driver robustness** (a crash/corruption reachable
only by AWS's own device is a reliability/defense-in-depth finding) and as the **doc-gap pointer** to the
real guest→device boundary (Area 2). **Severity-if-a-customer-reachable-trigger-is-found:** High (guest
kernel corruption); if only device-reachable: Low/robustness. **Stop condition:** any sign the path
reaches beyond the single guest → hard stop.

### Area 2 — Guest→device admin-queue / descriptor interface [Lens D/V — data-plane ↔ service-plane] — HARD STOP, doc-gap
**Background.** The inverse direction of Area 1: the guest driver issues admin-queue commands, posts Tx/Rx
descriptors, and performs MMIO reads/writes to the Nitro-resident ENA device. This page describes the
*symptoms* (MMIO read-timeout → "surprise removal", stuck-Tx detection) but **not the wire protocol**.
**Security Concern.** This is the genuine **customer-guest ↔ AWS service-plane** boundary. The research
question is whether a **malicious guest** (which fully controls its own driver/kernel) can craft
admin-queue commands, descriptor rings, or MMIO sequences that the Nitro device mishandles to reach the
host, Nitro firmware, or another tenant on the same card.
**High-level Test Scenarios.** *Claim:* a crafted admin-queue command / out-of-range descriptor pointer
from the guest escapes the guest's address space or affects another tenant. *Mechanism:* undocumented —
the device spec and `amzn-drivers` are the only sources; this troubleshooting page confirms only that such
a channel exists (keep-alive, admin queue, MMIO, surprise-removal). *Oracle:* **not resolvable from
documentation.** Mark **doc-gap — confirm surface first** via the ENA device specification + driver
source, under explicit AWS authorization only.
**Preconditions / Cost / Severity.** **Service-plane target. HARD STOP.** Do not probe a live ENA device
for escape without authorization; on any evidence of host/tenant reach, stop and disclose.
**Severity-if-true:** Critical (hypervisor/cross-tenant). This plan's role is to **name the boundary and
stop**, not to pursue it.

### Area 3 — Driver-Store version-selection / planted-package [Lens EE / R] — local, cross-ref parent Area 6
**Background.** §`ts-ena-drv-sc-unexpected-vsn`: "Windows ranks all of the driver packages that are valid
for the given device in the local Driver Store … selects the package with the lowest rank value as the
best match. This can be different from the package that you intended to install." Mitigation: `PnPUtil`
removal of lower-ranked packages; install the intended `ena.inf` via "Have Disk".
**Security Concern.** A **predictable-name / shadow-resource (land-grab) shape at the Driver-Store level**:
a local attacker who can place a competing valid-for-the-device package in the Driver Store can bias
Windows into selecting **their** package (persistence / tampered NIC driver). This chains with the
parent plans' **Area 6 / N2** supply-chain finding — the AWS-published Windows install runbook fetches the
`…/ENA/Latest/AwsEnaNetworkDriver.zip` with no checksum/Authenticode step and disables script-signing
(`enhanced-networking-ena` Area N2) — so a MITM/compromise of the install step *is* the way to get a
malicious package into the Store in the first place.
**High-level Test Scenarios.** *Claim:* an attacker-planted ENA-compatible package ranks at/under the
intended one and is auto-selected. *Oracle:* confirm Driver-Store ranking inputs (INF date/version, WHQL
signature) and whether an unsigned/attacker package can out-rank; verify the fetched zip's integrity
posture (defer the download-integrity audit to parent Area 6 — **do not re-run it here**).
**Preconditions / Cost / Severity.** **Requires local Administrator** in the customer guest →
local-privesc / persistence, **single-tenant, customer-owned OS**. Mostly **out of scope** as a
standalone bug; **in scope only** as the downstream of the AWS-authored install runbook's missing
integrity step (parent Area 6/N2, Medium, reportable because AWS-authored). **Severity:** Low standalone;
inherits parent Area 6 Medium when reached via the unverified AWS install path.

### Area 4 — Adapter reset / surprise-removal / jumbo-frame drops as availability [Lens L / U] — single-tenant → mostly OOS
**Background.** §`ts-ena-drv-reset` + §`ts-ena-drv-sc-conn`: resets fire on missed keep-alive, stuck Tx, or
MMIO read-timeout (→ NDIS surprise removal); the detection "is subject to **false positives resulting from
CPU 0 starvation**" (mitigated by `Set-NetAdapterRss … -BaseProcessorNumber 1` to exclude CPU 0 on >16-vCPU
types). Jumbo frames (up to `9015` → 9001-byte payload) are **dropped** when the IP `Don't Fragment` flag
is set and MTU >1500 leaves a VPC (§`ts-ena-drv-jumbo-frames`).
**Security Concern.** Availability only. The lens question is whether any of these is **cross-tenant**.
**High-level Test Scenarios.** *Claim:* a tenant can induce resets or jumbo-drops on **another** tenant.
*Oracle:* every documented cause (CPU-0 starvation, keep-alive, stuck-Tx, MMIO, DF-drop) is **in-guest and
single-instance**; the docs state resets cause "minimal traffic disruption" and TCP "should be able to
recover". No shared-fleet or neighbor-reachable trigger is documented.
**Severity.** **Out of scope — single-tenant self-DoS / availability footgun** (per the catalog's explicit
exclusion). Documented so the hunter does not spend time trying to make it cross-tenant. The
**documented-guarantee** angle (Lens U — "minimal disruption", "should recover") is Informational: these
are advisory availability claims with no enforcement mechanism, not a security control.

### Area 5 — Metrics / event-log telemetry [Lens O] — cross-ref parent Area 7
**Background.** §`ts-ena-diagnostics-perf-metrics`: the driver publishes network-performance metrics
(Perf-Mon counters); with the CloudWatch agent installed, they flow to the account's CloudWatch namespace.
Event IDs and the `59000` code are visible in Event Viewer.
**Security Concern.** Whether metrics/events form a cross-boundary oracle or an audit-evasion gap.
**High-level Test Scenarios.** *Oracle:* the metric path is **intra-account** (guest → account CloudWatch),
no cross-tenant/cross-account crossing documented. The in-guest Event-Viewer/Perf-Mon audit surface is
customer-owned.
**Severity.** Informational; **defer the metrics side-channel/oracle depth to `enhanced-networking` Area 7
— do not re-derive it here.**

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Malformed device notification corrupts guest driver (Area 1) | ENA Windows kernel driver | NDIS bounds handling; v2.8.0 NBL double-free *fix* (prove no re-introduction) |
| Guest→device escape to host/tenant (Area 2) | ENA device / Nitro | Nitro isolation (service plane — HARD STOP, not customer-testable) |
| Planted driver package auto-selected (Area 3) | Windows Driver Store | WHQL/Authenticode signing; `PnPUtil` ranking cleanup; AWS install runbook (missing integrity step — parent Area 6) |
| Cross-tenant reset / jumbo-drop (Area 4) | Driver watchdog / MTU path | Resets single-instance; "minimal disruption"/"TCP recovers" (advisory, not a control) |
| Telemetry cross-boundary oracle (Area 5) | Perf-Mon / CloudWatch agent | Intra-account namespace (parent Area 7) |

## 7. Out-of-Scope Risk Categories (stated as confidently as in-scope)

- **The entire page is guest-OS / customer-owned.** Driver-Store ranking abuse, "Have Disk" / `ena.inf`
  install, `PnPUtil`, advanced-property tuning (RSS, Jumbo, Receive/Transmit Buffers, Max RSS Queues, LLQ
  Header Size Policy, Metrics Refresh Interval), and `Restart-Computer` all require **local admin in the
  customer's own instance** and cross no AWS trust boundary.
- **Single-tenant self-DoS / availability:** adapter resets, CPU-0-starvation false positives,
  surprise-removal recovery, jumbo-frame + Don't-Fragment drops. No cross-tenant trigger documented.
- **IMDS / enhanced-networking enable on managed hosts:** `ec2:ModifyInstanceAttribute enaSupport`,
  `sriovNetSupport`, `EnaQueueCount`, `EnaSrdSpecification` — **owned by the enabling / enhanced-networking
  / enhanced-networking-ena / ena-queues plans.** Not re-opened here.
- **Driver download-integrity audit (Lens R):** the mutable `…/ENA/Latest/` fetch, missing
  checksum/Authenticode, and script-signing-disable are **owned by `enhanced-networking` Area 6 /
  `enhanced-networking-ena` Area N2.** This plan only references them where Area 3 chains through them.
- **ENA / ENA-Express metrics side-channel:** owned by `enhanced-networking` Area 7.
- **AWS Nitro host, ENA device firmware, hypervisor, physical fleet:** AWS's own **service plane** — any
  guest→device escape (Area 2) is a **HARD STOP** disclosure target, not an in-scope hunting objective.
- **Third-party Microsoft documentation** linked from the page (surprise-removal, Driver-Store,
  device-manager error codes) — out of scope.

## 8. Null hypotheses / doc gaps (lenses that did not fire — pages checked named)

Pages read for all null determinations: `troubleshoot-ena-driver.md` (full, offline==online),
`troubleshooting-ena.md` (Linux twin), `ena-driver-releases-windows.md`, `monitoring-network-performance-ena.md`,
and the sibling plans listed in §Relationship.

- **Lens A (cross-tenant IDOR) — NULL.** No resource-by-ID API, tenant ID, opaque handle, or
  "revealed-after-step" disclosure appears on this page. Identifiers are Windows-local event IDs
  (`5001`–`5210`, `59000`) and a local `ena.inf`.
- **Lens B / C (PassRole / credential vending) — NULL.** No role ARN, `PassRole`, STS, session policy, or
  credential-provider field. (Nearest IAM action, `ModifyInstanceAttribute enaSupport`, is off-page.)
- **Lens G (SSRF) — NULL.** Checked every URL/path on the page: all are **doc hyperlinks**
  (learn.microsoft.com, repost.aws, docs.aws.amazon.com) or a **local file path** (`ena.inf`). No field is
  dereferenced server-side by an EC2 fetch identity. Consistent with the parent plans' explicit SSRF-null.
- **Lens H (KMS) — NULL.** No key, encryption context, or `kms:*` reference.
- **Lens I (tagging/ABAC) — NULL.** No tag field or `TagResource` action.
- **Lens J (OAuth/3P) — NULL.** No linking, `state`, callback, or 3P integration.
- **Lens K (prompt injection) — NULL.** No LLM/agent/knowledge-base in the pipeline.
- **Lens M (shared-identifier interception) — NULL.** No session_id, JWT, presigned URL, or socket-routed id.
- **Lens N (namespace migration) — NULL.** No dual ARN/endpoint; driver versions are not a security namespace.
- **Lens P (registration/proofing) — NULL.** No onboarding, OTP, uniqueness, or "must reach success before" gate.
- **Lens Q (upload) — NULL.** `ena.inf`/the driver zip is a **local guest install**, not a service-side
  upload parsed across a tenant boundary. (Its *integrity* is parent Area 6, Lens R.)
- **Lens R / S (IAM-artifact audit) — NULL on this page.** No policy JSON, managed policy, CFN, or
  "Required IAM permissions" block is printed here. (The AWS-authored *install runbook* that does carry a
  weak default is a different page, owned by parent Area 6 / N2.)
- **Lens U (doc-vs-enforcement) — fired weakly (Area 4):** the availability guarantees ("minimal
  disruption", "TCP connections should be able to recover") are advisory prose, not enforced controls —
  Informational only. No security-capability table with a `Describe*` equivalent on this page.
- **Lens W (attestation) — NULL.** No PCR/enclave/`kms:RecipientAttestation`.
- **Lens X (action-family parity) — NULL.** No action family; Linux-vs-Windows driver are platform twins,
  not an authz-parity surface.
- **Lens Y (transport/TLS/SigV4) — NULL.** The surface is a NIC driver, not an HTTP endpoint. (TLS-1.2
  enablement for the driver *download* is parent Area 6.)
- **Lens AA (share/revoke lifecycle) — NULL.** No share, grant, or revoke operation.
- **Lens BB / CC / DD / FF — NULL.** No multi-parser HTTP path, trusted-upstream header, cache layer, or
  JWT/OIDC validation anywhere on this page.

**Doc gaps carried for the hunter (confirm surface before investing):**
1. **(Highest value, but service-plane / hard-stop)** The device↔guest ENA **wire protocol** — admin-queue
   command format, descriptor-ring layout, the `59000` code semantics and value range, and the
   async-reset (v2.9.0) handshake — is **not documented** on this or any adjacent User-Guide page. Resolve
   via the ENA device specification + the open-source `amzn-drivers` Windows source, under AWS
   authorization only. This is where Area 1 (parser robustness) and Area 2 (guest→device escape, hard
   stop) are actually decided.
2. Whether the v2.9.0 "asynchronous reset requests initiated by the device" change re-touched the egress
   NBL completion path fixed in v2.8.0 (re-introduced double-free) — a changelog/source diff.
3. Whether a device-supplied `59000` code or admin-queue req-id is range-checked before use as an index
   or free target in the Windows driver (source review).

---
*Plan built with the `security-questionbuilder` skill. Verdict: a guest-OS troubleshooting page with no
originating cross-tenant/cross-account/control-plane boundary; net-new value is the device↔guest-driver
Lens-F surface (confirmed historical corruption bug in the class) and the hard-stop pointer to the
guest→Nitro boundary. Driver-install (Lens R) and metrics (Lens O) are cross-referenced to the
`enhanced-networking` / `enhanced-networking-ena` parent plans, not restated.*
