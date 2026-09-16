---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProductView.html
---

# DescribeProductView
<a name="API_DescribeProductView"></a>

Gets information about the specified product.

## Request Syntax
<a name="API_DescribeProductView_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProductView_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeProductView_RequestSyntax) **   <a name="servicecatalog-DescribeProductView-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribeProductView_RequestSyntax) **   <a name="servicecatalog-DescribeProductView-request-Id"></a>
The product view identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DescribeProductView_ResponseSyntax"></a>

```
{
   "ProductViewSummary": {
      "Distributor": "string",
      "HasDefaultPath": boolean,
      "Id": "string",
      "Name": "string",
      "Owner": "string",
      "ProductId": "string",
      "ShortDescription": "string",
      "SupportDescription": "string",
      "SupportEmail": "string",
      "SupportUrl": "string",
      "Type": "string"
   },
   "ProvisioningArtifacts": [
      {
         "CreatedTime": number,
         "Description": "string",
         "Guidance": "string",
         "Id": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeProductView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProductViewSummary](#API_DescribeProductView_ResponseSyntax) **   <a name="servicecatalog-DescribeProductView-response-ProductViewSummary"></a>
Summary information about the product.
Type: [ProductViewSummary](API_ProductViewSummary.md) object

 ** [ProvisioningArtifacts](#API_DescribeProductView_ResponseSyntax) **   <a name="servicecatalog-DescribeProductView-response-ProvisioningArtifacts"></a>
Information about the provisioning artifacts for the product.
Type: Array of [ProvisioningArtifact](API_ProvisioningArtifact.md) objects

## Errors
<a name="API_DescribeProductView_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProductView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeProductView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProductView)
