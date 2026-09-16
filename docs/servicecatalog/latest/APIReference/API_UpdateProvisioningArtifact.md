---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisioningArtifact.html
---

# UpdateProvisioningArtifact
<a name="API_UpdateProvisioningArtifact"></a>

Updates the specified provisioning artifact (also known as a version) for the specified product.

You cannot update a provisioning artifact for a product that was shared with you.

## Request Syntax
<a name="API_UpdateProvisioningArtifact_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Active": {{boolean}},
   "Description": "{{string}}",
   "Guidance": "{{string}}",
   "Name": "{{string}}",
   "ProductId": "{{string}}",
   "ProvisioningArtifactId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProvisioningArtifact_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_UpdateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Active](#API_UpdateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-request-Active"></a>
Indicates whether the product version is active.
Inactive provisioning artifacts are invisible to end users. End users cannot launch or update a provisioned product from an inactive provisioning artifact.
Type: Boolean
Required: No

 ** [Description](#API_UpdateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-request-Description"></a>
The updated description of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** [Guidance](#API_UpdateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-request-Guidance"></a>
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.
The `DEFAULT` value indicates that the product version is active.
The administrator can set the guidance to `DEPRECATED` to inform users that the product version is deprecated. Users are able to make updates to a provisioned product of a deprecated version but cannot launch new provisioned products using a deprecated version.
Type: String
Valid Values: `DEFAULT | DEPRECATED`
Required: No

 ** [Name](#API_UpdateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-request-Name"></a>
The updated name of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** [ProductId](#API_UpdateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ProvisioningArtifactId](#API_UpdateProvisioningArtifact_RequestSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-request-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_UpdateProvisioningArtifact_ResponseSyntax"></a>

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
<a name="API_UpdateProvisioningArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Info](#API_UpdateProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-response-Info"></a>
The URL of the AWS CloudFormation template in Amazon S3 or GitHub in JSON format.
Type: String to string map
Map Entries: Maximum number of 100 items.

 ** [ProvisioningArtifactDetail](#API_UpdateProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-response-ProvisioningArtifactDetail"></a>
Information about the provisioning artifact.
Type: [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md) object

 ** [Status](#API_UpdateProvisioningArtifact_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisioningArtifact-response-Status"></a>
The status of the current request.
Type: String
Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors
<a name="API_UpdateProvisioningArtifact_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProvisioningArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact)
