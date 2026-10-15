# AWS Managed Policies for Amazon EC2 — Attack / Research Plan

**Target:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam-awsmanpol.html`
(offline twin: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/security-iam-awsmanpol.md`)
**Skill:** `security-questionbuilder` (6-step boundary-first method)
**Date:** 2026-10-15
**Drift check:** offline `.md` == online `.md` == online `.html`, byte-verbatim. 15 policies, same changelog/dates. (Do **not** confuse with the separate SQL-Server variant at `docs/sql-server-ec2/latest/userguide/security-iam-awsmanpol.md` — different policy set.)

---

## 0. Scope, Trust Model, and Reporting Rule

This page is **not an API**. It is a catalogue of **AWS-authored, uneditable IAM artifacts** — customer-attachable managed policies and service-linked-role (SLR) policies. The security property of this surface is therefore different from a feature page:

- A weak default (over-broad `Resource:"*"`, a presence-only condition, a missing ownership binding, an unconditioned `PassRole`) in one of these documents is **AWS's own defect**, not a customer footgun — the customer attaches or inherits it verbatim and cannot edit it. These are **Tier-2 reportable** under the skill's rubric.
- **Primary lenses:** **R** (AWS-authored IAM-artifact audit), **S** (condition-key scoping semantics), **U** (documented-guarantee vs enforcement), **AA** (share/revoke lifecycle & Organizations grantee validation), with **B/C** (PassRole / confused-deputy), **E** (privilege escalation), **T** (cross-service secret reachability), **X** (action-family parity).
- **Universal confirm oracle (non-mutating, no resources touched, no live launch):** `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`. Feed the verbatim policy JSON (or the principal ARN), the action, a target ARN **not owned by the caller**, and the relevant `ContextEntries`; read `allowed` vs `implicitDeny`. Every lead below resolves this way without touching EC2.
- **Severity frame:** cross-account = Critical; cross-tenant / privilege-escalation = High; intra-account ABAC / least-privilege = Medium; audit/observability gap = Low.
- **Hard stop:** the moment any observation surfaces AWS's **own** service-plane identity/credential/ARN/account, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected from documentation analysis, but the SLRs here are AWS-fleet principals — treat their internal reconciliation behavior as out-of-scope / un-auditable from docs.)
- **Key structural fact (independently verified):** EC2 has **ZERO** Organizations condition keys. `grep` of `docs/service-authorization/latest/reference/list_ec2.md` (10190 lines) shows no `aws:PrincipalOrgID`, `aws:ResourceOrgID`, `aws:PrincipalOrgPaths`, or `aws:ResourceOrgPaths` anywhere. This is load-bearing for the Capacity Manager and share-lifecycle leads: EC2-side policy **cannot** bound a grant to an organization.

---

## 1. Components, Assets, and Design

**What this page ships:** 15 named IAM policy documents, each a JSON artifact. Two classes:

- **Customer-attachable managed policies** (a human/role can attach): `AmazonEC2FullAccess`, `AmazonEC2ReadOnlyAccess`, `AmazonEC2ImageReferencesAccessPolicy`, `EC2FastLaunchFullAccess`, `AWSEC2VssSnapshotPolicy`, `EC2InstanceConnect`, `DeclarativePoliciesEC2Report`.
- **Service-linked-role (SLR) policies** (only the named AWS service principal can assume; not user-attachable): `AWSEC2CapacityManagerServiceRolePolicy` (`ec2.capacitymanager.amazonaws.com`), `AWSEC2CapacityReservationFleetRolePolicy`, `AWSEC2FleetServiceRolePolicy`, `AWSEC2SpotFleetServiceRolePolicy`, `AWSEC2SpotServiceRolePolicy`, `EC2FastLaunchServiceRolePolicy` (`ec2fastlaunch.amazonaws.com`), `Ec2InstanceConnectEndpoint` (EICE SLR).

**Why the SLR/attachable split matters as a trust statement:** an attachable policy's blast radius is "whatever principal the customer attached it to" — including an **instance profile** (any code with IMDS access on that instance inherits it). An SLR policy's blast radius is "the AWS fleet principal," only reachable through a confused-deputy in the service internals (un-auditable from docs) — so SLR findings are flagged as defense-in-depth / fail-open hypotheses, while attachable-policy findings are directly weaponizable.

**Assets reachable through these artifacts:** every EC2 resource (instances, volumes, snapshots, images, ENIs, security groups, key pairs, capacity reservations), plus cross-service reach into `elasticloadbalancing:*`, `cloudwatch:*`, `autoscaling:*`, `organizations:*` (read), `ssm:*` (parameter read), `imagebuilder:*` (recipe read), `license-manager:*`, and `iam:PassRole`.

**Identifier shapes that gate authorization here:** EC2 resource tags (`CreatedBy`, `AwsVssConfig`, `InstanceConnectEndpointId`, `aws:ec2:fleet-id`, `aws:ec2spot:fleet-request-id`), `iam:PassedToService`, `aws:CalledVia`, `ec2:CreateAction`, `ec2:InstanceMarketType`, `ec2:CapacityReservationFleet` (ARN-presence), `ec2:SourceInstanceARN`. Several of these are **presence-only** or **value-shape-only** checks — the central weakness class on this page.

---

## 2. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Holder of `EC2FastLaunchFullAccess` (esp. an instance profile) | Any EC2-trusted IAM role in the account | `iam:PassRole` (role/\*, instance-profile/\*) + unconditioned `RunInstances` | Launch an instance with a higher-priv role attached, read its creds from IMDS → **privilege escalation to that role** |
| Holder of `EC2InstanceConnect` | Any instance's OS user (incl. `root`) account-wide | `ec2-instance-connect:SendSSHPublicKey` on `Resource:"*"`, no `InstanceOSUser`/tag condition | Push ephemeral SSH key to a non-owned instance's `root` → **interactive shell on any instance** |
| Holder of `AmazonEC2ReadOnlyAccess` / `AmazonEC2FullAccess` | Secrets embedded in instance `UserData` | `ec2:DescribeInstanceAttribute`/`Describe*` on `Resource:"*"` | Read plaintext UserData of a non-owned instance → **credential disclosure** |
| EICE SLR (`Ec2InstanceConnectEndpoint`) | **Any** security group in the account | `ec2:ModifyNetworkInterfaceAttribute` on `security-group/*` **with no condition** | SLR attaches/detaches an arbitrary SG onto an EICE ENI → **network control-plane tampering** |
| `AWSEC2CapacityManagerServiceRolePolicy` SLR | Whole-org account/structure read | `organizations:ListAccounts/DescribeOrganization` `Resource:"*"`, no org-condition-key (none exist) | SLR enumerates the entire AWS Organization structure with no org-scoping possible |
| Fleet/Spot/SpotFleet SLR | Any instance (`StartInstances`/`StopInstances`/`TerminateInstances` on `*`) | Unconditioned or presence-only (`"*"`) tag conditions | Service identity stops/starts/terminates instances not tagged to a fleet → **availability impact** |
| Fleet/Spot SLR | Any `elasticloadbalancing` target | `elasticloadbalancing:RegisterTargets` on `arn:...:*/*` (widest wildcard, no condition) | Register/deregister targets on a non-fleet load balancer → **traffic redirection / DoS** |
| Any EC2 admin w/ `ec2:CreateTags` | EICE/VSS/FastLaunch tag-gated resources | Forge `InstanceConnectEndpointId=eice-*` / `AwsVssConfig` / `CreatedBy` tags | Make an unrelated sensitive resource a valid target for an SLR's tag-scoped actions → **tag-forgery self-widening** |
| Holder of `AmazonEC2ImageReferencesAccessPolicy` | Account-wide SSM params / launch templates | 2nd stmt `Resource:"*"` gated only by `aws:CalledVia: ec2-images.amazonaws.com` | If `DescribeImageReferences` surfaces raw SSM/UserData values → cross-resource disclosure |
| **Any customer surface** | **AWS's own service plane** | SLR internal reconciliation | **HARD STOP** — any AWS fleet identity/credential/ARN = disclosure event |

---

## 3. Policy Inventory (the "API table" analogue)

| Policy | Class | Latest ver | Headline property | Weaponizable from docs? |
|---|---|---|---|---|
| `AmazonEC2FullAccess` | Attachable | v5 | `ec2:*`+`elb:*`+`cloudwatch:*`+`autoscaling:*` all `Resource:"*"` unconditioned; `CreateServiceLinkedRole` scoped to 6 principals; **NO `iam:PassRole`** | Yes (broad admin; refutes PassRole assumption) |
| `AmazonEC2ReadOnlyAccess` | Attachable | v5 | `ec2:Describe*`+`GetSecurityGroupsForVpc`+elb/cw/asg Describe, `Resource:"*"`; `GetPasswordData` NOT granted | Yes (UserData secret read) |
| `AmazonEC2ImageReferencesAccessPolicy` | Attachable | v3 | stmt2 `Resource:"*"` gated by `aws:CalledVia=ec2-images.amazonaws.com` | Hypothesis (response-content disclosure) |
| `EC2FastLaunchFullAccess` | Attachable | — | **`iam:PassRole` on role/\*+instance-profile/\* (PassedToService=ec2) + unconditioned `RunInstances`** | **Yes — HEADLINE privesc** |
| `AWSEC2VssSnapshotPolicy` | Attachable (on instance) | — | `CreateSnapshots` volume component unconditioned; `CreateTags` presence-only `AwsVssConfig:"*"` | Yes (cross-resource tag write, Low) |
| `EC2InstanceConnect` | Attachable | v1 (2019) | `SendSSHPublicKey` `Resource:"*"` **no condition at all** | **Yes — HEADLINE account-wide shell** |
| `DeclarativePoliciesEC2Report` | Attachable | — | pure read-only Describe\*/Get\* | Clean baseline |
| `AWSEC2CapacityManagerServiceRolePolicy` | SLR | v1 (NEW) | `organizations:*` read `Resource:"*"`; `ListDelegatedAdministrators` w/ `StringLikeIfExists`; **no `ec2:*`, no org-key, no PassRole** | Audit-incomplete (suspected sibling policy) |
| `AWSEC2CapacityReservationFleetRolePolicy` | SLR | v2 | CR actions gated by `ArnLike ec2:CapacityReservationFleet` (presence not ownership) | Fail-open hypothesis |
| `AWSEC2FleetServiceRolePolicy` | SLR | — | `RunInstances` `*` unconditioned; `PassRole` `*` (PassedToService only); `TerminateInstances` `*` w/ presence-only fleet-id | Fail-open hypothesis |
| `AWSEC2SpotFleetServiceRolePolicy` | SLR | — | same + **`elasticloadbalancing:RegisterTargets` on `arn:...:*/*`** (widest, no cond) | Fail-open hypothesis |
| `AWSEC2SpotServiceRolePolicy` | SLR | — | `RunInstances` Deny-unless `InstanceMarketType=spot` (good); but **`StartInstances`/`StopInstances` on `*` unconditioned** | Fail-open hypothesis (Medium availability) |
| `EC2FastLaunchServiceRolePolicy` | SLR | — | `PassRole` `Resource:"*"`; mutations gated by `CreatedBy="EC2 Fast Launch"` exact-value (good) | Low (defense-in-depth) |
| `Ec2InstanceConnectEndpoint` | SLR | v2 (2025-07-31) | `ModifyNetworkInterfaceAttribute` on `security-group/*` **unconditioned**; ENI side `StringLike eice-*` presence-only | **Yes-confirmable — SG fail-open** |
| *(suspected 15th / sibling)* | — | — | Capacity Manager EC2-action sibling not located in this page's audit | **Open — resolve first** |

> **Non-SDK / under-tested angle:** SLR policies are rarely audited by customers because they're not attachable and don't show in the console's policy picker — exactly the "tooling doesn't surface them" blind spot the skill flags. The Capacity Manager SLR is `[NEW]` (v1) → prime focus per the skill's "concentrate fire on new surface" rule.

---

## 4. Boundary-Lens Findings (question engine output)

### Lead 1 — `EC2FastLaunchFullAccess`: PassRole + RunInstances privilege escalation **[CRITICAL/HIGH — HEADLINE]**
**Lens:** B + E + R.
**Claim:** A holder of this *customer-attachable* policy can escalate to **any** EC2-trusted role in the account.
**Mechanism (verbatim):**
```json
{ "Sid": "EC2LaunchInstance", "Action": ["ec2:RunInstances"],
  "Resource": ["arn:aws:ec2:*:*:subnet/*","…:network-interface/*","…::image/*",
               "…:key-pair/*","…:security-group/*","…:launch-template/*","…license-configuration:*"]
  /* NO Condition block */ },
{ "Sid": "IAMSLRPassRole", "Action": "iam:PassRole",
  "Resource": ["arn:aws:iam::*:instance-profile/*","arn:aws:iam::*:role/*"],
  "Condition": { "StringEquals": { "iam:PassedToService": ["ec2.amazonaws.com","ec2.amazonaws.com.cn"] } } }
```
`PassRole` is constrained **only** by `PassedToService=ec2` — i.e. any role/instance-profile in the account that EC2 can assume. `RunInstances` has **no condition at all**. Chain: launch instance with a target high-priv instance profile → read SigV4 creds from IMDS → act as that role.
**Doc-vs-JSON drift:** per memory ([[ec2-security-hub-plan-note]]), the EC2-Security chapter's prose implies an `ec2fastlaunch`-name restriction that the JSON does **not** contain. The managed-policy page here prints the JSON straight — confirming the prose overclaims.
**Instance-profile amplifier:** if this policy is attached to an instance profile (plausible for launch/automation hosts), **any code on that instance** inherits the exact PassRole+RunInstances pair — SSRF/RCE on such a host → account-wide role pivot, not just fast-launch management.
**Oracle:** `iam:SimulatePrincipalPolicy`, `ActionNames=[iam:PassRole, ec2:RunInstances]`, `ResourceArns=[<any EC2-trusted role ARN>, arn:...:instance/*]`, `ContextEntries=[{iam:PassedToService: ec2.amazonaws.com}]` → expect `allowed`. No live launch.
**Severity:** High (Critical if a notably higher-priv role — e.g. an admin instance-profile — exists in the account).

### Lead 2 — `EC2InstanceConnect`: unconditioned account-wide SSH key push **[HIGH — HEADLINE]**
**Lens:** A + E + R.
**Claim:** Holder can push an ephemeral SSH key for **any** OS user (`root`, `ec2-user`, …) to **any** EC2 instance in the account.
**Mechanism (verbatim, v1, unchanged since 2019):**
```json
{ "Sid": "EC2InstanceConnect", "Effect": "Allow",
  "Action": ["ec2:DescribeInstances","ec2-instance-connect:SendSSHPublicKey"],
  "Resource": "*" }
```
No `ec2-instance-connect:InstanceOSUser` condition, no `ec2:ResourceTag` scoping — **both keys exist** in `list_ec2-instance-connect.md` and are used in modern scoped policies, but not here. "Push an SSH key" is routinely under-rated; it is equivalent to interactive shell on every Instance-Connect-capable instance account-wide, as any OS user.
**Oracle:** `iam:SimulatePrincipalPolicy`, `ActionNames=ec2-instance-connect:SendSSHPublicKey`, `ResourceArns=<arbitrary non-owned instance ARN>`, `ContextEntries=[{ec2-instance-connect:InstanceOSUser: "root"}]` → expect `allowed`.
**Severity:** High. This is the policy's entire grant *by design/name* — but it is a Tier-2-worthy AWS default: the policy ships zero scoping where two scoping keys exist.

### Lead 3 — `Ec2InstanceConnectEndpoint` SLR: security-group side fail-open **[HIGH — directly confirmable]**
**Lens:** S + X (action-family parity).
**Claim:** `ec2:ModifyNetworkInterfaceAttribute` requires authz on **two** resource types (the ENI and the SG being attached). The ENI side is scoped to `eice-*`-tagged ENIs; the **SG side carries no condition at all**:
```json
{ "Action": "ec2:ModifyNetworkInterfaceAttribute",
  "Resource": "arn:aws:ec2:*:*:security-group/*" /* NO Condition */ }
```
So even with ENI-targeting perfectly contained, the SLR can attach **any** security group in the account onto an EICE ENI (or detach a restrictive one) — asymmetric authorization gap, confirmable by simulation with **no** forgery/service-internals assumption.
**Oracle:** `iam:SimulateCustomPolicy`, `ActionNames=ec2:ModifyNetworkInterfaceAttribute`, `ResourceArns=[<eice-owned ENI ARN>, <arbitrary unrelated SG ARN>]` → expect `allowed`.
**Severity:** High (network control-plane tampering via an AWS SLR).

### Lead 4 — `Ec2InstanceConnectEndpoint` SLR: Null→StringLike swap narrows value-shape, not ownership **[MEDIUM — fail-open hypothesis]**
**Lens:** S + U + AA.
**Claim:** The documented condition change from `Null` to `StringLike "eice-*"` excludes garbage tag values but does **not** bind to the specific endpoint in the current request — it matches **any** EICE's ID. All of `ModifyNetworkInterfaceAttribute`, `AssignIpv6Addresses`/`UnassignIpv6Addresses`, and `DeleteNetworkInterface` key on the identical static `StringLike aws:ResourceTag/InstanceConnectEndpointId: ["eice-*"]` with no per-request binding. IAM cannot distinguish the SLR's authority over one EICE's ENI from every other EICE's ENI in the account.
**Tag-forgery precondition:** because the gate is a bare value-pattern (not a non-forgeable linkage), **any principal with ordinary `ec2:CreateTags` on network-interfaces** could tag an unrelated sensitive ENI (NAT GW, Lambda ENI) with `InstanceConnectEndpointId=eice-anything`, making it a valid target *if* the EICE control plane ever reconciles by tag-query rather than by its stored EICE→ENI mapping.
**Oracle (precondition only):** `iam:SimulateCustomPolicy` for the SLR, `ResourceArns=<ENI tagged for a different EICE>`, context `aws:ResourceTag/InstanceConnectEndpointId=eice-OTHER` → `allowed` confirms cross-endpoint reach. Whether the service is actually tricked depends on un-auditable internals → **flag for service team, documentation cannot resolve.**
**Severity:** Medium (same-account cross-EICE; per-account tag namespace, not cross-tenant).

### Lead 5 — `AWSEC2SpotServiceRolePolicy`: unconditioned Start/StopInstances **[MEDIUM — strongest SLR Lens-R finding]**
**Lens:** R + S.
**Claim:** The policy correctly Denies `RunInstances` unless `ec2:InstanceMarketType=spot` (good compensating control) — **but** `ec2:StartInstances` and `ec2:StopInstances` are granted on `Resource:"*"` with **no condition and no Deny**. The spot-market guardrail does not extend to start/stop. The SLR identity can stop/start **any** instance in the account, spot or not.
**Oracle:** `iam:SimulateCustomPolicy`, `ActionNames=[ec2:StopInstances]`, `ResourceArns=<non-spot instance ARN>` → expect `allowed`.
**Severity:** Medium (availability; fail-open hypothesis gated by whether the SLR is externally reachable, which it is not directly).

### Lead 6 — `AWSEC2SpotFleetServiceRolePolicy`: widest `elasticloadbalancing:RegisterTargets` wildcard **[MEDIUM]**
**Lens:** X + R.
**Claim:** `elasticloadbalancing:RegisterTargets` is granted on `arn:aws:elasticloadbalancing:*:*:*/*` — the broadest possible ELB wildcard — with **no condition**. `RegisterInstancesWithLoadBalancer` is comparatively scoped to `loadbalancer/*`. The SLR could register/deregister targets on a load balancer unrelated to any spot fleet → traffic redirection or target-group DoS.
**Oracle:** `iam:SimulateCustomPolicy`, `ActionNames=elasticloadbalancing:RegisterTargets`, `ResourceArns=<arbitrary non-fleet target-group ARN>` → expect `allowed`.
**Severity:** Medium (cross-resource within account; fail-open).

### Lead 7 — `AWSEC2CapacityManagerServiceRolePolicy` (NEW v1): org-wide read, no org-scoping possible **[MEDIUM — audit incomplete, resolve first]**
**Lens:** AA + U + R.
**Claim:** This brand-new SLR grants `organizations:ListAccounts / ListChildren / ListAWSServiceAccessForOrganization / DescribeOrganization` on `Resource:"*"` with **no condition**, plus `organizations:ListDelegatedAdministrators` gated by `StringLikeIfExists organizations:ServicePrincipal=ec2.capacitymanager.amazonaws.com`. It contains **no `ec2:*` actions, no PassRole, no KMS, and no org-condition-key** (none exist in EC2 anyway). The SLR can enumerate the **entire AWS Organization** structure.
**Two sub-questions:**
- (a) `StringLikeIfExists` is a **presence-skip** operator: when `organizations:ServicePrincipal` is absent from the request context, the condition is skipped and the action is allowed unscoped. Does any `ListDelegatedAdministrators` call path omit that context key → fail-open? (Lens S / IfExists fail-open, cf. [[iom-policies-for-amazon-ec2-plan-note]] finding on `IfExists`.)
- (b) An SLR with **only** org-read actions and no EC2 actions strongly implies a **sibling policy** carries the EC2 capacity actions. The audit of this page did not locate that sibling → **the Capacity Manager role's full permission set is not yet characterized.** This is the top open item.
**Oracle:** `iam:SimulateCustomPolicy` for (a) omitting the service-principal context key → check `allowed`. For (b): enumerate attached policies of the Capacity Manager SLR via `iam:ListAttachedRolePolicies` (read-only) — out of this doc's scope, flag for the hunter.
**Severity:** Medium (org-structure disclosure); escalate if sibling policy proves over-broad.

### Lead 8 — `AmazonEC2FullAccess` v5: broad cross-service admin, but **NO PassRole** **[informational — refutes an assumption]**
**Lens:** R + U.
**Finding:** `ec2:*`, `elasticloadbalancing:*`, `cloudwatch:*`, `autoscaling:*` all `Resource:"*"` unconditioned; `iam:CreateServiceLinkedRole` is correctly scoped to 6 named service principals; **there is no `iam:PassRole` statement.** This **refutes** the common assumption that EC2FullAccess enables a trivial PassRole privesc. Privesc from EC2FullAccess, if any, must route through `RunInstances`+an instance profile the principal can already pass via a *separate* policy, or through `autoscaling`/`elb` SLR creation — not through this policy directly. Record as a null/refutation so a future hunter doesn't chase it.
**Severity:** Informational (broad by design; documented).

### Lead 9 — `AmazonEC2ReadOnlyAccess` v5 + `AmazonEC2ImageReferencesAccessPolicy` v3: read-path secret disclosure **[LOW–MEDIUM]**
**Lens:** T + A.
**Claim (ReadOnly):** `ec2:Describe*` on `Resource:"*"` includes `DescribeInstanceAttribute`/`DescribeLaunchTemplateVersions`, which return plaintext **UserData** — a well-known place customers embed bootstrap secrets. A read-only principal reads any instance's UserData account-wide. (`GetPasswordData` is **not** granted — good.)
**Claim (ImageReferences):** stmt2 (`DescribeInstances`, `DescribeLaunchTemplates`, `DescribeLaunchTemplateVersions`, `ssm:DescribeParameters`, `ssm:GetParameters`, `imagebuilder:ListImageRecipes/ListContainerRecipes/GetContainerRecipe`) is `Resource:"*"` gated **only** by `ForAnyValue:StringEquals aws:CalledVia: ec2-images.amazonaws.com`. `aws:CalledVia` is call-chain provenance (confused-deputy-safe, not forgeable directly) — **but** stmt1 `ec2:DescribeImageReferences` is `Resource:"*"` with **no** condition. Open hypothesis: does the `DescribeImageReferences` *response* surface raw SSM parameter values or UserData? If yes, it is an account-wide read oracle for `ssm:GetParameters`-class data reachable without the caller holding `ssm:GetParameters` directly.
**Oracle:** doc-level — inspect `DescribeImageReferences` response schema in `list_ec2.md` / API reference for embedded parameter/UserData fields. Runtime confirm = `iam:SimulatePrincipalPolicy` for the Describe actions + response-content inspection (hunter, synthetic data).
**Severity:** Low (UserData read is documented ReadOnly behavior) → Medium if ImageReferences leaks SSM values.

### Lead 10 — Fleet/SpotFleet/CapacityReservationFleet SLRs: presence-only tag + PassRole scoping **[LOW — fail-open hypotheses]**
**Lens:** S + B.
**Findings (verbatim conditions):**
- `AWSEC2FleetServiceRolePolicy`: `RunInstances` on `*` unconditioned; `iam:PassRole` on `*` gated only by `iam:PassedToService=ec2.amazonaws.com[.cn]`; `TerminateInstances` on `*` gated by `StringLike ec2:ResourceTag/aws:ec2:fleet-id "*"` (**presence of the tag key, any value** — not ownership).
- `AWSEC2CapacityReservationFleetRolePolicy` v2: Create/Cancel/Modify on `capacity-reservation/*` gated by `ArnLike ec2:CapacityReservationFleet: arn:aws:ec2:*:*:capacity-reservation-fleet/crf-*` — **ArnLike is input-format hardening, not ownership**; `crf-*` matches any CRF.
- Common pattern: `CreateTags` gated by `ec2:CreateAction` (correct create-time binding).
**Claim:** The `"*"`-value tag conditions and `ArnLike crf-*` gate authorize the SLR against any resource merely *carrying* the tag/ARN shape, not resources belonging to the specific fleet in the request. Classic Lens-S presence-vs-ownership gap. Whether exploitable depends on the service reconciling by tag-query vs stored IDs (un-auditable from docs).
**Oracle:** `iam:SimulateCustomPolicy` with a target tagged `aws:ec2:fleet-id=<different-value>` → `allowed` confirms the presence-only semantics.
**Severity:** Low (SLR, not directly reachable; fail-open hypothesis).

### Lead 11 — `EC2FastLaunchServiceRolePolicy` + `AWSEC2VssSnapshotPolicy`: ownership-bound (controls hold) + two minor gaps **[LOW / informational]**
**Lens:** S.
- `EC2FastLaunchServiceRolePolicy`: `PassRole` on `Resource:"*"` (broadest shape) **but** this is an SLR only `ec2fastlaunch.amazonaws.com` can assume, and all mutations (`CreateSnapshot`, `DeleteSnapshot`, `DeleteVolume`, `DeleteNetworkInterface`, `Stop/TerminateInstances`) are gated on `StringEquals aws:ResourceTag/CreatedBy="EC2 Fast Launch"` (**exact value** = genuine ownership binding). Control holds. The `Resource:"*"` PassRole is a defense-in-depth nit (could have been scoped), not an exploit.
- `AWSEC2VssSnapshotPolicy` (attached to the role on Windows instances → any code on instance holds it): `ec2:CreateSnapshots`' **volume component is unconditioned** (`volume/*`, no tag/ARN/instance binding) — relies on API semantics (volumes attached to self-matched `InstanceId`) not IAM. Sibling `CreateSnapshotsAccessInstance` correctly self-binds via `ArnLike ec2:SourceInstanceARN=.../${ec2:InstanceId}`. Separately, `CreateTags` is gated by **presence-only** `StringLike ec2:ResourceTag/AwsVssConfig: "*"` with no self-binding → any instance holding this role can set `AppConsistent`/`Device` tags on **any** snapshot/image account-wide carrying an `AwsVssConfig` tag (cross-ownership tag write, but blast radius = two benign tag values, no delete/exfil).
**Oracle:** `iam:SimulateCustomPolicy` with a victim volume ARN / cross-instance snapshot ARN → `allowed`.
**Severity:** Low.

### Lens null hypotheses (checked, no finding — pages named)
- **Lens G (SSRF / server-dereferenced URL):** N/A — read all 15 policy JSONs; no policy contains a URL/host/endpoint field the service dereferences. Managed-policy artifacts carry no such field.
- **Lens Q (upload/blob parse):** N/A — no blob/attachment field in any policy document.
- **Lens P (identity-proofing / OTP gate):** N/A for this page — no challenge/code/one-per-account gate; the only gating primitives are IAM conditions (covered under R/S).
- **Lens F (translation-layer injection):** N/A — these are declarative JSON artifacts, not a transform of untrusted input.
- **Lens D (data→control-plane escape):** N/A at the artifact level — but the SLR fail-open hypotheses (Leads 3–6, 10) are the policy-layer shadow of this; actual escape would require service-internal reconciliation behavior (out of scope / HARD STOP if it touches AWS fleet identity).
- **DeclarativePoliciesEC2Report:** clean — pure `Describe*`/`Get*` read-only, no mutation, no cross-resource reach. Documented baseline.

---

## 5. Prioritized NEW / changed surface (concentrate fire)

1. **`EC2FastLaunchFullAccess` PassRole→privesc (Lead 1)** — highest weaponizability; customer-attachable; prose-vs-JSON drift already memory-noted. **Confirm first.**
2. **`EC2InstanceConnect` unconditioned SendSSHPublicKey (Lead 2)** — account-wide shell; trivially confirmable by simulation.
3. **`Ec2InstanceConnectEndpoint` SG-side fail-open (Lead 3)** — directly confirmable, no service-internals assumption; and its Null→StringLike change (Lead 4) is the only `[NEW]`-dated edit (2025-07-31) on this page besides the Capacity Manager SLR.
4. **`AWSEC2CapacityManagerServiceRolePolicy` (NEW v1, Lead 7)** — brand-new surface; **audit incomplete** → locate the EC2-action sibling policy and the `[NEW]` 15th policy before concluding.
5. **SLR fail-open hypotheses (Leads 5, 6, 10)** — Medium/Low, batch-confirmable by simulation, but gated by un-auditable service internals.
6. **Read-path disclosure (Lead 9)** — resolve the `DescribeImageReferences` response-schema question from the API reference.

---

## 6. Open items / doc-gaps for the next agent

- **The 15th policy / Capacity Manager sibling is uncharacterized.** The page lists 15 policies; this audit fully resolved 14. An SLR with only org-read actions (Lead 7) implies a sibling policy holds the EC2 capacity actions. **Action:** re-read `security-iam-awsmanpol.md` top-to-bottom for the policy name count, then resolve each un-audited policy's JSON via its `.md` twin at `docs/service-authorization/.../` or the policy-reference pages. Do not conclude Capacity Manager is "org-read-only" until the sibling is found.
- **Un-auditable service internals (HARD STOP boundary):** Leads 3–7 and 10 all hinge on whether each AWS SLR's control plane reconciles targets by **tag-query** (fail-open to forgery/presence) or by **stored resource ID** (safe). Documentation cannot settle this. The simulation oracles confirm the *IAM-layer* gap exists; actual exploitation requires behavioral testing by an authorized hunter, and the moment any observation surfaces an AWS fleet identity → **stop and disclose.**
- **Tag-forgery precondition (Lead 4):** whether `ec2:CreateTags` on network-interfaces is widely held in a target account is account-specific; the hunter should check the account's own policies.
- **`DescribeImageReferences` response content (Lead 9):** confirm from the EC2 API reference whether the response embeds raw SSM parameter / UserData values.
- **All oracles are `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — non-mutating, no resources created, no live launch. This entire plan is confirmable without mutating any EC2 state.

---

## 7. One-line confirm recipes (copy-paste ready for the hunter)

| Lead | `aws iam simulate-custom-policy` essentials |
|---|---|
| 1 | policy-input-list=`EC2FastLaunchFullAccess` JSON; action-names `iam:PassRole`,`ec2:RunInstances`; resource-arns `<target-role>`,`instance/*`; context `iam:PassedToService=ec2.amazonaws.com` → expect `allowed` |
| 2 | principal=`EC2InstanceConnect` holder; action `ec2-instance-connect:SendSSHPublicKey`; resource `<non-owned instance ARN>`; context `ec2-instance-connect:InstanceOSUser=root` → `allowed` |
| 3 | policy=`Ec2InstanceConnectEndpoint`; action `ec2:ModifyNetworkInterfaceAttribute`; resources `[eice-ENI, arbitrary-SG]` → `allowed` |
| 5 | policy=`AWSEC2SpotServiceRolePolicy`; action `ec2:StopInstances`; resource `<non-spot instance>` → `allowed` |
| 6 | policy=`AWSEC2SpotFleetServiceRolePolicy`; action `elasticloadbalancing:RegisterTargets`; resource `<non-fleet target-group>` → `allowed` |
| 7a | policy=`AWSEC2CapacityManagerServiceRolePolicy`; action `organizations:ListDelegatedAdministrators`; **omit** `organizations:ServicePrincipal` context → check `allowed` (IfExists fail-open) |
| 10 | policy=`AWSEC2FleetServiceRolePolicy`; action `ec2:TerminateInstances`; resource tagged `aws:ec2:fleet-id=<different-value>` → `allowed` (presence-only) |

---

## 8. Summary for a cold-start agent

This page ships 15 AWS-authored IAM artifacts. The two directly weaponizable, customer-attachable defects are **`EC2FastLaunchFullAccess`** (unconditioned `RunInstances` + `PassRole` on `role/*` → privesc to any EC2-trusted role, amplified if attached to an instance profile) and **`EC2InstanceConnect`** (`SendSSHPublicKey` on `Resource:"*"`, zero scoping → account-wide `root` shell). The clearest SLR defect, confirmable by pure simulation, is **`Ec2InstanceConnectEndpoint`**'s unconditioned `security-group/*` side of `ModifyNetworkInterfaceAttribute`. The brand-new **`AWSEC2CapacityManagerServiceRolePolicy`** grants whole-Organization read with no org-condition-key (EC2 has none) and is **not fully audited** — its EC2-action sibling policy must be located. The remaining SLRs (`Fleet`/`SpotFleet`/`Spot`/`CapacityReservationFleet`) share a presence-only / `ArnLike crf-*` / `"*"`-value tag-scoping pattern that is fail-open at the IAM layer but gated by un-auditable service internals. `AmazonEC2FullAccess` notably contains **no PassRole** (refuting a common assumption). Every lead resolves via `iam:SimulateCustomPolicy`/`iam:SimulatePrincipalPolicy` with no mutation and no live launch. Hard stop and disclose if any observation surfaces an AWS fleet identity/credential/ARN.
