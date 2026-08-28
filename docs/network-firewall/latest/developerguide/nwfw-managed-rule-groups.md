---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-managed-rule-groups.html
---

# Managed rule groups in AWS Network Firewall
<a name="nwfw-managed-rule-groups"></a>

Managed rule groups are collections of predefined, ready-to-use rules that AWS writes and maintains for you. Most AWS managed rule groups are available for at no additional cost to Network Firewall customers. The managed rule groups offered by Network Firewall combine thorough security coverage with the convenience and experitise of AWS managed solutions.

You can select one or more of the following rule groups to use in your Network Firewall policies:
+ **Active threat defense managed rule groups** – protect against active threats tracked by AWS threat intelligence.
+ **Domain and IP managed rule groups** – protect against domains known or suspected to be associated with malware or bots.
+ **Threat signature managed rule groups** – inspect for and defend against signatures that represent a variety of known threat categories.

Each set of managed rule groups counts as a single rule group toward the maximum number of stateful rule groups per firewall policy.

The following topics provide more details about the AWS managed rule groups supported by Network Firewall and how you can configure them to meet your security needs.

**Topics**
+ [AWS active threat defense for AWS Network Firewall](aws-managed-rule-groups-atd.md)
+ [AWS domain and IP managed rule groups for AWS Network Firewall](aws-managed-rule-groups-domain-list.md)
+ [AWS threat signature managed rule groups for AWS Network Firewall](aws-managed-rule-groups-threat-signature.md)
+ [Using AWS Marketplace rule groups](aws-marketplace-rule-groups.md)
+ [Working with AWS managed rule groups in the Network Firewall console](nwfw-using-managed-rule-groups-console.md)
+ [Troubleshooting AWS managed rule groups in Network Firewall](nwfw-using-managed-rule-groups-mitigating-false-positive.md)
+ [Considerations and disclaimers for using AWS managed rule groups in Network Firewall](aws-managed-rule-groups-disclaimer.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
