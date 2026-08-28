---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/request-processing-workflow.html
---

# Request processing workflow
<a name="request-processing-workflow"></a>

 **Lambda processing steps:**

1. API Gateway receives image transformation request

1. Request parameters are validated and parsed

1. Lambda function is invoked with transformation parameters

1. Original image is fetched from S3 bucket

1. Sharp library applies transformations (resize, crop, format conversion, etc.)

1. Processed image is returned through API Gateway

1. CloudFront caches the processed image for future requests

 **Supported transformations:** - Resize with various fit options (cover, contain, fill, inside, outside) - Crop with precise coordinates or smart cropping using Amazon Rekognition - Format conversion ("jpg", "jpeg", "heic", "png", "raw", "tiff", "webp", "gif", "avif") - Quality optimization and compression - Rotation and flip operations - Watermarking and overlay effects - Content moderation using Amazon Rekognition

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
