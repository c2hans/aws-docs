---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateVoiceParameters.html
---

# UpdateVoiceParameters
<a name="API_UpdateVoiceParameters"></a>

The updated delivery parameters for the voice channel. Absent members preserve the current value, and the empty sentinel on a member clears it.

## Contents
<a name="API_UpdateVoiceParameters_Contents"></a>

 ** inlineTemplateBody **   <a name="endusermessaging-Type-UpdateVoiceParameters-inlineTemplateBody"></a>
The updated freeform voice template body. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6000.
Pattern: `([\s\S]*\S[\s\S]*)?`
Required: No

 ** languageCode **   <a name="endusermessaging-Type-UpdateVoiceParameters-languageCode"></a>
The updated BCP 47 language code. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 35.
Pattern: `(\S{2,35})?`
Required: No

 ** voiceId **   <a name="endusermessaging-Type-UpdateVoiceParameters-voiceId"></a>
The updated Amazon Polly voice ID. An empty string clears the previously stored value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[A-Za-z0-9]*`
Required: No

 ** voiceMessageBodyTextType **   <a name="endusermessaging-Type-UpdateVoiceParameters-voiceMessageBodyTextType"></a>
The updated format of the voice message body. Valid values are TEXT and SSML. Omit this member to preserve the current value.
Type: String
Valid Values: `TEXT | SSML`
Required: No

## See Also
<a name="API_UpdateVoiceParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateVoiceParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateVoiceParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateVoiceParameters)
