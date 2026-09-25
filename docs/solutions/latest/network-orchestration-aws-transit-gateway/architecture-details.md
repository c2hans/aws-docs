---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this Guidance and the architecture details on how these components work together.

## AWS services in this Guidance
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)  |  **Core.** Deploys a transit gateway that connects VPCs through a central hub. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** Deploys multiple Lambda functions to support core microservices and create transit gateway attachments. |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  **Core.** Deploys a state machine to orchestrate the subnet and VPC tagging events and create transit gateway attachments. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core.** Deploys a DynamoDB table for VPC and transit gateway attachments, and for transit gateway peering attachments. |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Core.** Deploys an event bus and event rules to connect the deployed components. |
|  [AWS X-Ray](https://aws.amazon.com/xray/)  |  **Supporting.** Deploys traces for API Gateway and Step Functions, allowing you to investigate root causes of failures. |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  **Optional.** Deploys a topic that sends an email notification with the optional web UI URL. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Optional.** Deploys a user pool that supports identity authentication for the optional web UI. |
|  [AWS AppSync](https://aws.amazon.com/appsync/)  |  **Optional.** Deploys AWS AppSync schema and resolvers for the DynamoDB table and Lambda functions. Using resolvers, AWS AppSync translates GraphQL requests and fetches information from DynamoDB. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Optional.** Deploys Amazon S3 buckets to host the web UI assets. |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Optional.** Deploys AWS WAF web access control list (ACL) to protect AWS AppSync from common security events, such as SQL injection and cross-site scripting (XSS). |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Optional.** Deploys CloudFront with an Amazon S3 bucket as the origin. This restricts access to the Amazon S3 bucket so that it’s not publicly accessible and prevents direct access from the bucket. |
