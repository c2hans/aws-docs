---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListAccountsInAccountPool.html
---

# ListAccountsInAccountPool
<a name="API_ListAccountsInAccountPool"></a>

Lists the accounts in the specified account pool.

## Request Syntax
<a name="API_ListAccountsInAccountPool_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/account-pools/{{identifier}}/accounts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAccountsInAccountPool_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListAccountsInAccountPool_RequestSyntax) **   <a name="datazone-ListAccountsInAccountPool-request-uri-domainIdentifier"></a>
The ID of the domain in which the accounts in the specified account pool are to be listed.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_ListAccountsInAccountPool_RequestSyntax) **   <a name="datazone-ListAccountsInAccountPool-request-uri-identifier"></a>
The ID of the account pool whose accounts are to be listed.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListAccountsInAccountPool_RequestSyntax) **   <a name="datazone-ListAccountsInAccountPool-request-uri-maxResults"></a>
The maximum number of accounts to return in a single call to ListAccountsInAccountPool. When the number of accounts to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListAccountsInAccountPool_RequestSyntax) **   <a name="datazone-ListAccountsInAccountPool-request-uri-nextToken"></a>
When the number of accounts is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of accounts, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListAccountsInAccountPool_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAccountsInAccountPool_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "awsAccountId": "string",
         "awsAccountName": "string",
         "supportedRegions": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccountsInAccountPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAccountsInAccountPool_ResponseSyntax) **   <a name="datazone-ListAccountsInAccountPool-response-items"></a>
The results of the ListAccountsInAccountPool operation.
Type: Array of [AccountInfo](API_AccountInfo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.

 ** [nextToken](#API_ListAccountsInAccountPool_ResponseSyntax) **   <a name="datazone-ListAccountsInAccountPool-response-nextToken"></a>
When the number of accounts is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of accounts, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListAccountsInAccountPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

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
<a name="API_ListAccountsInAccountPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListAccountsInAccountPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListAccountsInAccountPool)
