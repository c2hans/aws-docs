---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateStage.html
---

# UpdateStage
<a name="API_UpdateStage"></a>

Updates a stage’s configuration.

## Request Syntax
<a name="API_UpdateStage_RequestSyntax"></a>

```
POST /UpdateStage HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "autoParticipantRecordingConfiguration": {
      "hlsConfiguration": {
         "targetSegmentDurationSeconds": {{number}}
      },
      "mediaTypes": [ "{{string}}" ],
      "recordingReconnectWindowSeconds": {{number}},
      "recordParticipantReplicas": {{boolean}},
      "storageConfigurationArn": "{{string}}",
      "thumbnailConfiguration": {
         "recordingMode": "{{string}}",
         "storage": [ "{{string}}" ],
         "targetIntervalSeconds": {{number}}
      }
   },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateStage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateStage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateStage_RequestSyntax) **   <a name="ivsrealtimeeapireference-UpdateStage-request-arn"></a>
ARN of the stage to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: Yes

 ** [autoParticipantRecordingConfiguration](#API_UpdateStage_RequestSyntax) **   <a name="ivsrealtimeeapireference-UpdateStage-request-autoParticipantRecordingConfiguration"></a>
Configuration object for individual participant recording, to attach to the stage. Note that this cannot be updated while recording is active.
Type: [AutoParticipantRecordingConfiguration](API_AutoParticipantRecordingConfiguration.md) object
Required: No

 ** [name](#API_UpdateStage_RequestSyntax) **   <a name="ivsrealtimeeapireference-UpdateStage-request-name"></a>
Name of the stage to be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

## Response Syntax
<a name="API_UpdateStage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "stage": {
      "activeSessionId": "string",
      "arn": "string",
      "autoParticipantRecordingConfiguration": {
         "hlsConfiguration": {
            "targetSegmentDurationSeconds": number
         },
         "mediaTypes": [ "string" ],
         "recordingReconnectWindowSeconds": number,
         "recordParticipantReplicas": boolean,
         "storageConfigurationArn": "string",
         "thumbnailConfiguration": {
            "recordingMode": "string",
            "storage": [ "string" ],
            "targetIntervalSeconds": number
         }
      },
      "endpoints": {
         "events": "string",
         "rtmp": "string",
         "rtmps": "string",
         "whip": "string"
      },
      "name": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [stage](#API_UpdateStage_ResponseSyntax) **   <a name="ivsrealtimeeapireference-UpdateStage-response-stage"></a>
The updated stage.
Type: [Stage](API_Stage.md) object

## Errors
<a name="API_UpdateStage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **

 ** exceptionMessage **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** PendingVerification **

 ** exceptionMessage **
 Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **

 ** exceptionMessage **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **

 ** exceptionMessage **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/UpdateStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/UpdateStage)
