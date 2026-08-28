---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSourceStatefulRulesDetails.html
---

# RuleGroupSourceStatefulRulesDetails
<a name="API_RuleGroupSourceStatefulRulesDetails"></a>

A Suricata rule specification.

## Contents
<a name="API_RuleGroupSourceStatefulRulesDetails_Contents"></a>

 ** Action **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesDetails-Action"></a>
Defines what Network Firewall should do with the packets in a traffic flow when the flow matches the stateful rule criteria.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Header **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesDetails-Header"></a>
The stateful inspection criteria for the rule.
Type: [RuleGroupSourceStatefulRulesHeaderDetails](API_RuleGroupSourceStatefulRulesHeaderDetails.md) object
Required: No

 ** RuleOptions **   <a name="securityhub-Type-RuleGroupSourceStatefulRulesDetails-RuleOptions"></a>
Additional options for the rule.
Type: Array of [RuleGroupSourceStatefulRulesOptionsDetails](API_RuleGroupSourceStatefulRulesOptionsDetails.md) objects
Required: No

## See Also
<a name="API_RuleGroupSourceStatefulRulesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSourceStatefulRulesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSourceStatefulRulesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSourceStatefulRulesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
