---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_IosImportClientBrandingAttributes.html
---

# IosImportClientBrandingAttributes
<a name="API_IosImportClientBrandingAttributes"></a>

The client branding attributes to import for iOS device types. These attributes are displayed on the iOS client login screen.

**Important**
Client branding attributes are public facing. Ensure you do not include sensitive information.

## Contents
<a name="API_IosImportClientBrandingAttributes_Contents"></a>

 ** ForgotPasswordLink **   <a name="WorkSpaces-Type-IosImportClientBrandingAttributes-ForgotPasswordLink"></a>
The forgotten password link. This is the web address that users can go to if they forget the password for their WorkSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(http|https)\://\S+`
Required: No

 ** LoginMessage **   <a name="WorkSpaces-Type-IosImportClientBrandingAttributes-LoginMessage"></a>
The login message. Specified as a key value pair, in which the key is a locale and the value is the localized message for that locale. The only key supported is `en_US`. The HTML tags supported include the following: `a, b, blockquote, br, cite, code, dd, dl, dt, div, em, i, li, ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul`.
Type: String to string map
Key Length Constraints: Fixed length of 5.
Key Pattern: `^[a-z]{2}_[A-Z]{2}$`
Value Length Constraints: Minimum length of 0. Maximum length of 2000.
Value Pattern: `^.*$`
Required: No

 ** Logo **   <a name="WorkSpaces-Type-IosImportClientBrandingAttributes-Logo"></a>
The logo. This is the standard-resolution display that has a 1:1 pixel density (or @1x), where one pixel is equal to one point. The only image format accepted is a binary data object that is converted from a `.png` file.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 447000.
Required: No

 ** Logo2x **   <a name="WorkSpaces-Type-IosImportClientBrandingAttributes-Logo2x"></a>
The @2x version of the logo. This is the higher resolution display that offers a scale factor of 2.0 (or @2x). The only image format accepted is a binary data object that is converted from a `.png` file.
 For more information about iOS image size and resolution, see [Image Size and Resolution ](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/) in the *Apple Human Interface Guidelines*.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 1770000.
Required: No

 ** Logo3x **   <a name="WorkSpaces-Type-IosImportClientBrandingAttributes-Logo3x"></a>
The @3x version of the logo. This is the higher resolution display that offers a scale factor of 3.0 (or @3x). The only image format accepted is a binary data object that is converted from a `.png` file.
 For more information about iOS image size and resolution, see [Image Size and Resolution ](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/) in the *Apple Human Interface Guidelines*.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 1770000.
Required: No

 ** SupportEmail **   <a name="WorkSpaces-Type-IosImportClientBrandingAttributes-SupportEmail"></a>
The support email. The company's customer support email address.
+ In each platform type, the `SupportEmail` and `SupportLink` parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.
+ The default email is `workspaces-feedback@amazon.com`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$`
Required: No

 ** SupportLink **   <a name="WorkSpaces-Type-IosImportClientBrandingAttributes-SupportLink"></a>
The support link. The link for the company's customer support page for their WorkSpace.
+ In each platform type, the `SupportEmail` and `SupportLink` parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.
+ The default support link is `workspaces-feedback@amazon.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(http|https)\://\S+`
Required: No

## See Also
<a name="API_IosImportClientBrandingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/IosImportClientBrandingAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/IosImportClientBrandingAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/IosImportClientBrandingAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
