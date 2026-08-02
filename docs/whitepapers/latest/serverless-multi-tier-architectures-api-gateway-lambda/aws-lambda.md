---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/aws-lambda.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Lambda
<a name="aws-lambda"></a>

 AWS Lambda is a compute service that enables you to run arbitrary code functions without provisioning, managing, or scaling servers. Supported languages include Python, Ruby, Java, Go, and .NET. Lambda functions are run in a managed, isolated container, and are launched in response to an event which can be one of several programmatic triggers that AWS makes available, called an *event source.* For more information on supported languages and event sources, refer to [Lambda FAQs](https://aws.amazon.com/lambda/faqs/).

 Many popular use cases for Lambda revolve around event-driven data processing workflows, such as processing files stored in [Amazon S3](https://aws.amazon.com/s3/) or streaming data records from [Amazon Kinesis](https://aws.amazon.com/kinesis/). When used in conjunction with Amazon API Gateway, a Lambda function performs the functionality of a typical web service: it initiates code in response to a client HTTPS request; API Gateway acts as the front door for your logic tier, and AWS Lambda invokes the application code.
