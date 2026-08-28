---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html
---

# Managing rule groups and rules in DNS Firewall
<a name="resolver-dns-firewall-rule-group-managing"></a>

To manage rule groups and rules in the console, follow the guidance in this section.

When you make changes to DNS Firewall entities, like rules and domain lists, DNS Firewall propagates the changes everywhere that the entities are stored and used. Your changes are applied within seconds, but there might be a brief period of inconsistency when the changes have arrived in some places and not in others. So, for example, if you add a domain to a domain list that's referenced by a blocking rule, the new domain might briefly be blocked in one area of your VPC while still allowed in another. This temporary inconsistency can occur when you first configure your rule group and VPC associations and when you change existing settings. Generally, any inconsistencies of this type last only a few seconds.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
