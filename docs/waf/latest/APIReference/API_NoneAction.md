---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_NoneAction.html
---

# NoneAction
<a name="API_NoneAction"></a>

Specifies that AWS WAF should do nothing. This is used for the `OverrideAction` setting on a [Rule](API_Rule.md) when the rule uses a rule group reference statement.

This is used in the context of other settings, for example to specify values for [RuleAction](API_RuleAction.md) and web ACL [DefaultAction](API_DefaultAction.md).

JSON specification: `"None": {}`

## Contents
<a name="API_NoneAction_Contents"></a>

The members of this exception structure are context-dependent.

## See Also
<a name="API_NoneAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/NoneAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/NoneAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/NoneAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
