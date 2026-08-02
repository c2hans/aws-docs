---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DefaultImportClientBrandingAttributes.html
---

# DefaultImportClientBrandingAttributes
<a name="API_DefaultImportClientBrandingAttributes"></a>

The default client branding attributes to be imported. These attributes display on the client login screen.

**Important**
Client branding attributes are public facing. Ensure that you do not include sensitive information.

## Contents
<a name="API_DefaultImportClientBrandingAttributes_Contents"></a>

 ** ForgotPasswordLink **   <a name="WorkSpaces-Type-DefaultImportClientBrandingAttributes-ForgotPasswordLink"></a>
The forgotten password link. This is the web address that users can go to if they forget the password for their WorkSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(http|https)\://\S+`
Required: No

 ** LoginMessage **   <a name="WorkSpaces-Type-DefaultImportClientBrandingAttributes-LoginMessage"></a>
The login message. Specified as a key value pair, in which the key is a locale and the value is the localized message for that locale. The only key supported is `en_US`. The HTML tags supported include the following: `a, b, blockquote, br, cite, code, dd, dl, dt, div, em, i, li, ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul`.
Type: String to string map
Key Length Constraints: Fixed length of 5.
Key Pattern: `^[a-z]{2}_[A-Z]{2}$`
Value Length Constraints: Minimum length of 0. Maximum length of 2000.
Value Pattern: `^.*$`
Required: No

 ** Logo **   <a name="WorkSpaces-Type-DefaultImportClientBrandingAttributes-Logo"></a>
The logo. The only image format accepted is a binary data object that is converted from a `.png` file.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 1500000.
Required: No

 ** SupportEmail **   <a name="WorkSpaces-Type-DefaultImportClientBrandingAttributes-SupportEmail"></a>
The support email. The company's customer support email address.
+ In each platform type, the `SupportEmail` and `SupportLink` parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.
+ The default email is `workspaces-feedback@amazon.com`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$`
Required: No

 ** SupportLink **   <a name="WorkSpaces-Type-DefaultImportClientBrandingAttributes-SupportLink"></a>
The support link. The link for the company's customer support page for their WorkSpace.
+ In each platform type, the `SupportEmail` and `SupportLink` parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.
+ The default support link is `workspaces-feedback@amazon.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(http|https)\://\S+`
Required: No

## See Also
<a name="API_DefaultImportClientBrandingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DefaultImportClientBrandingAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DefaultImportClientBrandingAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DefaultImportClientBrandingAttributes)
