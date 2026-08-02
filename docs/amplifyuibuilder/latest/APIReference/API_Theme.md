---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Theme.html
---

# Theme
<a name="API_Theme"></a>

A theme is a collection of style settings that apply globally to the components associated with an Amplify application.

## Contents
<a name="API_Theme_Contents"></a>

 ** appId **   <a name="amplifyuibuilder-Type-Theme-appId"></a>
The unique ID for the Amplify app associated with the theme.
Type: String
Required: Yes

 ** createdAt **   <a name="amplifyuibuilder-Type-Theme-createdAt"></a>
The time that the theme was created.
Type: Timestamp
Required: Yes

 ** environmentName **   <a name="amplifyuibuilder-Type-Theme-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-Theme-id"></a>
The ID for the theme.
Type: String
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-Theme-name"></a>
The name of the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** values **   <a name="amplifyuibuilder-Type-Theme-values"></a>
A list of key-value pairs that defines the properties of the theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: Yes

 ** modifiedAt **   <a name="amplifyuibuilder-Type-Theme-modifiedAt"></a>
The time that the theme was modified.
Type: Timestamp
Required: No

 ** overrides **   <a name="amplifyuibuilder-Type-Theme-overrides"></a>
Describes the properties that can be overriden to customize a theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-Theme-tags"></a>
One or more key-value pairs to use when tagging the theme.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Theme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/Theme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/Theme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/Theme)
