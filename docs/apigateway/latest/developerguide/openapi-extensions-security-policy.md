---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-security-policy.html
---

# x-amazon-apigateway-security-policy
<a name="openapi-extensions-security-policy"></a>

Specifies a security policy for a REST API. If you create a security policy that starts with `"SecurityPolicy_"`, you must also set the [endpoint access mode](openapi-extensions-endpoint-access-mode.md). To learn more about security policies, see [Security policies for REST APIs in API Gateway](apigateway-security-policies.md).

## `x-amazon-apigateway-security-policy` example
<a name="openapi-extensions-security-policy-example"></a>

The following example specifies `SecurityPolicy_TLS13_1_3_2025_09` for a REST API.

```
"x-amazon-apigateway-security-policy": "SecurityPolicy_TLS13_1_3_2025_09"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
