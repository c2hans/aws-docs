---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-settings.html
---

# Rule group settings in DNS Firewall
<a name="resolver-dns-firewall-rule-group-settings"></a>

When you create or edit a DNS Firewall rule group, you specify the following values:

**Name**
A unique name that lets you easily find a rule group on the dashboard.

**(Optional) Description**
A short description that provides more context for the rule group.

**Region**
The AWS Region that you choose when you create the rule group. A rule group that you create in one Region is available only in that Region. To use the same rule group in more than one Region, you must create it in each Region.

**Rules**
The rule group filtering behavior is contained in its rules. For information, see the following section.

**Tags**
Specify one or more keys and the corresponding values. For example, you might specify **Cost center** for **Key** and specify **456** for **Value**.
These are the tags that AWS Billing and Cost Management provides for organizing your AWS bill. For more information about using tags for cost allocation, see [Using cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide* .

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
