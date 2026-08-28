---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-best-practices.html
---

# Best practices in Trusted Remediator
<a name="tr-best-practices"></a>

The following are best practices to help you use Trusted Remediator:
+ If you're unsure about the remedation results, start with manual execution mode. Sometimes, applying automated execution for remediations from the start might cause unexpected results.
+ Conduct a weekly review of the remediations and OpsItems to gain insights in the Trusted Remediator results.
+ Member accounts inherit the configurations from the delegated administrator account. So, it’s important to structure the accounts in a way that helps you manage multiple accounts with the same configurations. You can exempt resources from the default configuration using tags.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
