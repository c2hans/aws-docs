# Amazon EC2 Key Pairs — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` (hub: `ec2-key-pairs.md` and its children `create-key-pairs.md`, `describe-keys.md`, `delete-key-pair.md`, `replacing-key-pair.md`, `verify-keys.md`, plus adjacent pages `TroubleshootingInstancesConnecting.md#replacing-lost-key-pair`, `ExamplePolicies_EC2.md`, `iam-policies-for-amazon-ec2.md`, `ec2-instance-connect-configure-IAM-role.md`, `ec2-instance-connect-methods.md`), cross-checked against the live twins (`*.html` pages fetched directly, no drift found on the hub page). Authoritative IAM surface: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (slug `list_ec2`) and `list_ec2-instance-connect.md`. CloudFormation resource reference: `AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.html` (fetched live; no offline mirror found under this tree).

Status: documentation-derived hypotheses only. Nothing has been tested against a live AWS account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives

1. Determine whether a principal who is denied all `ec2:*KeyPair*` actions can still obtain the cleartext private key material of a CloudFormation-generated key pair via the SSM Parameter Store path it is written to.
2. Determine whether the SSM parameter path (`/ec2/keypair/{key_pair_id}`) is discoverable by a principal holding only weaker/unrelated permissions (`ec2:DescribeKeyPairs`, `cloudformation:DescribeStacks`/`GetAtt`), independent of any key-pair-scoped IAM grant.
3. Determine whether `ec2:DescribeKeyPairs`' documented lack of resource-level permissions lets any principal with that single action enumerate every key pair (and, with `--include-public-key`, every public key) in the account regardless of tag-based ABAC intended to scope access.
4. Determine whether the asymmetric condition-key coverage across the `CreateKeyPair` / `ImportKeyPair` / `DeleteKeyPair` family (missing `ec2:KeyPairName` on Create/Import, missing `ec2:KeyPairType` and any public-key-content key on Import) lets a principal bypass a naming or key-type restriction intended by a least-privilege policy author.
5. Determine whether a stack update/rollback/delete failure on `AWS::EC2::KeyPair` can leave the SSM private-key parameter orphaned (secret outliving the resource) due to the documented separate `ssm:DeleteParameter` permission check.
6. Determine whether `ImportKeyPair` lets one principal plant attacker-chosen public key material under a name another principal/role later launches instances with (no condition key binds the imported key's content to anything the service can gate on).

## 2. Components, Assets, and Design

**Customer-facing interface:** `ec2:CreateKeyPair`, `ec2:ImportKeyPair`, `ec2:DeleteKeyPair`, `ec2:DescribeKeyPairs` (SigV4 API/CLI/console/PowerShell), plus the CloudFormation resource type `AWS::EC2::KeyPair` which wraps `CreateKeyPair`/`ImportKeyPair`/`DeleteKeyPair` via the CloudFormation service.

**Assets:**
- The **public key** — stored by Amazon EC2 itself (resource type `key-pair`, ARN `arn:${Partition}:ec2:${Region}:${Account}:key-pair/${KeyPairName}`); placed onto an instance's `~/.ssh/authorized_keys` at first boot (`ec2-key-pairs.md` line 16).
- The **private key** — for console/CLI-generated key pairs, EC2 **never stores it** ("Amazon EC2 doesn't keep a copy of your private key" — `ec2-key-pairs.md`). For CloudFormation-generated key pairs, the private key **is** persisted: "the private key is saved to AWS Systems Manager Parameter Store, using a parameter with the following name: `/ec2/keypair/{key_pair_id}`" (`create-key-pairs.md` lines 105-108; confirmed on the CFN resource page: "the private key is saved to AWS Systems Manager Parameter Store... When CloudFormation deletes a key pair that was created or imported by a stack, it also deletes the parameter").
- The **KeyPairId** (needed to construct the SSM path) — a second-class identifier, not the primary name, obtainable through at least two unrelated, weaker-permission surfaces (see Trust-Boundary Map row 1).

**Processes involved:** the EC2 control plane (owns `key-pair` resource type and public-key storage); the CloudFormation service (orchestrates `CreateKeyPair`/`ImportKeyPair`/`DeleteKeyPair` and separately writes/deletes the SSM parameter); AWS Systems Manager Parameter Store (owns the `SecureString` parameter and its KMS-based encryption — default managed key, per general SSM behavior; the EC2/CFN docs do not themselves name the KMS key — **doc gap**).

**Pipeline (CloudFormation path):**
```
customer template (AWS::EC2::KeyPair)
        │
        ▼
CloudFormation service  ──ec2:CreateKeyPair/ImportKeyPair──▶  EC2 control plane (stores PUBLIC key, mints KeyPairId)
        │                                                              │
        └──ssm:PutParameter (SecureString, default KMS key)──▶  SSM Parameter Store
                                                                 /ec2/keypair/{KeyPairId}  (PRIVATE key, created-only, not on import)
```
Reader path: `aws ssm get-parameter --name /ec2/keypair/{id} --with-decryption` (`create-key-pairs.md` line 140) — a completely different IAM namespace (`ssm:GetParameter` + `kms:Decrypt`) than the one that created the secret (`ec2:CreateKeyPair`).

**Identity model:** standard SigV4 IAM; no separate key-pair-specific authentication. Resource identified by **name** for most actions (`key-pair/${KeyPairName}` ARN) but by **KeyPairId** for the SSM storage path — two different identifier spaces for the same object (role flag for Lens A's "two ways to name one resource").

**Roles/privilege levels:** no key-pair-specific roles; ordinary IAM principals. The interesting split is CloudFormation's execution role (or the caller, if no service role is configured) needing *both* EC2 key-pair permissions *and* separate, independently-grantable SSM permissions (`ssm:PutParameter`, `ssm:DeleteParameter`) — see `create-key-pairs.md` "Required IAM permissions" block (Lens R trigger).

**Where untrusted data enters:** `ImportKeyPair`'s `PublicKeyMaterial` parameter is attacker-choosable public key bytes, written into `~/.ssh/authorized_keys` the moment an instance referencing that key name boots. No IAM condition key exists to inspect or constrain the content of this field.

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Principal denied all `ec2:*KeyPair*` / `cloudformation:*` on the key-pair resource | SSM Parameter Store `/ec2/keypair/{id}` (private key) | `ssm:GetParameter --with-decryption`, authorized purely under the SSM/KMS namespace | **Breach:** the denied principal retrieves cleartext private key material. |
| Principal holding only `ec2:DescribeKeyPairs` (no `ec2:*KeyPair*` write access, no tag-matching ABAC grant) | Every key pair in the account (names, IDs, fingerprints, and — with `--include-public-key` — public key material) | `DescribeKeyPairs` has **no resource types** and only `ec2:Region` as a condition key (`list_ec2.md:7086-7090`) | **Breach-adjacent (by design, but a lead for ABAC-dependent customers):** a tag-scoped allow policy on other key-pair actions provides **zero** scoping on Describe — any grant of this single action discloses the full account inventory. |
| Principal holding only `cloudformation:DescribeStacks` / stack-outputs read access (no EC2 or SSM permission at all) | `KeyPairId` (`Fn::GetAtt NewKeyPair.KeyPairId`), the input needed to build the SSM path | CFN exposes `KeyPairId` as a `GetAtt` attribute; stacks commonly surface it as an Output | **Breach:** a principal with zero EC2/SSM IAM grants learns the deterministic SSM path, enabling the first row's attack once paired with any SSM read access elsewhere. |
| Principal holding `ec2:ImportKeyPair` scoped only by tag/Region conditions | Any instance later launched with that key name (by any principal with `ec2:RunInstances` + that `key-pair` resource) | No condition key binds/validates `PublicKeyMaterial` content; `ec2:KeyPairType`/`ec2:KeyPairName` are **absent** from `ImportKeyPair`'s condition-key set (`list_ec2.md:3598-3600`, `8669-8673`) | **Breach:** attacker-supplied public key lands in `authorized_keys` on an instance the attacker cannot otherwise reach, because nothing lets the resource owner restrict *what* gets imported under a name they don't yet control, or restrict import to a name pattern. |
| CloudFormation stack lifecycle (create → update-replace → delete) | SSM parameter lifecycle | All `AWS::EC2::KeyPair` properties are `Update requires: Replacement`; delete of the old resource is supposed to delete its SSM parameter, gated by a **separate** `ssm:DeleteParameter` permission check (`create-key-pairs.md:143-149`) | **Breach:** a stack operation that creates a new key pair/parameter but fails (denied/rolled back) before or during deletion of the old one leaves the private key parameter live under a KeyPairId no longer tracked by any CloudFormation resource — "secret outlives the resource." |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:CreateKeyPair` | API/CLI/Console | Existing | Mutating | External | Generates RSA/ED25519 key pair, returns private key once, stores public key | Yes (SigV4) | Any IAM principal w/ grant | Resource `key-pair*`; condition keys: `aws:RequestTag`, `aws:TagKeys`, `ec2:KeyPairType`, `ec2:Region`. **No `ec2:KeyPairName`** — cannot restrict which *names* a principal may create. |
| `ec2:ImportKeyPair` | API/CLI/Console | Existing | Mutating | External | Imports caller-supplied public key material | Yes | Any IAM principal w/ grant | Resource `key-pair*`; condition keys: `aws:RequestTag`, `aws:TagKeys`, `ec2:Region` only. **No `ec2:KeyPairName`, no `ec2:KeyPairType`, and `ec2:PublicKey` does not exist as a condition key anywhere in `list_ec2.md`.** |
| `ec2:DeleteKeyPair` | API/CLI/Console | Existing | Mutating | External | Removes stored public key | Yes | Any IAM principal w/ grant | Resource `key-pair`; condition keys: `aws:ResourceTag`, `ec2:KeyPairName`, `ec2:KeyPairType`, `ec2:Region`, `ec2:ResourceTag`. Only action in the family that can be scoped by name. |
| `ec2:DescribeKeyPairs` | API/CLI/Console | Existing | Non-mutating | External | Lists key pairs; `--include-public-key` returns public key material | Yes | "All customers" (account-wide) | **No resource types at all**; only `ec2:Region`. Confirmed by `ec2-instance-connect-configure-IAM-role.md`: "`ec2:Describe*` API actions do not support resource-level permissions... the `*` wildcard is necessary." |
| `ssm:GetParameter` / `ssm:PutParameter` / `ssm:DeleteParameter` | API/CLI | Existing (different service) | Mixed | External | Reads/writes the CFN-created private key `SecureString` at `/ec2/keypair/{id}` | Yes | Whoever holds SSM grants — **independent of EC2 key-pair IAM** | Non-SDK-adjacent cross-service path; the actual secret-reachability surface (Lens T). |
| `cloudformation:AWS::EC2::KeyPair` (Create/Update/Delete via stack ops) | CFN | Existing | Mutating | External | Orchestrates the above + SSM write/delete | Yes | Stack's execution role or caller | All properties `Update requires: Replacement`; `GetAtt KeyPairId`/`KeyFingerprint` exposed to anyone who can read the stack. |
| `ec2-instance-connect:SendSSHPublicKey` | API/CLI/Console | Existing | Mutating | External | Pushes a temporary (60s) SSH public key into instance metadata, bypassing the long-lived key-pair resource entirely | Yes | Any IAM principal w/ grant | Resource `instance`; condition keys `ec2:osuser` (note: lowercase, undocumented-case gotcha), `aws:ResourceTag`, `ec2:ResourceTag`. A structurally separate "key" mechanism — see Lens X. |

Flagged per the skill's "undocumented knob" hunt: `ec2:ImportKeyPair`'s total absence of a content- or type-scoping condition key is the single most consequential gap in this inventory — it is accepted by the API/SDK with no public/console warning that import cannot be restricted beyond tag/Region.

## 5. Recommended Areas of Focus

### Area 1 — Cross-service secret reachability: CFN-generated private key via SSM (Lens T) [PRIMARY]
**Background:** `create-key-pairs.md` states plainly that CloudFormation-created key pairs have their private key "saved to AWS Systems Manager Parameter Store, using a parameter with the following name: `/ec2/keypair/{key_pair_id}`," retrieved via `aws ssm get-parameter --name /ec2/keypair/{id} --with-decryption`. This is a `SecureString`, which by default SSM behavior is encrypted under the AWS-managed key `alias/aws/ssm` unless a customer-managed key is specified (not mentioned anywhere in the EC2 or CFN pages — doc gap, confirm against SSM Parameter Store docs before testing).

**Security Concern:** The API that *creates* the secret (`ec2:CreateKeyPair`, inside CloudFormation's execution) and the API that *reads* the secret (`ssm:GetParameter`) live in two different IAM namespaces with two different, independently-grantable permission sets. A least-privilege policy author who diligently denies `ec2:CreateKeyPair`/`ec2:ImportKeyPair`/`ec2:DeleteKeyPair` to a principal has done nothing to the SSM side.

**High-level Test Scenarios:**
1. As principal A, create a CFN stack containing `AWS::EC2::KeyPair` (no `PublicKeyMaterial`, i.e. a generated key). Note the `KeyPairId` via `Fn::GetAtt`.
2. As principal B — explicitly denied `ec2:CreateKeyPair`, `ec2:ImportKeyPair`, `ec2:DeleteKeyPair`, `ec2:DescribeKeyPairs` — attempt `ssm:GetParameter --name /ec2/keypair/{id} --with-decryption`. If B holds any `ssm:GetParameter`/`kms:Decrypt` grant not scoped away from this path (e.g. a broad `parameter/*` grant typical of ops roles), does the call succeed and return cleartext key material?
3. Check B's decrypt preconditions. **CORRECTED 2026-10-15 (see §9):** AWS docs state that for the default `aws/ssm` managed key "you cannot establish access control policies," and that decrypting any `SecureString` value "the user needs `kms:Decrypt` permission" — so decrypt is gated by `kms:Decrypt` **in B's identity policy**, not by a `kms:ViaService` delegation on the key policy (that delegation is **not documented** for this key — do not assert it). The realistic precondition is therefore B holding a *broad* `ssm:GetParameter` **and** `kms:Decrypt` (e.g. ops/`parameter/*` + `kms:Decrypt` on `*`), not SSM access alone. Confirm live whether an account-root/`ViaService` grant nonetheless exists on `aws/ssm` (undocumented but historically present) — if so the precondition drops back to `ssm:GetParameter` only.
4. Delete the stack; immediately re-run the `GetParameter` call. Does the parameter still resolve (secret outliving the resource) if `ssm:DeleteParameter` was denied mid-delete, or if the delete only ran against a "fabricated" probe name per the documented import-vs-create distinction (`create-key-pairs.md` lines 143-149)?

**Doc evidence:** `create-key-pairs.md` lines 105-111, 137-149; CFN resource page `aws-resource-ec2-keypair.html` ("When CloudFormation deletes a key pair that was created or imported by a stack, it also deletes the parameter...").
**Severity-if-true:** Medium–High (per the skill's Lens T framing) — private-key recovery bypassing an IAM wall the customer believed was closing off key-pair access entirely. Owner-to-fix likely shared: AWS owns the managed-key delegation default and the cross-service storage choice; customer owns the least-privilege composition that must now additionally cover `ssm:*`/`kms:*`.

### Area 2 — Predictable/discoverable KeyPairId as the sole gate to Area 1 (Lens EE-adjacent / Lens U)
**Background:** The SSM path is keyed by `KeyPairId`, not `KeyPairName`. `KeyPairId` is obtainable via `describe-key-pairs --query KeyPairs[*].KeyPairId` (any principal with the unscopable `ec2:DescribeKeyPairs`) **or** via CloudFormation's `Fn::GetAtt KeyPairId` / stack Outputs (any principal who can read the stack, with zero EC2 IAM grants).

**Security Concern:** Two independent, lower-privilege disclosure paths exist for the one input Area 1's attack needs. Neither is gated by anything resembling a `key-pair`-scoped IAM condition.

**High-level Test Scenarios:**
1. Confirm `DescribeKeyPairs` truly ignores tag-based scoping intended elsewhere in the account's ABAC model — call it under a principal that holds `ec2:DescribeKeyPairs` with no `Resource`/condition restriction (the only form the API supports) and verify every key pair account-wide is returned, including ones whose other actions (Create/Delete) are tag-scoped away from this principal.
2. Confirm `cloudformation:DescribeStacks` (or `ListExports`) on a stack containing `AWS::EC2::KeyPair` discloses `KeyPairId` to a principal with no `ec2:*` grant at all.

**Doc evidence:** `list_ec2.md:7086-7090`; `ec2-instance-connect-configure-IAM-role.md` line 28-29 ("`ec2:Describe*` API actions do not support resource-level permissions"); CFN `Fn::GetAtt` section listing `KeyPairId`.
**Severity-if-true:** Low standalone (an ID, not a secret) but **escalates Area 1 to High** when chained — compose per Step 5's "kill chain" guidance: rate at the severity of the chain's end (cleartext private key), not the entry point (an ID lookup).

### Area 3 — Condition-key asymmetry across the Create/Import/Delete family (Lens S)
**Background:** `list_ec2.md` shows: `CreateKeyPair` condition keys = `aws:RequestTag`, `aws:TagKeys`, `ec2:KeyPairType`, `ec2:Region` (no `ec2:KeyPairName`). `ImportKeyPair` condition keys = `aws:RequestTag`, `aws:TagKeys`, `ec2:Region` only (no `ec2:KeyPairName`, no `ec2:KeyPairType`). `DeleteKeyPair` condition keys = `aws:ResourceTag`, `ec2:KeyPairName`, `ec2:KeyPairType`, `ec2:Region`, `ec2:ResourceTag`.

**Security Concern:** A policy author who writes `"Condition": {"StringLike": {"ec2:KeyPairName": "dev-*"}}` on `CreateKeyPair` or `ImportKeyPair` — a natural generalization from the fact that this key *does* work on `DeleteKeyPair`, `RunInstances`, `CreateTags`, `RequestSpotFleet`, and `RequestSpotInstances` (all confirmed in `list_ec2.md`) — gets **no error and no enforcement**; the condition key is silently absent from evaluation for the two creation-side actions. Likewise, nothing can scope `ImportKeyPair` by the public key's type or content (`ec2:PublicKey` is not a real condition key — confirmed by exhaustive grep of `list_ec2.md`), so a policy intending "only import ED25519 keys" or "never import a key matching known-bad fingerprint X" has no IAM mechanism at all.

**High-level Test Scenarios:**
1. Author a policy granting `ec2:CreateKeyPair` conditioned on `ec2:KeyPairName: "dev-*"` via `StringLike`. Attempt to create a key pair named `prod-admin`. Per the IAM reference, this condition key is not supported for this action — confirm whether IAM silently drops the unsupported condition (treating the statement as unconditioned Allow) or denies by default.
2. Author a policy granting `ec2:ImportKeyPair` with no path to restrict `KeyType`; import an RSA key where only ED25519 was intended to be allowed; confirm no enforcement point exists.

**Doc evidence:** `list_ec2.md:561-562` (`CreateKeyPair`), `3598-3600` (`ImportKeyPair`), `1040-1041`/`5986-5990` (`DeleteKeyPair`), `9966` (key-pair resource type's full condition-key list, which is the union — showing `ec2:KeyPairName`/`ec2:KeyPairType` *exist* as keys, just not wired to Create/Import).
**Severity-if-true:** Medium (condition-key-is-the-access-control-mechanism scenario per Lens S's severity framing) — this is the IAM reference's own documented behavior, not a hidden bug, but it is exactly the kind of sparse/asymmetric condition-key set the skill flags as a lead in its own right.

### Area 4 — ImportKeyPair as attacker-controlled credential injection (Lens A/Q hybrid)
**Background:** `ImportKeyPair` accepts arbitrary `PublicKeyMaterial` (`create-key-pairs.md` "Requirements for key pairs"), which later gets placed verbatim into `~/.ssh/authorized_keys` on any instance that references the key pair name at launch (`ec2-key-pairs.md` line 16).

**Security Concern:** Within one account, a principal holding only `ec2:ImportKeyPair` (tag/Region-scoped, per Area 3's finding) can import a key pair under any **name not already taken** (name is a flat per-account+region namespace — `arn:...:key-pair/${KeyPairName}`). If any launch workflow elsewhere in the account (a launch template, an Auto Scaling group, CI/CD) references a key pair *by a name that principal can predict and does not yet exist*, that principal's imported public key becomes the credential for whoever launches against that name next — a land-grab (Lens EE) on the key-pair name namespace, same shape as AMI-name or bucket-name pre-registration.

**High-level Test Scenarios:**
1. Identify (from launch templates, Auto Scaling configs, or `RunInstances` call patterns elsewhere in the account) a key pair name that is referenced but does not yet exist (e.g. a template created before its key pair, or a key pair deleted per `delete-key-pair.md`'s explicit statement that deleting the EC2-side public key does **not** update any referencing launch template/configuration).
2. `ImportKeyPair` under that exact name with an attacker-controlled public key.
3. Trigger (or wait for) the launch workflow (e.g. an unhealthy-instance replacement in an Auto Scaling group) to fire with that key name.
4. Confirm oracle: the attacker's private key now authenticates as the default system user on the newly launched instance.

**Doc evidence:** `delete-key-pair.md` line 13 (Auto Scaling / launch template warning — explicitly says instance launch *fails* if the key is missing, implying launches *will* pick up any key pair later created under that exact name); `create-key-pairs.md` Requirements section (no server-side authenticity check on imported key content).
**Severity-if-true:** High if it lands on a shared/production launch path; this is the EE "predictable-name land-grab" lens applied to the `key-pair` namespace, which the catalog explicitly calls out as a precedent-backed pattern (Bucket Monopoly, whoAMI).

### Area 5 — AWS-authored sample-policy audit (Lens R)
**Background:** `ExamplePolicies_EC2.md`'s `RunInstances` AMI-restriction examples (lines 229-300) both grant `"arn:...:key-pair/*"` **unconditioned** alongside the AMI restriction — i.e., the sample's intent ("restrict which AMIs can be launched") is paired with a blanket allow on every key pair in the account.

**Security Concern:** A customer who copies this AWS-published sample verbatim (as the skill's Lens R explicitly treats as in-scope, non-footgun, AWS-owned surface) gets AMI restriction but **no** key-pair restriction, even though the surrounding narrative is about restricting `RunInstances` inputs. This is a case where the sample's own scope could silently mislead a reader into believing the whole launch surface is constrained.

**High-level Test Scenarios:**
1. Walk every `RunInstances` sample in `ExamplePolicies_EC2.md` that includes `key-pair/*` in its `Resource` list (lines 251, 294, 338, 380, 413, 455, 499, 575, 635, 735, 842, 1037, 1071, 1113, 1157, 1200, 1255) and confirm none of them pair it with an `ec2:KeyPairName` condition — i.e., every single sample grants launch-with-any-key-pair.
2. Determine (as a documentation finding, not a code bug) whether this is intentional (RunInstances legitimately needs *a* key-pair resource grant to launch at all, regardless of which key) or whether AWS should show at least one example scoping `ec2:KeyPairName` for defense-in-depth, given the key support exists per Area 3.

**Doc evidence:** `ExamplePolicies_EC2.md` lines 246-258, 289-300 (and the 15 other `key-pair/*` occurrences listed above).
**Severity-if-true:** Informational/Low — a documentation-completeness gap, not a privilege-escalation vector (RunInstances-with-any-key-pair is normal and expected), but recorded per the skill's mandate to audit every shipped sample statement-by-statement.

### Area 6 — Fingerprint algorithm confusion as a verification bypass (Lens U, minor)
**Background:** `verify-keys.md` documents that EC2 computes fingerprints with **different hash functions** depending on provenance: SHA-1 (RSA, EC2-created) vs MD5 (RSA, imported) vs SHA-256 (ED25519, either). "If you import a public RSA key to Amazon EC2, the fingerprint is calculated using an MD5 hash function. This is true regardless of how you created the key pair."

**Security Concern:** A user who re-imports a public key derived from an EC2-created private key gets a **different fingerprint** than the original (SHA-1 vs MD5), explicitly flagged in the doc itself as a point of confusion ("the imported public keys will have a different fingerprint than the original"). This is purely a usability/verification-reliability issue — a user who treats "fingerprint changed" as a tamper signal would get a false positive — not an access-control bypass, since fingerprint is not used as an authorization input anywhere in the IAM surface (confirmed: no `ec2:*Fingerprint*` condition key exists in `list_ec2.md`).
**High-level Test Scenarios:** Document-only confirmation that no IAM or launch-time control relies on fingerprint equality; this is a user-facing integrity-verification footgun, not a security boundary.
**Doc evidence:** `verify-keys.md` lines 17-28, 36-37.
**Severity-if-true:** Informational.

### Area 7 — EC2 Instance Connect as a parallel, un-tag-aligned "key" mechanism (Lens X)
**Background:** `ec2-instance-connect-methods.md` line 10: EC2 Instance Connect "automatically pushes an SSH public key to the instance metadata where it remains for 60 seconds," authorized purely by `ec2-instance-connect:SendSSHPublicKey` + the `ec2:osuser` condition key (lowercase, confirmed in `list_ec2-instance-connect.md:84`) — a structurally separate authorization path to the exact same outcome (SSH access) that the long-lived `key-pair` resource governs, but scoped to `instance` ARNs/tags, with **no relationship at all** to any `key-pair` resource, name, or tag.

**Security Concern:** A customer who locks down the `key-pair` resource family tightly (per Areas 1-4) but grants `ec2-instance-connect:SendSSHPublicKey` broadly (`Resource: "*"`, the configuration the doc explicitly warns about: "Otherwise, all IAM principals with permission for the `ec2-instance-connect:SendSSHPublicKey` action can connect to all EC2 instances" — `ec2-instance-connect-configure-IAM-role.md` line 14) has left the family's intended protection moot: the twin/cousin action bypasses it entirely.

**High-level Test Scenarios:**
1. Enumerate accounts/roles granted `ec2-instance-connect:SendSSHPublicKey` with `Resource: "*"` and no tag condition — confirm per the doc's own warning that this grants SSH to every instance regardless of any key-pair-level restriction.
2. Confirm `ec2:osuser`'s exact casing in any customer-authored policy a hunter encounters live — a policy mistakenly written with different casing (e.g. `ec2:OSUser`) against this specific, non-standard-cased key would silently fail to match (IAM string-condition evaluation is case-sensitive by key name convention established elsewhere, though the key itself is matched by exact string from the policy language's perspective — confirm against IAM's condition-key case-sensitivity rules before treating as a bug).

**Doc evidence:** `ec2-instance-connect-methods.md` line 10; `ec2-instance-connect-configure-IAM-role.md` lines 9-14; `list_ec2-instance-connect.md` lines 50-53, 84.
**Severity-if-true:** Medium (Lens X action-family-twin pattern) — not cross-account, but a documented sibling-action authorization-parity gap within the same "SSH into an instance" capability.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read a CFN-generated private key despite being denied all EC2 key-pair actions | SSM Parameter Store `/ec2/keypair/{id}` | Separation of `ec2:CreateKeyPair` IAM from `ssm:GetParameter`/`kms:Decrypt` IAM — attack the assumption that denying one denies the other |
| Discover a `KeyPairId` with zero EC2/SSM permissions | CloudFormation stack outputs / `Fn::GetAtt` | Attack the assumption that `KeyPairId` is as protected as the key-pair resource itself |
| Enumerate every key pair (name, fingerprint, public key) in the account via one unscoped action | `ec2:DescribeKeyPairs` | Attack the assumption that tag-based ABAC on Create/Delete also limits Describe |
| Create or import a key pair under a name/type a least-privilege policy intended to forbid | `ec2:CreateKeyPair`, `ec2:ImportKeyPair` | Attack the assumption that `ec2:KeyPairName`/`ec2:KeyPairType` conditions, which work on sibling actions, also work here |
| Land attacker-controlled public key material under a name a victim workflow will launch against | `ec2:ImportKeyPair` + flat per-account name namespace | Attack the assumption that import requires any relationship to the eventual launcher |
| Leave a private-key SSM parameter orphaned after a failed/partial stack delete | `AWS::EC2::KeyPair` lifecycle, `ssm:DeleteParameter` | Attack the assumption that CFN's delete-time permission check guarantees cleanup completes |
| Bypass key-pair-level restrictions via the sibling SSH mechanism | `ec2-instance-connect:SendSSHPublicKey` | Attack the assumption that restricting the `key-pair` resource restricts all SSH-credential paths |

## 7. Out-of-Scope Risk Categories

- The underlying SSM Parameter Store / KMS managed-key service internals (shared infrastructure) — only the EC2-specific *reachability* into that infrastructure via the documented `/ec2/keypair/{id}` path is in scope.
- IMDS/metadata-service behavior on fully-managed hosts generally (covered under a different cluster); only the 60-second EC2 Instance Connect public-key placement into instance metadata is referenced here, as a comparison point for Area 7.
- Any customer-authored IAM policy mistake (over-broad `Resource: "*"` the customer themselves wrote without AWS's `ExamplePolicies_EC2.md` as the direct source) — a least-privilege footgun the customer owns, not AWS.
- Brute-forcing/guessing a `KeyPairId` directly (it is not shown to have low entropy in these docs; the leads above rely on *disclosure* paths, not guessing).
- SSH client-side vulnerabilities (OpenSSH/PuTTY bugs) — out of scope for this documentation set.
- Windows password-decryption-via-private-key flow — mentioned once (`ec2-key-pairs.md` line 8) but not elaborated in this doc cluster; would need `connecting_to_windows_instance.md` for a dedicated pass (not requested in scope).

## 8. Null hypotheses / doc gaps

- **Lens B/C (PassRole/credential vending):** N/A — checked `create-key-pairs.md`, `ec2-key-pairs.md`, `delete-key-pair.md`, `describe-keys.md`, `replacing-key-pair.md`, `verify-keys.md`; no role-ARN-accepting parameter anywhere in the key-pair family. CloudFormation's own execution-role PassRole concern is a stack-level concern already covered elsewhere, not key-pair-specific.
- **Lens D/V (data-plane→control-plane / network segmentation):** N/A for this cluster — key-pair actions are control-plane-only API calls; no ENI/network path. Checked all five hub children plus `TroubleshootingInstancesConnecting.md`.
- **Lens F (translation-layer injection):** N/A — no parser/wire-protocol translation in the key-pair create/import/delete/describe path. (EC2 Instance Connect's SSH negotiation is a different mechanism, out of this cluster's primary scope; noted only as Area 7.)
- **Lens G (SSRF):** N/A — no field in any key-pair page is a URL/host the service dereferences. Checked all five hub children; `PublicKeyMaterial` is parsed as key material, not a reference.
- **Lens H (CMK/encryption-context confusion):** Partial doc-gap — the SSM `SecureString`'s KMS key is never named in the EC2 or CFN pages reviewed (`create-key-pairs.md`, `aws-resource-ec2-keypair.html`). Flagged inside Area 1 rather than as a standalone lens; needs the SSM Parameter Store docs to resolve definitively — doc-gap, confirm surface first.
- **Lens J (OAuth/3P linking):** N/A — no 3P integration in this cluster.
- **Lens K (prompt injection):** N/A — no LLM/agent component anywhere in the key-pair docs.
- **Lens L (resource exhaustion):** Weak signal only — `create-key-pairs.md` notes a 5,000-key-pairs-per-Region cap with a support-case path to raise it; no indication this is tenant-shared or exploitable for cross-tenant DoS. Checked `create-key-pairs.md` only; no other size/rate limit text found in the cluster.
- **Lens M (shared-identifier interception):** N/A — no session/presigned-URL/one-time-token concept in this cluster. (EC2 Instance Connect's 60-second temporary key, Area 7, is the nearest analog and is covered there.)
- **Lens N (namespace/ARN migration):** N/A — `key-pair` ARN format is stable and singular; no legacy/dual-namespace language found.
- **Lens O (audit-log evasion):** N/A — no CloudTrail/audit-log statements appear anywhere in the five hub children or `TroubleshootingInstancesConnecting.md`. Doc-gap if a hunter needs this: confirm against the general EC2 CloudTrail logging reference, not covered in this cluster's pages.
- **Lens P (identity proofing/registration):** N/A — no onboarding/OTP/uniqueness-gate workflow for key pairs beyond the flat name-uniqueness implicitly enforced by the `key-pair/${KeyPairName}` ARN itself (which Area 4 already treats as a land-grab vector, not a proofing gate).
- **Lens W (attestation-conditioned auth):** N/A — no `kms:RecipientAttestation`/enclave language in this cluster.
- **Lens Y (transport/TLS/sigversion):** N/A — no `http://`, TLS-floor, or SigV2 language in the key-pair pages; standard SigV4 API calls throughout. Not independently verified against the API Reference's transport requirements — doc-gap if deeper transport analysis is wanted.
- **Lens AA (share/revoke lifecycle):** Partial — no RAM/cross-account share mechanism for key pairs exists at all (key pairs are not shareable resources per these docs), so the lens's primary trigger is absent; the closest analog, "does delete cascade cleanup," is already captured as Area 1/the Threat Model table's orphaned-parameter row rather than a separate AA write-up.
- **Lens BB/CC/DD/FF (canonicalization, trusted-header injection, cache-key divergence, JWT/OIDC confusion):** N/A — none of these mechanisms (multi-layer routing, upstream-asserted identity headers, caching, bearer tokens) appear anywhere in the key-pair API surface. Checked all five hub children, `ExamplePolicies_EC2.md`, `iam-policies-for-amazon-ec2.md`, and both EC2 Instance Connect IAM pages.
- **Offline-vs-online drift:** None found. The offline `ec2-key-pairs.md` hub matches the live `.html` page's topic list and prose verbatim (both list exactly five child topics: create, describe, delete, replace, verify). The CloudFormation `AWS::EC2::KeyPair` resource page has no offline mirror under the paths searched; all CFN-specific detail in this plan was sourced live and cross-checked against the EC2-side description in `create-key-pairs.md`, which is consistent.

## 9. Verification Addendum (2026-10-15 — live-doc confirmation pass)

A second pass re-fetched the live online sources (`list_ec2.html` = 35,512 lines; the EC2 UserGuide, CFN resource, and KMS/SSM pages) to confirm the load-bearing facts and resolve the §8 Lens-H doc-gap. **All IAM-backbone claims verified; two facts corrected.**

**Confirmed against live `list_ec2.html` (condition-key cells per action):**
- `CreateKeyPair` → `aws:RequestTag`, `aws:TagKeys`, `ec2:KeyPairType`, `ec2:Region` — **`ec2:KeyPairName` absent** (verified: KeyPairName is first wired at the `DeleteKeyPair` block, not Create). ✓ Area 3.
- `ImportKeyPair` → `aws:RequestTag`, `aws:TagKeys`, `ec2:Region` only — **no `KeyPairName`, no `KeyPairType`** (0 `ec2_KeyPairName` refs in the Import action block). ✓ Areas 3/4.
- `DeleteKeyPair` → `aws:ResourceTag`, `ec2:KeyPairName`, `ec2:KeyPairType`, `ec2:Region`, `ec2:ResourceTag`. ✓ (only family member scopable by name).
- `DescribeKeyPairs` → **only `ec2:Region`, no resource type** (unscopable account-wide read). ✓ Areas 2/3.
- **No `ec2:PublicKey` / `ec2:*Fingerprint` / `ec2:*PublicKey` condition key exists anywhere** (`grep -ci` = 0 across all 35,512 lines). ✓ Area 3/4 — import content/type is structurally un-gateable in IAM.
- Live `ec2-key-pairs.html` hub = 5 children, matches offline verbatim. **No drift.**

**§8 Lens-H doc-gap RESOLVED (updates Area 1):**
- The SSM path `/ec2/keypair/{key_pair_id}` for CFN-**generated** keys is confirmed verbatim on both `aws-resource-ec2-keypair.html` and `create-key-pairs.html` ("the private key is saved to AWS Systems Manager Parameter Store").
- **Neither the CFN nor the EC2 page ever states the parameter is a `SecureString` or names a KMS key** — the `SecureString` nature is *inferred* only from the documented reader command using `--with-decryption`. The default-key fact (`alias/aws/ssm` when no KeyId is supplied) comes from the **SSM/KMS** docs (`parameter-create-console.html`, `kms/.../services-parameter-store.html`), **not** the EC2/CFN pages — so a hunter must confirm the parameter type live.
- **CORRECTION (propagated to Area 1 Scenario 3):** decrypt of a `SecureString` "the user needs `kms:Decrypt` permission," and for the default `aws/ssm` key "you cannot establish access control policies." The `kms:ViaService`-delegation path the original Area 1 asserted is **not documented** — treat Area 1's precondition as `ssm:GetParameter` **+ `kms:Decrypt`**, with the ViaService/root-delegation shortcut demoted to a live-only open question.

**New confirmations that tighten the lifecycle leads:**
- **Imported key pairs get NO SSM parameter written** (CFN page: "AWS CloudFormation does not create or return the private key material when you import a key pair"). ⇒ the orphaned-secret concern (Trust-Boundary row 5 / Threat row 6 / Objective 5) applies to **generated keys only**.
- **`ssm:DeleteParameter` is required even for imported keys** (create page, verbatim): CFN runs a permission check "using a fabricated parameter name that does not match any parameter in your account," so an `AccessDeniedException` may surface a fabricated `/ec2/keypair/...` name. ⇒ a CFN execution role missing `ssm:DeleteParameter` **fails stack deletes of imported-key stacks too** — a cleaner Lens-R/availability lead than the plan's original framing, and the "fabricated name in the error" is itself a minor info-disclosure/confusion signal.
- `AWS::EC2::KeyPair` `Fn::GetAtt` exposes `KeyPairId` + `KeyFingerprint`; `Ref` returns the name. ✓ Area 2 (KeyPairId disclosure with zero EC2/SSM IAM).

**Dead-URL note for hunters:** `systems-manager/latest/userguide/sysman-paramstore-securestring.html` is a soft-404 — use `parameter-create-console.html` and `kms/latest/developerguide/services-parameter-store.html` for SecureString/default-key facts.

**Net verdict:** the plan's priority order is sound and its headline (Area 1, Lens T — CFN-generated private key reachable via SSM under a different IAM namespace) stands, now with a corrected, doc-grounded precondition (`ssm:GetParameter` + `kms:Decrypt`) rather than the weaker `ViaService` assumption. No new firing lens was discovered; coverage of the `ec2-key-pairs.html` cluster is complete.
