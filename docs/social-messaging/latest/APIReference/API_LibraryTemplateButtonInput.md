---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LibraryTemplateButtonInput.html
---

# LibraryTemplateButtonInput
<a name="API_LibraryTemplateButtonInput"></a>

Configuration options for customizing buttons in a template from Meta's library.

## Contents
<a name="API_LibraryTemplateButtonInput_Contents"></a>

 ** otpType **   <a name="Social-Type-LibraryTemplateButtonInput-otpType"></a>
The type of one-time password for OTP buttons.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: No

 ** phoneNumber **   <a name="Social-Type-LibraryTemplateButtonInput-phoneNumber"></a>
The phone number in E.164 format for CALL-type buttons.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

 ** supportedApps **   <a name="Social-Type-LibraryTemplateButtonInput-supportedApps"></a>
List of supported applications for this button type.
Type: Array of string to string maps
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 30.
Value Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** type **   <a name="Social-Type-LibraryTemplateButtonInput-type"></a>
The type of button (for example, QUICK\_REPLY, CALL, or URL).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: No

 ** url **   <a name="Social-Type-LibraryTemplateButtonInput-url"></a>
The URL with dynamic parameters for URL-type buttons.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 30.
Value Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** zeroTapTermsAccepted **   <a name="Social-Type-LibraryTemplateButtonInput-zeroTapTermsAccepted"></a>
When true, indicates acceptance of zero-tap terms for the button.
Type: Boolean
Required: No

## See Also
<a name="API_LibraryTemplateButtonInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/LibraryTemplateButtonInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/LibraryTemplateButtonInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/LibraryTemplateButtonInput)
