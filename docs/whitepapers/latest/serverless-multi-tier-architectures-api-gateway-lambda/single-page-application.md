---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/single-page-application.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Single-page application
<a name="single-page-application"></a>

![Architecture diagram showing client authentication flow through API Gateway, Lambda functions, and AWS services.](http://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/images/single-page-application.png)

* Architectural pattern for serverless single-page application *

* Table 2 - Single-page application components *

|  Tier  |  Components  |
| --- | --- |
|  Presentation  |  Static website content hosted in Amazon S3, distributed by CloudFront. <br /> AWS Certificate Manager allows a custom SSL/TLS certificate to be used.  |
|  Logic  |  API Gateway with AWS Lambda. <br /> This architecture shows three exposed services (`/tickets`, `/shows`, and `/info`). API Gateway endpoints are secured by a Lambda authorizer. In this method, users sign in through a third-party identity provider and obtain access and ID tokens. These tokens are included in API Gateway calls, and the Lambda authorizer validates these tokens and generates an IAM policy containing API initiation permissions. <br /> Each Lambda function is assigned its own IAM role to provide access to the appropriate data source.  |
|  Data  |  Amazon DynamoDB is used for the `/tickets` and `/shows` services. <br /> Amazon ElastiCache is used by the `/shows` service to improve database performance. Cache misses are sent to DynamoDB. <br /> Amazon S3 is used to host static content used by the `/info service`.  |
