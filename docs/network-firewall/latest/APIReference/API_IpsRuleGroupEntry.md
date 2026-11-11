---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_IpsRuleGroupEntry.html
---

# IpsRuleGroupEntry
<a name="API_IpsRuleGroupEntry"></a>

A single entry in the IPS section of a Next Generation policy. An entry either references an existing IPS engine rule group by ARN or embeds a rule group directly in the policy. IPS section entries don't use a priority.

## Contents
<a name="API_IpsRuleGroupEntry_Contents"></a>

 ** InlineRuleGroup **   <a name="networkfirewall-Type-IpsRuleGroupEntry-InlineRuleGroup"></a>
An IPS engine rule group defined directly in the policy, instead of referenced by ARN. Provide either `InlineRuleGroup` to embed a rule group or `ResourceArn` to reference an existing rule group.
Type: [IpsRuleGroup](API_IpsRuleGroup.md) object
Required: No

 ** Override **   <a name="networkfirewall-Type-IpsRuleGroupEntry-Override"></a>
The setting that allows the policy owner to change the behavior of the IPS engine rule group within this policy, such as changing a managed rule group's action from `DROP` to `ALERT`.
Type: [IpsRuleGroupOverride](API_IpsRuleGroupOverride.md) object
Required: No

 ** ResourceArn **   <a name="networkfirewall-Type-IpsRuleGroupEntry-ResourceArn"></a>
The Amazon Resource Name (ARN) of an existing IPS engine rule group to reference in this entry. Provide either `ResourceArn` to reference an existing rule group or `InlineRuleGroup` to embed a rule group in the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

## See Also
<a name="API_IpsRuleGroupEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/IpsRuleGroupEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/IpsRuleGroupEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/IpsRuleGroupEntry)
