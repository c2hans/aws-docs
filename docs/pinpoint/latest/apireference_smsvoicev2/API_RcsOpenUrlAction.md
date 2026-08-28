---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsOpenUrlAction.html
---

# RcsOpenUrlAction
<a name="API_RcsOpenUrlAction"></a>

A suggested action that opens a URL in the recipient's browser or an in-app webview.

## Contents
<a name="API_RcsOpenUrlAction_Contents"></a>

 ** PostbackData **   <a name="pinpoint-Type-RcsOpenUrlAction-PostbackData"></a>
The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Text **   <a name="pinpoint-Type-RcsOpenUrlAction-Text"></a>
The display text of the action. Maximum 25 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: Yes

 ** Url **   <a name="pinpoint-Type-RcsOpenUrlAction-Url"></a>
The URL to open. Must start with https://. Maximum 2048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://\S+`
Required: Yes

 ** Application **   <a name="pinpoint-Type-RcsOpenUrlAction-Application"></a>
How to open the URL. BROWSER opens in the device's default browser. WEBVIEW opens in an in-app webview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Z_]+`
Required: No

 ** WebviewViewMode **   <a name="pinpoint-Type-RcsOpenUrlAction-WebviewViewMode"></a>
The display mode of the webview. Valid values are FULL, HALF, and TALL. Only applicable when Application is WEBVIEW.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Z_]+`
Required: No

## See Also
<a name="API_RcsOpenUrlAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsOpenUrlAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsOpenUrlAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsOpenUrlAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
