---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-partner-panw-best-practices.html
---

# Best practices for Palo Alto Networks partner managed rules
<a name="firewall-partner-panw-best-practices"></a>

We recommend the following best practices when using Palo Alto Networks partner managed DNS threat protection:
+ **Testing before production:** Before deploying to production, use `ALERT` mode to perform a dry run. Review alert logs, then switch to `BLOCK` after it is validated.
+ **Multiple rules per category:** Each security category creates a separate rule. You can assign different actions to different categories.
+ **Amazon VPC association:** After adding rules, make sure the rule group is associated with a Amazon VPC for the rules to take effect.
+ **AWS Firewall Manager integration:** Use the **Associate with an AWS Firewall Manager policy** option to apply rule groups across your organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
