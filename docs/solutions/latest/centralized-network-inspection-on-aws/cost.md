---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/cost.html
---

# Cost
<a name="cost"></a>

 You are responsible for the cost of the AWS services used while running this guidance. As of this revision, the cost for running this guidance with the default settings in the US East (N. Virginia) Region is approximately **$620.55 per month**. These costs are for the resources shown in the [Sample cost table](#sample-cost-table).

 We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html)  through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this guidance](architecture-details.md#amazon-cloudwatch).

## Sample cost table
<a name="sample-cost-table"></a>

 The following table provides a sample cost breakdown for deploying this guidance with the default parameters in the US East (N. Virginia) Region for one month.

|  AWS service  |  Dimensions  |  Total cost (per month) [USD]  |
| --- | --- | --- |
| **AWS Network Firewall (endpoint) ** |  2 endpoints/24 hours ($0.395/endpoint/hour)  |  $568.80  |
| **AWS Network Firewall (data processed) ** |  5 GB ($0.65/GB)  |  $9.75  |
| **AWS Transit Gateway (VPC attachment) ** |  24 hours ($0.05/hour)  |  $36.00  |
| ** AWS Transit Gateway (data processed) ** |  10 GB ($0.02/GB)  |  $6.00  |
| **Amazon CodePipeline ** |   |  Depends on number of CodePipeline executions  |
| **Amazon CodeBuild ** |   |  Depends on number of CodePipeline executions  |
| **Amazon S3 ** |   |  Depends on number of CodePipeline executions and Network Firewall log activity  |
|   |  Total  |  $620.55  |
