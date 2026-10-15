# EC2 Key-Pair Fingerprint Verification (`verify-keys.html`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-keys.html` (offline twin `/work/aws-docs/.../verify-keys.md`; online==offline **zero drift**, fetched 2026-10-15) + the IAM Service Authorization Reference `list_ec2` (35,512 lines, fetched 2026-10-15) + the cross-referenced instance-fingerprint page `connection-prereqs-general.html#connection-prereqs-fingerprint`. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

**This plan is the page-level deep-dive CHILD of the key-pairs cluster HUB `ec2-key-pairs-attack-research-plan.md`, and SIBLING of `create-key-pairs-attack-research-plan.md`, `describe-keys-attack-research-plan.md`, and `delete-key-pair-attack-research-plan.md`.** It OWNS the surface both the HUB (its Area 6, "fingerprint") and the describe-keys plan (its Area 3, "Fingerprint FORMAT = create-vs-import provenance — doc-gap, confirm via verify-keys") explicitly **deferred to a dedicated verify-keys plan**: the **fingerprint-as-verification-control defect**. It COMPLEMENTS, does not restate — shared leads (CFN private-key→SSM reachability, DescribeKeyPairs unscopability, import crypto-floor, land-grab, EIC twin) are cross-referenced to the owning sibling.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This page is **thin, procedural, and almost entirely client-side.** Its security value is NOT a new API or a cross-tenant primitive — it is a **documented security *property* ("these fingerprints should match" = key authenticity verification) whose enforcing mechanism is broken-by-design cryptography (MD5/SHA-1) and unenforceable in IAM.** The dominant lenses are therefore **U** (doc-guarantee-vs-enforcement), **crypto-weakness** (an addendum to U/F), **A/O** (provenance/correlation oracle), and **R/S** (the absence of any IAM lever). Classic cross-tenant IDOR is a **genuine null** here — state that up front.
- **There is NO cross-account customer-testable primitive produced by this page itself.** Realistic deliverables: (1) a crypto/verification-integrity gap AWS owns, settleable by local computation + doc reasoning; (2) a provenance/audit-correlation oracle that chains to the describe-sibling's unscopable `DescribeKeyPairs`; (3) a user-misdirection (instance-fingerprint vs key-pair-fingerprint) that weakens the one real MITM control.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected on this page.)
- **DryRun is caller-IAM only, never an ownership oracle.** `iam:SimulateCustomPolicy`/`SimulatePrincipalPolicy` is the safe first oracle for every "is there a condition key?" claim — no resource created.

---

## 1. Pentest Objectives

Concrete boundary-breach goals this page's surface implies:

1. **Defeat fingerprint-based key verification:** produce a key pair (or substitute one) whose EC2-reported fingerprint matches a *trusted* key's fingerprint, so a victim's out-of-band "these should match" check passes on the wrong key. (Lens crypto/U — rides on MD5 for imported RSA, SHA-1 for created RSA.)
2. **Defeat "same key" audit correlation:** make one logical key appear as two unrelated keys (or vice-versa) to a defender who correlates key reuse across Regions/accounts by fingerprint. (Lens O/U — create-vs-import hash divergence.)
3. **Use the fingerprint as a provenance + existence oracle:** from a captured fingerprint alone, determine whether a key was EC2-created vs imported vs ED25519, and confirm its existence/name in an account. (Lens A — chains to describe-sibling's unscopable `DescribeKeyPairs Filter Name=fingerprint`.)
4. **Misdirect the MITM control:** cause an operator to verify the *key-pair* fingerprint when the *instance (SSH host-key)* fingerprint is the actual MITM defense — granting false assurance on connect. (Lens U doc-confusion.)
5. **Confirm the fingerprint posture is IAM-unenforceable:** prove no condition key lets an org forbid the weak-hash path, require ED25519, or restrict who reads fingerprints. (Lens R/S/U — synthesis across siblings.)

---

## 2. Components, Assets, and Design

**What this page actually is:** a verification *procedure*, not a service surface. It tells an operator how to confirm that the private key they hold corresponds to the key pair EC2 shows them, by comparing two fingerprints.

**Components / data flow (all comparison is out-of-band / client-side):**

```
                 ┌─────────────────────────────────────────────┐
   EC2 control   │ EC2 stores public key; computes a fingerprint│
   plane         │   RSA created  → SHA-1 (over PKCS8 DER priv) │
   (AWS-owned)   │   RSA imported → MD5  (over pubkey DER)      │
                 │   ED25519 both → SHA-256                     │
                 │   may append '=' padding                    │
                 └───────────────┬─────────────────────────────┘
                                 │  DescribeKeyPairs / console
                                 │  returns KeyFingerprint (+ padding)
                                 ▼
   Operator's    ┌─────────────────────────────────────────────┐
   LOCAL machine │ openssl / ssh-keygen recompute fingerprint   │
   (customer-    │   from the LOCAL private key .pem file       │   ← no network;
    owned)       │   (ssh-keygen OMITS '=' padding)             │     reads local file only
                 └───────────────┬─────────────────────────────┘
                                 │  HUMAN / tool string-compare
                                 ▼
                       "these fingerprints should match"
                         = the asserted security property
```

- **Customer-facing interface for the data being verified:** `ec2:DescribeKeyPairs` (returns `KeyFingerprint`; `IncludePublicKey` optional) and the EC2 console **Key pairs** page. The fingerprint is a **returned attribute of a public key**, not a secret.
- **Local tools:** `openssl` (pkcs8/rsa/sha1/md5), `ssh-keygen`. These operate on the **local private-key file** (`{{path_to_private_key}}`) — a client-side path, never a URL the service dereferences.
- **Resource identifiers:** key-pair ARN is **name-keyed** `arn:…:key-pair/${KeyPairName}` (`list_ec2:33256`); `KeyPairId` (`key-xxxx`) exists but is **not** a condition key. The **fingerprint itself is an identifier** of the public key — low-ambiguity but **hash-algorithm-dependent** (same key, two algos → two fingerprints).
- **Identity:** reading the EC2-side fingerprint = SigV4 IAM (`ec2:DescribeKeyPairs`). Computing the local fingerprint = no AWS identity (local openssl). Verification "trust" = a human comparison, not an authz decision.
- **Adjacent surface the page cross-links:** the **instance (SSH host-key) fingerprint** (`connection-prereqs-general.html#connection-prereqs-fingerprint`) — a *different* fingerprint, SHA-256, obtained from `ec2:GetConsoleOutput` (`BEGIN SSH HOST KEY FINGERPRINTS`), gated by "**you must be the instance owner to get the console output**," and used for **SSH MITM protection on first connect**.

**Mandatory coverage sweep (pages opened for this plan):** `verify-keys.html` (full), `connection-prereqs-general.html` (instance-fingerprint section, full), `describe-keys.html` (sibling, via memory + Area-3 doc-gap it handed here), `create-key-pairs.html`/`delete-key-pair.html` (siblings, via memory), `list_ec2` (grepped: `fingerprint`=**0 hits**, `publickey`=0, `md5`/`sha`/`hash` as condition keys=0; only `ec2:KeyPairName` (34834) + `ec2:KeyPairType` (34842) exist; `ec2:KeyPairId`=0). No upload field, no server-dereferenced URL field, no OTP/registration gate, no secret *generated by this page* (the private key is generated by Create/Import — sibling-owned).

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Attacker who can substitute/import a key | Victim's trust decision ("fingerprints match") | A **fingerprint collision** (MD5 for imported RSA, SHA-1 for created RSA) makes a *different* key present the *same* fingerprint | Victim's documented comparison returns "match" on a key the attacker controls → key-authenticity verification defeated |
| Any `ec2:DescribeKeyPairs` holder (intra-account, unscopable per describe-sibling) | Provenance / existence of any key pair | Fingerprint **format + length** encodes create-vs-import-vs-ED25519; `Filter Name=fingerprint` matches a captured value | From a captured public key alone, determine source algorithm and confirm name/existence of the matching key pair in the account |
| Defender correlating key reuse by fingerprint | "Is this the same key across Regions/accounts?" | EC2-created RSA (SHA-1) and the *same key re-imported* (MD5) have **different fingerprints** | Fingerprint-equality audit shows two unrelated keys for one logical key → reuse goes undetected (audit false-negative) |
| Operator seeking MITM protection | The *instance* (SSH host-key) fingerprint | Page distinguishes key-pair fp from instance fp; a confused operator verifies the **wrong** fingerprint | Operator "verifies" the key-pair fingerprint and connects with false assurance; a MITM host-key swap is not caught |
| Caller of `ec2:GetConsoleOutput` | Another account's instance host-key fingerprint | Instance fingerprint lives in console output; gate = "must be the instance owner" | Reading another account's console output / host-key fingerprint = breach (pointer; GetConsoleOutput authz, not owned here) |
| **Any customer surface** | **AWS service plane** | — | **Hard stop** — not reachable from this page (all compute is local). |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ec2:DescribeKeyPairs` | Non-mutating | No | Yes (SigV4) | **Unscopable account/Region-wide** (`list_ec2:22641`, blank resource cell + `ec2:Region` only — see describe-sibling Area 1) | Returns `KeyFingerprint` **by default** (no `IncludePublicKey` needed); `Filter Name=fingerprint`/`key-name`/`key-pair-id` is query-side, NOT an ACL. The fingerprint read oracle. |
| EC2 console **Key pairs** page | Non-mutating | No | Yes | console users | Same fingerprint; applies `=` padding. |
| `openssl` / `ssh-keygen` (local) | n/a | No | No (local) | local user | Operate on local `.pem`. **No AWS identity, no server fetch** → Lens G null. |
| `ec2:ImportKeyPair` | Mutating | Yes | Yes | `key-pair` ARN + `aws:RequestTag`/`aws:TagKeys`/`ec2:Region` (`list_ec2:27407`/`9727`) — **no `ec2:KeyPairType`, no key-length key** | Determines the **MD5 path**: any imported RSA key is fingerprinted with MD5. Crypto-floor/land-grab mechanics = **create-sibling + delete-sibling**. |
| `ec2:CreateKeyPair` | Mutating | Yes | Yes | `key-pair` ARN + `ec2:KeyPairName`/`ec2:KeyPairType` (`list_ec2:14999`/`15008`) | SHA-1 path (RSA) / SHA-256 (ED25519). |
| `ec2:GetConsoleOutput` | Non-mutating | No | Yes | instance owner (per `connection-prereqs-general`) | Source of the **instance (host-key) fingerprint** — the real MITM control. Cross-tenant read = pointer lead, not owned here. |

**Console-hidden knob:** the `=`-padding behavior and the per-source hash algorithm are **documented only on this page and in `DescribeKeyPairs` output** — neither is a settable parameter, neither is surfaced in the console UI as "this is MD5/SHA-1." No API parameter weakens auth here; the weakness is intrinsic to the chosen hash.

---

## 5. Recommended Areas of Focus

### Area 1 — HEADLINE (Lens crypto / Lens U): fingerprint-based key verification rests on collision-broken hashes (MD5 for imported RSA, SHA-1 for created RSA)

**Background.** The page's asserted security property is verbatim: *"compare the fingerprint displayed … with the fingerprint that you generate using the private key on your local computer. **These fingerprints should match.**"* The "How the fingerprints are calculated" table states the hash is **MD5** for any **imported RSA** key (footnote ¹: "regardless of how you created the key pair"), **SHA-1** for **EC2-created RSA**, and **SHA-256** for ED25519 (both sources).

**Security Concern.** Fingerprint equality is being used as a **key-authenticity / anti-substitution control**, but:
- **MD5** (imported RSA path) has **practical chosen-prefix collisions** (public precedent). The fingerprint is `MD5(DER SubjectPublicKeyInfo)` (the `openssl rsa -pubout -outform DER | openssl md5 -c` recipe). A fingerprint match therefore does **not** cryptographically prove the two keys are the same key.
- **SHA-1** (created RSA path) is collision-weak (SHAttered); the fingerprint is `SHA-1(PKCS8 DER private key)` (`openssl pkcs8 … -topk8 -nocrypt | openssl sha1 -c`).
- Only **ED25519 (SHA-256)** is collision-resistant *and* source-invariant.

So a key-pair fingerprint check is a **cryptographically weak verification** for every RSA key, and **weakest (MD5) for exactly the keys an attacker is most likely to introduce** — *imported* keys (the land-grab / substitution vector; see delete-sibling D3 delete→reimport and create-sibling Area 1). An org **cannot** forbid the MD5 path in IAM (Area 5).

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** For two distinct RSA public keys, EC2 can report the same imported-key fingerprint. → **Mechanism:** fingerprint = `MD5(pubkey DER)`; MD5 chosen-prefix collisions are practical. → **Oracle:** construct two valid RSA SubjectPublicKeyInfo DER blobs that MD5-collide (research-grade but established), import both, confirm `DescribeKeyPairs` reports an identical `KeyFingerprint`. **Even without executing a full collision, the *reliance* on MD5 is the confirmed defect** — demonstrable by computing fingerprints and citing MD5's broken collision resistance. → **Severity-if-true:** Medium (verification-integrity / crypto-agility gap, AWS-owned framing; the control the docs tell customers to use does not provide the integrity it implies). Not Critical because the fingerprint is a verification aid, not a secret and not an authz gate.
- **Claim:** The weak path cannot be avoided by policy. → See Area 5 (no `ec2:KeyPairType`/length key on `ImportKeyPair`). → the customer cannot mandate ED25519 (the only sound fingerprint).
- **Chain:** delete-sibling **D3** (delete frees the name → `ImportKeyPair` under the freed name = credential substitution) + this Area = *substitute an attacker key AND make its fingerprint match the deleted trusted key* so a fingerprint-based detection of the swap fails. Rate at the chain end (key substitution surviving fingerprint verification).

**Doc evidence:** `verify-keys.html` — "These fingerprints should match"; hash-function table + footnote ¹; the three OpenSSL/ssh-keygen recipes. **Severity-if-true:** Medium (Tier-2-adjacent: AWS-authored verification guidance recommending a broken-hash integrity check). Owner-to-fix: AWS (hash choice) + customer (don't treat RSA fingerprint equality as authentication).

### Area 2 — (Lens A / Lens O): fingerprint as a provenance + "same-key" correlation oracle — RESOLVES describe-sibling Area 3 doc-gap

**Background.** This page supplies the facts describe-sibling Area 3 flagged as "confirm via verify-keys": the hash per source. EC2-created RSA fp = SHA-1 (40 hex / 20 bytes, over the *private* key DER); imported RSA fp = MD5 (32 hex / 16 bytes, over the *public* key DER); ED25519 fp = SHA-256 (both sources). The page's **Note** states verbatim that an EC2-created RSA key whose public key is then re-imported *"will have a different fingerprint than the original … because the fingerprint of the original … is calculated using a SHA-1 hash function, while the fingerprint of the imported … is calculated using an MD5 hash function."*

**Security Concern.**
- **Provenance oracle (Lens A):** the fingerprint's **length/charset alone** reveals whether a key is EC2-created RSA (SHA-1), imported RSA (MD5), or ED25519 (SHA-256) — with no additional API call. Combined with describe-sibling Area 1 (`DescribeKeyPairs` is **fully unscopable**, `ec2:Region` only) and Area 3 (`Filter Name=fingerprint`), any `DescribeKeyPairs` holder can take a **captured public key / fingerprint** (public, non-secret) and confirm existence + name + source-algorithm of the matching key pair **account-wide**, with inert ABAC.
- **Correlation false-negative (Lens O/U):** a defender who audits "is the same key reused across Regions/accounts?" by comparing fingerprints is **defeated by design** — the same logical key presents SHA-1 in the creating Region and MD5 in every Region it's re-imported to (the page's whole "different Regions" section tells customers to re-import, guaranteeing the divergence). Key-reuse detection built on fingerprint equality silently fails.

**High-level Test Scenarios:**
- **Claim:** Fingerprint format discloses key source with no extra privilege. → **Oracle:** classify a set of `DescribeKeyPairs` `KeyFingerprint` values by length/hash; verify against known create vs import provenance. → **Severity:** Low–Info (public data; AWS-owned enforcement gap — no `ec2:PublicKey`/fingerprint key to allow-metadata-deny-material, Area 5).
- **Claim:** A captured 3rd-party public key can be matched to a key pair in an account the capturer only has `DescribeKeyPairs` on. → **Oracle:** `aws ec2 describe-key-pairs --filters Name=fingerprint,Values=<captured>` returns the name/id. → **Severity:** Low–Medium (intra-account recon oracle; chains to delete→reimport land-grab target selection).
- **Claim:** Fingerprint equality cannot establish key identity across the create/import boundary. → **Oracle:** create an EC2 RSA key, export the public key, re-import it, compare the two fingerprints (page guarantees they differ). → **Severity:** Low (audit-integrity).

**Doc evidence:** `verify-keys.html` "How the fingerprints are calculated" table + the "different Regions" Note; describe-sibling Areas 1 & 3. **Severity-if-true:** Low–Medium.

### Area 3 — (Lens U / canonicalization differential): the `=`-padding mismatch between EC2 and ssh-keygen trains operators to ignore fingerprint mismatches

**Background.** Verbatim: *"When Amazon EC2 calculates a fingerprint, Amazon EC2 might append padding to the fingerprint with `=` characters. Other tools, such as **ssh-keygen**, might omit this padding."*

**Security Concern.** The **generation layer (EC2)** and the **comparison layer (local ssh-keygen/human)** canonicalize the fingerprint string differently. Consequences:
- A naive **string-equality** comparison (or a verification script) sees a **mismatch on a legitimately-matching key** → the operator is conditioned to **dismiss "mismatch" as a known cosmetic artifact** and proceed anyway — a **fail-open on the human control** (the exact behavior an attacker substituting a key wants). This is the fingerprint-comparison analogue of a Lens-BB parser differential: two layers "equal to one, different to the other."
- Conversely a tool that **strips `=` to compare** may mask a trailing-character difference between near-identical encodings.

**High-level Test Scenarios:**
- **Claim:** The documented verification yields a byte-level mismatch for a correct key, with no guidance to normalize. → **Oracle:** run the page's own recipes against a real EC2 key, diff the two strings byte-for-byte; confirm the `=` delta and that the page gives no canonicalization step. → **Severity:** Low (verification usability → integrity; the risk is behavioral — users learning to ignore mismatches). AWS-owned (doc could prescribe exact normalization).

**Doc evidence:** `verify-keys.html` padding sentence; the three recipes (OpenSSL `-c` colon-hex vs `ssh-keygen -l` base64-SHA256 produce *entirely different* formats — a second, larger comparison-format inconsistency the page does not reconcile). **Severity-if-true:** Low.

### Area 4 — (Lens U doc-confusion): key-pair fingerprint vs instance (SSH host-key) fingerprint — verifying the wrong one defeats MITM protection

**Background.** The page itself flags the confusion: *"If you're trying to verify the fingerprint of your Linux EC2 instance, not the fingerprint of your key pair, see Get the instance fingerprint."* The **instance fingerprint** (`connection-prereqs-general.html#connection-prereqs-fingerprint`) is a **different** value — the SSH **host-key** fingerprint (SHA-256; `BEGIN SSH HOST KEY FINGERPRINTS` in `get-console-output`) — and is explicitly the **MITM-protection control**: *"To protect yourself from man-in-the-middle attacks, you can verify the authenticity of the instance … If the fingerprints don't match, someone might be attempting a man-in-the-middle attack."*

**Security Concern.** The **key-pair** fingerprint (this page) authenticates *the key you hold*, and provides **no MITM protection on connect**. An operator who conflates the two and "verifies" the key-pair fingerprint gains **false assurance** against a host-key swap. The two live on adjacent, cross-linked pages with similar names and similar `openssl`/`ssh-keygen` tooling — a realistic documentation-induced security-decision error.

**Adjacent lead (pointer, not owned here):** the instance fingerprint is read via `ec2:GetConsoleOutput`, gated by "**you must be the instance owner**." Whether that ownership check is enforced resource-level (vs a foreign `i-…`), and whether host-key fingerprints for another account's instance can be read, is a **GetConsoleOutput authz** question — route to a broader EC2 console/troubleshooting plan, not this one. Also: the console output is **first-boot only** and depends on cloud-init printing the host key (AMI-dependent) — an availability gap for the control, not an isolation break.

**High-level Test Scenarios:**
- **Claim:** The docs let an operator substitute the key-pair fingerprint check for the instance fingerprint check. → **Oracle:** doc-walk showing both pages present "verify the fingerprint" with near-identical tooling and only a one-line disambiguation. → **Severity:** Low (doc-clarity → MITM false-assurance).
- **Claim (pointer):** `GetConsoleOutput` ownership check is bypassable / reads a foreign instance's host-key fingerprint. → defer to GetConsoleOutput authz review. → **Severity-if-true:** cross-account read = High (but not established here).

**Doc evidence:** `verify-keys.html` instance-fingerprint cross-link; `connection-prereqs-general.html#connection-prereqs-fingerprint`. **Severity-if-true:** Low (+ a High *pointer* for GetConsoleOutput cross-tenant, out of this page's scope).

### Area 5 — (Lens R / S / U synthesis): the entire fingerprint-verification posture is IAM-unenforceable

**Background.** Grep of `list_ec2` (35,512 lines, 2026-10-15): **`fingerprint` = 0 hits**, `publickey` = 0, no `md5`/`sha`/`hash`/`KeyPairId` condition key; the ONLY key-pair condition keys are `ec2:KeyPairName` (34834) and `ec2:KeyPairType` (34842). `ImportKeyPair` (27407) carries **neither** of those (only `aws:RequestTag`/`aws:TagKeys`/`ec2:Region`) — create-sibling Area 1.

**Security Concern.** An org **cannot** author an EC2 IAM/SCP condition that:
- **forbids the weak-hash path** — there is no key for hash algorithm or key length;
- **requires ED25519** (the only algorithm whose fingerprint is sound and source-invariant) — `ImportKeyPair` lacks `ec2:KeyPairType` entirely, so even "deny importing RSA" is inexpressible (create-sibling Area 1 owns this); `CreateKeyPair` *does* carry `ec2:KeyPairType`, so the asymmetry is import-only;
- **restrict who may read fingerprints** — `DescribeKeyPairs` is fully unscopable (describe-sibling Area 1), and there is no `ec2:PublicKey`/fingerprint key to separate metadata from material (describe-sibling Area 2).

So **every** mitigation a defender might reach for against Areas 1–2 (mandate strong keys, deny the MD5 path, gate fingerprint reads) is **unavailable in IAM** — the posture is pure prose/orchestration. This is the Lens-U "guarantee enforced only by documentation" shape, confirmed statically.

**High-level Test Scenarios:**
- **Claim:** No condition key can deny the MD5/SHA-1 fingerprint path or require ED25519 on import. → **Oracle:** `iam:SimulateCustomPolicy` with a guessed `ec2:KeyPairType`/length condition on `ImportKeyPair` → the key is inert (no effect); no resource created. → **Severity:** Medium (AWS-owned condition-key coverage gap; Tier-2-adjacent, same class as create-sibling import crypto-floor and describe-sibling IncludePublicKey gap).

**Doc evidence:** `list_ec2` grep (0 fingerprint/length keys); create-sibling Area 1; describe-sibling Areas 1–2. **Severity-if-true:** Medium. **Defers** the import crypto-floor mechanics (1024-bit RSA accepted) to **create-sibling Area 1**; owns only the "fingerprint posture unenforceable" synthesis.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Substitute a key whose fingerprint matches a trusted key (MD5 imported-RSA collision) | `ImportKeyPair` + `DescribeKeyPairs` fingerprint | "These fingerprints should match" (verification by fingerprint equality) |
| Make the same logical key appear as two unrelated keys to a fingerprint-equality auditor | create vs import hash divergence | fingerprint used as key identity across Regions |
| Match a captured 3rd-party public key to a named key pair account-wide | `DescribeKeyPairs Filter Name=fingerprint` (unscopable) | (none — no fingerprint/publickey condition key) |
| Condition operators to ignore a legitimate fingerprint "mismatch" | `=`-padding + format differential (EC2 vs ssh-keygen) | padding disclaimer (no normalization step prescribed) |
| Verify the key-pair fingerprint believing it provides MITM protection | key-pair fp vs instance (host-key) fp confusion | one-line cross-link disambiguation |
| Enforce strong-key / ED25519-only / fingerprint-read restriction | IAM (`ImportKeyPair`/`DescribeKeyPairs`) | **no condition key exists** (unenforceable) |
| (Pointer) Read a foreign instance's host-key fingerprint | `GetConsoleOutput` | "must be the instance owner" |

---

## 7. Out-of-Scope Risk Categories

- **Local tooling** — openssl/ssh-keygen running on the operator's machine against a local `.pem`. No AWS trust boundary; `{{path_to_private_key}}` is a local path, not a server-dereferenced URL (Lens G null).
- **Cross-account IDOR of key pairs** — **genuine null**: key pairs are **not RAM-shareable**, the ARN is account-scoped (`list_ec2:33256`), there is no `launchPermission`-style share, and the fingerprint is derived from the **public** key (non-secret). Ceiling for Areas 1–2 is **intra-account**; cross-account requires a *separate* breach (e.g. the Lens-T CFN→SSM private-key path, HUB §9 — not this page).
- **The weakness of MD5/SHA-1 as a general matter** — a well-known fact; in scope here **only** because AWS documentation recommends fingerprint equality as a verification control and offers no sound alternative for RSA. Report the *reliance*, not MD5 itself.
- **GetConsoleOutput cross-tenant authz** — a real question but a *different action/page*; pointer only.
- **Private-key secrecy, CFN KeyPair → SSM reachability** — HUB Area 1 / §9 and create-sibling; not restated.
- **Shared-responsibility line / AWS service plane** — hard stop.

---

## 8. Null hypotheses / doc gaps

- **Lens G (SSRF) — NULL.** Pages checked: `verify-keys` (all three recipes), `connection-prereqs-general`. Every command reads a **local file**; no field the service fetches/validates/renders server-side. `{{path_to_private_key}}` = client-side path.
- **Lens Q (upload) — NULL.** No upload on this page. The only server-side parse of key *material* is `ImportKeyPair`'s public-key parser — owned by **create-sibling Area 2** (multi-format DER/OpenSSH/RFC4716 parser), not restated here.
- **Lens F (translation/injection) — NULL on this page.** No wire-protocol/translation layer; local hashing only. Server-side DER/MD5 parse of an imported key = create-sibling.
- **Lens B / C / D / H / J / M / N / V / W / Y / AA / BB / CC / DD / EE / FF — NULL.** No role ARN/PassRole, no STS session, no control-plane ENI, no CMK/encryption-context, no OAuth/3P, no session token, no namespace migration, no network segmentation, no attestation gate, no transport/TLS claim (comparison is offline), no share/revoke lifecycle, no multi-parser request path, no upstream-context header, no cache, no predictable-name land-grab *on this page* (the land-grab is delete→reimport, delete-sibling D3), no JWT/token. Page is a static client-side procedure.
- **Lens A cross-account — NULL** (key pairs not shareable; fingerprint is public-key-derived). Intra-account provenance/correlation oracle (Area 2) is the real residual.
- **Lens P — NULL.** No registration/proofing/OTP gate.
- **Lens O — FIRES at Area 2** (fingerprint-equality audit false-negative) and **Area 3** (operators trained to ignore mismatches).
- **Lens U / crypto — FIRES at Areas 1, 3, 4, 5** (headline).
- **Lens R / S — FIRES at Area 5** (no condition key over hash/length/fingerprint-read).

**Doc gaps / confirm-first:**
- Whether a *re-imported* ED25519 key truly keeps an identical fingerprint in practice (page asserts SHA-256 both ways → it should; cheap to confirm). Load-bearing for Area 2's "ED25519 is the one sound path."
- The **exact byte input** to the created-RSA SHA-1 (PKCS8 DER of the *private* key, per the recipe) vs imported-RSA MD5 (DER of the *public* key) — confirms *why* a created-then-exported-then-imported key diverges, and bounds the collision-construction target for Area 1 (imported path = public SubjectPublicKeyInfo DER, the standard collision target).
- `GetConsoleOutput` resource-level ownership enforcement (Area 4 pointer) — defer to a GetConsoleOutput/console-troubleshooting plan.
- Whether the EC2 console surfaces *which* hash a given fingerprint uses (page says output "can vary by OS, AMI version, and whether AWS created the key pairs") — if not, Area 2's provenance oracle is operator-invisible but API-derivable.

**Mirror parity:** `verify-keys.md`/`.html` byte-identical online==offline 2026-10-15; `connection-prereqs-general` instance-fingerprint section fetched online; `list_ec2` fetched live (35,512 lines). No drift.

**Cross-references:** key-pairs HUB `ec2-key-pairs-attack-research-plan.md` (Area 6 fingerprint — this plan is its deep-dive); `describe-keys-attack-research-plan.md` (Areas 1/3 — unscopable Describe + fingerprint oracle; this plan resolves its Area-3 doc-gap); `create-key-pairs-attack-research-plan.md` (Area 1 import crypto-floor / no `ec2:KeyPairType`); `delete-key-pair-attack-research-plan.md` (D3 delete→reimport substitution — chains with Area 1); IAM reference slug `list_ec2` per the reference memory.
