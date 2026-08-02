---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListPackagesForDomain.html
---

# ListPackagesForDomain
<a name="API_ListPackagesForDomain"></a>

Lists all packages associated with an Amazon OpenSearch Service domain. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_ListPackagesForDomain_RequestSyntax"></a>

```
GET /2021-01-01/domain/{{DomainName}}/packages?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPackagesForDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_ListPackagesForDomain_RequestSyntax) **   <a name="opensearchservice-ListPackagesForDomain-request-uri-DomainName"></a>
The name of the domain for which you want to list associated packages.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [MaxResults](#API_ListPackagesForDomain_RequestSyntax) **   <a name="opensearchservice-ListPackagesForDomain-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_ListPackagesForDomain_RequestSyntax) **   <a name="opensearchservice-ListPackagesForDomain-request-uri-NextToken"></a>
If your initial `ListPackagesForDomain` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListPackagesForDomain` operations, which returns results in the next page.

## Request Body
<a name="API_ListPackagesForDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPackagesForDomain_ResponseSyntax"></a>

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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListPackagesForDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainPackageDetailsList](#API_ListPackagesForDomain_ResponseSyntax) **   <a name="opensearchservice-ListPackagesForDomain-response-DomainPackageDetailsList"></a>
List of all packages associated with a domain.
Type: Array of [DomainPackageDetails](API_DomainPackageDetails.md) objects

 ** [NextToken](#API_ListPackagesForDomain_ResponseSyntax) **   <a name="opensearchservice-ListPackagesForDomain-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListPackagesForDomain_Errors"></a>

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

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_ListPackagesForDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListPackagesForDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListPackagesForDomain)
