---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/cost.html
---

# Cost

You are responsible for the cost of the AWS services provisioned while running this solution. As of this revision, the cost for running this solution at a medium scale in the US East (N. Virginia) Region is approximately **USD $65.25 per month**.

**Note**
The cost for running Innovation Sandbox on AWS in the AWS Cloud depends on the deployment configuration you choose. The following examples provide cost breakdown for various deployment configurations in the US East (N. Virginia) Region. AWS services listed in the example tables below are billed (in US$) on a monthly basis.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Example cost table
<a name="example-cost-tables"></a>

| Deployment type | Small deployment | Medium deployment | Large deployment |
| --- | --- | --- | --- |
| Example | 50 accounts, 30 leases (per month), 10 lease templates | 300 accounts, 150 leases (per month), 80 lease templates | 1000 accounts, 500 leases (per month), 100 lease templates |
|  **AWS Services**  | Cost (USD) | Cost (USD) | Cost (USD) |
| Amazon DynamoDB | $0.25 | $1.20 | $3.71 |
| AWS Lambda | $4.41 | $4.51 | $4.81 |
| AWS KMS | $4.91 | $4.91 | $4.92 |
| Amazon API Gateway | $1.05 | $1.05 | $1.05 |
| AWS WAF | $11.18 | $11.18 | $11.18 |
| AWS CodeBuild | $6.75 | $33.75 | $112.50 |
| AWS Step Functions | $0.18 | $0.91 | $3.04 |
| Amazon CloudFront | $0.21 | $0.22 | $0.22 |
| Amazon Simple Email Service | $0.02 | $0.11 | $0.35 |
| AWS Cost Explorer | $7.20 | $7.20 | $7.20 |
|  **Total Cost per month (USD)**  | \~**$36.40**  | \~**$65.25**  | \~**$149.20**  |

**Important**
This estimate does not include the costs incurred by sandbox account usage or blueprint deployments. You are responsible for setting appropriate lease configurations, monitoring spend of sandbox accounts, and considering the cost of resources deployed through blueprints.

**Note**
Blueprint deployments may incur additional costs depending on the resources defined in your CloudFormation StackSets. Consider the cost of blueprint resources when planning your deployment and setting lease budget limits. For example, a blueprint that deploys Amazon RDS databases, Amazon ElastiCache clusters, or Amazon EC2 instances will incur ongoing costs for the duration of the lease.

## Optional feature costs
<a name="optional-feature-costs"></a>

The following usage-based costs depend on the optional features that you enable:
+  **Estimated cost tracking**: For example, estimated cost tracking can cost less than USD $0.01 for each monitored lease each month. This estimate covers incremental Amazon DynamoDB reads and AWS Lambda calculations. It excludes the existing hourly AWS Cost Explorer polling represented in the example cost table.
+  **Amazon Bedrock token monitoring**: For example, Amazon Bedrock token monitoring can cost approximately USD $0.18–USD $0.35 for each monitored lease each month in each managed Region. This estimate covers baseline Amazon CloudWatch metric reads. A single query window requests four metrics, while a query split across two windows requests eight. Activity-dependent per-model queries increase this cost.
+  **Cost reconciliation**: Token monitoring shares an hourly AWS Cost Explorer reconciliation query. For example, a one-page query batch can cost approximately USD $7.20 for a 30-day month and cover up to 99 accounts. The example cost is approximately USD $0.07 for each account only when the page contains all 99 accounts. Additional pages, batches, and fallback queries increase the cost.
