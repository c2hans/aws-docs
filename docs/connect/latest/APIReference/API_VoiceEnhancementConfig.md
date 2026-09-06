---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_VoiceEnhancementConfig.html
---

# VoiceEnhancementConfig
<a name="API_VoiceEnhancementConfig"></a>

Configuration settings for voice enhancement.

## Contents
<a name="API_VoiceEnhancementConfig_Contents"></a>

 ** Channel **   <a name="connect-Type-VoiceEnhancementConfig-Channel"></a>
The channel for this voice enhancement configuration. **Only `VOICE` is supported for this data type.**
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** VoiceEnhancementMode **   <a name="connect-Type-VoiceEnhancementConfig-VoiceEnhancementMode"></a>
The voice enhancement mode.
Type: String
Valid Values: `VOICE_ISOLATION | NOISE_SUPPRESSION | NONE`
Required: Yes

## See Also
<a name="API_VoiceEnhancementConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/VoiceEnhancementConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/VoiceEnhancementConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/VoiceEnhancementConfig)
