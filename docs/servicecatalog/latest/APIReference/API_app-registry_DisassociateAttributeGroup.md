---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_DisassociateAttributeGroup.html
---

# DisassociateAttributeGroup
<a name="API_app-registry_DisassociateAttributeGroup"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application's metadata. This operation reverts `AssociateAttributeGroup`.

## Request Syntax
<a name="API_app-registry_DisassociateAttributeGroup_RequestSyntax"></a>

```
DELETE /applications/{{application}}/attribute-groups/{{attributeGroup}} HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_DisassociateAttributeGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_DisassociateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_DisassociateAttributeGroup-request-uri-application"></a>
 The name, ID, or ARN of the application.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

 ** [attributeGroup](#API_app-registry_DisassociateAttributeGroup_RequestSyntax) **   <a name="servicecatalog-app-registry_DisassociateAttributeGroup-request-uri-attributeGroup"></a>
 The name, ID, or ARN of the attribute group that holds the attributes to describe the application.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+)`
Required: Yes

## Request Body
<a name="API_app-registry_DisassociateAttributeGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_DisassociateAttributeGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "attributeGroupArn": "string"
}
```

## Response Elements
<a name="API_app-registry_DisassociateAttributeGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_app-registry_DisassociateAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_DisassociateAttributeGroup-response-applicationArn"></a>
The Amazon resource name (ARN) that specifies the application.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

 ** [attributeGroupArn](#API_app-registry_DisassociateAttributeGroup_ResponseSyntax) **   <a name="servicecatalog-app-registry_DisassociateAttributeGroup-response-attributeGroupArn"></a>
The Amazon resource name (ARN) that specifies the attribute group.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/attribute-groups/[-.\w]+`

## Errors
<a name="API_app-registry_DisassociateAttributeGroup_Errors"></a>

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_DisassociateAttributeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DisassociateAttributeGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
