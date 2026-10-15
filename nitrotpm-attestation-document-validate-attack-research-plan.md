# NitroTPM Attestation Document *Validation* — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-attestation-document-validate.html`
(online `.md` twin + offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/nitrotpm-attestation-document-validate.md`
— **byte-identical, no drift, verified 2026-10-15**). Status: documentation-derived hypotheses only; nothing tested
against a live account.

> **This plan is the PAGE-LEVEL deep-dive COMPLEMENT of the attestation hub**
> (`nitrotpm-attestation-attack-research-plan.md`). The hub already OWNS the **AWS-KMS gate** path and its PCR-defeat
> layer (its A1 reproducible-measurement, A2 all-zeros-PCR12, A3 key-family confusion, A4 KMS-replay/nonce, A5
> CRL-disabled, A6 COSE-alg-pin). **This target page is the DOC-EVIDENCE SOURCE the hub cites for A5/A6** — so this
> plan does NOT restate the KMS path. It OWNS the one surface the hub only summarised: the **third-party-validator
> *recipe itself*** — the exact 4-step procedure + CDDL + Java `CertPathValidator` snippet an external key-management
> service is told to implement verbatim when it is **NOT** using AWS KMS. Siblings cross-referenced:
> `prepare-attestation-service-*` (KMS key-policy artifact), `nitrotpm-attestation-document-content-*` (PCR-semantics
> catalog), `attestation-get-doc-*` (the `nitro-tpm-attest` retrieval client / request-side passthrough fields).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop
  condition.** Work in priority order; look left and right for adjacent bugs.
- **Scope note (read first — this changes what "a finding" is here).** This page contains **no AWS API, no IAM policy,
  no live AWS endpoint under test.** It is an **AWS-authored validation *recipe*** — prose + a CDDL schema + a Java
  snippet — that a customer's **third-party** key-management service is instructed to build its attestation-document
  validator from. The attack surface is therefore the **class of validator a reader faithfully implementing this page
  produces**, and the defects are in the **recipe** (omissions / insecure framing AWS ships), analogous to Lens-R
  "AWS-published sample CODE insecure defaults." A hunter cannot "exploit docs.aws.amazon.com" here; a hunter
  **(a)** audits the recipe for what a faithful implementation gets wrong, and **(b)** tests a *reference / customer*
  validator built from it with attacker-supplied attestation documents (the attacker's own genuine Nitro instance is
  a legitimate, cheap document source — see Area 1 preconditions).
- **What "breach" means on this page:** the external service's attestation gate is the **sole control** over whatever
  it protects (secrets, key release, admission). A breach = **the gate grants trust to a document it should reject** —
  from the wrong instance (wrong PCRs), stale (replay), with a substituted signature/algorithm, or chained to an
  attacker-supplied root.
- **HARD STOP:** never attempt to forge, extract, or MITM the AWS Nitro Attestation PKI signing key / intermediate CAs.
  The moment evidence touches AWS's own signer or service plane, stop, preserve evidence, flag for AWS-Security.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce against a validator built from this recipe:
1. **Trust-decision bypass (headline):** make a validator built from the documented 4 steps *accept* an attestation
   document produced by an **attacker-controlled** NitroTPM instance (different boot measurements / different account)
   and treat it as "a trustworthy entity" — proving the recipe authenticates the *PKI* but never binds *what was
   measured*.
2. **Replay:** have the same validator accept a **stale, previously-captured** document (no freshness/TTL/nonce check
   in the procedure).
3. **Signature / algorithm substitution:** have the validator accept a document whose COSE protected header /
   algorithm / signed-bytes were manipulated, because the recipe says only "ensure properly signed" without pinning
   `alg = ES384` or specifying the COSE_Sign1 `Sig_structure`.
4. **Chain / trust-anchor confusion:** have the validator build a path to an **attacker-supplied root** carried in the
   document's own `cabundle`, because the recipe reverses and consumes the attacker-supplied bundle and never says
   "pin `cabundle[0]`/the anchor to the published fingerprint."
5. **Revocation blindness:** have the validator accept a document in a chain containing a **revoked** cert, because the
   recipe mandates `setRevocationEnabled(false)` / "CRL must be disabled" with no stated compensating bound.
6. **Parser DoS:** crash or hang the validator with a malformed / oversized / deeply-nested CBOR blob or an unbounded
   `cabundle` array (self-DoS of the external service; cross-tenant DoS if that service is multi-customer).

---

## 2. Components, Assets, and Design

**What the page describes.** The *consumer side* of the NitroTPM attestation flow for the **non-AWS-KMS** case: how an
external ("third-party") key-management / relying-party service must parse and validate the signed Attestation Document
an EC2 NitroTPM instance obtained (via `nitro-tpm-attest`, owned by `attestation-get-doc-*`) and presented to it.

**Actors / assets:**
- **Attesting instance** — a NitroTPM-enabled EC2 instance. Its Nitro system is the root of trust and signs the
  document. *Any* such instance (incl. an attacker's own, in the attacker's own account) can mint genuine documents.
- **AWS Nitro Attestation PKI** — root `AWS_NitroEnclaves_Root-G1` (AWS Private CA, 30-yr lifetime, subject
  `CN=aws.nitro-enclaves, C=US, O=Amazon, OU=AWS`), published at
  `https://aws-nitro-enclaves.amazonaws.com/AWS_NitroEnclaves_Root-G1.zip`, pinned by SHA-256 fingerprint
  `64:1A:03:21:A3:E2:44:EF:E4:56:46:31:95:D6:06:31:7E:D7:CD:CC:3C:17:56:E0:98:93:F3:C6:8F:79:BB:5B`. **This is the
  Nitro Enclaves PKI (shared root of trust).** *HARD STOP asset — never target the signer.*
- **The Attestation Document** (the untrusted input): CBOR-encoded, COSE_Sign1-signed (CBOR tag 18), COSE algorithm
  `{1: -35}` = ECDSA P-384 (ES384), `digest = "SHA384"`. Fields: `module_id` (text), `timestamp` (uint, ms since
  epoch), `digest`, `nitrotpm_pcrs` (`{+ index => pcr}`, `index = 0..31`, `pcr = bytes .size (32/48/64)`),
  `certificate` (`cert = bytes .size (1..1024)`), `cabundle` (`[* cert]` — **unbounded array**), and three OPTIONAL
  caller-passthrough fields `public_key` / `user_data` / `nonce` (each `bytes .size (0..1024)`).
- **The validator the customer builds** — the actual code under test. The page's prose + CDDL + Java
  `CertPathValidator` (PKIX, `setRevocationEnabled(false)`) snippet are its specification.

**Pipeline (consumer side):**
```
attacker/legit NitroTPM instance                3rd-party key-mgmt / relying-party service (customer-built)
  Nitro system signs ──► Attestation Document ──►  [ CBOR decode ] ──► [ extract COSE_Sign1 ]
  (genuine PKI sig over                              │                      │
   attacker-chosen PCRs,                             ▼                      ▼
   stale timestamp possible)                 [ verify cert chain ]    [ ensure signed ]
                                                     │                      │
                                                     └──────► GRANT TRUST ◄─┘   ← recipe STOPS here
                                     (PCR-value check? nonce freshness? timestamp TTL?  = "custom protocol", OPTIONAL)
```
The gap between "GRANT TRUST" and the optional, unspecified "custom validation protocol" is the entire finding set.

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| *(none — this page defines no AWS API)* | — | — | — | — | Client-side validation recipe only | — | — | The only network action is a **GET of the public root-cert ZIP** over HTTPS (benign AWS public endpoint). All validation is local to the customer's service. |

Interface surface that matters is the **document schema** (CDDL above) and the **validation steps** — treat every CDDL
field as attacker-controlled input and every step as a check that can be omitted/misimplemented.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Any NitroTPM instance (incl. attacker's own) | The external service's trust decision | Presenting a genuinely-Nitro-signed document | **A validator built from the 4 steps grants trust to a document from an instance the service does not intend to admit (wrong PCRs / wrong account) — proves PKI-authenticated ≠ trustworthy.** |
| Holder of a captured old document | The external service | Re-presenting a stale document | **The same document is accepted again later with no freshness/nonce/TTL rejection = replay.** |
| Crafter of a malformed COSE_Sign1 | The signature check | Manipulated protected header / `alg` / signed bytes | **A document whose `alg` ≠ ES384 or whose `Sig_structure` was not recomputed over protected+payload still "validates".** |
| Supplier of a self-signed chain inside `cabundle` | The chain validator | Attacker root/intermediate in the document's own bundle | **Path validates to an attacker-supplied anchor instead of the published, fingerprint-pinned Nitro root.** |
| Holder of a revoked Nitro cert | The chain validator | `setRevocationEnabled(false)` | **A chain containing a revoked cert still validates (no CRL/OCSP).** |
| Supplier of a hostile CBOR blob | The parser | Oversized / deeply-nested / unbounded `cabundle` | **The external service crashes/hangs (self-DoS; cross-tenant DoS if the validator fleet is shared).** |
| Any customer surface | **AWS Nitro signing key / intermediate CAs** | — | **HARD STOP — touching the AWS signer is a service-plane breach; preserve evidence, disclose.** |

---

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE] The documented procedure authenticates the PKI but makes NO trust decision (PCR-value + freshness checks omitted)  — Lens W / U
**Background.** The page states the purpose of attestation verbatim: *"to prove that an instance is a trustworthy
entity, based on the code and configuration that it is running."* The code/configuration is captured in
`nitrotpm_pcrs`. Yet the **"overall validation process"** is exactly four steps: (1) decode CBOR → COSE_Sign1,
(2) extract the Attestation Document, (3) **verify the certificate's chain**, (4) **ensure the document is properly
signed.** Every subsection that follows (COSE/CBOR, Semantic validity, Certificate validity, Certificate chain
validity) elaborates **only steps 3–4**. The document's `nitrotpm_pcrs`, `timestamp`, and `nonce` are **never**
referenced by any validation step; the page relegates `public_key`/`user_data`/`nonce` to an OPTIONAL *"custom
validation protocol between an attesting instance and the external service."*

**Security Concern.** A relying-party validator implemented faithfully from these four steps verifies that the document
was **signed by the genuine AWS Nitro PKI** — i.e. that it came from *some* real Nitro instance — and then **grants
trust**, without ever **(a)** comparing `nitrotpm_pcrs` to a known-good measurement set (is this the *expected* boot
state?), **(b)** verifying a fresh `nonce` the service issued, or **(c)** enforcing a `timestamp` TTL. Because *any*
NitroTPM instance in *any* AWS account can mint a genuinely-signed document (generation needs **no IAM**, is guest-local,
and binds **boot state, not caller identity** — see `attestation-get-doc-*` A3), the attacker simply attests **their
own** instance and presents that document. The PKI signature is valid, the chain is valid → the recipe's validator
admits the attacker. This collapses the attestation guarantee from "trustworthy, measured instance" to "any real Nitro
instance," defeating the stated purpose. The PCR comparison — the one step that would bind *what is running* — is the
step the procedure omits and offloads to an optional, unspecified "custom protocol."

**[CONFIRMED cross-source, 2026-10-15 — the omission is AWS's DOCUMENTED cross-page DESIGN, which SHARPENS rather than
weakens the finding.]** Cross-doc review settled the key question "is the PCR/nonce/timestamp omission unique to this
page or standard/deferred?" → **standard/deferred, and that is precisely the defect's shape:**
- The Nitro Enclaves sibling `enclaves/latest/user/verify-root.html` ("Verifying the root of trust") is a **near-verbatim
  twin** — identical 4 steps, identical CRL note, identical root fingerprint — and **also** checks no PCRs / nonce /
  timestamp. So this is a *reused* AWS validation recipe, not a one-page slip.
- Where PCR comparison IS made mandatory is **one layer up, on different pages**: `nitrotpm-attestation.html` frames
  "compare the actual measurements … against the reference measurements" as a *distinct* step **after** validation;
  `kms/.../conditions-nitro-tpm.html` makes it a **hard gate only on the AWS-KMS path** via
  `kms:RecipientAttestation:NitroTPMPCR<id>` ("If the request does not include an attestation document, permission is
  denied"); and `attestation-attest.html` tells third-party integrators verbatim: *"If you are attesting to a
  third-party service, you must build your own custom mechanisms for receiving, parsing, and validating Attestation
  Documents."*
- **No AWS doc anywhere** (searched EC2 UG, Enclaves UG, KMS dev guide) states **nonce-freshness or timestamp-TTL** as a
  required step — they appear only as schema fields, never operationalized (so Area 8 replay is wholly un-mitigated in docs).
- **No AWS drop-in reference *verifier* exists** (confirmed: `aws-nitro-enclaves-cose` is COSE-Sign1 only — no cert
  chain/revocation/PCR; `nsm-api`/`sdk-c`/`nitrotpm-tools` generate or request, never verify; AWS KMS is the only
  AWS-run verifier and it is closed-source). **So for the third-party path this page's recipe IS the implementation
  spec** — there is no library whose safer defaults a reader inherits.

**Reframed defect (the net-new owned finding):** the page titles its 4 steps the **"overall validation process"** and
is the destination `attestation-attest.html` sends third parties to — yet the single step that converts "a genuine
Nitro box" into "a *trustworthy* box" (PCR comparison) and the only freshness mechanism (nonce) live on *other* pages or
are relegated to an unspecified "custom protocol." A reader who implements "the overall validation process" as written
builds a **fail-open** gate. This is an AWS doc-architecture defect (trust-granting step severed from the recipe a 3P is
told to implement), not merely "deferred."

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A validator built from the 4 documented steps accepts a document generated by an attacker-controlled
  NitroTPM instance whose PCRs differ from the relying party's expected values.
  → **Mechanism:** steps 3–4 check only chain + signature; `nitrotpm_pcrs` is in no step.
  → **Oracle:** feed the reference/customer validator two genuine documents — one from an "expected" instance, one from
  an attacker instance with different PCR4/7/12 — and observe both pass. Refuted if the implementer added the PCR check
  the page omitted (e.g. followed `nitrotpm-attestation.html` separately).
- **Claim:** The same validator accepts a replayed stale document (Area 8 develops freshness).
- **Claim [CONFIRMED by doc review]:** The "overall validation process" on this page does not include PCR comparison or
  freshness, and the trust-granting PCR step is documented only on separate pages / the KMS path → a 3P implementing
  this page literally is fail-open.

**Doc evidence:** `#validation-process` 4-step list; `#doc-def` nonce "proof of authenticity" relegated to optional
"custom validation protocol"; the stated purpose sentence; twins `enclaves/.../verify-root.html`,
`attestation-attest.html`, `nitrotpm-attestation.html`, `kms/.../conditions-nitro-tpm.html`. **Severity-if-true:**
**High** — the gate is the sole control over whatever the external service releases; it reduces to "is this any genuine
Nitro box." **Stop:** once you show PCR/freshness is absent from the required procedure; do not weaponise against a real
relying party you don't own.

---

### Area 2 — AWS instructs disabling revocation (`CRL must be disabled`) with no stated compensating bound — Lens Y / AA
**Background.** Under *Certificate chain validity* the page carries a hard **Note: "CRL must be disabled when doing the
validation,"** and the Java sample sets `validationParameters.setRevocationEnabled(false)`.

**Security Concern.** Revocation is the mechanism by which a *compromised or retired* intermediate/leaf certificate is
rejected after issuance. The recipe **mandates turning it off** and offers **no alternative** (no OCSP, no
short-lifetime assertion on the page, no "the Nitro certs rotate every N hours so expiry is the bound"). A validator
built from this page therefore trusts **any** cert that merely chains to the root and is within its validity window —
including one AWS has revoked. Whether this is acceptable depends entirely on an **unstated** fact: how short-lived the
Nitro intermediate/leaf certs are (if they live minutes, expiry is a de-facto revocation bound; if hours/days, the
window is real). The page's silence on *why* revocation is disabled is itself the defect — a reader cannot reason about
the residual risk. (The hub's A5 owns this fact at summary level; **this plan is the page that is its evidence source**
and develops the "no compensating control is documented" gap.)

**[CONFIRMED cross-source, 2026-10-15.]** (a) **No AWS doc explains *why* CRL must be disabled for the Nitro
Attestation PKI specifically** — the instruction appears only as the bare, unexplained Note on this page and its
`verify-root.html` twin. (b) The generic rationale for disabling revocation DOES exist in AWS Private CA docs
(`privateca/.../short-lived-certificates.html`: *"These short-lived certificates expire so quickly that they can be
deployed without a revocation mechanism"*), **but Nitro Enclaves / NitroTPM is NOT in the list of services that use AWS
Private CA's `SHORT_LIVED_CERTIFICATE` mode** (that list names only AppStream and WorkSpaces) — so the short-lived-cert
justification is *plausible but not documented as applying here.* (c) **Intermediate/leaf cert lifetime and rotation
cadence are undocumented** — only the root's 30-year lifetime is stated. Residual severity therefore genuinely cannot
be bounded from docs: if the per-document leaf lives minutes the window is small; if it lives days, a compromised leaf
is trusted for days with no revocation path. This is the owned doc-gap.

**High-level Test Scenarios:**
- **Claim:** A validator built from the recipe accepts a chain containing a cert AWS has revoked, because CRL/OCSP is
  off by instruction. → **Oracle:** documentation review confirms no revocation path exists; a live confirmation would
  require a revoked Nitro cert (not obtainable without AWS → **doc-gap, confirm the cert-lifetime bound first**).
- **Claim:** The page provides no stated certificate-lifetime / rotation bound that would compensate for disabled
  revocation. → **Oracle:** grep this page + sibling Nitro Enclaves PKI docs for a rotation/lifetime statement; absence
  = AWS-authored recipe gap.

**Doc evidence:** `#chain` Note + Java `setRevocationEnabled(false)`. **Severity-if-true:** **Medium–High** (depends on
intermediate/leaf lifetime — pending Area-2 cross-source confirmation). **Stop:** at establishing the documented absence
of a revocation/lifetime bound.

---

### Area 3 — COSE_Sign1 algorithm not pinned + signed-bytes construction unspecified — Lens W / FF-analog / Y
**Background.** The algorithm `{1: -35}` (ES384) appears **only as an inline comment** in the illustrative COSE_Sign1
structure (`/* This is equivalent with {algorithm: ECDS 384} */`). Step 4 says merely *"Ensure that the Attestation
Document is properly signed."* The page never states: the verifier **MUST** reject any protected-header `alg` other than
ES384, and **MUST** recompute the COSE_Sign1 `Sig_structure` (the `"Signature1"` context, protected headers, and
payload) and verify the ECDSA signature over *that* — not over the raw payload alone.

**Security Concern.** A hand-rolled verifier that trusts the **document's own declared `alg`**, or that verifies the
signature over the wrong byte structure, is open to algorithm-substitution and signature-structure confusion. For an
EC/ECDSA key the classic HS/RS "use the public key as an HMAC secret" confusion does not apply directly, but the
*omission* class does: accepting `alg: none`-style/empty protected headers, accepting a mismatched curve, or validating
over the bare payload instead of the canonical `Sig_structure` all let a crafted COSE_Sign1 pass. The terse 4-step
recipe does not inoculate the implementer against any of these — it describes "ensure signed" as a solved black box.

**High-level Test Scenarios:**
- **Claim:** A validator built from the recipe does not pin `alg = ES384` in the protected header and accepts a document
  advertising a different/no algorithm. → **Oracle:** craft COSE_Sign1 variants with altered protected-header `alg`;
  observe acceptance. Refuted if the implementer pinned ES384 (which the page did not tell them to).
- **Claim:** The recipe does not specify the `Sig_structure` to sign/verify over, inviting verify-wrong-bytes bugs.
  → **Oracle:** RFC 8152/9052 COSE_Sign1 requires signing over `["Signature1", protected, external_aad, payload]`; the
  page's 4 steps + array illustration never state this → documented omission.

**[CONFIRMED against RFC 8152/9052, 2026-10-15.]** (a) COSE_Sign1 verification MUST reconstruct the `Sig_structure`
`["Signature1", body_protected, external_aad, payload]`, encode it to `ToBeSigned`, and verify the signature over
*that* — **a verifier that checks `sig` against the raw `payload` alone is not implementing COSE_Sign1 at all** (§4.4).
The page's step 4 ("ensure properly signed") never states this → verify-wrong-bytes is an open implementer error.
(b) RFC §3.1: `alg` "MUST be authenticated where the ability to do so exists" — being in the signed `body_protected`
makes it *tamper-evident*, but **the verifier is still the party responsible for deciding whether the algorithm it
reads is one it will accept for that key** (the COSE analogue of JWS `alg:none` confusion). The page pins nothing.
(c) **The one AWS COSE library a 3P might reach for, `aws-nitro-enclaves-cose`, is NOT a hard ES384 pin** — it derives
the expected algorithm from the supplied key's EC curve (SECP384R1→ES384, P-256→ES256, P-521→ES512) and accepts any of
them; so a validator that feeds it a non-P-384 key, or trusts the document's declared curve, widens the accepted
algorithm set beyond ES384. (d) §2/§4.2: a bare CBOR array of the right shape is **not self-describing** as COSE_Sign1
vs. a single layer of COSE_Sign/COSE_Mac — the page says the document "can be encoded as either tagged or untagged" tag
18, so a lenient verifier that accepts untagged arrays without the application protocol fixing the type invites
message-type confusion.

**Doc evidence:** `#COSE-CBOR` `{1:-35}` as a comment only; `#validation-process` step 4 unspecified; tagged-vs-untagged
note ("encoded as either tagged or untagged … tag 18"). RFC 8152 §2/§3.1/§4.2/§4.4. **Severity-if-true:**
**High** (signature-trust bypass). **Stop:** at establishing the recipe does not mandate alg-pin / Sig_structure.

---

### Area 4 — CBOR/COSE parser memory-safety & resource bounds on an attacker-supplied blob — Lens F / L
**Background.** The validator's input is a *"binary blob"* fully controlled by the presenter. The CDDL exposes several
attacker-sized/shaped elements: `cabundle: [* cert]` (**unbounded array**), `nitrotpm_pcrs: {+ index => pcr}`
(unbounded map, `index 0..31`), `cert .size (1..1024)`, `user_data .size (0..1024)`, `pcr .size (32/48/64)`.

**Security Concern.** A validator — especially one using a C/C++ CBOR/COSE library — that trusts attacker-declared CBOR
lengths/nesting-depth, or iterates an **unbounded `cabundle`** before enforcing a cap, is exposed to OOB reads, UAF,
unbounded allocation, and parser hangs. A giant `cabundle` also forces quadratic/expensive certificate-path building
(Area 5) before any size check. The page states the CDDL size caps but **never tells the implementer to enforce them
before parsing**, nor to bound `cabundle` length or recursion depth.

**High-level Test Scenarios:**
- **Claim:** A validator built from the recipe hangs or exhausts memory on a `cabundle` array of thousands of entries or
  a deeply-nested/oversized CBOR structure. → **Oracle:** feed a malformed/oversized/deeply-nested CBOR document to a
  reference/customer validator; observe crash, hang, or OOM. 
- **Claim:** Size caps (`cert ≤1024`, `pcr ∈ {32,48,64}`) are not enforced pre-parse by a naive implementer. → **Oracle:**
  present over-cap fields; a correct validator rejects, a naive one dereferences the declared length first.

**Doc evidence:** `#doc-spec` CDDL (`cabundle: [* cert]`, size caps). **Severity-if-true:** **Medium** (self-DoS of the
external service); **High** if that service is a **shared/multi-customer** fleet (cross-tenant DoS). **Stop:** at a single
crash/hang signal; do not iterate payloads against infrastructure you don't own.

---

### Area 5 — Certificate-chain / trust-anchor construction footguns baked into the recipe — Lens U / Y
**Background.** The page hands the validator the document's **own** `cabundle` (ordered `[ROOT, INTERM_1, …, INTERM_N]`),
tells it to **reverse** it to `[TARGET_CERT, INTERM_N, …, INTERM_1, ROOT_CERT]`, and then validate with the Java
`PKIXParameters(trustAnchors)` where `trustAnchors` is seeded with `rootCertificate`.

**Security Concern.** The entire security of the chain hinges on the trust anchor being the **pinned, fingerprint-verified
published root** — NOT whatever root the attacker placed at `cabundle[0]`. The recipe's own sample does the right thing
(anchors on `rootCertificate`), **but the page never explicitly warns:** "the document's `cabundle` is attacker-supplied;
you MUST pin the anchor to the published root fingerprint and MUST NOT trust `cabundle[0]` as the anchor." A reader who
builds `trustAnchors` from `cabundle[0]` (the natural reading of "start from the Attestation Document CA bundle and
generate the required chain") validates an attacker-supplied self-signed chain **against itself** → total bypass. Adjacent
PKIX footguns the terse page does not caution against: not enforcing `basicConstraints cA:TRUE` / `pathLenConstraint`,
accepting an intermediate as an anchor, not checking that the terminal root equals the pinned fingerprint, name-constraint
omission.

**High-level Test Scenarios:**
- **Claim:** A validator that seeds its trust anchor from the document's `cabundle` (rather than the pinned published
  root) accepts a fully attacker-generated chain. → **Oracle:** present a document whose `cabundle` contains an
  attacker self-signed root + intermediates and whose leaf signs the COSE; a mis-anchored validator passes it, a
  correctly-pinned one rejects (root fingerprint ≠ published).
- **Claim:** The page does not instruct enforcing `basicConstraints`/pathLen on intermediates. → **Oracle:** doc review;
  present a chain using a non-CA cert as an issuer and observe a naive validator accept.

**[CONFIRMED on Java-PKIX semantics, 2026-10-15 — which NARROWS where the real risk sits.]** The sample as written is
actually *safe*: `CertPathValidator.getInstance("PKIX")` + `CertificateFactory.generateCertPath(List)` **does
automatically enforce** `basicConstraints cA:TRUE`, `pathLenConstraint`, `nameConstraints`, and `keyUsage.keyCertSign`
(RFC 5280 §6.1.4). The real footguns are therefore (i) **trust-anchor mis-selection** — `PKIXParameters(Set<TrustAnchor>)`
takes the anchor *out-of-band* and the PKIX algorithm **cannot verify "is this the root I meant"**; a reader hand-reversing
`[ROOT, INTERM_1..N]` can easily seed the anchor with the wrong array element (an intermediate, or an attacker-supplied
`cabundle[0]`) → validation silently succeeds against a shorter/attacker chain; and (ii) **abandoning `CertPathValidator`
for a manual `cert.verify(issuerPublicKey)` loop** (a plausible reaction to the confusing reversal instructions) — that
checks only the cryptographic signature chain and **silently skips** basicConstraints/pathLen/nameConstraints/keyUsage,
re-opening every constraint the PKIX path would have enforced. (iii) Off-by-one on the reversal with N=1 (drop/duplicate
an intermediate) or including ROOT in *both* the CertPath and TrustAnchors (non-standard) are additional
mis-implementation shapes. So the live test should target **anchor provenance** (does the validator pin the anchor to
the published fingerprint, or trust the bundle?) and **whether a manual verify-loop was used**.

**Doc evidence:** `#semantic-validation` (reverse the bundle), `#chain` Java snippet (`trustAnchors.add(rootCertificate)`),
`#validation-process` ("start from the Attestation Document CA bundle"); Java PKIX javadoc + RFC 5280 §6.1.4.
**Severity-if-true:** **High** (full chain bypass if mis-anchored or if a manual verify-loop replaces PKIX). **Stop:** at
demonstrating the mis-anchor / manual-loop path on a validator you built; never target a real root.

---

### Area 6 — Root-cert acquisition: pin-by-fingerprint vs fetch-and-trust (MITM/TOFU) — Lens Y / EE-analog
**Background.** The published root is distributed as a **ZIP over HTTPS** from
`https://aws-nitro-enclaves.amazonaws.com/AWS_NitroEnclaves_Root-G1.zip` and the page supplies a SHA-256 fingerprint to
verify it against.

**Security Concern.** Faithfully done (download once, **verify the fingerprint**, pin the DER) this is sound. The defect
risk is in the recipe's *framing*: it presents the download URL first and the fingerprint as a follow-on ("it can be
verified using the following fingerprint") rather than as a mandatory precondition. An implementer who **fetches the ZIP
at runtime and skips/forgets the fingerprint check**, or who trusts the TLS endpoint alone, is open to substitution/MITM
of the root of trust. The page gives no guidance on caching, rotation, or re-pinning of the root.

**High-level Test Scenarios:**
- **Claim:** A validator that fetches the root ZIP without verifying the published SHA-256 fingerprint will trust a
  substituted root. → **Oracle:** code review of the customer validator; or a controlled MITM of the fetch against a
  validator you own that omits the fingerprint check.
- **Claim:** The page does not mandate fingerprint verification as a precondition of trust. → **Oracle:** doc review
  (fingerprint presented as optional-sounding "can be verified").

**Doc evidence:** `#validation-process` root download URL + fingerprint block + 30-yr PCA statement. **Severity-if-true:**
**Low–Medium** (the fingerprint IS provided; the gap is emphasis/ordering). **Lens-G note:** a *server-side fetch* of this
URL by the external service is **benign** (AWS's own public endpoint, not an attacker-chosen target) → **SSRF N/A here**.

---

### Area 7 — PCR index range `0..31` in the document vs the NitroTPM `PCR0..23` register set (which indices to pin?) — Lens U / W
**Background.** The CDDL permits `index = 0..31` and `nitrotpm_pcrs` is an **open** map (`{+ index => pcr}`). The NitroTPM
KMS condition-key family is `NitroTPMPCR0..NitroTPMPCR23` (24 registers), and only PCR4/7/12 are the documented
meaningful triad (owned by `nitrotpm-attestation-document-content-*`, which also records a **cross-source PCR-semantics
contradiction** between the User Guide and `list_kms`).

**Security Concern.** This page gives the third-party validator **no list of which indices to compare, which must be
present, or how to treat unknown/extra indices.** Combined with Area 1 (PCR comparison omitted entirely), an implementer
who *does* add a PCR check has no AWS guidance on binding scope → under-binds (pins too few registers; cf. the hub's A2
all-zeros-PCR12 under-binding) or ignores registers 24–31 / an unexpected index an attacker populated. The register-range
mismatch (doc allows 0..31; NitroTPM defines 0..23) is itself an AWS doc inconsistency a validator author must resolve
blind.

**High-level Test Scenarios:**
- **Claim:** The validation guidance does not specify which PCR indices a third-party validator must pin or require.
  → **Oracle:** doc review across this page + content page + KMS condition-key family; absence = recipe gap feeding Area 1.
- **Claim:** A validator pinning only a subset (e.g. PCR4) admits an instance differing in unpinned registers.
  → **Oracle:** present documents differing only in unpinned indices; both pass. (Exploit itself owned by the hub A1 /
  content-page A1; here it is the *coverage-selection* gap.)

**Doc evidence:** `#doc-spec` `index = 0..31`; cross-ref `nitrotpm-attestation-document-content-attack-research-plan.md`
A1; hub A2. **Severity-if-true:** **Low–Medium** (doc-gap that amplifies Area 1). **Stop:** at documenting the
range/coverage gap.

---

### Area 8 — Optional, uncomputed `nonce`/`timestamp`/`public_key` → replay & response-binding confusion — Lens M / AA / U
**Background.** The document carries `timestamp` (uint ms, "UTC time when document was created") and three OPTIONAL fields
`public_key` ("an optional DER-encoded key the attestation consumer can use to encrypt data with"), `user_data`, and
`nonce` ("an optional cryptographic nonce provided by the attestation consumer **as a proof of authenticity**"). The
validation steps **never** reference any of them; the page frames them as a "custom validation protocol."

**Security Concern.** `nonce` is the *only* freshness/liveness mechanism and it is **optional and uncomputed by the
documented procedure**. A third-party validator that follows the 4 steps and does not implement a challenge-response
nonce (and/or a `timestamp` TTL) is **replayable**: any captured genuine document works indefinitely. `public_key` binds
the **response** the consumer encrypts, **not** the request/caller identity — a recipient-selection field, not an
authenticator (cross-ref `attestation-get-doc-*` A1; on the AWS-KMS path the hub A4 records nonce is "not used for
attestation with AWS KMS," so freshness is *entirely* a third-party-protocol responsibility, i.e. exactly this page's
readers). The page's "proof of authenticity" wording **overstates** what an optional, unverified nonce provides.

**High-level Test Scenarios:**
- **Claim:** A validator built from the 4 steps accepts a replayed stale document (no nonce/TTL enforcement).
  → **Oracle:** present the same captured document twice to a reference/customer validator; both accepted = replayable.
- **Claim:** `public_key` does not authenticate the presenter (binds only the response). → **Oracle:** doc semantics +
  cross-ref; a validator that treats `public_key` presence as caller identity is confused.
- **Claim:** The page provides no `timestamp` freshness window. → **Oracle:** doc review (`timestamp` in no validation step).

**Doc evidence:** `#doc-def` optional fields + "proof of authenticity"; `#doc-spec` `timestamp`. Cross-ref hub A4,
`attestation-get-doc-*` A1. **[CONFIRMED 2026-10-15]** no AWS doc (EC2 UG, Enclaves UG, KMS dev guide) operationalizes
`nonce` or `timestamp` into a *required* check — both appear only as schema fields → the replay gap is wholly
un-mitigated in documentation. **Severity-if-true:** **Medium–High** (replay against the gate). **Stop:** at
demonstrating replay on a validator you own.

---

### Area 9 — One shared Nitro root serves BOTH NitroTPM and Nitro Enclaves → cross-product document confusion — Lens U / A-analog
**Background.** [CONFIRMED cross-source, 2026-10-15.] This page (NitroTPM) and the Nitro Enclaves `verify-root.html`
cite the **identical** root download URL, SHA-256 fingerprint, PCA subject (`CN=aws.nitro-enclaves`), and 30-year
lifetime — i.e. **one shared PKI root (`AWS_NitroEnclaves_Root-G1`) underpins both products' attestation.** The two
document formats differ (NitroTPM carries `nitrotpm_pcrs` with `index 0..31`; Nitro Enclaves carries a `pcrs` map with
different register semantics + an `ImageSha384`/module measurement), but **both chain to the same root and both are
COSE_Sign1/ES384.**

**Security Concern.** A third-party validator that implements only this page's 4 steps authenticates "a document that
chains to `AWS_NitroEnclaves_Root-G1` and is properly signed" — which is satisfied **equally by a NitroTPM instance
document and by a Nitro *Enclave* attestation document**. The recipe gives no instruction to assert *which product*
produced the document (e.g. require the `nitrotpm_pcrs` key / reject `module_id`-less or enclave-shaped payloads). A
relying party that intends to admit only genuine NitroTPM *instances* could be handed an **Enclave** document (or vice
versa) that still passes chain+signature; combined with Area 1 (no PCR comparison), the validator cannot even tell it is
looking at the wrong *kind* of attestation. This is a doc-level under-specification of the document's product/type
binding.

**High-level Test Scenarios:**
- **Claim:** A validator built from this page accepts a Nitro Enclaves attestation document (different product, same
  root) when it intended to accept only NitroTPM instance documents. → **Oracle:** present an Enclave-shaped COSE_Sign1
  that chains to the shared root; a recipe-literal validator passes it on chain+signature. Refuted if the implementer
  added a product/field discriminator the page never specified.
- **Claim:** The page never tells the validator to assert document *type*/product before trusting. → **Oracle:** doc
  review (no "ensure this is a NitroTPM document" step).

**Doc evidence:** shared root URL/fingerprint/subject across `nitrotpm-attestation-document-validate.html` +
`enclaves/.../verify-root.html`; distinct CDDL field sets. Cross-ref `nitrotpm-attestation-document-content-*` (PCR
semantics differ by family). **Severity-if-true:** **Low–Medium** (type-confusion that amplifies Area 1; High only if a
service's trust decision hinges on product kind). **Stop:** at documenting the missing type-discriminator step.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attacker's own genuine Nitro instance admitted (no PCR check) | 4-step procedure | "verify chain + ensure signed" presented as *the* validation; PCR check offloaded to optional "custom protocol" (Area 1) |
| Replay of a captured document | Procedure / optional nonce | `nonce` "proof of authenticity" is **optional**; no `timestamp` TTL (Area 8) |
| Algorithm substitution / wrong signed-bytes | COSE_Sign1 verify | `alg {1:-35}` shown only as a comment; step 4 "ensure properly signed" unspecified (Area 3) |
| Attacker-supplied root in `cabundle` trusted as anchor | Chain validation | Sample anchors on `rootCertificate` but page never warns against trusting `cabundle[0]`; fingerprint-pin not mandated as precondition (Areas 5, 6) |
| Revoked cert accepted | Chain validation | `setRevocationEnabled(false)` / "CRL must be disabled" with no compensating lifetime bound (Area 2) |
| Parser crash/hang/OOM | CBOR/COSE parser | CDDL size caps stated but enforcement + `cabundle` length/depth bounds not mandated (Area 4) |
| Under-binding of PCR coverage | PCR comparison (if implemented) | No index list / `0..31`-vs-`0..23` range mismatch unresolved (Area 7) |
| Enclave document accepted where NitroTPM expected (cross-product) | Chain validation | One shared root serves both products; no document-type/product discriminator step (Area 9) |

---

## 7. Out-of-Scope Risk Categories
- **The AWS Nitro Attestation PKI signing key, intermediate CAs, and the Nitro hypervisor's signing behavior** — HARD
  STOP; never forge/extract/MITM the signer. Testing *detects* recipe weaknesses, it does not attack AWS's root of trust.
- **The AWS-KMS attestation-gate path** (`kms:RecipientAttestation:NitroTPMPCR*`, the Allow-vs-mandatory-Deny gate, the
  all-zeros-PCR12 example, key-family confusion) — owned by the hub `nitrotpm-attestation-*` + `prepare-attestation-service-*`.
- **The attestation-document *generation* / `nitro-tpm-attest` request-side fields** — owned by `attestation-get-doc-*`.
- **PCR *semantics* / reproducible-measurement bypass / the UG-vs-list_kms contradiction** — owned by
  `nitrotpm-attestation-document-content-*` and the hub A1.
- **A customer validator's own bugs that do not stem from the recipe** — out of scope as *AWS* findings (the customer
  owns their code). In-scope framing is strictly: *the AWS-authored recipe omits/misframes a check a faithful
  implementation needs.*
- **Single-tenant self-DoS** of a customer's own validator (Area 4 is only elevated if the validator fleet is shared).

---

## 8. Null hypotheses / doc gaps
- **Lens A (cross-tenant IDOR):** N/A — this page defines no AWS resource-by-ID, no tenant/account identifier, no shared
  AWS fleet; it is a client-side recipe. (Pages checked: this page in full.)
- **Lens B/C (PassRole / credential vending):** N/A — no role ARN, no STS, no session policy on this page.
- **Lens D/V (data→control / network segmentation):** N/A — no ENI/VPC/network interface described.
- **Lens E (RBAC privesc):** N/A — no IAM roles/identities on this page.
- **Lens G (SSRF):** N/A — the only server-side fetch is the **AWS public root-cert ZIP** at a fixed AWS endpoint, not
  an attacker-chosen target (noted in Area 6). No field the external service dereferences to an attacker URL.
- **Lens H (KMS/encryption-context):** deferred — the KMS path is explicitly out of scope of this (third-party) page;
  owned by hub + `prepare-attestation-service-*`.
- **Lens I (tagging/ABAC), J (OAuth), K (prompt injection), N (namespace migration), O (audit — customer-owned logging),
  P (registration/proofing), Q (file upload — the "upload" here is the attestation blob, covered under Lens F/Area 4),
  R/S (no IAM policy JSON on *this* page — the KMS key-policy artifact is on `prepare-attestation-service.html`),
  T (secret storage), BB/CC/DD (multi-parser edge/cache/upstream-context — no such AWS component here),
  FF (JWT/OIDC — the token here is a COSE_Sign1 object; the alg-substitution analog is captured in Area 3):** N/A for
  this page's surface (each checked against the full page content).
- **Doc gaps — RESOLVED by cross-source subagents 2026-10-15 (results folded into the Areas above):**
  1. **PCR/nonce/timestamp a REQUIRED step for the 3P path? → NO, by documented design.** The 4-step recipe is reused
     verbatim on `enclaves/.../verify-root.html`; PCR comparison is mandatory only one layer up (`nitrotpm-attestation.html`
     "distinct step"; KMS condition keys on the KMS path); `attestation-attest.html` tells 3P integrators to "build your
     own custom mechanisms." No doc operationalizes nonce/timestamp into a required check. → Area 1 reframed as a
     doc-architecture fail-open (trust-granting step severed from the recipe); Area 8 replay is un-mitigated in docs.
  2. **Intermediate/leaf cert lifetime? → UNDOCUMENTED.** Only the root's 30-yr lifetime is stated; Nitro is NOT in AWS
     Private CA's `SHORT_LIVED_CERTIFICATE` service list, so the "short-lived ⇒ revocation unnecessary" rationale is
     plausible but not documented as applying. → Area 2 residual severity genuinely unbounded from docs.
  3. **AWS reference verifier? → DOES NOT EXIST (drop-in).** `aws-nitro-enclaves-cose` = COSE-Sign1 only (no chain/
     revocation/PCR) and is NOT a hard ES384 pin (key-curve-derived, multi-alg); `nsm-api`/`sdk-c`/`nitrotpm-tools`
     generate/request only; AWS KMS is the only AWS verifier and it is closed-source. → the recipe IS the 3P
     implementation spec (folded into Areas 1 & 3).
  4. **`index 0..31` (document) vs `NitroTPMPCR0..23` (KMS family)? → genuine range mismatch, unreconciled by AWS docs**
     → Area 7 (owned here as the coverage-selection gap).
  - NEW surfaced during resolution: **one shared root serves both NitroTPM and Nitro Enclaves** → cross-product
    document confusion, now Area 9.

> See `project-aws-research-plans` memory note for the plan convention and `reference-aws-iam-service-auth-ref-url`.
> Cross-references: `nitrotpm-attestation-attack-research-plan.md` (hub),
> `nitrotpm-attestation-document-content-attack-research-plan.md`, `attestation-get-doc-attack-research-plan.md`,
> `prepare-attestation-service-attack-research-plan.md`.
