---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/integration-with-aws-lambda.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Integration with AWS Lambda
<a name="integration-with-aws-lambda"></a>

 Amazon API Gateway supports both REST and HTTP types of APIs. An API Gateway API is made up of resources and methods. A resource is a logical entity that an app can access through a resource path (for example, `/tickets`). A method corresponds to an API request that is submitted to an API resource (for example, `GET /tickets`). API Gateway enables you to back each method with a Lambda function, that is, when you call the API through the HTTPS endpoint exposed in API Gateway, API Gateway invokes the Lambda function.

 You can connect API Gateway and Lambda functions using proxy integrations and non-proxy integrations.

## Proxy integrations
<a name="proxy-integrations"></a>

 In a proxy integration, the entire client HTTPS request is sent as-is to the Lambda function. API Gateway passes the entire client request as the event parameter of the Lambda handler function, and the output of the Lambda function is returned directly to the client (including status code, headers, and so forth.).

## Non-proxy integrations
<a name="non-proxy-integrations"></a>

 In a non-proxy integration, you configure how the parameters, headers, and body of the client request are passed to the event parameter of the Lambda handler function. Additionally, you configure how the Lambda output is translated back to the user.

**Note**
 API Gateway can also proxy to additional serverless resources outside AWS Lambda, such as mock integrations (useful for initial application development), and direct proxy to S3 objects.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
