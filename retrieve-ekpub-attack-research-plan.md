# Retrieve NitroTPM Endorsement Key (`GetInstanceTpmEkPub`) — Attack Research Plan

> **Scope split — read this first.** This plan is the dedicated **EK-READ RUNBOOK COMPLEMENT** for the
> single page `retrieve-ekpub.html` and its API reference `API_GetInstanceTpmEkPub.html`. It is a
> **thin, procedural complement** — the *mechanism-level* EK leads already live in two sibling plans and
> are **NOT re-derived here**:
> - `nitrotpm-attack-research-plan.md` (the HUB) owns the EK-identity/IDOR leads **A-1 (cross-account
>   EKpub read)** and **A-2 (intra-account cross-tenant EK tracking via `Resource:"*"`)**, plus the
>   `TPM2_MakeCredential` channel note. This plan is the authoritative **execution reference** for those
>   two leads (it documents the exact command, params, and oracle a hunter runs) and it **corrects and
>   enriches** the hub's condition-key facts — but it defers the IDOR *severity framing* to the hub.
> - `nitrotpm-attestation-attack-research-plan.md` owns everything attestation (EK-cert-chain absence,
>   COSE, PCR, KMS `RecipientAttestation`). Hand-offs only.
> - `verify-nitrotpm-support-on-instance-attack-research-plan.md` owns the `GetInstanceTpmEkPub`
>   (scopable) **vs** `DescribeInstances` (unscopable) **Lens-X parity asymmetry** (its Area 2). Cross-ref,
>   not restated.
>
> **Net-new value of THIS page vs the hub:** (1) a **condition-key CORRECTION** — the action carries ~21
> instance-resource keys, not the 6 the hub listed nor the "zero" the attestation plan claimed;
> (2) the **`DryRun` false-oracle trap** (from the API ref, absent from the hub's A-1 oracle);
> (3) the page's **"securely retrieve … at any time"** guarantee (Lens U/Y — unenforced marketing word +
> no instance-state gate); (4) the **closed-enum / required-param validation** surface (Lens F);
> (5) the **empty Errors section** → A-1 error-oracle behavior is fully undocumented (doc-gap).

Source of leads: `UserGuide/retrieve-ekpub.html` (+`.md` twin, fetched live this session) and
`APIReference/API_GetInstanceTpmEkPub.html` (+`.md`), authoritative IAM facts from
`service-authorization/.../list_ec2.md` (action table line ~8330). Online `.md` twin of the UserGuide
page fetched 2026-10-15; offline mirror present and consistent. Status: **documentation-derived
hypotheses only; nothing tested against a live account.**

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity.**
- `GetInstanceTpmEkPub` is **non-mutating** (Access level: Read). All leads here are safe read-only probes
  against **instances you own in accounts you own**. Never name another tenant's `InstanceId`.
- **HARD STOP:** if any response exposes an identity/credential/ARN belonging to AWS's own Nitro service
  plane (EK *private* material, host TPM backing store, internal attestation PKI), stop, preserve
  evidence, flag for AWS-Security disclosure. The EK *public* key is customer-readable by design; the
  private half must never appear — its appearance is the hard stop.

## 1. Pentest Objectives
1. Settle whether `GetInstanceTpmEkPub` enforces **caller-account ownership** of `InstanceId` or only
   existence (cross-account EKpub read = IDOR) — and record the **exact error-code behavior**, which this
   page documents **nowhere** (empty Errors section). *(Severity framing → hub Lead A-1.)*
2. Prove the **`DryRun` false-oracle trap**: that `--dry-run` reflects **caller IAM only**, is evaluated
   **before** resource resolution, and therefore must **not** be used as the cross-account ownership /
   existence oracle for Objective 1.
3. Enumerate the **actual condition-key set** on the action (correct the hub/attestation undercounts) and
   confirm which keys can scope an EK read — the deliverable `Condition` block that fixes hub Lead A-2.
4. Test the page's **"securely retrieve … at any time"** guarantee: what mechanism makes it "secure"
   (transport/SigV4 only — is there `aws:SecureTransport` to enforce it?), and does "at any time" mean the
   EK is readable regardless of instance **run-state** (stopped/hibernated) — a stable-identifier
   availability property.
5. Confirm **input-validation fail-closed** on the two required closed enums (`KeyType`, `KeyFormat`) and
   the required `InstanceId`, and whether the two `KeyType` values yield **two distinct but each-stable**
   EKpub values for one instance (affects the A-2 tracking primitive).

## 2. Components, Assets, and Design

**What this page is.** The customer-facing runbook for one control-plane API that reads out the **public**
half of a NitroTPM instance's **Endorsement Key**. One instance → one persistent EK; the API returns its
public component in a caller-chosen encoding. No mutation, no enablement, no attestation document.

**Interface:** SigV4 IAM over the regional EC2 HTTPS endpoint. CLI `aws ec2 get-instance-tpm-ek-pub`;
PowerShell `Get-EC2InstanceTpmEkPub`. No console route (consistent with the whole NitroTPM surface being
console-invisible — see hub §Undocumented knobs). No SDK-hidden/non-SDK variant (present in all listed
SDKs).

**Request shape (API ref, authoritative):**
- `InstanceId` *(String, **Required**)* — the only resource identifier. Shape `i-`+17 hex ⇒ blind
  enumeration infeasible.
- `KeyFormat` *(String, **Required**, closed enum `der | tpmt`)* — `der` = OpenSSL-compatible,
  `tpmt` = TPM-2.0 / tpm2-tools. Output base64.
- `KeyType` *(String, **Required**, closed enum `rsa-2048 | ecc-sec-p384`)*.
- `DryRun` *(Boolean, optional)* — "verify whether the request will succeed, without actually making the
  request." → `DryRunOperation` on success, `UnauthorizedOperation` otherwise. **IAM-only probe.**

**Response shape:** `instanceId`, `keyFormat`, `keyType`, `keyValue` (base64 EK public material),
`requestId`. **No EK certificate / manufacturer-genuineness chain is returned** → hand-off to attestation
plan (third-party-verifier trust gap).

**Errors section: EMPTY** — only "Common Error Types" are referenced. The service's behavior for a
foreign-owned or nonexistent `InstanceId` (NotFound vs Unauthorized vs validation) is **undocumented**,
which is itself the input to Objective 1's oracle.

**Trust zones:** customer account (owns instance + IAM) ↔ **AWS Nitro plane** (holds EK *private* key,
HARD STOP). There is **no resource-based sharing primitive for `instance` objects**, so ownership is
expected to be account-bound by ARN resolution — an inference, not a documented guarantee (Objective 1).

```
   caller (SigV4) ──ec2:GetInstanceTpmEkPub(InstanceId, KeyType, KeyFormat)──►  EC2 control plane
        │  [DryRun=true → IAM-only check, pre-resource-resolution]                     │
        │                                                                              ▼
        │                                                            instance* (21 scopable cond keys)
        ▼                                                                              │
   base64 keyValue  ◄──── public EK only (der|tpmt, rsa-2048|ecc-p384) ────────────────┘
                          ▲ EK PRIVATE half never leaves Nitro plane  ── HARD STOP if it ever appears
```

## 3. API / Interface Surface

| Name | Mutating | Resource (list_ec2) | Condition keys | Access | Notes |
|---|---|---|---|---|---|
| `GetInstanceTpmEkPub` | **No** (Read) | `instance*` (\*required) | **~21 keys** — see §4 Lens S | Read | `DryRun` optional; `InstanceId`/`KeyType`/`KeyFormat` required; empty Errors section; no console route; no cert chain. |

**Undocumented / page-level deltas:**
- `KeyType=ecc-sec-p384` is **never shown on this page** — all four examples use `rsa-2048`. The ECC type
  is only in the API-ref enum. (Confirms hub's "UG examples hide ECC"; this is the specific page.)
- `DryRun` is in the **API ref only** — the UserGuide runbook examples omit it, so a hunter copying the
  runbook won't see it; the API ref is where the false-oracle trap surfaces.
- **Doc-internal inconsistency:** the `list_ec2` *action-summary* block (line ~3264) prints the condition
  key field **blank**, while the authoritative *action table* (line ~8330) lists ~21 keys. Trust the
  action table; the blank summary is a presentation gap (Lens U doc-vs-doc, Informational).

## 4. Boundary-Lens Catalog

### Lens A — Cross-tenant resource access (IDOR)  → severity framing DEFERRED to hub Lead A-1/A-2
This page is the **execution reference** for the hub's two EK IDOR leads; it adds the error-oracle doc-gap
and the DryRun trap below, but does **not** restate A-1/A-2 severity. Net-new here:

**Lead A-oracle (error-behavior is undocumented).**
- **Claim:** Because the Errors section is empty, the response to a **foreign-owned** `InstanceId` is
  unspecified and must be measured, not assumed.
- **Oracle (run under a principal allowed on `Resource:"*"`, naming an instance in a 2nd account you own):**
  `InvalidInstanceID.NotFound` ⇒ account-scoped server-side, **refuted, no leak**; `UnauthorizedOperation`
  ⇒ instance resolved then denied ⇒ **existence oracle** (weak leak); `keyValue` returned ⇒ **cross-account
  IDOR, Critical** → HARD-STOP-adjacent, escalate per hub A-1.
- **Severity:** per hub A-1 (Critical-if-true; expected refuted). Value of *this* lead = it records that
  the page documents **zero** error behavior, so the oracle result is pure net-new evidence.

### Lens A (variant) — `DryRun` as a FALSE ownership/existence oracle  ★ NET-NEW HEADLINE
- **Claim (to establish, so hunters don't mis-call A-1):** `--dry-run` reflects **only the caller's IAM
  permission**, is evaluated **before resource resolution**, and therefore returns `DryRunOperation` /
  `UnauthorizedOperation` **independent of whether the named instance exists or is cross-account**.
- **Mechanism (doc evidence):** API ref `DryRun` — "verify whether the request *will succeed*… If the
  request will succeed, the response is `DryRunOperation`. Otherwise `UnauthorizedOperation`." This is an
  authorization pre-check, not an existence check. Matches the skill's Lens-A variant warning: *treat
  `DryRunOperation` as caller-IAM only, NOT an ownership oracle — a false-positive trap.*
- **Confirm/Refute oracle:** With a principal allowed on `Resource:"*"`, call `--dry-run` three ways:
  (a) a **real owned** instance, (b) a **syntactically valid but nonexistent** `i-…`, (c) a **foreign-owned**
  instance id. If all three return `DryRunOperation` (because IAM allows), DryRun is confirmed **blind to
  resource ownership/existence** → it must **not** be used for A-1; only the **real** (non-dry-run) call
  settles ownership. If (b)/(c) differ, record the divergence (unexpected — would itself be an oracle).
- **Severity:** Informational **methodology control** — but high leverage: it prevents a hunter from
  reporting a false cross-account IDOR (DryRun "succeeding" on a foreign id proves nothing).

### Lens S — Condition-key scoping semantics  ★ NET-NEW CORRECTION
**Correction anchor (trust this over both siblings):** per the `list_ec2` **action table** (line ~8330),
`ec2:GetInstanceTpmEkPub` on `instance*` carries **~21 condition keys**, not 6 and not zero:
`aws:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:CpuOptionsAmdSevSnp`,
`ec2:EbsOptimized`, `ec2:InstanceAutoRecovery`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`,
`ec2:InstanceMarketType`, `ec2:InstanceMetadataTags`, `ec2:InstanceProfile`, `ec2:InstanceType`,
`ec2:ManagedResourceOperator`, `ec2:MetadataHttpEndpoint`, `ec2:MetadataHttpPutResponseHopLimit`,
`ec2:MetadataHttpTokens`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:RootDeviceType`, `ec2:Tenancy`.
- This is the **generic `instance*` resource-type key bundle** (near-identical to `GetInstanceUefiData`),
  **not** an EK-specific set. There is **no condition key keyed on `KeyType`/`KeyFormat`** → you can scope
  *which instance's* EK is readable, never *which key type/format*.
- **Lead S-1 (the A-2 remediation deliverable — stronger than the hub's).** Because the action is richly
  scopable, hub Lead A-2 (cross-team EK harvesting on `Resource:"*"`) is a **customer IAM hygiene gap, not
  an AWS defect** — and the fix set is broad: scope by `ec2:ResourceTag/team`, by `ec2:Tenancy`
  (`dedicated`/`host` isolation), by `ec2:InstanceProfile`, even by `ec2:CpuOptionsAmdSevSnp` (restrict EK
  reads to confidential-compute instances). **Oracle:** author a Deny with
  `Condition: StringNotEquals { ec2:ResourceTag/team: "${aws:PrincipalTag/team}" }` on
  `GetInstanceTpmEkPub` and confirm via `iam:SimulatePrincipalPolicy` that a cross-team EK read is denied
  while same-team is allowed. **Severity:** Low–Medium (customer footgun; AWS ships the fix).
- **Lead S-2 (tag-key presence vs ownership — skill Lens-S warning).** `aws:ResourceTag/${TagKey}:"*"`
  matches the tag **key** regardless of value → a Deny/Allow written on tag-key *presence* passes **any**
  tagged instance. Confirm the EK-scoping policy binds a tag **value** bound to the principal, not mere
  presence. **Severity:** Low (bounds the A-2 blast radius if mis-authored).

### Lens U / Y — "securely retrieve … at any time" guarantee vs enforcement  ★ NET-NEW
- **Claim (to test):** The page's opening promise *"You can **securely** retrieve the public endorsement
  key for an instance **at any time**"* is backed by **no stated mechanism** beyond SigV4/TLS transport.
- **Mechanism / sub-tests:**
  - **"securely"** = transport (HTTPS SigV4) + IAM; the EK *public* key is non-secret by design, so
    "securely" is largely marketing. **Y-oracle:** is there an `aws:SecureTransport` condition key to
    *deny* a cleartext call, and does the EC2 endpoint reject `http://`? (Global key; enforceable — confirm
    the service honors it. Expected: TLS-only, so Informational.)
  - **"at any time"** = **no instance run-state gate** — the EK persists for instance life, so a
    **stopped / hibernated** instance's EK should still read out. **Oracle:** stop an owned NitroTPM
    instance, call `get-instance-tpm-ek-pub`, confirm `keyValue` returned (no `IncorrectInstanceState`).
    Confirms the EK is a run-state-independent stable identifier (reinforces the A-2 tracking primitive —
    an attacker who read the EK once can re-confirm an instance's identity across stop/start/resize).
- **Severity:** Informational (guarantee is advisory/transport-only; "at any time" is by-design TPM
  persistence). Value = closing the guarantee cleanly and documenting the run-state-independence that
  makes the EK a durable tracking token.

### Lens F — Closed-enum / required-param validation (fail-closed)
- **Claim:** `KeyType` and `KeyFormat` are **required closed enums**; the service must reject out-of-set
  values and missing params with `ValidationException`/`MissingParameter`, not fall back to a default.
- **Oracle:** call with `--key-type rsa-4096` (out of set), `--key-format pem` (out of set), omit
  `--key-type`, and send a malformed `--instance-id`. Expect clean 400-class rejection each time; a
  **default-on-unknown** (e.g. silently returning rsa-2048 for an unknown type) or a 500 would be the
  finding. **Also:** confirm the **two valid `KeyType` values each return a distinct, individually stable**
  `keyValue` for one instance (both derived from the same per-instance seed) — relevant to A-2 (an attacker
  can fingerprint on either type). **Severity:** Low (expected fail-closed; a default-fallback or 500 would
  raise to Medium as a validator/enumeration oracle).

## 4b. Explicit NULL hypotheses (pages checked, lens does not fire)
Pages read: `retrieve-ekpub.html` (+`.md`), `API_GetInstanceTpmEkPub.html` (+`.md`), `list_ec2` action
table + summary.
- **Lens G (SSRF):** NULL — no field on this API is a location the service dereferences; `keyValue` is a
  read-out, `InstanceId` is a resource id, not a URL.
- **Lens Q (upload/parse):** NULL — no customer blob ingested; all inputs are an id + two enums.
- **Lens B / C (PassRole / cred-vending):** NULL — no role-ARN input, no session policy, no credential
  returned (public key only).
- **Lens EE (land-grab):** NULL for this page — `InstanceId` is caller-scoped, not a predictable global
  namespace. (The whoAMI land-grab lives on the *enablement/discovery* pages → hub Lead EE-1.)
- **Lens X (twin/parity):** fires but **owned by the verify-on-instance plan** (GetInstanceTpmEkPub
  scopable vs DescribeInstances unscopable). Cross-ref only.
- **Lens O (audit):** `GetInstanceTpmEkPub` is a control-plane call ⇒ CloudTrail-logged (Read event) —
  unlike the guest-side `tpm.msc` path on the verify plan. Informational; no evasion surface on this API.
- **Attestation / EK-cert-chain / PCR / KMS RecipientAttestation:** **→ DEFER** to
  `nitrotpm-attestation-attack-research-plan.md`. Only hand-off: this API returns **no cert chain**, an
  input to that plan's third-party-verifier trust analysis.

## 5. Priority order (concentrate fire)
1. **Lens A-variant — DryRun false-oracle trap.** Cheapest, highest-leverage: three dry-run calls settle
   that `--dry-run` must not be used for the cross-account IDOR test. Do this *before* A-1 to avoid a false
   positive.
2. **Lens A-oracle — real (non-dry-run) cross-account call** (hub Lead A-1 execution): record the exact
   error code (page documents none). Critical-if-key-returned; expected refuted.
3. **Lens S — condition-key correction + A-2 remediation policy** via `iam:SimulatePrincipalPolicy`
   (resource-free, safest first oracle). Delivers the fix block; corrects both sibling plans' key counts.
4. **Lens U/Y — "at any time" run-state independence + `aws:SecureTransport`.** One stopped-instance read.
5. **Lens F — enum/param fail-closed + per-KeyType stable-value fingerprint.**

## 6. Hand-offs & carried doc-gaps
- **To the hub (`nitrotpm-attack-research-plan.md`):** this plan is the execution reference for its
  Leads A-1/A-2 and **supersedes its condition-key list** for `GetInstanceTpmEkPub` (6 → ~21 keys; §4
  Lens S). Update the hub's §3 table row and §8 corrections accordingly.
- **To the attestation plan:** confirms **no EK certificate chain** is returned by this API (feeds the
  3P-verifier trust gap). Also corrects that plan's "zero condition keys on `GetInstanceTpmEkPub`" to the
  ~21-key reality.
- **To the verify-on-instance plan:** reinforces its Lens-X parity (this scopable Read vs unscopable
  `DescribeInstances`); the ~21-key set here is the "scopable" side of that asymmetry.
- **Doc-gaps:** (a) **empty Errors section** — foreign-/nonexistent-id behavior undocumented (Lead
  A-oracle). (b) **`DryRun` pre-resource-resolution semantics** stated only generically — confirm live.
  (c) `aws:SecureTransport` enforceability for the "securely" claim not stated on-page. (d) EK
  **rotation / `TPM2_Clear`** semantics across stop/start/resize undocumented — Lens U/Y "at any time"
  and A-2 tracking both assume per-instance-life stability; confirm the EK value is unchanged across a
  stop/start.

## 7. Severity summary (doc-stage)

| Lead | Lens | Class | Verdict (doc-stage) | Severity |
|---|---|---|---|---|
| DryRun false-oracle | A (variant) | methodology control | plausible per API-ref semantics | Informational (high-leverage) |
| A-oracle (error behavior) | A | undocumented error path | needs live oracle | per hub A-1 (Critical-if-true) |
| Cond-key correction / A-2 fix | S | AWS doc-count error + customer-hygiene fix | confirmed from list_ec2 action table | Low–Medium |
| "at any time" run-state + SecureTransport | U/Y | guarantee-vs-mechanism | by-design; transport-only | Informational |
| enum/param fail-closed | F | input validation | expected fail-closed | Low (Medium if default-fallback/500) |
| doc-internal cond-key blank summary | U | doc-vs-doc integrity | observed (line 3264 vs 8330) | Informational |

## 8. Corrections this plan makes to sibling plans
- **Both `nitrotpm` hub (§3/§8) and `nitrotpm-attestation` (Area 8):** `GetInstanceTpmEkPub` carries the
  **full ~21-key `instance*` bundle** (listed in §4 Lens S) — not the hub's 6-key subset and not the
  attestation plan's "zero condition keys." The genuinely absent keys are **EK-attribute keys**
  (no `KeyType`/`KeyFormat` condition) — you can scope *which instance*, never *which key material shape*.
- **`DryRun` is NOT an ownership/existence oracle** — add this caveat wherever a sibling proposes probing
  cross-account EK access (hub A-1): only the real call settles it.
