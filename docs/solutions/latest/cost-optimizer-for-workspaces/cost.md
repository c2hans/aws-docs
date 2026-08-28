---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. The total cost of running this solution depends on the number of WorkSpaces that this solution monitors. As of the latest revision, the cost for running this solution with default settings in the US East (N. Virginia) Region is approximately **$42.00 per month** for 1,000 WorkSpaces. This reflects Amazon VPC, Amazon CloudWatch, Amazon DynamoDB, Amazon ECS (Fargate), Amazon S3, and AWS Lambda charges and does not include the cost of the individual WorkSpaces (refer to [Amazon WorkSpaces Pricing](https://aws.amazon.com/workspaces/pricing)).

The majority of this cost ($33.08/month) comes from the NAT Gateway. To reduce costs, you can deploy the solution in your existing Amazon VPC by providing your subnet IDs and security group ID during deployment.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](http://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this solution.

## CUDOS Dashboard
<a name="cudos-dashboard"></a>

While this solution helps you optimize WorkSpaces costs, to see the actual cost savings, you can also deploy a CUDOS dashboard by following the steps in our [CUDOS Dashboard lab](https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/#cudos-dashboard) and see the metrics for the cost saving. After deploying the CUDOS dashboard, you can navigate to the **End User Computing** tab to see the graphs for **Average Workspaces Cost per region** and **Workspaces spend per region**.

## Sample cost table: Scenario 1
<a name="sample-cost"></a>

The following table provides a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region for one month.

The cost for **Scenario 1** is based on the following assumptions:
+ Number of WorkSpaces: 1,000
+ Number of Amazon ECS Task runs per month: 30
+ Amazon ECS task run time in seconds: 600 (10 minutes)

| AWS service | Dimensions | Scenario 1 total cost (per month) [USD] |
| --- | --- | --- |
| Amazon VPC | NAT Gateway hourly and data processing charges (only if deploying a new VPC) | $33.08 |
| Amazon CloudWatch | Logs, metrics, dashboard, and API calls | $7.77 |
| Amazon DynamoDB | Storage and request units for UsageTable, UserSessionTable, and SpokeAccountTable | $0.83 |
| Amazon ECS (Fargate) | ECS task (0.25 vCPU, 1 GB memory) | $0.07 |
| Amazon S3 | Cost Optimizer Report bucket | $0.01 |
| AWS Lambda | Account registration and UUID generation (within free tier) | $0.00 |
|  **Total**  |  |  **$41.76**  |

The cost for **Scenario 2** is based on the following assumptions:
+ Number of WorkSpaces: 5,000
+ Number of Amazon ECS Task runs per month: 30
+ Amazon ECS task run time in seconds: 1,200 (20 minutes)

| AWS service | Dimensions | Scenario 2 total cost (per month) [USD] |
| --- | --- | --- |
| Amazon VPC | NAT Gateway hourly and data processing charges (only if deploying a new VPC) | $33.08 |
| Amazon CloudWatch | Logs, metrics, dashboard, and API calls | $17.21 |
| Amazon DynamoDB | Storage and request units for UsageTable, UserSessionTable, and SpokeAccountTable | $4.17 |
| Amazon ECS (Fargate) | ECS task (0.25 vCPU, 1 GB memory) | $0.15 |
| Amazon S3 | Cost Optimizer Report bucket | $0.01 |
| AWS Lambda | Account registration and UUID generation (within free tier) | $0.00 |
|  **Total**  |  |  **$54.62**  |

**Note**
The default values provided in Cost Optimizer for Amazon WorkSpaces for each of the WorkSpaces bundle type should be considered a guidance value only. Review Amazon WorkSpaces pricing for the AWS Region where you deployed the solution to determine the value for your location. Pricing differences between AWS Regions can mean a different billing break-even point between AutoStop and AlwaysOn instances.

Prices are subject to change. For full details, see the pricing webpage for each AWS service you will be using in this solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cost Optimizer for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
