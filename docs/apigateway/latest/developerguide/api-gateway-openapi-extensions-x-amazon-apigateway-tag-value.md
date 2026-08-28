---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-openapi-extensions-x-amazon-apigateway-tag-value.html
---

# x-amazon-apigateway-tag-value property
<a name="api-gateway-openapi-extensions-x-amazon-apigateway-tag-value"></a>

Specifies the value of an [AWS tag](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) for an HTTP API. You can use the `x-amazon-apigateway-tag-value` property as part of the root-level [OpenAPI tag object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#tag-object) to specify AWS tags for an HTTP API. If you specify a tag name without the `x-amazon-apigateway-tag-value` property, API Gateway creates a tag with an empty string for a value.

To learn more about tagging, see [Tagging your API Gateway resources](apigateway-tagging.md).

| Property name | Type | Description |
| --- | --- | --- |
| `name` | String | Specifies the tag key. |
| `x-amazon-apigateway-tag-value` | String | Specifies the tag value. |

## `x-amazon-apigateway-tag-value` example
<a name="api-gateway-openapi-extensions-x-amazon-apigateway-tag-value-example"></a>

 The following example specifies two tags for an HTTP API:
+ "Owner": "Admin"
+ "Prod": ""

```
"tags": [
    {
      "name": "Owner",
      "x-amazon-apigateway-tag-value": "Admin"
    },
    {
      "name": "Prod"
    }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
