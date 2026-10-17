# Amazon CloudWatch Application Insights — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-appinsights.html
(The EC2 UserGuide page is a thin pointer; the real service is **Amazon CloudWatch Application Insights**, documented under `AmazonCloudWatch/latest/monitoring/appinsights-*`.)

**Source of leads:** `AWSEC2/latest/UserGuide/monitoring-appinsights.md`; `AmazonCloudWatch/latest/monitoring/appinsights-what-is.md`, `-how-works.md`, `-iam.md`, `-cross-account.md`, `-ssm-documents.md`, `-ssm-packages.md`, `-cloudformation.md`, `-prereqs.md`, `-account-based-onboarding-permissions.md`, `security-iam-awsmanpol-appinsights.md`, `CHAP_using-service-linked-roles-appinsights.md`, `component-configuration-examples*.md`, `appinsights-cloudwatch-events.md`, `appinsights-problem-notifications.md`; AWS CLI reference `cli/latest/reference/application-insights/*`. Online `.md` pages verified against the offline mirror (byte-identical where checked).

**Status:** documentation-derived hypotheses only. **Nothing has been tested against a live account.** Confirmation requires an authorized test account.

---

## 0. How to use this document

- Each lead is: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity-if-true → Stop condition.** Work in priority order (§5 is ordered). Look left and right for adjacent bugs.
- **HARD STOP / disclosure trip-wire:** the moment evidence shows an identity, credential, ARN, or account belonging to **AWS's own service plane** (not the customer's own account/SLR acting intra-account), stop, preserve evidence, and flag for AWS-Security disclosure. Application Insights runs almost entirely *inside the customer's own account* via the SLR, so most leads here are **intra-account privilege-boundary** breaks, not service-plane breaks — keep that distinction sharp when rating.
- **The one AWS-owned, reportable artifact finding** regardless of live testing: AWS's **sample IAM policy** (`appinsights-iam.md`) and **AWS-managed policies** are copy-verbatim/uneditable artifacts; a weak default in them is AWS's defect (Lens R, Tier-2). See L7.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)

1. **Cross-resource-group / cross-team command execution:** Starting from a principal with only Application Insights rights (and *no* `ssm:SendCommand`/`cloudformation:*`/`iam:PassRole`), get the `AWSServiceRoleForApplicationInsights` SLR to run an SSM document, install/reconfigure the CloudWatch agent, or create a CloudFormation stack **against an EC2 instance or resource the principal could not touch directly** → **breach**.
2. **File exfiltration via agent config:** Cause the CloudWatch agent on a monitored instance to collect an **arbitrary filesystem path** (`logPath`) into a **log group the attacker can read** → **breach** (confidentiality of instance filesystem).
3. **Cross-tenant data read / mutation:** Read or mutate another account's or another resource group's Application Insights state (applications, problems, component config, SNS ARNs) by naming an identifier (`problemId`, `AccountId`, `componentName`-as-ARN) rather than being bound by the credential → **breach**.
4. **Notification hijack:** Redirect a victim application's problem notifications (affected-resource ARNs, account IDs) to an attacker-controlled SNS topic → **breach** (operational-data disclosure).
5. **AWS-authored artifact defect:** Prove an AWS-managed/sample IAM policy grants more than its stated purpose (self-escalation / over-broad SLR creation) → **reportable (Tier-2)**.
6. **Monitoring-pipeline integrity/availability:** Suppress another team's detected problems, delete unrelated log subscription filters, or DoS the log-processing pipeline → **breach** (integrity/availability within account).

---

## 2. Components, Assets, and Design

**What it is.** A managed observability feature that **scans a customer resource group, auto-detects workloads (SQL Server, .NET/IIS, Java/JMX, SAP HANA/ASE/NetWeaver, databases), and automatically provisions** CloudWatch alarms/anomaly detectors (via CloudFormation), installs/configures the CloudWatch agent and Prometheus exporters on EC2 instances (via SSM), writes agent config to SSM Parameter Store, and raises "problems" with automated dashboards + SNS/EventBridge/OpsCenter notifications.

**Customer-facing interface.** Public SigV4 API at `applicationinsights.<region>.amazonaws.com` (+ console + CloudFormation `AWS::ApplicationInsights::Application`). **No anonymous/pre-auth surface** — every call is IAM-authenticated. There is **no public API Reference page** (all `/appinsights/latest/APIReference/*` 404); the API shape is reconstructed from the AWS CLI reference (doc-gap, see §8).

**Identity / privilege model.**
- Callers hold `applicationinsights:<Action>` — AWS's example policy grants this with **`Resource:"*"` (no resource-level scoping documented)**.
- The engine acts via the **service-linked role `AWSServiceRoleForApplicationInsights`**, policy `CloudwatchApplicationInsightsServiceLinkedRolePolicy` (29 statements). Only `application-insights.amazonaws.com` can assume it (trust-policy JSON not printed — doc-gap). **No `iam:PassRole` anywhere.**
- Monitored EC2 instances need an instance role with `AmazonSSMManagedInstanceCore` + `CloudWatchAgentServerPolicy` (statements not printed — doc-gap, adjacent Lens R target).

**"Resource" shapes / identifiers.**
- `resourceGroupName` (bare name, AWS Resource Groups, caller's account) — primary scope for most APIs.
- `componentName` — **accepts either a plain name OR a full ARN** per its regex (dual-mode input, see L5).
- `problemId` — opaque `p-{8}-{4}-{4}-{4}-{12}` hex (UUID-like, low enumerability) — but **sole scoping key** for `DescribeProblem`/`UpdateProblem`/`DescribeProblemObservations`.
- `AccountId` — optional 12-digit field on `DescribeApplication`/`ListApplications`/`ListProblems`/`DescribeProblem` for OAM cross-account reads.
- Predictable managed-resource names: CFN stacks `ApplicationInsights-*`, Resource Groups `ApplicationInsights-*`, EventBridge rules + SSM parameters + log destinations `AmazonCloudWatch-ApplicationInsights-*`.

**ASCII pipeline:**
```
                 (SigV4 IAM caller: applicationinsights:*  Resource:"*")
                                   │  CreateApplication / CreateComponent(resourceList=[ARNs])
                                   │  UpdateComponentConfiguration(JSON: logPath, logGroupName, tier)
                                   ▼
                 ┌──────────────────────────────────────────┐
                 │  Application Insights control plane (AWS) │
                 └──────────────────────────────────────────┘
                                   │ assumes
                                   ▼
          ┌───────────────────────────────────────────────────────────┐
          │  SLR  AWSServiceRoleForApplicationInsights (customer acct) │
          └───────────────────────────────────────────────────────────┘
            │ cfn CreateStack          │ ssm:PutParameter            │ ssm:SendCommand / CreateAssociation
            │ stack/ApplicationInsights-* │ parameter/AmazonCloudWatch-   │ Resource: ec2:*:*:instance/*   ← UNCONDITIONED
            ▼                          │   ApplicationInsights-*     │   (every instance in the account)
   CloudWatch alarms /                ▼ (CW-agent JSON config)      ▼
   anomaly detectors        ┌───────────────────────┐    SSM docs: AWSEC2-DetectWorkload,
                            │  SSM Parameter Store   │───▶ AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure,
                            └───────────────────────┘     AWS-ConfigureAWSPackage (installs Prometheus exporters),
                                                          AmazonCloudWatch-ManageAgent
                                                                     │ runs on
                                                                     ▼
                                                    ┌──────────────────────────────┐
                                                    │  Customer EC2 instances       │
                                                    │  CloudWatch agent + Prometheus │
                                                    │  exporters (JMX/SQL/HANA/SAP)  │
                                                    └──────────────────────────────┘
   Problem detected ──▶ EventBridge event (problemId, resourceGroupName, problemUrl)
                   └──▶ SNS publish (snsNotificationArn / opsItemSNSTopicArn — caller-supplied, ownership unchecked)
                   └──▶ SSM OpsCenter OpsItem
   Cross-account: CloudWatch Observability Access Manager (OAM) sink/link — READ-only data sharing.
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv AppInsights caller | Any EC2 instance in the account (not in caller's resource group) | `CreateComponent(resourceList)` + `UpdateComponentConfiguration(monitor=true)` → SLR `ssm:SendCommand`/`CreateAssociation` on `instance/*` (unconditioned) | A CloudTrail `ssm:SendCommand`/`CreateAssociation` by `AWSServiceRoleForApplicationInsights` targeting an instance outside the caller's resource group = **breach** |
| Low-priv AppInsights caller | Arbitrary file on a monitored instance | `UpdateComponentConfiguration` `logPath` glob → CW-agent ships file to attacker-chosen `logGroupName` | File contents appearing in a log group the caller reads = **breach** |
| Account principal with `ssm:PutParameter` on `AmazonCloudWatch-ApplicationInsights-*` | CW-agent config on all monitored instances | SLR pulls that SSM param every ≤30 min and pushes it to instances | Agent applies attacker-written config (new logPath / plugin) = **breach** |
| Caller in resource group A | Problem owned by resource group B (or acct B) | `UpdateProblem(problemId)` / `DescribeProblem(problemId)` — ID-only, no RG/account scope in request | Mutating/reading B's problem by ID alone = **breach** (integrity / confidentiality) |
| Monitoring account (OAM) | Source account AppInsights state | `AccountId` param on `Describe/List` reads | **Reading data for an `AccountId` with no OAM link = breach**; a *write* crossing accounts = **critical breach** |
| Caller with `UpdateApplication` | Victim app's notification stream | repoint `snsNotificationArn`/`opsItemSNSTopicArn` to attacker topic | Problem notifications (affected-resource ARNs, acct id) delivered to attacker topic = **breach** |
| **Any customer surface** | **AWS service plane** | — | Any AWS-fleet identity/credential/ARN surfaced = **HARD STOP + disclosure** |
| AWS-authored IAM artifact | Principal who copies it verbatim | Sample policy / managed policy grants beyond purpose | A scoped principal holding only the artifact performs an action its description implies it cannot = **reportable Tier-2** |

**Canonical boundaries explicitly checked:**
- *Customer account ↔ service account:* AppInsights SLR runs **inside the customer account** → most leads are intra-account, not cross-tenant. Service-plane reach would be a hard stop.
- *Caller request context ↔ privileged SLR:* the **key boundary** — can caller-controlled config (`resourceList`, `componentConfiguration.logPath`) steer the SLR's `ssm:SendCommand`/`CreateStack` beyond the caller's own reach? (L1, L2)
- *Cross-account (OAM):* read-only by design; verify write paths truly cannot cross (null H4 of API subagent).

---

## 4. API / Interface Inventory

Endpoint `applicationinsights.<region>.amazonaws.com`, SigV4, no anonymous surface. "Authorized callers" below = any principal holding the action; AWS's example policy grants `applicationinsights:*` on `Resource:"*"` (**no resource-level scoping documented** — the pivotal unknown).

| Name | Mutating | Internet-callable | Caller-supplied scoping input | Flag |
|---|---|---|---|---|
| CreateApplication | Y | Y | `resourceGroupName` or `groupingType=ACCOUNT_BASED`; `opsItemSNSTopicArn`, `snsNotificationArn`; `attachMissingPermission` | Creates SLR; `attachMissingPermission` **auto-attaches managed policies to other IAM roles** (privilege-granting side effect) |
| UpdateApplication | Y | Y | `resourceGroupName`, SNS ARNs, `cweMonitorEnabled`, `opsCenterEnabled` | Repoint SNS ARNs → L4 |
| DeleteApplication | Y | Y | `resourceGroupName` | Monitoring state only |
| DescribeApplication | N | Y | `resourceGroupName` **+ optional `AccountId`** | Cross-account read → L6 |
| ListApplications | N | Y | optional `AccountId` | Returns AccountId + SNS ARNs per app |
| CreateComponent | Y | Y | `resourceGroupName`, `componentName`, **`resourceList` (ARNs)** | ARN membership not validated → **L1 (flagship)** |
| UpdateComponent | Y | Y | `resourceGroupName`, `componentName`, `newComponentName`, `resourceList` | Name-keyed |
| DeleteComponent | Y | Y | `resourceGroupName`, `componentName` | |
| DescribeComponent | N | Y | `resourceGroupName`, `componentName` (**name OR ARN**) | Dual-mode → L5 |
| DescribeComponentConfiguration | N | Y | `resourceGroupName`, `componentName` | Returns logPaths/alarm config |
| DescribeComponentConfigurationRecommendation | N | Y | `resourceGroupName`, `componentName`, `tier` | |
| UpdateComponentConfiguration | Y | Y | `resourceGroupName`, `componentName`, `tier`, `monitor`, **`componentConfiguration` (JSON ≤10k: logPath, logGroupName, metrics)** | **Drives SLR SSM/agent actions → L1/L2** |
| ListComponents | N | Y | `resourceGroupName` | |
| ListProblems | N | Y | optional `AccountId`, `resourceGroupName`, `componentName`, `visibility`, time | |
| DescribeProblem | N | Y | **`problemId` + optional `AccountId`** | ID-only scope → L3 |
| UpdateProblem | Y | Y | **`problemId`** + `updateStatus`/`visibility` | **No RG/account scope in request → L3 (flagship IDOR)** |
| DescribeProblemObservations | N | Y | `problemId` | ID-only |
| DescribeObservation | N | Y | `observationId` | ID-only |
| Create/Update/Delete/Describe/List LogPattern(s)/LogPatternSets | Mixed | Y | `resourceGroupName`, `patternSetName`, `patternName`, regex `pattern` | ReDoS → L8 |
| Add/Remove/Update/Describe/List Workload(s) | Mixed | Y | `resourceGroupName`, `componentName`, `workloadId` | Sub-component granularity |
| ListConfigurationHistory | N | Y | `resourceGroupName`, time | Recon surface |
| TagResource / UntagResource / ListTagsForResource | Mixed | Y | `resourceArn` (**generic any-service ARN regex**) | Type not enforced by regex |

**Undocumented/console-hidden knobs:** `componentName` accepting a full ARN (never shown in console) → L5. `attachMissingPermission` on CreateApplication (mutating IAM side effect) → L7-adjacent. `AccountId` on reads (OAM) → L6.

---

## 5. Recommended Areas of Focus (priority-ordered; one block per firing lens)

### L1 — [FLAGSHIP] Caller-controlled component `resourceList` → SLR SSM command execution on arbitrary same-account EC2 (Lens A + E + X + D)
**Background.** `CreateComponent`/`UpdateComponent` take a `resourceList` of ARNs; `UpdateComponentConfiguration(monitor=true)` then causes the SLR to install/configure the CloudWatch agent on those instances via `ssm:SendCommand`/`ssm:CreateAssociation`. The SLR's SSM grants are scoped to `arn:aws:ec2:*:*:instance/*` **with no resource-group/tag Condition** — i.e. **every instance in the account**.
**Security Concern.** The docs do not state that `resourceList` ARNs are validated to belong to the caller's `resourceGroupName` or that the caller has any right over them. A principal with only `applicationinsights:CreateComponent`+`UpdateComponentConfiguration` (via the common `Resource:"*"` grant) but **no direct `ssm:SendCommand` on instance B** may be able to add B's ARN to a component and get the privileged SLR to run AWS SSM documents against B.
**High-level Test Scenarios (falsifiable):**
- *Claim:* Adding a non-member instance ARN to a custom component and flipping `monitor=true` causes `AWSServiceRoleForApplicationInsights` to issue `ssm:SendCommand`/`CreateAssociation` against it. → *Oracle:* RG contains only instance A; `create-component` listing instance B (same account, different team, no AppInsights tag); `update-component-configuration --monitor`; CloudTrail shows SLR SSM action on B. → **Severity: High** (lateral movement / cross-team code-path on an AWS-signed document set).
- *Adjacent (X):* does the SLR's fixed document allowlist (`AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure`, `AWS-ConfigureAWSPackage`, `AmazonCloudWatch-ManageAgent`) constrain impact to "install agent / install exporter package," or can `AWS-ConfigureAWSPackage` be steered to an attacker-named package (land-grab, see L1b)?
**Doc evidence:** SLR `SSMSendCommand`/`SSMAssociation` Sids (`CHAP_using-service-linked-roles-appinsights.md`); CLI `create-component --resource-list`, `update-component-configuration --monitor` (CLI ref). **Precondition:** authorized 2-team/2-RG sandbox. **Severity-if-true:** High. **Stop condition:** one confirmed SLR SSM action on a non-member instance; if the targeted document or identity resolves to anything AWS-plane, HARD STOP.

### L1b — `logPath` in `componentConfiguration` → arbitrary-file exfiltration via CloudWatch agent (Lens Q + F + D)
**Background.** The component config JSON carries free-text `logPath` globs (e.g. `C:\LogFolder\*`) and `logGroupName`; the SLR writes this to `parameter/AmazonCloudWatch-ApplicationInsights-*` and the agent (running as SYSTEM/root) collects those paths.
**Security Concern.** If `logPath` is not constrained, a caller can point the agent at a sensitive file (`C:\Windows\...`, `/etc/...`, app secrets) and ship it to a `logGroupName` they can read — turning monitoring config into a server-side file-read primitive on every instance the component covers (compounds with L1's cross-team instance targeting).
**Test Scenarios:** *Claim:* `UpdateComponentConfiguration` with `logPath=<sensitive glob>` + `logGroupName=<attacker-readable>` causes the agent to ship file contents. → *Oracle:* set it, wait for the ≤30-min association run, read the log group. **Severity:** High (confidentiality of instance filesystem; cross-team if chained with L1).
**Doc evidence:** `component-configuration-examples-ec2.md` (`logPath`,`logGroupName`); `appinsights-ssm-documents.md` (association runs every 30 min / on change). **Stop:** one file-content leak into a readable log group.

### L2 — Agent-config injection via the predictable `AmazonCloudWatch-ApplicationInsights-*` SSM parameter prefix (Lens EE + D + Q)
**Background.** The SLR reads/writes the CloudWatch agent config at `arn:aws:ssm:*:*:parameter/AmazonCloudWatch-ApplicationInsights-*` and re-pushes it to instances every ≤30 min and immediately on change.
**Security Concern.** Any principal who gets `ssm:PutParameter` on that prefix (easy to grant by accident via a loose `ssm:PutParameter` on `*`) — *without* any AppInsights permission — could overwrite the agent config the SLR distributes fleet-wide.
**Test Scenarios:** *Claim:* overwriting an existing `AmazonCloudWatch-ApplicationInsights-*` parameter with a crafted agent config (new log collection / plugin) is applied to monitored instances on the next association run. → *Oracle:* low-priv principal with only `ssm:PutParameter` on the prefix writes a crafted value; observe agent behavior change. *Refute* if AppInsights re-derives/overwrites the parameter from its own stored state before each push (external writes transient). **Severity:** High if it holds. **Doc evidence:** SLR `SSMParameter` Sid; `appinsights-ssm-documents.md` schedule.
**Adjacent (Prometheus exporters, Lens F):** `appinsights-ssm-packages.md` shows exporter configs (`sql_exporter.yml`, HANA exporter) carrying **raw SQL** delivered as Base64 in **caller-named** SSM parameters (`SSM_EXPORTER_CONFIGURATION`, `{{ssm:<name>}}` indirection) **not** restricted to the AppInsights prefix. *Claim:* a caller can inject arbitrary SQL executed server-side by the exporter using the exporter's DB credentials (Secrets Manager). → *Oracle:* craft an exporter config with an injected query; confirm execution. **Severity:** Medium-High (server-side SQL on the monitored DB).

### L3 — [FLAGSHIP] `UpdateProblem` / `DescribeProblem` IDOR — problem access keyed only by `problemId` (Lens A)
**Background.** `UpdateProblem`, `DescribeProblem`, `DescribeProblemObservations` are scoped **only** by `problemId`; `UpdateProblem`'s documented request shape has **no `resourceGroupName`/`accountId`/`applicationArn`**. `problemId`s leak in SNS emails and EventBridge events (`problemUrl`, detail fields).
**Security Concern.** A caller with `applicationinsights:UpdateProblem` on `Resource:"*"` who obtains another resource group's (or account's) `problemId` from a notification could resolve/hide (`visibility=IGNORED`) or read that problem — suppressing another team's incident or reading affected-resource ARNs.
**Test Scenarios:** *Claim:* `update-problem --problem-id <B's id>` succeeds from a principal scoped to RG A. → *Oracle:* two RGs/accounts; capture B's problemId from its notification; call from A; success (state changes, no `AccessDenied`) confirms. **Severity:** Medium-High (integrity of incident response; confidentiality via `DescribeProblem`). **Doc evidence:** CLI `update-problem`/`describe-problem`; `appinsights-cloudwatch-events.md`/`appinsights-problem-notifications.md` (problemId in payloads). **Stop:** one cross-RG mutation/read.

### L4 — Notification redirect / confused deputy via caller-supplied SNS ARN (Lens J + M)
**Background.** `CreateApplication`/`UpdateApplication` accept `snsNotificationArn` and `opsItemSNSTopicArn` as free-form ARNs; no proof-of-possession of the topic is documented.
**Security Concern.** A caller with `UpdateApplication` can repoint a victim app's notifications to an attacker topic (if its topic policy allows the AppInsights principal to publish), exfiltrating affected-resource ARNs, account IDs, and problem detail. (The real control under test is SNS cross-account publish authorization.)
**Test Scenarios:** *Claim:* repointing `snsNotificationArn` to an attacker-owned topic delivers problem notifications there. → *Oracle:* set it to a 2nd-account topic allowing publish from the AppInsights service principal; trigger a synthetic problem; confirm delivery. **Severity:** Medium (operational-data disclosure). **Doc evidence:** CLI `create-application`/`update-application --sns-notification-arn`.

### L5 — `componentName` name-vs-ARN parser divergence (Lens BB + A)
**Background.** `componentName` on `DescribeComponent`/`UpdateComponentConfiguration`/`ListProblems` accepts **either a plain name or a full ARN** (`(?:^[\d\w\-_\.+]*$)|(?:^arn:aws...)`); the console only ever shows plain names.
**Security Concern.** Two parallel input formats for one field is a classic auth-scoping divergence: the friendly-name path likely re-derives scope from the resource group, while the ARN path may trust the ARN's embedded account/region segment.
**Test Scenarios:** *Claim:* passing a cross-RG/cross-account ARN as `--component-name` behaves differently (succeeds where the name form 404s). → *Oracle:* compare ARN-form vs name-form responses/errors. **Severity:** Low standalone; **enabler for L1** (ARN-form targeting bypassing RG containment). **Doc evidence:** CLI regex for `component-name`.

### L6 — Cross-account `AccountId` read scoping (OAM) (Lens A + J)
**Background.** `DescribeApplication`/`ListApplications`/`ListProblems`/`DescribeProblem` accept a caller-supplied `AccountId`, meant to work only when an OAM sink/link exists.
**Security Concern.** If the OAM-link authorization is missing/misordered, supplying an arbitrary unlinked `AccountId` may yield a partial response or an existence oracle rather than a clean `AccessDenied`; worse if `SNSNotificationArn`/ARNs leak.
**Test Scenarios:** *Claim:* `describe-application --resource-group-name X --account-id <unlinked>` leaks existence of X in that account. → *Oracle:* compare error for existing vs non-existing X in an unlinked account. **Severity:** Low-Medium (enumeration); Medium-High if real ARNs leak. **Doc evidence:** CLI `AccountId` param; `appinsights-cross-account.md` (OAM read-only model). **Note:** also test whether any *write* (`UpdateProblem`) honors `AccountId` — if a mutating call crosses accounts, that is **Critical**; current docs show no `AccountId` on `update-problem` (verify live).

### L7 — AWS-authored IAM-artifact audit (Lens R + S)
**Background.** AWS ships: a **sample onboarding policy** (`appinsights-iam.md`), **`CloudWatchApplicationInsightsFullAccess`**, **`...ReadOnlyAccess`**, the **SLR policy**, and an **account-based-onboarding permission list**.
**Security Concerns / findings (static, confirmable now):**
- **Sample policy grants `iam:CreateServiceLinkedRole` on `Resource:"*"` with no `Condition`** — a holder can create an SLR for **any** service, not just `application-insights.amazonaws.com`. AWS's own managed `FullAccess` policy scopes the *identical* permission to the one SLR ARN + `StringEquals iam:AWSServiceName`. AWS's sample teaches a strictly weaker pattern than AWS's own managed policy. → *Oracle:* `iam:SimulatePrincipalPolicy` for a principal holding only the sample policy calling `CreateServiceLinkedRole` with an unrelated `AWSServiceName` → `allowed`. **Severity: Medium-High. Reportable Tier-2** (AWS-authored, copy-verbatim artifact — the Lens R carve-out, *not* a customer footgun).
- **SLR `logs:DeleteSubscriptionFilter` on `arn:aws:logs:*:*:log-group:*` with no name constraint**, while its sibling `logs:PutSubscriptionFilter` is constrained to the `AmazonCloudWatch-ApplicationInsights-LogIngestionDestination*` destination. Asymmetric create-vs-delete scoping → the SLR can delete subscription filters on **any** log group (sabotage of unrelated log pipelines). → *Oracle:* under the SLR, `DeleteSubscriptionFilter` on a non-AppInsights log group. **Severity:** Medium (Lens S).
- **SLR `ssm:SendCommand`/`CreateAssociation` on `instance/*` and `ecs:UpdateClusterSettings` on `cluster/*` — unconditioned** (feeds L1). **CloudFormationStacks** read Sid on `Resource:"*"` (account-wide stack enumeration). `apigateway:GET` on `*` (broad read; note `GET /apikeys?includeValues` exposure risk).
- **`attachMissingPermission` on CreateApplication** auto-attaches managed policies to *other* IAM roles — a mutating privilege-granting side effect worth auditing (which roles, which policies, who can trigger it).
**Move:** pull `CloudWatchApplicationInsightsFullAccess` and `CloudwatchApplicationInsightsServiceLinkedRolePolicy` via `iam:GetPolicyVersion` to confirm the live JSON matches the docs; audit statement-by-statement; use `iam:SimulatePrincipalPolicy` as the no-touch first oracle.

### L8 — CreateLogPattern regex ReDoS (Lens L + M)
**Background.** `CreateLogPattern`/`UpdateLogPattern` take a caller-supplied regex applied across the component's log groups; `appinsights-troubleshooting.md` already names "High CPU usage from CloudWatch agent log processing" as a known failure mode.
**Security Concern.** No doc confirms regex complexity limits/timeouts → catastrophic-backtracking pattern on high-volume logs could DoS the processing pipeline. → *Oracle:* `(a+)+$`-style pattern on a high-volume component; observe latency/CPU. **Severity:** Low-Medium (single-account availability). **Doc evidence:** CLI `create-log-pattern --pattern`; troubleshooting doc.

### L9 — Predictable-name land-grab on managed CFN/Resource-Group resources (Lens EE)
**Background.** SLR grants `CreateStack`/`UpdateStack`/`DeleteStack` on `stack/ApplicationInsights-*` and `CreateGroup`/`DeleteGroup` on `group/ApplicationInsights-*` with no ownership check beyond the name prefix.
**Security Concern.** If the name-derivation algorithm is predictable (undocumented — doc-gap), an attacker who pre-creates a stack/group with the exact name the service will use could cause onboarding to adopt/update/delete the pre-staged resource or DoS onboarding.
**Test Scenarios:** pre-create `ApplicationInsights-<derived>` then onboard; observe fail vs silent adopt/update. **Severity:** Low-Medium (intra-account, per-account SLR → not cross-tenant). **Doc evidence:** SLR CFN/Resource-Groups Sids.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-team SSM command exec via component resourceList | CreateComponent / SLR SSM | SLR `instance/*` is unconditioned → the *only* backstop is API-side RG/ownership validation (undocumented → test it) |
| Instance file exfiltration via logPath | UpdateComponentConfiguration / CW agent | Any `logPath` validation / allowlist (none documented) |
| Agent-config poisoning via SSM parameter | SSM Parameter Store prefix | Whether AppInsights re-derives config vs trusting the stored parameter |
| Problem IDOR | UpdateProblem/DescribeProblem | Server-side RG/account authz on problemId (not in request shape → test) |
| Cross-account read over-reach | DescribeApplication AccountId | OAM link validation ordering/completeness |
| Notification hijack | UpdateApplication SNS ARN | SNS topic-policy cross-account publish control (not AppInsights-side) |
| SLR over-grant / sample-policy over-grant | IAM artifacts | ARN-prefix scoping; `iam:AWSServiceName` condition (absent in sample) |
| Log-pipeline sabotage | SLR DeleteSubscriptionFilter | No destination/name constraint (asymmetric vs PutSubscriptionFilter) |
| ReDoS | CreateLogPattern | Regex complexity limits/timeouts (undocumented) |

---

## 7. Out-of-Scope / Risk Categories to NOT pursue

- **AWS service-plane / shared infrastructure.** The SLR runs inside the customer account; this is not a multi-tenant shared fleet. Any evidence of an AWS-owned fleet identity/credential/ARN = **HARD STOP + disclose**, not continue.
- **IMDS on the managed CloudWatch-agent hosts** — these are the *customer's own* EC2 instances; agent behavior there is the customer's responsibility.
- **Customer-authored IAM policies / least-privilege footguns** — out of scope. (The *AWS-authored* sample/managed policies in L7 are **in** scope — Lens R carve-out.)
- **Third-party exporter binaries** (Prometheus JMX/SQL/HANA exporters) — bugs in the upstream exporter code are out of scope; *AppInsights's delivery of attacker-influenced config to them* (L2 adjacent) is in scope.
- **OAM internals** (sink/link policy semantics) — belongs to a CloudWatch cross-account observability plan, not this one, except where AppInsights' `AccountId` handling (L6) is the surface.
- **DoS of a customer's own single account** beyond noting it (L8) — single-tenant self-DoS is low priority.

---

## 8. Null hypotheses / doc gaps (surfaces to confirm before concluding)

**Null hypotheses (checked, no lead with current evidence):**
- **Direct privesc from `CloudWatchApplicationInsightsFullAccess`:** *refuted* — the attachable policy contains **no** `ssm:SendCommand`/`ssm:CreateAssociation`/`iam:PassRole`; those live only in the SLR (service-assumable only). Escalation must go *through* the API steering the SLR (L1), not via the user policy directly. Pages read: `security-iam-awsmanpol-appinsights.md`, `appinsights-iam.md`.
- **Cross-account *write* / confused deputy on AppInsights control plane:** *refuted on current docs* — cross-account is OAM read-only sharing; no `sts:AssumeRole` into source accounts, no `AccountId` on documented write APIs. Flip to **Critical** only if a live `update-*` call is found to honor `AccountId`. Pages read: `appinsights-cross-account.md`, `CloudWatch-Unified-Cross-Account.md`.
- **`iam:PassRole`-based escalation:** *null* — no PassRole in any of the 5 IAM pages.
- **Lens K (prompt injection):** *N/A* — AppInsights "insights"/root-cause are rule/classification-based, no customer-text-fed LLM in the pipeline. Pages read: `appinsights-what-is.md`, `appinsights-how-works.md`.
- **Lens H/W (KMS / attestation):** *N/A* — no customer-managed-key or attestation surface in these docs.

**Doc gaps (confirm surface first — do not conclude without these):**
1. **No public API Reference** (`/appinsights/latest/APIReference/*` 404). API shape reconstructed from the CLI reference — **field-level IAM condition keys, resource-level permission support, and authz error codes are undocumented.** This is the deciding gap for L1/L3/L6: *does `applicationinsights:*` support resource-level IAM scoping at all, or is `Resource:"*"` the only option?*
2. **SLR trust-policy JSON not printed** — needed to fully close cross-account/confused-deputy (any `aws:SourceAccount`/`aws:SourceArn`?).
3. **Whether `CreateComponent` `resourceList` ARNs are server-side validated** against the resource group/account (the hinge of L1) — not stated.
4. **CFN/Resource-Group/SSM-parameter name-derivation algorithm** — undocumented; blocks precise L9 land-grab without live experimentation.
5. **SSM document *content*** (`AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure`, `AWSEC2-DetectWorkload`) not published — can't confirm from docs whether `logPath`/parameters are shell-interpolated unsafely (would need `ssm:GetDocument` in an authorized account; relevant to escalating L1b/L2 from "file read" to RCE).
6. **`AmazonSSMManagedInstanceCore` + `CloudWatchAgentServerPolicy`** (required on the instance role) statements not printed here — adjacent Lens R targets deserving their own pass.
7. **Whether the instance's own role (not just the SLR) can `ssm:GetParameters` on `AmazonCloudWatch-ApplicationInsights-*`** — relevant to who else can read generated agent config.

---

## Appendix — Kill-chain to prioritize (chained leads, rated at the chain's end)

**Chain 1 (High→potentially Critical-if-service-plane):** L5 (ARN-form `componentName` bypasses RG containment) → L1 (SLR `ssm:SendCommand`/`CreateAssociation` on an out-of-scope instance, unconditioned `instance/*`) → L1b (`logPath` ships a sensitive file to an attacker-readable log group) **and/or** L2-adjacent (exporter config injects server-side SQL using Secrets-Manager DB creds). Entry primitive = narrow AppInsights rights; end = cross-team file read / DB query execution on instances the principal could never touch directly. **If any step surfaces an AWS-fleet identity → HARD STOP + disclose.**

**Chain 2 (Medium):** L4 (repoint `snsNotificationArn`) → harvest `problemId` + affected-resource ARNs from redirected notifications → L3 (`UpdateProblem` by ID to suppress the victim's real incident) — a disclosure-plus-integrity chain against another team's incident response.
