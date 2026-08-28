---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-gateway-responses.responseTemplates.html
---

# x-amazon-apigateway-gateway-responses.responseTemplates object
<a name="api-gateway-swagger-extensions-gateway-responses.responseTemplates"></a>

Defines [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) mapping templates, as a string-to-string map of key-value pairs, for a given gateway response. For each key-value pair, the key is the content type. For example, "application/json" and the value is a stringified mapping template for simple variable substitutions. A `GatewayResponse` mapping template isn't processed by the [Velocity Template Language (VTL)](https://velocity.apache.org/engine/devel/vtl-reference.html) engine.

| Property name | Type | Description |
| --- | --- | --- |
| {{content-type}} | string | A `GatewayResponse` body mapping template supporting only simple variable substitution to customize a gateway response body. |

## x-amazon-apigateway-gateway-responses.responseTemplates example
<a name="api-gateway-swagger-extensions-gateway-responses.responseTemplates-example"></a>

 The following OpenAPI extensions example shows a [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) mapping template to customize an API Gateway–generated error response into an app-specific format.

```
      "responseTemplates": {
        "application/json": "{ \"message\": $context.error.messageString, \"type\":$context.error.responseType, \"statusCode\": '488' }"
      }
```

 The following OpenAPI extensions example shows a [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html) mapping template to override an API Gateway–generated error response with a static error message.

```
      "responseTemplates": {
        "application/json": "{ \"message\": 'API-specific errors' }"
      }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
