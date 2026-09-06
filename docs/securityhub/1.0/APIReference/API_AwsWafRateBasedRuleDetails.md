---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRateBasedRuleDetails.html
---

# AwsWafRateBasedRuleDetails
<a name="API_AwsWafRateBasedRuleDetails"></a>

Details about a rate-based rule for global resources. A rate-based rule provides settings to indicate when to allow, block, or count a request. Rate-based rules include the number of requests that arrive over a specified period of time.

## Contents
<a name="API_AwsWafRateBasedRuleDetails_Contents"></a>

 ** MatchPredicates **   <a name="securityhub-Type-AwsWafRateBasedRuleDetails-MatchPredicates"></a>
The predicates to include in the rate-based rule.
Type: Array of [AwsWafRateBasedRuleMatchPredicate](API_AwsWafRateBasedRuleMatchPredicate.md) objects
Required: No

 ** MetricName **   <a name="securityhub-Type-AwsWafRateBasedRuleDetails-MetricName"></a>
The name of the metrics for the rate-based rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafRateBasedRuleDetails-Name"></a>
The name of the rate-based rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RateKey **   <a name="securityhub-Type-AwsWafRateBasedRuleDetails-RateKey"></a>
The field that AWS WAF uses to determine whether requests are likely arriving from single source and are subject to rate monitoring.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RateLimit **   <a name="securityhub-Type-AwsWafRateBasedRuleDetails-RateLimit"></a>
The maximum number of requests that have an identical value for the field specified in `RateKey` that are allowed within a five-minute period. If the number of requests exceeds `RateLimit` and the other predicates specified in the rule are met, AWS WAF triggers the action for the rule.
Type: Long
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafRateBasedRuleDetails-RuleId"></a>
The unique identifier for the rate-based rule.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRateBasedRuleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRateBasedRuleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRateBasedRuleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRateBasedRuleDetails)
