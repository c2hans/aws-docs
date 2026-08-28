---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/cost.html
---

# Cost
<a name="cost"></a>

 You are responsible for the cost of the AWS services used while running this solution. The total cost to run this solution depends on the number of policies installed, the number of AWS Lambda functions and their running duration, and the number of Amazon EventBridge events published. As of the most recent revision, the estimated cost for running this solution with default settings in the US East (N. Virginia) Region without Open Policy Agent (OPA) activated is approximately **$96.48**, and with OPA activated is approximately **$137.48**. The option with OPA activated provides advanced validation for the API. Refer to [Architecture overview](architecture-overview.md) for more details.

**Note**
 To activate the rules managed by this solution an AWS Network Firewall (ANFW) instance is required. Refer to [AWS Network Firewall pricing](https://aws.amazon.com/network-firewall/pricing/) for more details about the pricing. The following cost estimation excludes ANFW instance pricing.

|  **AWS service**  |  **Dimensions**  |  **Cost/month**  |
| --- | --- | --- |
|  AWS Lambda  |  8640 requests per month, Lambda memory: 3GB of memory  |  $8.64  |
|  AWS CloudWatch Events  |  Number of custom/cross-account events (8640), number of Lambda functions (2), number of requests per function (8640 per month).  |  $6.01  |
|  Amazon S3  |  0.1 GB bucket size  |  Negligible  |
|  NAT Gateway  |  0.5 GB data/hour, $ 0.059/hour |  $43.13  |
|  DynamoDB  |  1GB storage, 200Kb average size for attributes  |  $8.70  |
|  AWS Config  |  10000 resources  |  $30.00  |
|   |  Total (without OPA enabled):  |  $96.48  |
|  AWS Fargate\*  |  0.5 vCPU, 2GB vMemory  |  $22.00  |
|  Elastic Load Balancing (ELB)  |  1 \* ALB, 2 new connections per second  |  $19.00  |
|   |  Total (with OPA activated; enableOpa = true):  |  $137.48  |

 \*AWS Fargate is used with Amazon Elastic Container Service (Amazon ECS).

**Note**
 The cost associated with Amazon ECS on AWS Fargate and ELB only occurs with OPA activated, that is when configuration `enableOpa` is set to `true`.

 We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html)  through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
