---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-request-validators.requestValidator.html
---

# x-amazon-apigateway-request-validators.requestValidator object
<a name="api-gateway-swagger-extensions-request-validators.requestValidator"></a>

 Specifies the validation rules of a request validator as part of the [x-amazon-apigateway-request-validators object](api-gateway-swagger-extensions-request-validators.md) map definition.

| Property name | Type | Description |
| --- | --- | --- |
| `validateRequestBody` | Boolean | Specifies whether to validate the request body (`true`) or not (`false`).  |
| `validateRequestParameters` | Boolean | Specifies whether to validate the required request parameters (`true`) or not (`false`).  |

## `x-amazon-apigateway-request-validators.requestValidator` example
<a name="api-gateway-swagger-extensions-request-validators.requestValidator-example"></a>

 The following example shows a parameter-only request validator:

```
"params-only": {
    "validateRequestBody" : false,
    "validateRequestParameters" : true
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
