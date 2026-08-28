---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-get-customize-backup.html
---

# Customize backup in Accelerate
<a name="acc-get-customize-backup"></a>

You cannot customize AMS default back-up plans. Instead, create a new backup plan based on your application needs, and then attach resources to your custom plan using tags. It is up to you to choose which resources AMS should back up, how often, and for what retention period. We recommend evaluating the continuity, security, and compliance requirements of your organization to determine what backup plans you need.
+ To create a backup plan, see [Creating a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html).
+ To assign resources to a backup plan, see [Assigning resources to a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
