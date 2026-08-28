---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-extensions-importexport-version.html
---

# x-amazon-apigateway-importexport-version
<a name="api-gateway-extensions-importexport-version"></a>

Specifies the version of the API Gateway import and export algorithm for HTTP APIs. Currently, the only supported value is `1.0`. To learn more, see [exportVersion](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-exports-specification.html#w125aab9c10b3b1b4) in the *API Gateway Version 2 API Reference*.

## x-amazon-apigateway-importexport-version example
<a name="api-gateway-extensions-importexport-version-example"></a>

The following example sets the import and export version to `1.0`.

```
{
    "openapi": "3.0.1",
    "x-amazon-apigateway-importexport-version": "1.0",
    "info": { ...
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
