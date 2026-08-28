---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-domain-lists.html
---

# DNS Firewall Foundational Rules
<a name="resolver-dns-firewall-domain-lists"></a>

DNS Firewall Foundational rules provide you with the essential DNS protections to help you get started with DNS Firewall, with two main types of foundational rules:
+ Managed domain lists, which AWS creates and maintains for you.
+ Your own domain lists, which you create and maintain. You can use a single domain list in multiple rules and any updates that you do to the domain list automatically affect all rules that use it.

A *domain list* is a reusable set of domain specifications that you use in a DNS Firewall rule, inside a rule group. When you associate a rule group with a VPC, DNS Firewall compares your DNS queries against the domain lists that are used in the rules. If it finds a match, it handles the DNS query according to the matching rule's action. For more information about rule groups and rules, see [DNS Firewall rule groups and rules](resolver-dns-firewall-rule-groups.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
