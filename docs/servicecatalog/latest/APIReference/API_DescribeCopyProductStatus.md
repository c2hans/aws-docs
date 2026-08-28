---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeCopyProductStatus.html
---

# DescribeCopyProductStatus
<a name="API_DescribeCopyProductStatus"></a>

Gets the status of the specified copy product operation.

## Request Syntax
<a name="API_DescribeCopyProductStatus_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "CopyProductToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCopyProductStatus_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeCopyProductStatus_RequestSyntax) **   <a name="servicecatalog-DescribeCopyProductStatus-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [CopyProductToken](#API_DescribeCopyProductStatus_RequestSyntax) **   <a name="servicecatalog-DescribeCopyProductStatus-request-CopyProductToken"></a>
The token for the copy product operation. This token is returned by [CopyProduct](API_CopyProduct.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DescribeCopyProductStatus_ResponseSyntax"></a>

```
{
   "CopyProductStatus": "string",
   "StatusDetail": "string",
   "TargetProductId": "string"
}
```

## Response Elements
<a name="API_DescribeCopyProductStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CopyProductStatus](#API_DescribeCopyProductStatus_ResponseSyntax) **   <a name="servicecatalog-DescribeCopyProductStatus-response-CopyProductStatus"></a>
The status of the copy product operation.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED`

 ** [StatusDetail](#API_DescribeCopyProductStatus_ResponseSyntax) **   <a name="servicecatalog-DescribeCopyProductStatus-response-StatusDetail"></a>
The status message.
Type: String

 ** [TargetProductId](#API_DescribeCopyProductStatus_ResponseSyntax) **   <a name="servicecatalog-DescribeCopyProductStatus-response-TargetProductId"></a>
The identifier of the copied product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

## Errors
<a name="API_DescribeCopyProductStatus_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCopyProductStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeCopyProductStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeCopyProductStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
