---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_VoiceSettings.html
---

# VoiceSettings
<a name="API_VoiceSettings"></a>

Defines settings for using an Amazon Polly voice to communicate with a user.

Valid values include:
+  `standard`
+  `neural`
+  `long-form`
+  `generative`

## Contents
<a name="API_VoiceSettings_Contents"></a>

 ** voiceId **   <a name="lexv2-Type-VoiceSettings-voiceId"></a>
The identifier of the Amazon Polly voice to use.
Type: String
Required: Yes

 ** engine **   <a name="lexv2-Type-VoiceSettings-engine"></a>
Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user. For more information, see the [`engine` parameter of the `SynthesizeSpeech` operation](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine) in the *Amazon Polly developer guide*.
If you do not specify a value, the default is `standard`.
Type: String
Valid Values: `standard | neural | long-form | generative`
Required: No

## See Also
<a name="API_VoiceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/VoiceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/VoiceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/VoiceSettings)
