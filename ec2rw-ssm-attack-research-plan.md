# EC2Rescue for Windows Server via Systems Manager (`AWSSupport-RunEC2RescueForWindowsTool`) — Attack Research Plan

**Source of leads:**
- Primary: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rw-ssm.html` (mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2rw-ssm.md`) — online `.md` verified byte-identical to mirror.
- Parent / adjacent: `Windows-Server-EC2Rescue.md`, `Linux-Server-EC2Rescue.md`, `ec2rw-cli.md`, `ec2rw-gui.md`.
- Cross-reference (real IAM requirements + allow-patterns, NOT on the EC2 UserGuide page): `/work/aws-docs/docs/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-runec2rescueforwindowstool.md` and `/work/aws-docs/docs/systems-manager/latest/userguide/automation-ec2rescue.md`.
- IAM references: `/work/aws-docs/docs/service-authorization/latest/reference/list_ssm.md`, `list_kms.md`, `list_s3.md`.
- SSM Parameter Store internals: `parameter-store-how-to-retrieve.md`, `secure-string-parameter-kms-encryption.md`, `parameter-store-policy-conditions.md`, `parameter-store-setting-up.md` (all under `/work/aws-docs/docs/systems-manager/latest/userguide/`).

**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Every lead carries a confirm/refute oracle for a downstream hunter (`aws-vuln-hunter`).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **This is a single-tenant, in-account service** (a customer's own Windows EC2 instance, its instance-profile role, the customer's SSM Parameter Store / KMS / S3). There is **no shared AWS service-fleet multi-tenancy on this page.** The dominant finding class is therefore **in-account privilege escalation / lateral movement** and **AWS-authored IAM-artifact defects** (Lens R/S/T/U), NOT cross-tenant isolation.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the Distributor package host, the Support-owned document's internal role, an `awssupport-ssm.*` bucket owned by AWS), stop, preserve evidence, and flag for AWS-Security disclosure. Do not probe AWS-owned infrastructure.
- **Disclosure tiering:** the weak defaults in the *AWS-authored, copy-verbatim* IAM sample policies (§5.2) are **in scope / Tier-2 reportable** (AWS owns the artifact). A customer who then widens a policy themselves is a footgun (out of scope) — but the doc defect that *pressures* them to widen is AWS-owned.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Read a Windows instance's local Administrator password** from SSM Parameter Store as a principal who is *not* authorized to administer that instance (holds only `ssm:GetParameter`, denied `ssm:SendCommand`). → RDP as local admin = instance takeover.
2. **Reset the local Administrator password of an instance you do not own/administer**, purely via an over-broad `ssm:SendCommand` grant on the AWS-authored document, then read the new password (chains to #1).
3. **Write/overwrite another instance's password parameter** from a compromised instance-profile role whose `PutParameter` Resource was widened past a single instance-id (credential poisoning / lateral movement within a shared-role fleet).
4. **Exfiltrate `/collect:all` OS logs to an attacker-controlled or wrong-account S3 bucket** via the free-form bucket-name parameter under the published `Resource:"*"` sample policy.
5. **Redirect the admin-password ciphertext to a KMS key the attacker can also decrypt** by supplying a cross-account/attacker-controlled KMS key id to ResetAccess.
6. **Execute arbitrary PowerShell as the instance role** via the trusted AWS-signed document where the customer believed they had constrained the caller to "safe AWS-owned documents only."

---

## 2. Components, Assets, and Design

**Customer-facing interface:** `aws ssm send-command --document-name AWSSupport-RunEC2RescueForWindowsTool --instance-ids <id> --parameters "Command=<ResetAccess|CollectLogs|FixAll>, Parameters='<free-form>'"`. SigV4 IAM auth. No service endpoint of its own — rides the SSM Run Command / Distributor control plane.

**The document** `AWSSupport-RunEC2RescueForWindowsTool` is an **AWS-owned (Support-authored) SSM document**. It: (a) downloads + "verifies" EC2Rescue for Windows Server via the **SSM Distributor package `AWSSupport-EC2Rescue`** (AWS-owned infra; adjacent doc shows artifacts under `arn:aws:s3:::awssupport-ssm.*/*.zip`), (b) imports a PowerShell module, (c) runs `EC2RescueCmd` with the supplied command/parameters **on the customer instance, under the customer instance's IAM role.**

**Commands & their assets:**
| Command | Action | Asset touched | Identifier shape |
|---|---|---|---|
| `ResetAccess` | Resets local Administrator password; stores random pw in SSM Parameter Store | **SecureString at `/EC2Rescue/Password/<INSTANCE_ID>`** (prose) — *but policy grants `/EC2Rescue/Passwords/<instanceid>`*; encrypted with default `alias/aws/ssm` or a caller-supplied KMS key id | path is **deterministic** from `i-0abc...` (17-char instance id, enumerable via `ec2:DescribeInstances`) |
| `CollectLogs` | `/collect:all` → uploads OS logs & config to S3 | **customer S3 bucket**, name supplied free-form in `Parameters` | arbitrary global-namespace bucket name |
| `FixAll` | `/rescue:all` on an offline root volume | block device (e.g. `xvdf`) | device name string |

**Identity / roles:** the **EC2 instance-profile role** is the only identity that writes the parameter / encrypts / uploads to S3. The human/automation caller holds `ssm:SendCommand`. A *separate, later* reader holds `ssm:GetParameter` (+ maybe `kms:Decrypt`) to retrieve the password.

**Credential chaining / key fact:** the instance role is granted `kms:Encrypt` only (sample policy #2) — it never decrypts. **Decryption is gated solely by the KMS key policy + the reader's IAM, independent of SSM.** For the default `alias/aws/ssm` key, the key policy is account-wide-open and not customer-editable, so `ssm:GetParameter --with-decryption` alone (no explicit `kms:Decrypt` in the reader's identity policy) suffices.

```
   caller (ssm:SendCommand)                         later reader (ssm:GetParameter)
            |                                                   |
            v                                                   v
   [SSM Run Command control plane]                   [SSM Parameter Store]
            |  runs AWS-owned document                /EC2Rescue/Password/<id>  (SecureString)
            v  AS the instance-profile role                     ^   decrypt via alias/aws/ssm
   +--------------------------------+   PutParameter ───────────┘   (no kms:Decrypt needed on default key)
   | EC2 Windows instance           |   kms:Encrypt (key)
   |  EC2RescueCmd (PowerShell)      |   s3:PutObject ──────────►  [ S3 bucket (free-form name) ]
   |  Distributor pkg AWSSupport-*   |◄── download from AWS-owned awssupport-ssm.* bucket
   +--------------------------------+
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv principal (read-only / monitoring role) | Another instance's local-admin password | `ssm:GetParameter --with-decryption` on `/EC2Rescue/Password/<id>` | Plaintext password returned for an instance the principal cannot `SendCommand` to → **boundary breach** (confidentiality of the admin credential is NOT bound to EC2 admin rights) |
| Over-broad `ssm:SendCommand` holder | Any managed instance in the account | SendCommand of the AWS-signed document (name scopable only by Resource ARN, not a condition key) | Command runs as another instance's role / resets an instance the caller doesn't administer → **breach** |
| Compromised instance-profile role (widened `PutParameter`) | Sibling instances' password parameters | `PutParameter --overwrite` on a wildcarded path (`ssm:SourceInstanceARN` absent for instance-profile auth) | Writing/overwriting a parameter outside the writer's own instance-id → **breach** |
| ResetAccess caller | A KMS key in another account | `kms:Encrypt` with caller-supplied cross-account key id | Ciphertext encrypted under a key the caller (not the instance owner) can later decrypt → **breach** |
| CollectLogs caller | An S3 bucket in another account / attacker-pre-registered name | `s3:PutObject` to a free-form bucket under `Resource:"*"` sample policy | Sensitive OS logs land in a bucket not owned by the instance owner → **breach** |
| Caller restricted to "AWS-owned documents only" | Arbitrary PowerShell on the instance | Injection via free-form `Parameters` (if allow-pattern not enforced on the Command path) | Arbitrary code runs where the customer believed only fixed AWS logic could → **control bypass** |
| Customer surface | **AWS service plane** (Distributor package host, Support document internals, `awssupport-ssm.*` buckets) | artifact download / document execution | **HARD STOP** — any AWS-owned identity/ARN/account reached = preserve evidence, disclose, do not probe |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ssm:SendCommand` (this document) | API | Existing | **Mutating** | External | Runs ResetAccess/CollectLogs/FixAll on instance | Yes (SigV4) | Anyone with `ssm:SendCommand` on the document ARN + target instance | **Document name scopable only via Resource ARN** — no `ssm:documentArn`/`ssm:Document` condition key exists in `list_ssm.md` (contradicts a WebFetch-only claim — do not rely on it). Instance scoping = tags only. |
| `ssm:PutParameter` | API (by instance role) | Existing | **Mutating** | Internal (instance role) | Writes/overwrites admin pw SecureString | via SendCommand | instance-profile role | Supports `ssm:Overwrite`, `aws:RequestTag`, `ssm:Policies` condition keys. Sample policy uses **none**. |
| `ssm:GetParameter` / `GetParameters` / `GetParametersByPath` | API | Existing | Non-mutating | External | **Reads the admin password** | Yes (SigV4) | Anyone with the action on the parameter ARN/tag | **Separately grantable from PutParameter.** Only tag/ARN scoping; no path-ownership condition key. The prime IDOR/secret-reachability reader. |
| `kms:Encrypt` | API (by instance role) | Existing | Non-mutating | Internal | Encrypts pw under chosen key | via SendCommand | instance-profile role | Cross-account key usable if that key's policy allows. |
| `s3:PutObject` (+ `GetBucketAcl`/`GetBucketPolicy`/`GetBucketPolicyStatus`) | API (by instance role) | Existing | **Mutating** | Internal | Uploads `/collect:all` logs | via SendCommand | instance-profile role | **Omitted entirely from the EC2 UserGuide `ec2rw-ssm` Requirements section**; the runbook page shows them with `Resource:"*"`. |

**Undocumented / console-hidden knobs & doc-vs-doc deltas:**
- The EC2 UserGuide page omits S3 permissions and the input `allowedPattern`; the *automation-runbooks* page for the same document name documents both. **Open question: are these two underlying SSM documents (a Command doc vs an Automation runbook) of the same name?** That ambiguity is itself a lead (different validation on each path).
- `allowedPattern` on the runbook: `^[0-9a-z][a-z0-9-.]{3,63}$|^(dev\/[a-z0-9]{2,10}|xv[a-z0-9]{1,10})$|^(alias\\aws\\ssm|[a-zA-Z0-9-/_]{1,32})$` — no shell metachars. **Unconfirmed whether the Command (`send-command`) path enforces it.**

---

## 5. Recommended Areas of Focus

### 5.1 — [PRIORITY 1] Local-admin credential reachable at the storage layer, decoupled from instance-admin rights  (Lens T + A + U)
**Background:** `ResetAccess` resets the Windows local Administrator password and persists the random value as a SecureString at the **deterministic** path `/EC2Rescue/Password/<INSTANCE_ID>`, encrypted by default under the account-wide-open `alias/aws/ssm` managed key.

**Security Concern:** Confidentiality of the admin credential is enforced **only** by whatever ARN/tag scoping sits on `ssm:GetParameter` — a *different, usually weaker-gated* action than the `ssm:SendCommand`/EC2-admin rights one would assume gate it. `GetParameter` and `PutParameter` carry **no path-ownership condition key** (`list_ssm.md` L522-710: empty action condition-key fields; `parameter` resource supports only `aws:ResourceTag`/`ssm:resourceTag`). `parameter-store-policy-conditions.md` L33: *"To restrict which parameters a principal can read, use resource-level and action-level controls … rather than condition keys."* For the default key, `parameter-store-how-to-retrieve.md` L19: *"If you use the default AWS managed key for Parameter Store, separate AWS KMS permissions aren't required."* and `secure-string-parameter-kms-encryption.md` L227 + `parameter-store-setting-up.md` L198: the default key's policy is open account-wide and not customer-editable.

**High-level Test Scenarios:**
- **Claim:** A principal with only `ssm:GetParameter` on `arn:…:parameter/EC2Rescue/Password*/*` (no `kms:Decrypt`, no `ssm:SendCommand`) can read the plaintext local-admin password of any instance that ever ran ResetAccess. → **Oracle:** `get-parameter --with-decryption` returns plaintext. **Severity: High** (instance takeover via RDP).
- **Claim:** The path is enumerable — instance ids are discoverable (`ec2:DescribeInstances`, CloudTrail, tags) and the `/EC2Rescue/Password/<id>` shape is fixed. → **Oracle:** `GetParametersByPath --path /EC2Rescue/Password --recursive` lists every reset instance.
- **Claim:** A broad read-only/monitoring role (`ssm:Get*` or `ssm:GetParameter` on `parameter/*`) silently inherits this. → **Oracle:** inspect common managed/monitoring policies for `ssm:GetParameter` wildcards.

**Doc evidence:** `ec2rw-ssm.md` L17, L134; `list_ssm.md` L522-710, L1964; `parameter-store-*.md` as cited.  **Severity-if-true: High.**  **Stop condition:** plaintext returned once = confirmed; do not enumerate further instances or reuse the credential.

### 5.2 — [PRIORITY 1] AWS-authored IAM-artifact audit — the sample policies are the defect  (Lens R + S + U) — **Tier-2 reportable**
**Background:** The page ships two copy-verbatim sample IAM policies for the instance role; the runbook page ships a third (adds S3 with `Resource:"*"`). Customers attach these as-is.

**Security Concern / scenarios (audit statement-by-statement):**
- **Path mismatch (confirmed, live):** prose stores to `/EC2Rescue/Password/<id>` (singular) but **both** sample policies grant `parameter/EC2Rescue/Passwords/<id>` (plural). If the tool writes the singular path, `PutParameter` **fails closed** → customer broadens `Resource` to `parameter/EC2Rescue/*` or `parameter/*` to unblock. → **Oracle:** attach the published policy verbatim, run ResetAccess, observe AccessDenied. **Severity: Medium (root cause)** — this is the AWS-owned defect that drives the High-severity wildcard below.
- **No `ssm:Overwrite` guard:** sample omits it; `parameter-store-policy-conditions.md` L22-42 shows it is opt-in. On a widened path the instance role can **overwrite** sibling instances' password parameters (credential poisoning / DoS). → **Oracle:** from a widened instance-profile role, `put-parameter --name /EC2Rescue/Password/<other-id> --overwrite` succeeds.
- **No self-binding possible under instance-profile auth:** `list_ssm.md` L1996 — `ssm:SourceInstanceARN` *"is not present when the request comes from the managed instance authenticated with an IAM role associated with EC2 instance profile."* So the only condition key that could scope "this instance writes only its own parameter" is **disabled for exactly this auth mode** → the design relies on hand-substituted per-instance ARNs → wildcarding is the natural outcome. **Severity: High when combined** (fleet-wide read/write of admin passwords).
- **S3 policy `Resource:"*"` with no `s3:ResourceAccount`:** runbook sample (`automation-awssupport-runec2rescueforwindowstool.md` L60-81) grants `s3:PutObject`/`GetBucket*` on `*`. `s3:ResourceAccount` exists (`list_s3.md`) but is unused → no bucket-ownership pin. **Severity: Medium-High** (enables §5.5).

**Doc evidence:** `ec2rw-ssm.md` L33-82; `automation-awssupport-runec2rescueforwindowstool.md` L43-81; `list_ssm.md` L708-710, L1996; `parameter-store-policy-conditions.md` L22-42.  **Stop condition:** prove the deny/allow under a **scoped role holding exactly the artifact** (use `iam:SimulatePrincipalPolicy` first), never an over-privileged tester.

### 5.3 — [PRIORITY 2] Over-broad `SendCommand` → run the AWS-signed reset-admin document against any instance  (Lens E + R, "LOLBAS")
**Background:** `send-command` authorizes against two independent resource types (document + instance). Document-name granularity is achievable **only via the Resource ARN**, not a condition key (`list_ssm.md` SendCommand row). Instance scoping is tag-based only.

**Security Concern:** A principal over-granted `ssm:SendCommand` (AWS's own runbook example uses `Resource:"*"`) can run this AWS-signed document — which resets admin passwords and executes AWS-furnished PowerShell as the instance role — against **any managed instance**, with no need to author a malicious document. Chains directly into §5.1 (read the new password → RDP).

**High-level Test Scenarios:**
- **Claim:** A policy with `ssm:SendCommand` on `document/AWS*` + `instance/*` and no tag condition lets a low-priv principal reset+read the admin password of an instance they don't administer. → **Oracle:** run ResetAccess against a foreign-but-same-account instance; confirm command succeeds and the parameter appears.
- **Claim:** Instance-tag scoping that the customer *believes* constrains SendCommand can be defeated if the attacker can set instance tags (`ec2:CreateTags`) → ABAC self-widen. → **Oracle:** tag a target instance to match the allowed tag, then SendCommand.

**Severity-if-true: High** (in-account instance takeover / lateral movement).  **Stop condition:** one successful foreign-instance command = confirmed.

### 5.4 — [PRIORITY 3] KMS key-id parameter — ciphertext redirection  (Lens H)
**Background:** ResetAccess accepts a caller-supplied KMS key id. `kms:Encrypt` supports cross-account use (`API_Encrypt.html`: *"Cross-account use: Yes"*). Invalid/disabled/wrong-usage keys are rejected at the KMS layer (`DisabledException`/`InvalidKeyUsageException`/`KMSInvalidStateException`/`NotFoundException`) — so this is **not** an injection/validation-bypass.

**Security Concern:** An attacker with `ssm:SendCommand`+ResetAccess but not key-admin can supply a **cross-account key they also control** (whose key policy grants this account `kms:Encrypt`, e.g. an over-permissive/public key policy), so the admin-password ciphertext is encrypted under a key the attacker can later **decrypt** — moving the real gate off the instance owner.

**High-level Test Scenarios:**
- **Claim:** ResetAccess with a cross-account key id the attacker controls encrypts the pw under that key; attacker then decrypts the SecureString ciphertext out-of-band. → **Oracle:** supply attacker-account key ARN; confirm parameter `KeyId` reflects it and attacker can `kms:Decrypt` the stored ciphertext.
- **Claim (doc gap):** a failed Encrypt/PutParameter is or isn't cleanly surfaced in `GetCommandInvocation` (silent-failure → customer thinks pw stored when it isn't). → **Oracle:** supply a disabled key; inspect command output.

**Severity-if-true: Medium** (self-impact variant) → **Medium-High** when it converts the pw into an attacker-decryptable blob.  **Stop condition:** confirm `KeyId` redirection; do not exfiltrate real credentials.

### 5.5 — [PRIORITY 3] CollectLogs → sensitive OS logs to an arbitrary / cross-account / pre-registered S3 bucket  (Lens Q + EE + A)
**Background:** `/collect:all` gathers OS logs and config files (sensitive) and uploads them to a **free-form bucket name** in `Parameters`. The published instance-role policy for this action is `Resource:"*"` with no owner/region pin.

**Security Concern:** Under the verbatim sample policy, the instance role will `PutObject` to **any** bucket name the operator supplies — (a) a cross-account bucket whose policy allows the write (common central-logging pattern), or (b) a global-namespace name an attacker **pre-registered** in their own account (S3 bucket-name land-grab, à la Bucket Monopoly). Either lands sensitive OS data outside the owner's control.

**High-level Test Scenarios:**
- **Claim:** CollectLogs with `Parameters='<attacker-bucket>'` uploads logs to the attacker's bucket. → **Oracle:** supply an attacker-owned bucket name; confirm objects arrive.
- **Claim:** No runtime bucket-owner/region check beyond IAM. → **Oracle:** supply a same-name bucket in a foreign account; observe whether the upload is blocked.

**Severity-if-true: Medium-High** (sensitive log exfiltration).  **Preconditions:** `Resource:"*"` S3 grant (as published) and `ssm:SendCommand`+CollectLogs.  **Stop condition:** one object confirmed landing in a non-owner bucket; use synthetic/canary log content only.

### 5.6 — [PRIORITY 4] `Parameters` → PowerShell injection as a trusted-document control bypass  (Lens F)
**Background:** `Parameters` is "the PowerShell parameters to pass." The EC2 UserGuide page documents **no** sanitization; the runbook page shows a restrictive `allowedPattern`, but it is **unconfirmed whether the `send-command` Command-document path enforces it** (possible two-documents-one-name ambiguity).

**Security Concern:** For a caller who already holds `SendCommand` on the target, injecting PowerShell is **self-impact** (they could use `AWS-RunPowerShellScript` anyway) — low severity. The boundary crossing exists only where a customer **restricts callers to AWS-owned "Support" documents** (via `ssm:DocumentType`/tags) believing the logic is fixed/safe: unsanitized `Parameters` then yields **arbitrary PowerShell as the instance role despite the intended control.**

**High-level Test Scenarios:**
- **Claim:** The Command path does not enforce the runbook's `allowedPattern`; a `Parameters` value with shell metacharacters reaches PowerShell. → **Oracle:** supply a benign-but-out-of-pattern marker (e.g. a value that writes a canary file) and inspect command output. **Severity: Medium** (conditional control bypass). Confirm surface first.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read admin pw without instance-admin rights | SSM Parameter Store `GetParameter` | Resource-ARN/tag scoping only — **no ownership condition key** |
| Enumerate reset instances by path | `GetParametersByPath /EC2Rescue/Password` | deterministic path = none |
| Reset admin pw of foreign instance | over-broad `SendCommand` | instance **tag** condition (customer-set) + document Resource ARN |
| Overwrite sibling pw parameters | widened instance-role `PutParameter` | `ssm:Overwrite` deny (not in sample); per-instance ARN (defeated by wildcard) |
| Encrypt pw under attacker KMS key | ResetAccess key-id param | KMS key-policy of the chosen key (attacker-controlled by hypothesis) |
| Exfiltrate OS logs to foreign bucket | CollectLogs + `s3:PutObject Resource:"*"` | `s3:ResourceAccount` (unused in sample) |
| Arbitrary PowerShell via trusted doc | `Parameters` input | `allowedPattern` (runbook only; Command path unconfirmed) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **AWS-owned supply chain:** the Distributor package `AWSSupport-EC2Rescue` and its `awssupport-ssm.*` source buckets are AWS infrastructure — **HARD STOP**, do not probe; the "download/verify" mechanism is undocumented but AWS-owned (weak lead, confirm-surface-only).
- **A customer who widens their own policy** beyond the AWS sample is a footgun — *but the sample's path mismatch / missing-condition defects that pressure the widening are AWS-owned and in scope (§5.2).*
- **PowerShell execution on the caller's own instance** when the caller already holds unrestricted `SendCommand` = self-impact, no privilege gain.
- **Choosing your own KMS key for your own password** = self-impact unless it redirects to an attacker-decryptable key (§5.4).
- IMDS on the managed instance; single-tenant self-DoS; product/feature-parity gaps; MongoDB/translation/prompt-injection lenses — **N/A, no such component** (see §8).
- **No cross-*tenant*/cross-*account-fleet* isolation surface exists on this page** — all boundaries are intra-account.

## 8. Null hypotheses / doc gaps (pages checked named)
- **Lens K (prompt injection) — N/A.** No LLM/agent/GenAI component. Pages read: `ec2rw-ssm.md`, `Windows-Server-EC2Rescue.md`, `Linux-Server-EC2Rescue.md`.
- **Lens F (wire-protocol/translation/BSON/SQL) — N/A.** No query/translation layer; only PowerShell param passing (covered §5.6). Pages: `ec2rw-ssm.md`, `ec2rw-cli.md`, `ec2rw-gui.md`.
- **Lens D/V (data→control plane, network segmentation) — N/A.** No customer-reachable control/storage ENI or multi-host fleet described. Page: `ec2rw-ssm.md`.
- **Lens J/FF (OAuth/3P, JWT/OIDC) — N/A.** SigV4 IAM only; no 3P linking or token verification. Pages: `ec2rw-ssm.md`, `list_ssm.md`.
- **Lens W (attestation) — N/A.** No enclave/PCR/`RecipientAttestation` gating in this feature's docs (the key is used plainly). Page: `ec2rw-ssm.md`.
- **Lens BB/CC/DD (canonicalization / asserted-identity / cache divergence) — N/A.** No multi-parser HTTP front, no authorizer-context passing, no caching layer. Pages: `ec2rw-ssm.md`, `list_ssm.md`.
- **Doc gaps to resolve before hunting (confirm surface first):**
  1. **Password vs Passwords** path — no AWS page reconciles prose vs policy; verify which path the tool actually writes.
  2. **Command doc vs Automation runbook of the same name** — the EC2 UserGuide page omits S3 perms + `allowedPattern` that the runbook page lists; confirm whether these are one document or two with different validation.
  3. **No single doc sentence** states "no `kms:Decrypt` needed for `alias/aws/ssm`"; it is assembled from three pages — live-confirm.
  4. **Who is actually granted `ssm:GetParameter`/`kms:Decrypt` on `/EC2Rescue/Password/*`** is undocumented — the real gate on §5.1/§5.4; no AWS guidance restricts it.
  5. **EC2Rescue download verification** (hash/signature/source) is unspecified.

## 9. Adjacent surface worth a separate plan (not on this page, discovered via parent docs)
- **`AWSSupport-ExecuteEC2Rescue`** Automation runbook (`Windows-Server-EC2Rescue.md` note): *"can even examine Amazon EBS root volumes from **other** instances."* → a cross-*resource* reach (helper instance attaching another instance's EBS volume) — **Lens X/AA** candidate; warrants its own plan.
- **EC2Rescue for Linux** (`Linux-Server-EC2Rescue.md`): modules are **YAML files containing BASH or Python scripts** — a custom-module code-execution surface (on-instance, likely self-impact) and `AWSSupport-TroubleshootSSH` runbook.

---

*Generated by the `security-questionbuilder` skill (documentation-derived; no live testing performed).*
