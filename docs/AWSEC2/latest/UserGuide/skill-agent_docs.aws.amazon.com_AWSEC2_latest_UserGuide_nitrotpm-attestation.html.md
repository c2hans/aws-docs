# Amazon EC2 Instance Attestation (NitroTPM) — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-attestation.html
**Source of leads (all read, offline mirror + live cross-check 2026-09-13):**
`nitrotpm-attestation.md` (hub) · `attestation-attest.md` (KMS integration) · `prepare-attestation-service.md` (KMS key-policy sample) · `attestation-get-doc.md` (`nitro-tpm-attest` utility) · `nitrotpm-attestation-document-content.md` (PCR map) · `nitrotpm-attestation-document-validate.md` (3P validation flow) · `attestable-ami.md` · `isolate-data-operators.md` · `enable-nitrotpm-prerequisites.md` · live `kms/latest/developerguide/conditions-nitro-tpm.html`.
**Status:** documentation-derived hypotheses only. Nothing tested against a live account. This plan is the **attestation-hub** slice; it stands alone but shares crown jewels with the parent-page plan at `/work/aws-docs/nitrotpm-attack-research-plan.md` — read both before hunting to avoid duplicate work. Where they overlap, this file is the more current (adds live KMS-conditions-page semantics confirmed 2026-09-13).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity → Stop condition.** Section 5 is priority-ordered.
- **HARD STOP:** the moment evidence shows the Nitro Hypervisor signing key, the Nitro Attestation PKI private key, another instance's NitroTPM/PCR state, or any AWS service-plane credential/identity — stop, preserve evidence, flag for AWS-Security disclosure. The Nitro system is documented "zero operator access" (`isolate-data-operators.md`); a break of it is disclosure, not in-scope hunting.
- **Injection note:** the attestation doc pages do **NOT** carry the `## See also` / `aws agent-toolkit search-skills` prompt-injection block that other EC2 doc pages carry (offline mirror + live checked). No untrusted-directive block present on these pages. (Contrast: the parent `nitrotpm.html` family; see memory `aws-docs-see-also-injection`.)

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Attestation ≠ ownership:** satisfy a NitroTPM-gated KMS key policy from an account/instance that is *not* the key owner, by launching the same Attestable AMI and producing a document with matching PCRs → obtain `Decrypt`/`GenerateDataKey` output the owner intended to be reachable only from their own attested workload.
2. **Weak-PCR / partial-PCR grant:** prove that a policy pinned to an incomplete PCR set (only PCR4, or PCR0/PCR1 constants, or PCR12=all-zeros) grants far more broadly than the author intended (modified kernel command line, different boot binaries, or any NitroTPM instance).
3. **Document replay / freshness bypass:** replay a legitimately-attested victim's Attestation Document to a verifier (KMS or 3P) that does not enforce freshness → obtain crypto output.
4. **Break the encrypt-to-recipient binding:** substitute/omit the `public_key` in a document so `CiphertextForRecipient` decrypts under an attacker-held private key.
5. **Third-party verifier bypass:** exploit a custom verifier built per the doc's instructions (CRL disabled → no revocation, COSE `alg` trusted from untrusted header, root not pinned, PCRs unchecked, unsafe CBOR/COSE parsing) into accepting a bad/forged document.
6. **AWS-authored sample-policy defect:** show that a customer copying the AWS-published KMS key-policy sample verbatim inherits a weaker grant than the surrounding prose promises (single-PCR sample; all-zeros PCR12).

---

## 2. Components, Assets, and Design

**Customer-facing interfaces / actors**
- **In-guest utility `nitro-tpm-attest`** (pkg `aws-nitro-tpm-tools`, in `/usr/bin/`): produces a signed Attestation Document. Optional params: `--public-key` (**RSA only** — recipient encryption key), `--user-data` (protocol payload; **"Not used for attestation with AWS KMS"**), `--nonce` (challenge/response freshness; **"Not used for attestation with AWS KMS"**). Output = CBOR-encoded, COSE_Sign1-signed blob. Non-SDK, guest-local, callable by anyone on the instance.
- **Build-time utility `nitro-tpm-pcr-compute`**: computes reference PCR4/PCR7/PCR12 from the Unified Kernel Image (UKI) produced by KIWI NG. **Publicly available** → anyone can compute the reference measurements of any (public/shared/reproducible) Attestable AMI.
- **AWS KMS** — the built-in verifier. On `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom` with a `Recipient`-attached signed document, it matches the document's PCRs against `kms:RecipientAttestation:NitroTPMPCR<n>` and, on match, encrypts the plaintext under the document's `public_key`, returning `CiphertextForRecipient`.
- **Third-party verifier** — any external service the customer builds per `nitrotpm-attestation-document-validate.md` (KMS is optional; the doc explicitly supports rolling your own).

**Behind the interface (AWS service plane — HARD STOP zone)**
- **NitroTPM** — per-instance virtual TPM in the Nitro System; holds PCRs.
- **Nitro Hypervisor** — **signs** the Attestation Document (COSE_Sign1, ECDSA-384 / `{1:-35}`, digest SHA384).
- **Nitro Attestation PKI** — root CA (`CN=aws.nitro-enclaves, C=US, O=Amazon, OU=AWS`), 30-yr AWS Private CA key, root at `aws-nitro-enclaves.amazonaws.com/AWS_NitroEnclaves_Root-G1.zip`, fingerprint `64:1A:03:21:...:BB:5B`.

**Attestation Document spec** (`nitrotpm-attestation-document-validate.md`):
```
AttestationDocument = { module_id, timestamp (ms since epoch, uint .size 8),
  digest="SHA384", nitrotpm_pcrs:{index(0..31)=>pcr(32/48/64B)},
  certificate (DER 1..1024B), cabundle [ROOT..INTERM_N],
  ? public_key (DER, user_data 0..1024B), ? user_data (0..1024B), ? nonce (0..1024B) }
```
COSE_Sign1 array: `[protected, unprotected, payload, signature]`, tag 18, alg `{1:-35}`.

**PCR semantics** (`nitrotpm-attestation-document-content.md`):
- **PCR0/PCR1 = constant, AWS-controlled** ("will always contain constant values").
- **PCR4** = Boot Manager Code (boot-binary hash; embeds forward-locking hashes).
- **PCR7** = Secure Boot Policy (hash of UEFI Secure Boot policy/cert; the only PCR that can bind a *customer-private* signing cert → the only PCR giving genuine per-customer binding, and only while the cert stays private).
- **PCR12** = hash of the kernel **command line** ("Required in conjunction with PCR4 for standard boot to validate the command line was not modified").
- PCR8–15 OS-defined, PCR16 debug, PCR23 app.

**Attestable-AMI integrity model** (`attestable-ami.md`): measurements = **initial boot state only**. Instances must return to original boot state on restart via `erofs` (in-memory writes, discarded on reboot) + `dm-verity` (filesystem integrity hash stored in kernel command line → covered by PCR12). Base OS: Amazon Linux 2023 or NixOS; UEFI required.

### ASCII pipeline
```
 BUILD (customer, offline)          RUNTIME (in guest)                VERIFY (KMS or 3P)
 KIWI NG image desc                 nitro-tpm-attest                  KMS: match PCRs vs
   -> UKI -> nitro-tpm-pcr-compute    --public-key(RSA)                 kms:RecipientAttestation:
   -> reference PCR4/7/12             --user-data(3P only)              NitroTPMPCR<n>
        |                             --nonce(3P only)                  on match: encrypt reply
        v                                  |                            under public_key ->
   KMS key policy condition keys           v                           CiphertextForRecipient
                              guest PCRs -> [NitroTPM] -> doc           ------------------------
                                            |                          3P: decode CBOR/COSE_Sign1,
                              [Nitro Hypervisor SIGNS] (SERVICE PLANE)   verify chain to pinned
                                                                         root, CRL DISABLED,
                                                                         check PCRs + optional nonce
```

---

## 3. Trust-Boundary Map

| # | From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle (observable) |
|---|---|---|---|---|
| B1 | Instance guest (owner) | Owner's NitroTPM-gated KMS key | Attestation doc + PCR condition | KMS returns plaintext/`CiphertextForRecipient` when the running software does **not** match the pinned PCRs → measurement/policy bypass |
| B2 | **Account B** instance | **Account A**'s NitroTPM-gated KMS key | Same Attestable AMI ⇒ same PCR4/7/12 satisfies A's PCR-only condition | Account B obtains `Decrypt` output from A's key. **Attestation ≠ ownership. Cross-account = Critical** |
| B3 | Attacker replaying captured doc | KMS or 3P verifier | Signed doc is a bearer credential; `nonce` unused for KMS; freshness unstated | A doc captured earlier from a still-attesting victim is accepted → crypto output |
| B4 | Customer copying AWS sample policy | Intended "only attested workload" guarantee | AWS-published KMS sample pins **only PCR4** (conditions page) / **PCR12=all-zeros** (prepare page) | A workload with a modified command line / empty command line still decrypts → AWS-authored artifact weaker than prose |
| B5 | Attacker with attacker-built AMI | 3P verifier | Verifier follows doc verbatim (CRL disabled, alg from header, root unpinned) | Verifier accepts attacker's own Nitro-signed doc, a revoked-cert chain, or an alg-downgraded/forged doc |
| B6 | Post-boot runtime attacker | "Trusted" attestation verdict | PCRs = boot-time only | Runtime-compromised (boot-unchanged) instance keeps producing a passing document (TOCTOU) |
| B7 | Instance guest / data path | **Nitro Hypervisor key / Nitro PKI key / other instance's TPM state** | (attempted) guest→Nitro escape | ANY reach = **HARD STOP** service-plane breach |

---

## 4. API / Interface Inventory

| Name | Kind | Mutating | Facing | Functionality | Internet-callable | Authorized callers | Notes / lens |
|---|---|---|---|---|---|---|---|
| `nitro-tpm-attest --public-key/--user-data/--nonce` | In-guest utility (not an AWS API) | No | Guest-local | Produce signed Attestation Document | No (local) | Anyone on the instance | Non-SDK. `nonce`/`user_data` **unused for KMS**. RSA-only recipient key. → C/M/W |
| `nitro-tpm-pcr-compute` | Build-time utility | No | Offline | Compute reference PCR4/7/12 from UKI | No | Anyone (public tool) | **Reference measurements are attacker-computable** → B2/H/W |
| KMS `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom` (with `Recipient`) | KMS API | No (crypto) | External | Attestation-gated crypto; returns `CiphertextForRecipient` | Yes | IAM identity + key policy + `kms:RecipientAttestation:NitroTPMPCR<n>` | The core verifier. Fails **closed** on absent attestation (see AF-2). → H/M/C/W |
| `kms:RecipientAttestation:NitroTPMPCR<PCR_ID>` condition key | KMS policy element | n/a | Policy | Gate crypto on PCR match | n/a | Policy authors | **Single-valued**; lower-case hex ≤96 bytes; `StringEqualsIgnoreCase`; PCR4/7/12 only in samples. → R/S/U/W |
| 3P verifier (custom) | Customer-built | n/a | External | Parse/validate CBOR/COSE doc | Depends | Customer | Doc gives verbatim recipe incl. "CRL must be disabled". → F/M/Q/Y |

**Doc-flagged leads to keep verbatim:**
- "PCR0 and PCR1 … will always contain constant values."
- "`nonce` … **Not used for attestation with AWS KMS**." / "`user-data` … Not used for attestation with AWS KMS."
- "**CRL must be disabled** when doing the validation." / `validationParameters.setRevocationEnabled(false)`.
- "If the request does not include an attestation document, **permission is denied** because this condition is not satisfied." (KMS fail-closed on absent — confirmed live 2026-09-13).
- "The PCR value must be a **lower-case hexadecimal string of up to 96 bytes**." / condition key is **Single-valued**.
- conditions-page sample: `Condition` gates on **PCR4 only**. prepare-page sample: PCR4 **and** PCR12=`0000…` (all-zeros).
- "Only RSA keys are supported" for the recipient `--public-key`.

---

## 5. Recommended Areas of Focus (priority-ordered)

### AF-1 — Attestation authenticates code, not tenant → cross-account KMS access (Lens W + A + H) [PRIORITY 1] ⭐ CROWN JEWEL
**Background:** A NitroTPM KMS policy gates crypto on PCR values in a signed Attestation Document. Reference PCRs are computed by the **public** `nitro-tpm-pcr-compute` tool from an AMI; PCR0/PCR1 are constant AWS values. The attestation mechanism binds *which code booted*, signed by Nitro — it does **not** bind *which AWS account/instance owns the workload*.
**Security Concern:** Tenant isolation therefore rests entirely on (a) the KMS policy `Principal` and (b) the *secrecy/uniqueness* of the pinned reference measurements. PCR4/PCR12 are AMI-deterministic and reproducible by anyone (public tooling + reproducible KIWI NG builds). PCR7 binds a customer-private Secure Boot cert (real per-tenant binding **only while the cert stays private**). If a customer authors a policy that relies on PCR4/PCR12 without a *self-owned* `Principal` (e.g. `Principal:"*"`, a broad Org/OU, or a role in another account), any account launching the identical Attestable AMI produces matching PCRs and satisfies the condition.
**High-level Test Scenarios:**
- Claim: a policy whose only gate is `kms:RecipientAttestation:NitroTPMPCR{4,12}` with an over-broad `Principal` is satisfiable by a *different* account running the identical AMI. → **Oracle:** account B, running the same reproducible Attestable AMI, gets a successful `Decrypt` against account A's key. → **Severity:** cross-account data access = **Critical**.
- Claim: a policy pinned only to **PCR0/PCR1** (documented constant) grants **every** NitroTPM instance. → **Oracle:** any attestable instance satisfies it. → **Severity:** High (universal grant).
- Claim: **PCR7-only** vs **PCR4/12** coverage divergence — a PCR7-only policy accepts any instance presenting the same Secure Boot policy cert regardless of boot binaries/command line, and a PCR4-only policy accepts any command line. → **Oracle:** a differently-built AMI sharing the pinned PCR but not the others still decrypts. → **Severity:** High.
**Doc evidence:** `prepare-attestation-service.md`; `nitrotpm-attestation-document-content.md`; `attestable-ami.md`; conditions-nitro-tpm.html. **Severity-if-true:** Critical (cross-account) / High (weak PCR set).
**Owner-to-fix:** shared — the *mechanism* (attestation≠ownership) is AWS design; a customer policy omitting `Principal` scoping is a customer footgun, BUT test whether AWS docs adequately warn (they show a bound `Principal` but never state it is *required*). File the doc-guidance gap as Low/Informational (Lens U) alongside any live cross-account confirmation.
**Stop condition:** if a cross-account decrypt succeeds against a key you do not own without consent, stop at minimal proof; do not exfiltrate.

### AF-2 — Document replay & encrypt-to-recipient binding (Lens M + C + W) [PRIORITY 1] ⭐
**Background:** For the KMS path, `nonce` and `user_data` are **explicitly unused**. The KMS gate does **fail closed** on an *absent* document ("permission is denied because this condition is not satisfied" — confirmed live). So the residual replay defense is: (1) KMS encrypts the reply under the document's `public_key` (`CiphertextForRecipient`), readable only by the matching private key; (2) any freshness KMS enforces via `timestamp` (undocumented).
**Security Concern:** The replay defense hinges on `public_key` being **inside the signed COSE_Sign1 payload** (unforgeable) and on KMS refusing stale/attacker-substituted `public_key`s.
**High-level Test Scenarios:**
- Claim: `public_key` is in the signed body, so swapping it breaks the Nitro signature → a replayed doc yields ciphertext only the *original* instance can read. → **Oracle:** modify `public_key`, re-encode, submit — expect signature-verify failure. If a swapped `public_key` is accepted → **Critical** (replay → plaintext exfil).
- Claim: KMS enforces **freshness** so an old captured doc is rejected. → **Mechanism:** `timestamp` present but KMS docs silent; `nonce` unused. → **Oracle:** replay a document captured hours earlier from a still-valid instance; acceptance ⇒ freshness unenforced (bounded only by recipient-encryption). → **Severity:** Medium–High.
- Claim: for **3P** verifiers, the optional `nonce` being omitted makes replay trivial. → **Oracle:** a 3P verifier without a nonce challenge accepts a replayed doc. → **Severity:** High (verifier-dependent).
**Doc evidence:** `attestation-attest.md`, `attestation-get-doc.md`, `nitrotpm-attestation-document-validate.md`. **Severity-if-true:** Critical if binding broken; High for 3P replay.

### AF-3 — AWS-authored KMS sample-policy defects (Lens R + S + U) [PRIORITY 1] ⭐ (Tier 2, reportable)
**Background:** The docs print two KMS key-policy samples a customer is told to copy. These are AWS-authored artifacts — a weak default in them is AWS's defect, not a customer footgun.
**Security Concern:**
- The **conditions-nitro-tpm.html** example (`data-processing` role) gates on **PCR4 only** — it omits PCR12, which the content page says is "**Required in conjunction with PCR4 … to validate the command line was not modified**." A customer copying it authorizes any workload with the same boot binary regardless of kernel command line (dm-verity root hash lives in the command line → PCR12 covers filesystem-integrity args).
- The **prepare-attestation-service.md** example pins PCR12 = **all-zeros** (`0000…`, 48 bytes). An all-zeros PCR is the *never-extended* sentinel value. Question: is all-zeros a legitimate reference measurement, or does it trivially match any instance whose PCR12 was not extended → an inert command-line gate?
**High-level Test Scenarios:**
- Claim: the PCR4-only sample authorizes a workload with a modified/attacker-controlled kernel command line. → **Oracle:** launch an AMI with matching PCR4 but different PCR12 (altered command line) → `Decrypt` succeeds under the PCR4-only policy. → **Severity:** Medium–High (integrity gate omitted in AWS sample).
- Claim: pinning PCR12=all-zeros is satisfied by any instance that never extends PCR12. → **Oracle:** produce a document with PCR12 all-zeros; policy match despite arbitrary command line. → **Severity:** Medium.
- Claim (Lens S): the condition key is **single-valued**, so a policy cannot require a *set* of acceptable PCR4 values, and nothing enforces PCR4+PCR12 *pairing* — the author must remember to add both. The sample teaches only one. → **Oracle:** policy-authoring review + `iam:SimulateCustomPolicy` with a PCR4-match/PCR12-mismatch document context. → **Severity:** Low–Medium (guidance/enforcement gap).
**Doc evidence:** conditions-nitro-tpm.html (PCR4-only sample); `prepare-attestation-service.md` (PCR12=all-zeros); `nitrotpm-attestation-document-content.md` (PCR12 "Required in conjunction with PCR4"). **Severity-if-true:** Medium–High. **Route `aws-security` (Tier 2 — AWS-published sample copied verbatim).**

### AF-4 — Third-party verifier footguns (Lens F + M + Q + Y) [PRIORITY 2]
**Background:** The doc hands customers a verbatim recipe for building their own verifier. Several steps are dangerous defaults.
**High-level Test Scenarios:**
- Claim: **CRL disabled ⇒ no revocation** — `setRevocationEnabled(false)` is mandated, so a compromised/revoked Nitro intermediate cannot be revoked to relying parties following the doc. → **Oracle:** a doc chaining to a revoked-but-in-validity-window intermediate is accepted. → **Severity:** High (systemic; contingent on AWS PKI compromise — note as PKI-design observation; **HARD STOP** if you obtain Nitro key material).
- Claim: **COSE `alg` from the untrusted protected header** — a verifier that reads `{1:-35}` from the document instead of pinning ES384 is open to algorithm confusion / downgrade / `alg:none`-style bypass. → **Oracle:** submit a doc with a swapped `alg`/removed signature; acceptance ⇒ bypass. → **Severity:** High.
- Claim: verifier validates the **chain but not the PCR values** → any genuine Nitro-signed doc (incl. attacker's own instance) passes. → **Oracle:** attacker's own legit-signed doc (different software) accepted. → **Severity:** High.
- Claim: verifier does **not pin the published root fingerprint** / trusts the attacker-supplied `cabundle` as anchor → full bypass. → **Oracle:** self-signed root + forged chain accepted. → **Severity:** Critical (verifier-side).
- Claim: **cabundle ordering** confusion (doc warns Java CertPath needs reversed order) makes a verifier build/validate an attacker-influenced path. → **Oracle:** reordered cabundle accepted. → **Severity:** Medium–High.
- Claim: **CBOR/COSE parser abuse** — fields exceeding `≤1024B`, deeply-nested CBOR, malformed COSE tag 18, oversized `pcr` (>64B) → crash/hang or signature-check skip. → **Oracle:** verifier crash/hang or acceptance. → **Severity:** High (bypass) / Medium (DoS).
**Doc evidence:** `nitrotpm-attestation-document-validate.md` (all validation steps, "CRL must be disabled", root fingerprint, cabundle order, COSE_Sign1 `{1:-35}`, size limits). **Severity-if-true:** Critical→Medium by step. **Note:** bugs in a *specific* customer's verifier are out of scope; the reportable target is whether the **AWS-published recipe itself teaches an unsafe default** (CRL-disabled with no compensating guidance; no instruction to pin `alg`).

### AF-5 — Attestable-AMI supply chain & attestable-state integrity (Lens Q + P) [PRIORITY 2]
**Background:** The "attestable" quality is entirely the customer's build discipline. AWS ships a sample KIWI NG image description and sample repos (`aws/NitroTPM-Tools`, `aws/nitrotpm-attestation-samples`). Attestable state depends on `erofs` (in-memory writes discarded on reboot) + `dm-verity` (integrity hash in the kernel command line → PCR12).
**High-level Test Scenarios:**
- Claim: a compromised/typo-squatted sample image description or a poisoned `aws-nitro-tpm-tools` package silently changes the built binaries → PCRs still "match" a reference the attacker also controls (supply-chain, not a KMS bug). → **Oracle:** diff the built UKI vs the reference the policy pins. → **Severity:** Medium (customer supply chain; note if AWS sample repos lack pinning/signing guidance).
- Claim: if `erofs`/`dm-verity` are misconfigured, persistent post-launch writes change PCRs and *break* attestation (availability) — or, worse, a writable path lets an attacker alter code without changing the measured command-line hash. → **Oracle:** persist a change across reboot; observe PCR drift vs. continued attestation. → **Severity:** Medium.
- Claim: dm-verity root hash is in the kernel command line → **only PCR12 covers filesystem integrity**; a policy omitting PCR12 (see AF-3) does not attest the root filesystem contents at all. → **Oracle:** modify root FS, keep PCR4, decrypt under PCR4-only policy. → **Severity:** Medium–High (chains into AF-3).
**Doc evidence:** `attestable-ami.md`, `build-sample-ami.md`, `create-pcr-compute.md`. **Severity-if-true:** Medium–High.

### AF-6 — Boot-time-only measurement / attestation TOCTOU (Lens M, design) [PRIORITY 3]
**Security Concern:** PCR4/7/12 capture boot integrity, not live runtime integrity. A post-boot, memory-only compromise does not alter measured PCRs, so the instance keeps attesting "trusted" between attestation and KMS use.
**High-level Test Scenarios:**
- Claim: a runtime-compromised (boot-unchanged) instance still produces a passing document and drives `Decrypt`. → **Oracle:** inject a memory-resident change, re-attest, observe unchanged PCR4/7/12 and continued KMS access. → **Severity:** Medium (documented measured-boot limitation; check AWS docs set correct expectations for "isolated compute environment" claims in `isolate-data-operators.md`).
- Claim: long-lived recipient keypair widens the attest→use window. → **Oracle:** attest once, compromise, reuse recipient key for later KMS calls. → **Severity:** Medium.
**Doc evidence:** `attestable-ami.md` ("measurements are based on its initial boot state"), `isolate-data-operators.md`. **Severity-if-true:** Medium.

### AF-7 — Audit / visibility (Lens O) [PRIORITY 4]
**Security Concern:** Confirm attestation-gated KMS calls are fully logged with PCR/recipient attribution.
**High-level Test Scenarios:** Claim: an attestation-gated KMS op produces an audit record lacking PCR/recipient detail. → **Oracle:** perform the op, inspect CloudTrail (`ct-nitro-tpm.md`); the conditions page states the PCR value "is also included in CloudTrail events." → **Severity:** Low–Informational.
**Doc evidence:** conditions-nitro-tpm.html, `ct-nitro-tpm.md`. **Severity-if-true:** Low.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account decrypt via same Attestable AMI | KMS attestation policy | PCR condition keys + (sample) `Principal` ARN binding — test whether the `Principal` binding is *required* vs merely shown; PCRs are attacker-computable |
| Weak/partial PCR pinning grants broadly | KMS policy authoring | PCR0/1 constant; PCR4/7/12 carry trust; single-valued key; AWS sample pins PCR4-only / PCR12=all-zeros |
| Document replay → plaintext | KMS + `public_key` binding | Encrypt-to-recipient under signed `public_key`; `nonce`/`user_data` unused for KMS; freshness undocumented |
| Absent-attestation request | KMS gate | "permission is denied because this condition is not satisfied" — fail-closed (confirmed; treat as likely-true, still verify) |
| 3P verifier bypass | Custom verifier (doc recipe) | Chain-to-pinned-root, PCR match — but CRL disabled, alg from header, ordering caveat |
| Attestable-AMI supply chain | KIWI NG image desc / sample repos / `aws-nitro-tpm-tools` | Reproducible build + `nitro-tpm-pcr-compute`; erofs/dm-verity immutability |
| Runtime compromise still attests trusted | Measured boot (PCRs) | dm-verity/erofs immutability; measurements = boot state (scope caveat) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **The Nitro service plane** — Nitro Hypervisor signing key, Nitro Attestation PKI private key, any other instance's NitroTPM/PCR state. "Zero operator access" (`isolate-data-operators.md`); probing for a break is a **hard stop / disclosure**.
- **Customer-authored KMS policies** that omit `Principal` scoping — a customer footgun (report only the AWS doc-guidance gap, Lens U), distinct from the AWS-authored *sample* defects in AF-3 (in scope).
- **Bugs in a specific customer's 3P verifier** — out of scope; the in-scope target is whether the AWS-published verifier *recipe* teaches an unsafe default.
- **Third-party sample repos** (`aws/NitroTPM-Tools`, `aws/nitrotpm-attestation-samples`) code bugs — note supply-chain guidance gaps only.
- **Single-tenant self-DoS** (misconfigured erofs/dm-verity breaking one's own attestation) — availability footgun, low priority.
- **IMDS / host management on the managed Nitro host** — service plane.

---

## 8. Null Hypotheses / Doc Gaps (lens sweep evidence)
- **Lens W fail-open on absent attestation — REFUTED for KMS path.** conditions-nitro-tpm.html states absent attestation → deny. Residual W surface = *partial/weak* PCR sets (AF-1/AF-3) and *malformed/wildcard* values: **still open** — test whether `PutKeyPolicy` accepts a bogus PCR id (`NitroTPMPCR99`), a wrong-length value (not 96-byte hex), or whether `StringLike` wildcards (`PCR4:"abc*"`) are honored. (Pages checked: conditions-nitro-tpm.html, `prepare-attestation-service.md`.)
- **Lens B/PassRole — N/A on the attestation surface.** No API on these pages accepts a role ARN the service assumes; the KMS `Principal` is a policy element, not a passed role. (Pages checked: all 8 sub-pages + conditions page.)
- **Lens G/SSRF — N/A.** No field the service dereferences server-side; `--public-key`/`--user-data`/`--nonce` are opaque bytes embedded in a signed doc, not URLs. (Pages checked: `attestation-get-doc.md`, `attestation-attest.md`.)
- **Lens D/V network segmentation — N/A on this page** (no ENI/control-plane surface described here); covered by the parent nitrotpm plan / instance-networking plans.
- **Lens N/AA/I/J/K — did not fire.** No namespace migration, no share/revoke lifecycle, no tagging/ABAC, no OAuth, no LLM/agent on these pages.
- **Doc gap:** KMS freshness/replay behavior for a captured document is **unstated** — AF-2 must confirm empirically. The `timestamp` field's role in KMS validation is undocumented.
- **Doc gap:** whether an all-zeros PCR value is a legitimate reference or a never-extended sentinel (AF-3) is undocumented — confirm via `nitro-tpm-pcr-compute` output on a no-command-line build.
- **Cross-reference:** EK retrieval (`GetInstanceTpmEkPub`), `RegisterImage --tpm-support`, and instance/AMI TPM-support attribute reads are on the **parent** `nitrotpm.html` surface — see `/work/aws-docs/nitrotpm-attack-research-plan.md` §AF-4/AF-6 rather than duplicating here.

---
*Generated by security-questionbuilder against nitrotpm-attestation.html and its 8 sub-pages. Documentation-derived hypotheses only; no live testing performed.*
