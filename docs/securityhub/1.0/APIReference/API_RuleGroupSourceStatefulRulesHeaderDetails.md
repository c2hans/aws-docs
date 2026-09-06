---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSourceStatefulRulesHeaderDetails.html
---

# RuleGroupSourceStatefulRulesHeaderDetails
<a name="API_RuleGroupSourceStatefulRulesHeaderDetails"></a>

The inspection criteria for a stateful rule.

## Contents
<a name="API_RuleGroupSourceStatefulRulesHeaderDetails_Contents"></a>

 ** Destination **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesHeaderDetails-Destination"></a>
The destination IP address or address range to inspect for, in CIDR notation. To match with any address, specify `ANY`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DestinationPort **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesHeaderDetails-DestinationPort"></a>
The destination port to inspect for. You can specify an individual port, such as `1994`. You also can specify a port range, such as `1990:1994`. To match with any port, specify `ANY`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Direction **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesHeaderDetails-Direction"></a>
The direction of traffic flow to inspect. If set to `ANY`, the inspection matches bidirectional traffic, both from the source to the destination and from the destination to the source. If set to `FORWARD`, the inspection only matches traffic going from the source to the destination.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Protocol **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesHeaderDetails-Protocol"></a>
The protocol to inspect for. To inspector for all protocols, use `IP`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Source **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesHeaderDetails-Source"></a>
The source IP address or address range to inspect for, in CIDR notation. To match with any address, specify `ANY`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourcePort **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesHeaderDetails-SourcePort"></a>
The source port to inspect for. You can specify an individual port, such as `1994`. You also can specify a port range, such as `1990:1994`. To match with any port, specify `ANY`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RuleGroupSourceStatefulRulesHeaderDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSourceStatefulRulesHeaderDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSourceStatefulRulesHeaderDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSourceStatefulRulesHeaderDetails)
