---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.gatewayResponse.html
---

# x-amazon-apigateway-gateway-responses.gatewayResponse object
<a name="api-gateway-swagger-extensions-gateway-responses.gatewayResponse"></a>

Defines a gateway response of a given response type, including the status code, any applicable response parameters, or response templates.

| Property name | Type | Description |
| --- | --- | --- |
| {{responseParameters}} | [x-amazon-apigateway-gateway-responses.responseParameters](api-gateway-swagger-extensions-gateway-responses.responseParameters.md) | Specifies the [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) parameters, namely the header parameters. The parameter values can take any incoming [request parameter](rest-api-parameter-mapping.md) value or a static custom value. |
| {{responseTemplates}} | [x-amazon-apigateway-gateway-responses.responseTemplates](api-gateway-swagger-extensions-gateway-responses.responseTemplates.md) | Specifies the mapping templates of the gateway response. The templates are not processed by the VTL engine. |
| {{statusCode}} | string | An HTTP status code for the gateway response. |

## x-amazon-apigateway-gateway-responses.gatewayResponse example
<a name="api-gateway-swagger-extensions-gateway-responses.gatewayResponse-example"></a>

 The following example of the API Gateway extension to OpenAPI defines a [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) to customize the `INVALID_API_KEY` response to return the status code of `456`, the incoming request's `api-key` header value, and a `"Bad api-key"` message.

```
    "INVALID_API_KEY": {
      "statusCode": "456",
      "responseParameters": {
        "gatewayresponse.header.api-key": "method.request.header.api-key"
      },
      "responseTemplates": {
        "application/json": "{\"message\": \"Bad api-key\" }"
      }
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
