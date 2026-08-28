---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_StatefulRuleGroup.html
---

# StatefulRuleGroup
<a name="API_StatefulRuleGroup"></a>

 AWS Network Firewall stateful rule group, used in a [NetworkFirewallPolicyDescription](API_NetworkFirewallPolicyDescription.md).

## Contents
<a name="API_StatefulRuleGroup_Contents"></a>

 ** Override **   <a name="fms-Type-StatefulRuleGroup-Override"></a>
The action that allows the policy owner to override the behavior of the rule group within a policy.
Type: [NetworkFirewallStatefulRuleGroupOverride](API_NetworkFirewallStatefulRuleGroupOverride.md) object
Required: No

 ** Priority **   <a name="fms-Type-StatefulRuleGroup-Priority"></a>
An integer setting that indicates the order in which to run the stateful rule groups in a single Network Firewall firewall policy. This setting only applies to firewall policies that specify the `STRICT_ORDER` rule order in the stateful engine options settings.
 Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy. For information about
 You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so there's a wide range in between, for example use 100, 200, and so on.
Type: Integer
Required: No

 ** ResourceId **   <a name="fms-Type-StatefulRuleGroup-ResourceId"></a>
The resource ID of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** RuleGroupName **   <a name="fms-Type-StatefulRuleGroup-RuleGroupName"></a>
The name of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## See Also
<a name="API_StatefulRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/StatefulRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/StatefulRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/StatefulRuleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
