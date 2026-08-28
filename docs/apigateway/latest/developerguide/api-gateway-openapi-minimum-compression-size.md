---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-openapi-minimum-compression-size.html
---

# x-amazon-apigateway-minimum-compression-size
<a name="api-gateway-openapi-minimum-compression-size"></a>

Specifies the minimum compression size for a REST API. To enable compression, specify an integer between 0 and 10485760. To learn more, see [Payload compression for REST APIs in API Gateway](api-gateway-gzip-compression-decompression.md).

## x-amazon-apigateway-minimum-compression-size example
<a name="api-gateway-openapi-minimum-compression-size-example"></a>

The following example specifies a minimum compression size of `5242880` bytes for a REST API.

```
"x-amazon-apigateway-minimum-compression-size": 5242880
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
