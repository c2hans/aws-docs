---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_FraudDetectionResult.html
---

# FraudDetectionResult
<a name="API_connect-voice-id_FraudDetectionResult"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The fraud detection result produced by Voice ID, processed against the current session state and streamed audio of the speaker.

## Contents
<a name="API_connect-voice-id_FraudDetectionResult_Contents"></a>

 ** AudioAggregationEndedAt **   <a name="connect-Type-connect-voice-id_FraudDetectionResult-AudioAggregationEndedAt"></a>
A timestamp of when audio aggregation ended for this fraud detection result.
Type: Timestamp
Required: No

 ** AudioAggregationStartedAt **   <a name="connect-Type-connect-voice-id_FraudDetectionResult-AudioAggregationStartedAt"></a>
A timestamp of when audio aggregation started for this fraud detection result.
Type: Timestamp
Required: No

 ** Configuration **   <a name="connect-Type-connect-voice-id_FraudDetectionResult-Configuration"></a>
The `FraudDetectionConfiguration` used to generate this fraud detection result.
Type: [FraudDetectionConfiguration](API_connect-voice-id_FraudDetectionConfiguration.md) object
Required: No

 ** Decision **   <a name="connect-Type-connect-voice-id_FraudDetectionResult-Decision"></a>
The fraud detection decision produced by Voice ID, processed against the current session state and streamed audio of the speaker.
Type: String
Valid Values: `HIGH_RISK | LOW_RISK | NOT_ENOUGH_SPEECH`
Required: No

 ** FraudDetectionResultId **   <a name="connect-Type-connect-voice-id_FraudDetectionResult-FraudDetectionResultId"></a>
The unique identifier for this fraud detection result. Given there can be multiple fraud detections for a given session, this field helps in identifying if the returned result is from previous streaming activity or a new result. Note that in the absence of any new streaming activity or risk threshold changes, Voice ID always returns cached Fraud Detection result for this API.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** Reasons **   <a name="connect-Type-connect-voice-id_FraudDetectionResult-Reasons"></a>
The reason speaker was flagged by the fraud detection system. This is only be populated if fraud detection Decision is `HIGH_RISK`, and the following possible values: `KNOWN_FRAUDSTER` and `VOICE_SPOOFING`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `KNOWN_FRAUDSTER | VOICE_SPOOFING`
Required: No

 ** RiskDetails **   <a name="connect-Type-connect-voice-id_FraudDetectionResult-RiskDetails"></a>
Details about each risk analyzed for this speaker. Currently, this contains KnownFraudsterRisk and VoiceSpoofingRisk details.
Type: [FraudRiskDetails](API_connect-voice-id_FraudRiskDetails.md) object
Required: No

## See Also
<a name="API_connect-voice-id_FraudDetectionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/FraudDetectionResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/FraudDetectionResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/FraudDetectionResult)
