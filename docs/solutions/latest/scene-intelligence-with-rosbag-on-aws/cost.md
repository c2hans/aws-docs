---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. As of this revision, the cost for running this solution with the default settings in the default US East (N. Virginia) Region is approximately **$605.13 per month**.

See the pricing webpage for each AWS service used in this solution.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this solution](aws-services-in-this-solution.md).

## Sample cost table
<a name="sample-cost-table"></a>

The following table provides a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region for one month.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
|  **Amazon MWAA**  | 31 days × 24 hours/day (1 worker, 2 schedulers) | $355.00 |
|  **Amazon EMR Serverless**  | 2 vCPU × vCPU-hours rate ($0.052624) × job runtime in hour (8 min/60 min)<br />4GB memory × GB-hours rate($0.0057785) × job runtime in hour (8 min/60 min) | $0.016 |
|  **Amazon OpenSearch Service**  | 31 days × 24 hours/day (1 node with 50 GB storage and no dedicated master) | $128.00 |
|  **Amazon EC2**  | Includes AWS Batch jobs processing (only when invoked) and Amazon EC2 proxy (31 days × 24 hours/day) for querying OpenSearch Service | $49.00 |
|  **AWS Lambda**  |  [AWS Free Tier](https://aws.amazon.com/free/compute/)  | $0.00 |
|  **Systems Manager Parameter Store**  |  | $0.05 |
|  **AWS CodeBuild**  | Invoked during deploying and destroying the solution | $25.00 |
|  **Amazon CloudWatch**  |  | $20.00 |
|  **Amazon VPC**  |  | $19.00 |
|  **Amazon S3**  |  | $6.20 |
|  **Amazon ECR**  |  | $1.60 |
|  **AWS KMS**  |  | $1.20 |
|  **Amazon SageMaker AI**  | LaneDet and object detection | $0.06 |
|  **Amazon DynamoDB**  |  [AWS Free Tier](https://aws.amazon.com/free/database/)  | $0.00 |
|  |  **Total:**  |  **$605.13 [USD] / month**  |
