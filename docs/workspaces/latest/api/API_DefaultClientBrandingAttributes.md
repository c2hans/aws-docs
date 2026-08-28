---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DefaultClientBrandingAttributes.html
---

# DefaultClientBrandingAttributes
<a name="API_DefaultClientBrandingAttributes"></a>

Returns default client branding attributes that were imported. These attributes display on the client login screen.

**Important**
Client branding attributes are public facing. Ensure that you don't include sensitive information.

## Contents
<a name="API_DefaultClientBrandingAttributes_Contents"></a>

 ** ForgotPasswordLink **   <a name="WorkSpaces-Type-DefaultClientBrandingAttributes-ForgotPasswordLink"></a>
The forgotten password link. This is the web address that users can go to if they forget the password for their WorkSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(http|https)\://\S+`
Required: No

 ** LoginMessage **   <a name="WorkSpaces-Type-DefaultClientBrandingAttributes-LoginMessage"></a>
The login message. Specified as a key value pair, in which the key is a locale and the value is the localized message for that locale. The only key supported is `en_US`. The HTML tags supported include the following: `a, b, blockquote, br, cite, code, dd, dl, dt, div, em, i, li, ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul`.
Type: String to string map
Key Length Constraints: Fixed length of 5.
Key Pattern: `^[a-z]{2}_[A-Z]{2}$`
Value Length Constraints: Minimum length of 0. Maximum length of 2000.
Value Pattern: `^.*$`
Required: No

 ** LogoUrl **   <a name="WorkSpaces-Type-DefaultClientBrandingAttributes-LogoUrl"></a>
The logo. The only image format accepted is a binary data object that is converted from a `.png` file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(http|https)\://\S+`
Required: No

 ** SupportEmail **   <a name="WorkSpaces-Type-DefaultClientBrandingAttributes-SupportEmail"></a>
The support email. The company's customer support email address.
+ In each platform type, the `SupportEmail` and `SupportLink` parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.
+ The default email is `workspaces-feedback@amazon.com`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$`
Required: No

 ** SupportLink **   <a name="WorkSpaces-Type-DefaultClientBrandingAttributes-SupportLink"></a>
The support link. The link for the company's customer support page for their WorkSpace.
+ In each platform type, the `SupportEmail` and `SupportLink` parameters are mutually exclusive.You can specify one parameter for each platform type, but not both.
+ The default support link is `workspaces-feedback@amazon.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(http|https)\://\S+`
Required: No

## See Also
<a name="API_DefaultClientBrandingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DefaultClientBrandingAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DefaultClientBrandingAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DefaultClientBrandingAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
