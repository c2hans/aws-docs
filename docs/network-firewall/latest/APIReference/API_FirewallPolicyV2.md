---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicyV2.html
---

# FirewallPolicyV2
<a name="API_FirewallPolicyV2"></a>

The object that defines a Next Generation policy. This, along with the [FirewallPolicyV2Response](API_FirewallPolicyV2Response.md), define the policy.

A Next Generation policy defines how the firewall engine and IPS engine inspect and control your VPC network traffic. You define the policy as a firewall section and an IPS section, each a collection of rule groups, along with policy-wide settings such as the policy mode and default actions. For more information, see [Next Generation policies](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies-v2.html) in the * AWS Network Firewall Developer Guide*.

## Contents
<a name="API_FirewallPolicyV2_Contents"></a>

 ** FirewallDefaultAction **   <a name="networkfirewall-Type-FirewallPolicyV2-FirewallDefaultAction"></a>
The action that the firewall engine takes on traffic that doesn't match any firewall engine rule at a hook. The firewall engine is drop by default. You can set the default action to one of the following:
+  `DROP` - Block the traffic.
+  `ACCEPT` - Allow the traffic.
+  `REJECT` - Block the traffic and send a TCP reset packet back to the client.
+  `ALERT` - Allow the traffic and generate an alert log for the traffic that reaches the default action at every hook. This is distinct from setting the policy mode to `MONITOR`.
For more information, see [Next Generation policies](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies-v2.html) in the * AWS Network Firewall Developer Guide*.
Type: String
Valid Values: `DROP | ACCEPT | REJECT | ALERT`
Required: No

 ** FirewallRuleGroupEntries **   <a name="networkfirewall-Type-FirewallPolicyV2-FirewallRuleGroupEntries"></a>
The firewall section of the policy—the rule groups that the firewall engine evaluates. Each entry references an existing firewall engine rule group or embeds a rule group directly in the policy, and each entry has a unique priority that sets its evaluation order within the section.
Type: Array of [FirewallRuleGroupEntry](API_FirewallRuleGroupEntry.md) objects
Required: No

 ** IpsRuleGroupEntries **   <a name="networkfirewall-Type-FirewallPolicyV2-IpsRuleGroupEntries"></a>
The IPS section of the policy—the rule groups that the IPS engine evaluates. Each entry references an existing IPS engine rule group or embeds a rule group directly in the policy. IPS section entries don't use a priority.
Type: Array of [IpsRuleGroupEntry](API_IpsRuleGroupEntry.md) objects
Required: No

 ** PolicyMode **   <a name="networkfirewall-Type-FirewallPolicyV2-PolicyMode"></a>
Indicates whether the policy's engines enforce their verdicts or only report them. In `ENFORCE` mode, the firewall engine and IPS engine apply their verdicts to traffic. In `MONITOR` mode, the engines evaluate traffic and generate logs and metrics, but don't block traffic, so you can observe how a policy would behave before you enforce it. For more information, see [Next Generation policies](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies-v2.html) in the * AWS Network Firewall Developer Guide*.
Type: String
Valid Values: `ENFORCE | MONITOR`
Required: No

 ** PolicyVariables **   <a name="networkfirewall-Type-FirewallPolicyV2-PolicyVariables"></a>
Contains variables that you can use to override default Suricata settings in your Next Generation policy.
Type: [PolicyVariables](API_PolicyVariables.md) object
Required: No

 ** Route53ResolvedIPValidation **   <a name="networkfirewall-Type-FirewallPolicyV2-Route53ResolvedIPValidation"></a>
The settings that enable resolved IP validation for the Next Generation policy. Resolved IP validation verifies that a connection's destination IP address is one that the Amazon Route 53 Resolver returned in a DNS response for a domain. A VPC that's associated with the Route 53 Resolver DNS Firewall rule group that you specify must send the response. This checks how the destination IP address was obtained, instead of relying only on the domain that the client asserts in its TLS Server Name Indication (SNI) or HTTP `Host` header. For more information, see [Route53ResolvedIPValidation](API_Route53ResolvedIPValidation.md).
Type: [Route53ResolvedIPValidation](API_Route53ResolvedIPValidation.md) object
Required: No

 ** StatefulEngineOptions **   <a name="networkfirewall-Type-FirewallPolicyV2-StatefulEngineOptions"></a>
Additional options governing how the engines handle stateful traffic, such as the stream exception policy and flow timeouts.
Type: [StatefulEngineOptionsV2](API_StatefulEngineOptionsV2.md) object
Required: No

 ** TLSInspectionConfigurationArn **   <a name="networkfirewall-Type-FirewallPolicyV2-TLSInspectionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration to use to decrypt traffic for inspection. Next Generation policies support session holding only. For more information, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the * AWS Network Firewall Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

## See Also
<a name="API_FirewallPolicyV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallPolicyV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallPolicyV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallPolicyV2)
