# EC2 Spot Fleet — Attack Research Plan

**Source of leads:** AWS EC2 User Guide, anchored on `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-spot-fleets.html` and its neighborhood (states, prerequisites, create, tag, modify, cancel, manage, automatic-scaling, target-tracking, step-scaling, scheduled-scaling, examples), the EC2 API Reference (`RequestSpotFleet`, `SpotFleetRequestConfigData`, `SpotFleetLaunchSpecification`, `ModifySpotFleetRequest`, `CancelSpotFleetRequests`, `DescribeSpotFleet*`, `SpotFleetTagSpecification`, `SpotFleetMonitoring`), the four AWS-managed policies (`AWSEC2SpotFleetServiceRolePolicy`, `AmazonEC2SpotFleetTaggingRole`, `AmazonEC2SpotFleetAutoscaleRole`, `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy`), the AWS Batch spot-fleet-role runbook pages, and the Config rule `ec2-spot-fleet-request-ct-encryption-at-rest`.
Offline mirror: `/work/aws-docs/docs/**`. Online `.md` twins cross-checked (append `.md` to any `.html` page) — **no sync gaps found** on any audited artifact (SLR policy v4 and all nine lifecycle/launch pages matched byte-for-byte).
**Status:** Documentation-derived hypotheses only. **Nothing in this plan has been tested against a live AWS account.** It is the plan a hunter (e.g. `aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill — orchestrator pass on the IAM artifacts + core request mechanism, plus 3 parallel documentation-only deep-analysis subagents (auto-scaling; request lifecycle/describe/cancel/history; launch-spec/Batch-integration/IAM-artifact).

> **Relationship to the sibling plan.** Spot Fleet is the **legacy console twin of EC2 Fleet** ("no planned investment"; AWS tells you to use EC2 Fleet or an Auto Scaling group instead). Most of the launch-template / `PassRole` late-binding / KMS-grant surface is shared with `ec2-fleet-attack-research-plan.md` in this directory — read that first for the EC2-Fleet-specific depth. This plan concentrates on what is **distinct to Spot Fleet**: its three service-linked roles and the copy-verbatim `aws-ec2-spot-fleet-tagging-role`, the `RequestSpotFleet`/`ModifySpotFleetRequest`/`CancelSpotFleetRequests` legacy API family, Spot-Fleet auto-scaling, and the Batch integration that depends on the tagging role.

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs.
- **Prefer the safe oracle first.** Nearly every lead here is confirmable **before touching any live resource** with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` and read-only `iam:GetPolicyVersion` / `iam:GetRole` / `kms:ListGrants` / `aws ... --dry-run`. Live confirmation uses only synthetic canary roles/instances/keys in an account you are authorized to test, torn down immediately.
- **This service runs almost entirely inside the customer's own account.** There is no multi-tenant service fleet and no customer-reachable data plane — the "service" is the control-plane API plus the service-linked roles that call `RunInstances`/`TerminateInstances` on your behalf. The usual **cross-tenant** surface is therefore thin; the real value is **intra-account privilege escalation via AWS-authored IAM artifacts** and **confused-deputy / cross-account trust** that AWS leaves unscoped by default.
- **HARD STOP:** The only true AWS-service-plane identities in scope are the service principal `spotfleet.amazonaws.com` and the service-linked roles `AWSServiceRoleForEC2SpotFleet`, `AWSServiceRoleForEC2Spot`, and `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`. Treat them read-only. The moment any evidence shows you have reached, assumed, or extracted credentials/ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. Starting from the AWS-published Spot Fleet "user" sample policy (`spot-fleet-prerequisites`), **escalate to an arbitrary / admin role** in the account — chaining the optional `iam:CreateRole`/`AttachRolePolicy`/`AddRoleToInstanceProfile`/`CreateInstanceProfile` block, or exploiting the SLR's own wildcard `iam:PassRole`, to attach a privileged instance profile to an instance the attacker controls.
2. As a principal who holds `ec2:RequestSpotFleet` but **not** `iam:PassRole` for a powerful instance-profile role, cause a Spot Fleet to launch an instance carrying that role (launch-spec `IamInstanceProfile` late-binding / SLR wildcard-PassRole bypass).
3. Drive `spotfleet.amazonaws.com` to **assume a same-named `aws-ec2-spot-fleet-tagging-role` in another account** (`IamFleetRole` ARN with wildcard account segment + default no-condition trust policy) — a classic confused-deputy chain.
4. Use the SLR's unconditioned `ec2:TerminateInstances` (keyed only on **presence** of the `aws:ec2spot:fleet-request-id` tag key) or the tagging role's fully-unconditioned `TerminateInstances`/`RunInstances`/`CreateTags` on `*` to **terminate or mis-manage instances outside the fleet that passed the role**.
5. Use the SLR's `elasticloadbalancing:RegisterTargets` on `*/*` to **register fleet instances into a target group fronting another workload** in the account (traffic hijack / insertion).
6. From the auto-scaling permission set, **describe/modify a Spot Fleet request you do not own**, or **push target capacity past the scaling policy's min/max** by calling `ec2:ModifySpotFleetRequest` directly, or **tamper with the CloudWatch alarms** that gate a victim fleet's scaling (cost/availability DoS).
7. Enumerate **doc-vs-reality** and **detection-blind-spot** deltas: the SLR's actual attached policy vs its documented action list; the Config rule `ec2-spot-fleet-request-ct-encryption-at-rest` ignoring all launch-template-based fleets; `cancelled_running` orphaned instances outliving their 48-hour event history.

---

## 2. Components, Assets, and Design

**What it is.** Spot Fleet is a console-supported, API/CLI-drivable orchestration layer (`RequestSpotFleet`) that launches a mixed fleet of Spot + optional On-Demand instances from either inline **launch specifications** (`LaunchSpecifications.N`) or a versioned **launch template** (`LaunchTemplateConfigs.N`), into the **caller's own account/VPC**. It is the legacy twin of EC2 Fleet (`CreateFleet`), explicitly "no planned investment." Request types: `request` (one-time) and `maintain` (self-replenishing; the only type that can be modified or auto-scaled). `instant` is listed in the API but "not used by Spot Fleet."

**Customer-facing interface.** SigV4 EC2 Query/SDK APIs + the EC2 console "Spot Requests" screen. No non-SDK/internal endpoints documented. No customer-reachable data plane. Resource-level IAM permissions are **not supported** for the `spot-fleet-request` resource type (documented in `tag-spot-fleet` — specifying it as a `Resource` yields an unauthorized exception), so policies gating these APIs are forced to `Resource:"*"`.

**Identity / roles.**
- `AWSServiceRoleForEC2SpotFleet` — SLR assumable only by `spotfleet.amazonaws.com`; attached policy `AWSEC2SpotFleetServiceRolePolicy` (v4, edited 2020-03-16). Launches/terminates/tags instances on your behalf.
- `AWSServiceRoleForEC2Spot` — SLR for the underlying Spot Instance requests.
- `aws-ec2-spot-fleet-tagging-role` — a **customer-created role you pass as `IamFleetRole`**; AWS tells you to attach the managed policy `AmazonEC2SpotFleetTaggingRole` (v5). This is the copy-verbatim artifact at the center of the plan.
- `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest` — SLR for Spot-Fleet auto-scaling (policy `AWSApplicationAutoscalingEC2SpotFleetRequestPolicy`). Legacy customer-managed `aws-ec2-spot-fleet-autoscale-role` + `AmazonEC2SpotFleetAutoscaleRole` are "no longer required."
- End-user principal: holds the **AWS-authored sample policy** copied verbatim from `spot-fleet-prerequisites` (primary attack surface).

**Resource identifiers.** Spot Fleet request IDs `sfr-` + a UUIDv4-class 8-4-4-4-12 hex string (~122 bits entropy — the "short-hex" vs "UUID-style" examples in the docs are the same high-entropy format, **not enumerable**). Instance/volume IDs, launch-template IDs + `$Latest`/`$Default` version aliases, CMK ARNs, target-group/LB ARNs.

**Untrusted-data entry points.** Launch-spec/launch-template `UserData` (base64 boot code, 16 KB), `IamInstanceProfile`, `ImageId` (incl. the `resolve:ssm:<ARN>` alias in launch templates), `GroupSet`/`NetworkInterfaceSet`/`SubnetId`, `BlockDeviceMapping` (encrypted AMI/EBS → KMS grant), `TagSpecifications`, `LoadBalancersConfig`, price-protection knobs. `Context` field is "Reserved."

```
 Caller (IAM principal w/ AWS sample policy)
     │  RequestSpotFleet / ModifySpotFleetRequest / CancelSpotFleetRequests
     │  (passes IamFleetRole ARN  ──┐  + optional launch-spec IamInstanceProfile)
     ▼                              │  PassRole gate (user policy scoped to :role/aws-ec2-spot-fleet-tagging-role, account = * )
 Spot Fleet control plane          │
     │  assumes (sts:AssumeRole)    ▼
     ├─► aws-ec2-spot-fleet-tagging-role  (IamFleetRole; trust = spotfleet.amazonaws.com, NO SourceArn/SourceAccount by default)
     │        policy AmazonEC2SpotFleetTaggingRole: RunInstances/TerminateInstances/CreateTags on *  (NO condition);  PassRole * (PassedToService=ec2)
     └─► AWSServiceRoleForEC2SpotFleet (SLR)
              policy AWSEC2SpotFleetServiceRolePolicy:
                 RunInstances/RequestSpotInstances/Describe* on *
                 PassRole on *  (cond: PassedToService = ec2.amazonaws.com)        ◄── pass ANY role to EC2
                 TerminateInstances on *  (cond: tag KEY aws:ec2spot:fleet-request-id = "*")  ◄── presence, not ownership
                 elasticloadbalancing:RegisterTargets on *:*:*/*                    ◄── any target group in acct
                                   │ RunInstances
                                   ▼
                           EC2 instance (IamInstanceProfile creds via IMDS; UserData boot code; EBS from encrypted AMI → KMS grant)
                                   │ (maintain-type) register as Application Auto Scaling scalable target
                                   ▼
                   Application Auto Scaling SLR ──ModifySpotFleetRequest / CloudWatch alarms (all Resource:*)──► scale
```

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `RequestSpotFleet` | SDK/Query | **Yes** | External | Create a Spot Fleet request; takes `IamFleetRole`, launch specs/templates, tags | Yes | Caller w/ `ec2:RequestSpotFleet` + `iam:PassRole` | **Legacy, no investment.** `Context` = Reserved. No resource-level perms. |
| `ModifySpotFleetRequest` | SDK/Query | **Yes** | External | Change target capacity (maintain only) | Yes | Caller or autoscale role; `Resource:"*"` | Resource-by-ID (`sfr-`). Also in autoscale SLR policy. |
| `CancelSpotFleetRequests` | SDK/Query | **Yes** | External | Cancel ≤100 fleets; `TerminateInstances` boolean | Yes | Caller; `Resource:"*"` | `--no-terminate-instances` orphans running instances (`cancelled_running`). No instance-ID parameter. |
| `DescribeSpotFleetRequests` | SDK/Query | No | External | List "your" fleet requests + config/tags | Yes | Caller; `Resource:"*"` | `MaxResults` has **no documented range** (siblings cap 1–1000). |
| `DescribeSpotFleetInstances` | SDK/Query | No | External | Instances of one `sfr-` | Yes | Caller | Requires single `sfr-`; `MaxResults` 1–1000. |
| `DescribeSpotFleetRequestHistory` | SDK/Query | No | External | Event history of one `sfr-` | Yes | Caller | Events delayed ≤30 s, retained **48 h**. |
| `CreateTags` (on fleet/instance/volume) | SDK/Query | **Yes** | External | Tag resources | Yes | Caller + SLR + tagging role | `Resource:"*"` forced for `spot-fleet-request`. |
| `register-scalable-target` / `put-scaling-policy` / `put-scheduled-action` (Application Auto Scaling) | SDK/Query | **Yes** | External | Register `sfr-` as scalable target; attach scaling policy / schedule | Yes | Caller w/ autoscale policy | Example policy = single statement, `application-autoscaling:*` + `cloudwatch:*` + `sns:*` on `*`, **no Condition**. |

**Doc-flagged pointers kept verbatim:** "resource-level permissions are not currently supported for the `spot-fleet-request` resource" (`tag-spot-fleet`); "We strongly discourage using the RequestSpotFleet API because it is a legacy API with no planned investment" (`API_RequestSpotFleet`); the `IamFleetRole`/user-policy "inconsistent tagging behavior" warning (`spot-fleet-prerequisites`); "The rule does not evaluate spot fleet requests using launch templates" (Config rule).

---

## 4. Boundary-lens catalog — firing lenses

### Lens R/S — AWS-authored IAM-artifact audit (HIGHEST YIELD)

**R1 — SLR grants wildcard `iam:PassRole` to EC2.**
**Claim:** `AWSEC2SpotFleetServiceRolePolicy` lets the Spot Fleet SLR pass **any** role in the account to EC2 as an instance profile, so a caller who can influence the launch spec's `IamInstanceProfile` (or chain through it) attaches a role they could not pass directly.
**Mechanism:** policy statement 2 — `"Action":["iam:PassRole"], "Resource":["*"], "Condition":{"StringEquals":{"iam:PassedToService":["ec2.amazonaws.com","ec2.amazonaws.com.cn"]}}` (confirmed online, v4).
**Confirm/Refute oracle:** read-only `iam:GetPolicyVersion` to confirm the statement; then `iam:SimulatePrincipalPolicy` of a scoped canary user holding **only** the AWS sample user policy, asking whether a Spot Fleet request can land a privileged instance profile the user lacks direct `PassRole` for. Live: synthetic canary role + fleet, torn down.
**Preconditions / Cost:** canary IAM only; free to simulate. **Severity-if-true:** High (non-admin → privileged-role creds on an instance). **Stop:** confirm existence; do not use the obtained creds.

**R2 — `AmazonEC2SpotFleetTaggingRole` is strictly broader than the SLR and fully unconditioned.**
**Claim:** The copy-verbatim role a customer passes as `IamFleetRole` can `RunInstances`/`TerminateInstances`/`CreateTags` on `Resource:"*"` with **no tag/ownership condition at all** — so a fleet using this role can terminate/mis-manage **any** instance in the account, not just its own.
**Mechanism:** `AmazonEC2SpotFleetTaggingRole` (v5) statement 1 — those four actions + `DescribeImages`/`DescribeSubnets`/`DescribeInstanceStatus`/`RequestSpotInstances` on `*`, no Condition; statement 2 `iam:PassRole` on `*` (PassedToService ec2). Unlike the SLR, `TerminateInstances` here is **not** even tag-gated.
**Confirm/Refute oracle:** `iam:GetPolicyVersion` on `arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetTaggingRole`; `iam:SimulatePrincipalPolicy` for `ec2:TerminateInstances` against an arbitrary foreign-fleet instance ARN under this policy → expect `allowed`.
**Severity-if-true:** Medium–High (AWS-authored, copy-attach → in-scope per Lens R carve-out; blast radius = whole account's EC2). **Owner-to-fix:** AWS (uneditable managed policy).

**R3 — Tagging-role trust policy ships with no confused-deputy condition.**
**Claim:** AWS's own CLI runbook creates `aws-ec2-spot-fleet-tagging-role` with a trust policy that trusts `spotfleet.amazonaws.com` for `sts:AssumeRole` with **no `aws:SourceArn`/`aws:SourceAccount`** — and the console flow leaves it a blank "optional" slot; the hardening is only *recommended* in the EC2 prereqs page, never defaulted.
**Mechanism:** `batch/.../spot-fleet-roles-cli.md` prints the exact no-`Condition` trust policy; `spot-fleet-prerequisites` §"Cross-service confused deputy prevention" only *recommends* adding the keys.
**Confirm/Refute oracle:** read-only `iam:GetRole` → inspect `AssumeRolePolicyDocument` for the absent `Condition`. **Severity-if-true:** enabler for B1 (not a standalone breach). **Owner-to-fix:** shared (AWS default guidance + customer).

**S1 — SLR `TerminateInstances` keys on tag *presence*, not ownership.**
**Claim:** `ec2:TerminateInstances` is allowed on `Resource:"*"` conditioned only `StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id : "*"` — i.e. matches the tag **key** regardless of value, so the SLR can terminate **any** instance carrying that key (including instances of a *different* Spot Fleet in the same account).
**Mechanism:** `AWSEC2SpotFleetServiceRolePolicy` statement 4 (confirmed online).
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` with a resource context tag `aws:ec2spot:fleet-request-id` set to a *different* fleet's id → expect `allowed`. Can an attacker set this key on a victim instance to mark it for termination? The `aws:` prefix is a **reserved/service tag** normally unsettable by `CreateTags` — test that boundary (`ec2:CreateTags` with that key → expect denied/ignored). If reserved-tag protection holds, this is a cross-fleet-only self-impact (Low); if a user can set it, it becomes a victim-instance-termination primitive (Medium–High).
**Severity-if-true:** Medium (cross-fleet termination within account). **Owner-to-fix:** AWS.

**S2 — SLR `elasticloadbalancing:RegisterTargets` on `*:*:*/*`.**
**Claim:** The SLR can register fleet instances into **any** ELB target group / with any Classic LB in the account; `LoadBalancersConfig` lets the caller name the target. An attacker fleet could insert its instances behind a target group fronting a victim workload.
**Mechanism:** `AWSEC2SpotFleetServiceRolePolicy` statements 5–6 (`loadbalancer/*` and `*/*`); `SpotFleetRequestConfigData.LoadBalancersConfig` registers running instances with "specified" LBs/target groups.
**Confirm/Refute oracle:** `iam:GetPolicyVersion` confirms `*/*`; `iam:SimulatePrincipalPolicy` of the SLR for `elasticloadbalancing:RegisterTargets` against a foreign target-group ARN → `allowed`. Live: register a canary instance into a canary-but-"other-workload" target group you own; confirm no ownership/consistency check binds the target group to the fleet.
**Severity-if-true:** Medium–High (traffic insertion / request smuggling into another service). **Owner-to-fix:** AWS (scoping) + customer (target-group resource policy, if any).

**S3 — User sample policy teaches a privesc-capable optional block.**
**Claim:** The "Optional IAM APIs" block in `spot-fleet-prerequisites` (`iam:CreateRole`, `iam:AttachRolePolicy`, `iam:AddRoleToInstanceProfile`, `iam:CreateInstanceProfile`, `iam:GetRole`, `iam:ListPolicies` on `*`) is a textbook self-escalation combo — a holder can craft an admin role + instance profile and (via the fleet) attach it to an instance they control.
**Mechanism:** `spot-fleet-prerequisites` §"Optional IAM APIs" lists these verbatim with no resource scoping.
**Confirm/Refute oracle:** `iam:SimulatePrincipalPolicy` chain: `CreateRole`→`AttachRolePolicy(AdministratorAccess)`→`CreateInstanceProfile`→`AddRoleToInstanceProfile`→ pass via fleet. **Severity-if-true:** High (admin). **Owner-to-fix:** customer footgun **but** AWS-published guidance — flag as a documentation hardening recommendation (Informational→Low on the artifact; the live privesc is a customer-config High).

### Lens B — Confused deputy / cross-account PassRole

**B1 — Cross-account `IamFleetRole`.**
**Claim:** The user sample policy's `iam:PassRole` resource is `arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role` — the **account segment is wildcarded**. Combined with R3 (no SourceArn/SourceAccount on the victim role's trust policy), a caller in account A may be able to drive `spotfleet.amazonaws.com` to assume a same-named tagging role in account B, inheriting B's unconditioned `RunInstances`/`TerminateInstances`/`CreateTags` on `*`.
**Mechanism:** `spot-fleet-prerequisites` sample policy (`::*:role/aws-ec2-spot-fleet-tagging-role`); `API_RequestSpotFleet` documents `IamFleetRole` as a bare ARN string with no stated same-account constraint.
**Confirm/Refute oracle:** read-only `iam:SimulatePrincipalPolicy` for `iam:PassRole` with resource = a tagging-role ARN in a different account + `iam:PassedToService=ec2.amazonaws.com`. Then — **the decisive step** — determine whether `RequestSpotFleet` itself enforces same-account `IamFleetRole` server-side (undocumented): a single `--dry-run` `RequestSpotFleet` naming a role ARN in a **second account you also own/are authorized for**. If accepted → cross-account confused deputy.
**Preconditions / Cost:** sample `PassRole` wildcard attached; a reachable `aws-ec2-spot-fleet-tagging-role` with default trust in the target account; one simulate + one dry-run. **Severity-if-true:** High (cross-account role assumption via AWS's SLR). **Severity-if-false:** collapses to intra-account privesc (still real via R1/R2). **Stop:** on any evidence the assumed identity is AWS's own fleet plane, hard-stop.

### Lens A — Cross-tenant / IDOR  (mostly null, documented here with evidence)

**A1 — Resource-by-ID APIs on `Resource:"*"`.** `DescribeSpotFleetRequests`/`DescribeSpotFleetInstances`/`DescribeSpotFleetRequestHistory`/`ModifySpotFleetRequest`/`CancelSpotFleetRequests` all take `sfr-` IDs and (resource-level perms unsupported) run under `Resource:"*"`.
**Oracle & verdict:** `iam:SimulatePrincipalPolicy` confirms IAM cannot scope by ID — this is a **within-account over-broad-grant** (any principal that can call these at all can call them for *every* fleet in the account), **not** cross-tenant. Cross-account reachability is **untestable from docs** and shows no fleet-specific weakness vs the generic EC2 account-partitioning that protects `DescribeInstances` etc. `sfr-` IDs are ~122-bit UUIDs → **ID enumeration null**. `CancelSpotFleetRequests` has **no instance-ID parameter** (termination targets are derived server-side from the fleet's own tracked instances) → **no instance-redirection vector**. `sfr-` is paired with SigV4 on every call → **not a bearer capability** (Lens M null). **Severity:** the within-account unscopable-grant is a least-privilege design gap worth flagging to an IAM reviewer (Low); cross-tenant is a null hypothesis given the evidence.

### Lens X — Action-family / twin parity

**X1 — `MaxResults` validator divergence.** `DescribeSpotFleetRequests` documents `MaxResults` with **no valid range**, while `DescribeSpotFleetInstances`/`History` cap it at 1–1000.
**Oracle:** read-only `DescribeSpotFleetRequests MaxResults=0` / `=100000` against your own account → does it 400 (shared validator) or clamp/accept (looser)? **Severity:** Low (input-validation inconsistency / minor error-oracle, not an isolation bypass).
**X2 — Legacy alias:** none found; "See Also" lists exactly one Query action per API, whole family flagged legacy → **null**.

### Lens O — Audit-log evasion / orphaned resources

**O1 — `cancelled_running` orphans instances.** `CancelSpotFleetRequests --no-terminate-instances` leaves instances running under `cancelled_running` indefinitely ("until interrupted or terminated manually"); request record is only deleted 48 h **after instances are terminated**, so an orphaned fleet may never hit the deletion clock.
**O2 — history decays at 48 h.** `DescribeSpotFleetRequestHistory` events retained only 48 h — an attacker's fleet-launch history self-expires independent of whether orphaned instances still exist.
**Oracle:** read-only — cancel a canary fleet with `--no-terminate-instances`, confirm `cancelled_running` persists + instances still billing + history empty after 48 h. **Severity:** Medium — post-exploitation persistence ("leave payload instances running while the fleet looks deleted") + forensic decay; within-account / compromised-credential technique, not cross-tenant. **Note:** both are *documented* AWS behaviors, so this is an IR/detection-assumption gap, not a bug.

### Lens L — Resource exhaustion / scaling-guardrail / DoS (auto-scaling)

**L1 — Direct `ModifySpotFleetRequest` bypasses scaling min/max.** The docs phrase the min/max bound as a property of **scaling policies** ("Scaling policies do not scale … below min / above max"), never of the raw EC2 API. The autoscale permission set grants `ec2:ModifySpotFleetRequest` directly on `Resource:"*"` with **no `aws:CalledVia application-autoscaling.amazonaws.com` condition**. The `Set to` step-adjustment sets absolute capacity; cooldown is asymmetric (scale-out "immediately" even during scale-in cooldown).
**Oracle:** `iam:SimulatePrincipalPolicy` confirms unconditional `ModifySpotFleetRequest`; whether EC2 re-validates against the registered scalable-target min/max is **undocumented** — flag for API-reference confirmation, test only with a canary maintain-fleet. **Severity:** High (uncapped Spot launches = billing DoS; capacity→0 = outage).
**L2 — CloudWatch alarm tampering.** `cloudwatch:PutMetricAlarm`/`DeleteAlarms`/`DescribeAlarms` on `Resource:"*"` → create a spoofed alarm to trigger a victim fleet's step-scaling, or delete the protective alarm. The target-tracking page literally warns "Do not edit or delete the CloudWatch alarms that Spot Fleet manages" — process, not IAM, is the control.
**Oracle:** `iam:SimulatePrincipalPolicy` for `PutMetricAlarm`/`DeleteAlarms` against another fleet's auto-named alarm ARN (`TargetTracking-sfr-<id>-AlarmHigh-…`) → `allowed`. **Severity:** Medium–High (cost / availability).
**L3 — lifecycle churn / modify race.** Cancel-without-terminate churn bounded by 100-fleets-per-call + account quota (self-DoS, folds into O1). Concurrent `ModifySpotFleetRequest` on one maintain fleet — server-side locking undocumented; low-cost race probe against a self-owned fleet. **Severity:** Low–Medium, within-account.

### Lens E — RBAC / role exceeds purpose (auto-scaling)

**E1 — autoscale example policy over-broad.** The documented "sufficient to autoscale a spot fleet" policy includes `application-autoscaling:*` (not scoped to the EC2 `spot-fleet-request` scalable-target type) and `sns:CreateTopic`/`sns:Subscribe` on `*` — a credential provisioned for one feature can manage autoscaling for unrelated services and stand up SNS topics (exfil/phishing channel).
**Oracle:** `iam:SimulatePrincipalPolicy` for `application-autoscaling:RegisterScalableTarget` with `ServiceNamespace=dynamodb|ecs|sagemaker` → `allowed` confirms cross-feature reach. **Severity:** Medium (blast-radius widening on compromise), within-account.

### Lens H — KMS / encryption + Config-rule blind spot

**H1 — Config rule ignores launch-template fleets.** `ec2-spot-fleet-request-ct-encryption-at-rest` checks only `encrypted==true` on EBS in **classic launch-spec** fleets and explicitly "does not evaluate spot fleet requests using launch templates," and inspects only the boolean (no CMK/key-id / encryption-context awareness).
**Oracle:** read-only `configservice get-compliance-details-by-config-rule` + `describe-spot-fleet-requests` to find `LaunchTemplateConfigs`-based fleets that generate zero findings regardless of encryption state. **Severity:** Medium (compliance/detection blind spot). **Owner-to-fix:** AWS (managed rule).
**H2 — encrypted-AMI/EBS CMK grant (shared with EC2 Fleet).** `spot-fleet-prerequisites` tells you to `kms:create-grant` the SLR `Decrypt/Encrypt/GenerateDataKey/GenerateDataKeyWithoutPlaintext/CreateGrant/DescribeKey/ReEncryptFrom/ReEncryptTo` on the CMK — broader than launching needs (`CreateGrant`, `Encrypt`, `ReEncrypt*`) and with **no encryption-context constraint**. Check grant survival after the documented "delete the SLR" teardown and whether recreating the identically-named SLR silently re-inherits CMK access. **Oracle:** read-only `kms:ListGrants`. **Severity:** Medium (over-scoped grant; grant-survival = see EC2 Fleet plan §KMS, same shape). Cross-reference `ec2-fleet-attack-research-plan.md`.

### Lens I — Tagging / ABAC

**I1 — inconsistent tagging → ABAC escape.** `spot-fleet-prerequisites` documents that differences between the **user's** and the **`IamFleetRole`'s** `CreateTags` permissions cause **some fleet-launched instances to not be tagged**. If the account enforces ABAC/governance on launched instances via tags, instances the fleet launches **untagged** escape that control. The AWS fix for the underlying tagging bug was to **widen** the role (unscoped `CreateTags` on `*`, the `AmazonEC2SpotFleetRole`→`AmazonEC2SpotFleetTaggingRole` migration) rather than add an ABAC condition.
**Oracle:** `iam:GetPolicyVersion` to confirm no `aws:ResourceTag` condition on `CreateTags`; reason about an ABAC policy keyed on a required tag vs an untagged fleet instance. **Severity:** Medium if ABAC is the access-control mechanism. Also: `SpotFleetTagSpecification.ResourceType` must be exactly `instance` (launch-spec) or `spot-fleet-request`/`instance` (request-level) or the whole request **fails** — a brittle validator, not obviously a breach (Low).

---

## 5. Recommended Areas of Focus (priority order)

1. **AWS-authored IAM artifacts (R1, R2, S1, S2, R3)** — highest yield, mostly confirmable read-only with `GetPolicyVersion` + `SimulatePrincipalPolicy`. Intra-account privesc / over-broad SLR; in-scope per the Lens R carve-out because the policies are AWS-managed and uneditable.
2. **Cross-account confused deputy (B1)** — the one potential *cross-account* lead; decisive oracle is a single `--dry-run RequestSpotFleet` with a second-account `IamFleetRole`. Elevate above intra-account leads **only if** the dry-run is accepted.
3. **User-policy privesc chain (S3)** — the optional `CreateRole/AttachRolePolicy/…` block → admin.
4. **ELB target insertion (S2)** and **KMS grant scope/survival (H2)** — cross-workload reach within the account.
5. **Auto-scaling DoS (L1, L2) and role-excess (E1)** — cost/availability + blast-radius; all `Resource:"*"` no-condition.
6. **Detection blind spots (H1 Config rule, O1/O2 orphaned instances + history decay)** — defense-evasion / IR assumptions.
7. **Lower:** X1 validator divergence, I1 tagging/ABAC edge, A1 within-account unscopable grant.

**Kill-chain to compose:** S3 (craft admin role+instance profile) → R1 (SLR wildcard PassRole lets the fleet attach it) → launch-spec `IamInstanceProfile` on an attacker-controlled instance → `UserData` boot code reads the admin creds from IMDS → account-wide admin. Rate at the **end** of the chain (Critical if it lands admin), not the entry point.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Non-admin → admin via fleet-attached instance profile | SLR `PassRole *` + launch-spec `IamInstanceProfile` | User-policy `PassRole` scoped to tagging-role name only; SLR condition `PassedToService=ec2` |
| Cross-account role assumption via `IamFleetRole` | `RequestSpotFleet` + tagging-role trust | *Recommended* `aws:SourceArn`/`aws:SourceAccount` (not default); server-side same-account check (undocumented) |
| Terminate instances outside the fleet | SLR/tagging-role `TerminateInstances` | SLR tag-key condition (presence only); tagging role = none; `aws:`-prefixed reserved tag unsettable by users |
| Insert instances behind a victim target group | SLR `RegisterTargets */*` + `LoadBalancersConfig` | None documented beyond target-group resource policy (if any) |
| Push capacity past scaling min/max; alarm tamper | autoscale `ModifySpotFleetRequest`/CloudWatch on `*` | Min/max enforced only in the scaling-policy path; "don't edit the alarms" prose |
| Over-scoped / surviving CMK grant | SLR KMS grant | Grant operations list in docs; no encryption-context constraint |
| Unencrypted EBS escapes compliance | Config rule | Rule skips launch-template fleets; boolean-only |
| Persist via orphaned `cancelled_running` instances | Cancel API | None (documented behavior) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-tenant IDOR via guessing `sfr-` IDs** — IDs are ~122-bit UUIDs; EC2 account-partitioning protects these APIs as it does every `Describe*`/`Cancel*`. No fleet-specific weakness. (A1.)
- **`sfr-` as a leaked capability** — never a bearer token; every call is SigV4-authed.
- **IMDS on the managed instances** — the instances are the customer's own; a user steering their own instance's boot/creds is not a boundary breach (becomes in-scope only when a *more-privileged* role is attached via R1/S3).
- **UserData as "injection"** — attacker-controlled boot code on one's own instance is expected; only interesting chained to a privileged instance profile (K/B).
- **Single-tenant self-DoS / cost churn** (L3 churn) — bounded by the attacker's own account quotas/bill, unless from compromised credentials (then it is a griefing technique, O1).
- **AWS's own service plane** — `spotfleet.amazonaws.com` and the SLRs are the shared-responsibility line and a **hard stop**.
- **Customer-authored policies** — a weak policy the customer wrote themselves is a footgun (out of scope); the in-scope artifacts here are the AWS-managed/uneditable and copy-verbatim-runbook ones (R1/R2/R3/S1/S2/H1/I1).

---

## 8. Null hypotheses / doc gaps (pages named)

- **Lens C (credential vending / STS session scope):** null. No session-policy / ProvidedContext / per-tenant role-vending surface — `IamFleetRole` is a static ARN. (Pages: `spot-fleet-prerequisites`, `API_RequestSpotFleet`, `API_SpotFleetRequestConfigData`.) B1 is the PassRole/trust variant, routed to Lens B.
- **Lens D / V (data-plane→control-plane / network segmentation):** null. No service-owned fleet, no control/storage ENI, no multi-tenant subnet — all instances live in the customer VPC. (Pages: `work-with-spot-fleets`, `create-spot-fleet`.)
- **Lens F (translation-layer / wire-protocol injection):** null. No query/protocol translator; the API is plain EC2 Query/SDK. (Pages: `API_RequestSpotFleet`, `API_SpotFleetRequestConfigData`.)
- **Lens G (SSRF):** null. No field the service dereferences server-side (no URL/webhook/logo/import). `ImageId`/`SubnetId`/`IamFleetRole` are AWS resource identifiers, not fetched locations. The `resolve:ssm:<ARN>` AMI alias (launch templates) is the one adjacent surface → see EC2 Fleet plan Lens EE/U. (Pages: `API_SpotFleetLaunchSpecification`, `create-spot-fleet`.)
- **Lens K (prompt injection):** N/A — no LLM/agent in the pipeline.
- **Lens M (shared-identifier interception):** null — `sfr-` IDs always paired with SigV4; no presigned/one-time-token flow. (Pages: all five `API_*` request pages.)
- **Lens N (ARN/namespace migration):** null — single legacy namespace, no dual-live migration. (`spot-fleet-states`, API "See Also" blocks.)
- **Lens P (identity proofing / registration):** N/A — no onboarding/KYC/OTP workflow.
- **Lens Q (untrusted file upload):** did not fire from the pages reviewed; `UserData` boot code lives on `SpotFleetLaunchSpecification` (read) but has no server-side parse/render step the service performs — it is handed to the customer's own instance. No logo/image/attachment upload. (Pages: `API_SpotFleetLaunchSpecification`, `API_SpotFleetTagSpecification`.)
- **Lens O for `SpotFleetMonitoring`:** null — the `Enabled` field toggles 1-min vs 5-min CloudWatch metrics, not an audit control. (`API_SpotFleetMonitoring`.) (O1/O2 above fire from the lifecycle pages instead.)
- **Lenses W, Y, AA, BB, CC, DD, EE, FF:** no triggers in the Spot Fleet doc set (no attestation gate, no customer-facing TLS endpoint/mTLS, no share/revoke lifecycle beyond the KMS grant in H2, no multi-parser request path, no upstream-asserted-identity header, no caching layer, no predictable-global-namespace resolution by Spot Fleet itself, no JWT/OIDC). EE's AMI-name-resolution variant and AA's KMS-grant-survival variant are covered by the EC2 Fleet plan — cross-reference rather than duplicate.

**Doc gaps requiring live/API-reference confirmation (not resolvable from docs):**
1. Does `RequestSpotFleet` enforce **same-account `IamFleetRole`** server-side? (gates B1 severity)
2. Does EC2 re-validate `ModifySpotFleetRequest` against the registered scalable-target **min/max**? (gates L1)
3. Can `ec2:CreateTags` set the **`aws:ec2spot:fleet-request-id`** reserved tag key? (gates S1 → victim-instance termination)
4. Server-side locking for concurrent `ModifySpotFleetRequest`. (L3)
5. `CommonErrors.md` — is there a documented NotFound-vs-AccessDenied distinction that forms an existence oracle? (A1)

---
*End of plan. Documentation-derived hypotheses only; nothing herein has been executed against a live AWS account.*
