# EC2 Diagnostic Interrupt (`SendDiagnosticInterrupt`) — Attack Research Plan

Source of leads:
- `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/diagnostic-interrupt.html` (mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/diagnostic-interrupt.md`) — verified identical online and offline on 2026-10-17.
- `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SendDiagnosticInterrupt.html` (mirror: `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_SendDiagnosticInterrupt.md`).
- EC2 Service Authorization Reference: mirror `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`, action `ec2:SendDiagnosticInterrupt`.

Status: **documentation-derived hypotheses only; nothing tested against a live account.** Produced with the `security-questionbuilder` skill.

---

## 0. How to use this document

- Each lead is stated as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered by impact). Look left and right for adjacent bugs in the instance-lifecycle action family.
- This is a **tiny, old, single-API surface** (one mutating action, two parameters, GA for years — not `[NEW]`). The honest headline is that the *documented* security story is simple: it is an authenticated, IAM-gated, **destructive/DoS-capable** action against an instance resource. The research value is concentrated in (a) IAM **scoping / action-family parity**, (b) the **managed-resource / operator** and **service-plane** boundary, and (c) the **confidential-compute / crash-dump memory-disclosure** hypotheses. Everything else is a null hypothesis recorded with the pages checked.
- **HARD STOP:** the moment evidence shows the interrupt reaching the Nitro controller, the host, a neighboring tenant, or any identity/credential/ARN/account belonging to AWS's own service plane — stop, preserve evidence, flag for AWS-Security disclosure. Do **not** exploit beyond proving existence. Because the primitive is inherently destructive (crash + reboot + possible data loss), any live confirmation must be done **only against an instance you own, that you have quiesced, and whose data loss is acceptable** — never a shared/managed/foreign instance.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Cross-account / cross-tenant crash:** cause `SendDiagnosticInterrupt` to crash+reboot an instance in an account or tenant the caller does not own — by naming its `InstanceId` directly, by a condition-key scoping gap, or via a sibling action with a weaker authz gate.
2. **Service-plane / managed-instance disruption:** crash an instance that AWS or another AWS service **operates on the customer's behalf** (a managed/operator-owned instance), i.e. reach past the shared-responsibility line.
3. **Memory / enclave disclosure:** turn the forced crash dump into a **confidentiality** breach — capture AMD SEV-SNP / Nitro Enclave / otherwise-encrypted memory in a dump, or chain the crash to a separate read primitive (console output/screenshot) to read memory without in-guest access.
4. **Privilege / parity gap:** obtain the crash-the-instance capability while holding **fewer / weaker** permissions than a policy author intended, via action-family parity (`RebootInstances`/`StopInstances`/`ModifyInstanceAttribute` vs `SendDiagnosticInterrupt`) or via a self-widenable tag condition.
5. **Blast radius beyond the target:** show that crashing one instance affects a **co-resident** instance (dedicated host / dedicated tenancy), the Nitro controller, or auto-recovery/health machinery across a tenant boundary.
6. **Stealth / audit evasion:** perform the disruption with no CloudTrail record or no attributable source.

---

## 2. Components, Assets, and Design

**What the feature is.** A control-plane API (`ec2:SendDiagnosticInterrupt`) that instructs the EC2/Nitro control plane to inject a hardware interrupt into a running guest instance. On Intel/AMD instances the interrupt is delivered as an **unknown non-maskable interrupt (NMI)**; the guest OS, if configured (`kernel.unknown_nmi_panic=1` + `crashkernel=` reserved memory + kdump/kexec on Linux; Startup/Recovery settings on Windows), responds with a **kernel panic / stop error**, typically crashing, writing a local crash/memory dump (`/var/crash` by default), and rebooting.

**Customer-facing interface.**
- API: `SendDiagnosticInterrupt` (EC2 query/SigV4 API, also AWS CLI `aws ec2 send-diagnostic-interrupt`, PowerShell `Send-EC2DiagnosticInterrupt`).
- Parameters: **`InstanceId`** (String, required) and **`DryRun`** (Boolean, optional). Nothing else.
- Response: `requestId` + `return` (boolean true on success). No data returned to the caller.

**Assets / resources.**
- The resource is a single **EC2 instance** (`instance*`, required) identified by its `InstanceId` (shape `i-[0-9a-f]{8,17}` — includes an embedded value, not purely sequential, but low-entropy enough that valid IDs in a target account may be learnable from other APIs/logs/tags).
- The *protected asset* is the **availability and integrity of the instance's running state and data** (crash → possible data loss) and, in the confidential-compute case, the **confidentiality of guest memory**.

**Processes / hosts behind it.**
- EC2 control plane (receives the API call, authorizes it).
- **Nitro System** controller / Nitro card — the component that actually injects the hardware interrupt into the guest. Diagnostic interrupt is supported on **all Nitro-based instance types except AWS Graviton** (so the delivery path is Nitro-card → guest vCPU). Graviton (Arm) is explicitly excluded.
- The guest OS kernel (customer-owned) is what turns the NMI into a panic/dump.

**Accounts / trust zones.**
- **Customer account** owns the target instance and the IAM identity making the call.
- **AWS service plane** owns the Nitro controller / host / hypervisor — the shared-responsibility line.
- Possible third zone: **managed / operator-owned instances** (instances run by another AWS service or an operator on the customer's behalf) — see Lens boundary below; `ec2:ManagedResourceOperator` is an allowed condition key, implying the authz model contemplates operator-managed instances.

**Identity.** SigV4 IAM. Authorization is standard EC2 resource-level policy on the `instance` resource with the condition keys listed in Section 4.

**Where untrusted data enters.** Essentially nowhere structurally — the only caller input is an `InstanceId` string and a boolean. There is no parser, no URL the service dereferences, no uploaded blob, no role ARN passed, no translation layer. (This narrowness is why most injection/SSRF/upload lenses are null here.) The *interesting* untrusted-influence question is the hardware interrupt itself as "input" to the guest and, transitively, to the Nitro layer.

```
Caller (IAM principal)
   │  SendDiagnosticInterrupt(InstanceId, DryRun?)   [SigV4]
   ▼
EC2 control plane ──(authz: ec2:SendDiagnosticInterrupt on instance ARN + condition keys)
   │  inject interrupt
   ▼
Nitro controller / Nitro card   ── [SERVICE-PLANE BOUNDARY: host, controller, neighbors]
   │  hardware NMI → guest vCPU
   ▼
Guest OS kernel (customer-owned)
   │  unknown_nmi_panic → kernel panic / stop error
   ▼
crash + local crash/memory dump (/var/crash) + reboot   → potential DATA LOSS
                                                         → (SEV-SNP/Enclave: encrypted memory?)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Customer IAM principal | Instance in **same account** | `SendDiagnosticInterrupt(InstanceId)` authorized by resource policy + condition keys | *Expected* — in scope of the grant. Breach only if it reaches an instance the policy's conditions should have excluded. |
| Customer IAM principal (account A) | Instance in **account B** | `InstanceId` names a foreign instance | **A crash/reboot of an instance in account B = cross-account breach (Critical).** EC2 instance ARNs are account-scoped, so this should fail at authz — confirm the ARN is resolved under the caller's account, not just by ID existence. |
| Customer IAM principal | **Managed / operator-owned** instance (run by another AWS service on the customer's behalf) | `InstanceId` names a managed instance; `ec2:ManagedResourceOperator` condition key exists | **Crashing an instance AWS/another service operates = reaching past the shared-responsibility line.** Confirm whether a plain customer principal can target such an instance and whether any condition gates it. |
| Guest / caller-induced interrupt | **Nitro controller / host / neighbor tenant** | Hardware NMI injected by Nitro card | **Any observable effect on the controller, host, or a co-resident instance = hard-stop service-plane breach.** Almost certainly isolated-by-design; treat as a hard-stop hypothesis, not an expectation. |
| Caller with only `SendDiagnosticInterrupt` | **Confidentiality of guest memory** (SEV-SNP / Enclave / plaintext RAM) | Forced crash dump captures memory; separate read primitive retrieves it | **Encrypted/enclave memory appearing in a readable dump, or dump contents readable without in-guest access, = confidentiality breach (High–Critical).** |
| Caller | **AWS's own service plane** (any AWS-owned identity/ARN/account) | any of the above | **HARD STOP.** Preserve evidence, flag for disclosure. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `SendDiagnosticInterrupt` | EC2 query API (SigV4) | Existing (GA, long-standing) | **Mutating** (crashes/reboots the instance; Access level **Write**) | External-facing | Injects NMI → kernel panic/stop error on the target instance | Yes (public EC2 endpoint) | Any IAM principal granted `ec2:SendDiagnosticInterrupt` on the instance | Only params: `InstanceId` (req), `DryRun` (opt). Returns only a boolean. |

**IAM facts (from `list_ec2.md`):**
- Action: `ec2:SendDiagnosticInterrupt` — "Grants permission to send a diagnostic interrupt to an Amazon EC2 instance." Access level **Write**.
- Required resource type: **`instance*`** (ARN-identified; account-scoped).
- Condition keys allowed: `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:CpuOptionsAmdSevSnp`, `ec2:EbsOptimized`, `ec2:InstanceAutoRecovery`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`, `ec2:InstanceMarketType`, `ec2:InstanceMetadataTags`, `ec2:InstanceProfile`, `ec2:InstanceType`, `ec2:ManagedResourceOperator`, `ec2:MetadataHttpEndpoint`, `ec2:MetadataHttpPutResponseHopLimit`, `ec2:MetadataHttpTokens`, `ec2:Region`, `ec2:RootDeviceType`, `ec2:Tenancy`.
- **`DryRun`** param: "If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`." → caller-IAM only, evaluated **before** resource resolution. **Not an ownership oracle** (false-positive trap for hunters).

**Undocumented-knob check:** the API model exposes no auth-weakening enum/parameter (no `authorizerType`-style knob, no force/override flag). The only params are `InstanceId` + `DryRun`. Null result for the "console-hidden knob" hunt.

---

## 5. Recommended Areas of Focus

> Ordered by impact. Areas 1–3 carry the research value; Area 4 is the parity sweep; the rest are quick confirmations.

### Area 1 — Cross-account / cross-tenant crash via direct InstanceId or scoping gap (Lens A / S)
**Background.** The only caller-controlled input that selects the victim is the `InstanceId` string. EC2 instance ARNs are account-scoped, so authz *should* resolve the instance under the caller's own account and refuse a foreign ID. But the action also supports tag-based conditions (`aws:ResourceTag`, `ec2:ResourceTag`) that a policy author may use instead of an ARN scope.
**Security Concern.** If authz validates instance **existence** but not **account ownership**, a caller could crash any instance by ID. If a policy is written `Resource:"*"` gated only on a tag whose value the caller can also set (via `ec2:CreateTags`), the caller can self-widen into instances they shouldn't disrupt.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* `SendDiagnosticInterrupt` with an `InstanceId` from another account returns success. → *Oracle:* 200/`return=true` (crash observed) vs `UnauthorizedOperation`/`InvalidInstanceID.NotFound`. Expectation: denied — a success is **Critical**.
- *Claim:* a principal whose policy is `Resource:"*"` + `Condition ec2:ResourceTag/env: prod` can crash a `prod`-tagged instance it does not own, *and* can set that tag itself via `CreateTags`. → *Oracle:* confirm both the crash and the self-tag under a scoped role. Severity: cross-tenant = High; intra-account self-widen = least-priv footgun (customer-authored → lower).
- *Claim:* distinct errors (`NotFound` vs `UnauthorizedOperation` vs validation) form an **instance-existence enumeration oracle** across the account boundary. → *Oracle:* differential responses/timing for a known-valid foreign ID vs a random ID. (Note: `DryRun` is IAM-only — do **not** use it as the ownership oracle.)
**Doc evidence:** `instance*` required resource + the tag condition keys in `list_ec2.md`. **Severity-if-true:** cross-account crash = **Critical**; enumeration oracle = Low–Medium.

### Area 2 — Managed-instance delegation boundary & service plane (Lens X / U + hard stop) — TOP LEAD
**Background.** EC2 "managed instances" are instances provisioned in the customer's account but **operated by another AWS service** (EKS Auto Mode, ECS managed instances, WorkSpaces Core, Lambda managed instances, Bedrock AgentCore runtime, EC2 Fast Launch). `amazon-ec2-managed-instances.md` makes an explicit delegation promise: *"You can't directly modify the settings of a managed instance or terminate it … However, you can add, modify, or remove tags from your managed instances."* The `ec2:ManagedResourceOperator` condition key ("Filters access by the presence of an EC2 operator provisioning a managed resource") is a **grant-side** key used to scope what the *operator service* can do (per `AWSLambdaManagedEC2ResourceOperator`), **not documented as a customer-side restriction.**
**Security Concern.** `SendDiagnosticInterrupt` is **neither a "modify settings" (`ModifyInstanceAttribute`) nor a "terminate" (`TerminateInstances`) call in the literal API sense** — it crashes the guest OS via NMI without changing any EC2-API-visible attribute or lifecycle state. The documented delegation promise is therefore **narrower in wording than the actual crash capability**: the docs never state whether the service-side protection that blocks modify/terminate on managed instances also blocks a diagnostic interrupt. If it does not, a plain customer principal could crash (and risk data loss on) compute AWS operates on their behalf — a side-door around the delegation boundary.
**High-level Test Scenarios:**
- *Claim (headline):* a customer-owned principal (not the operator service) holding `ec2:SendDiagnosticInterrupt` can successfully crash a managed instance (`Managed=true`, e.g. `Operator=eks.amazonaws.com`/`ecs`/`lambda`/`workspaces-core`/`bedrock-agentcore`), despite the "can't modify or terminate" promise. → *Oracle:* the interrupt returns `return=true` / crash observed against a managed instance that `ModifyInstanceAttribute`/`TerminateInstances` would refuse. **If the managed instance is AWS-operated, this reaches past the shared-responsibility line — HARD STOP: preserve evidence, disclose, do not repeat.**
- *Claim:* crashing one instance on a **Dedicated Host / dedicated tenancy** (`ec2:Tenancy` ∈ dedicated/host) observably affects a co-resident instance. → *Oracle:* any health/availability change on a sibling. **Hard stop if it crosses to another tenant.** (doc-gap — no page asserts isolation either way for the NMI path.)
- *Claim:* the injected NMI influences the **Nitro controller** or host, not just the guest. → *Oracle:* any controller/host-side observable. Strongly isolated-by-design per the Nitro passive-communications architecture (see 9B) — treat as a low-confidence hard-stop hypothesis.
**Doc evidence:** `amazon-ec2-managed-instances.md` delegation promise; `ec2:ManagedResourceOperator`/`ec2:Tenancy` keys; `AWSLambdaManagedEC2ResourceOperator`. **Severity-if-true:** customer→managed/AWS-operated crash = **Critical + hard stop**; co-resident blast radius = Critical. **Both are doc-gaps — confirm the managed-instance targeting behavior first.**

### Area 3 — Crash-induced memory / enclave disclosure (Lens W / Q, chained)
**Background.** The crash writes a **local crash/memory dump**. The action needs **no OS-level access** — only the IAM permission. The condition-key set includes **`ec2:CpuOptionsAmdSevSnp`** (AMD SEV-SNP confidential compute), and EC2 offers Nitro Enclaves and NitroTPM measured boot.
**Security Concern.** Two confidentiality angles: (a) a forced panic on a confidential-compute instance could capture otherwise-encrypted/enclave memory in a dump or disrupt attestation/PCR state; (b) an attacker holding only `SendDiagnosticInterrupt` plus a **separate read primitive** (`GetConsoleOutput` / `GetConsoleScreenshot` / serial console) could read post-crash state (panic trace, memory in console output) without ever logging into the box — a no-in-guest-footprint disclosure chain.
**High-level Test Scenarios:**
- *Claim:* a diagnostic interrupt on a SEV-SNP / NitroTPM / Enclave instance produces a dump containing cleartext of memory the confidential-compute guarantee is supposed to protect, **or** resets/forges attestation (PCR) state. → *Oracle:* dump/attestation inspection on an owned confidential-compute instance. Severity: **High–Critical** if the confidentiality guarantee breaks.
- *Claim (chain):* `SendDiagnosticInterrupt` + `GetConsoleOutput`/`GetConsoleScreenshot` lets a caller without SSH read panic/memory data. → *Oracle:* the console read returns kernel-memory/panic contents after a caller-induced crash. Rate at the end of the chain.
**Doc evidence:** `ec2:CpuOptionsAmdSevSnp` condition key; "crash dump data is generated locally"; Enclave/NitroTPM docs. **Severity-if-true:** confidential-memory disclosure = **Critical**; console-read chain = High. *(Likely partly doc-gap — confirm the enclave-memory-in-dump behavior against docs/hardware before asserting.)*

### Area 4 — Action-family / twin authorization parity (Lens X)
**Background.** `SendDiagnosticInterrupt` is one of several instance-targeting **Write** actions that disrupt a single instance: `RebootInstances`, `StopInstances`, `StartInstances`, `TerminateInstances`, `ModifyInstanceAttribute`, `GetConsoleOutput`, `GetConsoleScreenshot`, `CreateReplaceRootVolumeTask`.
**Security Concern.** If siblings enforce a **different** (weaker) condition-key set for the same "disrupt this instance" capability, a policy author who gated `StopInstances`/`RebootInstances` carefully may leave `SendDiagnosticInterrupt` (or vice-versa) with a looser gate — a parity gap that reaches an equivalent-or-worse outcome (crash + **data loss**, which `StopInstances` does not cause).
**Result of the documentation sweep (see 9A):** **largely a null hypothesis.** No disruptive Write sibling has a strictly weaker condition-key set — `SendDiagnosticInterrupt` (19 keys) is the same-or-slightly-narrower than `Reboot`/`Stop`/`Terminate`/`CreateReplaceRootVolumeTask` (22) and `ModifyInstanceAttribute` (25); it misses only `ec2:PlacementGroup`/`ec2:ProductCode`, which change nothing material. The classic "gate the twin, forget this one" gap does not appear in the Write family.
**Remaining nuance (Medium footgun, not a bypass):** `GetConsoleOutput`/`GetConsoleScreenshot` are **Read** actions carrying a near-identical condition-key surface to the destructive Write actions. A policy author who scopes by condition block alone (ignoring access level) can accidentally make the same principals eligible for console-peek *and* interrupt grants under one shared condition — relevant to the Area 3 crash+console-read chain. Also note `ModifyInstanceAttribute(userData)` is a strictly-more-dangerous sibling (PassRole-adjacent privesc vector) — a principal holding it already out-powers diagnostic interrupt.
**Doc evidence:** per-action condition-key lists in `list_ec2.md`. **Severity-if-true:** Read/Write condition-reuse footgun = Medium (customer-authored → lower).

### Area 5 — Availability / unconfigured-kernel DoS & stealth (Lens L / O)
**Background.** The feature page warns a diagnostic interrupt "could trigger an instance to crash and reboot, which could lead to the loss of data." Prereqs (unknown_nmi_panic, crashkernel, kdump) are what make the panic *clean*; an **unconfigured** kernel's response to an unexpected NMI is undefined.
**Security Concern.** A caller holding only `ec2:SendDiagnosticInterrupt` (no Stop/Reboot/Terminate) can force crash + reboot + **data loss** with no in-guest footprint. On an unconfigured instance the result may be a hang or unpredictable state (a worse DoS than a clean reboot). Repeated calls = sustained availability attack.
**High-level Test Scenarios:**
- *Claim:* the action is callable (and effective) against an instance whose OS is **not** configured for diagnostic interrupt, producing an undefined/hung state rather than a clean recoverable panic. → *Oracle:* behavior on an owned, unconfigured instance.
- *Claim (Lens O):* the call is **not** recorded in CloudTrail, or source attribution relies on a spoofable field. → *Oracle:* CloudTrail event lookup for `SendDiagnosticInterrupt`. Expectation: it *is* logged (standard EC2 mutating API) — a null here is the likely outcome; record it.
**Doc evidence:** the "loss of data" warning; the prereqs section. **Severity-if-true:** single-tenant self-DoS = Low/out-of-scope; forcing it on instances a caller shouldn't disrupt escalates via Areas 1–2.

### Area 6 — Auto-recovery / health-check interaction (Lens U)
**Background.** `ec2:InstanceAutoRecovery` is a condition key. Repeated forced crashes could interact with auto-recovery, status-check-based recovery, or billing.
**Security Concern.** If repeated interrupts defeat or loop auto-recovery, or trigger recovery actions, that is an availability/cost amplifier.
**Test Scenario:** *Claim:* repeated `SendDiagnosticInterrupt` interacts with auto-recovery/health checks in a way that amplifies impact. → *Oracle:* observed recovery/health behavior on an owned instance. **Severity-if-true:** Low–Medium (amplifier). *(Likely doc-gap — confirm.)*

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account crash by foreign `InstanceId` | EC2 control-plane authz | Account-scoped instance ARN resolution |
| Self-widen via caller-settable tag condition | IAM resource policy + `CreateTags` | Tag-key gating; separation of tag-write from this action |
| Crash a managed/operator-owned instance | `ec2:ManagedResourceOperator` gate | (confirm the gate exists / is applied) |
| Co-resident blast radius on dedicated host | Nitro isolation | Hardware/Nitro tenant isolation |
| Enclave/SEV-SNP memory in crash dump | Confidential compute | Memory-encryption / enclave isolation during crash |
| Memory read via crash + console-read chain | `GetConsoleOutput`/`Screenshot` authz | Console-output scoping / sanitization |
| Action-family parity gap | IAM per-action condition keys | Consistent condition-key coverage across disruptive actions |
| Interrupt influences Nitro controller/host | Nitro controller | One-directional control→guest injection (hard stop if broken) |
| Unlogged disruption | CloudTrail | Standard mutating-API logging |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Single-tenant self-DoS:** a customer crashing their *own* instance with their *own* permissions is the documented, intended behavior — out of scope.
- **Customer-authored IAM footguns:** an over-broad policy *the customer wrote* granting `SendDiagnosticInterrupt` too widely is a least-privilege footgun, not an AWS defect. (In scope **only** if the weak default ships in an AWS-managed/AWS-published policy — none is documented for this action.)
- **In-guest / OS configuration:** whether the customer's kernel is configured for kdump, where `/var/crash` points, Windows dump settings — customer-owned, out of scope.
- **Nitro/host hardware isolation as a general claim:** attacking the Nitro hypervisor itself is service-plane; stop and disclose rather than pursue.
- **IMDS on managed hosts, DNS rebinding against private endpoints, product/feature-parity gaps** — standard out-of-scope carve-outs.
- **The user steering their own instance's crash** — intended.

---

## 8. Null hypotheses / doc gaps (lenses checked, pages named)

Pages checked for triggers: the `diagnostic-interrupt` UserGuide page, `API_SendDiagnosticInterrupt`, and the `SendDiagnosticInterrupt` entry in `list_ec2.md`.

- **Lens B/C (PassRole / credential vending) — N/A.** The action accepts no role ARN, token, or credential input; it does not assume a role or vend credentials. No `roleArn`/`PassRole`/`credentialProvider` field exists.
- **Lens F (injection / translation / parser) — N/A.** No customer input is parsed or translated; the only inputs are an `InstanceId` string and a boolean. No wire-protocol/BSON/SQL/metamodel layer.
- **Lens G (SSRF) — N/A.** No field the service dereferences, fetches, previews, or renders. Checked the API params and the feature page — there is no URL/URI/endpoint input.
- **Lens H (KMS / encryption-context) — N/A at the API** (no KMS key input). The SEV-SNP/enclave memory-encryption angle is tracked under Area 3 (Lens W), not key-policy confusion.
- **Lens J (OAuth/3P), Lens K (prompt injection), Lens P (registration/proofing), Lens Q upload-side, Lens FF (JWT) — N/A.** No 3P linking, no LLM/agent, no registration/OTP workflow, no file/blob upload, no JWT/OIDC token validation in this surface. (Lens Q's *render* side is repurposed only as the crash-dump disclosure angle in Area 3.)
- **Lens BB/CC/DD (canonicalization / upstream-context / cache) — N/A.** Single control-plane API with one identifier param; no multi-parser request path, no asserted-upstream identity header, no caching layer documented.
- **Lens Y (transport/signature) — doc-gap, low.** Standard SigV4 EC2 endpoint; no action-specific transport claim. No reason to suspect a weaker path, but not separately asserted.
- **Lens O (audit) — likely null.** `SendDiagnosticInterrupt` is a standard mutating EC2 API and is expected in CloudTrail; confirm (Area 5) but treat as informational.

**Doc gaps to confirm before asserting a finding:**
- Whether `ec2:ManagedResourceOperator` is *enforced by default* or only available for customers to add to their own policies (Area 2).
- Enclave/SEV-SNP memory behavior during a forced crash dump — not documented on the feature page (Area 3).
- Auto-recovery interaction (Area 6).

---

## 9. Deeper analysis appendix (documentation-only sub-analyses)

Two focused sub-analyses were run against the mirror. Both touched no live account. Key files cited: `list_ec2.md`, `API_SendDiagnosticInterrupt.md`, `diagnostic-interrupt.md`, `amazon-ec2-managed-instances.md`, `AWSLambdaManagedEC2ResourceOperator.md`, `iam-policies-for-amazon-ec2.md`, `dedicated-hosts-understanding.md`, the Nitro System whitepaper pages (`passive-communications-design.md`, `the-components-of-the-nitro-system.md`), `sev-snp.md`, `enclaves/latest/user/security.md`, `nitro-enclave-concepts.md`, `nitrotpm.md`, `ec2-instance-recover.md`, `API_GetConsoleOutput.md`, `API_GetConsoleScreenshot.md`, `troubleshoot-unreachable-instance.md`, `monitor-with-cloudtrail.md`.

### 9A — IAM scoping & action-family parity

**Action-family parity (feeds Area 4).** Condition-key counts on the `instance` resource: `SendDiagnosticInterrupt` = 19 keys; `RebootInstances`/`StopInstances`/`TerminateInstances`/`CreateReplaceRootVolumeTask` = 22; `ModifyInstanceAttribute` = 25 (adds `ec2:Attribute`, `ec2:Attribute/${AttributeName}`); `GetConsoleOutput` = 22 (**Read**); `GetConsoleScreenshot` = 23 (**Read**, anomalously lists `ec2:NewInstanceProfile` — looks like template copy/paste). `SendDiagnosticInterrupt` is missing only `ec2:PlacementGroup`/`ec2:ProductCode` vs the Write siblings — none of which meaningfully weakens it.
- **Conclusion:** there is **no disruptive Write sibling with a strictly weaker key set** — the family is consistent, so the classic "gate one, forget the twin" parity gap is **largely a null hypothesis** here. The real nuance is **cross-access-level condition reuse**: `GetConsoleOutput`/`GetConsoleScreenshot` are **Read** yet carry a near-identical condition-key surface to the destructive actions, so a policy author who scopes by condition block alone (ignoring access level) can accidentally make the same principals eligible for both console-peek and interrupt grants. Severity: Medium policy-authoring footgun, not a technical bypass.

**Condition-key semantics (feeds Area 1).**
- `instance*` is required → ownership is bound by the **ARN** (`arn:aws:ec2:region:account:instance/i-…`), which encodes account+region+instance. `ec2:InstanceID` ("Filters access by the ID of an instance") is therefore **largely a redundant restatement of the ARN** for this single-resource action — it adds scoping power only for `StringLike` wildcard/negation across many IDs, not for ownership binding.
- **Tag self-widening is plausible as documented:** `CreateTags`/`DeleteTags` on `instance` are gated only by the tag-condition keys (`aws:RequestTag`, `aws:ResourceTag`, `aws:TagKeys`, `ec2:Region`, `ec2:ResourceTag`) — a **much narrower** set than the 19 keys on `SendDiagnosticInterrupt` (no `InstanceID`/`ManagedResourceOperator`/`Tenancy`). So if `SendDiagnosticInterrupt` is scoped via `ec2:ResourceTag/Team=Alpha` and the same principal also holds `ec2:CreateTags`, it can tag an arbitrary instance `Team=Alpha` and then satisfy the interrupt condition. Nothing in the docs technically prevents this. Severity: High if confirmed live (low-priv → crash-capability escalation over out-of-scope instances).
- **Value case-sensitivity fail-open:** IAM key *names* are case-insensitive, but enum *values* (`ec2:Tenancy` ∈ {default,dedicated,host}; `ec2:ManagedResourceOperator` = a service-principal string) are matched case-sensitively by `StringEquals`. A policy author with mismatched casing could silently fail to match → a Deny that is inert. **doc-gap — confirm canonical stored value casing.**

**DryRun (feeds Area 4/0).** Confirmed verbatim: DryRun checks caller IAM permissions only and returns `DryRunOperation`/`UnauthorizedOperation` **before** resource resolution. It does **not** prove the target exists, is owned, is non-managed, or that the real call would succeed. Exclude DryRun results from any "confirmed capability" claim.

### 9B — Hardware / confidential-compute / crash-dump boundary

**Hypervisor / control-plane delivery path (Area 2 / Lens D-V) — likely isolated-by-design, LOW confidence for a finding.** The Nitro whitepaper repeatedly asserts a strictly passive design: *"The Nitro Controller … never initiates any outbound communications on the EC2 control plane network"*; the hypervisor *"never initiates outbound communication … has no networking stack"*; any hypervisor outreach *"would be a clear signal of a firmware flaw or possible system compromise … denied and alarmed."* The interrupt path is control-plane → Nitro Controller → guest NMI, one-directional by construction. Doc-gap: no page addresses the diagnostic-interrupt mechanism *specifically* for abuse back toward the Controller — the isolation is inferred from general architecture, not asserted feature-by-feature. Treat as the hard-stop hypothesis, not an expectation.

**Confidential compute (Area 3 / Lens W) — the genuine standout doc-gap.** AWS documents diagnostic-interrupt, SEV-SNP, NitroTPM, and Nitro Enclaves as **four feature pages that never cross-reference each other's crash/panic behavior.** Specifics:
- SEV-SNP encrypts memory *from the host/hypervisor view*; the guest kernel sees its own memory in cleartext, so a kdump taken by the guest contains the same plaintext an OS-level user already sees — but **the docs never state this for the crash-dump case** (notable given `ec2:CpuOptionsAmdSevSnp` is a listed condition key). doc-gap.
- **SEV-SNP excludes Nitro Enclaves and Hibernation** (`sev-snp.md` Considerations) — so the "double confidential-compute" scenario cannot co-occur; analyze SEV-SNP-alone and Enclave-alone separately.
- Enclave memory is isolated *"from the processes, applications, or users (root or admin) of the parent instance"* — but this is scoped to *parent-instance access*, **not** to a parent kernel-panic/NMI event. The enclave has no independent instance ID (`i-…-enc…`); the API only documents parent `i-…` IDs. doc-gap: unclear whether the API can target an enclave or what happens to enclave vCPU/memory on parent panic.
- NitroTPM/PCR: no page states what happens to PCR values or PCR-sealed secrets across a forced-panic reboot. doc-gap. Repeated-crash-to-defeat-measured-boot is the least-covered angle.
- **This is the top escalation candidate for an authorized live-test plan** precisely because of the silence — but AWS's general isolation claims suggest design intent is isolation; mark leads "doc-gap — confirm surface first."

**Crash-dump / console-read chain (Area 3 / Lens Q) — real but likely benign.** The dump stays local (`/var/crash`); **no documented path exfiltrates the dump file**. The viable chain is `SendDiagnosticInterrupt` → kernel prints panic banner/backtrace to console → caller with a *separately-granted* `ec2:GetConsoleOutput`/`ec2:GetConsoleScreenshot` reads it (Linux console = "exact console output … on a physical monitor"; Windows console = "last three system event log errors" + a screenshot that could capture a BSOD banner). This reads **console-visible crash metadata** (kernel version, panic message, module list), which is the documented *purpose* of those APIs → Medium/working-as-intended, **unless** console output under crash conditions is shown to leak raw memory bytes/secrets → then High. Note the chain requires two distinct IAM actions, and "Only the instance owner can access the console output."

**Availability DoS (Area 5 / Lens L) — confirmed as intended behavior.** AWS's own warning ("could … crash and reboot, which could lead to the loss of data") plus the distinct `ec2:SendDiagnosticInterrupt` Write action confirm a single-permission, no-in-guest-footprint, data-loss-capable DoS primitive. CloudTrail logs all EC2 API actions as management events (exact event shape not shown in docs). Unconfigured-kernel behavior on an unexpected NMI is undocumented (guest-OS territory). Severity: Medium-High as a least-privilege/blast-radius-awareness item for policy authors, not a service bug.

**Auto-recovery (Area 6) — premise corrected, deprioritize.** `ec2:InstanceAutoRecovery` is generic IAM resource-matching scaffolding ("Filters access by whether the instance type supports auto recovery"), attached to most instance actions — **not** a functional coupling. EC2 automatic recovery triggers on **system status-check / host hardware** failures, *not* a guest kernel panic, so a diagnostic-interrupt-induced crash should **not** fire auto-recovery; the guest's own kdump/reboot handles it. No documented billing linkage. Severity: Low.
