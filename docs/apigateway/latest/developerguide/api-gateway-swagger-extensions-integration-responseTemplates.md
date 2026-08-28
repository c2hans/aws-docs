---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responseTemplates.html
---

# x-amazon-apigateway-integration.responseTemplates object
<a name="api-gateway-swagger-extensions-integration-responseTemplates"></a>

 Specifies mapping templates for a response payload of the specified MIME types.

| Property name | Type | Description |
| --- | --- | --- |
| {{MIME type}} | string | Specifies a mapping template to transform the integration response body to the method response body for a given MIME type. For information about creating a mapping template, see [Mapping template transformations for REST APIs in API Gateway](models-mappings.md). An example of the {{MIME type}} is `application/json`.  |

## x-amazon-apigateway-integration.responseTemplate example
<a name="api-gateway-swagger-extensions-response-template-example"></a>

 The following example sets mapping templates for a request payload of the `application/json` and `application/xml` MIME types.

```
"responseTemplates" : {
    "application/json" : "#set ($root=$input.path('$')) { \"stage\": \"$root.name\", \"user-id\": \"$root.key\" }",
    "application/xml" : "#set ($root=$input.path('$')) <stage>$root.name</stage> "
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
