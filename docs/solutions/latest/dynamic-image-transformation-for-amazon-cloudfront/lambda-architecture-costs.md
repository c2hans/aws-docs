---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/lambda-architecture-costs.html
---

# Lambda architecture costs
<a name="lambda-architecture-costs"></a>

You are responsible for the cost of the AWS services used while running the Lambda architecture. The below table gives the breakdown of costs for different workload sizes.

## Assumptions
<a name="lambda-cost-table"></a>
+ 90% cache hit rate
+ Average image size: 45 KB
+ 350 ms processing time per image

| AWS service | 10M images served | 125M images served | 500M images served |
| --- | --- | --- | --- |
|  **Amazon API Gateway**  | $1.00 | $13.00 | $50.00 |
|  **AWS Lambda**  | $0.93 | $12.08 | $46.46 |
|  **Amazon CloudFront**  | $200.00 | $200.00 | $1000.00 |
|  **Amazon S3**  | $0.40 | $5.00 | $20.00 |
|  **Amazon CloudWatch**  | $1.15 | $19.17 | $75.67 |
|  **Total**  |  **$203.48**  |  **$249.25**  |  **$1192.13**  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
