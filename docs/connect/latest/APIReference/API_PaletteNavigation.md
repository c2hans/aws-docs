---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PaletteNavigation.html
---

# PaletteNavigation
<a name="API_PaletteNavigation"></a>

Contains color configuration for navigation elements in a workspace theme.

## Contents
<a name="API_PaletteNavigation_Contents"></a>

 ** Background **   <a name="connect-Type-PaletteNavigation-Background"></a>
The background color of the navigation area.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** InvertActionsColors **   <a name="connect-Type-PaletteNavigation-InvertActionsColors"></a>
Whether to invert the colors of action buttons in the navigation area.
Type: Boolean
Required: No

 ** Text **   <a name="connect-Type-PaletteNavigation-Text"></a>
The text color in the navigation area.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** TextActive **   <a name="connect-Type-PaletteNavigation-TextActive"></a>
The text color for active navigation items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** TextBackgroundActive **   <a name="connect-Type-PaletteNavigation-TextBackgroundActive"></a>
The background color for active navigation items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** TextBackgroundHover **   <a name="connect-Type-PaletteNavigation-TextBackgroundHover"></a>
The background color when hovering over navigation text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** TextHover **   <a name="connect-Type-PaletteNavigation-TextHover"></a>
The text color when hovering over navigation items.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

## See Also
<a name="API_PaletteNavigation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PaletteNavigation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PaletteNavigation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PaletteNavigation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
