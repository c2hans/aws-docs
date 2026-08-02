---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceToneAnalysisTask.html
---

# GetVoiceToneAnalysisTask
<a name="API_voice-chime_GetVoiceToneAnalysisTask"></a>

Retrieves the details of a voice tone analysis task.

## Request Syntax
<a name="API_voice-chime_GetVoiceToneAnalysisTask_RequestSyntax"></a>

```
GET /voice-connectors/{{VoiceConnectorId}}/voice-tone-analysis-tasks/{{VoiceToneAnalysisTaskId}}?isCaller={{IsCaller}} HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_GetVoiceToneAnalysisTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IsCaller](#API_voice-chime_GetVoiceToneAnalysisTask_RequestSyntax) **   <a name="chimesdk-voice-chime_GetVoiceToneAnalysisTask-request-uri-IsCaller"></a>
Specifies whether the voice being analyzed is the caller (originator) or the callee (responder).
Required: Yes

 ** [VoiceConnectorId](#API_voice-chime_GetVoiceToneAnalysisTask_RequestSyntax) **   <a name="chimesdk-voice-chime_GetVoiceToneAnalysisTask-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** [VoiceToneAnalysisTaskId](#API_voice-chime_GetVoiceToneAnalysisTask_RequestSyntax) **   <a name="chimesdk-voice-chime_GetVoiceToneAnalysisTask-request-uri-VoiceToneAnalysisTaskId"></a>
The ID of the voice tone analysis task.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_GetVoiceToneAnalysisTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_GetVoiceToneAnalysisTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VoiceToneAnalysisTask": {
      "CallDetails": {
         "IsCaller": boolean,
         "TransactionId": "string",
         "VoiceConnectorId": "string"
      },
      "CreatedTimestamp": "string",
      "StartedTimestamp": "string",
      "StatusMessage": "string",
      "UpdatedTimestamp": "string",
      "VoiceToneAnalysisTaskId": "string",
      "VoiceToneAnalysisTaskStatus": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_GetVoiceToneAnalysisTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VoiceToneAnalysisTask](#API_voice-chime_GetVoiceToneAnalysisTask_ResponseSyntax) **   <a name="chimesdk-voice-chime_GetVoiceToneAnalysisTask-response-VoiceToneAnalysisTask"></a>
The details of the voice tone analysis task.
Type: [VoiceToneAnalysisTask](API_voice-chime_VoiceToneAnalysisTask.md) object

## Errors
<a name="API_voice-chime_GetVoiceToneAnalysisTask_Errors"></a>

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
<a name="API_voice-chime_GetVoiceToneAnalysisTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/GetVoiceToneAnalysisTask)
