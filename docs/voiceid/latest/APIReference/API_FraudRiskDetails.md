---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_FraudRiskDetails.html
---

# FraudRiskDetails
<a name="API_connect-voice-id_FraudRiskDetails"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Details regarding various fraud risk analyses performed against the current session state and streamed audio of the speaker.

## Contents
<a name="API_connect-voice-id_FraudRiskDetails_Contents"></a>

 ** KnownFraudsterRisk **   <a name="connect-Type-connect-voice-id_FraudRiskDetails-KnownFraudsterRisk"></a>
The details resulting from 'Known Fraudster Risk' analysis of the speaker.
Type: [KnownFraudsterRisk](API_connect-voice-id_KnownFraudsterRisk.md) object
Required: Yes

 ** VoiceSpoofingRisk **   <a name="connect-Type-connect-voice-id_FraudRiskDetails-VoiceSpoofingRisk"></a>
The details resulting from 'Voice Spoofing Risk' analysis of the speaker.
Type: [VoiceSpoofingRisk](API_connect-voice-id_VoiceSpoofingRisk.md) object
Required: Yes

## See Also
<a name="API_connect-voice-id_FraudRiskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/FraudRiskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/FraudRiskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/FraudRiskDetails)
