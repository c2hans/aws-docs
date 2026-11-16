# IAM Roles Anywhere — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/rolesanywhere/latest/**` (userguide + APIReference), `/work/aws-docs/docs/aws-managed-policy/latest/reference/AWSRolesAnywhere{FullAccess,ReadOnly,ServicePolicy}.md`, `/work/aws-docs/docs/service-authorization/latest/reference/list_rolesanywhere.md`; cross-checked against the live pages at `https://docs.aws.amazon.com/rolesanywhere/latest/...` (append `.md` to any `.html`). Entry page: `userguide/getting-started.html`.
Status: documentation-derived hypotheses only; nothing in this document was tested against a live account *in this run*. **A prior live run (accounts 183174222929 / 289531347876, us-east-1, 2026-09-30) already settled several of these — those results are folded in below and marked `[SETTLED]`; do not re-litigate them.** Prior-run tooling (a from-scratch Python `AWS4-X509-RSA-SHA256` CreateSession signer + cert/CRL generators) lives at `/work/ra/` and should be reused.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — in particular if the **automatic-CDP-revocation fetch** (Area 1) egresses from an AWS fleet identity to a link-local/metadata/internal target — stop, preserve evidence (request IDs, raw responses), and flag for AWS-Security disclosure. Do **not** escalate past existence.
- Roles Anywhere holds **no customer private keys and stores no customer data at rest** (`data-protection.html`: "IAM Roles Anywhere does not hold customer private keys"). Several at-rest / KMS / secret-reachability lenses are therefore genuine null hypotheses (Section 8), not unexamined gaps.
- Positive control first: always run an honest `CreateSession` (honest EE cert + its own trust anchor + a profile that passes a role trusting `rolesanywhere.amazonaws.com`) to validate the signer before any spoof/crux test.

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Vend credentials for a role the caller should not reach** — cross-account, cross-trust-anchor, or bypassing the role trust-policy `Condition` (certificate-attribute or `aws:SourceArn`). `[Largely SETTLED negative — see Area 2]`
2. **Turn the service into a confused deputy / SSRF egress** — make the RA fleet fetch an attacker-chosen target (CDP revocation), or sign/act against a target of the attacker's choosing, under AWS's own identity. `[NEW — Area 1, top priority]`
3. **Forge or widen a session's identity attributes** — populate a `PrincipalTag` / `sts:SourceIdentity` the caller does not legitimately own, or defeat a trust-policy condition via attribute-mapping semantics. `[Partly SETTLED — residual in Area 3]`
4. **Authenticate with a non-conforming signature** — get `CreateSession` to accept a request whose security-relevant content is outside the signature, or crash/confuse the X.509 / ML-DSA / CRL parsers. `[NEW parser surface — Area 4]`
5. **Privilege-escalate within the account** using RA's AWS-managed policies and the `PassRole→assume` chain. `[SETTLED mechanism — Area 5, confirm artifact defect vs customer footgun]`
6. **Defeat revocation / disable, or evade audit attribution** — keep a revoked cert usable, or strip/forge CloudTrail attribution. `[Partly SETTLED — Area 6]`

---

## 2. Components, Assets, and Design

**What it is.** IAM Roles Anywhere bridges a customer PKI to IAM: an X.509 end-entity (EE) certificate, chaining to a CA the customer registered as a *trust anchor*, is exchanged for short-lived STS credentials for an IAM role named in a *profile*. There is **no multi-tenant data-plane fleet** and **no customer data at rest**; the attack surface is (a) a control plane of CRUD APIs and (b) an authentication/vending plane (`CreateSession`).

**Customer-facing interfaces**
- **Control-plane APIs** (standard SigV4, in SDK/CLI): `Create/Get/List/Update/Delete/Enable/Disable` × `TrustAnchor | Profile | Crl`; `GetSubject/ListSubjects`; `Put/DeleteAttributeMapping`; `Put/ResetNotificationSettings`; `Tag/Untag/ListTagsForResource`; `ImportCrl`.
- **Vending plane — `CreateSession` `POST /sessions`** (NON-SDK; custom `AWS4-X509-{RSA,ECDSA,MLDSA}` signing). "CreateSession is an X.509 wrapper around AssumeRole … not included in any SDK or client." (`authentication-create-session.html`)
- **Endpoints:** `rolesanywhere.{region}.amazonaws.com` and dual-stack `rolesanywhere.{region}.api.aws` (IPv4+IPv6, `ip-access.html`); FIPS endpoints; PrivateLink `com.amazonaws.{region}.rolesanywhere` with VPCe policies supported for all actions incl. `CreateSession`.

**Resources & identifiers** (all **account-scoped** ARNs; no cross-tenant namespace):
- `trust-anchor/${TrustAnchorId}`, `profile/${ProfileId}`, `crl/${CrlId}` — UUIDs (see CloudTrail `0ace5b12-24b9-427e-a483-c55884852fbf`).
- `subject/${SubjectId}` — an **audit record keyed by the certificate Subject**; created automatically on first authentication; **no `DeleteSubject` API exists** (persists after all TAs/profiles removed). `[SETTLED]`

**Identity establishment**
- Trust anchor `source.sourceType ∈ {AWS_ACM_PCA, CERTIFICATE_BUNDLE, SELF_SIGNED_REPOSITORY}` (`API_Source`). Only the first two appear in prose/console; **`SELF_SIGNED_REPOSITORY` is API/SDK-only** (undocumented knob — Area 7).
- Cert fields → session: Subject/Issuer/SAN RDNs become `aws:PrincipalTag/x509{Subject,Issuer,SAN}/*`; Subject CN → `sts:SourceIdentity`; **role session name defaults to the hex cert serial** (overridable only if profile `acceptRoleSessionName=true`).
- Signing: `Credential` field carries the **decimal certificate serial** in place of the access-key-id; EE cert in `X-Amz-X509` (b64 DER), chain in `X-Amz-X509-Chain`.

**Roles / privilege levels**
- Service principal `rolesanywhere.amazonaws.com` assumes the customer role (role trust policy grants `sts:AssumeRole`, `sts:TagSession`, `sts:SetSourceIdentity`).
- Service-linked role backed by `AWSRolesAnywhereServicePolicy` (CloudWatch `PutMetricData` + `acm-pca:Get/DescribeCertificateAuthority`).
- Human/automation operators via `AWSRolesAnywhereFullAccess` / `AWSRolesAnywhereReadOnly`.

**Untrusted-data entry / transforms (injection & fetch seams)**
1. EE/chain **X.509 certificate** (DER) → signature verification (RSA / ECDSA / **ML-DSA**) → chain-to-trust-anchor validation → RDN/SAN extraction → PrincipalTags. *(Parser + canonicalization + tag-mapping seam.)*
2. **CA certificate bundle / CRL** (PEM/DER) uploaded via `CreateTrustAnchor` / `ImportCrl` → parsed. *(Parser seam.)*
3. **CDP URLs read out of the attacker's certificate** → **server-side HTTP(S) fetch by the RA fleet** when `crlDpRevocationEnabled=true`. *(SSRF seam — NEW, highest value.)*
4. `sessionPolicy` (JSON) + `managedPolicyArns` on a profile → passed into the AssumeRole call. *(Policy-shaping seam; admin-controlled.)*

```
  attacker-controlled                         AWS-owned (service plane = shared-responsibility line)
  ┌──────────────────┐   POST /sessions      ┌──────────────────────────────────────────────┐
  │ workload + EE cert├──AWS4-X509 signature─▶│ RA vending plane                               │
  │ (+ CA as TA)      │                       │  1. verify sig (RSA/ECDSA/ML-DSA parser)       │
  │ cert CDP URLs ───────┐                    │  2. chain → trust-anchor CA (bound to TA ARN)  │
  └──────────────────┘   │                    │  3. revocation: imported CRL  OR  ┌─ CDP fetch ┼──▶ attacker URL? internal? 169.254.x?
         ▲               └──(attacker URLs)──▶│                                    └───────────┤   [HARD STOP if fleet→internal]
         │ temp creds                         │  4. extract RDN/SAN → PrincipalTags            │
         │                                    │  5. AssumeRole (aws:SourceArn = TA ARN)────────┼──▶ STS ─▶ role creds (customer acct only)
  ┌──────┴───────┐  SigV4 CRUD                │                                                │
  │ IAM operator ├───────────────────────────▶│ RA control plane (trust-anchor/profile/crl/subj)│  account-scoped resources
  └──────────────┘                            └──────────────────────────────────────────────┘
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| External workload (attacker cert) | Customer IAM role creds | `CreateSession` → AssumeRole | Vending creds for a role whose trust `Condition` (cert attr / `aws:SourceArn`) the caller doesn't satisfy, or in another account. `[SETTLED negative: cross-acct blocked both layers; TA↔CA crypto-bound]` |
| Attacker (chooses cert CDP URLs) | **RA service fleet egress → arbitrary host** | `crlDpRevocationEnabled` CDP download | Any fleet-originated request reaching a non-public / link-local / metadata / internal target, or a timing/existence oracle on internal hosts. **HARD STOP if fleet identity.** `[NEW]` |
| RA service principal | Customer role (acts "on your behalf") | STS AssumeRole w/ `aws:SourceArn=TA ARN` | RA assuming a role the caller could not have used directly / cross-account. `[SETTLED: aws:SourceArn is real, reflects true TA, not spoofable]` |
| Caller-supplied cert fields | Session PrincipalTags / `sts:SourceIdentity` | RDN/SAN → tag mapping | Populating an ABAC key the caller shouldn't control, forging `SourceIdentity`, or defeating a `StringNotEquals` condition via a dropped tag. `[Partly SETTLED; dropped-tag fail-open residual]` |
| MITM / non-conforming client | `CreateSession` auth decision | `AWS4-X509` signature coverage | A request whose security-relevant header/param is **unsigned yet still authenticates**, or a signed-vs-executed param divergence. `[NEW]` |
| Low-priv IAM principal (holds RA managed policy) | Any RA-trusting role / admin | `CreateTrustAnchor`+`CreateProfile`+`iam:PassRole` | Assuming a role / reaching permissions beyond what the holder's policy names. `[SETTLED mechanism — artifact-vs-footgun question open]` |
| Caller | Another account's RA resource | `Get*`/`Update*` by ARN/UUID | Reading/mutating a resource in another account. `[Expected negative — account-scoped; confirm no cross-acct Get*]` |
| Any customer surface | **AWS service plane** | — | Any AWS-fleet identity/credential/ARN. **Hard stop + disclosure.** |

---

## 4. API / Interface Inventory

| Name | Method | Mut? | Facing | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| **CreateSession** | `POST /sessions` | Mut (vends creds) | External, **non-SDK** | Yes | Anyone presenting a cert that chains to a TA + satisfies role trust + (optional) VPCe/`CreateSession` resource policy | **The crown jewel.** Custom `AWS4-X509` signing. `durationSeconds=min(profile,request)`. `roleSessionName` honored only if profile opts in. Prime target. |
| CreateTrustAnchor | `POST /trustanchors` | Mut | External | Yes | `rolesanywhere:CreateTrustAnchor` | Inputs: `source{sourceType∈…SELF_SIGNED_REPOSITORY}`, `crlDpRevocationEnabled`, `notificationSettings[≤50]`, `enabled`, tags. |
| UpdateTrustAnchor | `PUT`/`PATCH` | Mut | External | Yes | `rolesanywhere:UpdateTrustAnchor` on `trust-anchor/*` | For ACM-PCA TAs, **only validity period is modifiable; must re-register to refresh**. Flips `crlDpRevocationEnabled`. |
| CreateProfile | `POST /profiles` | Mut | External | Yes | `rolesanywhere:CreateProfile` **+ `iam:PassRole`** (PassedToService=rolesanywhere) | `acceptRoleSessionName`, `managedPolicyArns[≤50]`, `sessionPolicy`, `roleArns[≤250]`, `requireInstanceProperties` (**"Unused, saved for future use"**). |
| UpdateProfile / EnableProfile | — | Mut | External | Yes | + `iam:PassRole` | Note: `EnableProfile` and `UpdateProfile` both require PassRole (per service-auth op table). |
| Put/DeleteAttributeMapping | — | Mut | External | Yes | `…AttributeMapping` on `profile/*` | Controls which cert fields become tags → **governs whether trust-policy conditions can be satisfied/dropped** (Area 3). |
| **ImportCrl** | `POST /crls` | Mut | External | Yes | `rolesanywhere:ImportCrl` | Upload CRL (DER). No resource-type required (RequestTag/TagKeys only). Parser + stale-CRL surface. |
| Enable/Disable/Delete {TA,Profile,Crl} | — | Mut | External | Yes | per-resource | Disable/revoke effect is **immediate (<1.5 s, no TOCTOU)**. `[SETTLED]` |
| Get/List {TA,Profile,Crl,Subject} | — | Non-mut | External | Yes | per-resource; `ListSubjects` **account-scoped** `[SETTLED]` | UUID resources. Enumeration/cross-acct oracle test (low). |
| Put/ResetNotificationSettings | — | Mut | External | Yes | on `trust-anchor/*`; also `Resource:*` in FullAccess | CA/EE expiry notifications via CW/EventBridge/Health. |
| Tag/Untag/ListTagsForResource | — | Mut/Non | External | Yes | ABAC-relevant | `ListTagsForResource` is `Resource:*` in both managed policies. |

Undocumented / console-hidden knobs to probe (Step-3 discipline): **`sourceType=SELF_SIGNED_REPOSITORY`**, **`requireInstanceProperties`** (declared unused), the **deprecated `sessionName`** body param (vs `roleSessionName`), and the `CreateSession` **query-string parameter path** (`postEmptyBody` canonicalization path — Area 4).

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — [NEW, TOP PRIORITY] SSRF / confused-deputy via automatic CDP revocation fetch
**Freshness.** This feature **shipped 2026-11-04** (`doc-history.md`) — **12 days old** at time of writing. Brand-new, immature, attacker-controlled server-side fetch path: the single highest-value lead in this plan.
**Background.** `crlDpRevocationEnabled` (trust-anchor setting, default `false`) turns on *automatic revocation checking*: on **every** `CreateSession`, RA "reads the distribution point URLs **directly from the certificates presented** during authentication, downloads the matching CRLs" server-side (`trust-model.html` §Revocation). The URLs are **entirely attacker-controlled**: "Because the distribution points are read from the certificate, you don't import or register them." The attacker registers their own CA as a trust anchor (`CERTIFICATE_BUNDLE` or `SELF_SIGNED_REPOSITORY`), enables `crlDpRevocationEnabled`, and issues an EE cert whose CDP extension points anywhere — zero AWS-side curation. The fetch is **unauthenticated, identity-less, and has no documented per-tenant allowlist** beyond "public IP + internet-reachable". **Amplification math:** "for each certificate **in the chain**, for each distribution point" × "at most five distribution point URLs for each certificate" → a deep attacker chain multiplies the 5×/cert fan-out across every chain cert, per `CreateSession` call.

**Security Concern.** This is a server-side fetch from an AWS-owned fleet identity driven by attacker-chosen URLs — the textbook SSRF seam (Lens G), plus a cross-tenant DoS amplifier (Lens L). Documented guards: HTTP/HTTPS only; **default port 80/443 only**; host must "resolve to **public IP addresses** and be reachable from the internet"; no redirects followed; ≤2048-char URL; ≤1 MB CRL; ≤5 URLs/cert; "first time … downloads the CRL during the `CreateSession` request, which can add latency." If no valid CRL is obtained → request **denied** (fail-closed — good).

**High-level Test Scenarios** (all require ONLY an attacker-owned TA + cert — no victim):
- **Claim:** the "public IP" guard is evaluated once / at DNS-resolution time and can be defeated by **DNS rebinding** (public A record at check, private/link-local at fetch) → fleet fetches `169.254.169.254` or an internal host. **Oracle:** controlled authoritative DNS flipping A record between resolve and fetch; a hit to `http://169.254.169.254/…` from AWS fleet egress. **Severity if true: Critical + HARD STOP.**
- **Claim:** the latency of the "first-time download during CreateSession" is an **existence/port oracle** for internal/public hosts (open vs filtered vs closed → distinguishable `CreateSession` response time), even if content is never reflected. **Oracle:** differential timing across known-open vs filtered CDP hosts. **Severity: Medium (blind SSRF oracle); High if it probes internal ranges.**
- **Claim:** redirect-not-followed / port-restriction / public-IP checks are enforced on the **first** URL but not on **refresh** (CRLs refreshed up to 30 min) or not on URLs 2–5. **Oracle:** mixed CDP list (first benign-public, later entries internal); observe which get fetched. **Severity: High.**
- **Claim:** amplification/DoS — N CreateSession calls × 5 URLs × attacker-chosen large-but-≤1 MB CRLs force the shared fleet to egress heavily to a victim host (reflected DoS), or exhaust the fleet's fetch workers (noisy-neighbor). **Oracle:** egress volume at an attacker-run sink; cross-tenant CreateSession latency rise. **Severity: High if cross-tenant.**
- **Claim:** any downloaded CRL content or fetch error is **reflected** into a `CreateSession`/`GetCrl` response, CloudTrail `additionalEventData`, or a notification → blind SSRF becomes readable. **Oracle:** sentinel content in the attacker CRL appearing in any API/log field. **Severity: High→Critical if internal content returned.** **Doc-derived expectation = NEGATIVE/blind:** CDP-fetched CRLs "are not created as resources in your account. You can't view or manage individual distribution points" — **no API surfaces their content**, so expect a *blind* SSRF (timing/egress-only), not a content-reflection oracle. (`ImportCrl` does echo `crlData`, but that is self-reflection of attacker-uploaded bytes — useless.) Treat this scenario as a quick confirm-then-move-on; the value is in the timing/rebinding/egress oracles above.
**Doc evidence:** `trust-model.html` §"Automatic revocation checking with CRL distribution points"; `doc-history.md` (2026-11-04). **Stop condition:** on any link-local/metadata/internal hit from fleet identity, STOP + preserve + disclose.
**Subagent note:** DNS-rebinding and fleet-DoS/amplification are the two priority sub-leads — the docs never state the resolved IP is *re-validated on each 30-min refresh* (vs. validated-once-then-cached), and state **no per-caller throttling** for the CDP-fetch subsystem. Both are doc-gaps requiring live confirmation, not provable from docs.

### Area 2 — Credential vending scope & trust-policy bypass (`CreateSession` core)
**Background.** `CreateSession(profileArn, roleArn, trustAnchorArn)` → AssumeRole. Authorization depends on: (a) cert chains to the CA of the *named* trust anchor; (b) role trust policy trusts `rolesanywhere.amazonaws.com` and its `Condition` (cert-attr tags and/or `aws:SourceArn=TA ARN`) is satisfied; (c) role is listed in the profile's `roleArns`.
**Security Concern.** Can the three identifiers be mixed across tenants/anchors, or the trust `Condition` be defeated?
**High-level Test Scenarios:**
- `[SETTLED — negative]` `trustAnchorArn` is cryptographically bound to the signing CA: attacker cert + victim's TA ARN → `403 Untrusted signing certificate`. `aws:SourceArn` reflects the *real* TA and cannot be spoofed; STS enforces the role-trust condition. Confused-deputy mitigation is real.
- `[SETTLED — negative]` Cross-account vend blocked at **two** layers: `CreateProfile` ("Cross-account pass role is not allowed") and `CreateSession` (`400` "different account ID").
- **Still open:** mismatched-but-same-account triples — `profileArn` of profile P (lists role R1) with `roleArn`=R2 (not in P). **Oracle:** does CreateSession enforce `roleArn ∈ profile.roleArns`, or vend R2? **Severity: High (intra-account privilege broadening) if it vends.**
- **Still open:** `durationSeconds` interplay — request a duration > role `MaxSessionDuration` but ≤ profile; confirm it errors (documented) rather than silently clamps to a longer-than-intended window. **Severity: Low.**
**Doc evidence:** `authentication-create-session.html`; `trust-model.html` §Trust policy. **Reuse** `/work/ra/createsession.py`.

### Area 3 — Attribute-mapping / PrincipalTag / SourceIdentity integrity
**Background.** The profile's `attributeMappings` decide which cert RDN/SAN values become `aws:PrincipalTag/x509*`. Trust-policy conditions key on those tags. Multi-valued RDNs are concatenated with `/`; SAN maps only the **first** DNS/DN/URI value.
**Security Concern.** Caller controls the *cert contents*; the customer controls the *mapping* and the *trust policy*. Breaches: forge a tag the policy trusts, or exploit the documented drop-tag semantics.
**High-level Test Scenarios:**
- `[SETTLED — negative]` Mappings are confined to `x509{Subject,Issuer,SAN}`; `certificateField` is an enum and `specifier` is validated. Cannot populate a foreign/arbitrary ABAC key or set arbitrary `sts:SourceIdentity`.
- **Open / documented fail-open (Lens S/U):** when the mapping drops a field, a `StringNotEquals` condition on that `x509*` tag evaluates **`true`** (condition "disregarded when the principal tag is dropped") — a `DeleteAttributeMapping` by an operator can silently flip a deny-list condition to allow. **Oracle:** profile with no `x509Issuer/CN` mapping + a role trust using `StringNotEquals aws:PrincipalTag/x509Issuer/CN` → assume succeeds for any issuer. **Severity: Medium (customer-authored, but AWS-documented footgun worth a hardening note).**
- **Open:** multi-value concatenation (`OU=Security/Engineering/Research`) and `/`-containing RDN values — can a crafted RDN value inject a `/` to **spoof a different composite tag** a policy matches? SAN "first value only" — can ordering hide a value a policy expects? **Oracle:** cert with adversarial RDN ordering/`/` content vs a `StringEquals` policy. **Severity: Medium.**
- **Open:** Subject CN length edge cases driving `sts:SourceIdentity` prefix rules (`CN=` ≤61; `""` 62–256; `ID=` when CN absent, zero-padded even hex of serial; >256 fails). Boundary/`ID=` collisions as a `sts:SourceIdentity` condition bypass. **Severity: Low–Medium.**
**Doc evidence:** `attribute-mapping-and-trust-policy.html`, `trust-model.html` §Source identity rules, `workload-identities.html`.

### Area 4 — [NEW] `AWS4-X509` signature coverage + ML-DSA / X.509 / CRL parser surface
**Background.** `CreateSession` uses a custom SigV4-variant. CloudTrail `additionalEventData` records `missingSignedHeaders`, `postEmptyBody`, `algorithmMismatch` — and the object **appears only on *successfully authenticated* requests**, i.e. these non-conformances do **not** by themselves reject the request.
**Security Concern (Lens Y / F / BB).**
- **Signature coverage gap:** RA "checks `host` on every request and checks the other four [`x-amz-x509`, `x-amz-x509-chain`, `x-amz-date`, `content-type`] **only when they appear**." A header left out of `SignedHeaders` is merely *logged* in `missingSignedHeaders`, not rejected — and `additionalEventData` (hence `missingSignedHeaders`) is emitted **only for requests that authenticated successfully**, so the doc's own worked example showing populated `missingSignedHeaders` on a success path is a **documentary admission that unsigned-but-present security headers do not block authentication**. The "`x-amz-x509` MUST be signed" language lives only in `authentication-sign-process.html`'s canonical-request instructions for a *conforming client* — not as a server-side rejection rule. **Claim:** the presented identity (**`x-amz-x509` / `x-amz-x509-chain`**) can be delivered unsigned, letting a MITM/proxy swap the certificate or chain while the signature still validates → the swapped cert's serial becomes `Credential` and changes attribution/vended identity. **Oracle:** craft a request where `x-amz-x509` is present but excluded from `SignedHeaders`; does it authenticate (201) or reject? If it authenticates, test substituting the cert bytes. **Severity: High–Critical (identity substitution) / else Low.** *Confirm whether cert content is independently bound to the signature via another channel — doc text does not rule out the gap.*
- **`postEmptyBody` / query-vs-body divergence (Lens BB):** POST + non-empty query string + empty body "exercises a canonicalization code path that does not conform to the SigV4 specification," and a client "sends CreateSession parameters in the query string instead of the JSON body." **Claim:** when `profileArn`/`roleArn`/`trustAnchorArn` appear in **both** query and body, the *signed* set differs from the *executed* set (param smuggling) → vend against a trust anchor/role the signature didn't cover. **Oracle:** sign over query params but place different ARNs in the body (or vice-versa); observe which triple is used for the vend vs the signature. **Severity: High if divergence vends.**
- **ML-DSA parser (Lens F):** post-quantum algorithms `AWS4-X509-MLDSA` / `ML-DSA-44/65/87`, **added 2026-02-27** (`doc-history.md`) — a fresh native PQC parser fed an attacker-controlled cert + signature blob. **Claim:** malformed ML-DSA public keys/signatures (bad lengths, truncated, oversized, wrong-level) trigger a parser crash / resource exhaustion, or an **algorithm-confusion/downgrade** (declare `MLDSA` with a classical/EC key, or a weaker ML-DSA level than the key). `algorithmMismatch` is documented as a *detection* field ("specifies whether … the declared algorithm implies a key type that does not match the certificate's public key") that appears **only on successfully authenticated requests** — it is **not stated to hard-reject**. **Oracle:** a single successful `CreateSession` CloudTrail event with `algorithmMismatch:true` **refutes** "mismatch = hard reject" (= verification-bypass lead); separately, crafted blobs → 5xx / latency / inconsistent accept. **Severity: Medium (crash) → High (verification bypass).**
- **X.509 / chain / CRL DER parser:** deeply-nested/oversized/odd-serial (negative, huge, zero) certs; empty-subject certs (documented **not supported** — confirm clean reject, not crash); malformed uploaded CA bundle; **`ImportCrl` `crlData` is capped at 300,000 bytes** (≈293 KB — *not* the 1 MB cap, which applies only to CDP-fetched CRLs), must parse as a PEM X.509 CRL, no indirect-CRL support → bounded-size CRL-parser robustness surface; and the chain in `X-Amz-X509-Chain`. **Severity: Medium (parser DoS); Low unless cross-tenant.**
**Doc evidence:** `authentication-sign-process.html`, `logging-using-cloudtrail.html` §additionalEventData, `authentication-create-session.html`. **Reuse/extend** `/work/ra/createsession.py`, `/work/ra/certs.py`.

### Area 5 — AWS-managed-policy audit & intra-account privilege escalation (Lens R/S)
**Background.** Three shipped, uneditable artifacts.
- `AWSRolesAnywhereFullAccess` (v3): `Sid PassRoleToRolesAnywhere` → `iam:PassRole` on **`Resource:"*"`** gated only by `iam:PassedToService=rolesanywhere.amazonaws.com`; `Sid OtherRolesAnywherePermissions` → `PutAttributeMapping`, `TagResource`, `PutNotificationSettings`, etc. on **`Resource:"*"`**.
- `AWSRolesAnywhereServicePolicy` (SLR): `acm-pca:GetCertificateAuthorityCertificate` + `DescribeCertificateAuthority` on **`arn:aws:acm-pca:*:*:*`** (all PCAs), and `cloudwatch:PutMetricData` (namespace-scoped — fine).
- `AWSRolesAnywhereReadOnly` (v3): `ListTagsForResource` on `Resource:"*"`.
**Security Concern.** The `PassRole Resource:*` + `CreateTrustAnchor` + `CreateProfile` combination = **AssumeRole-equivalent for any role in the account that trusts `rolesanywhere.amazonaws.com`** (standard PassRole→compute escalation, RA as the consuming service). This is an **AWS-authored artifact a customer attaches verbatim** → in scope, Tier-2 reportable, not a customer footgun.
**High-level Test Scenarios:**
- `[SETTLED mechanism]` A principal holding **only** `AWSRolesAnywhereFullAccess` can create a TA (attacker CA), create a profile passing a victim role that trusts the RA service principal, then `CreateSession` to obtain that role's creds — escalating to whatever that role holds.
- **Confirm the artifact defect precisely** under a scoped role holding *only* the managed policy using `iam:SimulatePrincipalPolicy` first (no resources touched), then a live canary assume. **Oracle:** scoped holder vends creds for a role it was never granted `sts:AssumeRole` on directly.
- **SLR over-reach:** does the SLR's `acm-pca:*:*:*` let the RA service read/describe PCAs unrelated to any trust anchor? Note as least-privilege gap (`Describe/GetCertificateAuthorityCertificate` only — low data value). **Severity: non-admin→role-reach = High; SLR breadth = Low–Medium.**
**Doc evidence:** the three `aws-managed-policy` reference pages; `security-iam-awsmanpol.html`.

### Area 6 — Revocation completeness, disable lifecycle & audit attribution
**Background.** Revocation = imported CRLs and/or automatic CDP. Session attribution rides `roleSessionName` (default = cert serial).
**High-level Test Scenarios:**
- `[SETTLED]` **CRL is per-trust-anchor, NOT per-CA:** the same CA registered as two trust anchors → a CRL imported on TA-1 does **not** block the cert presented via TA-2. **Severity: Medium (revocation-completeness footgun).**
- `[SETTLED]` TA/profile disable and CRL revocation take effect immediately (<1.5 s) — no usable TOCTOU.
- **Open (Lens AA/U):** **imported CRLs: "IAM Roles Anywhere does not check the expiration date of a CRL that you import … continues to use an imported CRL … even after `nextUpdate` has passed"** → a stale imported CRL silently diverges from CA state (can keep *un-revoking* nothing, but also means a newly-revoked cert stays valid until re-import). Contrast with automatic CDP which *does* honor `nextUpdate`/fail-closed. **Oracle:** import CRL, revoke a cert at CA, don't re-import → cert still vends. **Severity: Medium.**
- **Open (Lens O — audit evasion):** profile `acceptRoleSessionName=true` lets the caller set an **arbitrary `roleSessionName`**, replacing the traceable cert serial in the assumed-role ARN/CloudTrail → impersonate another workload's session name in logs. Also: `additionalEventData` is **omitted on rejected auths** (failed CreateSession leaves a thinner record); infra headers (`X-Forwarded-For`, `X-Amzn-Trace-Id`) are explicitly **not** signature-evaluated. **Oracle:** vend with a chosen session name; inspect CloudTrail attribution. **Severity: Low–Informational.**
- **Open:** `UpdateTrustAnchor` validity-period re-registration ("honors certificates based on the validity period found during the most recent Create/Update event") — can a validity-window change create a revocation/expiry blind spot? **Severity: Low.**
**Doc evidence:** `trust-model.html` §Revocation + §Imported CRLs; `authentication-create-session.html` (roleSessionName); `logging-using-cloudtrail.html`.

### Area 7 — Undocumented knobs & VPCe-policy ordering
**Background / Scenarios:**
- **`sourceType=SELF_SIGNED_REPOSITORY`** — accepted by the API (`API_Source`) but absent from prose/console. **Claim:** it enables a trust-anchor mode with weaker/different validation (e.g. self-signed EE directly, no CA chain). **Oracle:** `CreateTrustAnchor` with this type; characterize what certs it then trusts and whether chain/signature checks weaken. **Severity: unknown → High if it relaxes signature/chain validation.**
- **`requireInstanceProperties`** ("Unused, saved for future use") — set `true` on a profile; observe whether it changes `CreateSession` validation or errors. **Severity: Low (surface characterization).**
- **VPCe `CreateSession` policy "evaluated *before* the certificate-based authentication is complete"** and uses `rolesanywhere:x509*` condition keys that are **attacker-chosen cert strings** (same spoofability as trust-policy conditions lacking `aws:SourceArn`). **Claim:** a VPCe policy relying on `rolesanywhere:x509Subject/CN` is defeatable by an attacker simply issuing a cert with that CN (from any CA chaining to an allowed TA). **Oracle:** VPCe policy allowing CN=Bob; present a cert with CN=Bob from an attacker-controlled-but-trusted CA. **Severity: Medium (defense-in-depth bypass; needs the attacker already inside the VPC + a trusted TA).**
- **Deprecated `sessionName` body param** vs `roleSessionName` — twin-parameter parity (Lens X): does the legacy field still influence the session name / bypass `acceptRoleSessionName=false`? **Severity: Low.**

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| SSRF to internal/metadata via cert CDP | CDP auto-revocation fetch | "host name resolves to public IP addresses"; no redirects; port 80/443; fail-closed |
| Reflected/amplified fleet DoS | CDP fetch | ≤5 URLs, ≤1 MB, ≤2048-char URL, 30-min refresh |
| Cross-account / cross-TA vend | CreateSession→AssumeRole | TA↔CA crypto binding; `aws:SourceArn`; two-layer cross-acct block `[SETTLED]` |
| Trust-policy condition bypass | attribute mapping + role trust | mapping enum-validated; `aws:SourceArn` strongly recommended; drop-tag semantics documented |
| Unsigned-header / param-smuggling auth | AWS4-X509 signing | `host` always checked; `additionalEventData` audit flags (logging, not rejection) |
| ML-DSA / X.509 / CRL parser abuse | signature + cert + CRL parsers | X.509v3 constraints; SHA256+; MD5/SHA1 rejected; empty-subject unsupported |
| Intra-account privesc via managed policy | AWSRolesAnywhereFullAccess | `iam:PassedToService` condition (but `Resource:*`) |
| Stale/partial revocation | imported CRL vs CDP | per-TA CRL scope; imported-CRL `nextUpdate` not checked `[SETTLED/doc]` |
| Audit attribution forgery | roleSessionName | default = cert serial; `acceptRoleSessionName=false` default |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Customer PKI hygiene** — RA holds no private keys; key compromise on customer hosts, weak CA issuance policy, and a customer choosing *not* to use `aws:SourceArn`/attribute conditions are **customer footguns**, not RA defects. (The `x509Subject/Issuer/SAN` trust conditions are attacker-chosen strings and are worthless without `aws:SourceArn` — this matches AWS's own "strongly recommended" guidance. `[SETTLED]`)
- **Shared STS / IAM control plane** — behavior of `AssumeRole` itself, STS quotas, IMDS on managed hosts.
- **Cross-account resource access** — resource-based policies are **not supported** (`security_iam_service-with-iam.html`); cross-acct vend blocked `[SETTLED]`.
- **Single-tenant self-DoS** (hitting your own CreateSession quota), product/feature-parity gaps, and the non-deletable `subject` audit record (synthetic-CN only, inert) `[SETTLED]`.
- **DNS rebinding against private-only endpoints** is out — but DNS rebinding of the **CDP fetch** (Area 1) is firmly **in scope** because the fleet is the resolver/fetcher.

---

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens H (KMS / encryption-context):** N/A. Read `data-protection.html`, `trust-model.html`, `CreateTrustAnchor`/`CreateProfile` API — RA stores no customer data at rest and holds no private keys; no CMK/branch-key/encryption-context surface.
- **Lens K (prompt injection):** N/A — no LLM/agent anywhere in the service (read introduction, trust-model, workload-identities).
- **Lens J (OAuth/3P):** N/A — no 3P OAuth linking; identity is X.509 only.
- **Lens W (attestation):** N/A — no Nitro/enclave attestation gate.
- **Lens T (cross-service secret reachability):** N/A — no generated-and-persisted secret (vended STS creds are ephemeral, returned to caller only).
- **Lens A cross-tenant IDOR:** largely null — all resources account-scoped UUID ARNs; `ListSubjects` account-scoped `[SETTLED]`. Residual low-value check: cross-account `Get{TrustAnchor,Profile,Crl,Subject}` by ARN should return AccessDenied/NotFound (confirm no existence oracle).
- **Lens DD (cache vs authz):** only caching is the CDP CRL 30-min refresh (revocation staleness, folded into Area 6) — not an authz-decision cache.
- **Doc gaps to confirm on a live account first:** `ImportCrl` max CRL size and parse limits (not stated); exact behavior of `SELF_SIGNED_REPOSITORY`; whether `missingSignedHeaders` non-conformance rejects vs only logs (Area 4 hinges on this); whether `CreateSession` enforces `roleArn ∈ profile.roleArns` (Area 2). Mark these **"doc-gap — confirm surface first."**

---
*Prior-run reuse:* `/work/ra/createsession.py` (AWS4-X509-RSA-SHA256 signer), `/work/ra/certs.py` (CA+EE gen), `/work/ra/poll.py` (TOCTOU poller). Run a positive control before any crux test. The Go `aws_signing_helper` could not be installed offline — the Python signer is authoritative here.
