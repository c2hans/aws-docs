---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_BrandingConfiguration.html
---

# BrandingConfiguration
<a name="API_BrandingConfiguration"></a>

The branding configuration output including custom images metadata, localized strings, color theme, and terms of service.

## Contents
<a name="API_BrandingConfiguration_Contents"></a>

 ** colorTheme **   <a name="workspacesweb-Type-BrandingConfiguration-colorTheme"></a>
The color theme for components on the web portal.
Type: String
Valid Values: `Light | Dark`
Required: Yes

 ** favicon **   <a name="workspacesweb-Type-BrandingConfiguration-favicon"></a>
Metadata for the favicon image file, including the MIME type, file extension, and upload timestamp.
Type: [ImageMetadata](API_ImageMetadata.md) object
Required: Yes

 ** localizedStrings **   <a name="workspacesweb-Type-BrandingConfiguration-localizedStrings"></a>
A map of localized text strings for different languages, allowing the portal to display content in the user's preferred language.
Type: String to [LocalizedBrandingStrings](API_LocalizedBrandingStrings.md) object map
Valid Keys: `de-DE | en-US | es-ES | fr-FR | id-ID | it-IT | ja-JP | ko-KR | pt-BR | zh-CN | zh-TW`
Required: Yes

 ** logo **   <a name="workspacesweb-Type-BrandingConfiguration-logo"></a>
Metadata for the logo image file, including the MIME type, file extension, and upload timestamp.
Type: [ImageMetadata](API_ImageMetadata.md) object
Required: Yes

 ** termsOfService **   <a name="workspacesweb-Type-BrandingConfiguration-termsOfService"></a>
The terms of service text in Markdown format that users must accept before accessing the portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 153600.
Required: No

 ** wallpaper **   <a name="workspacesweb-Type-BrandingConfiguration-wallpaper"></a>
Metadata for the wallpaper image file, including the MIME type, file extension, and upload timestamp.
Type: [ImageMetadata](API_ImageMetadata.md) object
Required: No

## See Also
<a name="API_BrandingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/BrandingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/BrandingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/BrandingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
