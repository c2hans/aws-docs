---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution.

**Note**
The cost for running Spatial Data Management on AWS depends on your deployment configuration, data volume, and usage patterns. The following examples provide cost breakdowns for various deployment sizes in the US West (Oregon) Region.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Example Cost Table
<a name="example-cost-table"></a>

| Deployment Size | Small | Medium | Large |
| --- | --- | --- | --- |
|  **Example**  | < 1 TB data, 10 users | 1-10 TB data, 50 users | > 10 TB data, 100\+ users |
|  **AWS Services**  |  **Cost (USD)**  |  **Cost (USD)**  |  **Cost (USD)**  |
| Amazon S3 | $23.55 | $235.50 | $2,355.00 |
| Amazon DynamoDB | $5.00 | $25.00 | $100.00 |
| AWS Lambda | $10.00 | $50.00 | $200.00 |
| Amazon API Gateway | $3.50 | $17.50 | $70.00 |
| Amazon OpenSearch Serverless | $350.00 | $350.00-$700.00 | $700.00\+ |
| Amazon CloudFront | $5.00 | $25.00 | $100.00 |
| AWS Key Management Service | $5.00 | $5.00 | $5.00 |
| Amazon Cognito | $2.00 | $10.00 | $40.00 |
| VPC endpoints | $15.00 | $15.00 | $15.00 |
| Amazon CloudWatch | $5.00 | $15.00 | $50.00 |
| AWS Deadline Cloud | $8.00 | $40.00 | $160.00 |
|  **Total Cost per month (USD)**  | \~**$432.00**  | \~**$788.00–$1,138.00**  | \~**$3,795.00\+**  |

**Important**
This estimate assumes: S3 storage costs based on data volume (1 TB = $23.55/month), moderate API request volume, standard data transfer rates, and on-demand pricing for all services. AWS Deadline Cloud costs assume a small percentage of files undergo metadata extraction jobs and one file conversion job per file to generate preview (for example, E57 to MP4 turntable low-resolution preview). Amazon OpenSearch Serverless has a minimum cost of approximately $350/month (2 OCUs for indexing and search) regardless of data volume or usage — this represents the base cost floor for all deployments.

Actual costs will vary based on:
+ Data volume and growth rate
+ Number of API requests
+ Data transfer (uploads/downloads)
+ Search query frequency
+ Number of concurrent users
+ Compute resources used for data transformations and integration orchestration with external applications

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
