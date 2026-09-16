# NitroTPM Attestation Document Retrieval (`attestation-get-doc` / `nitro-tpm-attest`) — Attack Research Plan

**Source of leads:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-get-doc.html` (primary target) plus the immediate family it links: `nitrotpm-attestation-document-content.html`, `nitrotpm-attestation-document-validate.html`, `attestation-attest.html`, `prepare-attestation-service.html`, `nitrotpm-attestation.html` (hub), `build-sample-ami.html`, and `kms/latest/developerguide/conditions-nitro-tpm.html`. Offline mirror `/work/aws-docs` + live docs.aws.amazon.com. **Live == offline, verified 2026-09-13 (no sync drift).**
**Status:** documentation-derived hypotheses only; nothing tested against a live account.
**Scope note:** This target is a **focused CHILD** of the NitroTPM attestation family. The broad hub, KMS condition-key semantics, and Attestable-AMI supply chain are covered by the pre-existing `/work/aws-docs/nitrotpm-attack-research-plan.md` (224 lines) and the `nitrotpm-plan` / `iid-plan` memories. **This plan concentrates on what is unique to the document-*retrieval* + *validation* slice:** the `nitro-tpm-attest` utility, the three optional params (`public-key`/`user-data`/`nonce`), the CBOR/COSE document structure, and the AWS-published validation procedure. Deep KMS-policy hunting is routed to the hub plan; do not re-derive it here.

**No "See also" / AI-agent CLI injection block on this page** (live or offline, checked 2026-09-13). Cf. `[[aws-docs-see-also-injection]]`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/private key belonging to AWS's own service plane — the **Nitro Hypervisor attestation signing key**, the **AWS Nitro Attestation PKI private key** (`CN=aws.nitro-enclaves`), or **AWS KMS's own attestation-document parser/validator** — stop, preserve evidence, flag for AWS-Security disclosure. Never mint a forged document against production KMS; analysis only.
- **Two owners split this surface.** (a) The instance-local `nitro-tpm-attest` tool and any **customer/3rd-party verifier** the customer builds → mostly customer-owned exploitation. (b) The **KMS built-in verifier** and the **Nitro signing PKI** → AWS service-plane, hard-stop. The **AWS-owned reportable core** is the *design* of the document and the *published validation guidance* (Areas A, B, C below), not a control-plane API — there is no EC2 API on this page.

---

## 1. Pentest Objectives
Stated as concrete breach outcomes:
1. **Cross-account KMS decrypt via code-only attestation.** Cause AWS KMS to release plaintext (as `CiphertextForRecipient`) to an instance in **account B** against a key whose policy the owner (account A) believed was bound to their instances — because the Attestation Document proves *which code booted*, never *who owns the instance*, and the reference PCRs are attacker-reproducible.
2. **Replay / stale-liveness acceptance.** Get a verifier (KMS or a 3P service) to accept an Attestation Document from an instance that is terminated, cloned, or no longer trustworthy, exploiting the documented fact that **`nonce` is "Not used for attestation with AWS KMS."**
3. **Revoked-certificate acceptance.** Get a 3P verifier to trust an Attestation Document whose Nitro PKI intermediate has been revoked, exploiting the AWS-published instruction to **disable CRL checking** (`setRevocationEnabled(false)`).
4. **Parser compromise.** Crash/corrupt/hang a CBOR/COSE Attestation-Document parser (KMS's = hard stop; a customer/3P verifier's = customer-owned) via length/depth/size fields the CBOR structure exposes.
5. **Weak recipient-encryption.** Defeat the `CiphertextForRecipient` confidentiality guarantee by supplying a weak/small RSA `public-key` the tool/KMS does not reject.

---

## 2. Components, Assets, and Design

### What this page actually describes
- **`nitro-tpm-attest`** — an **instance-local userspace utility** (single command), installed on Amazon Linux 2023 via `sudo yum install aws-nitro-tpm-tools`, and **preinstalled** into `/usr/bin/` by the sample AL2023 image description. It calls down to the NitroTPM to obtain a signed **Attestation Document**. Source: `github.com/aws/NitroTPM-Tools/` (out-of-scope 3P repo, but the *packaged binary from the AL repo* is the in-band artifact).
- **The Attestation Document** — a CBOR-encoded, **COSE_Sign1**-signed blob. **Signed by the Nitro Hypervisor** using **ECDSA P-384** (`{1: -35}` = "ECDS 384"), chained to the **AWS Nitro Attestation PKI** root (`CN=aws.nitro-enclaves, C=US, O=Amazon, OU=AWS`, 30-yr PCA, fingerprint `64:1A:03:…:5B`, downloadable zip).
- **Two verifiers:**
  - **AWS KMS** (built-in): validates PCRs against `kms:RecipientAttestation:NitroTPMPCR{4,7,12}` in the key policy; on match, encrypts the plaintext under the doc's `public_key` and returns `CiphertextForRecipient` (on `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom`).
  - **Customer/3P verifier** (build-your-own): follows the AWS-published `validate` procedure.

### Attestation Document structure (from `nitrotpm-attestation-document-validate`)
```
module_id, timestamp (uint .size 8, ms since epoch), digest ("SHA384"),
nitrotpm_pcrs { index(0..31) => pcr(bytes 32/48/64) },
certificate (cert bytes 1..1024), cabundle [* cert],
? public_key (user_data bytes 0..1024),
? user_data  (bytes 0..1024),
? nonce      (bytes 0..1024)
```
COSE_Sign1 = `[protected Header, unprotected Header, payload, signature]`, CBOR tag 18, alg `{1:-35}`.

### The three optional `nitro-tpm-attest` parameters (the heart of this page)
| Param | Purpose (verbatim intent) | KMS path | 3P path |
|---|---|---|---|
| `public-key` | Recipient-encryption key; embedded in doc; response ciphertext encrypted under it. **"Only RSA keys are supported."** No documented min size/validation. | **Used** (produces `CiphertextForRecipient`) | optional |
| `user-data` | "additional signed data … complete an agreed protocol." | **"Not used for attestation with AWS KMS."** | protocol-defined |
| `nonce` | "challenge-response authentication … verify it is interacting with a **live** instance and not an impersonator that is **reusing an old Attestation Document**." | **"Not used for attestation with AWS KMS."** | opt-in |

### Critical asset facts (drive the leads)
- **The document carries NO account / instance-owner / tenant identity.** It attests *code+config* (PCRs) + optional bytes. Ownership binding, if any, lives entirely in the **KMS key-policy `Principal`** (SigV4), not in the attestation.
- **Reference PCRs are attacker-reproducible.** `build-sample-ami` states the public `nitro-tpm-pcr-compute` utility computes the reference measurements from the AMI's UKI at build time (`pcr_measurements.json`). Anyone who possesses / is shared / rebuilds the same Attestable AMI computes the identical PCR4/7/12 values → they are **not secrets**.
- **KMS condition key is Single-valued**, lowercase-hex up to 96 bytes, compared with `StringEqualsIgnoreCase` (confirmed in `conditions-nitro-tpm`). No enforced PCR *pairing* — a policy can pin PCR4 alone and drop PCR12 cmdline integrity.
- **PCR0/PCR1 are constant AWS-controlled values** (documented) → carry no tenant/customer entropy.
- **Validation guidance disables revocation:** `validate` page + Java sample sets `setRevocationEnabled(false)` and states "CRL must be disabled."

### ASCII pipeline
```
                                (AWS service plane — HARD STOP)
 [Attestable AMI] --nitro-tpm-pcr-compute--> reference PCRs (NOT SECRET, reproducible)
        |
        v launch (NitroTPM-enabled instance, customer acct)
 ┌─────────────────────────────────────────────┐
 │ Customer instance                            │
 │  app --gen RSA keypair--> pub/priv           │
 │  nitro-tpm-attest --public-key --user-data --nonce
 │        |                                      │
 │        v  (measured boot: PCRs)               │
 │   NitroTPM  --> [doc] --signed by--> Nitro Hypervisor (ECDSA P-384)  ← signing key = HARD STOP
 └────────┬──────────────────────────────────────┘
          │ doc = CBOR/COSE_Sign1 (module_id,timestamp,PCRs,cert,cabundle,pub,userdata,nonce)
          v
   ┌──────────────┐        ┌──────────────────────────┐
   │  AWS KMS     │        │ Customer/3P verifier      │
   │ (built-in)   │        │ (build-your-own; CRL off) │
   │ PCR match →  │        │ chain to Nitro PKI root   │
   │ CiphertextForRecipient│ + your own freshness/nonce│
   │ (enc under doc pub_key)│ + your own tenant binding│
   └──────────────┘        └──────────────────────────┘
   nonce IGNORED here        nonce/user_data usable here
```

---

## 3. API / Interface Inventory
There is **no EC2 control-plane API on this page.** The interface surface is a local CLI + a document format + two verifiers.

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `nitro-tpm-attest --public-key/--user-data/--nonce` | local CLI | Existing | Non-mut. (reads TPM) | Instance-local | Retrieve signed Attestation Document | No | Any local process that can run the binary (root-installed in `/usr/bin`) | Client-side. Local privilege only; not a network boundary. |
| `yum install aws-nitro-tpm-tools` | pkg install | Existing | Mutating (host) | AL2023 repo | Install utility | No (repo pull) | root | **Supply-chain: package + repo signing (AL-repo owned).** |
| KMS `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom` **with `Recipient`=attestation doc** | SigV4 API | Existing | Non-mut. | External (KMS) | Verify PCRs → return `CiphertextForRecipient` | Yes | KMS key-policy `Principal` + PCR condition | The **doc is caller-supplied input** to KMS's parser. Attacking KMS's parser = HARD STOP. |
| Attestation Document (CBOR/COSE blob) | data artifact | Existing | n/a | flows customer→verifier | Signed measurement bundle | n/a (transported by caller) | anyone who obtains it | **Untrusted blob to any 3P verifier.** |
| Nitro Attestation PKI root cert (`AWS_NitroEnclaves_Root-G1.zip`) | HTTPS download | Existing | Non-mut. | `aws-nitro-enclaves.amazonaws.com` | trust anchor | Yes | public | Pinned by fingerprint; TOFU on first fetch (Lens Y). |

**Undocumented-knob hunt:** the GitHub tool may expose flags beyond the three documented (`--public-key/--user-data/--nonce`). Enumerate the packaged binary's real flag set vs the doc — a param that weakens key validation or accepts a non-RSA/short key is a lead (Lens U doc-vs-impl delta). *(Binary is in the AL repo; the GitHub repo itself is out-of-scope 3P source.)*

---

## 4. Boundary-lens catalog — findings

### FIRING LENSES

#### ★★ Lens W — Attestation-conditioned authorization (the core; code-not-tenant)
**Claim:** A KMS key whose policy grants Decrypt/GenerateDataKey to instances *of the owner* can be satisfied by an instance in a **different account** that boots the **same Attestable AMI**, whenever the policy pins only `kms:RecipientAttestation:NitroTPMPCR*` without a tenant-scoping `Principal`.
**Mechanism:** The Attestation Document contains **no account/owner identity** (`content` page structure); the PCR condition is the *only* attestation-derived gate, is **Single-valued**, uses `StringEqualsIgnoreCase`, and its reference values are **attacker-reproducible** via the public `nitro-tpm-pcr-compute` on any copy of the AMI (`build-sample-ami`). Nothing in the attestation binds the requester's account. → routes to `[[nitrotpm-plan]]` hub for full KMS-policy sweep.
**Confirm/Refute oracle:** In a controlled 2-account test, launch the same Attestable AMI in account B; call `Decrypt` with a fresh account-B keypair against account A's key whose policy has PCR conditions and `Principal:"*"` (or a broad org principal). **Breach = account B receives valid `CiphertextForRecipient` it can decrypt with its own private key.** Fail-closed = `AccessDenied`.
**Sub-oracles / gate-fail-open (attack the condition itself):**
- **Absent-attestation fail-open:** does a request with *no* `Recipient`/attestation doc still satisfy a PCR-conditioned statement (evaluated as no-key-present → allowed)? Doc says the condition "is effective only when the `Recipient` parameter … specifies a signed attestation document" — probe whether a statement lacking a paired `Bool aws:… present` guard fails **open** for requests that omit the doc. Fail-closed = deny.
- **Under-binding:** PCR4-only policy (drops PCR12 cmdline integrity) — can a differently-cmdline'd boot with matching PCR4 pass? (Single-valued, no enforced pairing — confirmed.)
- **Wildcard/case:** `StringLikeIgnoreCase … "abc*"` or all-zeros PCR (e.g. the `PCR12:"0000…"` shown in `prepare-attestation-service` — an all-zero measurement) — does an all-zero/debug value match unintended boots?
**Preconditions:** 2 authorized accounts; a shared/rebuildable Attestable AMI. **Cost:** medium. **Severity if true:** cross-account KMS decrypt = **Critical**. Under-binding / all-zero match = **High**.
**Stop condition:** stop before touching KMS's signing/validation internals; this tests *customer policy composition* + the *documented mechanism*, not KMS's plane. If evidence shows KMS accepting a **forged** (non-Nitro-signed) doc → HARD STOP + disclose.

#### ★ Lens U — Documented-guarantee vs actual enforcement (+ nonce/liveness gap)
**Claim 1 (liveness):** The hub promises attestation lets you "cryptographically prove … only trusted software … is running" and prevent "an impostor reusing an old Attestation Document" — yet on the **KMS path the `nonce` is explicitly "Not used."** So KMS proves *code identity + recipient-key possession*, **not liveness**. A document captured from an instance that has since been **terminated, snapshotted/cloned, or compromised post-boot** still validates at KMS as long as PCRs match and the caller holds the matching private key.
**Mechanism:** `attestation-get-doc` verbatim: `nonce` "Not used for attestation with AWS KMS"; the anti-replay compensation on the KMS path is only the `public_key` recipient-encryption (confidentiality binding, *not* freshness/liveness binding). `timestamp` exists in the doc but there is **no documented KMS staleness/skew check** on it.
**Confirm/Refute oracle:** capture an instance's Attestation Document + retain its private key; **after the instance is stopped/terminated**, replay the same doc to KMS `Decrypt`. Breach = KMS still returns valid `CiphertextForRecipient` (proves no liveness/freshness enforcement). Also: query `ct-nitro-tpm` CloudTrail — does the event record the doc `timestamp` (so an operator *could* detect staleness) or not?
**Claim 2 (doc-vs-impl):** "Only RSA keys are supported" for `public-key` — is there a **minimum key size**? Nothing documents one. A 512/1024-bit RSA recipient key, if accepted by the tool + KMS, makes `CiphertextForRecipient` **factorable/crackable**, defeating the whole confidentiality guarantee. (See Lens H.)
**Severity:** liveness-gap is **AWS-owned design, Info→Medium** (real impact realized only in a verifier that assumed liveness); weak-RSA acceptance = **High** if unbounded. **Reportable core** = the documented guarantee ("prove … running", "prevent impostor reusing old doc") vs the KMS path silently dropping the `nonce` that delivers it.

#### ★ Lens AA — Revocation completeness ("CRL must be disabled")
**Claim:** A 3P verifier following AWS's published procedure will trust an Attestation Document even if the signing **Nitro PKI intermediate certificate has been revoked**, because AWS instructs `setRevocationEnabled(false)` / "CRL must be disabled."
**Mechanism:** `nitrotpm-attestation-document-validate` §"Certificate chain validity" note + Java `validateCertsPath` sample both **disable revocation**. So a compromised/rotated-out intermediate remains trusted until natural expiry (root is a **30-year** PCA).
**Confirm/Refute oracle:** documentation-level = confirmed as written (revocation off by design). Live/impact oracle (customer-owned verifier): a doc signed by a revoked-but-unexpired intermediate passes `validateCertsPath`. Also check whether the **KMS built-in verifier** likewise ignores revocation (that would be AWS-owned).
**Severity:** AWS-owned validation *guidance* weakness = **Medium/Info** (it removes revocation as a control across the whole ecosystem of 3P verifiers); if KMS itself ignores Nitro-PKI revocation = **High** and disclose.
**Stop condition:** do not attempt to obtain or use a genuinely revoked Nitro cert; reason from the documented procedure.

#### Lens F / Q — CBOR/COSE parser memory-safety & untrusted-blob validation
**Claim:** The Attestation Document is an **attacker-shapeable CBOR/COSE blob** fed to a parser (KMS's, or the customer's 3P verifier). The structure exposes explicit **length/size/depth** fields — `cert bytes 1..1024`, `user_data 0..1024`, `pcr 32/48/64`, `index 0..31`, `cabundle [* cert]` (unbounded array), nested maps. A parser that trusts a declared length/size before bounds-checking, or that recurses on `cabundle`/nested CBOR without a depth cap, is exploitable (OOB read, UAF, alloc-bomb, hang).
**Mechanism:** `validate` page CDDL + COSE_Sign1 spec; native CBOR/COSE parsing implied.
**Confirm/Refute oracle:** *(3P verifier / offline analysis only)* feed malformed docs: oversized `cert` (>1024), `pcr` of wrong size (not 32/48/64), `index`>31, deeply-nested `cabundle`, truncated COSE array, wrong CBOR tag (≠18), duplicate map keys. Breach = crash/hang/OOB in the verifier. **Against AWS KMS this is a HARD STOP** — do not fuzz KMS's parser; note as a service-plane hypothesis for AWS-Security only.
**Severity:** 3P/customer parser crash = **Medium**; any signal of KMS-parser corruption = **Critical + HARD STOP**.

#### Lens H — Recipient-key / encryption-context confusion
**Claim:** The `public_key` recipient encryption can be defeated or confused: (a) weak/small RSA accepted (see Lens U Claim 2) → `CiphertextForRecipient` crackable; (b) is the RSA key **bound to the attesting instance's identity** at all, or can a caller embed **any** public key (including one whose private half a third party holds) → misdirected plaintext? Since the doc has no owner identity, the only recipient binding is "whoever holds the private key for the embedded public key."
**Mechanism:** `attestation-get-doc` (public-key param), `attestation-attest` (`CiphertextForRecipient` under doc public key), "Only RSA keys are supported," no size floor documented.
**Oracle:** supply a 512-bit RSA `public-key`; observe whether tool/KMS reject it. If accepted, `CiphertextForRecipient` from a real `GenerateDataKey` is factor-and-decrypt (analysis on your own data only). Also test: does KMS validate padding/OAEP vs PKCS1v1.5 (padding-oracle surface)?
**Severity:** weak-RSA accepted = **High**; padding-oracle on KMS = HARD STOP.

#### Lens Y — Transport / trust-anchor bootstrap
**Claim:** The Nitro PKI **root cert is fetched over HTTPS** (`aws-nitro-enclaves.amazonaws.com/AWS_NitroEnclaves_Root-G1.zip`) and pinned only by a **published fingerprint** the operator must check manually. A verifier that trusts-on-first-use without checking the fingerprint, or fetches over a MITM-able path, roots its whole chain in an attacker cert.
**Mechanism:** `validate` page download URL + fingerprint.
**Oracle:** *(customer verifier)* does the verifier hardcode/verify the fingerprint, or fetch-and-trust? Design-level: AWS ships the anchor as a zip + manual fingerprint (no automatic pinning). **Severity:** Medium (customer-owned verifier bootstrap; AWS-owned distribution mechanism).

#### Lens R / S — AWS-published sample KMS key policy (in `prepare-attestation-service`)
**Claim:** The AWS-authored sample policy is copied verbatim by customers. Audit it: it **does** scope `Principal` to `role/MyEC2InstanceRole` **and** pins PCR4+PCR12 → reasonably tight. But note the **all-zero `PCR12:"0000…"`** value in the example and the single-valued conditions: a customer who copies the shape but omits/broadens `Principal` (a common edit) loses the *only* tenant binding (feeds Lens W). Also `Resource:"*"` in the sample (typical for key policies, benign in-key).
**Move:** for the *managed* condition-key semantics and any AWS-managed policy, resolve via `conditions-nitro-tpm` (done: Single-valued, hex≤96B) and route the managed-policy audit to `[[nitrotpm-plan]]`.
**Oracle:** `iam:SimulateCustomPolicy` on the sample as-written (should deny cross-account) vs the sample with `Principal:"*"` (should allow → demonstrates the footgun magnitude).
**Severity:** the *sample as written* is sound (**Info**); the mechanism's reliance on the customer to add `Principal` for tenant isolation, given code-only attestation, is the **High** systemic point (Lens W).

#### Lens O — Audit (minor, enabler)
**Claim:** `ct-nitro-tpm` CloudTrail records the PCR condition value; verify whether it also records enough (doc `timestamp`, `module_id`) to *detect* replay/staleness after the fact. If the KMS event omits doc `timestamp`/`module_id`, defenders cannot spot a replayed/cloned-instance doc.
**Severity:** Low/Informational (raises Lens U impact as a detection gap).

### NULL HYPOTHESES (pages checked — `attestation-get-doc`, `attestation-attest`, `-content`, `-validate`, `prepare-attestation-service`, `nitrotpm-attestation` hub, `conditions-nitro-tpm`)
- **Lens A (cross-tenant IDOR):** N/A on this page — no resource-by-id EC2 API, no opaque IDs, no "hosts multiple customers" fleet described. (The cross-account concern is realized through Lens W, not an IDOR.)
- **Lens B/C (PassRole / credential vending):** N/A — the utility passes **no role ARN**; KMS auth is the caller's own SigV4. No STS session-policy/ProvidedContext construction here.
- **Lens D/V (data→control plane / network segmentation):** N/A — no ENIs, VPCs, control-plane hosts, or fleet described on this page. NitroTPM is instance-local hardware.
- **Lens E (RBAC privesc):** N/A — no roles/hidden admins in this slice.
- **Lens G (SSRF):** N/A — no server-side-dereferenced URL field on these pages. The only URL (`public-key`) is a key blob, not a fetch target; the root-cert zip is a client-side download (covered under Y). Checked all six family pages — no `*Url`/`*Uri`/webhook/import field the service fetches.
- **Lens I (tagging/ABAC):** N/A — no tag operations in this slice.
- **Lens J (OAuth/3P linking):** N/A.
- **Lens K (prompt injection):** N/A — no LLM/agent in the attestation pipeline.
- **Lens L (DoS):** partially folded into Lens F (parser resource exhaustion); no shared-fleet multi-tenant surface on this page. NitroTPM per-instance.
- **Lens M (shared-identifier interception):** N/A — the doc `public_key` is the recipient binding (covered under H); no session-id/presigned-URL surface here.
- **Lens N (namespace migration):** N/A — no dual ARN/endpoint migration.
- **Lens P (registration/OTP):** N/A — no proofing/OTP/uniqueness workflow.
- **Lens T (cross-service secret reachability):** N/A on this page — the RSA private key is generated and **stays in the instance** (not persisted to SSM/Secrets Manager by this flow). *(If a customer app stores it, that's their design.)*
- **Lens X (action-family parity):** N/A — no EC2 action family here; the KMS Decrypt/GenerateDataKey family variance is governed by KMS, not this page.

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Code-not-tenant → cross-account KMS decrypt (Lens W)  ★★ **Critical if true**
**Background:** The Attestation Document proves booted code (PCRs) + recipient key possession, never instance ownership; reference PCRs are reproducible from any copy of the (shareable) Attestable AMI via public `nitro-tpm-pcr-compute`.
**Security Concern:** A KMS policy pinning only PCR conditions (no/loose `Principal`) is satisfiable by *any* account launching the same AMI.
**Test Scenarios:** (a) 2-account decrypt with `Principal:"*"` + PCR conditions; (b) absent-attestation fail-open probe; (c) PCR4-only under-binding; (d) all-zero/wildcard PCR match. **Doc evidence:** `-content` (no owner field), `build-sample-ami` (public PCR compute), `conditions-nitro-tpm` (Single-valued). **Severity:** Critical (cross-account) / High (under-binding). Route full KMS-policy sweep to `[[nitrotpm-plan]]`.

### Area 2 — nonce-disabled-for-KMS liveness/replay gap (Lens U)  ★ **AWS-owned design**
**Background:** KMS path drops the `nonce` that the docs sell as the anti-impersonation/liveness proof.
**Security Concern:** KMS proves code+key-possession, not liveness; a doc from a since-terminated/cloned/compromised instance still validates.
**Test Scenarios:** replay a retained doc+privkey after instance teardown to KMS Decrypt; check CloudTrail records `timestamp`/`module_id` for post-hoc detection. **Doc evidence:** `attestation-get-doc` ("Not used for attestation with AWS KMS"), `nitrotpm-attestation` hub ("prevent impostor reusing an old Attestation Document"). **Severity:** Info→Medium (design); realized-High in a liveness-assuming verifier.

### Area 3 — Revocation disabled in AWS validation guidance (Lens AA)  ★
**Background:** AWS instructs 3P verifiers to disable CRL/revocation; root is a 30-yr PCA.
**Security Concern:** a revoked-but-unexpired Nitro intermediate stays trusted across the whole ecosystem of build-your-own verifiers.
**Test Scenarios:** confirm the published Java sample disables revocation (done, as written); test whether KMS's own verifier ignores Nitro-PKI revocation. **Doc evidence:** `-validate` "CRL must be disabled" + `setRevocationEnabled(false)`. **Severity:** Medium (guidance) / High + disclose if KMS ignores revocation.

### Area 4 — Weak-RSA recipient key & padding (Lens H/U)
**Background:** "Only RSA keys are supported," no documented min size or padding scheme for the recipient key.
**Security Concern:** small-RSA acceptance makes `CiphertextForRecipient` crackable; unclear padding → oracle surface (KMS side = hard stop).
**Test Scenarios:** submit 512/1024-bit RSA; observe accept/reject. **Doc evidence:** `attestation-get-doc`, `attestation-attest`. **Severity:** High if unbounded.

### Area 5 — CBOR/COSE parser & supply chain (Lens F/Q)
**Background:** attacker-shapeable CBOR/COSE doc with explicit size/depth fields; utility delivered via `yum install aws-nitro-tpm-tools`.
**Security Concern:** parser memory-safety in **3P/customer verifiers** (KMS parser = HARD STOP); AL-repo package/signing integrity for the delivered binary.
**Test Scenarios:** malformed-doc fuzz against a *customer* verifier only; verify AL2023 repo GPG signing of the package. **Doc evidence:** `-validate` CDDL; `attestation-get-doc` install cmd. **Severity:** Medium (3P parser); Critical+HARD STOP (KMS parser); repo-signing is AL-owned.

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account decrypt via same-AMI PCRs | KMS key policy + Attestation Doc | `Principal` scoping in key policy (attestation itself has none) |
| Replay of stale/cloned-instance doc | KMS built-in verifier | `nonce` (**disabled for KMS**) / doc `timestamp` (no documented KMS check) |
| Trust a revoked Nitro intermediate | 3P verifier (+ KMS?) | Cert-chain validation with **CRL disabled by instruction** |
| Crack `CiphertextForRecipient` | recipient RSA key | "Only RSA supported" (no min size documented) |
| Corrupt/hang the doc parser | CBOR/COSE parser (3P; KMS=stop) | CDDL size/type constraints (parser must enforce) |
| Root-anchor MITM/TOFU | 3P verifier bootstrap | Published SHA-256 fingerprint (manual check) |
| Under-binding (PCR4 w/o PCR12) | KMS condition keys | Single-valued keys; customer must pin PCR4+PCR12 |

---

## 7. Out-of-Scope Risk Categories
- **The instance-local `nitro-tpm-attest` binary as a local-privilege surface** (arg handling, who can run it) — local/customer-owned, not a network trust boundary.
- **NitroTPM / Nitro Hypervisor hardware isolation and the Nitro signing key / attestation PKI private key** — AWS service plane; **HARD STOP** if reached.
- **AWS KMS's own attestation-document parser/validator internals** — service plane; do not fuzz; hypotheses for AWS-Security only.
- **The out-of-scope `github.com/aws/NitroTPM-Tools` source repo** — 3P reference code (the AL-repo *packaged binary* is the in-band artifact).
- **Customer-authored KMS key policies and customer-built 3P verifiers** — the *composition* mistakes are customer footguns; the reportable AWS core is the *mechanism/guidance* that makes those mistakes catastrophic (code-only attestation, nonce-off-for-KMS, CRL-off).
- **Attestable AMI build supply chain / reference-measurement generation** — covered by `[[nitrotpm-plan]]` hub, not re-derived here.
- **IMDS on managed hosts; single-instance self-DoS.**

## 8. Null hypotheses / doc gaps
- **Lenses A, B, C, D, E, G, I, J, K, M, N, P, T, V, X = N/A** on this slice (see §4 NULL, with pages named). This is deliberately a *client-side utility + document-format + verifier-guidance* page; it has **no EC2 control-plane API, no role/URL/tag/registration surface.**
- **Doc gaps to confirm on a live/tool basis first:**
  - Does the tool/KMS enforce a **minimum RSA key size** and a specific **padding** for `public-key`? (Not documented → Area 4.)
  - Does KMS perform **any `timestamp` staleness check**, and does `ct-nitro-tpm` record `timestamp`/`module_id`? (Not documented → Areas 2/6.)
  - Does a PCR-conditioned KMS statement **fail open** for a request that omits the `Recipient` doc entirely? (Doc says condition "effective only when `Recipient`… specifies a doc" — the fail-open shape is unconfirmed → Area 1b.)
  - The **real flag set** of the packaged `nitro-tpm-attest` vs the three documented params (undocumented-knob delta).
- **Live-vs-mirror:** target page byte-identical live vs offline 2026-09-13; **no See-also/AI-agent injection block** on this page (cf. `[[aws-docs-see-also-injection]]` which affects other EC2 pages).

---

### Completion notes for the next agent
- **Crown jewels, in order:** (1) code-not-tenant → cross-account KMS decrypt when `Principal` is loose [Critical]; (2) `nonce` disabled for KMS = no liveness/replay defense on that path [design, Info→High]; (3) AWS guidance disables CRL/revocation [Med, High if KMS too]; (4) unbounded RSA recipient key [High]; (5) CBOR/COSE parser [Med / HARD STOP for KMS].
- **This plan is the *retrieval+validation* child.** The KMS condition-key sweep, Attestable-AMI supply chain, and the broad hub live in `/work/aws-docs/nitrotpm-attack-research-plan.md` and memories `[[nitrotpm-plan]]`, `[[iid-plan]]`. Do not duplicate; chain to them for the cross-account KMS proof.
- **Hard stops:** Nitro signing key, Nitro Attestation PKI private key, KMS's own doc parser/validator. Analysis-only on any forged-document hypothesis; never mint against production KMS.
