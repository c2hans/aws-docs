---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateThemeData.html
---

# CreateThemeData
<a name="API_CreateThemeData"></a>

Represents all of the information that is required to create a theme.

## Contents
<a name="API_CreateThemeData_Contents"></a>

 ** name **   <a name="amplifyuibuilder-Type-CreateThemeData-name"></a>
The name of the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** values **   <a name="amplifyuibuilder-Type-CreateThemeData-values"></a>
A list of key-value pairs that deﬁnes the properties of the theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: Yes

 ** overrides **   <a name="amplifyuibuilder-Type-CreateThemeData-overrides"></a>
Describes the properties that can be overriden to customize an instance of the theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-CreateThemeData-tags"></a>
One or more key-value pairs to use when tagging the theme data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_CreateThemeData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CreateThemeData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CreateThemeData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CreateThemeData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
