---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsDialPhoneAction.html
---

# RcsDialPhoneAction
<a name="API_RcsDialPhoneAction"></a>

A suggested action that initiates a phone call to a specified number when tapped by the recipient.

## Contents
<a name="API_RcsDialPhoneAction_Contents"></a>

 ** PhoneNumber **   <a name="pinpoint-Type-RcsDialPhoneAction-PhoneNumber"></a>
The phone number to dial in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** PostbackData **   <a name="pinpoint-Type-RcsDialPhoneAction-PostbackData"></a>
The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Text **   <a name="pinpoint-Type-RcsDialPhoneAction-Text"></a>
The display text of the action. Maximum 25 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: Yes

## See Also
<a name="API_RcsDialPhoneAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsDialPhoneAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsDialPhoneAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsDialPhoneAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
