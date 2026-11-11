---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_IpsRuleGroup.html
---

# IpsRuleGroup
<a name="API_IpsRuleGroup"></a>

The object that defines an IPS engine rule group, for use in a Next Generation policy. An IPS engine rule group provides threat-detection rules that the IPS engine evaluates in the context of the traffic flow. You provide the rules as a Suricata-compatible rule string. For more information, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide*.

## Contents
<a name="API_IpsRuleGroup_Contents"></a>

 ** RulesSource **   <a name="networkfirewall-Type-IpsRuleGroup-RulesSource"></a>
The stateful inspection criteria for the IPS engine rule group.
Type: [IpsRulesSource](API_IpsRulesSource.md) object
Required: Yes

 ** ReferenceSets **   <a name="networkfirewall-Type-IpsRuleGroup-ReferenceSets"></a>
The list of a rule group's reference sets.
Type: [ReferenceSets](API_ReferenceSets.md) object
Required: No

 ** RuleVariables **   <a name="networkfirewall-Type-IpsRuleGroup-RuleVariables"></a>
Settings that are available for use in the rules in the IPS engine rule group.
Type: [RuleVariables](API_RuleVariables.md) object
Required: No

## See Also
<a name="API_IpsRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/IpsRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/IpsRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/IpsRuleGroup)
