---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Theme.html
---

# Theme
<a name="API_Theme"></a>

The custom branding theme, which might include a custom logo, website links, and other branding to display to users.

## Contents
<a name="API_Theme_Contents"></a>

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-Theme-CreatedTime"></a>
The time the theme was created.
Type: Timestamp
Required: No

 ** StackName **   <a name="WorkSpacesApplications-Type-Theme-StackName"></a>
The stack that has the custom branding theme.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: No

 ** State **   <a name="WorkSpacesApplications-Type-Theme-State"></a>
The state of the theme.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** ThemeFaviconURL **   <a name="WorkSpacesApplications-Type-Theme-ThemeFaviconURL"></a>
The URL of the icon that displays at the top of a user's browser tab during streaming sessions.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ThemeFooterLinks **   <a name="WorkSpacesApplications-Type-Theme-ThemeFooterLinks"></a>
The website links that display in the catalog page footer.
Type: Array of [ThemeFooterLink](API_ThemeFooterLink.md) objects
Required: No

 ** ThemeOrganizationLogoURL **   <a name="WorkSpacesApplications-Type-Theme-ThemeOrganizationLogoURL"></a>
The URL of the logo that displays in the catalog page header.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ThemeStyling **   <a name="WorkSpacesApplications-Type-Theme-ThemeStyling"></a>
The color that is used for the website links, text, buttons, and catalog page background.
Type: String
Valid Values: `LIGHT_BLUE | BLUE | PINK | RED`
Required: No

 ** ThemeTitleText **   <a name="WorkSpacesApplications-Type-Theme-ThemeTitleText"></a>
The browser tab page title.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[-@./#&+\w\s]*$`
Required: No

## See Also
<a name="API_Theme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Theme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Theme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Theme)
