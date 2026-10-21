# EC2 CreateKeyPair — Attack Research Plan

Source of leads: `API_CreateKeyPair.html` + `API_ImportKeyPair.html` + `API_DeleteKeyPair.html` + `API_DescribeKeyPairs.html` + `API_KeyPairInfo.html` (EC2 API Reference); `ec2-key-pairs.html` + `create-key-pairs.html` (EC2 User Guide); `aws-resource-ec2-keypair.html` (CloudFormation); EC2 Service Authorization Reference (`list_ec2.md` offline mirror); SSM Parameter Store + KMS `services-parameter-store` docs. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the SSM↔KMS delegation internals, an AWS-fleet role), stop, preserve evidence, flag for AWS-Security disclosure. This plan is almost entirely *customer-plane* — the one service-plane-adjacent item is the `aws/ssm` managed-key delegation (Area 2, Claim 2.2).
- Oracle discipline carried from the corpus: **`DryRunOperation` is caller-IAM-only, NOT an ownership oracle** — several leads below use DryRun to prove a *condition-key* is inert, which is valid; do not use it to infer resource ownership.

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Recover a private key the origin API says is unrecoverable** — read cleartext `keyMaterial` for a CFN-created key pair without ever holding `ec2:CreateKeyPair`/`ec2:DescribeKeyPairs` (cross-service secret-reachability wall bypass).
2. **One-call mass key exfiltration** — dump every CFN-issued EC2 private key in an account/Region in a single request, overriding per-parameter IAM Deny.
3. **Defeat an org key-governance control** — create/import a key that violates an intended "ed25519-only" / naming / format guardrail the policy author believed was enforced.
4. **ABAC self-widen** — mint a key tagged so a later `aws:ResourceTag` Deny (e.g. protecting "production" keys from deletion) does not apply.
5. **Key-substitution persistence** — plant attacker-chosen material at the deterministic `/ec2/keypair/{id}` path that downstream tooling will later trust.
6. **Kill chain** — convert any recovered private key into instance compromise (SSH / Windows admin-password decrypt) and onward to the instance role's IMDS credentials.

---

## 2. Components, Assets, and Design

**Customer-facing interface:** EC2 Query/JSON API `CreateKeyPair` (SigV4, `ec2.<region>.amazonaws.com`), plus twins `ImportKeyPair`, `DeleteKeyPair`, `DescribeKeyPairs`; console "Key Pairs"; CloudFormation `AWS::EC2::KeyPair`.

**What a "key pair" is:**
- Public key — stored by EC2, placed in instance `~/.ssh/authorized_keys` at first boot (Linux) or used to encrypt the Windows admin password.
- Private key `keyMaterial` — returned **unencrypted, exactly once**, in the `CreateKeyPair` response (PKCS#1 PEM, or PPK for PuTTY). EC2 asserts it keeps **no copy**.
- Identifiers: `keyName` (≤255 ASCII, unique per account+Region), `keyPairId` (`key-` + 17 hex), `keyFingerprint`.
- ARN (IAM): `arn:${Partition}:ec2:${Region}:${Account}:key-pair/${KeyPairName}` — **name-keyed only; there is no `key-pair/${KeyPairId}` ARN form.**

**Accounts/zones:** single customer account+Region (no multi-tenant service fleet is exposed here). The notable cross-zone seam is **cross-service**, not cross-account: EC2 ↔ SSM Parameter Store ↔ KMS (`aws/ssm` default key).

**Where untrusted data enters / where secrets come to rest:**
- `KeyName`, `KeyType` (`rsa|ed25519`), `KeyFormat` (`pem|ppk`), `TagSpecification` → CreateKeyPair.
- `PublicKeyMaterial` (base64, attacker-chosen) → ImportKeyPair.
- **CFN path:** generated private key is persisted to SSM at `/ec2/keypair/{key_pair_id}` as a **SecureString** under the **`aws/ssm` AWS-managed KMS key**. Deleted only when CFN deletes the key pair *and* the deleting principal holds `ssm:DeleteParameter`.

```
                         ┌──────────────────────────────────────────┐
  CreateKeyPair ─────────┤ EC2 control plane: stores PUBLIC key only │
     (direct API)        │ returns PRIVATE key ONCE (keyMaterial)    │  "EC2 keeps no copy"
                         └──────────────────────────────────────────┘
                                         │ (CloudFormation path only)
                                         ▼
          AWS::EC2::KeyPair  ──►  SSM Parameter Store  /ec2/keypair/{key_pair_id}  (SecureString)
                                         │ encrypted under  alias/aws/ssm  (AWS-managed CMK, uneditable key policy)
                                         ▼
     ssm:GetParameter --with-decryption  /  ssm:GetParametersByPath --recursive   ◄── SECRET-REACHABILITY WALL BYPASS
                                         │
                                         ▼
                    PRIVATE KEY (cleartext PEM) ──► SSH to instance / decrypt Windows admin pw ──► IMDS instance-role creds
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal denied all `ec2:*KeyPair*` | CFN-created private key | `ssm:GetParameter` / `GetParametersByPath` on `/ec2/keypair/*` | Returning cleartext PEM for a key the caller's EC2 IAM forbids = **wall bypass (High)** |
| Principal with broad `ssm:GetParameter*` (CI/automation) | **every** CFN key in Region | `GetParametersByPath(/ec2/keypair, Recursive, WithDecryption)` | One response enumerating ≥1 foreign-created private key, incl. any under explicit per-param Deny = **Critical** |
| Policy author's "ed25519-only" intent | actual key material created | `ImportKeyPair` (no `ec2:KeyPairType` key) | An RSA/1024-bit key exists under a policy that only type-gated `CreateKeyPair` = **governance bypass (Med-High)** |
| Low-priv creator | later ABAC Deny on `aws:ResourceTag` | self-chosen `TagSpecification` at create | A key the creator tagged to dodge a production-protection Deny = **ABAC self-widen (Low-Med)** |
| Attacker with `ssm:PutParameter` | downstream key consumers | `PutParameter Overwrite` at `/ec2/keypair/{id}` under attacker KMS key | Tooling later fetches attacker-planted material as "the" key = **key-substitution persistence (Med/High-chained)** |
| Any holder of `ec2:DescribeKeyPairs` | all key metadata in Region | Describe has no resource-level perms | Enumerating every key's name/id/fingerprint/public key regardless of tags/owner = **recon (Med)** |
| Recovered private key | EC2 instance / instance role | SSH / `GetPasswordData` decrypt → IMDS | Shell on instance + STS creds from IMDS = **end-of-chain (Critical)** |

---

## 4. API / Interface Inventory

| Name | Method | New/Exist | Mutating | Int/Ext | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| CreateKeyPair | POST/Query | Existing | **Yes** | External | Generate RSA-2048/ed25519 keypair, return private key once | Yes (SigV4) | holder of `ec2:CreateKeyPair` | cond keys: `aws:RequestTag`,`aws:TagKeys`,`ec2:KeyPairType`,`ec2:Region` — **no KeyName/KeyFormat key** |
| ImportKeyPair | POST/Query | Existing | Yes | External | Upload attacker-chosen public key | Yes | `ec2:ImportKeyPair` | **no `ec2:KeyPairType` key** → type-restriction bypass twin; accepts 1024-bit RSA |
| DeleteKeyPair | POST/Query | Existing | Yes | External | Remove public key (by name OR id) | Yes | `ec2:DeleteKeyPair` | cond keys incl. `ec2:KeyPairName`,`aws:ResourceTag` — richer than Create (Lens X asymmetry) |
| DescribeKeyPairs | GET/Query | Existing | No | External | List names/ids/fingerprints; `IncludePublicKey`; filters incl. `fingerprint` | Yes | `ec2:DescribeKeyPairs` | **no resource-level perms** → Region-wide all-or-nothing recon; supplies `keyPairId` for SSM path |
| ssm:GetParameter / GetParametersByPath | — | Existing (adjacent) | No | External | Read `/ec2/keypair/{id}` SecureString | Yes | holder of `ssm:GetParameter*` | the secret-reachability bypass; recursive path read overrides per-param Deny |
| ssm:PutParameter | — | adjacent | Yes | External | Overwrite `/ec2/keypair/{id}` | Yes | holder of `ssm:PutParameter` | key-substitution / re-encrypt under attacker key |
| AWS::EC2::KeyPair (CFN) | — | Existing | Yes | External | Create key + write private key to SSM | via CFN | CFN role | needs only `ssm:PutParameter`+`ssm:DeleteParameter` — **no EC2 action gates SSM read** |

Undocumented/console-hidden knob sweep: `KeyFormat=ppk` and `KeyType` are API enums with **no corresponding IAM condition key for format**; `ImportKeyPair` silently accepts 1024-bit RSA (create path cannot). No `authorizerType`-style hidden auth knob here.

---

## 5. Recommended Areas of Focus

### Area 1 — Cross-service private-key reachability (Lens T) — **TOP PRIORITY**
**Background:** CFN-created key pairs persist the generated private key to SSM `/ec2/keypair/{key_pair_id}` (SecureString, `aws/ssm` key). The required IAM for the CFN path is only `ssm:PutParameter`/`ssm:DeleteParameter` — **no EC2 action gates read of the stored secret.**
**Security Concern:** the origin-service access wall (`ec2:*KeyPair*`) is irrelevant to the storage-service read path (`ssm:GetParameter`). A security review that audited only EC2 key-pair permissions for private-key exposure misses this entirely.
**High-level Test Scenarios:**
- **Claim 1.1 (wall bypass):** A principal *explicitly denied* `ec2:CreateKeyPair`+`ec2:DescribeKeyPairs` but holding `ssm:GetParameter` on `arn:aws:ssm:<r>:<a>:parameter/ec2/keypair/*` recovers the cleartext PEM. → **Oracle:** `aws ssm get-parameter --name /ec2/keypair/<id> --with-decryption` returns `-----BEGIN ... PRIVATE KEY-----`. Precondition: know/derive one `keyPairId`. Severity: **High.**
- **Claim 1.2 (one-call mass dump — CRITICAL):** `GetParametersByPath(Path="/ec2/keypair", Recursive=true, WithDecryption=true)` returns *every* stored private key in the Region, and per SSM docs the recursive read **overrides an explicit per-parameter Deny** on an individual `/ec2/keypair/{id}`. → **Oracle:** single response containing ≥1 key the caller never created, including one under a targeted Deny. Precondition: `ssm:GetParametersByPath` covering the `/ec2`/`/ec2/keypair` prefix (common in CI/deploy roles). Severity: **Critical.**
- **Claim 1.3 (deterministic path):** `keyPairId` from `ec2:DescribeKeyPairs --query KeyPairs[*].KeyPairId` fully determines the SSM path → no guessing needed. **Oracle:** path built from Describe output reads successfully.
- **Claim 1.4 (orphan/outlives key):** if `ssm:DeleteParameter` was denied at stack-delete, the SecureString (and up to 100 historical versions) survives the key pair's deletion → stale recoverable private key. **Oracle:** delete stack without `ssm:DeleteParameter`, re-read old path, still get PEM.
Doc evidence: `create-key-pairs.html#create-key-pair-cloudformation`; `aws-resource-ec2-keypair.html`; SSM `API_GetParametersByPath`. Severity-if-true: **Critical.**

### Area 2 — KMS decrypt delegation & encryption-context (Lens H / service-plane edge)
**Background:** SecureString decrypt requires `kms:Decrypt`, but the `aws/ssm` default key's key policy is AWS-fixed and **cannot be tightened by the customer** ("you cannot establish access control policies for the default `aws/ssm` KMS key").
**Security Concern:** protection for this secret collapses to "whatever `kms:Decrypt` grants already exist" — routinely audited for CMKs, rarely for the free default key. Broad `kms:Decrypt` on `Resource:*` (common in legacy/PowerUser policies) silently satisfies it.
**High-level Test Scenarios:**
- **Claim 2.1:** `ssm:GetParameter --with-decryption` with **no** `kms:Decrypt` anywhere fails (fail-closed) → confirm the documented requirement holds. **Oracle:** `AccessDeniedException`/KMS error. If it *succeeds*, that refutes the model = Critical + **HARD STOP** (service-plane delegation defect).
- **Claim 2.2 (service-plane edge — doc-gap):** the exact SSM→KMS authorization primitive for the `aws/ssm` key (grant vs `kms:ViaService` vs root-policy inheritance) is undocumented. Probe only to the point of confirming delegation shape; **do not** exercise AWS-fleet identity. 
- **Claim 2.3 (encryption-context):** ciphertext is bound to `PARAMETER_ARN` encryption context → cross-parameter ciphertext substitution fails decryption (likely a genuine null — record as negative).
Doc evidence: `kms/.../services-parameter-store.html`. Severity-if-true: Medium-High (audit blind spot); service-plane surprise = Critical/hard-stop.

### Area 3 — Documented-guarantee vs enforcement: the "no copy" contradiction (Lens U)
**Background:** `ec2-key-pairs.html` states **"Because Amazon EC2 doesn't keep a copy of your private key, there is no way to recover a private key if you lose it."** True narrowly for the direct API — but the CFN path deposits a durable cleartext copy in SSM.
**Security Concern:** a customer compliance control attesting "no durable copy of EC2 private keys exists" is **provably false for every CFN-created key**, and nothing in EC2's own security framing flags SSM `/ec2/keypair/*` as in-scope. A data-classification sweep filtering "EC2 outputs" never checks SSM.
**High-level Test Scenarios:** enumerate `ssm:DescribeParameters --parameter-filters Key=Name,Option=BeginsWith,Values=/ec2/keypair` (metadata-only, silent) → count of stored keys a "no copy" control claims cannot exist. Severity-if-true: Medium-High (false-attestation / compliance), AWS-owned doc defect.

### Area 4 — Key-governance condition-key gaps (Lens S / I)
**Background:** `CreateKeyPair` supports only `aws:RequestTag`, `aws:TagKeys`, `ec2:KeyPairType`, `ec2:Region`.
**Security Concern:** several intuitive guardrails are **not IAM-expressible**:
- **Claim 4.1:** No `ec2:KeyPairName` on Create/Import → "key names must match `teamX-*`" is unenforceable at creation. **Oracle:** policy `StringLike ec2:KeyPairName teamX-*` on `CreateKeyPair`; DryRun `CreateKeyPair(KeyName="prod-admin")` returns `DryRunOperation` (condition inert). Severity: Medium.
- **Claim 4.2:** No condition key for `KeyFormat` at all → cannot forbid PPK output. Severity: Low-Medium.
- **Claim 4.3 (fail-open tagging):** `CreateKeyPair` with no `TagSpecification` succeeds even under tag-intent policies unless `aws:RequestTag`/`aws:TagKeys` (with `ForAnyValue`) is on the Create statement itself. **Oracle:** create untagged under a `CreateTags`-gated-by-`ec2:CreateAction` policy → succeeds. Severity: Medium (inventory/ABAC gap).
- **Claim 4.4 (ABAC self-widen):** creator chooses `TagSpecification` values → can self-tag a new key `environment=dev` to dodge a `Deny ec2:DeleteKeyPair` on `aws:ResourceTag/environment=production`, unless `aws:RequestTag` pins values. Severity: Low-Medium.
Doc evidence: EC2 Service Authorization Reference; `supported-iam-actions-tagging.html`. 

### Area 5 — Twin/legacy parity: Import bypasses Create's type gate (Lens X)
**Background:** condition-key asymmetry across the family — `ImportKeyPair` has **no `ec2:KeyPairType`**; `DeleteKeyPair` has a *richer* key set (`ec2:KeyPairName`, `aws:ResourceTag`, `ec2:KeyPairType`) than `CreateKeyPair`.
**Security Concern:**
- **Claim 5.1 (type-gate bypass):** A policy `Allow CreateKeyPair if ec2:KeyPairType=ed25519` + `Allow ImportKeyPair` (the natural "generate only ed25519, but imports allowed" posture) places **no type constraint on imported material** — attacker imports RSA, including **weak 1024-bit RSA** (import accepts 1024/2048/4096; create cannot). **Oracle:** `ImportKeyPair` with 1024-bit RSA `PublicKeyMaterial` under that policy → `DryRunOperation`/success. Severity: **Medium-High** for "ed25519/strong-key-only" orgs; only mitigation is denying `ImportKeyPair` or post-hoc Config detection.
- **Claim 5.2 (crypto-weakness):** independent of IAM, `ImportKeyPair` accepting 1024-bit RSA is a weak-key surface with no native guardrail. Severity: Medium.
Doc evidence: `create-key-pairs.html` key requirements; Service Authorization Reference per-action tables.

### Area 6 — DescribeKeyPairs enumeration & disclosure (Lens A recon)
**Background:** Describe has **no resource-level permissions** — only `ec2:Region`.
**Security Concern:** any holder of `ec2:DescribeKeyPairs` sees **every** key pair in the Region (name, `keyPairId`, fingerprint; public key via `IncludePublicKey`), ungated by tag/owner. You cannot build "team A sees only its keys." Combined with Area 1, Describe is the `keyPairId` feeder for the SSM path. Filters support `fingerprint` and wildcard `key-name` → enumeration oracle. Severity: Medium (recon enabler; High as Area-1 precondition).

### Area 7 — Key-substitution / re-encryption persistence (Lens T write-side / EE)
**Background:** `ssm:PutParameter Overwrite=true` with a caller-chosen `KeyId` can overwrite `/ec2/keypair/{id}` under an attacker-controlled CMK, with no cross-check against the original key/value/EC2 state.
**Security Concern:** attacker with `ssm:PutParameter` on the path (no `ec2:*` needed) plants a *different* private key that CFN/deploy tooling/runbooks later fetch and trust as "the" key for `key_pair_id X` — a supply-chain-style substitution enabled purely by the deterministic, EC2-correlated path name. **Oracle:** overwrite path under attacker CMK with no EC2 perms → succeeds; later consumer reads attacker material. Severity: Medium standalone / **High chained.**
**Intra-account name squatting (EE):** `keyName` namespace is per account+Region (no cross-account squatting — explicit null). But a low-priv principal can **race to claim** a predictable name (`prod-deploy-key`) before privileged automation; the only defense is the hard duplicate-name error (no silent overwrite). Doc-gap: AWS doesn't discuss this race.

### Area 8 — Audit-log evasion & info leak (Lens O)
**Background:** `keyMaterial` is returned in the API response; CFN's permission pre-check uses a **fabricated parameter name** that appears in `AccessDeniedException` messages.
**Security Concern / Scenarios:**
- **Claim 8.1:** confirm whether CloudTrail redacts `keyMaterial` from `responseElements` (expected redacted) and whether CLI/CloudShell history or `--output` files leak it — doc-gap, verify. 
- **Claim 8.2:** the fabricated-parameter-name in error messages is a minor info-leak / confusion oracle (Informational).
Severity: Low-Informational (enabler).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Recover "unrecoverable" private key via SSM | SSM `/ec2/keypair/*` | EC2 "keeps no copy" guarantee (Area 3) — bypassed by CFN storage |
| One-call dump of all Region private keys | `GetParametersByPath` recursive | per-parameter IAM Deny — explicitly overridden by recursive read |
| ed25519-only / strong-key policy | `ImportKeyPair` | `ec2:KeyPairType` on Create — absent on Import |
| Name-prefix / format governance | `CreateKeyPair` | `ec2:KeyPairName`/KeyFormat condition keys — don't exist for Create |
| Production-key deletion protection | `DeleteKeyPair` `aws:ResourceTag` | self-chosen create-time tag defeats it unless `aws:RequestTag` pins value |
| Per-team key visibility | `DescribeKeyPairs` | resource-level perms — unsupported, Region-wide |
| Trusted key substitution | `ssm:PutParameter` on path | none — Overwrite + arbitrary KeyId uncross-checked |
| Private key → instance → IMDS role | SSH / GetPasswordData / IMDS | key secrecy — defeated once Area 1 succeeds |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account key-pair access/squatting** — ARN is account+Region scoped; no shared namespace (explicit null, Area 7).
- **Encryption-context ciphertext substitution** across parameters — bound to `PARAMETER_ARN`, fails decrypt (likely genuine null).
- **Customer-authored** over-broad `ssm:GetParameter*`/`kms:Decrypt:*` policies — a customer footgun *unless* it's an AWS-published sample/managed policy (none identified for this surface). The AWS-owned defect here is the storage-choice + "no copy" guarantee, not the customer's grant breadth.
- Single-tenant self-DoS (5,000 keys/Region cap), IMDS on managed hosts, DNS-rebinding against private endpoints — out of scope.
- A user steering their own key lifecycle within their own permissions.

## 8. Null hypotheses / doc-gaps
- **Lens G/SSRF — N/A:** read `CreateKeyPair`, `ImportKeyPair`, `create-key-pairs.html`, `aws-resource-ec2-keypair.html`; no field the service dereferences/fetches server-side (`PublicKeyMaterial` is parsed, not fetched). 
- **Lens K/prompt-injection, Lens F/translation, Lens D-V/network, Lens W/attestation, Lens BB/CC/DD/FF — N/A:** no LLM, no wire-protocol translator, no multi-ENI/network fabric, no attestation gate, no multi-parser request path, no JWT/authorizer in this surface (checked the four API pages + both User Guide pages).
- **Lens Y/transport — N/A for this action** (standard SigV4 HTTPS; no documented cleartext/SigV2 path specific to key pairs).
- **Doc-gaps flagged:** (a) Service Authorization Reference descriptions for Create/Import are **stale** ("2048-bit RSA only", omit ed25519); (b) no doc states a guaranteed lifecycle binding between a `KeyPairId` and deletion of its `/ec2/keypair/{id}` SSM parameter (orphan risk unquantified); (c) SSM→KMS delegation primitive for `aws/ssm` undocumented; (d) intra-account KeyName race undocumented; (e) CloudTrail handling of `keyMaterial` unstated — confirm surface before relying.

---
### Kill chain (rate at end severity = Critical)
`ec2:DescribeInstances` (find instance + its `keyName`) → `ec2:DescribeKeyPairs` (`keyName`→`keyPairId`) → `ssm:GetParametersByPath /ec2/keypair --recursive --with-decryption` (private key, **no EC2 perm, overrides per-key Deny**) → SSH to Linux instance *or* `ec2:GetPasswordData` + private key → decrypt Windows admin password → on-box IMDSv2 → instance-role STS credentials → lateral movement. Entry primitive is a single coarse `ssm:GetParameter*` grant; end state is instance-role compromise.
