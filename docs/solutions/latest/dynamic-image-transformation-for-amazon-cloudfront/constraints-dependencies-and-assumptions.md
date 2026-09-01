---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/constraints-dependencies-and-assumptions.html
---

# Constraints, dependencies, and assumptions
<a name="constraints-dependencies-and-assumptions"></a>

 **Constraints**
+ Lambda architecture: Supports transformation for images up to 6MB
+ ECS architecture: Supports transformation for images up to 100MB
+ Maximum 100 transformations per policy
+ ECS architecture: Auto-scaling based on CPU utilization
+ ECS architecture (v8.1\+): Amazon Rekognition service limits apply. `DetectFaces` returns up to 100 faces per image, `DetectLabels` up to 1000 labels, and `DetectText` up to 100 text detections. Custom Labels detection requires a customer-managed model that is running; a stopped model returns `ResourceNotReadyException`.

 **Dependencies**
+ Sharp Node.js library for image processing
+ Thumbor compatibility layer for legacy support
+ ECS architecture (v8.1\+): Amazon Rekognition for smart cropping and content moderation detection APIs
+ ECS architecture (v8.1\+): aws-jwt-verify library for application-level Cognito access token verification (extended metrics)

 **Assumptions**
+ Source images in supported formats (JPEG, PNG, WebP, AVIF, TIFF, GIF)
+ ECS architecture: Configuration changes may take up to 5 minutes to propagate
+ Cached images remain until expiration or manual invalidation
+ Lambda architecture: Standard AWS Lambda concurrency limits (1000 default)
+ CloudFront caching improves performance for repeated requests
+ ECS architecture (v8.1\+): Amazon Rekognition default TPS limits apply per API per account (5 TPS in most Regions; 50 TPS in US East (N. Virginia), US West (Oregon), and Europe (Ireland)). CloudFront caching is the primary mechanism for staying within these limits.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
