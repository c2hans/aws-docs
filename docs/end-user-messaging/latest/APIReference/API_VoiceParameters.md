---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_VoiceParameters.html
---

# VoiceParameters
<a name="API_VoiceParameters"></a>

The delivery parameters for the voice channel.

## Contents
<a name="API_VoiceParameters_Contents"></a>

 ** inlineTemplateBody **   <a name="endusermessaging-Type-VoiceParameters-inlineTemplateBody"></a>
The freeform message template used to render the one-time passcode for the voice channel. The template must contain the code placeholder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6000.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** languageCode **   <a name="endusermessaging-Type-VoiceParameters-languageCode"></a>
The BCP 47 language code used to render the voice message.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Pattern: `\S+`
Required: No

 ** voiceId **   <a name="endusermessaging-Type-VoiceParameters-voiceId"></a>
The Amazon Polly voice ID used for the voice channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** voiceMessageBodyTextType **   <a name="endusermessaging-Type-VoiceParameters-voiceMessageBodyTextType"></a>
The format of the voice message body. Valid values are TEXT and SSML.
Type: String
Valid Values: `TEXT | SSML`
Required: No

## See Also
<a name="API_VoiceParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/VoiceParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/VoiceParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/VoiceParameters)
