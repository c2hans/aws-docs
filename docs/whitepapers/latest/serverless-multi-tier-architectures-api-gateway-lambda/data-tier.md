---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/data-tier.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data tier
<a name="data-tier"></a>

 Using AWS Lambda as your logic tier does not limit the data storage options available in your data tier. Lambda functions connect to any data storage option by including the appropriate database driver in the Lambda deployment package, and use IAM role-based access or encrypted credentials (through AWS KMS or AWS Secrets Manager).

 Choosing a data store for your application is highly dependent on your application requirements. AWS offers a number of serverless and non-serverless data stores that you can use to compose the data tier of your application.
