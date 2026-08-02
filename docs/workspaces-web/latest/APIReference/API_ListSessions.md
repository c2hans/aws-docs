---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_ListSessions.html
---

# ListSessions
<a name="API_ListSessions"></a>

Lists information for multiple secure browser sessions from a specific portal.

## Request Syntax
<a name="API_ListSessions_RequestSyntax"></a>

```
GET /portals/{{portalId}}/sessions?maxResults={{maxResults}}&nextToken={{nextToken}}&sessionId={{sessionId}}&sortBy={{sortBy}}&status={{status}}&username={{username}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSessions_RequestSyntax) **   <a name="workspacesweb-ListSessions-request-uri-maxResults"></a>
The maximum number of results to be included in the next page.
Valid Range: Minimum value of 1.

 ** [nextToken](#API_ListSessions_RequestSyntax) **   <a name="workspacesweb-ListSessions-request-uri-nextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [portalId](#API_ListSessions_RequestSyntax) **   <a name="workspacesweb-ListSessions-request-uri-portalId"></a>
The ID of the web portal for the sessions.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

 ** [sessionId](#API_ListSessions_RequestSyntax) **   <a name="workspacesweb-ListSessions-request-uri-sessionId"></a>
The ID of the session.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9\-]+`

 ** [sortBy](#API_ListSessions_RequestSyntax) **   <a name="workspacesweb-ListSessions-request-uri-sortBy"></a>
The method in which the returned sessions should be sorted.
Valid Values: `StartTimeAscending | StartTimeDescending`

 ** [status](#API_ListSessions_RequestSyntax) **   <a name="workspacesweb-ListSessions-request-uri-status"></a>
The status of the session.
Valid Values: `Active | Terminated`

 ** [username](#API_ListSessions_RequestSyntax) **   <a name="workspacesweb-ListSessions-request-uri-username"></a>
The username of the session.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`

## Request Body
<a name="API_ListSessions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sessions": [
      {
         "endTime": number,
         "portalArn": "string",
         "sessionId": "string",
         "startTime": number,
         "status": "string",
         "username": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSessions_ResponseSyntax) **   <a name="workspacesweb-ListSessions-response-nextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [sessions](#API_ListSessions_ResponseSyntax) **   <a name="workspacesweb-ListSessions-response-sessions"></a>
The sessions in a list.
Type: Array of [SessionSummary](API_SessionSummary.md) objects

## Errors
<a name="API_ListSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
There is an internal server error.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource cannot be found.
 ** resourceId **
Hypothetical identifier of the resource affected.
 ** resourceType **
Hypothetical type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
There is a throttling error.
 ** quotaCode **
The originating quota.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
 ** serviceCode **
The originating service.
HTTP Status Code: 429

 ** ValidationException **
There is a validation error.
 ** fieldList **
The field that caused the error.
 ** reason **
Reason the request failed validation
HTTP Status Code: 400

## See Also
<a name="API_ListSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-web-2020-07-08/ListSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/ListSessions)
