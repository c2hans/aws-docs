---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SpeakerDiarizationSettings.html
---

# SpeakerDiarizationSettings
<a name="API_SpeakerDiarizationSettings"></a>

Specifies configuration that restricts speech detection to the primary (loudest) speaker during streaming audio conversations, so that speech from background speakers does not start a turn, interrupt the bot, or reach speech recognition.

## Contents
<a name="API_SpeakerDiarizationSettings_Contents"></a>

 ** enabled **   <a name="lexv2-Type-SpeakerDiarizationSettings-enabled"></a>
Specifies whether speaker diarization is enabled for the bot locale. Set to `true` to have Amazon Lex treat speech from speakers other than the primary speaker as non-speech. Set to `false` to disable speaker diarization and rely on voice activity detection alone.
Type: Boolean
Required: Yes

## See Also
<a name="API_SpeakerDiarizationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SpeakerDiarizationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SpeakerDiarizationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SpeakerDiarizationSettings)
