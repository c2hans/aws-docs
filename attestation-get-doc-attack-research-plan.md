# Get the NitroTPM Attestation Document (`nitro-tpm-attest` retrieval client) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-get-doc.html` (and `.md` twin), its two child pages `nitrotpm-attestation-document-content.html` / `nitrotpm-attestation-document-validate.html`, the referenced GitHub repo `github.com/aws/NitroTPM-Tools` (per-tool READMEs for `nitro-tpm-attest` + `nitro-tpm-pcr-compute`), `build-sample-ami.md`, and KMS references `API_RecipientInfo.md`, `conditions-nitro-tpm.md`, `cryptographic-attestation.md`. IAM references `list_kms.md` / `list_ec2.md`. Live `.md` fetched 2026-10-15 (no 404s); online==offline where both exist. Status: documentation-derived hypotheses only; nothing tested against a live account.

> **Scope / sibling coordination — READ FIRST.** This page is the **document-retrieval client** chapter: it introduces the `nitro-tpm-attest` guest utility, its install, and its three request parameters, and it links two child pages (document *content* and *validation*). The **KMS-verifier gate, PCR under-binding, reproducible-measurement bypass, replay-against-KMS, CRL-disabled validation, and COSE algorithm-pinning** are already owned by the chapter hub plan **`nitrotpm-attestation-attack-research-plan.md`** (its Areas 1–6, which already cite `attestation-get-doc.md` for the nonce/freshness point) and the KMS-policy artifact plan **`prepare-attestation-service-attack-research-plan.md`**. This plan therefore **does not restate** them — it cross-references them and OWNS only the net-new **retrieval-client / request-side-contract / tool-supply-chain** surface:
> - the three caller-controlled passthrough fields (`--public-key` RSA-only, `--user-data`, `--nonce`) and how they bind (or fail to bind) the request vs the response;
> - the **non-KMS ("external service") attestation path**, for which this page is the authoritative request contract and where freshness is opt-in;
> - the `aws-nitro-tpm-tools` package + `NitroTPM-Tools` GitHub supply chain;
> - the "document generation requires no IAM / is guest-local" boundary statement (attestation proves *boot state*, not *caller identity*).
>
> The AMI-build/measurement supply chain is owned by `build-sample-ami` / `attestable-ami` / `create-pcr-compute` plans; EK retrieval by `retrieve-ekpub`; enablement/verify by the `enable-*`/`verify-*` siblings.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in §5 priority order; look left and right for adjacent bugs; follow cross-refs into the hub plan rather than re-deriving.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account or signing-key material belonging to AWS's own service plane (the Nitro Hypervisor's attestation signing key, the Nitro Attestation PKI private keys), stop, preserve evidence, flag for AWS-Security disclosure. Document *generation* is AWS-signed — never attempt to forge or extract the signer; the in-scope question is only what the **caller-controlled fields** and **consumers** do with a legitimately-signed document.

## 1. Pentest Objectives
1. Determine whether the three caller-supplied fields embedded into the signed Attestation Document (`public_key`, `user_data`, `nonce`) create any authorization-relevant gap — i.e. whether the party that chooses the recipient key or the user-data/nonce is the party the consumer *believes* it is talking to.
2. Determine whether the **non-KMS ("external service") attestation path** — the only path for which `user_data`/`nonce` are live — can be defeated by a reused/stale document because freshness is opt-in and not forced by the document format.
3. Determine whether a captured, PCR-matching document can be re-presented to KMS with an **attacker-chosen `public_key`** to redirect the plaintext response to the attacker (bounded by what minting a fresh document requires). (The pure KMS replay oracle itself is hub Area 4 — this plan owns the recipient-redirection refinement.)
4. Characterize the supply chain of the retrieval client itself (`aws-nitro-tpm-tools` RPM; `NitroTPM-Tools` GitHub build) for provenance/pinning gaps distinct from the AMI-measurement supply chain.
5. State precisely the trust boundary the retrieval client sits on: generation is guest-local and un-IAM-gated, so attestation binds *the software that booted*, never *the principal that called* — and confirm the docs do not imply otherwise.

## 2. Components, Assets, and Design

**What this page is.** `attestation-get-doc.html` documents `nitro-tpm-attest`, the guest-OS utility that asks the Nitro Hypervisor for a signed Attestation Document at runtime. The document is **CBOR-encoded and COSE_Sign1-signed by the AWS Nitro Attestation PKI**. The caller may attach three optional inputs; everything else in the document is AWS-populated and signature-bound.

**The Attestation Document request contract (the asset this plan owns).** CDDL from `nitrotpm-attestation-document-validate.md`:
```
AttestationDocument = {
    module_id, timestamp, digest, nitrotpm_pcrs, certificate, cabundle,   ; AWS-populated, signature-bound
    ? public_key: user_data,   ; OPTIONAL, caller-supplied — DER-encoded key the consumer uses to encrypt its response
    ? user_data: user_data,    ; OPTIONAL, caller-supplied — "additional signed data, defined by protocol"
    ? nonce:     user_data,    ; OPTIONAL, caller-supplied — challenge-response proof-of-liveness
}
user_data = bytes .size (0..1024)     ; <= 1024-byte cap on EACH of public_key / user_data / nonce
pcr       = bytes .size (32/48/64)    ; SHA384
```
The three `?` fields are **caller-controlled passthrough**: the signature proves AWS saw them, not that they are correct or fresh — "these will be included in the attestation document returned by the NitroTPM" (`nitro-tpm-attest` README). The identity binding is `nitrotpm_pcrs` only.

**Two consumer paths, different field semantics.**
- **KMS path (first-class verifier):** `aws kms decrypt --recipient "KeyEncryptionAlgorithm=RSAES_OAEP_SHA_256,AttestationDocument=<doc>"`. KMS gates on PCR condition keys (`kms:RecipientAttestation:NitroTPMPCR<0-23>`, hub territory), then **encrypts the plaintext response under the document's embedded `public_key`** and returns it as `CiphertextForRecipient`. `API_RecipientInfo`: `KeyEncryptionAlgorithm` valid value is **only `RSAES_OAEP_SHA_256`**; `AttestationDocument` is Base64, **max 262144 bytes**, and **`Required: No`**. The page states `user_data` and `nonce` are **"Not used for attestation with AWS KMS."**
- **External-service / third-party path:** the page's own framing — `user_data` "to deliver any additional signed data to an external service … complete an agreed protocol"; `nonce` "to set up challenge-response authentication … to help prevent impersonation attacks … verify that it is interacting with a live instance and not an impersonator that is reusing an old Attestation Document." On this path freshness exists **only if the integrator implements the nonce check** — nothing in the document format forces it.

**Tooling / supply chain.**
- `nitro-tpm-attest` — installed via `sudo yum install aws-nitro-tpm-tools` (Amazon Linux 2023 repo) and **baked into the sample AMI at `/usr/bin/`** (`build-sample-ami.md`). GitHub source builds via Docker + `cargo build --release` over TSS2; no release-signing/SBOM/pinning documented.
- Nitro Hypervisor / Nitro Attestation PKI — AWS-owned signer; root cert `AWS_NitroEnclaves_Root-G1` (30-yr AWS Private CA, `CN=aws.nitro-enclaves`). Not customer-reachable; HARD STOP if ever implicated.

**Accounts/trust zones:** guest OS of the instance (anyone with code-exec there can mint documents) vs AWS Nitro signer (root of trust) vs the consumer — AWS KMS or a customer-built "external service." The retrieval client sits entirely inside the guest; it is a *reader of hypervisor state*, not an authenticated API caller.

**ASCII pipeline (request side — this plan's focus):**
```
[Guest OS caller — ANY code-exec principal, NO IAM required]
   nitro-tpm-attest --public-key PK[RSA] --user-data UD --nonce N
        |                 (PK, UD, N each <=1024 bytes, caller-chosen)
        v
[Nitro Hypervisor] -- COSE_Sign1 signs --> Doc{ pcrs(AWS), ..., public_key=PK, user_data=UD, nonce=N }
        |
   +----+-----------------------------+
   v                                   v
[AWS KMS]  gate on PCRs (hub);        [Customer "external service"]  verifies sig+chain+PCRs;
 encrypts response under PK;           nonce/user_data ONLY meaningful here;
 ignores UD and N                      freshness = integrator must check N
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Any guest-OS principal with code-exec on a PCR-matching instance | The recipient of a KMS plaintext response | Supplying an **attacker-chosen `--public-key`** into a freshly-minted (or replayed-then-reminted) document, then calling `Decrypt`/`GenerateDataKey` with it | KMS returns `CiphertextForRecipient` decryptable by the **attacker's** private key for a key the AMI author intended only the trusted workload to use — the recipient is bound by a caller-chosen field, not by identity (only the IAM `Principal` + PCRs constrain this; see hub Area 1). |
| An impersonator holding one captured Attestation Document | A customer-built "external service" verifier | Re-presenting the document on the 3P path where the integrator did **not** implement the opt-in nonce check | The external service accepts a stale/replayed document as proof of a *live* trusted instance — the exact attack the page says the nonce *would* prevent, defeated because nonce-checking is optional and un-enforced by the format. |
| Caller supplying `--user-data` / `--nonce` | A naive 3P consumer parsing those fields | ≤1024-byte attacker-controlled byte strings echoed verbatim into a signed, trusted-looking document | A consumer that treats signature-validity as content-validity parses attacker bytes from `user_data`/`nonce` as if AWS vouched for their meaning (injection/confused-trust into the consumer; inherits consumer severity). |
| Operator installing/baking the tool | The `nitro-tpm-attest` binary that mints all documents | `yum install aws-nitro-tpm-tools` with no documented pin/checksum; or an unpinned GitHub `cargo` build baked into a shared AMI | A tampered/substituted `nitro-tpm-attest` (or build dependency) silently alters what gets requested/embedded, or exfiltrates the caller's `--public-key`/private material — a measured-boot blind spot if the tool runs after the measured region or from a mutable path. |
| Any guest principal | The "attestation proves identity" assumption | Generation is guest-local and requires **no IAM** | A document minted by *any* process on the box (not just the trusted workload) is cryptographically indistinguishable to a consumer — attestation binds boot state, not the calling principal; a consumer relying on it for caller-identity is misusing it. |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `nitro-tpm-attest --public-key --user-data --nonce` | Guest-local CLI (Rust crate also) | New | Non-mutating (reads hypervisor state) | **Internal to the guest**, not a network API | Requests a COSE-signed Attestation Document with ≤3 caller-supplied ≤1024-byte fields | No (local only) | **Anyone with code-exec on the guest — NO IAM** | The core boundary statement: no credential, role, or AWS API call gates document *generation* (inferred from silence + "interact with the TPM2 device" language — flag as inferred, confirm live). |
| `yum install aws-nitro-tpm-tools` | Package install | New | Mutating (host) | External (AL2023 repo) | Installs `nitro-tpm-attest` + `nitro-tpm-pcr-compute` to `/usr/bin/` | n/a | Root on the instance | No GPG/checksum/pin documented *on this page* (AL2023 repo signing is implicit, not stated) — doc-gap, Lens R/Q. |
| KMS `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom` `--recipient` | API | Existing API + attestation `Recipient` | Crypto op | External | Consumes the document; gates on PCRs; encrypts response under embedded `public_key` | Yes | Per key policy `Principal` + `kms:RecipientAttestation:*` | `KeyEncryptionAlgorithm` = **only** `RSAES_OAEP_SHA_256`; `AttestationDocument` Base64 ≤262144 B, **Required:No**. Gate semantics = **hub Area 1–4**; this plan owns only the `public_key`-is-caller-chosen refinement. |

Non-SDK / least-reviewed: the `nitro-tpm-attest` CLI and its Rust crate (not an AWS SDK surface), and the ≤1024-byte passthrough-field contract that only the API/CDDL reference states.

## 5. Recommended Areas of Focus

### Area 1 — Caller-chosen recipient key + opt-in freshness on the external-service path (Lens U / M / W) [headline]
**Background:** The page documents three optional inputs. `--public-key` (RSA-only) is the key the consumer encrypts its response under; `--user-data`/`--nonce` are "Not used for attestation with AWS KMS" and exist for the "external service" path, where `nonce` is the stated anti-replay/anti-impersonation mechanism. The CDDL confirms all three are optional, caller-supplied, ≤1024-byte fields; the signature binds that AWS *saw* them, not that they are correct or fresh.
**Security Concern:**
- (a) **Recipient redirection:** `--public-key` binds only the **response**, never the request (confirmed across `attestation-get-doc.md`, `nitrotpm-attestation.md`, GitHub README — "automatically encrypts the response with the public key included in the Attestation Document"). The party that can present a PCR-matching document chooses who can read the KMS plaintext. If the trusted workload can be induced to mint a document with an attacker-supplied key, or an attacker with code-exec on a matching instance mints one directly, KMS returns `CiphertextForRecipient` the attacker can decrypt — the PCR gate authenticated "this software," and the recipient was never bound to identity. (The reproducible-measurement/broad-Principal preconditions are **hub Area 1**; this plan owns the "recipient is a caller-chosen field" link in that chain.)
- (b) **Opt-in freshness on the 3P path:** the format provides a `timestamp` (informational, not an expiry) and an **optional** `nonce`. Nothing forces a non-KMS verifier to check the nonce; the page even markets the nonce as the thing that stops "an impersonator that is reusing an old Attestation Document" — i.e. absent a nonce, reuse is expected. A customer-built external service that validates signature+chain+PCRs but omits a nonce challenge accepts a replayed document as live-instance proof.
**High-level Test Scenarios:**
1. Mint two documents on one instance with two different `--public-key` values; confirm each `CiphertextForRecipient` from KMS decrypts only under the matching private key → proves the recipient is fully caller-selected, not identity-bound. **Oracle:** both succeed with the respective attacker-held private keys.
2. On the 3P path, present a document with no `nonce` (or a fixed one) to a reference external-service verifier built strictly from `nitrotpm-attestation-document-validate.md`; replay it later. **Oracle:** the verifier accepts the replay as a fresh live-instance proof (freshness never enforced by the format).
3. Chain with hub Area 4: replay a captured document to KMS. Note the replayed document carries the *original* `public_key`, so a bare replayer cannot read the plaintext — **the request contract bounds replay to "trigger the side-effect" unless the attacker can also mint a fresh document with their own key (requires guest code-exec on a matching instance).** Record this as the precise severity ceiling of KMS replay.
**Doc evidence:** `attestation-get-doc.md` public-key/user-data/nonce paragraphs; CDDL optional fields; `API_RecipientInfo` (`RSAES_OAEP_SHA_256`, `Required:No`); `nitrotpm-attestation.md` KMS integration paragraph.
**Severity-if-true:** 3P-path replay (no nonce) = High for the integrator; recipient-redirection = High–Critical **only in combination with hub Area 1's broad-Principal/reproducible-measurement precondition** (rate at the chain end, not here).
**Stop condition:** once the recipient-is-caller-chosen fact and the opt-in-nonce fact are documented; do not probe the KMS PCR gate itself (hub Area 1–4).

### Area 2 — Retrieval-client supply chain (Lens R / Q / EE)
**Background:** `nitro-tpm-attest` is the single binary that mints every document for an instance. It is installed via `sudo yum install aws-nitro-tpm-tools` and **pre-baked into the sample AMI at `/usr/bin/`**; GitHub source builds via Docker + unpinned `cargo build --release` over TSS2. No GPG/checksum/SBOM/release-signing is documented on these pages.
**Security Concern:** This is a supply chain *distinct from* the AMI-measurement supply chain (owned by `build-sample-ami`/`attestable-ami`). The risk is integrity of the minting tool itself: (a) if `nitro-tpm-attest` runs from a **mutable path or after the measured-boot region closes** (`attestable-ami.md`: integrity depends on `erofs`+`dm-verity` holding at runtime), a substituted binary mints attacker-shaped documents or leaks the caller's `--public-key`/private key handling while PCR4/7/12 still look pristine; (b) a baked-in, unpinned GitHub build inherits any upstream/dependency compromise into every launched instance; (c) the AL2023 repo GPG model is *not stated on this page*, so an operator cannot confirm from the docs that the package is signature-verified.
**High-level Test Scenarios:**
1. Doc-gap confirm: does any AWS page state GPG/signature verification or a pinned version for `aws-nitro-tpm-tools`? If not, file the Lens-U documentation gap (operator cannot verify tool provenance from the docs).
2. Determine whether `/usr/bin/nitro-tpm-attest` sits inside the `dm-verity`/`erofs` read-only measured region in the sample AMI or on a writable overlay (settle against `al2023-isolated-compute-recipe`/`customize-sample-ami` siblings — a tool outside the measured region is a measured-boot blind spot).
3. Review the GitHub build for pinning/signing (unpinned `cargo` + Docker base image = future-compromise/dep-confusion lead, not a current CVE).
**Doc evidence:** `attestation-get-doc.md` install block; `build-sample-ami.md` dnf line + "preinstalled in `/usr/bin/`"; `attestable-ami.md` erofs/dm-verity dependency; GitHub top-level README build steps.
**Severity-if-true:** Medium (provenance/documentation gap) → High if the minting tool is confirmed outside the measured/read-only region (undermines the whole attestation chain for that AMI). Cross-ref `customize-sample-ami-plan-note` (overlay-overwrites-measurer finding) — the same overlay class could overwrite `nitro-tpm-attest`.

### Area 3 — Generation is guest-local and un-IAM-gated: boot-state ≠ caller-identity (Lens E / A framing)
**Background:** No fetched source names any IAM permission, role, or AWS API call as a prerequisite for running `nitro-tpm-attest`; the GitHub README describes it as interacting "with the TPM2 device." IAM enters only downstream at the KMS call.
**Security Concern:** Any process with code-exec on the instance — not only the "trusted workload" — can mint a validly-signed, PCR-matching document, because PCRs reflect *what booted*, not *who is calling now*. A consumer (KMS key policy, or a 3P service) that treats a valid document as proof of a specific *caller* or *principal* is misusing the primitive; the only principal binding on the KMS path is the key-policy `Principal` clause (hub Area 1). This is the boundary statement the page's existence establishes and should be stated explicitly so a hunter does not chase a non-existent "forge a document as another principal" bug.
**High-level Test Scenarios:**
1. Confirm (live) that `nitro-tpm-attest` succeeds with no instance role / no AWS credentials present → generation needs no IAM (resolves the inferred-from-silence note).
2. From a non-privileged (but code-exec-capable) user on a matching instance, mint a document and present it to a PCR-gated KMS key whose `Principal` is broad → success proves the gate never distinguished the workload from any co-resident process (chains to hub Area 1).
**Doc evidence:** absence of any IAM prerequisite across `attestation-get-doc.md`/README/`nitrotpm-attestation.md`; usage example runs the bare binary.
**Severity-if-true:** Informational as a standalone framing; High as the enabler that defines what hub Area 1 is actually exploiting.
**Stop condition:** this is a scoping/framing area — once the no-IAM, boot-state-not-identity fact is confirmed, do not treat "another principal can mint a document" as a bug (it is by design).

### Area 4 — Request-field size/strength and passthrough-parsing edges (Lens Y / F) [minor]
**Background:** `public_key`/`user_data`/`nonce` are each `bytes .size (0..1024)`; the whole Base64 `AttestationDocument` is capped at 262144 bytes at KMS; `KeyEncryptionAlgorithm` is fixed at `RSAES_OAEP_SHA_256`.
**Security Concern:** (a) **RSA strength:** the page says only "RSA keys are supported" with no minimum modulus stated; a caller could embed a weak RSA public key so `CiphertextForRecipient` confidentiality is only as strong as that key (a self-footgun unless combined with a consumer that trusts the embedded key blindly). The ≤1024-byte DER cap also implicitly bounds key size (RSA-8192 DER ≈1050 B may not fit) — confirm whether oversized/undersized keys are rejected or silently accepted. (b) **Passthrough parsing:** a 3P consumer that parses attacker-controlled `user_data`/`nonce` bytes (e.g. as JSON/protobuf for its "agreed protocol") inherits an injection seam — the signature does not vouch for the *structure* of those fields.
**High-level Test Scenarios:**
1. Supply a deliberately weak/oversized/undersized RSA `--public-key`; observe whether `nitro-tpm-attest` or KMS rejects (expected) or embeds it silently. **Oracle:** acceptance of a sub-2048-bit key = a weak-recipient footgun worth a Lens-U doc note.
2. Embed structured attacker bytes in `--user-data`; confirm they appear verbatim in the signed document → the consumer, not AWS, must sanitize them (indirect-injection seam, inherits consumer severity).
**Doc evidence:** CDDL size caps; `API_RecipientInfo` fixed algorithm + 262144 cap; `attestation-get-doc.md` "Only RSA keys are supported."
**Severity-if-true:** Low (self-footgun / doc-hardening) unless a 3P consumer blindly trusts the embedded key or parses the fields unsafely (then inherits that consumer's severity).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Redirect KMS plaintext to attacker via caller-chosen `--public-key` | KMS `Decrypt` `--recipient` + document `public_key` | Only the key-policy `Principal` + PCR condition (hub Area 1); recipient key itself is unbound |
| Replay a document to a 3P verifier that omits the nonce check | Customer-built external service | Opt-in `nonce` only — not enforced by the document format |
| Treat attacker-supplied `user_data`/`nonce` as AWS-vouched content | 3P consumer parsing passthrough fields | None — signature binds presence, not meaning/structure |
| Substitute/tamper the `nitro-tpm-attest` minting binary | `aws-nitro-tpm-tools` / baked `/usr/bin/` | Undocumented (no stated GPG/pin); depends on erofs/dm-verity covering the binary |
| Mint a valid document from a non-trusted co-resident process | Guest OS (no IAM on generation) | None — attestation binds boot state, not caller principal |
| Embed a weak/oversized RSA recipient key | `--public-key` field | None stated (no minimum modulus documented) |

## 7. Out-of-Scope Risk Categories
- The Nitro Hypervisor's document signing and the Nitro Attestation PKI private keys (AWS service plane — HARD STOP, never probe/forge).
- The **KMS PCR gate, PCR under-binding, reproducible-measurement cross-account bypass, CRL-disabled validation, and COSE alg-pinning** — owned by `nitrotpm-attestation-attack-research-plan.md` (hub Areas 1–6) and `prepare-attestation-service-attack-research-plan.md`; cross-referenced here, not re-tested.
- The AMI-measurement supply chain (`nitro-tpm-pcr-compute`, KIWI build, PCR4/7/12 derivation) — owned by `build-sample-ami`/`attestable-ami`/`create-pcr-compute` plans.
- EK retrieval / enablement / verification — owned by `retrieve-ekpub`, `enable-nitrotpm-*`, `verify-nitrotpm-*`, `nitrotpm-instance` plans.
- A customer locking themselves out by misconfiguring their own recipient key or policy — self-footgun, not a boundary breach.
- The AL2023 repo's generic package-signing model (standard distro mechanism) except insofar as *this feature's docs* fail to state it (Area 2 scenario 1).

## 8. Null hypotheses / doc gaps

Lenses that did **not** fire for the retrieval-client surface, with pages checked (`attestation-get-doc.md`, `nitrotpm-attestation-document-content.md`, `nitrotpm-attestation-document-validate.md`, `build-sample-ami.md`, GitHub `NitroTPM-Tools` READMEs):
- **Lens G (SSRF):** Null. No field on this page is a URL/host the service dereferences; `--public-key` is key material, not a fetch target. (The only URL, the root-cert `.zip`, is a static AWS-published artifact fetched by the *verifier*, not server-side by AWS.)
- **Lens B/C (PassRole / credential vending):** Null. Generation requires no role; no service assumes a role on the caller's behalf. The downstream KMS call uses the ordinary caller IAM identity (hub territory).
- **Lens J/K (OAuth / prompt injection):** Null. No 3P-linking flow and no LLM/agent in the retrieval pipeline.
- **Lens P (identity proofing/OTP):** Null. The `nonce` is a liveness challenge for a *consumer's* protocol, not an onboarding/registration gate; no dedup/OTP workflow.
- **Lens I (tagging/ABAC), N (namespace migration), V/D (network segmentation), DD (cache), CC (trusted-header), BB (canonicalization):** Null — a guest-local CLI → signed-blob flow with no HTTP router/authorizer/cache/ENI story.
- **Lens X (action-family parity):** Null for this page — `nitro-tpm-attest` has no legacy alias or lower-level API twin for document generation.

Doc gaps (confirm surface before investing):
- Whether `nitro-tpm-attest` document generation truly requires **no IAM** is inferred from silence + "interact with the TPM2 device" — confirm live (Area 3 scenario 1).
- Whether `aws-nitro-tpm-tools` is GPG/signature-verified and version-pinned is **not stated** on these pages (Area 2) — doc gap, not confirmed absence.
- Whether KMS/NitroTPM validate the embedded RSA `public_key` modulus size / reject oversized DER (Area 4) — unstated.
- Whether `/usr/bin/nitro-tpm-attest` falls inside the `erofs`/`dm-verity` measured read-only region in the sample AMI (Area 2 scenario 2) — resolve against `al2023-isolated-compute-recipe`/`customize-sample-ami`.
- **Deferred to hub (not gaps, owned elsewhere):** the KMS replay oracle (hub Area 4), reproducible-measurement/broad-Principal bypass (hub Area 1), CRL-disabled 3P validation (hub Area 5), COSE alg-pinning (hub Area 6), document field semantics / PCR under-binding (hub Area 2) — all cited here only as chain preconditions.
