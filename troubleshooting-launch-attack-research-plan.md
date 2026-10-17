# EC2 Instance Launch Path (troubleshooting-launch) — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html (`.md` mirror). Supporting pages fetched online and from the `/work/aws-docs` mirror: `ExamplePolicies_EC2`, `iam-policies-ec2-console`, `ebs-encryption-requirements`, `how-ebs-encryption-works`, `AMIEncryption`, `sharingamis-explicit`, `share-kms-key`, `cancel-sharing-an-AMI`, `kms/.../ebs-volume-encryption`, `grant-delete`, `configuring-IMDS-new-instances`, `configuring-instance-metadata-options`, `instance-metadata-transition-to-version-2`, `API_ModifyInstanceMetadataDefaults`, `organizations/.../orgs_manage_policies_ec2_syntax`, `finding-an-ami`, `finding-an-ami-parameter-store`, `ec2-allowed-amis`, `device_naming`, `block-device-mapping-concepts`, `instance-block-device-mapping`, `creating-an-ami-instance-store`, `ami-tools-commands`, `placement-strategies`, `ec2-resource-limits`.

**Status: documentation-derived hypotheses only. Nothing in this plan has been tested against a live AWS account.** This is the plan a hunter (e.g. `aws-vuln-hunter`) executes next; several leads below are explicitly flagged "doc-silence — confirm surface first."

The target page is a *troubleshooting* page, not an API reference. Its value is that every documented launch failure is a **boundary mechanism revealing itself at the point it rejects (or fails to reject) a request**: an IAM authorizer (`ec2:RunInstances`+`iam:PassRole`), a KMS decrypt gate for encrypted volumes (masked as `Client.InternalError`), an async "accept-then-terminate" error oracle (`StateReason`), an account-level IMDSv2 enforcement gate (`httpTokensEnforced`), AMI/device-name/snapshot resolution, and shared-capacity exhaustion. Each is enumerated below.

---

## 0. How to use this document
- Each lead is written as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (§5 is ordered highest-impact first); look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (notably the `aws:ec2-infrastructure/<instance_id>` identity-only role, any EC2/EBS fleet grant principal, or a control-plane host), **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not escalate.
- Dummy/canary data only. Confirm *existence* of a boundary break, never exploit beyond it (one cross-account read = PoC; do not enumerate further). Tear down every resource created.
- Error oracles (`StateReason`, `DescribeInstances`, decoded authorization messages) are read-only — safe to probe. Cross-account/KMS/capacity leads require two authorized test accounts with synthetic data.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Launch an instance with a role the caller cannot `PassRole`** — or reach an instance role's live credentials via a non-`PassRole` write path — proving the launch-path PassRole gate is incomplete.
2. **Read or boot from a snapshot/AMI/volume owned by another account** by naming its ID in a block-device-mapping override or AMI name/SSM-alias resolution, proving device/AMI resolution checks existence (or format) but not ownership.
3. **Cause another tenant's data to decrypt under, or be re-encrypted under, the wrong KMS key** — or demonstrate the identity-only-role grant is replayable (no encryption-context binding) — on the encrypted-launch path.
4. **Launch an IMDSv1-enabled instance in an account/region where IMDSv2 is "enforced,"** or disable the enforcement from a principal the guarantee implies should not be able to, proving the account-level control is bypassable or reversible.
5. **Boot a victim's still-registered S3-backed AMI from an attacker-repopulated bundle bucket** (bucket-monopoly on the orphaned `ImageLocation`), proving launch-time part-fetch trusts a global, re-claimable S3 name.
6. **Exhaust shared AZ / cluster-placement-group capacity** to deny other tenants' launches (noisy-neighbor), distinct from the per-account quota wall.
7. Use `StateReason` / decoded-authorization-message / differential launch errors as a **cross-tenant existence/ configuration oracle** without any other access.

---

## 2. Components, Assets, and Design

**Customer-facing interface:** the `RunInstances` control-plane API (also reached via `StartInstances` for stopped instances, launch templates, Spot, and Auto Scaling groups — all documented as funneling through the same `RunInstances` codepath). SigV4 IAM identity. Console "launch wizard" is a thin layer over the same API.

**Processes / fleets behind it (named in docs):**
- The **RunInstances authorizer / orchestrator** (control plane) — performs the synchronous IAM check (`ec2:RunInstances`, `iam:PassRole`, resource-level + condition-key checks) and the **account-level IMDSv2 enforcement check** (a *second-pass* check applied *after* instance/account/AMI precedence resolution).
- The **launch workflow** (async) — after the API returns and the instance enters `pending`, this stage attaches volumes, fetches AMI parts, and issues KMS grants. Failures here surface only via `StateReason` (accept-then-terminate model).
- **EC2/EBS–KMS integration** — a per-instance **"identity-only role"** `arn:<partition>:iam::<account>:role/aws:ec2-infrastructure/<instance_id>`; AWS KMS issues a `CreateGrant` to its assumed-role session so EBS can `GenerateDataKeyWithoutPlaintext`/`Decrypt` the volume data key. The data key then lives in **Nitro hardware** for the life of the attachment. **This role is AWS service-plane: not enumerable or assumable by the account owner → HARD STOP if evidence touches it.**
- **S3 (for S3-backed / instance-store AMIs)** — launch workflow fetches `image.manifest.xml` + `image.part.xx` live from the bucket named in the AMI's `ImageLocation` at every launch; bundle is unencrypted at rest, gated only by bucket/object ACLs the AMI owner set.
- **SSM Parameter Store** — `resolve:ssm:` AMI aliases resolved at launch (format-validated, not ownership-validated).

**Accounts / trust zones:** customer account (caller) ↔ **AWS EC2/EBS service plane** (identity-only role, fleet grants, shared physical capacity, control plane) ↔ **other customer accounts** (cross-account shared AMIs/snapshots/KMS keys; shared AZ capacity; global S3 bucket namespace). AWS Organizations management/delegated-admin account ↔ member account (declarative policy for metadata defaults).

**Resource identifiers & shapes:** `i-...` instance IDs, `ami-...` (plus name-pattern & `ImageLocation` `bucket/path/manifest`), `snap-...` snapshot IDs (usable in BDM override), `subnet-...`, KMS key IDs/ARNs, role ARNs (`iam:PassRole` target). S3 bucket names = **global first-come namespace**.

**Where untrusted data enters & transforms:** `RunInstances` request params (BDM overrides, AMI id/name, `httpTokens`, instance-profile/role ARN, user-data) → authorizer → async launch workflow → KMS/S3/SSM dereferences. User-data (e.g. the documented Windows registry script) is executed on the guest at boot.

```
caller (SigV4 IAM)
   │  RunInstances / StartInstances / LaunchTemplate / Spot / ASG
   ▼
[Control-plane authorizer]  ── ec2:RunInstances + iam:PassRole + condition keys
   │                         ── IMDSv2 enforcement check (2nd pass, after precedence)
   │  (accept → pending)                                   ╲ reject → UnsupportedOperation / UnauthorizedOperation
   ▼
[Async launch workflow] ───────────────┬──────────────┬───────────────┐
   │ attach EBS                         │ fetch AMI    │ KMS grant     │ resolve AMI
   ▼                                    ▼              ▼               ▼
 EBS volume (BDM override: snap-ID)   S3 bundle      identity-only    SSM resolve:ssm
   │                                   image.part.xx  role grant       / name filter
   ▼ fail → terminated                 (unencrypted,  (CreateGrant,    (format-checked,
 StateReason {Message: Client.* ,       bucket ACL)    Nitro-resident,  not owner-pinned)
             Code: Server.InternalError}               ← SERVICE PLANE)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (observation that proves it broke) |
|---|---|---|---|
| Caller IAM principal | An IAM role it lacks `PassRole` for | `RunInstances` / `AssociateIamInstanceProfile` / `ModifyInstanceAttribute(userData)` / launch template | An instance running with, or reaching, a role's live credentials the caller could not `PassRole` directly |
| Caller account | Another account's snapshot/volume | BDM override naming `snap-...` at launch | A booted/attached volume whose data belongs to a snapshot the caller does not own |
| Caller account | Another account's / attacker's AMI | name-filter or `resolve:ssm` resolution without owner pinning | `RunInstances` boots an AMI published by an untrusted owner because only name/format matched |
| Caller account | Another account's KMS CMK / wrong key | encrypted-launch grant; shared-AMI default-key substitution | Data decrypts/re-encrypts under a key the caller should not use, or a grant usable beyond its intended resource |
| Caller / any account | **AWS EC2/EBS service plane** (`aws:ec2-infrastructure/*` role, fleet grants, control plane) | identity-only-role grant; async launch workflow | **Any credential/ARN/grant belonging to AWS's own fleet → HARD STOP, preserve, disclose** |
| Member account principal (admin-equiv) | Account-wide IMDSv2 enforcement guarantee | `ModifyInstanceMetadataDefaults HttpTokensEnforced=disabled`; per-region gap | IMDSv1 instance launches after enforcement was "on," or enforcement reversed by a principal the guarantee implies cannot |
| Attacker (global S3 namespace) | Victim's still-registered S3-backed AMI | re-claim orphaned `ImageLocation` bucket, repopulate parts | Victim's future launch boots attacker-supplied root volume contents |
| One tenant | Shared AZ / cluster-placement-group capacity | bulk `RunInstances` | Other tenants receive `InsufficientInstanceCapacity` attributable to the first tenant's consumption |
| Any caller (read-only) | Cross-tenant existence/config | `StateReason` / decoded authz message / differential errors | A distinct error/latency reveals existence or configuration of a resource the caller cannot otherwise read |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `RunInstances` | POST (SigV4) | Yes | External | Launch instance(s); accepts AMI id/name, BDM overrides (`snap-...`), role/instance-profile, `httpTokens`, user-data, subnet | Yes | Any principal w/ `ec2:RunInstances` (+ `iam:PassRole`, +resource perms) | Prime cross-tenant/privesc target. Example policies ship `Resource:"*"` unconditioned |
| `StartInstances` | POST | Yes | External | Restart stopped instance (re-runs launch workflow incl. KMS/limit checks) | Yes | Principal w/ `ec2:StartInstances` | Action-family twin of RunInstances for the KMS/limit/metadata gates (Lens X) |
| `ModifyInstanceAttribute` | POST | Yes | External | Edit instance attrs incl. **userData** | Yes | Principal w/ the action | Reaches instance role indirectly (Lens B variant) — no `iam:PassRole` called |
| `AssociateIamInstanceProfile` | POST | Yes | External | Attach instance profile post-launch | Yes | Principal w/ action + `iam:PassRole` | Second PassRole-sensitive path; confirm parity with RunInstances |
| `ModifyInstanceMetadataDefaults` | POST | Yes | External | Set/clear account+region IMDS defaults & `HttpTokensEnforced` | Yes | **Any principal w/ `ec2:ModifyInstanceMetadataDefaults`** (no special gate by default) | Can set `HttpTokensEnforced=disabled` to re-enable IMDSv1 account-wide |
| `GetInstanceMetadataDefaults` | GET | No | External | Read account defaults + `ManagedBy` (account vs declarative-policy) | Yes | Principal w/ action | Recon: tells attacker whether local Modify calls will be honored |
| `DescribeInstances` | GET | No | External | Read `StateReason` (`Message`/`Code`) | Yes | Principal w/ action | The async error oracle (Lens A) |
| `DescribeImages` | GET | No | External | AMI lookup; **default returns all public + shared + owned** AMIs | Yes | Any principal | whoAMI precondition when `--owners` omitted |
| `register-image` (`--image-location`) | POST | Yes | External | Register S3-backed AMI pointing at `bucket/path/image.manifest.xml` | Yes | Principal w/ action | `ImageLocation` is a global S3 key (bucket-monopoly surface) |
| `modify-image-attribute` / `cancel-image-launch-permission` | POST | Yes | External | Share / self-unshare AMI launch permission | Yes | AMI owner / shared-with account | Unshare does **not** touch the CMK key policy (revocation gap, Lens AA) |
| STS `DecodeAuthorizationMessage` | POST | No | External | Decode the authz-failure blob from a launch denial | Yes | Caller | Reveals which perms/resources were evaluated — info-disclosure/enum oracle |

Doc-flagged focus: the troubleshooting page itself plants leads — "`Client.InternalError` → KMS permissions," "decode the authorization failure message," and "`httpTokensEnforced` enforced via account settings **or an AWS Organization declarative policy**." Keep those pointers.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — PassRole completeness on the launch path (Lens B, X; variant: non-PassRole paths to a role's creds)
**Background.** The page states a launch needs `ec2:RunInstances` **and** `iam:PassRole` "with the resource matching the role ARN." But `RunInstances` can attach an instance profile whose role yields live credentials inside the instance.
**Security Concern.** The PassRole check may be enforced only at `RunInstances` and not on sibling paths that bind or mutate the role/credentials after the fact — `AssociateIamInstanceProfile`, `ModifyInstanceAttribute(userData)` (confirmed exemplar in prior EC2 hunts), launch-template `$Latest`/`$Default` late-binding, and `StartInstances` of a pre-configured stopped instance.
**High-level Test Scenarios.**
- **Claim:** A principal with `ec2:RunInstances`+`ec2:ModifyInstanceAttribute` but *without* `iam:PassRole` on role R can obtain R's credentials by launching a bare instance then setting user-data/instance-profile that reaches R. → **Oracle:** instance metadata serves R's STS creds. → Sev: **High** (privesc).
- **Claim:** `AssociateIamInstanceProfile` enforces PassRole differently (or not) vs RunInstances. → **Oracle:** association succeeds for a role the caller cannot pass at launch.
- **Claim:** A launch template created by a higher-privileged principal, launched via `$Latest`, passes a role the launcher lacks. → **Oracle:** instance runs with the template's role.
**Doc evidence:** troubleshooting-launch "Insufficient permissions" (`ec2:RunInstances`,`iam:PassRole`); `ExamplePolicies_EC2` RunInstances section (which notably contains **no** `iam:PassRole` example and no instance-profile condition). **Severity-if-true:** High. **Stop:** one role's creds retrieved = PoC.

### Area 2 — AWS-authored "launch instances" example policies ship unconditioned (Lens R, S)
**Background.** `ExamplePolicies_EC2` is a page customers copy verbatim. Its "Describe, launch, stop, start, and terminate all instances" example grants `ec2:RunInstances`,`ec2:StartInstances`,`ec2:TerminateInstances`,`ec2:StopInstances` with **`Resource:"*"` and zero condition keys**; the dedicated RunInstances section demonstrates subnet/instance-type/tag/AMI-owner/launch-template scoping but **never shows `iam:PassRole` scoping at all**.
**Security Concern.** A customer following the simplest shipped example gets an unconditioned launch/terminate grant with no PassRole guardrail — AWS-authored, copy-verbatim artifact (in-scope Tier-2 per the skill's carve-out, *not* a customer footgun).
**High-level Test Scenarios.**
- **Claim:** Holding only the "launch…all instances" example policy, a principal can `TerminateInstances` on any instance in the account (no tag/ownership condition) and pass any role already permitted elsewhere. → **Oracle:** `iam:SimulatePrincipalPolicy` with exactly that policy returns `allowed` for `TerminateInstances` on an arbitrary `instance/*`; escalate to a scoped-role live call on a canary instance only. → Sev: **Medium–High**.
- **Claim:** The example's omission of a PassRole statement, combined with Area 1, means the doc's own "to launch, you need PassRole" guidance is unsatisfiable from the example → pushes customers to attach a broad `iam:PassRole":"*"`. → **Oracle:** doc-vs-doc contradiction (informational), plus simulate a `PassRole":"*"` escalation.
**Doc evidence:** `ExamplePolicies_EC2#iam-example-instances-all` (verbatim `Resource:"*"`), `#iam-example-runinstances` (no PassRole). **Severity-if-true:** Medium–High (High if it enables non-admin→admin via unscoped PassRole). **Stop:** simulate first; one scoped-role confirmation.

### Area 3 — IMDSv2 account-level enforcement bypass & reversal (Lens U, E, X, A)
**Background.** The page's IMDSv1-launch-fails section: `httpTokensEnforced=enabled` is documented as a hard launch gate "regardless of how the instance or AMI is configured," enforced via account settings **or** an Organizations declarative policy, reversible via `ModifyInstanceMetadataDefaults`.
**Security Concern.** The guarantee has several documented seams: (a) it is **per-region** when set directly (a region where it was never set allows IMDSv1); (b) it is **reversible by any principal holding `ec2:ModifyInstanceMetadataDefaults`** — no org-admin-only gate by default (AWS explicitly tells customers to *add* a restricting IAM policy); (c) it is **forward-only** (instances already IMDSv1-enabled stay so); (d) ASG/Spot are asserted to share the RunInstances path but not explicitly carved out — a doc gap.
**High-level Test Scenarios.**
- **Claim:** With enforcement `enabled` in region A, a launch in region B (never configured) succeeds with `httpTokens=optional`. → **Oracle:** IMDSv1 reachable on the region-B instance. → Sev: **Medium–High** (guarantee bypass).
- **Claim:** A non-security, admin-equivalent principal calls `ModifyInstanceMetadataDefaults HttpTokensEnforced=disabled` and immediately launches an IMDSv1 instance. → **Oracle:** `GetInstanceMetadataDefaults` shows `ManagedBy: account`, Modify succeeds, launch succeeds. → Sev: **Medium–High**.
- **Claim (doc gap):** An ASG/Spot/launch-template path or a specific instance type slips `httpTokens=optional` past enforcement. → **Oracle:** launched instance exposes IMDSv1 despite `enabled`.
- **Claim (fail-open, doc-silence):** When the account-setting read fails/region not yet propagated, launch defaults to allowing IMDSv1. → **doc-gap — confirm surface first.**
**Doc evidence:** troubleshooting-launch IMDSv1 section; `configuring-IMDS-new-instances` ("regardless of how the instance or AMI is configured"; per-region; "prevent access to the ModifyInstanceMetadataDefaults API"); `configuring-instance-metadata-options` precedence (enforcement is a 2nd pass). **Severity-if-true:** Medium–High. **Stop:** one IMDSv1-reachable instance under "enforced" = PoC.

### Area 4 — Block-device-mapping snapshot override: ownership vs existence (Lens A/IDOR, X)
**Background.** Launch accepts a BDM override that maps an EBS volume from a `snap-...` ID; the override "overwrites or merges with the AMI's mapping." Device-name validation is purely structural (reserved-for-root, in-use-by-AMI, duplicate, OS-format). The BDM-snapshot parameter doc states only one restriction — "can't specify an archived snapshot" — and does **not** mention an ownership/authz check.
**Security Concern.** If the launch workflow validates the snapshot *exists / is not archived* but not that the caller *owns or is granted* it, a caller could boot/attach another account's snapshot by ID (IDOR). The "Instance terminates immediately → corrupted snapshot / KMS permission" errors are the differential oracle for how far resolution got.
**High-level Test Scenarios.**
- **Claim:** `RunInstances` with a BDM mapping a foreign-account `snap-...` (unshared) attaches/boots its data. → **Oracle:** readable volume content from the foreign snapshot, or a `StateReason` that distinguishes "no access" (expected) from "corrupted/decrypt" (leak). → Sev: **High–Critical** (cross-account data).
- **Claim:** Error/latency differs for a *nonexistent* vs *existing-but-foreign* snapshot ID → existence-enumeration oracle. → **Oracle:** distinct `StateReason`/API error. → Sev: Low–Medium.
- **Claim:** Device-name collision (`NoDevice` suppression, root-device reuse) causes the AMI's intended root to be replaced by a caller-supplied mapping. → **Oracle:** booted root is the attacker's volume.
**Doc evidence:** troubleshooting-launch "Invalid device name" + "corrupted snapshot"; `device_naming`; `block-device-mapping-concepts` ("can't specify the ID of an archived snapshot" — only stated restriction); `instance-block-device-mapping` (override merges/overwrites). **Severity-if-true:** High–Critical. **Stop:** one foreign snapshot's bytes read = PoC; do not enumerate.

### Area 5 — AMI resolution without owner pinning (whoAMI) (Lens EE, U)
**Background.** `DescribeImages` "by default returns all AMIs that are public, that you own, and that are shared with you." `resolve:ssm:` validates the resolved value is a syntactically valid AMI ID, not its owner. The "Allowed AMIs" control that would pin providers is **opt-in and disabled by default**.
**Security Concern.** An automation/launch that selects an AMI by name pattern without `--owners`, or via an SSM alias an attacker can influence, can boot an attacker-published public AMI (whoAMI) — code execution in the victim account at boot.
**High-level Test Scenarios.**
- **Claim:** A name-filter launch (`Name=amzn2-ami-hvm-*`) with no `--owners` selects a public AMI from an arbitrary account. → **Oracle:** `DescribeImages` returns a non-Amazon-owned AMI matching the pattern; a launch would boot it. → Sev: **High–Critical** (boot attacker code).
- **Claim:** With "Allowed AMIs" disabled (default), no owner restriction is applied to discovery or launch. → **Oracle:** `ec2-allowed-amis` state = disabled + successful foreign-AMI launch.
- **Claim:** `resolve:ssm` pointed at a parameter resolving to a foreign AMI launches it with no owner re-check. → **Oracle:** instance boots the foreign AMI.
**Doc evidence:** `finding-an-ami` (default returns all public); `finding-an-ami-parameter-store` (format-validated); `ec2-allowed-amis` (default-off). **Severity-if-true:** High–Critical. **Stop:** demonstrating selection of a foreign/attacker AMI = PoC (do not weaponize boot payload).

### Area 6 — Encrypted-launch KMS gate: fail-open window, key substitution, grant binding (Lens H, A, AA, T)
**Background.** EC2 gets decrypt capability via a per-instance **identity-only role** (`aws:ec2-infrastructure/<instance_id>`) that KMS grants `CreateGrant`/`Decrypt`; the data key then lives in Nitro for the attachment lifetime. KMS failures surface late as `StateReason` `Client.InternalError`.
**Security Concern.** Several documented seams: (a) **fail-open** — disabling/deleting the CMK does not evict a currently-attached volume (data key stays in Nitro) and is only re-checked at next attach; (b) **key substitution** — a shared encrypted AMI launched with no encryption params is silently re-encrypted under the **recipient's default key**; (c) **revocation gap** — `cancel-image-launch-permission` does not strip the recipient from the CMK key policy; (d) **no encryption-context binding** documented on the EBS↔KMS grant (doc-silence) → possible grant replay across resources; (e) grant propagation is eventually-consistent (minutes), widening the fail-open window.
**High-level Test Scenarios.**
- **Claim (service-plane — HARD STOP territory):** The `aws:ec2-infrastructure/<instance_id>` grant can be observed, enumerated, or replayed against a CMK for a resource other than the one it was issued for. → **Oracle:** a `Decrypt`/grant usable beyond its intended volume/snapshot. → **If this touches the fleet role, STOP and disclose.** Sev: **Critical**.
- **Claim:** After `cancel-image-launch-permission`, the recipient account still holds a live `Encrypt/Decrypt/CreateGrant` path via the un-revoked CMK key-policy statement. → **Oracle:** recipient still performs a KMS op on the owner's CMK post-unshare. → Sev: **High** (surviving cross-account access). *(doc-inference — confirm.)*
- **Claim:** A disabled/scheduled-deletion CMK still serves I/O on an attached volume (confirmed by doc) — verify the window and whether a re-attach race re-grants. → **Oracle:** read succeeds post-disable until detach.
- **Claim (doc-silence):** No encryption-context ties the grant to a specific volume/snapshot. → **doc-gap — confirm via CreateGrant/GenerateDataKeyWithoutPlaintext behavior first.**
**Doc evidence:** `ebs-encryption-requirements` (identity-only role ARNs); `how-ebs-encryption-works` ("unusable KMS keys"; CreateGrant sequence); `AMIEncryption` (default-key substitution for shared AMIs); `sharingamis-explicit`+`share-kms-key` (two separate controls); `cancel-sharing-an-AMI` (no key-policy touch); `grant-delete` (eventual consistency); `kms/.../ebs-volume-encryption` (no EncryptionContext mentioned). **Severity-if-true:** High–Critical. **Stop:** HARD STOP on any fleet-role/service-plane evidence.

### Area 7 — StateReason / decoded-authz / differential-error oracle (Lens A, O)
**Background.** `StateReason` returns `{"Message":"Client.VolumeLimitExceeded: Volume limit exceeded","Code":"Server.InternalError"}` — a **Client-cause reported under a `Server.InternalError` Code**. The page maps specific `Message` substrings to each of four root causes (volume limit, KMS permission, corrupted snapshot, missing S3 part). STS `DecodeAuthorizationMessage` reveals evaluated perms/resources.
**Security Concern.** The `Code`/`Message` mismatch and the enumerated cause→message mapping let a read-only caller fingerprint *why* a launch failed (KMS-permission vs corrupted-snapshot vs missing-part vs quota) — a configuration/existence oracle usable cross-tenant when combined with Areas 4–6 (e.g., does a foreign snapshot ID yield "no access" or "corrupted"?). Decoded authz messages may over-disclose resource ARNs.
**High-level Test Scenarios.**
- **Claim:** The four documented `StateReason.Message` substrings reliably distinguish root cause regardless of `Code`. → **Oracle:** reproduce each cause with canaries; confirm the mapping. → Sev: Low–Medium (enabler).
- **Claim:** For a foreign/nonexistent snapshot or KMS key, `StateReason`/API error differs enough to confirm existence. → **Oracle:** differential response. → Sev: Low–Medium (becomes High as an enumeration enabler for Areas 4/6).
- **Claim:** `DecodeAuthorizationMessage` discloses role/resource ARNs beyond what the caller can read. → **Oracle:** decoded blob names a resource the caller cannot `Describe`.
**Doc evidence:** troubleshooting-launch "Instance terminates immediately" (verbatim JSON + cause→message list), "Insufficient permissions" (decode link). **Severity-if-true:** Low–Medium standalone; raises severity of Areas 4–6. **Stop:** read-only; safe to fully characterize.

### Area 8 — S3-backed AMI bundle: bucket-monopoly & integrity (Lens EE, Q, U)
**Background.** A "missing part (`image.part.xx`)" is a documented launch-terminate cause. The bundle (`image.manifest.xml`+parts) is fetched **live at every launch** from the bucket in the AMI's `ImageLocation`, is **unencrypted at rest**, gated only by bucket/object ACLs, and the tooling creates the bucket "if the bucket name is available" and can orphan it on delete.
**Security Concern.** `ImageLocation` is a fixed, discoverable global S3 key. If the original bucket is deleted (cleanup/account closure) an attacker can re-register the same global bucket name and repopulate the manifest+parts; a victim's still-registered AMI then boots attacker-controlled root contents. No doc states EC2 re-verifies bundle digests against the registered AMI at launch.
**High-level Test Scenarios.**
- **Claim:** A still-registered S3-backed AMI whose bucket was deleted can be hijacked by re-claiming the bucket name and uploading a tampered manifest/parts. → **Oracle:** a launch from the AMI boots the attacker's root volume (or fails integrity if a check exists). → Sev: **High–Critical**.
- **Claim:** Launch-time part fetch performs no integrity check vs the registered AMI. → **Oracle:** modified part accepted at boot. *(doc-silence — confirm.)*
**Doc evidence:** troubleshooting-launch (missing-part cause); `creating-an-ami-instance-store` (live fetch, unencrypted, ACL-gated); `ami-tools-commands` (`--bucket` created if available; `ec2-delete-bundle --clear` orphans bucket). **Severity-if-true:** High–Critical. **Stop:** demonstrate control of the bundle source = PoC; do not plant a live boot payload against a third party.

### Area 9 — Shared-capacity noisy-neighbor DoS (Lens L, V)
**Background.** `InsufficientInstanceCapacity` is explicitly a shared, time-varying, per-AZ/instance-type pool ("capacity can shift frequently"); cluster placement groups contend for a finite nearby hardware segment. Per-account quotas (`InstanceLimitExceeded`, e.g. 5 public AMIs/region) are a *separate* wall from physical capacity.
**Security Concern.** One tenant's bulk launches can transiently exhaust shared AZ / cluster-placement-group capacity, denying other tenants — the quota wall does not bound this.
**High-level Test Scenarios.**
- **Claim:** Concentrated launches of a scarce instance type in one AZ/cluster placement group raise `InsufficientInstanceCapacity` for co-located tenants. → **Oracle:** cross-tenant launch failures correlated with the first tenant's consumption. → Sev: **High** if cross-tenant; else out-of-scope self-DoS.
**Doc evidence:** troubleshooting-launch capacity section; `placement-strategies` (cluster capacity errors); `ec2-resource-limits`. **Severity-if-true:** High (cross-tenant) / Low (self). **Stop:** do not actually degrade a shared production AZ — reason from quota/placement docs and a bounded authorized test only.

### Area 10 — User-data as a boot-time execution vector (Lens Q, K)
**Background.** The Windows high-CPU tip hands the user a registry-editing script to paste into **user-data**, which runs on the guest at launch.
**Security Concern.** Lower priority (the launcher steers their own instance), but relevant where a *higher-privileged* principal supplies a launch template / AMI with user-data, or where user-data is sourced from an attacker-influenced field — chains into Area 1 (reaching the instance role) and Area 5 (attacker AMI with malicious user-data defaults).
**High-level Test Scenarios.**
- **Claim:** A launch-template default user-data authored by another principal executes with the instance's role (chains Area 1). → **Oracle:** template-supplied user-data runs and reaches role creds. → Sev: inherits Area 1 (High).
**Doc evidence:** troubleshooting-launch "High CPU…" (user-data script); `user-data.md`. **Severity-if-true:** High (as a chain). **Stop:** per Area 1.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Launch/reach a role without PassRole | RunInstances authorizer / ModifyInstanceAttribute / AssociateIamInstanceProfile | "`iam:PassRole` with the resource matching the role ARN" (page) — test it covers all paths |
| Copy-verbatim example policy over-grants | `ExamplePolicies_EC2` artifact | `Resource:"*"` with no condition keys / no PassRole statement |
| Boot foreign/attacker AMI | DescribeImages / resolve:ssm / Allowed AMIs | owner pinning (`--owners`, `ec2:Owner`), Allowed AMIs (opt-in, default off) |
| Attach foreign snapshot via BDM | async launch workflow | only "not archived" stated; ownership check unverified |
| Wrong-key decrypt / grant replay / fail-open | EC2↔KMS identity-only role | grant scoped to key+grantee; "unusable key" re-check only at attach |
| Surviving cross-account KMS access post-unshare | AMI share + CMK key policy | two separate controls; `cancel-image-launch-permission` ≠ key-policy edit |
| IMDSv1 under "enforced" / enforcement reversal | control-plane enforcement check | "regardless of instance/AMI config"; per-region; add IAM policy to prevent reversal |
| S3-backed AMI bundle hijack | launch-time S3 part fetch | bundle unencrypted, ACL-gated, bucket re-claimable; integrity re-check undocumented |
| Cross-tenant capacity exhaustion | shared AZ / cluster placement group | per-account quota (separate wall); "capacity can shift frequently" |
| Error-oracle cross-tenant enumeration | DescribeInstances StateReason / DecodeAuthorizationMessage | `Code`/`Message` mismatch; cause→message mapping |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **The AWS service plane is a hard stop.** The `aws:ec2-infrastructure/<instance_id>` identity-only role, EBS/EC2 fleet grants, Nitro, and control-plane hosts belong to AWS. Observing them = disclosure, not exploitation. Do not attempt to assume/enumerate the identity-only role as an objective.
- **IMDS on fully-managed hosts** and the Nitro data-key residency behavior itself (documented design) — out of scope except as the Area 3/6 *bypass* leads describe.
- **Single-tenant self-DoS** (hitting your own instance/volume quota) — out of scope; only *cross-tenant* capacity exhaustion is in scope, and only under a bounded authorized test.
- **A user steering their own instance via user-data** — out of scope; only cross-principal/template-sourced user-data (Area 10 chain) is in scope.
- **Customer-authored IAM policy footguns** — out of scope. The in-scope IAM artifact (Area 2) is in scope *only because it is AWS-authored and copy-verbatim*.
- **Shared physical capacity / Spot interruption as a product behavior** — out of scope beyond the specific noisy-neighbor cross-tenant claim.
- **DNS rebinding / private-only endpoints**, port scanning, and anything below the HTTP/API layer.

## 8. Null hypotheses / doc gaps
- **No SSRF field on this surface (Lens G): N/A.** Checked troubleshooting-launch, `block-device-mapping-concepts`, `instance-block-device-mapping`, `finding-an-ami*` — the launch path dereferences AMI/snapshot IDs, SSM aliases, and S3 bundle keys (covered by Areas 4/5/8), but no customer-supplied URL the service fetches/previews server-side. Re-open if a launch field taking a URL appears.
- **No OAuth/3P linking, no multi-tenant web session, no JWT/token validation on this page (Lens J/M/FF): N/A** — launch is pure SigV4 IAM; no page here exposes a token/session surface.
- **Encryption-context binding on EBS↔KMS grants (Lens H):** doc-silence. The cryptographic-details page describes grants scoped to key+grantee with no `EncryptionContext`. **doc-gap — confirm the live grant/`GenerateDataKeyWithoutPlaintext` behavior before treating replay as fact.**
- **Unshare→KMS-key-policy auto-revocation (Lens AA):** inferred from two separate documented control surfaces with no cross-reference; **confirm live** before relying on the surviving-access claim.
- **ASG/Spot/launch-template IMDSv2-enforcement coverage (Lens X/U):** docs assert these funnel through `RunInstances` but do not explicitly carve them out of enforcement. **doc-gap — confirm each path honors `httpTokensEnforced`.**
- **Fail-open on account-setting read failure / region propagation (Lens U):** not documented either way. **doc-gap.**
- **Launch-time integrity re-check of S3-backed AMI bundle (Lens EE/Q):** digests are generated at bundle time, but no page states EC2 verifies them at launch. **doc-gap — confirm.**

---

### Priority ranking for the hunter
1. **Area 4** (cross-account snapshot via BDM) and **Area 5** (whoAMI) — cross-account data / attacker-code-boot, cheapest to probe read-only first.
2. **Area 1** (PassRole completeness) + **Area 10 chain** — privesc to instance role creds.
3. **Area 6** (KMS fail-open / revocation / grant binding) — High–Critical but HARD-STOP sensitive; characterize read-only first.
4. **Area 3** (IMDSv2 bypass/reversal) and **Area 8** (S3-backed AMI hijack).
5. **Area 2** (example-policy audit — simulate-only), **Area 7** (error oracle — read-only enabler), **Area 9** (capacity DoS — bounded test).
