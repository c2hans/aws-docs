# EC2 Credential Guard for Windows (`credential-guard.html`) — Attack Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/credential-guard.html` (markdown twin `credential-guard.md`; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/credential-guard.md`). Online vs offline verified **byte-identical** on all substantive lines (only cosmetic front-matter/whitespace drift), 2026-10-15 — either copy is citable.

**Authoritative IAM source:** AWS Service Authorization Reference `list_ec2` (`https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` / `.md`, ~35,500 lines when rendered). Line numbers below are from a 2026-10-15 fetch; re-grep by action name if they drift.

**Status:** documentation-derived hypotheses only — nothing tested against a live account.

---

## 0. How to use this document — and its relationship to existing plans

Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs. **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (Nitro root-of-trust, attestation signer, SSM service identity), stop, preserve evidence, flag for AWS-Security disclosure.

**This is a FOCUSED COMPLEMENT, not a standalone re-derivation.** A broader bundled plan already exists and still owns several leads — do not re-run them from zero:

| Existing plan | Owns (do not duplicate) |
|---|---|
| `ec2-windows-credential-guard-attack-research-plan.md` (4-page bundle: credential-guard + windows-best-practices + update-management + compliance-validation) | **§5.1** `ModifyInstanceAttribute(userData)` → guest-SYSTEM non-PassRole privesc (its TOP lead); **§5.2** unsigned `Invoke-WebRequest`+`msiexec` install scripts (Lens R); **§5.3** Windows-Update-off + HVCI-disable compounding defaults; **§5.5** SSM Patch Manager data→control-plane reach (doc-gap). This plan references those by number rather than restating them. |
| `nitrotpm-attestation-attack-research-plan.md` (+ `-document-content`, `-document-validate`) | KMS `kms:RecipientAttestation:NitroTPMPCR<N>` gate, reproducible-measurement/replay, PCR7-cert control, attestation-doc internals. **This closes the bundle plan's "attestation plan is missing" drift note — those plans now exist.** |
| `nitrotpm-instance-attack-research-plan.md` | `nitrotpm-instance.html` launch-only-enable / can't-disable / in-guest "stop using" surface. |
| `enable-nitrotpm-prerequisites-attack-research-plan.md` | The Requirements/Considerations page: launch prereqs as un-IAM-expressible guarantees, static instance-type-list drift, BitLocker original-instance-only, `Update-EC2SecureBootCertificate.ps1` runbook. |
| `verify-nitrotpm-support-on-instance-attack-research-plan.md` | Instance-side `DescribeInstances` read/verify surface, `tpm-support` filter. |

**What THIS plan owns (net-new to `credential-guard.html` specifically):** the gap between what Credential Guard *claims* to protect and what AWS can *observe or enforce* about it — attestability of VBS state (Lens W), the capability-table-vs-API gap for the supported-instance-type allowlist (Lens U/X), UEFI-lock irreversibility (Lens AA), and **two factual corrections to the bundle plan's IAM claims** (see §5.4 note).

---

## 1. Pentest Objectives

1. Prove or refute that **"Credential Guard is running" is unverifiable from outside the guest** — no EC2 API, console field, CloudTrail event, EventBridge event, or NitroTPM attestation PCR reflects VBS/Credential-Guard/HVCI state — so any policy, automation, or human control that *trusts* CG is enabled is trusting a self-asserted in-guest `msinfo32.exe` reading that a compromised guest can forge. (Lens W / U / O)
2. Prove or refute that the page's ~35-entry **supported-instance-type allowlist is pure prose with no API backing**: no `DescribeInstanceTypes` filter, `InstanceTypeInfo` field, or IAM condition key reports "supports Credential Guard / VBS," so neither a policy author nor an operator can programmatically validate the allowlist or detect its drift. (Lens U / X)
3. Determine whether the **only** IAM lever that *can* enforce the allowlist — `ec2:InstanceType` on `RunInstances` — is adequate, given it is a flat string match with no "deny bare-metal" / "deny the excluded `.48xlarge` family member" predicate, and given AWS's own page never mentions it. (Lens U / S)
4. Determine whether the **UEFI-lock irreversibility** the page attaches to memory integrity ("can't be disabled after it has been enabled with UEFI lock … create a new instance") — mirrored by NitroTPM's launch-only/can't-disable property — creates a lifecycle footgun with no control-plane remediation and no outside-visible state. (Lens AA / U)
5. Correct and tighten the bundle plan's IAM claims for `GetPasswordData` / `GetInstanceTpmEkPub` / `GetInstanceUefiData` / `ModifyInstanceAttribute` (they are **not** condition-keyless), and re-scope the resulting Credential-Guard-boundary side-channel question accordingly. (Lens C / T / S)

---

## 2. Components, Assets, and Design (delta over the bundle plan's §2)

The bundle plan's §2 already enumerates the EC2 control plane, RDP, `gpedit.msc`, EC2Launch/SSM, and the VTL0/VTL1 split. This section adds only what `credential-guard.html` contributes that the bundle treated thinly:

- **The protection claim (verbatim):** Credential Guard "uses the AWS Nitro System to protect Windows login credentials from being extracted from the operating system's memory." The protected asset is **LSA secrets (NTLM hashes, Kerberos TGTs) in the Isolated LSA (secure VTL1)**. The threat model it addresses is explicitly *in-OS memory extraction* — nothing about the AWS control plane.
- **Prerequisite chain (each is a separate owner/boundary):**
  - AMI must be preconfigured for **NitroTPM + UEFI Secure Boot** (links `enable-nitrotpm-prerequisites.md`; owned by that plan + the NitroTPM cluster). Secure Boot's root of trust (PK/KEK/db/dbx) is **image-owner-chosen** via `register-image --uefi-data` — self-signed attacker keys are fully supported by the documented API (`create-ami-with-uefi-secure-boot.md`, `how-uefi-secure-boot-works.md`). Attestation plans own this; cite for the trust-root caveat.
  - **Memory integrity (HVCI) must be DISABLED** before CG can be enabled, and once HVCI is "Enabled with UEFI lock" it "can't be disabled" (page's own disable-memory-integrity section). HVCI-disable compounding-default is the bundle plan's §5.3; the *irreversibility* half is net-new here (§5.3 below).
  - A **supported, non-bare-metal instance type** from a hardcoded ~35-entry list; `C7i.48xlarge`/`M7i.48xlarge`/`R7i.48xlarge` are explicitly **excluded** despite the rest of their families being included.
- **Enable path:** entirely in-guest — RDP in, `gpedit.msc` → Computer Configuration → Administrative Templates → System → Device Guard → Turn On Virtualization Based Security → "Secure Boot and DMA Protection" + Credential Guard Configuration = **"Enabled with UEFI lock."**
- **Verify path:** entirely in-guest — `msinfo32.exe`, confirm "Credential Guard" shows "Running." **This is the only verification mechanism the page offers.**
- **The sample launch** (`aws ec2 run-instances --image-id resolve:ssm:/aws/service/ami-windows-latest/{{TPM-Windows_Server-2022-English-Full-Base}} --instance-type {{c6i.large}} …`) carries **no NitroTPM/Secure-Boot flags** — the prerequisite is baked into the chosen AMI, not expressed at launch. (`resolve:ssm:/aws/service/*` is AWS-exclusive public-parameter namespace → Lens EE null, same as bundle plan §7.)

**Ownership seam that matters:** NitroTPM + Secure Boot are **AWS-attested, boot-time, measurable**. Credential Guard / VBS / HVCI are **customer-toggled, post-boot, in-guest, and NOT measured by anything AWS exposes.** The feature stacks a non-attestable guest-OS control on top of an attestable firmware root — and markets the combination as "uses the AWS Nitro System to protect." That seam is the spine of this plan.

---

## 3. Trust-Boundary Map (delta rows)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Any outside observer / automation / KMS attestation policy | "Is Credential Guard actually running on instance X?" | **No crossing exists** — the only answer source is in-guest `msinfo32.exe`; no PCR, API, or event reflects it | If a party gates access, trust, or compliance on CG being enabled and the only evidence is a value a root-compromised guest can fabricate (or that was simply never set), the "protection" is self-asserted — reaching the "trusted" state without CG actually running is the breach. |
| Policy author (SCP/permission-boundary) | "Only launch CG-capable instance types" | `ec2:InstanceType` on `RunInstances` (flat string match) — **no capability predicate** | Launching an excluded type (`*.48xlarge`, bare metal) that slips a hand-maintained allow/deny list, OR being unable to express the allowlist without hardcoding the same prose list AWS published, is the enforcement gap. |
| Instance owner (lifecycle) | A CG/HVCI-misconfigured instance | UEFI-lock + NitroTPM launch-only-enable irreversibility | No control-plane action disables NitroTPM or a UEFI-locked HVCI/CG state; the only "fix" is terminate + relaunch. A caller who can `RunInstances` but not terminate (or who relies on in-place reconfig) is stuck, and the bad state is invisible to the control plane. |
| Caller with `ec2:GetPasswordData` on the instance ARN | Initial Administrator password (outside CG's VTL1 boundary) | `GetPasswordData` — resource-level IAM, **tag-scopable** (`aws:ResourceTag`) but no CG-state condition | Retrieving the RDP admin password via the control plane while CG protects only *in-OS-memory* extraction demonstrates CG's guarantee does not cover the API-vended initial credential. Not an AWS bug — a scope-of-guarantee clarification unless a policy *believes* it gated this and structurally did not. |
| Shared-responsibility line (AWS Nitro / attestation signer) | — | NitroTPM measured boot / Secure Boot vs. customer CG GPO | Any AWS-service-plane identity/credential/ARN surfacing here = HARD STOP, preserve + disclose. |

---

## 4. API / Interface Inventory (corrected IAM facts)

Only rows where this plan **adds or corrects** the bundle plan's §4. Resource type `instance*` throughout; keys verified against `list_ec2` 2026-10-15.

| Name | Mut. | Condition keys (authoritative) | Net-new note |
|---|---|---|---|
| `RunInstances` | Yes | `instance*` row includes **`ec2:InstanceType`** (line 31202); `image*` row has `ec2:ImageID`,`ec2:Owner`,`ec2:Public`,`ec2:RootDeviceType`,… but **NOT** `ec2:BootModeOverride` | `ec2:InstanceType` is the *only* lever to enforce the CG instance-type allowlist. **No boot-mode key on launch** → cannot IAM-require UEFI/Secure-Boot at `RunInstances` time. |
| `GetPasswordData` | No | **~20 generic instance-attribute keys incl. `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:InstanceID`, `ec2:Region`, `ec2:MetadataHttpTokens`, …** (action rows ~26855+) | **CORRECTION:** not "no condition keys." It IS tag/ABAC-scopable. What it lacks is any *action-specific* or *CG-state* key. |
| `GetInstanceTpmEkPub` | No | Same generic set as above (rows 26345-26367) | Same correction. NitroTPM-EK read; attestation plans own the EK-outside-attestation-flow question. |
| `GetInstanceUefiData` | No | Same set + `ec2:NewInstanceProfile`,`ec2:PlacementGroup`,`ec2:ProductCode` (rows 26392-26420) | Same correction. |
| `ModifyInstanceAttribute` | Yes | `instance*` row incl. **`ec2:Attribute`**, **`ec2:Attribute/${AttributeName}`** + the generic set (rows ~27903-27930) | **CORRECTION:** has keys. `ec2:Attribute/${AttributeName}` is the *only* lever to block `userData` rewrite (bundle §5.1) while allowing other attribute edits — document this as the mitigation the bundle plan's top lead needs. |
| `CreateImage` | Yes | `image*` row **includes `ec2:BootModeOverride`** (line 14549) | The *sole* API where boot-mode is IAM-scopable — and it's image creation, not launch. Asymmetry worth noting. |
| `DescribeInstanceTypes` | No | — | Filters include `nitro-tpm-support`, `supported-boot-mode`; **no `credential-guard`/`vbs`/`memory-integrity` filter.** `InstanceTypeInfo` has `nitroTpmSupport`,`SupportedBootModes`,`bareMetal` but **no CG/VBS field.** The allowlist is not API-derivable. |

---

## 5. Recommended Areas of Focus

### 5.1 Lens W / O — Credential Guard state is non-attestable and has no control-plane signal (PRIMARY net-new lead)
**Background:** `credential-guard.md` offers exactly one verification method: in-guest `msinfo32.exe` showing "Credential Guard … Running." `nitrotpm-attestation-document-content.md` enumerates every PCR: PCR0–7 are firmware/boot-manager/Secure-Boot-policy measurements; PCR8–15 are generically "Defined for use by the Static Operating System" with **no AWS statement that Windows extends VBS/CG/HVCI status into them**; only PCR4/PCR7/PCR12 are used to validate an Attestable AMI. `enable-nitrotpm-prerequisites.md` states even the underlying "NitroTPM state is not displayed in the Amazon EC2 console." No CloudTrail/EventBridge/API signal for CG/VBS/HVCI exists anywhere in the cluster.
**Security Concern:** Credential Guard is marketed as "uses the AWS Nitro System to protect," which invites the inference that Nitro/attestation can *vouch* for it. It cannot. "CG is running" is a claim made **by the very OS CG is supposed to protect**, readable only from inside that OS. Consequences:
- A root-compromised guest can report "Running" via a forged `msinfo32`/WMI/registry surface while CG is off and LSA secrets are extractable.
- A KMS key policy or external verifier gated on NitroTPM attestation PCRs is validating **boot/firmware integrity only** — it will happily release secrets to an instance that booted a Secure-Boot-signed image but never enabled CG (or had it disabled post-boot). The attestation-conditioned-authz gap is architectural, not a bug in any single policy.
- Compliance automation that "confirms Credential Guard is enabled fleet-wide" has no trustworthy data source; it is either reading agent-reported guest state (forgeable) or assuming the GPO took.
**High-level Test Scenarios (hunter):**
- Enumerate every documented source of CG/VBS state (`msinfo32`, WMI `Win32_DeviceGuard`, registry `HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard`, event logs) and confirm all are in-guest and OS-trust-dependent — i.e. a SYSTEM-level attacker can set each to report "Running" independent of actual VTL1 enforcement.
- Generate a NitroTPM Attestation Document on a CG-enabled and a CG-disabled instance built from the *same* Attestable AMI; confirm the PCR set (and therefore any KMS/verifier decision) is **identical** regardless of CG state → attestation cannot distinguish them. (Cross-ref `nitrotpm-attestation-attack-research-plan.md` for the KMS-gate PoC harness; this lead supplies the "CG is invisible to it" input.)
- Search for any AWS mechanism (Inspector, Config rule, SSM Inventory) that purports to report CG state and trace it to its data source; if it reads guest agent output, it inherits the forgeability.
**Breach oracle:** reaching a "CG-trusted" decision (KMS release, Config PASS, compliance tick) on an instance where CG is provably not enforcing, OR extracting LSA secrets while every documented control reports "Running."
**Preconditions:** guest admin/SYSTEM for the forgery half (realistic post-exploit); none for the attestation-blindness half (pure doc/architecture fact). **Severity-if-true:** Medium–High — defeats the assurance value of the feature, not the feature's in-memory protection itself; escalates where a credential-release decision depends on it. **Stop:** once attestation is shown CG-blind and in-guest state shown forgeable, the architectural gap is established — do not chase individual verifier products.

### 5.2 Lens U / X — Supported-instance-type allowlist is prose with no API backing or capability predicate
**Background:** the page hardcodes ~35 supported types (C5/C5d/C5n/C6i/C6id/C6in/C7i/C7i-flex/M5/M5d/M5dn/M5n/M5zn/M6i/M6id/M6idn/M6in/M7i/M7i-flex/R5/R5b/R5d/R5dn/R5n/R6i/R6id/R6idn/R6in/R7i/R7iz/T3) and excludes bare metal + `C7i.48xlarge`/`M7i.48xlarge`/`R7i.48xlarge`. Subagent audit: **no `DescribeInstanceTypes` filter and no `InstanceTypeInfo` field** reports CG/VBS capability (only `nitroTpmSupport`, `SupportedBootModes`, `bareMetal` exist); **no IAM condition key** encodes CG/VBS; the *only* enforcement lever is `ec2:InstanceType` on `RunInstances` (line 31202), a flat string match.
**Security Concern (two shapes):**
- **(a) Capability-table-vs-API gap (Lens U):** an operator or policy author cannot programmatically ask "can this type run CG" — they must copy AWS's prose list and maintain it by hand, with **no way to detect drift** when AWS silently edits the supported set (same drift class `enable-nitrotpm-prerequisites-attack-research-plan.md` flags for the NitroTPM type list). A fleet built against a stale copy either over-restricts or launches CG-incapable types believing they're covered.
- **(b) Enforcement is flat-string-only (Lens X/S):** `ec2:InstanceType` cannot express "all of family M7i except `m7i.48xlarge`" or "no bare-metal" as a predicate — the policy must enumerate every allowed/denied type literally. The excluded `.48xlarge` members are the trap: they belong to otherwise-allowed families, so a family-prefix allow (`m7i.*`) — a natural way to write the policy — **silently permits the one excluded size**. AWS's page documents the exclusion but never warns that the obvious IAM encoding fails to honor it.
**High-level Test Scenarios:**
- Confirm from `list_ec2`/API refs (done: no CG filter/field/key) and document the exact enforcement ceiling.
- Draft the "correct" SCP enforcing the allowlist and show how many literal exclusions it needs; demonstrate that a `StringLike` family-glob permits `m7i.48xlarge`.
- Launch (in a lab) an excluded `*.48xlarge` and confirm no API/service-side guard rejects it for CG purposes — the only failure surfaces in-guest at CG-enable time.
**Breach oracle:** a plausibly-written allowlist policy that admits an excluded type, or an operator with no API path to validate the list. **Severity-if-true:** Low–Medium (customer least-privilege/robustness footgun + AWS doc-vs-mechanism gap under the Lens U carve-out). **Stop:** once the no-API-backing fact and the glob-bypass are both shown.

### 5.3 Lens AA / U — UEFI-lock + NitroTPM irreversibility with no control-plane remediation or visibility
**Background:** `credential-guard.md` disable-memory-integrity section: memory integrity (HVCI) "can't be disabled after it has been enabled with UEFI lock. We recommend creating a new instance … and terminating the unsupported instance." CG itself is set to "Enabled with UEFI lock" by the same mechanism (irreversibility for CG is *implied by the identical VBS/UEFI-lock mechanism*, not stated verbatim — note the inference). `nitrotpm-instance.md`: NitroTPM is launch-only-enable, "After an instance is enabled for NitroTPM, you can't disable it" — the only "stop using" path is disabling the in-guest TPM driver (cosmetic, not a control-plane state change).
**Security Concern:** the whole CG prerequisite stack is a one-way ratchet with **no control-plane off switch** and **no outside-visible state** (§5.1). A misconfiguration (CG enabled on a workload that then needs HVCI; HVCI UEFI-locked by mistake; CG-locked instance that must be rolled back) is only remediable by terminate-and-relaunch. For a principal scoped to `RunInstances`+`ModifyInstanceAttribute` but **not** `TerminateInstances`, the bad state is unrecoverable by that principal; for any automation that reasons about CG/HVCI via the control plane, the ratchet is invisible. This is the Lens-AA lifecycle shape the bundle plan did not develop (it listed instance-type exclusions as out-of-scope "capability gaps").
**High-level Test Scenarios:**
- Confirm from docs that no EC2 API disables NitroTPM or a UEFI-locked HVCI/CG state (done); enumerate what a `CreateReplaceRootVolumeTask` or AMI re-register can and cannot undo (cross-ref `nitrotpm-instance`/`working-with-isolated-amis` plans).
- Model the "stuck instance" scenario: principal with launch+modify but not terminate, instance in UEFI-locked HVCI state — show there is no self-service path back.
- Confirm the irreversible state produces no CloudTrail/console signal (ties to §5.1).
**Breach oracle:** an irreversible security-posture state reachable by a principal who cannot undo it and that no AWS surface reports. **Severity-if-true:** Low–Medium (availability/manageability + assurance-visibility, not confidentiality). **Stop:** once the no-off-switch + no-visibility facts are confirmed.

### 5.4 Lens C / T / S — CG-boundary side channels, re-scoped with CORRECTED IAM facts
**Background & CORRECTION:** the bundle plan (§4 table, §5.4, §8) repeatedly states `GetPasswordData`/`GetInstanceTpmEkPub`/`GetInstanceUefiData`/`ModifyInstanceAttribute` have "**no condition keys**." **This is wrong.** The `list_ec2` audit shows all four carry the full generic instance-attribute key set — **including `aws:ResourceTag/${TagKey}` and `ec2:ResourceTag/${TagKey}`, `ec2:InstanceID`, `ec2:Region`, metadata-options keys, `ec2:Tenancy`, etc.** `ModifyInstanceAttribute` additionally has `ec2:Attribute` and `ec2:Attribute/${AttributeName}`. What they lack is any *action-specific* or *CG/VBS/password-reason* key — not keys outright.
**Security Concern (re-scoped):**
- The bundle plan's §5.4 conclusion ("a customer cannot write a tag/ABAC-scoped policy to further restrict them beyond resource-level ARN matching") is **false** — `aws:ResourceTag` ABAC *is* available. The real, narrower finding: a customer **can** tag-scope these reads, but there is **no condition key tying the read to CG/attestation state** — so even a perfectly tag-scoped `GetPasswordData` still returns the API-vended initial admin credential, which lives entirely **outside** CG's "in-OS-memory extraction" boundary. CG's guarantee and the password-vending API are orthogonal; a reader must not conflate "credentials can't be extracted from OS memory" with "credentials can't be obtained."
- Positive hardening note worth surfacing: because `ec2:Attribute/${AttributeName}` *does* exist, the bundle plan's top lead (§5.1 `userData` rewrite → SYSTEM) **is** IAM-mitigable (`Deny` on `ModifyInstanceAttribute` where `ec2:Attribute/${AttributeName}` = `userData`). The bundle plan missed this because it believed the action was keyless.
**High-level Test Scenarios:**
- Verify the corrected key sets against live `list_ec2` (re-grep by action name) before citing; patch the bundle plan's §4/§5.4/§8 accordingly (done in this cycle — see §8 of the bundle plan now cross-referenced).
- Build the `ec2:Attribute/${AttributeName}=userData` deny and confirm it blocks the §5.1 privesc while permitting other attribute edits.
- Confirm `GetPasswordData` returns the initial credential regardless of CG state (documentation already implies this via `connect-rdp.md`).
**Breach oracle:** a policy author who believes `aws:ResourceTag` is unavailable (per the stale bundle claim) and therefore over-grants, OR conflation of CG's boundary with the credential-vending APIs. **Severity-if-true:** Low/Informational as a scope-clarification + doc-accuracy fix; the `ec2:Attribute` mitigation discovery is a positive hardening result. **Stop:** once corrected and the mitigation confirmed.

### 5.5 Lens U — Secure Boot root-of-trust is image-owner-chosen (pointer to attestation cluster)
**Background:** CG's prerequisite is an AMI with UEFI Secure Boot; `how-uefi-secure-boot-works.md` + `create-ami-with-uefi-secure-boot.md` show PK/KEK/db/dbx are **customer/image-owner-generated** and installable via `register-image --uefi-data <blob>`; in `SetupMode` "all key variables can be updated without a cryptographic signature." A new AMI copy that alters `UefiData` can even **disable** Secure Boot (`launch-instance-with-uefi-sb.md`).
**Security Concern:** CG inherits a trust root that is only as strong as whoever controls image registration. Self-signed, attacker-owned Secure Boot keys are fully supported by the documented API, so "UEFI Secure Boot enabled" on a CG prerequisite says nothing about *whose* keys. This is **owned by `nitrotpm-attestation-*` and the UEFI-Secure-Boot pages** — included here only so a CG hunter does not treat "Secure Boot = trustworthy boot chain" as given. **Do not re-derive; cross-reference.**
**Severity-if-true:** see attestation plans (there the PCR7-cert-pinning / stale-trust leads live). **Stop:** immediately — pointer only.

---

## 6. Threat Model Test Objectives (net-new rows)

| Threat/Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Forge "CG Running" in-guest while LSA extractable | Guest msinfo32/WMI/registry | None — in-guest self-report is the only source |
| KMS/verifier releases to a booted-but-CG-off instance | NitroTPM attestation + CG | Attestation measures boot/firmware only; CG not in any PCR |
| Allowlist SCP admits excluded `*.48xlarge` via family glob | `ec2:InstanceType` on RunInstances | Flat string match; no capability predicate; no CG filter/field |
| Unrecoverable UEFI-locked HVCI/CG state | Instance lifecycle | No control-plane disable; terminate+relaunch only |
| Over-grant from believing reads are condition-keyless | IAM policy | `aws:ResourceTag` ABAC *is* available (corrects bundle plan) |
| `userData`-rewrite privesc blocked by attribute key | ModifyInstanceAttribute | `ec2:Attribute/${AttributeName}=userData` deny (newly identified mitigation) |

## 7. Out-of-Scope / HARD STOP
- Whether a given customer actually enables CG/HVCI inside their guest — shared-responsibility (the AWS-published *steps* are in scope for Lens R via the bundle plan; a customer following them is not).
- Full attestation-document / KMS-condition-key / PCR-semantics internals — owned by `nitrotpm-attestation-*` plans; this plan supplies only the "CG is invisible to attestation" input.
- `resolve:ssm:/aws/service/ami-windows-latest/*` AMI alias — Lens EE null (AWS-exclusive namespace), same as bundle plan §7.
- The in-guest VTL0→VTL1 memory-extraction attack itself (Mimikatz-vs-CG) — a Windows/VBS research question, not an AWS-surface question.
- Any AWS-service-plane identity/credential/ARN encountered in the Nitro/attestation chain — **HARD STOP, preserve, disclose.**

## 8. Null hypotheses / doc gaps (delta over bundle plan §8)
- **Lens W:** no longer a doc-gap. The cross-reference plans the bundle plan called "missing" now exist (`nitrotpm-attestation-attack-research-plan.md` + `-document-content` + `-document-validate`); the CG-specific Lens-W finding (CG is non-attestable / self-asserted, §5.1) is **confirmed from docs**, not deferred.
- **Lens G/F/H/J/K/M/N/P/Q:** null for `credential-guard.html` specifically — same evidence as bundle plan §8 (re-verified; no URL-deref field, no parser/translation layer, no customer-KMS use on this page, no 3P/OAuth, no LLM, no shared-identifier, no namespace-migration, no registration/OTP, no upload).
- **Lens V:** CG itself is in-guest; RDP security-group guidance is customer-owned (`connect-rdp.md`) — no AWS-managed control/storage ENI on this page.
- **Lens EE:** `resolve:ssm` alias refuted (AWS namespace).
- **Carried doc-gap (unchanged):** SSM Patch Manager / `AWSSupport-UpgradeWindowsAWSDrivers` runbook IAM internals live outside the EC2 mirror — bundle plan §5.5 stub still open.
- **Open follow-on:** whether any Windows Server AMI release note or the Windows AMI Reference recommends a compensating control when HVCI is disabled for CG (not checked here; bundle plan §5.3 flags the trade-off, neither plan found a compensating-control recommendation).

---
*Companion to `ec2-windows-credential-guard-attack-research-plan.md` (bundle) and the `nitrotpm-attestation-*` cluster. Downstream: `aws-vuln-hunter`.*
