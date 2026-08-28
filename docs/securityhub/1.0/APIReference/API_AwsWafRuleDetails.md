---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRuleDetails.html
---

# AwsWafRuleDetails
<a name="API_AwsWafRuleDetails"></a>

Provides information about a AWS WAF rule. This rule specifies the web requests that you want to allow, block, or count.

## Contents
<a name="API_AwsWafRuleDetails_Contents"></a>

 ** MetricName **   <a name="securityhub-Type-AwsWafRuleDetails-MetricName"></a>
The name of the metrics for this rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafRuleDetails-Name"></a>
A descriptive name for the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PredicateList **   <a name="securityhub-Type-AwsWafRuleDetails-PredicateList"></a>
Specifies the `ByteMatchSet`, `IPSet`, `SqlInjectionMatchSet`, `XssMatchSet`, `RegexMatchSet`, `GeoMatchSet`, and `SizeConstraintSet` objects that you want to add to a rule and, for each object, indicates whether you want to negate the settings.
Type: Array of [AwsWafRulePredicateListDetails](API_AwsWafRulePredicateListDetails.md) objects
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafRuleDetails-RuleId"></a>
The ID of the AWS WAF rule.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRuleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRuleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRuleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRuleDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
