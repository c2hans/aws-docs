---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsNetworkFirewallRuleGroupDetails.html
---

# AwsNetworkFirewallRuleGroupDetails
<a name="API_AwsNetworkFirewallRuleGroupDetails"></a>

Details about an AWS Network Firewall rule group. Rule groups are used to inspect and control network traffic. Stateless rule groups apply to individual packets. Stateful rule groups apply to packets in the context of their traffic flow.

Rule groups are referenced in firewall policies.

## Contents
<a name="API_AwsNetworkFirewallRuleGroupDetails_Contents"></a>

 ** Capacity **   <a name="securityhub-Type-AwsNetworkFirewallRuleGroupDetails-Capacity"></a>
The maximum number of operating resources that this rule group can use.
Type: Integer
Required: No

 ** Description **   <a name="securityhub-Type-AwsNetworkFirewallRuleGroupDetails-Description"></a>
A description of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleGroup **   <a name="securityhub-Type-AwsNetworkFirewallRuleGroupDetails-RuleGroup"></a>
Details about the rule group.
Type: [RuleGroupDetails](API_RuleGroupDetails.md) object
Required: No

 ** RuleGroupArn **   <a name="securityhub-Type-AwsNetworkFirewallRuleGroupDetails-RuleGroupArn"></a>
The ARN of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleGroupId **   <a name="securityhub-Type-AwsNetworkFirewallRuleGroupDetails-RuleGroupId"></a>
The identifier of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleGroupName **   <a name="securityhub-Type-AwsNetworkFirewallRuleGroupDetails-RuleGroupName"></a>
The descriptive name of the rule group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsNetworkFirewallRuleGroupDetails-Type"></a>
The type of rule group. A rule group can be stateful or stateless.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsNetworkFirewallRuleGroupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsNetworkFirewallRuleGroupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsNetworkFirewallRuleGroupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsNetworkFirewallRuleGroupDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
