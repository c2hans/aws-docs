---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SearchSessions.html
---

# SearchSessions
<a name="API_amazon-q-connect_SearchSessions"></a>

Searches for sessions.

## Request Syntax
<a name="API_amazon-q-connect_SearchSessions_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/searchSessions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "searchExpression": {
      "filters": [
         {
            "field": "{{string}}",
            "operator": "{{string}}",
            "value": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_SearchSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_SearchSessions_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchSessions-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_SearchSessions_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchSessions-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_SearchSessions_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchSessions-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_amazon-q-connect_SearchSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [searchExpression](#API_amazon-q-connect_SearchSessions_RequestSyntax) **   <a name="connect-amazon-q-connect_SearchSessions-request-searchExpression"></a>
The search expression to filter results.
Type: [SearchExpression](API_amazon-q-connect_SearchExpression.md) object
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_SearchSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sessionSummaries": [
      {
         "assistantArn": "string",
         "assistantId": "string",
         "sessionArn": "string",
         "sessionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_amazon-q-connect_SearchSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_amazon-q-connect_SearchSessions_ResponseSyntax) **   <a name="connect-amazon-q-connect_SearchSessions-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [sessionSummaries](#API_amazon-q-connect_SearchSessions_ResponseSyntax) **   <a name="connect-amazon-q-connect_SearchSessions-response-sessionSummaries"></a>
Summary information about the sessions.
Type: Array of [SessionSummary](API_amazon-q-connect_SessionSummary.md) objects

## Errors
<a name="API_amazon-q-connect_SearchSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_SearchSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/SearchSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SearchSessions)
