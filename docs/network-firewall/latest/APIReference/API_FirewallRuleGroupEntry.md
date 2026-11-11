---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallRuleGroupEntry.html
---

# FirewallRuleGroupEntry
<a name="API_FirewallRuleGroupEntry"></a>

A single entry in the firewall section of a Next Generation policy. An entry either references an existing firewall engine rule group by ARN or embeds a rule group directly in the policy, and it carries the priority that sets the rule group's evaluation order within the firewall section.

## Contents
<a name="API_FirewallRuleGroupEntry_Contents"></a>

 ** InlineRuleGroup **   <a name="networkfirewall-Type-FirewallRuleGroupEntry-InlineRuleGroup"></a>
A firewall engine rule group defined directly in the policy, instead of referenced by ARN. Provide either `InlineRuleGroup` to embed a rule group or `ResourceArn` to reference an existing rule group. An embedded rule group can't use a domain list rules source; to filter on a domain list, reference a standalone rule group by ARN instead.
Type: [FirewallRuleGroup](API_FirewallRuleGroup.md) object
Required: No

 ** Priority **   <a name="networkfirewall-Type-FirewallRuleGroupEntry-Priority"></a>
The priority of the rule group entry within the firewall section. AWS Network Firewall evaluates the firewall section's entries in order of increasing priority value. Each entry in the firewall section must have a unique priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** ResourceArn **   <a name="networkfirewall-Type-FirewallRuleGroupEntry-ResourceArn"></a>
The Amazon Resource Name (ARN) of an existing firewall engine rule group to reference in this entry. Provide either `ResourceArn` to reference an existing rule group or `InlineRuleGroup` to embed a rule group in the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

## See Also
<a name="API_FirewallRuleGroupEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallRuleGroupEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallRuleGroupEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallRuleGroupEntry)
