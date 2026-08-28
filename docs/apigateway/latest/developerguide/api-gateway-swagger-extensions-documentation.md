---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-documentation.html
---

# x-amazon-apigateway-documentation object
<a name="api-gateway-swagger-extensions-documentation"></a>

Defines the documentation parts to be imported into API Gateway. This object is a JSON object containing an array of the `DocumentationPart` instances.

| Property name | Type | Description |
| --- | --- | --- |
| documentationParts | Array |  An array of the exported or imported `DocumentationPart` instances. |
| version | String |  The version identifier of the snapshot of the exported documentation parts. |

## x-amazon-apigateway-documentation example
<a name="api-gateway-swagger-extensions-documentation-example"></a>

 The following example of the API Gateway extension to OpenAPI defines `DocumentationParts` instances to be imported to or exported from an API in API Gateway.

```
{ ...
  "x-amazon-apigateway-documentation": {
    "version": "1.0.3",
    "documentationParts": [
       {
         "location": {
           "type": "API"
       },
        "properties": {
          "description": "API description",
          "info": {
            "description": "API info description 4",
            "version": "API info version 3"
          }
        }
      },
      {
         … // Another DocumentationPart instance
      }
    ]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
