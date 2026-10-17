# EC2 ↔ AWS CloudTrail Audit-Logging Integration — Attack Research Plan

**Source of leads:**
- Primary target: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-with-cloudtrail.html (`.md` mirror fetched online).
- Supporting (fetched online as `.md`): CloudTrail *Logging management events* (`logging-management-events-with-cloudtrail`), *Logging data events* (`logging-data-events-with-cloudtrail`), *Validating log file integrity* (`cloudtrail-log-file-validation-intro`), *S3 bucket policy for CloudTrail* (`create-s3-bucket-policy-for-cloudtrail`).
- Related existing plans in this dir (do NOT duplicate): `EC2-CloudWatch-monitoring-attack-research-plan.md`, `EC2-instance-state-change-events-attack-research-plan.md`. This plan covers **CloudTrail (audit/attribution)** specifically.

**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Local mirror `/work/aws-docs` was stale for the newer CloudTrail pages; all citations are from the online `.md` versions.

**Target nature.** This is not a multi-tenant data plane. It is an **audit / observability** surface: the "assets" are the CloudTrail *records themselves*, the *configuration* that decides what is recorded (event selectors), and the *delivery/storage pipeline* (S3 bucket, digest files, KMS). The adversary's goal is therefore not cross-tenant data theft but **evasion, suppression, tampering, mis-attribution, and reaching sensitive data through paths that produce no record.** The dominant lens is **O (audit-log evasion)**, closely supported by **U (documented-guarantee vs enforcement)** and **X (action-twin / lower-level-cousin parity)**.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Severity framing here is defender-impact: an evasion/tamper primitive is rated by *what it lets an attacker hide and how durably*, and whether it blinds **other** principals (org/management account) or only the attacker's own account.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. the CloudTrail delivery role, a CloudTrail-owned KMS key, an AWS-internal account id in a digest/delivery path), stop, preserve evidence, flag for AWS-Security disclosure.
- Most leads here are **customer-configuration footguns** (the customer chooses to narrow selectors, skip integrity validation, omit `SourceArn`). Those are **out of scope as AWS bugs** unless (a) the weak behavior is the *AWS default* that the EC2 doc's guarantee contradicts, or (b) the weakness lives in an **AWS-authored artifact the customer copies verbatim** (the sample S3 bucket policy). Those two carve-outs are the reportable core — see §5 Areas 1, 2, 6.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Perform a security-relevant EC2 mutation that produces no CloudTrail record on a correctly-"enabled" trail** — i.e. defeat the EC2 page's claim "All Amazon EC2 API actions are logged as management events."
2. **Read EC2/EBS data (snapshot bytes, instance access) through a path CloudTrail does not record by default** (EBS direct APIs; the SSH session behind EC2 Instance Connect).
3. **Blind a defender for a specific actor** — carve the attacker's own identity out of logging while the trail still reports "logging management events, all event sources."
4. **Tamper with or delete delivered log/digest files in S3 without detection** (integrity validation off).
5. **Redirect or confuse the delivery pipeline** — make a trail deliver to, or confuse CloudTrail into writing to, a bucket outside the intended trust relationship (confused-deputy / cross-account).
6. **Mis-attribute an action** — forge or poison the attribution fields (`userAgent`, injected `requestParameters`) that defenders key alerts on.
7. **Exfiltrate secrets that land in the log** (request parameters captured in cleartext) via S3 read without holding the originating EC2 permission.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces**
- EC2 control-plane API (`ec2.amazonaws.com`) — every call is captured as a CloudTrail **management event** by default.
- CloudTrail configuration API (`cloudtrail.amazonaws.com`) — `PutEventSelectors`, `CreateTrail/UpdateTrail/DeleteTrail`, `StartLogging/StopLogging`, `CreateEventDataStore/UpdateEventDataStore`. **This is the real attack surface for evasion** — the knobs that decide what the first interface records.
- EC2 Instance Connect API (`ec2-instance-connect.amazonaws.com`) — `SendSSHPublicKey`, `SendSerialConsoleSSHPublicKey`. **Separate event source.**
- EBS direct APIs (`ebs.amazonaws.com`, `resources.type AWS::EC2::Snapshot`) — `GetSnapshotBlock`, `PutSnapshotBlock`, `ListSnapshotBlocks`, `ListChangedBlocks`. **Data events, off by default.**
- CloudTrail Lake — SQL queries over an immutable event data store (ORC).

**Processing / storage behind it**
- CloudTrail capture → event selector evaluation → delivery.
- **Delivery sinks:** (a) 90-day *Event history* (management events only, immutable, free, cannot be narrowed by selectors); (b) a **trail** → customer S3 bucket (+ optional hourly **digest files** when integrity validation is enabled); (c) a **CloudTrail Lake event data store** (immutable, selector-filtered).
- Encryption: S3 logs may be SSE-S3 or customer-managed SSE-KMS (trail-level setting).

**Accounts / trust zones**
- Single customer account (standard trail), OR **organization trail** owned by the management account aggregating all member accounts into one management-account bucket.
- CloudTrail service principal `cloudtrail.amazonaws.com` writes to the customer bucket (service-to-customer-resource crossing → confused-deputy zone).

**Identifiers of interest**
- `userIdentity.arn` / `principalId` / `accessKeyId` (attribution subject — and a *selector field*).
- `sourceIPAddress`, `userAgent` (attribution signals; `userAgent` is caller-controlled).
- Trail ARN (`aws:SourceArn` value), S3 bucket name (global namespace), KMS key id.
- `recipientAccountId` vs `userIdentity.accountId` (the Instance Connect example shows these differing — a cross-account shape).

**ASCII pipeline**
```
EC2 API (ec2.amazonaws.com) ──┐
EC2 Instance Connect ─────────┤
  (ec2-instance-connect)      │          ┌─ Event history (mgmt only, 90d, immutable, free)
EBS direct (ebs, DATA evt) ───┼─ capture ┼─ event-selector filter ─┬─ Trail ─▶ S3 bucket ─(opt)▶ digest files
CloudTrail config API ────────┘          │   (readOnly / eventSource│                 (SSE-S3 | SSE-KMS)
  (the control knobs) ───────────────────┘    / userIdentity.arn /  └─ Lake event data store (immutable, SQL)
                                               eventName / eventType)
                      ▲ attacker who holds cloudtrail:* edits the filter here = evasion
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (what proves it broke) |
|---|---|---|---|
| Attacker IAM principal in account | The *record* of its own EC2 actions | `PutEventSelectors` / `UpdateEventDataStore` narrowing | A security-relevant EC2 action occurs but no event is delivered, while `GetEventSelectors`/console still reports the trail "enabled / logging management events". |
| Attacker | Snapshot bytes | EBS direct `GetSnapshotBlock` (data event, off by default) | Snapshot contents are read and **no CloudTrail event** appears on an otherwise-complete default trail. |
| Attacker | An EC2 instance's OS | Instance Connect key-push, then direct SSH (off-API) | Repeated/persistent interactive access with exactly one (or zero) `SendSSHPublicKey` events and no record of the session itself. |
| Attacker | Delivered log/digest files | S3 object write/delete when integrity validation is off | Log file modified or deleted in S3 with no digest/alarm; `aws cloudtrail validate-logs` not possible. |
| CloudTrail service principal | Customer/other S3 bucket | Bucket policy `Allow cloudtrail.amazonaws.com s3:PutObject` without `aws:SourceArn` | Another account's trail induces writes into / probes this bucket (confused deputy). |
| Member account actor | Org trail record (management account) | Org trail captures member activity into mgmt bucket | Member cannot stop/read the org record — but can the member suppress its *own* local trail and rely on no local record? (defender-coverage gap, not an AWS bug.) |
| Attacker-controlled input fields | Defender's SIEM / Lake query / console | `userAgent`, `requestParameters` logged verbatim | Attacker string in a log field alters a downstream parser/dashboard/query (log injection). |
| **Any surface** | **AWS service plane** | delivery role / CloudTrail KMS key / internal account id | **Hard stop + disclose.** |

---

## 4. API / Interface Inventory

| Name | Service / eventSource | Mutating? | Logged by default? | Role in attack | Notes |
|---|---|---|---|---|---|
| `RunInstances`, `TerminateInstances`, `StopInstances` | ec2 | yes | **Write mgmt — yes** | the audited baseline | doc's cited examples |
| `DescribeInstances`, `DescribeSecurityGroups`, `DescribeSubnets` | ec2 | no | **Read mgmt — yes by default, but droppable** | recon that `readOnly:false` selector silently drops | doc: read events "don't change your configurations" |
| `ModifyInstanceAttribute` (userData/launch spec) | ec2 | yes | Write mgmt — yes | privesc-adjacent (see Lens B variant) | not on this page, but reaches a role's creds |
| `GetSnapshotBlock`, `ListSnapshotBlocks`, `ListChangedBlocks`, `PutSnapshotBlock` | **ebs** | read+write | **NO — data event, off by default** | **read snapshot bytes unlogged** | `resources.type AWS::EC2::Snapshot` |
| `SendSSHPublicKey` | **ec2-instance-connect** | yes (transient key) | mgmt — yes, but **different eventSource** | audits the key-push, not the session | 60s key; separate from `ec2.*` |
| `SendSerialConsoleSSHPublicKey` | ec2-instance-connect | yes | mgmt — yes | serial-console access, separate event | |
| `PutEventSelectors` / `UpdateEventDataStore` | cloudtrail | yes | Write mgmt — yes (**if the attacker didn't exclude themselves first**) | **the evasion knob** | can filter by `eventSource`, `readOnly`, `eventName`, `userIdentity.arn`, `eventType`, `sessionCredentialFromConsole` |
| `StopLogging` / `DeleteTrail` / `UpdateTrail` | cloudtrail | yes | Write mgmt — yes | blinding primitive | |
| `GetEventSelectors` / `GetTrailStatus` | cloudtrail | no | Read mgmt — yes | recon on current coverage | |

**Undocumented / easily-missed knobs (route to Lens O/U):** the `userIdentity.arn` **NotStartsWith** selector field — the management-events doc *literally ships an example* titled "Exclude management events for a specific IAM identity" that drops all events from `assumed-role/bucket-scanner-role`. The same primitive drops the attacker's own role. Console-driven users rarely see this; it is a CLI/API field.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — "All EC2 API actions are logged" is a default-only, selector-defeatable, EC2-API-scoped claim  [Lens U + Lens O]  ★ highest priority
**Background.** The target page states flatly: *"All Amazon EC2 API actions are logged as management events."* The management-events doc qualifies this heavily: logging is the **default**, but a trail/EDS can be reconfigured with advanced event selectors to **exclude by `eventSource`, `readOnly`, `eventName`, `eventType`, `userIdentity.arn`, or `sessionCredentialFromConsole`**.
**Security Concern.** The sentence reads as an invariant ("all … are logged") but is only a *default*. Three concrete erosions, each leaving the trail reporting "enabled / logging management events":
- **Write-only narrowing:** a selector with `readOnly:false` drops **every** EC2 `Describe*`/`Get*` recon call. The doc confirms read events are logged by default and are separable.
- **`eventSource NotEquals ec2.amazonaws.com`-style exclusion** (the KMS/RDS examples prove the mechanism) silently removes all EC2 events.
- **Scope mismatch:** the claim covers only `ec2.amazonaws.com`. EC2 Instance Connect (`ec2-instance-connect.amazonaws.com`) and EBS direct (`ebs.amazonaws.com`) are **different event sources** → a trail/alert keyed on `ec2.amazonaws.com` misses them even with full logging. (→ Areas 3, 4.)
**High-level Test Scenarios.**
- Claim: *A trail that `GetTrailStatus` reports as logging can be configured so a chosen EC2 write action produces no delivered event.* Oracle: configure a selector excluding `ec2.amazonaws.com` (or the specific `eventName`), run `StopInstances`, confirm the event is absent from S3/Lake while status = logging.
- Claim: *The EC2 doc's guarantee is not qualified with the selector caveat.* Oracle: doc-vs-mechanism inconsistency — the EC2 page never links the "read/write events" or "exclude event source" behavior. **Reportable as a documentation-integrity defect (Informational/Low), because a customer could build a compliance control on the literal "all … are logged" wording.**
**Doc evidence.** EC2 page §"Amazon EC2 API management events in CloudTrail"; management-events doc §"Read and write events" and §"Examples … exclude … event source". **Severity-if-true:** Low–Medium (the configurable-evasion itself is a customer footgun; the *doc guarantee gap* is the AWS-owned, reportable piece).

### Area 2 — The "exclude a specific IAM identity" selector is a precise self-blinding primitive  [Lens O + Lens E]  ★
**Background.** The management-events doc ships a ready-made example: a selector with `{"Field":"userIdentity.arn","NotStartsWith":["arn:aws:sts::123456789012:assumed-role/bucket-scanner-role"]}` that logs everything **except** that identity.
**Security Concern.** An attacker who holds `cloudtrail:PutEventSelectors` / `cloudtrail:UpdateEventDataStore` (an authorization frequently lumped into broad "logging admin" or "security tooling" roles, and almost never scoped to forbid *self-exclusion*) can insert a selector excluding **their own** assumed-role ARN. AWS itself warns that this authorization is dangerous: the *CloudTrail security best practices* doc states *"Users with the `AWSCloudTrail_FullAccess` policy have the ability to disable or reconfigure the most sensitive and important auditing functions in their AWS accounts. This policy is not intended to be shared or applied broadly to IAM identities in your AWS account."* (`cloudtrail/.../best-practices-security.html`). Note `cloudtrail:*` is a **separate action namespace from `ec2:*`** — "EC2 permissions alone" never grant it; the risk is a role that bundles both (a common over-provisioning anti-pattern). The trail then logs normally for every other principal — passing most "is logging enabled?" and "is EC2 covered?" checks — while the attacker operates invisibly. This is strictly stealthier than `StopLogging` (which trips Config rules / GuardDuty `Stealth:IAMUser/CloudTrailLoggingDisabled`).
**High-level Test Scenarios.**
- Claim: *An attacker can carve their own `userIdentity.arn` out of a trail while leaving it "enabled, all event sources".* Oracle: add the NotStartsWith selector for the attacker role, perform EC2 actions as that role, confirm absence in S3 while other principals' events still land.
- Claim: *The act of editing selectors is itself logged, so a defender could notice.* Oracle: confirm `PutEventSelectors` emits a `cloudtrail.amazonaws.com` event — but note that if the attacker **first** excludes their own ARN and **then** performs the edit under that ARN, even the edit may be filtered (ordering race). Test which happens first.
- Left/right: does the exclusion also apply to **Event history** (90-day)? Doc says selector settings "do not apply to Event history" — so Event history is a residual detection channel. Verify EC2 actions still appear there (they should), making this a *trail/Lake* blind spot, not total.
**Doc evidence.** management-events doc §"Example: Exclude management events for a specific IAM identity"; note "settings that you apply to a trail or event data store do not apply to Event history". **Severity-if-true:** High as an attacker-stealth primitive (durable, selective, status-clean); but **owner-to-fix is the customer's IAM scoping** → in scope as a *detection-evasion technique to document*, not as an AWS code bug. Worth flagging to AWS only if `PutEventSelectors` can exclude the editing principal's own edit event (a genuine design gap).

### Area 3 — EBS direct APIs read snapshot bytes with no record on a default trail  [Lens X + Lens O + Lens U]  ★ highest priority
**Background.** EBS direct APIs (`GetSnapshotBlock`, `ListSnapshotBlocks`, `ListChangedBlocks`) read the raw block contents of an EBS snapshot. The data-events doc confirms they are **data events** (`resources.type AWS::EC2::Snapshot`) and that *"By default, trails and event data stores do not log data events."*
**Security Concern.** This is the classic **lower-level-cousin parity gap** (Lens X): the management-event path to snapshot data (`CreateSnapshot`, `CopySnapshot`, `CreateVolume` from snapshot) is logged by default, but the **`ebs.amazonaws.com` direct-read path to the same bytes is not**. An attacker with `ebs:GetSnapshotBlock`/`ListSnapshotBlocks` can exfiltrate the entire contents of a snapshot (OS disk, secrets, DB files) and, on the overwhelmingly common default-trail configuration, generate **zero** CloudTrail evidence. The EC2 page's "all EC2 API actions are logged" wording actively hides this because EBS direct is a sibling API family under a different event source.
**High-level Test Scenarios.**
- Claim: *Snapshot contents can be read via `GetSnapshotBlock` with no event on a trail logging all management events.* Oracle: with a default trail (management events, all sources), read blocks from a canary snapshot, confirm no CloudTrail record; then enable data events for `AWS::EC2::Snapshot` and confirm the records appear — proving the gap is a default-off data-event, not a bug.
- Claim: *A detection built on `ec2:CreateSnapshot`/`CopySnapshot` misses `ebs:*` exfiltration.* Oracle: compare event presence between the two paths.
- Left/right: `PutSnapshotBlock` (write) — can an attacker modify a snapshot's blocks unlogged on a default trail, planting a backdoor into a disk image that will later boot?
**Doc evidence.** data-events doc: EBS direct APIs = `AWS::EC2::Snapshot` data events; "By default, trails and event data stores do not log data events." **Severity-if-true:** High (unlogged bulk data exfiltration). The *default-off* is an AWS design choice (defensible, cost-driven) → the **reportable AWS-owned piece is the EC2 doc guarantee** that implies completeness it does not have.

### Area 4 — EC2 Instance Connect audits the key-push, not the session  [Lens O + Lens M + Lens U]
**Background.** The target page's "Audit connections made using EC2 Instance Connect" section presents `SendSSHPublicKey` (eventSource `ec2-instance-connect.amazonaws.com`) as the way to "audit the users that connect to your instances." The event records `instanceId`, `osUser`, `publicKey`, `sourceIPAddress`.
**Security Concern.** `SendSSHPublicKey` pushes a **transient (~60s) public key** to the instance; the **actual SSH session** that follows is a direct TCP connection to the instance that does **not** traverse the AWS API and is **not** in CloudTrail. Therefore:
- The audit records the *authorization to connect*, not the connection, its duration, or what was done. One `SendSSHPublicKey` event can precede a long-lived session (keep the TCP session open; or, within the key's validity, establish a session that persists).
- `sourceIPAddress` in the event is the IP of the API caller, which may differ from the IP of the SSH session itself.
- Access paths that bypass this event entirely leave the "audit Instance Connect" control blind: a key added directly to `authorized_keys` / baked into the AMI, SSM Session Manager (`StartSession`, eventSource `ssm.amazonaws.com`), a classic key-pair SSH, or serial console (`SendSerialConsoleSSHPublicKey`, a *different* event). A defender auditing only `ec2-instance-connect.amazonaws.com` sees none of these.
- The doc example shows `userIdentity.accountId` `123456789012` but `recipientAccountId` `0987654321` — a **cross-account** shape; investigate whether the instance-owner account receives the connection record or only the caller's account.
**High-level Test Scenarios.**
- Claim: *An interactive session can outlive / be decoupled from its single `SendSSHPublicKey` event.* Oracle: push one key, establish a session, keep it active past 60s, perform actions over minutes — confirm no further events.
- Claim: *A key pushed for `osUser:ec2-user` can be used to authenticate as a different OS user if the instance's `authorized_keys`/PAM is permissive.* Oracle: push for one user, attempt login as another; refute if the instance enforces per-user key placement.
- Claim: *Instance-owner account lacks a record when connect is driven cross-account.* Oracle: compare where the `SendSSHPublicKey` event lands (caller vs recipient account).
**Doc evidence.** target page §"Audit connections made using EC2 Instance Connect"; the example event's `recipientAccountId` ≠ `accountId`. **Severity-if-true:** Medium–High (false sense of session auditability; attribution/coverage gap). The session-not-logged behavior is inherent to SSH, not an AWS bug — the **reportable angle is the doc framing** that `SendSSHPublicKey` lets you "audit the users that connect," which overstates coverage.

### Area 5 — Log/digest tamper when integrity validation is off (creation-path-dependent)  [Lens O tamper]
**Background.** Log file integrity validation (SHA-256 hashing + RSA-signed hourly **digest files**) default **depends on how the trail was created**: the enabling doc says *"By default, this feature is enabled for new trails"* via the **console**, but the **CLI/API path is opt-in** — *"use the `--enable-log-file-validation` option"* (`cloudtrail-log-file-validation-enabling`). A trail provisioned by CLI/CloudFormation/Terraform without that flag delivers **no digest files**. Separately, log immutability (S3 Object Lock / MFA-Delete) is never default — the best-practices doc frames MFA-Delete as optional hardening and notes *"The CloudTrail trail default is to store log files indefinitely"* with no delete-protection.
**Security Concern.** When validation is off, an attacker who can write/delete objects in the log bucket (via a separate S3 misconfiguration, a bucket-policy weakness, or compromised credentials) can **modify or delete delivered CloudTrail log files with no cryptographic trip-wire** — there is no digest to compare against, and `aws cloudtrail validate-logs` cannot assert integrity. This converts an S3-write primitive into targeted log forgery/erasure.
**High-level Test Scenarios.**
- Claim: *A delivered EC2 log object can be altered/deleted and still "validate" (because nothing validates).* Oracle: `aws cloudtrail get-trail-status` → check `LogFileValidationEnabled`; on a CLI/IaC-provisioned trail it is often `false`. With validation off, delete a log object; confirm no digest/alarm; then enable validation and confirm the digest chain would have detected it.
- Left/right: even with validation **on**, the digest files land in the **same bucket** ("delivered to the same Amazon S3 bucket associated with your trail"). If the attacker can delete both the log *and* the digest and the chain is not independently archived (no S3 Object Lock / MFA Delete / separate account), detection depends on noticing a missing digest. Test whether a *gap* in the digest chain is alarmed by anything by default (it is not — the customer must run `validate-logs`).
**Doc evidence.** integrity-validation doc: "Enabling log file integrity validation allows CloudTrail to deliver digest log files … but does not validate the integrity"; digests "delivered to the same Amazon S3 bucket". **Severity-if-true:** Medium (tamper-detection gap; depends on a separate write primitive). Default-off is a customer footgun → documentation/hardening note, not an AWS code bug.

### Area 6 — CloudTrail→S3 confused-deputy: `aws:SourceArn` is "best practice", not enforced  [Lens B + Lens R/S + Lens EE]  ★
**Background.** The CloudTrail service principal `cloudtrail.amazonaws.com` writes log objects into the customer's S3 bucket. The S3-bucket-policy doc says: *"As a security best practice, add an `aws:SourceArn` condition key"* — i.e. it is **optional**, and historically CloudTrail attached bucket policies **without** it.
**Security Concern.** This is a textbook **confused-deputy** seam (and an **AWS-authored sample-policy audit**, Lens R — the customer copies this JSON verbatim):
- Without `aws:SourceArn`/`aws:SourceAccount`, a bucket policy that `Allow`s `cloudtrail.amazonaws.com` to `s3:PutObject`/`s3:GetBucketAcl` is satisfiable by **any account's** trail. An attacker who knows/guesses a victim bucket name and whose own trail targets it can induce CloudTrail (the deputy) to probe/write to it, or conversely a victim's logs can be caused to land cross-account.
- The `s3:PutObject` `Resource` is a **wildcard** (`…/AWSLogs/{{myAccountID}}/*`) — audit whether the account-id segment is actually pinned by condition or only by the resource string (which a sibling statement or org-write statement could broaden).
- **Lens EE angle:** the destination bucket name is in S3's **global namespace**. Explore whether a predictable/convention-based CloudTrail bucket name (`aws-cloudtrail-logs-<accountid>-<hash>` default naming) can be **pre-claimed** by an attacker so that a victim's `CreateTrail` default-bucket creation collides or so logs route to an attacker-owned bucket that already carries the permissive `cloudtrail.amazonaws.com` policy.
**High-level Test Scenarios.**
- Claim: *A bucket policy lacking `aws:SourceArn` accepts writes driven by a foreign-account trail.* Oracle: point a second-account trail at a bucket whose policy omits SourceArn; confirm cross-account delivery/ACL-check succeeds; add SourceArn and confirm it is denied.
- Claim: *The AWS-published sample policy ships SourceArn only as prose ("best practice"), so a copy-paste customer is confused-deputy-exposed by default.* Oracle: audit the printed JSON — the base `s3-bucket-policy` block *does* include SourceArn in the current doc, but the "receiving logs from other accounts" and legacy variants must be checked statement-by-statement.
- Claim: *An attacker can occupy the predictable default bucket name.* Oracle: test default `CreateTrail` bucket-naming determinism and global-namespace pre-registration.
**Doc evidence.** s3-bucket-policy doc: "As a security best practice, add an `aws:SourceArn`…"; org-trail third statement writes to `…/AWSLogs/{{o-organizationID}}/*`; "You can configure CloudTrail to deliver log files from multiple AWS accounts to a single S3 bucket." **Severity-if-true:** Medium–High if a copy-verbatim AWS artifact leaves a confused-deputy open (Lens R Tier-2, route `aws-security`); the bucket pre-registration angle is High if demonstrable (route `aws-security`).

### Area 7 — Secrets captured in `requestParameters` readable via S3 without EC2 permission  [Lens T]
**Background.** CloudTrail records `requestParameters`/`responseElements` verbatim. The Instance Connect example logs the **public key** in cleartext; general EC2 events log instance ids, and potentially sensitive launch parameters.
**Security Concern.** A principal who can read the **log S3 bucket** (e.g. a SIEM-ingest role, a broad `s3:GetObject`, or a cross-account log-sharing grant) but who has **no EC2 permissions** can recover whatever sensitive values EC2 writes into the log. Investigate which EC2 request/response fields CloudTrail captures vs redacts — especially `RunInstances` **UserData** (frequently contains bootstrap secrets/credentials), `ImportKeyPair` key material, `GetPasswordData`/`responseElements` password data, and `ModifyInstanceAttribute(userData)`. If any lands un-redacted, the log bucket becomes a **secret store reachable under weaker IAM than the originating API** (the Lens T wall-bypass shape).
**Key doc signal.** The CloudTrail record-contents reference states the **only** documented `requestParameters` exclusion is a generic size cap: *"This field has a maximum size of 100 KB. When the field size exceeds 100 KB, the `requestParameters` content is omitted."* There is **no documented per-service/per-field redaction for EC2** — so a `RunInstances` call with sub-100 KB UserData is a strong candidate to land in the log verbatim (base64). This elevates the lead from "believed" to "documented absence of any redaction mechanism."
**High-level Test Scenarios.**
- Claim: *`RunInstances` UserData appears (base64) in the CloudTrail event's `requestParameters.userData`.* Oracle: launch an instance with a canary UserData string < 100 KB, inspect the delivered event; refute only if CloudTrail silently omits UserData (**doc-gap — the record-contents doc describes only the 100 KB cap, so confirm against a live event**).
- Claim: *A role with only `s3:GetObject` on the log bucket and an explicit EC2 deny can still read the captured parameters.* Oracle: prove the EC2 deny and the S3 read allow in one run under a scoped role. Note the log-bucket read grant is frequently broad (shared "log-archive" buckets per the "Receiving log files from other accounts" pattern).
**Doc evidence.** target page example events show `requestParameters` captured in full (incl. the Instance Connect `publicKey`); `cloudtrail-event-reference-record-contents` documents only the 100 KB truncation; EC2-specific redaction is **not stated anywhere → doc-gap**. **Severity-if-true:** High if a secret-bearing field (UserData, `ImportKeyPair` material) is un-redacted — the audit log becomes a secrets-exfil channel reachable by a principal with zero EC2 privilege (owner-to-fix shared: AWS owns the capture/redaction default, customer owns log-bucket IAM and the UserData-secrets anti-pattern).

### Area 8 — Log injection via attacker-controlled fields  [Lens O/F/Q-adjacent]
**Background.** `userAgent` is fully attacker-controlled, and several `requestParameters` carry attacker-supplied strings (tag values, names, the Instance Connect `publicKey`/`osUser`). All land in the JSON log and in CloudTrail Lake / downstream SIEMs.
**Security Concern.** (a) **Attribution poisoning:** a defender keying detections on `userAgent` (the doc markets it as an identifying field) can be evaded or mis-directed by spoofing a benign agent string. (b) **Log/SIEM injection:** attacker strings containing newlines, JSON control characters, or SQL/HTML metacharacters can corrupt log parsers, poison CloudTrail Lake SQL queries that `SELECT` on these fields, or achieve stored-XSS in a SIEM dashboard that renders them.
**High-level Test Scenarios.**
- Claim: *`userAgent` is caller-set and unreliable for attribution.* Oracle: send an EC2 call with a forged `User-Agent`, confirm it is logged verbatim.
- Claim: *An attacker string in a logged `requestParameters` field (e.g. a resource tag or `osUser`) breaks a downstream Lake query or dashboard.* Oracle: inject control chars, run a representative Lake query, observe parse corruption. (Scope: self-targeting unless the log is consumed by a shared/central SIEM → then cross-boundary.)
**Doc evidence.** target page example events contain `userAgent` and verbatim `requestParameters`; CloudTrail Lake "run SQL-based queries on your events". **Severity-if-true:** Low (attribution) to Medium (SIEM injection, if a central consumer is reachable).

### Area 9 — Organization-trail coverage asymmetry  [Lens AA + Lens O]
**Background.** For an org trail, "organization log files are accessible only to the management account"; member accounts cannot read or stop the org trail.
**Security Concern.** This is mostly a *defensive strength* (member attacker cannot `StopLogging`/`DeleteTrail`/reconfigure the org trail — *"users in member accounts do not have sufficient permissions to … turn logging on or off, change what types of events are logged, or otherwise change an organization trail in any way"*). Nuance to respect: member accounts **do** retain their own local 90-day *Event history* regardless of the org trail (*"To view member account events in Event history, sign in with the member account"*), so a member is not fully blind — what they lack is independent long-term S3 custody of their own record (delegated entirely to the management account). Residual concerns: a member attacker can still `StopLogging`/narrow their **own** account-level trail (if any), and revocation completeness — when an account **leaves** the organization, does the org trail stop capturing it cleanly, and are previously-delivered member logs retained or orphaned?
**High-level Test Scenarios.**
- Claim: *A member attacker cannot blind the org trail.* Oracle: attempt `StopLogging`/`PutEventSelectors` on the org trail from a member principal → expect AccessDenied (confirms the strength; refuting it = High finding).
- Claim: *Account removal from the org creates a logging gap.* Oracle: doc-gap — confirm capture behavior across the leave boundary.
**Doc evidence.** s3-bucket-policy doc §org trail: "organization log files are accessible only to the management account." **Severity-if-true:** mostly Informational; High only if a member can mutate the org trail.

### Area 10 — Log-encryption default self-contradiction (SSE-KMS vs SSE-S3)  [Lens U + Lens H/Y]
**Background.** Two AWS pages disagree on the default. *best-practices-security* asserts *"By default, the log files delivered by CloudTrail to your S3 bucket are encrypted by using server-side encryption with a KMS key (SSE-KMS)."* The dedicated encryption page qualifies it: *"**If you don't enable SSE-KMS encryption**, your log files and digest files are encrypted using SSE-S3 encryption."*
**Security Concern.** The second statement implies SSE-KMS is **opt-in** (so the real default is SSE-S3). This matters because the "who can read the log" boundary AWS advertises for SSE-KMS — *"A user must have S3 read permissions for the bucket … [and] a policy or role applied that allows decrypt permissions by the KMS key policy"* — **only exists if SSE-KMS was actually configured.** Under the SSE-S3 default, the KMS decrypt gate is absent, and anyone with `s3:GetObject` on the bucket reads the logs (amplifying Area 7's secrets-in-logs reach).
**High-level Test Scenarios.**
- Claim: *A freshly created trail with no explicit KMS config stores logs under SSE-S3, not SSE-KMS.* Oracle: `aws cloudtrail get-trail` → check for a `KmsKeyId` field; absent ⇒ SSE-S3 ⇒ no KMS reader gate.
- Claim: *The doc contradiction is itself an AWS doc-integrity defect a compliance control could rely on.* Oracle: the two quoted sentences conflict directly.
**Doc evidence.** `best-practices-security` vs `encrypting-cloudtrail-log-files-with-aws-kms`. **Severity-if-true:** Low as a pure doc inconsistency; Medium as an enabler of Area 7 (no KMS gate on secret-bearing logs). AWS-owned (doc + default behavior).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Perform EC2 write with zero delivered event on a "logging" trail | event selectors | "By default, trails … log management events" (default ≠ guarantee) |
| Self-exclude attacker ARN from logging | `userIdentity.arn` selector | the shipped "exclude a specific IAM identity" example *is* the primitive |
| Exfiltrate snapshot bytes unlogged | EBS direct APIs | "data events are not logged by default" |
| Long-lived instance session behind one key-push | EC2 Instance Connect | "audit the users that connect" (audits key-push only) |
| Tamper/delete delivered logs undetected | integrity validation | validation is opt-in; digests share the bucket |
| Cross-account/confused-deputy log delivery | S3 bucket policy | `aws:SourceArn` is "best practice", not enforced |
| Read secrets from log bucket without EC2 perms | `requestParameters` capture | redaction behavior unstated for EC2 (doc-gap) |
| Pre-claim predictable log bucket name | S3 global namespace | default bucket naming determinism (doc-gap) |
| Poison attribution via `userAgent` | log fields | doc markets `userAgent` as identifying |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Customer-authored IAM / trail-config footguns** as AWS bugs: a customer choosing write-only selectors, excluding event sources, skipping integrity validation, over-granting `s3:GetObject` on the log bucket, or omitting `aws:SourceArn` in a *bucket policy they wrote* — these are customer responsibility. In scope only as **techniques to document** or where the weakness is in an **AWS-authored copy-verbatim artifact** (Area 6) or contradicts an **AWS doc guarantee** (Areas 1, 3, 4).
- **CloudTrail's own default of not logging data events** — a defensible, cost-driven AWS design choice; the reportable piece is the EC2 doc's overbroad "all actions" wording, not the default.
- **SSH session content not appearing in CloudTrail** — inherent to SSH/TCP, not an AWS defect.
- **Billing/DoS via misconfigured-trail 30-day redelivery charges** — product/cost behavior, out of scope.
- **Cross-tenant data access, SSRF, prompt injection, upload parsing** — no mechanism on these pages (see §8).
- **Anything implicating AWS's own service plane** — hard stop + disclose, not to be exploited.

## 8. Null hypotheses / doc gaps (pages checked named)

- **Lens A (cross-tenant IDOR):** N/A. Pages checked: `monitor-with-cloudtrail`, `logging-management-events`, `logging-data-events`, `create-s3-bucket-policy`. This is single-account audit config; no shared-fleet resource-by-id surface. (The *org-trail* and *cross-account log sharing* are the only cross-account seams → covered as Lens B/AA in Areas 6, 9.)
- **Lens G (SSRF):** N/A. Pages checked: all four above. No field the service dereferences server-side (no URL/webhook/fetch field on these pages).
- **Lens K (prompt injection) / Lens F (translation injection, backend):** N/A — no LLM; the only "translation" is CloudTrail Lake SQL over the customer's own store (self-targeting), captured as the log-injection angle in Area 8.
- **Lens P (proofing), Lens W (attestation), Lens FF (JWT), Lens CC (upstream-context), Lens BB (canonicalization), Lens V (network), Lens N (namespace migration), Lens J (OAuth), Lens I (tagging), Lens DD (cache):** N/A for this doc set — no corresponding mechanism on the CloudTrail integration pages.
- **Lens H/Y (KMS/encryption):** fires — see **Area 10** (SSE-KMS-vs-SSE-S3 default contradiction). The EC2 CloudTrail page itself does not describe trail KMS config; **doc-gap — confirm actual default via `get-trail` `KmsKeyId` if testing Areas 7/10.**
- **Doc-gaps to resolve before hunting:** (1) whether EC2 `RunInstances` **UserData** is captured or redacted in the CloudTrail event (Area 7); (2) default CloudTrail bucket-naming determinism / global pre-registration (Area 6); (3) exact event source string for EBS direct APIs (`ebs.amazonaws.com` assumed; data-events doc gave `resources.type` but not the eventSource — confirm against a live event, Area 3); (4) whether `PutEventSelectors` can filter the editing principal's own edit event (Area 2); (5) org-trail capture behavior across an account-leave boundary (Area 9).

---

### Priority order for a hunter
1. **Area 3** (EBS direct snapshot read, unlogged on default trail) — highest-impact unlogged exfiltration, concrete oracle.
2. **Area 1 / Area 2** (selector-based evasion; self-exclude ARN) — the core evasion primitives; Area 2 is the stealthiest.
3. **Area 6** (CloudTrail→S3 confused-deputy / bucket pre-claim) — only lead with a potential AWS-reportable artifact defect.
4. **Area 4** (Instance Connect session-vs-key-push coverage gap).
5. **Area 7** (secrets in logs reachable via S3) — pending the UserData-redaction doc-gap.
6. **Areas 5, 8, 9** (tamper-when-validation-off, log injection, org-trail asymmetry).

*Chaining note:* Area 6 (induce delivery to attacker bucket) + Area 5 (no integrity validation) + Area 7 (secrets in `requestParameters`) chains into **attacker-side collection of another account's audit stream containing cleartext secrets** — rate at the end of the chain (High/Critical) if each link confirms.
