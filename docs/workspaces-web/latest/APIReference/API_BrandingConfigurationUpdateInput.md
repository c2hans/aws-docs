---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_BrandingConfigurationUpdateInput.html
---

# BrandingConfigurationUpdateInput
<a name="API_BrandingConfigurationUpdateInput"></a>

The input configuration for updating branding settings. All fields are optional when updating existing branding.

## Contents
<a name="API_BrandingConfigurationUpdateInput_Contents"></a>

 ** colorTheme **   <a name="workspacesweb-Type-BrandingConfigurationUpdateInput-colorTheme"></a>
The color theme for components on the web portal. Choose `Light` if you upload a dark wallpaper, or `Dark` for a light wallpaper.
Type: String
Valid Values: `Light | Dark`
Required: No

 ** favicon **   <a name="workspacesweb-Type-BrandingConfigurationUpdateInput-favicon"></a>
The favicon image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.
Type: [IconImageInput](API_IconImageInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** localizedStrings **   <a name="workspacesweb-Type-BrandingConfigurationUpdateInput-localizedStrings"></a>
A map of localized text strings for different supported languages. Each locale must provide the required fields `browserTabTitle` and `welcomeText`.
Type: String to [LocalizedBrandingStrings](API_LocalizedBrandingStrings.md) object map
Valid Keys: `de-DE | en-US | es-ES | fr-FR | id-ID | it-IT | ja-JP | ko-KR | pt-BR | zh-CN | zh-TW`
Required: No

 ** logo **   <a name="workspacesweb-Type-BrandingConfigurationUpdateInput-logo"></a>
The logo image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.
Type: [IconImageInput](API_IconImageInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** termsOfService **   <a name="workspacesweb-Type-BrandingConfigurationUpdateInput-termsOfService"></a>
The terms of service text in Markdown format. To remove existing terms of service, provide an empty string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 153600.
Required: No

 ** wallpaper **   <a name="workspacesweb-Type-BrandingConfigurationUpdateInput-wallpaper"></a>
The wallpaper image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 5 MB in JPEG or PNG format.
Type: [WallpaperImageInput](API_WallpaperImageInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_BrandingConfigurationUpdateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/BrandingConfigurationUpdateInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/BrandingConfigurationUpdateInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/BrandingConfigurationUpdateInput)
