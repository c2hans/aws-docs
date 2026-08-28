---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPartLocation.html
---

# DocumentationPartLocation
<a name="API_DocumentationPartLocation"></a>

Specifies the target API entity to which the documentation applies.

## Contents
<a name="API_DocumentationPartLocation_Contents"></a>

 ** type **   <a name="apigw-Type-DocumentationPartLocation-type"></a>
The type of API entity to which the documentation content applies. Valid values are `API`, `AUTHORIZER`, `MODEL`, `RESOURCE`, `METHOD`, `PATH_PARAMETER`, `QUERY_PARAMETER`, `REQUEST_HEADER`, `REQUEST_BODY`, `RESPONSE`, `RESPONSE_HEADER`, and `RESPONSE_BODY`. Content inheritance does not apply to any entity of the `API`, `AUTHORIZER`, `METHOD`, `MODEL`, `REQUEST_BODY`, or `RESOURCE` type.
Type: String
Valid Values: `API | AUTHORIZER | MODEL | RESOURCE | METHOD | PATH_PARAMETER | QUERY_PARAMETER | REQUEST_HEADER | REQUEST_BODY | RESPONSE | RESPONSE_HEADER | RESPONSE_BODY`
Required: Yes

 ** method **   <a name="apigw-Type-DocumentationPartLocation-method"></a>
The HTTP verb of a method. It is a valid field for the API entity types of `METHOD`, `PATH_PARAMETER`, `QUERY_PARAMETER`, `REQUEST_HEADER`, `REQUEST_BODY`, `RESPONSE`, `RESPONSE_HEADER`, and `RESPONSE_BODY`. The default value is `*` for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other `location` attributes, the child entity's `method` attribute must match that of the parent entity exactly.
Type: String
Required: No

 ** name **   <a name="apigw-Type-DocumentationPartLocation-name"></a>
The name of the targeted API entity. It is a valid and required field for the API entity types of `AUTHORIZER`, `MODEL`, `PATH_PARAMETER`, `QUERY_PARAMETER`, `REQUEST_HEADER`, `REQUEST_BODY` and `RESPONSE_HEADER`. It is an invalid field for any other entity type.
Type: String
Required: No

 ** path **   <a name="apigw-Type-DocumentationPartLocation-path"></a>
The URL path of the target. It is a valid field for the API entity types of `RESOURCE`, `METHOD`, `PATH_PARAMETER`, `QUERY_PARAMETER`, `REQUEST_HEADER`, `REQUEST_BODY`, `RESPONSE`, `RESPONSE_HEADER`, and `RESPONSE_BODY`. The default value is `/` for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other `location` attributes, the child entity's `path` attribute must match that of the parent entity as a prefix.
Type: String
Required: No

 ** statusCode **   <a name="apigw-Type-DocumentationPartLocation-statusCode"></a>
The HTTP status code of a response. It is a valid field for the API entity types of `RESPONSE`, `RESPONSE_HEADER`, and `RESPONSE_BODY`. The default value is `*` for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other `location` attributes, the child entity's `statusCode` attribute must match that of the parent entity exactly.
Type: String
Pattern: `^([1-5]\d\d|\*|\s*)$`
Required: No

## See Also
<a name="API_DocumentationPartLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/DocumentationPartLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/DocumentationPartLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/DocumentationPartLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
