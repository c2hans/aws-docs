---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisionedProduct.html
---

# UpdateProvisionedProduct
<a name="API_UpdateProvisionedProduct"></a>

Requests updates to the configuration of the specified provisioned product.

If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.

You can check the status of this request using [DescribeRecord](API_DescribeRecord.md).

## Request Syntax
<a name="API_UpdateProvisionedProduct_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PathId": "{{string}}",
   "PathName": "{{string}}",
   "ProductId": "{{string}}",
   "ProductName": "{{string}}",
   "ProvisionedProductId": "{{string}}",
   "ProvisionedProductName": "{{string}}",
   "ProvisioningArtifactId": "{{string}}",
   "ProvisioningArtifactName": "{{string}}",
   "ProvisioningParameters": [
      {
         "Key": "{{string}}",
         "UsePreviousValue": {{boolean}},
         "Value": "{{string}}"
      }
   ],
   "ProvisioningPreferences": {
      "StackSetAccounts": [ "{{string}}" ],
      "StackSetFailureToleranceCount": {{number}},
      "StackSetFailureTolerancePercentage": {{number}},
      "StackSetMaxConcurrencyCount": {{number}},
      "StackSetMaxConcurrencyPercentage": {{number}},
      "StackSetOperationType": "{{string}}",
      "StackSetRegions": [ "{{string}}" ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProvisionedProduct_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PathId](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-PathId"></a>
The path identifier. This value is optional if the product has a default path, and required if the product has more than one path. You must provide the name or ID, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [PathName](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-PathName"></a>
The name of the path. You must provide the name or ID, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [ProductId](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProductId"></a>
The identifier of the product. You must provide the name or ID, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProductName](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProductName"></a>
The name of the product. You must provide the name or ID, but not both.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** [ProvisionedProductId](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProvisionedProductId"></a>
The identifier of the provisioned product. You must provide the name or ID, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProvisionedProductName](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProvisionedProductName"></a>
The name of the provisioned product. You cannot specify both `ProvisionedProductName` and `ProvisionedProductId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}|arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [ProvisioningArtifactId](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProvisioningArtifactName](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProvisioningArtifactName"></a>
The name of the provisioning artifact. You must provide the name or ID, but not both.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** [ProvisioningParameters](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProvisioningParameters"></a>
The new parameters.
Type: Array of [UpdateProvisioningParameter](API_UpdateProvisioningParameter.md) objects
Required: No

 ** [ProvisioningPreferences](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-ProvisioningPreferences"></a>
An object that contains information about the provisioning preferences for a stack set.
Type: [UpdateProvisioningPreferences](API_UpdateProvisioningPreferences.md) object
Required: No

 ** [Tags](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-Tags"></a>
One or more tags. Requires the product to have `RESOURCE_UPDATE` constraint with `TagUpdatesOnProvisionedProduct` set to `ALLOWED` to allow tag updates.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** [UpdateToken](#API_UpdateProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-request-UpdateToken"></a>
The idempotency token that uniquely identifies the provisioning update request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

## Response Syntax
<a name="API_UpdateProvisionedProduct_ResponseSyntax"></a>

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
<a name="API_UpdateProvisionedProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecordDetail](#API_UpdateProvisionedProduct_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisionedProduct-response-RecordDetail"></a>
Information about the result of the request.
Type: [RecordDetail](API_RecordDetail.md) object

## Errors
<a name="API_UpdateProvisionedProduct_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProvisionedProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/UpdateProvisionedProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisionedProduct)
