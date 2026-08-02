---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services provisioned while running this solution. As of this revision, the cost for running this solution using the single instance deployment option in the US East (N. Virginia) Region is approximately **$0.58 per hour** or **$425.19 per month**.

**Note**
The cost for running Workload Discovery on AWS in the AWS Cloud depends on the deployment configuration you choose. The following examples provide cost breakdown for single instance and multiple instances deployment configurations in the US East (N. Virginia) Region. AWS services listed in the example tables below are billed on a monthly basis.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Example cost tables
<a name="example-cost-tables"></a>

### Option 1: Single instance deployment (default)
<a name="option-1-single-instance-deployment-default"></a>

When deploying this solution using an AWS CloudFormation template, modifying the **OpensearchMultiAz** parameter to `No` deploys a single instance for the OpenSearch Service domain, and modifying the **CreateNeptuneReplica** parameter to `No` deploys a single instance for the Neptune data store. The single instance deployment option incurs a lower cost, but it reduces the availability of Workload Discovery on AWS in the event of an Availability Zone failure.

| AWS service | Instance type | Hourly cost [USD] | Monthly cost [USD] |
| --- | --- | --- | --- |
| Amazon Neptune |  `db.r7g.large`  | $0.276 | $201.48 |
| Amazon OpenSearch Service |  `m6g.large.search`  | $0.128 | $93.44 |
| AppSync |  `cache.small`  | $0.044 | $32.12 |
| Amazon VPC (NAT Gateway) | N/A | $0.090 | $65.70 |
| AWS Config | N/A | $0.003 per resource | $0.003 per resource |
| Amazon ECS (AWS Fargate Task) | N/A | $0.02 | $12.01 |
| Total |  |  **$0.558**  |  **$404.75**  |

### Option 2: Multiple instances deployment
<a name="option-2-multiple-instances-deployment"></a>

When deploying this solution using an AWS CloudFormation template, modifying the **OpensearchMultiAz** parameter to `Yes` deploys two instances in two Availability Zones for the OpenSearch Service domain, and modifying the **CreateNeptuneReplica** parameter to `Yes` deploys two instances in two Availability Zones for the Neptune data store. The multiple instances deployment option will cost more to run, but it increases the availability of Workload Discovery on AWS in the event of an Availability Zone failure.

| AWS service | Instance type | Hourly cost | Monthly cost [USD] |
| --- | --- | --- | --- |
| Amazon Neptune |  `db.r7.xlarge`  | $0.552 | $402.96 |
| Amazon OpenSearch Service |  `m6g.large.search`  | $0.256 | $186.88 |
| AppSync |  `cache.small`  | $0.044 | $32.12 |
| Amazon VPC (NAT Gateway) | N/A | $0.09 | $65.70 |
| AWS Config | N/A | $0.003 per resource | $0.003 per resource |
| Amazon ECS (AWS Fargate Task) | N/A | $0.02 | $12.01 |
| Total |  |  **$0.962**  |  **$699.677**  |
+ Your final cost depends on the number of resources that AWS Config detects. $0.003 per resource item recorded will be incurred in addition to the amount provided in the table.

**Important**
The cost for Amazon Neptune and Amazon OpenSearch Service varies, depending on the instance type you select.
