# EC2 Instance Type Changes (Resize) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html` (+ `.md`) and its child pages: `resize-limitations.html`, `change-instance-type-of-ebs-backed-instance.html`, `migrate-instance-configuration.html`, `ec2-instance-recommendations.html`, `troubleshoot-change-instance-type.html`, `migrating-latest-types.html`, `instance-cpu-options-rules.html`. Offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`. Cross-checked against live docs 2026-09-08.
Status: **documentation-derived hypotheses only; nothing tested against a live account.** Method: `security-questionbuilder`.

> **Scope reality.** This is a **thin, customer-facing operational doc set** describing a single control-plane operation (change an instance's type) plus its console workflow and an alternative "launch a new instance and migrate" procedure. There is **no new multi-tenant service, no new ARN, no new network fabric** here. The security-relevant substance is almost entirely: (1) the **authorization semantics of the underlying `ModifyInstanceAttribute` API** (a heavily multiplexed action), (2) **AWS-authored SSM migration runbooks** the docs tell customers to run, and (3) **billing / license-integrity levers** exposed by resize + CPU-options. Most raw "resize" concerns (instance-store wipe, public-IPv4 release, ASG churn) are documented, customer-owned, single-account behaviors — enumerated below and mostly routed **out of scope** so the hunter stays off shared/managed infra.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Prove every authorization claim under a **scoped IAM role holding exactly the permission in question**, never an over-privileged tester. Use `iam:SimulatePrincipalPolicy` / `SimulateCustomPolicy` as the first, zero-touch oracle before any live call. Use only synthetic/canary instances you own.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (a Nitro host, an SSM automation-service principal acting outside your account, a cross-account resource you did not create), stop, preserve evidence, and flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Attribute-confusion privilege escalation:** show whether an IAM grant intended only to let a principal *resize* an instance (`ec2:ModifyInstanceAttribute`) also grants **`userData` rewrite** (→ boot-time code execution as the instance profile role) or **`disableApiTermination` / IMDS** changes when the operator omits the `ec2:Attribute` condition key — and whether that key is case-sensitive fail-open (the action *is* attribute-scopable, but only if the condition is written and honored).
2. **Resize authorization scoping gap:** show whether `ec2:ModifyInstanceAttribute` for the instance-type change can (or cannot) be constrained by *which target instance type*, by *resource tag*, or by *ownership*, and whether any published AWS-managed policy grants it over-broadly.
3. **AWS-authored runbook over-privilege / code-exec:** audit `AWSSupport-MigrateXenToNitroLinux` and `AWSSupport-UpgradeWindowsAWSDrivers` (and any Windows-Nitro variant) — do they require a broad `AutomationAssumeRole`, run in-guest commands via SSM RunCommand (code exec on the instance), or create AMIs/snapshots that persist or leak?
4. **Billing / license integrity:** show whether resize + CPU-options manipulation lets a caller shift or evade compute/license billing (the documented "fewer than four vCPUs → default billing is applied" lever) in a way not intended.
5. **Data-lifecycle / continuity on the forced stop:** confirm instance-store erase and public-IPv4 release are correctly bounded (no cross-tenant remanence, no attacker-influenced reallocation on the resize path).

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane API + console. The console "Change instance type" action (`Actions → Instance settings → Change instance type`, enabled **only when instance state = `stopped`**) maps to the **`ModifyInstanceAttribute`** API with the `instanceType` attribute (and optionally `ebsOptimized`, and CPU/vCPU options via the Advanced-details panel). There is **no `ResizeInstance` API** — resize is an *attribute modification* on a stopped instance. The "migrate" alternative is not an API at all: it is a runbook of `RunInstances` + EBS snapshot/attach + EIP reassociation.

**Processes / hosts.** No new fleet. The operation is:
- EC2 control plane validates compatibility (virtualization type, processor architecture, network-adapter/ENA/ENA-Express support, NVMe support, EBS volume-count limit, NitroTPM support — see `resize-limitations.md`) and re-places the (stopped) instance onto **new underlying hardware** on start.
- Optionally, **AWS Systems Manager Automation** runs an AWS-owned runbook (`AWSSupport-MigrateXenToNitroLinux`, `AWSSupport-UpgradeWindowsAWSDrivers`) that drives driver installs / config changes **inside the guest** and/or control-plane calls, under an assume-role.
- Optionally, **AWS Compute Optimizer** (separate service, per-account opt-in) reads the instance's CloudWatch utilization metrics and returns type recommendations.

**Accounts / tenancy.** Single customer account throughout. The only cross-boundary elements are (a) the **managed Nitro/Xen host** the instance lands on (AWS service plane — out of scope unless something crosses it), (b) the **SSM Automation service** running an AWS-authored document, and (c) **Compute Optimizer's** service-side metric analysis.

**"Resource" + identifier shape.** The instance (`i-…` id) is the target resource; the target *instance type* (`m5.large`) is a caller-supplied string. No new opaque IDs.

**Identity.** Standard SigV4 IAM. Relevant actions: `ec2:ModifyInstanceAttribute`, `ec2:StopInstances`, `ec2:StartInstances`, `ec2:DescribeInstances`; for migrate: `ec2:RunInstances`, `ec2:CreateSnapshot`, `ec2:AttachVolume`, `ec2:AssociateAddress`, `ec2:TerminateInstances`; for the automated path: `ssm:StartAutomationExecution` + the runbook's `AutomationAssumeRole`.

**Untrusted-input transforms.** Essentially none on the resize path (the inputs are enum-like: an instance-type string, boolean flags, integer CPU core/thread counts). The richest transform is **in-guest command execution inside the SSM runbook** (Area 3) and the **`userData` blob** reachable through the same multiplexed API (Area 1).

```
                         ec2:ModifyInstanceAttribute (instance STOPPED)
 caller (IAM) ──────────►  ┌──────────────────────────────────────────┐
   │                       │ attribute = instanceType | ebsOptimized   │  ── multiplexed: SAME action also sets
   │                       │            | userData | disableApiTerm |  │     userData, disableApiTermination,
   │                       │            | cpuOptions(at resize) | ...  │     sourceDestCheck, kernel, ...
   │                       └──────────────────────────────────────────┘
   │                                        │
   │  ssm:StartAutomationExecution          ▼ start → re-placed on NEW managed host (Nitro/Xen)
   ├───────────────────────────►  AWSSupport-MigrateXenToNitroLinux / -UpgradeWindowsAWSDrivers
   │                               (AutomationAssumeRole + in-guest RunCommand)  [Lens R/S/K]
   │
   └── Compute Optimizer (opt-in) ── reads CloudWatch metrics → type recommendation  [info]
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv caller (grant = "resize only") | The instance's `userData` / termination protection | `ec2:ModifyInstanceAttribute` is one action gating **all** attributes; scopable only via `ec2:Attribute` if the operator writes it | A principal whose policy grants the action **without** an `ec2:Attribute` condition successfully sets `userData` (→ boot-time code exec as the instance-profile role) or clears `disableApiTermination` = boundary breach (privilege beyond intent). Also test `ec2:Attribute` case-sensitivity fail-open. |
| Caller with `ssm:StartAutomationExecution` | In-guest OS + control-plane calls | AWS-authored runbook runs under `AutomationAssumeRole` and via SSM RunCommand | Runbook executes with privileges (or reaches guests) exceeding the caller's own = confused-deputy / privesc breach |
| Resized instance (stopped→started) | New managed host / prior tenant's instance-store bytes | Re-placement onto new hardware; NVMe instance-store volumes auto-exposed | Any instance-store block readable on the new host containing **another tenant's** residual data = **hard-stop service-plane breach** |
| Instance losing its public IPv4 on stop | The next account to receive that IPv4 | Address released on stop, re-pooled | Attacker-influenced/targeted reallocation of a specific released IPv4 = cross-account takeover (routed to instance-addressing plan; not resize-specific) |
| Caller with only `ec2:ModifyInstanceAttribute`/`StopInstances` on an ASG member | The Auto Scaling group's capacity | Stop marks instance unhealthy → ASG terminates + replaces | Induced ASG termination/replacement of instances the caller cannot directly terminate = indirect capacity manipulation |
| Any customer surface | AWS's own service plane (Nitro host, SSM service principal) | — | **Hard stop.** Any AWS-owned identity/credential/ARN observed → preserve evidence, disclose. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ModifyInstanceAttribute` | POST (Query) | Existing | **Yes** | External | Change `instanceType`, `ebsOptimized`, `userData`, `disableApiTermination`, `sourceDestCheck`, IMDS options, etc. Requires instance **stopped** for `instanceType`. | Yes | IAM principals with the action | **Multiplexed** — but IS attribute-scopable via `ec2:Attribute` / `ec2:Attribute/${AttributeName}` condition keys (see Area 1). Prime Lens S/E/X target. |
| `ModifyInstanceCpuOptions` | POST | Existing | **Yes** | External | Change CPU cores × threads/core (vCPU count) — the "CPU options" applied during a console resize. Requires instance **`Stopped`**. | Yes | IAM principals | **Separate action** from `ModifyInstanceAttribute`. Own condition keys (`ec2:CpuOptionsAmdSevSnp`). Billing/license lever (Area 3). |
| `StopInstances` / `StartInstances` | POST | Existing | Yes | External | Required stop/start bracketing the resize; start re-places on new hardware. | Yes | IAM principals | Start releases/reassigns public IPv4; ASG marks stopped member unhealthy. |
| `DescribeInstances` / `DescribeInstanceTypes` | POST | Existing | No | External | Read current config / supported-type capabilities. | Yes | IAM principals | Capability table (NitroTPM, ENA Express, NVMe) — Lens U doc-vs-API cross-check surface. |
| `RunInstances` (+ `CreateSnapshot`, `AttachVolume`, `AssociateAddress`, `TerminateInstances`) | POST | Existing | Yes | External | The "migrate to a new instance" alternative path. | Yes | IAM principals | Standard launch surface; routed to launch-instances / EBS plans. |
| `ssm:StartAutomationExecution` (`AWSSupport-MigrateXenToNitroLinux`, `AWSSupport-UpgradeWindowsAWSDrivers`) | POST | Existing | Yes | External | AWS-authored driver-migration automation; runs in-guest + control-plane steps under an assume-role. | Yes | Caller + `AutomationAssumeRole` | **AWS-authored artifact — Lens R/S/K. Audit its IAM + in-guest exec.** |
| Compute Optimizer `GetEC2InstanceRecommendations` | POST | Existing | No | External | Returns type recommendations from utilization metrics (per-account, opt-in). | Yes | Opt-in account principals | Cross-service; low signal. |

**Undocumented/CLI-only knob:** the docs note (`troubleshoot-change-instance-type.md`) that the **console only offers AMI-compatible types**, but **`the AWS CLI lets you specify an incompatible AMI + instance type`** — i.e. the console validation is *client-side only*; the API accepts combinations the console hides. Any safety the console appears to enforce on type selection is **not** an API-side guarantee (Lens U).

---

## 5. Recommended Areas of Focus

### Area 1 — `ModifyInstanceAttribute` attribute-multiplexing & the `ec2:Attribute` scoping key: does a "resize" grant leak into `userData`/termination control?  *(Lens S / E / X — PRIMARY)*
**Background.** The console "Change instance type" workflow is driven by a single multiplexed API, `ec2:ModifyInstanceAttribute` (Attribute = `instanceType`, `ebsOptimized`), which *the same action* can also set to `userData`, `disableApiTermination`, `instanceInitiatedShutdownBehavior`, `sourceDestCheck`, IMDS options, etc. The corpus already confirms `ModifyInstanceAttribute(userData)` as **the** non-`PassRole` action that reaches a role's live credentials (boot-time code exec as the instance-profile role). **Correction from the naive assumption:** the *Service Authorization Reference* (`list_ec2.md`) shows this action **does** expose per-attribute condition keys — **`ec2:Attribute`** and **`ec2:Attribute/${AttributeName}`** — plus `ec2:InstanceType`, `ec2:MetadataHttpTokens`, `ec2:InstanceProfile`, `ec2:EbsOptimized`, `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, and ~20 more. So the action *is* scopable to `instanceType` only — **if the operator actually writes the `ec2:Attribute` condition.**
**Security Concern.** The footgun is therefore **conditional and enforcement-shaped**, and the real Lens-S questions are: (1) do AWS-managed/AWS-published policies that grant `ModifyInstanceAttribute` (e.g. inside migration runbooks, Area 2) scope it with `ec2:Attribute`, or grant it unconstrained → resize permission silently includes `userData` privesc? (2) is `ec2:Attribute` **case-sensitive fail-open** — a confirmed corpus Lens-S failure shape — so a `Deny` written for lowercase `userData` is inert against a request field in a different casing? (3) does `ec2:InstanceType` on this action evaluate the instance's **current** type or the **new** `InstanceType.Value` being set (doc-gap — no worked example exists for the `ModifyInstanceAttribute` side; only for `RunInstances`), which determines whether it can bound the *destination* of a resize.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A policy that grants `ModifyInstanceAttribute` for resize but omits an `ec2:Attribute` condition also authorizes `userData` rewrite on the same instance → privesc. → **Oracle:** `SimulateCustomPolicy` the resize grant against a `userData`-setting request; Allow = the leak is real. Then confirm the fix (`ec2:Attribute StringEquals instanceType`) actually blocks the `userData` request.
- **Claim (case-sensitivity fail-open):** a `Deny` keyed on `ec2:Attribute` with one casing is bypassed by the other casing. → **Oracle:** `SimulateCustomPolicy` Deny(`ec2:Attribute == userData`) vs a request populating the key with `UserData`/`USERDATA`; an Allow-through = inert Deny.
- **Claim (target-type scoping semantics):** `ec2:InstanceType` cannot bound which type a resize moves *to* because it evaluates current-not-new. → **Oracle:** `SimulatePrincipalPolicy ModifyInstanceAttribute` with `ec2:InstanceType` allow-list = {t3.micro} against a request setting `InstanceType=p4d.24xlarge`; if allowed, the key does not gate the destination (cost-amplification / GPU-escape lead).
**Doc evidence:** `list_ec2.md` (`ModifyInstanceAttribute` condition-key list incl. `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:InstanceType`); `ExamplePolicies_EC2.md` (only `RunInstances` example for `ec2:InstanceType`); `API_ModifyInstanceAttribute.md`. **Severity-if-true:** High (privesc) where an AWS-published policy grants it unscoped; case-fail-open on the access-control key = Medium–High; customer-authored unscoped grant = Low footgun.

### Area 2 — AWS-authored SSM migration runbooks: `Resource:"*"` sample policy, optional assume-role, in-guest code execution  *(Lens R / S / K)*
**Background.** `change-instance-type-of-ebs-backed-instance.md` tells Linux customers to run the **`AWSSupport-MigrateXenToNitroLinux`** runbook; `migrating-latest-types.md` offers **`AWSSupport-UpgradeWindowsAWSDrivers`** (there is **no** `AWSSupport-MigrateXenToNitroWindows` — the Windows path is the manual `migrating-latest-types.md` procedure). These are **AWS-authored automation documents** the customer invokes verbatim. Confirmed facts from the SSM runbook reference:
- **`AutomationAssumeRole` is *optional*** — "If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook." So absent a scoped role, the runbook executes with the **caller's own ambient permissions**, not a bounded service role.
- **Broad required permission set** (Clone&Migrate workflow): `ec2:ModifyInstanceAttribute`, `ec2:CreateImage`, `ec2:RunInstances`, `ec2:DeregisterImage`, `ec2:DeleteSnapshot`, `ec2:Terminate/Start/StopInstances`, **`iam:PassRole`**, `iam:ListRoles`, `kms:CreateGrant*`, `kms:ReEncrypt`, and multiple `ssm:*` including **`ssm:SendCommand`** (in-guest execution). FullMigration adds `ec2:Detach/AttachVolume`, `ec2:CreateTags`, `cloudformation:DescribeStackResources`.
- **The companion child runbook `AWSSupport-CloneXenEC2InstanceAndMigrateToNitro` ships a *sample IAM policy using `"Resource": "*"`.`** This is an **AWS-published sample policy** the customer is steered to copy → **Lens R/S Tier-2 finding candidate**: a printed AWS-authored least-privilege artifact that is actually unconstrained.
- **In-guest mutation via SSM RunCommand:** steps `checkAndInstallENADrivers`, `checkAndAddNVMEDrivers`, `checkAndModifyFSTABEntries` edit `/etc/fstab`, `/etc/default/grub` (or `menu.lst`), and delete `/etc/udev/rules.d/70-persistent-net.rules` inside the guest; steps `createTestImage`/`createBackupImage`/`createImageAfterDriversInstallation` create AMIs; `setNitroInstanceTypeForClonedInstance` calls `ModifyInstanceAttribute`.
**Security Concern.** Tier-2 in-scope (AWS-authored artifact — weak default is AWS's defect). (a) The `"Resource":"*"` sample policy printed for `CloneXenEC2InstanceAndMigrateToNitro` grants `iam:PassRole`, `ec2:RunInstances`, `kms:CreateGrant` unconstrained → a customer copying it verbatim self-grants a privesc-capable policy. (b) With the assume-role optional and defaulting to caller permissions, a confused-deputy framing is weak (it *is* the caller), but the **`iam:PassRole` requirement** + `RunInstances` means the runbook is a PassRole-privesc vehicle if the caller can pass a more-privileged role. (c) In-guest `/etc/fstab`/`grub`/`udev` edits + AMI creation are code-exec-equivalent on the instance and persist into published AMIs.
**High-level Test Scenarios:**
- **Claim:** the `AWSSupport-CloneXenEC2InstanceAndMigrateToNitro` **published sample IAM policy** grants materially more than its steps require (`"Resource":"*"` on `iam:PassRole`/`ec2:RunInstances`/`kms:CreateGrant`), so a customer attaching it verbatim gains self-escalation. → **Oracle:** read the printed policy JSON on the runbook page; `SimulateCustomPolicy` it against a privesc request (`PassRole` of an admin role into `RunInstances`); Allow = Tier-2 AWS-published-artifact defect. → **Severity: High.**
- **Claim:** running the runbook with no `AutomationAssumeRole` + a caller holding `iam:PassRole` on a broad role escalates via the runbook's `RunInstances`/instance-profile step. → **Oracle:** map which step consumes `iam:PassRole` and whether the passed role is caller-chosen.
- **Claim (Lens K supply-chain):** the ENA/NVMe driver-install `ssm:SendCommand` steps fetch driver artifacts from a source that is customer-influenceable or unauthenticated → guest supply-chain. → **Oracle:** identify the fetch URL/source in the runbook step definitions (doc-gap until the document content/`aws:runCommand` inputs are read).
**Doc evidence:** `systems-manager-automation-runbooks/.../automation-awssupport-migrate-xen-to-nitro.md`, `automation-awssupport-clonexenec2instanceandmigratetonitro.md` (sample policy `"Resource":"*"`; `AllowInstanceStoreInstances` warning), `automation-awssupport-checkxentonitromigrationrequirements.md`; `change-instance-type-of-ebs-backed-instance.md`; `migrating-latest-types.md`. **Severity-if-true:** `"Resource":"*"` sample policy → non-admin-to-admin privesc = **High** (Tier-2, route `aws-security`); in-guest supply-chain = High.

### Area 3 — Billing / license integrity via resize + CPU-options  *(Lens U — billing-integrity)*
**Background.** Resize changes the billed rate ("When you change the instance type, you'll start paying the rate of the new instance type"). During a resize the console also lets you set **CPU options** (cores × threads/core) — implemented by the **separate `ModifyInstanceCpuOptions` API** (also requires the instance `Stopped`), *not* `ModifyInstanceAttribute`. `instance-cpu-options-rules.md` states: *"To save on licensing costs for instances launched from Windows and SQL Server license-included AMIs, you must configure a minimum of four vCPUs. **If you configure fewer than four vCPUs, default billing is applied.**"* and *"You cannot exceed the default number of vCPUs for the instance."*
**Security Concern.** Two documented levers deserve a "does enforcement match the promise" check: (1) whether reducing vCPUs at resize on a license-included Windows/SQL AMI actually re-prices as documented ("default billing applied") or lets a workload run with more compute than it pays license for; (2) whether the "cannot exceed default vCPUs" bound is API-enforced by `ModifyInstanceCpuOptions` or console-only (the CLI-accepts-what-console-hides pattern from `troubleshoot-change-instance-type.md`). Note `ModifyInstanceCpuOptions` is a *distinct IAM action* from resize, so a policy granting one does not imply the other — but both are needed for the full console resize experience.
**High-level Test Scenarios:**
- **Claim:** the "< 4 vCPUs ⇒ default billing" and "cannot exceed default vCPUs" rules are enforced control-plane-side by `ModifyInstanceCpuOptions`, not merely in console UI. → **Oracle:** attempt the disallowed CPU-options combination via the `modify-instance-cpu-options`/`run-instances` API directly; a 200 where the console blocks = Lens U enforcement gap.
- **Claim:** changing instance type is not gated by any billing/purchasing control, so a principal with `ModifyInstanceAttribute(instanceType)` can move a workload to an arbitrarily expensive type (cost-amplification) with no separate authorization — and `ec2:InstanceType` may not bound the *destination* (Area 1). → **Oracle:** SimulatePrincipalPolicy; note absence of a purchasing/cost condition on the action.
**Doc evidence:** `ec2-instance-resize.md`, `instance-cpu-options-rules.md`, `API_ModifyInstanceCpuOptions.md`. **Severity-if-true:** Low–Medium (billing-integrity is AWS-owned but largely intra-account/self-inflicted; not cross-tenant). Mostly a documented-guarantee-vs-enforcement check.

### Area 4 — Console-only compatibility validation vs API acceptance  *(Lens U)*
**Background.** `troubleshoot-change-instance-type.md`: the console offers only AMI-compatible types, **but the CLI/API accepts an incompatible AMI + instance type** (the instance then fails to boot). `resize-limitations.md` lists many compatibility rules (virtualization, architecture, ENA/ENA-Express, NVMe, **volume-count limit**, **NitroTPM**).
**Security Concern.** Any "the instance types shown are the compatible ones" safety is a **UI convenience, not an API guarantee** — a script/automation trusting that a resize will fail-closed on incompatibility is wrong. More interesting: is each *documented* constraint (volume-limit, NitroTPM-preserved-only-to-supporting-type, ENA-Express-must-match) actually enforced by the API, or can the API be driven into an inconsistent state (e.g. resize to a type that silently drops NitroTPM, weakening an attestation the customer relied on)?
**High-level Test Scenarios:**
- **Claim:** resizing an ENA-Express-enabled or NitroTPM-enabled instance to a non-supporting type is rejected by the API (fails closed), not silently downgraded. → **Oracle:** `ModifyInstanceAttribute` against a non-supporting target; expect an explicit error, else a Lens U/W security-property-erosion gap (attestation/feature silently lost).
- **Claim:** the "volume count must be ≤ new type's limit or the request fails" rule is enforced server-side. → **Oracle:** attempt a down-resize below the attached-volume count; confirm clean failure (docs say it fails).
**Doc evidence:** `resize-limitations.md`, `troubleshoot-change-instance-type.md`. **Severity-if-true:** Informational–Low (a silent NitroTPM loss on resize could undermine a compliance control → Low, worth filing).

### Area 5 — Data lifecycle & continuity on the forced stop  *(Lens L / data-remanence — mostly out of scope, verify boundary)*
**Background.** Resize forces `stop`. Docs state (`instance-store-lifetime.md`, "Data persistence"): *"When the instance is stopped, hibernated, or terminated, **every block of the instance store volume is cryptographically erased.**"* — and its persistence table rows "The instance type is changed → The data does not persist" with the note that a new type gets fresh instance-store volumes with no data transfer. On new hardware, **all NVMe instance-store volumes are exposed even if not in the AMI/BDM** (`change-instance-type-of-ebs-backed-instance.md`); the instance is **moved to a new host** on stop/start (`ec2-instance-lifecycle.md`); and the **public IPv4 is released** and reassigned (`troubleshoot-change-instance-type.md`).
**Security Concern (boundary confirmation only).** The only *service-plane* question is whether an instance-store volume newly exposed on the new host could ever surface **another tenant's residual bytes**. AWS documents *cryptographic erasure of every block* on stop → the expected result is a **clean null** (boundary holds). The deliverable here is to *confirm* that and stop immediately if it does not.
**High-level Test Scenarios:**
- **Claim (hard-stop test):** an NVMe instance-store volume auto-exposed after a resize contains only zeros, never prior-tenant data. → **Oracle:** read the raw block device after resize; any non-zero foreign data = **hard-stop service-plane breach, disclose.**
- **Claim (adjacency, not resize-specific):** the released public IPv4 can be targeted/reallocated to an attacker account. → **Oracle:** routed to the **instance-addressing / EIP** plan (`[[project_instance-addressing-plan]]`); out of scope here.
**Doc evidence:** as above. **Severity-if-true:** cross-tenant instance-store remanence = Critical + hard stop (expected N/A); otherwise out of scope.

### Area 6 — Auto Scaling / stop-triggered capacity churn  *(Lens L — Low)*
**Background.** `change-instance-type-of-ebs-backed-instance.md`: if the instance is in an ASG, stopping it makes Auto Scaling mark it **unhealthy** and possibly **terminate + replace** it (mitigation: suspend scaling processes).
**Security Concern.** A principal holding `ec2:StopInstances`/`ModifyInstanceAttribute` on an ASG member — but **not** `TerminateInstances` — can indirectly cause the ASG to terminate and relaunch instances, an indirect capacity/state manipulation and a possible cost or availability abuse.
**High-level Test Scenarios:** **Claim:** stop-induced ASG termination requires no ASG-level permission from the actor. → **Oracle:** confirm the ASG reaction is driven by health, not by the actor's identity; note it is an indirect effect. **Severity:** Low (single-account, availability/cost nuisance).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| "Resize" IAM grant also permits `userData` rewrite → boot-time code exec as instance role | `ec2:ModifyInstanceAttribute` (multiplexed) | `ec2:Attribute` / `ec2:Attribute/${AttributeName}` condition keys (must be written by operator; test case-fail-open) |
| AWS-published sample IAM policy uses `"Resource":"*"` on `iam:PassRole`/`RunInstances`/`kms:CreateGrant` | `AWSSupport-CloneXenEC2InstanceAndMigrateToNitro` runbook | Printed "sample" policy customer copies verbatim (Lens R/S) |
| Resize to arbitrary expensive/GPU type with no purchasing control | `ModifyInstanceAttribute(instanceType)` | (none documented) — billing follows type |
| AWS-authored runbook over-privileged / in-guest code exec / supply-chain driver fetch | `AWSSupport-MigrateXenToNitroLinux`, `AWSSupport-UpgradeWindowsAWSDrivers` | `AutomationAssumeRole` scoping; SSM RunCommand |
| CPU-options license-billing rule not API-enforced (console-only) | CPU options at resize | "< 4 vCPUs ⇒ default billing"; "cannot exceed default vCPUs" |
| API accepts incompatible AMI+type / silently drops NitroTPM or ENA-Express on resize | `ModifyInstanceAttribute` + compatibility rules | `resize-limitations.md` constraints; console filtering (UI-only) |
| Instance-store block on new host exposes prior-tenant data | Re-placement + NVMe auto-exposure | Instance-store zeroed on stop / before exposure (AWS-owned) |
| Stop-triggered ASG termination without terminate permission | ASG + `StopInstances` | Suspend scaling processes (customer action) |

---

## 7. Out-of-Scope Risk Categories (state explicitly)
- **Shared/managed Nitro & Xen host infrastructure**, hypervisor isolation, instance-store zeroing implementation — AWS service plane. Only *confirm the boundary*; do not probe it.
- **IMDS behavior on managed hosts**, in-guest **Windows administrator-password reset** by the `InitializeInstance.ps1` EC2Launch script (customer-side, in-guest — `change-instance-type-of-ebs-backed-instance.md`), driver installs inside the customer OS.
- **Public-IPv4 release/reallocation cross-account takeover** — real, but not resize-specific; routed to `[[project_instance-addressing-plan]]` / EIP plan.
- **Single-account self-DoS** (resize downtime, ASG churn you cause on your own group), **product/feature-parity gaps** (a type not being resize-compatible), and **customer-authored IAM policies** (a customer over-granting `ModifyInstanceAttribute` to themselves is a footgun, not an AWS defect — *unless* the over-grant ships in an AWS-managed/AWS-published policy, which flips it in-scope for Area 1).
- **Compute Optimizer** recommendation content — per-account, opt-in, low signal; deep cross-account IDOR on the recommendations API belongs to a Compute Optimizer plan, not here.

---

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens A (cross-tenant IDOR):** N/A on this surface — read all four child pages + troubleshoot page; the only resource is the caller's own `i-…` instance addressed by id under the caller's credential; no shared multi-tenant service, no resource-by-id lookup returning others' data. (Public-IPv4 reallocation is the only cross-account adjacency, routed out.)
- **Lens G (SSRF):** N/A — no field on the resize path is a URL/host the service dereferences (inputs are enum-like: type string, booleans, integers). Only possible fetch is *inside* the SSM runbook's driver download → captured under Area 2, doc-gap until the runbook definition is read.
- **Lens Q (upload):** N/A — no file/blob upload on the resize path.
- **Lens H / T (KMS / secret reachability):** N/A on resize itself; EBS-volume encryption keys are unchanged by a type change (no key operation documented). Windows password reset writes to guest, not a persisted AWS secret.
- **Lens W (attestation):** partial — resize preserves NitroTPM/ENA Express only to a supporting type (`resize-limitations.md`, compatibility gate only); **doc-gap** on whether resizing regenerates/reseals TPM measurements or endorsement material across the new-hardware move. Captured as the "silent NitroTPM loss" claim in Area 4.
- **Remaining doc-gaps requiring live/surface confirmation (enrichment resolved 2026-09-08 unless noted):**
  - **`ec2:InstanceType` evaluation side (OPEN doc-gap):** the key is confirmed *applicable* to `ModifyInstanceAttribute` (`list_ec2.md`) but no worked example exists for the resize side — whether it evaluates the instance's *current* type or the *new* `InstanceType.Value`. This decides whether it can bound a resize's destination (Area 1). Confirm live via SimulatePrincipalPolicy.
  - **`ec2:Attribute` case-sensitivity (OPEN):** whether a Deny keyed on it fails open under casing variance (Area 1) — no doc statement; confirm via SimulateCustomPolicy.
  - **Runbook driver-fetch source (OPEN):** the ENA/NVMe `ssm:SendCommand` steps' artifact source (Lens K supply-chain, Area 2) — requires reading the SSM document body, not just the reference page.
  - **RESOLVED:** CPU options = separate `ModifyInstanceCpuOptions` API (not `ModifyInstanceAttribute`), instance must be Stopped; runbook `AutomationAssumeRole` is optional (defaults to caller perms) with a `"Resource":"*"` sample policy in the clone runbook; instance-store is cryptographically erased every block on stop.
  - **IMDS options / instance-profile continuity across resize (OPEN doc-gap):** docs never explicitly state these survive a type change (IMDS options are instance-level per `configuring-instance-metadata-options.md`, implying yes; instance-profile not addressed). Low-priority.

---

## 9. Related plans (memory cross-links)
- `[[project_instance-purchasing-options-plan]]` — billing/purchasing hub (Area 3 cost angle).
- `[[project_launch-instances-plan]]` — `RunInstances` + PassRole/IMDS (the "migrate" alternative path; Area 1 userData privesc detail).
- `[[project_instance-addressing-plan]]` — public-IPv4/EIP reallocation (Area 5 adjacency).
- `[[project_nitrotpm-plan]]` — NitroTPM attestation (Area 4/6 continuity-on-resize).
- `[[project_ebs-storage-plan]]` — EBS volume-limit / attach semantics (resize-limitations volume rule; migrate path).
```
