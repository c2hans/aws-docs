---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AssociatePackages.html
---

# AssociatePackages
<a name="API_AssociatePackages"></a>

Operation in the Amazon OpenSearch Service API for associating multiple packages with a domain simultaneously.

## Request Syntax
<a name="API_AssociatePackages_RequestSyntax"></a>

```
POST /2021-01-01/packages/associateMultiple HTTP/1.1
Content-type: application/json

{
   "DomainName": "{{string}}",
   "PackageList": [
      {
         "AssociationConfiguration": {
            "KeyStoreAccessOption": {
               "KeyAccessRoleArn": "{{string}}",
               "KeyStoreAccessEnabled": {{boolean}}
            }
         },
         "PackageID": "{{string}}",
         "PrerequisitePackageIDList": [ "{{string}}" ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_AssociatePackages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociatePackages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DomainName](#API_AssociatePackages_RequestSyntax) **   <a name="opensearchservice-AssociatePackages-request-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [PackageList](#API_AssociatePackages_RequestSyntax) **   <a name="opensearchservice-AssociatePackages-request-PackageList"></a>
A list of packages and their prerequisites to be associated with a domain.
Type: Array of [PackageDetailsForAssociation](API_PackageDetailsForAssociation.md) objects
Required: Yes

## Response Syntax
<a name="API_AssociatePackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainPackageDetailsList": [
      {
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
   ]
}
```

## Response Elements
<a name="API_AssociatePackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainPackageDetailsList](#API_AssociatePackages_ResponseSyntax) **   <a name="opensearchservice-AssociatePackages-response-DomainPackageDetailsList"></a>
List of information about packages that are associated with a domain.
Type: Array of [DomainPackageDetails](API_DomainPackageDetails.md) objects

## Errors
<a name="API_AssociatePackages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
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
<a name="API_AssociatePackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AssociatePackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AssociatePackages)
