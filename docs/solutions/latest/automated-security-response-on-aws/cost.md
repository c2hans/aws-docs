---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used to run this solution.

As of this revision, the estimated monthly costs are:
+ Small deployment (10 accounts, 1 region - US East/N. Virginia): Approximately $14.70 for 300 remediations/month
+ Medium deployment (100 accounts, 1 region - US East/N. Virginia): Approximately $106.40 for 3,000 remediations/month
+ Large deployment (1,000 accounts, 10 regions): Approximately $7,360.00 for 30,000 remediations/month

**Important**
Prices are subject to change. For full details, refer to the pricing page for each AWS service used in this solution.

**Note**
Many AWS Services include a Free Tier - a baseline amount of the service that customers can use at no charge. Actual costs may be more or less than the pricing examples provided.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through AWS Cost Explorer to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this solution.

## Sample cost table
<a name="sample-cost-table"></a>

The total cost to run this solution depends on the following factors:
+ The number of AWS Security Hub member accounts
+ The number of active automatically invoked remediations
+ The frequency of remediation

This solution uses the following AWS components, which incur a cost based on your configuration. Pricing examples are provided for small, medium, and large organizations.

| Service | Free Tier | Pricing [USD] |
| --- | --- | --- |
|  [AWS Systems Manager Automation - Step Count](https://aws.amazon.com/systems-manager/pricing/)  | No Free Tier | Each basic step is charged at $0.002 per step. For multi-account automations, all steps including those run in any child accounts are counted only in the originating account. |
|  [AWS Systems Manager Automation - Step Duration](https://aws.amazon.com/systems-manager/pricing/)  | No Free Tier | Each `aws:executeScript` action step is charged at $0.00003 for every second. |
|  [AWS Systems Manager Automation - Storage](https://aws.amazon.com/systems-manager/pricing/)  | No Free Tier | $0.046 per GB per month |
|  [AWS Systems Manager Automation - Data Transfer](https://aws.amazon.com/systems-manager/pricing/)  | No Free Tier | $0.900 per GB transferred (for cross-account or out-of-Region) |
|  [AWS Security Hub CSPM - Security Checks](https://aws.amazon.com/security-hub/cspm/pricing/)  | No Free Tier | First 100,000 checks/account/Region/month costs $0.0010 per check<br />Next 400,000 checks/account/Region/month costs $0.0008 per check<br />Over 500,000 checks/account/Region/month costs $0.0005 per check |
|  [AWS Security Hub CSPM - Finding Ingestion Events](https://aws.amazon.com/security-hub/cspm/pricing/)  | First 10,000 events/account/Region/month is free. Finding ingestion events associated with Security Hub’s security checks. | Over 10,000 events/account/Region/month costs $0.00003 per event |
|  [Amazon CloudWatch - Metrics](https://aws.amazon.com/cloudwatch/pricing/)  | Basic Monitoring Metrics (at 5-minute frequency) 10<br />Detailed Monitoring Metrics (at 1-minute frequency) 1<br />1 Million API requests (not applicable to GetMetricData, GetInsightRuleReport and GetMetricWidgetImage) | First 10,000 metrics costs $0.30 metric/month<br />Next 240,000 metrics costs $0.10 metric/month<br />Next 750,000 metrics costs $0.05 metric/month<br />Over 1,000,000 metrics costs $0.02 metric/month<br />API calls cost $0.01 per 1,000 requests |
|  [Amazon CloudWatch - Dashboard](https://aws.amazon.com/cloudwatch/pricing/)  | 3 Dashboards for up to 50 metrics per month | $3.00 per dashboard per month |
|  [Amazon CloudWatch - Alarms](https://aws.amazon.com/cloudwatch/pricing/)  | 10 Alarm metrics (not applicable to high-resolution alarms) | Standard Resolution (60 sec) costs $0.10 for each alarm metric<br />High Resolution (10 sec) costs $0.30 per alarm metric<br />Standard Resolution Anomaly Detection costs $0.30 per alarm<br />High Resolution Anomaly Detection costs $0.90 per alarm<br />Composite costs $0.50 per alarm |
|  [Amazon CloudWatch - Logs Collection](https://aws.amazon.com/cloudwatch/pricing/)  | 5GB Data (ingestion, archive storage, and data scanned by Logs Insights queries) | $0.50 per GB |
|  [Amazon CloudWatch - Logs Storage](https://aws.amazon.com/cloudwatch/pricing/)  | 5GB Data (ingestion, archive storage, and data scanned by Logs Insights queries) | $0.005 per GB of data scanned |
|  [AWS Lambda - Requests](https://aws.amazon.com/lambda/pricing/)  | 1M free requests per month | $0.20 per 1M requests |
|  [AWS Lambda - Duration](https://aws.amazon.com/lambda/pricing/)  | 400,000 GB-seconds of compute time per month | $0.0000166667 for every GB-second. The price for Duration depends on the amount of memory you allocate to your function. You can allocate any amount of memory to your function between 128MB and 10,240MB, in 1MB increments. |
|  [AWS Step Functions - State Transitions](https://aws.amazon.com/step-functions/pricing/)  | 4,000 free state transitions per month | $0.025 per 1,000 state transitions thereafter |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/pricing/)  | All state change events published by AWS services are free | Custom events cost $1.00/million custom events published<br />Third-party (SaaS) events cost $1.00/million events published<br />Cross-account events cost $1.00/million cross-account events sent |
|  [Amazon SNS](https://aws.amazon.com/sns/pricing/)  | First 1 million Amazon SNS requests per month are free | $0.50 per 1 million requests thereafter |
|  [Amazon SQS](https://aws.amazon.com/sqs/pricing/)  | First 1 million Amazon SQS requests per month are free | $0.40 per 1 million to 100 billion requests thereafter |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/pricing/)  | First 25GB of storage is free | $0.25 per GB per month for storage beyond the free tier. On-demand request pricing is $1.25 per 1 million write request units and $0.25 per 1 million read request units. The solution provisions several tables in the admin account (Findings, Remediation History, Remediation Configuration, Resource Filters, Notification Configuration, Notification Batches, Scheduling, and User Account Mapping). Storage for the Findings and Remediation History tables grows with the number of findings aggregated across your accounts and Regions. |
|  [AWS Key Management Service](https://aws.amazon.com/kms/pricing/)  | 20,000 requests/month | $1.00 per 1 AWS KMS key. $0.03 per 10,000 API requests. For AWS KMS keys that you rotate automatically or on demand, the first and second rotations of the key add $1/month (prorated hourly) in cost.<br /> **Note: This solution includes AWS KMS caching optimizations (S3 Bucket Keys, 60-minute SQS data key reuse, 5-minute Secrets Manager caching) that reduce AWS KMS API calls by approximately 70%.**  |
|  [Amazon Cognito](https://aws.amazon.com/cognito/pricing/)  | In the Essentials tier, the first 10,000 Monthly Active Users are free.<br />Note: This free tier is 50 Monthly Active Users when users authenticate via external IdP (SAML/OIDC). | $0.015 per Monthly Active User greater than 10,000 users. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/pricing/)  | Free tier includes 1 TB of data transfer out and 10,000,000 HTTP or HTTPS Requests per month. | (US/Canada/Mexico) First 9TB is $0.085 per month. Next 40TB is $0.080 per month.<br />$0.0075 per HTTP request. $0.0100 per HTTPS request. |
|  [Amazon S3](https://aws.amazon.com/s3/pricing/)  | No Free Tier | First 50 TB is $0.023 per GB per month.<br />$0.005 per 1,000 PUT, COPY, POST, LIST requests.<br />$0.0004 per 1,000 GET, SELECT, and all other requests. |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/pricing/)  | 1 Million REST API calls in the first 12 months of usage. | $3.50 per million for the first 333 million API calls. |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/pricing/)  | 30-day free trial per secret. | $0.40 per secret per month. $0.05 per 10,000 API calls. Used to store credentials for the Slack, JIRA, and ServiceNow notification and ticketing channels; one secret per configured channel. |
|  [AWS WAF](https://aws.amazon.com/waf/pricing/)  | No Free Tier | $5.00 per web ACL per month. $1.00 per rule per month. $0.60 per 1 million requests. Deployed to protect the Web UI API when the Web UI is enabled, with 10 rules (7 AWS Managed Rule groups plus 3 rate-based rules for per-user and per-IP rate limiting). The AWS Managed Bot Control rule group adds intelligent threat mitigation pricing of $10.00 per month plus $1.00 per 1 million requests. |
|  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/pricing/)  | First copy of management events is free. | $2.00 per 100,000 management events. Data events cost $0.10 per 100,000 events. Only incurred when you enable the Action Log with the **EnableCloudTrailForASRActionLog** parameter. |

## AWS KMS cost optimization
<a name="kms-optimization"></a>

Since **version 3.1.0**, this solution includes AWS KMS caching optimizations that reduce cryptographic operation costs by approximately 70%
+  **S3 Bucket Keys**: Reduces AWS KMS GenerateDataKey calls for S3 encryption operations
+  **SQS Data Key Reuse**: 60-minute cache period for message encryption
+  **Secrets Manager Caching**: 5-minute TTL in Lambda functions

 **Performance Impact**: These optimizations improve latency by 10-15ms for S3 operations and full workflows while reducing costs, with no throughput degradation.

## Pricing examples (monthly)
<a name="pricing-examples"></a>

**Note**
The Amazon DynamoDB figures in the following examples account for the Findings and Remediation History tables, which dominate storage. The solution’s other tables — Remediation Configuration, Resource Filters, Notification Configuration, Notification Batches, Scheduling, and User Account Mapping — hold negligible data and are omitted for clarity. The examples also assume you have not configured Slack, JIRA, or ServiceNow channels; each channel you configure adds one AWS Secrets Manager secret (see the preceding component table). The AWS Lambda and Amazon SNS line items include the notification pipeline (the notification-dispatcher and per-channel fanout Lambda functions and the per-configuration SNS topics they publish to); at the request volumes modeled here these add well under $0.01 to Lambda ($0.20 per 1M requests) and SNS ($0.50 per 1M requests). AWS WAF (and its Bot Control intelligent threat mitigation charge) appears only in the Web UI-enabled examples, since the WAF-protected API Gateway is deployed only when the Web UI is enabled.

### Example 1: 300 remediations per month
<a name="example-1-300-remediations-per-month"></a>
+ 10 accounts, 1 Region
+ 30 remediations per account/Region/month
+ 500 Security Hub findings processed per account/Region/month
+  **Web UI disabled**
+  **Action Log disabled**
+ Total cost $14.70 per month

| Service | Assumptions | Monthly charges [USD] |
| --- | --- | --- |
| AWS Systems Manager Automation | Steps: \~4 steps \* 300 remediations \* $0.002 = $2.40<br />Duration: 10s \* 300 remediations \* $0.00003 = $0.09 | $2.49 |
| AWS Security Hub | No billable services utilized | $0 |
| Amazon CloudWatch Logs | $0.50 per GB | < $0.01 |
| AWS Lambda - Requests | 300 remediations \* 7 requests = 2,100 requests<br />5,000 findings \* 1 request = 5,000 requests<br />$0.20 / 1,000,000 requests = $0.0000002 per request | $0.00142 |
| AWS Lambda - Duration | (512MB Memory)<br />4,000ms \* 300 remediations \* $0.0000000083 = $0.00996<br />449ms \* 5,000 findings \* $0.0000000083 = $.0186 | $0.029 |
| AWS Step Functions | 19 state transitions \* 300 remediations = 5,700<br />$0.025 \* (5,700/1,000) state transitions = $0.14 | $0.14 |
| Amazon EventBridge rules | No charge for rules | $0 |
| AWS Key Management Service | 1 key \* 10 accounts \* 1 Region \* $1 = $10<br />(Encrypt/Decrypt API requests)<br />(300 remediations \* 2 requests) \+ (5,000 findings \* 4 requests) = 20,600 requests<br />With AWS KMS caching: 20,600 \* 0.30 = 6,180 requests<br />$0.03 per 10,000 requests ⇒ $0.03 \* (6,180 / 10,000) = $0.02 | $10.02 |
| Amazon DynamoDB | $2.00 \* 1,000,000 read and writes = $2.00<br />(Findings Table) 15MB \* 10 accounts \* 1 region = 150MB<br />(History Table) 10MB \* 10 accounts \* 1 region = 100MB<br />$0.25 per GB-month \* 0.25 GB = $0.0625 | $2.0625 |
| Amazon SQS | $0.40 \* 1,000,000 requests = $0.40 | $0.40 |
| Amazon SNS | $0.50 \* (600 / 1,000,000 notifications) = $0.0003 | $0.0003 |
| Amazon CloudWatch - Metrics | (Enhanced Metrics Disabled)<br />$0.30 \* 7 custom metrics = $2.10<br />$0.01 \* (300 put metrics API calls / 1,000) = $0.003 | $2.10 |
| Amazon CloudWatch - Dashboards | $3.00 \* 1 dashboard = $3.00 | $3.00 |
| Amazon CloudWatch - Alarms | (Enhanced Metrics Disabled)<br />$0.10 \* 4 alarms = $0.40 | $0.40 |
| Amazon CloudWatch - X-Ray Traces | 300 remediations \* 7 requests = 2,100 Lambda invocations<br />5,000 findings \* 1 request = 5,000 Lambda invocations<br />$0.000005 per trace \* 7,100 traces = $0.0355 | $0.0355 |
|  **Total**  |  |  **$14.70**  |

### Example 2: 300 remediations per month (Web UI Enabled)
<a name="example-2-300-remediations-per-month"></a>
+ 10 accounts, 1 Region
+ 30 remediations per account/Region/month
+ 5,000 Security Hub findings processed per account/Region/month
+  **Web UI enabled**
+  **Action Log disabled**
+ Total cost $49.31 per month

| Service | Assumptions | Monthly charges [USD] |
| --- | --- | --- |
| AWS Systems Manager Automation | Steps: \~4 steps \* 300 remediations \* $0.002 = $2.40<br />Duration: 10s \* 300 remediations \* $0.00003 = $0.09 | $2.49 |
| AWS Security Hub | No billable services utilized | $0 |
| Amazon CloudWatch Logs | $0.50 per GB | < $0.01 |
| AWS Lambda - Requests | 300 remediations \* 7 requests = 2,100 requests<br />5,000 findings \* 1 request = 5,000 requests<br />$0.20 / 1,000,000 requests = $0.0000002 per request | $0.00142 |
| AWS Lambda - Duration | (512MB Memory)<br />4,000ms \* 300 remediations \* $0.0000000083 = $0.00996<br />449ms \* 5,000 findings \* $0.0000000083 = $.0186 | $0.029 |
| AWS Step Functions | 19 state transitions \* 300 remediations = 5,700<br />$0.025 \* (5,700/1,000) state transitions = $0.14 | $0.14 |
| Amazon EventBridge rules | No charge for rules | $0 |
| AWS Key Management Service | 1 key \* 10 accounts \* 1 Region \* $1 = $10<br />(Encrypt/Decrypt API requests)<br />(300 remediations \* 2 requests) \+ (5,000 findings \* 4 requests) = 20,600 requests<br />With AWS KMS caching: 20,600 \* 0.30 = 6,180 requests<br />$0.03 per 10,000 requests ⇒ $0.03 \* (6,180 / 10,000) = $0.02 | $10.02 |
| Amazon DynamoDB | $2.00 \* 1,000,000 read and writes = $2.00<br />(Findings Table) 15MB \* 10 accounts \* 1 region = 150MB<br />(History Table) 10MB \* 10 accounts \* 1 region = 100MB<br />$0.25 per GB-month \* 0.25 GB = $0.0625 | $2.0625 |
| Amazon SQS | $0.40 \* 1,000,000 requests = $0.40 | $0.40 |
| Amazon SNS | $0.50 \* (600 / 1,000,000 notifications) = $0.0003 | $0.0003 |
| Amazon CloudWatch - Metrics | (Enhanced Metrics Disabled)<br />$0.30 \* 7 custom metrics = $2.10<br />$0.01 \* (300 put metrics API calls / 1,000) = $0.003 | $2.10 |
| Amazon CloudWatch - Dashboards | $3.00 \* 1 dashboard = $3.00 | $3.00 |
| Amazon CloudWatch - Alarms | (Enhanced Metrics Disabled)<br />$0.10 \* 4 alarms = $0.40 | $0.40 |
| Amazon CloudWatch - X-Ray Traces | 300 remediations \* 7 requests = 2,100 Lambda invocations<br />5,000 findings \* 1 request = 5,000 Lambda invocations<br />$0.000005 per trace \* 7,100 traces = $0.0355 | $0.0355 |
| Amazon Cognito | (Essentials Tier)<br />500 Monthly Active Users | $0 |
| Amazon CloudFront | Regional Data Transfer Out to Origin (per GB) = $0.020<br />Regional Data Transfer Out to Internet (per GB) = $0.085<br />Request Pricing for All HTTP Methods (per 10,000) = $0.0075 | $0.1125 |
| Amazon S3 | (UI Hosting)<br />$0.023 per GB \* 0.002 GB = $0.000046<br />(History Export) $0.023 per GB \* 0.50 GB = $0.0125<br />$0.0004 per 1,000 GET requests | $0.0125 |
| AWS WAF | 1 Web ACL = $5.00 per month<br />10 rules \* $1.00 per rule = $10.00 (7 AWS Managed Rule groups \+ 3 rate-based rules)<br />Bot Control intelligent threat mitigation = $10.00 per month (plus $1.00 per 1M requests and $0.60 per 1M WAF request charges, both negligible at Web UI request volumes) | $25.00 |
| Amazon API Gateway | $3.50 per million REST API calls | $3.50 |
|  **Total**  |  |  **$49.31**  |

### Example 3: 3,000 remediations per month
<a name="example-3-3000-remediations-per-month"></a>
+ 100 accounts, 1 Region
+ 30 remediations per account/Region/month
+ 500 Security Hub findings processed per account/Region/month
+  **Web UI disabled**
+  **Action Log disabled**
+ Total cost $106.49 per month

| Service | Assumptions | Monthly charges [USD] |
| --- | --- | --- |
| AWS Systems Manager Automation | Steps: \~4 steps \* 3,000 remediations \* $0.002 = $24.00<br />Duration: 10s \* 3,000 remediations \* $0.00003 = $0.90 | $24.90 |
| AWS Security Hub | No billable services utilized | $0 |
| Amazon CloudWatch Logs | $0.50 per GB | < $0.01 |
| AWS Lambda - Requests | 3,000 remediations \* 7 requests = 21,000 requests<br />50,000 findings \* 1 request = 50,000 requests<br />$0.20 / 1,000,000 requests = $0.0000002 per request | $0.01 |
| AWS Lambda - Duration | (512MB Memory)<br />4,000ms \* 3,000 remediations \* $0.0000000083 = $0.0996<br />449ms \* 50,000 findings \* $0.0000000083 = $0.186 | $0.29 |
| AWS Step Functions | 19 state transitions \* 3,000 remediations = 57,000<br />$0.025 \* (57,000/1,000) state transitions = $1.425 | $1.425 |
| Amazon EventBridge rules | No charge for rules | $0 |
| AWS Key Management Service | 1 key \* 100 accounts \* 1 Region \* $1 = $100<br />(Encrypt/Decrypt API requests)<br />(3,000 remediations \* 2 requests) \+ (50,000 findings \* 4 requests) = 206,000 requests<br />With AWS KMS caching: 206,000 \* 0.30 = 61,800 requests<br />$0.03 per 10,000 requests ⇒ $0.03 \* (61,800 / 10,000) = $0.185 | $100.185 |
| Amazon DynamoDB | $2.00 \* 1,000,000 read and writes = $2.00<br />(Findings Table) 15MB \* 100 accounts \* 1 region = 1,500MB<br />(History Table) 10MB \* 100 accounts \* 1 region = 1,000MB<br />$0.25 per GB-month \* 2.5 GB = $0.625 | $2.625 |
| Amazon SQS | $0.40 \* 1,000,000 requests = $0.40 | $0.40 |
| Amazon SNS | $0.50 \* 1,000,000 notifications = $0.50 | $0.50 |
| Amazon CloudWatch - Metrics | (Enhanced Metrics Disabled)<br />$0.30 \* 7 custom metrics = $2.10<br />$0.01 \* (3000 / 1,000) put metrics API calls = $0.03 | $2.13 |
| Amazon CloudWatch - Dashboards | $3.00 \* 1 dashboard = $3.00 | $3.00 |
| Amazon CloudWatch - Alarms | $0.10 \* 4 alarms = $0.40 | $0.40 |
| Amazon CloudWatch - X-Ray Traces | 3,000 remediations \* 7 requests = 21,000 Lambda invocations<br />50,000 findings \* 1 request = 50,000 Lambda invocations<br />$0.000005 per trace \* 71,000 traces = $0.355 | $0.355 |
|  **Total**  |  |  **$106.49**  |

### Example 4: 30,000 remediations per month
<a name="example-4-30000-remediations-per-months"></a>
+ 1,000 accounts, 10 Regions
+ 30 remediations per account/Region/month
+ 500 Security Hub findings processed per account/Region/month
+  **Web UI disabled**
+  **Action Log disabled**
+ Total cost $7,360.00 per month

| Service | Assumptions | Monthly charges [USD] |
| --- | --- | --- |
| AWS Systems Manager Automation | Steps: \~4 steps \* 30,000 remediations \* $0.002 = $240.00<br />Duration: 10s \* 30,000 remediations \* $0.00003 = $9.00 | $249.00 |
| AWS Security Hub | No billable services utilized | $0 |
| Amazon CloudWatch Logs | $0.50 per GB | < $0.01 |
| AWS Lambda - Requests | 30,000 remediations \* 7 requests = 210,000 requests<br />5,000,000 findings \* 1 request = 5,000,000 requests<br />$0.20 / 1,000,000 requests = $0.0000002 per request | $1.042 |
| AWS Lambda - Duration | (512MB Memory)<br />4,000ms \* 30,000 remediations \* $0.0000000083 = $0.996<br />449ms \* 5,000,000 findings \* $0.0000000083 = $18.63 | $19.63 |
| AWS Step Functions | 19 state transitions \* 30,000 remediations = 570,000<br />$0.025 \* (570,000/1,000) state transitions = $14.25 | $14.25 |
| Amazon EventBridge rules | No charge for rules | $0 |
| AWS Key Management Service | (1 key) $1 \* 1,000 accounts \* 10 Region = $10,000<br />(Encrypt/Decrypt API requests)<br />(30,000 remediations \* 2 requests) \+ (5,000,000 findings \* 4 requests) = 20,060,000 requests<br />With AWS KMS caching: 20,060,000 \* 0.30 = 6,018,000 requests<br />$0.03 per 10,000 requests ⇒ $0.03 \* (6,018,000 / 10,000) = $18.05 | $10,018.05 |
| Amazon DynamoDB | $2.00 \* (10,000,000 read and writes / 1,000,000) = $20.00<br />(Findings Table) 15MB \* 1000 accounts \* 10 region = 150GB<br />(History Table) 10MB \* 1000 accounts \* 10 region = 100GB<br />$0.25 per GB-month \* 250 GB = $62.50 | $82.50 |
| Amazon SQS | $0.40 \* (5,060,000 requests / 1,000,000 ) = $2.024 | $2.024 |
| Amazon SNS | $0.000005 \* 1,000,000 notifications = $0.50 | $0.50 |
| Amazon CloudWatch - Metrics | (Enhanced Metrics Disabled)<br />$0.30 \* 7 custom metrics = $2.10<br />$0.01 \* (30,000 / 1,000) put metrics API calls = $0.30 | $2.40 |
| Amazon CloudWatch - Dashboards | $3.00 \* 1 dashboard = $3.00 | $3.00 |
| Amazon CloudWatch - Alarms | (Enhanced Metrics Disabled)<br />$0.10 \* 4 alarms = $0.40 | $0.40 |
| Amazon CloudWatch - X-Ray Traces | 30,000 remediations \* 7 requests = 210,000 Lambda invocations<br />5,000,000 findings \* 1 request = 5,000,000 Lambda invocations<br />$0.000005 per trace \* 5,210,000 traces = $26.05 | $26.05 |
|  **Total**  |  |  **$7,360.00**  |

### Example 5: 30,000 remediations per month (Web UI Enabled)
<a name="example-5-30000-remediations-per-months"></a>
+ 1,000 accounts, 10 Regions
+ 30 remediations per account/Region/month
+ 500 Security Hub findings processed per account/Region/month
+  **Web UI enabled**
+  **Action Log disabled**
+ Total cost $7,393.10 per month

| Service | Assumptions | Monthly charges [USD] |
| --- | --- | --- |
| AWS Systems Manager Automation | Steps: \~4 steps \* 30,000 remediations \* $0.002 = $240.00<br />Duration: 10s \* 30,000 remediations \* $0.00003 = $9.00 | $249.00 |
| AWS Security Hub | No billable services utilized | $0 |
| Amazon CloudWatch Logs | $0.50 per GB | < $0.01 |
| AWS Lambda - Requests | 30,000 remediations \* 7 requests = 210,000 requests<br />5,000,000 findings \* 1 request = 5,000,000 requests<br />$0.20 / 1,000,000 requests = $0.0000002 per request | $1.042 |
| AWS Lambda - Duration | (512MB Memory)<br />4,000ms \* 30,000 remediations \* $0.0000000083 = $0.996<br />449ms \* 5,000,000 findings \* $0.0000000083 = $18.63 | $19.63 |
| AWS Step Functions | 19 state transitions \* 30,000 remediations = 570,000<br />$0.025 \* (570,000/1,000) state transitions = $14.25 | $14.25 |
| Amazon EventBridge rules | No charge for rules | $0 |
| AWS Key Management Service | (1 key) $1 \* 1,000 accounts \* 10 Region = $10,000<br />(Encrypt/Decrypt API requests)<br />(30,000 remediations \* 2 requests) \+ (5,000,000 findings \* 4 requests) = 20,060,000 requests<br />With AWS KMS caching: 20,060,000 \* 0.30 = 6,018,000 requests<br />$0.03 per 10,000 requests ⇒ $0.03 \* (6,018,000 / 10,000) = $18.05 | $10,018.05 |
| Amazon DynamoDB | $2.00 \* (10,000,000 read and writes / 1,000,000) = $20.00<br />(Findings Table) 15MB \* 1000 accounts \* 10 region = 150GB<br />(History Table) 10MB \* 1000 accounts \* 10 region = 100GB<br />$0.25 per GB-month \* 250 GB = $62.50 | $82.50 |
| Amazon SQS | $0.40 \* (5,060,000 requests / 1,000,000 ) = $2.024 | $2.024 |
| Amazon SNS | $0.000005 \* 1,000,000 notifications = $0.50 | $0.50 |
| Amazon CloudWatch - Metrics | (Enhanced Metrics Disabled)<br />$0.30 \* 7 custom metrics = $2.10<br />$0.01 \* (30,000 / 1,000) put metrics API calls = $0.30 | $2.40 |
| Amazon CloudWatch - Dashboards | $3.00 \* 1 dashboard = $3.00 | $3.00 |
| Amazon CloudWatch - Alarms | (Enhanced Metrics Disabled)<br />$0.10 \* 4 alarms = $0.40 | $0.40 |
| Amazon CloudWatch - X-Ray Traces | 30,000 remediations \* 7 requests = 210,000 Lambda invocations<br />5,000,000 findings \* 1 request = 5,000,000 Lambda invocations<br />$0.000005 per trace \* 5,210,000 traces = $26.05 | $26.05 |
| Amazon Cognito | (Essentials Tier)<br />5,000 Monthly Active Users | $0 |
| Amazon CloudFront | Regional Data Transfer Out to Origin (per GB) = $0.020<br />Regional Data Transfer Out to Internet (per GB) = $0.085<br />Request Pricing for All HTTP Methods (per 10,000) = $0.0075 | $0.1125 |
| Amazon S3 | (UI Hosting)<br />$0.023 per GB \* 0.002 GB = $0.000046<br />(History Export) $0.023 per GB \* 100 GB = $2.30<br />$0.0004 per 1,000 GET requests \* 5,000 requests = $2.00 | $4.30 |
| AWS WAF | 1 Web ACL = $5.00 per month<br />10 rules \* $1.00 per rule = $10.00 (7 AWS Managed Rule groups \+ 3 rate-based rules)<br />Bot Control intelligent threat mitigation = $10.00 per month (plus $1.00 per 1M requests and $0.60 per 1M WAF request charges, both negligible at Web UI request volumes) | $25.00 |
| Amazon API Gateway | $3.50 per million REST API calls | $3.50 |
|  **Total**  |  |  **$7,393.10**  |

**Important**
 **AWS KMS Key Rotation Costs** AWS Key Management Service (AWS KMS) automatically rotates customer managed keys once per year when rotation is enabled. Each rotation incurs a cost of $1.00 per key per year. For example, with 1000 accounts in a single region, this results in an additional $1000/year (1 rotation × 1000 keys × $1.00).

## Additional cost for optional features
<a name="additional-cost-optional"></a>

This section identifies additional costs associated with optional features for this solution.

### Enhanced CloudWatch metrics
<a name="additional-cost-enhanced-metrics"></a>

If you select `yes` for the **EnableEnhancedCloudWatchMetrics** parameter when deploying the admin stack, the solution creates two custom metrics and one alarm for each control ID. The cost depends on the number of control IDs that you are remediating. In the following table, we assume that you are remediating all 96 different control IDs per month, to determine the upper bound of costs.

| Service | Assumptions 96 control IDs \* 2 = 192 custom metrics | Monthly charges [USD] |
| --- | --- | --- |
| Amazon CloudWatch - Metrics | $0.30 \* 192 custom metrics = $57.60 | $57.60 |
| Amazon CloudWatch - Alarms | $0.10 \* 96 alarms = $9.60 | $9.60 |
|  **Total**  |  |  **$67.20**  |

### CloudTrail Action Log
<a name="additional-cost-action-log"></a>

In each member account that you enable the Action Log feature for, the solutions creates a CloudTrail trail to log all write management events. A Lambda function filters out events not related to the solution. This means that the cost is related to the total number of management events in your account, since events not related to the solution are still captured by the trail and processed by the Lambda function.

For the following table, we assume 150,000 management events per month in the account. The actual cost depends on the actual management event activity in your account.

| Service | Assumptions | Monthly charges [USD] |
| --- | --- | --- |
| AWS CloudTrail | 150,000 \* $2.00/100,000 = $3.00 | $3.00 |
| Lambda | 150,000 \* 0.2 \* 0.125 = 3,750 GB-seconds<br />3,750 \* $0.0000166667 = $0.0625 compute time cost<br />0.15 \* $0.20 = $0.03 request cost<br />$0.0625 \+ $0.03 = $0.0925 total Lambda cost | $0.0925 |
|  **Total**  |  |  **$3.09 per member account**  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
