---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRegionalRuleGroupDetails.html
---

# AwsWafRegionalRuleGroupDetails
<a name="API_AwsWafRegionalRuleGroupDetails"></a>

Provides information about an AWS WAF Regional rule group. The rule group is a collection of rules for inspecting and controlling web requests.

## Contents
<a name="API_AwsWafRegionalRuleGroupDetails_Contents"></a>

 ** MetricName **   <a name="securityhub-Type-AwsWafRegionalRuleGroupDetails-MetricName"></a>
A name for the metrics for this rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafRegionalRuleGroupDetails-Name"></a>
The descriptive name of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleGroupId **   <a name="securityhub-Type-AwsWafRegionalRuleGroupDetails-RuleGroupId"></a>
The ID of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Rules **   <a name="securityhub-Type-AwsWafRegionalRuleGroupDetails-Rules"></a>
Provides information about the rule statements used to identify the web requests that you want to allow, block, or count.
Type: Array of [AwsWafRegionalRuleGroupRulesDetails](API_AwsWafRegionalRuleGroupRulesDetails.md) objects
Required: No

## See Also
<a name="API_AwsWafRegionalRuleGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRegionalRuleGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRegionalRuleGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRegionalRuleGroupDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
