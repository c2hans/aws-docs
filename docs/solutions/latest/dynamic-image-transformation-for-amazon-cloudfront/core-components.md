---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/core-components.html
---

# Core components
<a name="core-components"></a>

 **Amazon API Gateway** - RESTful API endpoint for image transformation requests - Request validation and parameter parsing - Integration with AWS Lambda for processing - Built-in throttling and caching capabilities

 **AWS Lambda** - Serverless compute for image processing using Sharp library - Automatic scaling based on request volume - 6 MB payload limit for requests and responses - Memory allocation from 128 MB to 10,240 MB

 **Amazon CloudFront** - Global content delivery network for caching processed images - Edge locations reduce latency for end users - Custom cache behaviors for different request types - Origin Shield for additional caching layer

 **Amazon S3** - Source image storage with versioning and encryption support - Processed image caching (optional) - Static website hosting for Demo UI - Cross-region replication capabilities
