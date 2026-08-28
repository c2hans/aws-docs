---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreatePackage.html
---

# CreatePackage
<a name="API_CreatePackage"></a>

Creates a package for use with Amazon OpenSearch Service domains. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_CreatePackage_RequestSyntax"></a>

```
POST /2021-01-01/packages HTTP/1.1
Content-type: application/json

{
   "EngineVersion": "{{string}}",
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
   "PackageName": "{{string}}",
   "PackageSource": {
      "S3BucketName": "{{string}}",
      "S3Key": "{{string}}"
   },
   "PackageType": "{{string}}",
   "PackageVendingOptions": {
      "VendingEnabled": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_CreatePackage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EngineVersion](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-EngineVersion"></a>
The version of the Amazon OpenSearch Service engine for which is compatible with the package. This can only be specified for package type `ZIP-PLUGIN`
Type: String
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: No

 ** [PackageConfiguration](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-PackageConfiguration"></a>
 The configuration parameters for the package being created.
Type: [PackageConfiguration](API_PackageConfiguration.md) object
Required: No

 ** [PackageDescription](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-PackageDescription"></a>
Description of the package.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [PackageEncryptionOptions](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-PackageEncryptionOptions"></a>
The encryption parameters for the package being created.
Type: [PackageEncryptionOptions](API_PackageEncryptionOptions.md) object
Required: No

 ** [PackageName](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-PackageName"></a>
Unique name for the package.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [PackageSource](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-PackageSource"></a>
The Amazon S3 location from which to import the package.
Type: [PackageSource](API_PackageSource.md) object
Required: Yes

 ** [PackageType](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-PackageType"></a>
The type of package.
Type: String
Valid Values: `TXT-DICTIONARY | ZIP-PLUGIN | PACKAGE-LICENSE | PACKAGE-CONFIG`
Required: Yes

 ** [PackageVendingOptions](#API_CreatePackage_RequestSyntax) **   <a name="opensearchservice-CreatePackage-request-PackageVendingOptions"></a>
 The vending options for the package being created. They determine if the package can be vended to other users.
Type: [PackageVendingOptions](API_PackageVendingOptions.md) object
Required: No

## Response Syntax
<a name="API_CreatePackage_ResponseSyntax"></a>

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
<a name="API_CreatePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PackageDetails](#API_CreatePackage_ResponseSyntax) **   <a name="opensearchservice-CreatePackage-response-PackageDetails"></a>
Basic information about an OpenSearch Service package.
Type: [PackageDetails](API_PackageDetails.md) object

## Errors
<a name="API_CreatePackage_Errors"></a>

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

 ** InvalidTypeException **
An exception for trying to create or access a sub-resource that's either invalid or not supported.
HTTP Status Code: 409

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceAlreadyExistsException **
An exception for creating a resource that already exists.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_CreatePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CreatePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CreatePackage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
