---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/aws-services-used-for-lambda-architecture.html
---

# AWS services used for Lambda architecture
<a name="aws-services-used-for-lambda-architecture"></a>

| AWS service | Description |
| --- | --- |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core.** Provides a caching layer to reduce latency and the cost of image processing for subsequent identical requests. Allows pre/post processing of requests and responses. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** Runs functions to retrieve, modify, and invoke other services to analyze images. Also runs a function to support URL signature validation. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core.** Stores images, logs, and a demo UI. |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  **Supporting.** Provides API endpoints to invoke Lambda functions. Only used if EnableS3ObjectLambda is set to "No". |
|  [Amazon S3 Object Lambda](https://aws.amazon.com/s3/features/object-lambda/)  | This option has been deprecated. Amazon S3 Object Lambda will no longer be open to new customers starting on November 7, 2025. If you were not an existing user of S3 Object Lambda before November 7, 2025, select 'No". For more information, please visit https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html.<br /> **Supporting.** Provide S3 Origin to invoke Lambda functions. Only used if EnableS3ObjectLambda is set to "Yes". |
|  [AWS CDK](https://aws.amazon.com/cdk/)  |  **Supporting.** Provides infrastructure as code constructs to generate the solution’s underlying CloudFormation templates. |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Supporting.** Deploys the solution’s underlying AWS resources. |
|  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)  |  **Supporting.** Allows for fine-grained access permissions. |
|  [Amazon Rekognition](https://aws.amazon.com/rekognition/)  |  **Optional.** Uses machine learning (ML) to analyze images. |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  **Optional.** Manages secrets to support URL signatures. |
