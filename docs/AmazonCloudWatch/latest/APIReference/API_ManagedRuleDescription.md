---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ManagedRuleDescription.html
---

# ManagedRuleDescription
<a name="API_ManagedRuleDescription"></a>

 Contains information about managed Contributor Insights rules, as returned by `ListManagedInsightRules`.

## Contents
<a name="API_ManagedRuleDescription_Contents"></a>

 ** ResourceARN **   <a name="ACW-Type-ManagedRuleDescription-ResourceARN"></a>
 If a managed rule is enabled, this is the ARN for the related AWS resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** RuleState **   <a name="ACW-Type-ManagedRuleDescription-RuleState"></a>
 Describes the state of a managed rule. If present, it contains information about the Contributor Insights rule that contains information about the related AWS resource.
Type: [ManagedRuleState](API_ManagedRuleState.md) object
Required: No

 ** TemplateName **   <a name="ACW-Type-ManagedRuleDescription-TemplateName"></a>
 The template name for the managed rule. Used to enable managed rules using `PutManagedInsightRules`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9A-Za-z][\-\.\_0-9A-Za-z]{0,126}[0-9A-Za-z]`
Required: No

## See Also
<a name="API_ManagedRuleDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ManagedRuleDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ManagedRuleDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ManagedRuleDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
