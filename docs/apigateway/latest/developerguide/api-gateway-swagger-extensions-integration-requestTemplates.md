---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestTemplates.html
---

# x-amazon-apigateway-integration.requestTemplates object
<a name="api-gateway-swagger-extensions-integration-requestTemplates"></a>

 Specifies mapping templates for a request payload of the specified MIME types.

| Property name | Type | Description |
| --- | --- | --- |
| {{MIME type}} | string |  An example of the MIME type is `application/json`. For information about creating a mapping template, see [Mapping template transformations for REST APIs in API Gateway](models-mappings.md).  |

## x-amazon-apigateway-integration.requestTemplates example
<a name="api-gateway-swagger-extensions-request-template-example"></a>

 The following example sets mapping templates for a request payload of the `application/json` and `application/xml` MIME types.

```
"requestTemplates" : {
    "application/json" : "#set ($root=$input.path('$')) { \"stage\": \"$root.name\", \"user-id\": \"$root.key\" }",
    "application/xml" : "#set ($root=$input.path('$')) <stage>$root.name</stage> "
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
