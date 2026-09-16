# Enhanced Networking with ENA — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html` (target) + children `enabling_enhanced_networking.html`, `test-enhanced-networking-ena.html`, `ena-queues.html`, `troubleshooting-ena.html`, `troubleshoot-ena-driver.html`; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`. Cross-checked against live docs 2026-09-13 (**live == offline; no drift**).
Status: documentation-derived hypotheses only; nothing tested against a live account.

> **Relationship to sibling plan.** This is the **ENA-specific child slice** of the enhanced-networking hub. The hub plan (`skill-agent_..._enhanced-networking.html.md`) already frames the SR-IOV/ENA-Express/Intel-VF family. This plan is self-contained for the `enaSupport` + ENA-queue-allocation + ENA-driver surface and does **not** re-scope SR-IOV/ENA-Express/Intel VF (route those to the hub plan) or the general ENI surface (route to `using-eni` / `prefix-eni` plans). Where the two overlap on systemic anchors (no value-level condition key; `ModifyInstanceAttribute` multiplexing) they agree.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the ENA data path terminates on the **Nitro card / shared SR-IOV fabric**. The moment evidence touches ENA hardware isolation, another tenant's VF, the Nitro controller, or any AWS service-plane identity — stop, preserve evidence, flag for AWS-Security disclosure. Do not fuzz the ENA device/MMIO/queues toward the hypervisor.
- This is a **single-account, customer-side / in-guest** surface. There is no AWS multi-tenant fleet in the ENA *control* path (the customer owns the instance, the AMI, and the ENI). Lens A (cross-tenant IDOR), B/C (cross-account PassRole/vending), K (LLM), P (registration), J (OAuth) do **not** fire — see §8. The live value is concentrated in **IAM condition-key enforceability (S/U)**, **attribute-API multiplexing privesc (B/E variant)**, **availability/integrity via attribute flip (L/U)**, and **driver supply chain (G/TOFU)**.

---

## 1. Pentest Objectives
1. Determine whether an IAM grant intended to only "manage ENA" (`enaSupport`, `EnaQueueCount`) can be abused to change a **more dangerous** instance/ENI attribute (esp. `userData`) via the same multiplexed API → de-facto code-exec-on-instance privesc.
2. Determine whether an org/account can actually **enforce or forbid** an ENA-related setting (`enaSupport`, `EnaQueueCount`) at the *value* level via IAM condition keys, or whether the only lever is the coarse `ec2:Attribute` (name-only) key — and whether that key is case-/null-fail-open.
3. Determine whether the `enaSupport`-toggle availability hazard the docs themselves warn about ("might render … unreachable", PV instances become unreachable) is reachable by a low-privileged intra-account principal as an integrity/availability attack.
4. Determine whether the three write-paths that set `enaSupport` (`ModifyInstanceAttribute`, `RegisterImage`, AMI inheritance) enforce **parity** — i.e. whether a principal denied one path can still set it via another.
5. Assess the ENA driver install/upgrade flow as a **software supply-chain** (TOFU git clone + root compile) surface.

---

## 2. Components, Assets, and Design

**What the page is.** A thin sub-hub that (a) points customers at the ENA driver (Linux: GitHub `amzn/amzn-drivers`; Windows: managed-driver pages), (b) documents the `enaSupport` prerequisite/enable/test/disable lifecycle, and (c) documents configurable **ENA queue allocation** (`EnaQueueCount` per ENI). No API/IAM policy JSON is printed on the target page itself; the concrete API surface lives in the children.

**Assets / attributes.**
- `enaSupport` — a boolean attribute on **two** resource types: the **instance** (`EnaSupport` in `DescribeInstances`) and the **image/AMI** (`EnaSupport` in `DescribeImages`). Set on instance via `ModifyInstanceAttribute`; set on AMI via `RegisterImage`; **inherited** AMI→instance at launch. Flipping it wrong = instance unreachable at next boot.
- `EnaQueueCount` — per-ENI packet-processing queue count. Constraints: power of 2; ≤ vCPU count of the instance; capped per-ENI and per-instance by instance type (see `ena-queues.html` tables). Set at `RunInstances` (NIC spec), `AttachNetworkInterface`, or `ModifyNetworkInterfaceAttribute`; instance must be **stopped** to modify. Lives on the ENI **attachment** (`Attachment.EnaQueueCount`).
- The **ENA driver** (Linux kernel module `ena`; Windows ENA driver) — for non-Amazon-Linux/Ubuntu distros the doc instructs a `git clone https://github.com/amzn/amzn-drivers`, compile-as-root, `depmod`, `dracut -f`, grub edit (`net.ifnames=0`).

**Identity / plane.** All control actions are SigV4 EC2 APIs authorized by customer IAM in the customer's own account. Everything below `enaSupport` (the actual ENA device, SR-IOV VF, queues in silicon, keep-alive/reset, MMIO) is **Nitro-card / AWS-owned hardware** = shared-responsibility hard stop.

```
 Customer IAM principal
   │  ec2:ModifyInstanceAttribute(--ena-support / --no-ena-support)   [instance attr]
   │  ec2:RegisterImage(--ena-support)                                 [AMI attr, inherited at launch]
   │  ec2:RunInstances / AttachNetworkInterface / ModifyNetworkInterfaceAttribute(EnaQueueCount)
   ▼
 ┌───────────────────────── customer account / customer instance ─────────────────────────┐
 │  Guest OS  ──in-guest──►  ENA kernel driver (amzn-drivers, git-clone+root-compile: TOFU) │
 │                                     │                                                    │
 └─────────────────────────────────────┼────────────────────────────────────────────────┘
                                        ▼   (enaSupport flag gates whether guest gets the VF)
 ==================== HARD STOP: Nitro card / SR-IOV fabric / ENA device (AWS-owned) =======
```

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ModifyInstanceAttribute` (`--ena-support`/`--no-ena-support`) | POST | **Yes** | External | Toggle instance `enaSupport` (instance must be stopped, EBS) | Yes | IAM principal w/ `ec2:ModifyInstanceAttribute` on the instance | **Multiplexes ~20 attributes incl. `userData`, `instanceType`, `disableApiTermination`, `sriovNetSupport`, `instanceInitiatedShutdownBehavior`.** One action name. |
| `RegisterImage` (`--ena-support`/`--no-ena-support`) | POST | Yes | External | Bake `enaSupport` into an AMI (instance-store path) | Yes | `ec2:RegisterImage` | Attribute inherited by every instance launched from the AMI. Alt write-path for `enaSupport`. |
| `DescribeInstances` (`.EnaSupport`) | GET | No | External | Read instance `enaSupport` | Yes | `ec2:DescribeInstances` | Also returns `Attachment.EnaQueueCount`. Describe is unscopable per-field (see §5). |
| `DescribeImages` (`.EnaSupport`) | GET | No | External | Read AMI `enaSupport` | Yes | `ec2:DescribeImages` | — |
| `AttachNetworkInterface` (`--ena-queue-count`) | POST | Yes | External | Attach ENI with a chosen queue count | Yes | `ec2:AttachNetworkInterface` | `EnaQueueCount` on attachment. |
| `RunInstances` (NIC spec `EnaQueueCount`) | POST | Yes | External | Launch with per-ENI queue count | Yes | `ec2:RunInstances` | — |
| `ModifyNetworkInterfaceAttribute` (`EnaQueueCount`) | POST | Yes | External | Change queue count (instance stopped) | Yes | `ec2:ModifyNetworkInterfaceAttribute` | **Multiplexes ENI attributes** (SG, source/dest check, description, queue count) — same "one action, many attributes" shape as `ModifyInstanceAttribute`. |
| `git clone amzn/amzn-drivers` | n/a | n/a | in-guest | Fetch + compile ENA driver as root | n/a (guest egress) | in-guest root | Not an AWS API. TOFU supply chain. |

**Undocumented/console-hidden knob check:** The target page states "Enhanced networking cannot be managed from the Amazon EC2 console" for `enaSupport` — i.e. the ONLY way to set it is the API/CLI. That means any console-based least-privilege reasoning misses this attribute entirely; the API accepts it regardless of console exposure. `EnaQueueCount` *is* console-exposed (per-NIC). Confirm at hunt time whether the API accepts an `EnaQueueCount` value the console rejects (non-power-of-2, > vCPU) → validation-location delta.

---

## 4. Boundary-lens catalog — firing lenses

### ⭐ Lens B/E (variant: non-PassRole action reaching dangerous attribute) — attribute-API multiplexing privesc
**Claim:** An IAM policy written to let a principal "enable ENA" — e.g. `Allow ec2:ModifyInstanceAttribute` with a `Condition ec2:Attribute = "enaSupport"` (or with no condition at all) — actually lets that principal set **`userData`** (and `instanceType`, `disableApiTermination`, `sriovNetSupport`, `instanceInitiatedShutdownBehavior`) on the same instance, because `ModifyInstanceAttribute` is one action multiplexing ~20 attributes. Setting `userData` on a stopped instance + start = **code execution as root/SYSTEM at next boot**.
**Mechanism (doc evidence):** `enabling_enhanced_networking.html` — `aws ec2 modify-instance-attribute --instance-id … --ena-support`; the same CLI/action sets `--user-data`. The corpus-confirmed exemplar (`[[stop-start-plan]]`, `[[launch-instances-plan]]`, hub `[[enhanced-networking-plan]]`): `ec2:ModifyInstanceAttribute(userData)` is PassRole-equivalent.
**Confirm/Refute oracle:** Under a scoped role holding only `ec2:ModifyInstanceAttribute` (+ Describe/Stop/Start) intended for ENA: (a) call `modify-instance-attribute --ena-support` → expect allow; (b) call `modify-instance-attribute --user-data <canary>` on the same instance → **if allowed, boundary broken**. Then verify whether an `ec2:Attribute`-conditioned variant blocks (b): craft `Condition StringEquals ec2:Attribute enaSupport` and re-test (b) with the PascalCase request field.
**Preconditions:** ability to stop/start instance (EBS) to make `userData` effective. **Cost:** low. **Severity if true:** High (instance root via a grant that reads as "networking-only").
**Stop condition:** confirmed on one instance you own with a scoped role — do not pivot to other instances.

### ⭐ Lens S / U — no value-level condition key; `ec2:Attribute` case/null fail-open; enforceability gap
**Claim:** There is **no IAM condition key that scopes the *value* of `enaSupport` or `EnaQueueCount`** — the only relevant key is `ec2:Attribute`, which matches the attribute *name*, not its value or the resource's ownership context. Therefore an org cannot write "principals may set `enaSupport=true` but never `enaSupport=false`" (no downgrade guard), nor "no ENA queue count above N". Further, `ec2:Attribute` is a documented case-sensitivity fail-open shape (a Deny written against lowercase `enasupport` is inert when the request populates PascalCase), and absent-key `Null` handling may fail open.
**Mechanism (doc evidence):** the enable/disable/test pages expose only attribute *names*; no condition key appears anywhere on these pages. Sibling systemic anchor confirmed across `[[network-bandwidth-plan]]`, `[[burstable-unlimited-mode-plan]]`, `[[instance-optimize-cpu-plan]]`, `[[stop-start-plan]]` (case-fail-open), hub `[[enhanced-networking-plan]]` (marked DOC-GAP — resolve here).
**Confirm/Refute oracle:** Resolve the **Service Authorization Reference for `ec2`** at hunt time and grep the condition-key table for any key naming `enaSupport`/`EnaSupport`/`EnaQueue`/`ena`. Refute if such a value-level key exists. Confirm the gap if only `ec2:Attribute` is present. Then live-test: write a Deny with `Condition StringEquals ec2:Attribute "enaSupport"` (lowercase `s`) and attempt `--ena-support` — if it succeeds, case-fail-open confirmed. Test `Null: ec2:Attribute true/false` behavior.
**Preconditions:** IAM policy authoring in a test account. **Cost:** low. **Severity if true:** Medium (org posture unenforceable — AWS-owned governance gap; enabler for the B/E privesc above because the intended fine-grained guard cannot be written).

### Lens U / L (integrity + availability) — documented "renders instance unreachable" hazard as an attack
**Claim:** A low-privileged intra-account principal holding `ec2:ModifyInstanceAttribute` (+ Stop/Start) can **deliberately break a victim instance's connectivity** by toggling `enaSupport`: enabling it on an OS/kernel without a working `ena` module, or on a PV instance, makes it **unreachable at next boot**; `--no-ena-support` silently **downgrades** the instance to the stock adapter (performance/throughput regression, integrity of a networking SLA). The doc itself asserts the hazard.
**Mechanism (doc evidence):** target page: "Updating the ENA kernel driver and enabling the `enaSupport` attribute might render incompatible instances or operating systems unreachable." `troubleshooting-ena.html`: "If you enable enhanced networking for a PV instance or AMI, this can also make your instance unreachable." + documented `--no-ena-support` fallback.
**Confirm/Refute oracle:** On a disposable instance you own, with a scoped role, set `enaSupport` inconsistent with the running kernel, stop/start, and observe loss of reachability (integrity/availability breach demonstrated within your own account). This is a **single-account self/lateral-DoS** — do NOT run it against any instance you do not own.
**Preconditions:** stop/start rights on the target instance. **Cost:** low, disruptive. **Severity if true:** Medium (single-account integrity/availability; **not** cross-tenant). Raises to a real risk when combined with over-broad `ec2:ModifyInstanceAttribute Resource:"*"` in a shared account.

### Lens X — write-path parity for `enaSupport` (ModifyInstanceAttribute vs RegisterImage vs AMI inheritance)
**Claim:** `enaSupport` can be set through three paths, and a principal **denied** `ec2:ModifyInstanceAttribute` (or blocked by an `ec2:Attribute` condition) can still achieve an ENA-enabled instance by (a) `RegisterImage --ena-support` then launching, or (b) launching from an existing AMI that already carries `enaSupport=true` (inheritance). If governance only guards `ModifyInstanceAttribute`, the `RegisterImage`/inheritance paths are an unguarded twin.
**Mechanism (doc evidence):** `enabling_enhanced_networking.html` — "(Optional) Create an AMI … The AMI **inherits** the enhanced networking `enaSupport` attribute"; instance-store path uses `register-image --ena-support`. `troubleshooting-ena.html` disable path likewise uses RegisterImage `--no-ena-support`.
**Confirm/Refute oracle:** Under a role **denied** `ModifyInstanceAttribute` but allowed `RegisterImage`+`RunInstances`, produce an instance with `EnaSupport=true` (via `DescribeInstances .EnaSupport`). If it succeeds, the guard is bypassable. Check the `ec2` Service Authz Ref for any condition key on `RegisterImage` that constrains `ena-support` (expected: none).
**Preconditions:** RegisterImage/RunInstances rights. **Cost:** low. **Severity if true:** Low–Medium (governance-parity gap; the end-state — ENA enabled — is itself benign, so severity is bounded unless chained to the availability hazard above by baking a *broken* config into a shared AMI).

### Lens L — ENA queue allocation resource pressure (bounded)
**Claim:** Configurable `EnaQueueCount` lets a principal over- or mis-allocate queues; test whether the documented caps (power-of-2, ≤ vCPU, per-instance max) are enforced **server-side by the API** or only by the console, and whether one workload can starve another.
**Mechanism (doc evidence):** `ena-queues.html` — "The total per ENI and per instance is still capped"; "must be a power of 2"; "cannot exceed the number of vCPUs". Set via `attach-network-interface --ena-queue-count`, `RunInstances`, `modify-network-interface-attribute`.
**Confirm/Refute oracle:** Call `attach-network-interface --ena-queue-count` with a non-power-of-2 value, a value > vCPU, and a value that would exceed the per-instance cap; observe whether the API rejects (`ValidationException`) or the console-only rule is the gate. Queues are **per-instance hardware allocation capped by instance type**, so cross-tenant starvation is **not** reachable (bounded by the Nitro card) — refute cross-tenant here and route any hardware-fabric question to HARD STOP.
**Preconditions:** an ENI + stopped instance you own. **Cost:** low. **Severity if true:** Low (self-scoped mis-config / validation-location delta at most). No value-level condition key for `EnaQueueCount` → folds into the Lens S anchor above.

### Lens G / supply chain (TOFU) — ENA driver install
**Claim:** The AWS-published runbook for non-Amazon-Linux/Ubuntu distros instructs `git clone https://github.com/amzn/amzn-drivers`, compile and install as **root**, with **no signature/checksum verification** (trust-on-first-use). A MITM, a compromised mirror, or a typo-squat of the clone URL yields kernel-mode code execution in the guest. The prerequisite "Ensure that the instance has internet connectivity" widens the guest's egress for exactly this fetch.
**Mechanism (doc evidence):** `enabling_enhanced_networking.html` RHEL/SUSE/CentOS procedure — `git clone`, "Compile and install the `ena` kernel driver", `sudo depmod`, `dracut -f`. No GPG/sig step. Windows path routes to managed driver pages (`ena-adapter-driver-install-upgrade-win.html`, `ena-driver-releases-windows.html`) — check those for signed-driver / SHA-2 requirements (`troubleshoot-ena-driver.html`).
**Confirm/Refute oracle:** Documentation review — confirm no integrity verification is prescribed. This is **in-guest, customer-side**; runs in the customer's guest, not on any AWS-fetched path (no SSRF from AWS fleet identity). No live AWS-plane test.
**Preconditions:** none (doc-level). **Cost:** none. **Severity if true:** Low (customer-side, in-guest; AWS-published-runbook hygiene gap — worth flagging that the runbook omits any pin/verify step). **Not** a service-plane SSRF.

---

## 5. Recommended Areas of Focus (priority order)

1. **Area 1 — ⭐ ModifyInstanceAttribute multiplexing privesc (Lens B/E).** *Background:* the page's core action `modify-instance-attribute --ena-support` is the same action that sets `userData`. *Security Concern:* an ENA-scoped grant is a de-facto root-on-instance grant. *Test:* the Lens B/E oracle. *Severity:* High.
2. **Area 2 — ⭐ Condition-key enforceability (Lens S/U).** *Background:* only `ec2:Attribute` exists; no value/ownership key for `enaSupport`/`EnaQueueCount`. *Security Concern:* org cannot forbid an ENA downgrade or enforce a queue ceiling; `ec2:Attribute` case/null fail-open. *Test:* resolve Service Authz Ref + case-fail-open live test. *Severity:* Medium (AWS-owned governance gap; enabler for Area 1).
3. **Area 3 — Availability/integrity via attribute flip (Lens U/L).** *Background:* docs warn `enaSupport` toggle can render instance unreachable. *Security Concern:* intra-account low-priv DoS/downgrade. *Test:* own-account reachability-loss demonstration. *Severity:* Medium (single-account).
4. **Area 4 — Write-path parity (Lens X).** RegisterImage/inheritance bypass of a ModifyInstanceAttribute guard. *Severity:* Low–Medium.
5. **Area 5 — ENA queue caps + driver supply chain (Lens L + G/TOFU).** Validation-location delta on `EnaQueueCount`; runbook omits driver integrity verification. *Severity:* Low.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| ENA-scoped IAM grant sets `userData` → root | `ModifyInstanceAttribute` | (none documented — the action is a single multiplexed verb) |
| Org cannot forbid `enaSupport` downgrade / queue ceiling | IAM condition keys | `ec2:Attribute` (name-only) — insufficient; verify no value key exists |
| Case/null fail-open on `ec2:Attribute` Deny | IAM evaluation | claimed key match — test PascalCase/Null |
| Low-priv principal renders victim instance unreachable | `enaSupport` toggle + Stop/Start | doc warning only ("might render … unreachable") — no IAM guard |
| Guard on ModifyInstanceAttribute bypassed via RegisterImage/inheritance | `RegisterImage`, AMI inherit | (none — parity unverified) |
| API accepts `EnaQueueCount` the console rejects | `AttachNetworkInterface`/`ModifyNetworkInterfaceAttribute` | power-of-2/≤vCPU/cap rules — confirm enforced server-side |
| Unsigned ENA driver (TOFU git clone, root compile) | in-guest driver install | none in runbook (Linux); SHA-2/signed-driver on Windows |

---

## 7. Out-of-Scope Risk Categories
- **ENA device / SR-IOV fabric / Nitro card isolation, queues-in-silicon, keep-alive/reset, MMIO/register access** — AWS-owned hardware, shared-responsibility **HARD STOP**. Do not fuzz the ENA device toward the hypervisor or other tenants.
- **Cross-tenant queue starvation** — bounded by per-instance/per-type caps on the Nitro card; not reachable from the control plane.
- **SR-IOV / ENA Express (SRD) / Intel 82599 VF** — route to hub `[[enhanced-networking-plan]]`; co-residency/shared-fabric questions route to `[[instance-topology-plan]]` (and are hard-stop at the fabric).
- **General ENI attach/permission/source-dest-check surface** — route to `[[using-eni-plan]]` / `[[prefix-eni-plan]]`.
- **In-guest driver compilation** as an AWS-plane bug — it runs in the customer guest, fetched by the guest (not AWS fleet identity) → not service-plane SSRF; flagged only as runbook-hygiene (Low).
- Third-party repo bugs in `amzn/amzn-drivers` itself.

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens A (cross-tenant IDOR) — null.** Checked target + `enabling_enhanced_networking`, `test-enhanced-networking-ena`, `ena-queues`, `troubleshooting-ena`. All resources (`instance`, `image`, `ENI`) are owned in the caller's account and named by ownership-bound ids; no shared multi-tenant fleet in the ENA control path.
- **Lens B/C (cross-account PassRole / credential vending) — null.** No role-ARN input, no STS/session-policy, no `SecretsManagerAccessRoleArn`-style field on any ENA page. (The B/E *variant* fires — see Area 1 — but that is intra-account attribute-multiplexing, not cross-account PassRole.)
- **Lens K (prompt injection), P (registration/anti-abuse), J (OAuth), H/W (KMS/attestation), M (session interception), N (namespace migration) — null.** No LLM, onboarding gate, 3P linking, KMS/encryption-context, session token, or dual-namespace ARN on these pages.
- **Lens R — null (no artifact printed).** No AWS-managed policy, SLR, CFN snippet, or "Required IAM permissions" JSON is printed on the target or its children. (Contrast: siblings like `win-fast-launch` do print such artifacts.)
- **Lens O (audit) — Informational.** `enaSupport`/`EnaQueueCount` changes are `ModifyInstanceAttribute`/`ModifyNetworkInterfaceAttribute` CloudTrail events; no documented blind spot. The silent `--no-ena-support` **downgrade** (no alarm on performance regression) is a monitoring gap, folded into Area 3.
- **Doc gaps to close at hunt time:** (1) exact `ec2` condition-key set for `enaSupport`/`EnaQueueCount` — resolve the Service Authorization Reference (the hub plan left this open; close it here). (2) Whether `RegisterImage` exposes any `ena-support` condition key (expected: none). (3) Server-side vs console-only enforcement of the `EnaQueueCount` power-of-2/≤vCPU/cap rules.

---

### Completion note
- **Assigned skill:** `security-questionbuilder` (`/work/.claude/skills/security-questionbuilder`).
- **Target:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html` (+ 4 children).
- **Inputs read:** target page (live + offline, identical, no injected AI-agent/See-also block), `enabling_enhanced_networking`, `test-enhanced-networking-ena`, `ena-queues`, `troubleshooting-ena`; mirror grep for the ENA-queue API.
- **Result:** documentation-derived plan produced. 6 firing lenses (B/E ⭐, S/U ⭐, U/L, X, L, G-TOFU); 8 explicit null hypotheses with pages named.
- **Could not fully test (recommend hunter/orchestrator):** live resolution of the `enaSupport`/`EnaQueueCount` condition-key set; case/null fail-open live test on `ec2:Attribute`; server-side vs console `EnaQueueCount` validation delta. Hard stop remains the Nitro/SR-IOV fabric.
