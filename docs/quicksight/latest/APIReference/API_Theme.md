---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Theme.html
---

# Theme
<a name="API_Theme"></a>

Summary information about a theme.

## Contents
<a name="API_Theme_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-Theme-Arn"></a>
The Amazon Resource Name (ARN) of the theme.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-Theme-CreatedTime"></a>
The date and time that the theme was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-Theme-LastUpdatedTime"></a>
The date and time that the theme was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-Theme-Name"></a>
The name that the user gives to the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ThemeId **   <a name="QS-Type-Theme-ThemeId"></a>
The identifier that the user gives to the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** Type **   <a name="QS-Type-Theme-Type"></a>
The type of theme, based on how it was created. Valid values include: `QUICKSIGHT` and `CUSTOM`.
Type: String
Valid Values: `QUICKSIGHT | CUSTOM | ALL`
Required: No

 ** Version **   <a name="QS-Type-Theme-Version"></a>
A version of a theme.
Type: [ThemeVersion](API_ThemeVersion.md) object
Required: No

## See Also
<a name="API_Theme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Theme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Theme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Theme)
