---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetParticipant.html
---

# GetParticipant
<a name="API_GetParticipant"></a>

Gets information about the specified participant token.

## Request Syntax
<a name="API_GetParticipant_RequestSyntax"></a>

```
POST /GetParticipant HTTP/1.1
Content-type: application/json

{
   "participantId": "{{string}}",
   "sessionId": "{{string}}",
   "stageArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetParticipant_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetParticipant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [participantId](#API_GetParticipant_RequestSyntax) **   <a name="ivsrealtimeeapireference-GetParticipant-request-participantId"></a>
Unique identifier for the participant. This is assigned by IVS and returned by [CreateParticipantToken](API_CreateParticipantToken.md).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]*`
Required: Yes

 ** [sessionId](#API_GetParticipant_RequestSyntax) **   <a name="ivsrealtimeeapireference-GetParticipant-request-sessionId"></a>
ID of a session within the stage.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `st-[a-zA-Z0-9]+`
Required: Yes

 ** [stageArn](#API_GetParticipant_RequestSyntax) **   <a name="ivsrealtimeeapireference-GetParticipant-request-stageArn"></a>
Stage ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetParticipant_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "participant": {
      "attributes": {
         "string" : "string"
      },
      "browserName": "string",
      "browserVersion": "string",
      "firstJoinTime": "string",
      "ingestConfigurationArn": "string",
      "ispName": "string",
      "osName": "string",
      "osVersion": "string",
      "participantId": "string",
      "protocol": "string",
      "published": boolean,
      "recordingS3BucketName": "string",
      "recordingS3Prefix": "string",
      "recordingState": "string",
      "redundantIngest": boolean,
      "replicationState": "string",
      "replicationType": "string",
      "sdkVersion": "string",
      "sourceSessionId": "string",
      "sourceStageArn": "string",
      "state": "string",
      "userId": "string"
   }
}
```

## Response Elements
<a name="API_GetParticipant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [participant](#API_GetParticipant_ResponseSyntax) **   <a name="ivsrealtimeeapireference-GetParticipant-response-participant"></a>
The participant that is returned.
Type: [Participant](API_Participant.md) object

## Errors
<a name="API_GetParticipant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetParticipant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/GetParticipant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/GetParticipant)
