---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-req-backup.html
---

# Managing tags for backups in Accelerate
<a name="acc-tag-req-backup"></a>

AMS Accelerate manages the backing up of supported resources. For more information about this service offering, see [Continuity management in AMS Accelerate](acc-backup.md).

AMS Accelerate backup management uses tags to identify which resources should be automatically backed up (and also provides manual backup capabilities). You can use any tag key:value combination to associate your resources with backup plans. To opt in to automated backups using the **ams-default-backup-plan** AWS Backup plan, you must apply the following tag to your supported resources:

| Key | Value |
| --- | --- |
| ams:rt:backup-orchestrator | true |

**Note**
During onboarding, AMS Accelerate tags all resources with **ams:rt:backup-orchestrator-onboarding** with value **true** for short interval, short retention snapshots. This is managed by the **ams-onboarding-backup-plan** backup plan. For more information about AMS Accelerate-managed AWS Backup plans, see [Select an AMS backup plan](acc-backup-select-plan.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
