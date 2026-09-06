---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_FraudDetectionConfiguration.html
---

# FraudDetectionConfiguration
<a name="API_connect-voice-id_FraudDetectionConfiguration"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The configuration used for performing fraud detection over a speaker during a session.

## Contents
<a name="API_connect-voice-id_FraudDetectionConfiguration_Contents"></a>

 ** RiskThreshold **   <a name="connect-Type-connect-voice-id_FraudDetectionConfiguration-RiskThreshold"></a>
Threshold value for determining whether the speaker is a fraudster. If the detected risk score calculated by Voice ID is higher than the threshold, the speaker is considered a fraudster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** WatchlistId **   <a name="connect-Type-connect-voice-id_FraudDetectionConfiguration-WatchlistId"></a>
The identifier of the watchlist against which fraud detection is performed.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

## See Also
<a name="API_connect-voice-id_FraudDetectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/FraudDetectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/FraudDetectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/FraudDetectionConfiguration)
