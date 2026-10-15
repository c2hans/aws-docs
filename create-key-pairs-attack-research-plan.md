# create-key-pairs.html — Attack Research Plan (page-level deep-dive child)

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html` (`.md` twin fetched live 2026-10-15; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/create-key-pairs.md` is **content-identical** — only frontmatter + trailing-whitespace drift). Authoritative IAM surface: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (slug `list_ec2`) and `list_ec2-instance-connect.md` (both read offline by targeted grep).

**Status:** documentation-derived hypotheses only. Nothing tested against a live AWS account.

**Relationship to the existing plan — READ THIS FIRST.** This is the **page-level deep-dive child** of the cluster HUB plan `ec2-key-pairs-attack-research-plan.md`, which already treats `create-key-pairs.md` as one of its five source children. This plan does **NOT** restate the hub's leads; it **cross-references** them and owns only the surface that is *specific to this page* and that the hub covered at summary level or not at all. The hub owns, and this plan defers to it:
- **Hub Area 1 (Lens T)** — CFN-generated private key reachable via SSM `/ec2/keypair/{id}` across an IAM wall. *(This plan deepens only the page-mechanism detail in §5.3; the cross-service reachability test itself is the hub's.)*
- **Hub Area 2 (Lens EE/U)** — `KeyPairId` discoverable via unscopable `DescribeKeyPairs` or CFN `GetAtt`.
- **Hub Area 3 (Lens S)** — `ec2:KeyPairName` absent from Create/Import; name-scoping silently inert.
- **Hub Area 4 (Lens A/EE)** — `ImportKeyPair` predictable-name land-grab on the flat `key-pair/${KeyPairName}` namespace.
- **Hub Area 5 (Lens R)** — `ExamplePolicies_EC2.md` `RunInstances` samples grant `key-pair/*` unconditioned.
- **Hub Area 6 (Lens U)** — fingerprint hash-function confusion (lives on `verify-keys.md`, not this page).
- **Hub Area 7 (Lens X)** — EC2 Instance Connect `SendSSHPublicKey` as a parallel SSH-credential path.

**What THIS page uniquely introduces into the corpus (the net-new surface this plan owns):** the explicit **key-material requirements block** — supported *types* (RSA / ED25519 / no DSA), supported *formats* (OpenSSH / SSH2 / DER / RFC 4716), and supported *lengths* (**1024**, 2048, 4096) — plus the CloudFormation YAML snippet and the "fabricated parameter name" permission-probe prose. None of these are developed in the hub.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- Oracles here are overwhelmingly **read-only / static-analysis** (`iam:SimulateCustomPolicy`, a single scoped `import-key-pair` with a canary key). No cross-tenant primitive exists on this page — it is a single-account control-plane surface.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives
1. Determine whether a least-privilege policy author can prevent the import of a **weak (1024-bit) RSA** public key — or any sub-2048-bit / legacy-format key — through *any* IAM condition key on `ec2:ImportKeyPair`, given the page explicitly advertises 1024-bit as a supported import length while EC2-created keys and the EC2 Instance Connect path both floor at 2048.
2. Determine whether `ec2:ImportKeyPair`'s total absence of a key-**type** condition key (`ec2:KeyPairType` is wired to Create but not Import) lets a principal bypass an org intent of "only ED25519 keys may enter this account."
3. Determine whether the EC2 control-plane multi-format public-key **parser** (OpenSSH / SSH2 / DER / RFC 4716 / base64-DER) exhibits any robustness or format-confusion issue when fed malformed, oversized, or ambiguous `PublicKeyMaterial`.
4. Determine whether the AWS-published **CloudFormation snippet** on this page, copied verbatim, ships the generated private key into SSM under weaker-than-intended protection (default managed key, no `DeletionPolicy`, no CMK) and whether the documented "fabricated parameter name" delete-time probe leaks or misbehaves.
5. Confirm the doc-vs-IAM integrity gap: the IAM reference Descriptions ("2048-bit RSA key pair" / "import a public key from an RSA key pair") contradict this page's stated ED25519 support — does any downstream control rely on the narrower IAM wording?

## 2. Components, Assets, and Design

**Customer-facing interface (this page's three creation paths):**
1. **EC2-native create** — `ec2:CreateKeyPair` (Console / CLI `create-key-pair` / PowerShell `New-EC2KeyPair`). EC2 generates the pair, stores the **public** key (resource `key-pair`, ARN `arn:${Partition}:ec2:${Region}:${Account}:key-pair/${KeyPairName}`), returns the **private** key exactly once (`KeyMaterial`), never retains it. IAM Description pins it to **2048-bit RSA** (`list_ec2.md:5248`); ED25519 also offered in the console.
2. **CloudFormation create** — `AWS::EC2::KeyPair` resource. CFN calls `CreateKeyPair` and additionally writes the private key to **SSM Parameter Store** `SecureString` at `/ec2/keypair/{key_pair_id}` (requires `ssm:PutParameter` + `ssm:DeleteParameter`). *(Cross-service reachability = hub Area 1 / Lens T.)*
3. **Third-party create + import** — `ec2:ImportKeyPair` with caller-supplied `PublicKeyMaterial` (CLI `--public-key-material fileb://…`, PowerShell `Import-EC2KeyPair`). Caller controls the type, length, and format of the imported key within the page's stated requirements.

**Assets:** the **private key** (downloaded-once for native; persisted in SSM for CFN; held entirely by the caller for import), the **public key** (stored in EC2, placed into `~/.ssh/authorized_keys` at first boot), the **key name** (flat per-account+Region namespace, ≤255 ASCII chars), and the **KeyPairId** (second-class id used only for the SSM path — hub Area 2).

**Untrusted-data entry point (the page-specific one):** `ImportKeyPair.PublicKeyMaterial` — attacker-choosable bytes in **five accepted encodings** (OpenSSH `authorized_keys`, SSH2, base64 DER, RFC 4716, and — for the EIC SSH path — SSH2), of **three RSA lengths (1024/2048/4096)** or ED25519, parsed server-side by the EC2 control plane into the stored key.

**Pipeline (import path):**
```
third-party tool → PublicKeyMaterial (RSA 1024/2048/4096 | ED25519; OpenSSH/SSH2/DER/RFC4716)
        │  aws ec2 import-key-pair --public-key-material fileb://…   (client-side file read; NOT a server fetch)
        ▼
EC2 control-plane multi-format key parser  ──▶  stored key-pair/${KeyPairName}  ──(first boot)──▶  instance ~/.ssh/authorized_keys
   IAM gate on this call: key-pair* resource + {aws:RequestTag, aws:TagKeys, ec2:Region}   ← NO type key, NO length key
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Principal holding `ec2:ImportKeyPair` (tag/Region-scoped only) | The account's *cryptographic key-strength policy* | `--public-key-material` carrying a **1024-bit RSA** or legacy-format key; no `ec2:KeyPair(Length\|Bits\|Type)` condition exists to stop it | **Breach (policy-expressibility):** a key the org's crypto standard forbids is accepted and becomes a valid SSH credential; the admin provably **cannot author** an IAM/SCP statement that denies it. |
| Caller-supplied `PublicKeyMaterial` (5 formats) | EC2 control-plane key parser | server-side parse of attacker-chosen bytes | **Breach:** parser crash / format-confusion / oversize-induced error that leaks internals or deviates across formats (Lens F/Q — robustness, not isolation). |
| Customer copying the page's CFN YAML verbatim | SSM `SecureString` under `alias/aws/ssm` (default) | snippet omits `DeletionPolicy` and any CMK; private key lands under the default managed key | **Breach-adjacent:** private key stored under broader-reach default-key delegation than the author assumes (feeds hub Area 1 Lens T), and no retain-on-delete guard. |
| EC2-native create (2048 floor) vs EC2 Instance Connect (2048/4096 floor) vs **Import (1024 allowed)** | one "SSH into the instance" capability | three documented paths with **divergent length floors** | **Breach (Lens X parity):** the weakest floor (import, 1024-bit) silently undercuts the stronger floors enforced on the sibling paths. |

## 4. API / Interface Inventory

| Name | Method | Mutating | Functionality | Authorized callers | Notes (page-specific) |
|---|---|---|---|---|---|
| `ec2:CreateKeyPair` | API/CLI/Console/PS | Yes | Generate pair, return private key once | IAM principal w/ grant | IAM Desc = **"2048-bit RSA"** (`list_ec2.md:5248`); cond keys `aws:RequestTag`, `aws:TagKeys`, **`ec2:KeyPairType`**, `ec2:Region` — **no `ec2:KeyPairName`** (hub Area 3). ED25519 offered in console but not named in IAM Desc. |
| `ec2:ImportKeyPair` | API/CLI/Console/PS | Yes | Import caller-supplied public key (1024/2048/4096 RSA or ED25519; 5 formats) | IAM principal w/ grant | IAM Desc = **"import a public key from an RSA key pair"** (`list_ec2.md:8670`); cond keys `aws:RequestTag`, `aws:TagKeys`, `ec2:Region` **only** — **no `ec2:KeyPairType`, no `ec2:KeyPairName`, no length key** (`list_ec2.md:8669-8673`). The weakest-scopable action in the family. |
| `AWS::EC2::KeyPair` (CFN) | CFN stack op | Yes | Create/import + SSM `PutParameter`/`DeleteParameter` | Stack role or caller | Page snippet: `KeyName: new-key-pair`, no `DeletionPolicy`, no CMK. Delete-time `ssm:DeleteParameter` probe uses a **fabricated parameter name** → surfaces in `AccessDeniedException`. |
| `aws ssm get-parameter --with-decryption /ec2/keypair/{id}` | CLI (SSM) | No | Read CFN-stored private key | SSM/KMS grant holders | Cross-service reachability = **hub Area 1 (Lens T)** — not restated here. |

**Undocumented-knob / asymmetry hunt (page-specific):**
- `ec2:ImportKeyPair` accepts a **1024-bit RSA** key and a key of **any supported type**, with **no condition key for either** — the control-plane accepts a weaker artifact than the console-native path, un-gated. This is the page's single most consequential IAM gap.
- The CLI `--query "KeyMaterial" --output text > file` and `fileb://`/`file://` arguments are **client-side botocore operations**, wire-identical to inline bytes — **not** a server-side fetch (Lens G null, see §8).

## 5. Recommended Areas of Focus

### Area 1 — Weak / legacy key-material import with no IAM strength floor (Lens U + crypto-weakness + Lens X) [PRIMARY, NET-NEW]
**Background:** This page's "Requirements for key pairs" block states, verbatim, **"Supported lengths: 1024, 2048, and 4096."** By contrast, `CreateKeyPair`'s own IAM Description is *"Grants permission to create a **2048-bit** RSA key pair"* (`list_ec2.md:5248`), and the page's EIC caveat says the EC2 Instance Connect SSH path supports only lengths **2048 and 4096**. So **import is the only one of the three documented key paths that admits a 1024-bit RSA key.**

**Security Concern:** An exhaustive grep of all 10,206 lines of `list_ec2.md` returns **ZERO** condition keys matching key length/bits/size (`ec2:KeyPair(Length|Bits|Size)`, `ec2:KeyLength`, etc. — none exist). `ec2:ImportKeyPair` carries only `aws:RequestTag` / `aws:TagKeys` / `ec2:Region` (`list_ec2.md:8669-8673`) — it does **not** even carry `ec2:KeyPairType` (which *is* wired to `CreateKeyPair`). Therefore an administrator **cannot author any IAM/SCP statement** that (a) forbids importing a 1024-bit (deprecated, materially weaker) RSA key, (b) forbids a given key *type* on import, or (c) requires a minimum strength. A "require ED25519 / ≥2048-bit SSH keys" organizational mandate is **unenforceable at the IAM layer on the import path** — it can only be met by prose/governance or detective controls. A principal scoped tightly on everything else can still plant a weak-but-valid SSH credential that lands in `authorized_keys` at first boot.

**High-level Test Scenarios:**
1. `iam:SimulateCustomPolicy` with an Allow on `ec2:ImportKeyPair` conditioned on a guessed strength key (`ec2:KeyPairLength`, `ec2:KeyPairBits`) and on `ec2:KeyPairType` — confirm the simulator treats all of them as **unsupported/inert** for this action (the statement collapses to unconditioned Allow), i.e. the mandate silently does not bind. (Mirror hub Area 3's `ec2:KeyPairName`-is-inert result for the strength/type dimension.)
2. Under a scoped canary role holding only `ec2:ImportKeyPair`, import a **1024-bit RSA** key (`ssh-keygen -t rsa -b 1024 -m PEM`) and confirm acceptance; repeat with an RSA key where only ED25519 was intended — confirm no enforcement point exists.
3. Confirm the Lens-X floor asymmetry: the same 1024-bit key is rejected by the EIC `SendSSHPublicKey` path (page: 2048/4096 only) but accepted by `ImportKeyPair`, proving the weakest floor undercuts the siblings.

**Doc evidence:** page "Requirements for key pairs" (lengths 1024/2048/4096; EIC 2048/4096); `list_ec2.md:5248` (Create = 2048-bit), `8669-8673` (Import cond keys), whole-file grep = no length/bits key.
**Severity-if-true:** Medium (Lens U "documented-guarantee-vs-enforcement" + Lens S "condition key that does not exist → cannot deny by it", AWS-owned schema gap). A customer who builds a "strong-keys-only" compliance control on IAM will find it has no teeth on import. Reportable as an AWS condition-key coverage gap (route `aws-security`, Tier-2-adjacent — it is a reference/schema gap, not a customer footgun).

### Area 2 — Multi-format public-key parser robustness (Lens F / Lens Q, NET-NEW framing)
**Background:** The page enumerates **five** accepted encodings for imported public keys: OpenSSH `authorized_keys` format, SSH2 (via the EIC path), **base64-encoded DER**, SSH public-key file format per **RFC 4716**, and PEM/PPK private-key formats for the local side. The EC2 control plane must parse attacker-chosen bytes in any of these into a stored key.

**Security Concern:** Any multi-format parser consuming untrusted, caller-controlled bytes is a robustness seam (the catalog's Lens F "native memory-safety / parser trusts an attacker-supplied length/depth/offset" and Lens Q "true-type vs claimed-type confusion"). DER in particular is a TLV structure where a malformed length prefix is the classic over-read trigger; RFC 4716 has explicit header/continuation framing. The hub plan treats `PublicKeyMaterial` only as *credential content* (land-grab, Area 4) — it never asks whether the **parse itself** is safe or whether a blob that is valid in one format is misinterpreted as another.

**High-level Test Scenarios:**
1. Submit malformed DER (truncated length, over-long length prefix, deeply-nested wrapper), oversized key material (far beyond 4096-bit), and empty/truncated RFC 4716 headers via `import-key-pair` under a scoped canary role; observe whether the response is a clean `ValidationException` (good), a 500/InternalError (robustness-oracle, Lens A 500-vs-400), or an inconsistent result across formats.
2. Format-confusion: submit bytes that are simultaneously parseable as two formats (e.g. a DER blob that is also valid base64 of an OpenSSH line) and check whether EC2's chosen interpretation is deterministic and matches what later lands in `authorized_keys`.
3. Null-check true-type confusion: there is no "claimed Content-Type" channel here (bytes are self-describing), so Lens Q's MIME-confusion variant is weak — record whether any format-sniffing ambiguity exists at all.

**Doc evidence:** page "Supported formats" list; `list_ec2.md:8669-8673` (no content/format condition key — `ec2:PublicKey` does not exist).
**Severity-if-true:** Low–Medium (single-tenant control-plane robustness; a crash that crosses tenants on shared EC2 control-plane infra would be higher but is not indicated by the docs — treat an actual cross-tenant effect as a HARD STOP and disclosure item). Primarily a doc-derived *question*, not a claimed bug.

### Area 3 — CFN snippet default-protection + fabricated-parameter-name delete probe (Lens R / U / O — deepens hub Area 1)
**Background:** This page prints the canonical `AWS::EC2::KeyPair` YAML (`KeyName: new-key-pair`, nothing else) and states that CloudFormation writes the private key to SSM `SecureString` `/ec2/keypair/{key_pair_id}`. The "Required IAM permissions" block requires `ssm:PutParameter` + `ssm:DeleteParameter`, and adds: *"CloudFormation tests for the required permission using a **fabricated parameter name** that does not match any parameter in your account. Therefore, you might see a fabricated parameter name in the `AccessDeniedException` error message… This permission is required whether the key pair was imported or created."*

**Security Concern (three sub-leads, all page-specific):**
1. **Default-key / no-DeletionPolicy copy-verbatim artifact (Lens R):** the snippet ships no `DeletionPolicy: Retain|Delete` and names no CMK, so a verbatim copy lands the private key under the **default `alias/aws/ssm` managed key** — exactly the broader-reach delegation surface the hub's Lens-T attack (Area 1) relies on. The page never warns the operator that the private key's confidentiality now rides on *SSM/KMS* IAM, not EC2 key-pair IAM. This is the page-mechanism that *creates* the hub-Area-1 condition; the hub owns the reachability test, this plan owns the "the AWS-authored snippet is what puts it there" observation.
2. **Delete-time probe fires even when no parameter exists (Lens U/O):** for **imported** keys CFN never created an SSM parameter, yet it still performs the `ssm:DeleteParameter` permission check against a fabricated name on stack delete. Question: does this probe ever (a) leak a real adjacent parameter name through an error oracle, or (b) interact with the orphan-parameter scenario (hub Area 1 scenario 4) so that a created-key stack whose delete is denied mid-way leaves the real `/ec2/keypair/{id}` live while the error only ever mentions the fabricated name — masking the orphan from an operator reading logs?
3. **Audit-signal shape (Lens O):** confirm the fabricated name is non-colliding by construction (page says "does not match any parameter in your account") and cannot be steered to probe-read a chosen path.

**High-level Test Scenarios:**
1. Deploy the verbatim snippet; confirm the SSM parameter's `KeyId` is `alias/aws/ssm` (default) with no customer action — establishing the Lens-T precondition is AWS-snippet-induced.
2. Create an **imported**-key stack, deny `ssm:DeleteParameter` on the role, delete the stack; capture the `AccessDeniedException` and confirm it carries only a fabricated name (no real-parameter disclosure), and that no real parameter was orphaned (import path never wrote one).
3. Create a **generated**-key stack, revoke `ssm:DeleteParameter` after creation, delete the stack; confirm whether the real `/ec2/keypair/{id}` survives (orphaned secret) — this is the concrete realization of the hub's Threat-Model "orphaned parameter" row.

**Doc evidence:** page CFN section + "Required IAM permissions" + fabricated-name paragraph.
**Severity-if-true:** Low–Medium. Sub-lead 1 is an AWS-authored-sample completeness gap (Lens R, reportable but informational-leaning); sub-lead 2 orphaned-secret realization inherits the private-key-recovery severity of hub Area 1 (Medium–High) *when* chained.

### Area 4 — Doc-vs-IAM-reference integrity on key type (Lens U, minor, NET-NEW)
**Background:** The page and the EC2 console support **ED25519** key pairs for Linux (create and import). But the IAM Service Authorization Reference Descriptions read: `CreateKeyPair` = *"create a **2048-bit RSA** key pair"* (`list_ec2.md:5248`) and `ImportKeyPair` = *"import a public key from an **RSA** key pair created with a third-party tool"* (`list_ec2.md:8670`) — both omit ED25519 entirely.

**Security Concern:** A pure doc-vs-API capability inconsistency (Lens U "diff the capability column against the control-plane"). No authorization decision is known to key on the Description string, so impact is low — but if any customer tooling or governance scanner parses the IAM reference Description to infer "this account only allows RSA key creation," it would be relying on a stale/narrow AWS statement contradicted by the feature.

**High-level Test Scenarios:** Document-only: confirm no IAM evaluation or launch-time control reads the action Description (it is metadata); file the inconsistency as an AWS-owned reference-accuracy defect.
**Doc evidence:** page type list (RSA + ED25519); `list_ec2.md:5248`, `8670`.
**Severity-if-true:** Informational / Low (AWS-owned doc-vs-API inconsistency, per Lens U severity framing).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Import a 1024-bit (weak) RSA key despite an org "strong keys only" mandate | `ec2:ImportKeyPair` | Attack the assumption that any IAM condition key can floor key strength on import — none exists |
| Import an RSA key where only ED25519 was intended | `ec2:ImportKeyPair` | Attack the assumption that `ec2:KeyPairType` (which works on Create) also scopes Import — it is absent there |
| Crash / confuse the multi-format public-key parser | EC2 control-plane key parser | Attack the assumption that DER/RFC4716/OpenSSH parsing of attacker bytes is robust and deterministic |
| Store the CFN private key under a weaker key / orphan it on failed delete | `AWS::EC2::KeyPair` + SSM `SecureString` | Attack the assumption that the AWS-published snippet protects the key as well as EC2-native storage would |
| Rely on the IAM reference Description to infer allowed key types | `list_ec2` action metadata | Attack the assumption that the capability statement matches the live feature set |

## 7. Out-of-Scope Risk Categories
- The hub's leads (CFN→SSM reachability, KeyPairId discovery, name-scoping asymmetry, land-grab, sample-policy audit, fingerprint confusion, EIC twin) — owned by `ec2-key-pairs-attack-research-plan.md`; cross-referenced, not re-tested here.
- SSM Parameter Store / KMS managed-key internals (shared infrastructure) — only the EC2-induced *reachability/storage choice* via the CFN snippet is in scope.
- Client-side `fileb://` / `file://` / `--query … > file` behavior — local CLI file I/O, not a server-dereferenced URL (see §8, Lens G null).
- Customer-authored IAM mistakes not sourced from an AWS-published artifact — least-privilege footguns the customer owns.
- SSH client / OpenSSH / PuTTY vulnerabilities; `.ppk` PuTTY format conversion bugs — third-party, out of this doc set.
- Guessing a `KeyPairId` by brute force — relies on *disclosure* paths (hub Area 2), not entropy; not re-opened here.
- The 5,000-key-pairs-per-Region cap as a DoS — single-account, support-case-raisable, no cross-tenant sharing indicated (Lens L weak signal, see §8).

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF): N/A.** Checked all three creation paths on this page. `--public-key-material fileb://…` and `--query KeyMaterial --output text > file` are **client-side botocore file operations** (wire-identical to inline bytes); there is no field this page's service *dereferences* server-side (no URL/host/`*Uri`). `PublicKeyMaterial` is parsed as key bytes, not fetched as a reference.
- **Lens A (cross-tenant IDOR): N/A on this page.** Create/Import only *produce* a resource in the caller's own account+Region; no resource-by-foreign-id read. Cross-account disclosure of the *produced* secret is the hub's Lens-T concern, not an IDOR on this page.
- **Lens B/C (PassRole / credential vending): N/A.** No role-ARN parameter in any of the three paths. CloudFormation's own execution-role PassRole is a stack-level concern, not key-pair-specific.
- **Lens H (CMK / encryption-context): doc-gap, folded into Area 3.** The page never names the KMS key behind the SSM `SecureString`; default is `alias/aws/ssm` per general SSM behavior — confirm against SSM docs before testing the hub's Lens-T decrypt-delegation scenario.
- **Lens L (resource exhaustion): weak signal only.** 5,000 key pairs/Region cap, support-case-raisable; no indication of a tenant-shared pool → self-DoS at most, out of scope.
- **Lens D/V/K/M/N/J/P/W/Y/AA/BB/CC/DD/FF: N/A.** No network/ENI path, no LLM/agent, no session/one-time-token, no ARN migration, no 3P OAuth, no proofing/OTP gate, no attestation condition, no `http://`/TLS-floor/SigV2 language, no RAM/cross-account share mechanism for key pairs, no multi-parser routing of a *request*, no upstream-asserted identity header, no caching of an authz decision, no JWT/OIDC — none appear on `create-key-pairs.html`. (Transport: standard SigV4 throughout; not independently verified against the API Reference's transport section — doc-gap if deeper transport analysis is wanted.)
- **Offline-vs-online drift:** none of substance — `/work/aws-docs/.../create-key-pairs.md` differs from the live `.md` twin only in frontmatter and trailing whitespace. IAM facts read from the offline `list_ec2.md` mirror (slug `list_ec2`; `list_amazonec2` is dead — see the reference-URL memory).

**Carried doc-gaps for the hunter:** (1) does the EC2 import parser enforce any *maximum* key length beyond 4096, or silently accept larger (Area 2)? (2) is the CFN `SecureString` ever placeable under a CMK via the resource, or is it hard-wired to the default key (Area 3 sub-lead 1)? (3) does the fabricated-parameter-name probe ever surface a *real* adjacent parameter in any error path (Area 3 sub-lead 2)? Settle (1)/(3) with scoped canary calls; (2) against the `AWS::EC2::KeyPair` CFN resource reference. See `ec2-key-pairs-attack-research-plan.md` (hub) and the `reference-aws-iam-service-auth-ref-url` memory for fetch technique.
