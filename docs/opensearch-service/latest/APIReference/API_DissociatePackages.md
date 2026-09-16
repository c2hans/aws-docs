---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DissociatePackages.html
---

# DissociatePackages
<a name="API_DissociatePackages"></a>

Dissociates multiple packages from a domain simultaneously.

## Request Syntax
<a name="API_DissociatePackages_RequestSyntax"></a>

```
POST /2021-01-01/packages/dissociateMultiple HTTP/1.1
Content-type: application/json

{
   "DomainName": "{{string}}",
   "PackageList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DissociatePackages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DissociatePackages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DomainName](#API_DissociatePackages_RequestSyntax) **   <a name="opensearchservice-DissociatePackages-request-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [PackageList](#API_DissociatePackages_RequestSyntax) **   <a name="opensearchservice-DissociatePackages-request-PackageList"></a>
A list of package IDs to be dissociated from a domain.
Type: Array of strings
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

## Response Syntax
<a name="API_DissociatePackages_ResponseSyntax"></a>

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
<a name="API_DissociatePackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainPackageDetailsList](#API_DissociatePackages_ResponseSyntax) **   <a name="opensearchservice-DissociatePackages-response-DomainPackageDetailsList"></a>
A list of package details for the packages that were dissociated from the domain.
Type: Array of [DomainPackageDetails](API_DomainPackageDetails.md) objects

## Errors
<a name="API_DissociatePackages_Errors"></a>

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
<a name="API_DissociatePackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DissociatePackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DissociatePackages)
