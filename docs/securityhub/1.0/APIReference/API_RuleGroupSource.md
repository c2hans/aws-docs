---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSource.html
---

# RuleGroupSource
<a name="API_RuleGroupSource"></a>

The rules and actions for the rule group.

## Contents
<a name="API_RuleGroupSource_Contents"></a>

 ** RulesSourceList **   <a name="securityhub-Type-RuleGroupSource-RulesSourceList"></a>
Stateful inspection criteria for a domain list rule group. A domain list rule group determines access by specific protocols to specific domains.
Type: [RuleGroupSourceListDetails](API_RuleGroupSourceListDetails.md) object
Required: No

 ** RulesString **   <a name="securityhub-Type-RuleGroupSource-RulesString"></a>
Stateful inspection criteria, provided in Suricata compatible intrusion prevention system (IPS) rules.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StatefulRules **   <a name="securityhub-Type-RuleGroupSource-StatefulRules"></a>
Suricata rule specifications.
Type: Array of [RuleGroupSourceStatefulRulesDetails](API_RuleGroupSourceStatefulRulesDetails.md) objects
Required: No

 ** StatelessRulesAndCustomActions **   <a name="securityhub-Type-RuleGroupSource-StatelessRulesAndCustomActions"></a>
The stateless rules and custom actions used by a stateless rule group.
Type: [RuleGroupSourceStatelessRulesAndCustomActionsDetails](API_RuleGroupSourceStatelessRulesAndCustomActionsDetails.md) object
Required: No

## See Also
<a name="API_RuleGroupSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
