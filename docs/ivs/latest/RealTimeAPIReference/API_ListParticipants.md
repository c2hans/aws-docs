---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipants.html
---

# ListParticipants
<a name="API_ListParticipants"></a>

Lists all participants in a specified stage session.

## Request Syntax
<a name="API_ListParticipants_RequestSyntax"></a>

```
POST /ListParticipants HTTP/1.1
Content-type: application/json

{
   "filterByPublished": {{boolean}},
   "filterByRecordingState": "{{string}}",
   "filterByState": "{{string}}",
   "filterByUserId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sessionId": "{{string}}",
   "stageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListParticipants_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListParticipants_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterByPublished](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-filterByPublished"></a>
Filters the response list to only show participants who published during the stage session. Only one of `filterByUserId`, `filterByPublished`, `filterByState`, or `filterByRecordingState` can be provided per request.
Type: Boolean
Required: No

 ** [filterByRecordingState](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-filterByRecordingState"></a>
Filters the response list to only show participants with the specified recording state. Only one of `filterByUserId`, `filterByPublished`, `filterByState`, or `filterByRecordingState` can be provided per request.
Type: String
Valid Values: `STARTING | ACTIVE | STOPPING | STOPPED | FAILED`
Required: No

 ** [filterByState](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-filterByState"></a>
Filters the response list to only show participants in the specified state. Only one of `filterByUserId`, `filterByPublished`, `filterByState`, or `filterByRecordingState` can be provided per request.
Type: String
Valid Values: `CONNECTED | DISCONNECTED`
Required: No

 ** [filterByUserId](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-filterByUserId"></a>
Filters the response list to match the specified user ID. Only one of `filterByUserId`, `filterByPublished`, `filterByState`, or `filterByRecordingState` can be provided per request. A `userId` is a customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [maxResults](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-maxResults"></a>
Maximum number of results to return. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-nextToken"></a>
The first participant to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

 ** [sessionId](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-sessionId"></a>
ID of the session within the stage.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: Yes

 ** [stageArn](#API_ListParticipants_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-request-stageArn"></a>
Stage ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_ListParticipants_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "participants": [
      {
         "firstJoinTime": "string",
         "ingestConfigurationArn": "string",
         "participantId": "string",
         "published": boolean,
         "recordingState": "string",
         "redundantIngest": boolean,
         "replicationState": "string",
         "replicationType": "string",
         "sourceSessionId": "string",
         "sourceStageArn": "string",
         "state": "string",
         "userId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListParticipants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListParticipants_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-response-nextToken"></a>
If there are more participants than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [participants](#API_ListParticipants_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListParticipants-response-participants"></a>
List of the matching participants (summary information only).
Type: Array of [ParticipantSummary](API_ParticipantSummary.md) objects

## Errors
<a name="API_ListParticipants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListParticipants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/ListParticipants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ListParticipants)
