---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateProduct.html
---

# CreateProduct
<a name="API_CreateProduct"></a>

Creates a product.

A delegated admin is authorized to invoke this command.

The user or role that performs this operation must have the `cloudformation:GetTemplate` IAM policy permission. This policy permission is required when using the `ImportFromPhysicalId` template source in the information data section.

## Request Syntax
<a name="API_CreateProduct_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Description": "{{string}}",
   "Distributor": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "Name": "{{string}}",
   "Owner": "{{string}}",
   "ProductType": "{{string}}",
   "ProvisioningArtifactParameters": {
      "Description": "{{string}}",
      "DisableTemplateValidation": {{boolean}},
      "Info": {
         "{{string}}" : "{{string}}"
      },
      "Name": "{{string}}",
      "Type": "{{string}}"
   },
   "SourceConnection": {
      "ConnectionParameters": {
         "CodeStar": {
            "ArtifactPath": "{{string}}",
            "Branch": "{{string}}",
            "ConnectionArn": "{{string}}",
            "Repository": "{{string}}"
         }
      },
      "Type": "{{string}}"
   },
   "SupportDescription": "{{string}}",
   "SupportEmail": "{{string}}",
   "SupportUrl": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateProduct_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Description](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-Description"></a>
The description of the product.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** [Distributor](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-Distributor"></a>
The distributor of the product.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** [IdempotencyToken](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [Name](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-Name"></a>
The name of the product.
Type: String
Length Constraints: Maximum length of 8191.
Required: Yes

 ** [Owner](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-Owner"></a>
The owner of the product.
Type: String
Length Constraints: Maximum length of 8191.
Required: Yes

 ** [ProductType](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-ProductType"></a>
The type of product.
Type: String
Length Constraints: Maximum length of 8191.
Valid Values: `CLOUD_FORMATION_TEMPLATE | MARKETPLACE | TERRAFORM_OPEN_SOURCE | EXTERNAL | TERRAFORM_CLOUD`
Required: Yes

 ** [ProvisioningArtifactParameters](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-ProvisioningArtifactParameters"></a>
The configuration of the provisioning artifact.
Type: [ProvisioningArtifactProperties](API_ProvisioningArtifactProperties.md) object
Required: No

 ** [SourceConnection](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-SourceConnection"></a>
Specifies connection details for the created product and syncs the product to the connection source artifact. This automatically manages the product's artifacts based on changes to the source. The `SourceConnection` parameter consists of the following sub-fields.
+  `Type`
+  `ConnectionParamters`
Type: [SourceConnection](API_SourceConnection.md) object
Required: No

 ** [SupportDescription](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-SupportDescription"></a>
The support information about the product.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** [SupportEmail](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-SupportEmail"></a>
The contact email for product support.
Type: String
Length Constraints: Maximum length of 254.
Required: No

 ** [SupportUrl](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-SupportUrl"></a>
The contact URL for product support.
 `^https?:\/\// `/ is the pattern used to validate SupportUrl.
Type: String
Length Constraints: Maximum length of 2083.
Required: No

 ** [Tags](#API_CreateProduct_RequestSyntax) **   <a name="servicecatalog-CreateProduct-request-Tags"></a>
One or more tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 20 items.
Required: No

## Response Syntax
<a name="API_CreateProduct_ResponseSyntax"></a>

```
{
   "ProductViewDetail": {
      "CreatedTime": number,
      "ProductARN": "string",
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
      "SourceConnection": {
         "ConnectionParameters": {
            "CodeStar": {
               "ArtifactPath": "string",
               "Branch": "string",
               "ConnectionArn": "string",
               "Repository": "string"
            }
         },
         "LastSync": {
            "LastSuccessfulSyncProvisioningArtifactId": "string",
            "LastSuccessfulSyncTime": number,
            "LastSyncStatus": "string",
            "LastSyncStatusMessage": "string",
            "LastSyncTime": number
         },
         "Type": "string"
      },
      "Status": "string"
   },
   "ProvisioningArtifactDetail": {
      "Active": boolean,
      "CreatedTime": number,
      "Description": "string",
      "Guidance": "string",
      "Id": "string",
      "Name": "string",
      "SourceRevision": "string",
      "Type": "string"
   },
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProductViewDetail](#API_CreateProduct_ResponseSyntax) **   <a name="servicecatalog-CreateProduct-response-ProductViewDetail"></a>
Information about the product view.
Type: [ProductViewDetail](API_ProductViewDetail.md) object

 ** [ProvisioningArtifactDetail](#API_CreateProduct_ResponseSyntax) **   <a name="servicecatalog-CreateProduct-response-ProvisioningArtifactDetail"></a>
Information about the provisioning artifact.
Type: [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md) object

 ** [Tags](#API_CreateProduct_ResponseSyntax) **   <a name="servicecatalog-CreateProduct-response-Tags"></a>
Information about the tags associated with the product.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_CreateProduct_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** TagOptionNotMigratedException **
An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the AWS Management Console to perform the migration process before retrying the operation.
HTTP Status Code: 400

## See Also
<a name="API_CreateProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/CreateProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/CreateProduct)
