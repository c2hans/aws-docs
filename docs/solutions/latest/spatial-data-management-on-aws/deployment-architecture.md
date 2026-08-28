---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/deployment-architecture.html
---

# Deployment Architecture
<a name="deployment-architecture"></a>

The solution is deployed using AWS CloudFormation with nested stacks:

| Stack | Components |
| --- | --- |
| VPC Stack | Network infrastructure |
| Auth Stack | Amazon Cognito and Amazon Verified Permissions |
| Asset Management Stack | Core services (Lambda, DynamoDB, S3, API Gateway) |
| OpenSearch Stack | Search infrastructure |
| Portal Stack | Amazon CloudFront and web assets |
| Deadline Stack | Rendering and batch processing services |
| Monitoring Stack | Amazon CloudWatch, AWS CloudTrail, and AWS X-Ray |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
