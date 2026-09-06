---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_EvaluateSession.html
---

# EvaluateSession
<a name="API_connect-voice-id_EvaluateSession"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Evaluates a specified session based on audio data accumulated during a streaming Connect Customer Voice ID call.

## Request Syntax
<a name="API_connect-voice-id_EvaluateSession_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "SessionNameOrId": "{{string}}"
}
```

## Request Parameters
<a name="API_connect-voice-id_EvaluateSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_connect-voice-id_EvaluateSession_RequestSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-request-DomainId"></a>
The identifier of the domain where the session started.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: Yes

 ** [SessionNameOrId](#API_connect-voice-id_EvaluateSession_RequestSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-request-SessionNameOrId"></a>
The session identifier, or name of the session, that you want to evaluate. In Voice ID integration, this is the Contact-Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `(id#[a-zA-Z0-9]{22}|[a-zA-Z0-9][a-zA-Z0-9_-]*)`
Required: Yes

## Response Syntax
<a name="API_connect-voice-id_EvaluateSession_ResponseSyntax"></a>

```
{
   "AuthenticationResult": {
      "AudioAggregationEndedAt": number,
      "AudioAggregationStartedAt": number,
      "AuthenticationResultId": "string",
      "Configuration": {
         "AcceptanceThreshold": number
      },
      "CustomerSpeakerId": "string",
      "Decision": "string",
      "GeneratedSpeakerId": "string",
      "Score": number
   },
   "DomainId": "string",
   "FraudDetectionResult": {
      "AudioAggregationEndedAt": number,
      "AudioAggregationStartedAt": number,
      "Configuration": {
         "RiskThreshold": number,
         "WatchlistId": "string"
      },
      "Decision": "string",
      "FraudDetectionResultId": "string",
      "Reasons": [ "string" ],
      "RiskDetails": {
         "KnownFraudsterRisk": {
            "GeneratedFraudsterId": "string",
            "RiskScore": number
         },
         "VoiceSpoofingRisk": {
            "RiskScore": number
         }
      }
   },
   "SessionId": "string",
   "SessionName": "string",
   "StreamingStatus": "string"
}
```

## Response Elements
<a name="API_connect-voice-id_EvaluateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthenticationResult](#API_connect-voice-id_EvaluateSession_ResponseSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-response-AuthenticationResult"></a>
Details resulting from the authentication process, such as authentication decision and authentication score.
Type: [AuthenticationResult](API_connect-voice-id_AuthenticationResult.md) object

 ** [DomainId](#API_connect-voice-id_EvaluateSession_ResponseSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-response-DomainId"></a>
The identifier of the domain that contains the session.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`

 ** [FraudDetectionResult](#API_connect-voice-id_EvaluateSession_ResponseSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-response-FraudDetectionResult"></a>
Details resulting from the fraud detection process, such as fraud detection decision and risk score.
Type: [FraudDetectionResult](API_connect-voice-id_FraudDetectionResult.md) object

 ** [SessionId](#API_connect-voice-id_EvaluateSession_ResponseSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-response-SessionId"></a>
The service-generated identifier of the session.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `id#[a-zA-Z0-9]{22}`

 ** [SessionName](#API_connect-voice-id_EvaluateSession_ResponseSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-response-SessionName"></a>
The client-provided name of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

 ** [StreamingStatus](#API_connect-voice-id_EvaluateSession_ResponseSyntax) **   <a name="connect-connect-voice-id_EvaluateSession-response-StreamingStatus"></a>
The current status of audio streaming for this session. This field is useful to infer next steps when the Authentication or Fraud Detection results are empty or the decision is `NOT_ENOUGH_SPEECH`. In this situation, if the `StreamingStatus` is `ONGOING/PENDING_CONFIGURATION`, it can mean that the client should call the API again later, after Voice ID has enough audio to produce a result. If the decision remains `NOT_ENOUGH_SPEECH` even after `StreamingStatus` is `ENDED`, it means that the previously streamed session did not have enough speech to perform evaluation, and a new streaming session is needed to try again.
Type: String
Valid Values: `PENDING_CONFIGURATION | ONGOING | ENDED`

## Errors
<a name="API_connect-voice-id_EvaluateSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Check the error message and try again.
HTTP Status Code: 400

 ** ConflictException **
The request failed due to a conflict. Check the `ConflictType` and error message for more details.
 ** ConflictType **
The type of conflict which caused a ConflictException. Possible types and the corresponding error messages are as follows:
+  `DOMAIN_NOT_ACTIVE`: The domain is not active.
+  `CANNOT_CHANGE_SPEAKER_AFTER_ENROLLMENT`: You cannot change the speaker ID after an enrollment has been requested.
+  `ENROLLMENT_ALREADY_EXISTS`: There is already an enrollment for this session.
+  `SPEAKER_NOT_SET`: You must set the speaker ID before requesting an enrollment.
+  `SPEAKER_OPTED_OUT`: You cannot request an enrollment for an opted out speaker.
+  `CONCURRENT_CHANGES`: The request could not be processed as the resource was modified by another request during execution.
HTTP Status Code: 400

 ** InternalServerException **
The request failed due to an unknown error on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found. Check the `ResourceType` and error message for more details.
 ** ResourceType **
The type of resource which cannot not be found. Possible types are `BATCH_JOB`, `COMPLIANCE_CONSENT`, `DOMAIN`, `FRAUDSTER`, `SESSION` and `SPEAKER`.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Please slow down your request rate. Refer to [ Connect Customer Voice ID Service API throttling quotas ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas) and try your request again.
HTTP Status Code: 400

 ** ValidationException **
The request failed one or more validations; check the error message for more details.
HTTP Status Code: 400

## See Also
<a name="API_connect-voice-id_EvaluateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/voice-id-2021-09-27/EvaluateSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/EvaluateSession)
