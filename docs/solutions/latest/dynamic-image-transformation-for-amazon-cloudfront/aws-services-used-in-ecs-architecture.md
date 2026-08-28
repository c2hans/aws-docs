---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/aws-services-used-in-ecs-architecture.html
---

# AWS services used in ECS architecture
<a name="aws-services-used-in-ecs-architecture"></a>

| AWS service | Description |
| --- | --- |
|  **Compute & Serverless**  |  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  | Image processing functions, API handlers |
|  [Amazon Rekognition](https://aws.amazon.com/rekognition/)  | Image transformation features (smart cropping, content moderation) |
|  **API & Networking**  |  |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  | REST API for image transformation requests |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  | CDN for content delivery and caching |
|  [Elastic Load Balancing v2](https://aws.amazon.com/elasticloadbalancing/)  | Application load balancing (for ECS architecture) |
|  **Storage**  |  |
|  [Amazon S3](https://aws.amazon.com/s3/)  | Source image storage, transformed image cache |
|  **Database**  |  |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  | Storing transformation policies, mappings, and origins |
|  **Authentication & Authorization**  |  |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  | User authentication for admin UI |
|  [AWS IAM](https://aws.amazon.com/iam/)  | Roles, policies, and permissions |
|  **Monitoring & Logging**  |  |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  | Supporting service for metrics, dashboards, alarms, and log management |
|  **Container Services (ECS Architecture)**  |  |
|  [Amazon ECS](https://aws.amazon.com/ecs/)  | Container orchestration for image processor |
|  [Amazon ECR](https://aws.amazon.com/ecr/)  | Container image registry |
|  [Amazon EC2](https://aws.amazon.com/ec2/)  | VPC, subnets, security groups for ECS |
|  **Automation & Events**  |  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  | Event-driven automation |
|  [AWS Application Auto Scaling](https://aws.amazon.com/application-auto-scaling/)  | ECS task auto-scaling |
|  **Security & Encryption**  |  |
|  [AWS KMS](https://aws.amazon.com/kms/)  | Encryption key management |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  | Manages secrets to support URL signatures |
|  **Deployment & Management**  |  |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  | Infrastructure as code |
|  [AWS CDK](https://aws.amazon.com/cdk/)  | Infrastructure definition framework |

**Important**
 **Configuration Delay and Cached Images**
Changes to origins, transformation policies, or mappings may take up to 5 minutes to propagate across all image processing tasks. During this period, some requests may still use the previous configuration. Configuration updates do not automatically refresh cached images. Cached images processed with previous settings will remain available until they expire or are manually invalidated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
