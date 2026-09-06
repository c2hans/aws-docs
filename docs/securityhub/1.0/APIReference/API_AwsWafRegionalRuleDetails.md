---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRegionalRuleDetails.html
---

# AwsWafRegionalRuleDetails
<a name="API_AwsWafRegionalRuleDetails"></a>

Provides information about an AWS WAF Regional rule. This rule identifies the web requests that you want to allow, block, or count.

## Contents
<a name="API_AwsWafRegionalRuleDetails_Contents"></a>

 ** MetricName **   <a name="securityhub-Type-AwsWafRegionalRuleDetails-MetricName"></a>
A name for the metrics for the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafRegionalRuleDetails-Name"></a>
A descriptive name for the rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PredicateList **   <a name="securityhub-Type-AwsWafRegionalRuleDetails-PredicateList"></a>
Specifies the `ByteMatchSet`, `IPSet`, `SqlInjectionMatchSet`, `XssMatchSet`, `RegexMatchSet`, `GeoMatchSet`, and `SizeConstraintSet` objects that you want to add to a rule and, for each object, indicates whether you want to negate the settings.
Type: Array of [AwsWafRegionalRulePredicateListDetails](API_AwsWafRegionalRulePredicateListDetails.md) objects
Required: No

 ** RuleId **   <a name="securityhub-Type-AwsWafRegionalRuleDetails-RuleId"></a>
The ID of the rule.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRegionalRuleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRegionalRuleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRegionalRuleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRegionalRuleDetails)
