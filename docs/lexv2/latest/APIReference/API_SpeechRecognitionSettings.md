---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SpeechRecognitionSettings.html
---

# SpeechRecognitionSettings
<a name="API_SpeechRecognitionSettings"></a>

Settings that control how Amazon Lex processes and recognizes speech input from users.

## Contents
<a name="API_SpeechRecognitionSettings_Contents"></a>

 ** speechModelConfig **   <a name="lexv2-Type-SpeechRecognitionSettings-speechModelConfig"></a>
Configuration settings for the selected speech-to-text model.
Type: [SpeechModelConfig](API_SpeechModelConfig.md) object
Required: No

 ** speechModelPreference **   <a name="lexv2-Type-SpeechRecognitionSettings-speechModelPreference"></a>
The speech-to-text model to use.
Type: String
Valid Values: `Standard | Neural | Deepgram`
Required: No

## See Also
<a name="API_SpeechRecognitionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SpeechRecognitionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SpeechRecognitionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SpeechRecognitionSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
