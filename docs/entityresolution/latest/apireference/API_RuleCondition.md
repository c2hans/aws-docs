---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_RuleCondition.html
---

# RuleCondition
<a name="API_RuleCondition"></a>

An object that defines the `ruleCondition` and the `ruleName` to use in a matching workflow.

## Contents
<a name="API_RuleCondition_Contents"></a>

 ** condition **   <a name="API-Type-RuleCondition-condition"></a>
A statement that specifies the conditions for a matching rule.
If your data is accurate, use an Exact matching function: `Exact` or `ExactManyToMany`.
If your data has variations in spelling or pronunciation, use a Fuzzy matching function: `Cosine`, `Levenshtein`, or `Soundex`.
Use operators if you want to combine (`AND`), separate (`OR`), or group matching functions `(...)`.
For example: `(Cosine(a, 10) AND Exact(b, true)) OR ExactManyToMany(c, d)`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

 ** ruleName **   <a name="API-Type-RuleCondition-ruleName"></a>
A name for the matching rule.
For example: `Rule1`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: Yes

## See Also
<a name="API_RuleCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/RuleCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/RuleCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/RuleCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
