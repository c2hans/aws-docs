---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/aws-services.html
---

# AWS services used in this guidance
<a name="aws-services"></a>

| AWS service | Description |
| --- | --- |
| AWS Lambda |  **Core.** Deploys multiple Lambda functions to support four core microservices. |
| AWS Step Functions |  **Core.** Deploys state machine to orchestrate the multiple Lambda functions to scan resource-based policies across multiple accounts and services. The Map state allows the guidance to invoke parallel Lambda functions to scan accounts and services asynchronously. |
| Amazon DynamoDB |  **Core.** Deploys a DynamoDB table for each microservice. Each microservice reads and writes to their specific table. This allows every microservice to own its own data. |
| Amazon API Gateway |  **Core.** Deploys API Gateway and integrates with Lambda functions for each API. The proxy integration allows change in the Lambda function implementation at any time without needing to redeploy your API. |
| Amazon S3 |  **Core.** Deploys Amazon S3 buckets to host the web UI assets. |
| Amazon EventBridge |  **Core.** Starts a policy scan on a daily schedule. |
| Amazon CloudFront |  **Core.** Deploys CloudFront with an Amazon S3 bucket as the origin. This restricts access to the Amazon S3 bucket so that it’s not publicly accessible and prevents direct access from the bucket. |
| Amazon Cognito |  **Supporting.** Deploys Cognito user pool to authenticate and authorize users to access the guidance web UI. |
| AWS WAF |  **Supporting.** Deploys AWS WAF web ACL to protect your API Gateway API from common web exploits, such as SQL injection and cross-site scripting (XSS) attacks. |
| AWS X-Ray |  **Supporting.** Deploys AWS X-Ray to trace API Gateway, Step Functions, and Lambda functions, allowing you to investigate root causes of failed scans. |
