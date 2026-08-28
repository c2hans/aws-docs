---
source_url: https://docs.aws.amazon.com/EDI/latest/eco-support-guide/eco-default-backup.html
---

# ECO default backup plan
<a name="eco-default-backup"></a>

AWS Backup doesn't support "continuous backups" for ECO default backup plans. For information about different types of backup plans, see [Continuous backups and point-in-time recovery (PITR)](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html).

Use the following tag key–value pair to identify EDI resources that you want ECO to back up.

 `TAG key: ams:rt:backup-orchestrator TAG value: true`

**Important**
Backup monitoring and reporting are only available in EDI supported regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Energy Data Insights on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query EDI` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
