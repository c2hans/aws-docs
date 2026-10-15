# EC2 Spot Fleet *Prerequisites / Permissions* — Attack Research Plan

**Source of leads:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-prerequisites.html` (the "Spot Fleet permissions" page) and its immediate IAM neighborhood — `spot-fleet-auto-scaling-IAM.html`, `tag-spot-fleet.html`, the AWS Batch `spot-fleet-roles-cli` / `spot-fleet-not-authorized` / `spot-fleet-roles-console` runbooks — plus the **actual resolved JSON** of every AWS-authored IAM policy the page ships (AWS Managed Policy Reference, pulled and audited statement-by-statement).
Offline mirror: `/work/aws-docs/docs/**`. Online `.md`/`.html` twins cross-checked on every quoted artifact (CMK-grant command, trust-policy JSON, `aws:SourceArn` table, all five managed policies' JSON/version/timestamps) — **no online/offline sync drift found.** The only documentation gap is AWS's own catalog: the deprecated `AmazonEC2SpotFleetRole` reference page is absent from both the live catalog and the mirror.

**Status:** Documentation-derived hypotheses only. **Nothing in this plan has been tested against a live AWS account.** It is the plan a hunter (e.g. `aws-vuln-hunter`) executes next. Nearly every lead is confirmable **read-only first** (`iam:GetPolicyVersion`, `iam:SimulatePrincipalPolicy`/`SimulateCustomPolicy`, `iam:GetRole`, `kms:ListGrants`) before any live mutation; live confirmation uses only synthetic canary roles/instances/keys in an authorized account, torn down immediately.

**Produced by:** `security-questionbuilder` skill — orchestrator pass anchored on the prerequisites page, plus three parallel documentation-only deep-analysis subagents: (1) statement-by-statement audit of the resolved managed-policy JSON; (2) privilege-escalation / confused-deputy chains from the AWS-authored user sample policy; (3) the CMK grant lifecycle + the cross-service confused-deputy section.

> **Relationship to the sibling plans in this directory.** This is the **permissions-page-focused companion** to `spot-fleet-attack-research-plan.md` (which maps the whole Spot Fleet request/lifecycle neighborhood) and overlaps the launch-template/`PassRole`/KMS-grant surface shared with `ec2-fleet-attack-research-plan.md`. Where those plans summarize the IAM artifacts as *background*, this plan treats them as **the primary attack surface** and carries the resolved JSON, the exact over-broad statements, and the privesc/confused-deputy chains that originate on this one page. Read this one when the hunter's job is "audit the Spot Fleet IAM artifacts."

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc/JSON evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs.
- **Prefer the safe oracle first.** The resolved policy JSON (§2) means most leads are confirmable *statically* with `iam:GetPolicyVersion` + `iam:SimulatePrincipalPolicy`/`SimulateCustomPolicy` and read-only `iam:GetRole`/`kms:ListGrants`, touching **no resource**. Only the three genuine behavior gaps (does `RequestSpotFleet` accept a cross-account `IamFleetRole`; is `PassRole` re-checked at launch-template late-binding; is the SLR's `TerminateInstances` internally scoped to its own fleet) require a canary.
- **This service runs almost entirely inside the customer's own account.** There is no multi-tenant service fleet and no customer-reachable data plane. Classic cross-tenant IDOR is thin; the real value is **intra-account privilege escalation via AWS-authored IAM artifacts** (Lens R/S), **confused-deputy / cross-account trust that AWS leaves unscoped by default** (Lens B/U), and **KMS-grant survival** (Lens AA).
- **HARD STOP:** The only true AWS-service-plane identities in scope are the service principals `spotfleet.amazonaws.com` / `spot.amazonaws.com` / `ec2.application-autoscaling.amazonaws.com` and the service-linked roles `AWSServiceRoleForEC2SpotFleet`, `AWSServiceRoleForEC2Spot`, `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`. Treat them read-only. The moment any evidence shows you have reached, assumed, or extracted credentials/ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. Starting from the AWS-published Spot Fleet **"user" sample policy** (verbatim on the prerequisites page) **plus the page's "Optional IAM APIs" block**, escalate to an **arbitrary/admin role** in the account — create a role named `aws-ec2-spot-fleet-tagging-role`, attach `AdministratorAccess`, build an instance profile, and launch an instance carrying it (the sample's own `PassRole` statement authorizes passing that exact name).
2. Drive `spotfleet.amazonaws.com` to **assume a same-named `aws-ec2-spot-fleet-tagging-role` in *another* account** — the sample `PassRole` resource wildcards the account segment (`arn:aws:iam::*:role/...`) and the page documents the un-hardened (no `SourceArn`/`SourceAccount`) trust policy as the default. Determine whether `RequestSpotFleet` accepts a cross-account `IamFleetRole` ARN (the crux unknown).
3. Using the **copy-verbatim `AmazonEC2SpotFleetTaggingRole`** managed policy that AWS *recommends* a customer attach to `IamFleetRole`, **terminate / mis-manage any EC2 instance in the account** — its `ec2:TerminateInstances` is on `Resource:"*"` with **zero condition**, strictly weaker than even the SLR's tag-gated version.
4. Use the SLR's / tagging role's `elasticloadbalancing:RegisterTargets` on `*/*` to **register fleet instances into a target group fronting an unrelated workload** (traffic insertion / hijack).
5. Recover / persist CMK access via the **KMS grant** the page tells customers to mint for `AWSServiceRoleForEC2SpotFleet`: confirm the grant is over-broad (`Encrypt`/`ReEncrypt*`/`CreateGrant` beyond launch needs), unconstrained (no encryption context), and **never retired** by any documented lifecycle event — and that it **silently re-attaches** when the identically-named SLR is recreated.
6. From the auto-scaling permission sets, **delete arbitrary CloudWatch alarms** account-wide (`cloudwatch:DeleteAlarms` on `*`, no condition) to blind monitoring, and **modify any Spot Fleet request** in the account.
7. Enumerate **doc-vs-reality** deltas: the deprecated `AmazonEC2SpotFleetRole` whose reference page AWS no longer publishes; the asymmetry whereby the Spot-*Instance* SLR has a `RunInstances` market-type `Deny` guard that the Spot-*Fleet* SLR/tagging-role lack.

---

## 2. Components, Assets, and Design

**What it is.** The prerequisites page is the IAM gateway to Spot Fleet (`RequestSpotFleet` legacy API — "no planned investment; use EC2 Fleet or an Auto Scaling group instead"). It ships, as **copy-verbatim / uneditable artifacts**: one end-user sample policy, three roles the customer must create/pass, and one `kms create-grant` command. These artifacts are the attack surface.

**Customer-facing interface.** SigV4 EC2 Query/SDK APIs + the EC2 console "Spot Requests" screen + the IAM console. No customer-reachable data plane. Resource-level IAM is **not supported** for the `spot-fleet-request` resource type (documented in `tag-spot-fleet`), forcing the gating policies to `Resource:"*"`.

**Identities / roles the page provisions.**
- **End-user principal** — holds the AWS-authored sample policy (primary attack surface).
- `AWSServiceRoleForEC2SpotFleet` — SLR assumable only by `spotfleet.amazonaws.com`; policy `AWSEC2SpotFleetServiceRolePolicy` (v4, edited 2020-03-16). Launches/terminates/tags on your behalf. Trust policy fixed by AWS, **not customer-editable**.
- `AWSServiceRoleForEC2Spot` — SLR (`spot.amazonaws.com`); policy `AWSEC2SpotServiceRolePolicy` (v4, 2018-12-12). Underlies every individual Spot Instance launch.
- `aws-ec2-spot-fleet-tagging-role` — a **customer-created role you pass as `IamFleetRole`**; AWS tells you to attach the managed policy `AmazonEC2SpotFleetTaggingRole` (v5, 2020-04-23). Trust policy is **customer-editable but defaults open** (no confused-deputy condition).
- `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest` — SLR for auto-scaling; policy `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` (v1, 2017-10-25, never revised). Legacy customer-managed `aws-ec2-spot-fleet-autoscale-role` + `AmazonEC2SpotFleetAutoscaleRole` (v3) "no longer required" but still live.
- Deprecated `AmazonEC2SpotFleetRole` — referenced by the Batch runbook; **reference page absent from AWS's current catalog** (doc-coverage gap).

**Resolved JSON of the AWS-authored policies (audited verbatim — this is the backbone of §4):**

```
AWSEC2SpotFleetServiceRolePolicy (SLR AWSServiceRoleForEC2SpotFleet) v4
  S1  Allow  ec2:DescribeImages/DescribeSubnets/RequestSpotInstances/DescribeInstanceStatus/RunInstances   Resource "*"   (no Condition)
  S2  Allow  iam:PassRole   Resource "*"   Cond StringEquals iam:PassedToService in {ec2.amazonaws.com, ec2.amazonaws.com.cn}
  S3  Allow  ec2:CreateTags  Resource instance/* , spot-instances-request/* , spot-fleet-request/* , volume/*   (scoped — OK)
  S4  Allow  ec2:TerminateInstances   Resource "*"   Cond StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id = "*"   ◄── tag-KEY PRESENCE, not fleet ownership
  S5  Allow  elasticloadbalancing:RegisterInstancesWithLoadBalancer   Resource loadbalancer/*
  S6  Allow  elasticloadbalancing:RegisterTargets   Resource *:*:*/*   (no Condition)   ◄── any TG/listener/rule in account

AmazonEC2SpotFleetTaggingRole (customer IamFleetRole) v5  ◄── WEAKEST OF THE SET
  S1  Allow  ec2:DescribeImages/DescribeSubnets/RequestSpotInstances/TerminateInstances/DescribeInstanceStatus/CreateTags/RunInstances   Resource "*"   (NO Condition — TerminateInstances fully unconditioned)
  S2  Allow  iam:PassRole   Resource "*"   Cond iam:PassedToService in {ec2.*}
  S3  Allow  elasticloadbalancing:RegisterInstancesWithLoadBalancer   Resource loadbalancer/*
  S4  Allow  elasticloadbalancing:RegisterTargets   Resource *:*:*/*   (no Condition)

AmazonEC2SpotFleetAutoscaleRole (legacy) v3
  Allow  ec2:DescribeSpotFleetRequests/ModifySpotFleetRequest   Resource "*"
  Allow  cloudwatch:DescribeAlarms/PutMetricAlarm/DeleteAlarms   Resource "*"   ◄── DeleteAlarms account-wide
  Allow  iam:CreateServiceLinkedRole   Resource <app-autoscaling SLR ARN>   Cond iam:AWSServiceName (scoped — OK)

AWSApplicationAutoscalingEC2SpotFleetRequestPolicy (SLR) v1
  Allow  ec2:DescribeSpotFleetRequests/ModifySpotFleetRequest + cloudwatch:PutMetricAlarm/DescribeAlarms/DeleteAlarms   Resource "*"   (ZERO conditions anywhere)

AWSEC2SpotServiceRolePolicy (SLR AWSServiceRoleForEC2Spot) v4  ◄── BEST-DESIGNED
  Allow  ec2:DescribeInstances/StartInstances/StopInstances/RunInstances   Resource "*"
  Deny   ec2:RunInstances   Resource instance/*   Cond StringNotEquals ec2:InstanceMarketType = "spot"   ◄── market-type guard the Fleet policies LACK
  Allow  iam:PassRole   Cond iam:PassedToService in {ec2.*}
  Allow  ec2:CreateTags   Resource "*"   Cond StringEquals ec2:CreateAction = "RunInstances"   (tight — OK)
```

**AWS-authored user sample policy (verbatim from the page) + optional block:**
```
Base:  ec2:RunInstances, ec2:CreateTags, ec2:RequestSpotFleet, ec2:ModifySpotFleetRequest,
       ec2:CancelSpotFleetRequests, ec2:DescribeSpotFleet{Requests,Instances,RequestHistory}   Resource "*"
       iam:PassRole   Resource arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role      ◄── ACCOUNT SEGMENT = "*"
       iam:CreateServiceLinkedRole, iam:ListRoles, iam:ListInstanceProfiles   Resource "*"   ◄── CreateSLR unscoped (no iam:AWSServiceName)
Optional (page tells you to add): iam:AddRoleToInstanceProfile, iam:AttachRolePolicy, iam:CreateInstanceProfile,
       iam:CreateRole, iam:GetRole, iam:ListPolicies   Resource "*" (no PolicyArn/path constraint)
```

**KMS grant the page tells you to mint (verbatim):**
```
kms create-grant  --grantee-principal <AWSServiceRoleForEC2SpotFleet SLR ARN>
  --operations Decrypt Encrypt GenerateDataKey GenerateDataKeyWithoutPlaintext CreateGrant DescribeKey ReEncryptFrom ReEncryptTo
  (NO --constraints / encryption-context ; NO --retiring-principal ; example key-id is in a DIFFERENT account than the grantee)
```

```
 End-user principal (AWS sample policy + optional IAM block)
     │  RequestSpotFleet(IamFleetRole=ARN, launch spec/template)      PassRole gate: only :role/aws-ec2-spot-fleet-tagging-role, account "*"
     ▼
 Spot Fleet control plane
     ├─ sts:AssumeRole ─► aws-ec2-spot-fleet-tagging-role (IamFleetRole)   trust = spotfleet.amazonaws.com, NO SourceArn/Account by default
     │        AmazonEC2SpotFleetTaggingRole: TerminateInstances/RunInstances/CreateTags on * (NO cond); RegisterTargets */*; PassRole *(PassedToService=ec2)
     └─ assumes AWSServiceRoleForEC2SpotFleet (SLR)
              AWSEC2SpotFleetServiceRolePolicy: RunInstances *; PassRole *(ec2); TerminateInstances *(tag-key presence); RegisterTargets */*
                 │ RunInstances (encrypted AMI/EBS ─► uses KMS grant on customer CMK: over-broad ops, no enc-context, never retired)
                 ▼
            EC2 instance (IamInstanceProfile creds via IMDS ; UserData boot code)
                 │ (maintain) register as Application Auto Scaling scalable target
                 ▼
         App Auto Scaling SLR ── ModifySpotFleetRequest / cloudwatch:DeleteAlarms (all Resource:*) ─► scale
```

**Untrusted-data / caller-controlled inputs on this surface:** `IamFleetRole` ARN (account-wildcard-matchable), launch-spec/launch-template `IamInstanceProfile` (late-bindable via `$Latest`/`$Default`), `LoadBalancersConfig` (names the target group), the KMS `key-id`/`grantee-principal` (cross-account-capable), tag keys/values.

---

## 3. API / Interface Inventory (prerequisites-relevant)

| Name | Mutating | Facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|
| `RequestSpotFleet` | Yes | External | Create fleet; takes `IamFleetRole`, launch specs/templates | user w/ `ec2:RequestSpotFleet` + `iam:PassRole` | Legacy. **Does it accept a cross-account `IamFleetRole`? — undocumented, crux of B1.** |
| `iam:PassRole` (gate) | — | — | Authorizes which role rides the request/instance | user policy | Sample scopes to role **name** only; **account = `*`**. |
| `iam:CreateRole` / `AttachRolePolicy` / `CreateInstanceProfile` / `AddRoleToInstanceProfile` | Yes | External | Optional block the page tells users to add | user policy | **Unscoped `Resource:"*"`, no `PolicyArn` constraint** → privesc chain (R-S3/P1). |
| `iam:CreateServiceLinkedRole` | Yes | External | Create SLRs | user policy | **No `iam:AWSServiceName` condition** → create SLR for *any* service (P5). |
| `sts:AssumeRole` (tagging role trust) | — | — | `spotfleet.amazonaws.com` assumes `IamFleetRole` | service principal | **Default trust has NO `SourceArn`/`SourceAccount`** (confused-deputy). |
| `kms:CreateGrant` (one-time, by customer) | Yes | External | Grant SLR CMK use | customer | Over-broad ops; no enc-context; **no documented retirement**. |
| `ec2:ModifySpotFleetRequest` / `cloudwatch:DeleteAlarms` (autoscale) | Yes | External | Scale / manage alarms | autoscale role/SLR | `Resource:"*"`, no condition → account-wide. |
| `ec2:TerminateInstances` (via tagging role / SLR) | Yes | External | Terminate | assumed role | Tagging role: **zero condition**; SLR: tag-key presence only. |

---

## 4. Boundary-lens catalog — firing lenses

### Lens R / S — AWS-authored IAM-artifact audit (HIGHEST YIELD)

**R1 — `AmazonEC2SpotFleetTaggingRole` can terminate ANY instance in the account (zero condition).**
**Claim:** The copy-verbatim managed policy AWS *recommends* a customer attach to `IamFleetRole` grants `ec2:TerminateInstances` on `Resource:"*"` with **no `Condition` at all** — strictly weaker than even the SLR's tag-gated version. Any principal/flow that uses this role can destroy any instance in the account, fleet-owned or not. `RunInstances`/`CreateTags` are likewise unconditioned.
**Mechanism:** resolved JSON `AmazonEC2SpotFleetTaggingRole` v5 statement S1 (above). The prerequisites page's "Important" callout *steers customers to this policy*: "to ensure all instances launched by the fleet are tagged, we recommend that you use the `aws-ec2-spot-fleet-tagging-role` role for the `IamFleetRole`. Alternatively … attach the `AmazonEC2SpotFleetTaggingRole` AWS Managed Policy." Following AWS's own remediation **downgrades** blast radius from "any Spot-Fleet-tagged instance" to "any instance, period."
**Confirm/Refute oracle:** read-only `iam:GetPolicyVersion arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetTaggingRole --version-id v5` confirms the statement; `iam:SimulatePrincipalPolicy --action-names ec2:TerminateInstances --resource-arns <unrelated-untagged-instance-ARN>` under a role holding only this policy → expect `allowed`. **Run this first.**
**Severity-if-true:** High–Critical (account-wide instance destruction via an AWS-managed, uneditable, *recommended* policy). **Owner-to-fix:** AWS. In scope per the Lens R carve-out (AWS-authored / copy-verbatim).

**R2 — SLR `TerminateInstances` keys on tag *presence*, not fleet ownership.**
**Claim:** `AWSEC2SpotFleetServiceRolePolicy` S4 allows `ec2:TerminateInstances` on `*` conditioned only `StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id = "*"` — matches the tag **key** regardless of value. In pure-IAM terms the SLR can terminate **any** instance carrying that system tag, i.e. instances of a *different* Spot Fleet in the same account; there is no execution-context binding to the invoking `sfr-`.
**Mechanism:** resolved JSON S4. `aws:ec2spot:fleet-request-id` is a **reserved/service tag EC2 stamps** on every Spot-Fleet instance — not customer-settable via `ec2:CreateTags`.
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` with resource tag `aws:ec2spot:fleet-request-id` = a *different* fleet's id → expect `allowed`. **Decisive unknown:** whether EC2's internal (non-IAM, unpublished) request routing independently restricts the SLR's call to its own fleet's instances. If not → cross-fleet termination within account (High). If yes → the IAM statement is defense-in-depth only (Informational). Also test the reserved-tag boundary: `ec2:CreateTags` setting `aws:ec2spot:fleet-request-id` on a victim instance → expect denied; if a user *can* set it, this becomes a victim-instance-termination primitive.
**Severity-if-true:** Medium–High (cross-fleet termination). **Owner-to-fix:** AWS.

**R3 — `elasticloadbalancing:RegisterTargets` on `*/*` (SLR *and* tagging role), no condition.**
**Claim:** Both `AWSEC2SpotFleetServiceRolePolicy` S6 and `AmazonEC2SpotFleetTaggingRole` S4 allow `RegisterTargets` on `arn:aws:elasticloadbalancing:*:*:*/*` — the ELB ARN shape `<type>/<name>/<id>` means `*/*` spans target-group / listener / rule. `LoadBalancersConfig` lets the caller name the target. An attacker fleet can register its instances into a target group fronting an **unrelated** load-balanced workload (traffic insertion / request-steering / DoS). This is the single broadest unconditioned grant in the set.
**Confirm/Refute oracle:** `iam:GetPolicyVersion` confirms `*/*`; `iam:SimulatePrincipalPolicy` for `RegisterTargets` from both the SLR and the `IamFleetRole` context against a foreign target-group ARN never attached to any fleet → `allowed`. Live: register a canary instance into a canary "other-workload" target group you own; confirm no fleet-ownership binding.
**Severity-if-true:** High (cross-workload traffic insertion). **Owner-to-fix:** AWS (scoping) + customer (target-group resource policy, if any).

**R4 — Market-type `Deny` guard asymmetry.**
**Claim:** `AWSEC2SpotServiceRolePolicy` (Spot *Instance* SLR) correctly bounds its unconditioned `Allow RunInstances` with an explicit `Deny RunInstances` when `ec2:InstanceMarketType != spot`. The Spot-*Fleet* SLR (`AWSEC2SpotFleetServiceRolePolicy`) and the tagging role (`AmazonEC2SpotFleetTaggingRole`) call `RunInstances` on `*` with **no such Deny** — so a confused/coerced Fleet role can launch non-Spot (on-demand) capacity. AWS demonstrably *can* write this guard; its absence on the Fleet policies is an avoidable regression.
**Confirm/Refute oracle:** `iam:GetPolicyVersion` on all three; `iam:SimulatePrincipalPolicy` for `RunInstances` with `ec2:InstanceMarketType=on-demand` under the Fleet SLR / tagging role → `allowed` (vs `Deny` under the Spot-Instance SLR).
**Severity-if-true:** Low–Medium (cost / capacity, not takeover) but a clean AWS-owned hardening finding. **Owner-to-fix:** AWS.

**R5 — Autoscale policies: `cloudwatch:DeleteAlarms` + `ec2:ModifySpotFleetRequest` on `*`.**
**Claim:** `AmazonEC2SpotFleetAutoscaleRole` (v3) and `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy` (v1, never revised) both allow `cloudwatch:DeleteAlarms` and `ec2:ModifySpotFleetRequest` on `Resource:"*"` with no condition. A fleet-scaling credential can **delete any CloudWatch alarm in the account** (blinding billing/GuardDuty/Config-remediation/security alarms) and **modify any Spot Fleet request**. The SLR variant is service-gated; the legacy customer-managed variant is directly attachable.
**Confirm/Refute oracle:** `iam:GetPolicyVersion`; `iam:SimulatePrincipalPolicy` for `cloudwatch:DeleteAlarms` against an unrelated alarm ARN → `allowed`.
**Severity-if-true:** Medium–High (detection evasion / monitoring tamper). **Owner-to-fix:** AWS. Also flag the v1-never-revised policy for "silently-needed-but-never-shipped tighter version."

**R6 — Deprecated `AmazonEC2SpotFleetRole` has no reference page (doc-coverage gap).**
**Claim:** AWS managed policies are never deleted, so `arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetRole` almost certainly still resolves live and is still attachable, yet its reference page is absent from AWS's current catalog **and** the offline mirror — a docs-only auditor cannot see its JSON. The Batch runbook describes it as *lacking* `ec2:CreateTags` (a missing-permission/functionality bug, the inverse failure mode AWS fixed by shipping `AmazonEC2SpotFleetTaggingRole` — i.e. R1 is the regression of that fix).
**Confirm/Refute oracle:** `iam:GetPolicyVersion arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetRole` (read-only; close the gap and compare to R1's over-grant).
**Severity-if-true:** Informational–Low (documentation coverage), but run it to close the audit.

### Lens P / B — Privilege escalation & confused deputy from the user sample policy

**P1 — Non-admin → admin via self-created tagging-role + instance profile.**
**Claim:** A principal holding the base sample policy **+ the "Optional IAM APIs" block** can self-escalate to admin: `iam:CreateRole`(name `aws-ec2-spot-fleet-tagging-role`, trust `ec2.amazonaws.com`) → `iam:AttachRolePolicy`(`arn:aws:iam::aws:policy/AdministratorAccess` — **unconstrained** by the policy) → `iam:CreateInstanceProfile` → `iam:AddRoleToInstanceProfile` → `ec2:RunInstances` with that instance profile. The sample's own `PassRole` statement (`arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role`) authorizes passing exactly that name; the admin creds are then readable from IMDS on the attacker's instance.
**Mechanism:** page "Optional IAM APIs" block (verbatim, `Resource:"*"`, no `PolicyArn` constraint) + base `PassRole` + `RunInstances` on `*`. `ec2:RunInstances` has no instance-profile resource type to gate — `PassRole` is the sole choke point and it is satisfied by the name.
**Gate / precondition:** the role name `aws-ec2-spot-fleet-tagging-role` must **not already exist** (IAM role names are unique per account). The page itself hints many CLI/API accounts never auto-created it ("you must ensure that these roles exist"). The granted `iam:ListRoles`/`GetRole` let the attacker check availability for free.
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` over the verbatim sample+optional JSON for `CreateRole`, `AttachRolePolicy{PolicyArn=AdministratorAccess}`, `AddRoleToInstanceProfile`, `PassRole{Resource=::<self>:role/aws-ec2-spot-fleet-tagging-role}` → expect all `allowed`. Fallback: isolated sandbox account with no pre-existing tagging role, run the chain with synthetic names, confirm the instance boots with admin creds, tear down.
**Severity-if-true:** High (intra-account non-admin → admin), contingent on the name-collision gate. **Owner-to-fix:** AWS-published guidance — the optional block is AWS-authored copy-text with no scoping; file as a documentation-hardening finding (add `PolicyArn`/path constraints and a warning).

**B1 — Cross-account `IamFleetRole` confused deputy (the one potential *cross-account* lead).**
**Claim:** The sample `PassRole` resource `arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role` wildcards the **account** segment. Combined with the page's documented **default (un-hardened) trust policy** on `aws-ec2-spot-fleet-tagging-role` — `Principal: spotfleet.amazonaws.com`, `sts:AssumeRole`, **no `aws:SourceArn`/`aws:SourceAccount`** — a caller in account A may be able to drive `spotfleet.amazonaws.com` to assume a same-named tagging role in account B, inheriting B's unconditioned `TerminateInstances`/`RunInstances`/`CreateTags` on `*`.
**Mechanism:** sample policy (`::*:role/...`); the page's "Cross-service confused deputy prevention" section presents `SourceArn`/`SourceAccount` as an **optional, later add-on**, and the console wizard + the Batch `spot-fleet-roles-cli` runbook both create the role with a **no-`Condition`** trust policy. The `aws:SourceArn` table scopes to `spot-fleet-request/sfr-*` *owned by the calling account*.
**Crux unknown (the single most valuable live test):** does `RequestSpotFleet` enforce **same-account `IamFleetRole`** server-side *before* invoking STS? If yes, B1 collapses to intra-account PassRole confusion (High via P1/R1). If no, the absent trust condition is the only backstop and cross-account assumption succeeds (Critical).
**Confirm/Refute oracle:** read-only `iam:GetRole` on any real `aws-ec2-spot-fleet-tagging-role` to confirm the trust policy lacks `Condition`; `iam:SimulatePrincipalPolicy` for `PassRole` with a cross-account role ARN → confirms IAM-side permissiveness. **Decisive step:** a single `--dry-run RequestSpotFleet` naming an `IamFleetRole` ARN in a *second account you are authorized for*. Accepted → cross-account confused deputy.
**Severity-if-true:** Critical (cross-account role assumption via AWS's deputy). **Stop:** on any evidence the assumed identity is AWS's own fleet plane, hard-stop. **Owner-to-fix:** shared — AWS (default trust guidance + the account-wildcard in its own sample `PassRole`) + customer.

**P2 — Launch-template `$Latest`/`$Default` late-binding of `IamInstanceProfile`.**
**Claim:** The page closes the *direct* bypass ("if you specify a role for the IAM instance profile in the launch specification **or launch template**, you must grant `PassRole`"), but is **silent** on the case where a restricted caller merely *references* a pre-existing template by `LaunchTemplateId`+`$Latest` (authored by a more-privileged principal) without ever naming the role themselves — and on whether `PassRole` is re-evaluated at **launch time** (when the SLR calls `RunInstances`) vs only at `RequestSpotFleet`/`ModifySpotFleetRequest` time. A template owner who later publishes a new `$Latest`/`$Default` version pointing at a sensitive instance profile could silently upgrade the privilege of a fleet an attacker (holding `ec2:ModifySpotFleetRequest` from the base policy) still controls.
**Mechanism:** `tag-spot-fleet` confirms the fleet stores a *reference*, not a frozen copy; precedent = historical Auto Scaling launch-configuration `PassRole` gaps. Not asserted by the docs — flagged.
**Confirm/Refute oracle:** not resolvable from docs; two-principal / two-phase canary — privileged author creates template v1 (safe role) with `PassRole`; attacker (base policy, no `PassRole` for the sensitive role) submits `RequestSpotFleet` referencing `$Latest`; author publishes v2 with a sensitive `IamInstanceProfile`; observe whether the next launch cycle attaches it with no `PassRole` check against the attacker's policy (CloudTrail).
**Severity-if-true:** High–Critical (late-binding privesc). **Lowest-confidence lead — test, don't assert.**

**P3 — Unscoped `iam:CreateServiceLinkedRole`.**
**Claim:** The base sample policy grants `iam:CreateServiceLinkedRole` on `Resource:"*"` with **no `iam:AWSServiceName` condition**, so a holder can create SLRs for *any* AWS service, not just `spotfleet.amazonaws.com`. Combined with the unconditionally-granted recon actions (`iam:ListRoles`/`GetRole`/`ListInstanceProfiles`/`ListPolicies`), it also hands an attacker free enumeration of exploitable role names/trust policies before running P1/B1.
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` for `iam:CreateServiceLinkedRole` with `iam:AWSServiceName=elasticbeanstalk.amazonaws.com` (or any unrelated service) → expect `allowed`.
**Severity-if-true:** Low–Medium (most SLRs are self-trust-limited) + recon enabler. **Owner-to-fix:** AWS-published guidance (add the condition).

### Lens H / AA / T — KMS CMK grant for encrypted AMIs / EBS

**H1 — Grant operation set is wider than launching needs.**
**Claim:** The page's `kms create-grant` command grants `Encrypt`, `ReEncryptFrom`, `ReEncryptTo`, and `CreateGrant` in addition to the launch-necessary `Decrypt`/`GenerateDataKey`/`GenerateDataKeyWithoutPlaintext`/`DescribeKey`. Launching an instance from an existing encrypted AMI/EBS never re-encrypts arbitrary plaintext (`Encrypt`), re-keys ciphertext (`ReEncrypt*`), or needs to mint sub-grants (`CreateGrant`). `CreateGrant` on the grantee means the SLR can **fan out its own CMK access to further grantees** without the key owner's involvement (KMS docs liken grant-creation permission to `kms:PutKeyPolicy`).
**Confirm/Refute oracle:** read-only `kms:ListGrants --key-id <cmk>` after an encrypted-AMI fleet has run → confirm `Encrypt`/`ReEncrypt*`/`CreateGrant` present; CloudTrail diff to show EC2 never invokes them during a normal launch. (`SimulatePrincipalPolicy` N/A — grants aren't identity policy.)
**Severity-if-true:** Medium (over-broad grant on a customer CMK, AWS-published command → AWS defect; blast-radius amplifier for any SLR confusion). **Owner-to-fix:** AWS.

**H2 — The grant is never retired (silently renewable persistence).**
**Claim:** No documented lifecycle event retires this grant. The page's only cleanup guidance is for the *SLR* ("we recommend you delete the `AWSServiceRoleForEC2SpotFleet` role"); the IAM role-deletion doc mentions nothing about KMS/grants; KMS grants are deleted only by explicit `RetireGrant`/`RevokeGrant`, never automatically on principal deletion. Worse: the page says EC2 will **recreate the identically-named SLR** on next console use — and a KMS grant keyed on `(key, grantee ARN)` **re-attaches automatically** to the recreated role, restoring CMK access with zero customer action and no re-run of `create-grant`. The page never tells the customer to `retire-grant`.
**Confirm/Refute oracle:** read-only `kms:ListGrants` before/after (a) `CancelSpotFleetRequests` and (b) deleting the SLR — a surviving `GrantId` confirms non-retirement (no mutation needed to observe).
**Severity-if-true:** High (permanent, silently-renewable CMK access tied to a predictable role-ARN pattern; doc gap). **Owner-to-fix:** AWS (add retirement guidance) + customer.

**H3 — No encryption-context constraint; cross-account CMK is the documented example.**
**Claim:** The `create-grant` command has **no `--constraints`** → the grant authorizes CMK use for *any* resource under that key, not just the AMI/snapshot that prompted it — even though AWS's own KMS/confused-deputy docs name encryption-context as the native anti-confused-deputy mechanism for grants. The page's example ARNs put `key-id` in account `444455556666` and `grantee-principal` in account `111122223333`, i.e. **cross-account by design**, which raises H1/H2 from an intra-account to a cross-account persistence/access vector.
**Confirm/Refute oracle:** `kms:ListGrants` → inspect `Constraints` (absent) and `GranteePrincipal` account vs key account.
**Severity-if-true:** Medium–High (within-key over-reach; cross-account amplification). **Owner-to-fix:** AWS (add `--constraints` guidance).

### Lens I — Tagging / ABAC escape (documented inconsistency)

**I1 — Permission mismatch leaves fleet instances untagged → ABAC escape.** The page documents that differences between the **user's** and the **`IamFleetRole`'s** `CreateTags` permissions cause **some fleet-launched instances to not be tagged** (`maintain` type). If the account enforces ABAC/governance keyed on a required tag, instances the fleet launches untagged escape that control. AWS's fix was to **widen** the role (unconditioned `CreateTags` on `*`), not add an ABAC condition.
**Oracle:** `iam:GetPolicyVersion` confirms no `aws:ResourceTag` condition on the tagging role's `CreateTags`; reason about an ABAC policy vs an untagged fleet instance. **Severity:** Medium where ABAC is the access-control mechanism. **Owner-to-fix:** AWS.

---

## 5. Recommended Areas of Focus (priority order)

1. **R1 — tagging-role unconditioned `TerminateInstances` on `*`.** Highest yield, confirmable read-only, and AWS *recommends* the policy. Run the `SimulatePrincipalPolicy` termination test first.
2. **B1 — cross-account `IamFleetRole` confused deputy.** The one potential *cross-account* (Critical) lead; decisive oracle is a single `--dry-run RequestSpotFleet` with a second-account role ARN. Elevate above everything else **iff** the dry-run is accepted.
3. **P1 — user-sample-policy privesc to admin** (optional block → `CreateRole`/`AttachRolePolicy`/instance-profile → `PassRole` by name). Confirmable with `SimulateCustomPolicy`; gated on the role-name being free.
4. **R3 — `RegisterTargets */*`** (SLR + tagging role) — cross-workload traffic insertion. **H1/H2/H3 — KMS grant** over-broad + never-retired + cross-account.
5. **R2 — SLR tag-presence `TerminateInstances`** (cross-fleet), **R5 — autoscale `DeleteAlarms` on `*`** (detection evasion), **P2 — launch-template late-binding** (test, don't assert).
6. **R4 market-type guard asymmetry, R6 deprecated-policy coverage gap, P3 unscoped CreateSLR, I1 ABAC escape** — hardening / lower severity, cheap read-only confirmation.

**Kill-chain to compose (rate at the end of the chain):** P1 (craft admin role + instance profile, name = `aws-ec2-spot-fleet-tagging-role`) → the sample `PassRole` authorizes passing it → `ec2:RunInstances`/`RequestSpotFleet` lands it on an attacker-controlled instance → `UserData` reads admin creds from IMDS → **account-wide admin (Critical)**. Alternative entry: B1 (cross-account) → inherit account B's unconditioned tagging role → R1 (destroy B's instances) / R3 (hijack B's load-balanced traffic).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Non-admin → admin via self-created tagging role + instance profile | user sample policy "Optional IAM APIs" + base `PassRole` by name | `PassRole` scoped to role *name* only (account `*`); no `PolicyArn` constraint on `AttachRolePolicy` |
| Cross-account role assumption via `IamFleetRole` | sample `PassRole` account-wildcard + tagging-role default trust | *Recommended* (not default) `aws:SourceArn`/`aws:SourceAccount`; undocumented server-side same-account check |
| Terminate any instance in the account | `AmazonEC2SpotFleetTaggingRole` `TerminateInstances *` | **None** (zero condition); AWS *recommends* attaching this policy |
| Terminate another fleet's instances | SLR `TerminateInstances` tag-key-presence condition | Tag-key presence only; unpublished internal routing (unknown) |
| Insert instances behind an unrelated target group | SLR / tagging-role `RegisterTargets */*` + `LoadBalancersConfig` | None documented beyond target-group resource policy (if any) |
| Launch non-Spot capacity via Fleet role | Fleet SLR / tagging-role `RunInstances *` | Spot-*Instance* SLR has a market-type `Deny`; Fleet policies do not |
| Permanent / renewable CMK access | KMS grant on `AWSServiceRoleForEC2SpotFleet` | None — no retirement/`--constraints` guidance; grant survives + re-attaches |
| Blind monitoring / modify any fleet | autoscale `cloudwatch:DeleteAlarms` / `ModifySpotFleetRequest` on `*` | None (no condition) |
| ABAC/governance escape via untagged instances | tagging permission mismatch | AWS widened the role instead of adding an ABAC condition |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-tenant IDOR via guessing `sfr-` IDs** — IDs are `sfr-`+UUIDv4 (~2^122); EC2 account-partitioning protects these APIs. The `aws:SourceArn` `sfr-*` scoping is **not** weak via enumerability (it is weak only via the customer's own choice of account-wide wildcard). Null for the enumerability sub-question (pages checked: prerequisites `aws:SourceArn` table, `tag-spot-fleet` describe examples).
- **The `AWSServiceRoleForEC2SpotFleet` trust policy's lack of `SourceArn`** — SLR trust policies are **AWS-fixed and not customer-editable**; the SLR's confused-deputy protection, if any, lives in AWS's unpublished internal implementation and is not independently testable from docs. The reportable angle is only B1 and the doc's failure to distinguish "yours to close" (tagging role) from "AWS's to have closed" (SLR).
- **IMDS / UserData on the managed instances** — the instances are the customer's own; steering one's own instance boot/creds is not a boundary breach (becomes in-scope only when a *more-privileged* role is attached via P1/B1).
- **Customer-authored policies** — a weak policy the customer wrote is a footgun (out of scope). The in-scope artifacts here are the **AWS-managed / uneditable** policies (R1–R6, I1) and the **copy-verbatim AWS-published guidance** (the user sample policy + optional block in P1/P3, the `create-grant` command in H1–H3, the default trust policy in B1).
- **Single-tenant self-DoS / cost churn** — bounded by the attacker's own account quota/bill, unless via compromised credentials (then a griefing technique).
- **AWS's own service plane** — `spotfleet.amazonaws.com` / `spot.amazonaws.com` / the SLRs are the shared-responsibility line and a **hard stop**.

---

## 8. Null hypotheses / doc gaps (pages named)

- **Lens C (credential vending / STS session scope):** null — `IamFleetRole` is a static ARN; no session-policy/ProvidedContext/per-tenant role-vending. (Pages: prerequisites, `spot-fleet-auto-scaling-IAM`.) B1 is the PassRole/trust variant, routed to Lens B.
- **Lens D / V (data-plane→control-plane / network segmentation):** null — no service-owned fleet, no control/storage ENI; all instances live in the customer VPC. (Pages: prerequisites, `tag-spot-fleet`.)
- **Lens F (translation-layer / wire-protocol injection):** null — plain EC2 Query/SDK; no translator/parser on this surface.
- **Lens G (SSRF):** null — no field the service dereferences server-side on this page (no URL/webhook/logo/import). `IamFleetRole`/CMK ARNs are AWS resource identifiers, not fetched locations. (Pages: prerequisites, `tag-spot-fleet`, `spot-fleet-auto-scaling-IAM`.)
- **Lens K (prompt injection), P-identity-proofing, Q (upload), M (shared-identifier), N (namespace migration), W/Y/BB/CC/DD/EE/FF:** no triggers on the prerequisites surface (no LLM, no onboarding/OTP, no upload, no bearer-capability, no dual namespace, no attestation gate, no customer-facing TLS endpoint, no multi-parser request path, no upstream-asserted-identity header, no caching layer, no predictable-global-namespace resolution by Spot Fleet, no JWT/OIDC). The `resolve:ssm:<ARN>` AMI-name-resolution variant (launch templates, Lens EE/U) is cross-referenced to `ec2-fleet-attack-research-plan.md`.
- **Lens O (audit evasion):** partially covered by R5 (`DeleteAlarms`); the `cancelled_running` orphan / 48-h history-decay techniques live in the sibling `spot-fleet-attack-research-plan.md`.

**Doc gaps requiring live/API-reference confirmation (not resolvable from docs alone):**
1. Does `RequestSpotFleet` enforce **same-account `IamFleetRole`** server-side, independent of the trust policy? (gates B1: Critical vs High)
2. Does EC2's internal (unpublished) routing restrict the SLR's `TerminateInstances` to its own fleet's instances, despite the tag-key-presence IAM condition? (gates R2)
3. Is `iam:PassRole` re-evaluated at launch-template **launch time** vs only at request time (P2 late-binding)?
4. Can `ec2:CreateTags` set the reserved `aws:ec2spot:fleet-request-id` key on a victim instance? (would escalate R2 to a victim-termination primitive)
5. The deprecated `AmazonEC2SpotFleetRole` live JSON — `iam:GetPolicyVersion` to close R6.

---
*End of plan. Documentation-derived hypotheses only; nothing herein has been executed against a live AWS account. Companion to `spot-fleet-attack-research-plan.md` and `ec2-fleet-attack-research-plan.md` in this directory.*
