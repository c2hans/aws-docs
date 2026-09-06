---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdatePackage.html
---

# UpdatePackage
<a name="API_UpdatePackage"></a>

Updates a package for use with Amazon OpenSearch Service domains. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_UpdatePackage_RequestSyntax"></a>

```
POST /2021-01-01/packages/update HTTP/1.1
Content-type: application/json

{
   "CommitMessage": "{{string}}",
   "PackageConfiguration": {
      "ConfigurationRequirement": "{{string}}",
      "LicenseFilepath": "{{string}}",
      "LicenseRequirement": "{{string}}",
      "RequiresRestartForConfigurationUpdate": {{boolean}}
   },
   "PackageDescription": "{{string}}",
   "PackageEncryptionOptions": {
      "EncryptionEnabled": {{boolean}},
      "KmsKeyIdentifier": "{{string}}"
   },
   "PackageID": "{{string}}",
   "PackageSource": {
      "S3BucketName": "{{string}}",
      "S3Key": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdatePackage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CommitMessage](#API_UpdatePackage_RequestSyntax) **   <a name="opensearchservice-UpdatePackage-request-CommitMessage"></a>
Commit message for the updated file, which is shown as part of `GetPackageVersionHistoryResponse`.
Type: String
Length Constraints: Maximum length of 160.
Required: No

 ** [PackageConfiguration](#API_UpdatePackage_RequestSyntax) **   <a name="opensearchservice-UpdatePackage-request-PackageConfiguration"></a>
The updated configuration details for a package.
Type: [PackageConfiguration](API_PackageConfiguration.md) object
Required: No

 ** [PackageDescription](#API_UpdatePackage_RequestSyntax) **   <a name="opensearchservice-UpdatePackage-request-PackageDescription"></a>
A new description of the package.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [PackageEncryptionOptions](#API_UpdatePackage_RequestSyntax) **   <a name="opensearchservice-UpdatePackage-request-PackageEncryptionOptions"></a>
Encryption options for a package.
Type: [PackageEncryptionOptions](API_PackageEncryptionOptions.md) object
Required: No

 ** [PackageID](#API_UpdatePackage_RequestSyntax) **   <a name="opensearchservice-UpdatePackage-request-PackageID"></a>
The unique identifier for the package.
Type: String
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

 ** [PackageSource](#API_UpdatePackage_RequestSyntax) **   <a name="opensearchservice-UpdatePackage-request-PackageSource"></a>
Amazon S3 bucket and key for the package.
Type: [PackageSource](API_PackageSource.md) object
Required: Yes

## Response Syntax
<a name="API_UpdatePackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PackageDetails": {
      "AllowListedUserList": [ "string" ],
      "AvailablePackageConfiguration": {
         "ConfigurationRequirement": "string",
         "LicenseFilepath": "string",
         "LicenseRequirement": "string",
         "RequiresRestartForConfigurationUpdate": boolean
      },
      "AvailablePackageVersion": "string",
      "AvailablePluginProperties": {
         "ClassName": "string",
         "Description": "string",
         "Name": "string",
         "UncompressedSizeInBytes": number,
         "Version": "string"
      },
      "CreatedAt": number,
      "EngineVersion": "string",
      "ErrorDetails": {
         "ErrorMessage": "string",
         "ErrorType": "string"
      },
      "LastUpdatedAt": number,
      "PackageDescription": "string",
      "PackageEncryptionOptions": {
         "EncryptionEnabled": boolean,
         "KmsKeyIdentifier": "string"
      },
      "PackageID": "string",
      "PackageName": "string",
      "PackageOwner": "string",
      "PackageStatus": "string",
      "PackageType": "string",
      "PackageVendingOptions": {
         "VendingEnabled": boolean
      }
   }
}
```

## Response Elements
<a name="API_UpdatePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PackageDetails](#API_UpdatePackage_ResponseSyntax) **   <a name="opensearchservice-UpdatePackage-response-PackageDetails"></a>
Information about a package.
Type: [PackageDetails](API_PackageDetails.md) object

## Errors
<a name="API_UpdatePackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdatePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdatePackage)
