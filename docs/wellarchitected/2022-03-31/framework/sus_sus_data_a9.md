---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a9.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP08 Back up data only when difficult to recreate
<a name="sus_sus_data_a9"></a>

 To minimize storage consumption, only back up data that has business value or is needed to satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that doesn’t provide value in a recovery scenario.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use your data classification to establish what data needs to be backed up.
+  Exclude data that you can easily recreate.
+  Exclude ephemeral data from your backups.
+  Exclude local copies of data, unless the time required to restore that data from a common location exceeds your service level agreements (SLAs).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Using AWS Backup to back up and restore Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html)
+  [Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
+  [Working with backups on Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
