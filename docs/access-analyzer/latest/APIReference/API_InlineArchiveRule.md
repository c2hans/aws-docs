---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InlineArchiveRule.html
---

# InlineArchiveRule
<a name="API_InlineArchiveRule"></a>

An criterion statement in an archive rule. Each archive rule may have multiple criteria.

## Contents
<a name="API_InlineArchiveRule_Contents"></a>

 ** filter **   <a name="accessanalyzer-Type-InlineArchiveRule-filter"></a>
The condition and values for a criterion.
Type: String to [Criterion](API_Criterion.md) object map
Required: Yes

 ** ruleName **   <a name="accessanalyzer-Type-InlineArchiveRule-ruleName"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

## See Also
<a name="API_InlineArchiveRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InlineArchiveRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InlineArchiveRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InlineArchiveRule)
