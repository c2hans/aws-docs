---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-payload-encodings-import-and-export.html
---

# Import and export content encodings for API Gateway
<a name="api-gateway-payload-encodings-import-and-export"></a>

 To import the `binaryMediaTypes` list on a [RestApi](https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html), use the following API Gateway extension to the API's OpenAPI definition file. The extension is also used to export the API settings.
+ [x-amazon-apigateway-binary-media-types property](api-gateway-swagger-extensions-binary-media-types.md)

To import and export the `contentHandling` property value on an `Integration` or `IntegrationResponse` resource, use the following API Gateway extensions to the OpenAPI definitions:
+ [x-amazon-apigateway-integration object](api-gateway-swagger-extensions-integration.md)
+ [x-amazon-apigateway-integration.response object](api-gateway-swagger-extensions-integration-response.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
