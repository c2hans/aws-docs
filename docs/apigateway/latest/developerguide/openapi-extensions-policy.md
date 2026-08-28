---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-policy.html
---

# x-amazon-apigateway-policy
<a name="openapi-extensions-policy"></a>

Specifies a resource policy for a REST API. To learn more about resource policies, see [Control access to a REST API with API Gateway resource policies](apigateway-resource-policies.md). For resource policy examples, see [API Gateway resource policy examples](apigateway-resource-policies-examples.md).

## `x-amazon-apigateway-policy` example
<a name="openapi-extensions-policy-example"></a>

The following example specifies a resource policy for a REST API. The resource policy denies (blocks) incoming traffic to an API from a specified source IP address block. On import, `"execute-api:/*"` is converted to `arn:aws:execute-api:{{region}}:{{account-id}}:{{api-id}}/*`, using the current Region, your AWS account ID, and the current REST API ID.

```
"x-amazon-apigateway-policy": {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": [
                "execute-api:/*"
            ]
        },
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": [
               "execute-api:/*"
            ],
            "Condition" : {
                "IpAddress": {
                    "aws:SourceIp": "{{192.0.2.0/24}}"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
