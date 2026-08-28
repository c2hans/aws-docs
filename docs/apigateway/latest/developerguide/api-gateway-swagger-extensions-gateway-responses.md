---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.html
---

# x-amazon-apigateway-gateway-responses object
<a name="api-gateway-swagger-extensions-gateway-responses"></a>

Defines the gateway responses for an API as a string-to-[GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) map of key-value pairs. The extension applies to the root-level OpenAPI structure.

| Property name | Type | Description |
| --- | --- | --- |
| {{responseType}} | [x-amazon-apigateway-gateway-responses.gatewayResponse](api-gateway-swagger-extensions-gateway-responses.gatewayResponse.md) | A `GatewayResponse` for the specified {{responseType}}. |

## x-amazon-apigateway-gateway-responses example
<a name="api-gateway-swagger-extensions-gateway-responses-example"></a>

 The following API Gateway extension to OpenAPI example defines a [GatewayResponses](https://docs.aws.amazon.com/apigateway/latest/api/API_GetGatewayResponses.html) map that contains two [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) instances—one for the `DEFAULT_4XX` type and another for the `INVALID_API_KEY` type.

```
{
  "x-amazon-apigateway-gateway-responses": {
    "DEFAULT_4XX": {
      "responseParameters": {
        "gatewayresponse.header.Access-Control-Allow-Origin": "'domain.com'"
      },
      "responseTemplates": {
        "application/json": "{\"message\": test 4xx b }"
      }
    },
    "INVALID_API_KEY": {
      "statusCode": "429",
      "responseTemplates": {
        "application/json": "{\"message\": test forbidden }"
      }
    }
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
