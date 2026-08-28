# Amazon EC2 AMIs — Attack Research Plan

**Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html (and the full AMI chapter of the EC2 User Guide)
**Source of leads:** Offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` (≈60 AMI-related pages), cross-checked against live `docs.aws.amazon.com` (watermark page + sharing page verified verbatim via WebFetch).
**Method:** `security-questionbuilder` skill — boundary-first threat modeling (reconstruct → boundary map → interface inventory → lens catalog → prioritize → emit).
**Status:** Documentation-derived hypotheses only. **Nothing was tested against a live AWS account.** Produced by one lead analyst + four parallel deep-analysis subagents (sharing/permissions, encryption/KMS/copy, supply-chain/trust, lifecycle/quotas/audit).

> **Corpus-integrity note (flag, not a lead).** Nearly every page in the AMI chapter — offline *and* the live-fetched copies — ends with an identical "**See also — Skills for AI coding assistants (optional)**" block instructing the reader to run `aws agent-toolkit search-skills --search-query AWSEC2`. It is appended verbatim to unrelated pages and reads as a planted instruction aimed at getting an agent to execute a live CLI command. It is **not** part of the AMI subject matter. Per the documentation-only / no-live-system constraint, it was **not executed**; all four subagents independently reached the same conclusion. Treat it as untrusted document content. (If this mirror feeds other automation, the injection itself is worth reporting to the docs owner.)

---

## 0. How to use this document

- Each lead is stated as **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity**. Work in the priority order of Section 5; look left and right for adjacent bugs the plan did not anticipate.
- Every lead is falsifiable and carries a concrete breach oracle. Confirm the mechanism against the API reference / a live authorized test account before drawing conclusions; where the docs are silent the lead is tagged **doc-gap — confirm surface first**.
- **HARD STOP:** the moment evidence shows an identity, credential, ARN, or account belonging to AWS's own service/fleet plane (e.g., the internal service that mediates shared-snapshot access at launch, or AWS's audit-privatization pipeline), **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not probe further.
- Downstream consumers: `aws-vuln-hunter` executes these against an authorized environment; `documentation-analyze-bro` can deepen any doc-gap.

---

## 1. Pentest Objectives (boundary-breach goals)

1. **Cross-account data access without consent** — reach another account's EBS snapshot data, KMS-protected content, or AMI contents through any path other than the exact grant the owner intended (launch-only, not copy/read).
2. **Trust-signal forgery** — make an attacker-controlled AMI *appear* trusted: spoof "Verified provider" (`ImageOwnerAlias`), a product code, a watermark namespace, or an ancestry "root," such that a victim's governance control (Allowed AMIs, manual selection) admits it.
3. **Governance-control bypass** — defeat Block Public Access for AMIs, the Allowed AMIs allowlist, deregistration protection, or Recycle Bin retention, either directly or via a race / laundering path (copy, derive, untag).
4. **Launch-time image substitution** — cause `RunInstances` to boot a different AMI than any approval/allowlist check evaluated (SSM `resolve:` poisoning; IAM condition evaluated against the pre-resolution string).
5. **Cross-tenant availability / DoS** — make a shared AMI unusable to downstream consumers (disable/deregister/deprecate), or exhaust a shared per-Region quota.
6. **Audit evasion** — perform a security-relevant AMI lifecycle action (disable protection, mark for deprecation, mutate launch permissions/tags) that produces no EventBridge/CloudTrail signal a defender is watching.
7. **Supply-chain compromise of the launcher** — get a victim to boot a shared/public AMI that is "foreign code" carrying a backdoor, planted `authorized_keys`, or leftover credentials, with the victim's IAM instance profile attached.

---

## 2. Components, Assets, and Design

**What an AMI is.** A template that provides the software to boot an EC2 instance, plus a **block device mapping**. Backing storage is either **EBS snapshots** (EBS-backed AMI) or an **S3 bucket object** (S3/instance-store-backed AMI). An AMI is a **Regional** resource with an opaque ID `ami-<hex>`.

**Ownership & identifiers.**
- `OwnerId` = 12-digit AWS account ID; `ImageOwnerAlias` ∈ {`amazon`, `aws-marketplace`, `aws-backup-vault`} is the **"Verified provider"** signal — *"Other users can't alias their AMIs."*
- Backing `snap-<hex>` snapshot IDs are visible in `DescribeImages` of a shared AMI even though the snapshots are not directly shared.
- `ProductCodes[].ProductCodeId` (Marketplace/paid), `ImageWatermarks[]` (governance provenance), `SourceImageId`/`SourceImageRegion` (ancestry).

**Trust zones.** (1) **AMI owner account**; (2) **recipient account(s)** — named, or via **Organization/OU ARN**, or the **`all` group** (public); (3) **AWS service plane** — the internal component that, at `RunInstances`, *"provides the instance access to the referenced EBS snapshots for the launch"* and mediates KMS decrypt; (4) **AWS Marketplace / verified-provider registration**; (5) **AWS auditing pipeline** that privatizes AMIs with reused SSH host keys.

**Identity / auth.** All customer-facing operations are **SigV4 IAM**. Owner-only mutations: `ModifyImageAttribute` (launchPermission), watermark attach/detach, disable/enable, deregister, deprecation, deregistration protection. Account-level (per-Region) controls: Block Public Access for AMIs, Allowed AMIs — both settable directly **or** via an Organizations **declarative policy** (which is supposed to preempt in-account changes).

**Where untrusted data enters & is transformed.**
- A **shared/public AMI is booted as-is** — the AMI *contents* are the untrusted blob (Lens Q), executed with the launcher's instance profile.
- **`RegisterImage`** ingests caller-supplied snapshots + an optional caller-supplied **UEFI variable store** blob → a new AMI with **no recorded ancestry**.
- **`CreateStoreImageTask`** decrypts EBS snapshots and packs the AMI into a **single S3 object** (partition/Region portability) — a KMS→S3-ACL confidentiality downgrade.
- **`resolve:ssm:<param>`** is a late-bound AMI-ID reference **resolved server-side at launch time** from an SSM parameter.
- **Allowed AMIs `ImageCriteria`** evaluates provider/name/product-code/watermark/date criteria at discovery & launch.

**ASCII pipeline (sharing + launch + governance):**

```
                    ┌─────────────────────── AMI OWNER ACCOUNT ───────────────────────┐
                    │  CreateImage / RegisterImage / CopyImage                         │
                    │      │            │                 │                            │
                    │   EBS snapshots   S3 object    UEFI varstore blob                │
                    │      │  (KMS CMK)      (store/restore)                           │
                    │  ModifyImageAttribute(launchPermission): UserId | Group=all |    │
                    │                       OrganizationArn | OU-Arn                   │
                    │  AttachImageWatermark  ·  Enable(Deregistration Protection)      │
                    └───────────────┬───────────────────────────────┬─────────────────┘
   account-level controls           │ share                         │ audit
   (per Region, or via              ▼                               ▼
    declarative policy):   ┌──────────────────┐         ┌───────────────────────────┐
   BlockPublicAccess ─────▶│  SHARED / PUBLIC  │        │ AWS auditing (SSH host-key │
   AllowedAMIs allowlist ─▶│       AMI         │        │  reuse only) → privatize   │
   (ImageProviders,        └────────┬─────────┘         └───────────────────────────┘
    ImageNames, watermark,          │ RunInstances(resolve:ssm:param?)
    productCode, dates)             ▼
                          ┌───────────────────────────────┐   ┌────────────────────────┐
                          │ RECIPIENT / LAUNCHER ACCOUNT   │   │  AWS SERVICE PLANE      │
                          │ boots AMI w/ its instance      │◀──│ mediates snapshot access│
                          │ profile; can re-CreateImage,   │   │ + KMS decrypt at launch │
                          │ CopyImage (needs storage+KMS)  │   │  ***HARD STOP zone***   │
                          └───────────────────────────────┘   └────────────────────────┘
```

---

## 3. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|---|
| B1 | Recipient (AMI shared via `launchPermission` only) | Owner's EBS snapshot | Launch-time implicit grant: *"the system provides the instance access to the referenced EBS snapshots for the launch"* | Recipient reaches `snap-xxxx` by any path other than that launch — `CopySnapshot`/`CreateVolume`/`DescribeSnapshotAttribute` — with no `createVolumePermission` |
| B2 | Recipient of a shared encrypted AMI | Owner's KMS CMK | Owner adds recipient to key policy (`Resource:"*"`, no encryption-context condition) | Recipient decrypts **any other** resource under that CMK, not just the shared snapshot |
| B3 | Copying account | Source owner's storage | `CopyImage` cross-account *requires* explicit `createVolumePermission` + KMS share (stronger than B1) | `CopyImage` succeeds with only `launchPermission` granted — the two trust models collapse |
| B4 | Non-owner account | Owner's `launchPermission` recipient list | `describe-image-attribute --attribute launchPermission` (caller-scoping undocumented) | A non-owner enumerates other tenants' 12-digit account IDs / org / OU ARNs |
| B5 | AMI owner | `all` group during BPA enable window | `modify-image-attribute Add=[{Group=all}]` during the ≤10-min BPA propagation lag | Public share succeeds while `get-image-block-public-access-state` still returns `unblocked`/mid-transition |
| B6 | AMI owner | Org/OU (public-equivalent reach) | `launchPermission.OrganizationArn` — **not** gated by Block Public Access | BPA reports `block-new-sharing` yet an org-wide share to thousands of accounts succeeds |
| B7 | Principal with only `ssm:PutParameter` | Every future `resolve:ssm:` launch | `aws:ec2:image` param validated as *an AMI ID*, not for ownership/trust | Repointing the parameter substitutes the booted AMI with no `ec2:RunInstances` held by the attacker |
| B8 | Any AMI owner | Trust signals (alias / product code / watermark / ancestry root) | Self-attach product code; server-derived-but-inheritable watermark; `RegisterImage` root | An attacker AMI passes a victim's Allowed-AMIs or manual "is this trusted" check |
| B9 | Principal with `DeleteTags`+`DeregisterImage` | Recycle Bin tag-retention rule | Untag immediately before deregister removes the AMI from the rule's match set | AMI is permanently deleted instead of recoverable — no `rbin:*` permission needed to defeat the safety net |
| B10 | AMI owner action (disable/deregister/deprecate) | Downstream consumer accounts / ASGs / launch templates | Instantaneous, account-wide availability change | Consumers' launches begin failing with no consumer-side warning; deregistration protection does **not** block `DisableImage` |
| B11 | Org management account (declarative policy) | Member account's BPA / Allowed AMIs setting | Declarative policy vs. direct in-account API call | A member's direct `enable/disable-*` call mutates effective state (even transiently) despite the policy |
| B12 | Any customer surface | **AWS service plane** (snapshot-mediation / KMS-decrypt fleet, audit-privatization) | Launch-time snapshot access; store-task decrypt; audit pipeline | **HARD STOP** — any AWS-owned identity/credential/ARN observed |

---

## 4. API / Interface Inventory

Legend: **M** = mutating, **N** = non-mutating. All external-facing / callable via SigV4 unless noted.

| API / CLI | M/N | Owner-gated? | Cross-account input | Notes / lead hook |
|---|---|---|---|---|
| `ModifyImageAttribute (launchPermission)` | M | Yes | account ID, `all`, OrgArn, OU-Arn | Core sharing primitive; public+explicit+org can coexist → B4/B5/B6 |
| `DescribeImageAttribute (launchPermission)` | N | **undocumented** | — | Returns full recipient list → **B4 / Q-A1** |
| `ResetImageAttribute (launchPermission)` | M | Yes | — | Clears all shares incl. org/OU in one call |
| `cancel-image-launch-permission` | M | self-only (implied) | — | No account param documented → self-service IDOR sanity check |
| `RunInstances` (+`Encrypted`/`KmsKeyId`, `resolve:ssm:`) | M | launcher | shared AMI's snapshots | Implicit snapshot grant (B1); SSM late-binding (B7) |
| `CopyImage` (`ec2:CopyImage`, auto-bundles `ec2:CopySnapshot`) | M | needs storage+KMS share | source AMI, `KmsKeyId` | B3; bundled snapshot-copy privilege (audit blind spot) |
| `RegisterImage` (`--block-device-mappings SnapshotId=`, `--uefi-data`) | M | account | arbitrary snapshot IDs, UEFI blob | **No ancestry recorded**; snapshot-ownership validation undocumented → B8/Q-supplychain |
| `CreateStoreImageTask` / `DescribeStoreImageTasks` / `CreateRestoreImageTask` | M/N | own or directly-shared | target/source S3 bucket | Decrypts snapshots to an S3 object → KMS→S3 downgrade |
| `attach-image-watermark` / `detach-image-watermark` | M | **owner-only** | — | `WatermarkKey={caller-acct}:{name}` (acct prefix **server-derived**); inherits to derivatives; detach does NOT propagate |
| `enable/disable-image-block-public-access` · `get-image-block-public-access-state` | M/N | account, per-Region | — | ~10-min propagation race (B5); `ManagedBy: account|declarative-policy` |
| `get/enable/disable-allowed-images-settings` · `replace-image-criteria-in-allowed-images-settings` | M/N | account, per-Region | — | States `enabled`/`disabled`/`audit-mode`; only governs public/shared AMIs, never own-account AMIs → copy-to-launder (B8) |
| `describe-instance-image-metadata` | N | account | — | `image-allowed` compliance filter |
| `modify-image-attribute --product-codes` | M | own AMI | product code string | Immutable once set; self-attach spoof (B8) |
| `disable-image` / `enable-image` | M | Yes | — | Strips shares; **not** blocked by deregistration protection; shares don't auto-restore (B10) |
| `deregister-image` (`--delete-associated-snapshots`) | M | Yes | — | Permanent unless a Recycle Bin rule matches (B9/B10) |
| `enable/disable-image-deprecation` | M | Yes (implied) | — | Hides from non-owner listings; **no IAM-perm section documented** (doc-gap) |
| `enable/disable-image-deregistration-protection` | M | Yes (implied) | — | Blocks deregister "regardless of IAM"; optional 24h cooldown; **no IAM-perm section documented** (doc-gap) |
| `describe-image-attribute (lastLaunchedTime)` | N | **owner-only** | — | 24h delay + pre-2017 gap → stale-decommission risk |
| `describe-images (--executable-users, --include-deprecated/-disabled, filter image-watermark-key)` | N | — | — | Enumeration surface; owner-vs-sharee visibility asymmetry |
| `describe-image-references` | N | self-scoped | any AMI ID (incl. not owned) | Own-resource dependency mapping on arbitrary AMI IDs |
| `get-image-ancestry` (`DescribeImageAncestry`) | N | accessible AMIs | — | Caps at 50; tolerates deregistered/inaccessible ancestors → provenance gaps |
| `create-image-usage-report` family | M/N | owner (per-AMI) | — | Who references your AMI; quotas 2000/acct, 1/AMI |
| `rbin create/update/lock/unlock-rule`, `list-images-in-recycle-bin`, `restore-image-from-recycle-bin` | M/N | `rbin:*` namespace | — | Region rules w/ exclusion tags can't be locked; restore→share-state doc-gap |
| SSM: `put-parameter (aws:ec2:image)`, `get-parameter`, public `/aws/service/ami-*` params | M/N | param-scoped | any AMI ID | Launch-time resolution poisoning (B7) |
| `get-instance-uefi-data` | N | own instance | — | Extract seller-enrolled Secure Boot PK/KEK/db |
| Attestable-AMI: `nitro-tpm-pcr-compute` (build), NitroTPM KMS attestation (boot) | — | builder self-attests | — | Integrity-since-build ≠ benignity-of-build |

**Doc-flagged dates / [NEW]-style markers to prioritize:** resource-level `CopyImage` permissions **since 2024-10-28**; **AMI watermarks** + **Allowed AMIs `ImageWatermarks` criterion** (newest governance surface); **Attestable AMIs** (NitroTPM/UEFI, newest integrity surface); **`DescribeImageReferences`** + `AmazonEC2ImageReferencesAccessPolicy`.

---

## 5. Recommended Areas of Focus

Ordered by priority (see Section 5.0). Each area = Background → Security Concern → High-level Test Scenarios (falsifiable claims) → Doc evidence → Severity-if-true.

### 5.0 Priority order
1. **Cross-account snapshot/KMS reach** (A-Enc) — the only place AWS documents *two* trust models for the same resource; Critical ceiling.
2. **Trust-signal forgery feeding Allowed AMIs / provenance** (B-Trust) — newest surface (watermarks, ancestry), governance-defeating.
3. **Launch-time image substitution via SSM `resolve:`** (C-SSM) — confused-deputy, launcher-side RCE-equivalent.
4. **Governance-control bypass & races** (D-Gov) — BPA propagation TOCTOU, org/OU scope gap, copy-to-launder, untag-before-deregister.
5. **Cross-account disclosure** (E-Disc) — recipient list, encrypted-AMI metadata.
6. **Availability / audit-evasion** (F-Avail) — disable-under-protection, quota exhaustion, EventBridge gaps.
7. **Supply-chain of the booted image** (G-Supply) — foreign-code AMI, attestation/Secure-Boot limits (largely customer shared-responsibility; scope carefully).

---

### 5.A — Cross-account snapshot & KMS reach (Lens A + H + B)

**Background.** Sharing an AMI grants launch permission only; *"You do not need to share the Amazon EBS snapshots… the system provides the instance access to the referenced EBS snapshots for the launch."* Copying, by contrast, *"requires the owner to grant you read permissions for the storage that backs the AMI, not just for the AMI itself."* Encrypted AMIs additionally require sharing the KMS CMK; AWS's own example key policies use `Resource:"*"` with no encryption-context condition.

**Security Concern.** The launch-time implicit grant may leak beyond the `RunInstances` code path; the two trust models (launch-implicit vs. copy-explicit) may collapse; a shared CMK may over-grant to every resource encrypted under it; `RegisterImage` may let a share recipient re-delegate the owner's snapshot to a third party.

**High-level Test Scenarios**
- **A1 (High) — Implicit grant escapes the launch path.** *Claim:* with only `launchPermission` (no `createVolumePermission`), the recipient can reach the backing `snap-xxxx` directly. *Oracle:* obtain the snapshot ID via `DescribeImages` on the shared AMI, then attempt `CopySnapshot`/`CreateVolume`/`DescribeSnapshotAttribute`; success = grant leaked. *Evidence:* sharingamis-explicit.md vs. EBS `createVolumePermission` docs.
- **A2 (High) — CopyImage without the explicit grant.** *Claim:* `CopyImage` succeeds on a `launchPermission`-only AMI, piggybacking the implicit grant. *Oracle:* share via launchPermission only (no snapshot/KMS share); attempt `CopyImage` from recipient — expected fail; success = models collapsed. *Evidence:* how-ami-copy-works.md "Resource permissions."
- **A3 (Critical) — RegisterImage snapshot re-delegation chain.** *Claim:* B (holding only `createVolumePermission` on A's snapshot S, no AMI) runs `RegisterImage` referencing S, then shares the new AMI-B with C, whom A never authorized; C launches and reaches A's data. *Oracle:* run the A→B→C chain; C's successful launch = uncontrolled re-share. *Evidence:* creating-an-ami-ebs.md / ami-block-device-mapping.md accept arbitrary `SnapshotId`; **doc-gap** on ownership validation.
- **A4 (Med-High) — Shared-CMK over-grant.** *Claim:* adding a recipient to a CMK policy to unlock one shared snapshot grants decrypt to *every* resource under that CMK. *Oracle:* owner encrypts shared snapshot A and unshared snapshot B with the same CMK; recipient attempts `kms:Decrypt`/`CopySnapshot` against B. *Evidence:* share-kms-key.md / allow-org-ou-to-use-key.md example policies use `Resource:"*"`, no `kms:EncryptionContext`/`kms:ViaService`.
- **A5 (Med-High) — Store-to-S3 confidentiality downgrade.** *Claim:* `CreateStoreImageTask` turns a CMK-encrypted snapshot into an S3 object gated only by bucket ACL/policy. *Oracle:* store a CMK-encrypted AMI to a bucket with SSE off; confirm the object is retrievable/decompressible with `s3:GetObject` alone, no KMS call. *Evidence:* work-with-ami-store-restore.md ("snapshots are decrypted as part of the store process"; "If this can't be done, use of these APIs is not recommended").
- **A6 (doc-gap/High) — Restore encryption state.** *Claim:* a store→restore round-trip in an account with EBS-encryption-by-default **off** yields an *unencrypted* AMI from a previously-encrypted source. *Oracle:* restore and inspect resulting snapshot encryption. *Evidence:* store-restore-how-it-works.md silent on final state.

**Severity-if-true:** A3 **Critical** (cross-account confused-deputy defeating the snapshot-consent model); A1/A2/A5/A6 **High**; A4 **Med-High**.

---

### 5.B — Trust-signal forgery & provenance laundering (Lens A + P + N + I)

**Background.** Customers and the Allowed AMIs feature rely on trust signals: `ImageOwnerAlias` ("Verified provider"), `ProductCodeId`, `ImageWatermarks` (`{account-id}:{name}`), and `get-image-ancestry` "root." Watermarks: **owner-only** to attach, account-id prefix **server-derived** from the caller, but they **inherit onto derivative AMIs, persist across copy/share, and are visible to recipients**; detaching does **not** remove them from derivatives. Allowed AMIs' `ImageWatermarks` criterion can stand alone as an entire `ImageCriterion`.

**Security Concern.** An attacker may make an attacker-owned AMI carry a *trusted* watermark namespace (via inheritance from a legitimately-watermarked base), self-attach a product code, or present a clean `RegisterImage` "root," thereby passing a victim's Allowed-AMIs criterion or manual trust check.

**High-level Test Scenarios**
- **B1 (High) — Watermark inheritance laundering.** *Claim:* an attacker launches an instance from a shared/public AMI legitimately watermarked `X:prod-baseline`, runs `CreateImage` to produce an attacker-owned derivative that **inherits** `X:prod-baseline`, which then satisfies a victim's Allowed-AMIs `ImageWatermarks`-only criterion keyed on `X:prod-baseline`. *Oracle:* build the derivative; `describe-images` shows the inherited `WatermarkKey`; the victim's `enabled` Allowed-AMIs setting returns `ImageAllowed:true` for it. *Evidence:* ami-watermark.md (inherit/persist/visible); ec2-allowed-amis.md (ImageCriterion 5 uses only `ImageWatermarks`). **Confirm first:** does inheritance carry the *original owner's* account-id prefix onto an AMI owned by someone else? (Verified in docs that prefix is server-derived on *attach*; inheritance semantics on `CreateImage` from a watermarked base is the crux — **doc-gap to resolve**.)
- **B2 (High) — Watermark filter with omitted `WatermarkKey`.** *Claim:* an `ImageWatermarks` filter entry that omits `WatermarkKey` (only `MaximumDaysSinceWatermarkCreated`) matches any watermark, so an attacker's own-account watermark passes. *Oracle:* configure such a criterion; attach a same-named watermark from an unauthorized account; confirm `ImageAllowed:true`. *Evidence:* ec2-allowed-amis.md ("Each filter can include the following fields"); **doc-gap** on field-optionality — confirm via `ImageCriterionRequest` API ref.
- **B3 (Med-High) — `ImageNames`-only criterion squatting.** *Claim:* an `ImageCriterion` using `ImageNames:["golden-ami-*"]` without `ImageProviders` admits an attacker AMI named `golden-ami-evil`. *Oracle:* publish such an AMI from an untrusted account; confirm launchable when Allowed AMIs `enabled`. *Evidence:* ec2-allowed-amis.md best practice: *"Using ImageNames alone might not uniquely identify an AMI."*
- **B4 (High) — Copy-to-launder.** *Claim:* copying a disallowed shared AMI into the local account makes it "owned by your account" and thus **always allowed** (Allowed AMIs never restricts own-account AMIs). *Oracle:* with Allowed AMIs excluding provider X, `CopyImage` an X AMI locally; confirm `ImageAllowed:true`/launchable. *Evidence:* ec2-allowed-amis.md ("It does not restrict the AMIs owned by your account… always discoverable and usable").
- **B5 (Med) — Product-code self-attach.** *Claim:* `modify-image-attribute --product-codes` lets an owner claim an arbitrary/real Marketplace product code on a self-owned AMI, and it is immutable thereafter. *Oracle:* set a product code belonging to a real listing; observe whether billing/support/`describe-images` treat it as entitled and whether AWS rejects unauthorized codes. *Evidence:* using-paid-amis-support.md; immutability limitation.
- **B6 (Med) — `RegisterImage` "root" parity.** *Claim:* an attacker-registered AMI presents in `get-image-ancestry` identically to a verified-provider root (no `ImageOwnerAlias`, no ancestor). *Oracle:* `RegisterImage` from raw snapshots; `get-image-ancestry` returns a single root with no alias; check whether any surface distinguishes it from a true verified root. *Evidence:* ami-ancestry.md root definition.
- **B7 (Med) — Ancestry truncation / dead-end.** *Claim:* a >50-deep copy chain truncates ancestry, or a deregistered mid-chain ancestor becomes an uninspectable dead-end, hiding the true root. *Oracle:* chain >50 copies; deregister a mid-chain AMI; inspect `get-image-ancestry`. *Evidence:* ami-ancestry.md (50-cap; preserves deregistered/inaccessible ancestors by ID only).
- **B8 (doc-gap/Critical) — AMI-ID reuse across owners.** *Claim:* a previously-public, auto-unshared/obsolete AMI ID could be re-registered under a different `OwnerId`, letting a new (malicious) owner "become" an AMI ID still hardcoded in victims' launch templates/ASGs. *Oracle:* determine from the API reference whether `ami-` IDs are ever reused across owners. *Evidence:* sharingamis-intro.md describes obsolete-AMI unsharing but gives **no ID-non-reuse guarantee** — **resolve before hunting.**

**Severity-if-true:** B1/B2/B4 **High** (full governance/allowlist bypass); B8 **Critical** if ID reuse is possible; B3/B5/B6/B7 **Medium–Med-High**.

---

### 5.C — Launch-time image substitution via SSM `resolve:` (Lens A + B)

**Background.** `run-instances --image-id resolve:ssm:<param>[:<version>]` late-binds the AMI ID from an SSM parameter, resolved **server-side at launch**. The `aws:ec2:image` parameter type only validates the value *is an AMI ID*.

**Security Concern.** A principal who can write the parameter — but cannot launch — controls what boots; and an IAM `ec2:ImageId` allowlist may be evaluated against the literal `resolve:ssm:` string rather than the resolved ID.

**High-level Test Scenarios**
- **C1 (High) — Write-only launch redirection.** *Claim:* `ssm:PutParameter` on `golden-ami` alone suffices to repoint every `resolve:ssm:golden-ami` launch. *Oracle:* low-priv principal repoints the param to an attacker-controlled (real) AMI ID; the normal automation boots it. *Evidence:* using-systems-manager-parameter-to-find-AMI.md.
- **C2 (doc-gap/High) — IAM allowlist evaluated pre-resolution.** *Claim:* an `ec2:RunInstances` policy allowing only literal AMI X still permits `--image-id resolve:ssm:golden-ami` after the param is repointed to Y. *Oracle:* set such a policy; launch via `resolve:` while the param → X; repoint → Y; relaunch with identical call/policy; observe. *Evidence:* resolution-vs-authorization ordering **undocumented** — resolve first.
- **C3 (Med→High) — Cross-account AMI in a parameter.** *Claim:* `aws:ec2:image` accepts a third-party/public AMI ID with no ownership restriction. *Oracle:* set a param to an arbitrary public AMI ID; confirm `PutParameter` succeeds and `resolve:` launches it. *Evidence:* type validates "as an AMI ID" only.

**Severity-if-true:** C1/C2 **High** (confused-deputy launch substitution / allowlist bypass); C3 **Medium** alone, **High** chained with C1/C2.

---

### 5.D — Governance-control bypass & races (Lens A + I + N)

**Background.** Block Public Access for AMIs (per-Region, ~10-min enable propagation), Allowed AMIs, deregistration protection (+ optional 24h cooldown), and Recycle Bin retention rules are the AMI governance controls. Several are settable via Organizations declarative policy that is supposed to preempt in-account changes.

**Security Concern.** Timing windows and scope gaps may let a mutation slip past a control that appears active.

**High-level Test Scenarios**
- **D1 (High) — BPA enable-propagation TOCTOU.** *Claim:* `Group=all` succeeds during the window when BPA still reads `unblocked`. *Oracle:* call `enable-image-block-public-access`, then race `modify-image-attribute Add=[{Group=all}]`. *Evidence:* manage-block-public-access-for-amis.md (≤10-min window, state reads `unblocked`).
- **D2 (High) — BPA doesn't cover org/OU sharing.** *Claim:* with BPA `block-new-sharing`, an org-wide `OrganizationArn` share (to thousands of accounts, incl. orgs the owner doesn't administer) still succeeds — public-equivalent reach. *Oracle:* share to a large org ARN while BPA reports blocked. *Evidence:* BPA pages describe only `all`-group sharing; org/OU path never mentioned as gated.
- **D3 (High) — Untag-before-deregister evades Recycle Bin.** *Claim:* stripping the matching tag with `DeleteTags` before `DeregisterImage` forces permanent deletion, bypassing tag-level retention — needs no `rbin:*` permission. *Oracle:* create a `tag:env=prod` EC2_IMAGE rule; tag an AMI; `DeleteTags` then `DeregisterImage`; confirm it never enters the Recycle Bin. *Evidence:* recycle-bin-create-rule.md + deregister-ami.md.
- **D4 (High) — Declarative-policy precedence bypass.** *Claim:* a member account's direct `enable/disable-*` call mutates effective BPA/Allowed-AMIs state (even transiently) despite an authoritative declarative policy. *Oracle:* under such a policy, issue the direct call; observe reject vs. silent no-op vs. transient change of `ManagedBy`/state. *Evidence:* block-public-access-to-amis.md / ec2-allowed-amis.md ("you can't modify the setting directly" — phrased as UI/policy, not confirmed as hard API rejection).
- **D5 (Low-Med) — Public+watermark invariant race.** *Claim:* concurrent `attach-image-watermark` and `Group=all` yields a public AMI that also carries a watermark, breaking the "watermarks only on private AMIs" invariant Allowed-AMIs filtering assumes. *Oracle:* fire both back-to-back; a `Public:true` AMI with non-empty `ImageWatermarks` = breach. *Evidence:* ami-watermark.md mutual-exclusion note; no stated atomicity.

**Severity-if-true:** D1/D2/D3/D4 **High**; D5 **Low-Med** (governance/audit inconsistency).

---

### 5.E — Cross-account disclosure (Lens A + M)

**Background.** `describe-image-attribute launchPermission` returns the recipient list; sharing an encrypted AMI requires a separate KMS grant, so metadata visibility and data access may decouple.

**High-level Test Scenarios**
- **E1 (High) — Recipient-list enumeration by a non-owner.** *Claim:* an account holding only launch permission (or a generic `ec2:DescribeImageAttribute` grant) reads the AMI's full `launchPermission` list — other tenants' account IDs, org/OU ARNs. *Oracle:* account B calls `describe-image-attribute --attribute launchPermission` on owner A's AMI. *Evidence:* share-amis-org-ou-manage.md sample output includes `OrganizationalUnitArn`; caller-scoping never stated.
- **E2 (Med) — Encrypted-AMI metadata without the KMS grant.** *Claim:* a recipient granted `launchPermission` but not the KMS key can still `describe-images`/`describe-image-attribute` (name, description, snapshot IDs) — disclosure before the real (KMS) access boundary. *Oracle:* share without the KMS grant; confirm metadata read succeeds and only `RunInstances` fails at decrypt. *Evidence:* sharingamis-explicit.md (KMS grant is separate).
- **E3 (Med) — Org/OU revocation false-negative (documented).** *Claim:* `Remove=[{UserId=...}]` returns success while access silently persists because the account is also covered by a shared OU. *Oracle:* remove the UserId; confirm success response; confirm the target can still launch/describe. *Evidence:* share-amis-org-ou-manage.md verbatim ("Amazon EC2 returns a success message. However, the AMI continues to be shared").
- **E4 (Med) — S3 store-object metadata leak.** *Claim:* the stored `.bin` object exposes owner account ID + AMI metadata via `s3:GetObjectTagging` independent of AMI-level sharing. *Oracle:* grant only `GetObjectTagging`; read owner account ID/metadata. *Evidence:* store-restore-how-it-works.md metadata tags.

**Severity-if-true:** E1 **High** (cross-account account-ID/org recon); E2/E3/E4 **Medium**.

---

### 5.F — Availability & audit evasion (Lens L + O + A)

**Background.** Owner lifecycle actions are instantaneous and account-wide for all consumers. `EC2 AMI State Change` EventBridge events fire only for Copy/Create/Restore/Deregister/Disable/Enable/Register — not for deprecation, deregistration-protection, tag, or launch-permission changes. `LastLaunchedTime` has a 24h delay + pre-2017 gap and is owner-only. Per-Region quotas: 50,000 AMIs (incl. pending/disabled/Recycle Bin), 1,000 sharing entities.

**High-level Test Scenarios**
- **F1 (High) — Disable defeats deregistration protection.** *Claim:* `DisableImage` strips all shares and blocks launches on an AMI whose deregistration protection is ON (and during its 24h cooldown). *Oracle:* enable protection; call `disable-image`; confirm consumers lose access. *Evidence:* ami-deregistration-protection.md vs. disable-an-ami.md (no cross-reference; cooldown scoped to deregister only).
- **F2 (Med) — Governance actions unlogged.** *Claim:* enabling/disabling deprecation or deregistration protection, and mutating tags/launch permissions, produce no `EC2 AMI State Change` event. *Oracle:* subscribe the rule; perform the actions; confirm silence. *Evidence:* monitor-ami-events.md operations table omits them. *(Cross-check CloudTrail separately — EventBridge silence ≠ CloudTrail silence; but a defender relying on this integration is blind.)*
- **F3 (Med) — Stale last-launched → premature decommission.** *Claim:* the 24h delay makes an actively-used AMI read as unused, prompting deprecate/deregister that breaks a live consumer. *Oracle:* launch, then query `LastLaunchedTime` within 24h (absent/stale); confirm non-owners can't query it at all. *Evidence:* ami-last-launched-time.md; ami-deprecate.md recommends it as the decommission signal.
- **F4 (Low-Med / High if multi-tenant) — Per-Region AMI quota exhaustion.** *Claim:* one principal's runaway `CreateImage`/`RegisterImage` exhausts the 50,000 cap (disabled/pending count), blocking every other team. *Oracle:* approach the cap in an isolated test Region; confirm a second principal's `CreateImage` fails. *Evidence:* ami-quotas.md. *(Self-DoS in a single-tenant account is out-of-scope; High only for shared platform accounts.)*
- **F5 (Low-Med) — Recycle Bin exclusion-tag rules can't be locked.** *Claim:* a Region-level rule with exclusion tags can never be locked, leaving its exception list mutable by any `rbin:UpdateRule` holder. *Oracle:* attempt to lock such a rule; confirm rejection. *Evidence:* recycle-bin-create-rule.md note.
- **F6 (doc-gap/Med) — Restore doesn't re-share.** *Claim:* restoring from the Recycle Bin does not restore prior launch permissions (mirroring `EnableImage`), silently leaving consumers broken. *Oracle:* share→deregister(→bin)→restore; check whether consumer B regains access without re-`ModifyImageAttribute`. *Evidence:* disable-an-ami.md analog; recycle-bin restore page silent → **resolve.**

**Severity-if-true:** F1 **High**; F4 **High** on multi-tenant platform accounts (else Low-Med); F2/F3/F5/F6 **Medium**.

---

### 5.G — Supply chain of the booted image (Lens Q — mostly customer shared-responsibility)

**Background.** *"You use a shared AMI at your own risk… treat shared AMIs as you would any foreign code."* AWS's only documented automated integrity control for public AMIs is **reused-SSH-host-key detection** (→ privatize after a grace period). Attestable AMIs and UEFI Secure Boot are integrity mechanisms; `CreateImage` copies the instance's UEFI variable store into the AMI.

**Security Concern.** A malicious shared/public AMI runs with the launcher's instance profile; and the integrity features attest *integrity-since-build*, not *benignity-of-build*, while trusting seller-chosen key material.

**High-level Test Scenarios**
- **G1 (High, customer-facing) — Foreign-code AMI vs. thin AWS scanning.** *Claim:* AWS's audit catches only reused SSH host keys, not backdoors, planted `authorized_keys`, or embedded credentials. *Oracle:* (sandbox) publish an AMI reusing a host key vs. one with a planted `authorized_keys`; observe which AWS flags/privatizes. *Evidence:* building-shared-amis.md (only host-key reuse is AWS-audited); sharing-amis.md foreign-code warning.
- **G2 (High) — Attestation ≠ benignity.** *Claim:* a spec-compliant Attestable AMI containing a persistence-free malicious payload still attests to KMS on every restart. *Oracle:* build such an AMI (AL2023/NixOS, NitroTPM, UEFI, erofs+dm-verity, correct PCR compute) and confirm attestation succeeds. *Evidence:* attestable-ami.md (hash computed by the AMI's own builder; no AWS content review).
- **G3 (Med-High) — Inherited Secure Boot root of trust.** *Claim:* a shared AMI with preconfigured Secure Boot carries a seller-chosen PK/KEK/db the buyer never reviewed and *"cannot change… without creating a new AMI."* *Oracle:* `get-instance-uefi-data` on a launched shared AMI; decode enrolled certs; confirm no pre-launch API to verify the cert subject/fingerprint against a known-good seller identity. *Evidence:* create-ami-with-uefi-secure-boot.md.
- **G4 (Low/Info) — TPM posture invisible in console.** *Claim:* console buyers can't see `TpmSupport`; only CLI reveals it. *Oracle:* confirm no console column/filter. *Evidence:* verify-nitrotpm-support-on-ami.md ("The Amazon EC2 console does not display TpmSupport"). Raises G2/G3 severity by shrinking the population that checks.

**Severity-if-true:** G1/G2 **High** (as trust-model/coverage gaps); G3 **Med-High**; G4 **Low/Info**. *Much of G is the customer side of the shared-responsibility line — frame findings as "the trust signal means less than a customer assumes," not as an AWS service-plane bug.*

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Reach a shared AMI's snapshot outside the launch path | Launch-time snapshot mediation | "system provides instance access… for the launch" scoping (A1) |
| Re-delegate an owner's snapshot A→B→C via RegisterImage | RegisterImage + sharing | (undocumented ownership validation) (A3) |
| Over-decrypt via a reused shared CMK | KMS key policy | `Resource:"*"`, no encryption-context condition (A4) |
| Read a CMK-encrypted AMI as plaintext from S3 | Store/restore to S3 | bucket ACL/policy + optional SSE (A5) |
| Pass Allowed AMIs with an inherited/forged watermark | Watermarks + `ImageWatermarks` criterion | server-derived account-id prefix; owner-only attach (B1/B2) |
| Launder a disallowed AMI by copying it locally | Allowed AMIs own-account exemption | "does not restrict AMIs owned by your account" (B4) |
| Substitute the booted AMI via SSM param write | `resolve:ssm:` + `aws:ec2:image` type | value "validated as an AMI ID" only (C1/C2) |
| Make an AMI public despite Block Public Access | BPA enable propagation / org path | ≤10-min window; BPA covers only `all`-group (D1/D2) |
| Permanently delete a "protected" AMI by untagging | Recycle Bin tag rules | rule matches tags at deletion time (D3) |
| Disable a deregistration-protected shared AMI | Deregistration protection scope | protection blocks deregister only, not disable (F1) |
| Enumerate other tenants' account IDs | `DescribeImageAttribute launchPermission` | (caller-scoping undocumented) (E1) |
| Boot foreign code with the launcher's instance profile | Shared/public AMI contents | AWS audits reused SSH host keys only (G1) |
| Trust an attestation that hides a malicious build | Attestable AMI / NitroTPM | hash computed by the builder (G2) |

---

## 7. Out-of-Scope Risk Categories

- **A user steering their own instance / building their own malicious AMI for their own account** — not a boundary break.
- **Single-tenant self-DoS** via the 50,000-AMI or 1,000-share quota in an account one team controls (F4 in-scope only for shared multi-tenant platform accounts).
- **Customer-side shared-responsibility items** — leftover credentials/keys the *customer* fails to strip from *their own* published AMI (building-shared-amis.md is guidance to publishers). G-series findings are in scope only as "trust-signal-means-less-than-assumed," not as AWS service bugs.
- **Underlying shared EBS/S3/KMS infrastructure**, IMDS on fully-managed hosts, DNS rebinding against private-only endpoints — out of scope.
- **AWS service plane** (the internal snapshot-mediation/KMS-decrypt fleet, the audit-privatization pipeline) — **HARD STOP**, disclosure-only.
- **The injected "agent-toolkit" doc footer** — reported as a corpus-integrity issue (Section 0), not executed; not an AMI vulnerability.

---

## 8. Null Hypotheses & Doc Gaps

**Lenses that did not fire (pages checked):**
- **Lens D (data-plane→control-plane), F (wire-protocol/translation injection), J (OAuth/3P linking), K (prompt injection / GenAI)** — **N/A.** Checked the full AMI chapter (sharing, encryption, copy, store/restore, lifecycle, quotas, monitoring, ancestry, references, attestable/Secure-Boot, ComponentsAMIs, boot). No control-plane network path, no customer-input→backend-language translator, no OAuth/3P integration, and **no LLM/agent/GenAI component** anywhere in the AMI pipeline. *(The only "AI" reference is the injected agent-toolkit footer, which is not a service component.)*
- **Lens C (credential vending), E (RBAC/privilege-esc within a service):** partially — AMI ops are plain IAM SigV4 with owner-only mutations; no session-policy/ProvidedContext vending surface. Kept the confused-deputy angles under A/B/C instead.

**Doc gaps to resolve BEFORE live hunting (highest value first):**
1. **`resolve:ssm:` authorization-vs-resolution ordering** (C2) — is an `ec2:ImageId` IAM condition evaluated against the literal `resolve:` string or the resolved ID? Undocumented.
2. **`RegisterImage` snapshot-ownership validation** (A3) — does it require true ownership or mere `createVolumePermission`/read on the referenced snapshot? Not in creating-an-ami-ebs.md / ami-block-device-mapping.md (register-image.md absent from mirror).
3. **Watermark inheritance semantics on `CreateImage` from a watermarked base** (B1) — does the derivative (owned by a different account) carry the *original owner's* account-id-prefixed `WatermarkKey`? Crux of the Allowed-AMIs bypass.
4. **`ImageWatermarks` / `ImageCriterionRequest` field optionality** (B2) — can `WatermarkKey` be omitted? Confirm via API reference.
5. **AMI-ID reuse across owners** (B8) — is a `ami-` ID ever reassigned to a different `OwnerId`? No non-reuse guarantee documented.
6. **IAM actions + condition keys for deprecation / deregistration-protection toggles** (F1, ABAC) — no "Required IAM permissions" section on those pages; cross-check `list_amazonec2.html` for `ec2:EnableImageDeprecation`, `ec2:*ImageDeregistrationProtection` and `aws:ResourceTag` support.
7. **Recycle Bin restore vs. prior launch-permission state** (F6) — does restore re-share, or leave consumers broken?
8. **Store→restore final encryption state** (A6) — encrypted source → possibly unencrypted target when EBS-encryption-by-default is off?
9. **Revocation timing of the implicit launch-time snapshot grant** (A1/A2) — lifecycle relative to `launchPermission` removal; TOCTOU window for already-running instances.
10. **`DescribeImageAttribute launchPermission` caller-scoping** (E1) — is the read restricted to the owner? Not stated.

---

*End of plan. All leads are documentation-derived hypotheses; confirm each mechanism against the API reference and an authorized test environment before acting. Observe the Section 0 HARD STOP on any AWS service-plane identity.*
