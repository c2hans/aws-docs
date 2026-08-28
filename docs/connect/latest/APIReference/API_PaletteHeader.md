---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PaletteHeader.html
---

# PaletteHeader
<a name="API_PaletteHeader"></a>

Contains color configuration for header elements in a workspace theme.

## Contents
<a name="API_PaletteHeader_Contents"></a>

 ** Background **   <a name="connect-Type-PaletteHeader-Background"></a>
The background color of the header.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** InvertActionsColors **   <a name="connect-Type-PaletteHeader-InvertActionsColors"></a>
Whether to invert the colors of action buttons in the header.
Type: Boolean
Required: No

 ** Text **   <a name="connect-Type-PaletteHeader-Text"></a>
The text color in the header.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** TextHover **   <a name="connect-Type-PaletteHeader-TextHover"></a>
The text color when hovering over header elements.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

## See Also
<a name="API_PaletteHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PaletteHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PaletteHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PaletteHeader)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
