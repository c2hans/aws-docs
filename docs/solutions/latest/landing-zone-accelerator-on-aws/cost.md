---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. As of this revision, the cost for running this solution using the Landing Zone Accelerator on AWS [sample configuration](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations/lza-sample-config) with AWS Control Tower in the US East (N. Virginia) Region within a non-critical sandbox environment with no activity or workloads is approximately **$430.22 (USD)** each month.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Sample cost table
<a name="cost-table"></a>

The following table provides a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region, with no activity, for one month.

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| AWS CloudTrail |  +  4 million read/write management events <br />+  4.7 million paid events <br />+  Insights turned off (sample configuration)   | $99.00 |
| AWS Config |  +  2,000 AWS Config items <br />+  17,000 AWS Config rule evaluations   | $23.00 |
| AWS KMS |  +  43 customer managed keys (CMKs) <br />+  521,288 symmetric requests   | $44.56 |
| Amazon Kinesis |  +  4.5 million `PUT` payload units <br />+  744 `Shard` hours   | $11.22 |
| Amazon Data Firehose | 33,735 records x 5 KB | $4.66 |
| Amazon S3 |  +  7 GB standard storage <br />+  505,000 `PUT`, `COPY`, `POST`, or `LIST` requests <br />+  265,000 `GET`, `SELECT`, and other requests   | $2.79 |
| Amazon VPC |  +  2 Transit Gateway attachments with 3 GB each month ($73.12) <br />+  14 endpoints and 1 Availability Zone at 3 GB each month ($102.23)   | $175.35 |
| Amazon CloudWatch |  +  12 metrics <br />+  12 GB standard logs <br />+  2 GB logs delivered with 1-month retention   | $15.71 |
| AWS Security Hub |  +  1 account <br />+  30,000 security checks   | $30.00 |
| Amazon GuardDuty |  +  2.4 million management event analysis <br />+  2.4 million Amazon S3 data event analysis   | $11.52 |
| Amazon Route 53 | 6 hosted zones | $3.00 |
| Amazon Macie | 16 Amazon S3 buckets | $1.60 |
| AWS Secrets Manager | 2 secrets for 30 days | $0.81 |
| AWS CodePipeline | 2 pipelines each month | $1.00 |
| AWS CodeBuild | 60 builds a month x 5 minutes | $6.00 |
|  **Total monthly cost**  |  |  **$430.22**  |

**Note**
Data transfer, AWS CodeArtifact, Amazon Detective, Amazon DynamoDB, AWS Lambda, AWS Service Catalog, Amazon Simple Notification Service (Amazon SNS), Amazon Simple Queue Service (Amazon SQS), AWS Step Functions, and AWS Systems Manager are priced at the Free Tier or less than $0.01 each month.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
