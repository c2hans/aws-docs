# attach-iam-role — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attach-iam-role.html` (online `.md` twin fetched 2026-10-15, verbatim); authoritative IAM data from `list_ec2.md` (Service Authorization Reference, fresh copy /tmp/list_ec2.md, read by offline grep). Status: documentation-derived hypotheses only; nothing tested against a live account.

> **Scope / relationship to siblings.** This is the **page-level, procedural-operations COMPLEMENT** of the parent plan `iam-roles-for-amazon-ec2-attack-research-plan.md` (same directory), which already **OWNS** the headline surface: `ReplaceIamInstanceProfileAssociation` in-place/no-reboot + over-broad `iam:PassRole` → attach-high-priv-role → harvest-IMDS-creds privesc (its §5A Critical), the refutation of the "Replace skips PassRole" myth (PassRole IS enforced on all 4 paths), the `ec2:InstanceProfile` (RunInstances) vs `ec2:NewInstanceProfile` (Associate/Replace) key-name split as an inert-Deny trap, `iam:AssociatedResourceArn` as the un-taught PassRole pin, IMDS creds bypassing `MaxSessionDuration`, and the §5B IMDS-enforcement + §5C SSM-DHMC confused-deputy surface. **This plan does NOT restate those — it cross-references them** and develops only the net-new granular surface that `attach-iam-role.html` itself introduces: the three CLI/API operation shapes (associate / replace / disassociate) driven by the **`iip-assoc-` AssociationId**, the **`DescribeIamInstanceProfileAssociations` read oracle**, the **console "Modify IAM role" single-button** that collapses three distinct API actions, the **inline "Create new IAM role" at-launch** console flow, and **credential-revocation completeness** on detach/replace. See [[project-iam-roles-for-amazon-ec2-plan-note]].

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- Policy-scoping leads settle **read-only** via `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (a condition key either applies to an action or it does not — no resource creation). Resolution/revocation/IMDS-timing leads are **live-only** → hand to `aws-vuln-hunter` with a synthetic two-instance, two-team canary.
- **DryRun is caller-IAM-only** (evaluated before resource resolution) — it is NOT an ownership/resolution oracle for the AssociationId→instance leads. Do not treat a DryRun pass as proof of cross-team reach.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. an IMDS cred that resolves to an AWS-fleet role, or an SSM identity role), stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives
Stated as concrete breach outcomes for the attach/replace/detach operations:
1. Using **only** `ec2:ReplaceIamInstanceProfileAssociation` (or `Disassociate`) scoped to one instance/team, mutate the IAM-role attachment of a **different team's instance** in the same account by naming its `iip-assoc-` AssociationId.
2. Enumerate **every** instance→role attachment in the account (instance-id, `iip-assoc-` id, instance-profile ARN) from a principal that cannot `DescribeInstances` or read the target instances' tags — i.e. prove `DescribeIamInstanceProfileAssociations` is an unscopable account-wide recon oracle.
3. Reproduce a console "Modify IAM role" operation (attach/replace/detach) and determine the exact minimal API+PassRole permission set, exposing any delta between what the console implies and what the API enforces.
4. Via the inline "Create new IAM role" at-launch flow, create a role + same-named instance profile and determine whether the predictable instance-profile name is pre-claimable/collidable, and whether the AWS-sample managed-policy steer over-grants.
5. After `Disassociate`/`Replace`, prove whether already-vended IMDS role credentials for the old profile remain usable (revocation-incompleteness).

## 2. Components, Assets, and Design
**Customer-facing interface.** EC2 control-plane API (SigV4), AWS CLI, PowerShell cmdlets, and the EC2 console "Instances → Actions → Security → Modify IAM role" route. No non-SDK/internal endpoint on this page.

**The four actions the page drives (all `ec2:*`, confirmed in `list_ec2.md`):**

| Operation | API action | CLI on page | Resource bound in IAM | Caller-supplied identifier |
|---|---|---|---|---|
| Attach (new/stopped/running, no existing role) | `AssociateIamInstanceProfile` | `associate-iam-instance-profile` | **`instance*`** | `--instance-id i-…` + profile Name/ARN |
| Replace (instance must be **running**) | `ReplaceIamInstanceProfileAssociation` | `replace-iam-instance-profile-association` | **`instance*`** | **`--association-id iip-assoc-…`** + new profile |
| Detach (running or stopped) | `DisassociateIamInstanceProfile` | `disassociate-iam-instance-profile` | **`instance*`** | **`--association-id iip-assoc-…`** |
| Enumerate | `DescribeIamInstanceProfileAssociations` | `describe-iam-instance-profile-associations` | **(blank — none)** | optional `--filters instance-id` |

**Resource identifiers / entropy.** Instance ARN `arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}`. The **association** is identified by `iip-assoc-` + 16 hex (`iip-assoc-0044d817db6c0a4ba`) ≈ 64-bit — **but there is NO `iam-instance-profile-association` resource type in `list_ec2`** (grep empty), so IAM never authorizes against the AssociationId; it authorizes against the **instance behind it**, which the service must resolve server-side. Instance profile named by ARN or bare Name.

**Identity / credential chain.** An attached instance profile → role → creds vended through IMDS (`/iam/security-credentials/<role>`), auto-rotated ~every 6h regardless of role `MaxSessionDuration` (parent §5A). This is the asset the attach/replace primitive delivers.

**Roles / privilege.** The attach operations themselves need `ec2:Associate|Replace|Disassociate…` + (where a role is passed) `iam:PassRole` on the role (parent-owned). The inline create-role console flow additionally implies `iam:CreateRole` + `iam:CreateInstanceProfile` + `iam:AddRoleToInstanceProfile` + the role's trust to `ec2.amazonaws.com`.

**Pipeline (console abstraction over three API actions):**
```
Console "Modify IAM role" (one button)
        │  current state decides which API fires:
        ├─ no role attached → AssociateIamInstanceProfile      (instance running|stopped)
        ├─ role attached, pick different → ReplaceIamInstanceProfileAssociation (instance MUST be running)
        └─ "No IAM Role" → DisassociateIamInstanceProfile       (running|stopped)
                           │
                 resolve iip-assoc- ──► instance ──► IAM authz on instance ARN + tags + PassRole
                           │
                 instance profile swap in-place (NO reboot) ──► IMDS vends new role creds (~6h rotation)
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller scoped to instance tag/team A | Instance of team B (same account) | `Replace`/`Disassociate` naming B's `iip-assoc-` id; IAM resolves to instance ARN | B's role attachment mutated / removed under a policy that intended only team-A instances = intra-account cross-team breach (least-priv footgun → higher if the resolution skips the instance tag check) |
| Low-recon caller (no `DescribeInstances`, no tag read) | Every instance→role mapping in account | `DescribeIamInstanceProfileAssociations` (no resource type, only `ec2:Region`) | A returned list of foreign `(instance-id, iip-assoc-, instance-profile ARN, state)` the caller could not read via `DescribeInstances` = unscopable recon oracle |
| Caller holding only `ec2:Associate…` (not Replace) | A console-equivalent replace | console "Modify IAM role" button mapping | Button performs an action the caller's single API grant did not cover, or vice-versa = doc-vs-API authorization delta |
| App on instance that already read IMDS creds | Old role after `Disassociate`/`Replace` | IMDS cred caching / rotation window | Old-profile creds still authenticate after detach/replace = revocation-incompleteness |
| Any customer surface | AWS service plane | IMDS cred resolving to an AWS-fleet/SSM identity role | **HARD STOP** — preserve, disclose |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `AssociateIamInstanceProfile` | SigV4/CLI | Existing | **Yes** | Yes | holders of `ec2:AssociateIamInstanceProfile` on the instance + `iam:PassRole` on role | binds `instance*`; carries `ec2:NewInstanceProfile` + `ec2:InstanceProfile` + full instance-attribute/IMDS key set + `aws:ResourceTag`/`ec2:ResourceTag` |
| `ReplaceIamInstanceProfileAssociation` | SigV4/CLI | Existing | **Yes** | Yes | holders of the action on the instance + PassRole | **named by `iip-assoc-`**; **instance must be running**; in-place no-reboot (parent §5A Critical); same condition-key set incl. `ec2:NewInstanceProfile` |
| `DisassociateIamInstanceProfile` | SigV4/CLI | Existing | **Yes** | Yes | holders of the action on the instance | **named by `iip-assoc-`**; `ec2:NewInstanceProfile` **absent** (nothing attached); `ec2:InstanceProfile` present (current) |
| `DescribeIamInstanceProfileAssociations` | SigV4/CLI | Existing | No (List) | Yes | **any holder of `ec2:DescribeIamInstanceProfileAssociations`** | **blank resource type + only `ec2:Region`** → unscopable; the recon primitive feeding the `iip-assoc-` ids to Replace/Disassociate |

Console route: **Instances → Actions → Security → Modify IAM role → Update IAM role** collapses associate/replace/detach into one UI gesture (state-dependent). Inline **"Create new IAM role"** form at launch (Advanced details → IAM instance profile) mints role+profile.

## 5. Recommended Areas of Focus

### Area 1 — The `iip-assoc-` AssociationId indirection: authz anchors to the instance, not the id the caller names (Lens A / X / S)
**Background.** `Replace` and `Disassociate` are invoked by **AssociationId** (`--association-id iip-assoc-0044d817db6c0a4ba`, both CLI examples on the page), yet `list_ec2` binds both to the **`instance*`** resource type with `aws:ResourceTag`/`ec2:ResourceTag` support and **no `iam-instance-profile-association` resource type exists**. So the service must resolve `iip-assoc-` → instance, then authorize against the instance ARN + its tags. This is the classic "two ways to name one resource, authz checks the resolved one" shape — the question is whether the resolution-then-tag-check actually holds for a caller scoped to a *different* instance.
**Security Concern.** A policy that scopes these write actions by instance tag (the documented ABAC pattern) is only as strong as the server-side `iip-assoc-`→instance resolution happening **before** the tag condition is evaluated. If resolution is correct, cross-team mutation is blocked (expected). The residual risk is intra-account: a caller granted `Replace`/`Disassociate` on `Resource:"*"` (or any instances lacking the scoping tag) can mutate/strip the role attachment of a high-value instance whose `iip-assoc-` they learned from Area 2 — turning Replace into the parent's privesc primitive against instances the operator never intended, and Disassociate into a targeted credential-denial (DoS) primitive.
**High-level Test Scenarios.**
- **Claim:** a principal whose policy allows `ec2:ReplaceIamInstanceProfileAssociation` only on `ec2:ResourceTag/team = A` can still replace the profile on a `team=B` instance by passing B's `iip-assoc-`. → **Oracle:** `iam:SimulateCustomPolicy` with the scoped policy + the B-instance ARN as `ResourceArns` and the `team=B` context key → expect **implicitDeny**; a live `replace-iam-instance-profile-association` returning 200 against B's `iip-assoc-` under that scoped role **refutes** correct resolution (needs two-instance canary). Severity-if-true: High (cross-team role swap → privesc per parent §5A).
- **Claim:** `Disassociate` naming a foreign `iip-assoc-` strips the victim instance's role (credential-denial DoS) even though no instance-id is supplied by the caller. → **Oracle:** scoped-role live `disassociate-iam-instance-profile --association-id <foreign>` → 200 = breach; `AccessDenied` = resolution enforced.
- **Claim (null guard):** cross-**account** IDOR via `iip-assoc-` is foreclosed — the id is account-scoped and 64-bit (not fabricable), so this is intra-account only. State it, don't chase cross-account.
**Doc evidence.** Page CLI blocks for replace/detach (`--association-id iip-assoc-…`); `list_ec2.md:9407/7921` (`instance*` + ResourceTag keys); absence of any `*-association` resource type (grep). **Severity-if-true:** High (intra-account cross-team privesc / DoS); the mechanism is parent-owned, the **AssociationId-resolution gap is this plan's net-new angle.**

### Area 2 — `DescribeIamInstanceProfileAssociations` is an unscopable account-wide recon oracle (Lens A / U)
**Background.** `list_ec2.md:6870` gives this List action a **blank resource-type cell and only `ec2:Region`** — no `instance`/`instance-profile` resource type, no `aws:ResourceTag`/`ec2:ResourceTag`, no ARN scoping of any kind.
**Security Concern.** A principal holding just this one action can enumerate **every instance→instance-profile association in the account/region** — instance-id, the `iip-assoc-` AssociationId, the attached instance-profile ARN, and association state — with **no way for an admin to tag- or ARN-scope it**. This is the recon layer that makes Area 1 and the parent's Replace-privesc *practical and targeted*: you do not need `DescribeInstances` or the target's tags; you dump associations, pick the instance-profile ARN with the fattest role, read off its `iip-assoc-`, and feed it to Replace/Disassociate. It is the exact inert-ABAC shape already catalogued in this corpus for `DescribeSpotFleetRequests` / `DescribeCapacityReservations` (see [[project-aws-research-plans]]).
**High-level Test Scenarios.**
- **Claim:** a `Deny` carrying `aws:ResourceTag`/`ec2:ResourceTag`/instance-ARN conditions cannot restrict `DescribeIamInstanceProfileAssociations` (the keys are inert — not in the action's supported set). → **Oracle:** `iam:SimulateCustomPolicy` for the action with those condition keys set → still **Allowed** (condition never evaluated) = confirmed unscopable; cross-check the SAR row shows only `ec2:Region`.
- **Claim:** the returned list discloses foreign-team instance-profile ARNs the caller cannot otherwise read. → **Oracle:** live `describe-iam-instance-profile-associations` under a role denied `ec2:DescribeInstances`, returning other teams' associations.
- Chain pointer: output `iip-assoc-` ids feed **Area 1** and parent §5A.
**Doc evidence.** `list_ec2.md:6870` (blank resource + `ec2:Region` only); page uses it as step 1 of both replace and detach. **Severity-if-true:** Medium (account-wide recon enabler; raises the practicality/severity of the privesc chain it feeds).

### Area 3 — Console "Modify IAM role" collapses three distinct API actions → doc-vs-API authorization delta (Lens U)
**Background.** The console presents one gesture — **Actions → Security → Modify IAM role → Update IAM role** — that performs attach, replace, OR detach depending on the instance's current state. The page never states which IAM action(s) or `iam:PassRole` each gesture requires, nor that "change to a different role" is a **Replace that requires the instance to be running** while "No IAM Role" is a Disassociate.
**Security Concern.** The console abstraction hides a three-action authorization surface. Two concrete gaps: (a) an operator granted only `ec2:AssociateIamInstanceProfile` (common "allow attaching a role" intent) **cannot** change an already-attached role (that is `ReplaceIamInstanceProfileAssociation`) nor remove one (`Disassociate`) — a least-privilege-mapping confusion that pushes admins toward granting all three; (b) conversely, granting the console workflow broadly hands the caller the **Replace** primitive that the parent §5A shows is the privesc lever. The doc gives no permission matrix, so the operator cannot reason about least privilege for the button.
**High-level Test Scenarios.**
- **Claim:** the console "Update IAM role" to a *different* role fails for a principal lacking `ec2:ReplaceIamInstanceProfileAssociation` even though it holds `ec2:AssociateIamInstanceProfile`. → **Oracle:** `iam:SimulatePrincipalPolicy` for each of the three actions under the candidate policy; live console attempt corroborates. Documents the exact minimal set.
- **Claim:** "Modify IAM role" to a different role is silently a Replace and therefore **requires the instance running** — a stopped-instance role change via the console path fails where attach would have succeeded. → **Oracle:** doc comparison (page: "To replace the IAM role … the instance must be running") vs the single-button UX; live console on a stopped instance.
**Doc evidence.** Page "To replace an IAM role for an instance … the instance must be running"; three identical console step-lists all ending in "Modify IAM role"/"Update IAM role". **Severity-if-true:** Low–Medium (least-privilege mapping / doc-clarity; enabler for over-granting the Replace privesc).

### Area 4 — Inline "Create new IAM role" at launch: predictable same-named instance profile + AWS-sample policy steer (Lens R / EE / E)
**Background.** The console's at-launch flow (Advanced details → IAM instance profile → **Create new IAM role**) mints a role, **auto-creates an instance profile with the same name as the role**, reviews a trust policy allowing `ec2.amazonaws.com`, and the page's worked example attaches **`AmazonS3ReadOnlyAccess`** ("to grant S3 access, select the `AmazonS3ReadOnlyAccess` managed policy").
**Security Concern.** Three sub-leads: (a) **EE land-grab / name coupling** — the instance-profile name is deterministically the role name. If an instance profile of that name already exists (or an attacker pre-creates one), does the flow collide, adopt, or overwrite? A pre-existing attacker-influenced instance profile of a predictable name being adopted would couple the launched instance to an unintended role container. (b) **Lens R insecure-default steer** — the AWS-authored example steers the reader to `AmazonS3ReadOnlyAccess`, which is **account-wide S3 read** (`s3:Get*`/`List*` on `*`), presented as the canonical "grant S3 access" starting point rather than a scoped inline policy; a copy-verbatim reader over-grants the instance role. (c) the flow bundles `iam:CreateRole` + `iam:CreateInstanceProfile` + `iam:AddRoleToInstanceProfile` + `iam:PassRole` + `ec2:RunInstances` behind one console step — a principal who can do all of this at launch can mint and pass a role in one gesture (parent §5A privesc, create-side).
**High-level Test Scenarios.**
- **Claim:** creating a new role via the inline flow when an instance profile of that name pre-exists adopts/overwrites rather than failing. → **Oracle:** live — pre-create `iam create-instance-profile --instance-profile-name EC2-S3-Access-Role`, then run the inline flow with that role name; observe collision behavior. Severity-if-true: Medium (resource-adoption / confused coupling).
- **Claim:** the `AmazonS3ReadOnlyAccess` steer yields an account-wide-S3-read instance role as the documented default. → **Oracle:** resolve `arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess` via `iam:GetPolicyVersion`; confirm `Resource:"*"`. This is an **AWS-authored doc sample** → Lens R Tier-2 (over-broad default), reportable not a customer footgun.
- **Claim:** the trust policy minted allows `ec2.amazonaws.com` with no `aws:SourceArn`/`aws:SourceAccount` confused-deputy guard. → **Oracle:** inspect the generated trust policy; note absence of the condition keys the parent §5C flags.
**Doc evidence.** Page "Creating and attaching an IAM role during instance launch (Recommended)" steps; Note "an instance profile with the same name as the role is automatically created"; example `AmazonS3ReadOnlyAccess`. **Severity-if-true:** Medium (over-broad AWS-sample default; predictable-name adoption); defers the PassRole/privesc core to parent §5A.

### Area 5 — Detach / Replace do not necessarily revoke already-vended IMDS credentials (Lens C / AA / O)
**Background.** The page sells Replace as interruption-free ("API actions performed by applications running on the instance are not interrupted") and allows Detach on a running instance. Parent §5A notes IMDS vends role creds on a **~6h rotation independent of `MaxSessionDuration`**.
**Security Concern.** If an application on the instance has already fetched role credentials from IMDS, `Disassociate` (or `Replace` swapping to a lower-priv role) may **not** invalidate those cached creds until their natural expiry — so "detaching the role" is not a credential **revocation**. An operator responding to a compromise by detaching the role could believe access is cut while the attacker's already-exfiltrated creds remain valid for up to the rotation/expiry window. Replace's "no interruption" guarantee implies the old creds remain usable across the swap.
**High-level Test Scenarios.**
- **Claim:** credentials read from IMDS before `Disassociate` continue to authenticate (e.g. `sts:GetCallerIdentity`, a scoped `s3:ListBucket`) after the association is removed, until their documented expiry. → **Oracle:** live — fetch creds via IMDS, `disassociate-iam-instance-profile`, then use the creds off-instance; success after detach = revocation-incompleteness. Severity-if-true: Medium (incident-response gap; creds survive the "cut").
- **Claim:** after `Replace` to role B, role A's previously-vended creds still work until expiry (the "no interruption" guarantee as a non-revocation). → **Oracle:** same pattern, swap instead of detach.
- Lens O corollary: is the detach/replace event itself (and the old-cred usage after it) distinguishable in CloudTrail, or does the old cred's continued use look like normal pre-detach activity?
**Doc evidence.** Page: "ensure that API actions … are not interrupted" (replace); detach allowed on running instance; parent §5A IMDS rotation note. **Severity-if-true:** Medium (revocation completeness; live-only). **Note:** IMDS-on-managed-host specifics are the customer's instance — in scope only as a documented-guarantee-vs-enforcement gap, not as an AWS-fleet reach.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-team role swap via foreign `iip-assoc-` | `ReplaceIamInstanceProfileAssociation` | server-side `iip-assoc-`→instance resolution + instance-tag ABAC (Area 1) |
| Account-wide association enumeration | `DescribeIamInstanceProfileAssociations` | **none** — only `ec2:Region` (Area 2) |
| Over-granting via console abstraction | console "Modify IAM role" | undocumented 3-action permission mapping (Area 3) |
| Predictable instance-profile name adoption / sample over-grant | inline Create-new-role at launch | same-name auto-create; `AmazonS3ReadOnlyAccess` steer (Area 4) |
| Creds survive detach/replace | IMDS cred cache + Disassociate/Replace | "not interrupted" guarantee ≠ revocation (Area 5) |
| High-priv role attach → IMDS cred harvest | all write actions + `iam:PassRole` | **parent §5A (Critical) — not restated here** |

## 7. Out-of-Scope Risk Categories
- The **PassRole privesc core, `iam:AssociatedResourceArn` pin, `ec2:InstanceProfile` vs `ec2:NewInstanceProfile` inert-Deny trap, IMDSv2 enforcement, and SSM-DHMC confused-deputy** — owned by the parent plan (`iam-roles-for-amazon-ec2`); cross-ref, do not duplicate.
- **Cross-account IDOR via `iip-assoc-`** — foreclosed (account-scoped, 64-bit non-fabricable id). Null, stated.
- **IMDS on fully-managed hosts** as an AWS-fleet reach — out of scope except Area 5's documented-guarantee-vs-enforcement framing; any IMDS cred resolving to an **AWS service-plane** role is a **HARD STOP**, not a lead to pursue.
- Single-tenant self-DoS (detaching your own instance's role), product/feature-parity gaps, console UX bugs with no authorization consequence.
- Customer-authored scoped policies that over-grant (least-priv footgun) — in scope **only** where the artifact is AWS-authored (Area 4's `AmazonS3ReadOnlyAccess` sample steer).

## 8. Null hypotheses / doc gaps
- **Lens B/C (PassRole / vending):** fires but **parent-owned** — not re-run here. The attach actions do accept a role indirectly (via the instance profile); PassRole enforcement is parent §5A.
- **Lens G (SSRF):** N/A — read `attach-iam-role.html` in full; no field the service dereferences (all inputs are identifiers: instance-id, `iip-assoc-`, instance-profile Name/ARN — none fetched as a URL).
- **Lens Q (upload):** N/A — no blob/file/image field on this page.
- **Lens F (injection), W (attestation), BB/CC/DD (edge/cache/upstream-context), FF (JWT):** N/A — no translation layer, no attestation gate, no multi-parser edge path, no token validation on this page.
- **Lens H (KMS):** N/A on this page (instance profiles carry no CMK field here).
- **Lens P (proofing):** N/A — no registration/OTP/uniqueness gate; the "running-instance required for Replace" precondition is a state gate, covered under Area 3, not an identity-proofing gate.
- **Doc-gaps to confirm live first:** (1) exact server-side `iip-assoc-`→instance resolution ordering vs the instance-tag condition (Area 1 — DryRun cannot answer, needs canary); (2) inline-create-role behavior on a pre-existing same-named instance profile (Area 4); (3) IMDS cred lifetime after detach/replace (Area 5). All three are **live-only**; `iam:SimulateCustomPolicy` settles only the static scopability of Areas 1–3's policy claims.

---
*Cross-references:* [[project-iam-roles-for-amazon-ec2-plan-note]] (parent — PassRole/IMDS/SSM headline surface), [[project-aws-research-plans]] (unscopable-Describe-oracle pattern; `list_ec2`-over-prose rule), [[reference-aws-iam-service-auth-ref-url]].
