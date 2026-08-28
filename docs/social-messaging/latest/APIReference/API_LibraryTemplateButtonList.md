---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LibraryTemplateButtonList.html
---

# LibraryTemplateButtonList
<a name="API_LibraryTemplateButtonList"></a>

Defines a button in a template from Meta's library.

## Contents
<a name="API_LibraryTemplateButtonList_Contents"></a>

 ** otpType **   <a name="Social-Type-LibraryTemplateButtonList-otpType"></a>
The type of one-time password for OTP buttons.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: No

 ** phoneNumber **   <a name="Social-Type-LibraryTemplateButtonList-phoneNumber"></a>
The phone number in E.164 format for CALL-type buttons.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

 ** supportedApps **   <a name="Social-Type-LibraryTemplateButtonList-supportedApps"></a>
List of supported applications for this button type.
Type: Array of string to string maps
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 30.
Value Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** text **   <a name="Social-Type-LibraryTemplateButtonList-text"></a>
The text displayed on the button (maximum 40 characters).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Required: No

 ** type **   <a name="Social-Type-LibraryTemplateButtonList-type"></a>
The type of button (for example, QUICK\_REPLY, CALL, or URL).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: No

 ** url **   <a name="Social-Type-LibraryTemplateButtonList-url"></a>
The URL for URL-type buttons.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** zeroTapTermsAccepted **   <a name="Social-Type-LibraryTemplateButtonList-zeroTapTermsAccepted"></a>
When true, indicates acceptance of zero-tap terms for the button.
Type: Boolean
Required: No

## See Also
<a name="API_LibraryTemplateButtonList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/LibraryTemplateButtonList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/LibraryTemplateButtonList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/LibraryTemplateButtonList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
