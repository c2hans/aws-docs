# Security Research Plan — NitroTPM for Amazon EC2 (skill-agent output)

**Skill run:** `security-questionbuilder` (single pass).
**Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html
**Run date:** 2026-09-02.
**Documentation is the input; nothing here was tested against a live AWS account.**

## Provenance & currency
- **Sources read (offline mirror + live confirmation):** `nitrotpm.md`, `nitrotpm-attestation.md`, `nitrotpm-attestation-document-content.md`, `nitrotpm-attestation-document-validate.md`, `nitrotpm-instance.md`, `enable-nitrotpm-prerequisites.md`, `retrieve-ekpub.md`, `attestation-get-doc.md`, `attestation-attest.md` (all under `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`), and `kms/latest/developerguide/conditions-nitro-tpm.md`.
- **Live cross-check:** `docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html` fetched 2026-09-02 — matches the offline mirror byte-for-byte on headings, Topics list, pricing, and the "See also" block. **No offline/live sync drift.**
- This plan reuses and re-validates the pre-existing, deeper analysis at `/work/aws-docs/nitrotpm-attack-research-plan.md` (224 lines), whose doc-evidence still matches the current pages (including the newer attestation-flow subpages). That file and this one are equivalent deliverables; this file is the self-contained copy for the target page.

## ⚠ SUSPECTED PROMPT INJECTION (untrusted page content, NOT followed)
Every NitroTPM (and the KMS conditions) page carries a "See also → **Skills for AI coding assistants (optional)**" footer instructing the reader to run `aws agent-toolkit search-skills --search-query AWSEC2`. This is untrusted documentation content aimed at AI agents, not a user instruction. It was **ignored** during analysis and **not executed**; recorded here so a downstream agent treats it as data. No AWS CLI / agent-toolkit command was run.

---


**Source of leads:** AWS documentation only — offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` and the live pages under `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/` (nitrotpm*, enable-nitrotpm-*, attestation-*, attestable-ami, build-sample-ami, retrieve-ekpub, verify-nitrotpm-*, isolate-data-operators), `.../APIReference/API_NitroTpmInfo.html`, and `https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html`.
**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Every item below is a boundary that *might not hold* plus the exact observation that would settle it.

> **Note on the docs:** every NitroTPM page carries a boilerplate "Skills for AI coding assistants (optional) … run `aws agent-toolkit search-skills`" footer. This is untrusted page content, not an instruction; it was ignored during analysis and is flagged here as `SUSPECTED PROMPT INJECTION`-style noise for downstream awareness.

---

## 0. How to use this document
- Each lead is: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- The central mental model for NitroTPM: **an Attestation Document proves *which software booted*, signed by AWS's Nitro root of trust — it does NOT prove *who owns the instance* and does NOT prove *runtime* (post-boot) state.** Most high-value leads are specializations of that gap.
- **HARD STOP / service-plane boundary:** the moment evidence implicates AWS's own plane — the Nitro Hypervisor signing key, the Nitro Attestation PKI private key, another instance's NitroTPM internal state, or any cross-instance/cross-tenant Nitro artifact — **stop, preserve evidence, flag for AWS Security disclosure.** Nitro provides documented "zero operator access"; a breach of it is a hard stop, not a lead to escalate.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Forge or replay** an Attestation Document that a verifier (AWS KMS or a third-party verifier) accepts for software the attacker is *not* running → satisfy a PCR-gated KMS policy and obtain `Decrypt`/`GenerateDataKey` output.
2. **Cross-account key access via attestation:** from account B, satisfy account A's NitroTPM-attestation KMS key policy by running the *same* attestable AMI (attestation authenticates code, not tenant).
3. **Weak-PCR policy grant:** prove that a KMS policy pinned to AWS-controlled/constant PCRs (PCR0/PCR1) or an incomplete PCR set grants access far more broadly than the author intended.
4. **Break the encrypt-to-recipient binding:** obtain KMS plaintext by substituting an attacker-held `public_key` into (or replaying) a valid document so `CiphertextForRecipient` decrypts under the attacker's private key.
5. **Third-party verifier bypass:** exploit a naive custom verifier (no root pinning, CRL disabled → no revocation, unchecked PCRs, unsafe CBOR/COSE parsing) into accepting a bad document.
6. **Cross-tenant EK / attribute disclosure:** read another account's instance endorsement key (`get-instance-tpm-ek-pub`) or NitroTPM support attributes without ownership.
7. **Measurement-integrity / TOCTOU:** demonstrate that a runtime-compromised instance still attests as "trusted" because measurements are boot-time only.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces**
- **EC2 control-plane APIs** (SigV4/IAM): `RegisterImage` (`--tpm-support v2.0`, `--boot-mode uefi`), `DescribeImages`/`DescribeImageAttribute` (`tpmSupport`), `DescribeInstances` (`TpmSupport`), **`GetInstanceTpmEkPub`** (returns per-instance RSA-2048 endorsement public key, `tpmt`/`der`), `DescribeInstanceTypes` → `NitroTpmInfo.SupportedVersions`.
- **In-guest device**: NitroTPM presented as a TPM 2.0 CRB device to the guest OS (Linux tpm-tools / Windows tpm.msc). Not network-reachable; local to the instance.
- **In-guest utility**: `nitro-tpm-attest` (pkg `aws-nitro-tpm-tools`) — produces a signed Attestation Document; optional `--public-key` (RSA only), `--user-data`, `--nonce`.
- **Build-time utility**: `nitro-tpm-pcr-compute` — computes reference measurements (PCR4/PCR7/PCR12) from the UKI. **Publicly available** → anyone can compute reference measurements for any given (public/shared) AMI.
- **Verifier interfaces**: **AWS KMS** (`Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`, `GenerateDataKeyPair`, `GenerateRandom` with the `Recipient` parameter carrying the signed doc) or a **customer-built third-party verifier**.

**Processes / trust roots behind the interface**
- **NitroTPM** — per-instance virtual TPM inside the AWS Nitro System; holds PCRs, EK, sealed secrets.
- **Nitro Hypervisor** — signs Attestation Documents. **AWS service plane.**
- **AWS Nitro Attestation PKI** — root CA (ACM Private CA, 30-yr, `CN=aws.nitro-enclaves, C=US, O=Amazon, OU=AWS`; published root at `aws-nitro-enclaves.amazonaws.com/AWS_NitroEnclaves_Root-G1.zip`, fingerprint `64:1A:03:...:5B`). **AWS service plane.**
- **AWS KMS** — built-in NitroTPM verifier; matches PCRs in the doc against `kms:RecipientAttestation:NitroTPMPCR<n>` condition keys; encrypts response under the doc's `public_key`.

**Accounts / ownership**
- **Customer account** owns the AMI, the instance, the IAM principal, and the KMS key/policy.
- **AWS-controlled** Nitro plane owns the hypervisor signing key, the attestation PKI, and NitroTPM internal state (documented zero operator access).
- There is **no multi-tenant service *account* hosting customer resources** here in the classic sense; the sensitive shared surface is the **Nitro signing/PKI plane** (hard stop) and the **KMS verifier** which treats *any* validly-signed doc with matching PCRs as authorized regardless of tenant.

**Assets & identifier shapes**
- Attestation Document (CBOR/COSE_Sign1, ECDSA-384): `module_id`, `timestamp` (ms since epoch), `digest=SHA384`, `nitrotpm_pcrs` (index 0..31 → 32/48/64-byte value), `certificate` (DER ≤1024B), `cabundle` [root…interm], optional `public_key`/`user_data`/`nonce` (≤1024B each).
- PCRs: **PCR0/PCR1 = constant, AWS-controlled** ("always contain constant values"). **PCR4 (boot manager code), PCR7 (Secure Boot policy), PCR12 (kernel command line)** carry customer trust. PCR8–15 OS-defined; PCR16 debug; PCR23 app.
- Instance EK: RSA-2048 public key, per instance, retrievable at any time by an authorized caller via `GetInstanceTpmEkPub(instance-id)`.
- AMI/instance ids: `ami-…`, `i-…` (short/structured, enumerable).

**ASCII pipeline**
```
                    build time (customer)
  Attestable AMI  --nitro-tpm-pcr-compute--> reference PCR4/PCR7/PCR12 --> KMS key policy
  (KIWI NG, dm-verity/erofs, AL2023/NixOS)                                 (condition keys)
                                                                              |
  guest OS (measured boot) --PCRs--> [NitroTPM] --doc--> [Nitro Hypervisor SIGNS]
        |  nitro-tpm-attest(--public-key/--user-data/--nonce)    |  (AWS service plane)
        v                                                        v
   Attestation Document (CBOR/COSE) --Recipient param--> [ AWS KMS verifier ]
        |                                                   match PCRs? encrypt reply
        |                                                   under doc.public_key
        +---------------------------------------------> [ 3P verifier (customer-built) ]
                                                          chain+PCR+root-pin (CRL disabled)
```

---

## 3. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (observable proof) |
|---|---|---|---|---|
| B1 | Instance guest (customer code) | AWS KMS key of the *same* account | Attestation doc + PCR condition keys | KMS returns plaintext/`CiphertextForRecipient` when the running software does **not** match the pinned PCRs → measurement/policy bypass |
| B2 | **Account B** instance | **Account A**'s NitroTPM-gated KMS key | Same attestable AMI ⇒ same PCR4/7/12 satisfies A's PCR-only condition | Account B decrypts A's data (attestation ≠ ownership). **Cross-account = Critical** |
| B3 | Attacker (any) | Verifier (KMS or 3P) | Replayed / substituted Attestation Document | A doc not freshly produced by the attacker's live instance is accepted; response decrypts under attacker-held private key |
| B4 | Customer-built 3P verifier | Attestation PKI trust | CBOR/COSE parse + cert chain (CRL disabled) | Verifier accepts an unsigned/wrong-root/revoked/malformed doc, or crashes on crafted CBOR |
| B5 | Any IAM principal | Another account's instance EK | `GetInstanceTpmEkPub(instance-id)` | EK returned for an `i-…` the caller does not own (existence-only check) |
| B6 | Instance guest / data path | **Nitro Hypervisor signing key / Nitro PKI / other instances' TPM state** | (attempted) escape from guest to Nitro plane | **ANY** reach of the Nitro signing key, PKI private key, or another instance's TPM/PCR state = **HARD STOP** service-plane breach |
| B7 | Post-boot runtime attacker | Attestation "trusted" verdict | Measurements are boot-time only | A runtime-compromised instance still yields a passing (unchanged PCR4/7/12) document (TOCTOU) |

---

## 4. API / Interface Inventory

| Name | Method/Type | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes / lens |
|---|---|---|---|---|---|---|---|---|
| `GetInstanceTpmEkPub` | EC2 API (SigV4) | Existing | No | External | Returns per-instance RSA-2048 EK (`tpmt`/`der`) | Yes | IAM (`ec2:GetInstanceTpmEkPub`) | Resource-by-id (`instance-id`). **Confirm ownership vs existence.** → A/E |
| `RegisterImage` (`--tpm-support v2.0`, `--boot-mode uefi`) | EC2 API | Existing | **Yes** | External | Creates NitroTPM-enabled AMI from a snapshot | Yes | IAM (`ec2:RegisterImage`) | "attestable"/UEFI is customer-asserted at register time. → P |
| `DescribeImages` / `DescribeImageAttribute` (`tpmSupport`) | EC2 API | Existing | No | External | Reports AMI `TpmSupport` (`v2.0`) | Yes | IAM; owner for attribute | AMI sharing → attribute visibility. → A/I |
| `DescribeInstances` (`TpmSupport`) | EC2 API | Existing | No | External | Reports instance `TpmSupport` | Yes | IAM | Console does **not** show `TpmSupport` (visibility gap). → O |
| `DescribeInstanceTypes` → `NitroTpmInfo.SupportedVersions` | EC2 API | Existing | No | External | Lists supported NitroTPM versions per type | Yes | IAM | Informational. |
| `nitro-tpm-attest` (`--public-key/--user-data/--nonce`) | **In-guest utility** (not an AWS API) | Existing | No | Guest-local | Produces signed Attestation Document | No (local) | Anyone on the instance | Non-SDK. `nonce`/`user_data` "not used for KMS". → C/M |
| `nitro-tpm-pcr-compute` | Build-time utility | Existing | No | Offline | Computes reference PCR4/7/12 | No | Anyone | **Public → reference measurements are attacker-computable.** → B2/H |
| KMS `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom` (with `Recipient`) | KMS API | Existing | No (crypto) | External | Attestation-gated crypto; returns `CiphertextForRecipient` | Yes | IAM + key policy + `kms:RecipientAttestation:NitroTPMPCR<n>` | The core verifier. → H/M/C |

**Doc-flagged leads to keep verbatim:** "PCR0 and PCR1 … will always contain constant values" (constant, AWS-controlled). "nonce … Not used for attestation with AWS KMS." "CRL must be disabled when doing the validation." "The specified public key is included in the Attestation Document … [KMS] automatically encrypts the response with the public key." "up to 96 bytes" PCR value in KMS condition.

---

## 5. Recommended Areas of Focus (priority-ordered; one block per firing lens)

### AF-1 — Attestation authenticates code, not tenant → cross-account KMS access (Lens A + H)  [PRIORITY 1]
**Background:** A NitroTPM KMS policy gates crypto on PCR values in a signed Attestation Document. The reference PCRs are computed by the **public** `nitro-tpm-pcr-compute` tool from an AMI; PCR0/PCR1 are constant AWS values. Nothing in the *attestation mechanism itself* binds the document to a particular AWS account or instance owner — only the signed *code measurements* and the Nitro signature.
**Security Concern:** If a customer authors a KMS key policy that relies on the PCR condition keys **without also constraining `Principal` to their own account/role** (the sample policy *does* bind a role ARN, but the mechanism does not require it), then **any account that launches the same attestable AMI produces the same PCR4/7/12 and satisfies the condition** — a cross-account decrypt of the key owner's data.
**High-level Test Scenarios:**
- Claim: a KMS policy whose only gate is `kms:RecipientAttestation:NitroTPMPCR{4,7,12}` (Principal `*` or a broad org) is satisfiable by a *different* account running the identical AMI. → **Mechanism:** `prepare-attestation-service` policy relies on PCR condition keys; `nitro-tpm-pcr-compute` is public; PCRs are AMI-deterministic. → **Oracle:** account B, running the same public/shared attestable AMI, gets a successful `Decrypt` against account A's key. → **Severity:** cross-account data access = **Critical** (customer-authored misconfiguration; report as a hardening/guidance gap AND test whether AWS docs adequately warn).
- Claim: a policy pinned only to **PCR0/PCR1** (documented constant) grants **every** NitroTPM instance. → **Oracle:** any attestable instance satisfies it. → **Severity:** High (universal grant).
- Claim: **standard boot vs Secure Boot coverage gap** — a policy using only PCR7 (Secure Boot) accepts instances that merely present the same UEFI Secure Boot policy cert but differ in boot binaries (PCR4) / command line (PCR12), and vice-versa. → **Oracle:** a differently-built AMI sharing the pinned PCR but not the others still decrypts. → **Severity:** High.
**Doc evidence:** `prepare-attestation-service.md`; `nitrotpm-attestation-document-content.md` (PCR0/1 constant; PCR4/7/12 trust; PCR12 = command line); `conditions-nitro-tpm.html`. **Severity-if-true:** Critical (cross-account) / High (weak PCR set).
**Stop condition:** if a cross-account decrypt succeeds against a key you do not own without the owner's consent, stop and treat as sensitive; this is a real data-access breach — do not exfiltrate beyond minimal proof.

### AF-2 — Encrypt-to-recipient binding & document replay (Lens M + C)  [PRIORITY 1]
**Background:** For KMS attestation, `nonce` and `user_data` are **not used**; the documented replay/confidentiality defense is that KMS encrypts the plaintext response under the `public_key` carried **inside the signed document** and returns `CiphertextForRecipient`. Only the holder of the matching private key can read it.
**Security Concern:** The entire replay defense rests on `public_key` being **cryptographically bound (signed)** into the document by Nitro and on KMS refusing documents whose `public_key` is attacker-substitutable or stale. If the binding is weak, or a verifier accepts a doc with a swapped/omitted `public_key`, a captured document from a legitimately-attested victim instance can be replayed to read data.
**High-level Test Scenarios:**
- Claim: the `public_key` field is inside the COSE_Sign1 *signed payload* (not the unprotected header), so it cannot be swapped without breaking the Nitro signature. → **Mechanism:** `nitrotpm-attestation-document-validate.md` spec lists `public_key` in `AttestationDocument` (signed body); COSE_Sign1 signs the payload. → **Oracle:** modifying `public_key` and re-encoding invalidates signature verification → replay yields ciphertext only the *original* instance can decrypt. → **Severity if binding holds:** defense confirmed; if it does **not** hold → **Critical** (replay → plaintext exfil).
- Claim: KMS enforces **freshness** so an old captured doc is rejected. → **Mechanism:** `timestamp` present in doc but KMS docs are silent on freshness; `nonce` explicitly unused. → **Oracle:** replay a document captured hours earlier from a still-valid instance; if KMS accepts it, freshness is unenforced (replayability bounded only by the recipient-encryption defense). → **Severity:** Medium–High (depends on whether AF-2.1 binding holds).
- Claim: for **third-party** verifiers, absence of a mandated nonce means a naive verifier is trivially replayable. → **Oracle:** a 3P verifier that omits the optional `nonce` challenge accepts a replayed doc. → **Severity:** High (verifier-dependent).
**Doc evidence:** `attestation-attest.md`, `attestation-get-doc.md` (nonce/user_data unused for KMS; public_key encrypts response), `nitrotpm-attestation-document-validate.md` (doc spec). **Severity-if-true:** Critical if binding broken; High for 3P replay.

### AF-3 — Third-party verifier footguns (Lens F + M + Q)  [PRIORITY 2]
**Background:** AWS explicitly tells customers building non-KMS verifiers to implement their own receive/parse/validate logic, and documents the exact steps (decode CBOR → COSE_Sign1 → verify chain → verify signature), the root fingerprint to pin, the cabundle ordering, and — critically — **"CRL must be disabled when doing the validation."**
**Security Concern:** Each documented step is a place a real customer verifier goes wrong; the doc itself hands the attacker the failure modes.
**High-level Test Scenarios (against a hypothetical/customer verifier, documentation-derived):**
- Claim: **CRL disabled ⇒ no revocation** — a leaked/compromised Nitro *intermediate* cert cannot be revoked to relying parties following the doc verbatim. → **Oracle:** a doc chaining to a revoked-but-still-valid-window intermediate is accepted. → **Severity:** High (systemic, but depends on AWS PKI compromise — note as PKI-design observation, hard-stop if you actually obtain Nitro key material).
- Claim: a verifier that validates the **chain but not the PCR values** accepts any genuine Nitro-signed doc from *any* instance (including attacker's). → **Oracle:** attacker's own legitimately-signed doc (different software) passes. → **Severity:** High.
- Claim: a verifier that does **not pin the published root fingerprint** / accepts the attacker-supplied `cabundle` as trust anchor is fully bypassable. → **Oracle:** self-signed root + forged chain accepted. → **Severity:** Critical (verifier-side).
- Claim: **CBOR/COSE parser abuse** — oversized/`> ≤1024B` fields, deeply nested CBOR, malformed COSE tags, wrong `alg` (expecting `{1:-35}` ECDSA-384) → parser crash, memory issues, or signature-check skip. → **Oracle:** verifier crash/hang or acceptance of `alg:none`-style downgrade. → **Severity:** High (bypass) / Medium (DoS).
- Claim: **cabundle ordering** confusion (doc warns Java CertPath needs reversed order) causes a verifier to build a path that validates an attacker-influenced chain. → **Oracle:** reordered cabundle accepted. → **Severity:** Medium–High.
**Doc evidence:** `nitrotpm-attestation-document-validate.md` (all steps; "CRL must be disabled"; root fingerprint; cabundle order; COSE_Sign1 `{1:-35}`; size limits). **Severity-if-true:** Critical→Medium depending on which step fails.

### AF-4 — Cross-tenant EK / attribute disclosure (Lens A + E)  [PRIORITY 2]
**Background:** `GetInstanceTpmEkPub` returns the per-instance endorsement **public** key for an `instance-id` "at any time". `DescribeImageAttribute tpmSupport` and `DescribeInstances TpmSupport` expose NitroTPM enablement.
**Security Concern:** Resource-by-id APIs must scope to the caller's tenant, not merely to resource existence. The EK is a stable per-instance identity; leaking it cross-account enables fingerprinting/impersonation-adjacent research and enumeration.
**High-level Test Scenarios:**
- Claim: `GetInstanceTpmEkPub` returns the EK for an instance the caller does **not** own. → **Mechanism:** `retrieve-ekpub.md` (no ownership statement; takes `instance-id`). → **Oracle:** EK returned for another account's `i-…`, or distinct error (not-found vs access-denied) forming an enumeration oracle over the structured `i-…` space. → **Severity:** cross-account EK read = Medium (public key, but tenancy/enumeration leak); enumeration oracle = Low–Medium.
- Claim: `tpmSupport` attribute is readable on AMIs shared with the caller in a way that leaks owner intent. → **Oracle:** attribute visible on a shared AMI. → **Severity:** Low.
**Doc evidence:** `retrieve-ekpub.md`, `verify-nitrotpm-support-on-instance.md`, `verify-nitrotpm-support-on-ami.md`. **Severity-if-true:** Medium.

### AF-5 — Boot-time-only measurement / attestation TOCTOU (Lens M, design)  [PRIORITY 3]
**Background:** Measurements reflect the instance's **initial boot state**; the isolated-compute model depends on `dm-verity`/`erofs` read-only root so restarts return to the measured state.
**Security Concern:** PCR4/7/12 capture boot integrity, not live runtime integrity. A post-boot runtime compromise (memory-only, or any change not persisted through a restart) does **not** alter the attested measurements, so the instance keeps attesting as "trusted" between attestation and use.
**High-level Test Scenarios:**
- Claim: a runtime-compromised (but boot-unchanged) instance still produces a passing document and can drive KMS `Decrypt`. → **Oracle:** inject a memory-resident change, re-attest, observe unchanged PCR4/7/12 and continued KMS access. → **Severity:** Medium (documented TPM/measured-boot limitation; note as attestation-scope caveat, and check whether AWS docs set correct expectations).
- Claim: TOCTOU between attestation and KMS use — long-lived recipient keypair widens the window. → **Oracle:** attest once, compromise, reuse the recipient key for later KMS calls. → **Severity:** Medium.
**Doc evidence:** `attestable-ami.md` ("measurements are based on its initial boot state"), `isolate-data-operators.md`. **Severity-if-true:** Medium.

### AF-6 — AMI "attestable" property is customer-asserted at registration (Lens P)  [PRIORITY 3]
**Background:** `RegisterImage --tpm-support v2.0 --boot-mode uefi` marks an AMI as NitroTPM/UEFI. The "attestable" quality (immutable root, isolated compute, correct UKI/PCR computation) is entirely the customer's build discipline; `nitro-tpm-pcr-compute` is run by the customer offline.
**Security Concern:** There is no gate proving the snapshot is genuinely UEFI/attestable or that declared reference measurements correspond to the registered image; mismatches could let an operator register an AMI whose real measurements differ from the policy-pinned ones (feeding AF-1/AF-5).
**High-level Test Scenarios:**
- Claim: `RegisterImage` accepts `--tpm-support v2.0` on a snapshot that is not actually UEFI/attestable, or the reference measurements can be decoupled from the actual image. → **Oracle:** an instance from such an AMI fails/succeeds attestation inconsistently with declared PCRs. → **Severity:** Medium (enables policy-vs-reality drift).
**Doc evidence:** `enable-nitrotpm-support-on-ami.md`, `build-sample-ami.md`. **Severity-if-true:** Medium.

### AF-7 — Audit / visibility gaps (Lens O)  [PRIORITY 4]
**Background:** `TpmSupport` is "not displayed in the Amazon EC2 console" for either AMI or instance; NitroTPM state is excluded from EBS snapshots and VM Import/Export. KMS NitroTPM condition values appear in CloudTrail (`ct-nitro-tpm`).
**Security Concern:** Console blind spots hamper defenders' detection of NitroTPM misconfiguration; verify attestation-gated KMS calls are fully logged (PCRs, recipient) and that `GetInstanceTpmEkPub` is logged.
**High-level Test Scenarios:** Claim: an attestation-gated KMS operation or an EK retrieval produces no/low-fidelity audit record. → **Oracle:** perform the op, inspect CloudTrail for PCR/recipient attribution. → **Severity:** Low–Informational (enabler).
**Doc evidence:** `enable-nitrotpm-prerequisites.md` (console/snapshot/VMIE exclusions), `verify-*` pages, `conditions-nitro-tpm.html` (CloudTrail inclusion). **Severity-if-true:** Low.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account decrypt via same attestable AMI | KMS attestation policy | PCR condition keys + (sample) Principal ARN binding — test whether the Principal binding is *required* vs merely shown |
| Weak/constant PCR pinning grants broadly | KMS policy authoring | Doc statement that PCR0/1 are constant and PCR4/7/12 carry trust |
| Document replay → plaintext | KMS + `public_key` binding | Encrypt-to-recipient under signed `public_key`; nonce unused for KMS |
| Forged/malformed document accepted | 3P verifier | CBOR→COSE_Sign1 decode, chain build, signature verify, root fingerprint pin, cabundle order |
| No revocation of compromised intermediate | Nitro PKI + verifiers | "CRL must be disabled" (accepted design tradeoff — test blast radius) |
| Cross-account EK read / instance enumeration | `GetInstanceTpmEkPub` | IAM authorization (`ec2:GetInstanceTpmEkPub`) resource scoping |
| Runtime compromise still attests trusted | Measured boot (PCRs) | dm-verity/erofs immutability; measurements = boot state (scope caveat) |
| Register non-attestable AMI as attestable | `RegisterImage` | UEFI/`tpm-support v2.0` flags; customer build discipline |
| Guest → Nitro signing key / other-instance TPM | Nitro System | **Zero operator access** (hard-stop boundary) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **The Nitro service plane itself** — the Nitro Hypervisor signing key, the Nitro Attestation PKI private key, and any other instance's NitroTPM/PCR state. Nitro is documented "zero operator access"; probing for a break of it is a **hard stop / disclosure**, not in-scope hunting.
- **A customer steering their own instance's software** — the owner can run whatever code they like on their own instance; changing *their own* measurements is not a vuln. The bug class is only when this crosses to *another* tenant or defeats a verifier the attacker doesn't control.
- **Guest-OS / in-instance TPM usage** (BitLocker sealing, tpm-tools) confined to a single tenant's own instance — customer responsibility (shared-responsibility model, `nitrotpm-attestation.md`).
- **Bugs in third-party reference repos** (KIWI NG, coldsnap, erofs, dm-verity, NitroTPM-Tools GitHub) — note and route upstream; not the AWS service boundary. (Their *design footguns as documented by AWS* are in scope — AF-3.)
- **Generic TPM 2.0 spec weaknesses** not specific to NitroTPM's AWS integration.
- **Single-tenant self-DoS** (spamming `nitro-tpm-attest` on your own instance).

---

## 8. Null Hypotheses / Doc Gaps (lens sweep evidence)
- **Lens B (Confused deputy / PassRole):** N/A. Read `retrieve-ekpub`, `enable-nitrotpm-support-on-ami`, `attestation-attest`, `attestation-get-doc`, `prepare-attestation-service` — **no field accepts a role ARN the service assumes on the caller's behalf**; KMS uses the caller's own IAM principal plus the doc. No `iam:PassRole`/`SourceArn` surface in NitroTPM APIs.
- **Lens G (SSRF):** N/A. Read `attestation-get-doc`, `nitrotpm-attestation-document-validate`, `retrieve-ekpub`, `enable-nitrotpm-support-on-ami`, `prepare-attestation-service` — **no field the AWS service dereferences server-side**. The one URL (`aws-nitro-enclaves.amazonaws.com/...Root-G1.zip`) is fetched by the *customer/verifier*, not by the service. (If a future feature adds a service-side attestation-document fetch or webhook, re-open this lens.)
- **Lens J (OAuth/3P linking):** N/A. No 3P identity linking, `state` param, or callback in any NitroTPM page.
- **Lens K (Prompt injection / LLM):** N/A. No LLM/agent in the NitroTPM pipeline. (The "AI coding assistants" doc footer is boilerplate, not a service component.)
- **Lens N (namespace migration):** N/A. Single ARN/attribute model (`tpmSupport`/`TpmSupport`, `v2.0`); no dual-namespace migration described.
- **Lens I (tagging/ABAC):** Mostly N/A — `tpmSupport` is an image *attribute*, not a tag, and is not an access-control mechanism. Filter `Name=tpm-support` exists for discovery only.
- **Lens D (data→control plane):** Folded into B6/hard-stop — the only control-plane target is the Nitro plane, which is the hard-stop boundary.
- **Lens L (DoS):** Folded into AF-3 (verifier CBOR parser). No documented multi-tenant shared fleet to exhaust; single-tenant self-DoS out of scope.
- **Lens H (CMK/enc-context):** Fired — see AF-1 (PCR pinning is the encryption-authz control).
- **Doc gaps to confirm before hunting:** (a) whether KMS enforces Attestation Document **freshness/`timestamp`** (unspecified) — AF-2; (b) exact **IAM resource scoping** of `GetInstanceTpmEkPub` (ownership vs existence) — AF-4; (c) whether `RegisterImage` validates the snapshot is genuinely UEFI/attestable — AF-6; (d) whether `public_key` is in the COSE **protected/signed** payload vs unprotected header — AF-2.1 (spec implies signed body; confirm).

---

## Appendix A — Deep-dive: Attestation Document Cryptographic & Verifier Boundary
*Produced by a dedicated documentation-only subagent focused on the COSE/CBOR/PKI validation boundary. All items are unconfirmed hypotheses; each needs either reference-implementation inspection (aws/NitroTPM-Tools source) or controlled lab testing to become a finding.*

1. **CRL disabled ⇒ no revocation of a compromised Nitro intermediate.** Mechanism: validate page — *"CRL must be disabled when doing the validation"*, sample Java `setRevocationEnabled(false)`; no OCSP mentioned. Oracle: confirm AWS publishes no revocation channel / emergency rotation for the Nitro Attestation PKI (only per-cert validity window). Severity: **Critical** (single intermediate-key compromise = long-lived forgery, no verifier kill switch). *Note: obtaining Nitro key material is a HARD STOP.*
2. **Spec-literal verifier is replayable.** The documented 4-step validation (decode→extract→verify chain→verify signature) never checks `timestamp` freshness or `nonce`. Oracle: check whether any AWS reference verifier enforces recency. Severity: **High** (stale-doc replay for 3P verifiers).
3. **KMS path has no documented replay defense via nonce.** `nonce`/`user_data` "Not used for attestation with AWS KMS"; no freshness check described. Oracle: check KMS `Recipient` docs for a timestamp window; absence ⇒ captured doc + request potentially replayable within cert validity. Severity: **High** (bounded by AF-2 encrypt-to-recipient binding).
4. **CA-bundle reversal / fail-open chain building.** cabundle ships `[ROOT…INTERM_N]` but must be reversed to `[TARGET…ROOT]`; doc warns Java CertPath needs different order. Oracle: feed common libs (Go `x509.Verify`, OpenSSL, Java `CertPathValidator`) the raw order → hard error (safe) vs silent truncated-path accept (unsafe). Severity: **Critical if any mainstream lib fails open** (chain-verify bypass via glue-code bug).
5. **Root-pin ambiguity / no rotation story.** Fingerprint `64:1A:03:…` given without a named hash algorithm; static ZIP URL; 30-yr root, no documented backup/rotation. Oracle: confirm fingerprint algo is unambiguous across AWS refs; check for root-rotation guidance. Severity: **Medium** (pinning fragility footgun).
6. **Verify-after-use ordering risk.** `public_key`/`user_data`/`nonce`/PCRs are inside the signed COSE_Sign1 payload (sound by design), **but** the documented step order extracts (step 2) *before* signature verify (step 4) — an implementation acting on extracted fields before the crypto check is a textbook verify-after-use bug. Oracle: audit reference verifier ordering. Severity: **Critical if present in a real verifier**; low if all gate on signature success first.
7. **PCR0/PCR1-only policy = no boundary.** Doc: PCR0/1 "controlled by AWS … always contain constant values." A KMS policy/verifier pinning only these grants *any* NitroTPM instance. Oracle: confirm PCR0/1 identical across accounts/AMIs. Severity: **Critical** (policy-design flaw; under-specified guidance invites it). *(reinforces AF-1)*
8. **PCR7-only (Secure Boot) misses command-line integrity.** PCR12 = kernel command-line hash, "Required in conjunction with PCR4 for standard boot"; PCR7 covers only Secure Boot *policy* (which binaries may run), not their arguments. Oracle: determine if Secure Boot measures cmdline via any PCR; if not, a PCR7-only policy allows `init=/bin/sh`/lockdown-disable/cmdline tampering while PCR7 is unchanged. Severity: **High** (disable in-guest controls yet still attest). *(reinforces AF-1)*
9. **Digest/PCR size confusion.** CDDL fixes `digest="SHA384"` but `pcr = bytes .size (32/48/64)`; KMS condition value is "up to 96 bytes" hex (=48B, SHA-384 only). Oracle: feed a doc with `digest=SHA384` but 32/64-byte PCRs to parsers/comparators → silent false-accept vs crash. Severity: **Medium/High**.
10. **Unenforced field-size bounds → parser DoS.** `cert ≤1024B`, `user_data`/`nonce`/`public_key ≤1024B` are advisory; an oversized CBOR blob hits a permissive decoder pre-signature-check. Oracle: submit 10 MB `user_data` to common COSE/CBOR libs; check bounds enforced before/independent of signature verify. Severity: **Medium** (pre-auth parser hardening).
11. **Crypto-valid but semantically meaningless attestation (skipped PCR comparison).** The validate page's 4 steps never say to compare `nitrotpm_pcrs` against reference values — that guidance lives only on separate `content`/`prepare` pages framed around KMS. A 3P implementer may stop after "authentically signed by AWS" and skip "proves expected software runs." Oracle: review any AWS 3P-verifier sample for mandatory PCR comparison. Severity: **Critical** (authentic signature, unchecked measurements). *(reinforces AF-3)*
12. **Encrypt-to-recipient binds only to caller-chosen ephemeral key.** KMS encrypts the response under whatever RSA `public_key` the requesting instance embedded; no cross-check to a pre-registered identity. Intended design, but a footgun for verifiers assuming `public_key` implies instance-identity continuity. Oracle: confirm no identity/key continuity check exists. Severity: **Low/Informational** (design), flag as footgun. *(reinforces AF-2)*
13. **PCR4-without-PCR12 under-specification.** `prepare` says "PCR4 and PCR12 … for standard boot" (a set), but KMS condition keys are single-valued per-PCR with no enforced pairing — a policy with only PCR4 silently drops command-line integrity. Oracle: confirm KMS accepts a PCR4-only policy without warning. Severity: **High**. *(reinforces AF-1)*
14. **Policy-composition fail-open.** `conditions-nitro-tpm` shows the attestation-gated Allow in isolation; a separate unconditioned Allow (other key-policy statement or broad IAM) for the same KMS action bypasses attestation entirely. Oracle: lab-test a principal with both an attestation-gated and an unconditioned grant. Severity: **High** (general IAM composition risk; docs omit a least-privilege warning).

**Cross-cutting:** crypto/parsing (1,4,6,9,10,11); replay (2,3); pin/trust-anchor footguns (5,6); encrypt-to-recipient (12); PCR-as-authz (7,8,13,14). Highest-value next steps: inspect **aws/NitroTPM-Tools source** (not just README) and lab-test KMS policy composition + PCR subset behavior.
