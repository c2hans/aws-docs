---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/request-processing-workflow-2.html
---

# Request processing workflow
<a name="request-processing-workflow-2"></a>

 **Request resolution**

1. Incoming requests are analyzed to determine origin mapping

1. Host-header mappings take precedence over path-based mappings

1. Request resolver identifies the appropriate origin and transformation policy

1. Headers and authentication parameters are prepared for origin requests

 **Transformation resolution**

1. Policy resolver retrieves transformation policies from in-memory cache

1. Conditional logic evaluates client hints and request headers

1. Explicit query parameters override policy-defined transformations

1. Final transformation parameters are validated and normalized

 **Image processing**

1. Original image is fetched from the resolved origin (S3 or external)

1. Sharp library applies transformations in the specified order

1. Output format and quality are optimized based on client capabilities

1. Processed image is returned through the ALB to CloudFront
