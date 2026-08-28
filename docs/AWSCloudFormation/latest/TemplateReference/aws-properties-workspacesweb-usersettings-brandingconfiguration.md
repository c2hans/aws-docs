---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-usersettings-brandingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::UserSettings BrandingConfiguration
<a name="aws-properties-workspacesweb-usersettings-brandingconfiguration"></a>

The branding configuration that customizes the appearance of the web portal for end users. This includes a custom logo, favicon, localized strings, color theme, and optionally a wallpaper and terms of service. If you use an empty string as the wallpaper input during an update, it will remove your previously uploaded wallpaper and use the default wallpaper instead.

**Note**
The `LogoMetadata`, `FaviconMetadata`, and `WallpaperMetadata` properties are read-only and cannot be specified in your template. They are automatically populated by the service after you upload images and can be retrieved using the `Fn::GetAtt` intrinsic function.

## Syntax
<a name="aws-properties-workspacesweb-usersettings-brandingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-usersettings-brandingconfiguration-syntax.json"></a>

```
{
  "[ColorTheme](#cfn-workspacesweb-usersettings-brandingconfiguration-colortheme)" : {{String}},
  "[Favicon](#cfn-workspacesweb-usersettings-brandingconfiguration-favicon)" : {{String}},
  "[FaviconMetadata](#cfn-workspacesweb-usersettings-brandingconfiguration-faviconmetadata)" : {{ImageMetadata}},
  "[LocalizedStrings](#cfn-workspacesweb-usersettings-brandingconfiguration-localizedstrings)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Logo](#cfn-workspacesweb-usersettings-brandingconfiguration-logo)" : {{String}},
  "[LogoMetadata](#cfn-workspacesweb-usersettings-brandingconfiguration-logometadata)" : {{ImageMetadata}},
  "[TermsOfService](#cfn-workspacesweb-usersettings-brandingconfiguration-termsofservice)" : {{String}},
  "[Wallpaper](#cfn-workspacesweb-usersettings-brandingconfiguration-wallpaper)" : {{String}},
  "[WallpaperMetadata](#cfn-workspacesweb-usersettings-brandingconfiguration-wallpapermetadata)" : {{ImageMetadata}}
}
```

### YAML
<a name="aws-properties-workspacesweb-usersettings-brandingconfiguration-syntax.yaml"></a>

```
  [ColorTheme](#cfn-workspacesweb-usersettings-brandingconfiguration-colortheme): {{String}}
  [Favicon](#cfn-workspacesweb-usersettings-brandingconfiguration-favicon): {{String}}
  [FaviconMetadata](#cfn-workspacesweb-usersettings-brandingconfiguration-faviconmetadata): {{
    ImageMetadata}}
  [LocalizedStrings](#cfn-workspacesweb-usersettings-brandingconfiguration-localizedstrings): {{
    {{Key}}: {{Value}}}}
  [Logo](#cfn-workspacesweb-usersettings-brandingconfiguration-logo): {{String}}
  [LogoMetadata](#cfn-workspacesweb-usersettings-brandingconfiguration-logometadata): {{
    ImageMetadata}}
  [TermsOfService](#cfn-workspacesweb-usersettings-brandingconfiguration-termsofservice): {{String}}
  [Wallpaper](#cfn-workspacesweb-usersettings-brandingconfiguration-wallpaper): {{String}}
  [WallpaperMetadata](#cfn-workspacesweb-usersettings-brandingconfiguration-wallpapermetadata): {{
    ImageMetadata}}
```

## Properties
<a name="aws-properties-workspacesweb-usersettings-brandingconfiguration-properties"></a>

`ColorTheme`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-colortheme"></a>
The color theme for components on the web portal. Choose `Light` if you upload a dark wallpaper, or `Dark` for a light wallpaper.
*Required*: No
*Type*: String
*Allowed values*: `Light | Dark`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Favicon`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-favicon"></a>
The favicon image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.
*Required*: No
*Type*: String
*Pattern*: `(^s3://[a-z0-9][a-z0-9\.\-]{1,61}[a-z0-9]/.+$)|(^(?=(.{4})*$)[A-Za-z0-9+/]*={0,2}$)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FaviconMetadata`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-faviconmetadata"></a>
Read-only. Metadata for the favicon image file, including the MIME type, file extension, and upload timestamp. This property is automatically populated by the service and cannot be specified in your template. It can be retrieved using the `Fn::GetAtt` intrinsic function.
*Required*: No
*Type*: [ImageMetadata](aws-properties-workspacesweb-usersettings-imagemetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalizedStrings`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-localizedstrings"></a>
A map of localized text strings for different languages, allowing the portal to display content in the user's preferred language.
*Required*: No
*Type*: Object of [LocalizedBrandingStrings](aws-properties-workspacesweb-usersettings-localizedbrandingstrings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logo`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-logo"></a>
The logo image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 100 KB in JPEG, PNG, or ICO format.
*Required*: No
*Type*: String
*Pattern*: `(^s3://[a-z0-9][a-z0-9\.\-]{1,61}[a-z0-9]/.+$)|(^(?=(.{4})*$)[A-Za-z0-9+/]*={0,2}$)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogoMetadata`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-logometadata"></a>
Read-only. Metadata for the logo image file, including the MIME type, file extension, and upload timestamp. This property is automatically populated by the service and cannot be specified in your template. It can be retrieved using the `Fn::GetAtt` intrinsic function.
*Required*: No
*Type*: [ImageMetadata](aws-properties-workspacesweb-usersettings-imagemetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TermsOfService`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-termsofservice"></a>
The terms of service text in Markdown format that users must accept before accessing the portal.
*Required*: No
*Type*: String
*Maximum*: `153600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Wallpaper`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-wallpaper"></a>
The wallpaper image for the portal. Provide either a binary image file or an S3 URI pointing to the image file. Maximum 5 MB in JPEG or PNG format. If not provided, a default wallpaper will be used as the background image.
*Required*: No
*Type*: String
*Pattern*: `(^s3://[a-z0-9][a-z0-9\.\-]{1,61}[a-z0-9]/.+$)|(^(?=(.{4})*$)[A-Za-z0-9+/]*={0,2}$)`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WallpaperMetadata`  <a name="cfn-workspacesweb-usersettings-brandingconfiguration-wallpapermetadata"></a>
Read-only. Metadata for the wallpaper image file, including the MIME type, file extension, and upload timestamp. This property is automatically populated by the service and cannot be specified in your template. It can be retrieved using the `Fn::GetAtt` intrinsic function.
*Required*: No
*Type*: [ImageMetadata](aws-properties-workspacesweb-usersettings-imagemetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
