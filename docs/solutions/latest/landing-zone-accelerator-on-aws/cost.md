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
| AWS CloudTrail |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $99.00 |
| AWS Config |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $23.00 |
| AWS KMS |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $44.56 |
| Amazon Kinesis |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $11.22 |
| Amazon Data Firehose | 33,735 records x 5 KB | $4.66 |
| Amazon S3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $2.79 |
| Amazon VPC |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $175.35 |
| Amazon CloudWatch |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $15.71 |
| AWS Security Hub |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $30.00 |
| Amazon GuardDuty |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/cost.html)  | $11.52 |
| Amazon Route 53 | 6 hosted zones | $3.00 |
| Amazon Macie | 16 Amazon S3 buckets | $1.60 |
| AWS Secrets Manager | 2 secrets for 30 days | $0.81 |
| AWS CodePipeline | 2 pipelines each month | $1.00 |
| AWS CodeBuild | 60 builds a month x 5 minutes | $6.00 |
|  **Total monthly cost**  |  |  **$430.22**  |

**Note**
Data transfer, AWS CodeArtifact, Amazon Detective, Amazon DynamoDB, AWS Lambda, AWS Service Catalog, Amazon Simple Notification Service (Amazon SNS), Amazon Simple Queue Service (Amazon SQS), AWS Step Functions, and AWS Systems Manager are priced at the Free Tier or less than $0.01 each month.
