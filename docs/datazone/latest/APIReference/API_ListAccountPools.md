---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListAccountPools.html
---

# ListAccountPools
<a name="API_ListAccountPools"></a>

Lists existing account pools.

## Request Syntax
<a name="API_ListAccountPools_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/account-pools?maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAccountPools_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListAccountPools_RequestSyntax) **   <a name="datazone-ListAccountPools-request-uri-domainIdentifier"></a>
The ID of the domain where exsting account pools are to be listed.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListAccountPools_RequestSyntax) **   <a name="datazone-ListAccountPools-request-uri-maxResults"></a>
The maximum number of account pools to return in a single call to ListAccountPools. When the number of account pools to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountPools to list the next set of account pools.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [name](#API_ListAccountPools_RequestSyntax) **   <a name="datazone-ListAccountPools-request-uri-name"></a>
The name of the account pool to be listed.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [nextToken](#API_ListAccountPools_RequestSyntax) **   <a name="datazone-ListAccountPools-request-uri-nextToken"></a>
When the number of account pools is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of account pools, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountPools to list the next set of account pools.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [sortBy](#API_ListAccountPools_RequestSyntax) **   <a name="datazone-ListAccountPools-request-uri-sortBy"></a>
The sort by mechanism in which the existing account pools are to be listed.
Valid Values: `NAME`

 ** [sortOrder](#API_ListAccountPools_RequestSyntax) **   <a name="datazone-ListAccountPools-request-uri-sortOrder"></a>
The sort order in which the existing account pools are to be listed.
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_ListAccountPools_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccountPools_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdBy": "string",
         "domainId": "string",
         "domainUnitId": "string",
         "id": "string",
         "name": "string",
         "resolutionStrategy": "string",
         "updatedBy": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccountPools_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAccountPools_ResponseSyntax) **   <a name="datazone-ListAccountPools-response-items"></a>
The results of the ListAccountPools operation.
Type: Array of [AccountPoolSummary](API_AccountPoolSummary.md) objects

 ** [nextToken](#API_ListAccountPools_ResponseSyntax) **   <a name="datazone-ListAccountPools-response-nextToken"></a>
When the number of account pools is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of account pools, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountPools to list the next set of account pools.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListAccountPools_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListAccountPools_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListAccountPools)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListAccountPools)
