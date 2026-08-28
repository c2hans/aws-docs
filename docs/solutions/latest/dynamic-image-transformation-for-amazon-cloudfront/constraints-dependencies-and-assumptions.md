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

 **Dependencies**
+ Sharp Node.js library for image processing
+ Thumbor compatibility layer for legacy support

 **Assumptions**
+ Source images in supported formats (JPEG, PNG, WebP, AVIF, TIFF, GIF)
+ ECS architecture: Configuration changes may take up to 5 minutes to propagate
+ Cached images remain until expiration or manual invalidation
+ Lambda architecture: Standard AWS Lambda concurrency limits (1000 default)
+ CloudFront caching improves performance for repeated requests

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
