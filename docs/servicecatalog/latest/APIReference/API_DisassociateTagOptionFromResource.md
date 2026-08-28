---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DisassociateTagOptionFromResource.html
---

# DisassociateTagOptionFromResource
<a name="API_DisassociateTagOptionFromResource"></a>

Disassociates the specified TagOption from the specified resource.

## Request Syntax
<a name="API_DisassociateTagOptionFromResource_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "TagOptionId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateTagOptionFromResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceId](#API_DisassociateTagOptionFromResource_RequestSyntax) **   <a name="servicecatalog-DisassociateTagOptionFromResource-request-ResourceId"></a>
The resource identifier.
Type: String
Required: Yes

 ** [TagOptionId](#API_DisassociateTagOptionFromResource_RequestSyntax) **   <a name="servicecatalog-DisassociateTagOptionFromResource-request-TagOptionId"></a>
The TagOption identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Elements
<a name="API_DisassociateTagOptionFromResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateTagOptionFromResource_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** TagOptionNotMigratedException **
An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the AWS Management Console to perform the migration process before retrying the operation.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateTagOptionFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateTagOptionFromResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
