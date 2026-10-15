# Amazon EC2 — "Example policies to control access to the EC2 console" — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-ec2-console.html` (offline mirror `docs/AWSEC2/latest/UserGuide/iam-policies-ec2-console.md`, 449 lines). Cross-checked statement-by-statement against the AWS IAM service-authorization reference `docs/service-authorization/latest/reference/list_ec2.md`. Live `.md` is **byte-identical** to the offline mirror (verified via WebFetch 2026-10-15 — no sync drift).
Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This page is a gallery of **five AWS-authored sample IAM policies that customers copy verbatim** into their accounts. Per the security-questionbuilder Lens R/S/U carve-out, a weak default in an AWS-authored copy-verbatim artifact is **in scope and reportable (disclosure Tier 2)** — it is *not* a "customer footgun" even though the blast radius is intra-account. That carve-out is what makes the headline lead reportable.
- Everything here is **intra-account least-privilege / false-sense-of-restriction** (Lens R/S/U). There is **no cross-tenant or service-plane surface** on this page — see §7.
- **Primary oracle for every lead = `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** (non-mutating; honors EC2 resolve-to-`*` / IfExists / resource-AND semantics). Escalate to a live scoped call only with canary data, under a role holding **exactly** the sample policy (never the over-privileged tester).
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected to fire on this page.)

## 0a. Relationship to sibling plans (do NOT re-chase)
This page sits between three already-covered EC2 IAM pages. Read those notes first; this plan only claims what is **net-new to the console sample set**:
- `ExamplePolicies_EC2-attack-research-plan.md` — the general sample-policy gallery. Owns: Spot untagged resource-non-evaluation **fail-open** (H1), IMDS `$Latest`/`$Default` Auto-Scaling bypass (H2), PassRole prefix-privesc (H3), hop-limit Deny gates only RunInstances (H4). **Do not restate.**
- `iam-policies-for-amazon-ec2-attack-research-plan.md` — condition-key **evaluation semantics**. Owns: resolve-to-`*` ResourceID fail-open, `ec2:Attribute` case-sensitivity fail-open, `AssociateSecurityGroupVpc` destination-VPC unscopable, ABAC self-widen mechanism. **Do not restate.**
- `ec2-security-iam` HUB — owns S1 (ResourceID fail-open), C4/#6 (ABAC self-widen), #2 (FullAccess→userData→IMDS).

**What THIS page uniquely contributes:** the console samples pair a *scoped* "action" statement (RunInstances / rule-modify gated by tag or ARN) with a *silently unscoped* "setup" statement (`Resource:"*"` Describe + **CreateSecurityGroup + AuthorizeSecurityGroupIngress + CreateKeyPair**). The gap between what the policy's *title/prose promises* ("Restrict access to a specific instance type, subnet, and Region") and what the `Resource:"*"` setup statement *actually grants* (open any SG account-wide) is the headline, and it exists **only** in the console-oriented samples because the console needs those extra Describe/Create actions to render its wizards.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce, each under a role holding exactly one of the five sample policies:
1. **A1 — Network-exposure escalation hidden by a "restriction":** holding the policy titled *"Restrict access to a specific instance type, subnet, and Region,"* add an inbound `0.0.0.0/0` rule (SSH/RDP/DB port) to a security group the user has no other relationship to — e.g. the SG protecting a production database. The policy's own title claims the user is restricted to launching `t2.micro` in one subnet.
2. **A2 — SG land-grab:** holding any launch-wizard sample, create security groups in arbitrary VPCs account-wide.
3. **A3 — ABAC defeat chain:** holding the launch-wizard sample *plus* `ec2:CreateTags` (which the console requires to set an instance **Name**), re-tag an arbitrary security group to `Department=Test`, then — holding the *security-groups* sample — modify that SG's rules the tag was meant to protect.
4. **A4 — Account-wide SSM parameter enumeration + over-broad secret read** via the AMI-selection SSM policy.
5. **A5 — Unscopable spend:** holding the Reserved-Instances sample, purchase Reserved Instances (financial commitment) — confirm no resource-level control is possible on the purchase action.
6. **A6 — Confirm/refute the SG-rule AND-semantics "fail-open":** prove whether the unconditioned `security-group-rule/*` statement in the security-groups sample lets rules be modified on a **non-`Department=Test`** SG (expected: refuted — fails closed on the SG-resource gate).

---

## 2. Components, Assets, and Design
**Interface:** AWS Management Console → EC2 service → multiple `ec2:*` (and `cloudwatch:*`, `ssm:*`) control-plane API calls per screen. No service fleet, no data plane, no network interfaces in scope — this page is purely an **IAM identity-policy authoring surface**.

**Assets:** the five copy-verbatim policy documents themselves. Each is an attack surface because the customer attaches it unmodified:
| # | Sample | Scoped action(s) | Silently-unscoped setup statement |
|---|---|---|---|
| 1 | Read-only (two variants) | `ec2:Describe*` (unscopable by design) + `cloudwatch:*` | — |
| 2 | Launch wizard — basic | `ec2:RunInstances` on `Resource:"*"` | `Describe*`, **CreateSecurityGroup, AuthorizeSecurityGroupIngress, CreateKeyPair** on `Resource:"*"` |
| 3 | Launch wizard — **"Restrict to t2.micro/subnet/Region"** | `RunInstances` gated by subnet ARN + `ec2:InstanceType` + `ec2:Owner=amazon` | **Same `Resource:"*"` CreateSecurityGroup + AuthorizeSecurityGroupIngress + CreateKeyPair** ← **headline** |
| 3b | SSM-parameter AMI selection | `ssm:GetParameters` on `parameter/prod-*` | `ssm:DescribeParameters` on `Resource:"*"` |
| 4 | Security groups — view+modify rules | rule actions gated by `aws:ResourceTag/Department=Test` on `security-group/*` | `ec2:ModifySecurityGroupRules` on `security-group-rule/*` **unconditioned** (3rd stmt) |
| 4b | Create Security Group dialog | Delete/Authorize gated by `ArnEquals ec2:Vpc=vpc-…` | `CreateSecurityGroup` on `Resource:"*"` (any VPC) |
| 5 | Reserved Instances | all on `Resource:"*"` incl. `PurchaseReservedInstancesOffering` | (no resource type exists for the purchase action) |

**Identity model:** standard IAM principal in the customer account. The only "privilege levels" are what each sample grants. No roles assumed, no PassRole on this page, no cross-account anything.

**Why the console angle matters:** the page's own opening paragraph states *"The console uses additional API actions for its features"* — i.e. these samples deliberately grant **more** than the task needs so the console UI renders. That is precisely the mechanism that smuggles the `Resource:"*"` CreateSecurityGroup/AuthorizeSecurityGroupIngress grants into a policy sold as a restriction.

---

## 3. API / Interface Inventory (scopability from `list_ec2.md`, verified)
| Action | Required resource(s) | Can it be condition-scoped? | How the sample grants it | Gap |
|---|---|---|---|---|
| `ec2:Describe*` | none / `*` | **No** (no resource-level perms) | `Resource:"*"` | By-design unscopable (Lens U null) |
| `ec2:RunInstances` | instance, image, subnet, SG, NI, volume, key-pair | **Yes** (per-resource + `ec2:InstanceType`,`ec2:Owner`) | scoped in sample 3 | correctly scoped |
| `ec2:AuthorizeSecurityGroupIngress` | `security-group*` (req) + `security-group-rule` (opt) | **Yes** — `ec2:Vpc`,`ec2:SecurityGroupID`,`aws:ResourceTag` | **`Resource:"*"`, NO condition** (samples 2,3) | **HEADLINE — open any SG** |
| `ec2:CreateSecurityGroup` | `security-group*` + `vpc` | **Yes** — `ec2:VpcID`,`ec2:Tenancy`,`aws:ResourceTag` | `Resource:"*"`, no condition | create SG in any VPC |
| `ec2:CreateKeyPair` | `key-pair*` | **Yes** — `ec2:KeyPairType`,`aws:RequestTag` | `Resource:"*"`, no condition | minor |
| `ec2:ModifySecurityGroupRules` | `prefix-list*` **AND** `security-group*` **AND** `security-group-rule*` (all required) | SG row scopable; rule row only `ResourceTag`; prefix-list row scopable | SG via tag (stmt 2) + rule unconditioned (stmt 3); **prefix-list NOT granted** | AND-semantics (Lead B) |
| `ssm:DescribeParameters` | `*` | account-wide only | `Resource:"*"` | enumeration leak (Lead C) |
| `ssm:GetParameters` | `parameter/…` | **Yes** by name prefix | `parameter/prod-*` | over-broad for AMI use case |
| `ec2:AllocateAddress` | `elastic-ip*` (+ ipam-pool / ipv4pool) | only `aws:RequestTag` on the EIP | `Resource:"*"` | unscopable at allocate (matches EIP sibling) |
| `ec2:AssociateAddress` | elastic-ip, instance, network-interface | **Yes** — `ec2:InstanceID`,`ec2:Subnet`,… | `Resource:"*"` | can bind EIP to any instance (intra-acct) |
| `ec2:PurchaseReservedInstancesOffering` | **none** | **No** (only `ec2:Region`) | `Resource:"*"` | genuinely unscopable spend (Lead E) |
| `ec2:ModifyReservedInstances` | `reserved-instances*` | **Yes** — `ec2:ResourceTag`,`ec2:InstanceType`,… | `Resource:"*"` | **doc says "not possible"; API disagrees** (Lead F) |

---

## 4. Trust-Boundary Map
| From (actor) | To (resource) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| low-priv console user (sample 3) | any security group account-wide | `AuthorizeSecurityGroupIngress` on `Resource:"*"` | an inbound rule appears on a SG the user has no RunInstances/tag relationship to → **boundary broke** |
| low-priv console user | SGs/key-pairs in arbitrary VPCs | `CreateSecurityGroup`/`CreateKeyPair` `Resource:"*"` | resource created outside the "restricted" subnet/VPC |
| user w/ CreateTags (Name field) | tag-gated resources (ABAC) | retag → defeat `aws:ResourceTag` gate | modify-rules succeeds on a formerly-protected SG after retag |
| console user | all SSM parameter names account-wide | `ssm:DescribeParameters` `Resource:"*"` | parameter inventory returned that the EC2 policy otherwise denies |
| console user | account billing | `PurchaseReservedInstancesOffering` (no resource) | purchase succeeds; no policy can prevent it |

**No cross-account, no data→control-plane, no network boundary on this page.**

---

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE, Tier-2 High] "Restricted" launch policy silently grants account-wide `AuthorizeSecurityGroupIngress`
**Background:** The sample titled *"Restrict access to a specific instance type, subnet, and Region"* (mirror l.164-219) carefully scopes `RunInstances` to `subnet-1a2b3c4d`, `t2.micro`, and `ec2:Owner=amazon`. Its **first statement**, however, grants `ec2:CreateSecurityGroup`, `ec2:AuthorizeSecurityGroupIngress`, and `ec2:CreateKeyPair` on `Resource:"*"` with **no condition** — because the console wizard needs them to render the "create/select security group" screen.
**Security Concern:** `AuthorizeSecurityGroupIngress` requires only the `security-group*` resource (confirmed `list_ec2.md` l.4894-4897) and is fully condition-scopable (`ec2:Vpc`, `ec2:SecurityGroupID`, `aws:ResourceTag`). On `Resource:"*"` with no condition, the "restricted" user can **add an inbound rule to any security group in the account** — including SGs attached to production databases, bastions, or other teams' instances the user cannot otherwise touch. Opening `0.0.0.0/0:22` or a DB port on a shared SG is a direct network-exposure escalation. The policy's **title and prose assert a restriction that the setup statement silently voids** (Lens U documented-guarantee vs actual-enforcement + Lens S unconditioned broad grant). Same defect is present in the "basic launch wizard" sample (l.111-138), but there the framing is honest ("basic access"); it is the **"Restrict…"** sample where the title makes it reportable.
**High-level Test Scenarios:**
- **Claim:** a principal holding *only* this sample can `AuthorizeSecurityGroupIngress` on a security group outside `subnet-1a2b3c4d` / not owned by the user. → **Oracle:** `iam:SimulateCustomPolicy` with the sample + `action=ec2:AuthorizeSecurityGroupIngress` + `resource=arn:…:security-group/<any-sg>` → expect **allowed**. Confirm live by adding a canary ingress rule to a canary "prod" SG; the rule appearing is the breach. → **Severity: High** (intra-account, but AWS-authored copy-verbatim artifact → Tier 2 reportable).
- Adjacent: same for `AuthorizeSecurityGroupEgress` if the operator added it per the "you can add" prose (l.145); and `CreateSecurityGroup`/`CreateKeyPair` land-grab (Area 2).
**Doc evidence:** mirror l.167-181 (first statement `Resource:"*"`); `list_ec2.md` l.4894-4897 (SG* required, Vpc/ResourceTag scopable). **Severity-if-true: High.** **Stop condition:** one canary SG gains a rule it should not; do not touch any real SG.

### Area 2 — [Tier-2 Medium] `CreateSecurityGroup` / `CreateKeyPair` land-grab across VPCs
**Background:** Every launch-wizard sample and the "Create Security Group dialog" sample (l.342-368) grant `ec2:CreateSecurityGroup` on `Resource:"*"`. The dialog sample's prose says *"Users can create security groups for a VPC"* (singular, implying the pinned `vpc-1a2b3c4d`), but only the **rule-authorization** statement carries the `ArnEquals ec2:Vpc` condition — `CreateSecurityGroup` is unconditioned in statement 1.
**Security Concern:** `CreateSecurityGroup` is scopable by `ec2:VpcID`/`ec2:Tenancy` (`list_ec2.md`) but the sample pins nothing, so the user creates empty SGs in **any** VPC in the account. Combined with Area 1 (open the SG wide), this is "create and expose" anywhere. `CreateKeyPair` on `Resource:"*"` is lower impact but lets the user mint key material and fill the account's key-pair namespace.
**High-level Test Scenarios:** `SimulateCustomPolicy` → `CreateSecurityGroup` allowed on a VPC other than `vpc-1a2b3c4d`. **Severity: Medium.**
**Doc evidence:** l.344-352; `list_ec2.md` CreateSecurityGroup (security-group* + vpc, VpcID scopable). **Stop condition:** one canary SG created outside the pinned VPC.

### Area 3 — [Tier-2 Medium, CHAIN] `ec2:CreateTags` (instance Name) → ABAC self-widen → defeat the security-groups `Department=Test` gate
**Background:** The launch-wizard section (l.147-148 **Important** callout) states that specifying a **Name** at launch *"creates a tag and requires the `ec2:CreateTags` action"* and warns that granting `CreateTags` *"limits your ability to use the `aws:ResourceTag` condition key… they can change a resource's tag to bypass those restrictions."* The **security-groups** sample (l.271-313) relies on exactly that key: it gates rule modification on `aws:ResourceTag/Department=Test`.
**Security Concern:** A console operator who wants users to name their instances will add `ec2:CreateTags` (the console forces this). A principal holding both samples can then `CreateTags` to stamp `Department=Test` onto **any** security group, then use the security-groups sample's statement 2 to modify that SG's rules — defeating the tag gate. This is the known ABAC self-widen (hub C4/#6), but the **console-specific delivery** (Name field → mandatory CreateTags grant → cross-sample chain into the tag-gated SG policy) is net-new and worth emitting as a chain.
**High-level Test Scenarios:** grant {launch-wizard + `ec2:CreateTags` on `Resource:"*"`} + security-groups sample → `SimulateCustomPolicy`/live: `CreateTags Department=Test` on a non-Test SG, then `AuthorizeSecurityGroupIngress`/`ModifySecurityGroupRules` on it → expect **allowed**. **Severity: Medium** (AWS pre-admits the mechanism; rate on the chain's end impact = SG rule mutation on an unintended SG).
**Doc evidence:** l.147-148, l.297-301. **Stop condition:** canary SG retagged and its rules changed once.

### Area 4 — [Medium] SSM-parameter AMI-selection policy over-grants
**Background:** To let users pick an AMI via SSM parameters, the page (l.149, l.234-253) adds `ssm:DescribeParameters` on `Resource:"*"` and `ssm:GetParameters` on `parameter/prod-*`.
**Security Concern:** (a) `ssm:DescribeParameters` on `Resource:"*"` returns **every parameter name + metadata in the account** — parameter names/descriptions routinely disclose infra topology, secret-store layout, DB endpoints (Lens A info-disclosure); nothing about AMI selection needs account-wide parameter enumeration. (b) `ssm:GetParameters` on `parameter/prod-*` lets the user read the **values** of all `prod-*` parameters — if any are `SecureString` application secrets rather than AMI-ID pointers, this is a cross-purpose secret read (Lens T), bounded only by whether the caller also holds `kms:Decrypt` on the backing key. The sample grants far more than "select an AMI."
**Refute note (whoAMI / `resolve:ssm`):** could a user point the launch at an **attacker-controlled** AMI via an SSM parameter? On the restricted sample (Area 1's policy), `RunInstances` is still gated by `ec2:Owner=amazon`, so even an SSM-resolved AMI must be Amazon-owned → **fail-closed, refuted**. On the *basic* wizard sample (no `ec2:Owner` gate) the resolved AMI is unconstrained, but that is the honestly-"basic" policy. Record as refuted-for-restricted.
**High-level Test Scenarios:** `SimulateCustomPolicy` → `ssm:DescribeParameters` allowed on `*`; enumerate canary parameter names. `GetParameters` on a canary `prod-secret` SecureString → confirm read (and whether KMS blocks it). **Severity: Medium** (info-disclosure; High only if `prod-*` holds decryptable secrets).
**Doc evidence:** l.235-252.

### Area 5 — [Low / Informational] Reserved-Instances sample: unscopable spend + doc-vs-API inconsistency
**Background:** Sample 5 (l.424-442) grants `ModifyReservedInstances`, `PurchaseReservedInstancesOffering`, and Describe actions on `Resource:"*"`, with prose: *"It's not possible to set resource-level permissions for individual Reserved Instances."*
**Security Concern:**
- **Lead E — unscopable spend:** `PurchaseReservedInstancesOffering` has **no resource type** (`list_ec2.md` — only `ec2:Region`), so a user granted RI *view* in this sample also silently holds **purchase**, a financial-commitment action no IAM condition can prevent beyond Region. A read-oriented grant becomes a billing-DoS lever. The page's own last paragraph suggests "removing DescribeInstances/DescribeAvailabilityZones means read-only" — but that does **not** remove the purchase action, so the "read-only" guidance is misleading. (Lens U.)
- **Lead F — doc-vs-API inconsistency:** the prose claims resource-level permissions are *not possible* for Reserved Instances, but `ModifyReservedInstances` **does** carry the required `reserved-instances*` resource type with `ec2:ResourceTag`, `ec2:InstanceType`, `ec2:AvailabilityZone` condition keys (`list_ec2.md`). So `ModifyReservedInstances` **is** scopable; only `PurchaseReservedInstancesOffering` is truly unscopable. The blanket "not possible" statement is inaccurate and may steer operators to grant `Resource:"*"` where a tag/instance-type scope was available. (Lens U doc-vs-API capability inconsistency.)
**High-level Test Scenarios:** `SimulateCustomPolicy` → confirm `PurchaseReservedInstancesOffering` cannot be denied by any resource ARN; confirm `ModifyReservedInstances` CAN be denied by `ec2:ResourceTag`. **Severity: Low/Informational** (file the doc-vs-API inconsistency to `aws-security` as a Lens U artifact defect; the spend-unscopability is a true-null design limit worth stating).
**Doc evidence:** l.417, l.446-448.

### Area 6 — EIP sample (cross-reference only, no net-new)
`AllocateAddress`/`AssociateAddress` on `Resource:"*"` (l.392-408). `AllocateAddress` is unscopable at allocate time (`elastic-ip*` row carries only `aws:RequestTag`); `AssociateAddress` **is** scopable (`ec2:InstanceID`,`ec2:Subnet`) but the sample grants `Resource:"*"`, letting the user bind an EIP to any instance account-wide. This matches and does not extend the already-covered EIP sibling plans (`elastic-ip-eip`, `using-instance-addressing`). **No new hunt — defer to those plans.**

---

## 6. Threat Model Test Objectives
| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Open inbound rule on any account SG while "restricted" to one subnet | sample 3 statement 1 | policy title "Restrict access to… subnet, and Region" |
| Create SG/key-pair in arbitrary VPC | samples 2,3,4b | prose "create security groups for a VPC" (singular) |
| Retag arbitrary SG to `Department=Test`, defeat ABAC | CreateTags + sample 4 | `aws:ResourceTag/Department=Test` condition |
| Enumerate all account SSM parameters; read `prod-*` secrets | sample 3b | prose "to use Systems Manager parameters when selecting an AMI" |
| Purchase Reserved Instances from a "read-ish" grant | sample 5 | prose "removing Describe… means read-only access" |
| Modify-rules on non-Test SG via unconditioned `security-group-rule/*` stmt | sample 4 stmt 3 | AND of 3 required resources (expected fail-closed) |

---

## 7. Out-of-Scope Risk Categories
- **No cross-tenant / cross-account surface.** Every grant is intra-account; there is no shared fleet, no RAM share, no cross-account principal on this page.
- **No service-plane reach**, no data→control-plane, no network/ENI boundary, no PassRole, no KMS, no attestation, no transport layer.
- `ec2:Describe*` unscopability is **by design** (AWS states it; `list_ec2` confirms no resource-level perms) — a true null, not a defect.
- `PurchaseReservedInstancesOffering` unscopability is a **true design limit** (no resource type exists) — report the misleading "read-only" prose, not the limit itself.
- Customer-*authored* tightenings of these samples are out of scope; only the **AWS-authored sample as shipped** is in scope (Lens R/S carve-out).
- Prompt-injection, file-upload, SSRF, deserialization, token/JWT, caching, canonicalization lenses: **N/A** — pages read: this entire page (no URL/blob/token/parser/cache/multi-parser surface anywhere in the five samples).

## 8. Null hypotheses / doc gaps / resolved contradictions (do not re-chase)
- **Lead B — `ModifySecurityGroupRules` "unconditioned `security-group-rule/*`" is NOT a bypass (REFUTED, fail-closed).** `ModifySecurityGroupRules` requires **three** resource types simultaneously — `prefix-list*`, `security-group*`, `security-group-rule*` (`list_ec2.md` l.8998-9004, all `*required`). In sample 4, statement 2 gates the **security-group** resource to `Department=Test` and statement 3 grants the **security-group-rule** resource unconditioned. Because authorization is the **AND** of all required resource types, the SG-resource gate (statement 2) still binds — a non-Test SG has no satisfying Allow for its `security-group` portion, so the call fails closed. Statement 3 merely supplies the second required resource; it does **not** widen access. **Verify once** with `SimulateCustomPolicy` (`ModifySecurityGroupRules` on a non-Test SG → expect **implicitDeny**), then drop. *Secondary note:* the sample grants **no** Allow for the required `prefix-list` resource, so `ModifySecurityGroupRules` on a rule referencing a managed prefix list will be denied — a functionality/fail-closed gap (Lens U completeness), not a security hole.
- **`AuthorizeSecurityGroupIngress` "security-group-rule resource-level permission only enforced when the request includes TagSpecifications" (REFUTED as a bypass here).** The IAM reference flags this fail-open (`list_ec2.md` l.4895) — same shape as the ExamplePolicies Spot H1 finding. But the console samples scope `AuthorizeSecurityGroupIngress` on the **`security-group*` resource** (always required, always enforced: `ec2:Vpc`/`aws:ResourceTag`), **not** on the optional `security-group-rule` row — so the tag-skip fail-open does not weaken samples 4/4b. Record as resolved; the real defect is the plain `Resource:"*"` grant in Area 1, independent of TagSpecifications.
- **whoAMI / `resolve:ssm` AMI poisoning — REFUTED for the restricted sample** (`ec2:Owner=amazon` gates `RunInstances` regardless of how the AMI ID is sourced). See Area 4.
- No subagents were spawned: the page is 449 lines, fully self-contained, and heavily overlaps two already-exhaustively-covered sibling plans; the only technically deep questions (SG-rule AND-semantics, AuthorizeSecurityGroupIngress TagSpecifications rule) were settled directly from the authoritative `list_ec2.md`, so a fan-out would have been redundant token spend.

---
*Prepared with the `security-questionbuilder` skill. All condition-key / resource-type claims cross-checked against `docs/service-authorization/latest/reference/list_ec2.md`. Oracles are `iam:SimulatePrincipalPolicy`/`SimulateCustomPolicy` unless a live tagged-vs-untagged differential is explicitly required (none on this page). Nothing herein was tested against a live account.*
