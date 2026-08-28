---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-cors-configuration.html
---

# x-amazon-apigateway-cors object
<a name="api-gateway-swagger-extensions-cors-configuration"></a>

Specifies the cross-origin resource sharing (CORS) configuration for an HTTP API. The extension applies to the root-level OpenAPI structure. To learn more, see [Configure CORS for HTTP APIs in API Gateway](http-api-cors.md).

| Property name | Type | Description |
| --- | --- | --- |
| allowOrigins | Array | Specifies the allowed origins. |
| allowCredentials | Boolean | Specifies whether credentials are included in the CORS request. |
| exposeHeaders | Array | Specifies the headers that are exposed.  |
| maxAge | Integer | Specifies the number of seconds that the browser should cache preflight request results. |
| allowMethods | Array | Specifies the allowed HTTP methods. |
| allowHeaders | Array | Specifies the allowed headers. |

## x-amazon-apigateway-cors example
<a name="api-gateway-swagger-extensions-cors-configuration"></a>

The following is an example CORS configuration for an HTTP API.

```
"x-amazon-apigateway-cors": {
    "allowOrigins": [
      "https://www.example.com"
    ],
    "allowCredentials": true,
    "exposeHeaders": [
      "x-apigateway-header",
      "x-amz-date",
      "content-type"
    ],
    "maxAge": 3600,
    "allowMethods": [
      "GET",
      "OPTIONS",
      "POST"
    ],
    "allowHeaders": [
      "x-apigateway-header",
      "x-amz-date",
      "content-type"
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
