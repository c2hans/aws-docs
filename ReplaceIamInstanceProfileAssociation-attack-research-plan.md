# EC2 `ReplaceIamInstanceProfileAssociation` (IAM Instance Profile Association family) — Attack Research Plan

**Source of leads:**
- Target page: `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceIamInstanceProfileAssociation_section.html` (mirror: `docs/ec2/latest/devguide/example_ec2_ReplaceIamInstanceProfileAssociation_section.md`) — online fetch confirmed byte-identical to mirror, no sync drift.
- API refs: `docs/AWSEC2/latest/APIReference/API_{ReplaceIamInstanceProfileAssociation,AssociateIamInstanceProfile,DisassociateIamInstanceProfile,DescribeIamInstanceProfileAssociations,IamInstanceProfileAssociation,IamInstanceProfileSpecification,IamInstanceProfile}.md`, `CommonErrors.md`
- IAM/EC2 user guide: `docs/AWSEC2/latest/UserGuide/{permission-to-pass-iam-roles,iam-roles-for-amazon-ec2,iam-policies-for-amazon-ec2,ExamplePolicies_EC2,instance-metadata-security-credentials,instancedata-data-retrieval,configuring-instance-metadata-options,monitor-with-cloudtrail,attach-iam-role}.md`
- Authorization reference: `docs/service-authorization/latest/reference/list_ec2.md` (**action-with-resources** table rows ~4749 Associate / ~7915 Disassociate / ~9401 Replace / ~6864 Describe; condition-key defs ~10096/10117; `instance` resource type ~9949)
- Cross-service example: `docs/ec2/latest/devguide/example_cross_ResilientService_section.md` (+ `code-library/.../ec2_example_cross_ResilientService_section.md`)
- IAM: `docs/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md`, `troubleshoot_iam-ec2.md`

**Status:** documentation-derived hypotheses only. **Nothing has been tested against a live AWS account.** Each item is a boundary that *might not hold* plus the exact observation that would settle it.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5). Look left and right for adjacent bugs.
- This API family is, by design, a **privilege-management primitive inside a single customer account.** The dominant risk class is **intra-account IAM privilege escalation**, not cross-tenant isolation (instance-profile associations are account-local). Headline question: *"can an identity obtain credentials it was never granted by swapping the role an instance presents to IMDS?"*
- **Safe-oracle discipline for a hunter:** the first oracle for every IAM-scoping lead is **`iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`** (touches no resources). Escalate to a live scoped call only with synthetic canary roles/instances you created, under a test principal holding *exactly* the policy under test — never the over-privileged tester identity.
- **HARD STOP / out of scope:** the moment any evidence shows an identity, credential, ARN, or account belonging to **AWS's own service plane** — e.g. the **instance-identity-role** path `arn:aws:iam::<acct>:assumed-role/aws:ec2-instance/<instance-id>`, a service-linked-role credential, or an AWS-owned fleet account — **stop, preserve evidence, flag for AWS-Security disclosure.** Do not probe IMDS on AWS-managed hosts; do not reuse any discovered service-plane credential.
- A clean/negative result is a correct result. Confirm existence only; never escalate beyond existence-proof.

---

## 1. Pentest Objectives (concrete boundary-breach goals)

1. **Privilege escalation by profile swap.** From a principal holding `ec2:ReplaceIamInstanceProfileAssociation` (or `Associate…`) + a scoped `iam:PassRole`, obtain the credentials of a role **more privileged than the caller**, by attaching that role's instance profile to a reachable instance and reading the vended credentials from IMDS. **Breach = caller performs an AWS action its own identity denies, using instance-vended credentials for a role it was not granted.**
2. **PassRole / `ec2:NewInstanceProfile` scope break.** Attach a role the caller has no `iam:PassRole` for, or a profile an `ec2:NewInstanceProfile` condition should exclude — via the profile-name-vs-role-name indirection, a prefix/wildcard scope, a Name-vs-Arn inconsistency, or the condition key being accepted-but-not-enforced.
3. **Instance resource-scope fail-open.** `Replace`/`Disassociate` on an instance an `aws:ResourceTag`/`instance-ARN` policy was meant to exclude — proving the resource-level condition is not resolved from the opaque `AssociationId` before authz (account-wide blast radius).
4. **Replace-vs-Associate authorization parity.** Succeed via the single `Replace` call where the equivalent `Disassociate`+`Associate` pair would be denied (combined check looser than the AND of its halves).
5. **Credential persistence after revoke.** Credentials vended under the old profile remain valid for their full TTL after `Disassociate`/`Replace` (no server-side revocation).
6. **AWS-authored artifact / guidance defect.** The flagship sample policy grants materially more than needed despite AWS providing a precise control it omits (Tier-2 disclosure candidate — copied verbatim).

---

## 2. Components, Assets, and Design

**What the API does.** `ReplaceIamInstanceProfileAssociation` changes the IAM instance profile on a *running* instance **without first disassociating** the old one (API ref: *"change the IAM instance profile … without having to disassociate the existing IAM instance profile first"*). Siblings: `AssociateIamInstanceProfile` (attach to running/stopped instance; takes **InstanceId**), `DisassociateIamInstanceProfile` (detach; takes **AssociationId** only), `DescribeIamInstanceProfileAssociations` (list "your" associations).

**Inputs / identifier shapes.**
- `AssociationId` — opaque, shape `iip-assoc-<17 hex>` (e.g. `iip-assoc-08049da59357d598c`) — the standard post-2016 EC2 ~68-bit random resource-id family, no embedded ownership checksum; opacity is not an access-control boundary. Supplied to `Replace` and `Disassociate`. **Neither takes an InstanceId** — the authorization decision must resolve the association → instance internally.
- `IamInstanceProfile` = `IamInstanceProfileSpecification{ Name | Arn }` — profile named by **Name OR ARN** (two naming forms; `ec2:NewInstanceProfile` is ARN-typed, so a `Name` input must be resolved to an ARN before the condition can be evaluated).
- An **instance profile** is a container for exactly one IAM **role**; profile name and role name **can differ** (user guide, *Instance profiles*). `iam:PassRole` keys on the *role* name; the ec2 action and `ec2:(New)InstanceProfile` key on the *profile* ARN — a deliberate decoupling.

**The credential pathway (why this is sensitive).** After (re)association, the instance's **IMDS** (`169.254.169.254`, `/latest/meta-data/iam/security-credentials/<role>`) vends **temporary STS credentials for the new role**. Anything that can read IMDS on that instance (the workload, or an SSRF bug in it) then holds those credentials. **EC2 IAM-role credentials are explicitly NOT subject to the role's max-session-duration** (user guide Note). Removing a role from a profile has an **up-to-one-hour** propagation delay; credentials rotate on expiry, with **no documented push-revocation** on disassociate/replace.

**Trust zones (single customer account).**
- **Calling IAM principal** — bounded by its identity policy (`ec2:*InstanceProfile*`, `iam:PassRole`, and the condition keys below).
- **Role inside the attached profile** — its privileges become reachable via IMDS post-association.
- **EC2 service principal** `ec2.amazonaws.com` — the `iam:PassedToService` target.
- **AWS service plane** (instance-identity-role, SLRs, AWS fleet acct) — **out of scope / HARD STOP.**

```
caller principal ──(ec2:Replace… + iam:PassRole, gated by ec2:NewInstanceProfile / aws:ResourceTag)──▶ EC2 control plane
                                                                                                          │ attaches
                                                                                                          ▼
                                                              Instance Profile ─contains─▶ IAM Role (target privileges)
                                                                                                          │ vends creds via
                                                                                                          ▼
                 workload / SSRF on instance ──read──▶ IMDS 169.254.169.254  ──▶  STS temp creds for target role
                                                                                                          │
                                                                                                          ▼  (end of kill chain)
                                                                                      actions the caller's own identity denies
```

**Mandatory coverage sweep (pages opened):** all four API refs + three data types + `CommonErrors.md`; `permission-to-pass-iam-roles.md` (flagship sample, `Resource:"*"`); `ExamplePolicies_EC2.md` (tag-scoped sample + `TestRole-*`/`DevTeam*` prefix samples); `iam-roles-for-amazon-ec2.md` (resource-level claim, cred-TTL note, instance-identity-role); `iam-policies-for-amazon-ec2.md`; the authorization-reference action-with-resources + condition-key tables; the ResilientService example (all SDK tabs); IMDS + CloudTrail pages. **No** server-side-fetched URL field, upload/blob field, OAuth/3P link, translation layer, multi-tenant fleet, KMS key, or attestation gate appears in this surface (Section 8).

---

## 3. API / Interface Inventory

| Name | Mutating | Input id | Resource-level (confirmed from authz ref) | Key condition keys | PassRole | Notes |
|---|---|---|---|---|---|---|
| `ReplaceIamInstanceProfileAssociation` | **Yes** | `AssociationId` (+profile) | **`instance*` (required)** | `aws:ResourceTag`, `ec2:ResourceTag`, `ec2:InstanceProfile` (current), **`ec2:NewInstanceProfile` (being attached)** | **Required** (`iam:PassedToService=ec2.amazonaws.com`) | No InstanceId input → assoc→instance resolved internally for authz |
| `AssociateIamInstanceProfile` | **Yes** | `InstanceId` (+profile) | **`instance*` (required)** | same incl. `ec2:NewInstanceProfile` | **Required** | Write twin of Replace (takes InstanceId) — compare parity |
| `DisassociateIamInstanceProfile` | **Yes** | `AssociationId` | **`instance*` (required)** | same **minus `ec2:NewInstanceProfile`** (nothing attached) | **Not required** | Detach-only; no PassRole → role-strip DoS primitive |
| `DescribeIamInstanceProfileAssociations` | No | — | **None** (`Resource types` empty) | only `ec2:Region` | — | **No resource-level perms / no ABAC.** Account-scoped ("your"). Free recon of every assoc + profile ARN in the account for any holder of `ec2:Describe*` |

**Key authorization facts (confirmed in `list_ec2.md` action-with-resources table):**
- All three *mutating* actions require the **`instance`** resource type (`arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}`) and support **`aws:ResourceTag`/`ec2:ResourceTag`** (instance ABAC) **and** the profile-scoping keys **`ec2:InstanceProfile`** ("ARN of an instance profile") and **`ec2:NewInstanceProfile`** ("ARN of the instance profile being attached", on Associate+Replace only). **So AWS provides a precise control to constrain *which* profile/role may be attached.**
- The **flagship how-to sample** (`permission-to-pass-iam-roles.md`) uses **`Resource:"*"` with no condition block** on the ec2 actions and relies solely on a role-name-prefix PassRole (`role/DevTeam*`). It uses **none** of `instance`/`aws:ResourceTag`/`ec2:NewInstanceProfile`. The safer tag-scoped variant lives on a separate page (`ExamplePolicies_EC2.md`) and is **not cross-referenced** from the how-to page.
- `Describe…` is account-scoped and supports **no** resource-level permissions → any `ec2:Describe*` holder enumerates all associations (recon accelerant for Objective 1).
- The markdown mirror's *inline action-list* view renders the condition-key cells blank (true even for `TerminateInstances`); the authoritative data is the **action-with-resources** table above. Confirm against the live HTML reference if in doubt.

---

## 4. Trust-Boundary Map

| From (actor) | To (resource) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv caller | Privileged role's credentials | `Replace/Associate` + `iam:PassRole` → IMDS vends target role creds | Caller performs an action denied to its own identity using instance-vended creds = **privesc breach** |
| Caller w/ scoped PassRole or `ec2:NewInstanceProfile` | A role/profile outside the scope | name≠ARN indirection; prefix/wildcard; Name→ARN resolution; **condition key accepted-but-ignored** | Action attaches a role/profile the scope should forbid = **scope break** |
| Caller scoped to tagged/ARN'd instances | An excluded instance | assoc→instance resolution for `aws:ResourceTag`/`instance` condition | `Replace`/`Disassociate` succeeds on an excluded instance via its opaque `AssociationId` = **resource-scope fail-open** |
| Caller denied by split Disassociate+Associate | Same end-state via one call | `Replace` = conceptual disassociate+associate, single authz check | `Replace` succeeds where the two-call sequence is denied = **parity gap** |
| Holder of old vended creds | AWS APIs after profile removed | IMDS cred TTL; no server-side revoke | Old-role creds still authorize after `Disassociate`/`Replace` = **credential persistence** |
| Any caller | AWS service plane (instance-identity-role, SLR, AWS acct) | — | **HARD STOP** — disclosure, preserve evidence, cease |

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Privilege escalation by profile swap (Lens B / E) — **PRIORITY 1 (the named target mechanism)**

**Background.** The ec2 association action attaches a role (via its profile); the instance then vends that role's credentials through IMDS. The gate on *which* role may be attached is `iam:PassRole` (role name) and optionally `ec2:NewInstanceProfile` (profile ARN). The flagship sample uses neither tightly.

**Security Concern.** A limited principal can obtain the privileges of a **more-powerful role** it can pass. AWS's own samples scope PassRole by **name pattern** — `role/DevTeam*` (`permission-to-pass-iam-roles.md`, `ExamplePolicies_EC2.md`) and `role/TestRole-*`. Any role matching the pattern that is more privileged than the caller is an escalation target.

**High-level Test Scenarios:**
- **Lead B1 — passable-role privesc (core).** *Claim:* a caller holding the flagship sample policy verbatim (ec2 actions on `Resource:"*"`, `iam:PassRole` on `role/DevTeam*`) can `Replace`/`Associate` a more-privileged `DevTeam*` role onto any reachable instance and read its creds from IMDS. → *Mechanism:* `permission-to-pass-iam-roles.md` sample JSON — ec2 actions ungated by instance identity, PassRole by prefix only; `IamInstanceProfileSpecification.Name` → role → IMDS path. → *Oracle:* instance-vended creds call an API the caller's identity denies and it **succeeds** (prove with `SimulatePrincipalPolicy` first, then a canary-role live check). → *Preconditions:* the two permissions; a reachable instance; a more-priv in-scope role. → *Cost:* low (1 API call + 1 IMDS read; `associating` state is near-immediate). → *Severity:* **High**, **Critical** if the reached role is effectively admin. → *Stop:* on first cross-privilege success; do not use the creds further.
- **Lead B2 — prefix/wildcard PassRole self-escalation.** *Claim:* a caller that can also create/rename roles+profiles matching `DevTeam*`/`TestRole-*` and attach an admin policy can pass its own over-privileged role. → *Mechanism:* name-prefix PassRole scopes. → *Oracle:* self-created `DevTeam-x` admin role attached; its creds work. → *Preconditions:* also holds `iam:CreateRole`/`CreateInstanceProfile`/`AddRoleToInstanceProfile`/`AttachRolePolicy`. → *Severity:* **High**. → *Stop:* on existence proof.
- **Lead B3 — profile-name vs role-name indirection.** *Claim:* PassRole evaluates the *role* name while the ec2 action/`ec2:NewInstanceProfile` evaluate the *profile* ARN; a PassRole scope an operator wrote against the *profile* name (the doc explicitly warns *"specify the name of the IAM role and not the instance profile"*) fails to constrain the real role, and a profile whose name differs from its role can defeat an operator's mental model. → *Oracle:* demonstrate the keying (attach succeeds/denies in a way proving PassRole binds role name, not profile name). → *Severity:* **Medium–High** (scope-break enabler). → *Stop:* on demonstrating the keying.
- **Lead B4 — free target recon (accelerant).** *Claim:* `DescribeIamInstanceProfileAssociations` (commonly bundled in `ec2:Describe*`) returns every association's instance id + profile ARN account-wide with no resource-level perms, pre-selecting high-value targets at zero cost. → *Mechanism:* authz ref — Describe has no resource type, only `ec2:Region`; "your" = account-scoped. → *Oracle:* a low-priv `Describe*` holder lists all associations. → *Severity:* Low standalone, **High as a chain accelerant** for B1. → *Stop:* fold into B1.

### Area 2 — `ec2:NewInstanceProfile` / instance-scope enforcement (Lens S / U) — **PRIORITY 2**

**Background.** AWS provides `ec2:NewInstanceProfile` (ARN of the profile being attached) and `aws:ResourceTag`/`instance`-ARN scoping on all three mutating actions — a precise way to say "only these profiles, only these instances." Whether these are *enforced* (vs accepted-but-ignored) and *correctly resolved* from the opaque `AssociationId` is the question.

**Security Concern.** If `ec2:NewInstanceProfile` is accepted at policy-validation time but silently ignored at enforcement, every policy relying on it to prevent admin-profile attachment is a **documented-but-non-functional control** (Lens U) — the privesc path B1 is wide open even for a "properly scoped" policy. Separately, because `Replace`/`Disassociate` take only `AssociationId`, the `instance`/`aws:ResourceTag` condition must be evaluated against the *internally resolved* instance — a place it can bind nothing or the wrong object.

**High-level Test Scenarios:**
- **Lead S1 — `ec2:NewInstanceProfile` accepted-but-ignored.** *Claim:* a policy allowing `Replace` with `Condition {"ArnNotEquals":{"ec2:NewInstanceProfile":"arn:…:instance-profile/Admin*"}}` still permits attaching the Admin profile. → *Mechanism:* authz ref declares the key (def ~line 10117); enforcement unverified. → *Oracle:* `SimulatePrincipalPolicy` with the Admin profile ARN → if it returns `allowed`, the key is cosmetic; corroborate with a canary live call. → *Preconditions:* a scoped test role; a canary admin-named profile. → *Cost:* low. → *Severity:* **High** if ignored (defeats the only precise anti-privesc control). → *Stop:* on first allow against the forbidden profile.
- **Lead S2 — assoc→instance resolution fail-open.** *Claim:* under a role scoped to `instance/i-MINE*` (or `aws:ResourceTag/dept=test`), `Replace`/`Disassociate` on the `AssociationId` of a **non-matching** instance succeeds because the resource constraint is not evaluated against the resolved instance. → *Mechanism:* `Replace`/`Disassociate` take only `AssociationId` (API refs); authz ref says the required resource is `instance*`, but the mapping from id→instance is internal and undocumented w.r.t. ordering vs authz. → *Oracle:* `AccessDenied`/`UnauthorizedOperation` = resolved pre-authz (good); `200`/`associating` on the excluded instance = **fail-open breach**. → *Preconditions:* two same-account instances (matching/excluded), scoped test role. → *Cost:* low (2 instances). → *Severity:* **Medium–High** (High where the tag is the sole control). → *Stop:* on first 200 against the excluded instance.
- **Lead S3 — self-tag widening.** *Claim:* a holder scoped by `aws:ResourceTag/dept=test` who also has `ec2:CreateTags` tags any instance `dept=test` then replaces its profile. → *Oracle:* tag a foreign-workload instance, `Replace` succeeds. → *Severity:* **Medium–High** (customer-authored-policy footgun if self-inflicted; still document). → *Stop:* on existence proof.
- **Lead S4 — Name→ARN resolution TOCTOU.** *Claim:* `ec2:NewInstanceProfile` is ARN-typed but the API accepts `Name`; if a profile is deleted and recreated under the same Name with a different Id between policy intent and call time, a Name-based request may authorize against a different profile Id than intended. → *Mechanism:* `IamInstanceProfileSpecification{Name|Arn}`; ARN-typed key; resolution timing undocumented. → *Oracle:* compare authz outcome for `Name=X` vs `Arn=ARN(X)`, and across a delete/recreate of X. → *Severity:* **Medium** (same-account confused-deputy/TOCTOU). → *Stop:* null if per-account name uniqueness makes resolution deterministic at call time.

### Area 3 — Twin / sibling authorization parity (Lens X) — **PRIORITY 2**

**Background.** Three mutating actions change the same binding with different inputs. `Replace` is "disassociate+associate" in one call; its condition-key set is the **union** of Associate's and Disassociate's keys (it carries both `ec2:InstanceProfile` and `ec2:NewInstanceProfile`).

**Security Concern.** If `Replace`'s single authz check is evaluated as an **OR** (or only the new-profile half) rather than the **AND** of both halves, a caller denied by a split `Disassociate`+`Associate` policy can still succeed via `Replace`. Also, `Associate` has an InstanceId to check; `Replace`/`Disassociate` do not.

**High-level Test Scenarios:**
- **Lead X1 — Replace looser than its two-call twin.** *Claim:* a policy allowing `Disassociate` of profile `OLD` but denying `Associate` of `NEW` (via `ec2:NewInstanceProfile`) is bypassed by a single `Replace OLD→NEW`. → *Oracle:* two-call sequence → `AccessDenied` on the Associate; single `Replace` → `200`. → *Severity:* **Medium–High**. → *Stop:* on the divergent 200. *(Doc alone cannot resolve AND-vs-OR; this needs a live/simulator test.)*
- **Lead X2 — Associate vs Replace instance-scope parity.** *Claim:* a condition that correctly blocks `Associate` on an instance (checked via its InstanceId input) does not block `Replace` for that instance's association (no InstanceId input). → *Oracle:* same scoped role: `Associate` → `AccessDenied`, `Replace` → `200`. → *Severity:* **Medium–High**. → *Stop:* on divergent 200. *(Overlaps S2.)*
- **Lead X3 — Disassociate role-strip DoS.** *Claim:* `Disassociate` needs no `iam:PassRole`; a caller with only `ec2:DisassociateIamInstanceProfile` strips a workload's role, breaking every app relying on instance credentials. → *Mechanism:* no PassRole row for Disassociate (authz ref); takes only `AssociationId`. → *Oracle:* disassociate succeeds with no PassRole in the policy; workload loses AWS access. → *Severity:* **Medium** (single-account integrity/availability). → *Stop:* on existence proof — do not repeat.

### Area 4 — Credential lifecycle, IMDS exposure & kill-chain (Lens C) — **PRIORITY 2**

**Background.** After (re)association the new role's creds appear in IMDS; EC2 role creds are **not** bounded by max-session-duration; role removal has an up-to-1h propagation delay; creds rotate on expiry with no documented push-revocation.

**Security Concern.** Profile swap/detach may **not revoke already-vended credentials**, and IMDS is the delivery vector that turns the control-plane primitive into realized access.

**High-level Test Scenarios:**
- **Lead C1 — cred persistence after replace/disassociate.** *Claim:* creds read from IMDS under profile A stay valid after `Replace`→B or `Disassociate`, until their `Expiration`. → *Mechanism:* `instance-metadata-security-credentials.md` describes rotation/expiry, not push-revocation; `iam-roles-for-amazon-ec2.md` documents up-to-1h propagation for role removal. → *Oracle:* capture A's creds, swap to B, retry an A-scoped call with the cached creds — still `200` before expiry = persistence. → *Severity:* **Medium** (incident-containment gap — "swap the profile" does not cut off an attacker who already pulled creds; needs role deletion / explicit deny / session revocation). → *Stop:* once cached creds succeed once post-swap. **Do not exfiltrate/reuse beyond this single check; never touch service-plane identity paths.** *(Known STS bearer-token property — documentation-supported, not novel.)*
- **Lead C2 — kill-chain terminus (rate at the end).** *Chain:* `ec2:Replace` + `iam:PassRole(admin)` → swap → read admin creds from IMDS → **full account compromise**. → *Amplifier:* on instances with `HttpTokens=optional` (IMDSv1), the IMDS leg is reachable via a plain **SSRF** in the workload (no PUT-token needed), widening the attacker population from "code-exec on instance" to "any SSRF into the instance". → *Doc note:* **no SDK tab of the ResilientService launch-template sample sets `MetadataOptions`/`HttpTokens`** — AWS's own reference code never demonstrates `HttpTokens: required` (Lens-R insecure-default-by-omission). The authz ref also exposes `ec2:MetadataHttpTokens` as a condition key — a control the samples don't use. → *Severity:* **Critical** at the terminus. → *Stop:* HARD STOP if any surfaced identity is service-plane; IMDS on fully-managed hosts is out of scope.

### Area 5 — AWS-authored sample-policy / guidance audit (Lens R / U) — **PRIORITY 3**

**Background.** Two AWS-published samples cover this use case. `permission-to-pass-iam-roles.md` (the "how much permission do I need" **how-to** page customers copy first) grants the three ec2 actions with **`Resource:"*"`, no condition**, PassRole on `role/DevTeam*`. `ExamplePolicies_EC2.md` offers a tighter tag-scoped variant *and* a `TestRole-*` prefix variant.

**Security Concern.** AWS ships the **account-wide-blast-radius** variant on the primary page, omitting the `instance`/`aws:ResourceTag`/`ec2:NewInstanceProfile` controls its own authorization reference documents, and never cross-references the safer pattern. The customer did not invent the wildcard — AWS's primary how-to did.

**High-level Test Scenarios:**
- **Lead R1 — over-broad AWS sample (guidance defect).** *Claim:* the `permission-to-pass-iam-roles.md` sample, copied verbatim, grants account-wide profile replacement + any `DevTeam*` role, when AWS's authz reference provides `ec2:NewInstanceProfile`/`aws:ResourceTag` to prevent exactly that. → *Mechanism:* compare the flagship sample (no Condition, `Resource:"*"`) vs `ExamplePolicies_EC2.md` (instance/* + `aws:ResourceTag/department`) vs the authz ref's available keys. → *Oracle:* textual/`SimulatePrincipalPolicy` — a principal holding only the flagship sample performs a replace the prose implies it should not. → *Severity:* **Medium–High** (AWS-authored, copy-verbatim, uneditable guidance → **Tier-2 disclosure**, routed `aws-security`; *not* a customer footgun). → *Stop:* on simulate/existence proof. *(This is a doc-quality/default-guidance finding, not a server-side enforcement bug — label it so.)*

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Low-priv principal gains admin creds via swap | `Replace/Associate` + IMDS | `iam:PassRole` (role ARN); `ec2:NewInstanceProfile` (profile ARN); least-priv role design |
| Attach a role/profile outside scope | PassRole vs `ec2:NewInstanceProfile`; name≠ARN | role-ARN PassRole; ARN-typed `ec2:NewInstanceProfile` — **enforcement unverified (S1)** |
| `Replace`/`Disassociate` on an excluded instance | assoc→instance resolution for `instance`/`aws:ResourceTag` | `instance*` required resource type + `aws:ResourceTag` — **resolution ordering unverified (S2)** |
| `Replace` looser than Disassociate+Associate | single-call authz semantics | condition-key set is the union — **AND-vs-OR unverified (X1)** |
| Strip workload role (availability) | `Disassociate` (no PassRole) | action-level IAM grant only |
| Old creds survive profile removal | IMDS cred TTL | up-to-1h propagation; expiry only; no push-revoke documented |
| Copy flagship AWS sample → account-wide | `permission-to-pass-iam-roles.md` | prose "least privilege" note on PassRole only; safer variant not cross-referenced |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account access to associations / profiles.** Instance profiles, roles, instances, and `iip-assoc-` ids are **account-local**; `Describe…` returns only "your" associations; the backing store is account-partitioned. Cross-account attachment/enumeration is a **null hypothesis** — confirm the account-local binding (expect `InvalidAssociationID.NotFound` / empty on a foreign id), do not chase it as a primary lead.
- **Association-ID brute force.** ~68-bit random ids are not guessable; the only realistic path is a **foreign id obtained via another channel**, which only matters combined with S2.
- **IMDS on fully-managed / serverless compute** (Fargate, Lambda) and the **instance-identity-role** path — AWS service plane. **HARD STOP.**
- **A principal steering privileges it already holds** (no escalation if the caller already has everything the target role has).
- **Customer-authored over-broad policies / tag-ABAC self-tagging** — in scope *only* when the weak default ships in an AWS-authored/copy-verbatim artifact (R1). The generic `aws:ResourceTag` + `ec2:CreateTags` footgun (S3) is a well-known AWS-wide ABAC caveat, not unique to this family.
- **Third-party reference-repo code** — the `aws-doc-sdk-examples` ResilientService programs, the `AWS-RunShellScript`/`server.py` step, helper functions. **Command-injection in the SSM step was checked and REFUTED**: the command string is a hardcoded literal in every SDK tab (.NET/Python/JS), no caller-controlled value is interpolated. Bugs in that repo are not an AWS service defect.
- **Single-tenant self-DoS** — the sample's Replace→sleep→Reboot→SSM chain has no rollback if the target profile lacks SSM perms (the retry budget can exhaust and proceed to a confusing `InvalidInstanceId`), but this is self-inflicted, recoverable, single-instance. Reference-code robustness note only.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, with pages)

- **Lens A (cross-tenant IDOR):** checked all four API refs + data types + `CommonErrors.md`. Account-local ids, account-scoped `Describe`, no shared fleet. Residual *in-scope* sub-questions are intra-account (S2 resolution, B4 recon), not cross-account. **Error-oracle sub-lead (Low–Med):** the four API refs carry no action-specific error table (all defer to `CommonErrors.md`), so docs can't say whether a foreign/garbage `AssociationId` yields a generic pre-authz `InvalidParameterValue` (existence leaks before authz → enumeration oracle) vs a uniform post-authz error. Confirm by comparing error type/message/latency for a well-formed-nonexistent vs a real-foreign id. Priority: low, and only as a prerequisite signal for S2.
- **Lens G (SSRF):** API refs + `IamInstanceProfileSpecification` + example page — **no field the service dereferences/fetches** (Name/Arn/AssociationId only). N/A.
- **Lens Q (upload):** no upload/blob/image field. N/A.
- **Lens K (command injection):** the only shell step is in the **third-party** ResilientService sample and uses a **hardcoded literal** command (checked all SDK tabs) — **refuted**; out of scope regardless. N/A for the service.
- **Lens H/W (KMS / attestation):** no KMS key, encryption context, or attestation condition. N/A.
- **Lens J/FF (OAuth / JWT):** no 3P linking or token validation. N/A.
- **Lens V/D (network segmentation / control-plane escape):** control-plane IAM API, not a data-plane network path. N/A except the IMDS reachability amplifier (C2), which belongs to the instance's own workload.
- **Lens O (audit):** `Replace/Associate/Disassociate` **are** CloudTrail management events (`monitor-with-cloudtrail.md`: "All Amazon EC2 API actions are logged as management events"). **Attribution gap (Informational→Medium enabler):** the subsequent IMDS credential *use* is a local `169.254.169.254` HTTP GET — **never an AWS API call, so structurally not CloudTrail-logged** (confirmed null for "is IMDS fetch logged"); a responder must manually join the downstream assumed-role event to the `Replace` call by time + instance-id, with no native cross-reference field. Not a bug; a detection-ergonomics note.
- **PassRole re-check on Replace (L4, likely null):** authz ref lists `iam:PassRole`/`PassedToService=ec2.amazonaws.com` identically for Associate and Replace; docs are consistent that PassRole is required for the new role on every call. Treat as null unless a hunter's CloudTrail evidence shows Replace skips/mis-targets the PassRole check against the *new* role — if so, Critical.
- **Cross-account profile reference (null-by-absence):** `IamInstanceProfileSpecification{Name|Arn}` are unconstrained strings with no documented account-boundary check, but nothing supports cross-account use either (instance profiles are account-local; PassRole trust is the boundary). Not refutable from docs alone; only a live cross-account test could settle, and it is low priority.
- **Authorization-reference "doc-gap" — RESOLVED:** the mirror's inline action-list renders condition cells blank, but the **action-with-resources table** authoritatively declares `instance*` + `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:InstanceProfile`/`ec2:NewInstanceProfile` for the mutating actions. Resource-level + profile-scoping support is **confirmed available**; the open question is now *enforcement* (S1) and *resolution ordering* (S2), carried as live leads, not a doc gap.

---

*Generated from AWS public documentation only; no live testing performed. Three documentation-only subagents (PassRole/IAM-artifact; IDOR/ownership/parity; credential-lifecycle/IMDS/audit) contributed the leads integrated above. Hunter: execute Section 5 in priority order under the Section 0 safe-oracle discipline and HARD STOP.*
