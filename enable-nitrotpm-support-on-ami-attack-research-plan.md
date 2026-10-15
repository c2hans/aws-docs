# Enable a Linux AMI for NitroTPM — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-support-on-ami.html` (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/enable-nitrotpm-support-on-ami.md`), its `RegisterImage` API reference (`API_RegisterImage.md`), the IAM Service Authorization Reference (`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`, 10190 lines), and the UEFI-Secure-Boot / NitroTPM-attestation page cluster. **Online == offline byte-identical, verified 2026-10-15** (target page + `create-ami-with-uefi-secure-boot.md` + `nitrotpm-attestation-document-content.md` twins all match). Status: documentation-derived hypotheses only; nothing tested against a live account.

**Scope / relationship to siblings — this is a page-level COMPLEMENT, not a duplicate.**
- The broad **`nitrotpm-attack-research-plan.md`** (NitroTPM hub) OWNS, at summary level, the headline "`RegisterImage --tpm-support v2.0` enablement is IAM-ungatable *by value*", plus EK retrieval (`GetInstanceTpmEkPub`), whoAMI-on-Windows, BitLocker "original instance only", and cross-account AMI share. This plan **cross-references** those and does NOT restate them.
- **`enable-nitrotpm-prerequisites-attack-research-plan.md`** OWNS the launch-time prerequisites (AMI TpmSupport=v2.0 + UEFI boot + NitroTPM-capable type un-expressible in IAM), the static-instance-type-list drift, the instance-type-change resize gap, and BitLocker/snapshot-can't-carry-NitroTPM. Its Area 4 already cites `enable-nitrotpm-support-on-ami.md:12`. This plan **cross-references** those.
- **`nitrotpm-attestation-attack-research-plan.md`** OWNS the KMS attestation gate / PCR reproducibility / replay / CRL / COSE depth (Lens W). This plan feeds it one net-new upstream primitive (register-time PCR7 control) and otherwise defers.
- Parent: **`ec2-security-attack-research-plan.md`** (EC2 Security chapter hub, NitroTPM = Area 2).

**What THIS page uniquely owns:** the four-step snapshot → `RegisterImage` *enablement runbook itself*, and in particular the **register-time co-parameters the runbook co-locates with (or omits next to) `--tpm-support v2.0`** — `--uefi-data` (the UEFI variable store = Secure Boot root of trust / PCR7 source), `--boot-mode`, and the omitted `--imds-support`. These are the parameters an operator sets *in the same call* that enables the TPM, and none of them is IAM-gatable.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The read-only first oracle for every IAM-scoping lead here is **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — a condition key either applies to an action or it does not; no AMI/snapshot need be created to prove inertness. Escalate to a live `register-image --dry-run` (IAM-only) and then a scoped real call with a canary snapshot only to settle a true behavioral gap.
- **`DryRunOperation` is caller-IAM-only** (evaluated before resource resolution) — it is NOT an ownership/provenance oracle. Do not treat a `DryRunOperation` success on a foreign snapshot id as proof the register would succeed.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. an AWS-fleet-rooted UEFI key, an AWS-side attestation signer), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Author an SCP/identity policy that an org admin would believe forbids (or mandates) NitroTPM/UEFI/IMDS posture on `RegisterImage`, then prove it is inert** — i.e. a `Deny` on `--tpm-support`, `--boot-mode`, `--uefi-data`, or `--imds-support` that never fires because no condition key keys on those request fields.
2. **Register a NitroTPM-enabled, Secure-Boot-"on" AMI whose PCR7 the registrant fully controls** (attacker-chosen PK/KEK/db via `--uefi-data`), and show the resulting attestation document is internally self-consistent — so a measurement-pinning attestation/KMS policy that was NOT pinned to a specific certificate hash accepts an attacker-built AMI.
3. **Build an "attestation-grade" AMI via the exact AWS runbook command and show it ships IMDSv1-allowed** (`HttpTokens=optional`) because the runbook omits `--imds-support v2.0` — an SSRF→credential-theft precondition orthogonal to and unmitigated by the TPM.
4. **Register a `--tpm-support v2.0` AMI from a snapshot the registrant does not own** (shared/public snapshot), and determine whether provenance/ownership of the backing disk is enforced at register time or only the snapshot's existence.
5. Confirm the **immutability + console-invisibility** of the TpmSupport attribute compounds all of the above (silent, un-auditable-via-console state).

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** NitroTPM for a *Linux* AMI is enabled exactly once, at AMI registration, through a single control-plane call. The runbook is purely client-side orchestration around that call:

```
[1] RunInstances(any Linux AMI)         ← temp instance, caller account
        │
        ▼
[2] CreateSnapshot(root EBS volume)      ← snapshot, caller account (or a snapshot
        │                                   shared-in / public — see Area 4)
        ▼
[3] RegisterImage                        ← THE enablement step. image* resource minted in caller acct.
      --tpm-support v2.0   ◄── enables NitroTPM 2.0   (immutable, no later change)
      --boot-mode uefi     ◄── hard NitroTPM prereq
      --uefi-data <b64>    ◄── (OPTIONAL, runbook omits) UEFI variable store = PK/KEK/db/dbx
      --imds-support v2.0  ◄── (OPTIONAL, runbook OMITS) IMDSv2 enforcement on launched instances
      --block-device-mappings …SnapshotId=snap-… ◄── backing root disk
        │
        ▼
[4] TerminateInstances(temp)
```

- **Customer-facing interface:** `RegisterImage` (SDK/CLI `register-image`, PowerShell `Register-EC2Image`). **Not** console, **not** VM Import/Export (target page line 12 — console/VM-I/E cannot set TpmSupport).
- **Resource & identifier shape:** output `image/ami-…` (newly minted, owned by caller). Backing `snapshot/snap-…` is an input, optionally foreign. No cross-tenant resource is *read-by-id* here — RegisterImage creates.
- **Identity:** SigV4 IAM principal calling `ec2:RegisterImage` (+ `ec2:CreateTags` if `TagSpecification` used; the action detail row at `list_ec2.md:4214-4216` pairs `ec2:CreateTags` with `ec2:RegisterImage`).
- **The asset that matters:** the resulting AMI's **UEFI variable store (Secure Boot policy, PCR7 source)** and its **TpmSupport flag** — these become the measured-boot root of trust for every instance launched from the AMI, and feed any NitroTPM attestation an attestation/KMS consumer later evaluates.
- **Untrusted-data-in transform:** `--uefi-data` is a caller-supplied base64 binary variable-store blob (built offline with the third-party `awslabs/python-uefivars` tool), stored verbatim; `--tpm-support`/`--boot-mode`/`--imds-support` are enum request fields. The transform of interest is register-time attacker input → the measured boot state an *attestation consumer in another account* later trusts.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Org admin's intended IAM/SCP control | `RegisterImage` request fields (`tpm-support`/`boot-mode`/`uefi-data`/`imds-support`) | IAM policy evaluation at register time | A `Deny`/`Allow` condition the admin writes against any of these fields is **inert** (no matching condition key) → the posture is set at caller discretion. **Settle read-only via SimulateCustomPolicy.** |
| Registrant (AMI author) | Measured-boot state (PCR7) trusted by an attestation/KMS consumer, possibly in another account | `--uefi-data` writes PK/KEK/db/dbx → PCR7 Secure Boot Policy | Registrant supplies attacker-chosen keys, instance boots attacker-signed binaries, attestation document's PCR7 is internally consistent → a consumer policy not pinned to a specific cert hash **accepts the attacker AMI**. |
| Registrant | Backing root disk provenance | `--block-device-mappings SnapshotId=` with a snapshot shared-in/public | Registering `--tpm-support v2.0` from a snapshot the registrant does **not own** succeeds → a "trusted/attestable" AMI minted over foreign-origin disk contents. |
| Operator following the AWS runbook verbatim | Launched instances' IMDS posture | Runbook omits `--imds-support v2.0` | Instances launched from the "attestation-grade" AMI default to `HttpTokens=optional` (IMDSv1) → SSRF→cred-theft precondition, orthogonal to the TPM. |
| Any customer surface | AWS service plane (UEFI key rooting, attestation signer) | — | Any AWS-fleet-rooted key/identity surfacing = **HARD STOP**, preserve + disclose. |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `RegisterImage` | SDK/CLI/PS | **Yes** (creates `image*`) | Yes | Register AMI; sets `TpmSupport`, `BootMode`, `UefiData`, `ImdsSupport`, BDM | Yes (SigV4) | `ec2:RegisterImage` holder | **Only** NitroTPM-Linux enablement path. image\* row keys = `aws:RequestTag`,`aws:TagKeys`,`ec2:ImageID`,`ec2:Owner`,`ec2:Region` (`list_ec2.md:9319-9321`). **No `ec2:BootModeOverride`, no TpmSupport/ImdsSupport/UefiData key anywhere.** |
| `CreateSnapshot` | SDK/CLI | Yes | Yes | Snapshot temp instance root vol | Yes | caller | Runbook step 2. snapshot\* scopable (`ec2:ParentVolume`, tags). |
| `CreateImage` | SDK/CLI | Yes | Yes | EBS-backed AMI from instance in one call | Yes | caller | **Recommended default over RegisterImage** (API ref line 11). Its `image*` row DOES carry `ec2:BootModeOverride` (`list_ec2.md:5144`) — asymmetry vs RegisterImage. **Does `CreateImage` offer a `TpmSupport` path?** It auto-copies the instance's UEFI varstore (per subagent (c)); does it propagate an instance's NitroTPM? → doc-gap, Area 5. |
| `GetInstanceTpmEkPub` | SDK/CLI | No (Read) | Yes | Return per-instance NitroTPM EK | Yes | `instance*`-scoped (`list_ec2.md:8330-8336`) | Cross-ref only — owned by hub plan. |
| `GetInstanceUefiData` | SDK/CLI | No (Read) | Yes | Read instance UEFI varstore | Yes | caller | Confidentiality note: anyone with this perm reads varstore (`uefi-variables.md:12-13`). The read-twin of `--uefi-data` write. |
| `ModifyImageAttribute` / `ModifySnapshotAttribute` | SDK/CLI | Yes | Yes | launchPermission share (`ec2:Add/userId`,`ec2:Add/group`) | Yes | owner | The share path for distributing a `--tpm-support` AMI (hub plan Lens AA). Cross-ref. |
| EC2 console / VM Import-Export | — | — | — | **Cannot** set TpmSupport | — | — | Target page line 12 — enablement is console-invisible both to set AND to inspect. |

Undocumented/console-hidden knob angle: `--uefi-data` and `--imds-support` are API/CLI-only register-time controls with **no console equivalent** on this path; combined with the console's inability to even *display* TpmSupport, the entire security-relevant posture of the AMI is set and visible only via the API.

---

## 5. Recommended Areas of Focus

### Area 1 — Register-time posture is IAM-ungatable: `tpm-support`, `boot-mode`, `uefi-data`, `imds-support` have no condition key (Lens S / U / R) — HEADLINE
**Background.** The runbook's single security-defining call sets four posture fields. `list_ec2.md` RegisterImage `image*` row (lines 9319-9321) carries **only** `aws:RequestTag/${TagKey}`, `aws:TagKeys`, `ec2:ImageID`, `ec2:Owner`, `ec2:Region`. A whole-file grep returns **zero** keys named `TpmSupport`, `NitroTpm`, `ImdsSupport`, or `UefiData`; `ec2:BootModeOverride` (def `list_ec2.md:10059`) exists but is bound to `CreateImage`'s `image*` row (`:5144`) and the generic `image` resource (`:9945`) — it is **absent from RegisterImage's row**. IMDS keys (`ec2:MetadataHttpTokens` etc., def `:10114`) exist only on the `instance` resource, never on `image`.

**Security Concern.** An org that wants to mandate "every registered AMI must enable NitroTPM 2.0 + UEFI + IMDSv2" — or conversely "no team may register a TpmSupport AMI outside the golden pipeline" — **cannot express any of it in EC2 IAM.** A `Deny` written against `ec2:TpmSupport`/`ec2:ImdsSupport`/`ec2:BootModeOverride`-on-RegisterImage is silently vacuous (keys don't exist / don't apply to this action), the single most dangerous failure mode because it reads as a working control. This is the register-time analogue of the prerequisites plan's launch-time Area 1 and the data-protection plan's R6 (`ec2:AmdSevSnp` guessed-key fail-open).

**High-level Test Scenarios.**
- *Claim:* a policy `"Deny" ec2:RegisterImage if ec2:TpmSupport != v2.0` never affects the request. → *Oracle:* `SimulateCustomPolicy` shows the statement does not match (unknown key → not evaluated); a `register-image --tpm-support v2.0 --dry-run` under a role carrying that Deny returns `DryRunOperation`, not `UnauthorizedOperation`. → *Severity-if-true:* Low–Medium, **AWS-owned reportable (Tier-2)** — the absence is in the AWS IAM schema, not a customer artifact.
- *Claim:* `ec2:BootModeOverride` can be used to force `--boot-mode uefi` on RegisterImage the way it can on CreateImage. → *Oracle:* key absent from RegisterImage's row → inert. → confirms the CreateImage-vs-RegisterImage **action-family parity gap** (Lens X): the same conceptual control exists on the sibling create action but not here.
- *Claim:* the one control that DOES work is `ec2:Owner` on the snapshot row (Area 4) and tag-on-create — enumerate what is actually expressible so the hunter knows the real (narrow) boundary.

**Doc evidence:** `list_ec2.md:9319-9321` (RegisterImage keys), `:5144` (CreateImage has BootModeOverride), `:9945` / `:10059` / `:10114`; `API_RegisterImage.md:125-129` (TpmSupport enum, Required:No), `:54-60` (BootMode), `:83-88` (ImdsSupport). **Severity-if-true:** Low–Medium (Tier-2 reportable, AWS-owned schema gap). **Stop condition:** once SimulateCustomPolicy confirms each key is inert, the lead is settled — do not attempt to force the posture by other means.

### Area 2 — `--uefi-data` co-located with `--tpm-support` lets the registrant own PCR7 (Secure Boot policy) of an "attestable" AMI (Lens W / U) — PRIMARY HIGH-VALUE LEAD
**Background.** `RegisterImage` accepts `UefiData` (base64 non-volatile UEFI variable store; `API_RegisterImage.md:131-135`), buildable **offline** with the third-party `awslabs/python-uefivars` tool, in the *same call* that sets `--tpm-support v2.0`. AWS's own procedure `create-ami-with-uefi-secure-boot.md` ("Option B", lines 266-312) walks exactly this: the registrant generates their **own** PK/KEK/db/dbx with `openssl -x509` (arbitrary CN), packs them (`uefivars.py … -O blob.bin -P PK.esl -K KEK.esl --db db.esl --dbx dbx.esl`), and uploads via `register-image --uefi-data …`. `how-uefi-secure-boot-works.md:32-35`: "By default, UEFI Secure Boot is disabled and the system is in `SetupMode`… all key variables can be updated without a cryptographic signature. When the PK is set, UEFI Secure Boot is enabled." → **the first writer of PK owns the chain of trust**, and at register time that is the registrant.

**Security Concern.** `nitrotpm-attestation-document-content.md:8-29`: "PCR4, PCR7, and PCR12 specifically are used to validate that an instance was launched using an Attestable AMI… **PCR7 (Secure Boot Policy)**… contains a hash of the instance's UEFI Secure Boot policy" — i.e. a hash of exactly the PK/KEK/db/dbx the registrant supplied via `--uefi-data`. PCR0/PCR1 are AWS-controlled constants; **PCR7 is attacker-steerable.** AWS's own doc states the consequence verbatim: "During creation of an Attestable AMI, you can… sign the boot binary with your certificate and install it as the only permitted certificate in the AMI's UEFI-data… this model requires you to still generate a new certificate… and update AMIs if you want to prevent instances launched from old (**untrusted**) AMIs from passing your KMS policy." And `nitrotpm-attestation.md:8-29` describes attestation purely as **measurement comparison with a caller-supplied KMS keypair** — there is **no AMI-owner / account / provenance field anywhere in the attestation document contents** → **attestation binds boot measurements, not caller identity.**

**Composed concern (the kill chain):** a registrant who can call `RegisterImage` builds a NitroTPM-enabled AMI with (a) `--tpm-support v2.0`, (b) `--uefi-data` carrying attacker-chosen PK/db so attacker-signed bootloaders pass Secure Boot, producing (c) an internally-consistent PCR7. Because attestation is measurement-only and PCR7 is attacker-chosen, **any attestation/KMS consumer policy that was written to require "Secure Boot on" / "PCR7 present" but did NOT pin a specific trusted certificate-hash value accepts the attacker's AMI** — the attacker's enclave/instance decrypts the gated secret. This is the register-time *source* of the attestation plan's PCR-reproducibility concern; this plan owns the primitive, the attestation plan owns the KMS-gate exploitation.

**High-level Test Scenarios.**
- *Claim:* RegisterImage accepts `--uefi-data` **and** `--tpm-support v2.0` together with no mutual-exclusion and no content validation. → *Oracle:* register with both set; AMI created; `verify-nitrotpm-support-on-ami` + `GetInstanceUefiData`/attestation on a launched instance shows attacker keys active and TPM enabled. → **Severity: High** (foundation for a cross-account attestation-gate bypass).
- *Claim:* there is **no integrity/authenticity check** on `--uefi-data` at register time (no signature, no AWS/Microsoft-root requirement; stored verbatim). → *Oracle:* register with a self-signed PK/db chain (arbitrary CN) and a malformed/oversized varstore; observe acceptance / error behavior. **Doc-gap:** no page states any check — absence of a stated check ≠ proof of none, confirm live. → High if accepted.
- *Claim:* a consumer attestation/KMS policy keyed on `NitroTPMPCR7` *existence* or a wildcard rather than a pinned hash accepts the attacker PCR7. → hand off the KMS-gate half to `nitrotpm-attestation-attack-research-plan.md` (Lens W fail-open scenarios); this plan proves only that the attacker controls the PCR7 input.

**Doc evidence:** `API_RegisterImage.md:131-135`; `create-ami-with-uefi-secure-boot.md:266-312`; `how-uefi-secure-boot-works.md:32-35`; `nitrotpm-attestation-document-content.md:8-29`; `nitrotpm-attestation.md:8-29`; `uefi-variables.md:12-13` (confidentiality note, not integrity). **Severity-if-true:** High (register-time primitive); **Critical** if the downstream KMS gate is cross-account and un-pinned (chain end — rate at the end). **Stop condition:** once attacker-chosen PCR7 is demonstrated in an attestation document, STOP — do not pursue the actual cross-account secret; preserve evidence and route the KMS half to the attestation plan / disclosure.

### Area 3 — AWS runbook omits `--imds-support v2.0` → "attestation-grade" AMI ships IMDSv1-allowed (Lens R / U)
**Background.** The target page's example `register-image` command sets `--tpm-support v2.0 --boot-mode uefi` but **not** `--imds-support v2.0`. IMDS posture precedence is launch-setting > account-setting > **AMI setting** (`configuring-instance-metadata-options.md:43-46`). With no `ImdsSupport` on the AMI (and absent an account-level `required` default, which AWS does not pre-set), launched instances resolve to **`HttpTokens=optional` = IMDSv1 allowed** (`configuring-IMDS-new-instances.md:67/75` "otherwise it defaults to `1`"; `instance-metadata-transition-to-version-2.md:30` "IMDSv1 enabled (`httpTokens = optional`)").

**Security Concern.** The operator is building a *security-hardened, measured-boot, attestation-grade* image by following an AWS-authored runbook — and that runbook silently leaves the single most impactful instance-metadata hardening (IMDSv2) off. The resulting box is the classic SSRF→IMDSv1→role-credential-theft target, entirely orthogonal to and unmitigated by the NitroTPM the operator just enabled. This is a Lens-R insecure-default in an **AWS-published copy-verbatim runbook** (in scope, Tier-2), the register-time twin of the EC2-Security IAM child's `MetadataOptions.HttpTokens:"optional"` sample-code finding.

**High-level Test Scenarios.**
- *Claim:* an AMI registered with the page's exact command, launched in an account with default IMDS settings, yields `HttpTokens=optional`. → *Oracle:* `register-image` per runbook → `run-instances` → `describe-instances … MetadataOptions.HttpTokens` = `optional`. → **Severity: Medium (High in a role-bearing fleet)**, AWS-owned (runbook defect).
- *Claim:* the omission cannot be back-stopped by IAM on RegisterImage (ties Area 1) — no `ec2:MetadataHttpTokens` key on the `image` row to force `imds-support` at register. → *Oracle:* SimulateCustomPolicy.
- *Adjacent:* does the runbook anywhere warn to also pass `--imds-support`? (It does not — the omission is unflagged.)

**Doc evidence:** target page example block; `configuring-instance-metadata-options.md:35,43-46`; `configuring-IMDS-new-instances.md:67/75`; `instance-metadata-transition-to-version-2.md:30`; `API_RegisterImage.md:83-88`. **Severity-if-true:** Medium–High (Tier-2 reportable). **Stop condition:** confirming the default `optional` settles the doc defect; do not weaponize the IMDSv1 box further.

### Area 4 — Register `--tpm-support v2.0` from a snapshot you don't own? (Lens A provenance / U)
**Background.** RegisterImage's `snapshot` resource row is **non-required** (not asterisked: `list_ec2.md:9322` lists `snapshot`, not `snapshot*`) and carries `ec2:Owner` among its keys. The runbook assumes a self-made snapshot, but the API accepts any `SnapshotId` in the block device mapping. Shared/public EBS snapshots are launchable by non-owners; the docs never state whether `RegisterImage` requires the backing snapshot to be caller-owned.

**Security Concern.** If a registrant can set `--tpm-support v2.0` on an AMI backed by a **snapshot shared-in or public from another account**, they mint a "NitroTPM-enabled / attestable" AMI over disk contents whose provenance is foreign — laundering arbitrary (possibly backdoored) disk state into an image that *looks* trustworthy and self-attests (feeds Area 2). Conversely, `ec2:Owner` on the snapshot row IS the one real positive control: an admin *can* scope "only register from snapshots my account owns" — worth documenting as the boundary that actually holds.

**High-level Test Scenarios.**
- *Claim:* `register-image --tpm-support v2.0 --block-device-mappings …SnapshotId=<foreign-shared-snap>` succeeds. → *Oracle:* two-account canary: owner shares a snapshot to the registrant; registrant registers with TpmSupport; AMI created? (Remember: `--dry-run` is caller-IAM-only and will NOT answer provenance — must do the real register with a canary snapshot.) → **Severity: Medium** (provenance-laundering; Medium–High if it feeds a cross-account attestation gate via Area 2).
- *Claim:* `ec2:Owner` on the snapshot row correctly blocks a foreign snapshot when an admin scopes it. → *Oracle:* SimulateCustomPolicy + scoped real call — prove the control works (negative-space documentation).

**Doc evidence:** `list_ec2.md:9322` (snapshot row, non-required, `ec2:Owner`); `API_RegisterImage.md:15-19,47-52` (register from snapshot BDM; "If the snapshot is encrypted, or encryption by default is enabled, the root volume… is encrypted" — note it says nothing about ownership). **Severity-if-true:** Medium (Medium–High chained). **Stop condition:** determine owned-vs-foreign behavior once; do not enumerate others' snapshots.

### Area 5 — Immutability + console-invisibility compound every finding (Lens U / O)
**Background.** Target page line 8: "You can't configure NitroTPM support later on"; line 12: "You can't use the Amazon EC2 console or VM Import/Export." TpmSupport is set once, immutable, and invisible in the console (inspectable only via `Describe*`/API — owned by attestation plan Area 7 and prereqs Area 5).

**Security Concern.** A mis-registered posture (Area 2 attacker PCR7, Area 3 IMDSv1, Area 4 foreign-snapshot provenance) is **frozen into the AMI and invisible to a console-only reviewer**. There is no remediation short of deregister+re-register; detection of a maliciously/sloppily built NitroTPM AMI requires API-level audit the console never surfaces. This is a compounding enabler, not a standalone bug.

**High-level Test Scenarios.**
- *Claim:* neither TpmSupport nor the active UEFI Secure Boot keys of an AMI are visible in the EC2 console. → *Oracle:* register, inspect console vs `describe-images`/attestation. → **Severity: Low (enabler).**
- *Open doc-gap:* does `CreateImage` (the AWS-recommended default per `API_RegisterImage.md:11`) offer any NitroTPM propagation — i.e. if you `CreateImage` from a NitroTPM instance, does TpmSupport carry? The docs are silent; if it does, that is a second (console-reachable?) enablement path the hub plan's "RegisterImage is the ONLY enablement path" claim would need to reconcile. Confirm against `API_CreateImage.md` before relying on the single-path assumption.

**Doc evidence:** target page lines 8,12; `API_RegisterImage.md:11`. **Severity-if-true:** Low (enabler) / doc-gap for the CreateImage question.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| SCP/IAM `Deny` on tpm-support/boot-mode/imds-support/uefi-data is inert | RegisterImage IAM eval | *(none — no condition key exists; this IS the finding)* |
| Registrant controls PCR7 via attacker-chosen `--uefi-data` keys on a `--tpm-support v2.0` AMI | UEFI varstore → PCR7 → attestation | "install it as the only permitted certificate… update AMIs… to prevent… untrusted AMIs passing your KMS policy" (`attestation-document-content.md`) — i.e. consumer MUST pin a cert hash |
| No integrity check on `--uefi-data` content at register | RegisterImage | *(doc-gap — no stated validation)* |
| Runbook AMI launches IMDSv1-allowed | AMI ImdsSupport default | `--imds-support v2.0` (runbook omits it); account-level IMDS default = `required` |
| Register `--tpm-support v2.0` from foreign/shared snapshot | RegisterImage snapshot resource | `ec2:Owner` condition key on the snapshot row (admin must set it) |
| Attestation accepts attacker AMI (measurement-only, no identity binding) | NitroTPM attestation + KMS policy | pinned PCR hash values in `kms:RecipientAttestation:NitroTPMPCR7` (→ attestation plan Lens W) |
| Mis-built NitroTPM AMI invisible to console reviewer | Console vs API | API-level (`Describe*`) audit only |

---

## 7. Out-of-Scope / Risk Categories
- **A customer's OWN mis-scoped identity policy** that fails to require NitroTPM — out of scope (customer footgun). In-scope here is only the **AWS schema gap** (no key exists to express it) and the **AWS-authored runbook** omissions (Areas 1, 3).
- **EK retrieval / `GetInstanceTpmEkPub` cross-tenant tracking** — owned by `nitrotpm-attack-research-plan.md` (hub).
- **The KMS attestation-gate fail-open exploitation (wildcard/all-zero/absent PCR)** — owned by `nitrotpm-attestation-attack-research-plan.md` (Lens W). This plan supplies only the register-time PCR7-control primitive.
- **BitLocker "original instance only" / snapshot-can't-carry-NitroTPM data-loss** — owned by prerequisites plan Area 4.
- **Windows `Update-EC2SecureBootCertificate.ps1` plain-S3-download-run-as-admin** — isolated to the Windows AMI reference page (`ami-windows-tpm.md:95,100`); confirmed **no cross-link** to/from the Linux UEFI-SB pages. Owned by the ec2-windows-credential-guard child / prereqs Area 6.
- **Launch-time prerequisites** (NitroTPM-capable instance type, UEFI boot, type-change resize) — prerequisites plan Area 1-3.
- **AWS service-plane UEFI key rooting / attestation signer** — HARD STOP, disclosure.
- Instance-store-backed `ImageLocation` register path, Marketplace billing-product-code propagation — not NitroTPM-relevant to this runbook (noted, not pursued).

---

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens G (SSRF):** NULL. The only "URL-ish" field here is `ImageLocation` (S3 manifest path for instance-store AMIs, requires `aws-exec-read` ACL) — a client-named S3 object, not a server-side-dereferenced attacker URL on the NitroTPM/EBS path. `--uefi-data` is an inline base64 blob, not a fetch. Checked `enable-nitrotpm-support-on-ami.md`, `API_RegisterImage.md`, `create-ami-with-uefi-secure-boot.md`.
- **Lens A (classic cross-tenant IDOR):** NULL for RegisterImage *output* (creates a caller-owned `image/ami-…`; `ami-` ids not read-by-foreign-id here). The provenance variant (register from a foreign *snapshot*) is Area 4 — a provenance test, not resource-read IDOR.
- **Lens Q (upload):** `--uefi-data` is the closest thing to a parsed blob, but it is a UEFI variable store consumed by the guest firmware, not a service-side parser/renderer → routed to Lens W (Area 2), not Q. Checked `uefi-variables.md`, `API_RegisterImage.md`.
- **Lens B/C (PassRole/vending):** NULL — RegisterImage takes no role ARN, assumes no role on the caller's behalf.
- **Lens H (KMS):** register-from-encrypted-snapshot inherits the snapshot's key ("you can't set the encryption state… if the snapshot is encrypted… the root volume is encrypted", `API_RegisterImage.md:17`) — no new KMS key chosen on this path; the copy-path KMS gap is owned by `data-protection-attack-research-plan.md` R2. NULL here.
- **Doc-gaps to confirm before investing:** (1) **UefiData integrity check** at register (Area 2 — no stated validation); (2) **register-from-shared/public-snapshot** ownership enforcement (Area 4 — docs silent); (3) **CreateImage NitroTPM propagation** (Area 5 — does the AWS-recommended default action carry TpmSupport, challenging the hub's "RegisterImage is the ONLY path" claim?); (4) whether `--uefi-data` and `--tpm-support` have any undocumented mutual-exclusion (subagent found none stated).
- **Byte-identical online==offline confirmed 2026-10-15** for the target page and the two load-bearing Area-2 pages; no drift.

---

*Cross-references: `nitrotpm-attack-research-plan.md` (hub — EK, whoAMI, enablement-by-value summary, AMI share), `enable-nitrotpm-prerequisites-attack-research-plan.md` (launch prereqs, BitLocker/snapshot, Secure-Boot .ps1), `nitrotpm-attestation-attack-research-plan.md` (KMS gate / Lens W — consumes Area 2's PCR7 primitive), `ec2-security-attack-research-plan.md` (parent hub), `data-protection-attack-research-plan.md` (copy-path KMS). See reference `list_ec2` as authoritative over User-Guide prose.*
