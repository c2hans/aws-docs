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
