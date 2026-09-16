---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSpeakerSearchTask.html
---

# GetSpeakerSearchTask
<a name="API_voice-chime_GetSpeakerSearchTask"></a>

Retrieves the details of the specified speaker search task.

## Request Syntax
<a name="API_voice-chime_GetSpeakerSearchTask_RequestSyntax"></a>

```
GET /voice-connectors/{{VoiceConnectorId}}/speaker-search-tasks/{{SpeakerSearchTaskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_GetSpeakerSearchTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SpeakerSearchTaskId](#API_voice-chime_GetSpeakerSearchTask_RequestSyntax) **   <a name="chimesdk-voice-chime_GetSpeakerSearchTask-request-uri-SpeakerSearchTaskId"></a>
The ID of the speaker search task.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** [VoiceConnectorId](#API_voice-chime_GetSpeakerSearchTask_RequestSyntax) **   <a name="chimesdk-voice-chime_GetSpeakerSearchTask-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_GetSpeakerSearchTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_GetSpeakerSearchTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SpeakerSearchTask": {
      "CallDetails": {
         "IsCaller": boolean,
         "TransactionId": "string",
         "VoiceConnectorId": "string"
      },
      "CreatedTimestamp": "string",
      "SpeakerSearchDetails": {
         "Results": [
            {
               "ConfidenceScore": number,
               "VoiceProfileId": "string"
            }
         ],
         "VoiceprintGenerationStatus": "string"
      },
      "SpeakerSearchTaskId": "string",
      "SpeakerSearchTaskStatus": "string",
      "StartedTimestamp": "string",
      "StatusMessage": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_GetSpeakerSearchTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SpeakerSearchTask](#API_voice-chime_GetSpeakerSearchTask_ResponseSyntax) **   <a name="chimesdk-voice-chime_GetSpeakerSearchTask-response-SpeakerSearchTask"></a>
The details of the speaker search task.
Type: [SpeakerSearchTask](API_voice-chime_SpeakerSearchTask.md) object

## Errors
<a name="API_voice-chime_GetSpeakerSearchTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request were made simultaneously.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_GetSpeakerSearchTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/GetSpeakerSearchTask)
