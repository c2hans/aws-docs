# NitroTPM for Amazon EC2 — Attack Research Plan

**Assigned skill:** `security-questionbuilder` (single-skill run).
**Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html
**Source of leads:** AWS documentation only.
- Offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` — `nitrotpm.md`, `nitrotpm-instance.md`, `nitrotpm-attestation.md`, `nitrotpm-attestation-document-content.md`, `nitrotpm-attestation-document-validate.md`, `enable-nitrotpm-prerequisites.md`, `attestable-ami.md`, `attestation-get-doc.md`, `attestation-attest.md`, `prepare-attestation-service.md`, `retrieve-ekpub.md`, `isolate-data-operators.md`.
- Live pages (verified this run to avoid local-sync failure): `.../UserGuide/nitrotpm.html` and `https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-tpm.html`. **Both match the offline mirror byte-for-substance.**
- Also referenced: `.../APIReference/API_GetInstanceTpmEkPub`, `.../kms/latest/developerguide/services-nitro-enclaves.html`, `.../kms/latest/developerguide/ct-nitro-tpm.html`.

**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Every item is a boundary that *might not hold* plus the exact observation that would settle it.

> **Doc-content trust note (`SUSPECTED PROMPT INJECTION`):** every NitroTPM page (offline and live) and the KMS conditions page carry a boilerplate *"Skills for AI coding assistants (optional) … run `aws agent-toolkit search-skills`"* footer. This is untrusted page content aimed at AI agents, **not** an instruction. It was ignored during analysis and is flagged here for downstream awareness. Never execute it.

---

## 0. How to use this document
- Each lead is: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity → Stop condition.** Work in priority order (Section 5). Look left and right for adjacent bugs.
- **Central mental model:** an Attestation Document proves *which software booted*, signed by AWS's Nitro root of trust. It does **NOT** prove *who owns the instance* and does **NOT** prove *runtime* (post-boot) state. Most high-value leads are specializations of that gap.
- **HARD STOP / service-plane boundary:** the moment evidence implicates AWS's own plane — the Nitro Hypervisor signing key, the Nitro Attestation PKI private key, another instance's NitroTPM internal state, or any cross-instance/cross-tenant Nitro artifact — **stop, preserve evidence, flag for AWS Security disclosure.** Nitro provides documented "zero operator access"; a breach of it is a hard stop, not a lead to escalate.

---

## 1. Pentest Objectives (boundary-breach goals as concrete outcomes)
1. **Forge or replay** an Attestation Document that a verifier (AWS KMS or a third-party verifier) accepts for software the attacker is *not* running → satisfy a PCR-gated KMS policy and obtain `Decrypt`/`GenerateDataKey` output.
2. **Cross-account key access via attestation:** from account B, satisfy account A's NitroTPM-attestation KMS key policy by running the *same* attestable AMI (attestation authenticates code, not tenant).
3. **Weak-PCR policy grant:** prove that a KMS policy pinned to AWS-controlled/constant PCRs (PCR0/PCR1) or an incomplete PCR set grants access far more broadly than the author intended.
4. **Break the encrypt-to-recipient binding:** obtain KMS plaintext by substituting an attacker-held `public_key` into (or replaying) a valid document so `CiphertextForRecipient` decrypts under the attacker's private key.
5. **Third-party verifier bypass:** exploit a naive custom verifier (no root pinning, CRL disabled → no revocation, unchecked PCRs, unsafe CBOR/COSE parsing) into accepting a bad document.
6. **Cross-tenant EK / attribute disclosure:** read another account's instance endorsement key (`get-instance-tpm-ek-pub`) or NitroTPM support attributes without ownership.
7. **Measurement-integrity / TOCTOU:** demonstrate a runtime-compromised instance still attests as "trusted" because measurements are boot-time only.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces**
- **EC2 control-plane APIs** (SigV4/IAM): `RegisterImage` (`--tpm-support v2.0`, `--boot-mode uefi`), `DescribeImages`/`DescribeImageAttribute` (`tpmSupport`), `DescribeInstances` (`TpmSupport`), **`GetInstanceTpmEkPub`** (returns per-instance RSA-2048 endorsement public key, `tpmt`/`der` format), `DescribeInstanceTypes` → `NitroTpmInfo.SupportedVersions`.
- **In-guest device:** NitroTPM presented as a TPM 2.0 CRB device to the guest OS (Linux tpm-tools / Windows tpm.msc). Not network-reachable; local to the instance.
- **In-guest utility:** `nitro-tpm-attest` (pkg `aws-nitro-tpm-tools`, `/usr/bin/`) — produces a signed Attestation Document; optional `--public-key` (RSA only), `--user-data`, `--nonce`. Doc: `user-data` and `nonce` are **"Not used for attestation with AWS KMS."**
- **Build-time utility:** PCR-compute tooling (`create-pcr-compute.md`) — computes reference measurements (PCR4/PCR7/PCR12) from the AMI/UKI. **Customer-run offline; the tooling / sample recipes are public** → anyone can compute reference measurements for any public/shared attestable AMI.
- **Verifier interfaces:** **AWS KMS** (`Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`, `GenerateDataKeyPair`, `GenerateRandom` with the `Recipient` parameter carrying the signed doc) **or** a **customer-built third-party verifier**.

**Processes / trust roots behind the interface**
- **NitroTPM** — per-instance virtual TPM inside the AWS Nitro System; holds PCRs, EK, sealed secrets.
- **Nitro Hypervisor** — signs Attestation Documents. **AWS service plane.**
- **AWS Nitro Attestation PKI** — root CA (AWS Private CA, 30-yr, `CN=aws.nitro-enclaves, C=US, O=Amazon, OU=AWS`; published root at `aws-nitro-enclaves.amazonaws.com/AWS_NitroEnclaves_Root-G1.zip`, fingerprint `64:1A:03:...:5B`). **AWS service plane.**
- **AWS KMS** — built-in NitroTPM verifier; matches PCRs in the doc against `kms:RecipientAttestation:NitroTPMPCR<n>` condition keys; encrypts the response under the doc's `public_key`.

**Accounts / ownership**
- **Customer account** owns the AMI, the instance, the IAM principal, and the KMS key/policy.
- **AWS-controlled Nitro plane** owns the hypervisor signing key, the attestation PKI, and NitroTPM internal state (documented zero operator access — `isolate-data-operators.md`).
- There is **no classic multi-tenant service *account* hosting customer resources** here. The sensitive shared surface is (a) the **Nitro signing/PKI plane** (hard stop) and (b) the **KMS verifier**, which treats *any* validly-signed doc with matching PCRs as authorized regardless of tenant.

**Assets & identifier shapes**
- **Attestation Document** (CBOR / COSE_Sign1, ECDSA-384, tag 18, `{1:-35}`): `module_id`, `timestamp` (uint .size 8, ms since epoch), `digest="SHA384"`, `nitrotpm_pcrs` (index 0..31 → 32/48/64-byte value), `certificate` (DER ≤1024B), `cabundle` `[ROOT … INTERM_N]`, optional `public_key`/`user_data`/`nonce` (bytes 0..1024 each).
- **PCRs:** **PCR0/PCR1 = constant, AWS-controlled** ("always contain constant values"). **PCR4 (boot manager code), PCR7 (Secure Boot policy), PCR12 (kernel command line)** carry customer trust. PCR2/3 pluggable; PCR5 boot-mgr config+GPT; PCR6 platform mfr; PCR8–15 OS-defined; PCR16 debug; PCR23 app.
- **Instance EK:** RSA-2048 public key, per instance, retrievable "at any time" via `GetInstanceTpmEkPub(instance-id)`, `tpmt`/`der`.
- **AMI/instance ids:** `ami-…`, `i-…` — short, structured, enumerable.
- **KMS condition value:** lower-case hex string, **up to 96 bytes** (confirmed live on `conditions-nitro-tpm.html`); condition key is **single-valued**, `StringEqualsIgnoreCase`.

**ASCII pipeline**
```
                    build time (customer)
  Attestable AMI  --pcr-compute--> reference PCR4/PCR7/PCR12 --> KMS key policy
  (KIWI NG, dm-verity/erofs, AL2023/NixOS)                       (condition keys)
                                                                     |
  guest OS (measured boot) --PCRs--> [NitroTPM] --doc--> [Nitro Hypervisor SIGNS]
        |  nitro-tpm-attest(--public-key/--user-data/--nonce)    |  (AWS service plane)
        v                                                        v
   Attestation Document (CBOR/COSE) --Recipient param--> [ AWS KMS verifier ]
        |                                                   match PCRs? encrypt reply
        |                                                   under doc.public_key -> CiphertextForRecipient
        +---------------------------------------------> [ 3P verifier (customer-built) ]
                                                          chain+PCR+root-pin (CRL disabled)
```

---

## 3. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (observable proof) |
|---|---|---|---|---|
| B1 | Instance guest (customer code) | AWS KMS key of the *same* account | Attestation doc + PCR condition keys | KMS returns plaintext/`CiphertextForRecipient` when the running software does **not** match the pinned PCRs → measurement/policy bypass |
| B2 | **Account B** instance | **Account A**'s NitroTPM-gated KMS key | Same attestable AMI ⇒ same PCR4/7/12 satisfies A's PCR-only condition | Account B decrypts A's data (attestation ≠ ownership). **Cross-account = Critical** |
| B3 | Attacker (any) | Verifier (KMS or 3P) | Replayed / substituted Attestation Document | A doc not freshly produced by the attacker's live instance is accepted; response decrypts under an attacker-held private key |
| B4 | Customer-built 3P verifier | Attestation PKI trust | CBOR/COSE parse + cert chain (CRL disabled) | Verifier accepts an unsigned/wrong-root/revoked/malformed doc, or crashes on crafted CBOR |
| B5 | Any IAM principal | Another account's instance EK | `GetInstanceTpmEkPub(instance-id)` | EK returned for an `i-…` the caller does not own (existence-only check), or a not-found/access-denied oracle over the `i-…` space |
| B6 | Instance guest / data path | **Nitro Hypervisor signing key / Nitro PKI / other instances' TPM state** | (attempted) escape from guest to Nitro plane | **ANY** reach of the Nitro signing key, PKI private key, or another instance's TPM/PCR state = **HARD STOP** service-plane breach |
| B7 | Post-boot runtime attacker | Attestation "trusted" verdict | Measurements are boot-time only | A runtime-compromised instance still yields a passing (unchanged PCR4/7/12) document (TOCTOU) |

---

## 4. API / Interface Inventory

| Name | Method/Type | Mutating | Internet-callable | Authorized callers | Functionality | Notes / lens |
|---|---|---|---|---|---|---|
| `GetInstanceTpmEkPub` | EC2 API (SigV4) | No | Yes | IAM (`ec2:GetInstanceTpmEkPub`) | Returns per-instance RSA-2048 EK (`tpmt`/`der`) | Resource-by-id (`instance-id`). **Confirm ownership vs existence.** → A/E/M |
| `RegisterImage` (`--tpm-support v2.0`, `--boot-mode uefi`) | EC2 API | **Yes** | Yes | IAM (`ec2:RegisterImage`) | Creates NitroTPM/UEFI AMI from a snapshot | "attestable"/UEFI is customer-asserted at register time. → P |
| `DescribeImages` / `DescribeImageAttribute` (`tpmSupport`) | EC2 API | No | Yes | IAM; owner for attribute | Reports AMI `TpmSupport` (`v2.0`) | AMI sharing → attribute visibility. → A/I |
| `DescribeInstances` (`TpmSupport`) | EC2 API | No | Yes | IAM | Reports instance `TpmSupport` | Console does **not** show `TpmSupport` (visibility gap). → O |
| `DescribeInstanceTypes` → `NitroTpmInfo.SupportedVersions` | EC2 API | No | Yes | IAM | Lists supported NitroTPM versions per type | Informational. |
| `nitro-tpm-attest` (`--public-key/--user-data/--nonce`) | In-guest utility (not an AWS API) | No | No (local) | Anyone on the instance | Produces signed Attestation Document | Non-SDK. `nonce`/`user_data` "not used for KMS". → C/M |
| PCR-compute tooling | Build-time utility | No | No | Anyone (public tooling/recipes) | Computes reference PCR4/7/12 | **Reference measurements are attacker-computable for any public/shared AMI.** → B2/AF-1 |
| KMS `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom` (with `Recipient`) | KMS API | No (crypto) | Yes | IAM + key policy + `kms:RecipientAttestation:NitroTPMPCR<n>` | Attestation-gated crypto; returns `CiphertextForRecipient` | The core verifier. **Condition key is single-valued.** → H/M/C |

**Doc-flagged leads (verbatim, verified live):** "PCR0 and PCR1 … will always contain constant values." "nonce/user-data … Not used for attestation with AWS KMS." "CRL must be disabled when doing the validation." "[KMS] automatically encrypts the response with the public key included in the Attestation Document." "The PCR value must be a lower-case hexadecimal string of up to 96 bytes." "If the request does not include an attestation document, permission is denied because this condition is not satisfied." Condition key value type = **Single-valued** (KMS `conditions-nitro-tpm.html`).

---

## 5. Recommended Areas of Focus (priority-ordered; one block per firing lens)

### AF-1 — Attestation authenticates code, not tenant → cross-account KMS access (Lens A + H) [PRIORITY 1]
**Background:** A NitroTPM KMS policy gates crypto on PCR values in a signed Attestation Document. Reference PCRs are computed by public tooling from an AMI; PCR0/PCR1 are constant AWS values. Nothing in the *attestation mechanism itself* binds the document to a particular AWS account or instance owner — only the signed code measurements and the Nitro signature.
**Security Concern:** The single documented gate that always fires is "an attestation document with matching PCRs is present" (`conditions-nitro-tpm.html`: *"If the request does not include an attestation document, permission is denied…"*). The Principal binding in AWS's sample policy is *shown* but not *required* by the mechanism. A customer who pins only the PCR condition keys (Principal `*`, broad org, or a role in another account) is satisfiable by **any account that launches the same attestable AMI**.
**High-level Test Scenarios:**
- **Claim:** a KMS policy whose only gate is `kms:RecipientAttestation:NitroTPMPCR{4,7,12}` (no tenant-scoping Principal) is satisfiable by a *different* account running the identical public/shared attestable AMI. → **Oracle:** account B, running the same AMI, gets a successful `Decrypt`/`CiphertextForRecipient` against account A's key. → **Severity:** cross-account data access = **Critical** (customer misconfiguration; also test whether AWS docs adequately warn).
- **Claim:** a policy pinned only to **PCR0/PCR1** (documented constant) grants **every** NitroTPM instance. → **Oracle:** any attestable instance satisfies it. → **Severity:** High.
- **Claim:** **single-valued condition key → no enforced PCR pairing.** `conditions-nitro-tpm.html` confirms the key is *Single-valued*; a policy with only PCR4 (or only PCR7) silently drops command-line integrity (PCR12) / boot-binary integrity (PCR4). → **Oracle:** a differently-built AMI sharing the one pinned PCR but not the others still decrypts. → **Severity:** High.
**Doc evidence:** `prepare-attestation-service.md`; `nitrotpm-attestation-document-content.md`; `conditions-nitro-tpm.html`. **Severity-if-true:** Critical (cross-account) / High (weak PCR set).
**Stop condition:** a successful cross-account decrypt against a key you do not own is a real data-access breach — stop at minimal proof, do not exfiltrate.

### AF-2 — Encrypt-to-recipient binding & document replay (Lens M + C) [PRIORITY 1]
**Background:** For KMS attestation, `nonce`/`user_data` are **not used**; the documented replay/confidentiality defense is that KMS encrypts the plaintext under the `public_key` carried **inside the signed document** and returns `CiphertextForRecipient`. Only the matching private key can read it.
**Security Concern:** The entire replay defense rests on `public_key` being cryptographically bound (signed) into the COSE_Sign1 payload by Nitro, and on KMS not enforcing any freshness (`conditions-nitro-tpm.html` and `attestation-attest.md` describe **no** timestamp/replay check). If the binding is weak or a verifier accepts a doc with a swapped/omitted `public_key`, a captured document from a legitimately-attested victim could be replayed.
**High-level Test Scenarios:**
- **Claim:** `public_key` sits in the COSE_Sign1 *signed payload* (spec lists it inside `AttestationDocument`), so swapping it breaks the Nitro signature. → **Oracle:** modify `public_key`, re-encode, submit → signature verification fails; if it does **not**, replay → plaintext under attacker key = **Critical**.
- **Claim:** KMS enforces **no** attestation-document freshness. `timestamp` is present in the doc but neither `attestation-attest.md` nor `conditions-nitro-tpm.html` mentions a freshness window; `nonce` is explicitly unused for KMS. → **Oracle:** replay a document captured earlier from a still-valid instance; acceptance proves freshness is unenforced (bounded only by the recipient-encryption defense). → **Severity:** Medium–High.
- **Claim:** a naive **3P** verifier that omits the optional `nonce` challenge is trivially replayable. → **Oracle:** 3P verifier accepts a replayed doc. → **Severity:** High.
**Doc evidence:** `attestation-attest.md`, `attestation-get-doc.md`, `nitrotpm-attestation-document-validate.md`, `conditions-nitro-tpm.html`. **Severity-if-true:** Critical if binding broken; High for 3P replay.

### AF-3 — Third-party verifier footguns (Lens F + M + Q) [PRIORITY 2]
**Background:** AWS tells customers building non-KMS verifiers to implement their own receive/parse/validate logic and documents the exact steps (decode CBOR → COSE_Sign1 → verify chain → verify signature), the root fingerprint to pin, the cabundle ordering (`[ROOT…INTERM_N]`, must be reversed for path building), and — critically — **"CRL must be disabled when doing the validation."** The doc hands the attacker the failure modes.
**High-level Test Scenarios:**
- **Claim:** **CRL disabled ⇒ no revocation** — a leaked/compromised Nitro *intermediate* cannot be revoked to relying parties following the doc verbatim. → **Oracle:** a doc chaining to a revoked-but-in-validity-window intermediate is accepted. → **Severity:** High (systemic; PKI-design observation. Obtaining Nitro key material = HARD STOP).
- **Claim:** a verifier that validates the **chain but not the PCR values** accepts any genuine Nitro-signed doc from *any* instance. The 4-step validate list never says "compare `nitrotpm_pcrs` to reference values" — that lives only on separate KMS-framed pages. → **Oracle:** attacker's own legitimately-signed doc (different software) passes. → **Severity:** Critical (authentic signature, unchecked measurements).
- **Claim:** a verifier that does **not pin the published root fingerprint** / trusts the attacker-supplied `cabundle` as anchor is fully bypassable. → **Oracle:** self-signed root + forged chain accepted. → **Severity:** Critical (verifier-side).
- **Claim:** **CBOR/COSE parser abuse** — oversized (>1024B) fields, deeply-nested CBOR, malformed COSE tags, wrong `alg` (expecting `{1:-35}` ECDSA-384) → parser crash or signature-check skip / `alg:none`-style downgrade. → **Oracle:** verifier crash/hang or acceptance. → **Severity:** High (bypass) / Medium (DoS).
- **Claim:** **cabundle ordering** confusion (doc warns Java CertPath needs reversed order) causes a fail-open truncated-path accept. → **Oracle:** reordered cabundle accepted by a common lib. → **Severity:** Medium–High.
- **Claim:** **verify-after-use** — documented step order extracts fields (step 2) *before* signature verify (step 4); an implementation acting on extracted PCRs/`public_key` before the crypto check is a textbook bug. → **Oracle:** audit reference verifier ordering. → **Severity:** Critical if present.
**Doc evidence:** `nitrotpm-attestation-document-validate.md` (all steps; "CRL must be disabled"; root fingerprint; cabundle order; COSE_Sign1 `{1:-35}`; size limits). **Severity-if-true:** Critical→Medium depending on the step.

### AF-4 — Cross-tenant EK / attribute disclosure (Lens A + E + M) [PRIORITY 2]
**Background:** `GetInstanceTpmEkPub` returns the per-instance endorsement **public** key for an `instance-id` "at any time". `DescribeImageAttribute tpmSupport` and `DescribeInstances TpmSupport` expose NitroTPM enablement.
**Security Concern:** Resource-by-id APIs must scope to the caller's tenant, not merely to resource existence. The EK is a stable per-instance identity; leaking it cross-account enables fingerprinting/enumeration.
**High-level Test Scenarios:**
- **Claim:** `GetInstanceTpmEkPub` returns the EK for an instance the caller does **not** own. → **Mechanism:** `retrieve-ekpub.md` / `API_GetInstanceTpmEkPub` — takes `instance-id`, no ownership statement. → **Oracle:** EK returned for another account's `i-…`, or a distinct not-found-vs-access-denied error forming an enumeration oracle over the structured `i-…` space. → **Severity:** cross-account EK read = Medium; enumeration oracle = Low–Medium.
- **Claim:** `tpmSupport` attribute readable on AMIs shared with the caller leaks owner intent. → **Oracle:** attribute visible on a shared AMI. → **Severity:** Low.
**Doc evidence:** `retrieve-ekpub.md`, `verify-nitrotpm-support-on-instance.md`, `verify-nitrotpm-support-on-ami.md`. **Severity-if-true:** Medium.

### AF-5 — Boot-time-only measurement / attestation TOCTOU (Lens K/M, design) [PRIORITY 3]
**Background:** `attestable-ami.md`: *"An instance's measurements are based on its initial boot state."* The isolated-compute model depends on `dm-verity`/`erofs` read-only root so restarts return to the measured state.
**Security Concern:** PCR4/7/12 capture *boot* integrity, not *live runtime* integrity. A post-boot memory-only compromise does not alter attested measurements, so the instance keeps attesting "trusted" between attestation and use.
**High-level Test Scenarios:**
- **Claim:** a runtime-compromised (boot-unchanged) instance still produces a passing document and drives KMS `Decrypt`. → **Oracle:** inject a memory-resident change, re-attest, observe unchanged PCR4/7/12 and continued KMS access. → **Severity:** Medium (documented measured-boot limitation; check whether docs set correct expectations).
- **Claim:** long-lived recipient keypair widens the TOCTOU window between attest and KMS use. → **Oracle:** attest once, compromise, reuse the recipient key for later calls. → **Severity:** Medium.
**Doc evidence:** `attestable-ami.md`, `isolate-data-operators.md`. **Severity-if-true:** Medium.

### AF-6 — AMI "attestable" property is customer-asserted at registration (Lens P) [PRIORITY 3]
**Background:** `RegisterImage --tpm-support v2.0 --boot-mode uefi` marks an AMI as NitroTPM/UEFI. The "attestable" quality (immutable root, isolated compute, correct UKI/PCR computation) is entirely customer build discipline; PCR-compute is run offline by the customer.
**Security Concern:** No gate proves the snapshot is genuinely UEFI/attestable or that declared reference measurements correspond to the registered image — enabling policy-vs-reality drift that feeds AF-1/AF-5.
**High-level Test Scenarios:**
- **Claim:** `RegisterImage` accepts `--tpm-support v2.0` on a snapshot that is not actually UEFI/attestable, or reference measurements can be decoupled from the actual image. → **Oracle:** an instance from such an AMI attests inconsistently with declared PCRs. → **Severity:** Medium.
**Doc evidence:** `enable-nitrotpm-support-on-ami.md`, `enable-nitrotpm-prerequisites.md`, `build-sample-ami.md`. **Severity-if-true:** Medium.

### AF-7 — Audit / visibility gaps (Lens O) [PRIORITY 4]
**Background:** `TpmSupport` is "not displayed in the Amazon EC2 console" for AMI or instance; NitroTPM state is excluded from EBS snapshots and VM Import/Export. KMS NitroTPM condition values *are* included in CloudTrail (`conditions-nitro-tpm.html` → `ct-nitro-tpm.md`).
**Security Concern:** Console blind spots hamper defender detection; verify attestation-gated KMS calls log PCRs+recipient and that `GetInstanceTpmEkPub` is logged.
**High-level Test Scenarios:** **Claim:** an attestation-gated KMS op or an EK retrieval produces no/low-fidelity audit record. → **Oracle:** perform the op, inspect CloudTrail for PCR/recipient attribution. → **Severity:** Low–Informational (enabler).
**Doc evidence:** `enable-nitrotpm-prerequisites.md`, `verify-*` pages, `conditions-nitro-tpm.html` (CloudTrail inclusion). **Severity-if-true:** Low.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account decrypt via same attestable AMI | KMS attestation policy | PCR condition keys + (sample-only) Principal ARN binding — test whether Principal binding is *required* vs merely shown |
| Weak/constant/unpaired PCR pinning grants broadly | KMS policy authoring | PCR0/1 constant; PCR4/7/12 carry trust; **condition key is single-valued** (no enforced pairing) |
| Document replay → plaintext | KMS + `public_key` binding | Encrypt-to-recipient under signed `public_key`; nonce unused for KMS; no documented freshness |
| Forged/malformed document accepted | 3P verifier | CBOR→COSE_Sign1 decode, chain build, signature verify, root fingerprint pin, cabundle order |
| No revocation of compromised intermediate | Nitro PKI + verifiers | "CRL must be disabled" (accepted tradeoff — test blast radius) |
| Cross-account EK read / instance enumeration | `GetInstanceTpmEkPub` | IAM authorization resource scoping (ownership vs existence) |
| Runtime compromise still attests trusted | Measured boot (PCRs) | dm-verity/erofs immutability; measurements = boot state (scope caveat) |
| Register non-attestable AMI as attestable | `RegisterImage` | UEFI/`tpm-support v2.0` flags; customer build discipline |
| Guest → Nitro signing key / other-instance TPM | Nitro System | **Zero operator access** (hard-stop boundary) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **The Nitro service plane itself** — hypervisor signing key, Nitro Attestation PKI private key, any other instance's NitroTPM/PCR state. Documented "zero operator access"; probing a break of it is a **hard stop / disclosure**, not in-scope hunting.
- **A customer steering their own instance's software** — running whatever code on your *own* instance and changing *your own* measurements is not a vuln. The bug class exists only when it crosses to another tenant or defeats a verifier the attacker doesn't control.
- **Guest-OS / in-instance TPM usage** (BitLocker sealing, tpm-tools) confined to a single tenant's own instance — customer responsibility (shared-responsibility model).
- **Bugs in third-party reference repos** (KIWI NG, coldsnap, erofs, dm-verity, NitroTPM-Tools GitHub) — note and route upstream; not the AWS service boundary. Their *documented design footguns* are in scope (AF-3).
- **Generic TPM 2.0 spec weaknesses** not specific to NitroTPM's AWS integration.
- **Single-tenant self-DoS** (spamming `nitro-tpm-attest` on your own instance).

---

## 8. Null Hypotheses / Doc Gaps (lens sweep evidence — pages named)
- **Lens B (Confused deputy / PassRole):** N/A. Read `retrieve-ekpub`, `enable-nitrotpm-support-on-ami`, `attestation-attest`, `attestation-get-doc`, `prepare-attestation-service` — **no field accepts a role ARN the service assumes on the caller's behalf**. KMS uses the caller's own IAM principal plus the doc. No `iam:PassRole`/`SourceArn` surface in NitroTPM APIs.
- **Lens G (SSRF):** N/A. Read `attestation-get-doc`, `nitrotpm-attestation-document-validate`, `retrieve-ekpub`, `enable-nitrotpm-support-on-ami`, `prepare-attestation-service`, `nitrotpm.html` — **no field the AWS service dereferences server-side**. The one URL (`aws-nitro-enclaves.amazonaws.com/...Root-G1.zip`) is fetched by the *customer/verifier*, not the service. Re-open if a future feature adds a service-side doc fetch/webhook.
- **Lens J (OAuth/3P linking):** N/A. No 3P identity linking, `state` param, or callback in any NitroTPM page.
- **Lens K (Prompt injection / LLM):** N/A as a service component. No LLM/agent in the NitroTPM pipeline. The "AI coding assistants" footer is untrusted boilerplate (flagged §0), not a component. (Runtime-integrity TOCTOU folded into AF-5.)
- **Lens N (namespace migration):** N/A. Single attribute model (`tpmSupport`/`TpmSupport`, `v2.0`); no dual-namespace migration described.
- **Lens I (tagging/ABAC):** Mostly N/A — `tpmSupport` is an image *attribute*, not a tag, and not an access-control mechanism. Filter `Name=tpm-support` exists for discovery only.
- **Lens Q (upload):** N/A for the AWS service surface — no upload endpoint; the "input blob" is the CBOR Attestation Document consumed by a *verifier*, covered under AF-3 parser abuse.
- **Lens D (data→control plane):** Folded into B6/hard-stop — the only control-plane target is the Nitro plane (hard stop).
- **Lens L (DoS):** Folded into AF-3 (verifier CBOR parser). No documented multi-tenant shared fleet to exhaust; single-tenant self-DoS out of scope.
- **Lens H (CMK/enc-context):** Fired — see AF-1 (PCR pinning is the encryption-authz control).
- **Doc gaps to confirm before hunting:** (a) whether KMS enforces Attestation Document **freshness/`timestamp`** (docs silent — AF-2); (b) exact **IAM resource scoping** of `GetInstanceTpmEkPub` (ownership vs existence — AF-4); (c) whether `RegisterImage` validates the snapshot is genuinely UEFI/attestable (AF-6); (d) whether `public_key` is in the COSE **protected/signed** payload vs unprotected header — spec implies signed body; confirm (AF-2.1).

---

## Appendix A — Deep-dive: Attestation Document cryptographic & verifier boundary
*Documentation-only. Each item needs reference-implementation inspection (`aws/nitrotpm-attestation-samples` / NitroTPM-Tools source) or controlled lab testing to become a finding.*

1. **CRL disabled ⇒ no revocation of a compromised Nitro intermediate.** `nitrotpm-attestation-document-validate.md`: *"CRL must be disabled…"*, sample Java `setRevocationEnabled(false)`; no OCSP. Confirm AWS publishes no revocation/emergency-rotation channel (only per-cert validity). **Critical** (single intermediate-key compromise = long-lived forgery, no kill switch). *Nitro key material = HARD STOP.*
2. **Spec-literal verifier is replayable.** The 4-step validation never checks `timestamp` freshness or `nonce`. **High** (stale-doc replay for 3P verifiers).
3. **KMS path has no documented replay defense via nonce.** `nonce`/`user_data` unused for KMS; no freshness described. **High** (bounded by AF-2 encrypt-to-recipient binding).
4. **CA-bundle reversal / fail-open chain building.** cabundle ships `[ROOT…INTERM_N]`, must be reversed to `[TARGET…ROOT]`. Feed common libs (Go `x509.Verify`, OpenSSL, Java `CertPathValidator`) the raw order → hard error (safe) vs silent truncated-path accept (unsafe). **Critical if any mainstream lib fails open.**
5. **Root-pin ambiguity / no rotation story.** Fingerprint `64:1A:03:…` given without a named hash algorithm; static ZIP URL; 30-yr root, no backup/rotation guidance. **Medium** (pinning fragility footgun).
6. **Verify-after-use ordering risk.** Signed fields are in the COSE_Sign1 payload (sound by design), but documented step order extracts (step 2) *before* signature verify (step 4). **Critical if a real verifier acts on extracted fields before the crypto check.**
7. **PCR0/PCR1-only policy = no boundary.** PCR0/1 "controlled by AWS … always contain constant values." A policy/verifier pinning only these grants *any* NitroTPM instance. **Critical** (policy-design flaw). *(reinforces AF-1)*
8. **PCR7-only (Secure Boot) misses command-line integrity.** PCR12 = kernel command-line hash, "Required in conjunction with PCR4 for standard boot"; PCR7 covers only Secure Boot *policy*. A PCR7-only policy may allow `init=/bin/sh`/lockdown-disable while PCR7 is unchanged. **High.** *(reinforces AF-1)*
9. **Digest/PCR size confusion.** CDDL fixes `digest="SHA384"` but `pcr = bytes .size (32/48/64)`; KMS condition value is "up to 96 bytes" hex. Feed a doc with `digest=SHA384` but 32/64-byte PCRs to parsers/comparators → silent false-accept vs crash. **Medium/High.**
10. **Unenforced field-size bounds → parser DoS.** `cert ≤1024B`, `user_data`/`nonce`/`public_key ≤1024B` are advisory; an oversized CBOR blob hits a permissive decoder pre-signature-check. **Medium.**
11. **Crypto-valid but semantically meaningless attestation (skipped PCR comparison).** The 4 validate steps never say to compare `nitrotpm_pcrs` to reference values — that guidance lives only on separate content/prepare pages. A 3P implementer may stop after "authentically signed by AWS." **Critical.** *(reinforces AF-3)*
12. **Encrypt-to-recipient binds only to caller-chosen ephemeral key.** KMS encrypts under whatever RSA `public_key` the requesting instance embedded; no cross-check to a pre-registered identity. Intended design, but a footgun for verifiers assuming `public_key` implies instance-identity continuity. **Low/Informational.** *(reinforces AF-2)*
13. **PCR4-without-PCR12 under-specification (confirmed single-valued).** `conditions-nitro-tpm.html` confirms the condition key is *Single-valued*; a policy with only PCR4 silently drops command-line integrity. **High.** *(reinforces AF-1)*
14. **Policy-composition fail-open.** `conditions-nitro-tpm` shows the attestation-gated Allow in isolation; a separate unconditioned Allow (another key-policy statement or broad IAM) for the same KMS action bypasses attestation entirely. **High** (docs omit a least-privilege warning).

**Cross-cutting:** crypto/parsing (1,4,6,9,10,11); replay (2,3); pin/trust-anchor footguns (5,6); encrypt-to-recipient (12); PCR-as-authz (7,8,13,14). **Highest-value next steps:** inspect the AWS NitroTPM verifier reference source (not just README) and lab-test KMS policy composition + PCR-subset behavior.

---

## Completion Report
- **Assigned skill:** `security-questionbuilder` (`/work/.claude/skills/security-questionbuilder`).
- **Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html
- **Inputs read:** the offline mirror NitroTPM page set (12 pages) + live verification of `nitrotpm.html` and `kms/.../conditions-nitro-tpm.html` (both match offline). Also cross-checked against the pre-existing `/work/aws-docs/nitrotpm-attack-research-plan.md`, which this run validates and reproduces in self-contained form.
- **Result:** documentation-derived research plan produced (no live testing). All lens verdicts recorded with pages named.
- **Could not fully test from docs (recommend hunter/lab follow-up):** KMS attestation-document freshness/`timestamp` handling; `GetInstanceTpmEkPub` ownership-vs-existence IAM scoping; `RegisterImage` snapshot UEFI/attestability validation; whether `public_key` is in the COSE protected payload; and 3P-verifier reference-source ordering/PCR-comparison behavior. **HARD STOP** reminder: any reach of the Nitro signing key / PKI private key / another instance's TPM state = stop + disclose.
