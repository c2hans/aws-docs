---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateThemeData.html
---

# UpdateThemeData
<a name="API_UpdateThemeData"></a>

Saves the data binding information for a theme.

## Contents
<a name="API_UpdateThemeData_Contents"></a>

 ** values **   <a name="amplifyuibuilder-Type-UpdateThemeData-values"></a>
A list of key-value pairs that define the theme's properties.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-UpdateThemeData-id"></a>
The unique ID of the theme to update.
Type: String
Required: No

 ** name **   <a name="amplifyuibuilder-Type-UpdateThemeData-name"></a>
The name of the theme to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** overrides **   <a name="amplifyuibuilder-Type-UpdateThemeData-overrides"></a>
Describes the properties that can be overriden to customize the theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: No

## See Also
<a name="API_UpdateThemeData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/UpdateThemeData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/UpdateThemeData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/UpdateThemeData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
