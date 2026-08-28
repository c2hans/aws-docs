---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html
---

# API Gateway HTTP APIs
<a name="http-api"></a>

REST APIs and HTTP APIs are both RESTful API products. REST APIs support more features than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price. For more information, see [Choose between REST APIs and HTTP APIs](http-api-vs-rest.md).

You can use HTTP APIs to send requests to AWS Lambda functions or to any routable HTTP endpoint. For example, you can create an HTTP API that integrates with a Lambda function on the backend. When a client calls your API, API Gateway sends the request to the Lambda function and returns the function's response to the client.

HTTP APIs support [OpenID Connect](https://openid.net/developers/how-connect-works/) and [OAuth 2.0](https://oauth.net/2/) authorization. They come with built-in support for cross-origin resource sharing (CORS) and automatic deployments.

You can create HTTP APIs by using the AWS Management Console, the AWS CLI, APIs, CloudFormation, or SDKs.

**Topics**
+ [Develop HTTP APIs in API Gateway](http-api-develop.md)
+ [Publish HTTP APIs for customers to invoke](http-api-publish.md)
+ [Protect your HTTP APIs in API Gateway](http-api-protect.md)
+ [Monitor HTTP APIs in API Gateway](http-api-monitor.md)
+ [Troubleshooting issues with HTTP APIs in API Gateway](http-api-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
