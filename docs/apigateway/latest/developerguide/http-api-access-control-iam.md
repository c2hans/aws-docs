---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html
---

# Control access to HTTP APIs with IAM authorization in API Gateway
<a name="http-api-access-control-iam"></a>

You can enable IAM authorization for HTTP API routes. When IAM authorization is enabled, clients must use [Signature Version 4 (SigV4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) to sign their requests with AWS credentials. API Gateway invokes your API route only if the client has `execute-api` permission for the route.

IAM authorization for HTTP APIs is similar to that for [REST APIs](api-gateway-control-access-using-iam-policies-to-invoke-api.md).

**Note**
Resource policies aren't currently supported for HTTP APIs.

For examples of IAM policies that grant clients the permission to invoke APIs, see [Control access for invoking an API](api-gateway-control-access-using-iam-policies-to-invoke-api.md).

## Enable IAM authorization for a route
<a name="http-api-access-control-iam-example"></a>

The following [update-route](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/update-route.html) command enables IAM authorization for an HTTP API route:

```
aws apigatewayv2 update-route \
    --api-id {{abc123}} \
    --route-id {{abcdef}} \
    --authorization-type AWS_IAM
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
