# EC2 Describe Key Pairs — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-keys.html` ("Describe your key pairs") fetched online 2026-10-15 (the `/work/aws-docs` offline mirror does not carry this UserGuide content page — only API_* stubs + sibling plans); authoritative IAM facts from `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` (`list_ec2.md`, 35,512 lines, fetched 2026-10-15) and `API_DescribeKeyPairs.html`. Status: documentation-derived hypotheses only; nothing tested against a live account.

**This plan is a PAGE-LEVEL DEEP-DIVE CHILD** of the key-pairs cluster hub `ec2-key-pairs-attack-research-plan.md` (which already consumes `describe-keys.md` as one of its sources) and a SIBLING of the create-side child `create-key-pairs-attack-research-plan.md`. It COMPLEMENTS, does not restate: it owns the **read / describe surface** of EC2 key pairs. It cross-references and explicitly defers the create-side crypto-floor/parser/CFN leads to the create sibling, and the private-key cross-service secret-reachability (Lens T, CFN→SSM) to the hub.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **Primary oracle for every lead here is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — a condition key either applies to an action or it does not; this is settleable read-only with zero resources created. Escalate to a scoped live `describe-key-pairs` call (canary key pairs in one account) only to confirm the account-wide read breadth.
- **`DryRunOperation` is caller-IAM only, NOT an ownership/scoping oracle** (evaluated before resource resolution) — do not use it to "prove" cross-key or cross-tenant reach. It is a false-positive trap here because `DescribeKeyPairs` has no resource-level permission anyway.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected on this page — key pairs are a same-account resource.)

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Read another team's key-pair inventory in the same account** that an admin intended to fence off — prove that `ec2:DescribeKeyPairs` cannot be scoped to a subset of key pairs, so any describe-holder enumerates every key pair's name, ID, type, fingerprint, creation time, and tags account-/Region-wide.
2. **Retrieve public key material** (`IncludePublicKey=true`) for key pairs an admin tried to withhold, and prove there is **no IAM condition key** that allows metadata-describe while denying material retrieval.
3. **Correlate a public key / fingerprint captured elsewhere** (a leaked `.pub`, an instance `authorized_keys`, a git commit) to a named key pair in the account via the `fingerprint`/`key-name` filters — an existence+name+provenance oracle.
4. **Mislead an SSH-access audit** that relies on the launch `KeyName` (via DescribeKeyPairs, DescribeInstances, or IMDS `public-keys/0`) — prove the reported key is the immutable *launch-time* record, not the *current* `authorized_keys`.
5. Confirm the **absence of a cross-account read path** (key pairs are not RAM-shareable, ARNs are account-scoped) — i.e. establish the realistic ceiling is **intra-account over-exposure (Medium)**, not cross-tenant (so hunters do not burn time hunting cross-account key-pair IDOR that cannot exist).

---

## 2. Components, Assets, and Design

The page documents three read sub-surfaces over the EC2 key-pair resource:

- **(a) Describe key pairs** — `aws ec2 describe-key-pairs` / `Get-EC2KeyPair` / console **Key Pairs** table. Returns per key pair: **KeyName, KeyPairId (`key-xxxxxxxx`), KeyType (rsa|ed25519), KeyFingerprint, CreateTime (UTC), Tags**, and — only when `IncludePublicKey=true` — **PublicKey (full material)**.
- **(b) Retrieve public key material** — four paths: `describe-key-pairs --include-public-key` (control-plane), `ssh-keygen -y -f key.pem` / PuTTYgen (local, from the *private* key — out of band, not a service call), and **IMDS** `GET http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key` via **IMDSv2 (token) and IMDSv1 (tokenless)**.
- **(c) Identify public key specified at launch** — `aws ec2 describe-instances --query "…KeyName"` / `Get-EC2Instance`. The page states: *"The public key name reported for an instance does not change, even if you change the public key on the instance or add public keys."*

**Resource & identifier shape.** Key-pair ARN = `arn:${Partition}:ec2:${Region}:${Account}:key-pair/${KeyPairName}` (name-keyed) with a parallel opaque ID `key-xxxxxxxx` (`KeyPairId`). Both the name and ID are account-scoped; **there is no RAM share, no `launchPermission`, no cross-account exposure of a key pair.** The fingerprint is SHA-1 of the DER-encoded private key for EC2-created RSA keys, and MD5 of the public key for imported keys (provenance differential — see create/verify siblings).

**Identity.** All three paths are SigV4 IAM (control plane) except the IMDS path, which is unauthenticated instance-local HTTP (gated only by IMDSv1/v2 posture + hop limit).

```
                         ec2:DescribeKeyPairs  (ec2:Region ONLY — unscopable)
   caller identity ───────────────────────────────────────────────► key-pair inventory
     (any describe-holder)        + IncludePublicKey=true (no IAM lever)   name/id/type/
                                  + Filter: key-name|fingerprint|tag       fingerprint/time/
                                                                           tags/PUBLIC KEY

   caller identity ── ec2:DescribeInstances (ec2:Region ONLY) ──► Instance.KeyName (launch, immutable)

   anything on instance ── IMDSv1/v2 /meta-data/public-keys/0/openssh-key ──► launch public key
     (incl. SSRF via IMDSv1)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv principal in account A (has `ec2:DescribeKeyPairs`) | Every key pair in account A / this Region | `DescribeKeyPairs` (no resource-level perm) | **Reading name/id/type/fingerprint/tags/public-key of a key pair the admin intended to fence from this principal is the breach** (intra-account over-exposure — the ceiling, since no cross-account path exists). |
| Same principal, metadata-only intent | Public key *material* of all key pairs | `IncludePublicKey=true` | **Material returned despite a policy author's attempt to withhold it = enforcement gap** (there is no condition key to withhold it). |
| Holder of a captured public key / fingerprint | Named key pair + provenance in account A | `Filter.N = fingerprint` / `key-name` | **A query by a known fingerprint returning the matching key-pair name/id = correlation/existence oracle.** |
| Defender auditing SSH access | Current `authorized_keys` on an instance | `DescribeInstances.KeyName` / IMDS `public-keys/0` | **Reported KeyName ≠ current instance key material = audit integrity gap** (stale launch record). |
| SSRF foothold on an instance (IMDSv1 enabled) | Launch public key | IMDS `public-keys/0/openssh-key` tokenless | A tokenless `169.254.169.254` fetch returning the openssh public key = recon leak (low; the IMDS credential prize is owned by the imds-credentials plan). |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `DescribeKeyPairs` | GET/Query | No | Yes | Yes | any principal w/ `ec2:DescribeKeyPairs` | **Resource cell BLANK, condition keys = `ec2:Region` ONLY** (`list_ec2.md:22641`). `IncludePublicKey` (Bool, Default `false`), `Filter.N` (key-pair-id / fingerprint / key-name / tag-key / tag:<k>), `KeyName.N`, `KeyPairId.N`, `DryRun`. |
| `DescribeInstances` | GET/Query | No | Yes | Yes | any principal w/ `ec2:DescribeInstances` | **Resource cell BLANK, condition keys = `ec2:Region` ONLY** (`list_ec2.md:22431`). Returns `Reservations[].Instances[].KeyName` — second read path to the launch key name. |
| `CreateKeyPair` | POST | Yes | Yes | Yes | scopable | Resource `key-pair*`, keys `ec2:KeyPairType` (+ RequestTag/TagKeys). (Create-sibling owns.) |
| `ImportKeyPair` | POST | Yes | Yes | Yes | scopable | Resource `key-pair*`, no KeyPairType/length key (create-sibling Area 1). |
| `DeleteKeyPair` | POST | Yes | Yes | Yes | scopable | Resource `key-pair`, keys `ec2:KeyPairName`/`ec2:KeyPairType` (`list_ec2.md:18897`). |
| IMDS `/meta-data/public-keys/0/openssh-key` | GET (HTTP) | No | No (instance-local) | No (169.254.169.254) | anything on the instance / SSRF | Served under IMDSv1 (tokenless) and IMDSv2. |

**Scopability asymmetry (the structural fact behind Areas 1–2):** every *write/lifecycle* action on a key pair (`CreateKeyPair`, `ImportKeyPair`, `DeleteKeyPair`, plus `key-pair` as a resource type on `RunInstances`/`CreateTags`/etc.) is scopable by `ec2:KeyPairName` and the `key-pair/${KeyPairName}` ARN. The **read action `DescribeKeyPairs` is the lone exception** — blank resource cell, `ec2:Region` only. The condition keys that *exist* for key pairs are exactly two: `ec2:KeyPairName` and `ec2:KeyPairType` (`list_ec2.md:34834,34842`). **There is NO `ec2:PublicKey`, no fingerprint key, no `ec2:IncludePublicKey` key anywhere in `list_ec2.md` (grep = 0).**

---

## 5. Recommended Areas of Focus

### Area 1 — `DescribeKeyPairs` is an unscopable account-/Region-wide read oracle; write-vs-read scopability asymmetry (HEADLINE) — Lens A / S / X / U
**Background.** The key-pair resource is fully ABAC/ARN-scopable for every mutating action, but `DescribeKeyPairs` carries a blank resource-type cell and only `ec2:Region`. An admin can write "this team may only Create/Delete key pairs named `teamA-*`" but **cannot** write "this team may only *describe* key pairs named `teamA-*`" or "...tagged `team=A`." The `Filter.N` names (`key-name`, `fingerprint`, `tag:<k>`) are **query-side result shaping, not authorization** — the caller chooses them and can omit them to dump everything.

**Security Concern.** Any principal holding `ec2:DescribeKeyPairs` (commonly granted via `AmazonEC2ReadOnlyAccess`, `ReadOnlyAccess`, or a broad `ec2:Describe*`) enumerates **every** key pair in the account/Region: `KeyName`, `KeyPairId`, `KeyType`, `KeyFingerprint`, `CreateTime`, `Tags`. This is the key-pair twin of the `manage-spot-fleet` unscopable `DescribeSpotFleetRequests` oracle and the inert-ABAC shape recurring across the corpus. It makes any `aws:ResourceTag`-based Deny on describe **inert** (vacuously inapplicable — the action has no resource context to match). It also fuels the hub's `ImportKeyPair` name land-grab (enumerate existing names → squat/collide) and KeyPairId discovery, and leaks tag values an ABAC scheme may treat as sensitive.

**High-level Test Scenarios.**
- **Claim:** No policy can restrict which key pairs a principal may describe. → **Mechanism:** `list_ec2.md:22641` blank resource cell, `ec2:Region` only; `ec2:KeyPairName` exists but is wired only to write actions (15004/16611/18897/30622/30717/31217/33253). → **Oracle:** `iam:SimulateCustomPolicy` for `ec2:DescribeKeyPairs` with a `Condition {StringLike ec2:ResourceTag/team:A}` or a `Resource: key-pair/teamA-*` — both resolve to the condition/resource being ignored (Allow regardless, or the resource constraint non-binding). Confirm live with a scoped role holding only `ec2:DescribeKeyPairs` + `Deny` on `ec2:ResourceTag/team=secret`: the Deny does not fire, all key pairs returned. → **Severity:** Medium (intra-account over-exposure + inert ABAC; **AWS-owned IAM condition-key coverage gap** — read action lacks the scoping the write actions have, same class as the create sibling's import crypto-floor gap, Tier-2-adjacent).
- **Claim (Lens X twin parity):** A `Deny ec2:DescribeKeyPairs` does not stop a principal from learning a key pair's existence/name via `DescribeInstances.KeyName`. → **Mechanism:** `DescribeInstances` is likewise `ec2:Region`-only (`list_ec2.md:22431`); it returns `Instances[].KeyName`. → **Oracle:** with `ec2:DescribeKeyPairs` denied but `ec2:DescribeInstances` allowed, enumerate launch key names from instances. → **Severity:** Low–Medium (the KeyName leaks through a second unscopable read; no new cross-boundary reach, but defeats a describe-key-pairs-only Deny).
- **Adjacent (confirm the null):** attempt a *cross-account* `DescribeKeyPairs` naming another account's `key-pair/…` — key pairs have no RAM share / launchPermission; expect `AccessDenied`/empty, confirming **no cross-account path** (keeps the finding at Medium, not Critical).

**Doc evidence:** `describe-keys.html` §"Describe your key pairs" (fields enumerated); `API_DescribeKeyPairs` (Filter.N / IncludePublicKey / KeyName.N / KeyPairId.N); `list_ec2.md:22641,22431,34834`. **Severity-if-true:** Medium.

### Area 2 — `IncludePublicKey=true` discloses public key material with no IAM lever — Lens U / S
**Background.** `IncludePublicKey` (Boolean, **Default `false`**, "If `true`, the public key material is included in the response") is the one request parameter that upgrades a metadata describe into a material-disclosure call. The default-off suggests AWS treats the material as more sensitive than metadata — yet nothing in IAM lets a policy author enforce that boundary.

**Security Concern.** Because `DescribeKeyPairs` has no condition keys beyond `ec2:Region`, an admin **cannot** author "allow describe (metadata) but deny `IncludePublicKey`" — there is no `ec2:IncludePublicKey` / request-parameter condition key, and no `ec2:PublicKey` key (grep of `list_ec2.md` = 0). So any `ec2:DescribeKeyPairs` holder can set `IncludePublicKey=true` and pull the full public key of every key pair account-/Region-wide. Public keys are not cryptographic secrets, so the direct severity is bounded; the real value is (a) completing the fingerprint→material→provenance correlation of Area 3 and (b) demonstrating a documented-sensitivity-vs-no-enforcement gap on an AWS-owned action. **Note the honest severity ceiling: this is NOT private-key disclosure** — the private-key cross-service reachability (CFN `AWS::EC2::KeyPair` → SSM SecureString, readable by a principal denied `ec2:*KeyPair*`) is **Lens T, owned by the hub (§9) and the create sibling — do not re-run it here.**

**High-level Test Scenarios.**
- **Claim:** No policy allows metadata-describe while denying public-key-material. → **Mechanism:** `API_DescribeKeyPairs` IncludePublicKey (Default false); `list_ec2.md` DescribeKeyPairs row = `ec2:Region` only; no `ec2:PublicKey`/`ec2:IncludePublicKey` key. → **Oracle:** `iam:SimulateCustomPolicy` with any Condition keyed on the request param → key is unknown/ignored (Simulate treats it as inert); live `describe-key-pairs --include-public-key` under a describe-only role returns `PublicKey` for all keys. → **Severity:** Low–Informational (public material; AWS-owned enforcement gap worth filing).
- **Adjacent (Lens U doc-vs-console delta):** the console **Key Pairs** table and `describe-keys.html` console steps surface name/id/type/fingerprint/tags but **not** `IncludePublicKey` (material is CLI/API-only). Confirm the parameter is reachable via SDK/API even where the console hides it (console-hidden knob, Step-3 move) — relevant if an org assumes the console view bounds disclosure.

**Doc evidence:** `API_DescribeKeyPairs` RequestParameters (IncludePublicKey); `describe-keys.html` §"Retrieve the public key material" (`--include-public-key`, `--query "KeyPairs[].PublicKey"`). **Severity-if-true:** Low–Informational (AWS-owned, Tier-2-adjacent coverage gap).

### Area 3 — Fingerprint / public-key as a correlation, existence, and provenance oracle — Lens A (oracle variant)
**Background.** The default `DescribeKeyPairs` response (no `IncludePublicKey`) **already returns `KeyFingerprint`** for every key pair (confirmed in the API example response). `Filter.N` accepts `Name=fingerprint` and `Name=key-name` as server-side filters.

**Security Concern.** An attacker who has captured a *public* key or fingerprint out of band — from an instance's `~/.ssh/authorized_keys`, a leaked `.pub`, a committed deploy key, or a prior describe — can query `--filters Name=fingerprint,Values=<fp>` and learn **whether that key is a registered EC2 key pair in this account and its `KeyName`/`KeyPairId`**. This is a cross-reference oracle linking an opaque captured key to a named, enumerable resource. Two deepenings: (1) **provenance** — EC2-created RSA keys fingerprint as SHA-1-of-DER-private (59-char `aa:bb:…`), imported keys as MD5-of-public (47-char); the fingerprint *format alone* reveals create-vs-import (cross-ref `verify-keys` / create sibling), telling an attacker which keys the account holds the private half for vs which were imported (candidate for a known/weak key). (2) **ED25519** keys use a different fingerprint scheme — a key-type + fingerprint-shape matrix is a classification oracle.

**High-level Test Scenarios.**
- **Claim:** A known fingerprint confirms+names a key pair without prior knowledge of its name/ID. → **Oracle:** `describe-key-pairs --filters Name=fingerprint,Values=<captured-fp>` returns 1 item (name+id) vs empty = existence oracle; the fingerprint format classifies create-vs-import. → **Preconditions:** `ec2:DescribeKeyPairs` + a captured public key/fingerprint. → **Severity:** Low–Medium (recon/correlation; raises the value of a leaked public key).
- **Adjacent:** combine with Area 2 (`IncludePublicKey`) to pull the full material for a fingerprint-matched key, then compare against instance `authorized_keys` to map key pairs → instances the key authorizes.

**Doc evidence:** `API_DescribeKeyPairs` Filter.N (`fingerprint`, `key-name`) + example response (`keyFingerprint` present without IncludePublicKey). **Severity-if-true:** Low–Medium.

### Area 4 — Launch `KeyName` is an immutable stale record, not current SSH access — Lens U / O / X
**Background.** The page states verbatim: *"If you specify a public key when you launch an instance, the public key name is recorded by the instance. The public key name reported for an instance does not change, even if you change the public key on the instance or add public keys."* The same launch `KeyName` is reachable three ways: `DescribeKeyPairs` (metadata), `DescribeInstances.KeyName`, and IMDS `public-keys/0/openssh-key`.

**Security Concern (audit/integrity).** A defender who audits "who can SSH to this instance" by reading `KeyName` (console **Key pair assigned at launch**, `describe-instances --query KeyName`, or IMDS) is reading the **launch-time** record, which is explicitly frozen. If an operator (or attacker with host access) appended keys to `authorized_keys`, rotated the key, or removed the original, `KeyName`/IMDS still report the original launch key — so the control-plane/IMDS view **understates or misstates current access**. A detective control keyed on `KeyName` is defeated silently (no API lies, but the field means "launched-with", not "currently-authorizes"). This is a documented doc-vs-reality integrity gap, not a product bug — flag it as an assurance/Lens-U finding and a Lens-O detection blind spot.

**High-level Test Scenarios.**
- **Claim:** `KeyName` / IMDS `public-keys/0` does not reflect added/rotated instance keys. → **Oracle:** launch an instance with `teamA-key`; append a second public key to `authorized_keys`; re-read `DescribeInstances.KeyName` and IMDS `public-keys/0/openssh-key` → still report only the launch key → the second key is invisible to any audit built on these fields. → **Severity:** Low–Informational (audit integrity; raises severity of any access-review control that trusts it).
- **Adjacent (Lens X):** both read paths to KeyName (`DescribeKeyPairs`, `DescribeInstances`) are unscopable (`ec2:Region` only) — note for Area 1 twin parity; neither can be fenced, and denying one does not deny the other.

**Doc evidence:** `describe-keys.html` §"Identify the public key specified at launch". **Severity-if-true:** Low–Informational.

### Area 5 — IMDS `public-keys/0/openssh-key` under IMDSv1 (tokenless) — Lens G / D (thin pointer)
**Background.** The page shows retrieving the launch public key from inside an instance via IMDSv2 (token) **and IMDSv1 (no token)**: `curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key`.

**Security Concern.** On an instance still allowing IMDSv1 (`HttpTokens=optional`, AWS's default), a **blind SSRF** that can reach `169.254.169.254` leaks the launch public key name/material — a low-sensitivity recon datum (confirms which key pair launched the box, feeds Area 3 correlation). This is **not a service-side SSRF** (the fetch is instance-local, caller-initiated), and the public key is not a secret. The genuinely dangerous IMDS prize on this endpoint tree is the **credential path** (`iam/security-credentials/…`), which is **owned by the `imds-credentials` plan and the ec2-security-iam child (N-2: identity creds present on 100% of instances; N-9: whether the identity IMDS path obeys IMDSv2/hop-limit)** — do not re-derive it here; cross-reference only.

**High-level Test Scenarios.**
- **Claim:** IMDSv1 serves `public-keys/0/openssh-key` tokenless. → **Oracle:** on an `HttpTokens=optional` instance, tokenless GET returns the key. → **Severity:** Informational (recon only); escalates only as a chain into the credentials endpoint — route to the imds-credentials plan.

**Doc evidence:** `describe-keys.html` §"Retrieve the public key material" → IMDSv1/IMDSv2 tabs. **Severity-if-true:** Informational.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Describe every key pair despite a tag/name-scoped Deny | `DescribeKeyPairs` | `ec2:ResourceTag`/`ec2:KeyPairName` ABAC — **absent on the read action** (inert) |
| Retrieve public key material an admin tried to withhold | `DescribeKeyPairs IncludePublicKey` | No condition key gates the parameter (none exists) |
| Correlate a captured fingerprint/public key to a named key pair | `Filter fingerprint/key-name` | None — filter is query-side; account/Region-wide read |
| Mislead SSH-access audit via frozen launch KeyName | `DescribeInstances.KeyName` / IMDS | Doc states KeyName is immutable launch record (the mitigation gap IS the behavior) |
| Learn key-pair existence via DescribeInstances when DescribeKeyPairs denied | `DescribeInstances` | Both unscopable (`ec2:Region` only) — Deny on one does not cover the other |
| Cross-account read of another account's key pair | `DescribeKeyPairs` | Key pairs are account-scoped, no RAM/launchPermission → expected **AccessDenied** (null) |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account / cross-tenant key-pair access** — no RAM share, no `launchPermission`, ARNs account-scoped. The realistic ceiling for this page is **intra-account over-exposure (Medium)**. State this up front so the hunter does not chase a cross-account key-pair IDOR that cannot exist.
- **Private-key disclosure / CFN `AWS::EC2::KeyPair` → SSM SecureString reachability (Lens T)** — owned by the **hub (§9)** and the **create sibling**; this read page exposes only *public* material.
- **Import weak-key crypto floor, multi-format public-key parser robustness, CFN snippet DeletionPolicy/CMK (Lens U/F/Q/R)** — owned by `create-key-pairs-attack-research-plan.md`.
- **Fingerprint-algorithm confusion as a *verification* defect** — owned by `verify-keys` surface (hub); here fingerprint is used only as a read/correlation oracle.
- **IMDS credential vending / identity-role IMDS path** — owned by `imds-credentials` and `ec2-security-iam` plans; Area 5 is a cross-reference only.
- **IMDS on fully-managed hosts, DNS rebinding against private endpoints, user steering their own instance** — standard exclusions.
- `--query`, `fileb://`, `--cli-input-json file://` — client-side botocore handling, **not server-side fetch** → no SSRF.

---

## 8. Null Hypotheses / Doc Gaps (pages checked)
- **Lens B / C (PassRole / credential vending): N/A** — read-key-pairs, DescribeKeyPairs/DescribeInstances pages read; no role ARN input, no AssumeRole, no session-policy construction on this surface.
- **Lens G (server-side SSRF): N/A** — `describe-keys.html` read in full; the only URL/host on the page is the instance-local IMDS `169.254.169.254` (self-fetch, caller-initiated) and `--query`/`fileb://` (client-side). No field the *service* dereferences server-side. (Area 5 covers the IMDS self-fetch as recon, not service SSRF.)
- **Lens H (KMS): N/A on this page** — no KMS key input on the read path; private-key SSM encryption key is the hub's carried doc-gap.
- **Lens Q (upload) / P (proofing) / J (OAuth) / W (attestation) / FF (JWT): N/A** — none of these mechanisms appear on `describe-keys.html` (checked all three sub-sections: describe, retrieve-material, identify-at-launch).
- **Lens A cross-account IDOR: genuine NULL** — key pairs are not shareable; cross-account read path does not exist. Residual risk is intra-account unscopable read (Area 1).
- **Doc-gap — IncludePublicKey introduction date / console exposure:** confirm whether `IncludePublicKey` is a recent addition and whether any console view surfaces material (believed CLI/API-only) — a Step-3 console-hidden-knob confirmation, cheap.
- **Doc-gap — ED25519 fingerprint format:** the exact fingerprint scheme/length for ED25519 keys (vs RSA SHA-1-DER / imported MD5) should be confirmed against `verify-keys` before relying on fingerprint-shape as a key-type oracle in Area 3.
- **Offline/online drift:** `describe-keys.html` content fetched online 2026-10-15; offline mirror lacks this UserGuide content page (only API_* stubs). `list_ec2.md` facts confirmed against the live reference (35,512 lines).

---
*Cross-references:* hub `ec2-key-pairs-attack-research-plan.md` (owns Lens T private-key→SSM, ImportKeyPair land-grab, KeyPairId discovery, verify-keys fingerprint-confusion); sibling `create-key-pairs-attack-research-plan.md` (owns import crypto-floor, parser, CFN); `imds-credentials` + `ec2-security-iam` plans (IMDS credential path). This plan OWNS: the read/describe scopability asymmetry (Area 1), IncludePublicKey material disclosure with no IAM lever (Area 2), fingerprint correlation oracle (Area 3), launch-KeyName stale-audit integrity gap (Area 4).
