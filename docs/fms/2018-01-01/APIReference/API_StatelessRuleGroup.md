---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_StatelessRuleGroup.html
---

# StatelessRuleGroup
<a name="API_StatelessRuleGroup"></a>

 AWS Network Firewall stateless rule group, used in a [NetworkFirewallPolicyDescription](API_NetworkFirewallPolicyDescription.md).

## Contents
<a name="API_StatelessRuleGroup_Contents"></a>

 ** Priority **   <a name="fms-Type-StatelessRuleGroup-Priority"></a>
The priority of the rule group. AWS Network Firewall evaluates the stateless rule groups in a firewall policy starting from the lowest priority setting.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** ResourceId **   <a name="fms-Type-StatelessRuleGroup-ResourceId"></a>
The resource ID of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** RuleGroupName **   <a name="fms-Type-StatelessRuleGroup-RuleGroupName"></a>
The name of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## See Also
<a name="API_StatelessRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/StatelessRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/StatelessRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/StatelessRuleGroup)
