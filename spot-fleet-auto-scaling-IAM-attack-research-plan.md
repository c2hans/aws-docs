# Spot Fleet Auto Scaling IAM (sample operator policy) — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/spot-fleet-auto-scaling-IAM.html` (= "IAM permissions required for Spot Fleet automatic scaling"), online + offline mirror (`/work/aws-docs/docs/AWSEC2/latest/UserGuide/spot-fleet-auto-scaling-IAM.md`) cross-checked and byte-identical. Scoping semantics resolved from the IAM **Service Authorization Reference** mirror: `list_sns.md`, `list_cloudwatch.md`, `list_iam.md`, `list_application-autoscaling.md` (all under `/work/aws-docs/docs/service-authorization/latest/reference/`). **Status: documentation-derived hypotheses only; nothing tested against a live account.**

> **Slug pitfall (reusable):** the Service Authorization Reference pages for these services are `list_sns`, `list_cloudwatch`, `list_iam` — **no `amazon`/`aws` prefix**. `list_amazonsns`, `list_amazoncloudwatch`, `list_awsidentityandaccessmanagement` all 404. Application Auto Scaling is the **hyphenated** `list_application-autoscaling` (see [[reference-aws-iam-service-auth-ref-url]] and the sibling plan's §8).

> **Scope note / relationship to siblings.** This page is also cited as a *child* lead-source by `spot-fleet-automatic-scaling-attack-research-plan.md` (the control-loop companion). That sibling owns the **Spot-Fleet-side** mechanics of this surface — the SLR policy audit (its Area S1), the IAM-unscopable ownership chain that terminates a foreign fleet (A1), min/max guarantee-vs-enforcement (U1), managed-alarm/custom-metric tampering (L1/L2), the caller-`RoleARN` confused deputy (B1), and the legacy-role parity (X1). **This plan deliberately does NOT restate those.** It owns the one thing the sibling only lists in a single table row and never develops: the **printed sample *identity* policy audited as an AWS-published, copy-verbatim artifact — specifically its over-grants that reach services OTHER than EC2 Spot Fleet** (SNS, account-wide CloudWatch read, any-service SLR creation, all-service Application Auto Scaling). Where a lead reaches the Spot-Fleet terminate/launch primitive it **cross-references** the sibling (and `modify-spot-fleet-attack-research-plan.md`) rather than restating it.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This surface is a **single AWS-authored artifact** (an identity policy a human copies verbatim). Per the fleet-services memory, the highest-value finding class here is **intra-account over-grant / blast-radius escalation via an uneditable-or-copy-verbatim AWS artifact**, not cross-tenant IDOR. The relevant lenses are **R (IAM-artifact audit)**, **S (condition-key scoping)**, **U (doc guarantee vs artifact)**, with chains into **J-style exfil** (SNS Subscribe) and the sibling's **A1** terminate chain.
- **In-scope vs footgun:** the sample policy is **AWS-published and the docs tell the customer to copy it verbatim** ("users must have permissions to use the actions shown in the following example policy"). Per the skill's carve-out, a weak default in an AWS-published copy-verbatim artifact is **in scope / Tier-2 reportable**, NOT a customer footgun.
- The safe first oracle for every lead here is **`iam:SimulateCustomPolicy`** (paste the exact sample JSON, no resources touched) and `iam:SimulatePrincipalPolicy` against a scoped canary role. Escalate to live calls only with a scoped role holding **exactly** the sample policy, in an authorized account, with synthetic/canary resources, and tear everything down.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives
1. Show that a principal holding **only the published sample policy** can perform actions **against services entirely unrelated to Spot Fleet auto-scaling** — the artifact's own purpose statement ("to use automatic scaling for Spot Fleet") implies it should not.
2. **SNS:** show the holder can **subscribe an attacker-controlled endpoint to any existing SNS topic in the account** (notification/data exfil) and **enumerate+read every topic's attributes, policy, data-protection policy and subscriptions** — far beyond "scaling notifications."
3. **CloudWatch:** show the holder can **read all metric data in the account** (`GetMetricStatistics`/`ListMetrics` — operational/business-data disclosure) and **delete/overwrite/disable any alarm in the account** (silence security/ops alerting), none of it scoped to the fleet's own `TargetTracking*` alarms.
4. **IAM:** show the holder can **create a service-linked role for any AWS service**, not just `application-autoscaling.amazonaws.com`.
5. **Application Auto Scaling:** show the holder can **register/scale/deregister scalable targets for completely unrelated services** (DynamoDB, ECS, Aurora, Lambda, SageMaker, …), because `application-autoscaling:*` on `*` is cross-namespace and there is no resource-id condition key.
6. Show the doc's claim that you "can also create your own IAM policies that allow more fine-grained permissions" is undercut by the sample itself being maximally coarse (every one of its blocks had a documented narrowing mechanism it declined to use).

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** The page is a single **sample IAM identity policy** the docs instruct a human operator to attach so they can configure Spot Fleet auto-scaling from the console/CLI. "Automatic scaling for Spot Fleet is made possible by a combination of the Amazon EC2, Amazon CloudWatch, and Application Auto Scaling APIs." The policy is **one `Allow` statement, 17 action entries, `Resource:"*"`, no `Condition` block**, spanning **five services**: EC2, CloudWatch, Application Auto Scaling, IAM, and SNS.

- **The artifact (asset under audit):** the printed JSON (verbatim below). It is AWS-authored and the customer copies it as-is.
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "application-autoscaling:*",
      "ec2:DescribeSpotFleetRequests", "ec2:ModifySpotFleetRequest",
      "cloudwatch:DeleteAlarms", "cloudwatch:DescribeAlarmHistory",
      "cloudwatch:DescribeAlarms", "cloudwatch:DescribeAlarmsForMetric",
      "cloudwatch:GetMetricStatistics", "cloudwatch:ListMetrics",
      "cloudwatch:PutMetricAlarm", "cloudwatch:DisableAlarmActions",
      "cloudwatch:EnableAlarmActions",
      "iam:CreateServiceLinkedRole",
      "sns:CreateTopic", "sns:Subscribe", "sns:Get*", "sns:List*"
    ],
    "Resource": "*"
  }]
}
```
- **Who holds it:** the human operator configuring auto-scaling. This is an **identity (not resource) policy**, so it is bounded only by SCPs/permission-boundaries, not by any resource policy.
- **Second AWS-authored artifact named on the page:** the **service-linked role** `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest` (audited in the sibling's Area S1 — not restated here) and the **legacy role name** `aws-ec2-spot-fleet-autoscale-role` ("no longer required").
- **Services the artifact reaches, and whether each action is scopable (from the Service Authorization Reference):**

| Service / action | Documented narrowing mechanism that EXISTS | Used by the sample? |
|---|---|---|
| `sns:Subscribe` | `topic*` resource ARN **+** `sns:Endpoint` / `sns:Protocol` condition keys | **No** — `*`, no condition |
| `sns:CreateTopic` | `topic*` resource ARN (name/prefix) | **No** — `*` |
| `sns:Get*` / `sns:List*` | partial (`GetTopicAttributes`/`GetDataProtectionPolicy`/`ListSubscriptionsByTopic` support `topic*`); `ListTopics`/`ListSubscriptions`/`GetSMSAttributes` have **no** scoping | **No** — `*` |
| `cloudwatch:GetMetricStatistics`, `ListMetrics`, `DescribeAlarmsForMetric` | **none exists** — inherently account-wide | n/a (unscopable by design) |
| `cloudwatch:PutMetricAlarm`/`DeleteAlarms`/`Disable`/`EnableAlarmActions` | `alarm` ARN (by `AlarmName`, e.g. `alarm:TargetTracking*`) + tags + `cloudwatch:AlarmActions` | **No** — `*`, no condition |
| `iam:CreateServiceLinkedRole` | `iam:AWSServiceName` condition key | **No** — `*`, no condition |
| `application-autoscaling:*` | `service-namespace` / `scalable-dimension` condition keys (no resource-id key exists) | **No** — wildcard action, no condition, `Resource:"*"` |
| `ec2:ModifySpotFleetRequest` / `DescribeSpotFleetRequests` | `spot-fleet-request*` ARN + `aws:ResourceTag` (see `modify-spot-fleet` plan) | **No** — `*` |

```
          ┌──────────────────────── one AWS-published identity policy (copy-verbatim) ───────────────────────┐
 operator │ Resource:"*"  no Condition                                                                        │
   holds ─┤                                                                                                   │
          │  sns:Subscribe/CreateTopic/Get*/List*  ─────────► EVERY SNS topic in the account (not scaling only)│──► Lens R/J: exfil + recon
          │  cloudwatch:GetMetricStatistics/ListMetrics ───► ALL metric data in the account                   │──► Lens R/U: data disclosure
          │  cloudwatch:Put/Delete/Disable/EnableAlarm ────► ANY alarm (not just TargetTracking*)              │──► Lens R/O: silence alerting
          │  iam:CreateServiceLinkedRole ──────────────────► SLR for ANY AWS service                           │──► Lens R: any-SLR
          │  application-autoscaling:* ────────────────────► scalable targets for ECS/DynamoDB/Aurora/Lambda…  │──► Lens R/S: cross-service
          │  ec2:ModifySpotFleetRequest ───────────────────► (Spot-Fleet terminate/launch primitive)           │──► see sibling A1 / modify-spot-fleet
          └───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Operator holding only the sample policy | **Any SNS topic** in the account (incl. topics owned by other teams/apps) | `sns:Subscribe` on `*` with no `sns:Endpoint`/`sns:Protocol` condition | A subscription to an **attacker-controlled** endpoint is created on a topic the operator's role has no business touching → notification/data exfil (intra-account cross-team) |
| Operator | **Every topic's attributes/policy/subscriptions + account SMS settings** | `sns:Get*`/`List*` on `*` | `GetTopicAttributes`/`GetDataProtectionPolicy`/`ListSubscriptions` return data for topics unrelated to Spot Fleet → account-wide SNS recon |
| Operator | **All metric data** in the account | `cloudwatch:GetMetricStatistics`/`ListMetrics` on `*` (no scoping exists) | Reading a custom/business metric published by an unrelated workload → operational-data disclosure |
| Operator | **Any CloudWatch alarm** (incl. security/ops alarms) | `cloudwatch:DeleteAlarms`/`DisableAlarmActions` on `*` | A non-`TargetTracking*` alarm belonging to another system is deleted or silenced → alerting-evasion enabler |
| Operator | **Any AWS service's SLR** | `iam:CreateServiceLinkedRole` on `*`, no `iam:AWSServiceName` | An SLR for a service other than `application-autoscaling` is created → unrelated managed policy instantiated |
| Operator | **Scalable targets of unrelated services** (ECS/DynamoDB/Aurora/Lambda/SageMaker…) | `application-autoscaling:*` on `*`, cross-namespace, no resource-id key | Register/scale/deregister a DynamoDB/ECS/Aurora scalable target → wrong-service capacity control |
| Any customer surface | **AWS's own service plane** | — | **HARD STOP** — any AWS-fleet identity/ARN/account = disclosure, preserve evidence |

---

## 4. API / Interface Inventory

| Name | Service | Mutating | Facing | Functionality | Authorized caller (sample grants it on `*`) | Notes |
|---|---|---|---|---|---|---|
| `Subscribe` | sns | ✔ | External | Add a subscription (email/https/sqs/lambda/application) to a topic | holder of sample | **topic-scopable + `sns:Endpoint`/`sns:Protocol` keys exist** → `*`/no-condition is the over-grant. In-account `sqs`/`lambda` need **no** confirmation handshake |
| `CreateTopic` | sns | ✔ | External | Create a topic | holder | topic-ARN-scopable; `*` lets any name |
| `GetTopicAttributes` | sns | ✘ | External | Read topic policy, delivery policy, **KmsMasterKeyId**, subscription counts | holder | topic-scopable but granted on `*` → every topic |
| `GetDataProtectionPolicy` | sns | ✘ | External | Read topic data-protection policy | holder | account-wide under `*` |
| `GetSMSAttributes` | sns | ✘ | External | Account-wide SMS send settings/spend limits | holder | **no resource scoping exists** |
| `ListTopics` / `ListSubscriptions` / `ListSubscriptionsByTopic` | sns | ✘ | External | Enumerate every topic/subscription (endpoint+protocol) | holder | `ListTopics`/`ListSubscriptions` unscopable |
| `GetMetricStatistics` / `ListMetrics` | cloudwatch | ✘ | External | Read any metric's datapoints / enumerate all metrics | holder | **no resource/condition scoping exists** → all-account read |
| `DescribeAlarmsForMetric` | cloudwatch | ✘ | External | Alarms on a metric | holder | unscopable |
| `DescribeAlarms` / `DescribeAlarmHistory` | cloudwatch | ✘ | External | Alarm config/history | holder | `alarm*`+tag scopable; granted on `*` |
| `PutMetricAlarm` / `DeleteAlarms` / `DisableAlarmActions` / `EnableAlarmActions` | cloudwatch | ✔ | External | Create/overwrite/delete/silence any alarm | holder | `alarm` ARN scopable (`alarm:TargetTracking*`); granted on `*` |
| `CreateServiceLinkedRole` | iam | ✔ | External | Create an SLR | holder | **`iam:AWSServiceName` key exists**; sample omits → any-service SLR |
| `application-autoscaling:*` (`RegisterScalableTarget`, `DeregisterScalableTarget`, `PutScalingPolicy`, `DeleteScalingPolicy`, `PutScheduledAction`, `DeleteScheduledAction`, `TagResource`, `UntagResource`, `Describe*`) | application-autoscaling | ✔/✘ | External | Full scaling control, all namespaces | holder | no `resource-id` condition key; cross-service |
| `ec2:ModifySpotFleetRequest` / `DescribeSpotFleetRequests` | ec2 | ✔/✘ | External | The Spot-Fleet terminate/launch + read primitive | holder | **owned by sibling (A1) + `modify-spot-fleet`** — cross-ref only |

**Undocumented/hidden-knob note.** The page prints only the human-operator identity policy; it hides which *console* calls actually fire. Enumerate the real call set the "Auto Scaling" console tab issues and diff against the 17 granted actions — every action in the grant not on the console path is a confirmed over-grant (Lens U). The sibling plan already flags the `AWS::ApplicationAutoScaling::ScalableTarget.RoleARN` hidden knob (its B1).

---

## 5. Recommended Areas of Focus

### Area R1 — SNS block is a cross-topic subscription/exfil + account-wide recon primitive (Lens R / S / J) — PRIORITY
**Background.** The sample grants `sns:Subscribe`, `sns:CreateTopic`, `sns:Get*`, `sns:List*` on `Resource:"*"` with **no** `Condition`. The stated purpose is scaling *notifications*. The Service Authorization Reference (`list_sns.md`) shows `Subscribe` **requires a `topic*` resource** and supports the condition keys **`sns:Endpoint`** ("the URL, email address, or ARN from a Subscribe request") and **`sns:Protocol`** — i.e. AWS ships the exact knobs to restrict Subscribe to one topic and/or one endpoint/protocol, and the sample uses none of them.

**Security Concern.** A principal holding only this policy can, account-wide:
1. **Subscribe an attacker-controlled endpoint to ANY existing topic** — including topics owned by unrelated workloads that carry sensitive data (CloudTrail/Config/GuardDuty findings, deployment or billing notifications, application events). For `email`/`http(s)` endpoints a confirmation token is sent, but the **attacker owns the endpoint receiving it**, so they confirm their own subscription; for **in-account `sqs`/`lambda`/`application` endpoints there is no out-of-band confirmation at all** → silent exfil.
2. **Enumerate and read every topic** via `ListTopics` + `GetTopicAttributes` (returns the topic access **policy**, delivery policy, and **`KmsMasterKeyId`**), `GetDataProtectionPolicy`, and `ListSubscriptions`/`ListSubscriptionsByTopic` (every endpoint+protocol in the account) + `GetSMSAttributes` (account SMS settings). `ListTopics`/`ListSubscriptions`/`GetSMSAttributes` have **no** resource-level scoping at all.

**High-level Test Scenarios.**
- **Claim:** holding only the sample policy, a role can subscribe an attacker-owned SQS queue to a topic it does not own. **Mechanism:** `Subscribe` on `*`, no `sns:Endpoint`/`sns:Protocol` condition; `list_sns.md` Subscribe row. **Oracle:** `iam:SimulateCustomPolicy` of the sample JSON for `sns:Subscribe` against an arbitrary foreign topic ARN → `allowed`; live confirm with a canary topic + canary SQS queue in one authorized account under a role holding exactly the sample. **Severity:** **Medium–High** intra-account (data exfil of another team's notifications via an AWS-published copy-verbatim artifact → Tier-2 report). **Stop:** on any topic/ARN that resolves to an AWS service-plane account.
- **Claim:** the sample grants account-wide SNS reconnaissance (topic policies, KMS key ids, subscription endpoints). **Oracle:** `SimulateCustomPolicy` for `sns:GetTopicAttributes`/`ListSubscriptions`/`GetSMSAttributes` against arbitrary ARNs → `allowed`; the reference shows `ListTopics`/`ListSubscriptions`/`GetSMSAttributes` are unscopable. **Severity:** Low–Medium (info-disclosure enabler; feeds the exfil target selection in the first claim).
- **Chain (kill-chain):** `GetTopicAttributes` reveals a sensitive topic's `KmsMasterKeyId` + access policy → `ListSubscriptionsByTopic` confirms it has real traffic → `Subscribe` an attacker in-account SQS/Lambda endpoint → exfil, no confirmation. Rate at the **end** of the chain (data exfil = Medium–High).

**Doc evidence:** `spot-fleet-auto-scaling-IAM.html` sample JSON (`sns:*` block, `Resource:"*"`); `list_sns.md` rows for `Subscribe` (`topic*` required; `sns:Endpoint`/`sns:Protocol` keys), `GetTopicAttributes`/`GetDataProtectionPolicy`/`ListTopics`/`ListSubscriptions`/`GetSMSAttributes`. **Severity-if-true:** Medium–High. **Note:** the sibling plan lists the SNS block only in one API-row and never develops it — this Area is the net-new value of this plan.

### Area R2 — CloudWatch block = account-wide metric-data read + any-alarm tamper (Lens R / S / O / U) — PRIORITY
**Background.** Beyond the alarm-management actions the sibling plan touches on the *SLR* side (its S1/L1), the **identity** sample here additionally grants **`cloudwatch:GetMetricStatistics`, `ListMetrics`, `DescribeAlarmsForMetric`** on `*`. Per `list_cloudwatch.md`, these three read actions have **no resource-level permission and no condition key** — they are account-wide by design. The write/alarm actions (`PutMetricAlarm`/`DeleteAlarms`/`DisableAlarmActions`/`EnableAlarmActions`) **do** support an `alarm` ARN resource (ARN `…:alarm:${AlarmName}`), so AWS *could* have scoped them to `alarm:TargetTracking*` (exactly what AWS did for the ElastiCache/SageMaker Application-Auto-Scaling SLR policies — see sibling S1's changelog finding); the sample does not.

**Security Concern.** The holder can (1) **read every metric datapoint in the account** — custom/business metrics published by unrelated workloads (`PutMetricData`), billing metrics, etc. → operational/business-data disclosure that the policy's "Spot Fleet scaling" purpose never implies; and (2) **delete, overwrite, disable, or re-enable any alarm in the account**, including security/compliance alarms (root-login, GuardDuty, budget) belonging to other systems — an alerting-evasion enabler. There is **no `cloudwatch:namespace` condition** available on the alarm actions (only on `PutMetricData`), so the only lever AWS left — the `alarm` ARN prefix — is the one the sample threw away with `Resource:"*"`.

**High-level Test Scenarios.**
- **Claim:** the holder can read a metric published by an unrelated workload. **Oracle:** `SimulateCustomPolicy` for `cloudwatch:GetMetricStatistics` (reference confirms blank resource/condition → always account-wide); corroborate the no-scoping fact from `list_cloudwatch.md`. **Severity:** Low–Medium (data disclosure).
- **Claim:** the holder can disable or delete a non-`TargetTracking*` alarm. **Mechanism:** `DeleteAlarms`/`DisableAlarmActions` on `*`; `list_cloudwatch.md` shows these support an `alarm` ARN (so `alarm:TargetTracking*` scoping was available and declined). **Oracle:** `SimulateCustomPolicy` of the sample for `cloudwatch:DeleteAlarms`/`DisableAlarmActions` against an arbitrary foreign `alarm:` ARN → `allowed`; live only against a canary alarm. **Severity:** Medium (any-alarm tamper → alerting evasion; Tier-2 because AWS-published). **Stop:** do not touch non-canary alarms in a live account.
- **Claim (U):** the sample is strictly broader than the fleet's own alarms require, mirroring the un-hardened pattern the sibling S1 found on the SLR side — i.e. AWS hardened the alarm actions for *other* scaling SLRs to `alarm:TargetTracking*` but never narrowed this operator sample. **Oracle:** diff this sample's `cloudwatch:*` resource (`*`) vs the ElastiCache/SageMaker scaling policy alarm resource (`alarm:TargetTracking*`) on `security-iam-awsmanpol.html`. **Severity:** Low–Medium (AWS-authored over-grant, file-worthy).

**Doc evidence:** sample JSON `cloudwatch:*` block; `list_cloudwatch.md` rows (`GetMetricStatistics`/`ListMetrics`/`DescribeAlarmsForMetric` blank resource+condition; alarm actions carry `alarm*` ARN + only tag conditions, no namespace key). **Severity-if-true:** Medium. **Cross-ref:** sibling S1 (SLR-side alarm over-grant + the 2023-11-13 sibling-hardening changelog) — not restated.

### Area R3 — `iam:CreateServiceLinkedRole` on `*` with no `iam:AWSServiceName` → any-service SLR (Lens R) — PRIORITY
**Background.** The sample grants `iam:CreateServiceLinkedRole` on `Resource:"*"` with no `Condition`. `list_iam.md` confirms the action supports the condition key **`iam:AWSServiceName`** ("Filters access by the AWS service to which this role is attached") — the exact key AWS's *own* Application Auto Scaling UG example and the legacy managed policy use to pin the action to the single scaling service principal.

**Security Concern.** Without `iam:AWSServiceName`, the holder can create a service-linked role for **any** AWS service that supports SLRs (not just `*.application-autoscaling.amazonaws.com`) — e.g. `elasticache`, `rds`, `autoscaling`, etc. Each SLR instantiates that service's AWS-managed policy in the account. This is a resource-creation/privilege-amplification primitive that the artifact's purpose ("enable Spot Fleet auto-scaling, which creates `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`") never implies.

**High-level Test Scenarios.**
- **Claim:** the sample permits creating an SLR for a service unrelated to auto-scaling. **Mechanism:** `CreateServiceLinkedRole` on `*`, no `iam:AWSServiceName`; `list_iam.md` row. **Oracle:** `SimulateCustomPolicy` of the sample for `iam:CreateServiceLinkedRole` with an arbitrary `AWSServiceName` (e.g. `elasticache.amazonaws.com`) → `allowed`; contrast with the scoped example on `application-auto-scaling-service-linked-roles.html`. **Severity:** Medium (over-broad AWS-published sample → Tier-2 report).

**Doc evidence:** sample JSON `iam:CreateServiceLinkedRole`; `list_iam.md` (`iam:AWSServiceName` key); page prose "it creates a service-linked role named `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`." **Severity-if-true:** Medium. **Cross-ref:** sibling R1 opened this claim; this Area carries the authoritative `list_iam.md` confirmation + the any-service enumeration.

### Area R4 — `application-autoscaling:*` is cross-service and unpinnable to Spot Fleet (Lens R / S) — PRIORITY
**Background.** The sample grants the **wildcard** `application-autoscaling:*` on `*`, no `Condition`. `list_application-autoscaling.md` confirms the service's write set — `RegisterScalableTarget`, `DeregisterScalableTarget`, `PutScalingPolicy`, `DeleteScalingPolicy`, `PutScheduledAction`, `DeleteScheduledAction`, `TagResource`, `UntagResource` — applies across **every** service namespace (ecs, dynamodb, rds/aurora, lambda, sagemaker, ec2 spot-fleet, elasticache, cassandra, kafka, neptune, comprehend, workspaces, custom-resource, …). There is **no `application-autoscaling:resource-id` condition key** — the only keys are `service-namespace`, `scalable-dimension`, and tags.

**Security Concern.** (1) **Cross-service:** a holder of a policy labeled "Spot Fleet scaling" can register/scale/deregister scalable targets and scaling policies for **unrelated services** — e.g. deregister a production DynamoDB table's auto-scaling, drive an ECS service or Aurora read-replica count, delete another team's scaling policies. (2) **Unpinnable:** even a well-intentioned tightening cannot restrict the grant to *one* Spot Fleet, because there is no resource-id condition key; `service-namespace=ec2` + `scalable-dimension=ec2:spot-fleet-request:TargetCapacity` are shared by every Spot Fleet in the account (this is the structural fact the sibling's A1 relies on for its terminate chain — cross-referenced, not restated).

**High-level Test Scenarios.**
- **Claim:** the sample lets its holder deregister/alter the auto-scaling of a non-Spot-Fleet service. **Oracle:** `SimulateCustomPolicy` for `application-autoscaling:DeregisterScalableTarget` / `DeleteScalingPolicy` against a `scalable-target/` ARN in the `dynamodb`/`ecs` namespace → `allowed`; `list_application-autoscaling.md` confirms single resource type across namespaces + no resource-id key. **Severity:** Medium–High intra-account (cross-service availability/cost impact via an AWS-published artifact). **Stop:** canary scalable targets only.
- **Chain:** `application-autoscaling:*` → register a **foreign-owned** `sfr-xxxx` + scale-in-to-0 → terminate via the two SLR hops. **This is the sibling plan's headline A1 — execute it there, not here.**

**Doc evidence:** sample JSON `application-autoscaling:*`; `list_application-autoscaling.md` (write-action list, single `ScalableTarget` resource type across namespaces, condition keys = `service-namespace`/`scalable-dimension`/tags, no resource-id). **Severity-if-true:** Medium–High. **Cross-ref:** sibling A1/S1.

### Area U1 — "You can create more fine-grained permissions" vs the maximally-coarse sample (Lens U)
**Background.** The page says: "You can also create your own IAM policies that allow more fine-grained permissions for calls to the Application Auto Scaling API." It then presents, as *the* example a customer should copy, a single `Resource:"*"` / no-`Condition` statement spanning five services.
**Security Concern.** The audit above shows **every one of the sample's blocks had a documented narrowing mechanism AWS declined to use** (SNS topic ARN + `sns:Endpoint`/`sns:Protocol`; CloudWatch `alarm:` ARN; `iam:AWSServiceName`; AAS `service-namespace`/`scalable-dimension`; EC2 `spot-fleet-request*` ARN). The "you can be more fine-grained" sentence is advisory prose that points *only* at the Application Auto Scaling API and leaves the SNS/CloudWatch/IAM/EC2 over-grants unflagged — so an operator who copies the sample verbatim (the documented default action) inherits an account-wide blast radius while believing they granted "Spot Fleet scaling."
**High-level Test Scenarios.**
- **Claim:** the sample is the opposite of least-privilege for its stated purpose, and the doc's one mitigation pointer (the AAS auth-and-access-control link) does not cover the SNS/CloudWatch/IAM over-grants. **Oracle:** map each of the 17 actions to the actual console/CLI auto-scaling-configuration call set; every unused action = confirmed over-grant; cross-check that the linked `auth-and-access-control.html` scopes AAS only, not the other four services. **Severity:** Low–Informational (AWS-authored doc/artifact quality defect, file-worthy; raises effective severity of R1–R4 by legitimizing the copy).
**Doc evidence:** page prose + sample JSON; the four reference pages above. **Severity-if-true:** Informational–Low.

### Area X1 — Legacy role name `aws-ec2-spot-fleet-autoscale-role` (Lens X) — cross-ref
**Background.** The page states the "original managed Spot Fleet role for Application Auto Scaling was `aws-ec2-spot-fleet-autoscale-role`, but it is no longer required." The still-published managed policy `AmazonEC2SpotFleetAutoscaleRole` and the legacy-vs-SLR `ModifySpotFleetRequest` parity question are **owned by the sibling plan's Area X1** — execute there. Recorded here only so this plan's lens-sweep is complete.
**Severity-if-true:** Medium (parity/least-priv; AWS-managed artifact). **Cross-ref:** sibling X1.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Subscribe attacker endpoint to a foreign topic (exfil) | `sns:Subscribe` on `*` in sample | `topic` ARN + `sns:Endpoint`/`sns:Protocol` keys exist but unused |
| Account-wide SNS recon (policies, KMS ids, subscriptions) | `sns:Get*`/`List*` on `*` | partial resource scoping unused; `ListTopics`/`ListSubscriptions` unscopable |
| Read any workload's metric data | `cloudwatch:GetMetricStatistics`/`ListMetrics` on `*` | no scoping exists (account-wide by design) |
| Delete/disable a security/ops alarm | `cloudwatch:DeleteAlarms`/`DisableAlarmActions` on `*` | `alarm:` ARN (`TargetTracking*`) scoping available but unused |
| Create an SLR for an unrelated service | `iam:CreateServiceLinkedRole` on `*` | `iam:AWSServiceName` condition key unused |
| Control a non-Spot-Fleet service's scaling | `application-autoscaling:*` on `*` | `service-namespace`/`scalable-dimension` keys unused; no resource-id key exists |
| Terminate a foreign Spot Fleet via scaling | `application-autoscaling:*` → SLR hops | **sibling A1** — mitigation = none (IAM-unscopable) |
| Copy-verbatim operator inherits account-wide blast radius | the whole sample policy | "you can create more fine-grained permissions" (advisory, AAS-only) |

---

## 7. Out-of-Scope Risk Categories
- **Everything the sibling `spot-fleet-automatic-scaling-attack-research-plan.md` owns** — the SLR policy audit (S1), the IAM-unscopable foreign-fleet terminate chain (A1), min/max guarantee-vs-enforcement (U1), managed-alarm/custom-metric tampering (L1/L2), caller-`RoleARN` confused deputy (B1), legacy-role parity (X1). Cross-referenced, never re-tested here.
- **`ec2:ModifySpotFleetRequest` internals** (console-hidden `LaunchTemplateConfig.N`, `ExcessCapacityTerminationPolicy`, `ec2:Attribute` case-sensitivity) — owned by `modify-spot-fleet-attack-research-plan.md`.
- **A customer who writes their own over-broad policy** — footgun, out of scope. In scope here **only** because this policy is AWS-published and the docs say to copy it verbatim.
- **SNS/CloudWatch/Application Auto Scaling multi-tenant control-plane isolation**, SNS cross-account subscription *to a different account's* topic (needs that topic's resource policy — not granted by an identity policy), EventBridge Scheduler internals — AWS-shared infra / shared-responsibility line.
- **Cross-account / cross-tenant anything** — this is an identity policy bounded to the holder's own account; no cross-tenant surface. The realistic adversary is **intra-account cross-team** (a low-trust workload/role that was handed this "scaling" policy).
- **Single-tenant self-DoS**; IMDS on managed scaling hosts; product/parity gaps of the legacy Spot Fleet API.

---

## 8. Null hypotheses / doc gaps
- **Lens A (cross-account IDOR):** null — identity policy, single account; SNS cross-account subscribe needs the *target* topic's resource policy (not grantable here). Pages checked: the IAM page + `list_sns.md`/`list_cloudwatch.md`/`list_application-autoscaling.md`.
- **Lens G (SSRF):** null — no field on this page is dereferenced server-side. (`sns:Subscribe`'s `Endpoint` is a *delivery* target, not a server-side fetch the service validates by fetching; the HTTP(S) confirmation POST goes to the attacker's own endpoint and is an exfil channel, not an SSRF oracle.) Page checked: the IAM page.
- **Lens Q/F/K (upload / translation / prompt-injection):** null — no upload, parser, or LLM on this artifact-audit surface.
- **Lens B/C (PassRole / vending):** the caller-`RoleARN` confused-deputy on `RegisterScalableTarget` is **real but owned by the sibling (B1)** — not duplicated. `iam:CreateServiceLinkedRole` is covered as R3 (artifact over-grant), not as PassRole.
- **Lens H (KMS):** null for this policy — it mints no key. (It *can read* other topics' `KmsMasterKeyId` via `GetTopicAttributes` — captured as recon in R1, not a KMS-confusion lead.)
- **Doc-gap — SNS confirmation semantics by protocol:** the exfil severity in R1 depends on which Subscribe protocols require out-of-band confirmation. In-account `sqs`/`lambda`/`application` are documented as not requiring the subscriber's email/HTTP confirmation handshake; confirm the exact current behavior against the SNS Developer Guide before building a live PoC.
- **Doc-gap — console call set:** the exact AWS calls the EC2 "Auto Scaling" console tab issues (needed to prove the U1 over-grant action-by-action) are not on this page; capture them from a traffic trace before claiming a specific action is unused.
- **Reference-slug confirmation:** `list_sns`/`list_cloudwatch`/`list_iam` (no prefix) and the **hyphenated** `list_application-autoscaling` are the live slugs; the `amazon`/`aws`-prefixed variants 404 (consistent with the dead `list_amazonec2` pitfall — see [[reference-aws-iam-service-auth-ref-url]]). All four confirmed in the offline mirror.

---

> **Downstream hunter note.** This plan is a **static, no-touch IAM-artifact audit** — every lead is confirmable with `iam:SimulateCustomPolicy` on the pasted sample JSON **before any live call**. Run in order: **R1** (SNS: paste the sample, simulate `sns:Subscribe` against a foreign topic ARN → `allowed`; then live-confirm cross-topic subscribe with a canary topic + canary in-account SQS endpoint = the exfil PoC), **R2** (simulate `cloudwatch:DeleteAlarms`/`DisableAlarmActions` against a foreign `alarm:` ARN; confirm `GetMetricStatistics` is unscopable), **R3** (simulate `iam:CreateServiceLinkedRole` with a non-AAS `AWSServiceName`), **R4** (simulate `application-autoscaling:DeregisterScalableTarget` against a `dynamodb`/`ecs` scalable-target ARN). **U1** is a doc/console-diff exercise. For the Spot-Fleet terminate chain, the SLR audit, and the caller-`RoleARN` deputy, go to **`spot-fleet-automatic-scaling-attack-research-plan.md`** (A1/S1/B1) and **`modify-spot-fleet-attack-research-plan.md`**. Use a scoped role holding **exactly** the sample policy, canary resources only, tear everything down. **Hard stop** on any AWS service-plane identity/ARN/account.
