# EC2 "Security best practices for Windows instances" — Attack Research Plan

Source of leads: `ec2-windows-security-best-practices.html` / online `.md` twin (`https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-security-best-practices.md`), read 2026-10-15. Linked/child pages fetched online: `ec2launch-v2-install.html`, `ec2launch-v2.html`, `ec2launch-v2-settings.html`, `ec2launch-download.html`, `UsingConfig_Install.html`, SSM `quick-setup-host-management.md`, SSM runbook `automation-awssupport-upgradewindowsawsdrivers.html`, `xen-drivers-overview.html`, `aws-pv-drivers`/`aws-nvme-drivers` pages, SSM `parameter-store-public-parameters-ami.html`, `windows-ami-reference/ec2-windows-ami-version-history.html`. Authoritative IAM reference: `list_ec2` / `list_ssm` / `list_iam` (fetch per [[reference-aws-iam-service-auth-ref-url]]). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

Parent chapter: [EC2 Security](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html).

> **Scope note — this is a PROSE best-practices page; it introduces NO new EC2 API, parameter, role, or cross-account surface of its own.** Its security value is (a) the AWS-authored *mechanisms it tells the customer to adopt* — SSM Automation driver-upgrade runbook, SSM Quick Setup launch-agent auto-update, launch-agent install, SSM-Parameter-Store AMI lookup, Amazon Inspector — each of which is a **shipped artifact** (Lens R/EE/U) living on a child page, and (b) the **compounding insecure defaults / documented-guarantee-vs-enforcement gaps** that recur across the Windows-instance doc cluster. The plan therefore mines the *recommended mechanisms*, not the prose.
>
> **CO-OWNERSHIP / de-dup (important).** The combined plan `ec2-windows-credential-guard-attack-research-plan.md` already spans this exact page ("Windows Security Best Practices + Update Management + Compliance Validation") from the **Credential-Guard / VBS-defeat** angle and already OWNS: launch-agent **SYSTEM / `runAs: localSystem` user-data execution**, the install-command supply chain framed as plain `Invoke-WebRequest`-with-no-hash, the **"Windows Update off by default" insecure default**, and the `ec2:GetPasswordData` / `GetInstanceTpmEkPub` / `GetInstanceUefiData` **read-side-channel**. This plan does **not** re-derive those — it cross-references them (Areas A4/A5/A6/A7) and OWNS the surface credential-guard left as explicit doc-gaps: the **SSM Automation driver runbook IAM/PassRole/DoS**, the **Quick Setup / SSM Distributor auto-update supply chain**, the **AWS driver + agent S3 download-bucket integrity (Lens EE)**, the **plaintext-admin-password transit (Lens T)**, the **whoAMI / name-filter AMI-lookup residual (Lens EE/U)**, **Amazon Inspector**, and the **audit / log-export claims (Lens O/U)**.
>
> **Related plans (cross-ref, do not duplicate):** `ec2-windows-credential-guard-attack-research-plan.md` (SYSTEM-exec, VBS, GetPasswordData, install-command supply chain, Windows-Update default); `config-windows-multiple-ip-attack-research-plan.md` (Windows guest-OS secondary-IP binding); `compliance-validation` / `data-protection` plans (EC2 Security chapter template siblings).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The highest-value leads here are **AWS-authored-artifact** findings (Lens R/EE/U), which are **in scope and reportable (`aws-security`, Tier 2)** even though the surrounding page is "best practices." A weak default in an AWS-managed policy / AWS-published runbook / AWS-operated download bucket is **AWS's defect**, not a customer footgun. Settle IAM questions **read-only** first with `iam:SimulatePrincipalPolicy` / `GetPolicyVersion` (no resources touched); escalate to live scoped calls only with canary data on a disposable instance.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the host/Nitro side, the SSM control plane, write-access to an AWS-operated S3 bucket or SSM public parameter), stop, preserve evidence, flag for AWS-Security disclosure. The guest OS and the customer's own account are the only test surface.
- **Trap reminders:** `DryRunOperation` is caller-IAM only, **not** an ownership oracle. The public SSM AMI parameters under `/aws/service/` are **Amazon-owned** (empty-account ARN) — do not chase them as a write target.

## 1. Pentest Objectives
- Prove or refute that a principal holding **only** the AWS-named permissions required to run the `AWSSupport-UpgradeWindowsAWSDrivers` runbook (or only the `AmazonSSMAutomationRole` / `AmazonSSMManagedInstanceCore` managed policies) can **force-reboot / force-stop** or re-image another team's Windows instances (cross-team DoS + instance-store data loss) without holding `ec2:StopInstances`/`RebootInstances` directly.
- Prove or refute that the **documented customer workflow** for installing/updating the Windows launch agents **and AWS PV/ENA/NVMe drivers** contains **no integrity-verification step** (no published hash, no "verify the Authenticode signature" instruction) despite the binaries being fetched from a predictable, mutable `.../latest/...` S3 path — i.e. AWS ships a supply-chain workflow whose only integrity control is transport TLS.
- Prove or refute that the SSM **Quick Setup "update the EC2 launch agent every 30 days"** mechanism (SSM Distributor association `AWS-QuickSetup-Distributor-EC2Launch-Agent-*`, package `AWSEC2Launch-Agent`) can be **redirected or re-targeted** by a principal who can edit the Quick Setup configuration / Association, turning the auto-updater into a code-delivery primitive that runs as SYSTEM via SSM Agent.
- Prove or refute that the plaintext **administrator password** written to `agent-config.yml` before Sysprep (Lens T) is readable by any non-administrator-but-privileged guest principal during its exposure window, defeating the page's own "least privilege" guidance.
- Prove or refute that the best-practices cluster's own AMI-selection guidance (version-history page lists AMI **names** with **no `--owners amazon` / authenticity guidance**) steers a customer into the **whoAMI** name-collision pattern, while confirming the SSM-Parameter-Store path it recommends is owner-pinned and safe.
- Determine whether the page's **audit/accountability** promises (launch agents export Windows logs to CloudWatch; CloudTrail/Config track changes) have **blind spots** an attacker who already has SYSTEM can exploit to evade detection.

## 2. Components, Assets, and Design

**Customer-facing interfaces / mechanisms the page recommends (the actual surface):**
- **EC2 control plane** — `RunInstances` from an AWS Windows AMI; `GetPasswordData` (admin-password retrieval). *(GetPasswordData side-channel owned by credential-guard plan.)*
- **SSM Automation** — runbook `AWSSupport-UpgradeWindowsAWSDrivers` (`ssm:StartAutomationExecution`), with an optional caller-supplied `AutomationAssumeRole`; drives `aws:runCommand` (SSM Run Command) + `aws:changeInstanceState` against a single `InstanceId`.
- **SSM Quick Setup Host Management** — "Amazon EC2 Launch Agents" option = SSM Distributor association (`AWS-QuickSetup-Distributor-EC2Launch-Agent-*`, package `AWSEC2Launch-Agent`) that checks every 30 days and updates EC2Launch / EC2Launch v2 / EC2Config via the SSM Agent (SYSTEM context on the guest).
- **Launch agents on the guest** (EC2Launch v2 / EC2Launch v1 / EC2Config) — Windows service in SYSTEM context; execute user-data (`runAs: localSystem`), set the admin account, extend the root partition, start the SSM Agent. Config file `%ProgramData%\Amazon\EC2Launch\config\agent-config.yml`.
- **SSM Parameter Store public AMI aliases** — `/aws/service/ami-windows-latest/*` (Amazon-owned, ARN `arn:aws:ssm:<region>::parameter/aws/service/...` with **empty account field**).
- **Amazon Inspector** — assessment of EC2 instances (SSM-agent-based in Inspector v2).
- **CloudWatch Logs / CloudTrail / AWS Config** — audit sinks; launch agents export Windows system/security/application/IIS logs to CloudWatch Logs.
- Microsoft-side recommendations: AD DS, PowerShell DSC, JEA, SCCM/SCOM, CIS/NIST benchmarks — **customer-controlled, OS-side, out of scope for AWS-side testing** (noted §7).

**AWS-operated assets referenced (identifiers captured for the hunter):**
- Launch-agent download buckets: `amazon-ec2launch-v2` (`.../windows/amd64/latest/AmazonEC2Launch.msi`), `ec2-downloads-windows` (`.../EC2Launch/latest/EC2-Windows-Launch.zip`, `.../EC2Config/EC2Install.zip`).
- Driver download bucket: `ec2-windows-drivers-downloads` (`AWSPV/Latest/AWSPVDriver.zip`, `NVMe/Latest/AWSNVMe.zip`, `EBSNVMeID/Latest/ebsnvme-id.zip`; versioned `…/<version>/…`).
- Driver-notification SNS topic: `arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers`.

**ASCII pipeline (recommended-mechanism view):**
```
                      ┌─────────────────────────── AWS-operated (service plane; HARD STOP on write) ──┐
 customer IAM         │  S3: amazon-ec2launch-v2 / ec2-downloads-windows / ec2-windows-drivers-downloads│
 principal            │  SSM public params: /aws/service/ami-windows-latest/*  (empty-account ARN)      │
   │                  └───────────────▲───────────────────────────────▲──────────────────────────────┘
   │ StartAutomationExecution         │ latest/ (mutable alias)        │ GetParameters (read-only, safe)
   ▼                                  │ no hash / no sig-verify step   │
 SSM Automation ──aws:runCommand──►  SSM Agent (SYSTEM) ──installs──► launch agent / PV·ENA·NVMe driver
 (AWSSupport-Upgrade…)  aws:changeInstanceState (stop/start → reboot, instance-store loss)
   │                                  ▲
   │ AutomationAssumeRole (optional → caller's own perms)              Quick Setup Distributor assoc
   └──────────────────────────────────┴──────── AWS-QuickSetup-Distributor-EC2Launch-Agent-* ──────────
 guest OS: agent-config.yml (admin password CLEAR TEXT pre-Sysprep)  ──► Sysprep sets admin pw
```

## 3. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | Notes / lead |
|---|---|---|---|---|---|
| `ssm:StartAutomationExecution` (runbook `AWSSupport-UpgradeWindowsAWSDrivers`) | SSM Automation | **Yes** (reboot/stop/reinstall) | Yes (SigV4) | per caller IAM; `AutomationAssumeRole` optional → **defaults to caller's own permissions** | **Lens B/R/L/X headline.** `InstanceId` single required param; no AWS-enforced tag/resource scoping documented. |
| `ssm:SendCommand` / `aws:runCommand` (inside runbook) | SSM Run Command | Yes | via Automation | the Automation role / instance role | installs ENA/NVMe/PV driver; command-document name not printed (doc-gap). |
| `aws:changeInstanceState` (inside runbook, offline path) | SSM Automation | Yes | via Automation | Automation role | **force-stop → force-start**; instance-store data loss, public-IP change. |
| SSM Quick Setup Host Management config ("Amazon EC2 Launch Agents") | SSM Quick Setup / Distributor | Yes (deploys/updates agent) | console/API | config editor + instance profile | **Lens R/B/EE.** Who can edit/redirect the association's package/target = **doc-gap**. |
| `ssm:GetParameters` on `/aws/service/ami-windows-latest/*` | SSM | No | Yes | any (public, Amazon-owned) | **Safe** owner-pinned path (empty-account ARN). Recommended by the page. |
| `ec2:DescribeImages` (name-filter AMI selection) | EC2 | No | Yes | any | **Lens EE/U residual** — version-history page lists AMI names with **no `--owners amazon` guidance**. |
| S3 GET on agent/driver buckets (`…/latest/…`) | S3 anonymous | No | Yes | any | **Lens EE/U** — predictable mutable path; no documented hash/sig-verify. Passive bucket-ACL check only. |
| `GetPasswordData` | EC2 | No | Yes | per IAM | **Owned by credential-guard plan** (Lens A side-channel) — cross-ref only. |

**Undocumented/console-hidden knob sweep:** the runbook's `AutomationAssumeRole` ("If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook") and `ForceUpgrade` ("proceed even though your instance already has the latest drivers") are the two most-permissive-value params — neither warns the operator. No `authorizerType:NONE`-class auth-weakening enum found on these mechanisms.

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv IAM principal in account | Another team's Windows instances | `StartAutomationExecution` on `AWSSupport-UpgradeWindowsAWSDrivers` with `InstanceId` of a foreign-but-same-account instance | **The runbook reboots/stops an instance the caller holds no `ec2:StopInstances`/`RebootInstances` on** = intra-account authz-bypass DoS via the Automation role. |
| Config editor | Every instance targeted by a Quick Setup config | edit Distributor association package/target | **A modified association delivers a non-AWS package (or redirected version) that the SSM Agent installs as SYSTEM** = fleet-wide code delivery. |
| Network MITM / DNS / bucket-write | Guest performing agent/driver install | `.../latest/…` S3 GET with no hash/sig-verify in the documented workflow | **A payload differing from the published binary is installed as SYSTEM** because no integrity gate is documented. |
| Non-admin-but-privileged guest principal | Local administrator credential | read `agent-config.yml` during the clear-text window | **The admin password is read before Sysprep deletes it** = guest privilege escalation. |
| Customer launching by AMI name | Attacker-published AMI with a colliding name | `DescribeImages --filters name=…` without `--owners amazon` | **Launch resolves to a third-party AMI** (whoAMI) = attacker code at boot as SYSTEM. |
| Any customer surface | **AWS service plane** (S3 bucket write, SSM public param write, SSM control plane) | — | **Any write/identity on the AWS side = HARD STOP, disclose.** |

## 5. Recommended Areas of Focus

### Area 1 — `AWSSupport-UpgradeWindowsAWSDrivers` runbook: Automation-role authz bypass + forced-reboot DoS  *(Lens B / R / L / X — HIGHEST PRIORITY; this plan OWNS it, credential-guard carried it as a doc-gap)*
**Background:** the page tells customers to "Use the AWS Systems Manager Automation runbook `AWSSupport-UpgradeWindowsAWSDrivers` to easily apply the updates across your instances." Runbook docs: `AutomationAssumeRole` is *"(Optional) … If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook."* Required perms (verbatim): `ssm:StartAutomationExecution`, `ssm:SendCommand`, `ssm:GetAutomationExecution`; AWS names **`AmazonSSMManagedInstanceCore`** and recommends the Automation role **`AmazonSSMAutomationRole`**. The runbook's offline path runs `aws:changeInstanceState` "Stop … then Force-stop the source instance"; the online path "restarts the instance." `ForceUpgrade=true` reinstalls even when already current. Doc warns: *"Data stored in instance store volumes will be lost. The public IP address will change if you are not using an Elastic IP."*
**Security Concern:** the destructive capability (reboot/stop/reinstall-driver across instances) is gated **only by the caller's IAM on `ssm:StartAutomationExecution` + the Automation role's reach** — the runbook's `InstanceId` is a single string with **no AWS-enforced resource/tag scoping**. If `AmazonSSMAutomationRole` (AWS-authored) grants `ssm:SendCommand` / `aws:changeInstanceState` on `Resource:"*"`, a principal holding only the runbook-invocation permission can act on **any instance in the account**, routing around a direct `ec2:StopInstances`/`RebootInstances` deny.
**High-level Test Scenarios:**
- Pull the **actual JSON** of `AmazonSSMAutomationRole` and `AmazonSSMManagedInstanceCore` with `iam:GetPolicyVersion`; audit statement-by-statement for `ssm:SendCommand`/`ec2:StopInstances`/`StartInstances`/`CreateImage` on `Resource:"*"` with no ownership `Condition`. (Lens R/S.)
- With `iam:SimulatePrincipalPolicy`, confirm a principal holding **only** `ssm:StartAutomationExecution` (+ the recommended role) can start the runbook against an `InstanceId` it does not own — settle **before** any live call.
- Live (canary, disposable instances only): start the runbook with `ForceUpgrade=true` against a canary you own; confirm the reboot/stop fires via the Automation role, not the caller's identity.
**Doc evidence:** `automation-awssupport-upgradewindowsawsdrivers` (AutomationAssumeRole, Required IAM, offline/online stop/restart, ForceUpgrade, data-loss warning). **Severity-if-true:** intra-account cross-team DoS + instance-store data loss = **Medium–High**; if `AmazonSSMAutomationRole`'s own JSON over-grants on `*` it is an **AWS-authored artifact defect (Tier 2, in scope)**. **Stop:** if evidence reaches the SSM control plane, HARD STOP.

### Area 2 — Launch-agent + driver download integrity: no documented hash/signature verification on a mutable `latest/` path  *(Lens EE / U / Q — this plan OWNS the bucket-level detail; credential-guard owns the generic "Invoke-WebRequest no-hash" framing)*
**Background:** the install/update docs fetch binaries from predictable, **mutable** S3 locations: `s3.amazonaws.com/amazon-ec2launch-v2/windows/amd64/latest/AmazonEC2Launch.msi`, `.../ec2-downloads-windows/EC2Launch/latest/EC2-Windows-Launch.zip`, `.../EC2Config/EC2Install.zip`, and drivers `.../ec2-windows-drivers-downloads/{AWSPV,NVMe,EBSNVMeID}/Latest/*.zip`. **No page in the fetched set states any SHA256/MD5 checksum or any "verify the Authenticode signature" step.** (A PV changelog note that a driver "signature expires" confirms the binaries *are* Authenticode-signed — but the documented customer workflow never instructs a verification gate.) `AmazonEC2Launch.msi` *"uninstalls previous versions of the EC2 launch services"* with no stated version-identity check.
**Security Concern:** the only documented integrity control is transport TLS + a mutable `latest/` alias. A compromise of the mutable alias, a TLS-stripping/MITM position, or (HARD-STOP class) a bucket-write misconfiguration yields a payload installed **as SYSTEM** (agent) or as a **kernel driver** (PV/ENA/NVMe) with no documented customer-side detection. Also a **downgrade/forced-reinstall** surface via the MSI's silent uninstall of prior agents.
**High-level Test Scenarios:**
- **Doc-gap confirmation (settles the finding):** grep every install/update/driver page for `sha`/`checksum`/`signature`/`verify`/`Get-AuthenticodeSignature`/`signtool` → confirm absence. The *absence of an integrity instruction* in an AWS-authored supply-chain workflow is itself the reportable finding (Lens U/R).
- **Passive, read-only** (NOT a write): check whether the AWS-operated buckets (`amazon-ec2launch-v2`, `ec2-downloads-windows`, `ec2-windows-drivers-downloads`) permit anonymous `ListBucket`/expose object metadata. **Any write/ACL anomaly = HARD STOP, disclose — do not test write.**
- Binary-level: `signtool verify /pa` + `Get-AuthenticodeSignature` on the downloaded MSI/ZIP to document what signing *does* exist (so the report accurately states "signed but no documented verify step," not "unsigned").
**Doc evidence:** `ec2launch-v2-install`, `ec2launch-download`, `UsingConfig_Install`, `aws-pv-drivers`/`aws-nvme-drivers` download URLs; no integrity step. **Severity-if-true:** AWS-authored supply-chain doc-gap enabling SYSTEM/kernel code if the transport or alias is subverted = **Medium–High** (Tier 2). **Stop:** HARD STOP on any bucket-write capability.

### Area 3 — SSM Quick Setup "update launch agent every 30 days" / Distributor association as a code-delivery primitive  *(Lens R / B / EE — NET-NEW to the corpus)*
**Background:** the page says you can "opt in to automatic updates in the SSM Quick Setup Host Management console under Amazon EC2 Launch Agents." Quick Setup docs: *"Update the EC2 launch agent once every 30 days — Enables Systems Manager to check every 30 days for a new version … Systems Manager updates the agent on your instance … supports EC2Launch, EC2Launch v2, and EC2Config."* Mechanism = an **SSM Distributor association** named with prefix `AWS-QuickSetup-Distributor-EC2Launch-Agent-`, package `AWSEC2Launch-Agent`, executed by the SSM Agent (SYSTEM) under the instance profile. Quick Setup *"add[s] the required IAM policies to the existing instance profiles … or allow[s] Quick Setup to create the IAM policies and instance profiles."*
**Security Concern:** (a) the **"required IAM policies" are referenced but never enumerated** on the page (doc-gap) — the auto-created instance-profile policy is an **AWS-authored artifact** that must be audited for over-grant (Lens R). (b) **Who can edit/redirect an existing Quick Setup configuration or its underlying Association's package/version/target is not documented** (doc-gap) — if a principal with `ssm:UpdateAssociation`/Quick-Setup-edit rights can repoint the package or pin a chosen version, the 30-day auto-updater becomes a **fleet-wide SYSTEM code-delivery channel**. (c) The association **runs as SYSTEM via SSM Agent** on every targeted instance.
**High-level Test Scenarios:**
- Enumerate the auto-created instance-profile policy (Quick Setup); `GetPolicyVersion` + audit for `ssm:*`/`s3:*`/`UpdateAssociation` over-grants on `*`.
- Determine via `list_ssm` whether `ssm:UpdateAssociation`/`CreateAssociation`/`StartAssociationsOnce` and Quick-Setup edit actions can be scoped to a specific association ARN, and whether `AWS-QuickSetup-Distributor-EC2Launch-Agent-*` associations carry an owner/creator condition — the delta is the lead.
- Live (canary): confirm whether a non-admin principal with association-edit rights can change the Distributor package name/version an existing Quick Setup association installs. **If the package resolves from an AWS-owned Distributor namespace by name, test Lens EE: can a same-named package in the caller's account shadow it?**
**Doc evidence:** `quick-setup-host-management` ("every 30 days," "required IAM policies," instance-profile creation); `ec2launch-v2` (Distributor prefix/package). **Severity-if-true:** fleet-wide SYSTEM code delivery via redirected association = **High**; over-broad auto-created policy = **Medium–High (Tier 2)**. **Stop:** HARD STOP if the Distributor package or its source resolves to AWS-owned storage you can write.

### Area 4 — Launch-agent plaintext admin password in transit (`agent-config.yml`)  *(Lens T — NET-NEW; credential-guard did not cover the storage path)*
**Background:** EC2Launch `setAdminAccount`/`Specify` docs (verbatim): *"The password is stored in `agent-config.yml` as clear text and is deleted after Sysprep sets the administrator password. EC2Launch encrypts the password using the user's key."* `Random` type persists an encrypted blob; "user's key" is cryptographically unspecified. Config path `%ProgramData%\Amazon\EC2Launch\config\agent-config.yml`; AWS claims *"Permission to create files in this directory is restricted to the administrator account to prevent privilege escalation."*
**Security Concern:** a privileged local credential exists **in clear text on disk** during a window whose length/trigger is undocumented. The page's own "least privilege / EFS-encrypt sensitive data at rest" guidance is contradicted by AWS's own agent. The directory-ACL claim is a **documented guarantee** (Lens U) whose enforcement must be checked — a mis-scoped service account (SSM run-as, IIS app-pool identity the page itself recommends) that can read `%ProgramData%\Amazon\EC2Launch\config\` reads the cleartext.
**High-level Test Scenarios:**
- On a disposable instance: during/after first boot, `icacls %ProgramData%\Amazon\EC2Launch\config\agent-config.yml` and compare the actual ACL to the "administrator-only" claim; measure the clear-text window before Sysprep deletion.
- Determine what "the user's key" is (EC2 key pair public key? DPAPI?) for the `Random` encrypted blob — does recovery require the private key, or is it DPAPI-recoverable by any admin/SYSTEM? (Overlaps the credential-guard plan's `GetPasswordData` angle — reconcile, don't duplicate.)
**Doc evidence:** `ec2launch-v2-settings` (setAdminAccount), `ec2launch-v2-install` (directory ACL). **Severity-if-true:** guest priv-esc to local admin = **Medium–High**; pure doc-vs-enforcement ACL gap = Medium. **Stop:** stays within the guest OS — no service-plane reach expected.

### Area 5 — AMI selection: safe SSM-param path vs the whoAMI name-filter residual  *(Lens EE / U)*
**Background:** the page recommends two AMI-selection paths: "Query for the Latest Windows AMI Using Systems Manager Parameter Store" and "the latest AMI when you launch new instances or when you build your own custom images" (links the version-history reference). The SSM public parameters live at `/aws/service/ami-windows-latest/*` with ARN `arn:aws:ssm:<region>::parameter/aws/service/...` — **empty account field = Amazon-owned, owner-pinned, not customer-writable.** The version-history reference lists AMI **names** (`Windows_Server-2025-English-Full-Base`, `TPM-Windows_Server-2025-English-STIG-Full`, …) with **no `--owners amazon` guidance and no warning that AMI names are not unique across accounts.**
**Security Concern:** the **SSM-parameter path is safe** (owner-pinned) — a genuine **null** for Lens EE on that path, state it as such. The **residual** is the name-filter path: a customer who follows the version-history reference and selects by `DescribeImages --filters name=Windows_Server-2025-English-Full-Base*` **without `--owners amazon`** can resolve a third-party AMI of the same name = the published **whoAMI** attack pattern, booting attacker code as SYSTEM. The best-practices cluster never warns against this.
**High-level Test Scenarios:**
- Confirm (read-only) that `/aws/service/ami-windows-latest/*` parameters are Amazon-owned and cannot be written cross-account (null-confirm the safe path).
- Confirm the version-history / finding-an-AMI pages contain **no `--owners`/authenticity guidance** (grep) → the doc-gap is the finding (Lens U authenticity-filter omission). Severity is the customer's own `DescribeImages` usage (footgun) **unless** an AWS sample/CFN/launch-template on a linked page resolves by name without owners — if so, that sample is Tier-2 reportable.
- Check `resolve:ssm` usage in any AWS-published CFN/launch-template on linked pages: does it point at `/aws/service/ami-windows-latest/*` (safe) or at a customer/public parameter resolvable by name (poisonable)?
**Doc evidence:** `parameter-store-public-parameters-ami` (empty-account ARN); `ec2-windows-ami-version-history` (names, no owner guidance). **Severity-if-true:** whoAMI boot of attacker AMI = **High**, but gated on the customer omitting `--owners` (footgun) unless shipped in an AWS artifact. **Stop:** n/a (customer-account scope).

### Area 6 — Audit / accountability blind spots  *(Lens O / U — lower priority, AWS always asks)*
**Background:** the page promises audit via CloudTrail, AWS Config, and launch-agent export of "Windows system, security, application, and IIS logs to CloudWatch Logs." The driver runbook, Quick Setup, and agent actions are the attacker's setup steps.
**Security Concern:** the destructive/code-delivery steps in Areas 1–3 run **through SSM / the SSM Agent as SYSTEM** — once an attacker has SYSTEM (Area 2/3/4), the **CloudWatch Logs export is agent-driven from inside the guest** and can be stopped/tampered (the sink is downstream of the compromised identity). CloudTrail still logs the *control-plane* `StartAutomationExecution`/`UpdateAssociation`/`SendCommand` by default (management events) — so the **setup stays auditable even when the in-guest log channel goes dark**: note the asymmetry for the hunter (detect at the API layer, not the guest-log layer).
**High-level Test Scenarios:** enumerate which runbook/Distributor steps emit CloudTrail management events vs only guest-side CloudWatch logs; confirm whether an attacker with SYSTEM can disable the CloudWatch agent/log export without a corresponding control-plane event.
**Doc evidence:** page "Audit and accountability" section. **Severity:** Low–Informational (detection-evasion enabler).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Invoke driver runbook against foreign same-account instance → reboot/stop DoS | `AWSSupport-UpgradeWindowsAWSDrivers` + `AmazonSSMAutomationRole` | "Required IAM permissions" + optional AutomationAssumeRole (no resource scoping stated) |
| Install redirected/tampered agent or driver as SYSTEM | agent/driver S3 `latest/` buckets | *none documented* — TLS only; no hash/sig-verify step |
| Repoint Quick Setup Distributor association → fleet SYSTEM code delivery | Quick Setup Host Management / `AWS-QuickSetup-Distributor-EC2Launch-Agent-*` | "required IAM policies" (unenumerated); association ownership unstated |
| Read clear-text admin password from `agent-config.yml` | EC2Launch setAdminAccount | "restricted to the administrator account to prevent privilege escalation" (ACL claim) |
| Launch attacker AMI via name collision | AMI selection by name filter | SSM public parameter path (owner-pinned) — but no `--owners` warning on name path |
| Disable in-guest log export post-SYSTEM | launch-agent → CloudWatch Logs | CloudTrail management events (control-plane, survives guest tamper) |

## 7. Out-of-Scope Risk Categories
- **Everything inside the customer's own OS/AD estate** the page recommends: Active Directory Domain Services, PowerShell DSC/JEA, SCCM/SCOM, Windows Firewall, EFS/NTFS encryption, CIS/NIST/Microsoft benchmark hardening, IIS app-pool identities, bastion-host design. These are **customer-authored configurations** — misconfigurations are customer footguns, not AWS defects.
- **IMDS on the managed Windows host** (managed-host IMDS is out of scope per corpus convention).
- **Shared-responsibility line / AWS service plane:** writing to the agent/driver S3 buckets, writing SSM public parameters, the SSM control plane, the Nitro/host side — **HARD STOP, disclose.**
- **A customer's own over-broad IAM** on `ssm:StartAutomationExecution` / association edit (footgun) — in scope **only** where the over-grant ships inside an **AWS-managed policy or AWS-created Quick Setup instance-profile policy** (Tier 2).
- **Driver-notification SNS topic** `arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers` — open subscription is **by design** (notification channel); not a flaw.
- **Microsoft tooling / 3P benchmark content** (Best Practice Analyzer, Management Packs) — third-party, out of scope.
- Single-tenant self-DoS (rebooting your own instance).

## 8. Null Hypotheses / Doc Gaps
- **Lens A (cross-tenant IDOR):** NULL on this page — no multi-tenant shared fleet, no resource-by-ID API introduced; everything is single-account. (Checked: full page + runbook + Quick Setup + AMI pages.) Cross-account reach would only appear via a shared RAM/AMI path on a *different* page.
- **Lens EE on the SSM public-parameter path:** **NULL / refuted** — `/aws/service/ami-windows-latest/*` is Amazon-owned (empty-account ARN), not customer-writable. The whoAMI residual lives only on the `DescribeImages`-by-name path (Area 5).
- **Lens F/K/G/H/W/CC/DD/FF:** no translation layer, no LLM/agent, no server-side URL-dereference field, no customer-KMS/attestation gate, no authorizer/cache/JWT on this page → NULL (checked page + all child pages fetched).
- **Lens Y (transport):** the agent/driver downloads are HTTPS; no documented `aws:SecureTransport`/min-TLS enforcement claim to attack on this page — the integrity gap (Area 2) is the live lead, not TLS downgrade. NULL-adjacent.
- **DOC-GAPS to settle before investing (not fabricated — confirmed absent):**
  1. `AmazonSSMAutomationRole` / `AmazonSSMManagedInstanceCore` **actual JSON** not printed on the runbook page → pull with `GetPolicyVersion` (gates Area 1 severity).
  2. The runbook's underlying `aws:runCommand` **command-document name** not printed → identify before any live test.
  3. Quick Setup Host Management **"required IAM policies" never enumerated**; **who can edit/redirect an existing association** unstated (gates Area 3).
  4. EC2Launch v2 `executeScript` **`runAs` default** (when omitted) — `ec2launch-v2-task-definitions` 404'd on both `.md` and `.html`; confirm via the `aws/amazon-ec2launch-v2` GitHub source or a live `ec2launch get-agent-config` (gates whether *default* user-data runs as SYSTEM — the credential-guard plan carries the SYSTEM-exec angle; reconcile).
  5. `agent-config.yml` **clear-text password window length / deletion trigger** undocumented; **"user's key"** cryptographic meaning undocumented (gates Area 4).
  6. **No integrity-verification step** (hash/sig) documented for any agent or driver download (this absence IS the Area 2 finding).
  7. Driver download bucket `ec2-windows-drivers-downloads` and agent buckets — anonymous `ListBucket` status unknown (passive read-only check only; HARD STOP on any write capability).

---
*Cross-references: [[reference-aws-iam-service-auth-ref-url]], [[project-aws-research-plans]]. Companion plans: `ec2-windows-credential-guard-attack-research-plan.md` (SYSTEM-exec/VBS/GetPasswordData/install-command/Windows-Update-default), `config-windows-multiple-ip-attack-research-plan.md`.*
