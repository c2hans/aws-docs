---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CopyProduct.html
---

# CopyProduct
<a name="API_CopyProduct"></a>

Copies the specified source product to the specified target product or a new product.

You can copy a product to the same account or another account. You can copy a product to the same Region or another Region. If you copy a product to another account, you must first share the product in a portfolio using [CreatePortfolioShare](API_CreatePortfolioShare.md).

This operation is performed asynchronously. To track the progress of the operation, use [DescribeCopyProductStatus](API_DescribeCopyProductStatus.md).

## Request Syntax
<a name="API_CopyProduct_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "CopyOptions": [ "{{string}}" ],
   "IdempotencyToken": "{{string}}",
   "SourceProductArn": "{{string}}",
   "SourceProvisioningArtifactIdentifiers": [
      {
         "{{string}}" : "{{string}}"
      }
   ],
   "TargetProductId": "{{string}}",
   "TargetProductName": "{{string}}"
}
```

## Request Parameters
<a name="API_CopyProduct_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_CopyProduct_RequestSyntax) **   <a name="servicecatalog-CopyProduct-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [CopyOptions](#API_CopyProduct_RequestSyntax) **   <a name="servicecatalog-CopyProduct-request-CopyOptions"></a>
The copy options. If the value is `CopyTags`, the tags from the source product are copied to the target product.
Type: Array of strings
Valid Values: `CopyTags`
Required: No

 ** [IdempotencyToken](#API_CopyProduct_RequestSyntax) **   <a name="servicecatalog-CopyProduct-request-IdempotencyToken"></a>
 A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [SourceProductArn](#API_CopyProduct_RequestSyntax) **   <a name="servicecatalog-CopyProduct-request-SourceProductArn"></a>
The Amazon Resource Name (ARN) of the source product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [SourceProvisioningArtifactIdentifiers](#API_CopyProduct_RequestSyntax) **   <a name="servicecatalog-CopyProduct-request-SourceProvisioningArtifactIdentifiers"></a>
The identifiers of the provisioning artifacts (also known as versions) of the product to copy. By default, all provisioning artifacts are copied.
Type: Array of string to string maps
Valid Keys: `Id`
Required: No

 ** [TargetProductId](#API_CopyProduct_RequestSyntax) **   <a name="servicecatalog-CopyProduct-request-TargetProductId"></a>
The identifier of the target product. By default, a new product is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [TargetProductName](#API_CopyProduct_RequestSyntax) **   <a name="servicecatalog-CopyProduct-request-TargetProductName"></a>
A name for the target product. The default is the name of the source product.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

## Response Syntax
<a name="API_CopyProduct_ResponseSyntax"></a>

```
{
   "CopyProductToken": "string"
}
```

## Response Elements
<a name="API_CopyProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CopyProductToken](#API_CopyProduct_ResponseSyntax) **   <a name="servicecatalog-CopyProduct-response-CopyProductToken"></a>
The token to use to track the progress of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

## Errors
<a name="API_CopyProduct_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_CopyProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/CopyProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/CopyProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
