---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsReplyAction.html
---

# RcsReplyAction
<a name="API_RcsReplyAction"></a>

A suggested reply action that sends predefined text and postback data when tapped by the recipient.

## Contents
<a name="API_RcsReplyAction_Contents"></a>

 ** PostbackData **   <a name="pinpoint-Type-RcsReplyAction-PostbackData"></a>
The postback data sent to your webhook when the user taps this reply. Maximum 2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Text **   <a name="pinpoint-Type-RcsReplyAction-Text"></a>
The display text of the suggested reply. Maximum 25 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: Yes

## See Also
<a name="API_RcsReplyAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsReplyAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsReplyAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsReplyAction)
