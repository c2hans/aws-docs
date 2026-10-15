# EC2 Credential Guard for Windows + Windows Security Best Practices + Update Management + Compliance Validation — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/{credential-guard,ec2-windows-security-best-practices,update-management,compliance-validation}.md`, cross-checked against the live `docs.aws.amazon.com` twins; linked pages `enable-nitrotpm-prerequisites.md`, `nitrotpm-attestation.md`, `connect-rdp.md`, `ec2launch-v2-install.md`, `UsingConfig_Install.md`, `ec2launch-download.md`, `ec2launch-v2.md`, `serverupgrade.md`, `xen-drivers-overview.md`, `ec2-launch-instance-wizard.md`, `ec2-instance-reboot.md`; authoritative IAM reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (slug `list_ec2`). Status: documentation-derived hypotheses only; nothing tested against a live account.

Parent chapter: [EC2 Security](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html).

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.
- **Drift note (RESOLVED 2026-10-15):** this plan originally stated `nitrotpm-attestation-attack-research-plan.md` did not exist. It now **does**, along with `nitrotpm-attestation-document-content-`, `nitrotpm-attestation-document-validate-`, and `nitrotpm-instance-attack-research-plan.md`. Lens W/attestation internals are owned there. A dedicated **`credential-guard-attack-research-plan.md`** now complements this bundle for the `credential-guard.html`-page-specific surface (attestability of VBS state, instance-type-allowlist capability-table gap, UEFI-lock irreversibility) and **corrects two IAM claims in this plan** — see the correction note at §5.4.

## 1. Pentest Objectives
- Prove or refute that a principal who can only edit instance **attributes** (not an IAM role) can achieve code execution as SYSTEM inside a Windows guest and thereby defeat Credential Guard / VBS from outside the OS boundary the feature claims to protect.
- Prove or refute that AWS's own documented **install/update commands** for the Windows launch agents (EC2Launch v1/v2, EC2Config) can be tampered with in transit or supply-chain, given they are plain `Invoke-WebRequest` downloads over HTTPS with no printed hash/signature verification step.
- Determine whether the "Windows Update is off by default on AWS AMIs" default, combined with the "Credential Guard requires memory-integrity/HVCI to be *disabled*" prerequisite, constitutes AWS shipping two compounding insecure defaults on the same AMI family, each weakening a documented best practice elsewhere on the same page cluster.
- Determine whether `ec2:GetPasswordData`, `ec2:GetInstanceTpmEkPub`, and `ec2:GetInstanceUefiData` — all read actions with **no action-specific IAM condition keys** per `list_ec2.md` — constitute an AWS-API side channel that bypasses the credential/attestation protections Credential Guard and NitroTPM attestation promise at the OS layer.
- Determine whether SSM Patch Manager / `ssm:SendCommand`-driven update management is a documented data-plane→control-plane reach into the guest that could be abused to disable Credential Guard or tamper with patch state (carried as a doc-gap; SSM Automation docs are outside this plan's declared mirror scope).

## 2. Components, Assets, and Design

**Customer-facing interfaces in scope:**
- EC2 control-plane API (`RunInstances`/`run-instances`, `New-EC2Instance`, `ModifyInstanceAttribute`, `GetPasswordData`, `GetInstanceTpmEkPub`, `GetInstanceUefiData`) — SigV4, IAM-authorized, resource = `arn:...:instance/*`.
- RDP (TCP/3389) into the guest OS, gated by the instance's security group (customer-owned) — `connect-rdp.md`.
- Local Group Policy Editor (`gpedit.msc`) inside the guest — **entirely customer-controlled, out-of-scope for AWS-side testing**, but the exact AWS-published steps are themselves "sample configuration guidance" and fall under Lens R scrutiny for insecure defaults in the recommended end-state.
- SSM `SendCommand` / Patch Manager / Automation runbooks (`AWSSupport-UpgradeWindowsAWSDrivers`, `AWS-PatchAsgInstance`) reaching the guest's SSM Agent — a documented control-plane→data-plane path.
- Windows launch agents (EC2Launch v1/v2, EC2Config) running on the guest as a Windows service (SYSTEM context) that execute **user data** and task definitions (`executeScript`) at boot — `ec2launch-v2.md`, `user-data.md`.

**Processes / hosts:**
- Nitro hypervisor + NitroTPM (vTPM backed by Nitro Security Chip) — enforces the VBS/Credential-Guard isolation boundary claimed on `credential-guard.md`.
- Guest Windows kernel: normal VTL0 (LSA, kernel) vs. secure VTL1 (Isolated LSA / Credential Guard) — the boundary Credential Guard's "cannot be extracted from memory" guarantee rests on.
- EC2Launch v2 agent (`%ProgramFiles%\Amazon\EC2Launch`) — processes user data/task definitions on every boot; a non-PassRole write path into the guest's SYSTEM execution context.

**Accounts/ownership:** single customer account/VPC for all of credential-guard/best-practices/update-management; AWS-managed public SSM parameter namespace (`/aws/service/ami-windows-latest/*`) and public S3 download buckets (`s3.amazonaws.com/ec2-downloads-windows/...`) for AMI/agent artifacts.

**ASCII pipeline (credential/update path):**
```
Customer IAM principal
   │ SigV4: ec2:RunInstances / ModifyInstanceAttribute(userData) / GetPasswordData
   ▼
EC2 control plane (no resource-level condition keys on GetPasswordData/
GetInstanceTpmEkPub/GetInstanceUefiData/ModifyInstanceAttribute — list_ec2.md)
   │
   ▼
Nitro hypervisor ── NitroTPM (vTPM) ── UEFI Secure Boot
   │                                        │
   ▼                                        ▼
Guest OS boot: EC2Launch v2 (SYSTEM) ──► VTL0 kernel / LSA
   runs UserData + executeScript tasks         │ (VBS boundary, customer-enabled)
   │                                           ▼
   ▼                                   VTL1 Isolated LSA (Credential Guard,
Windows Update (OFF by default on            OFF unless customer runs
AWS Windows AMIs — update-management)        gpedit.msc steps on credential-guard.md)
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Customer IAM principal (any role with `ec2:ModifyInstanceAttribute`) | Guest OS SYSTEM execution context | `ModifyInstanceAttribute` on the `userData` attribute, consumed by EC2Launch/EC2Config at next boot | Attaching the attribute without holding any credential inside the guest, then observing attacker-controlled code execute as SYSTEM in the guest, is a breach of the "only an RDP-authenticated admin configures the guest" assumption the best-practices page relies on. |
| Guest-OS normal world (VTL0 / any process with admin rights) | Isolated LSA secrets (VTL1) | Credential Guard / VBS boundary (customer-enabled via `gpedit.msc`) | Extracting NTLM hashes / Kerberos TGTs from LSA memory while Credential Guard reports "Running" in `msinfo32.exe` is the documented breach oracle. |
| EC2 control-plane caller (`GetPasswordData`, `GetInstanceTpmEkPub`, `GetInstanceUefiData`) | Guest-OS credential/attestation material | AWS API read action with no action-specific IAM condition key (list_ec2.md) | Any principal holding only the bare action (no tag/ownership condition available to the customer to add) retrieving another workload's password/TPM-EK/UEFI data they should not reach under the org's intended ABAC is a breach — this is a *customer least-privilege ceiling*, not an AWS enforcement gap, unless the resource-level ARN scoping itself is bypassable. |
| AWS-authored install scripts (Invoke-WebRequest + msiexec, `ec2launch-v2-install.md`/`UsingConfig_Install.md`/`ec2launch-download.md`) | Guest OS SYSTEM (msiexec/exe execution) | Plain HTTPS download, no printed hash/signature check, executed immediately | A MITM or compromised S3 object serving a tampered MSI/EXE/PS1 that the printed commands execute without verification is a breach of the implicit "AWS-published install steps are safe to copy-paste" guarantee. |
| SSM control plane (`ssm:SendCommand`, Patch Manager, Automation runbooks) | Guest OS SYSTEM via SSM Agent | Documented data-plane reach for patch automation (`update-management.md`) | A patch/runbook document that can be redirected to run attacker content, or a document whose IAM scoping doesn't match the instance it targets, is a control-plane→data-plane breach (carried as doc-gap pending SSM docs). |
| Shared-responsibility line (AWS Nitro root-of-trust) ↔ customer guest-OS configuration | — | NitroTPM measured boot / UEFI Secure Boot vs. customer's Credential-Guard GPO choice | Any identity/credential/ARN/account belonging to AWS's own service plane surfacing in this chain is the hard stop. |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating/Non-mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `RunInstances` / `run-instances` / `New-EC2Instance` | API/CLI/PS | Existing | Mutating | External | Launches a Windows instance, optionally with `resolve:ssm:/aws/service/ami-windows-latest/...` AMI alias | Yes (SigV4) | Any principal with `ec2:RunInstances` | `credential-guard.md` sample uses the AWS-owned public SSM parameter namespace — not customer-writable, Lens EE null (see §8). |
| `ModifyInstanceAttribute` | API | Existing | Mutating | External | Can rewrite `userData`, which EC2Launch/EC2Config execute at next boot as SYSTEM | Yes | Any principal with `ec2:ModifyInstanceAttribute` — **no condition keys defined** (list_ec2.md) | Non-PassRole action reaching live SYSTEM execution — Lens B/E variant. Top lead, see §5. |
| `GetPasswordData` | API | Existing | Non-mutating | External | Returns RSA-encrypted initial Administrator password | Yes | Any principal with `ec2:GetPasswordData` — **no condition keys** | Documented explicitly on `connect-rdp.md` as the RDP-login credential path; sits entirely outside Credential Guard's protection boundary. |
| `GetInstanceTpmEkPub` | API | Existing | Non-mutating | External | Returns the NitroTPM endorsement-key public blob | Yes | Any principal with `ec2:GetInstanceTpmEkPub` — **no condition keys** | Adjacent to the (missing) NitroTPM attestation plan; flagged, not deep-dived here (§8). |
| `GetInstanceUefiData` | API | Existing | Non-mutating | External | Returns UEFI/boot variable data | Yes | Any principal with `ec2:GetInstanceUefiData` — **no condition keys** | Same adjacency as above. |
| EC2Launch v2 / EC2Config install commands | PowerShell script, docs-published | Existing | Mutating (on guest) | External (guest-local, but driven by a public S3 URL) | Downloads and executes `AmazonEC2Launch.msi` / `EC2Install.exe` / `install.ps1` | N/A (runs inside guest) | Whoever has RDP/console access to the guest | `Invoke-WebRequest -Uri $Url -OutFile ...` then immediate `msiexec`/`Start-Process`, **no hash/signature verification printed anywhere in the three install pages**. Lens R primary target. |
| `ssm:SendCommand` / Patch Manager / `AWSSupport-UpgradeWindowsAWSDrivers` / `AWS-PatchAsgInstance` runbooks | API | Existing | Mutating | External | Drives patch/driver updates into the guest | Yes | SSM-authorized principals | IAM permissions for these runbooks live outside the EC2 mirror scope defined for this task — doc-gap, §8. |
| Local Group Policy steps to enable Credential Guard | Console/guest-local | Existing | Mutating (guest) | Guest-internal | Toggles VBS/Credential Guard | N/A | Local Administrator inside guest | Entirely customer-owned/configured; AWS supplies only the recommended GPO values (Lens R applies to the *recommendation*, not enforcement). |

## 5. Recommended Areas of Focus

### 5.1 Lens B/E variant — UserData rewrite as a non-PassRole privilege-escalation path into SYSTEM
**Background:** `ec2-windows-security-best-practices.md` recommends "Use techniques such as Role Based Access Controls to reduce the surface area of administrative accounts" and leans on EC2 Run Command/PowerShell for "scripted, repeatable change processes." Separately, `ec2launch-v2.md` documents `executeScript` task definitions that EC2Launch v2 runs at boot, and `ModifyInstanceAttribute` (list_ec2.md) can rewrite the `userData` attribute with **no condition key** restricting it.
**Security Concern:** `ec2:ModifyInstanceAttribute` is not `iam:PassRole`-shaped, so it is easy to omit from a least-privilege review focused on role-assumption paths — yet it reaches the exact same outcome: arbitrary code execution as SYSTEM inside the guest on next reboot (or immediately, if the instance is stopped/started as part of the same operation), which can disable Credential Guard's GPO, exfiltrate LSA secrets before VBS is (re-)enabled, or tamper with Windows Update / patch state the other pages recommend.
**High-level Test Scenarios:**
- Grant a scoped IAM principal only `ec2:ModifyInstanceAttribute` (and `ec2:DescribeInstances`) on a target Windows instance (no `iam:PassRole`, no SSM, no RDP credential). Rewrite `userData` with a benign canary script, reboot (or stop/start) the instance, and confirm the canary executed as SYSTEM.
- Confirm the same principal can disable Credential Guard's GPO value (`reg.exe`/`gpedit`-equivalent registry write) from inside the injected script, and that this requires none of the "Administrator privileges... using RDP" the credential-guard.md procedure assumes.
- Check whether `ec2:ModifyInstanceAttribute` supports (or could support) a `UserData`-specific tag/ownership condition key the customer could add — per list_ec2.md it currently cannot, which is the enforcement gap to document.
**Doc evidence:** `ec2-windows-security-best-practices.md` ("Least privilege"/"Role Based Access Controls"); `ec2launch-v2.md` (`executeScript` task frequency); `list_ec2.md` lines ~3726 (`ModifyInstanceAttribute`, empty condition key). **Severity-if-true:** High — full guest SYSTEM compromise and Credential-Guard bypass from a role never granted RDP or PassRole.

### 5.2 Lens R — AWS-published install scripts: unsigned/unverified download-and-execute
**Background:** `ec2launch-v2-install.md`, `UsingConfig_Install.md`, and `ec2launch-download.md` each print a PowerShell snippet of the shape `Invoke-WebRequest -Uri $Url -OutFile $DownloadFile` immediately followed by `msiexec /i "$DownloadFile"`, `Start-Process .../EC2Install.exe`, or `& .../install.ps1`.
**Security Concern:** these are AWS-authored, copy-verbatim commands (in scope per the Lens R carve-out) that download an executable/installer over HTTPS and run it with **no printed hash, checksum, or Authenticode-signature verification step** anywhere in the three pages. The only security-adjacent note on these pages is about enabling TLS 1.2 for the download itself — nothing about verifying what was downloaded before executing it as a local admin/SYSTEM-adjacent install.
**High-level Test Scenarios:**
- Confirm (from docs alone, since this is documentation-only research) that no page in the EC2Launch/EC2Config install family instructs the operator to verify a signature/hash before running the downloaded artifact — grep the full page text for "signature", "hash", "checksum", "Authenticode", "SHA256" (none found in the three pages read).
- Document the exact URLs used (`https://s3.amazonaws.com/ec2-downloads-windows/...`) and whether AWS publishes an independent, out-of-band checksum for these objects anywhere in the Windows AMI reference (follow-on doc check, not yet done — §8).
- Treat this as a supply-chain/MITM resilience gap in AWS's own guidance rather than a direct vulnerability: the breach oracle is "the printed procedure succeeds with a substituted artifact and the operator has no step that would have caught it."
**Doc evidence:** `ec2launch-v2-install.md` lines 36-41; `UsingConfig_Install.md` lines 50-58; `ec2launch-download.md` lines 26-34. **Severity-if-true:** Medium — requires network-position or S3-object tampering (which AWS itself controls), but it is a documented AWS gap in copy-verbatim guidance, so it is reportable under the Lens R carve-out even though exploitation requires an additional precondition AWS doesn't control end-to-end.

### 5.3 Lens U — Compounding insecure defaults across the page cluster (Windows Update off / HVCI must be disabled)
**Background:** `ec2-windows-security-best-practices.md` states plainly: *"By default, instances that are launched from AWS Windows Server AMIs don't receive updates through Windows Update."* The same page's "Patch management" bullet recommends the opposite ("regularly patch, update, and secure the OS"). Separately, `credential-guard.md`'s Prerequisites section requires memory integrity (HVCI) to be **disabled** before Credential Guard can be turned on — the Microsoft-recommended companion VBS control is explicitly traded away.
**Security Concern:** two AWS-documented defaults/prerequisites each weaken a security property the surrounding prose otherwise recommends, and neither page cross-links the risk trade-off: (a) the AMI ships with its most basic patch-delivery mechanism off, so "update management" is entirely opt-in and easy to silently skip; (b) enabling Credential Guard per AWS's own steps requires disabling HVCI, with no caveat about what protection HVCI itself provided or how to compensate.
**High-level Test Scenarios:**
- Verify via `DescribeImages`/launch of a stock AWS Windows AMI (documentation-only: cite the exact sentence) that Windows Update is confirmed off by default — already directly asserted in the doc text, so this is largely a documentation fact-check plus "how would an operator discover this without reading this specific sentence" usability oracle.
- Check whether any AWS Windows AMI release notes or the Windows AMI Reference state a compensating control recommendation when HVCI is disabled for Credential Guard (follow-on check, §8).
- Cross-check `update-management.md`'s "AWS updates all Windows AMIs managed by AWS within five days after Microsoft releases a patch" claim against whether that only patches the **AMI** (new launches) and does nothing for **already-running instances** — the gap between "AMI patched" and "fleet patched" is exactly where Patch Manager is supposed to step in, but nothing enforces that it is configured.
**Doc evidence:** `ec2-windows-security-best-practices.md` line 42 (Windows Update default-off) and line 95 (five-day AMI patch cadence); `credential-guard.md` lines 25-26 (HVCI must be disabled). **Severity-if-true:** Medium/Informational — these are disclosed defaults, not hidden ones, but the plan flags them because they are AWS-authored defaults that directly undercut AWS's own adjacent best-practice recommendation, which is exactly the Lens U "guarantee vs. enforcement" shape (the "best practice" is prose; the default is the opposite).

### 5.4 Lens C/T — GetPasswordData / GetInstanceTpmEkPub / GetInstanceUefiData as un-scoped side channels adjacent to Credential Guard's guarantee
**Background:** `credential-guard.md` promises Credential Guard "protect[s] Windows login credentials from being extracted from the operating system's memory." `connect-rdp.md` separately documents that RDP login depends on `GetPasswordData`, and `list_ec2.md` shows `GetPasswordData`, `GetInstanceTpmEkPub`, and `GetInstanceUefiData` all have **no action-specific IAM condition keys**.
> **CORRECTION (2026-10-15, from `list_ec2` re-audit; see `credential-guard-attack-research-plan.md` §5.4):** the claim below and in the §4 table that these actions have "no condition keys" is **wrong.** `GetPasswordData`, `GetInstanceTpmEkPub`, `GetInstanceUefiData`, and `ModifyInstanceAttribute` all carry the full generic instance-attribute key set, **including `aws:ResourceTag/${TagKey}` and `ec2:ResourceTag/${TagKey}`** (plus `ec2:InstanceID`, `ec2:Region`, metadata-options keys, `ec2:Tenancy`, …). `ModifyInstanceAttribute` additionally has `ec2:Attribute`/`ec2:Attribute/${AttributeName}`. They lack only an *action-specific* / CG-state key. So customers **can** tag-scope (ABAC) these reads, and §5.1's `userData`-rewrite privesc **is** IAM-mitigable via `Deny ... ec2:Attribute/${AttributeName}=userData`. Read the paragraphs below with that correction.

**Security Concern:** Credential Guard's threat model is explicitly "credentials extracted from OS memory." It says nothing about, and cannot protect against, the AWS control-plane handing out the initial admin password or TPM/UEFI measurement material to any IAM principal who holds the action on the instance's ARN. The narrower true finding: these actions carry **no condition key tying the read to CG/attestation state**, so even a tag-scoped `GetPasswordData` still returns the API-vended initial admin credential, which lives entirely outside CG's "in-OS-memory extraction" boundary — do not conflate "credentials can't be extracted from OS memory" with "credentials can't be obtained."
**High-level Test Scenarios:**
- Enumerate, from `list_ec2.md`, every other credential/attestation-adjacent action on EC2 Windows instances and confirm which do/don't support `aws:ResourceTag`/`ec2:ResourceTag` conditions (did for the three named actions: none).
- Document this explicitly as a **scope boundary** of Credential Guard's guarantee (not a bug in Credential Guard itself) so a reader doesn't conflate "credentials can't be extracted from OS memory" with "credentials can't be obtained at all."
- Flag `GetInstanceTpmEkPub`/`GetInstanceUefiData` as adjacent to the NitroTPM attestation flow (`nitrotpm-attestation.md`) — whether EK-pub retrieval outside the formal attestation-document flow weakens the attestation guarantee is explicitly deferred to the (missing) NitroTPM attestation plan; this plan only raises the question (§8).
**Doc evidence:** `credential-guard.md` line 8 (guarantee statement); `connect-rdp.md` line 35 (`GetPasswordData` dependency); `list_ec2.md` entries for `GetPasswordData`, `GetInstanceTpmEkPub`, `GetInstanceUefiData` (all condition-key fields empty). **Severity-if-true:** Low/Informational as a doc-vs-scope clarification; would escalate to Medium–High if a customer-authored IAM policy could be shown to believe it was restricting these actions by tag when it structurally cannot.

### 5.5 Lens D/V — SSM Patch Manager / SendCommand as a documented data-plane reach into the guest (doc-gap)
**Background:** `update-management.md` names AWS Systems Manager Patch Manager and the `AWS-PatchAsgInstance` runbook; `ec2-windows-security-best-practices.md` names the `AWSSupport-UpgradeWindowsAWSDrivers` Automation runbook.
**Security Concern:** both are control-plane-initiated code execution into the guest (SSM Agent → guest SYSTEM), which is architecturally identical in effect to §5.1's UserData path, but is driven by SSM IAM rather than EC2 IAM. Whether the runbooks are scoped per-instance (tag conditions) or could be invoked against an unintended instance set is unanswerable from the EC2 UserGuide mirror alone.
**High-level Test Scenarios:**
- Pull and audit the actual `AWSSupport-UpgradeWindowsAWSDrivers` and `AWS-PatchAsgInstance` runbook permission/parameter documents (Lens R move) — requires the `systems-manager-automation-runbooks` doc tree, which is outside this task's declared mirror scope.
- Ask whether Patch Manager's target selection (tag-based) can be satisfied by a caller who controls tags but not the instance itself (self-widening, Lens S shape) — unanswerable without the SSM docs.
**Doc evidence:** `update-management.md` lines 8-10; `ec2-windows-security-best-practices.md` line 48. **Severity-if-true:** unknown pending doc-gap closure; carried to §8.

## 6. Threat Model Test Objectives

| Threat/Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Guest SYSTEM code exec via `ModifyInstanceAttribute(userData)` without PassRole/RDP | EC2Launch v2 / EC2Config | Least-privilege/RBAC prose on `ec2-windows-security-best-practices.md`; no IAM condition key on the action itself |
| LSA secret extraction from VTL0 while Credential Guard reports "Running" | Guest OS VBS/Isolated LSA | NitroTPM + UEFI Secure Boot + VBS isolation (`credential-guard.md`) |
| Tampered install artifact executed via AWS-published PowerShell | EC2Launch v1/v2, EC2Config | HTTPS-only download guidance; absence of hash/signature verification step |
| Admin-password/TPM-EK/UEFI-data retrieval by an under-scoped IAM principal | EC2 control plane | Resource-level IAM only; no action-specific condition keys (`list_ec2.md`) |
| Fleet-wide unpatched Windows exposure due to default-off Windows Update | Windows AMI defaults | "Patch management" best-practice bullet vs. documented default-off state |
| SSM runbook/Patch Manager misuse to reach guest SYSTEM | SSM Agent / Patch Manager | Doc-gap — requires SSM Automation runbook docs |

## 7. Out-of-Scope Risk Categories
- Whether an individual customer actually enables Credential Guard, HVCI alternatives, antivirus, or any Local Group Policy setting inside their own guest OS — pure shared-responsibility, customer-configured (the *steps* AWS prints are in scope for Lens R; whether a given customer *follows* them is not).
- Compliance-validation.md itself: it is a pointer page (AWS Artifact, compliance-programs-by-service) with no capability table, API, or security guarantee to trace — Lens U has nothing to attach to here beyond "AWS Artifact access control," which is a separate service's surface.
- IMDS/metadata-service hardening on these specific pages — none of the four target pages or their direct links print an IMDSv1/`HttpTokens optional` sample; do not manufacture a lead where the grep came back empty (see §8).
- Bare-metal / unsupported instance-type exclusions from Credential Guard — documented capability gaps, not security bugs.
- NitroTPM attestation-document/KMS-condition-key internals (full Lens W deep dive) — explicitly deferred to the missing cross-reference plan, not re-derived here.
- The `resolve:ssm:/aws/service/ami-windows-latest/...` AMI alias in the `credential-guard.md` CLI/PowerShell sample — checked for Lens EE (predictable-name hijack) and found null: `/aws/service/` is an AWS-exclusive public-parameter namespace, not customer-writable, so pre-registration/poisoning is not available to an external attacker.

## 8. Null hypotheses / doc gaps

- **Lens G (SSRF):** Null. Checked `credential-guard.md`, `ec2-windows-security-best-practices.md`, `update-management.md`, `compliance-validation.md`, and all nine directly linked pages read in full — no field in this cluster is a URL/host/endpoint the service dereferences server-side (the only URLs present are documentation hyperlinks and the hard-coded S3/console links the *customer's own browser or PowerShell session* fetches, not a server-side fetch on the customer's behalf).
- **Lens F (translation-layer injection):** Null. No wire-protocol/parser/query-translation layer appears in this cluster.
- **Lens H (CMK/encryption-context):** Null for this cluster specifically (no customer-managed KMS key use is documented on these four pages); KMS/attestation condition-key semantics belong to the NitroTPM attestation cluster, not here.
- **Lens I (tagging/ABAC):** Fired only as the negative finding in §5.4 (no condition keys to tag-scope); no `TagResource`/`UntagResource` surface documented on these pages themselves.
- **Lens J (OAuth/3P linking):** Null — no 3P integration on this cluster.
- **Lens K (prompt injection):** Null — no LLM/agent component.
- **Lens L (resource exhaustion):** Null — no size/rate-limited parser surface documented here; EC2Launch task-definition parsing could theoretically be probed but is not described with any limits in the read pages.
- **Lens M (shared-identifier interception):** Null — no session/presigned-URL/MagicLink surface in this cluster.
- **Lens N (namespace migration):** Null — no dual-ARN/migration language on these pages. EC2Launch v1→v2 is a feature migration, not an ARN/namespace one; tracked instead as an update-management lead, not Lens N.
- **Lens O (audit-log evasion):** Checked `ec2-windows-security-best-practices.md`'s "Audit and accountability" section — it describes CloudTrail/VPC Flow Logs/CloudWatch as customer-opt-in, not AWS-enforced; no blind-spot claim is made strongly enough to generate a falsifiable lead beyond "logging is optional, so an attacker who disables it before acting leaves no record" — a generic observation, not cluster-specific. Marked Low/out-of-scope.
- **Lens P (identity proofing/registration):** Null — no registration/OTP/uniqueness workflow in this cluster.
- **Lens Q (upload):** Null — no file-upload surface; the "download install.ps1/MSI" direction is covered under Lens R (§5.2), not Q (Q is for customer→service uploads).
- **Lens V (network segmentation):** Partially fired via `connect-rdp.md`'s security-group guidance (customer-owned, out of scope) — no AWS-managed control/storage ENI is described in this cluster.
- **Lens W (attestation-conditioned authz):** **No longer a doc-gap (resolved 2026-10-15).** The `nitrotpm-attestation-*` plans now exist and own attestation internals, and the CG-specific Lens-W finding is now developed and confirmed in `credential-guard-attack-research-plan.md` §5.1: Credential-Guard/VBS state is **not measured by any PCR** (PCR0–7 are firmware/boot; PCR8–15 reserved for the OS with no AWS statement that Windows extends VBS state) and has **no control-plane/CloudTrail/EventBridge signal** — "CG is running" is self-asserted via in-guest `msinfo32.exe` only. Any attestation/KMS gate validates boot integrity, never CG enablement.
- **Lens X/AA/BB/CC/DD/EE/FF:** Null for this cluster — no action-family/legacy-twin, no share/revoke lifecycle, no multi-layer canonicalization, no trusted-upstream-header consumption, no caching layer, and no JWT/OIDC token validation appears anywhere in `credential-guard.md`, `ec2-windows-security-best-practices.md`, `update-management.md`, or `compliance-validation.md` or their direct links. Lens EE was explicitly checked against the `resolve:ssm:` AMI alias and refuted (see §7).
- **Carried doc-gap:** SSM Patch Manager / Automation runbook IAM permission documents (`AWSSupport-UpgradeWindowsAWSDrivers`, `AWS-PatchAsgInstance`) were not pulled — they live under the `systems-manager-automation-runbooks` doc tree, outside this task's declared EC2 mirror scope. §5.5 is a stub pending that pull.
- **Carried doc-gap:** whether AWS publishes an independent checksum/signature for the EC2Launch/EC2Config S3 install artifacts was not checked beyond the three install pages themselves (none found there); the broader Windows AMI Reference was not searched.
