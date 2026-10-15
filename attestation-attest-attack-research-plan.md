# Integrating with AWS KMS (NitroTPM attestation consume step) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-attest.html` ("Integrating with AWS KMS"), the 4th and final child of the NitroTPM-attestation chapter hub (`nitrotpm-attestation.html`). Authoritative KMS-side mechanism cross-checked against the KMS Developer Guide (`cryptographic-attestation.html` [canonical; old slug `services-nitro-enclaves.html`], `conditions-attestation.html`, `conditions-nitro-tpm.html`, `conditions-nitro-enclave.html`, `attested-calls.html`, `ct-attestation.html`), the KMS API Reference (`API_Decrypt.md`, `API_RecipientInfo.md`, `API_PutKeyPolicy.md`), the EC2 validate page (`nitrotpm-attestation-document-validate.html`), and the IAM Service Authorization Reference (`list_kms.html`, 3263 lines). Offline mirror == online `.md` verbatim 2026-10-15. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The safe first oracle for every authorization lead here is **documentation + `iam:SimulateCustomPolicy` / `aws kms` dry authoring** — no customer plaintext is ever decrypted to settle a question. The one lead that *requires* a live call (Area 1 mandatoriness) uses a **synthetic canary ciphertext** and a principal presenting **no** attestation document; never real data.
- **HARD STOP:** the attestation document is COSE_Sign1-signed by the AWS Nitro Attestation PKI (root `CN=aws.nitro-enclaves`, the AWS service-plane root of trust). The moment any lead would require **forging, extracting, or impersonating that signer**, or reaches an identity/credential/ARN belonging to AWS's own Nitro/hypervisor fleet, stop, preserve evidence, flag for AWS-Security disclosure. Everything in this plan is reachable *without* breaking the signer.

### COMPLEMENT discipline (what this plan does NOT restate)
This is a **page-level deep-dive child of [`nitrotpm-attestation`](nitrotpm-attestation-attack-research-plan.md) (hub)**, and the **runtime-consume twin of [`prepare-attestation-service`](prepare-attestation-service-attack-research-plan.md)** (which owns the *authored key-policy artifact*). Those plans already own:
- **PCR-defeat layer** (hub A1 reproducible public-recipe measurements under a broad `Principal`; hub A2 under-binding / all-zeros-PCR12; hub A3 `PCR*`-vs-`NitroTPMPCR*` family confusion; hub A4 replay/no-nonce/no-TTL; hub A5-A6 COSE/CRL/alg 3P-verifier narrative).
- **Key-policy *artifact* structure** (prepare A1 **additive-not-mandatory** Deny-form; prepare A3 3-of-5 gated actions; prepare A4 missing ViaService/EncryptionContext/CallerAccount scoping).
- **Attestation-document generation request-side** ([`attestation-get-doc`](attestation-get-doc-attack-research-plan.md) A1 the 3 passthrough fields `public_key`/`user_data`/`nonce`; A2 the `nitro-tpm-attest` tool supply chain; A3 no-IAM guest-local generation).
- **The 3P (non-KMS) validator recipe** ([`nitrotpm-attestation-document-validate`](nitrotpm-attestation-document-validate-attack-research-plan.md) — 9 Areas, HEADLINE "fail-open by doc-architecture": the 4-step recipe stops at genuine-signature and never compares PCRs/nonce/timestamp; A2 CRL-disabled; A3 alg-not-pinned; A4 CBOR-DoS; A5 chain/anchor; A8 replay; A9 shared-root NitroTPM↔Enclave confusion). **That page is fully owned already** — this plan only *routes* to it from the consume side (Area 6), it does not restate those findings.

**This plan owns ONLY the runtime KMS *request/response* consume mechanics** that the siblings treat at summary level, and cross-references all the above for the rest.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce:
1. **Decrypt a key-policy-attestation-gated ciphertext while presenting NO attestation document** (gate is per-statement, not key-global → mandatoriness break). [Area 1]
2. **Receive the plaintext of a gated KMS operation under an attacker-chosen recipient key** — i.e. make KMS encrypt the response under a public key the attacker controls, by presenting a *validly-signed* attestation document the attacker minted on a correctly-measured instance of their own. [Area 2, chains hub A1]
3. **Replay a captured attestation document** against the gated key and get a KMS success (no freshness/TTL enforcement). [Area 3]
4. **Invoke an attestation-capable KMS action the key policy did NOT gate** (DeriveSharedSecret / GenerateDataKeyPair) against the protected CMK with no attestation. [Area 4]
5. **Cause a silent, un-erroring attestation lockout** by authoring a wrong-family / out-of-range condition key that can never match (availability / false-sense-of-security). [Area 5]
6. On the 3P (non-KMS) path, **get a forged/stale/alg-swapped document accepted** by a validator built per AWS's own incomplete sample. [Area 6]

---

## 2. Components, Assets, and Design

**What this page is.** `attestation-attest.html` ("Integrating with AWS KMS") is the **runtime consume step** of the NitroTPM-attestation workflow: *"Your instance should have an application that can make AWS KMS API requests with the Attestation Document retrieved from the NitroTPM. When you make a request with an Attestation Document, AWS KMS validates the measurements in the provided Attestation Document against the reference measurements in the KMS key policy. Requests are allowed only if the measurements … match."* It then lists the five KMS APIs that accept an attestation document and asserts the response-under-public-key behavior, and closes with a Note handing 3P integrators to the validate page. It is **not** an API page; it describes how to *call* the KMS crypto-operation family with a `Recipient` attestation document.

**Pipeline (who holds what):**
```
 [Attestable AMI build] --reference PCRs--> [KMS key policy]           (prepare-attestation-service: artifact)
         |                                        ^
         v                                        | authored once (PutKeyPolicy)
 [NitroTPM-enabled EC2 instance]                  |
   |   nitro-tpm-attest --public-key <CALLER-CHOSEN RSA pub>           (attestation-get-doc: generation, no IAM)
   |   => COSE_Sign1 Attestation Document (boot-state PCRs + embedded pub key; NO account/instance id field)
   v
 [consuming application on the instance]  --SigV4 (instance-role identity)-->  AWS KMS
   |   Decrypt/DeriveSharedSecret/GenerateDataKey/GenerateDataKeyPair/GenerateRandom
   |     Recipient = { AttestationDocument, KeyEncryptionAlgorithm: RSAES_OAEP_SHA_256 }
   v
 KMS: (1) validate signature chain to Nitro root + (2) match doc PCRs vs key-policy condition values
      on success => CiphertextForRecipient (plaintext RSA-OAEP-encrypted under the doc's embedded pub key);
      Plaintext field null.
```

**Two independent gates on every gated call (load-bearing):**
1. **IAM identity gate** — the calling principal (normally the EC2 **instance role** fetched from IMDS) must itself be allowed `kms:Decrypt`/etc. on the key. The attestation condition is **additive** to this, not a replacement.
2. **Attestation condition gate** — `kms:RecipientAttestation:NitroTPMPCR<N>` on the key policy's Allow statement, satisfied only when the request carries a `Recipient` document whose PCRs match the authored values.

**Assets:** the gated CMK and the plaintext/data keys it protects; the key policy; the caller-chosen RSA recipient key pair (private key = the de-facto decryption capability); the instance role credentials.

**Resource identifiers / entropy:** the attestation document has **no account_id/instance_id field** (CDDL `#doc-def`: `module_id`, `timestamp`, `digest`, `nitrotpm_pcrs`, `certificate`, `cabundle`, optional `public_key`/`user_data`/`nonce`) — `module_id` identifies the issuing *hypervisor module*, not the customer. So the document proves **boot state, not caller identity** (schema-level fact). Account scoping lives entirely in the *key policy's other conditions* (`Principal`, `kms:CallerAccount`), not in the document.

**Identity establishment:** SigV4 under the instance role for the KMS call; the attestation document itself requires **no IAM** to generate (local TPM/CLI operation, inferred from the absence of any documented IAM action or auth step for `nitro-tpm-attest`).

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `kms:Decrypt` (+`Recipient`) | API | Existing (attestation path NEW) | Non-mutating (returns plaintext/ciphertext) | External | Decrypt gated ciphertext into `CiphertextForRecipient` | Yes | Per key policy + IAM | `list_kms` l.1016; cond keys l.1033-1089. **Prime target** (Area 1/2). |
| `kms:GenerateDataKey` (+`Recipient`) | API | Existing | Mutating (mints key material) | External | Deliver a data key into attested env | Yes | Per key policy + IAM | `list_kms` ~l.1412. |
| `kms:GenerateRandom` (+`Recipient`) | API | Existing | Non-mutating | External | Deliver entropy into attested env | Yes | Per key policy + IAM | `list_kms` l.1656. **Outlier:** empty resource type (l.1661 `<p></p>`); **only** RecipientAttestation cond keys — no `ViaService`/`EncryptionContext`/`CallerAccount` (Area 4). |
| `kms:DeriveSharedSecret` (+`Recipient`) | API | Existing | Non-mutating | External | ECDH agreement into attested env | Yes | Per key policy + IAM | `list_kms` l.1164. **Omitted from prepare's example key policy** (Area 4). |
| `kms:GenerateDataKeyPair` (+`Recipient`) | API | Existing | Mutating | External | Deliver a data key *pair* into attested env | Yes | Per key policy + IAM | `list_kms` l.1495. **Omitted from prepare's example** (Area 4). |
| `kms:PutKeyPolicy` on the gated key | API | Existing | Mutating (authors the gate) | External | Writes the attestation condition | Yes | Per IAM / key policy | `API_PutKeyPolicy.md`: no documented semantic check of PCR index/value (Area 5). |
| `nitro-tpm-attest` (guest CLI) | guest tool | New feature | n/a | guest-local | Produces the `Recipient` document with a **caller-chosen** `--public-key` | n/a | **No IAM** — any co-resident process | Generation mechanism owned by `attestation-get-doc`; its caller-chosen key is the hinge of Area 2. |
| 3P custom validator | customer code | New feature | n/a | External/3P | Receive+parse+validate the document outside KMS | n/a | Customer-built | `nitrotpm-attestation-document-validate.html` — AWS sample is incomplete (Area 6). |

**Undocumented/under-surfaced knobs to flag:** `Recipient.KeyEncryptionAlgorithm` has exactly one valid value (`RSAES_OAEP_SHA_256`, `API_RecipientInfo.md`) → RSA-only recipient keys. `CiphertextForRecipient` + null `Plaintext` is the response shape on *every* attested call (`API_Decrypt.md` l.126-132). `GenerateRandom`'s empty resource-type / RecipientAttestation-only condition profile is a reference-level anomaly worth testing for scoping surprises.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Any instance-role principal holding `kms:Decrypt` on the key | Gated CMK plaintext | KMS call **without** a `Recipient` document | A **success** (non-`AccessDenied`) Decrypt of synthetic canary ciphertext proves the attestation gate is non-mandatory for that key (Area 1). |
| Attacker on a *correctly-measured instance of their own* (public AMI recipe) | Victim's gated plaintext | Mint a validly-signed doc embedding **attacker's** RSA public key; call gated action | KMS returns `CiphertextForRecipient` decryptable by the **attacker's** private key = plaintext crosses to attacker (Area 2; chains hub A1 reproducible measurement). |
| Holder of a **captured** attestation document | Gated CMK operation | Replay the stale document (within 30yr cert validity) | KMS success with no freshness error (Area 3). Severity bounded by the embedded original public key. |
| App authorized for an **un-gated** attestation-capable action (DeriveSharedSecret/GenerateDataKeyPair) | Protected CMK | Call the action the key policy forgot to gate | Operation succeeds with no `Recipient` (Area 4). |
| 3P service relying on AWS's sample validator | Its attestation-gated secret | Present a forged/stale/alg-swapped document | Validator accepts → secret released (Area 6; customer-owned severity). |
| **Any customer surface** | **AWS Nitro signer / hypervisor fleet** | — | **HARD STOP.** Any attempt to forge/extract the COSE signer or reach the Nitro service plane = disclosure, not a lead. |

---

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE] "Allowed only if measurements match" is per-STATEMENT fail-closed, not key-global (Lens W fail-open / Lens U doc-vs-enforcement)
**Background.** This page asserts in its own prose: *"Requests are allowed only if the measurements in the Attestation Document match the reference measurements in the KMS key policy."* A reader concludes the key is reachable *only* via attestation. The KMS-authoritative condition page confirms the per-statement half: `conditions-nitro-tpm.html` — *"If the request does not include an attestation document, permission is denied because this condition is not satisfied."* (standard IAM: `StringEqualsIgnoreCase` on an absent key → false → that `Allow` denies).
**Security Concern.** Fail-closed is a property of **that one condition statement**, not of the key. `conditions-attestation.html` states explicitly: *"If you don't provide a key policy when you create an AWS KMS key, AWS creates one for you. This default key policy grants the AWS accounts that own the KMS key full access … This policy allows all actions like Decrypt"* and even recommends mitigating with `NotAction: kms:Decrypt`. So **any co-existing Allow with no attestation condition** — the default root/`Enable IAM policies` statement, or any identity policy granting `kms:Decrypt` — authorizes decrypt with **no document at all**. The page's "only if match" guarantee is therefore enforced by *how the operator authored the rest of the policy*, i.e. prose/best-practice, **not a KMS mechanism**. This is the KMS-authoritative confirmation of prepare A1 (additive-not-mandatory), now cited from the KMS side (`conditions-attestation.html`), framed from the **consuming caller's** vantage.
**High-level Test Scenarios.**
- Claim: a principal holding identity-policy `kms:Decrypt` on an attestation-gated CMK can decrypt a synthetic canary ciphertext **without** a `Recipient` document. → Oracle: live `aws kms decrypt` with no `--recipient` returns `200`/plaintext (not `AccessDenied`). → Precondition: a key authored per AWS's shown Allow-only example (prepare A1) + the default root statement intact. → Cost: minutes, synthetic data only. → **Severity: High** (the sole documented control over the gated secret is advisory).
- Claim: the only policy shape that *actually* makes attestation mandatory (explicit `Deny` with `Null`/`StringNotEquals` guard) is never shown on this page or on `prepare-attestation-service`. → Oracle: `iam:SimulateCustomPolicy` of the shipped Allow-only artifact vs. a Deny-augmented one, with/without a `Recipient` context key. → defer the artifact remediation to prepare A1; **own here the consume-side proof**.
**Stop condition.** Decrypt denied without a document under the shipped example → gate *is* mandatory; downgrade and record the policy shape that achieved it.

### Area 2 — [HEADLINE] The response recipient is a CALLER-CHOSEN public key; KMS never proves private-key possession (Lens M / W / U)
**Background.** The page: *"these APIs encrypt the plaintext in the response under the public key from the Attestation Document, and return ciphertext … decrypted only by using the matching private key that was generated in the instance."* `nitrotpm-attestation.html`: *"you must specify a public key for a key pair that you own … The specified public key is included in the Attestation Document. When AWS KMS validates the Attestation Document and allows a decryption operation, it automatically encrypts the response with the public key included in the Attestation Document."* The key is supplied by the caller to `nitro-tpm-attest --public-key` (`attestation-get-doc`: *"Only RSA keys are supported"*), `RSAES_OAEP_SHA_256` (`API_RecipientInfo.md`). The hypervisor merely **embeds** it under its signature.
**Security Concern.** The attestation gate binds **boot state** (PCR measurements), not the identity of who controls the recipient key, and KMS does **not** verify at request time that the instance possesses the matching private key (SA-confirmed: possession is only *assumed* because the key was embedded when the doc was signed). Combine with two already-owned facts: (a) the document has **no account/instance identity field** (schema-level, §2) and (b) measurements are **reproducible from the public Attestable-AMI/KIWI recipe** (hub A1). An attacker who launches *their own* instance from the same public recipe boots to the **same PCR4/7/12**, mints a validly-signed document embedding **their own** RSA public key, and calls the gated action → **KMS encrypts the victim's gated plaintext to the attacker's key.** The recipient redirect that `attestation-get-doc` A1 flagged on the request-side becomes, at the consume step, a **plaintext-exfiltration primitive** — *if* the key policy's `Principal`/`CallerAccount` conditions are broad enough to admit the attacker (hub A1's "only `Principal` binds, not PCR"). This plan owns the **runtime consume framing + the KMS no-possession-check fact**; defers the measurement-reproducibility to hub A1 and the request-side public-key semantics to get-doc A1.
**High-level Test Scenarios.**
- Claim: a document minted on an attacker-controlled, identically-measured instance, embedding an attacker RSA key, is accepted by KMS and yields `CiphertextForRecipient` the attacker can RSA-OAEP-decrypt. → Oracle: cross-principal decrypt of synthetic canary succeeds (plaintext recovered with attacker private key); refuted if the key policy's `Principal`/`kms:CallerAccount` denies the attacker before the condition is reached. → Precondition: key policy `Principal` broad enough to admit the attacker's account/role (hub A1) + reproducible measurements. → **Severity: Critical if cross-account; High intra-account cross-workload.**
- Adjacent: does KMS reject a document whose embedded key is non-RSA / malformed / undersized at request time, or only at response-encrypt time? (`API_RecipientInfo.md` says RSA-only; no min modulus documented — cross-ref get-doc A4.)
**Stop condition.** If every realistic gated key policy also pins `kms:CallerAccount`/narrow `Principal` that excludes a foreign minter, the cross-account variant is refuted → the residual is intra-account cross-workload reuse; record and downgrade.

### Area 3 — No freshness / replay / TTL enforcement in the KMS attestation path (Lens U / W)
**Background.** The attestation document schema carries `timestamp: uint .size 8` ("UTC time when document was created, in milliseconds") and an optional `nonce`. AWS's own documented validation (the 4-step recipe on the validate page) checks **signature chain validity + measurement match only**; cert-chain validation checks *"the current date falls within the validity period specified in the certificate"* — i.e. **cert expiry (30-yr root), not document age**. `attestation-get-doc.html` is explicit: `nonce` and `user_data` are *"Not used for attestation with AWS KMS."*
**Security Concern.** KMS performs **no freshness/anti-replay check** on NitroTPM documents (SA1-confirmed). A document captured once (from logs, a crash dump, a prior legitimate request, or a co-resident observer) is valid indefinitely within cert lifetime. This confirms hub A4 from the KMS-authoritative side. **Important bound:** a *bare* replay carries the **original** embedded public key, so the replayer only obtains `CiphertextForRecipient` the *original* key-holder can read — bare replay alone is not plaintext exposure. It becomes exposure only when the replayer is also the minter (Area 2) or holds the original private key. So Area 3's standalone value is: (a) the gate provides **no liveness guarantee** — a decommissioned/compromised instance's old document keeps authorizing; (b) availability/audit implications; (c) it widens the Area 2 window (any captured valid-measurement doc can be a template once the attacker swaps in their own key via their own mint).
**High-level Test Scenarios.**
- Claim: a `Recipient` document reused across many requests, long after generation, is accepted by KMS with no `ExpiredException`/freshness error. → Oracle: repeated gated calls with one stale document all return success. → **Severity: Medium** (High if chained with Area 2 or with a key policy that trusts "attested == live").
**Stop condition.** Any documented or observed KMS-side timestamp/nonce enforcement → refuted (would contradict `conditions-nitro-tpm.html`).

### Area 4 — Gated-action completeness from the consume side: 5 callable, AWS's own example gates 3 (Lens U / R)
**Background.** This page explicitly enumerates **all five** attestation-capable KMS actions (Decrypt, DeriveSharedSecret, GenerateDataKey, GenerateDataKeyPair, GenerateRandom), each as a legitimate call *"with an Attestation Document."* `list_kms.html` confirms all five carry `RecipientAttestation:*`. The `prepare-attestation-service` example key policy gates **only three** (Decrypt, GenerateDataKey, GenerateRandom) and **omits DeriveSharedSecret + GenerateDataKeyPair** (prepare A3).
**Security Concern.** From the **consume** side: if the protected CMK is an asymmetric/agreement key (so DeriveSharedSecret/GenerateDataKeyPair are usable) and some Allow permits them, those two operations execute with **no attestation enforcement** — the "attested-only" intent is incomplete exactly where this page says the caller may still call them. Additionally, `GenerateRandom` is a **reference-level outlier**: `list_kms.html` l.1661 gives it an **empty resource type** and l.1663-1719 shows its **only** condition keys are the `RecipientAttestation:*` family (no `ViaService`/`EncryptionContext`/`CallerAccount`) — so a `GenerateRandom` Allow can be scoped *only* by attestation, and gating random-byte delivery by attestation (vs. key-derived material) is itself unusual (it exists to inject entropy into the attested env via `CiphertextForRecipient`). This plan owns the **runtime consequence**; the artifact-completeness remediation stays with prepare A3.
**High-level Test Scenarios.**
- Claim: `DeriveSharedSecret`/`GenerateDataKeyPair` against a CMK whose policy follows the shown 3-action example succeed with **no** `Recipient`. → Oracle: `iam:SimulateCustomPolicy` on the example policy for those two actions (no attestation context) → `Allowed`; live canary confirms. → **Severity: Medium–High** (completeness gap in an AWS-authored sample → Tier-2 reportable per Lens R carve-out).
**Stop condition.** The key spec makes those two actions inapplicable (symmetric-only key) → downgrade to Informational.

### Area 5 — Key-family / index confusion → silent never-match lockout + doc-integrity stale cross-ref (Lens U, Low/Info)
**Background.** NitroTPM uses **`kms:RecipientAttestation:NitroTPMPCR0`–`NitroTPMPCR23`** only. **`ImageSha384`** and **`PCR0`–`PCR31`** are **Nitro Enclaves-only** (`conditions-nitro-enclave.html`: *"effective only when … from an AWS Nitro enclave"*; `conditions-nitro-tpm.html`: *"effective only when … from NitroTPM"*). `API_PutKeyPolicy.md` documents **no semantic validation** of the condition value — error types are ARN/grammar/state/length only; a nonexistent `NitroTPMPCR24` or wrong-length hex is (per standard IAM behavior, inferred) simply **never matched** rather than rejected at author time.
**Security Concern.** (a) **Silent lockout / false security:** an operator who authors `PCR4` (Enclaves family) instead of `NitroTPMPCR4`, or an out-of-range index, gets a statement that can *never* be satisfied by a NitroTPM document — no `PutKeyPolicy` error, no runtime error distinguishable from "wrong instance" — i.e. a self-inflicted availability break, or worse a statement the operator *believes* is gating when it is inert (then Area 1's other Allow carries the traffic). This is a *lockout*, not a *bypass* (cross-ref hub A3). (b) **Doc-integrity (AWS-owned):** `list_kms.html` links `PCR<N>`/`ImageSha384` to **`conditions-nitro-enclaves.html`** (plural) which **302-redirects to the dev-guide root** — a stale cross-reference in AWS's own IAM reference; the live page is `conditions-nitro-enclave.html` (singular). Also `services-nitro-enclaves.html` (old) → `cryptographic-attestation.html` (consolidated), and there is **no NitroTPM-specific KMS top-level page** despite this EC2 page's link text ("Cryptographic attestation for NitroTPM") implying one.
**High-level Test Scenarios.**
- Claim: `PutKeyPolicy` accepts `kms:RecipientAttestation:NitroTPMPCR24` (out of 0-23) and a short/odd-length hex value with no error. → Oracle: author such a policy; success + a subsequent valid NitroTPM request that never matches = confirmed silent lockout. → **Severity: Low** (availability/misconfiguration; Informational for the stale link, but AWS-owned and filable per Lens U).
**Stop condition.** `PutKeyPolicy` returns `MalformedPolicyDocumentException` for the bogus key/value → refuted (KMS *does* validate; stronger than documented).

### Area 6 — [POINTER] This page is the consume-side ENTRY to the 3P (non-KMS) validation path — fully owned elsewhere
**Background.** The page's closing Note: *"If you are attesting to a third-party service, you must build your own custom mechanisms for receiving, parsing, and validating Attestation Documents"* → `nitrotpm-attestation-document-validate.html`. This page is the **doc-level handoff** that sends an integrator off the KMS-enforced path (where KMS does the validation) onto a path where the **customer's own code** is the entire gate.
**What this plan owns here (and only this):** the *consume-side framing* — that the moment an integrator chooses "third-party service" over KMS, **every protection analyzed in Areas 1–5 (the KMS-enforced measurement match, response-key binding, action gating) evaporates** and is replaced by whatever the customer builds from the validate recipe. That architectural fork is the lead; the fork's destination is owned downstream.
**Fully owned downstream — DO NOT restate (route the hunter there):** [`nitrotpm-attestation-document-validate`](nitrotpm-attestation-document-validate-attack-research-plan.md) owns all 9 Areas of the validator-recipe surface, including its HEADLINE **A1 fail-open-by-doc-architecture** (the 4-step recipe stops at "genuine Nitro signature" and never compares `nitrotpm_pcrs`/nonce/timestamp → any genuine doc from any account passes), **A2** CRL-disabled with no compensating control, **A3** COSE alg-not-pinned / `Sig_structure` unspecified, **A4** unbounded `cabundle` CBOR-parser DoS, **A5** chain/anchor footguns (PKIX sample safe verbatim; risk = mis-anchor from attacker `cabundle` or manual `cert.verify()` loop), **A8** nonce/timestamp-optional replay, and **A9** the net-new shared-root `AWS_NitroEnclaves_Root-G1` NitroTPM↔Enclave type confusion. Generic COSE/CBOR/CRL/alg narrative stays at hub A5-A6.
**Severity.** As a routing lead: Informational here. The underlying 3P-validator severities (High headline) live in the validate plan. **Note the cross-dependency with Area 2:** the "no account/instance identity in the document" fact this plan uses for Area 2 is the *same* fact that makes the validate plan's A1 fail-open — a hunter working Area 2 should read validate A1/A9 as the 3P mirror of the KMS no-possession-check.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Decrypt gated secret with no attestation document | KMS key policy eval | "Requests are allowed only if the measurements … match" (page prose) — tested against the per-statement/key-global gap (Area 1). |
| Plaintext encrypted to attacker-chosen recipient key | `Recipient.AttestationDocument` embedded pub key | "decrypted only … with the matching private key that was generated in the instance" — tested against KMS's no-possession-check + no identity binding (Area 2). |
| Stale document replay | KMS attestation validation | Implicit "live attestation" expectation — tested against documented absence of freshness/nonce check (Area 3). |
| Call an un-gated attestation-capable action | KMS key policy `Action` list | AWS example gates 3 of 5 (prepare A3) — tested from the consume side (Area 4). |
| Silent never-match from wrong key family/index | `PutKeyPolicy` | "PCR value must be a lower-case hexadecimal string of up to 96 bytes" (guidance only) — tested against lack of authoring-time validation (Area 5). |
| Forged/stale/alg-swapped doc accepted by 3P validator | AWS sample validator | 4-step recipe + "CRL must be disabled" — tested against sample incompleteness (Area 6). |
| Forge/extract the Nitro COSE signer | Nitro Attestation PKI | Root of trust — **HARD STOP, out of scope.** |

---

## 7. Out-of-Scope Risk Categories
- **Forging/extracting the AWS Nitro COSE signer or reaching the Nitro/hypervisor service plane** — hard stop, disclosure.
- **IMDS credential retrieval of the instance role** on the managed NitroTPM host — the identity gate's credential source is owned by [`iam-roles-for-amazon-ec2`](iam-roles-for-amazon-ec2-attack-research-plan.md); not re-derived here (IMDS on managed hosts is itself out-of-scope).
- **Reproducible-measurement / PCR under-binding / all-zeros-PCR12 / broad-`Principal`** mechanics — owned by **hub A1/A2** and `prepare-attestation-service` / `attestable-ami` / `build-sample-ami`; this plan *chains into* them (Area 2) but does not re-own them.
- **The key-policy artifact's Deny-form / 3-of-5 / missing-ViaService structure** — owned by `prepare-attestation-service` A1/A3/A4.
- **The `nitro-tpm-attest` tool supply chain + the 3 passthrough fields themselves** — owned by `attestation-get-doc` A1/A2/A3.
- **The 3P validator-recipe surface** (fail-open-by-architecture, CRL, alg-pin, CBOR DoS, chain/anchor, shared-root confusion) — fully owned by [`nitrotpm-attestation-document-validate`](nitrotpm-attestation-document-validate-attack-research-plan.md) (9 Areas); Area 6 here is a routing pointer only.
- **A bug in a specific customer's 3P validator** (vs. the AWS *recipe's* defects) — consumer-owned, out of scope beyond the reference PoC.
- **Generic COSE/CBOR/CRL/alg narrative** — hub A5/A6.

---

## 8. Null Hypotheses / Doc Gaps
- **Lens A (cross-tenant IDOR):** N/A at the API-shape level — KMS crypto ops name the key by ARN and are account/`Principal`-scoped; the attestation document has no tenant id to confuse. The cross-account reach is *not* an IDOR; it is the Area 2 **measurement-reproducibility + broad-Principal** chain. Checked: `attestation-attest.html`, `conditions-attestation.html`, `API_Decrypt.md`.
- **Lens V/D (network segmentation / data→control):** N/A — this is an application making an ordinary SigV4 KMS call to a public endpoint; no ENI/control-plane surface on this page. Checked: `attestation-attest.html`, `nitrotpm-attestation.html`.
- **Lens B/C (PassRole / credential vending):** N/A on this page — no role ARN is passed to KMS; the only identity is the caller's own instance role (identity gate, §2). No STS session-policy construction here.
- **Lens EE / N (predictable-name / namespace migration):** N/A — no name-resolution or dual-namespace surface; the only naming anomaly is the stale `conditions-nitro-enclaves.html` doc link (Area 5, doc-integrity not authz).
- **Lens H (CMK/encryption-context confusion):** partially present but **deferred** — `EncryptionContext` scoping of the gated statement is a prepare-A4 defense-in-depth concern; `GenerateRandom`'s inability to carry `EncryptionContext` is captured in Area 4.
- **Doc gaps to confirm live before investing:** (1) KMS no-private-key-possession check at request time is doc-silent (inferred from the embed-at-sign design — Area 2); (2) `PutKeyPolicy` semantic validation of PCR index/value is doc-silent (Area 5); (3) no-IAM document generation is inferred from the absence of any documented IAM action for `nitro-tpm-attest` (§2); (4) whether KMS rejects a non-RSA/undersized embedded recipient key at request vs. response time (Area 2 adjacent). All four are settleable read-only via `SimulateCustomPolicy` + synthetic-canary dry calls; none require real plaintext.

---
*Companion to [`nitrotpm-attestation`](nitrotpm-attestation-attack-research-plan.md) (hub), [`prepare-attestation-service`](prepare-attestation-service-attack-research-plan.md) (key-policy artifact), [`attestation-get-doc`](attestation-get-doc-attack-research-plan.md) (document generation), and [`nitrotpm-attestation-document-validate`](nitrotpm-attestation-document-validate-attack-research-plan.md) (3P validator recipe — routed to from Area 6). Trust `list_kms`/`list_ec2` over User-Guide prose for condition-key facts.*
