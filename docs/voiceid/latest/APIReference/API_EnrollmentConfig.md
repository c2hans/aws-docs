---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_EnrollmentConfig.html
---

# EnrollmentConfig
<a name="API_connect-voice-id_EnrollmentConfig"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains configurations defining enrollment behavior for the batch job.

## Contents
<a name="API_connect-voice-id_EnrollmentConfig_Contents"></a>

 ** ExistingEnrollmentAction **   <a name="connect-Type-connect-voice-id_EnrollmentConfig-ExistingEnrollmentAction"></a>
 The action to take when the specified speaker is already enrolled in the specified domain. The default value is `SKIP`, which skips the enrollment for the existing speaker. Setting the value to `OVERWRITE` replaces the existing voice prints and enrollment audio stored for that speaker with new data generated from the latest audio.
Type: String
Valid Values: `SKIP | OVERWRITE`
Required: No

 ** FraudDetectionConfig **   <a name="connect-Type-connect-voice-id_EnrollmentConfig-FraudDetectionConfig"></a>
The fraud detection configuration to use for the speaker enrollment job.
Type: [EnrollmentJobFraudDetectionConfig](API_connect-voice-id_EnrollmentJobFraudDetectionConfig.md) object
Required: No

## See Also
<a name="API_connect-voice-id_EnrollmentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/EnrollmentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/EnrollmentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/EnrollmentConfig)
