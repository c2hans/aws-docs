# EC2 Fleet (and Spot Fleet) — Attack Research Plan

**Source of leads:** AWS EC2 User Guide, anchored on `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-prerequisites.html` and its neighborhood. Offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/*.md`. Online `.md` twins cross-checked (append `.md` to any `.html` page) to avoid local-sync gaps.
**Status:** Documentation-derived hypotheses only. **Nothing in this plan has been tested against a live AWS account.** It is the plan a hunter (e.g. `aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill, 4 parallel deep-analysis subagents (IAM/PassRole, launch templates, KMS grant, capacity-reservation sharing) + an orchestrator pass on the core fleet mechanism pages.

---

## 0. How to use this document

- Each lead is a falsifiable claim in the form: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs.
- **Prefer the safe oracle first.** Most IAM leads here are confirmable with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` and read-only `iam:GetPolicyVersion` / `iam:GetRole` / `kms:ListGrants` **before** any live resource is created. Live confirmation uses only synthetic canary roles/instances/keys and is torn down immediately.
- **HARD STOP:** EC2 Fleet runs almost entirely *inside the customer's own account*, so the usual cross-tenant surface is thin. The one true AWS-service-plane identity in scope is the service-linked role **`AWSServiceRoleForEC2Fleet`** (and its Spot twins). Treat it as read-only. The moment any evidence shows you have reached, assumed, or extracted credentials/ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**
- **Why this service is interesting despite being single-account:** its entire security story is *delegation* — a service-linked role that launches instances on your behalf, an AWS-authored copy-verbatim IAM policy, a KMS grant AWS tells you to create, and launch-template *late-binding* that AWS itself documents as a `PassRole` bypass. The highest-value findings are **intra-account privilege escalation via AWS-authored artifacts** (in scope per Lens R carve-out) and **cross-account capacity/KMS trust** that re-arms itself without the resource owner's involvement.

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. Starting from the AWS-published "EC2 Fleet users" sample policy (`ec2:*` + narrow `iam:PassRole`), **escalate to an arbitrary / admin role** in the account without holding the IAM statements the policy author believed were the gate.
2. As a principal **explicitly denied `iam:PassRole`**, cause an EC2 Fleet to launch instances carrying an arbitrary instance profile (launch-template late-binding, or `instant`-fleet `CreateFleet` overrides).
3. **Bypass a documented `RunInstances`-scoped IAM control** (launch-template restriction, IMDSv2 enforcement, `aws:RequestTag` ABAC) by routing the launch through `CreateFleet` / the fleet SLR instead of a direct `RunInstances`.
4. Make the EC2 Fleet SLR exercise **KMS operations beyond what launching needs** (`CreateGrant`, `Encrypt`, `ReEncrypt*`) on a customer CMK; show the grant is over-scoped and lacks an encryption-context constraint.
5. Show the **KMS grant survives the documented teardown** ("delete the role") and that **recreating the identically-named role silently re-inherits** CMK access — cross-account worst case.
6. From a **consumer account**, use an EC2 Fleet to consume / exhaust / mis-bill another account's **shared Capacity Reservation** (ODCR / interruptible CR / Capacity Block), or keep consuming after the share is revoked.
7. Enumerate **doc-vs-reality** deltas: the SLR's actual attached policy vs its documented action list; doc-vs-doc contradictions (interruptible-CR grouping); audit blind spots (`instant` fleets emit no EventBridge events).

---

## 2. Components, Assets, and Design

**What it is.** EC2 Fleet is a CLI/API-only orchestration layer (`CreateFleet`) that launches a mixed fleet of On-Demand + Spot instances from a **launch template**, into the **caller's own account/VPC**. Spot Fleet is the legacy console-supported twin (`RequestSpotFleet`), "no planned investment." There is no multi-tenant service fleet and no customer-reachable data plane — the "service" is the control-plane API plus the service-linked roles that call `RunInstances`/`TerminateInstances` on your behalf.

**Request types** (`ec2-fleet-request-type.md`): `instant` (synchronous one-shot, EC2 Fleet only, **no SLR required**, the only type that consumes Capacity Reservations/Blocks, and the only type with `CreateFleet`-time overrides), `request` (async one-shot), `maintain` (async, self-replenishing — the type whose capacity-replacement cycle re-resolves `$Latest`/`$Default`). `instant` is used internally by **EC2 Auto Scaling and EMR**.

**Identity / roles.**
- `AWSServiceRoleForEC2Fleet` — SLR, assumable only by `ec2.amazonaws.com`; documented granted actions: `ec2:RunInstances`, `ec2:RequestSpotInstances`, `ec2:TerminateInstances`, `ec2:DescribeImages`, `ec2:DescribeInstanceStatus`, `ec2:DescribeSubnets`, `ec2:CreateTags` (no KMS, no PassRole in the printed list).
- Spot Fleet: `AWSServiceRoleForEC2SpotFleet`, `AWSServiceRoleForEC2Spot`, plus the passable `aws-ec2-spot-fleet-tagging-role`.
- End-user principal: holds an **AWS-authored sample policy** copied verbatim from the prerequisites pages (the primary attack surface).

**Resource identifiers.** Fleet IDs, launch template IDs + version aliases (`$Latest`/`$Default`), instance/volume IDs, Capacity Reservation IDs (`cr-` + 17 hex, opaque, service-allocated — not predictable → Lens EE null), CR Resource Group ARNs (per-account), CMK ARNs.

**Untrusted-data entry points.** Launch-template `UserData` (boot-time code, up to 16KB), `IamInstanceProfile`, AMI ID (including the `resolve:ssm:<ARN>` cross-account alias), `MetadataOptions`, tag specifications, `CapacityReservationTarget`, price-protection knobs.

```
 Caller (IAM principal w/ sample policy)
     │  CreateFleet / RequestSpotFleet          CreateLaunchTemplateVersion / ModifyLaunchTemplate
     │                                          (effectively grants PassRole — AWS-documented)
     ▼                                                        │
 EC2 Fleet control plane ──reads──► Launch Template (versioned, $Latest/$Default late-binding) ◄── v2 (attacker)
     │  assumes                                               │  AMI = resolve:ssm:<cross-acct ARN>  (mutable)
     ▼                                                        ▼
 AWSServiceRoleForEC2Fleet (SLR) ──RunInstances──► EC2 instance (IamInstanceProfile creds via IMDS)
     │  (for maintain/request; instant uses the caller path, no SLR)
     ├─ KMS grant (Decrypt/Encrypt/GenerateDataKey/CreateGrant/ReEncrypt*) ──► Customer CMK (encrypted AMI/EBS)
     └─ Capacity source ──► ODCR / interruptible CR / Capacity Block  (may be RAM-shared from ANOTHER account)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Holder of sample "EC2 Fleet users" policy (`ec2:*` + scoped PassRole) | Any role already attached to any instance in the account | `ec2:ModifyInstanceAttribute(userData)` + reboot/stop-start (inside `ec2:*`) | Attacker payload executes under a role the holder has no `PassRole` for; creds read from that instance's IMDS |
| Launch-template-version-writer, **PassRole denied** | Any IAM role nameable in `IamInstanceProfile` | `CreateLaunchTemplateVersion`/`ModifyLaunchTemplate` on a template a fleet tracks via `$Latest`/`$Default`; EC2 does **not** re-check perms at launch | Fleet-launched instance presents credentials for a role the writer could not pass directly |
| Caller IAM-restricted via `ec2:RunInstances` conditions (`ec2:LaunchTemplate`, IMDSv2, `aws:RequestTag`) | Templates / resources / configs outside that allowlist | `ec2:CreateFleet` → `RunInstances` runs as the **SLR**, not the caller | `CreateFleet` + launch succeeds where the equivalent direct `RunInstances` is denied |
| `instant`-fleet caller holding `CreateFleet` but not PassRole/template-write | Instance profile / raw user-data / `MetadataOptions` override fields | `Overrides.*` on `CreateFleet` | Instance launches with an override the caller could not set via a PassRole-checked path |
| `AWSServiceRoleForEC2Fleet` (SLR) | Customer CMK | Unconstrained `CreateGrant`/`Encrypt`/`ReEncrypt*` the docs tell you to grant | SLR activity touches the key for a resource outside the fleet, or mints a child grant |
| Grantee-role-owning account | CMK-owning account (doc example uses two distinct account IDs) | `GranteePrincipal` = foreign-account role ARN; teardown never retires the grant | Grantee deletes+recreates the role and silently regains CMK access with no action by / notice to the key owner |
| Consumer account's EC2 Fleet | Owner account's shared ODCR / interruptible CR / Capacity Block | Caller-supplied `CapacityReservationId` / group ARN matched by RAM/org share; or `open` auto-match | Fleet consumes / drains / out-of-quota the owner, or keeps consuming after unshare |
| Any customer's Spot Fleet workflow (confused deputy) | `aws-ec2-spot-fleet-tagging-role` | `spotfleet.amazonaws.com` `AssumeRole` on a trust policy whose `aws:SourceArn`/`SourceAccount` hardening is an **optional** customer add-on | `GetRole` on a console-created role shows no `Condition` on the trust statement |

**Hard-stop boundary:** any customer surface ↔ AWS's own service plane (the SLRs' live credentials). Read-only only.

---

## 4. API / Interface Inventory

| Name | Mutating | Facing | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `CreateFleet` | yes | external | Launch fleet; `instant` supports `Overrides` (IamInstanceProfile, UserData, MetadataOptions) | yes (SigV4) | caller principal | Prime target: override + CR-targeting paths; whose identity is PassRole-checked is **undocumented** |
| `ModifyFleet` | yes | external | Change target capacity (maintain only) | yes | caller | TOCTOU window with `$Latest` re-resolution |
| `DeleteFleets` | yes | external | Delete fleet (+ optionally terminate) | yes | caller | — |
| `DescribeFleets` / `DescribeFleetInstances` / `DescribeFleetHistory` | no | external | Read fleet state/instances/events | yes | caller | Account-scoped |
| `CreateLaunchTemplate` / `CreateLaunchTemplateVersion` / `ModifyLaunchTemplate` | yes | external | Author template content incl. role/user-data/AMI | yes | caller | **AWS-documented effective `PassRole` grant**; no resource-level control over template *body* |
| `DescribeLaunchTemplates` / `DescribeLaunchTemplateVersions` | no | external | Read template content | yes | caller | **Cannot carry resource-level/condition restrictions** → account-wide template content disclosure (recon) |
| `RequestSpotFleet` / `ModifySpotFleetRequest` / `CancelSpotFleetRequests` / `Describe*` | mixed | external | Legacy Spot Fleet | yes | caller | Legacy API, no planned investment |
| `kms:CreateGrant` (customer runs it per docs) | yes | external | Grants SLR 8 KMS ops on a CMK | yes | key admin | Over-scoped, no encryption-context constraint, cross-account exampled |
| `instant` fleet events | — | — | — | — | — | **No EventBridge events emitted** (`maintain`/`request` only) → audit blind spot (Lens O) |

**Doc-planted leads kept verbatim:** `use-launch-templates-to-control-launching-instances.md` / `permissions-for-launch-templates.md`: *"the user is effectively also granted the `iam:PassRole` permission … Amazon EC2 does not re-check permissions … because there is no user interaction with the AWS resource."* This is AWS telling you where the bug is.

---

## 5. Recommended Areas of Focus (priority order)

Priority = (AWS-flagged risk) > (intra-account privesc via AWS-authored artifact) > (RunInstances-control bypass via fleet path) > (cross-account KMS/capacity trust) > (doc-vs-reality / audit gaps).

### 5.1 Launch-template late-binding → PassRole bypass (AWS-documented) — **P0**
**Background:** A fleet of type `maintain`/`request` that references a launch template by `$Latest`/`$Default` re-resolves the version on every capacity-replacement cycle, and EC2 does **not** re-check the triggering principal's IAM at that point.
**Security Concern:** A principal with only `CreateLaunchTemplateVersion`/`ModifyLaunchTemplate` (PassRole **explicitly denied**) can (a) attach an arbitrary `IamInstanceProfile` to a new version and have the SLR launch instances as that role, or (b) change only `UserData` to exfiltrate the credentials of whatever role the current default version already carries — code-exec-as-role with no instance-profile write at all.
**High-level Test Scenarios:**
- Simulate: confirm the scoped principal denies `iam:PassRole` but allows the two template actions.
- Live canary: fleet pinned to `$Default` v1 (benign) → attacker creates v2 (privileged profile *or* exfil user-data), sets default → trigger a replacement cycle → confirm new instance carries the injected role / exfils creds.
- **Open doc-gap to resolve:** does EC2 Fleet re-resolve `$Latest` per-launch, or snapshot once at `CreateFleet`? No fleet page states the retry/replace re-resolution semantics.
**Doc evidence:** `permissions-for-launch-templates.md`, `use-launch-templates-to-control-launching-instances.md`. **Severity-if-true:** Critical (user-data variant strictly worse — needs only the commonly-granted "template editor" right).

### 5.2 Intra-account privesc from the AWS-authored "EC2 Fleet users" sample policy — **P0**
**Background:** `ec2-fleet-prerequisites.md` ships `{"Action":["ec2:*"],"Resource":"*"}` + `iam:PassRole`/`ListRoles`/`ListInstanceProfiles` on a role **name prefix** `role/DevTeam*`, with an optional `iam:CreateRole`+`iam:AttachRolePolicy`+`iam:CreateInstanceProfile` block **printed with no scoped JSON to copy**. In scope under the Lens R carve-out — AWS-authored, copy-verbatim, uneditable-pattern artifact.
**Security Concern:**
- `ec2:*` includes `ec2:ModifyInstanceAttribute(userData)` → edit user-data on *any* instance already carrying a privileged profile, reboot, run code as that role — **no `PassRole` needed at all.**
- The optional block has **no `iam:PolicyArn` condition** → `CreateRole DevTeam-x` (satisfies the prefix) → `AttachRolePolicy AdministratorAccess` → add to instance profile → pass via the already-granted PassRole → full admin.
- The PassRole statement has **no `Condition` / `iam:PassedToService`** → any `DevTeam*`-named role (incl. one more privileged, or trusted by another service) is passable to EC2.
**High-level Test Scenarios:** `SimulatePrincipalPolicy` for `ModifyInstanceAttribute`+`StopInstances` on a non-`DevTeam*` instance ARN (expect ALLOW, no condition); `SimulateCustomPolicy` for `AttachRolePolicy(AdministratorAccess, DevTeam-escalate)`; enumerate `DevTeam*` roles and simulate PassRole against each. Canary-confirm the user-data-swap chain only in a sandbox.
**Doc evidence:** `ec2-fleet-prerequisites.md` "Permissions for EC2 Fleet users" JSON. **Severity-if-true:** Critical (non-admin → admin).

### 5.3 `RunInstances`-scoped controls bypassed via the `CreateFleet` / SLR path — **P1**
**Background:** AWS's sample IAM controls (restrict-to-one-launch-template via `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource`; "Deny opt-out of IMDSv2"; `aws:RequestTag` ABAC) are written against `ec2:RunInstances` and evaluated against the **calling principal**. When the launch is driven through `CreateFleet`, the actual `RunInstances` is issued by the SLR (for `maintain`/`request`) or via a different internal path (`instant`, which uses no SLR).
**Security Concern (Lens X — twin-path parity):**
- A principal restricted by `ec2:RunInstances` + `ec2:LaunchTemplate` ArnLike to template A can reference template B via `CreateFleet` if `CreateFleet` has no equivalent condition key.
- IMDSv2-enforcement Deny (documented for ASG as *not* re-checked on `$Latest`/`$Default`) likely likewise bypassable for EC2 Fleet → fleet launches with `HttpTokens=optional` despite the org Deny.
- `aws:RequestTag`/`aws:TagKeys`-gated `RunInstances` may be satisfied by a *fleet-level* tag while the launched instances are untagged/differently-tagged (`tag-ec2-fleet.md`: fleet tags do **not** auto-propagate to instances).
- The first "restrict to this template" sample policy in `ExamplePolicies_EC2.md` omits `ec2:IsLaunchTemplateResource` → the template's embedded subnet/SG/NIC ARNs are overridable at launch, defeating the hardening intent.
**High-level Test Scenarios:** Attach each sample control to a scoped principal; attempt the restricted operation once directly (expect Deny) and once via `CreateFleet` (breach if it succeeds). Resolve the doc-gap: does `ec2:CreateFleet` expose `ec2:LaunchTemplate`-style condition keys at all? (Check the EC2 IAM Action/Condition reference — not mirrored in this UserGuide.)
**Doc evidence:** `ExamplePolicies_EC2.md`, `permissions-for-launch-templates.md`, `create-ec2-fleet.md`, `tag-ec2-fleet.md`. **Severity-if-true:** High (undermines baseline IMDSv2 / governance controls, chains into SSRF/credential theft).

### 5.4 `instant`-fleet `CreateFleet`-time overrides (IamInstanceProfile / UserData / MetadataOptions) — **P1**
**Background:** `create-ec2-fleet.md` states `instant` fleets accept direct overrides of `IamInstanceProfile`, `LaunchTemplateSpecificationUserData` (raw user-data), and `MetadataOptions` — bypassing the launch-template object (whose authoring the docs say to restrict to "trusted administrators").
**Security Concern:** Whose identity is `iam:PassRole`-checked for the override path is **undocumented**. If unchecked (or absorbed by the caller-path launch with no SLR), a holder of `CreateFleet` but not template-write / PassRole injects an instance profile or user-data directly; `MetadataOptions=HttpTokens:optional` further downgrades IMDS to ease credential theft from whatever role lands.
**High-level Test Scenarios:** `SimulatePrincipalPolicy` first; then `CreateFleet (instant)` with `Overrides.IamInstanceProfile` = a role the caller cannot pass directly — `AccessDenied`(PassRole) = fail-closed; a successful launch = breach (terminate immediately).
**Doc evidence:** `create-ec2-fleet.md` override list. **Severity-if-true:** High–Critical (doc-gap — confirm surface first).

### 5.5 KMS grant: over-scope, missing encryption-context, orphan-grant re-inheritance — **P1 (cross-account) / P2 (same-account)**
**Background:** The prerequisites pages tell every customer to `kms:create-grant` the SLR **8 operations** (`Decrypt Encrypt GenerateDataKey GenerateDataKeyWithoutPlaintext CreateGrant DescribeKey ReEncryptFrom ReEncryptTo`) with **no `--constraints`**, while EBS's documented KMS usage is only `GenerateDataKeyWithoutPlaintext` + `Decrypt` carrying `{"aws:ebs:id":<id>}`. The doc example uses **two different account IDs** (cross-account grant). Teardown says "delete the role" but never retires the grant.
**Security Concern:**
- **Over-scope (Lens R/U):** `CreateGrant` is a grant-chaining primitive (mint child grants to any principal); `Encrypt`/`ReEncrypt*` let the SLR re-encrypt data. None are needed to launch.
- **No encryption-context constraint (Lens H):** the grant works for *any* EBS resource on that CMK, not just the fleet's.
- **Orphan + re-inherit (Lens AA/EE):** grant survives role deletion; recreating the identically-named role (which the docs invite) *may* re-inherit it if `GranteePrincipal` binds by ARN rather than unique principal-ID — **undocumented, the crux doc-gap.** Cross-account worst case: a foreign grantee account re-arms standing access to your CMK with zero action by/notice to you.
- **Laundering (Lens B/T):** an EC2-Fleet user with no `kms:*` triggers fleet ops that transitively exercise the SLR's `CreateGrant`.
**High-level Test Scenarios:** grant only `Decrypt`+`GenerateDataKeyWithoutPlaintext`+`DescribeKey` → does the fleet still launch from an encrypted AMI? (proves the other 4 unneeded). Decrypt with an unrelated volume's encryption context (proves no scoping). `list-grants` after deleting the role (proves orphan). Delete+recreate role, attempt `Decrypt` as new role with no new grant (ARN-rebind = High; unique-ID = refuted, but confirms permanently orphaned grant). Shared-AMI variant re-runs the recreate test across accounts.
**Doc evidence:** `ec2-fleet-prerequisites.md` CMK section, `spot-fleet-prerequisites.md` (byte-identical), `kms/.../services-ebs.html`, `AMIEncryption.md`, `sharing-amis.md`. **Severity-if-true:** High (cross-account re-inherit) / Medium (same-account over-scope).
**Stop condition:** interaction with the SLR identity is read-only (`ListGrants`); if the real mechanism needs `CreateGrant` for a Nitro sub-identity, downgrade and document.

### 5.6 Cross-account shared Capacity Reservation abuse — **P1/P2**
**Background:** `instant` fleets are the only type that consume Capacity Reservations/Blocks, targeted by a caller-supplied `CapacityReservationId` / group ARN, or by `open` auto-matching. Reservations can be RAM/org-shared from another account.
**Security Concern:**
- **Cross-account quota drain (Lens L/A):** `capacity-reservation-sharing.md` states *consumer* usage counts against the **owner's** On-Demand Instance limit — a consumer's fleet can push the owner to `InstanceLimitExceeded` on unrelated launches. No documented per-consumer cap.
- **`open`-match silent consumption:** a consumer fleet lands in a shared `open` CR without ever naming it, crowding out the owner/other consumers.
- **Resource-group grantee-validation (Lens AA):** does `group-resources` accept a foreign CR ARN not actually shared with the caller? Differential error (`ValidationException` naming the resource vs generic `AccessDenied`) = existence oracle; success = bypass.
- **Doc-vs-doc (Lens U/X):** `interruptible-capacity-reservations.md` says consumers *can't* add interruptible CRs to groups; the multiple-CR-type walkthrough instructs a consumer to do exactly that. Resolve against real behavior — permissive = unenforced reclaim-protection via the group→fleet path.
**High-level Test Scenarios:** two-account setup; drive owner to quota via consumer fleet; `open`-match without a target and check `capacity-reservation-id` on the launched instance; `group-resources` with an unshared foreign CR ARN; one `group-resources` call to settle the interruptible-CR contradiction.
**Doc evidence:** `capacity-reservation-sharing.md`, `ec2-fleet-on-demand-capacity-reservations.md`, the targeted/interruptible/multiple-CR walkthroughs, `cr-groups.md`, `interruptible-capacity-reservations.md`, `assign-billing.md`. **Severity-if-true:** High (cross-account DoS/financial), Medium (grouping/enumeration).
**Stop condition:** requires two real accounts; do not test against production quotas.

### 5.7 Spot Fleet tagging-role confused deputy + wildcard-account PassRole — **P2**
**Background:** `spot-fleet-prerequisites.md` ships `iam:PassRole` on `arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role` (**wildcard account** field) and, for instance-profile roles, literally recommends `arn:aws:iam::*:role/{{IamInstanceProfile-role}}`. The confused-deputy `aws:SourceArn`/`SourceAccount` hardening on the tagging-role trust policy is framed as an **optional** customer step, implying the console wizard ships it **without** that condition.
**Security Concern (Lens B/R):** wildcard-account PassRole resources normalize an over-broad grant; the default-missing `SourceArn`/`SourceAccount` is a textbook confused-deputy gap AWS names but leaves off by default.
**High-level Test Scenarios:** `GetRole` on a wizard-created `aws-ec2-spot-fleet-tagging-role` → confirm absence of trust-policy `Condition` (direct read, no live cross-account action). Simulate the wildcard PassRole resource for reach.
**Doc evidence:** `spot-fleet-prerequisites.md`. **Severity-if-true:** Medium (bounded by the tagging role's capability).

### 5.8 Doc-vs-reality & audit gaps — **P3 (informational, enablers)**
- **SLR actual policy vs documented list (Lens U):** `GetPolicyVersion` on `AWSEC2FleetServiceRolePolicy`; diff against the 7 bulleted actions. Any extra (`iam:PassRole`, `ModifyInstanceAttribute`, broad `Describe*`) is a reportable delta. **Read-only — this is the service plane.**
- **`DescribeLaunchTemplateVersions` cannot be condition-scoped** → account-wide disclosure of every team's `UserData`/`IamInstanceProfile`/`KeyName`. The recon step that makes 5.1/5.2 targeted.
- **`instant` fleets emit no EventBridge events** (`monitor-ec2-fleet-using-eventbridge.md`) → a privesc/launch performed via an `instant` fleet has a weaker audit trail than `maintain`/`request`. And `instant` is what EMR/ASG use internally.
- **`resolve:ssm:<cross-account-ARN>` AMI alias:** the template owner trusts another account's ability to repoint the parameter to an attacker AMI at launch time, "launch template remains unchanged." Documented-but-under-warned trust (Lens U); redirect sharing-lifecycle work to SSM Parameter Store docs.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| PassRole-less role injection via `$Latest`/`$Default` | Launch template versioning + fleet SLR | "Grant template APIs only to trusted admins"; no per-launch re-check (AWS-stated gap) |
| Non-admin → admin via sample policy | AWS-authored "EC2 Fleet users" policy | Prose caveat "limit to specific actions"; `DevTeam*` prefix; optional-block scoping (absent) |
| RunInstances control bypass via CreateFleet | `ec2:CreateFleet` vs `ec2:RunInstances` condition keys | `ec2:LaunchTemplate`/`IsLaunchTemplateResource`/IMDSv2 Deny on RunInstances |
| `instant` override PassRole bypass | `CreateFleet` Overrides | Unspecified — doc silent on PassRole enforcement for overrides |
| CMK over-scope / grant chaining | KMS grant for SLR | Prose "so EC2 can launch on your behalf"; no constraints shipped |
| Orphan grant re-inheritance | KMS grant lifecycle vs role deletion | None — teardown never retires the grant |
| Cross-account CR quota drain / silent consume | Shared ODCR/interruptible CR/Block | Owner's On-Demand limit (shared, no per-consumer cap); `open` auto-match |
| Confused deputy on tagging role | `aws-ec2-spot-fleet-tagging-role` trust policy | `aws:SourceArn`/`SourceAccount` — optional, not default |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Classic cross-tenant IDOR on fleet/instance resources** — N/A: the fleet, its instances, and the SLR all live in the caller's own account.
- **AWS's own service-plane / SLR live credentials** — hard stop; read-only (`GetPolicyVersion`, `ListGrants`, `GetRole`) only.
- **Single-tenant self-DoS / price-protection footguns** — caller-controlled cost knobs on their own fleet (`OnDemandMaxPricePercentageOverLowestPrice` etc.) are self-inflicted, out of scope.
- **Customer-authored** least-privilege mistakes — out of scope. (The **AWS-authored** sample policies / KMS grant command / confused-deputy defaults are **in scope** per the Lens R carve-out — Tier-2, route `aws-security`.)
- **IMDS on fully-managed hosts, DNS rebinding against private endpoints, product/feature-parity gaps.**
- **SSRF, translation-layer/wire-protocol injection, prompt injection, attestation-gating, canonicalization/parser-differential, cache-key divergence, trusted-header injection** — N/A for this surface (see §8; no URL-dereference field, no parser/translator, no LLM, no enclave gate, no authorizer/edge/cache layer in front of the SigV4 API).

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire, pages checked)

- **Lens A (cross-tenant IDOR):** N/A — `instant-fleet.md`, `create-ec2-fleet.md`, `ec2-fleet-prerequisites.md`: everything is single-account. The only cross-account reachable resource is a *shared Capacity Reservation* (→ §5.6).
- **Lens EE (predictable-name land-grab):** N/A — CR IDs are opaque `cr-`+17 hex, service-allocated; CR group ARNs are per-account. Checked the CR pages + `cr-groups.md`. (Launch-template `resolve:ssm` cross-account alias is the nearest shape → §5.8, redirected to SSM docs.)
- **Lens F (injection/translation):** N/A — matching is attribute/enum-based (`InstanceRequirements` vCPU/memory/price numerics); no free-text query language. Checked `ec2-fleet-attribute-based-instance-type-selection.md` in full.
- **Lens G (SSRF):** N/A — reviewed `instant-fleet.md`, attribute-selection, `tag-ec2-fleet.md`, all walkthroughs; no URL/URI/webhook/callback field the service dereferences.
- **Lens K (prompt injection), W (attestation), BB/CC/DD (canonicalization / trusted-header / cache-key):** N/A — no LLM/agent, no enclave/`kms:RecipientAttestation`, no documented authorizer/WAF/CDN/cache layer in front of EC2 Fleet's SigV4 API.
- **Lens I (tag leakage via billing/CUR):** refuted by doc — `assign-billing.md`: owner's cost-allocation tags do not appear in the consumer's CUR.
- **KMS key disabled/deleted at fleet-create:** refuted as a vuln — `services-ebs.html` documents clean failure + EventBridge event, no partial state.

**Key doc-gaps to resolve before calling anything confirmed:**
1. Does EC2 Fleet re-resolve `$Latest`/`$Default` **per-launch** (like the ASG behavior AWS documents) or snapshot once at `CreateFleet`? (gates §5.1, §5.3-IMDSv2)
2. Is `iam:PassRole` evaluated against the **caller** for the `instant` `Overrides.IamInstanceProfile` path? (gates §5.4)
3. Does `ec2:CreateFleet` expose `ec2:LaunchTemplate`-style condition keys at all, or is the control structurally absent? (gates §5.3) — check the EC2 IAM Service Authorization Reference (not mirrored in this UserGuide).
4. Does KMS `CreateGrant` `GranteePrincipal` bind by **ARN** or by **unique principal-ID**? (gates §5.5 orphan re-inherit) — not stated in `grants.html`/`create-grant-overview.md`; the IAM Principal-element page documents the transform only for role trust policies.

---

### Kill-chain candidates (rate at the end of the chain)
- **§5.8 recon** (`DescribeLaunchTemplateVersions` reveals a team's privileged instance-profile ARN) → **§5.1/§5.2** (inject that exact profile / user-data via `$Latest` or `ModifyInstanceAttribute`) → **code-exec as the privileged role** → if that role can read a CMK or reach another account's shared CR, chain into **§5.5 / §5.6**. End severity: Critical (intra-account admin, possibly cross-account via KMS/CR trust).
- **§5.3 IMDSv2 downgrade** via late-binding → IMDSv1 reachable on the launched instance → SSRF-to-IMDS credential theft of the attached role. End severity: High.
