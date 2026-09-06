---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/lambda-architecture.html
---

# Lambda Architecture
<a name="lambda-architecture"></a>

This cost-optimized serverless architecture is suitable for most image transformation workloads with images up to 6 MB.

**Important**
This solution is intended for customers with public applications who want to provide an option to dynamically change or manipulate their public images. Because of these public requirements, this template creates a publicly accessible, unauthenticated CloudFront distribution and [Amazon API Gateway](https://aws.amazon.com/api-gateway/) endpoint in your account, allowing anyone to access it. For more information on API Gateway authorization, refer to the [Security](security.md) section. This solution supports signing requests, which can serve to restrict unauthorized requests, for more information, refer to the [Image URL Signature section](lambda-architecture-features.md#image-url-signature).

 **Lambda architecture for cost-optimized image processing**

![Lambda architecture diagram showing CloudFront](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/serverless-image-handler-architecture.png)

**Note**
AWS CloudFormation resources are created from [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) (AWS CDK) constructs.

The high-level process flow for the Lambda architecture is as follows:

1. An [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution provides a caching layer to reduce the cost of image processing and the latency of subsequent image delivery.

1.  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) provides endpoint resources and initiates the [AWS Lambda](https://aws.amazon.com/lambda/) function.

1. A Lambda function retrieves the image from a customer’s existing [Amazon S3](https://aws.amazon.com/s3/) bucket and uses `sharp` to return a modified version of the image to the API Gateway.

1. A solution-created S3 bucket provides log storage, separate from your customer-created S3 bucket for storing images.

1. (Optional) If you enter `Yes` for the **Enable Signature** template parameter, the Lambda function retrieves the secret value from your existing [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) secret to validate the signature.

1. (Optional) If you use the smart crop or content moderation features, the Lambda function calls [Amazon Rekognition](https://aws.amazon.com/rekognition/) to analyze your image and returns the results.

1. The viewer request is proxied through an Amazon CloudFront function to normalize headers and query parameters for improved cache hit rates.
