---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatelessRuleGroupReference.html
---

# StatelessRuleGroupReference
<a name="API_StatelessRuleGroupReference"></a>

Identifier for a single stateless rule group, used in a firewall policy to refer to the rule group.

## Contents
<a name="API_StatelessRuleGroupReference_Contents"></a>

 ** Priority **   <a name="networkfirewall-Type-StatelessRuleGroupReference-Priority"></a>
An integer setting that indicates the order in which to run the stateless rule groups in a single [FirewallPolicy](API_FirewallPolicy.md). Network Firewall applies each stateless rule group to a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** ResourceArn **   <a name="networkfirewall-Type-StatelessRuleGroupReference-ResourceArn"></a>
The Amazon Resource Name (ARN) of the stateless rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: Yes

## See Also
<a name="API_StatelessRuleGroupReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatelessRuleGroupReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatelessRuleGroupReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatelessRuleGroupReference)
