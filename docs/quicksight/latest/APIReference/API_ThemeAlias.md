---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ThemeAlias.html
---

# ThemeAlias
<a name="API_ThemeAlias"></a>

An alias for a theme.

## Contents
<a name="API_ThemeAlias_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AliasName **   <a name="QS-Type-ThemeAlias-AliasName"></a>
The display name of the theme alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)`
Required: No

 ** Arn **   <a name="QS-Type-ThemeAlias-Arn"></a>
The Amazon Resource Name (ARN) of the theme alias.
Type: String
Required: No

 ** ThemeVersionNumber **   <a name="QS-Type-ThemeAlias-ThemeVersionNumber"></a>
The version number of the theme alias.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ThemeAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ThemeAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ThemeAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ThemeAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
