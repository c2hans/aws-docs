---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/lambda-security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Lambda security
<a name="lambda-security"></a>

 To run a Lambda function, it must be invoked by an event or service that is permitted by an [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) policy. Using IAM policies, you can create a Lambda function that cannot be initiated at all unless it is invoked by an API Gateway resource that you define. Such policy can be defined using resource-based policy across various AWS services.

 Each Lambda function assumes an IAM role that is assigned when the Lambda function is deployed. This IAM role defines the other AWS services and resources your Lambda function can interact with (for example, Amazon DynamoDB Amazon S3). In context of Lambda function, this is called an [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html).

 Do not store sensitive information inside a Lambda function. IAM handles access to AWS services through the Lambda execution role; if you need to access other credentials (for example, database credentials and API Keys) from inside your Lambda function, you can use [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) with environment variables, or use a service such as [AWS](https://aws.amazon.com/secrets-manager/) Secrets Manager to keep this information safe when not in use.
