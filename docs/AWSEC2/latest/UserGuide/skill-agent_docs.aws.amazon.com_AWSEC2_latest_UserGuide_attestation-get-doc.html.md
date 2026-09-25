# NitroTPM `attestation-get-doc` — Attack Research Plan

**Source of leads:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-get-doc.html` (`.md` mirror confirmed identical, verified live 2026-09-23) + its two child pages `nitrotpm-attestation-document-content.md` and `nitrotpm-attestation-document-validate.md`, plus family siblings (`prepare-attestation-service`, `conditions-nitro-tpm`, NitroTPM hub, `attestable-ami`, `build-sample-ami`).
**Status:** documentation-derived hypotheses only; nothing tested against a live account. Skill: `security-questionbuilder`. Single-pass.
**Drift check:** Live == offline mirror, no drift 2026-09-23. **No "See also" / AI-agent injected `aws` CLI block on this page** (cf. the family injection pattern noted for other EC2 pages).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP** — preserve evidence and flag for AWS-Security the moment testing touches: the Nitro Hypervisor signing key, the Nitro Attestation PKI private key (CN=`aws.nitro-enclaves`, ~30-yr PCA root), **KMS's own attestation-document parser/validator**, or any attempt to *forge* a signed document and present it to production KMS. Reproducing the reference PCRs with the public `nitro-tpm-pcr-compute` tool and observing your **own** key-policy decision is in scope; minting a forged doc against prod KMS is not.

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Cross-account KMS decrypt via reproducible PCRs (crown jewel).** Demonstrate that an attacker in account B can satisfy an attestation-gated KMS key policy authored by account A, because the Attestation Document proves only *code measurements* (PCRs) + recipient-key possession — never *tenant/owner identity* — and the reference PCRs are attacker-reproducible from a shared/public Attestable AMI.
2. **Liveness / replay break.** Show that a captured Attestation Document + its private key from a terminated or cloned instance still validates under the AWS-KMS path, because `nonce` and `user-data` are documented as **not used for attestation with AWS KMS**.
3. **Validation-guidance weakness.** Show that the AWS-documented 3rd-party validation procedure (`setRevocationEnabled(false)` / CRL disabled; RSA-only recipient key with no floor) leaves a revoked-but-unexpired intermediate or a weak recipient key trusted.
4. **Parser / supply-chain integrity of the retrieval path.** Assess the CBOR/COSE document format and the `aws-nitro-tpm-tools` install channel as attacker-shapeable inputs to a 3rd-party verifier.

---

## 2. Components, Assets, and Design

**What this page is:** the *document-retrieval* leaf of the NitroTPM attestation family. It documents a **local Amazon Linux 2023 CLI utility**, `nitro-tpm-attest`, that returns a signed Attestation Document for the running EC2 instance. **There is NO EC2 control-plane API on this page** — the surface is a client-side binary + a CBOR/COSE document format + two downstream verifiers (AWS KMS built-in, or a customer 3rd-party service).

- **Customer-facing interface:** `/usr/bin/nitro-tpm-attest` (single command). No network endpoint, no SigV4 API. Output = CBOR-encoded, COSE_Sign1-signed Attestation Document.
- **Install channel:** `sudo yum install aws-nitro-tpm-tools` from the Amazon Linux 2023 repo; preinstalled in the sample AL2023 image (see `build-sample-ami.md`). → supply-chain trust in the AL repo signing.
- **Optional parameters (attacker-controllable inputs into the document):**
  - `public-key` — an **RSA-only** public key embedded in the doc; AWS KMS (or an external service) encrypts response plaintext under it and returns `CiphertextForRecipient`. Ensures only the private-key holder can decrypt. *No documented minimum size or padding scheme.*
  - `user-data` — arbitrary signed data for an agreed protocol with an external service. **"Not used for attestation with AWS KMS."**
  - `nonce` — challenge-response value to prove liveness to an *external* service. **"Not used for attestation with AWS KMS."**
- **Assets:** the signed Attestation Document (contains PCRs, timestamp, public-key, user-data, cabundle, COSE signature); the recipient RSA private key held by the instance; the KMS plaintext returned as `CiphertextForRecipient`; the KMS key policy's attestation condition keys.
- **Trust model (the core defect surface):** the document authenticates **measured code state (PCRs), not the tenant/account that produced it**. KMS authorization is a *policy condition* over PCR values; the PCR values for a given Attestable AMI are **reproducible by anyone who can read/launch that AMI** (public tool `nitro-tpm-pcr-compute`).

**Pipeline (conceptual):**
```
[EC2 instance / AL2023]                         [Verifier]
  RSA keypair (local) --pub--> nitro-tpm-attest
                                   | (TPM-measured PCRs + COSE_Sign1 sig
                                   |  over cabundle rooted at Nitro PKI)
                                   v
                           Attestation Document (CBOR)
                                   |
             +---------------------+----------------------+
             v                                            v
      AWS KMS (built-in)                        Customer 3P service
   - checks kms:RecipientAttestation:            - customer-authored validation
     NitroTPMPCR{n} in key policy                  (AWS sample: CRL disabled,
   - encrypts plaintext under doc's                 RSA recipient, PCR-subset)
     RSA pub -> CiphertextForRecipient          - nonce/user-data DO matter here
   - nonce/user-data IGNORED
```

**Related plans (do NOT duplicate):** broad NitroTPM hub / KMS key-policy sweep lives in the NitroTPM family plans (`nitrotpm-plan`, `nitrotpm-attestation-plan`, `attestable-ami-plan`, `iid-plan`, `conditions-nitro-tpm`). This leaf owns the retrieval-tool + document-format + validation-guidance slice.

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `nitro-tpm-attest` (CLI) | local exec | Existing (feature is relatively new) | No (read-only wrt instance) | Local to instance | Emits CBOR/COSE Attestation Document | No — on-box only | Any local process on the instance | No IAM. `public-key`/`user-data`/`nonce` optional inputs |
| `yum install aws-nitro-tpm-tools` | pkg install | Existing | Installs binary | AL2023 repo | Installs the utility | No | Local root | Supply-chain: AL repo signing |
| KMS `Decrypt`/`GenerateDataKey` w/ `Recipient` | API (elsewhere) | Existing | No | External-facing | Consumes the doc; returns `CiphertextForRecipient` | Yes (KMS endpoint) | Any principal the key policy allows | **Authz is the key policy's `kms:RecipientAttestation:NitroTPMPCR{n}` condition** — the real gate |
| `nitro-tpm-pcr-compute` (referenced tool) | local exec | Existing | No | Local | Computes expected PCRs for an AMI | No | Anyone with the AMI | **Makes reference PCRs attacker-reproducible** |

**Undocumented/console-hidden knob check:** the CLI exposes only three optional flags; the *authorization* surface is entirely in the KMS key policy condition keys (`conditions-nitro-tpm`): `kms:RecipientAttestation:NitroTPMPCR0..15`, single-valued, hex ≤96 bytes, `StringEqualsIgnoreCase`. The most-permissive dangerous authoring choices are: PCR-subset pinning, all-zero/wildcard PCR values, or omitting a tight `Principal`.

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Attacker account B instance | Account A's attestation-gated KMS key | Present a doc whose PCRs match A's key-policy condition | **KMS returns plaintext/`CiphertextForRecipient` to B** = cross-account decrypt break (Critical) |
| Terminated/cloned instance (past) | KMS now | Replay a captured doc + private key | **KMS validates a stale doc** (nonce/user-data ignored) = liveness/replay break |
| Revoked Nitro intermediate | 3P verifier trust chain | AWS doc says disable CRL / `setRevocationEnabled(false)` | **Revoked-but-unexpired cert still trusted** by verifier |
| Attacker-shaped CBOR/COSE doc | Customer 3P verifier (C/C++/Rust parser) | Malformed lengths/depths/offsets in CBOR fields | **Parser crash/UAF/OOB/hang** in 3P verifier (Med); KMS parser = HARD STOP |
| Malicious AL repo mirror / MITM | Instance installing tools | `yum install aws-nitro-tpm-tools` | **Unsigned/substituted binary executes** = supply-chain |
| Any customer surface | Nitro PKI private key / KMS validator | — | **HARD STOP** — AWS service-plane |

---

## 5. Recommended Areas of Focus (one block per firing lens)

### AREA 1 — ★★ Attestation-conditioned authorization: PCRs prove code, not tenant (Lens W) — CROWN JEWEL
**Background:** KMS authorizes an attestation-gated request by matching `kms:RecipientAttestation:NitroTPMPCR{n}` in the key policy against the PCR values in the presented Attestation Document. The document contains **no owner/account/tenant field** — only PCRs, a timestamp, the recipient public key, user-data, and the COSE signature chain.
**Security Concern:** the reference PCRs for a given Attestable AMI are **reproducible by anyone able to read/launch that AMI** via the public `nitro-tpm-pcr-compute` tool. If an account-A key policy pins only PCR values (with a loose or omitted `Principal`), an account-B attacker launching the same (shared/public) AMI produces a document with identical PCRs and satisfies the gate → cross-account decrypt.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A KMS key whose policy conditions only on `NitroTPMPCR{4,7,12}` (no tight `Principal`) authorizes a `Decrypt` from a *different account* whose instance runs the same Attestable AMI. → **Oracle:** account-B request returns `CiphertextForRecipient`/plaintext where the design implies only account A's workload should decrypt. **Severity: Critical.**
- **Claim (fail-open on absent attestation):** a `Decrypt` request carrying **no** attestation/`Recipient` is still authorized. → **Oracle:** 200 instead of `AccessDenied`. Fail-closed = deny. **High.**
- **Claim (PCR under-binding):** pinning only PCR4 (or PCR0) leaves kernel cmdline / app measurements (PCR12) free, so a modified workload with the same PCR4 still passes. → **Oracle:** doc with mismatched PCR12 authorizes. **High.**
- **Claim (all-zero / wildcard PCR):** `prepare-attestation-service` sample uses PCR12 = `"0000…"`; a key policy authored with all-zeros or `StringLike PCR:"…*"` matches a debug/uninitialized doc. → **Oracle:** zero/debug-PCR doc authorizes. **High.**
- **Claim (authoring-time schema validation):** `PutKeyPolicy` accepts a nonexistent `NitroTPMPCR99` or a wrong-length/odd measurement without error. → **Oracle:** `ValidationException` absent. **Medium (advisory-only gate).**
**Doc evidence:** `attestation-get-doc` ("verify the identity of the instance and prove it is running only trusted software"); `conditions-nitro-tpm` (single-valued, hex ≤96B, `StringEqualsIgnoreCase`); `prepare-attestation-service` (PCR12 `0000…` sample). **Severity-if-true: Critical.**
**Preconditions:** two accounts; a shared/public Attestable AMI; ability to author the victim-shaped key policy in a control account to isolate the defect. **Stop condition:** stop before touching any production KMS key you don't own; never forge against prod KMS.

### AREA 2 — ★ Liveness / replay: nonce & user-data ignored by KMS (Lens U / M)
**Background:** the page states verbatim that `nonce` and `user-data` are **"Not used for attestation with AWS KMS."** They exist only for a customer's *external* challenge-response protocol.
**Security Concern:** with KMS, the document proves *code measurement + possession of the recipient private key* but **not liveness**. There is a `timestamp` in the document but **no documented KMS staleness/freshness check**. A captured document plus its recipient private key — from a since-terminated or cloned instance — should therefore still validate.
**High-level Test Scenarios:**
- **Claim:** a document + private key captured from instance X (now terminated) still yields `CiphertextForRecipient` from KMS later. → **Oracle:** decrypt succeeds post-termination. **Severity: High (design), Info if AWS deems intended.**
- **Claim:** no documented upper bound on `timestamp` age is enforced by the KMS path. → **Oracle:** an old-timestamp doc authorizes. **Medium.**
- **Claim (nonce false-security):** a customer who *believes* nonce provides liveness against KMS is mistaken; confirm the doc does not surface this caveat prominently enough to prevent a compliance control being built on a false liveness assumption. **Info/Low.**
**Doc evidence:** `attestation-get-doc` `nonce`/`user-data` bullets. **Severity-if-true: High (AWS-owned design; likely Info–Medium after adjudication).**

### AREA 3 — ★ Validation-guidance weakness: CRL disabled + RSA-only recipient (Lens AA / Y / H)
**Background:** the child page `nitrotpm-attestation-document-validate` instructs `setRevocationEnabled(false)` ("CRL must be disabled"); the recipient key is **RSA-only** with **no documented minimum size or padding**.
**Security Concern:** the Nitro Attestation PKI root is a ~30-yr PCA; with revocation disabled, a **revoked-but-unexpired** intermediate/leaf stays trusted by any verifier following the AWS-published procedure. Separately, an unbounded RSA recipient key permits a weak (e.g. 512/1024-bit) key whose `CiphertextForRecipient` is crackable.
**High-level Test Scenarios:**
- **Claim:** the AWS sample validation code trusts a certificate that appears on a CRL because revocation is disabled per AWS instruction. → **Oracle:** verifier accepts a revoked (test) cert. **Med (High if the KMS built-in path also ignores revocation — verify carefully, do not attack KMS internals).**
- **Claim:** `nitro-tpm-attest --public-key` accepts a 512/1024-bit RSA key; `CiphertextForRecipient` under it is factorable/crackable. → **Oracle:** small-modulus key accepted, ciphertext recovered offline. **High if unbounded.**
- **Claim:** no padding scheme (OAEP vs PKCS#1v1.5) is specified → padding-oracle / Bleichenbacher exposure in a 3P verifier. → **Oracle:** decryption oracle behavior differs by padding. **Medium.**
**Doc evidence:** `nitrotpm-attestation-document-validate` (revocation-disabled guidance); `attestation-get-doc` ("Only RSA keys are supported"). **Severity-if-true: Medium–High.**

### AREA 4 — CBOR/COSE parser memory-safety + document field bounds (Lens F variant: native parser)
**Background:** the document is CBOR-encoded, COSE_Sign1-signed (ECDSA P-384, COSE tag 18), with explicit size/depth fields (cert 1..1024, user_data 0..1024, pcr 32/48/64 bytes, **unbounded cabundle**). A 3rd-party verifier parses this attacker-shapeable structure.
**Security Concern:** a C/C++/Rust CBOR/COSE parser that trusts an attacker-supplied length/depth/offset before bounds-checking is exposed to crash/UAF/OOB/hang; the **unbounded cabundle** invites resource exhaustion / deeply-nested parse.
**High-level Test Scenarios:**
- **Claim:** a document with an oversized/negative length field or a deeply-nested cabundle crashes or hangs a naïve 3P verifier. → **Oracle:** parser crash/hang on crafted doc. **Medium (single-verifier); the KMS built-in parser is HARD STOP — do not fuzz it.**
- **Claim:** field-size limits (cert 1..1024, user_data 0..1024) are not enforced by the sample verifier. → **Oracle:** over-limit field accepted. **Low–Medium.**
**Doc evidence:** `nitrotpm-attestation-document-content`. **Severity-if-true: Medium (3P verifier only). HARD STOP on KMS parser.**

### AREA 5 — Supply chain of the retrieval tool (Lens R/EE variant)
**Background:** `sudo yum install aws-nitro-tpm-tools` from the AL2023 repo; also baked into the sample AMI.
**Security Concern:** trust rests on AL repo GPG signing and TLS. A MITM/mirror-substitution or a compromised sample-AMI build step could ship a tampered `nitro-tpm-attest` that leaks the recipient private key or emits attacker-chosen docs.
**High-level Test Scenarios:**
- **Claim:** the install path does not enforce package signature verification in some documented configuration. → **Oracle:** unsigned/substituted package installs. **Medium (TOFU/supply-chain).**
- **Claim:** the sample AMI build (`build-sample-ami`) fetches the tool over an unpinned channel. → **Oracle:** build step lacks integrity pin. **Low–Medium.**
**Doc evidence:** `attestation-get-doc` install section; `build-sample-ami`. **Severity-if-true: Medium.** Note: attacking the AL repo infra itself is out of scope / service-plane.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account decrypt via reproduced PCRs | KMS key policy + doc | "verify the identity of the instance" — but doc carries no tenant identity; `conditions-nitro-tpm` PCR match only |
| Replay of stale/cloned-instance doc | KMS attestation path | nonce/user-data "Not used for attestation with AWS KMS"; timestamp present, no documented staleness check |
| Revoked-but-unexpired cert trusted | 3P verifier | AWS guidance `setRevocationEnabled(false)` |
| Weak/small RSA recipient key | `--public-key` handling | "Only RSA keys are supported" — no size/padding floor documented |
| CBOR/COSE parser corruption/DoS | 3P verifier / KMS parser | Field bounds documented (cert/user_data/pcr); cabundle unbounded |
| Tampered tool install | `aws-nitro-tpm-tools` pkg | AL repo signing (assumed) |

---

## 7. Out-of-Scope Risk Categories
- The Nitro Hypervisor signing key, Nitro Attestation PKI private key, and **KMS's own document parser/validator** — HARD STOP, service-plane.
- Forging a signed document against production KMS.
- Attacking Amazon Linux repository infrastructure itself.
- IMDS on the managed host; single-tenant self-DoS from a local process; a customer authoring their own weak KMS key policy is a footgun *unless* AWS's own sample (`prepare-attestation-service` all-zero PCR12, validate-page CRL-disabled) induces it — those samples are **AWS-authored, in scope (Tier-2)**.
- The broad NitroTPM hub / general KMS key-policy sweep (covered by sibling family plans).

## 8. Null hypotheses / doc gaps
Pages checked for triggers: `attestation-get-doc`, `nitrotpm-attestation-document-content`, `nitrotpm-attestation-document-validate`, `prepare-attestation-service`, `conditions-nitro-tpm`, NitroTPM hub, `attestable-ami`, `build-sample-ami`.
- **Lenses A, B, C, D, E, I, J, K, N, O, P, T, V, X, BB, CC, DD, FF = N/A** — this is a client-side local CLI + document format + validation guidance. No control-plane API, no role/ARN passed, no server-side fetch/URL, no tenant-id request field, no upload endpoint, no network fleet, no HTTP/token/session layer on this page. (Cross-account authz risk manifests at the *KMS* boundary, captured under Lens W above, not as an IDOR on this page.)
- **Firing lenses: W (crown), U, M, AA, Y, H, F, R/EE (supply chain), L (unbounded cabundle DoS).**
- **Doc gaps to confirm on a live account first:** (1) whether the KMS built-in path enforces any `timestamp` freshness (not documented); (2) whether `--public-key` enforces a minimum RSA modulus size / padding scheme; (3) whether `PutKeyPolicy` schema-validates `NitroTPMPCR{n}` value length and key existence; (4) whether the KMS built-in validator honors revocation independently of the customer verifier.
- **No injection block** present on this page (family "See also" AI-agent injection pattern not observed here).

---
### Handoff note for the next agent
Everything needed to execute is above; the *single highest-value test* is **AREA 1** — stand up a control-account KMS key gated on `NitroTPMPCR{4,7,12}` and prove (or refute) that a second account running the same Attestable AMI satisfies the gate. If it does, that is a cross-account decrypt (Critical) and the crown jewel of the whole NitroTPM family. AREA 2 (replay) and AREA 3 (CRL/RSA) are strong secondary leads that need no cross-account setup. Do NOT fuzz or forge against production KMS.
