---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-auth.html
---

# x-amazon-apigateway-auth object
<a name="api-gateway-swagger-extensions-auth"></a>

Defines an authorization type to be applied for authorization of method invocations in API Gateway.

| Property name | Type | Description |
| --- | --- | --- |
| type | string | Specifies the authorization type. Specify "NONE" for open access. Specify "AWS\_IAM" to use IAM permissions. Values are case insensitive. |

## x-amazon-apigateway-auth example
<a name="api-gateway-swagger-extensions-auth-example"></a>

The following example sets the authorization type for an API method.

------
#### [ OpenAPI 3.0.1 ]

```
{
  "openapi": "3.0.1",
  "info": {
    "title": "openapi3",
    "version": "1.0"
  },
  "paths": {
    "/protected-by-iam": {
      "get": {
        "x-amazon-apigateway-auth": {
          "type": "AWS_IAM"
        }
      }
    }
  }
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
