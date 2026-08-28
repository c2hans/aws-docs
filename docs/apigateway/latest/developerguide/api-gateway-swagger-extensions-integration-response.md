---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-response.html
---

# x-amazon-apigateway-integration.response object
<a name="api-gateway-swagger-extensions-integration-response"></a>

 Defines a response and specifies parameter mappings or payload mappings from the integration response to the method response.

| Property name | Type | Description |
| --- | --- | --- |
| statusCode | string | HTTP status code for the method response; for example, `"200"`. This must correspond to a matching response in the [OpenAPI Operation](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#operation-object) `responses` field. |
| responseTemplates | [x-amazon-apigateway-integration.responseTemplates object](api-gateway-swagger-extensions-integration-responseTemplates.md) | Specifies MIME type-specific mapping templates for the response’s payload. |
| responseParameters | [x-amazon-apigateway-integration.responseParameters object](api-gateway-swagger-extensions-integration-responseParameters.md) | Specifies parameter mappings for the response. Only the `header` and `body` parameters of the integration response can be mapped to the `header` parameters of the method.  |
| contentHandling | string | Response payload encoding conversion types. Valid values are 1) CONVERT\_TO\_TEXT, for converting a binary payload into a base64-encoded string or converting a text payload into a utf-8-encoded string or passing through the text payload natively without modification, and 2) CONVERT\_TO\_BINARY, for converting a text payload into a base64-decoded blob or passing through a binary payload natively without modification. |

## `x-amazon-apigateway-integration.response` example
<a name="api-gateway-swagger-extensions-response-example"></a>

The following example defines a `302` response for the method that derives a payload of the `application/json` or `application/xml` MIME type from the backend. The response uses the supplied mapping templates and returns the redirect URL from the integration response in the method's `Location` header.

```
{
    "statusCode" : "302",
    "responseTemplates" : {
         "application/json" : "#set ($root=$input.path('$')) { \"stage\": \"$root.name\", \"user-id\": \"$root.key\" }",
         "application/xml" : "#set ($root=$input.path('$')) <stage>$root.name</stage> "
    },
    "responseParameters" : {
        "method.response.header.Location": "integration.response.body.redirect.url"
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
