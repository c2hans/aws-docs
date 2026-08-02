---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRegionalRateBasedRuleMatchPredicate.html
---

# AwsWafRegionalRateBasedRuleMatchPredicate
<a name="API_AwsWafRegionalRateBasedRuleMatchPredicate"></a>

Details for a match predicate. A predicate might look for characteristics such as specific IP addresses, geographic locations, or sizes.

## Contents
<a name="API_AwsWafRegionalRateBasedRuleMatchPredicate_Contents"></a>

 ** DataId **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleMatchPredicate-DataId"></a>
The unique identifier for the predicate.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Negated **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleMatchPredicate-Negated"></a>
If set to `true`, then the rule actions are performed on requests that match the predicate settings.
If set to `false`, then the rule actions are performed on all requests except those that match the predicate settings.
Type: Boolean
Required: No

 ** Type **   <a name="securityhub-Type-AwsWafRegionalRateBasedRuleMatchPredicate-Type"></a>
The type of predicate. Valid values are as follows:
+  `ByteMatch`
+  `GeoMatch`
+  `IPMatch`
+  `RegexMatch`
+  `SizeConstraint`
+  `SqlInjectionMatch`
+  `XssMatch`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRegionalRateBasedRuleMatchPredicate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRegionalRateBasedRuleMatchPredicate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRegionalRateBasedRuleMatchPredicate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRegionalRateBasedRuleMatchPredicate)
