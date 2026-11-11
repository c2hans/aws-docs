---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallRulesSource.html
---

# FirewallRulesSource
<a name="API_FirewallRulesSource"></a>

The source of the rules for a firewall engine rule group. You provide the rules as a single Suricata-compatible rule string, as a list of structured firewall rules, or as a list of domain names to generate rules from.

## Contents
<a name="API_FirewallRulesSource_Contents"></a>

 ** FirewallRules **   <a name="networkfirewall-Type-FirewallRulesSource-FirewallRules"></a>
An array of individual firewall engine rules, provided as structured rules rather than as a rule string.
Type: Array of [FirewallRule](API_FirewallRule.md) objects
Required: No

 ** RulesSourceList **   <a name="networkfirewall-Type-FirewallRulesSource-RulesSourceList"></a>
Stateful inspection criteria for a domain list, specified as the list of domain names that Network Firewall generates firewall engine rules from.
Type: [RulesSourceList](API_RulesSourceList.md) object
Required: No

 ** RulesString **   <a name="networkfirewall-Type-FirewallRulesSource-RulesString"></a>
Firewall engine rules, provided as a single Suricata-compatible rule string in firewall mode. Use this to provide rules that you've already written in the Suricata firewall-mode format. For the rule format, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000000.
Required: No

## See Also
<a name="API_FirewallRulesSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallRulesSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallRulesSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallRulesSource)
