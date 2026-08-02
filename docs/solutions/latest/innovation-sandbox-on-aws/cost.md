---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services provisioned while running this solution. As of this revision, the cost for running this solution using the single instance deployment option in the US East (N. Virginia) Region is approximately **USD $65.25 per month**.

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
| AWS CostExplorer | $7.20 | $7.20 | $7.20 |
|  **Total Cost per month (USD)**  | \~**$36.40**  | \~**$65.25**  | \~**$149.20**  |

**Important**
This estimate does not include the costs incurred by sandbox account usage or blueprint deployments. Customers are responsible for setting appropriate lease configurations, monitoring spend of sandbox accounts, and considering the cost of resources deployed through blueprints.

**Note**
Blueprint deployments may incur additional costs depending on the resources defined in your CloudFormation StackSets. Consider the cost of blueprint resources when planning your deployment and setting lease budget limits. For example, a blueprint that deploys Amazon RDS databases, Amazon ElastiCache clusters, or Amazon EC2 instances will incur ongoing costs for the duration of the lease.
