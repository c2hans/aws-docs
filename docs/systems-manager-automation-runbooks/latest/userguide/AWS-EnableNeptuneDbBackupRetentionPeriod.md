---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/AWS-EnableNeptuneDbBackupRetentionPeriod.html
---

# `AWS-EnableNeptuneDbBackupRetentionPeriod`
<a name="AWS-EnableNeptuneDbBackupRetentionPeriod"></a>

 **Description**

The `AWS-EnableNeptuneDbBackupRetentionPeriod` runbook helps you enable automated backups with a backup retention period between 7 and 35 days for an Amazon Neptune DB cluster.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableNeptuneDbBackupRetentionPeriod)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ DbClusterResourceId

  Type: String

  Description: (Required) The resource ID of the Neptune DB cluster you want to enable backups for.
+ BackupRetentionPeriod

  Type: Integer

  Valid values: 7-35

  Description: (Required) The number of days backups are retained.
+ PreferredBackupWindow

  Type: String

  Description: (Optional) A daily time period of at least 30 minutes when backups are made. The value must be in Universal Time Coordinated (UTC) and use the format: `hh24:mm-hh24:mm`. The backup retention period can't conflict with the preferred maintenance window.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:GetAutomationExecution`
+  `ssm:StartAutomationExecution`
+  `neptune:DescribeDBCluster`
+  `neptune:ModifyDBCluster`
+  `rds:DescribeDBClusters`
+  `rds:ModifyDBCluster`

 **Document Steps**
+ GetNeptuneDbClusterIdentifier (`aws:executeAwsApi`) - Returns the ID of the Neptune DB cluster.
+ VerifyNeptuneDbEngine (`aws:assertAwsResourceProperty`) - Verifies the Neptune DB engine type is `neptune`.
+ VerifyNeptuneDbStatus (`aws:waitAwsResourceProperty`) - Verifies the Neptune DB cluster status is `available`.
+ ModifyNeptuneDbRetentionPeriod (`aws:executeAwsApi`) - Sets the retention period for the Neptune DB cluster.
+ VerifyNeptuneDbBackupsEnabled (`aws:executeScript`) - Verifies the retention period and backup window were successfully set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
