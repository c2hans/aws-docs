---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallRuleGroup.html
---

# FirewallRuleGroup
<a name="API_FirewallRuleGroup"></a>

The object that defines a firewall engine rule group, for use in a Next Generation policy. A firewall engine rule group provides access-control rules that the firewall engine evaluates at connection-state hooks. You provide the rules as a Suricata-compatible rule string, as structured firewall rules, or generated from a list of domain names. For more information, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide*.

## Contents
<a name="API_FirewallRuleGroup_Contents"></a>

 ** RulesSource **   <a name="networkfirewall-Type-FirewallRuleGroup-RulesSource"></a>
The stateful inspection criteria for the firewall engine rule group.
Type: [FirewallRulesSource](API_FirewallRulesSource.md) object
Required: Yes

 ** ReferenceSets **   <a name="networkfirewall-Type-FirewallRuleGroup-ReferenceSets"></a>
The list of a rule group's reference sets. Firewall engine rule groups don't support IP set references (reference sets); this setting applies to IPS engine rule groups. To use CIDR ranges in firewall engine rules, use rule variables instead.
Type: [ReferenceSets](API_ReferenceSets.md) object
Required: No

 ** RuleVariables **   <a name="networkfirewall-Type-FirewallRuleGroup-RuleVariables"></a>
Settings that are available for use in the rules in the firewall engine rule group, such as IP set and port variables that the rules reference.
Type: [RuleVariables](API_RuleVariables.md) object
Required: No

## See Also
<a name="API_FirewallRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallRuleGroup)
