---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallPolicyDescription.html
---

# NetworkFirewallPolicyDescription
<a name="API_NetworkFirewallPolicyDescription"></a>

The definition of the AWS Network Firewall firewall policy.

## Contents
<a name="API_NetworkFirewallPolicyDescription_Contents"></a>

 ** StatefulDefaultActions **   <a name="fms-Type-NetworkFirewallPolicyDescription-StatefulDefaultActions"></a>
The default actions to take on a packet that doesn't match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order.
 Valid values of the stateful default action:
+ aws:drop\_strict
+ aws:drop\_established
+ aws:alert\_strict
+ aws:alert\_established
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** StatefulEngineOptions **   <a name="fms-Type-NetworkFirewallPolicyDescription-StatefulEngineOptions"></a>
Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.
Type: [StatefulEngineOptions](API_StatefulEngineOptions.md) object
Required: No

 ** StatefulRuleGroups **   <a name="fms-Type-NetworkFirewallPolicyDescription-StatefulRuleGroups"></a>
The stateful rule groups that are used in the Network Firewall firewall policy.
Type: Array of [StatefulRuleGroup](API_StatefulRuleGroup.md) objects
Required: No

 ** StatelessCustomActions **   <a name="fms-Type-NetworkFirewallPolicyDescription-StatelessCustomActions"></a>
Names of custom actions that are available for use in the stateless default actions settings.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** StatelessDefaultActions **   <a name="fms-Type-NetworkFirewallPolicyDescription-StatelessDefaultActions"></a>
The actions to take on packets that don't match any of the stateless rule groups.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** StatelessFragmentDefaultActions **   <a name="fms-Type-NetworkFirewallPolicyDescription-StatelessFragmentDefaultActions"></a>
The actions to take on packet fragments that don't match any of the stateless rule groups.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** StatelessRuleGroups **   <a name="fms-Type-NetworkFirewallPolicyDescription-StatelessRuleGroups"></a>
The stateless rule groups that are used in the Network Firewall firewall policy.
Type: Array of [StatelessRuleGroup](API_StatelessRuleGroup.md) objects
Required: No

## See Also
<a name="API_NetworkFirewallPolicyDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallPolicyDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallPolicyDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallPolicyDescription)
