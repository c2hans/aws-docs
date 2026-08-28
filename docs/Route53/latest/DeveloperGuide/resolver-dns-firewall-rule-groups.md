---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-groups.html
---

# DNS Firewall rule groups and rules
<a name="resolver-dns-firewall-rule-groups"></a>

This section describes the settings that you can configure for your DNS Firewall rule groups and rules, to define the DNS Firewall behavior for your VPCs. It also describes how to manage the settings for your rule groups and rules.

When you have your rule groups configured the way you want them, you use them directly and you can share and manage them between accounts and across your organization in AWS Organizations.
+ You can associate a rule group with multiple VPCs, to provide consistent behavior across your organization. For information, see [Managing associations between your VPC and Resolver DNS Firewall rule group](resolver-dns-firewall-vpc-associating-rule-group.md).
+ You can share rule groups between accounts, for consistent DNS query management across your organization. For information, see [Sharing Resolver DNS Firewall rule groups between AWS accounts](resolver-dns-firewall-rule-group-sharing.md).
+ You can use rule groups across your organization in AWS Organizations by managing them in AWS Firewall Manager policies. For information about Firewall Manager, see [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
