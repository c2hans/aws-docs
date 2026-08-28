---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CustomizationConfiguration.html
---

# CustomizationConfiguration
<a name="API_CustomizationConfiguration"></a>

Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.

## Contents
<a name="API_CustomizationConfiguration_Contents"></a>

 ** customCSSUrl **   <a name="qbusiness-Type-CustomizationConfiguration-customCSSUrl"></a>
Provides the URL where the custom CSS file is hosted for an Amazon Q web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `(https?://[a-zA-Z0-9-_.+%/]+\.css)?`
Required: No

 ** faviconUrl **   <a name="qbusiness-Type-CustomizationConfiguration-faviconUrl"></a>
Provides the URL where the custom favicon file is hosted for an Amazon Q web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `(https?://[a-zA-Z0-9-_.+%/]+\.(svg|ico))?`
Required: No

 ** fontUrl **   <a name="qbusiness-Type-CustomizationConfiguration-fontUrl"></a>
Provides the URL where the custom font file is hosted for an Amazon Q web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `(https?://[a-zA-Z0-9-_.+%/]+\.(ttf|woff|woff2|otf))?`
Required: No

 ** logoUrl **   <a name="qbusiness-Type-CustomizationConfiguration-logoUrl"></a>
Provides the URL where the custom logo file is hosted for an Amazon Q web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `(https?://[a-zA-Z0-9-_.+%/]+\.(svg|png))?`
Required: No

## See Also
<a name="API_CustomizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CustomizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CustomizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CustomizationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
