---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AudioFillerSettings.html
---

# AudioFillerSettings
<a name="API_AudioFillerSettings"></a>

Configuration that plays background filler audio during speech-to-speech interactions to mask processing delays and improve the perceived responsiveness of the bot.

Audio filler requires `unifiedSpeechSettings` (speech-to-speech) to be enabled on the bot locale when `enabled` is `true`.

## Contents
<a name="API_AudioFillerSettings_Contents"></a>

 ** audioType **   <a name="lexv2-Type-AudioFillerSettings-audioType"></a>
The identifier of the audio filler to play while Amazon Lex processes the user's input. This field is required when `enabled` is `true`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `MELODY_CHIPPER_CHIME | MELODY_CURIOUS_CRAWL | MELODY_RISING_RIPPLE | MELODY_PATIENT_PING | MELODY_PONDERING_PONG | TYPING_KINETIC_KEYS | TYPING_QUIET_QWERTY`
Required: No

 ** enabled **   <a name="lexv2-Type-AudioFillerSettings-enabled"></a>
Specifies whether audio filler playback is enabled for the bot locale. Set to `true` to play filler audio while Amazon Lex processes a user utterance. Set to `false` to disable filler audio.
Type: Boolean
Required: No

 ** minimumPlayDurationInMilliseconds **   <a name="lexv2-Type-AudioFillerSettings-minimumPlayDurationInMilliseconds"></a>
The minimum time, in milliseconds, that audio filler plays once it has started, even if the bot response becomes ready sooner. Valid range is `1000` to `5000` milliseconds. If not specified, Amazon Lex uses a default of `3000` milliseconds.
Type: Integer
Required: No

 ** responseDeliveryDelayInMilliseconds **   <a name="lexv2-Type-AudioFillerSettings-responseDeliveryDelayInMilliseconds"></a>
The silent delay, in milliseconds, inserted between the end of audio filler playback and the start of the bot's response. Valid range is `200` to `1000` milliseconds. If not specified, Amazon Lex uses a default of `500` milliseconds.
Type: Integer
Required: No

 ** startDelayInMilliseconds **   <a name="lexv2-Type-AudioFillerSettings-startDelayInMilliseconds"></a>
The time, in milliseconds, to wait after the end of the user's utterance before starting audio filler playback. Valid range is `500` to `5000` milliseconds. If not specified, Amazon Lex uses a default of `2500` milliseconds.
Type: Integer
Required: No

## See Also
<a name="API_AudioFillerSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AudioFillerSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AudioFillerSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AudioFillerSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
