---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-architecture.html
---

# ECS Architecture
<a name="ecs-architecture"></a>

This high-performance container-based architecture supports images up to 100 MB and includes the solution’s advanced capabilities, including transformation policies, content-aware smart cropping, content moderation, multi-tier device detection, non-S3 origin support, and an administrative interface.

 **ECS architecture for high-performance image processing**

![ECS architecture diagram showing CloudFront](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/serverless-image-handler-alb-ecs-architecture.png)

The high-level process flow for the ECS architecture is as follows:

1. An Amazon CloudFront distribution provides global caching and content delivery.

1. An Amazon CloudFront function processes the viewer request before the cache lookup. It evaluates a multi-tier device-detection chain (responsive image width, viewport Client Hints, CloudFront device headers, and a configurable fallback) and normalizes the result into `dit-*` headers so that requests from all browsers map to the correct cached image variant.

1. An [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (ALB) distributes incoming requests across multiple ECS tasks for high availability and scalability.

1.  [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (ECS) tasks running on [AWS Fargate](https://aws.amazon.com/fargate/) process image transformation requests using containerized applications.

1. ECS tasks maintain in-memory caches of transformation policies and origin mappings for fast request resolution and reduced latency.

1. Images are retrieved from multiple origin types: Amazon S3 buckets or external HTTP-accessible domains based on configured origin mappings.

1. An administrative interface built with [AWS Amplify](https://aws.amazon.com/amplify/) provides policy and origin management capabilities through a secure web interface. It also hosts an interactive Playground for testing transformations.

1.  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) stores transformation policies, origin configurations, and mapping rules with high availability and performance, and caches Amazon Rekognition detection results so repeated transformations of the same source image reuse stored analysis.

1.  [Amazon Cognito](https://aws.amazon.com/cognito/) provides authentication and authorization for the administrative interface. The Playground uses the same Cognito user pool to authorize the extended transformation metrics returned by ECS.

1. (Optional) Amazon Rekognition integration for smart cropping and content moderation features. When a request misses the CloudFront edge cache and reaches ECS, the task first checks the DynamoDB result cache for stored detection results for that source image, and calls Amazon Rekognition only when no cached result is found.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
