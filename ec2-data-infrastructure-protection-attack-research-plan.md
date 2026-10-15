# EC2 Data Protection + Infrastructure Security + Resilience — Attack Research Plan

Scope: child cluster of [EC2 Security](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html) —
`data-protection.md`, `infrastructure-security.md`, `disaster-recovery-resiliency.md`, and their linked children
(EBS encryption family, NitroTPM/attestation, Nitro isolation claims). Documentation-only research, built per the
`security-questionbuilder` skill's six-step method. No live account was touched. EC2 networking (ENI/IP/EIP/placement/EFA)
is **out of scope here by design** — see `/work/aws-docs/ec2-networking-attack-research-plan.md` for that depth; this
plan only pulls in `infrastructure-security.md`'s network-traffic-control section as a trust-boundary citation, not a
re-derivation.

Base dir: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`. Authoritative IAM: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` and `list_kms.md` (trusted over prose per skill discipline).

---

## 0. How to use this document

Each item in Section 5 ("Recommended Areas of Focus") is a falsifiable claim with a doc-cited mechanism and a
concrete confirm/refute oracle. A hunter with live-account access executes the oracle; a reviewer without one can
still rank items by Severity-if-true. Section 6 is the master test-objective table. Section 7 lists what this plan
explicitly refuses to test (and why). Section 8 records null hypotheses (with pages checked) and doc gaps carried
forward — treat these as *open*, not closed, per the skill's discipline that an unexamined surface is a miss, not a
null result.

## 1. Pentest Objectives

1. Determine whether EBS/instance encryption-at-rest guarantees are **enforced at the mechanism** the docs claim
   (KMS key state, Nitro hardware data-key custody, encryption-by-default scope) or merely **advisory/console-level**.
2. Determine whether IAM condition keys actually let a customer **restrict which CMK** is used at the exact API calls
   that accept a `KmsKeyId` parameter (RunInstances, CopySnapshot, CreateVolume) — or whether there is a gap between
   "the parameter exists" and "the condition key to gate it exists."
3. Determine whether "encrypted," "isolated by the Nitro System," and "zero operator access" claims in
   `infrastructure-security.md` / `isolate-data-operators.md` map to a customer-observable, API-verifiable control, or
   are unfalsifiable-from-inside-the-account claims about AWS's own infrastructure (Lens U boundary with hardware).
4. Determine whether the NitroTPM attestation trust chain (Attestation Document → KMS `kms:RecipientAttestation:*`
   condition keys) has verification steps whose documented relaxations (e.g., disabled revocation checking) create a
   usable attack path for a party who can obtain or forge PCR values.
5. Determine whether disaster-recovery/resilience mechanisms (cross-Region AMI/snapshot copy, DLM) inherit or break
   the encryption-at-rest guarantees when data crosses Region/account boundaries.

## 2. Components, Assets, and Design

**Customer-facing interfaces:** EC2 API (RunInstances, CreateVolume, CreateSnapshot, CopySnapshot, CopyImage,
DescribeInstanceTypes), EBS direct APIs (StartSnapshot et al.), KMS API (Decrypt, GenerateDataKeyWithoutPlaintext,
CreateGrant, ReEncrypt), EC2 console "Data protection and security" settings tab, NitroTPM/vTPM device exposed inside
the guest, Attestation Document consumer (customer-run or third-party KMS-compatible verifier).

**Assets:**
- Plaintext EBS/instance-store data (at rest and the in-flight data key).
- The KMS data key, wrapped under a CMK, cached **in plaintext inside Nitro hardware memory** for the lifetime of
  volume attachment.
- The CMK itself (AWS managed `aws/ebs` or customer managed) and its key policy / grants.
- The Attestation Document and the PCR measurements it asserts.
- Default-KMS-key account/Region setting (`EbsEncryptionByDefault`, `EbsDefaultKmsKeyId`).
- Cross-Region/cross-account copies of snapshots/AMIs (re-encryption boundary).

**Processes/hosts:** EBS control plane (per Region), Nitro hardware/hypervisor on the host (holds the plaintext data
key while attached), KMS (CMK custody + grant/decrypt API), identity-only EC2 IAM roles
(`arn:{partition}:iam::{account}:role/aws:ec2-infrastructure/{instance_id}`) used by the instance to call KMS on the
customer's behalf.

**Pipeline (encrypt-on-create path, from `how-ebs-encryption-works.md` + `services-ebs.md`):**

```
Customer: CreateVolume/CreateSnapshot(KmsKeyId?, Encrypted?)
        │
        ▼
EC2/EBS control plane --GenerateDataKeyWithoutPlaintext(EncryptionContext={"aws:ebs:id": <vol|snap-id>})--> KMS
        │                                                                     │
        │   <-- wrapped data key (ciphertext blob) --------------------------┘
        ▼
Nitro hardware on host:  CreateGrant + Decrypt(ciphertext, same EncryptionContext) --> KMS
        │                                                                     │
        │   <-- plaintext data key (cached in Nitro HW memory while attached)┘
        ▼
Disk I/O encrypted/decrypted locally using cached plaintext data key
        │
        ▼
On detach: Nitro removes cached plaintext data key from hardware memory
           (CMK disable/delete has NO effect on an already-attached, running volume
            until the next detach — see Lead #1 below)
```

**Resilience path:** AMI/snapshot copy across Region or account re-runs the same `GenerateDataKeyWithoutPlaintext`
step under the *target* key (own default key if the destination doesn't own the source CMK) — see `AMIEncryption.md`.

## 3. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Customer IAM principal | KMS CMK custody | `kms:Decrypt`/`kms:GenerateDataKeyWithoutPlaintext` via identity-only EC2 instance role, gated by key policy + `kms:ViaService=ec2.<region>.amazonaws.com` | A principal without key-policy grant obtains a usable plaintext data key, or an instance role is usable outside the `ec2` service context despite `kms:ViaService` |
| Account A (CMK owner) | Account B (shared AMI/snapshot consumer) | `ModifySnapshotAttribute`/shared AMI restore; Account B's default key re-encrypts | Account B's restored volume is encrypted under a key that is *not* a key Account B's policy actually controls, or Account A's CMK remains independently reachable from Account B's resource post-copy |
| Running instance (attached volume) | KMS CMK lifecycle (disable/schedule-deletion) | CMK state change by key owner, intended as a kill-switch | Volume I/O continues to succeed after CMK is disabled/pending-deletion, because the plaintext data key already resides in Nitro HW memory (confirmed, see Lead #1) |
| Caller of RunInstances/CopySnapshot with `KmsKeyId` parameter | IAM policy evaluation | Action's own condition-key set (list_ec2.md) | Policy intended to restrict "only CMK X may be used" is unenforceable at RunInstances/CopySnapshot because `ec2:KmsKeyId` is absent from their condition-key sets (confirmed, see Lead #3) |
| Third-party/customer Attestation Document verifier | KMS attestation-gated CMK (`kms:RecipientAttestation:*`) | Validate COSE-signed Attestation Document, chase AWS Nitro root cert chain | Verifier accepts a document whose signing certificate has been revoked, because AWS's own sample code disables CRL checking (confirmed, see Lead #2) |
| EC2 control plane / DescribeInstanceTypes caller | Marketing/doc capability claim ("always-on memory encryption") | No corresponding API field | No API call can confirm or deny the claim for a given running instance — the claim is unfalsifiable from the account side (see Lead #4) |
| Customer account, Region without encryption-by-default enabled | Customer account, Local Zone/Outposts/Wavelength Zone | Same account, different enforcement regime (opt-in vs mandatory) | A customer who believes "my account has sane encryption defaults everywhere" is wrong in ordinary Regions unless they explicitly opted in — the posture is non-uniform across an account (see Lead #5) |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| RunInstances | API | Existing | Mutating | External | Launch instance, optionally create encrypted EBS volumes | Yes (SigV4) | Any principal with `ec2:RunInstances` | `KmsKeyId` block param present; **no `ec2:KmsKeyId` condition key** on its volume resource (list_ec2.md L9585-9614) |
| CreateVolume | API | Existing | Mutating | External | Create standalone EBS volume | Yes | `ec2:CreateVolume` | `ec2:KmsKeyId` condition key **present** (list_ec2.md L5122) — contrast case |
| CreateSnapshot | API | Existing | Mutating | External | Snapshot a volume | Yes | `ec2:CreateSnapshot` | `ec2:Encrypted` present; encryption context = volume ID |
| CopySnapshot | API | Existing | Mutating | External | Copy snapshot, optionally re-encrypt under new CMK | Yes | `ec2:CopySnapshot` | **No `ec2:KmsKeyId` condition key** (list_ec2.md L4999) despite accepting `KmsKeyId` param |
| CopyImage | API | Existing | Mutating | External | Copy AMI, re-encrypts backing snapshots | Yes | `ec2:CopyImage` | See `AMIEncryption.md` outcome tables |
| ModifySnapshotAttribute / ModifyImageAttribute | API | Existing | Mutating | External | Share resource cross-account | Yes | Resource owner | Public share blocked for encrypted snapshots; private share to specific accounts allowed |
| EnableEbsEncryptionByDefault / DisableEbsEncryptionByDefault | API | Existing | Mutating | External | Toggle Region-wide EBS default-encryption posture | Yes | `ec2:EnableEbsEncryptionByDefault` etc. | Region-scoped; "has no effect on existing resources" |
| ModifyEbsDefaultKmsKeyId | API | Existing | Mutating | External | Change the account/Region default CMK | Yes | `ec2:ModifyEbsDefaultKmsKeyId` | Changes only apply going forward |
| DescribeInstanceTypes | API | Existing | Non-mutating | External | Query instance-type capability metadata | Yes | Any | Has `ebs-info.encryption-support`, `network-info.encryption-in-transit-supported` filters; **no memory-encryption field** |
| KMS Decrypt / GenerateDataKeyWithoutPlaintext / CreateGrant / ReEncrypt | API | Existing | Mutating | Internal (invoked by EC2/EBS control plane + Nitro HW, not directly by customer in the EBS flow) | Data-key lifecycle | No (service-to-service, SigV4 internally) | EC2 identity-only instance roles, EBS service principal | `kms:ViaService`, `kms:EncryptionContext:aws:ebs:id`, `kms:RecipientAttestation:*` condition keys available |
| NitroTPM Attestation Document retrieval (in-guest) | vTPM/hypervisor call | Existing | Non-mutating | Internal to guest | Produces CBOR/COSE-signed measurement doc | No (guest-local) | Guest OS/attestation agent | Validation guidance explicitly disables CRL (nitrotpm-attestation-document-validate.md L149) |

## 5. Recommended Areas of Focus (Lens Sweep)

### Lens U — Documented guarantee vs. enforcement [FIRES — top severity]

**Background:** `how-ebs-encryption-works.md` states that EC2 uses the **data key**, not the KMS key, to encrypt
disk I/O for an attached volume, and that disabling/deleting the KMS key "has no immediate effect on the EC2 instance
or the attached EBS volumes" — the data key is only purged from Nitro hardware memory **on detach**.

**Security Concern:** Any customer runbook, compliance control, or incident-response procedure that treats
"disable/delete the KMS key" as an immediate access-revocation lever for data on a running, attached volume is wrong.
An attacker who has already obtained the plaintext data key's effect (i.e., is reading/writing through the attached
instance) is unaffected by the key being disabled. Likewise, a "break glass" revocation story told to auditors
("we disabled the key, so the data is now inaccessible") is false while the volume stays attached.

**High-level Test Scenarios:**
1. Attach an encrypted volume, confirm I/O works; disable the backing CMK; confirm I/O to the *already-attached*
   volume continues to succeed (read + write) — oracle: I/O succeeds post-disable.
2. Repeat with `ScheduleKeyDeletion`; confirm same result until actual deletion completes.
3. Attempt to attach the *same* volume to a **second** instance after the CMK is disabled — expect this new grant
   path to fail (new Decrypt call needed), establishing the exact boundary (detach/new-attach vs. steady-state).
4. Check whether CloudTrail/EventBridge surfaces a customer-visible signal that "your disabled key is still backing
   live I/O," or whether this is silent.

**Doc evidence:** `/work/aws-docs/docs/ebs/latest/userguide/how-ebs-encryption-works.md` lines 58-68.

**Severity-if-true:** High — this is a security-control-expectation gap (not a bypass of a stated boundary, since
AWS does disclose it), but it directly undermines a common incident-response assumption; worth a clear writeup
distinguishing "documented, but counter to users' mental model" from "undocumented."

---

### Lens W — Attestation-conditioned authorization [FIRES — novel finding]

**Background:** `nitrotpm-attestation-document-validate.md` gives sample Java validation code for the Nitro
Attestation Document chain and explicitly instructs: *"Note: CRL must be disabled when doing the validation"*
(line 149), followed by `validationParameters.setRevocationEnabled(false);`.

**Security Concern:** `kms:RecipientAttestation:*` condition keys let a key owner gate `Decrypt`/`GenerateDataKey*`
on specific PCR values / image hash measurements presented in the Attestation Document. If a third-party verifier
(or a customer rolling their own attestation-gated KMS integration) follows AWS's own published sample code verbatim,
they inherit a validation path that does not check certificate revocation. If any certificate in the Nitro
attestation PKI chain is ever revoked (compromised intermediate, decommissioned signing cert), a verifier built per
this guidance would still accept documents chained to it.

**High-level Test Scenarios:**
1. Confirm (via docs only, since this requires AWS's own CA infrastructure to test live) whether AWS publishes a CRL
   or OCSP endpoint for the Nitro attestation PKI at all — if not, the "disable CRL" instruction is moot and this
   becomes a doc-gap rather than a live gap.
2. If a CRL/OCSP endpoint exists, determine whether any AWS-provided SDK/library (aws-nitro-enclaves-cose,
   aws-nitro-enclaves-nsm-api, etc.) performs revocation checking by default, or whether every official sample
   disables it the same way.
3. Flag to the hunter: this is a "test the guidance, not the live boundary" lead — the actionable test is auditing
   whatever attestation-verification code a target customer/service actually ships (if in scope) for whether it
   copied this exact disablement.

**Doc evidence:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/nitrotpm-attestation-document-validate.md` line 149 +
surrounding code sample; root cert fingerprint
`64:1A:03:21:A3:E2:44:EF:E4:56:46:31:95:D6:06:31:7E:D7:CD:CC:3C:17:56:E0:98:93:F3:C6:8F:79:BB:5B` given on the same page.

**Severity-if-true:** Medium-High, conditional — severity depends entirely on whether AWS's Nitro attestation PKI
ever actually revokes certs in practice. If it never does, this is a latent/theoretical gap. If it does (e.g., for
compromised signing infrastructure), any verifier following this guidance is blind to it. Mark as **doc-gap**: no
page in scope confirms whether a CRL/OCSP distribution point is actually published for this chain — confirm that
first.

---

### Lens S — Condition-key scoping semantics (CMK restriction gap) [FIRES]

**Background:** `list_ec2.md` shows `ec2:KmsKeyId` present as a condition key on `CreateVolume` (line 5122) but
**absent** from `CopySnapshot` (line 4999) and from `RunInstances`'s volume resource block (lines 9585-9614), even
though both of the latter accept a `KmsKeyId` request parameter that determines the resulting resource's encryption
key.

**Security Concern:** A customer who writes an IAM policy intending "deny any encryption operation that doesn't use
our approved CMK `arn:...:key/approved-key-id`" using an `ec2:KmsKeyId` condition can enforce it on `CreateVolume`
but **cannot** enforce the equivalent restriction on `RunInstances` (instance launch with inline block-device-mapping
encryption) or on `CopySnapshot` (cross-account/cross-region re-encryption) via EC2-side IAM — the only backstop is
the CMK's own key policy (deny-by-default + explicit grant), which is a different control plane the EC2 policy author
may not be the owner of.

**High-level Test Scenarios:**
1. Write an SCP/IAM policy that denies `ec2:RunInstances` unless `ec2:KmsKeyId` equals the approved key ARN; attempt
   to launch an instance with an inline EBS block device specifying a *different*, non-key-policy-denied CMK — expect
   the policy to **not** block it (because the condition key doesn't exist on this action/resource), confirming the
   gap requires the CMK's own policy as the real enforcement point.
2. Repeat for `CopySnapshot` targeting a disallowed CMK.
3. Cross-check against `kms:ViaService`/key-policy-based mitigations recommended in
   `ebs-encryption-requirements.md` to document the *actual* enforcement path customers must use instead.

**Doc evidence:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (CreateVolume L5122;
CopySnapshot condition keys around L4999; RunInstances resource block L9585-9614).

**Severity-if-true:** Medium — this is a least-privilege/defense-in-depth gap, not a boundary bypass (the CMK key
policy still gates actual key usage), but it means EC2-side IAM policies that look like they enforce "approved CMK
only" are silently incomplete for two of the three primary encryption-setting entry points.

---

### Lens U — Capability-claim vs. API-verifiable surface (memory encryption) [FIRES]

**Background:** `data-protection.md` claims "always-on memory encryption" for Graviton2+, specific Intel Xeon
(Ice Lake/Sapphire Rapids TME), and specific AMD EPYC (Milan/Genoa SME) generations, pointing customers to
`describe-instance-types` only for the unrelated `network-info.encryption-in-transit-supported` filter.
`API_InstanceTypeInfo.md` and `API_MemoryInfo.md` were checked directly: `MemoryInfo` has only `SizeInMiB`; no
`InstanceTypeInfo` field names memory encryption at all (only `NitroEnclavesSupport` / `NitroTpmSupport` exist, which
are different features).

**Security Concern:** A customer (or compliance auditor) cannot programmatically verify, for a given running
instance type at a given moment, whether memory encryption is actually active — they must trust the static processor
family/generation claim in prose documentation, with no API cross-check equivalent to the EBS/network filters AWS
*does* provide for other encryption claims. If AWS silently narrows or changes the processor list, or if a given
instance type's documentation is wrong/stale, there is no way to detect the discrepancy from the API surface.

**High-level Test Scenarios:**
1. Enumerate `DescribeInstanceTypes` output for a sample of instance types named in the memory-encryption list and
   confirm no field corroborates the claim (expected: confirmed by doc read already — convert to a live check by
   diffing full API response schema against the claim list).
2. Check whether any other AWS doc (Nitro System whitepaper, Graviton processor page) exposes a verifiable attribute;
   if genuinely nowhere, log as a structural doc-gap, not just an EC2-API gap.

**Doc evidence:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/data-protection.md` lines 47-53;
`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_MemoryInfo.md` (sole field `SizeInMiB`);
`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_InstanceTypeInfo.md` (no memory-encryption field).

**Severity-if-true:** Low-Medium as a standalone finding (no exploitable bypass — it's an observability gap), but
high value as a **documentation-defect** finding: AWS asserts a security property with no corresponding
machine-checkable attribute anywhere in the API surface this plan reviewed.

---

### Lens U — Enforcement-strength non-uniformity (encryption-by-default scope) [FIRES, lower severity / contextual]

**Background:** `encryption-by-default.md`: EBS encryption-by-default is an **opt-in, Region-specific** account
setting (OFF unless the customer enables it) and "has no effect on existing EBS volumes or snapshots" even after
enabling. By contrast, `ebs-encryption-local-zones-outposts-wavelength.md` confirms specific Local Zones and *all*
Outposts/Wavelength Zones have **mandatory** encryption — a customer cannot create an unencrypted resource there
regardless of account settings.

**Security Concern:** "Does this account enforce encryption at rest" has no single answer — it depends on
Region/Zone and on a setting that must be independently enabled per Region and has zero retroactive effect. A
customer audit that checks `GetEbsEncryptionByDefault` in one Region and assumes the finding generalizes account-wide
is wrong, and even a customer with the setting enabled everywhere still has pre-existing unencrypted volumes/snapshots
that the setting never touches.

**High-level Test Scenarios:**
1. Enumerate all Regions' `EbsEncryptionByDefault` state plus check for pre-existing unencrypted volumes/snapshots
   that predate the setting being enabled — oracle: unencrypted resources exist despite "encryption by default: true."
2. Confirm the mandatory-encryption Local Zones/Outposts list is current and complete (cross-check against the
   current Local Zones list, since this is the kind of list that goes stale).

**Doc evidence:** `/work/aws-docs/docs/ebs/latest/userguide/encryption-by-default.md` lines 10, 13;
`/work/aws-docs/docs/ebs/latest/userguide/ebs-encryption-local-zones-outposts-wavelength.md`.

**Severity-if-true:** Low as a bug (fully documented behavior), but worth carrying forward as a **customer-facing
posture-assessment lead** — i.e., the actionable artifact is "build the account-wide encryption posture report AWS
doesn't give you," not a vulnerability in AWS's control.

---

### Lens H — CMK/encryption-context confusion [mechanism checked — confirmed sound, documented for completeness]

**Background:** `services-ebs.md` confirms the `aws:ebs:id` encryption-context key is bound to the exact volume ID
(for CreateSnapshot/volume creation operations) or snapshot ID (for CopySnapshot) on every `GenerateDataKey*`/
`Decrypt` call EBS makes to KMS.

**Security Concern (tested, not found):** The theoretical attack would be: can a wrapped data key blob for volume A
be replayed against KMS with volume B's context to decrypt under a grant scoped to B? Per standard KMS encryption
context semantics (context is authenticated associated data, not merely logged), a mismatched context causes
`Decrypt` to fail. No doc evidence suggests EBS deviates from this. This is a **confirmed-sound** mechanism, not a
lead — recorded per the skill's requirement to show checked work, not just hits.

**Doc evidence:** `/work/aws-docs/docs/kms/latest/developerguide/services-ebs.md`.

**Severity-if-true:** N/A — null result, mechanism holds as documented.

---

### Lens Y — Transport/TLS floor claims [partial fire — cross-reference only]

**Background:** `data-protection.md` line 12: "We require TLS 1.2 and recommend TLS 1.3." `infrastructure-security.md`
repeats a TLS 1.2+/PFS requirement for API endpoints.

**Security Concern:** Whether any EC2-adjacent endpoint (metadata service, legacy SDK paths, non-default endpoints)
actually negotiates below TLS 1.2 contradicting the stated floor is a live-testable claim, but it is **general EC2
network/endpoint surface**, not specific to data-protection/infra-security content beyond the claim itself.

**Disposition:** Flagged but **not expanded here** — this is explicitly the kind of generic transport-security
surface the task instructed this plan not to re-derive; defer to `ec2-networking-attack-research-plan.md` for IMDS/
endpoint-specific TLS testing. Kept here only as a pointer so the claim's source page is on record.

**Doc evidence:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/data-protection.md` line 12.

---

### Lens D / V — Network segmentation / data-plane isolation [out of scope by instruction — pointer only]

`infrastructure-security.md`'s "Controlling network traffic" and "Isolation on physical hosts" sections (hypervisor
CPU/memory isolation, memory scrubbing on stop/terminate, MAC/IP spoofing prevention) are the hub for this lens, but
per task scope this is EC2 networking depth already covered in the existing corpus. The one data-protection-specific
sub-claim worth preserving here: memory scrubbing on stop/terminate is asserted without an API-verifiable attribute
(same structural gap pattern as the memory-encryption lead above) — carried as a doc-gap in Section 8, not expanded
into a full lens writeup to avoid duplicating the networking plan.

**Doc evidence:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/infrastructure-security.md`.

## 6. Threat Model Test Objectives (master table)

| # | Objective | Lens | Oracle | Severity |
|---|---|---|---|---|
| 1 | Confirm attached-volume I/O survives CMK disable/delete until detach | U | I/O succeeds post-disable | High |
| 2 | Confirm/refute whether Nitro attestation PKI publishes a live CRL/OCSP that a "CRL disabled" verifier would miss | W | Revoked-cert doc chain still validates | Medium-High (conditional) |
| 3 | Confirm `ec2:KmsKeyId` condition is unenforceable on RunInstances/CopySnapshot | S | Policy with `ec2:KmsKeyId` deny fails to block disallowed-key launch/copy | Medium |
| 4 | Confirm no API field verifies "always-on memory encryption" claim | U | DescribeInstanceTypes/InstanceTypeInfo schema diff | Low-Medium |
| 5 | Build account-wide encryption-by-default posture report across Regions + flag pre-existing unencrypted resources | U | Unencrypted resources found despite default-on | Low (posture) |
| 6 | Verify `aws:ebs:id` encryption-context binding resists cross-resource replay | H | Decrypt fails on context mismatch | Null (confirmed sound) |
| 7 | Cross-Region/account AMI/snapshot copy re-encryption outcome matches `AMIEncryption.md` tables exactly | H | Live outcome diverges from documented table | Medium if divergent |

## 7. Out-of-Scope Risk Categories

- **"Zero operator access" / Nitro hardware isolation itself** (`isolate-data-operators.md`): tracing this claim to
  mechanism bottoms out in AWS's own hardware design and internal access controls — this is a hard stop per the
  shared-responsibility boundary; it cannot be tested from inside a customer account. Any evidence suggesting this
  claim is false would be a disclosure-grade finding handled outside normal pentest flow, not a test objective here.
- **Generic EC2 networking** (SG/NACL reachability, ENI/EIP, placement groups, EFA) — explicitly deferred to
  `/work/aws-docs/ec2-networking-attack-research-plan.md` per task instruction; not re-derived.
- **Physical-layer / inter-AZ encryption claims** ("all traffic between AZs is encrypted") — unfalsifiable from a
  customer account; no customer-observable interface exists to test AWS's backbone encryption.
- **Instance-store hardware module key custody** — "inaccessible to AWS personnel" claim shares the same hard-stop
  character as Nitro zero-operator-access.

## 8. Null Hypotheses and Doc Gaps Carried Forward

- **Lens A (cross-tenant/IDOR):** Checked `data-protection.md`, `ebs-encryption.md`, `encryption-examples.md`,
  `ebsapis-using-encryption.md` for shared/multi-tenant resource-by-ID patterns specific to this cluster. The
  cross-account surface that exists (snapshot/AMI sharing) is already gated by explicit `ModifySnapshotAttribute`/
  `ModifyImageAttribute` share lists, not an ID-guessing surface — no new IDOR trigger found beyond what the
  snapshot/AMI-sharing feature already documents elsewhere. Null for this cluster specifically.
- **Lens T (cross-service secret reachability):** Checked `data-protection.md`, `ebs-encryption-requirements.md`,
  `key-policy-requirements-EBS-encryption.md` — no customer secret/credential is generated and persisted by this
  cluster's mechanisms (KMS CMKs and grants are the only durable artifacts, and they are KMS-native, not stashed in
  SSM/Secrets Manager/S3/tags by EC2). Null.
- **Lens AA (share/revoke lifecycle):** Partially fires but not expanded — `ebs-modifying-snapshot-permissions.md`
  (share with specific accounts) implies a revoke path exists; whether revocation is immediate for a snapshot already
  copied/restored by the grantee was **not checked** (page not read in this pass) — **doc-gap, not null**: read
  `ebs-modifying-snapshot-permissions.md` next before closing this lens.
  the DisasterRecovery/DLM angle on this (does a DLM-automated cross-account copy schedule survive revocation) is
  also unchecked — doc-gap.
- **Lens EE (predictable-name/shadow-resource):** Checked `encryption-by-default.md`,
  `ebs-encryption-requirements.md` for predictable identity-only role ARNs
  (`arn:{partition}:iam::{account_id}:role/aws:ec2-infrastructure/{instance_id}`) — the ARN shape is predictable *by
  design* (that's the point of an identity-only role), and no pre-registration/shadow-resource race was found in the
  docs read. Null for this cluster.
- **Lens FF (token/claims validation confusion):** The one claims-bearing artifact in scope is the NitroTPM
  Attestation Document (COSE-signed CBOR). Validation steps were read in full
  (`nitrotpm-attestation-document-validate.md`); the CRL-disablement issue is captured as Lens W above. No separate
  claims-confusion issue (e.g., algorithm confusion, missing audience check) was found in the documented validation
  steps — but this is a **doc-gap, not a strong null**: the page gives Java sample code, not a formal spec, so a
  deeper review of actual COSE/CBOR parsing libraries used by real verifiers is warranted and out of reach of
  documentation alone.
- **Lens Q (upload validation):** N/A — no blob upload path exists in this cluster (volumes/snapshots are block
  storage, not parsed documents). Checked `data-protection.md`, `ebs-encryption.md`. Null.
- **Lens P (identity proofing/registration gates):** N/A — no onboarding/registration gate exists in this cluster.
  Null.
- **Nitro Enclaves:** No Nitro Enclaves-specific page was found directly under
  `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` in this scope walk (only NitroTPM, not Enclaves, is covered here);
  Enclaves has its own user guide tree not pulled into this pass — **doc-gap**: a dedicated Enclaves attestation/
  isolation pass is a natural follow-on and would likely add directly to the Lens W findings above (Enclaves uses the
  same `kms:RecipientAttestation:*` condition keys).
- **Resilience-specific (Section 1 objective 5):** `disaster-recovery-resiliency.md` itself is thin (24 lines,
  mostly AZ/Region/Auto Scaling background) and does not independently assert new security guarantees beyond pointing
  at AMI/snapshot copy (covered under Lens H/AMIEncryption) and DLM (unchecked in detail — doc-gap: DLM's own policy
  page was not read in this pass; worth checking whether DLM-automated snapshot copies respect the same encryption
  outcome tables or have divergent default behavior).

---

*Written per `security-questionbuilder` skill §6 skeleton. All leads trace to specific lines in the offline mirror
under `/work/aws-docs/docs/`; no live AWS account was accessed to produce this plan.*
