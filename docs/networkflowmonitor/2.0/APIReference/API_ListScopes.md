---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListScopes.html
---

# ListScopes
<a name="API_ListScopes"></a>

List all the scopes for an account.

## Request Syntax
<a name="API_ListScopes_RequestSyntax"></a>

```
GET /scopes?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListScopes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListScopes_RequestSyntax) **   <a name="networkflowmonitor-ListScopes-request-uri-maxResults"></a>
The number of query results that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListScopes_RequestSyntax) **   <a name="networkflowmonitor-ListScopes-request-uri-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.

## Request Body
<a name="API_ListScopes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListScopes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "scopes": [
      {
         "scopeArn": "string",
         "scopeId": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListScopes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListScopes_ResponseSyntax) **   <a name="networkflowmonitor-ListScopes-response-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String

 ** [scopes](#API_ListScopes_ResponseSyntax) **   <a name="networkflowmonitor-ListScopes-response-scopes"></a>
The scopes returned by the call.
Type: Array of [ScopeSummary](API_ScopeSummary.md) objects

## Errors
<a name="API_ListScopes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_ListScopes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/ListScopes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/ListScopes)
