---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSourceStatelessRuleMatchAttributes.html
---

# RuleGroupSourceStatelessRuleMatchAttributes
<a name="API_RuleGroupSourceStatelessRuleMatchAttributes"></a>

Criteria for the stateless rule.

## Contents
<a name="API_RuleGroupSourceStatelessRuleMatchAttributes_Contents"></a>

 ** DestinationPorts **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributes-DestinationPorts"></a>
A list of port ranges to specify the destination ports to inspect for.
Type: Array of [RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts](API_RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts.md) objects
Required: No

 ** Destinations **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributes-Destinations"></a>
The destination IP addresses and address ranges to inspect for, in CIDR notation.
Type: Array of [RuleGroupSourceStatelessRuleMatchAttributesDestinations](API_RuleGroupSourceStatelessRuleMatchAttributesDestinations.md) objects
Required: No

 ** Protocols **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributes-Protocols"></a>
The protocols to inspect for.
Type: Array of integers
Required: No

 ** SourcePorts **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributes-SourcePorts"></a>
A list of port ranges to specify the source ports to inspect for.
Type: Array of [RuleGroupSourceStatelessRuleMatchAttributesSourcePorts](API_RuleGroupSourceStatelessRuleMatchAttributesSourcePorts.md) objects
Required: No

 ** Sources **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributes-Sources"></a>
The source IP addresses and address ranges to inspect for, in CIDR notation.
Type: Array of [RuleGroupSourceStatelessRuleMatchAttributesSources](API_RuleGroupSourceStatelessRuleMatchAttributesSources.md) objects
Required: No

 ** TcpFlags **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributes-TcpFlags"></a>
The TCP flags and masks to inspect for.
Type: Array of [RuleGroupSourceStatelessRuleMatchAttributesTcpFlags](API_RuleGroupSourceStatelessRuleMatchAttributesTcpFlags.md) objects
Required: No

## See Also
<a name="API_RuleGroupSourceStatelessRuleMatchAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSourceStatelessRuleMatchAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSourceStatelessRuleMatchAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSourceStatelessRuleMatchAttributes)
