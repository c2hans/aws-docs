---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_EnrollmentJobFraudDetectionConfig.html
---

# EnrollmentJobFraudDetectionConfig
<a name="API_connect-voice-id_EnrollmentJobFraudDetectionConfig"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The fraud detection configuration to be used during the batch speaker enrollment job.

## Contents
<a name="API_connect-voice-id_EnrollmentJobFraudDetectionConfig_Contents"></a>

 ** FraudDetectionAction **   <a name="connect-Type-connect-voice-id_EnrollmentJobFraudDetectionConfig-FraudDetectionAction"></a>
The action to take when the given speaker is flagged by the fraud detection system. The default value is `FAIL`, which fails the speaker enrollment. Changing this value to `IGNORE` results in the speaker being enrolled even if they are flagged by the fraud detection system.
Type: String
Valid Values: `IGNORE | FAIL`
Required: No

 ** RiskThreshold **   <a name="connect-Type-connect-voice-id_EnrollmentJobFraudDetectionConfig-RiskThreshold"></a>
Threshold value for determining whether the speaker is a high risk to be fraudulent. If the detected risk score calculated by Voice ID is greater than or equal to the threshold, the speaker is considered a fraudster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** WatchlistIds **   <a name="connect-Type-connect-voice-id_EnrollmentJobFraudDetectionConfig-WatchlistIds"></a>
The identifier of watchlists against which fraud detection is performed.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

## See Also
<a name="API_connect-voice-id_EnrollmentJobFraudDetectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/EnrollmentJobFraudDetectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/EnrollmentJobFraudDetectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/EnrollmentJobFraudDetectionConfig)
