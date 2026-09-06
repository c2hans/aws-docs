---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_StartMedicalScribeListeningSession.html
---

# StartMedicalScribeListeningSession
<a name="API_StartMedicalScribeListeningSession"></a>

Starts a new Medical Scribe listening session for real-time audio transcription

## Request Syntax
<a name="API_StartMedicalScribeListeningSession_RequestSyntax"></a>

```
POST /medical-scribe-stream/ HTTP/1.1
x-amzn-medscribe-session-id: {{sessionId}}
x-amzn-medscribe-domain-id: {{domainId}}
x-amzn-medscribe-subscription-id: {{subscriptionId}}
x-amzn-medscribe-language-code: {{languageCode}}
x-amzn-medscribe-sample-rate: {{mediaSampleRateHertz}}
x-amzn-medscribe-media-encoding: {{mediaEncoding}}
Content-type: application/json

{
   "audioEvent": {
      "audioChunk": {{blob}}
   },
   "binaryAudioEvent": {
      "audioChunk": {{blob}}
   },
   "configurationEvent": {
      "channelDefinitions": [
         {
            "channelId": {{number}},
            "participantRole": "{{string}}"
         }
      ],
      "encounterContext": {
         "unstructuredContext": "{{string}}"
      },
      "postStreamActionSettings": {
         "clinicalNoteGenerationSettings": {
            "noteTemplateSettings": { ... }
         },
         "outputS3Uri": "{{string}}"
      }
   },
   "sessionControlEvent": {
      "type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartMedicalScribeListeningSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-domainId"></a>
The Domain identifier
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** [languageCode](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-languageCode"></a>
The Language Code for the audio in the session
Valid Values: `en-US`
Required: Yes

 ** [mediaEncoding](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-mediaEncoding"></a>
The encoding for the input audio
Valid Values: `pcm | flac`
Required: Yes

 ** [mediaSampleRateHertz](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-mediaSampleRateHertz"></a>
The sample rate of the input audio
Valid Range: Minimum value of 8000. Maximum value of 48000.
Required: Yes

 ** [sessionId](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-sessionId"></a>
The Session identifier
Length Constraints: Fixed length of 36.
Pattern: `.*[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}.*`
Required: Yes

 ** [subscriptionId](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-subscriptionId"></a>
The Subscription identifier
Length Constraints: Fixed length of 25.
Pattern: `sub-[a-zA-Z0-9]{21}`
Required: Yes

## Request Body
<a name="API_StartMedicalScribeListeningSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [audioEvent](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-audioEvent"></a>

Type: [MedicalScribeAudioEvent](API_MedicalScribeAudioEvent.md) object
Required: No

 ** [binaryAudioEvent](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-binaryAudioEvent"></a>
An event containing raw binary audio data for the Medical Scribe stream. The audio is sent as a raw binary payload rather than as a base64-encoded value.
Type: [MedicalScribeBinaryAudioEvent](API_MedicalScribeBinaryAudioEvent.md) object
Required: No

 ** [configurationEvent](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-configurationEvent"></a>

Type: [MedicalScribeConfigurationEvent](API_MedicalScribeConfigurationEvent.md) object
Required: No

 ** [sessionControlEvent](#API_StartMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-request-sessionControlEvent"></a>

Type: [MedicalScribeSessionControlEvent](API_MedicalScribeSessionControlEvent.md) object
Required: No

## Response Syntax
<a name="API_StartMedicalScribeListeningSession_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-medscribe-session-id: {{sessionId}}
x-amzn-medscribe-domain-id: {{domainId}}
x-amzn-medscribe-subscription-id: {{subscriptionId}}
x-amzn-request-id: {{requestId}}
x-amzn-medscribe-language-code: {{languageCode}}
x-amzn-medscribe-sample-rate: {{mediaSampleRateHertz}}
x-amzn-medscribe-media-encoding: {{mediaEncoding}}
Content-type: application/json

{
   "internalFailureException": {
   },
   "transcriptEvent": {
      "transcriptSegment": {
         "audioBeginOffset": number,
         "audioEndOffset": number,
         "channelId": "string",
         "content": "string",
         "isPartial": boolean,
         "segmentId": "string"
      }
   },
   "validationException": {
   }
}
```

## Response Elements
<a name="API_StartMedicalScribeListeningSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [domainId](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-domainId"></a>
The Domain identifier
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`

 ** [languageCode](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-languageCode"></a>
The Language Code for the audio in the session
Valid Values: `en-US`

 ** [mediaEncoding](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-mediaEncoding"></a>
The encoding for the input audio
Valid Values: `pcm | flac`

 ** [mediaSampleRateHertz](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-mediaSampleRateHertz"></a>
The sample rate of the input audio
Valid Range: Minimum value of 8000. Maximum value of 48000.

 ** [requestId](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-requestId"></a>
The Request identifier
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [sessionId](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-sessionId"></a>
The Session identifier
Length Constraints: Fixed length of 36.
Pattern: `.*[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}.*`

 ** [subscriptionId](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-subscriptionId"></a>
The Subscription identifier
Length Constraints: Fixed length of 25.
Pattern: `sub-[a-zA-Z0-9]{21}`

The following data is returned in JSON format by the service.

 ** [internalFailureException](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-internalFailureException"></a>

Type: Exception
HTTP Status Code: 500

 ** [transcriptEvent](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-transcriptEvent"></a>

Type: [MedicalScribeTranscriptEvent](API_MedicalScribeTranscriptEvent.md) object

 ** [validationException](#API_StartMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-StartMedicalScribeListeningSession-response-validationException"></a>

Type: Exception
HTTP Status Code: 400

## Errors
<a name="API_StartMedicalScribeListeningSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** InternalServerException **
This error is thrown when a transient error causes our API to fail.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
This error is thrown when the client exceeds the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_StartMedicalScribeListeningSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/StartMedicalScribeListeningSession)
