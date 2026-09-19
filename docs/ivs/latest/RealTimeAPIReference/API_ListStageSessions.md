---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStageSessions.html
---

# ListStageSessions
<a name="API_ListStageSessions"></a>

Gets all sessions for a specified stage.

## Request Syntax
<a name="API_ListStageSessions_RequestSyntax"></a>

```
POST /ListStageSessions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "stageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListStageSessions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListStageSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListStageSessions_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListStageSessions-request-maxResults"></a>
Maximum number of results to return. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListStageSessions_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListStageSessions-request-nextToken"></a>
The first stage session to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

 ** [stageArn](#API_ListStageSessions_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListStageSessions-request-stageArn"></a>
Stage ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_ListStageSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "stageSessions": [
      {
         "endTime": "string",
         "sessionId": "string",
         "startTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStageSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStageSessions_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListStageSessions-response-nextToken"></a>
If there are more stage sessions than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [stageSessions](#API_ListStageSessions_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListStageSessions-response-stageSessions"></a>
List of matching stage sessions.
Type: Array of [StageSessionSummary](API_StageSessionSummary.md) objects

## Errors
<a name="API_ListStageSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListStageSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/ListStageSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ListStageSessions)
