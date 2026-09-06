---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreateProvisioningArtifact.html
---

# CreateProvisioningArtifact
<a name="API_CreateProvisioningArtifact"></a>

Creates a provisioning artifact (also known as a version) for the specified product.

You cannot create a provisioning artifact for a product that was shared with you.

The user or role that performs this operation must have the `cloudformation:GetTemplate` IAM policy permission. This policy permission is required when using the `ImportFromPhysicalId` template source in the information data section.

## Request Syntax
<a name="API_CreateProvisioningArtifact_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "Parameters": {
      "Description": "{{string}}",
      "DisableTemplateValidation": {{boolean}},
      "Info": {
         "{{string}}" : "{{string}}"
      },
      "Name": "{{string}}",
      "Type": "{{string}}"
   },
   "ProductId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateProvisioningArtifact_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_CreateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-CreateProvisioningArtifact-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IdempotencyToken](#API_CreateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-CreateProvisioningArtifact-request-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [Parameters](#API_CreateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-CreateProvisioningArtifact-request-Parameters"></a>
The configuration for the provisioning artifact.
Type: [ProvisioningArtifactProperties](API_ProvisioningArtifactProperties.md) object
Required: Yes

 ** [ProductId](#API_CreateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-CreateProvisioningArtifact-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_CreateProvisioningArtifact_ResponseSyntax"></a>

```
{
   "Info": {
      "string" : "string"
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
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateProvisioningArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Info](#API_CreateProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-CreateProvisioningArtifact-response-Info"></a>
Specify the template source with one of the following options, but not both. Keys accepted: [ `LoadTemplateFromURL`, `ImportFromPhysicalId` ].
Use the URL of the AWS CloudFormation template in Amazon S3 or GitHub in JSON format.
 `LoadTemplateFromURL`
Use the URL of the AWS CloudFormation template in Amazon S3 or GitHub in JSON format.
 `ImportFromPhysicalId`
Use the physical id of the resource that contains the template; currently supports AWS CloudFormation stack ARN.
Type: String to string map
Map Entries: Maximum number of 100 items.

 ** [ProvisioningArtifactDetail](#API_CreateProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-CreateProvisioningArtifact-response-ProvisioningArtifactDetail"></a>
Information about the provisioning artifact.
Type: [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md) object

 ** [Status](#API_CreateProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-CreateProvisioningArtifact-response-Status"></a>
The status of the current request.
Type: String
Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors
<a name="API_CreateProvisioningArtifact_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## Examples
<a name="API_CreateProvisioningArtifact_Examples"></a>

### To create a provisioning artifact
<a name="API_CreateProvisioningArtifact_Example_1"></a>

The following shows an example JSON request.

#### Sample Request
<a name="API_CreateProvisioningArtifact_Example_1_Request"></a>

```
{
   "AcceptLanguage": "en",
   "ProductId": "prod-mjpjbit3pzuqi",
   "Parameters":
   {
      "Name": "Version-2",
      "Description": "my-test-2",
      "Info":
      {
         "LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..." ,
      },
      "Type": "CLOUD_FORMATION_TEMPLATE"
      "IdempotencyToken": "my-test-token-2"
   }
}
```

## See Also
<a name="API_CreateProvisioningArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/CreateProvisioningArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/CreateProvisioningArtifact)
