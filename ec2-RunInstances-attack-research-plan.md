# EC2 `RunInstances` — Attack / Research Plan

> **Target:** `ec2:RunInstances` (Amazon EC2 instance launch)
> **Doc entry point:** https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RunInstances_section.html
> **Method:** `security-questionbuilder` (boundary-first, falsifiable-hypothesis research plan). Reasoning is **documentation-only**; every lead is a hypothesis a hunter confirms later against an authorized account. No live system was touched to produce this plan.
> **Primary sources:** offline mirror `./aws-docs` cross-checked against `docs.aws.amazon.com` where reachable. Authoritative IAM data from `docs/service-authorization/latest/reference/list_ec2.md` (RunInstances action-with-resources table, ~lines 9585–9610); request params from `docs/AWSEC2/latest/APIReference/API_RunInstances.md`; sample policies from `docs/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md`.

---

## 0 — How to use this document

This is a research plan, not a findings report. Each **lead** in §5 is a falsifiable hypothesis in a fixed shape:

> **Claim** (a boundary that *should* hold, stated so it can be broken) → **Mechanism** (the exact doc page/field/condition-key that makes it plausible) → **Confirm/Refute oracle** (the single observation that settles it — a `iam:SimulatePrincipalPolicy` call or a `Describe*`/`--dry-run` read is always preferred over a resource-mutating probe) → **Preconditions / Cost / Severity-if-true** → **Stop condition** (what refutes the lead, so the hunter does not over-run it).

**Prioritization for the hunter (read §5 in this order):**
1. **§5.A Lead 1 + §5.C Lead 1 (the privesc core)** — `RunInstances` + `iam:PassRole` + `UserData`/IMDS is the single highest-yield chain; it turns "can launch" into "can act as a role I was never granted." Start here.
2. **§5.A Lead 2 / Lead 6 (multi-resource fail-open)** — the structural crown jewel: per-resource-type condition-key asymmetry means a condition on one resource statement silently fails to gate the others, and AWS's own shipped samples demonstrate the weak pattern. This is where real customer policies break.
3. **§5.B Lead 1 (whoAMI / AMI authenticity)** — supply-chain code-exec at boot; externally corroborated (see §5.B background).
4. Everything else as time permits.

**What "confirmed" means here:** most leads are settlable with **read-only** oracles (`iam:SimulatePrincipalPolicy`, `DescribeImages`, `DescribeInstances --filters`, `DescribeLaunchTemplateVersions`, policy text review). A hunter should exhaust those before any launch. Where a lead genuinely needs a launch to confirm, it is marked, and the launch must use a throwaway AMI/role/subnet in an authorized account only.

---

## 1 — Pentest objectives

1. Determine whether `ec2:RunInstances` can be used as a **privilege-escalation primitive** — passing an instance profile whose role exceeds the caller's own privilege, then retrieving that role's credentials via IMDS (directly, via `UserData`, or via a later SSRF). *(§5.A-1, §5.C-1, §5.C-2)*
2. Determine whether the **multi-resource-type authorization model** fails open — i.e. whether a condition attached to one of RunInstances' ~12 resource types leaves the other resource types (AMI, subnet, security-group, key-pair, snapshot, network-interface) unconstrained. *(§5.A-2, §5.A-6, §5.C-3)*
3. Determine whether **externally-owned resources** consumed by a launch (public/shared AMIs, shared snapshots, caller-chosen KMS keys) constitute a trust or supply-chain breach — in particular the **whoAMI** name-confusion class. *(§5.B-1, §5.B-2, §5.B-3)*
4. Determine whether documented **hardening controls** (`ec2:MetadataHttpTokens`, `ec2:Owner`, `ec2:AssociatePublicIpAddress`, `ec2:Encrypted`) are insecure-by-omission — present as condition keys but absent from AWS's own baseline sample policies. *(§5.A-5, §5.B-5, §5.C-2, §5.C-4)*
5. Audit every **AWS-authored sample policy / IAM artifact** shipped for RunInstances statement-by-statement for weak defaults that customers copy verbatim. *(§5.A-6)*
6. Characterize **credential-lifecycle and attribution** weaknesses that amplify any of the above during incident response (unbounded IMDS cred lifetime; no CloudTrail link from IMDS fetch to the originating launch). *(§5.C-5)*

**Hard stop (service-plane boundary):** The moment any evidence surfaces an identity/credential/ARN/account belonging to **AWS's own service plane** — e.g. the instance-identity role `arn:aws:iam::<acct>:assumed-role/aws:ec2-instance/<instance-id>`, an SLR credential, or an AWS fleet account — **stop, preserve the evidence, and flag for AWS-Security disclosure.** Do not probe IMDS on AWS-managed hosts.

---

## 2 — Components, assets, and design

### What the API is

`RunInstances` is a **single, composite, mutating, SigV4-authenticated** control-plane call (public SDK + CLI + console) that atomically:

- selects a machine image (`ImageId` — an AMI that may be **owned by the caller, shared with them, or public from any account**);
- provisions compute (`InstanceType`, `Placement`, `MinCount`/`MaxCount`);
- attaches storage (`BlockDeviceMapping.N` → EBS volumes, optionally from a `SnapshotId`, optionally encrypted with a caller-supplied `Ebs.KmsKeyId`);
- attaches an **identity** (`IamInstanceProfile` → an IAM role assumable later via IMDS — a *different principal* from the caller);
- injects **boot-time code** (`UserData`, base64, run as **root** at first boot);
- sets **network position** (`NetworkInterface.N` / `SubnetId` / `SecurityGroupId.N` / `PrivateIpAddress` / `AssociatePublicIpAddress`);
- sets the **credential-exposure surface** (`MetadataOptions.HttpTokens` / `HttpEndpoint` / `HttpPutResponseHopLimit` — i.e. IMDSv1-vs-v2 posture);
- optionally sources **all of the above from a `LaunchTemplate`** (with late-bound `$Latest`/`$Default` version resolution);
- tags the created resources (`TagSpecification.N`).

Two parameters are documented as **reserved/internal**: `Operator` ("Reserved for internal use") and `AdditionalInfo` ("Reserved") — see §3 hidden-knob note.

### Assets at stake

- **The instance-profile role's credentials** — vended by IMDS, not bounded by the role's max-session-duration, no push-revocation. *The crown-jewel asset.*
- **The root filesystem / execution context of the launched instance** — controlled by whoever controls the AMI and `UserData`.
- **Network reachability** — which VPC/subnet/security-group the instance lands in, and whether it gets a public IP.
- **EBS data at rest** — which KMS key protects it; whether a shared snapshot's key stays in the owner's control.
- **Key-pair private key** — for CloudFormation-provisioned pairs, persisted to SSM Parameter Store (§5.B-4).

### Identity / trust actors in one launch

| Actor | Identity | Notes |
|---|---|---|
| **Caller** | SigV4 IAM principal | Holds `ec2:RunInstances` (+ usually `iam:PassRole`, `ec2:CreateTags`). |
| **Instance profile role** | A *different* IAM role | Assumed later via IMDS; its privilege need not match the caller's. |
| **AMI owner** | Possibly a *third-party / public* account | Controls the booted root filesystem. |
| **Snapshot / KMS-key owner** | Possibly a *third-party* account | Example 6 shows a cross-account-shaped KMS ARN. |
| **Launch-template maintainer** | Possibly a *lower-privileged* principal | Can mutate `$Default` version after a grant is reviewed. |
| **AWS service plane** | `ec2.amazonaws.com`, instance-identity role | **Hard-stop boundary.** |

### ASCII design / data-flow

```
   Caller (ec2:RunInstances + iam:PassRole + ec2:CreateTags)
        │  one SigV4 call, ~12 resource types authorized INDEPENDENTLY
        ▼
┌──────────────────────── RunInstances authorization ────────────────────────┐
│  image*        instance*       key-pair     network-interface*  security-grp*│
│  (ec2:Owner,   (ec2:Instance   (ec2:KeyPair (ec2:Subnet,        (ec2:Security│
│   ec2:Public,   Profile,        Name)        ec2:Vpc,            GroupID,    │
│   ec2:ImageID)  ec2:Metadata                 ec2:AssociatePub..  ec2:Vpc)    │
│                 HttpTokens,                   ec2:NetworkIntfID)             │
│   subnet*       aws:RequestTag) volume        snapshot          launch-templ │
│  (ec2:SubnetID, ───────────────(ec2:Encrypted,(ec2:Owner,      (ec2:IsLaunch│
│   ec2:Vpc)       NO ec2:New-     ec2:Parent    ec2:SnapshotID)   TemplateRes,│
│                  InstanceProfile  Snapshot)                       ec2:Launch │
│    spot-instances-request (CONDITIONALLY EVALUATED — skipped if untagged)    │
│    + iam:PassRole  (iam:PassedToService = ec2.amazonaws.com)                 │
└──────────────────────────────────────────────────────────────────────────────┘
        │ launch succeeds
        ▼
   ┌─────────────── Launched instance ───────────────┐
   │  UserData runs as ROOT at first boot            │
   │        │                                        │
   │        ▼                                        │
   │  GET 169.254.169.254/latest/meta-data/iam/      │ ◀── IMDSv1 reachable by
   │      security-credentials/<role>  ──► STS creds │     plain SSRF when
   │        │  (not max-session-duration bounded,    │     HttpTokens=optional
   │        │   no CloudTrail event for this GET)    │     (the DEFAULT)
   │        ▼                                        │
   │  Act AS the instance-profile role, off-box,     │
   │  until natural rotation expiry                  │
   └──────────────────────────────────────────────────┘
        ▼
   Account-wide impact scaling with the passed role's privilege
```

The critical design fact: **one intent ("launch an instance"), N independent authorizations.** The caller's mental model is a single action; IAM evaluates a dozen resource statements, each gated only by the condition keys attached to *that* resource type. Every structural lead below is a specialization of that mismatch.

---

## 3 — API / interface inventory

| Name | Method | Mutating? | Internet-callable? | Authorized callers | Security-relevant inputs | Notes |
|---|---|---|---|---|---|---|
| `RunInstances` | SigV4 (SDK/CLI/console) | **Yes** | Yes | Any principal with `ec2:RunInstances` | `ImageId`, `IamInstanceProfile`, `UserData`, `MetadataOptions`, `BlockDeviceMapping.N` (`SnapshotId`,`KmsKeyId`), `KeyName`, `NetworkInterface.N`/`SubnetId`/`SecurityGroupId.N`, `TagSpecification.N`, `LaunchTemplate` | The target. Composite multi-resource authorization. |
| `iam:PassRole` | (implicit, co-required) | authz-only | — | Caller, for the passed role | role ARN; `iam:PassedToService` | **No linkage** back to which instance profile wraps the role (§5.A-1). |
| `ec2:CreateTags` | (implicit, tag-on-create) | Yes | — | Caller | `aws:RequestTag`, `aws:TagKeys` | Only re-evaluated if tags are specified. |
| `DescribeImages` | SigV4 | No | Yes | Any (`ec2:DescribeImages`) | `--owners` (optional!), name/tag filters | whoAMI root cause — returns public AMIs by default unless owner-pinned (§5.B-1). |
| `DescribeInstances` / `DescribeLaunchTemplateVersions` / `DescribeKeyPairs` | SigV4 | No | Yes | Read grants | — | **Read-only oracles** for the leads below. |

**Hidden / reserved knobs (API reference accepts, console/prose hide):**
- `Operator` — "Reserved for internal use" (relates to declarative/managed instances; `ec2:ManagedResourceOperator` condition key exists on `instance`/`launch-template`). **Lead-worthy:** what is the most-permissive value accepted, and does it change the trust posture of the instance? Confirm surface first (doc-gap).
- `AdditionalInfo` — "Reserved."
- `DisableApiTermination`, `DisableApiStop`, `InstanceInitiatedShutdownBehavior` — availability/DoS-relevant knobs.

**Doc-flagged lead:** the target devguide page is **thin on security** — it is a 12-language SDK/CLI code catalog (Example 3 = block-device-mappings, Example 4 = tag-on-create, Example 5 = user-data, PowerShell V5 Example 7 = DryRun). It never pins an AMI owner, never sets `MetadataOptions`, never sets a KMS key policy — so it *teaches the insecure-by-omission defaults* that §5 repeatedly turns into leads.

---

## 4 — Trust-boundary map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| B1 | Caller's own privilege | Instance-profile role's privilege | `IamInstanceProfile` + `iam:PassRole` → IMDS cred vend | Caller performs an action, via vended creds, that its own identity is denied → **privesc breach**. |
| B2 | One RunInstances resource statement | Sibling resource statements (AMI/subnet/SG/…) | Per-resource-type condition-key evaluation | A condition the author attached to gate the launch is **inert** for a sibling resource type the caller can freely choose → **fail-open scoping breach**. |
| B3 | Caller's account | Third-party / public AMI owner | `ImageId` resolved by name/filter without owner pin | Victim boots an attacker-published AMI → **supply-chain code-exec breach** (whoAMI). |
| B4 | Caller's account | Third-party snapshot / KMS-key owner | `BlockDeviceMapping.SnapshotId` / `Ebs.KmsKeyId` | A same-account `ec2:Owner` snapshot restriction is bypassed by an AMI's implicit backing-snapshot grant → **enforcement-gap breach** (unconfirmed, §5.B-2). |
| B5 | EC2 IAM surface | SSM Parameter Store `/ec2/keypair/*` | CFN-provisioned key pair persists private key to SSM | A principal denied EC2 key-pair actions reads the private key via `ssm:GetParameter` → **cross-service IAM-wall bypass** (§5.B-4). |
| B6 | Instance workload (any process / SSRF) | IMDS `169.254.169.254` | `HttpTokens=optional` (default) | Plain unauthenticated GET returns role creds → **credential-theft breach** (§5.C-2). |
| B7 | Lower-privileged template maintainer | RunInstances-granted principal's effective config | `$Default`/`$Latest` launch-template late-binding | Changing the default template version silently changes what a RunInstances grant authorizes → **grant-drift breach** (§5.A-4). |
| **B∞** | **Any customer surface** | **AWS service plane** (`ec2.amazonaws.com`, instance-identity role) | IMDS / SLR / fleet account | **Any such identity/credential/ARN surfaced = HARD STOP, preserve, disclose.** |

---

## 5 — Recommended areas of focus

Three lens clusters, each produced by a dedicated documentation-only deep-dive. Severity uses the AWS-aligned scale: cross-**account** data/credential access = **Critical**; intra-account privesc = **High**; ABAC/scoping gap = **Medium–High**; doc/sample-policy defect = **Medium**; attribution/awareness gap = **Informational–Medium**.

---

### §5.A — IAM authorization & condition-key scoping (Lens B / E / S / I / X / R / U)

**Background.** `ec2:RunInstances` requires an `Allow` across up to a dozen independently-typed resources in one call (`list_ec2.md` ~9585–9603: `image*`, `instance*`, `key-pair`, `launch-template`, `network-interface*`, `security-group*`, `subnet*`, `volume`, `snapshot`, `placement-group`, `capacity-reservation`, `spot-instances-request`, …), and **each resource type carries its own, non-overlapping condition-key set.** The policy author models "the launch"; IAM evaluates N resource-statements, each gated only by the keys attached to it. That mismatch is the structural root of this cluster.

**Security concern.** A policy that is "correct" for one resource type (e.g. AMI-owner-restricted) silently fails to constrain the others (instance profile, security group, subnet), and AWS's own shipped samples demonstrate the weak pattern.

---

**Lead 1 — PassRole / InstanceProfile decoupling → privilege escalation at launch.**
- **Claim:** A caller with `ec2:RunInstances` + `iam:PassRole` scoped by *role-name pattern* can attach an instance profile wrapping a role that was never meant to be reachable, because the RunInstances-side check (`ec2:InstanceProfile` = profile ARN) and the PassRole-side check (role ARN) authorize two independently-named objects that never cross-validate — and RunInstances has **no `ec2:NewInstanceProfile` key** (that key is only on `AssociateIamInstanceProfile`/`ReplaceIamInstanceProfileAssociation`).
- **Mechanism:** `permission-to-pass-iam-roles.md` lines 8–46 (RunInstances + PassRole scoped to `role/DevTeam*`, no resource tie on the RunInstances side); `iam-roles-for-amazon-ec2.md` line 46 — "you create the role and instance profile as separate actions, with potentially different names." So `ec2:InstanceProfile: "…instance-profile/Web*"` and `iam:PassRole: "…role/Web*"` are matched against two free-named objects; a profile `WebDeploy` wrapping role `AdminRole` defeats the intended bound.
- **Oracle:** `iam:SimulatePrincipalPolicy` for `ec2:RunInstances` with `ec2:InstanceProfile`=high-priv-profile-ARN **and** for `iam:PassRole` with `iam:PassedToService=ec2.amazonaws.com` against that role. Both `allowed` ⇒ confirmed, no launch needed. (Secondary: `RunInstances --dry-run` with the real `IamInstanceProfile`.)
- **Preconditions:** caller has RunInstances + name-wildcard PassRole; a profile whose name diverges from its wrapped role exists.
- **Cost:** low (one simulate pair). **Severity:** **High** (intra-account privesc without `sts:AssumeRole`).
- **Stop:** simulation shows profile/role ARNs are genuinely coupled in the test account (naming SCP enforced) → refuted for that account; remains a generic design gap.

**Lead 2 — Multi-resource fail-open: a condition on one resource type does not gate the call.**
- **Claim:** A condition attached to `instance*` (e.g. `ec2:InstanceType`) leaves every other resource type (image, subnet, security-group, key-pair, volume, snapshot, network-interface) governed only by whatever `Resource` ARNs the sibling statements list — typically `*`.
- **Mechanism:** `iam-policies-for-amazon-ec2.md` lines 195–196 (AWS's own warning that a condition key "applies only to the resource" its statement names — documented as the fail-*closed* mode; the fail-*open* inverse is the same mechanism). Demonstrated by `ExamplePolicies_EC2.md` lines 266–300: `image/ami-*` conditioned on `ec2:Owner=amazon`, but `instance/*`, `subnet/*`, `security-group/*`, `volume/*`, `key-pair/*`, `network-interface/*` granted with **no condition**.
- **Oracle:** `iam:SimulatePrincipalPolicy` for `ec2:RunInstances` supplying context keys for *all* resource types at once (self-owned AMI + arbitrary `ec2:SecurityGroupID` + arbitrary `ec2:Vpc`) and checking which per-resource evaluations return `allowed` — reveals the open resource types.
- **Preconditions:** a multi-statement policy where only a subset of resource types carries a condition.
- **Cost:** low. **Severity:** **Medium–High** — an open `security-group*`/`subnet*` statement is a network-exposure escalation, not just a cost-control bypass.
- **Stop:** every resource-type statement carries matching Deny-side coverage (e.g. the `ArnNotEquals` subnet-deny pattern, `ExamplePolicies_EC2.md` 423–461) → refuted.

**Lead 3 — Tag-on-create ABAC self-widening via `aws:RequestTag`.**
- **Claim:** `aws:RequestTag`/`aws:TagKeys` enforcement at launch covers only `instance`/`volume`/`network-interface`/`secondary-interface`/`spot-instances-request` — **not** image/security-group/subnet/key-pair/snapshot. A caller whose downstream lifecycle permissions are gated by `aws:ResourceTag` can self-assign the qualifying tag at launch (gated only by `aws:RequestTag` on `instance`), closing a loop the author treated as externally controlled.
- **Mechanism:** `ExamplePolicies_EC2.md` 212–217 (AWS's own "tag each instance to grant manage rights" recommended pattern — inherently self-assigned); `supported-iam-actions-tagging.md` 70, 105 (`aws:RequestTag` enforces *presence*, not *origin*). If the launch policy allows an attacker-controllable tag *value* (`StringLike "*"`, lines 86–90) and a separate statement grants `ec2:TerminateInstances` on `aws:ResourceTag/team=red`, the caller tags `team=red` on launch and inherits another team's lifecycle control.
- **AWS-acknowledged fail-open (same lead):** `ExamplePolicies_EC2.md` 751–752 — *"Surprise inconsistency number 2 … In the case of spot-instances-request, this policy will not be evaluated if there are no spot-instances-request tags, so a non-tag Spot on Run request will succeed."* (reconfirmed 999–1006, 1176–1181 "NOT SUPPORTED"). **Any Deny/ABAC condition on `spot-instances-request` is bypassable by simply not tagging the Spot request.**
- **Oracle:** `iam:SimulatePrincipalPolicy` for RunInstances with `aws:RequestTag/team=red` ⇒ `allowed`, then for `ec2:TerminateInstances` with `aws:ResourceTag/team=red`. For the Spot anomaly: simulate a Spot RunInstances with a `spot-instances-request` Deny, tag set vs unset — predicted skipped when unset.
- **Cost:** low. **Severity:** **Medium–High** (depends on whether tag *values* are restricted). The Spot anomaly is a permanent Tier-2 doc-gap (AWS documents it as by-design).
- **Stop:** tag-gating uses `StringEquals` on a fixed, non-attacker-chosen value tied to `${aws:username}` → self-widening refuted.

**Lead 4 — `ec2:IsLaunchTemplateResource` / `ec2:LaunchTemplate` late-binding & mutable default version.**
- **Claim:** A grant conditioned on `ec2:LaunchTemplate: ArnLike "launch-template/lt-X"` is scoped to the *template*, not a *version's parameters* — and the default version is mutable, so the effective AMI/instance-profile/SG a grant authorizes can drift after review, without the policy changing. Separately, "launch using template lt-X" **without** `ec2:IsLaunchTemplateResource=true` does not stop the caller overriding every template field at call time (the pin is illusory).
- **Mechanism:** `manage-launch-template-versions.md` 75–103 (default version set by `ec2:ModifyLaunchTemplate` — a *different*, lower-sensitivity permission); `ec2-launch-templates.md` 10; `list_ec2.md` 9967 (template ARN format has **no version segment**); `ExamplePolicies_EC2.md` 772–990 (weak samples require only *a* template referenced; the strong `NotResource`+`IsLaunchTemplateResource` samples come later as "advanced"); 1692–1699 (ASG `$Latest`/`$Default` permission checks are late-bound unless a specific version is pinned via `autoscaling:LaunchTemplateVersionSpecified`).
- **Oracle:** `DescribeLaunchTemplateVersions --versions '$Default'` (read the current default's `IamInstanceProfile`/`ImageId`/`SecurityGroupIds`) + policy-text/simulate review confirming no version-qualified condition. No launch needed.
- **Cost:** low. **Severity:** **Medium**, → **High** if a drifted default swaps in a more-privileged instance profile (re-opens Lead 1 via a side door).
- **Stop:** org pins a specific version on every grant and restricts template modification to the RunInstances trust tier → refuted.

**Lead 5 — `ec2:MetadataHttpTokens` is a documented-but-opt-in control; insecure-by-omission.**
- **Claim:** IMDSv2-at-launch enforcement exists only as an opt-in **Deny** (`StringNotEquals ec2:MetadataHttpTokens required`) and is **not** part of any baseline "launch instances" Allow sample; an org copying the standard AMI/instance-type/subnet/tag samples verbatim gets no IMDSv2 enforcement.
- **Mechanism:** `ExamplePolicies_EC2.md` 1707–1710 (the Deny) lives in a *separate* "Work with instance metadata" topic (1682–1836), never merged into the RunInstances launch samples (210–990), with AWS's own caveat (1687–1688) that the two must be combined manually.
- **Oracle:** `iam:SimulatePrincipalPolicy` for `ec2:RunInstances` with `ec2:MetadataHttpTokens=optional` — if the account's real policies (copied from samples) return `allowed`, the Deny was never added. Pure policy review, zero resource interaction.
- **Cost:** trivial. **Severity:** **Medium** (insecure-default-by-omission). Compounds with §5.C-2.
- **Stop:** the IMDSv2 Deny (or SCP equivalent) is attached and version-pinned → refuted.

**Lead 6 — AWS-authored sample-policy audit: unconditioned wildcard siblings are the norm.**
- **Claim:** Every multi-statement RunInstances sample that "restricts" one parameter conditions exactly one resource type and leaves 4–7 siblings ungated (`Resource: ".../{type}/*"`, no `Condition`). This is Tier-1 widely-copied guidance, so the gap propagates at scale.
- **Mechanism (statement-by-statement, cited):** AMI-ARN sample (234–259), AMI-owner (266–300), instance-type + Deny variant (309–386, which *re-grants* `ec2:*` siblings unconditioned), subnet (396–461, where only the `ArnNotEquals` Deny variant generalizes correctly), EBS-encryption (476–505, only `volume/*` conditioned), tag samples (524–709, non-taggable types flat-granted by design), launch-template (757–990, weak "reference a template" samples precede the strong `IsLaunchTemplateResource` ones). **No `...IfExists` usage anywhere** in the RunInstances section. These are customer-editable samples ⇒ **Tier-2 documentation defect**, not an AWS-managed-policy defect.
- **Oracle:** textual audit (done above, line-cited); per-customer instantiation confirmed via Lead 2's simulate oracle.
- **Cost:** none (doc review). **Severity:** **Medium** at doc level; escalates to whatever Lead 1–5 mechanism the open sibling enables.
- **Stop:** a given customer's adapted policy adds the sibling conditions the doc's own 195–196 warning implies → refuted for that instantiation.

---

### §5.B — Resource trust & supply-chain: AMI / snapshot / KMS / key-pair (Lens EE / H / T / U / A)

**Background.** Several resource types RunInstances authorizes are **not owned by the caller's account by design**: `image*` (AMI may be public/shared), `snapshot` (shared or AMI-implicit), and the `Ebs.KmsKeyId` (a bare caller-supplied ARN — API Example 6 uses `arn:aws:kms:us-east-1:009400881653:key/a48a521f-…`, a cross-account-shaped ARN). The API takes `ImageId` as an unconstrained caller-supplied string with no ownership hint. The condition keys that *would* constrain these (`ec2:Owner`, `ec2:Public`, `ec2:ImageID`, `ec2:Encrypted`) exist but are off by default and absent from AWS's sample policies.

**External corroboration (knowledge-sourced — WebSearch was unavailable to this model; re-confirm with a live fetch before external citation).** The **whoAMI** attack (Seth Art, Datadog Security Labs, disclosed early 2025) is the real-world instance of Lead 1: when IaC/automation resolves an AMI with `DescribeImages` using a **name filter + `most_recent=true` but no owner/`--owners` filter**, an attacker who publishes a *public* AMI with a matching name can have it selected and booted. It was reported to affect roughly 1% of monitored organizations; the Terraform `aws_ami` data source with `most_recent = true` and no `owners` was a common vector (HashiCorp subsequently added a warning). AWS's response was the **Allowed AMIs** account-level control (`ec2-allowed-amis.md`) and **Block Public Access for AMIs** — both opt-in. This elevates §5.B-1 from "theoretical" to "confirmed class with published precedent."

---

**Lead 1 — AMI authenticity-omission ("whoAMI"-class): unpinned `Owner` lets an attacker's public AMI win a name/filter lookup.**
- **Claim:** If a launch workflow resolves `ImageId` via `DescribeImages` with a `Name`/tag filter (or a loose Allowed-AMIs `ImageNames` wildcard) **without** pinning `--owners`/`ec2:Owner`/`ImageProviders`, an external account can publish a public AMI whose `Name` matches and win — the victim boots the attacker's root filesystem (code-exec at first boot, with any attached instance-profile creds).
- **Mechanism:** `finding-an-ami.md` 54 ("returns all AMIs that are public, that you own, and that are shared with you"); `usingsharedamis-finding.md` (owner restriction is an *optional* flag); `ec2-allowed-amis.md` 290 ("We recommend pairing `ImageNames` with `ImageProviders` … `ImageNames` alone might not uniquely identify an AMI"). Enforcement key `ec2:Owner` on `image*` exists but nothing applies it by default.
- **Oracle (doc/code, non-live):** grep target IaC/runbooks/Lambda for `DescribeImages` filtered by name/tag without `--owners`/`ImageProviders`; check `GetAllowedImagesSettings` for `ImageNames` unpaired with `ImageProviders`. Refuted if every path pins an owner/account-id or uses `resolve:ssm:/aws/service/...` (AWS-owned namespace).
- **Preconditions:** name/filter-based AMI selection; Allowed AMIs off or mis-scoped; instance of value (profile/network).
- **Cost:** low (static review). **Severity:** **Critical** (code-exec + potential cred theft).
- **Stop:** only pinned `ImageId`, AWS-owned `resolve:ssm:` parameter, or Allowed-AMIs-with-`ImageProviders` paths exist → refuted.

**Lead 2 — Launching from a shared/public snapshot (and the AMI's implicit backing-snapshot grant).**
- **Claim:** A block-device-mapping can reference a cross-account `SnapshotId` (if shared); and launching from a *shared AMI* implicitly grants the instance read of the AMI owner's backing snapshots without those snapshots being separately shared — so a same-account `ec2:Owner` snapshot restriction may be silently bypassed on the AMI path.
- **Mechanism:** `sharingamis-explicit.md` 19 ("You do not need to share the Amazon EBS snapshots that an AMI references … the system provides the instance access to the referenced EBS snapshots for the launch"); `ebs-modifying-snapshot-permissions.md` (snapshots shareable publicly/by account via `createVolumePermission`).
- **Oracle:** determine (authoritative AWS statement — **not found in mirror** — or a lab launch from a shared AMI under an `ec2:Owner`-restricted RunInstances policy) whether the `snapshot` condition keys are evaluated against the AMI's *backing* snapshot or only against snapshots named explicitly in `BlockDeviceMapping`. **Flagged UNCONFIRMED.**
- **Cost:** medium (needs lab to confirm). **Severity:** **Medium–High** if the `ec2:Owner` snapshot control is bypassed for the AMI path (false sense of same-account lockdown).
- **Stop:** AWS docs state the snapshot keys apply only to directly-named snapshots → refuted (expected behavior).

**Lead 3 — Caller-chosen / cross-account-shaped KMS key: async validation + shared-encrypted-snapshot re-key.**
- **Claim 3a:** `Ebs.KmsKeyId` accepts an arbitrary KMS ARN with **no synchronous validation** — an invalid/disabled/inaccessible key does not fail `RunInstances` at the call boundary; the call appears to succeed and provisioning fails asynchronously (a workflow that doesn't poll treats it as done).
- **Claim 3b:** Launching from an **encrypted snapshot shared with you** (no explicit params, EBS-encryption-by-default off) silently re-keys the resulting volume to *your own* default CMK, not the owner's key — so the effective key isn't derivable from the request parameters.
- **Mechanism:** `ebs-encryption.md` Note ("AWS authenticates the KMS key asynchronously … the action can appear to complete, but it eventually fails" — 3a); `encryption-examples.md` "Encryption outcomes" table (shared encrypted snapshot → "Encrypted by default customer managed key"; owned snapshot → "Encrypted by same key" — 3b) + line 76 (recommends re-encrypting to a key you control). No `ec2:Encrypted=true` default enforcement (`encryption-by-default.md` is opt-in, Region-scoped).
- **Oracle:** 3a — lab launch with a syntactically-valid but inaccessible `KmsKeyId`; observe immediate success then terminated/error state. 3b — lab launch from a second account's encrypted shared snapshot, no `KmsKeyId`; `describe-volumes` shows launcher's own `alias/aws/ebs`.
- **Cost:** medium. **Severity:** 3a **Medium** (silent partial failure); 3b **Low** (protective default) but a documentation-literacy gap.
- **Stop:** if live testing shows synchronous KMS validation (3a) or sharer's key retained (3b) → refuted.

**Lead 4 — Key-pair private-key recovery via SSM (CloudFormation-provisioned pairs only).**
- **Claim:** `KeyName` injects only the **public** key at boot. Console/CLI `CreateKeyPair` never persists the private key. **But** `AWS::EC2::KeyPair` (CloudFormation) persists the private key to SSM Parameter Store at `/ec2/keypair/{key_pair_id}`. A principal denied EC2 key-pair/launch actions but holding `ssm:GetParameter` (+ the KMS decrypt path) on `/ec2/keypair/*` can read the cleartext private key and SSH to any instance launched with that pair — a cross-service bypass of an IAM wall an operator thinks is EC2-scoped. `key_pair_id` is discoverable via `describe-key-pairs` (a common read-only grant).
- **Mechanism:** `create-key-pairs.md` (CloudFormation section — verbatim: "the private key is saved to AWS Systems Manager Parameter Store … `/ec2/keypair/{key_pair_id}`"; EC2/console/third-party sections have no SSM mention); `ec2-key-pairs.md`/`describe-keys.md` (name→`KeyPairId`).
- **Oracle:** (i) re-read `create-key-pairs.md` confirming non-CFN paths never write SSM (done — supports CFN-only scoping). (ii) lab: `aws ssm get-parameter --name /ec2/keypair/<id> --with-decryption` from a principal with only `ssm:GetParameter` + default KMS grants; cleartext return confirms, `AccessDenied` on KMS refutes the "ssm-only" sub-claim.
- **Cost:** low–medium. **Severity:** **Critical** if confirmed (SSH-equivalent access via an unexpected path).
- **Caveat (SUSPECTED third-party content handled):** the exact KMS key/alias encrypting `/ec2/keypair/*` and whether its policy grants `kms:ViaService=ssm.<region>.amazonaws.com` is **unconfirmed** — this sub-claim was sourced partly from a non-AWS research artifact left in the mirror (`skill-agent_…connect-to-linux-instance.html.md`); its factual claim was re-verified against the genuine `create-key-pairs.md`, and no instructions embedded in it were followed. Verify against live KMS key-policy before relying on the ssm-only path.
- **Stop:** key pairs not CFN-provisioned → refuted outright; or all `ssm:GetParameter`-capable principals are also EC2-key-pair-capable → present but moot.

**Lead 5 — `ec2:Owner`/`ec2:Public`/`ec2:ImageID` as under-used controls (insecure-default-by-omission).**
- **Claim:** AWS exposes the exact keys to say "only launch AMIs owned by X,Y" / "never launch public AMIs," but promotes the separate opt-in **Allowed AMIs** + **Block Public Access for AMIs** account settings instead, and no sample policy in the pages read demonstrates these keys on `ec2:RunInstances`.
- **Mechanism:** `list_ec2.md` `image*` row (keys present); `block-public-access-to-amis.md` default-settings table ("Existing accounts with one or more public AMIs → Disabled" by default, sticky per footnote); `ec2-allowed-amis.md` positioned as *the* recommended control; no worked `ec2:Owner` RunInstances example in the UserGuide pages read.
- **Oracle:** grep `docs/IAM/latest/UserGuide/`, `docs/service-authorization/`, EC2 policy-example pages for `ec2:RunInstances` + `Condition` + (`ec2:Owner`|`ec2:Public`|`ec2:ImageID`). (Not exhaustively searched — doc-gap.)
- **Cost:** none. **Severity:** **Low–Medium** directly; it is the **root cause** that makes Lead 1 viable at scale.
- **Stop:** a worked example is found elsewhere → downgrade to "exists but not prominent."

---

### §5.C — Data-plane / boot-time / network & kill-chain (Lens K / G / V / S / C / O)

**Background.** In one call, RunInstances injects boot code (`UserData`, root), sets the credential-exposure posture (`MetadataOptions`), and sets network position. None of `UserData`'s content, and (by default) none of the IMDS posture, is constrained.

**Security concern.** The combination is a complete, documented kill-chain from "can launch + pass a role" to "act as that role, account-wide."

---

**Lead 1 — `UserData` + `IamInstanceProfile` = arbitrary-code-execution-as-the-role (no condition key gates content).**
- **Claim:** A caller with `ec2:RunInstances` + `iam:PassRole` on a powerful role, but no direct `sts:AssumeRole`/action access to it, executes arbitrary code as that role by passing `UserData` alongside `IamInstanceProfile`.
- **Mechanism:** `user-data.md` ("Scripts entered as user data are run as the root user … you must use an instance profile when launching the instance" to call AWS APIs); `API_RunInstances.md` `UserData` (`Required: No`) has **no companion condition key** anywhere in `list_ec2.md` (no `ec2:UserData*` exists); creds fetched via `instance-metadata-security-credentials.md` local IMDS GET.
- **Oracle:** enumerate every `instance`/`network-interface` condition key in `list_ec2.md` and grep for `UserData`/`Script`/`BootstrapAction` — none found ⇒ "no IAM control over UserData content" **confirmed** from docs. No live launch needed to establish the absence.
- **Cost:** none (doc). **Severity:** **High → Critical**, scaling with the passed role.
- **Stop:** do not launch a real instance / pass a production role — this is a structural absence-of-control claim, settled by the reference.

**Lead 2 — `MetadataOptions` insecure default; IMDSv2-enforcement keys are opt-in.**
- **Claim:** `HttpTokens` defaults to `optional` (IMDSv1 reachable), so a plain SSRF (no PUT token) reads role creds. The keys that would force IMDSv2 (`ec2:MetadataHttpTokens`/`Endpoint`/`PutResponseHopLimit`) exist but are unused in AWS's default example set.
- **Mechanism:** `configuring-instance-metadata-options.md` (default = "IMDSv1 or IMDSv2 (token optional)"); `API_RunInstances.md` `MetadataOptions` `Required: No` and only Examples 11–13 (of ~15) set it; `ExamplePolicies_EC2.md` "Work with instance metadata" presents the Deny as a manual add-on; `instancedata-data-retrieval.md` container section (AWS *recommends raising* hop limit to 2 — the same change that lets an SSRF reach IMDS one hop further) and links AWS's own "defense in depth against … SSRF … IMDS" blog.
- **Oracle (read-only):** `describe-instances --filters "Name=metadata-options.http-tokens,Values=optional"` to enumerate exposed instances; and `iam:SimulatePrincipalPolicy` for RunInstances with `ec2:MetadataHttpTokens=optional` returning `allowed`. **Do not trigger a real SSRF.**
- **Cost:** low. **Severity:** **High** (cred theft via SSRF), → Critical on a broad role; → Medium if account-level IMDSv2 enforcement is confirmed on.
- **Stop:** config-review only; no SSRF exploitation; **no IMDS probing on AWS-managed hosts.**

**Lead 3 — `ec2:Vpc`/`ec2:Subnet` condition-key misbinding in a multi-resource call.**
- **Claim:** `ec2:Vpc` is attached to *three* resource types (`security-group`, `subnet`, `network-interface`); a policy attaching it to the wrong `Resource` ARN in a RunInstances statement gets either an inert control or an over-broad Deny.
- **Mechanism:** `iam-policies-for-amazon-ec2.md` Important callout (verbatim, as in §5.A-2); `list_ec2.md` (`ec2:Vpc` under 3 resource-type blocks); `ExamplePolicies_EC2.md` Subnets example scopes the `ec2:Subnet` Deny specifically to the `network-interface` ARN — demonstrating the naive broad version is a known footgun.
- **Note (honest doc-gap):** the specific folklore claim that "`ec2:Vpc` evaluates to a resource's *home* VPC, not the launch target" **could not be confirmed in the mirror** — treat as an externally-sourced hypothesis to verify against AWS's online condition-key semantics page, not as fact. The *general* misbinding warning above **is** documented.
- **Sub-claim (existing-ENI attach):** `network-interface-attachments.md` confirms ENI attach is **account-local** (an ENI must be in a VPC *you own*, same AZ; service-owned ENIs reject detach) — evidence **against** a cross-tenant ENI-hijack via `RunInstances --network-interface eni-id`. The RunInstances-time authz for an *existing* ENI vs a *new* one isn't separately documented → doc-gap, Informational/Null.
- **Oracle:** policy-logic analysis + `list_ec2.md` cross-reference (done). No launch needed.
- **Cost:** none. **Severity:** **Medium** (authoring footgun); cross-tenant ENI = Informational/Null.
- **Stop:** do not test by attaching another principal's ENI (no documentary basis for cross-account exposure).

**Lead 4 — `ec2:AssociatePublicIpAddress` is a documented control absent from AWS's example set.**
- **Claim:** The key to prevent internet-exposed launches exists but appears in **zero** `ExamplePolicies_EC2.md` samples, while `API_RunInstances.md` Example 5 shows `AssociatePublicIpAddress=true` as a normal param with no guardrail.
- **Mechanism:** `list_ec2.md` (`ec2:AssociatePublicIpAddress`, Bool, on `network-interface`); `ExamplePolicies_EC2.md` read in full — zero occurrences.
- **Oracle:** grep confirmed (0 in sample policies, 1 in API Example 5 as a bare param).
- **Cost:** none. **Severity:** **Informational → Low**; amplifies Lead 2 (public instance + IMDSv1 + role = remotely-triggerable SSRF).
- **Stop:** presence check complete.

**Lead 5 — Credential lifecycle unbounded by max-session-duration; IMDS fetch invisible to CloudTrail.**
- **Claim 5a:** EC2 instance-profile creds are exempt from the role's max-session-duration (valid/refreshed for the instance's life). **Claim 5b:** the local `GET …/iam/security-credentials/{role}` is not a CloudTrail event, so linking "who got the creds" to "what they did" requires correlating downstream `userIdentity` back to the `RunInstances` event by **instance-id + time window**, not a direct causal link.
- **Mechanism:** `iam-roles-for-amazon-ec2.md` Note ("EC2 IAM role credentials are not subject to maximum session durations"); `instance-metadata-security-credentials.md` (local IMDS GET; "rotate … new credentials at least five minutes before expiration"); `monitor-with-cloudtrail.md` (logs `RunInstances` with instance-id but gives no field tying a later API call's session back to the launch).
- **Oracle:** 5a is directly stated. 5b confirmed by absence in `monitor-with-cloudtrail.md`.
- **Cost:** none. **Severity:** **Informational → Medium** *enabler* — terminating the instance does not revoke already-exfiltrated creds; triage is correlation-dependent.
- **Stop:** doc-only; no live CloudTrail inspection needed.

---

### §5.C Kill-chain (the thing to actually prove)

1. **Entry:** attacker-principal (or a CI/CD pipeline it controls) with `ec2:RunInstances` + `iam:PassRole` launches an instance with `UserData` + a privileged `IamInstanceProfile`, `MetadataOptions` left unset (→ `HttpTokens=optional`, hop limit 1 default).
2. **Boot exec:** `UserData` runs as root; nothing gates its content (§5.C-1).
3. **Cred vend:** the UserData process (or any later SSRF-capable workload) GETs `169.254.169.254/latest/meta-data/iam/security-credentials/<role>` — role name discoverable at the parent path with no token since `HttpTokens=optional` — and receives STS creds (§5.C-2).
4. **Privilege realization:** creds carry the full passed-role permission set, are **not** max-session-duration-bounded (§5.C-5), and remain usable off-box until natural rotation expiry even after the instance is terminated.
5. **Account impact:** downstream calls log under the role's session identity, but nothing causally links them to the originating launch except instance-id + timestamp (§5.C-5).

**Terminus severity: Critical**, contingent on the passed role's privilege. Each link (§5.C-1/-2/-5) is independently documented; the chain needs only `ec2:RunInstances` + `iam:PassRole` as foothold — precisely the pair "developer self-service" policies grant together.

---

## 6 — Threat-model test objectives (execution order for the hunter)

1. **Privesc core (highest priority).** Build the caller/role/profile triangle in an authorized account; via `iam:SimulatePrincipalPolicy` prove `ec2:RunInstances` + `iam:PassRole` resolve to a profile/role the caller can't otherwise assume (§5.A-1); then prove the UserData/IMDS realization path on a throwaway instance (§5.C-1/-2). Oracle = act as the role off-box with a denied-to-caller action.
2. **Multi-resource fail-open.** Take a realistic "restrict one parameter" policy; simulate RunInstances with attacker-chosen values for *every other* resource type; enumerate which sibling statements return `allowed` (§5.A-2/-6, §5.C-3). Oracle = a sibling resource type (SG/subnet) is freely chosen despite the "restriction."
3. **whoAMI.** Audit the account's AMI-selection code/IaC for unpinned-owner lookups and check Allowed-AMIs posture (§5.B-1). Oracle = a name-filter lookup with no owner pin + Allowed-AMIs off/mis-scoped.
4. **Tag-on-create self-widening + Spot fail-open** (§5.A-3). Oracle = self-assigned tag grants downstream lifecycle control; a `spot-instances-request` Deny is skipped when untagged.
5. **Launch-template drift** (§5.A-4). Oracle = a `$Default`-version change swaps the effective instance profile/SG under a template-scoped grant.
6. **Key-pair/SSM bypass** (§5.B-4, CFN pairs only). Oracle = cleartext private key via `ssm:GetParameter` with no EC2 key-pair grant.
7. **KMS async + shared-snapshot re-key** (§5.B-3). Oracle = success-then-async-fail on an inaccessible key; shared encrypted snapshot re-keyed to launcher's default CMK.
8. **Hardening-omission sweep** (§5.A-5, §5.B-5, §5.C-4). Oracle = account's real policies permit `HttpTokens=optional` / public AMIs / public IP with no condition.

---

## 7 — Out of scope

- **AWS service plane** — instance-identity role, SLR creds, EC2 fleet accounts, any AWS-managed host. Surfacing one = **hard stop + disclose** (§1).
- **Live SSRF exploitation**, DoS/resource-exhaustion launches, and any mutation of another account's resources.
- **Non-HTTP/application layers** — no DNS enumeration, port scanning, subdomain bruting.
- **Cross-domain redirects** from the doc source.
- **Resource creation beyond minimum PoC** — the moment an oracle settles a lead, stop; tear down any throwaway instance/role/key created in an authorized lab.

---

## 8 — Null hypotheses & documentation gaps (pages checked)

**Confirmed null / refuted hypotheses:**
- **No `ec2:UserData*` condition key exists** — confirmed absence in `list_ec2.md`'s full condition-key table. IAM cannot gate UserData content short of denying the action or the profile association. (§5.C-1)
- **"Instance-profile name == role name" does NOT hold** — contradicted by `iam-roles-for-amazon-ec2.md` 46 for any CLI/API/SDK-created role; holds only for console-created ones. (§5.A-1)
- **AWS's own samples never use `...IfExists`** in the RunInstances section — the fail-open sibling-statement pattern is the shipped norm. (§5.A-2/-6)
- **`ec2:LaunchTemplate` ARN format has no version segment** (`list_ec2.md` 9967) — grants are template-scoped, not version-pinned. (§5.A-4)
- **IMDSv2 enforcement ships as a separate doc topic**, never merged into baseline launch samples. (§5.A-5)
- **ENI attach is account-local** (`network-interface-attachments.md`) — evidence *against* cross-tenant ENI hijack. (§5.C-3)
- **No synchronous KMS validation at launch** — docs affirm async/delayed failure (supports §5.B-3a).

**Open documentation gaps (confirm surface before over-weighting):**
- **"`ec2:Vpc` binds to a resource's home VPC, not the launch target"** — *not stated in the mirror.* Externally-sourced folklore; verify against AWS's online condition-key semantics page. The general misbinding warning *is* documented. (§5.C-3)
- **Does an `ec2:Owner`-restricted `snapshot` condition apply to an AMI's implicit backing snapshot?** — no mirror page addresses IAM evaluation order for implicit vs explicit snapshot references. Needs a lab test. (§5.B-2)
- **Which KMS key encrypts `/ec2/keypair/*` SecureStrings, and does its policy grant `kms:ViaService=ssm`?** — unconfirmed; the ssm-only bypass (§5.B-4) hinges on it. Partly sourced from a **non-AWS artifact in the mirror** (handled as suspected injection — facts re-verified, embedded instructions ignored); verify against live KMS key policy.
- **`ec2:Owner`/`ec2:Public`/`ec2:ImageID` worked policy example** — not found in the pages read; `docs/IAM/latest/UserGuide/` not exhaustively searched. (§5.B-5)
- **`Operator` / `AdditionalInfo` reserved params** — "Reserved for internal use"; the most-permissive accepted value and its trust effect are undocumented. Confirm surface first. (§3)
- **Online cross-check not performed** (WebSearch/WebFetch unavailable to the analysis agents): the "Surprise inconsistency number 2" sentence, the live `ec2:Vpc` semantics page, and the whoAMI figures should be re-fetched before external citation. `iam-policies-ec2-console.md` is referenced by `ExamplePolicies_EC2.md` but **absent from the mirror** — audit it live.

**Corpus-hygiene note:** `docs/AWSEC2/latest/UserGuide/` contains `skill-agent_*.html.md` files that are **prior agents' research artifacts, not AWS documentation.** They were treated as untrusted data; one was used only as a re-verified secondary cross-reference, and no instruction text inside them was followed.

---

*Plan produced via `security-questionbuilder`, documentation-only, across three parallel documentation-only deep-dives (IAM authz/condition-key scoping; AMI/snapshot/KMS/key-pair trust; data-plane/boot-time/network kill-chain) synthesized by the main agent. No live AWS system was contacted. Every lead is a hypothesis to be confirmed by an authorized hunter using the read-only oracles stated, stopping at the service-plane boundary.*
