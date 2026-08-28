---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.responseParameters.html
---

# x-amazon-apigateway-gateway-responses.responseParameters object
<a name="api-gateway-swagger-extensions-gateway-responses.responseParameters"></a>

Defines a string-to-string map of key-value pairs to generate gateway response parameters from the incoming request parameters or using literal strings. Supported only for REST APIs.

| Property name | Type | Description |
| --- | --- | --- |
| gatewayresponse.{{param-position}}.{{param-name}} | string | `{{param-position}}` can be `header`, `path`, or `querystring`. For more information, see [Parameter mapping for REST APIs in API Gateway](rest-api-parameter-mapping.md). |

## x-amazon-apigateway-gateway-responses.responseParameters example
<a name="api-gateway-swagger-extensions-gateway-responses.responseParameters-example"></a>

 The following OpenAPI extensions example shows a [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) response parameter mapping expression to enable CORS support for resources on the `*.example.domain` domains.

```
      "responseParameters": {
        "gatewayresponse.header.Access-Control-Allow-Origin": '*.example.domain',
        "gatewayresponse.header.from-request-header" : method.request.header.Accept,
        "gatewayresponse.header.from-request-path" : method.request.path.petId,
        "gatewayresponse.header.from-request-query" : method.request.querystring.qname
      }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
