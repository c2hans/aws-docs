---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AssociatePackage.html
---

# AssociatePackage
<a name="API_AssociatePackage"></a>

Associates a package with an Amazon OpenSearch Service domain. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_AssociatePackage_RequestSyntax"></a>

```
POST /2021-01-01/packages/associate/{{PackageID}}/{{DomainName}} HTTP/1.1
Content-type: application/json

{
   "AssociationConfiguration": {
      "KeyStoreAccessOption": {
         "KeyAccessRoleArn": "{{string}}",
         "KeyStoreAccessEnabled": {{boolean}}
      }
   },
   "PrerequisitePackageIDList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_AssociatePackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_AssociatePackage_RequestSyntax) **   <a name="opensearchservice-AssociatePackage-request-uri-DomainName"></a>
Name of the domain to associate the package with.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [PackageID](#API_AssociatePackage_RequestSyntax) **   <a name="opensearchservice-AssociatePackage-request-uri-PackageID"></a>
Internal ID of the package to associate with a domain. Use `DescribePackages` to find this value.
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

## Request Body
<a name="API_AssociatePackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssociationConfiguration](#API_AssociatePackage_RequestSyntax) **   <a name="opensearchservice-AssociatePackage-request-AssociationConfiguration"></a>
The configuration for associating a package with an Amazon OpenSearch Service domain.
Type: [PackageAssociationConfiguration](API_PackageAssociationConfiguration.md) object
Required: No

 ** [PrerequisitePackageIDList](#API_AssociatePackage_RequestSyntax) **   <a name="opensearchservice-AssociatePackage-request-PrerequisitePackageIDList"></a>
A list of package IDs that must be associated with the domain before the package specified in the request can be associated.
Type: Array of strings
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: No

## Response Syntax
<a name="API_AssociatePackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainPackageDetails": {
      "AssociationConfiguration": {
         "KeyStoreAccessOption": {
            "KeyAccessRoleArn": "string",
            "KeyStoreAccessEnabled": boolean
         }
      },
      "DomainName": "string",
      "DomainPackageStatus": "string",
      "ErrorDetails": {
         "ErrorMessage": "string",
         "ErrorType": "string"
      },
      "LastUpdated": number,
      "PackageID": "string",
      "PackageName": "string",
      "PackageType": "string",
      "PackageVersion": "string",
      "PrerequisitePackageIDList": [ "string" ],
      "ReferencePath": "string"
   }
}
```

## Response Elements
<a name="API_AssociatePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainPackageDetails](#API_AssociatePackage_ResponseSyntax) **   <a name="opensearchservice-AssociatePackage-response-DomainPackageDetails"></a>
Information about a package that is associated with a domain.
Type: [DomainPackageDetails](API_DomainPackageDetails.md) object

## Errors
<a name="API_AssociatePackage_Errors"></a>

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
<a name="API_AssociatePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AssociatePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AssociatePackage)
