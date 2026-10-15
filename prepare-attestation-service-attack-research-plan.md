# Prepare AWS KMS for attestation — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/prepare-attestation-service.md` (target page: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/prepare-attestation-service.html), linked KMS developer-guide page `conditions-nitro-tpm.html`, and the IAM Service Authorization Reference `/work/aws-docs/docs/service-authorization/latest/reference/list_kms.md`. Online `.md` twin of the target was fetched and compared to the offline mirror: **byte-identical, no drift** (2026-10-15), including the KMS key-policy JSON example and the three condition-key names. Status: documentation-derived hypotheses only; nothing tested against a live account.

> **PAGE-LEVEL DEEP-DIVE CHILD of `nitrotpm-attestation-attack-research-plan.md`.** The sibling plan already lists `prepare-attestation-service.md` among its sources and already develops the ways the *PCR condition can be satisfied by an attacker* who never ran the trusted workload: reproducible public-recipe measurements under a broad `Principal` (sibling Area 1), the under-binding / all-zeros-PCR12 footgun shipped in this very page's example (sibling Area 2), the `PCR*`-vs-`NitroTPMPCR*` key-family confusion (sibling Area 3), and attestation-document replay / no-nonce / no-TTL (sibling Area 4), plus the COSE/CBOR/CRL/algorithm 3P-verifier surface reached by this page's top Note (sibling Areas 5–6). **This plan does NOT restate those** — it cross-references them. This plan OWNS the one surface the sibling treats only at summary level: **the structure of the KMS key-policy artifact this page ships, and specifically whether the attestation gate it demonstrates is even *mandatory*** — i.e. the Lens W fail-open / Lens U doc-vs-enforcement / Lens R-S shipped-artifact-defect layer of the policy document itself, as opposed to the Lens A/W PCR-defeat layer the sibling owns.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The safe first oracle for every lead here is **documentation + `iam:SimulateCustomPolicy` / `aws kms` dry authoring** — no customer data is ever decrypted to settle a question. The attestation gate's *mandatoriness* (Area 1) is confirmed by a single live `Decrypt` from a principal presenting **no** attestation document; use synthetic canary ciphertext only.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own Nitro/KMS service plane (e.g. the Nitro Hypervisor COSE signing identity, a KMS fleet credential), stop, preserve evidence, flag for AWS-Security disclosure. Everything below is customer-side policy construction; nothing here should require touching the service plane.

---

## 1. Pentest Objectives
Stated as concrete breach outcomes a hunter proves or refutes:
1. **Attestation-not-mandatory:** demonstrate that a KMS key configured exactly as this page shows still permits `Decrypt`/`GenerateDataKey` from a principal that presents **no attestation document at all**, because the attestation condition is additive to (not restrictive of) the key's other authorization paths (default IAM-delegation statement). → the whole feature's security property is void with no deviation from the doc's happy path.
2. **Copy-verbatim artifact defect:** demonstrate that a customer who copies the page's example as-is inherits (a) an under-binding PCR12 (all-zeros) [defer to sibling Area 2], and/or (b) a non-functional policy from un-stripped `{{…}}` placeholders, and/or (c) a gate covering only 3 of the 5 attestation-capable KMS actions.
3. **Defense-in-depth omissions:** show the example omits `kms:ViaService` / `kms:EncryptionContext` / `kms:CallerAccount` scoping that would bound the gated statement to the EC2 integration and the caller's own account.

---

## 2. Components, Assets, and Design

**What this page is.** `prepare-attestation-service.html` ("Prepare AWS KMS for attestation") is the step in the NitroTPM-attestation workflow that tells a customer how to turn their reference PCR measurements into an **AWS KMS key policy** so that "only requests from instances launched using the Attestable AMI can perform cryptographic operations using the AWS KMS key." Its single deliverable is a **copy-verbatim KMS key-policy JSON artifact** (Lens R/S/U/W primary surface). It is not an API page; the API it configures is the KMS crypto-operation family invoked with a `Recipient` attestation document.

**The shipped artifact (verbatim from the page).** A key policy with **one statement**:
- `"Effect":"Allow"`, `"Sid":"Allow requests from instances with attested AMI only"`
- `"Principal":{"AWS":"{{arn:aws:iam::111122223333:role/MyEC2InstanceRole}}"}` — a single EC2 instance-profile role, wrapped in `{{…}}` doc-placeholder braces.
- `"Action":["kms:Decrypt","kms:GenerateDataKey","kms:GenerateRandom"]` — **3 actions.**
- `"Resource":"*"` — in a *key* policy this means "this key" (standard; benign).
- `"Condition":{"StringEqualsIgnoreCase":{ "kms:RecipientAttestation:NitroTPMPCR4":"{{EXAMPLE…EXAMPLE}}" (96-hex SHA-384), "kms:RecipientAttestation:NitroTPMPCR12":"{{0×96}}" }}` — PCR4 pinned to a real digest, **PCR12 pinned to 96 hex zeros.**

**Confirmed IAM-reference facts** (`list_kms.md`, read offline by targeted grep):
- The condition keys exist as two **numerically-overlapping families**: NitroTPM `kms:RecipientAttestation:NitroTPMPCR0…NitroTPMPCR23` (24 keys) + `…ImageSha384`; Nitro **Enclaves** `kms:RecipientAttestation:PCR0…PCR31` + `…ImageSha384`. (Family-confusion → sibling Area 3.)
- Exactly **five** actions carry the `RecipientAttestation:*` keys: `Decrypt` (l.393), `DeriveSharedSecret` (l.417), `GenerateDataKey` (l.471), `GenerateDataKeyPair` (l.477), `GenerateRandom` (l.501). The example gates **three** (Decrypt, GenerateDataKey, GenerateRandom) → omits DeriveSharedSecret + GenerateDataKeyPair.
- `Decrypt`/`DeriveSharedSecret`/`GenerateDataKey`/`GenerateDataKeyPair` rows also carry `kms:ViaService`, `kms:EncryptionContext:*`, `kms:EncryptionContextKeys`, `kms:CallerAccount`. **The `GenerateRandom` row (l.501) carries ONLY the `RecipientAttestation:*` keys** — no `ViaService`/`EncryptionContext`/`CallerAccount` — so GenerateRandom cannot be layered with those defenses even if the author wanted to.
- `kms:RecipientAttestation:NitroTPMPCR4` is documented (l.759) as "a contiguous measure of boot loader and additional drivers … loaded by the boot loader" (type **String**). PCR value length = **96 hex = SHA-384** (matches the 96-zero PCR12 in the example).

**Trust-root note.** The attestation document is COSE_Sign1-signed by the AWS Nitro Hypervisor (service plane root of trust) and is *caller-supplied* as the `Recipient` parameter on the KMS call. KMS is the built-in verifier of the PCR condition; on success it re-encrypts the response under the document's embedded RSA public key (`CiphertextForRecipient`). (Response-binding / RSA-only / replay → sibling Area 4.)

```
reference PCRs (from Attestable AMI build)  --author-->  [KMS key policy]
                                                             |  statement: Allow role R if NitroTPMPCR4/12 match
EC2 instance (role R, attested) --Decrypt(Recipient=attn doc)--> [KMS]
                                                             |  evaluates key policy
   ALSO present on almost every real CMK:  "Enable IAM policies" root statement (Allow root kms:* )
                                                             |  <-- this delegates to IAM, UN-conditioned by attestation  (Area 1)
any IAM principal with kms:Decrypt (NO attestation) --Decrypt--> [KMS]  --> plaintext ?  (fail-open test)
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `kms:Decrypt` / `GenerateDataKey` / `GenerateRandom` (+ `Recipient`) | API | Existing API, attestation-conditioned path | Crypto op / read of plaintext | External | The gated operations the page's policy protects | Yes | Per key policy `Principal` + `RecipientAttestation` conditions **AND any other allowing statement** | **Primary target — §5 Area 1 (is the gate mandatory?).** |
| `kms:DeriveSharedSecret` / `GenerateDataKeyPair` (+ `Recipient`) | API | Existing | Crypto op | External | Also attestation-capable but **omitted** from the example's `Action` list | Yes | Per key policy | §5 Area 3 completeness gap. |
| `kms:PutKeyPolicy` on the attestation-gated key | API | Existing | Mutating (authors the gate) | External | Writes the policy this page describes | Yes | Per IAM / key policy | Schema-validation of PCR index/value is an open doc-gap → sibling Area 2 / §5 Area 5. |
| EC2 NitroTPM attestation (`nitro-tpm-attest` → attestation document) | guest tool | New feature | n/a | guest | Produces the `Recipient` doc | n/a | Instance owner | Mechanism owned by sibling plan. |

Doc-flagged least-reviewed items (treat as new surface): the `kms:RecipientAttestation:NitroTPM*` condition-key family and the entire attestation-conditioned KMS authorization path.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Any IAM principal in the key-owner account **with `kms:Decrypt` in its identity policy, presenting NO attestation** | The attestation-"gated" CMK | The default `Enable IAM policies` root statement that co-exists with the page's Allow statement | **`Decrypt` returns plaintext without any attestation document** → the attestation gate was never mandatory (Area 1, headline). Fail-closed = `AccessDenied`. |
| Customer copying the example verbatim | Their own key policy | `{{…}}` placeholders, all-zeros PCR12, 3-of-5 action coverage | Policy is inert / under-binding / incomplete relative to the "only attested instances" promise (Areas 2–3, + sibling Area 2). |
| Attested instance role R | CMK via a non-EC2 service integration | No `kms:ViaService` on the gated statement | Gated statement usable outside the intended EC2 path (Area 4, defense-in-depth). |
| Any AWS customer who rebuilds the public Attestable-AMI recipe | Victim CMK whose `Principal` is broad | Matching PCR4/7/12 + presenting own attestation doc | → **sibling Area 1** (cross-account PCR-match defeat). |

---

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE] The demonstrated gate is *additive*, not *mandatory*: attestation can be bypassed through the key's other authorization paths (Lens W fail-open + Lens U doc-vs-enforcement + Lens R/S shipped-artifact)
**Background.** The page's prose says the key policy "allows key access **only if** API requests include an Attestation Document with measurements that match the reference measurements … This ensures that only requests from instances launched using the Attestable AMI can perform cryptographic operations using the AWS KMS key." The artifact it shows to achieve this is a **single `Allow` statement** carrying the `RecipientAttestation` condition.

**Security Concern.** KMS authorizes a crypto operation if **any** applicable statement in the key policy (or an IAM policy, when the key policy delegates to the account root) allows it and no `Deny` applies. A real customer-managed key almost always *also* contains the default statement that `CreateKey`/the console add — `{"Sid":"Enable IAM policies","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::<acct>:root"},"Action":"kms:*","Resource":"*"}` — which delegates authorization to IAM. **With that statement present, any principal in the account holding `kms:Decrypt`/`kms:GenerateDataKey` in its *identity* policy can perform the operation with NO attestation document at all**, because its access is granted by the delegation statement, not by the attestation statement. The attestation condition therefore grants an *extra* path for role R when attested; it does **not** prevent non-attested access. To make attestation genuinely mandatory the policy must carry an explicit **`Deny`** of the sensitive actions when the attestation condition is not satisfied (a `StringNotEquals`/`Null`-guarded Deny) — **the page never shows this form and never warns that the Allow-only form is insufficient.** The doc's "only if … ensures that only …" prose thus overstates what the shown artifact enforces. This is an AWS-authored, copy-verbatim guidance defect (not a customer footgun): a customer following the documented happy path believes they have an attestation lock that is in fact bypassable by ordinary IAM.

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** On a CMK whose policy is (default root `Enable IAM policies` statement) + (this page's attestation `Allow` statement), a principal with an identity policy granting `kms:Decrypt` on the key but presenting **no** `Recipient`/attestation document can still `Decrypt`. → **Mechanism:** KMS "any allow wins" evaluation + IAM delegation. → **Confirm/Refute oracle:** the `Decrypt` of synthetic canary ciphertext **succeeds** (gate not mandatory) vs `AccessDenied` (mandatory). → **Preconditions:** key has the standard default statement (overwhelmingly common); caller has `kms:Decrypt`. → **Cost:** one key, one canary blob. → **Severity-if-true:** **High** — the feature's sole security property is silently void with zero deviation from the documented procedure; AWS-authored → `aws-security` Tier-2 (doc/sample defect).
- **Claim:** Even without the default statement, if a *second* custom statement grants any principal a sensitive action unconditioned, the attestation statement does not constrain it. → **Oracle:** add such a statement, repeat the no-attestation `Decrypt`.
- **Claim:** The correct restrictive form (an explicit `Deny` when `kms:RecipientAttestation:NitroTPMPCR4` is absent/mismatched) is **not derivable from this page** and, when a customer attempts it, is prone to the `Null`/`ForAllValues` vacuous-truth trap (→ Area 5 / Lens S). → **Oracle:** survey whether any linked AWS page shows the Deny form; absence corroborates the guidance gap.

**Doc evidence.** `prepare-attestation-service.md` ll.13–15 ("only if … This ensures that only …") and the single-statement example ll.19–44; KMS policy-evaluation model (key policy + IAM delegation; "least-privilege via explicit deny for mandatory conditions"). **Severity-if-true:** High.

---

### Area 2 — Copy-verbatim artifact hygiene: `{{…}}` placeholders + all-zeros PCR12 + Resource:"*" (Lens R / U)
**Background.** The example's `Principal` and both PCR values are wrapped in **double-curly-brace** doc placeholders (`{{arn:…}}`, `{{EXAMPLE…EXAMPLE}}`, `{{0×96}}`). IAM/KMS policy variables use `${…}`, not `{{…}}`; `{{…}}` is literal text.

**Security Concern.**
- If a customer copies the policy **without stripping the braces**, the `Principal` becomes the invalid ARN string `{{arn:aws:iam::111122223333:role/MyEC2InstanceRole}}` → `PutKeyPolicy` should reject it (**fail-closed**, a usability bug), but the two **condition values** `{{EXAMPLE…}}` / `{{0×96}}` are plain strings that `PutKeyPolicy` accepts and that then **never match any real PCR** → **silent lockout** (safe-but-confusing; may push a frustrated operator to loosen the policy).
- The value a customer is *most likely to keep verbatim* is **PCR12 = 96 hex zeros** — the TPM's uninitialized/never-extended baseline, which binds no command-line integrity. This is the under-binding footgun **shipped in AWS's own reference artifact** — **owned by sibling Area 2; cross-reference, do not restate.** This plan adds only the brace-stripping and copy-fidelity dimension.
- `"Resource":"*"` inside a *key* policy scopes to the key itself (normal) — **note explicitly as benign** so a hunter does not misread it as an over-grant.

**High-level Test Scenarios.**
- **Claim:** `PutKeyPolicy` accepts a condition value still containing `{{…}}` with no warning, yielding a permanently inert condition. → **Oracle:** author it; attempt an attested `Decrypt` from a correctly-measured instance → `AccessDenied` despite valid attestation confirms the inert-value lockout.
- **Claim:** The verbatim all-zeros PCR12 half is satisfied by any boot that leaves PCR12 unextended. → **defer to sibling Area 2** for the measurement/boot reproduction.

**Doc evidence.** Example ll.27, 37–38 (`{{…}}`, 96-zero PCR12). **Severity-if-true:** Medium (under-binding → High, owned by sibling).

---

### Area 3 — Gated-action completeness: 3 of 5 attestation-capable actions; GenerateRandom cannot be ViaService-scoped (Lens U / R)
**Background.** `list_kms.md` confirms five actions accept `RecipientAttestation:*`: Decrypt, DeriveSharedSecret, GenerateDataKey, GenerateDataKeyPair, GenerateRandom. The example gates **Decrypt + GenerateDataKey + GenerateRandom** and omits **DeriveSharedSecret + GenerateDataKeyPair**.

**Security Concern.** If the protected CMK is an asymmetric/agreement key (so DeriveSharedSecret / GenerateDataKeyPair are usable), the "attested-only" intent is incomplete: those two operations are not constrained by this statement. More subtly, **gating `GenerateRandom` by attestation is unusual** — it returns random bytes, not key-derived material; its purpose here is delivering entropy *into* the attested environment via `CiphertextForRecipient`. The `GenerateRandom` IAM row (l.501) carries **only** the `RecipientAttestation` keys — **no `kms:ViaService`/`EncryptionContext`/`CallerAccount`** — so an author cannot add those defense-in-depth constraints to the GenerateRandom path even if they want to (asymmetry worth flagging; it also means a `GenerateRandom` allow is scopable *only* by the attestation condition).

**High-level Test Scenarios.**
- **Claim:** On an asymmetric CMK configured per this page, `DeriveSharedSecret`/`GenerateDataKeyPair` are reachable by an allowing statement without satisfying the attestation condition. → **Oracle:** policy-author review + `SimulateCustomPolicy`.
- **Claim:** No `kms:ViaService` can be attached to the `GenerateRandom` statement (not in its condition-key set). → **Oracle:** `list_kms.md` l.501 (confirmed) + `PutKeyPolicy` rejection if attempted.

**Doc evidence.** `list_kms.md` ll.393/417/471/477/501; example `Action` list ll.29–33. **Severity-if-true:** Low–Medium (completeness / defense-in-depth).

---

### Area 4 — Scoping omissions: no `kms:ViaService`, `kms:EncryptionContext`, or `kms:CallerAccount` (Lens H / S / defense-in-depth)
**Background.** The gated statement constrains the request *only* by `Principal` + the two PCR conditions. It adds no `kms:ViaService` (restrict to `ec2.<region>.amazonaws.com` / the intended integration), no `kms:EncryptionContext:*` (bind the ciphertext to a resource/purpose), and no `kms:CallerAccount` (all available on Decrypt/GenerateDataKey per `list_kms.md`).

**Security Concern.** Combined with Area 1 (gate not mandatory) and sibling Area 1 (reproducible PCRs + broad `Principal`), the absence of `ViaService`/`EncryptionContext` means that *when the attestation path is used*, nothing further bounds *which* service invoked it or *what context* the plaintext is bound to — the only bindings are the role identity and the PCR values (which are public/reproducible per the sibling). This is a defense-in-depth gap in the AWS-authored example, not an independent bypass.

**High-level Test Scenarios.**
- **Claim:** The example statement authorizes the gated ops regardless of invoking service / encryption context. → **Oracle:** `SimulateCustomPolicy` showing the conditions are absent; confirm no doc sentence recommends adding them.

**Doc evidence.** `list_kms.md` condition-key sets for the 5 actions; example `Condition` block (PCR-only). **Severity-if-true:** Low (hardening; raises severity of Area 1 / sibling Area 1 as an amplifier).

---

### Area 5 — Policy-evaluation semantics of the attestation condition (Lens S / W)
**Background.** The example uses `StringEqualsIgnoreCase` on a String-typed PCR key.

**Security Concern.**
- **Absent-attestation on the *Allow* form (fail-closed for the statement itself):** a request with no `Recipient` → the key `kms:RecipientAttestation:NitroTPMPCR4` is *absent* → `StringEqualsIgnoreCase` evaluates false → this statement does not apply. This is *why* authors wrongly believe the Allow-only form is a mandatory gate — the statement is individually fail-closed, but it does nothing to *deny* access granted by other statements (the crux of Area 1).
- **The Deny form customers must write to make it mandatory is exactly where vacuous-truth bites:** a naive `"Deny" … "StringNotEquals":{"kms:RecipientAttestation:NitroTPMPCR4":"<v>"}` is **skipped entirely for a request with no attestation key present** (absent key ⇒ `StringNotEquals` is true only if present-and-different; semantics must be paired with `Null`/`…IfExists`) → a no-attestation request slips past the Deny → fail-open. This is the Lens-S policy-evaluation-semantics trap, made likely *because the page omits the Deny form and its correct `Null` guard.*
- **`IgnoreCase` on hex:** benign for well-formed digests (hex is case-insensitive); carry only as a minor sub-check that no non-hex marker can widen a match.
- **Operator substitution (`StringLike`):** the KMS docs recommend `StringEqualsIgnoreCase` but never warn against `StringLike`; a customer who authors `"StringLike":{"kms:RecipientAttestation:NitroTPMPCR4":"*"}` (or any wildcard) silently accepts *any* measurement → attestation condition becomes vacuous. → **Oracle:** author it; any attestation doc satisfies the gate.
- **"up to 96 bytes" value-length imprecision:** the KMS page states the PCR value is "a lower-case hexadecimal string of up to 96 bytes." SHA-384 is 48 bytes / 96 hex chars; "up to" + "bytes" is ambiguous. → **Oracle:** does `PutKeyPolicy` accept a short/prefix value, and if so does matching compare only a prefix (a dangerous match-widening) or require exact equality? (open doc-gap #1).
- **`PutKeyPolicy` schema validation** of a bogus PCR index (`NitroTPMPCR99`) or wrong-length value → open doc-gap (owned as a carried item by sibling Area 2 / its §8 Lens-H note); confirm live, don't resolve from docs.

**High-level Test Scenarios.**
- **Claim:** A `Deny`-based "mandatory attestation" statement authored from first principles (no `Null` guard) fails open on a no-attestation request. → **Oracle:** author both the un-guarded and `Null`-guarded Deny forms; a no-`Recipient` `Decrypt` succeeds against the un-guarded form, `AccessDenied` against the guarded form.
- **Claim:** `PutKeyPolicy` accepts `kms:RecipientAttestation:NitroTPMPCR99` / a 95-hex value with no error. → **Oracle:** author it; observe accept/reject (doc-gap).

**Doc evidence.** Example `Condition` operator ll.36–38; `conditions-nitro-tpm.html` (semantics — see §8 subagent note); IAM policy-evaluation `Null`/absent-key rules. **Severity-if-true:** Medium–High where a customer's own mandatory-attestation Deny fails open.

---

### Cross-referenced areas (owned by `nitrotpm-attestation-attack-research-plan.md` — do NOT restate)
- **PCR-match defeat via reproducible public-recipe measurements under a broad `Principal`** → sibling **Area 1** (Critical-if-broad-Principal). This page's example `Principal` is a single role, but the prose nudges authors to over-trust the PCR condition.
- **Under-binding / all-zeros PCR12 shipped in this page's example** → sibling **Area 2** (High). This plan contributes only the copy-fidelity/brace angle (Area 2 here).
- **`PCR*` (Enclaves) vs `NitroTPMPCR*` (NitroTPM) key-family confusion** → sibling **Area 3** (silent lockout). This page never mentions the Enclaves family exists.
- **Attestation-document replay / `nonce` "Not used for attestation with AWS KMS" / no TTL / RSA-only response binding** → sibling **Area 4**.
- **3P-verifier COSE/CBOR/CRL/algorithm-pin surface** reached via this page's top Note → `nitrotpm-attestation-document-validate.md` → sibling **Areas 5–6**.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| No-attestation `Decrypt` succeeds via default IAM-delegation statement | KMS key policy (full, as deployed) | Page's "only if attestation" prose — attacked by showing the Allow-only form is additive, not restrictive (Area 1) |
| Verbatim copy yields inert/under-binding/incomplete policy | The shipped example artifact | The example itself (`{{…}}`, all-zeros PCR12, 3-of-5 actions) (Areas 2–3) |
| Customer-authored mandatory-attestation Deny fails open | `PutKeyPolicy` + condition semantics | None shown — page omits the Deny form and its `Null` guard (Area 5) |
| Gated statement invokable outside EC2 / unbound context | KMS crypto ops | Absent `ViaService`/`EncryptionContext`/`CallerAccount` (Area 4) |
| PCR condition satisfied by attacker's self-built AMI | KMS key policy `Principal` | `Principal` clause (the only non-public binding) → sibling Area 1 |
| `PutKeyPolicy` accepts bogus PCR index/length | KMS schema validation | Unconfirmed (doc-gap) → sibling Area 2 |

---

## 7. Out-of-Scope Risk Categories
- The AWS Nitro Hypervisor COSE signing identity / attestation-document root of trust and any KMS fleet credential — **service plane, hard stop.**
- The guest-side `nitro-tpm-attest` tooling internals and PCR measurement mechanics — owned by the sibling plan's attestable-AMI/build areas.
- A customer who authors their *own* over-broad key policy from scratch unrelated to this page's guidance — ordinary customer least-privilege footgun (out of scope). **In scope here only because the weak/incomplete artifact and misleading "only if" prose are AWS-authored and copy-verbatim** (Lens R/S/U carve-out → Tier-2).
- UEFI Secure Boot / PCR7 internals except as the measurement feeding the condition.
- Classic `kms:EncryptionContext` manipulation unrelated to the attestation path.

## 8. Null hypotheses / doc gaps
- **Lens A (cross-tenant IDOR):** Null for this page — the artifact is account-local policy construction; cross-account PCR-match is the sibling's Area 1, not an IDOR. Checked: the full page + `list_kms.md` condition-key rows.
- **Lens G (SSRF):** Null — no field on this page is a URL/host the service dereferences (the only URLs are doc hyperlinks). Checked the full page.
- **Lens B/C (PassRole/vending):** Null here — `Principal` is a static ARN in a resource policy, not a role the service assumes on the caller's behalf; EC2-role trust is the sibling's domain.
- **Lens H (encryption-context confusion):** fired only as the *omission* in Area 4; no active encryption-context interplay documented on this page.
- **Open doc-gaps (confirm live, do not resolve from docs):**
  1. Whether `PutKeyPolicy` schema-validates PCR *index* (reject `NitroTPMPCR99`) and *value length* (reject non-96-hex). [also carried by sibling]
  2. Exact fail-open/closed behavior of a request with no attestation document against the Allow-only form vs a `Deny`+`Null` form — **the Area 1 / Area 5 core oracle** (settled by the subagent's reading of `conditions-nitro-tpm.html`; see provenance below).
  3. Whether gating `GenerateRandom` by attestation has any security value given it returns non-key material, and whether its lack of `ViaService` is intentional.

### Provenance / KMS condition-key semantics (settled from `conditions-nitro-tpm.html` + siblings; online `.md` twins matched the offline mirror verbatim, 2026-10-15)
Facts a follow-up agent can rely on without re-reading the KMS developer guide:
- **Operation set (verbatim):** the `kms:RecipientAttestation:NitroTPMPCR<PCR_ID>` key "controls access to `Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`, `GenerateDataKeyPair`, and `GenerateRandom` … only when the PCRs from the signed attestation document in the request match the PCRs in the condition key." Matches `list_kms.md`. The target page's example gates 3 of these 5 (Area 3).
- **Value format (verbatim):** "The PCR value must be a lower-case hexadecimal string of **up to 96 bytes**." Note the doc says "up to" and "bytes" (SHA-384 is 48 bytes / 96 hex chars) — a **doc imprecision** worth confirming live: does `PutKeyPolicy` accept a *short/prefix* value, and does matching then compare a prefix? (carry into Area 5 / open doc-gap #1).
- **Fail behavior — THE Area 1 pivot (verbatim):** "If the request does not include an attestation document, permission is denied because this condition is not satisfied." → confirms the *Allow* statement is **individually fail-closed**. The KMS docs **never discuss these keys in a `Deny` statement** and never show a mandatory-attestation (Deny-form) policy. This is exactly why the Allow-only artifact *looks* like a hard gate while remaining bypassable via any other allowing statement (Area 1 headline) — and why a customer's hand-rolled Deny is prone to the `Null`/absent-key vacuous-truth trap the docs give no guidance on (Area 5).
- **Operator:** both the KMS page and the target recommend `StringEqualsIgnoreCase` (canonical values are lower-case; case-insensitive compare tolerates variance). **No warning against `StringLike`/wildcards** → a customer could author `StringLike` with `*` and silently widen the match (Area 5 sub-check).
- **No ImageSha384 for NitroTPM:** unlike Nitro **Enclaves** (`kms:RecipientAttestation:ImageSha384` = PCR0, plus a "custom PCR ID you defined" flexibility), the NitroTPM family exposes only the generic `NitroTPMPCR<id>` pattern — no image-digest shortcut, no custom-PCR language. (Family confusion → sibling Area 3.)
- **Recipient / response binding (verbatim):** NitroTPM uses the **same** `Recipient` mechanism as Enclaves; on success KMS returns `CiphertextForRecipient` encrypted to the RSA public key embedded in the attestation document and the `Plaintext` field is null/empty. The condition "is effective only when the `Recipient` parameter … specifies a signed attestation document from NitroTPM." (Response-binding / RSA-only / replay → sibling Area 4.)
- **Nonce (verbatim, EC2 UG `attestation-get-doc.md`):** the attestation-document `nonce` field is "**Not used for attestation with AWS KMS**" — confirms sibling Area 4's no-freshness finding for the KMS path specifically.
- **PCR semantics (verbatim, `nitrotpm-attestation-document-content.md`):** PCR4 = Boot Manager Code; PCR7 = Secure Boot Policy; PCR12 = hash of the UEFI boot-binary command line ("Required in conjunction with PCR4 for standard boot to validate the command line was not modified"). "PCR4, PCR7, and PCR12 specifically are used to validate that an instance was launched using an Attestable AMI." No doc warning anywhere about PCR12 all-zeros / under-binding (→ sibling Area 2 owns the smoking gun).
- **CloudTrail (`ct-nitro-tpm.md`):** attested calls surface PCR4/7/8/9/16/23 — a reader-side artifact; PCR17–22 are undocumented across the chapter.
