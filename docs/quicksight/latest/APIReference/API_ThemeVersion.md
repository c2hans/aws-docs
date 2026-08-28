---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ThemeVersion.html
---

# ThemeVersion
<a name="API_ThemeVersion"></a>

A version of a theme.

## Contents
<a name="API_ThemeVersion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-ThemeVersion-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** BaseThemeId **   <a name="QS-Type-ThemeVersion-BaseThemeId"></a>
The Quick Sight-defined ID of the theme that a custom theme inherits from. All themes initially inherit from a default Quick Sight theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** Configuration **   <a name="QS-Type-ThemeVersion-Configuration"></a>
The theme configuration, which contains all the theme display properties.
Type: [ThemeConfiguration](API_ThemeConfiguration.md) object
Required: No

 ** CreatedTime **   <a name="QS-Type-ThemeVersion-CreatedTime"></a>
The date and time that this theme version was created.
Type: Timestamp
Required: No

 ** Description **   <a name="QS-Type-ThemeVersion-Description"></a>
The description of the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Errors **   <a name="QS-Type-ThemeVersion-Errors"></a>
Errors associated with the theme.
Type: Array of [ThemeError](API_ThemeError.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Status **   <a name="QS-Type-ThemeVersion-Status"></a>
The status of the theme version.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** VersionNumber **   <a name="QS-Type-ThemeVersion-VersionNumber"></a>
The version number of the theme.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ThemeVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ThemeVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ThemeVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ThemeVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
