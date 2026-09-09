# EC2 CPU Options (Optimize CPUs) — Attack Research Plan

Source of leads:
- `AWSEC2/latest/UserGuide/instance-optimize-cpu.html` (hub) + its 5 children: `instance-cpu-options-rules.html`, `cpu-options-supported-instances-values.html`, `instance-specify-cpu-options.html`, `view-cpu-options.html`, `optimize-cpu.html`.
- API ref: `AWSEC2/latest/APIReference/API_ModifyInstanceCpuOptions.html`, `API_RunInstances.html` (CpuOptions request struct).
- IAM: `service-authorization/latest/reference/list_ec2.md` (authoritative action→resource→condition-key mapping, read offline 2026-09-08).

Status: **documentation-derived hypotheses only; nothing tested against a live account.** Online page fetched 2026-09-08 — content identical to offline mirror; **no injected "run this aws CLI" agent block on any of the CPU-options pages** (unlike some other EC2 UserGuide pages — see `[[project_aws-docs-see-also-injection]]`).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left/right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (billing/metering fleet, hypervisor scheduler), stop, preserve evidence, flag for AWS-Security disclosure.
- **Reality check up front:** this is a *thin, single-account, customer-controlled instance-configuration* surface — the same archetype as `[[project_burstable-unlimited-mode-plan]]`, `[[project_burstable-standard-mode-plan]]`, and `[[project_ec2-instance-resize-plan]]`. There is **no multi-tenant shared fleet, no service account, no untrusted-content parser, no server-side fetch, no role/credential vending** in this feature. Most lenses are genuine null hypotheses (Section 8). The value is concentrated in **two** places: (1) an IAM **governance/condition-key gap** over CpuOptions values (Lens S/U/R — doc-confirmed), and (2) **license-fee billing-integrity** of the Optimize CPUs metering (Lens U). Do not inflate the rest.

---

## 1. Pentest Objectives (concrete breach outcomes to aim for)
1. **Govern-value bypass:** demonstrate that an org/SCP author *cannot* write an IAM policy that constrains the CoreCount / ThreadsPerCore a principal sets (cannot force a minimum vCPU, cannot forbid SMT-disable, cannot cap cores) — because no condition key exists. (Governance gap, AWS-owned.)
2. **License-fee integrity:** determine whether the third-party license fee billed under "Optimize CPUs" is bound to a vCPU count the hypervisor actually enforces, or to a separately-tracked attribute a customer could make diverge from real compute (underpayment) — and whether the "< 4 vCPU ⇒ default billing" gate can be gamed by mid-period `ModifyInstanceCpuOptions` toggling.
3. **Write-path validation parity:** confirm the "you cannot exceed the default number of vCPUs" and instance-type-support rules are enforced identically across all three write paths (`RunInstances`, `CreateLaunchTemplate`, `ModifyInstanceCpuOptions`), including launch-template deferred-validation / `$Latest`/`$Default` late-binding.
4. **`ec2:Attribute` scoping soundness:** confirm whether a Deny keyed on `ec2:Attribute` actually applies to the *dedicated* `ModifyInstanceCpuOptions` API (or fails open because the key is unpopulated / case-mismatched) — the same shape as the confirmed `[[project_ec2-instance-resize-plan]]` `ec2:Attribute` case-fail-open lead.
5. **Cross-account instance IDOR (baseline):** confirm `ModifyInstanceCpuOptions` binds the target `instance-id` to the caller's account (expected to hold; verify it is not existence-only).

---

## 2. Components, Assets, and Design

**Feature.** "CPU options" lets a customer set two knobs on an EC2 instance:
- **`CoreCount`** — number of active CPU cores (≤ instance-type default cores).
- **`ThreadsPerCore`** — 1 (SMT/hyper-threading disabled) or 2 (default where supported).
- Derived: **vCPUs = CoreCount × ThreadsPerCore**, and **"you cannot exceed the default number of vCPUs for the instance type."**
- Sibling field in the same `CpuOptions` struct: **`AmdSevSnp`** (AMD SEV-SNP confidential compute) — surfaced in `describe-instances` / `Get-EC2Instance` output. **Out of scope here** → route to the confidential-compute / SEV-SNP / NitroTPM plans (`[[project_nitrotpm-plan]]`, `[[project_aws-instancetypes-existing-reports]]`).

**Interfaces / write paths (all SigV4 EC2 Query API, single account):**
- `RunInstances --cpu-options "CoreCount=..,ThreadsPerCore=.."` (at launch).
- `CreateLaunchTemplate` / `CreateLaunchTemplateVersion` — `LaunchTemplateData.CpuOptions` (stored spec, applied at later launch).
- `ModifyInstanceCpuOptions --instance-id --core-count --threads-per-core` — **post-launch; instance must be `Stopped`.** Dedicated API (NOT `ModifyInstanceAttribute`). Persists across stop/start/reboot.
- Read: `DescribeInstances …CpuOptions`.

**Assets / trust context:**
- The only "asset" is the **instance's CPU configuration** and the **billing/metering record** derived from it. Both live in the customer's own account.
- **Billing plane (AWS-owned):** "Optimize CPUs for License-Included instances" meters third-party license fees on the **active vCPU count** for license-included Windows / SQL Server AMIs (rate table: Windows `RunInstances:0002` $0.046/vCPU-hr; SQL Enterprise `:0102` $0.421; SQL Standard `:0006` $0.166; SQL Web `:0202` $0.063). For all other instances "you're charged the same as … default CPU options" (no additional charge for CpuOptions itself). This billing plane is the shared-responsibility line — **do not probe the metering fleet.**
- **Quota plane (AWS-owned):** doc explicitly states vCPU **quota** consumption is computed on **default** vCPUs and is **not** affected by CpuOptions — closes the "reduce CpuOptions to run more instances" DoS/quota-gaming angle (see Section 8, Lens L null).

```
customer principal (SigV4)
  │  RunInstances / CreateLaunchTemplate / ModifyInstanceCpuOptions
  ▼
EC2 control plane ──(sets CpuOptions attribute on instance)──► instance (customer account)
  │                                                              │
  │                                                              ▼
  └── active-vCPU value ──► Billing/metering plane (AWS-owned)  hypervisor enforces core/thread allocation
                            └─ license-included: fee = f(active vCPU)   [Optimize CPUs]
```
No control ENI, no data-plane→control-plane path, no cross-account fan-out. The single trust boundary that matters is **customer principal → CpuOptions attribute (IAM authz)** and the **derived boundary customer config → license-fee metering**.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv principal in account | An instance's CpuOptions | `ModifyInstanceCpuOptions` / `RunInstances` | Setting core/thread values an org policy *intended* to forbid — because no condition key exists to forbid it. **Breach = value change that no IAM policy could have blocked.** |
| Principal denied by an `ec2:Attribute` Deny | Same instance's CpuOptions | dedicated `ModifyInstanceCpuOptions` API | The modify succeeds despite a Deny keyed on `ec2:Attribute` (key unpopulated / case-mismatch for this API). **Breach = fail-open.** |
| Customer instance config | AWS license-fee metering | active-vCPU accounting | Actual scheduled compute > billed vCPU count, or "< 4 vCPU ⇒ default billing" gate mis-evaluated across a mid-period toggle. **Breach = license underpayment / metering divergence.** (Billing-integrity, AWS-owned; **stop at metering plane.**) |
| Caller-supplied `instance-id` | Another account's instance | `ModifyInstanceCpuOptions` | 200/accept on a foreign instance-id. **Breach = cross-account mutation** (expected NOT to happen — verify). |
| Launch-template CpuOptions (stored) | Later launch validation | `$Latest`/`$Default` late-binding | Invalid/over-default CpuOptions accepted at template-create, or a launch consumes a version whose CpuOptions the launcher couldn't set directly. Chains to `[[project_launch-templates-plan]]`. |
| **Any customer surface** | **AWS service plane** (hypervisor scheduler / metering fleet) | — | **Hard stop.** Any AWS-owned identity/credential/host = disclosure. |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ModifyInstanceCpuOptions` | POST (Query) | **Yes** | Yes | Set CoreCount/ThreadsPerCore on a **Stopped** instance | Yes (SigV4) | account principals w/ `ec2:ModifyInstanceCpuOptions` | Resource: `instance*`. **Condition keys: `aws:ResourceTag`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:AvailabilityZone(Id)`, `ec2:CpuOptionsAmdSevSnp`, `ec2:EbsOptimized`, `ec2:InstanceType`, `ec2:ManagedResourceOperator`, `ec2:Metadata*`, `ec2:ProductCode`, `ec2:Region`, `ec2:ResourceTag`, `ec2:RootDeviceType`, `ec2:Tenancy` — NO `ec2:CoreCount`, NO `ec2:ThreadsPerCore`.** |
| `RunInstances` (`--cpu-options`) | POST | Yes | Yes | Set CpuOptions at launch | Yes | account principals | Same absence: instance-resource condition keys include `ec2:CpuOptionsAmdSevSnp` but **no core/thread-value key**. |
| `CreateLaunchTemplate` / `…Version` | POST | Yes | Yes | Store `LaunchTemplateData.CpuOptions` | Yes | account principals | Validation timing of CpuOptions unclear from docs → **doc-gap, confirm.** |
| `DescribeInstances` (`…CpuOptions`) | GET | No | Yes | Read CoreCount/ThreadsPerCore/AmdSevSnp | Yes | account principals | Read path; also exposed via guest `lscpu`/Task Manager and AWS Config. |

**Undocumented/console-hidden knob check:** the API `CpuOptions` struct carries `AmdSevSnp` (not exposed on these UserGuide pages except in view output) — but it *has* a dedicated condition key, so it is *more* governable than the core/thread knobs that the console foregrounds. The delta worth flagging: **the console-prominent knobs (cores/threads) are the ungovernable ones; the console-hidden knob (SevSnp) is the governable one.**

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — CpuOptions value-governance gap: no `ec2:CoreCount` / `ec2:ThreadsPerCore` condition key  *(Lens S / U / R — CROWN JEWEL, doc-confirmed)*
**Background.** `CpuOptions` has three sub-fields. AWS shipped an IAM condition key for exactly one of them — **`ec2:CpuOptionsAmdSevSnp`** ("Filters access by the state of AMD SEV-SNP CPU Options") — and attached it to `RunInstances`, `ModifyInstanceCpuOptions`, `ModifyInstanceCreditSpecification`, and the `instance` resource type. It shipped **no** condition key for `CoreCount` or `ThreadsPerCore`.
**Security Concern.** Because no `ec2:CoreCount` / `ec2:ThreadsPerCore` key exists, an org/SCP/permission-boundary author **cannot**:
- force a **minimum** vCPU/core count (e.g., to stop a principal silently down-configuring a license-included SQL box to under-report license fees, or to stop a noisy self-inflicted right-sizing);
- **forbid disabling SMT** (`ThreadsPerCore=1`) on instances where the security team requires it;
- **cap** the cores a principal may activate.
The existence of `ec2:CpuOptionsAmdSevSnp` proves AWS knows how to mint a CpuOptions-sub-field condition key and chose not to for the two value knobs — this is an AWS-owned gap, not a customer artifact. Mirrors the confirmed `[[project_burstable-unlimited-mode-plan]]` finding (**no CpuCredits-value condition key**) exactly.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** `iam:SimulateCustomPolicy` shows that no combination of documented `ec2:*` condition keys can construct a Deny that fires on `ThreadsPerCore=1` while allowing `ThreadsPerCore=2` (or that caps `CoreCount`). → **Oracle:** enumerate every condition key on `ModifyInstanceCpuOptions`/`RunInstances`; confirm none reference core/thread values; simulate a policy attempting the constraint and show it cannot express it. **Refute** if any key (present or newly added) binds the value.
- **Claim:** the only expressible governance is coarse — deny the whole action (`ec2:ModifyInstanceCpuOptions`) or gate by instance tag/type/tenancy — never by requested value.
**Doc evidence:** `list_ec2.md` action rows for `ModifyInstanceCpuOptions` (line ~8800) and `RunInstances` (instance resource, line ~5093); `ec2:CpuOptionsAmdSevSnp` key def (line ~10027). **Severity-if-true:** **Low / Informational** governance gap — AWS-owned, reportable as a hardening/condition-key-coverage gap (Tier-2-adjacent: it is AWS's IAM surface, not a customer footgun). No cross-tenant impact.
**Stop condition:** once the absence is confirmed by enumeration + simulation, it is settled — do not attempt live abuse.

### Area 2 — Optimize CPUs license-fee billing integrity  *(Lens U — billing-integrity, AWS-owned)*
**Background.** For license-included Windows/SQL AMIs, "Optimize CPUs" bills the third-party license fee on the **number of active vCPUs configured** (per-vCPU-hour rate table). Rules add a gate: **"you must configure a minimum of four vCPUs. If you configure fewer than four vCPUs, default billing is applied."** Not supported on T3 or Dedicated Instances. RI discounts "may not be applied" with Optimize CPUs in the same payer account (opt-out list for pre-2025-10-15 usage).
**Security Concern.** The license fee is derived from a customer-set attribute. Two integrity questions:
1. **Metering-vs-reality binding:** is the billed active-vCPU count the one the **hypervisor actually enforces** (real scheduled cores), or a separately-tracked control-plane attribute that a customer could make diverge from actual compute (pay for N vCPUs, schedule on > N)? If they can diverge → **license underpayment**.
2. **Gate timing / TOCTOU:** the "< 4 vCPU ⇒ default billing" boundary and the RI-opt-out state are evaluated per metering interval. Can rapid `ModifyInstanceCpuOptions` toggling across the 4-vCPU boundary (instance must be Stopped to modify — so toggling implies stop/start cycles) land billing intervals in a cheaper regime than the compute delivered? Does a stop/modify/start straddle a metering boundary in the customer's favor?
**High-level Test Scenarios:**
- **Claim:** guest-visible cores (`lscpu`) can exceed the vCPU count the license fee is metered on. → **Oracle:** launch a license-included AMI with reduced CpuOptions, compare `lscpu`/perf-observable cores against the Optimize-CPUs line item's vCPU basis. **Expected to hold** (hypervisor really reduces allocation) — refutes underpayment; a divergence is a **billing-plane defect → HARD STOP, disclose.**
- **Claim:** the 4-vCPU gate is evaluated on *configured* not *delivered* vCPU, allowing a below-4 config to still schedule ≥4 effective. **Oracle:** as above.
**Doc evidence:** `optimize-cpu.md` (rate table, examples 1–3, min-4 rule, RI warning); `instance-cpu-options-rules.md` (min-4, T3/Dedicated exclusions). **Severity-if-true:** license underpayment = **Medium billing-integrity, AWS-owned**; a metering-fleet divergence = HARD STOP / disclosure. **Most likely null** — hypervisor enforcement makes real divergence implausible; record the negative with the `lscpu`-vs-bill evidence.
**Stop condition:** the instant evidence touches the metering/billing fleet identity — stop and disclose.

### Area 3 — Write-path validation parity + launch-template deferred validation  *(Lens X)*
**Background.** CpuOptions is settable via three paths (`RunInstances`, `CreateLaunchTemplate`, `ModifyInstanceCpuOptions`). Docs state hard rules: **cannot exceed default vCPUs**; must specify **both** core+threads; valid values per instance-type table; not on bare-metal; SMT-disable only where supported (not T2/C7a/M7a/R7a/Graviton/Apple-silicon for thread changes).
**Security Concern.** Do all three paths enforce the same validation? Launch templates historically **defer** validation to launch time and support **`$Latest`/`$Default`** late-binding (see `[[project_launch-templates-plan]]`, `[[project_ec2-fleet-config-plan]]`) — so an invalid/over-default CpuOptions may be **accepted at template-create** and either fail at launch (benign) or, worse, a launcher who could not call `ModifyInstanceCpuOptions` directly may cause a CpuOptions they couldn't set to be applied via a template version pointer.
**High-level Test Scenarios:**
- **Claim:** `CreateLaunchTemplate` accepts a `CpuOptions` that exceeds the instance type's default vCPUs (validation deferred), where `RunInstances`/`ModifyInstanceCpuOptions` reject inline. → **Oracle:** submit an over-default `CpuOptions` on each path; compare accept/reject and *when* the error surfaces (create vs launch). Divergence = validator-parity gap.
- **Claim:** a principal with only `RunInstances` + `ec2:LaunchTemplate` (not `ModifyInstanceCpuOptions`) can launch with a CpuOptions embedded in a `$Latest` template version authored by someone else — de-facto setting CpuOptions without the modify permission. **Oracle:** the `ec2:IsLaunchTemplateResource` / `$Latest` late-binding chain from the launch-templates plan.
**Doc evidence:** `instance-cpu-options-rules.md`; `instance-specify-cpu-options.md` (launch-template JSON examples); `list_ec2.md` `ec2:IsLaunchTemplateResource`/`ec2:LaunchTemplate` keys on the instance resource. **Severity-if-true:** validator divergence = **Low**; late-binding privilege-laundering of CpuOptions = **Low–Medium** (single-account). **Stop condition:** once accept/reject behavior per path is characterized.

### Area 4 — `ec2:Attribute` scoping soundness on the dedicated ModifyInstanceCpuOptions API  *(Lens S variant — case/populate fail-open)*
**Background.** `ModifyInstanceCpuOptions` lists `ec2:Attribute` and `ec2:Attribute/${AttributeName}` among its condition keys. But it is a **dedicated** API, not `ModifyInstanceAttribute`. The confirmed `[[project_ec2-instance-resize-plan]]` finding showed `ec2:Attribute` is **case-sensitivity fail-open** (a Deny written against a lowercase enum is inert when the key is populated with the PascalCase request field).
**Security Concern.** Does `ec2:Attribute` actually get **populated** for `ModifyInstanceCpuOptions` (a dedicated verb that may not map to an "attribute name"), and if so with what casing? If unpopulated or case-mismatched, a security team's Deny keyed on `ec2:Attribute` to block CPU-option changes **fails open**.
**High-level Test Scenarios:**
- **Claim:** a Deny of `ec2:ModifyInstanceCpuOptions` conditioned on `ec2:Attribute` (any documented casing) does not actually deny the call. → **Oracle:** `iam:SimulatePrincipalPolicy` with the Deny in place, then a scoped live call with canary instance; observe allow. **Refute** if the Deny fires.
**Doc evidence:** `list_ec2.md` `ModifyInstanceCpuOptions` condition-key list; cross-ref `[[project_ec2-instance-resize-plan]]`. **Severity-if-true:** **Low–Medium** (governance fail-open, single-account). **Stop condition:** once the key's populate/casing behavior is observed.

### Area 5 — Baseline cross-account instance IDOR on ModifyInstanceCpuOptions  *(Lens A — expected null, verify)*
**Background/Concern.** `ModifyInstanceCpuOptions` takes an `instance-id`; resource type is `instance*`. Standard EC2 ownership authz should bind the id to the caller's account.
**Scenario:** **Claim:** the API validates instance **existence** but not **ownership** (accepts a foreign `i-…`). → **Oracle:** call with an instance-id owned by the second in-scope account; expect `AccessDenied`/`NotFound`. A 200/accept on a foreign instance = cross-account mutation (**High**, and near the service-plane line — escalate carefully). **Expected to hold** — EC2 instance ownership is well-enforced. **Doc evidence:** `list_ec2.md` resource `instance*`. **Severity-if-true:** High (but very unlikely). **Stop condition:** first `AccessDenied`.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Govern CpuOptions values via IAM | `ModifyInstanceCpuOptions` / `RunInstances` | "Condition keys" list in SAR — show it lacks core/thread-value keys (only `CpuOptionsAmdSevSnp`) |
| License fee < delivered compute | Optimize CPUs metering | "pay licensing fees based on the number of vCPUs configured"; hypervisor vCPU enforcement |
| Below-4-vCPU billing-regime gaming | Optimize CPUs `<4 vCPU ⇒ default billing` gate | "must configure a minimum of four vCPUs" rule |
| Over-default vCPU via a write path | `CreateLaunchTemplate` deferred validation | "You cannot exceed the default number of vCPUs for the instance" |
| CpuOptions set without modify perm | Launch-template `$Latest`/`$Default` | `ec2:IsLaunchTemplateResource` / `ec2:LaunchTemplate` late-binding (`[[project_launch-templates-plan]]`) |
| `ec2:Attribute` Deny bypass | `ModifyInstanceCpuOptions` authz | `ec2:Attribute` condition key (case-fail-open per instance-resize plan) |
| Cross-account CPU-option mutation | `ModifyInstanceCpuOptions` instance-id | `instance*` resource ownership authz |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **AMD SEV-SNP (`AmdSevSnp` CpuOptions sub-field), confidential compute, attestation, measured boot** → separate feature with its own governance (`ec2:CpuOptionsAmdSevSnp` key + Nitro/SEV-SNP HW isolation). Route to `[[project_nitrotpm-plan]]` / `[[project_enclaves-existing-plans]]` / `[[project_aws-instancetypes-existing-reports]]`. **HW isolation of cores/threads across tenants = hard stop.**
- **Hypervisor CPU scheduling / core-to-tenant isolation / hyper-thread side-channels (L1TF/MDS)** — AWS-owned hardware isolation, out of scope.
- **Billing/metering fleet internals** — probe only the *customer-observable* line item; the metering plane itself is the service plane (hard stop).
- **vCPU quota gaming** — doc explicitly states quota is computed on *default* vCPUs, unaffected by CpuOptions → closed.
- **Instance-type CPU credit (T-family burstable) behavior** — different API (`ModifyInstanceCreditSpecification`) and feature; see `[[project_burstable-unlimited-mode-plan]]` / `[[project_burstable-standard-mode-plan]]`.
- **In-guest CPU tooling** (`lscpu`, Task Manager) — customer-side, informational only (used here only as a billing-vs-reality oracle).
- **Single-tenant self-DoS / right-sizing mistakes** — customer footgun.
- **Customer-authored SCPs/policies** that fail to govern CpuOptions — the *gap that they cannot* is Area 1 (AWS-owned); a customer merely forgetting to restrict is their own footgun.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, pages named)
- **Lens A (cross-tenant IDOR):** only baseline instance-id ownership (Area 5) — no shared-fleet multi-tenant resource. Pages: all 5 UserGuide pages + SAR. Null beyond Area 5.
- **Lens B/C (PassRole / credential vending):** no role ARN, no STS, no session policy in the CpuOptions surface. Pages: `instance-specify-cpu-options`, API ref. **Null.**
- **Lens D/V (data→control plane / network segmentation):** no ENI/control-VPC/host-service surface. **Null.**
- **Lens F (translation/injection):** CoreCount/ThreadsPerCore are bounded integers validated against a per-instance-type table; no parser/wire-protocol/untrusted transform. **Null.**
- **Lens G (SSRF):** no field the service dereferences/fetches/renders. Pages checked: hub, rules, specify, view, optimize-cpu — no URL/URI/location/webhook field. **Null.**
- **Lens H/W (KMS / attestation):** `AmdSevSnp` present but out of scope (Section 7). **Null here.**
- **Lens I (tagging/ABAC):** `aws:ResourceTag`/`aws:RequestTag` govern the *instance*, not CpuOptions values — folded into Area 1 (values are ungovernable) and Area 4. No CpuOptions-specific tag surface.
- **Lens K (prompt injection), Lens J (OAuth), Lens M (shared-id), Lens P (registration/identity-proofing), Lens Q (upload), Lens N (namespace migration), Lens AA (share/revoke), Lens Y (TLS/sig):** no triggering mechanism on any CPU-options page. **Null.**
- **Lens L (DoS/exhaustion):** quota unaffected by CpuOptions (doc-explicit) → no cross-tenant or self-amplification vector. **Null.**
- **Lens O (audit):** `ModifyInstanceCpuOptions` is a standard mutating EC2 API (CloudTrail-logged); AWS Config records CpuOptions changes (view page). No evasion surface flagged. **Low/Informational.**
- **Lens R (AWS-authored IAM artifact):** **no AWS-managed policy, SLR, CFN snippet, or "required IAM permissions" JSON is printed on any CPU-options page.** The only IAM artifact is the SAR condition-key set itself — audited in Area 1. **Null (no shipped policy to audit).**
- **Doc gaps to confirm on live surface first:** (a) launch-template CpuOptions **validation timing** (create vs launch) — Area 3; (b) whether `ec2:Attribute` is **populated** for the dedicated `ModifyInstanceCpuOptions` verb and with what casing — Area 4; (c) whether Optimize-CPUs active-vCPU billing basis is hypervisor-enforced — Area 2. All three are "confirm surface first" before deep effort.

---

### Analyst note (for the next agent)
This page ranks **low-yield** overall — it is a customer-side billing/config feature with no multi-tenant or service-plane attack surface. Spend effort **only** on Area 1 (condition-key gap — cleanly confirmable from the SAR, and consistent with the confirmed CpuCredits-key gap) and a quick negative on Area 2 (license-fee integrity). Areas 3–5 are parity/hygiene checks that likely hold. If a hunter finds nothing beyond the Area 1 governance gap, that is the correct and complete result for this surface.
