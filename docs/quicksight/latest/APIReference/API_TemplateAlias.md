---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TemplateAlias.html
---

# TemplateAlias
<a name="API_TemplateAlias"></a>

The template alias.

## Contents
<a name="API_TemplateAlias_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AliasName **   <a name="QS-Type-TemplateAlias-AliasName"></a>
The display name of the template alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)`
Required: No

 ** Arn **   <a name="QS-Type-TemplateAlias-Arn"></a>
The Amazon Resource Name (ARN) of the template alias.
Type: String
Required: No

 ** TemplateVersionNumber **   <a name="QS-Type-TemplateAlias-TemplateVersionNumber"></a>
The version number of the template alias.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_TemplateAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TemplateAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TemplateAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TemplateAlias)
