---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Represents an API resource.

## Contents
<a name="API_Resource_Contents"></a>

 ** id **   <a name="apigw-Type-Resource-id"></a>
The resource's identifier.
Type: String
Required: No

 ** parentId **   <a name="apigw-Type-Resource-parentId"></a>
The parent resource's identifier.
Type: String
Required: No

 ** path **   <a name="apigw-Type-Resource-path"></a>
The full path for this resource.
Type: String
Required: No

 ** pathPart **   <a name="apigw-Type-Resource-pathPart"></a>
The last path segment for this resource.
Type: String
Required: No

 ** resourceMethods **   <a name="apigw-Type-Resource-resourceMethods"></a>
Gets an API resource's method of a given HTTP verb.
Type: String to [Method](API_Method.md) object map
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
