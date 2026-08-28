---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRegionalRateBasedRuleDetails.html
---

# AwsWafRegionalRateBasedRuleDetails
<a name="API_AwsWafRegionalRateBasedRuleDetails"></a>

contains details about a rate-based rule for Regional resources. A rate-based rule provides settings to indicate when to allow, block, or count a request. Rate-based rules include the number of requests that arrive over a specified period of time.

## Contents
<a name="API_AwsWafRegionalRateBasedRuleDetails_Contents"></a>

 ** MatchPredicates **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleDetails-MatchPredicates"></a>
The predicates to include in the rate-based rule.
Type: Array of [AwsWafRegionalRateBasedRuleMatchPredicate](API_AwsWafRegionalRateBasedRuleMatchPredicate.md) objects
Required: No

 ** MetricName **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleDetails-MetricName"></a>
The name of the metrics for the rate-based rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleDetails-Name"></a>
The name of the rate-based rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RateKey **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleDetails-RateKey"></a>
The field that AWS WAF uses to determine whether requests are likely arriving from single source and are subject to rate monitoring.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RateLimit **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleDetails-RateLimit"></a>
The maximum number of requests that have an identical value for the field specified in `RateKey` that are allowed within a five-minute period. If the number of requests exceeds `RateLimit` and the other predicates specified in the rule are met, AWS WAF triggers the action for the rule.
Type: Long
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleDetails-RuleId"></a>
The unique identifier for the rate-based rule.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRegionalRateBasedRuleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRegionalRateBasedRuleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRegionalRateBasedRuleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRegionalRateBasedRuleDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
