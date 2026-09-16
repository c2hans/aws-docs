---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainsForPackage.html
---

# ListDomainsForPackage
<a name="API_ListDomainsForPackage"></a>

Lists all Amazon OpenSearch Service domains associated with a given package. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Request Syntax
<a name="API_ListDomainsForPackage_RequestSyntax"></a>

```
GET /2021-01-01/packages/{{PackageID}}/domains?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomainsForPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListDomainsForPackage_RequestSyntax) **   <a name="opensearchservice-ListDomainsForPackage-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_ListDomainsForPackage_RequestSyntax) **   <a name="opensearchservice-ListDomainsForPackage-request-uri-NextToken"></a>
If your initial `ListDomainsForPackage` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListDomainsForPackage` operations, which returns results in the next page.

 ** [PackageID](#API_ListDomainsForPackage_RequestSyntax) **   <a name="opensearchservice-ListDomainsForPackage-request-uri-PackageID"></a>
The unique identifier of the package for which to list associated domains.
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

## Request Body
<a name="API_ListDomainsForPackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomainsForPackage_ResponseSyntax"></a>

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
<a name="API_ListDomainsForPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainPackageDetailsList](#API_ListDomainsForPackage_ResponseSyntax) **   <a name="opensearchservice-ListDomainsForPackage-response-DomainPackageDetailsList"></a>
Information about all domains associated with a package.
Type: Array of [DomainPackageDetails](API_DomainPackageDetails.md) objects

 ** [NextToken](#API_ListDomainsForPackage_ResponseSyntax) **   <a name="opensearchservice-ListDomainsForPackage-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListDomainsForPackage_Errors"></a>

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
<a name="API_ListDomainsForPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListDomainsForPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListDomainsForPackage)
