---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/protection-plans-overview.html
---

# Overview
<a name="protection-plans-overview"></a>

The unified Protection Plans page replaces the need to navigate to individual protection plan pages for configuration. The console navigation shows a single **Protection Plans** link.

The page displays protection plans in the following order:

1. **Foundational GuardDuty** – Enable or disable GuardDuty and configure auto-enable for AWS Organizations accounts.

1. **S3 Protection** – Monitor Amazon S3 data events for potential threats to your data.

1. **Runtime Monitoring** – Monitor operating system-level events for EKS, ECS, and EC2 workloads.

1. **EKS Audit Logs** – Monitor Amazon EKS audit logs for potential threats to your clusters.

1. **RDS Protection** – Monitor RDS login activity for potential threats to your databases.

1. **Lambda Protection** – Monitor Lambda function network activity for potential threats.

Each protection plan displays the following information:
+ Feature status (Enabled or Not enabled)
+ Auto-enable status for AWS Organizations accounts
+ AWS Organizations accounts member statistics

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
