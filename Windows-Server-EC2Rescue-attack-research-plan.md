# EC2Rescue for Windows Server — Attack Research Plan

Source of leads: `docs.aws.amazon.com/AWSEC2/latest/UserGuide/Windows-Server-EC2Rescue.html` and its children
`ec2rw-gui.html`, `ec2rw-cli.html`, `ec2rw-ssm.html`; the AWS-authored SSM documents
`AWSSupport-ExecuteEC2Rescue`, `AWSSupport-StartEC2RescueWorkflow`, and the Run Command document
`AWSSupport-RunEC2RescueForWindowsTool`
(`docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/`). Offline mirror:
`/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2rw-*.md`.

**Status: documentation-derived hypotheses only. Nothing has been tested against a live AWS account.**
Every lead below is a claim that a boundary *might not hold* plus the exact observation that would settle it.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.**
  Work in priority order (Section 5 is pre-ranked). Look left and right for adjacent bugs.
- The highest-value *in-scope* finding here is an **AWS-authored IAM artifact** (the runbook's published
  "Required IAM permissions"), which a customer attaches **verbatim and cannot edit** — a weak default in it is
  AWS's defect (Lens R), **Tier 2**, route `aws-security`. The tool itself and offline-volume operations are
  mostly **customer-operated inside the customer's own account** — scope those honestly (Section 7).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service
  plane (e.g. the `awssupport-ssm.*` distribution buckets are AWS-owned, or the helper-AMI/Lambda belongs to an
  AWS fleet account), stop, preserve evidence, flag for AWS-Security disclosure. Do not exploit beyond existence.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)

1. **Privilege escalation via the AWS-authored runbook IAM policy:** a principal holding *only* the published
   `AWSSupport-StartEC2RescueWorkflow` "Required IAM permissions" obtains `AdministratorAccess` (or any
   policy) by creating + self-attaching + passing an `AWSSupport-EC2Rescue-*` role.
2. **Cross-principal recovery of a reset Administrator password:** a principal *without* rights on the instance
   (but with `ssm:GetParameter`) reads another instance's generated local-admin password from
   `/EC2Rescue/Password/<INSTANCE_ID>`, decrypting under the default `alias/aws/ssm` managed key.
3. **Confused-deputy / cross-ownership targeting:** make the SSM automation stop, image, detach-volume, or run
   code against an instance/volume the caller does not own.
4. **Code execution on the helper instance / onto a foreign root volume:** abuse the arbitrary `OfflineScript`
   (base64 PowerShell/Bash) or the `Ec2HandleUserData` "run a user-data script on next boot" primitive to plant
   execution on a volume that belongs to a different instance.
5. **Supply-chain substitution:** serve an attacker-controlled EC2Rescue binary / CloudFormation template / Lambda
   zip because its source name (`s3.amazonaws.com/ec2rescue/...`, `awssupport-ssm.*`) is predictable.
6. **Destructive / integrity breach:** the disk-signature auto-overwrite that fires *even under `/check-only`*
   mutates a volume the operator believed was read-only.

---

## 2. Components, Assets, and Design

**What EC2Rescue is.** A customer-run Windows troubleshooting tool (`EC2RescueCmd.exe`, plus a GUI) with two
modules: a *data collector* and an *analyzer*. It runs **only on EC2 Windows Server 2012+** (it self-checks that
it is on EC2). Three delivery paths, three very different trust profiles:

- **GUI / CLI (customer-driven, on-box):** the operator downloads the ZIP and runs it. Two execution modes:
  - `/online` — act on the instance EC2Rescue is installed on (collect logs, reset *this* box's admin password, fix firewall/RDP/EC2Config/EC2Launch/network/time).
  - `/offline:<device_id>` — act on an **EBS root volume detached from a *different* (faulty) instance** and
    re-attached to the working box. This is the key cross-resource seam: one instance's tool reads/writes
    another instance's OS, registry, and admin credentials.
- **SSM Run Command — `AWSSupport-RunEC2RescueForWindowsTool`:** downloads+verifies the tool from S3, imports a
  PowerShell module, and runs `EC2RescueCmd` with a `Command` (ResetAccess | CollectLogs | FixAll) and a
  free-form `Parameters` string ("The PowerShell parameters to pass for the specified command").
- **SSM Automation — `AWSSupport-ExecuteEC2Rescue` → `AWSSupport-StartEC2RescueWorkflow`:** the fully-managed
  path. Stops the target instance, (optionally) images it, **launches a helper "EC2Rescue" instance** via a
  CloudFormation stack, detaches the target's root volume and attaches it to the helper, runs an **arbitrary
  base64-encoded `OfflineScript`** (PowerShell for Windows) on the helper with the volume mounted, then reverses
  everything and deletes the stack.

**Assets.**
- Local Windows **Administrator password** → generated by `ResetAccess` / `ec2launch 'Reset Administrator Password'` / `ec2config Ec2SetPassword`.
- That password **stored in SSM Parameter Store** at `/EC2Rescue/Password/<INSTANCE_ID>`, encrypted with
  `alias/aws/ssm` (default) or a customer KMS key.
- **Backup AMIs** (`AWSSupport-EC2Rescue*`, pre/post) that persist and "It is your responsibility to secure access to the AMI" — may contain the target's disk contents and secrets.
- **Collected logs** uploaded to a customer S3 bucket (event logs, registry SYSTEM/SOFTWARE hives, memory dumps, SSM/patch logs).
- The **foreign root volume** mounted offline (registry hives, BCD, disk signature).
- **AWS-authored artifacts:** the runbooks' required-IAM policy, the CFN template + Lambda in `awssupport-ssm.*`,
  the `EC2Rescue_latest.zip` binary.

**Identifier shapes.** Parameter name is fully deterministic from the **public instance-id**
(`/EC2Rescue/Password/i-0cb2b964d3e14fd9f`). Auto-created IAM role/instance-profile/Lambda/stack names share the
predictable prefix `AWSSupport-EC2Rescue-*`.

**Identity / privilege.** SSM paths run under the automation `AutomationAssumeRole` (or, if none supplied, the
*caller's* permissions). The tool on-box runs as a local admin / SSM agent (SYSTEM).

```
  Customer operator / IAM principal
        │  ssm:StartAutomationExecution (AWSSupport-ExecuteEC2Rescue)
        ▼
  AWSSupport-ExecuteEC2Rescue  ──►  AWSSupport-StartEC2RescueWorkflow  (AutomationAssumeRole)
        │                                 │
        │ s3:GetObject awssupport-ssm.*    │ aws:createStack (CFN)  →  helper "EC2Rescue" instance
        │ (template/.zip)                  │ iam:CreateRole/PassRole AWSSupport-EC2Rescue-*  → instance profile
        ▼                                 ▼
   EC2Rescue_latest.zip (s3://ec2rescue)   STOP target → detach ROOT VOL → attach to helper (xvdf)
                                           → aws:runCommand <base64 OfflineScript> (PowerShell, SYSTEM, vol mounted)
                                           → re-attach vol → restore state → deleteStack
        ─────────────── on-box CLI/GUI path ───────────────
  EC2RescueCmd /online  → this instance  (collect / rescue / ResetAccess → SSM param)
  EC2RescueCmd /offline:<dev> → FOREIGN instance's detached root volume (registry/password/user-data/disk-sig)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal holding only the runbook "Required IAM permissions" | Account admin | `iam:CreateRole`+`PutRolePolicy`+`AttachRolePolicy`+`PassRole` on `AWSSupport-EC2Rescue-*` | A non-admin principal attaches `AdministratorAccess` to a self-created role and passes it to compute → **privesc**. |
| Principal w/o instance rights but with `ssm:GetParameter` | Another instance's admin password | Deterministic param `/EC2Rescue/Password/<id>` + `alias/aws/ssm` `kms:ViaService` delegation | **Reading the cleartext password of an instance you have no EC2/SSM-command rights on is a breach.** |
| Automation caller | An instance/volume they do not own | Caller-supplied `InstanceId`/`UnreachableInstanceId` | The runbook stops/images/detaches/runs-code against a **non-owned** instance → breach. |
| Operator who ran `/check-only` (read-only intent) | Attached foreign volume | Disk-signature auto-fix fires *even with `/check-only`* | **A write to the volume under read-only intent is an integrity breach.** |
| `OfflineScript` on helper instance | Target instance's OS / credentials / network | Arbitrary PowerShell run as SYSTEM with root vol mounted | Code runs with access to the foreign volume's secrets → by-design, but verify tenant containment. |
| AWS service plane (hard stop) | `awssupport-ssm.*` buckets, helper AMI, validation Lambda | `s3:GetObject`, CFN, `aws:invokeLambdaFunction` | **Any identity/ARN/account belonging to AWS's own fleet = HARD STOP, preserve + disclose.** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `EC2RescueCmd /collect` | on-box CLI | Existing | No (reads) | On-box | Collect log groups → zip | No | Local admin | `/output` path; offline reads foreign vol |
| `EC2RescueCmd /rescue` | on-box CLI | Existing | **Yes** | On-box | Fix firewall/RDP/EC2Config/EC2Launch/net/time; **reset admin pw** | No | Local admin | `/check-only` still fixes disk-sig |
| `EC2RescueCmd /restore` | on-box CLI | Existing | **Yes** | On-box | `lkgc`, `regback` on foreign vol | No | Local admin | Registry overwrite |
| `AWSSupport-RunEC2RescueForWindowsTool` | `ssm:SendCommand` | Existing | **Yes** | AWS-authored SSM doc | ResetAccess / CollectLogs / FixAll | via SSM API | `ssm:SendCommand` holder on a managed instance | **Free-form `Parameters` → PowerShell** |
| `AWSSupport-ExecuteEC2Rescue` | `ssm:StartAutomationExecution` | Existing | **Yes** | AWS-authored runbook | Stop+image+rescue an unreachable instance | via SSM API | runbook caller / `AutomationAssumeRole` | Delegates to StartEC2RescueWorkflow |
| `AWSSupport-StartEC2RescueWorkflow` | `ssm:StartAutomationExecution` | Existing | **Yes** | AWS-authored runbook | Launch helper, mount vol, **run arbitrary `OfflineScript`** | via SSM API | runbook caller / `AutomationAssumeRole` | `OfflineScript` = base64 PowerShell/Bash; `Lambda` input-validation step |
| `ssm:PutParameter` / `ssm:GetParameter` | SSM API | Existing | Put=Yes | External | Store/read `/EC2Rescue/Password/<id>` | via SSM API | per IAM | **Enumerable by instance-id** |

**Undocumented / console-hidden knobs to enumerate:** the `Parameters` field of the Run Command doc is
described only as "PowerShell parameters to pass" — its grammar/allowed values are not in the public docs
(doc-gap → injection lead). `CreatePreEC2RescueBackup`/`CreatePostEC2RescueBackup` default `false` but the AMIs
persist and are the caller's responsibility to secure.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### 5.1 [PRIORITY 1] AWS-authored runbook IAM policy → non-admin → admin privesc (Lens R / S / B)

**Background.** `AWSSupport-StartEC2RescueWorkflow` publishes a "Required IAM permissions" JSON that the
`AutomationAssumeRole` (or the running user) must hold. It is an **AWS-authored artifact a customer copies
verbatim and cannot edit.** It grants, scoped to the name prefix `AWSSupport-EC2Rescue-*`:
`iam:CreateRole`, `iam:CreateInstanceProfile`, `iam:PutRolePolicy`, `iam:AttachRolePolicy`, `iam:DetachRolePolicy`,
`iam:PassRole`, `iam:AddRoleToInstanceProfile`, `iam:DeleteRole`, … — and separately `lambda:CreateFunction`,
`ec2:Create*/Delete*` VPC actions on `Resource:"*"`.

**Security Concern.** `iam:AttachRolePolicy` is scoped on the **role** resource (`role/AWSSupport-EC2Rescue-*`)
but places **no constraint on which `PolicyArn` may be attached**, and the holder *also* has `iam:CreateRole`
on that same prefix. Classic self-escalation: the holder creates `AWSSupport-EC2Rescue-pwn`, attaches
`arn:aws:iam::aws:policy/AdministratorAccess` (or puts an inline `*:*` policy via `iam:PutRolePolicy`),
`iam:AddRoleToInstanceProfile`, and `iam:PassRole`s it onto a compute resource — escalating from the (intended,
narrow) "run EC2Rescue" grant to full admin. The name-prefix scope is **self-satisfiable** (the holder has
CreateRole on exactly that prefix), so it bounds nothing.

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A principal whose *only* permissions are this published policy can obtain `AdministratorAccess`.
  → **Mechanism:** `iam:AttachRolePolicy` has no `Condition`/`PolicyArn` limit; `iam:CreateRole`+`iam:PutRolePolicy`
  on the same `AWSSupport-EC2Rescue-*` prefix. → **Oracle:** under a scoped role holding *exactly* the artifact,
  `iam:SimulatePrincipalPolicy` shows `AttachRolePolicy`/`PutRolePolicy`/`PassRole` = **allowed** for
  `role/AWSSupport-EC2Rescue-*` with an admin `PolicyArn`; confirm (canary only) by creating one such role +
  attaching a benign managed policy. **Do not** attach real admin on a production account. → **Severity:** **High**
  (intra-account non-admin→admin, AWS-authored artifact → Tier 2, route `aws-security`).
- **Claim:** `lambda:CreateFunction` + `iam:PassRole` + `lambda:InvokeFunction` is a complete self-contained
  exec-as-admin chain. → **Mechanism:** `lambda:CreateFunction` is on `Resource:"*"` (no name limit on *create*)
  while `lambda:InvokeFunction` is scoped to `function:AWSSupport-EC2Rescue-*` — so create the function **named
  `AWSSupport-EC2Rescue-evil`** (satisfies the invoke scope), pass it the self-created admin role, and invoke it
  to run arbitrary code as admin. → **Oracle:** `iam:SimulateCustomPolicy` over the 5-action chain
  (CreateRole→PutRolePolicy→CreateFunction→PassRole→InvokeFunction) returns allowed end-to-end. → **Severity:** High/Critical.
- **Claim:** The broad `ec2:Create*/Delete* … Resource:"*"` block (VPC, subnet, route, IGW, VPC-endpoint) lets the
  holder mutate networking account-wide, not just the EC2Rescue stack's resources. → **Oracle:** policy simulation
  shows no `aws:ResourceTag`/stack-scoping condition on those statements.

**Doc evidence:** `automation-awssupport-startec2rescueworkflow.html` → "Required IAM permissions" JSON block.
**Severity-if-true:** High (privesc) / Medium (over-broad VPC mutation). **Stop condition:** once a scoped-role
simulation confirms admin reachability, that *is* the finding — do not perform the live attach on a real account.

### 5.2 [PRIORITY 2] ResetAccess password in Parameter Store — cross-principal reach & enumeration (Lens T / A / H)

**Background.** `ResetAccess` "resets the local Administrator password … the randomly generated password will be
securely stored in Parameter Store as `/EC2Rescue/Password/<INSTANCE_ID>`", encrypted with the default
`alias/aws/ssm` KMS key unless a customer key id is passed.

**Security Concern.** The secret leaves the origin control (the instance / `ssm:SendCommand`) and comes to rest
in Parameter Store under a **deterministic, instance-id-derived name** and the **account-default managed key**.
A principal that is *denied* instance access but holds a broad `ssm:GetParameter`/`GetParametersByPath` on
`/EC2Rescue/*` can **harvest every reset Administrator password in the account**, and the managed key's
`kms:ViaService` delegation means the caller may not even need an explicit `kms:Decrypt`.

**High-level Test Scenarios:**
- **Claim:** A role with `ssm:GetParametersByPath /EC2Rescue/Password/*` + `WithDecryption` reads admin passwords
  of instances it has no EC2/SSM-command rights over. → **Oracle:** under a scoped role lacking instance perms,
  `GetParameter(/EC2Rescue/Password/<id>, WithDecryption=true)` returns cleartext (canary instance only).
  → **Severity:** **Medium–High** (credential recovery bypassing the instance wall).
- **Claim:** Decryption succeeds with **no `kms:Decrypt`** in the caller's identity policy because `alias/aws/ssm`'s
  key policy delegates via `kms:ViaService`. → **Oracle:** scoped role with SSM read but explicit KMS deny still
  decrypts. → **Severity:** Medium (owner-to-fix is **shared**: AWS owns the managed-key delegation default).
- **Claim:** No encryption context binds the parameter to the instance, so the ciphertext/key is not scoped per
  resource. → **Oracle:** docs name none; confirm the `PutParameter` call omits `EncryptionContext`. → Lens H.
- **Claim:** The password **outlives** the instance (terminate the instance; the parameter remains) → stale
  credential lingering. → **Oracle:** parameter still present after instance termination.
- **Claim:** `/EC2Rescue/Password/<id>` is enumerable because instance-ids are visible to any
  `ec2:DescribeInstances` holder → a `GetParametersByPath` sweep yields all. → **Severity:** amplifies the above.

**Doc evidence:** `ec2rw-ssm.html` ResetAccess description + both sample IAM policies.
**Stop condition:** one cleartext read under a scoped role proves it; do not harvest more than the single canary.

### 5.3 [PRIORITY 2] Sample-policy path mismatch & scoping (Lens U / S)

**Background.** The prose says the parameter is written to `/EC2Rescue/Password/<INSTANCE_ID>` (**singular**
"Password"), but **both** printed sample IAM policies scope `ssm:PutParameter` to
`arn:aws:ssm:…:parameter/EC2Rescue/Passwords/<instanceid>` (**plural "Passwords"**).

**Security Concern.** If the runtime writes the *singular* path but the copy-verbatim policy grants only the
*plural* path, the customer-attached least-privilege policy **fails closed** — `PutParameter` is denied, the
operator sees a confusing failure, and the documented remedy ("wait a few minutes after attaching the policy")
masks it, pushing operators to broaden the grant to `parameter/*` (over-privilege). If instead the runtime writes
the plural path, the prose is simply wrong. Either way it is an **AWS-authored doc-vs-enforcement defect**.

**High-level Test Scenarios:**
- **Claim:** The actual `PutParameter` target does not match the sample policy's ARN → the published
  least-privilege policy does not authorize the runtime path. → **Oracle:** run `ResetAccess` with *only* the
  sample policy attached; observe `AccessDenied` on `PutParameter`, and read the created parameter's real name.
  → **Severity:** **Low–Informational** (AWS-owned doc/policy inconsistency; worth filing — it induces a broader grant).
- **Claim:** The custom-KMS sample policy grants `kms:Encrypt` but the Put under a customer CMK may also require
  `kms:GenerateDataKey`/`kms:Decrypt` (SecureString advanced) → still fails closed. → **Oracle:** attach exactly
  the sample policy + customer key, run ResetAccess, observe KMS `AccessDenied`.

**Doc evidence:** `ec2rw-ssm.html` prose vs. the two JSON policy blocks. **Severity-if-true:** Low–Informational.

### 5.4 [PRIORITY 3] Confused-deputy / cross-ownership targeting of the automation (Lens B / C / P)

**Background.** `AWSSupport-ExecuteEC2Rescue` takes `UnreachableInstanceId` and "stops this instance, and creates
an AMI before attempting any operations." `AWSSupport-StartEC2RescueWorkflow` takes `InstanceId`, stops it,
detaches its root volume, and runs code with it mounted. Authorization is whatever the `AutomationAssumeRole`
(or the running user) holds — there is no documented ownership/`aws:SourceArn` guard tying the caller to the
instance beyond ordinary EC2/SSM IAM. The published Run Command sample policy uses `Resource:"*"` for every
targeting action (`ssm:SendCommand`, `ssm:PutParameter`, `ssm:GetCommandInvocation`, …), and the SSM
service-authorization reference (`list_ssm.md`) confirms `SendCommand`'s `instance`/`managed-instance` resource
types support **only tag-based condition keys** (`aws:ResourceTag`, `ssm:resourceTag`) — there is **no built-in
ownership/source condition**, so scoping depends entirely on customer-authored tags that AWS's own samples omit.
**Lens P note:** no approval gate, break-glass, or `SourceArn`/`SourceAccount` condition is documented on any of
the four runbook pages — confirmed, not a doc-gap.

**Security Concern.** If the assume-role is over-broad (e.g. `ec2:*` on `*`), any caller who can start the
automation can stop/image/detach-volume/run-code against **any instance in the account** — including instances
owned by another team. There is no gate (no proofing step, no mutual consent) beyond IAM; and the automation's
side effects (stop, public-IP change, instance-store data loss, persistent backup AMI) are destructive.

**High-level Test Scenarios:**
- **Claim:** A principal with `StartAutomationExecution` + a permissive `AutomationAssumeRole` can run the workflow
  against an `InstanceId` it does not "own" (no tag/ABAC binding). → **Oracle:** the automation proceeds (stops +
  images + mounts) on an instance owned by a different team/tag. → **Severity:** **High** if the assume-role lacks
  resource scoping (note: owner-to-fix is **shared** — AWS ships the runbook; the customer scopes the role).
- **Claim:** The persistent backup AMI (`CreatePre/PostEC2RescueBackup`) captures the target's disk and is readable
  by anyone the customer's default AMI permissions allow. → **Oracle:** AMI created with no explicit launch-perm
  lock-down; docs explicitly offload securing it to the customer. → Lens AA (share lifecycle) + Q (data at rest).

**Doc evidence:** runbook parameter descriptions; "It is your responsibility to secure access to the AMI."

### 5.5 [PRIORITY 3] Arbitrary `OfflineScript` / `Parameters` injection (Lens F)

**Background.** `AWSSupport-StartEC2RescueWorkflow` runs a caller-supplied **base64-encoded PowerShell/Bash
`OfflineScript`** on the helper instance as SYSTEM with the foreign root volume mounted. The Run Command doc's
`Parameters` field is "The PowerShell parameters to pass for the specified command." There is one
`aws:invokeLambdaFunction - Perform additional input validation` step whose rules are not documented.

**Security Concern.** `OfflineScript` is arbitrary code **by design** — the relevant question is containment, not
"can you run code." For the Run Command `Parameters` field there is a **doc version-skew**: the EC2 UserGuide page
(`ec2rw-ssm.html`) describes `Parameters` only as "The PowerShell parameters to pass for the specified command"
with **no `allowPattern` at all**, whereas the Systems Manager Automation-runbooks page for the same-named
document publishes a restrictive
`Allow Pattern`: `^[0-9a-z][a-z0-9-.]{3,63}$|^(dev\/[a-z0-9]{2,10}|xv[a-z0-9]{1,10})$|^(alias\aws\ssm|[a-zA-Z0-9-/_]{1,32})$`.
If the live document in a given account still matches the *unrestricted* EC2-UserGuide schema, `Parameters` is
interpolated into a PowerShell `EC2RescueCmd` call with no character restriction → **argument/command injection**.
The pattern that *is* published is fairly tight (no spaces, `;`, `` ` ``, `$`, or `|`), so exploitability hinges
entirely on **which schema is authoritative** and on **how `{{Parameters}}` is interpolated** (literal string
concatenation vs. a bound `-Parameter` call) — neither is shown in the docs.

**High-level Test Scenarios:**
- **Claim:** The account's live `AWSSupport-RunEC2RescueForWindowsTool` accepts a `Parameters` value the published
  `allowPattern` would reject (schema skew) → argument injection into the PowerShell invocation. → **Oracle (live,
  future phase):** `aws ssm get-document --name AWSSupport-RunEC2RescueForWindowsTool --document-format JSON` to
  read the real `mainSteps` + parameter schema and the `{{Parameters}}` interpolation; then a benign canary
  (within whatever pattern applies) proving extra-argument execution. → **Severity:** High-if-true; currently
  **doc-gap — confirm the authoritative schema + interpolation first.** → **Preconditions:** `ssm:SendCommand`.
- **Claim:** The opaque `aws:invokeLambdaFunction` "additional input validation" in StartEC2RescueWorkflow fails
  open on a base64-encoded `OfflineScript`. → **Oracle:** doc-gap — the Lambda's rules are not published; "confirm surface first."

**Doc evidence:** `ec2rw-ssm.html` `Parameters` (no pattern) vs `automation-awssupport-runec2rescueforwindowstool.html` `Allow Pattern`; StartEC2RescueWorkflow `OfflineScript` + validation Lambda step.

### 5.6 [PRIORITY 3] Supply-chain / predictable-name substitution (Lens EE / Y)

**Background.** The tool is fetched from `https://s3.amazonaws.com/ec2rescue/windows/EC2Rescue_latest.zip`
(the docs' PowerShell one-liner uses that exact URL); the Run Command doc "Downloads and **verifies**" it. The
runbook's IAM grants `s3:GetObject` on `arn:aws:s3:::awssupport-ssm.*/*.template` and `*.zip` — i.e. the
CloudFormation template and Lambda/code are pulled from regional buckets named `awssupport-ssm.<something>`.

**Security Concern.** Predictable, globally-unique bucket names. The `ec2rescue` bucket is a long-standing legacy
path-style bucket referenced by AWS docs for years and the download URL is confirmed **HTTPS** (no HTTP fallback
documented) → classic on-path MITM and land-grab risk on *that* bucket is assessed **low**. The sharper concern is
the `awssupport-ssm.*` **wildcard**: if any regional `awssupport-ssm.<region>` variant the runbook will read is
**unclaimed** (new region/partition), an attacker could pre-register it and serve a malicious `*.template`/`*.zip`
the runbook executes under the automation role (Bucket-Monopoly / land-grab). Separately, the Windows EC2Rescue
download's **"verifies" step is entirely undocumented** (hash? Authenticode? nothing beyond TLS?) — a notable
asymmetry versus EC2Rescue **for Linux**, whose docs (`ec2rl_install.html`) specify a full GPG workflow
(`ec2rl.key`, detached `.sig`, `gpg --verify`, identity `ec2autodiag@amazon.com`).

**High-level Test Scenarios:**
- **Claim:** A regional `awssupport-ssm.<region>` bucket the runbook will read is not pre-claimed by AWS. →
  **Oracle:** `s3:HeadBucket` on the exact name returns no-such-bucket (STOP IMMEDIATELY and disclose if it
  resolves to AWS infrastructure — do **not** place content, do **not** `CreateBucket` on a name that may be
  adopted by the service). → **Severity:** Critical if claimable (service plane / all customers). **HARD STOP + disclose.**
- **Claim:** The Windows "verify" is a mutable hash (or absent), not a signature, unlike the Linux GPG flow. →
  **Oracle:** doc-gap — "verifies" is unqualified; pull the live SSM document to see the verification command, and
  inspect the ZIP for an Authenticode signature. Mark "confirm mechanism first."

**Doc evidence:** `ec2rw-gui/cli.html` HTTPS download URL; StartEC2RescueWorkflow IAM `s3:GetObject awssupport-ssm.*`;
`ec2rl_install.html` Linux GPG contrast.

### 5.7 [PRIORITY 4] Offline-volume mutation: disk-signature auto-overwrite & user-data planting (Lens U / integrity)

**Background.** Offline mode mutates a **foreign** instance's root volume: `regback` overwrites the registry,
`lkgc` changes boot state, `Ec2HandleUserData` "Allows you to run a user data script on the next boot of the
instance," and — most notably — **"If EC2Rescue detects a possible disk signature collision, it corrects the
signature after the offline process completes by default, *even when you use the `/check-only` option*."**

**Security Concern.** `/check-only` is documented as "generates a report but makes no modifications," yet the
disk-signature fix fires anyway unless `/no-fix-signature` is added — an **integrity violation of the tool's own
read-only guarantee** (Lens U). The `Ec2HandleUserData` path is a code-execution primitive planted onto a volume
that will later boot as a different instance. Mostly customer-operated within one account, but worth documenting
because the guarantee ("no modifications") is AWS's and is false.

**High-level Test Scenarios:**
- **Claim:** `/check-only` writes to the attached volume (disk signature) despite promising no modifications. →
  **Oracle:** run `/rescue:all /check-only` on a canary volume whose signature collides; observe a write. →
  **Severity:** Medium (integrity; AWS-owned doc-vs-behavior).
- **Claim:** `Ec2HandleUserData` on an offline volume causes code to run on the *target* instance's next boot. →
  **Oracle:** plant a canary user-data script offline; boot the target; observe execution. → scope: customer-owned.

**Doc evidence:** `ec2rw-cli.html` `/check-only` + `/no-fix-signature` note; `ec2rw-gui.html` Ec2HandleUserData.

### 5.8 [PRIORITY 2] The cross-ownership actions live in a referenced-but-not-reproduced managed policy (Lens R completeness)

**Background.** The printed "Required IAM permissions" for StartEC2RescueWorkflow is explicitly **additive** to the
AWS-managed policy `AmazonSSMAutomationRole` ("It is recommended the user … have the **AmazonSSMAutomationRole**
IAM managed policy attached. In addition to that policy, the user must have: …"). The printed JSON contains **no**
`ec2:StopInstances`, `ec2:AttachVolume`, `ec2:DetachVolume`, `ec2:CreateImage`, or `ec2:CreateTags` — yet the
runbook's own documented steps **stop the target, create an AMI, and detach/attach the root volume** (steps 12–13,
19–21, 27–29). Those grants must come from `AmazonSSMAutomationRole`, whose content neither EC2Rescue page reproduces.

**Security Concern.** The actions that actually **cross into another instance's data** (volume detach/attach,
instance stop, imaging) are hidden behind a broad general-purpose managed policy that — from the public policy
catalog — scopes `ec2:StopInstances`/`AttachVolume`/`DetachVolume`/`CreateImage` **without instance-id conditions**.
So the ownership-crossing audit (Section 5.4) cannot be completed from the EC2Rescue pages alone, and the likely
answer is "no resource scoping on the volume-movement actions."

**High-level Test Scenario:**
- **Claim:** `AmazonSSMAutomationRole` grants `ec2:DetachVolume`/`AttachVolume`/`StopInstances`/`CreateImage` on
  `Resource:"*"` with no ownership condition. → **Oracle:** `iam:GetPolicyVersion` on
  `arn:aws:iam::aws:policy/AmazonSSMAutomationRole` (a catalog lookup, not live-target testing) + statement audit.
  → **Severity:** Medium (completeness/over-scope; feeds 5.4's confused-deputy severity).

**Doc evidence:** `automation-ec2rescue.html` "In addition to that policy …"; StartEC2RescueWorkflow step list.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Non-admin → admin via copy-verbatim IAM policy | `AWSSupport-StartEC2RescueWorkflow` Required IAM | Name-prefix scoping on `AWSSupport-EC2Rescue-*` (claim: self-satisfiable, bounds nothing) |
| Read another instance's admin password | SSM Parameter Store `/EC2Rescue/Password/<id>` | "securely stored", default `alias/aws/ssm` key, sample PutParameter policy |
| Published policy fails closed → induces over-grant | ResetAccess sample IAM policies | Prose `/Password/` vs policy `/Passwords/` ARN |
| Act on a non-owned instance | ExecuteEC2Rescue / StartEC2RescueWorkflow `InstanceId` | Only `AutomationAssumeRole` IAM (no SourceArn ownership guard) |
| Argument injection via `Parameters` | `AWSSupport-RunEC2RescueForWindowsTool` | Undocumented grammar; `aws:invokeLambdaFunction` validation (opaque) |
| Malicious template/binary substitution | `awssupport-ssm.*` / `s3://ec2rescue` | Predictable bucket names; "verifies" (unqualified) |
| Read-only guarantee violated | `/check-only` disk-signature fix | `/no-fix-signature` opt-out (fires by default) |
| Backup AMI exposes target disk | `CreatePre/PostEC2RescueBackup` | "your responsibility to secure access to the AMI" |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Customer-operated code execution inside the customer's own account** — the on-box CLI/GUI, the arbitrary
  `OfflineScript`, and the `ssm:SendCommand`/`StartAutomationExecution` code paths all execute with permissions
  the operator already holds. "A customer can run code on their own instance / their own volume" is **not** a
  finding. The in-scope angle is only *cross-ownership* reach or an *AWS-authored artifact* defect.
- **Customer-authored IAM scoping** — if the customer broadens the `AutomationAssumeRole` themselves, that is a
  customer footgun. Only the **AWS-published** "Required IAM permissions" block (Section 5.1) and the printed
  **sample policies** (5.3) are in scope.
- **IMDS on the managed hosts**, instance-store data loss on stop, public-IP change — documented behavior, not a vuln.
- **The faulty instance's own owner recovering their own password** — intended function.
- **Product/feature-parity gaps** (encrypted root volumes "not supported") — a limitation, not a weakness, unless
  the "unsupported" path fails open (worth a one-line check, not a lead).
- **Bugs inside the EC2Rescue binary's Windows parsing** beyond what the docs expose — out of documentation scope
  here; would require the binary, not the docs.

---

## 8. Null hypotheses / doc gaps (lenses checked, did not fire, or need confirmation)

- **Lens K (prompt injection):** N/A — read all three EC2Rescue pages + both runbooks; no LLM/agent/GenAI component.
- **Lens J (OAuth/3P), Lens FF (JWT/OIDC), Lens DD (cache), Lens CC (upstream-context), Lens BB (parser
  differential across edge):** N/A — read all pages; EC2Rescue has no web/API-gateway/authorizer/OAuth/token
  surface. Auth is plain SigV4 IAM via the SSM/EC2 APIs.
- **Lens W (attestation):** N/A — no Nitro Enclaves / PCR gating in any page.
- **Lens V/D (network segmentation / data→control):** partial — the helper instance runs in a customer VPC (new
  VPC or the instance's subnet); no AWS control-ENI is reachable from the customer path per docs. Mark the
  `awssupport-ssm.*` bucket + validation Lambda ownership as the only service-plane surface (→ 5.6, HARD STOP).
- **Doc-gaps to confirm before hunting:** (a) **which `Parameters` schema is authoritative** — the EC2 UserGuide
  shows *no* `allowPattern` while the SSM Automation-runbooks page shows a restrictive one (version skew), plus how
  `{{Parameters}}` is interpolated into the PowerShell call; (b) what the StartEC2RescueWorkflow validation Lambda
  enforces; (c) whether the Windows "verifies" step = signature or hash (Linux uses documented GPG, Windows is
  silent); (d) whether `PutParameter` uses an `EncryptionContext`; (e) the real runtime parameter path
  (`/Password/` vs `/Passwords/`); (f) default launch permissions on the backup AMIs; (g) the actual contents of
  `AmazonSSMAutomationRole` (ownership scoping on `ec2:DetachVolume`/`AttachVolume`/`StopInstances`/`CreateImage`).

---

## 9. Handoff notes for the next agent

- Start at **5.1** — it is the cleanest, fully doc-grounded, *in-scope* (AWS-authored, copy-verbatim) lead and is
  confirmable with `iam:SimulatePrincipalPolicy` alone (no resource mutation). The policy JSON is reproduced in
  `automation-awssupport-startec2rescueworkflow.html` → "Required IAM permissions".
- **5.2/5.3** need a canary EC2 Windows instance + the exact sample policies attached to a scoped role; confirm
  with a single `GetParameter`/`PutParameter` and stop.
- **5.6** is the only service-plane lead — treat the `awssupport-ssm.*` bucket check as **HARD STOP + disclose**;
  never place content in a bucket that resolves to AWS infra.
- Mirror paths: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/{Windows-Server-EC2Rescue,ec2rw-gui,ec2rw-cli,ec2rw-ssm}.md`.
  Runbooks are best read online as `.md` (`systems-manager-automation-runbooks/latest/userguide/automation-awssupport-{executeec2rescue,startec2rescueworkflow}.md`).
