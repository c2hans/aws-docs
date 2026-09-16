---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_TerminateProvisionedProduct.html
---

# TerminateProvisionedProduct
<a name="API_TerminateProvisionedProduct"></a>

Terminates the specified provisioned product.

This operation does not delete any records associated with the provisioned product.

You can check the status of this request using [DescribeRecord](API_DescribeRecord.md).

## Request Syntax
<a name="API_TerminateProvisionedProduct_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "IgnoreErrors": {{boolean}},
   "ProvisionedProductId": "{{string}}",
   "ProvisionedProductName": "{{string}}",
   "RetainPhysicalResources": {{boolean}},
   "TerminateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_TerminateProvisionedProduct_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_TerminateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-TerminateProvisionedProduct-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IgnoreErrors](#API_TerminateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-TerminateProvisionedProduct-request-IgnoreErrors"></a>
If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.
Type: Boolean
Required: No

 ** [ProvisionedProductId](#API_TerminateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-TerminateProvisionedProduct-request-ProvisionedProductId"></a>
The identifier of the provisioned product. You cannot specify both `ProvisionedProductName` and `ProvisionedProductId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProvisionedProductName](#API_TerminateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-TerminateProvisionedProduct-request-ProvisionedProductName"></a>
The name of the provisioned product. You cannot specify both `ProvisionedProductName` and `ProvisionedProductId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}|arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [RetainPhysicalResources](#API_TerminateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-TerminateProvisionedProduct-request-RetainPhysicalResources"></a>
When this boolean parameter is set to true, the `TerminateProvisionedProduct` API deletes the AWS Service Catalog provisioned product. However, it does not remove the AWS CloudFormation stack, stack set, or the underlying resources of the deleted provisioned product. The default value is false.
Type: Boolean
Required: No

 ** [TerminateToken](#API_TerminateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-TerminateProvisionedProduct-request-TerminateToken"></a>
An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return **ResourceNotFound**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

## Response Syntax
<a name="API_TerminateProvisionedProduct_ResponseSyntax"></a>

```
{
   "RecordDetail": {
      "CreatedTime": number,
      "LaunchRoleArn": "string",
      "PathId": "string",
      "ProductId": "string",
      "ProvisionedProductId": "string",
      "ProvisionedProductName": "string",
      "ProvisionedProductType": "string",
      "ProvisioningArtifactId": "string",
      "RecordErrors": [
         {
            "Code": "string",
            "Description": "string"
         }
      ],
      "RecordId": "string",
      "RecordTags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "RecordType": "string",
      "Status": "string",
      "UpdatedTime": number
   }
}
```

## Response Elements
<a name="API_TerminateProvisionedProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecordDetail](#API_TerminateProvisionedProduct_ResponseSyntax) **   <a name="servicecatalog-TerminateProvisionedProduct-response-RecordDetail"></a>
Information about the result of this request.
Type: [RecordDetail](API_RecordDetail.md) object

## Errors
<a name="API_TerminateProvisionedProduct_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_TerminateProvisionedProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/TerminateProvisionedProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/TerminateProvisionedProduct)
