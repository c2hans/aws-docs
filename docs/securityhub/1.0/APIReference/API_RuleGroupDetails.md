---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupDetails.html
---

# RuleGroupDetails
<a name="API_RuleGroupDetails"></a>

Details about the rule group.

## Contents
<a name="API_RuleGroupDetails_Contents"></a>

 ** RulesSource **   <a name="securityhub-Type-RuleGroupDetails-RulesSource"></a>
The rules and actions for the rule group.
For stateful rule groups, can contain `RulesString`, `RulesSourceList`, or `StatefulRules`.
For stateless rule groups, contains `StatelessRulesAndCustomActions`.
Type: [RuleGroupSource](API_RuleGroupSource.md) object
Required: No

 ** RuleVariables **   <a name="securityhub-Type-RuleGroupDetails-RuleVariables"></a>
Additional settings to use in the specified rules.
Type: [RuleGroupVariables](API_RuleGroupVariables.md) object
Required: No

## See Also
<a name="API_RuleGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
