---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FirewallPolicyDetails.html
---

# FirewallPolicyDetails
<a name="API_FirewallPolicyDetails"></a>

Defines the behavior of the firewall.

## Contents
<a name="API_FirewallPolicyDetails_Contents"></a>

 ** StatefulRuleGroupReferences **   <a name="securityhub-Type-FirewallPolicyDetails-StatefulRuleGroupReferences"></a>
The stateful rule groups that are used in the firewall policy.
Type: Array of [FirewallPolicyStatefulRuleGroupReferencesDetails](API_FirewallPolicyStatefulRuleGroupReferencesDetails.md) objects
Required: No

 ** StatelessCustomActions **   <a name="securityhub-Type-FirewallPolicyDetails-StatelessCustomActions"></a>
The custom action definitions that are available to use in the firewall policy's `StatelessDefaultActions` setting.
Type: Array of [FirewallPolicyStatelessCustomActionsDetails](API_FirewallPolicyStatelessCustomActionsDetails.md) objects
Required: No

 ** StatelessDefaultActions **   <a name="securityhub-Type-FirewallPolicyDetails-StatelessDefaultActions"></a>
The actions to take on a packet if it doesn't match any of the stateless rules in the policy.
You must specify a standard action (`aws:pass`, `aws:drop`, `aws:forward_to_sfe`), and can optionally include a custom action from `StatelessCustomActions`.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** StatelessFragmentDefaultActions **   <a name="securityhub-Type-FirewallPolicyDetails-StatelessFragmentDefaultActions"></a>
The actions to take on a fragmented UDP packet if it doesn't match any of the stateless rules in the policy.
You must specify a standard action (`aws:pass`, `aws:drop`, `aws:forward_to_sfe`), and can optionally include a custom action from `StatelessCustomActions`.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** StatelessRuleGroupReferences **   <a name="securityhub-Type-FirewallPolicyDetails-StatelessRuleGroupReferences"></a>
The stateless rule groups that are used in the firewall policy.
Type: Array of [FirewallPolicyStatelessRuleGroupReferencesDetails](API_FirewallPolicyStatelessRuleGroupReferencesDetails.md) objects
Required: No

## See Also
<a name="API_FirewallPolicyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FirewallPolicyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FirewallPolicyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FirewallPolicyDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
