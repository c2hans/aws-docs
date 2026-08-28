---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integrations.html
---

# Lambda integrations for REST APIs in API Gateway
<a name="set-up-lambda-integrations"></a>

 You can integrate an API method with a Lambda function using Lambda proxy integration or Lambda non-proxy (custom) integration.

In Lambda proxy integration, the required setup is simple. Set the integration's HTTP method to POST, the integration endpoint URI to the ARN of the Lambda function invocation action of a specific Lambda function, and grant API Gateway permission to call the Lambda function on your behalf.

In Lambda non-proxy integration, in addition to the proxy integration setup steps, you also specify how the incoming request data is mapped to the integration request and how the resulting integration response data is mapped to the method response.

**Topics**
+ [Lambda proxy integrations in API Gateway](set-up-lambda-proxy-integrations.md)
+ [Set up Lambda custom integrations in API Gateway](set-up-lambda-custom-integrations.md)
+ [Set up asynchronous invocation of the backend Lambda function](set-up-lambda-integration-async.md)
+ [Handle Lambda errors in API Gateway](handle-errors-in-lambda-integration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
