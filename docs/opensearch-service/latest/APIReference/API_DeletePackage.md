---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeletePackage.html
---

# DeletePackage
<a name="API_DeletePackage"></a>

Deletes an Amazon OpenSearch Service package. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_DeletePackage_RequestSyntax"></a>

```
DELETE /2021-01-01/packages/{{PackageID}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PackageID](#API_DeletePackage_RequestSyntax) **   <a name="opensearchservice-DeletePackage-request-uri-PackageID"></a>
The internal ID of the package you want to delete. Use `DescribePackages` to find this value.
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

## Request Body
<a name="API_DeletePackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePackage_ResponseSyntax"></a>

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
<a name="API_DeletePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PackageDetails](#API_DeletePackage_ResponseSyntax) **   <a name="opensearchservice-DeletePackage-response-PackageDetails"></a>
 Information about the deleted package.
Type: [PackageDetails](API_PackageDetails.md) object

## Errors
<a name="API_DeletePackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DeletePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DeletePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DeletePackage)
