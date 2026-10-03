---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_NotifyParameters.html
---

# NotifyParameters
<a name="API_NotifyParameters"></a>

The delivery parameters for the preapproved notify-template route over the SMS or voice channels.

## Contents
<a name="API_NotifyParameters_Contents"></a>

 ** notifyTemplateId **   <a name="endusermessaging-Type-NotifyParameters-notifyTemplateId"></a>
The identifier of a preapproved notify template for the SMS or voice channels.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** voiceId **   <a name="endusermessaging-Type-NotifyParameters-voiceId"></a>
The Amazon Polly voice ID used when the notify template is delivered over the voice channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]+`
Required: No

## See Also
<a name="API_NotifyParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/NotifyParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/NotifyParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/NotifyParameters)
