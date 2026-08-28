---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-http-integrations.html
---

# Choose an HTTP integration tutorial
<a name="getting-started-http-integrations"></a>

 To build an API with HTTP integration, you can use either an HTTP proxy integration or an HTTP custom integration.

In an HTTP proxy integration, you only need to set the HTTP method and the HTTP endpoint URI, according to the backend requirements. We recommend that you use the HTTP proxy integration, whenever possible, to take advantage of the streamlined API set up.

You might want to use an HTTP custom integration if you need to transform client request data for the backend or transform the backend response data for the client.

**Topics**
+ [Tutorial: Create a REST API with an HTTP proxy integration](api-gateway-create-api-as-simple-proxy-for-http.md)
+ [Tutorial: Create a REST API with an HTTP non-proxy integration](api-gateway-create-api-step-by-step.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
