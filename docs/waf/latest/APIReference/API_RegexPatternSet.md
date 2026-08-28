---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RegexPatternSet.html
---

# RegexPatternSet
<a name="API_RegexPatternSet"></a>

Contains one or more regular expressions.

 AWS WAF assigns an ARN to each `RegexPatternSet` that you create. To use a set in a rule, you provide the ARN to the [Rule](API_Rule.md) statement [RegexPatternSetReferenceStatement](API_RegexPatternSetReferenceStatement.md).

## Contents
<a name="API_RegexPatternSet_Contents"></a>

 ** ARN **   <a name="WAF-Type-RegexPatternSet-ARN"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="WAF-Type-RegexPatternSet-Description"></a>
A description of the set that helps with identification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

 ** Id **   <a name="WAF-Type-RegexPatternSet-Id"></a>
A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

 ** Name **   <a name="WAF-Type-RegexPatternSet-Name"></a>
The name of the set. You cannot change the name after you create the set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

 ** RegularExpressionList **   <a name="WAF-Type-RegexPatternSet-RegularExpressionList"></a>
The regular expression patterns in the set.
Type: Array of [Regex](API_Regex.md) objects
Required: No

## See Also
<a name="API_RegexPatternSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RegexPatternSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RegexPatternSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RegexPatternSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
