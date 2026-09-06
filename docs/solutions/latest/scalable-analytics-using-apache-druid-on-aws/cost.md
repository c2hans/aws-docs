---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this guidance. As of the latest revision, the costs for running this guidance with the default settings (small usage profile) in the US East (N. Virginia) Region is approximately **$714.46 per month**, for a medium usage profile in the US East (N. Virginia) Region is approximately **$2,202.47 per month**, and for a large usage profile in the US East (N. Virginia) Region is approximately **$13,645.27 per month**.

These costs are for the resources shown in the [Cost table](#cost-table) section. See the pricing webpage for each AWS service used in this guidance.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this guidance](aws-services-in-this-solution.md).

## Cost table
<a name="cost-table"></a>

The following tables provide a sample cost breakdown for deploying this guidance with the default parameters in the US East (N. Virginia) Region for one month, encompassing the small, medium, and large usage profiles.

 **Small usage profile**

Profile assumptions: ingestion throughput at 30,000 records per second, query throughput at 25 queries per second.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| Amazon EC2 | \* Druid master: 3 x t4g.medium<br />\* Druid query: 3 x t4g.medium<br />\* Druid data: 3 x (t4g.medium \+ 100GB EBS GP2 volume)<br />\* ZooKeeper: 3 x t4g.small | $287.53 |
| Amazon ELB | 1 x ALB, 5 GB/h processed bytes (EC2 Instances and IP addresses as targets) | $45.63 |
| Amazon Aurora | 3 x db.t4g.medium | $247.81 |
| Amazon S3 | 1 TB standard storage \+ 1,000,000 requests per month | $29.67 |
| AWS Key Management Service | 7 x customer managed keys | $7 |
| AWS Secrets Manager | 4 x secrets | $1.6 |
| Amazon CloudWatch | 50 GB standard logs ingested per month, 200 custom metrics \+ 1,000,000 metric requests per month | $95.22 |
|  |  **Total:**  |  **$714.46 [USD] / month**  |

 **Medium usage profile**

Profile assumptions: ingestion throughput at 120,000 records per second, query throughput at 100 queries per second.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| Amazon EC2 | \* Druid master: 3 x m6g.xlarge<br />\* Druid query: 3 x m6g.xlarge<br />\* Druid data: 3 x (m6g.2xlarge \+ 500GB EBS GP2 volume)<br />\* ZooKeeper: 3 x t4g.medium | $1,572.62 |
| Amazon ELB | 1 x ALB, 20 GB/h processed bytes (EC2 Instances and IP addresses as targets) | $133.23 |
| Amazon Aurora | 3 x db.t4g.medium | $247.81 |
| Amazon S3 | 5 TB standard storage \+ 5,000,000 requests per month | $119.76 |
| AWS Key Management Service | 7 x customer managed keys | $7 |
| AWS Secrets Manager | 4 x secrets | $1.6 |
| Amazon CloudWatch | 100 GB standard logs ingested per month, 200 custom metrics \+ 1,000,000 metric requests per month | $120.45 |
|  |  **Total:**  |  **$2,202.47 [USD] / month**  |

 **Large usage profile**

Profile assumptions: ingestion throughput at 1.4 million records per second, query throughput at 1,200 queries per second.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| Amazon EC2 | \* Druid master: 3 x m6g.4xlarge<br />\* Druid query: 3 x m6g.4xlarge<br />\* Druid data: 3 x (m6g.16xlarge \+ 5 TB EBS GP2 volume)<br />\* ZooKeeper: 3 x m6g.2xlarge | $10,268.76 |
| Amazon ELB | 1 x ALB, 200 GB/h processed bytes (EC2 Instances and IP addresses as targets) | $1,184.43 |
| Amazon Aurora | 3 x db.t3.large | $427.39 |
| Amazon S3 | 50 TB standard storage \+ 10,000,000 requests per month | $1,181.60 |
| AWS Key Management Service | 7 x customer managed keys | $7 |
| AWS Secrets Manager | 4 x secrets | $1.6 |
| Amazon CloudWatch | 1,000 GB standard logs ingested per month, 200 custom metrics \+ 1,000,000 metric requests per month | $574.50 |
|  |  **Total:**  |  **$13,645.27 [USD] / month**  |
