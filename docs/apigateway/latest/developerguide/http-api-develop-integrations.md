---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html
---

# Create integrations for HTTP APIs in API Gateway
<a name="http-api-develop-integrations"></a>

*Integrations* connect a route to backend resources. HTTP APIs support Lambda proxy, AWS service, and HTTP proxy integrations. For example, you can configure a `POST` request to the `/signup` route of your API to integrate with a Lambda function that handles signing up customers.

**Topics**
+ [Create AWS Lambda proxy integrations for HTTP APIs in API Gateway](http-api-develop-integrations-lambda.md)
+ [Create HTTP proxy integrations for HTTP APIs](http-api-develop-integrations-http.md)
+ [Create AWS service integrations for HTTP APIs in API Gateway](http-api-develop-integrations-aws-services.md)
+ [Create private integrations for HTTP APIs in API Gateway](http-api-develop-integrations-private.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
