---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ExcludedRule.html
---

# ExcludedRule
<a name="API_ExcludedRule"></a>

Specifies a single rule in a rule group whose action you want to override to `Count`.

**Note**
Instead of this option, use `RuleActionOverrides`. It accepts any valid action setting, including `Count`.

## Contents
<a name="API_ExcludedRule_Contents"></a>

 ** Name **   <a name="WAF-Type-ExcludedRule-Name"></a>
The name of the rule whose action you want to override to `Count`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

## See Also
<a name="API_ExcludedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ExcludedRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ExcludedRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ExcludedRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
