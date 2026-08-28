---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Summary.html
---

# Summary
<a name="API_Summary"></a>

A complex type containing summaries of security protections provided by a rule group.

Network Firewall extracts this information from selected fields in the rule group's Suricata rules, based on your [SummaryConfiguration](API_SummaryConfiguration.md) settings.

## Contents
<a name="API_Summary_Contents"></a>

 ** RuleSummaries **   <a name="networkfirewall-Type-Summary-RuleSummaries"></a>
An array of [RuleSummary](API_RuleSummary.md) objects containing individual rule details that had been configured by the rulegroup's SummaryConfiguration.
Type: Array of [RuleSummary](API_RuleSummary.md) objects
Required: No

## See Also
<a name="API_Summary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Summary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Summary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Summary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
