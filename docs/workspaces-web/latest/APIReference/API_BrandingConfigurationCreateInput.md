---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_BrandingConfigurationCreateInput.html
---

# BrandingConfigurationCreateInput
<a name="API_BrandingConfigurationCreateInput"></a>

The input configuration for creating branding settings.

## Contents
<a name="API_BrandingConfigurationCreateInput_Contents"></a>

 ** colorTheme **   <a name="workspacesweb-Type-BrandingConfigurationCreateInput-colorTheme"></a>
The color theme for components on the web portal. Choose `Light` if you upload a dark wallpaper, or `Dark` for a light wallpaper.
Type: String
Valid Values: `Light | Dark`
Required: Yes

 ** favicon **   <a name="workspacesweb-Type-BrandingConfigurationCreateInput-favicon"></a>
The favicon image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.
Type: [IconImageInput](API_IconImageInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** localizedStrings **   <a name="workspacesweb-Type-BrandingConfigurationCreateInput-localizedStrings"></a>
A map of localized text strings for different supported languages. Each locale must provide the required fields `browserTabTitle` and `welcomeText`.
Type: String to [LocalizedBrandingStrings](API_LocalizedBrandingStrings.md) object map
Valid Keys: `de-DE | en-US | es-ES | fr-FR | id-ID | it-IT | ja-JP | ko-KR | pt-BR | zh-CN | zh-TW`
Required: Yes

 ** logo **   <a name="workspacesweb-Type-BrandingConfigurationCreateInput-logo"></a>
The logo image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.
Type: [IconImageInput](API_IconImageInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** termsOfService **   <a name="workspacesweb-Type-BrandingConfigurationCreateInput-termsOfService"></a>
The terms of service text in Markdown format. Users will be presented with the terms of service after successfully signing in.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 153600.
Required: No

 ** wallpaper **   <a name="workspacesweb-Type-BrandingConfigurationCreateInput-wallpaper"></a>
The wallpaper image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 5 MB in JPEG or PNG format. If not provided, a default wallpaper will be used as the background image.
Type: [WallpaperImageInput](API_WallpaperImageInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_BrandingConfigurationCreateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/BrandingConfigurationCreateInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/BrandingConfigurationCreateInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/BrandingConfigurationCreateInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
