# EC2 Fast Launch (Windows) — Attack Research Plan

**Source of leads:** `docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-ami-config-fast-launch.html` (hub) and its child pages — `win-start-fast-launch-prereqs`, `win-fast-launch-configure`, `win-view-fast-launch`, `win-fast-launch-manage-costs`, `win-fast-launch-monitor`, `slr-windows-fast-launch`, `win-fast-launch-troubleshoot` — plus the two AWS-managed IAM artifacts `EC2FastLaunchServiceRolePolicy` (SLR) and `EC2FastLaunchFullAccess` (customer prereq). Offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`. **Live re-validated 2026-09-22:** hub, configure, prereqs, view, monitor, and SLR pages verified live/offline-consistent; the `$Latest`/`$Default` PassRole-laundering warning is present verbatim on `win-fast-launch-configure`; the two AWS-managed policy JSONs re-fetched from the Managed Policy Reference and found **UNCHANGED vs the 2026-09-12 audit** — SLR `EC2FastLaunchServiceRolePolicy` still **v7 (edited 2026-02-12)**, `EC2FastLaunchFullAccess` still **v5 (edited 2026-08-04)**, both crown-jewel over-grants intact (see §5.1); **no "See also" / AI-agent injection block on any of the 8 Fast Launch pages** (grep `agent-toolkit` → NONE across the tree; unlike the windows-ami-reference siblings — watch for reappearance, see the see-also-injection memory).

**Status:** documentation-derived hypotheses only; nothing tested against a live account.

**Relationship to prior plans:** This plan supersedes the Fast Launch sketches folded into `ec2-windows-instances.html.md` (Area 3) and `security-iam.html.md` (Area 3/E2). It is the dedicated, page-complete plan for the Fast Launch feature tree. Cross-links: `[[project_ec2-windows-instances-plan]]`, `[[project_ec2-security-iam-plan]]`, `[[project_launch-templates-plan]]`, `[[project_sysprep-ami-plan]]`, `[[project_sharing-amis-plan]]`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **Scope reality:** The Fast Launch provisioning t3 instances and the auto-created VPC/subnet/LT/SG run **inside the customer's own account** (the prereq CloudFormation stack is created "in your AWS account"; the SLR launches instances "on your behalf"). So the PassRole/credential-harvest paths are **genuinely reachable intra-account** — they are *not* a service-plane hard-stop. Correct a stale earlier note that treated the t3 fleet as AWS-owned; only the `ec2fastlaunch.amazonaws.com` orchestration control plane is AWS-owned.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — e.g. reaching the `ec2fastlaunch.amazonaws.com` control plane, or IMDS/creds of an AWS-operated (not customer-account) provisioning host — stop, preserve evidence, flag for AWS-Security disclosure.
- **Owner-to-fix triage:** `EC2FastLaunchServiceRolePolicy` (SLR) and `EC2FastLaunchFullAccess` are **AWS-authored and uneditable / copy-verbatim** → any over-grant in them is **AWS's defect = Tier 2, route `aws-security`**, NOT a customer footgun. A weakness a customer creates in *their own* launch template or IAM policy is a footgun (out of scope / Low).

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce:
1. **Non-`PassRole` privilege escalation:** a principal holding neither `iam:PassRole` nor `EC2FastLaunchFullAccess` causes a Fast Launch provisioning instance to run with an arbitrary (e.g. admin) instance profile, then harvests those credentials from IMDS — using only `ec2:CreateLaunchTemplateVersion`/`ec2:ModifyLaunchTemplate` against a `$Latest`/`$Default`-configured Fast Launch AMI. **(This is the crown jewel — AWS documents the primitive itself.)**
2. **Cross-account snapshot access:** a consumer account that only has *launch* access to a shared Fast Launch AMI reads, copies, or otherwise reaches the **pre-provisioned snapshots that come from the AMI owner's account** (the docs say the consumer "can still use snapshots from the AMI owner's account" when its own are depleted).
3. **Snapshot remanence / secret recovery:** recover a consumed pre-provisioned snapshot (which contains a fully Sysprep-specialized + OOBE'd Windows image, potentially with baked state/credentials) via Recycle Bin retention after Fast Launch "deletes ... to prevent reuse."
4. **SLR over-privilege:** demonstrate the `AWSServiceRoleForEC2FastLaunch` SLR (or `EC2FastLaunchFullAccess`) authorizes an action its stated purpose does not need — unscoped `iam:PassRole`, over-broad `RunInstances`, KMS grant, or instance-profile scope wider than the `*ec2fastlaunch*` name the prose claims.
5. **Revocation completeness:** after an AMI owner disables Fast Launch / stops sharing, prove a consumer still consumes owner snapshots, or a KMS grant to the SLR survives feature-disable (orphaned grant).
6. **Enable-on-shared-AMI abuse:** a consumer enabling Fast Launch on a *shared* AMI forces cost/resource creation or state changes the owner did not consent to (griefing / consent boundary).

---

## 2. Components, Assets, and Design

**Customer-facing interface (all SigV4 IAM, EC2 Query API / SDK / CLI / console / CloudFormation):**
- `EnableFastLaunch` / `DisableFastLaunch` / `DescribeFastLaunchImages` (CLI: `enable-fast-launch`, `disable-fast-launch`, `describe-fast-launch-images`).
- Parameters: `ImageId`, `MaxParallelLaunches` (≥6; account quota 40/region), `ResourceType=snapshot`, `SnapshotConfiguration.TargetResourceCount`, `LaunchTemplate{Id|Name, Version}` (version may be a number **or the `$Latest`/`$Default` alias**).
- EC2 Image Builder integration (`FastLaunchConfiguration` in distribution settings) can enable Fast Launch as part of an Image Builder pipeline.

**Behind-the-interface processes / fleets:**
- **`ec2fastlaunch.amazonaws.com`** — the AWS-owned control plane / service principal that orchestrates pre-provisioning. **(AWS service plane — hard stop if reached.)**
- **Provisioning t3 instances** — temporary `t3`/`t3.xlarge` instances launched **in the customer account/VPC**, run Sysprep specialize + Windows OOBE, get snapshotted, then stopped/terminated. Each instance is allotted 30 minutes.
- **Auto-created CloudFormation stack** (when no custom LT and no default VPC): a VPC, private subnets across AZs, a launch template configured for **IMDSv2**, and a **security group with no inbound or outbound rules**. (Note: this is a *hardened* default — SG closed, IMDSv2 on.)
- **Recycle Bin** (Amazon EBS) — can retain "deleted" pre-provisioned snapshots if a retention rule matches.
- **EventBridge / CloudWatch** — `EC2 Fast Launch State-change Notification` events + `AWS/EC2` namespace metrics.

**Accounts / ownership:**
- Single-customer account owns the AMI, the SLR, the provisioning instances, the snapshots, the CFN stack.
- **Cross-account seam:** a shared AMI. The **AMI owner's account** holds one set of pre-provisioned snapshots; a **consumer account** that enables Fast Launch on the shared AMI holds its *own* set, but **falls back to consuming the owner's snapshots when depleted.**

**"Resource" identifiers & shapes:**
- `ImageId` (`ami-...`), `SnapshotId` (`snap-...`), `LaunchTemplateId` (`lt-...`) + version, instance profile ARN/name. `DescribeFastLaunchImages` returns `OwnerId` — **"not populated for AMIs that are shared with you."**

**Identity / roles:**
- Caller: SigV4 IAM principal (needs `ec2:EnableFastLaunch` etc.; if no custom LT, needs `EC2FastLaunchFullAccess`).
- **SLR `AWSServiceRoleForEC2FastLaunch`** (trusts `ec2fastlaunch.amazonaws.com`), policy `EC2FastLaunchServiceRolePolicy` (v7, see §5.1 for verbatim audit): EC2 RunInstances (**unconditioned** on network resources; tag-gated on volume/instance)/Stop/Terminate/CreateSnapshot/Delete*/CreateTags; **`iam:PassRole Resource:"*"`** (only `PassedToService`-gated — *not* name-scoped despite prose); CloudFormation `DescribeStacks`; CloudWatch `PutMetricData` (namespace `AWS/EC2`); EventBridge rule CRUD (`rule/FastLaunch*`). **KMS: only `kms:ListRetirableGrants` — the SLR does NOT create grants.** The CMK-use grant is created by the *customer's* own `kms:CreateGrant` (key-policy path) per `slr-windows-fast-launch.md`.
- **`EC2FastLaunchFullAccess`** — customer-attachable prereq (only needed when *not* supplying a custom LT). Hunter previously confirmed v5 grants **unrestricted `iam:PassRole` (`role/*` + `instance-profile/*`, only `PassedToService` condition) + `RunInstances` with no `CalledVia`** → pass any admin profile.

**Untrusted-input transforms:** minimal — no parser/translation layer. The main "untrusted content" seams are (a) a *shared* AMI's baked image content becoming a snapshot the consumer trusts, and (b) the consumer-controlled launch-template body that the SLR later executes.

```
Caller (IAM) --EnableFastLaunch(ImageId, LT=$Latest?)--> EC2 control API
                                                            |
                        (dry-run RunInstances perm check ONCE, at enable time)
                                                            v
              ec2fastlaunch.amazonaws.com (AWS control plane)  [HARD STOP]
                                                            |
        assumes SLR AWSServiceRoleForEC2FastLaunch (customer acct)
                                                            v
   launches temp t3 instances IN CUSTOMER VPC  <-- resolves LT $Latest/$Default AT LAUNCH TIME
        |  (Sysprep specialize + OOBE)             (NO re-check of caller perms)
        v
   pre-provisioned snapshot --> customer S3/EBS  --(consumed by launch, then "deleted")-->  Recycle Bin? (remanence)
        ^
   shared-AMI consumer falls back to OWNER-ACCOUNT snapshots when depleted  [CROSS-ACCOUNT SEAM]
```

---

## 3. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|---|
| B1 | Caller *without* `iam:PassRole` | An arbitrary IAM role/instance profile on a provisioning instance | Update `$Latest`/`$Default` LT version after the one-time enable-time dry-run check | An instance runs with a profile the caller could not `PassRole`; caller reads its creds from IMDS = **privilege escalation** |
| A1 | Shared-AMI consumer account | AMI **owner account's** pre-provisioned snapshots | "you can still use snapshots from the AMI owner's account" | Consumer reads/copies/enumerates a `snap-...` owned by the AMI owner = **cross-account snapshot access** |
| A2 | Any account with launch access | Owner Fast Launch config | `DescribeFastLaunchImages` on shared AMI | Config/`OwnerId`/LT details of the owner leaked via describe on a shared AMI |
| R1 | Principal holding only `EC2FastLaunchFullAccess` | Any role in the account (→ admin) | Unrestricted `iam:PassRole` in the AWS-managed policy | `SimulatePrincipalPolicy` allows `PassRole` on `role/*`; live pass of admin profile succeeds = **AWS-artifact privesc (Tier 2)** |
| R2 | SLR `AWSServiceRoleForEC2FastLaunch` | Instance profiles **not** named `*ec2fastlaunch*` / arbitrary roles | Policy `PassRole` scope wider than prose | Policy JSON `Resource` broader than the documented `*ec2fastlaunch*` = **doc-vs-artifact drift (Tier 2)** |
| AA1 | AMI owner (post-disable) / consumer | Owner snapshots, KMS grants | `DisableFastLaunch`, stop-sharing | Consumer still consumes owner snapshots after disable; KMS grant to SLR never retired = **revocation incompleteness** |
| Q1 | Attacker with `ebs:*`/Recycle-Bin read | Consumed pre-provisioned snapshot | Recycle Bin retention rule matches "deleted" snapshot | Recovering a specialized Windows image snapshot the service deleted "to prevent reuse" = **remanence** |
| H1 | Customer (grantor) → SLR (grantee) | Customer-managed KMS key | Customer `kms:create-grant --grantee AWSServiceRoleForEC2FastLaunch --operations CreateGrant` | Grant survives feature-disable (never retired), or the SLR (holding `CreateGrant` op) mints further grants = **grant sprawl / orphaned grant** (note: SLR's *own* IAM policy has only `ListRetirableGrants`, so retirement is the exit) |
| P1 | Shared-AMI consumer | Owner's cost/resources | Consumer `EnableFastLaunch` on a shared AMI | Owner incurs resource creation / state change without consent = **consent/griefing** |
| — | Any caller | `ec2fastlaunch.amazonaws.com` control plane / AWS provisioning hosts | — | **HARD STOP** — service plane |

---

## 4. API / Interface Inventory

| Name | Method | New/Exist | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `EnableFastLaunch` | POST (Query) | Exist | **Yes** | External | Enable pre-provisioning for an AMI; accepts `LaunchTemplate.Version=$Latest/$Default` | Yes (SigV4) | AMI owner **or any account with launch access to a shared AMI** | **Perm check is a one-time RunInstances dry-run at enable time only** |
| `DisableFastLaunch` | POST | Exist | Yes | External | Disable + clean up snapshots | Yes | Owner / consumer of shared AMI | "some pre-provisioned snapshots may still remain" on `disabling-failed` |
| `DescribeFastLaunchImages` | POST | Exist | No | External | List Fast Launch AMIs + LT/state/`OwnerId` | Yes | Any (per-AMI) | `OwnerId` **not populated for shared AMIs** — check what else it leaks on a shared AMI |
| (Image Builder) `FastLaunchConfiguration` | — | Exist | Yes | External | Enable Fast Launch via Image Builder distribution settings | Yes | Image Builder pipeline role | Alternate enable path — does it inherit the same `$Latest` laundering? |
| SLR-driven `RunInstances`/`StopInstances`/`TerminateInstances`/`CreateSnapshot`/`Delete*`/`CreateTags` | — | Exist | Yes | Internal (SLR) | Provisioning lifecycle in customer VPC | No (service-assumed) | `ec2fastlaunch.amazonaws.com` via SLR | Runs with SLR perms, resolves `$Latest`/`$Default` **at each launch** |
| `kms:CreateGrant` (customer→SLR) | — | Exist | Yes | External | Grant SLR CMK use for encrypted AMI | Yes | AMI owner | `--operations CreateGrant` grants the SLR the ability to create further grants |

**Undocumented / low-surfaced knobs to probe:** whether `EnableFastLaunch` accepts a `LaunchTemplate.Version` value beyond `$Latest`/`$Default`/number that changes binding semantics; whether `TargetResourceCount` / `MaxParallelLaunches` upper bounds are enforced server-side (quota bypass → cost griefing); whether `ResourceType` accepts any value other than `snapshot`.

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — `$Latest`/`$Default` launch-template PassRole laundering (CROWN JEWEL)
**Background:** Enabling Fast Launch triggers a **one-time** `RunInstances` **dry-run** permission check against the LT version *at enable time*. Thereafter the SLR launches provisioning instances repeatedly and **resolves `$Latest`/`$Default` at each launch, without re-checking the caller's permissions.**
**Security Concern:** The docs state verbatim: *"someone who can update the launch template could pass an IAM role or instance profile to an instance. This can happen even if they don't have the `iam:PassRole` permission for that role."* This is a documented **`iam:PassRole` bypass**: a principal with only `ec2:CreateLaunchTemplateVersion` / `ec2:ModifyLaunchTemplate` on a `$Latest`/`$Default`-bound Fast Launch AMI can inject an arbitrary `IamInstanceProfile`, and the SLR will launch a customer-account instance carrying it. Because provisioning instances run in the customer VPC, the caller (or a colluding IMDS-reachable path) can then harvest that profile's credentials → escalation to whatever the profile grants (e.g. admin).
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* With Fast Launch enabled on `$Latest`, a principal lacking `iam:PassRole` for role `Admin` can add an LT version specifying `IamInstanceProfile=Admin` and cause a provisioning instance to run with it. → *Oracle:* the launched t3 instance's IMDS returns `Admin` role credentials; refute if `RunInstances` by the SLR fails PassRole at launch (i.e. the SLR itself re-enforces PassRole for the *caller*). **Preconditions:** an existing `$Latest`-bound Fast Launch AMI + LT-modify rights. **Severity: High (intra-account privesc to admin).**
- *Claim:* The enable-time dry-run is the *only* PassRole gate; changing the LT after enable is never re-validated. → *Oracle:* modify LT version between enable and the next background replenishment launch; confirm the new profile is used.
- *Claim (chain):* Combine with a shared/owned AMI whose LT is writable by a low-priv team member → cross-team privesc.
**Doc evidence:** `win-fast-launch-configure.md` §"Permissions checks for EC2 Fast Launch". **Severity-if-true:** High. Owner-to-fix: partly AWS design (no re-check), partly customer (using `$Latest` + loose LT-modify IAM). The *design gap* (no re-check + SLR PassRole scope, see Area 4) is reportable; a customer choosing `$Latest` with loose IAM is a footgun. **Stop condition:** if credential harvest requires reaching an AWS-operated host rather than a customer-account instance → HARD STOP.

### Area 2 — Cross-account pre-provisioned snapshot access (shared AMI)
**Background:** For a shared Fast Launch AMI, "the pre-provisioned snapshots come from the AMI owner's account." A consumer that enables Fast Launch gets its own snapshots but, when depleted, "you can still use snapshots from the AMI owner's account."
**Security Concern (Lens A / X):** A consumer with only *launch* permission on the shared AMI is, by design, made able to **consume snapshots owned by another account.** Question whether that consumption is tightly mediated by the launch flow, or whether the consumer can name/read/copy the owner's `snap-...` directly (ownership-vs-existence), or whether a lower-level cousin (`ebs:GetSnapshotBlock`, `CopySnapshot`, `CreateVolume`) reaches the owner's snapshot bytes where the control-plane launch would refuse.
**High-level Test Scenarios:**
- *Claim:* The owner-account snapshot IDs consumed on the consumer's behalf are discoverable to the consumer (events, `DescribeSnapshots`, volume lineage) → enumeration oracle. → *Oracle:* consumer observes a `snap-...` with a foreign `OwnerId`.
- *Claim:* `ebs:GetSnapshotBlock` / `CopySnapshot` / `CreateVolume` by the consumer against the owner's pre-provisioned snapshot succeeds (bytes reachable) where direct control-plane access would deny. → *Oracle:* 200 / block data returned on a foreign-owned snap. **Severity: High–Critical (cross-account data).**
- *Claim (Lens A2):* `DescribeFastLaunchImages` on a shared AMI leaks owner LT id/name/version or config beyond the documented (nulled) `OwnerId`.
**Doc evidence:** hub page paragraphs on shared-AMI snapshot fallback; `win-view-fast-launch.md` (`OwnerId` not populated). **Severity-if-true:** cross-account snapshot read = Critical. **Stop condition:** confirm existence-vs-ownership with a benign metadata read before any block read.

### Area 3 — Pre-provisioned snapshot remanence via Recycle Bin
**Background:** "EC2 Fast Launch deletes pre-provisioned snapshots as soon as they're consumed by a launch ... **to prevent reuse.** However, if the deleted snapshots match a retention rule, Recycle Bin automatically retains them." A pre-provisioned snapshot is a **fully Sysprep-specialized + OOBE'd Windows image** — it may carry machine SIDs, cached credentials, DPAPI state, agent secrets, or (for a shared AMI) the owner's baked state.
**Security Concern (Lens Q / AA):** The service's own reasoning ("prevent reuse") implies these snapshots are security-sensitive. A Recycle Bin retention rule (a common, benign-looking config) silently defeats the deletion, leaving recoverable specialized images. On `disabling-failed`, the docs also admit "some pre-provisioned snapshots may still remain."
**High-level Test Scenarios:**
- *Claim:* A `snapshot` retention rule in Recycle Bin retains consumed Fast Launch snapshots; they are then restorable/attachable and expose in-image state. → *Oracle:* a consumed pre-provisioned `snap-...` is present in Recycle Bin, restored, and mounted. **Severity: Medium (single-account remanence); High if the retained snapshot is the owner's, recovered in a consumer account.**
- *Claim:* `disabling-failed` leaves orphaned snapshots with no automatic cleanup / no alert.
**Doc evidence:** hub Note (Recycle Bin); `win-fast-launch-monitor.md` (`disabling-failed`). **Severity-if-true:** Medium–High.

### Area 4 — AWS-managed IAM artifact audit (Lens R / S) — *SLR + `EC2FastLaunchFullAccess`*
**Background:** Two AWS-authored, uneditable/copy-verbatim policies define the whole feature's privilege: the SLR policy `EC2FastLaunchServiceRolePolicy` and the customer prereq `EC2FastLaunchFullAccess`.
**Security Concern:** A weak default here is **AWS's defect (Tier 2)**, not a customer footgun. The prose claims the SLR only uses "instance profiles whose name contains `ec2fastlaunch`," but the actual `PassRole` `Resource` must be audited — prior work indicated an unscoped `Resource:"*"`. `EC2FastLaunchFullAccess` was previously confirmed (v5) to grant **unrestricted `iam:PassRole`** → a holder can pass any role to an instance and self-escalate.
**High-level Test Scenarios (prove under a scoped role holding *only* the artifact; `iam:SimulatePrincipalPolicy` is the safe first oracle):**
- *Claim:* `EC2FastLaunchFullAccess`'s `iam:PassRole` `Resource` is `role/*`/`*` with only a `PassedToService` condition → holder passes an admin instance profile via a normal `RunInstances`/LT flow and harvests creds. → *Oracle:* Simulate allows `PassRole` on an unrelated admin role. **Severity: High (non-admin→admin).**
- *Claim:* The SLR policy's `iam:PassRole` `Resource` is **broader than `*ec2fastlaunch*`** (e.g. `"*"`), contradicting the UserGuide → doc-vs-artifact drift, independently reportable. → *Oracle:* `GetPolicyVersion` JSON `Resource` string vs prose.
- *Claim:* SLR `RunInstances` is `image/*` with no `aws:CalledVia`/ownership condition (over-broad).
- *Claim:* SLR pairs `iam:CreateServiceLinkedRole` / instance-profile use with unconstrained targets.
- *Claim (refined by §5.1):* The SLR policy carries only `kms:ListRetirableGrants` (not `CreateGrant`), but the customer-made grant to the SLR uses `--operations CreateGrant`, giving the SLR the ability to mint further grants → grant sprawl (feeds Area 5/H1).
**Doc evidence:** `slr-windows-fast-launch.md` (permissions list + prose scope claim); `win-start-fast-launch-prereqs.md` (`EC2FastLaunchFullAccess`); AWS Managed Policy Reference JSON. **Severity-if-true:** High privesc / Medium–High cross-workload reach; doc-vs-policy inconsistency = Low but AWS-owned. **Route:** `aws-security`, Tier 2.
> **Live policy JSON audit results are appended in §5.1 below (from the IAM-artifact subagent).**

### Area 5 — Revocation / lifecycle completeness (Lens AA)
**Background:** `DisableFastLaunch` "cleans up" snapshots; a KMS grant to the SLR is created out-of-band via `kms:create-grant`.
**Security Concern:** Grants are checked at grant time; revocation is the weak side. Does disabling Fast Launch, or un-sharing the AMI, sever *all* derived state — the consumer's ability to consume owner snapshots, and the KMS grant?
**High-level Test Scenarios:**
- *Claim:* A KMS grant the customer made to `AWSServiceRoleForEC2FastLaunch` (via `kms:create-grant --operations CreateGrant`) is **not automatically retired** when Fast Launch is disabled → orphaned grant persists and the SLR retains CMK use (and, holding the `CreateGrant` operation, could mint further grants). Note the SLR's own policy carries only `kms:ListRetirableGrants`, so retiring is the intended exit. → *Oracle:* grant still resolves after `DisableFastLaunch`; SLR can still decrypt volumes.
- *Claim:* After the owner stops sharing / disables, a consumer that still holds its own enabled state keeps consuming/launching. → *Oracle:* consumer launch still fast after owner revoke.
- *Claim:* `disabling-failed` leaves snapshots + SLR grant stranded with no cleanup path surfaced.
**Doc evidence:** `slr-windows-fast-launch.md` (create-grant), `win-fast-launch-configure.md`/`monitor.md` (disable + `disabling-failed`). **Severity-if-true:** surviving cross-account access after revoke = High; orphaned grant = Medium.

### Area 6 — Consent / griefing on shared-AMI enable + resource/quota abuse (Lens P / L)
**Background:** "If an AMI ... is shared with you, you can enable or disable faster launching on the shared AMI yourself." Enabling launches instances + creates snapshots (cost). `MaxParallelLaunches` ≥6, quota 40/region.
**Security Concern:** A consumer enabling Fast Launch on a *shared* AMI can trigger resource creation and consumes the owner's snapshots without the owner's explicit per-action consent; and there is no obvious owner-side veto. Also probe whether a caller can exceed `MaxParallelLaunches`/`TargetResourceCount` bounds server-side (cost DoS / quota bypass).
**High-level Test Scenarios:**
- *Claim:* A consumer's `EnableFastLaunch` on a shared AMI causes owner-account resource/state changes (snapshot consumption, events) the owner cannot pre-approve. → *Oracle:* owner-side events fire from a consumer action.
- *Claim:* `MaxParallelLaunches`/`TargetResourceCount` above quota is accepted → many t3 launches (self-cost-DoS, single-account = Low). **Severity:** consent gap = Low–Medium; single-account cost = Low/out-of-scope.
**Doc evidence:** hub (enable-on-shared), `win-start-fast-launch-prereqs.md` (quota). **Severity-if-true:** Low–Medium.

---

## 5.1 Live IAM-artifact audit (CONFIRMED — live AWS Managed Policy Reference, re-verified 2026-09-22; unchanged vs 2026-09-12)

Both policy JSONs were re-fetched live on 2026-09-22 and are **byte-equivalent in structure to the 2026-09-12 audit** — SLR still v7 (edited 2026-02-12), FullAccess still v5 (edited 2026-08-04). Findings are **documentation/policy-level structural observations**; no live account was touched. **Both artifacts are AWS-authored and uneditable → Tier 2, route `aws-security`.**

### `EC2FastLaunchServiceRolePolicy` (SLR policy — trusts `ec2fastlaunch.amazonaws.com`)
- ARN `arn:aws:iam::aws:policy/aws-service-role/EC2FastLaunchServiceRolePolicy`; **v7, created 2022-01-10, edited 2026-02-12T17:57Z** (post-cutoff edit). Attachable only to the SLR.
- **`AllowPassRole` = `iam:PassRole` on `"Resource":"*"`**, condition only `StringEquals iam:PassedToService ∈ [ec2.amazonaws.com, ec2.amazonaws.com.cn]`. **No `*ec2fastlaunch*` name pattern anywhere** → the SLR can pass **any** role/instance profile in the account to EC2. **CONTRADICTS** the prose in `slr-windows-fast-launch.md` ("instance profiles whose name contains `ec2fastlaunch`"). **Independently reportable doc-vs-artifact drift (Lens U/R).**
- `AllowRunInstances` on `subnet/*, network-interface/*, image/*, key-pair/*, security-group/*, launch-template/*, license-configuration:*` — **no condition**; a second `RunInstances` on `volume/*, instance/*` is tag-gated (`aws:RequestTag/CreatedBy=EC2 Fast Launch`). Stop/Terminate/CreateSnapshot/Delete*/CreateTags all `CreatedBy`-tag-gated (reasonable).
- **KMS: only `kms:ListRetirableGrants` (`Resource:"*"`, no condition). There is NO `kms:CreateGrant` in this policy** (re-confirmed 2026-09-22). The CMK-use grant is created by the *customer's* own `aws kms create-grant` call (KMS key-policy path), not by this IAM policy — corrects the earlier assumption that the SLR mints grants.
  - **⚠ Second doc-vs-artifact drift (Lens U, independently reportable):** `slr-windows-fast-launch.md` prose (line 32) claims the SLR has *"access to **create grants** and list grants that were created by EC2 Fast Launch that can be retired ... describe or use keys ... generate data keys"* — but the JSON contains **only `kms:ListRetirableGrants`** (no `CreateGrant`, no `Decrypt`/`GenerateDataKey`/`DescribeKey`/`ReEncrypt`). The KMS *usage* is authorized via the customer-made key-policy grant, not the SLR's IAM policy; the prose over-states the SLR policy's KMS scope. Low severity, AWS-owned, files alongside the `PassRole` name-scope drift below.
- No `iam:GetInstanceProfile` in the JSON (prose says "get ... instance profiles"); `iam:CreateServiceLinkedRole` is **not** here (it lives in `EC2FastLaunchFullAccess`, tightly scoped — see below). EventBridge scoped to `rule/FastLaunch*` + `events:ManagedBy=ec2fastlaunch.amazonaws.com`. CloudWatch `PutMetricData` namespace-gated to `AWS/EC2`.

### `EC2FastLaunchFullAccess` (customer prereq — attachable to users/groups/roles)
- ARN `arn:aws:iam::aws:policy/EC2FastLaunchFullAccess`; **v5, created 2024-05-13, edited 2026-08-04T20:27Z**.
- **`IAMSLRPassRole` = `iam:PassRole` on `["arn:aws:iam::*:instance-profile/*","arn:aws:iam::*:role/*"]`**, condition only `iam:PassedToService ∈ [ec2.amazonaws.com, ec2.amazonaws.com.cn]` → **pass ANY role/instance-profile in the account to EC2** (no fast-launch name restriction).
- **`EC2LaunchInstance` = `ec2:RunInstances` with NO `Condition` block at all** (Sid `EC2LaunchInstance`; Resource = `subnet/*, network-interface/*, image/*, key-pair/*, security-group/*, launch-template/*, license-configuration:*`; no `CreatedBy` tag, no `aws:CalledVia`). Its sibling Sid `EC2LaunchInstanceWithVolAndInstance` covers `volume/*, instance/*` gated by `aws:RequestTag/CreatedBy = "EC2 Fast Launch"` — **but that tag is supplied by the caller on the `RunInstances` call itself**, so it is trivially satisfiable and does **not** block the escalation (the attacker just sets the tag). Net: the `RunInstances` capability is effectively unconditioned for a privesc launch. *(Precise characterization refined 2026-09-22: not literally "RunInstances entirely unconditioned" — it is "unconditioned for the ENI/subnet/image/SG/LT/keypair resource types + self-settable-tag-gated for volume/instance"; the primitive holds either way.)*
- **⇒ Self-contained privilege escalation (Lens R, HIGH):** a principal holding **only** `EC2FastLaunchFullAccess` can `RunInstances` + `iam:PassRole` an admin instance profile (e.g. one carrying `AdministratorAccess`) — setting `CreatedBy=EC2 Fast Launch` as a request tag to satisfy the volume/instance statement — then read its credentials from IMDS. The textbook `PassRole`+`RunInstances` privesc, entirely within the AWS-authored policy, **without needing the `$Latest` laundering trick of Area 1.** `IAMSLR` (`iam:CreateServiceLinkedRole`) is tightly scoped to the single SLR ARN (`.../aws-service-role/ec2fastlaunch.amazonaws.com/AWSServiceRoleForEC2FastLaunch`) with `iam:AWSServiceName=ec2fastlaunch.amazonaws.com` → narrow, non-escalating. There is **no** `iam:CreateRole`/`AttachRolePolicy` (so no create-new-admin-role path) and **no** `kms:*` at all in this policy.

**Answers:** **(A)** SLR `PassRole Resource:"*"` — contradiction with prose CONFIRMED. **(B)** `EC2FastLaunchFullAccess` `PassRole` = `role/*`+`instance-profile/*` only `PassedToService`-gated — CONFIRMED effectively unscoped. **(C)** No CreateRole/AttachRolePolicy pairing, **but** unconstrained `PassRole` + **unconditioned** `RunInstances` in the same policy = a complete privesc primitive.

> **Severity/priority note:** the `EC2FastLaunchFullAccess` self-contained privesc (§5.1) is a *cleaner* crown jewel than Area 1's `$Latest` laundering — it needs no launch-template trick, only the AWS-managed policy the prereq page tells customers to attach. Hunter should prove it first with `iam:SimulatePrincipalPolicy` under a role holding **only** `EC2FastLaunchFullAccess` (safe, no resources touched), then, if authorized, a live `RunInstances` with a canary admin profile + IMDS creds read. Matches the prior hunter confirmation of the same policy at v5.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Non-PassRole holder passes arbitrary profile via `$Latest` LT | LT resolution at background launch | "checks your permissions ... before ... enables" (only once); "specify a numbered launch template version" recommendation |
| Consumer reads owner-account pre-provisioned snapshot | Shared-AMI snapshot fallback | Implicit: launch flow mediates consumption (unverified) |
| Recover consumed snapshot | Recycle Bin | "deletes ... to prevent reuse" (defeated by retention rule) |
| Holder of `EC2FastLaunchFullAccess` self-escalates | AWS-managed policy | Policy scoping via `PassedToService` (insufficient — no role scope) |
| SLR PassRole wider than prose | `EC2FastLaunchServiceRolePolicy` | Prose: "instance profiles whose name contains `ec2fastlaunch`" |
| Orphaned KMS grant after disable | SLR CMK grant | "delete role only after ... deleting all related resources" (grant not covered) |
| Consumer enables Fast Launch on shared AMI | Enable-on-shared | none documented (feature by design) |
| Reach `ec2fastlaunch.amazonaws.com` / AWS host | Control plane | **HARD STOP** |

---

## 7. Out-of-Scope Risk Categories
- The `ec2fastlaunch.amazonaws.com` control plane and any AWS-operated provisioning host — **hard stop / disclosure**, never actively tested.
- Single-account cost inflation from a customer over-setting `MaxParallelLaunches`/`TargetResourceCount` in their *own* account (self-DoS / footgun).
- A customer's own launch template being over-permissive, or a customer choosing `$Latest` with loose LT-modify IAM — footgun (the *design* gap of no-re-check + SLR scope is the reportable part).
- IMDS on the provisioning t3 instances *as a managed-host concept* is not out of scope here because the instances are in the customer account — but reaching IMDS of an AWS-operated host would be.
- EBS/Recycle Bin service internals; Windows Sysprep/OOBE in-guest behavior (covered by `[[project_sysprep-ami-plan]]` and `[[project_ec2-windows-instances-plan]]` — the "first-boot blank-password RDP window" lives there).
- Generic launch-template attack surface → `[[project_launch-templates-plan]]`.

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens F (translation/injection):** N/A — read all 8 Fast Launch pages; no parser/wire-protocol/translation layer. Snapshots are opaque EBS blocks.
- **Lens G (SSRF):** N/A — read hub, configure, prereqs, monitor; no field the service dereferences as a URL. (Image Builder integration URL is a doc link, not a service-fetched field.)
- **Lens J (OAuth/3P):** N/A — no third-party linking.
- **Lens K (prompt injection):** N/A — no LLM/agent in pipeline.
- **Lens M (shared-id interception):** N/A — no session/one-time-token surface.
- **Lens V (network segmentation):** partial — the auto-created SG has *no* inbound/outbound rules (hardened). Provisioning instances are in the customer VPC; no documented shared multi-tenant subnet. Mark "doc-gap — confirm the provisioning instances cannot be reached from other customer subnets during the 30-min window."
- **Lens W (attestation):** N/A.
- **Lens Y (transport/TLS/SigV):** N/A at feature level (standard EC2 API endpoints).
- **Lens O (audit-log):** low — EventBridge events are "best-effort"; `disabling-failed` may under-report stranded snapshots. Informational enabler.
- **Doc gap (scope-critical):** the docs never state *whose account IMDS/credentials* the provisioning t3 instances carry beyond "the instance profile from your launch template." Confirm the provisioning instances run under the customer's account (assumed here) before treating Area 1 credential harvest as in-scope; if they run under an AWS-operated identity → HARD STOP.
