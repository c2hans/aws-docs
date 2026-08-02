---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListSessions.html
---

# ListSessions
<a name="API_ListSessions"></a>

Lists sessions for the specified application. You can filter sessions by state and creation time.

## Request Syntax
<a name="API_ListSessions_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/sessions?createdAtAfter={{createdAtAfter}}&createdAtBefore={{createdAtBefore}}&maxResults={{maxResults}}&nextToken={{nextToken}}&states={{states}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListSessions_RequestSyntax) **   <a name="emrserverless-ListSessions-request-uri-applicationId"></a>
The ID of the application to list sessions for.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [createdAtAfter](#API_ListSessions_RequestSyntax) **   <a name="emrserverless-ListSessions-request-uri-createdAtAfter"></a>
The lower bound of the option to filter by creation date and time.

 ** [createdAtBefore](#API_ListSessions_RequestSyntax) **   <a name="emrserverless-ListSessions-request-uri-createdAtBefore"></a>
The upper bound of the option to filter by creation date and time.

 ** [maxResults](#API_ListSessions_RequestSyntax) **   <a name="emrserverless-ListSessions-request-uri-maxResults"></a>
The maximum number of sessions to return in each page of results.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListSessions_RequestSyntax) **   <a name="emrserverless-ListSessions-request-uri-nextToken"></a>
The token for the next set of session results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

 ** [states](#API_ListSessions_RequestSyntax) **   <a name="emrserverless-ListSessions-request-uri-states"></a>
An optional filter for session states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Valid Values: `SUBMITTED | STARTING | STARTED | IDLE | BUSY | FAILED | TERMINATING | TERMINATED`

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
         "applicationId": "string",
         "arn": "string",
         "createdAt": number,
         "createdBy": "string",
         "executionRoleArn": "string",
         "name": "string",
         "releaseLabel": "string",
         "sessionId": "string",
         "state": "string",
         "stateDetails": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSessions_ResponseSyntax) **   <a name="emrserverless-ListSessions-response-nextToken"></a>
The output displays the token for the next set of session results. This is required for pagination and is available as a response of the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

 ** [sessions](#API_ListSessions_ResponseSyntax) **   <a name="emrserverless-ListSessions-response-sessions"></a>
The output lists information about the specified sessions.
Type: Array of [SessionSummary](API_SessionSummary.md) objects

## Errors
<a name="API_ListSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/ListSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ListSessions)
