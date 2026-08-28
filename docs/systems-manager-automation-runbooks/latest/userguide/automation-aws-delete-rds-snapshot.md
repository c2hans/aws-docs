---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-rds-snapshot.html
---

# `AWSConfigRemediation-DeleteRDSInstanceSnapshot`
<a name="automation-aws-delete-rds-snapshot"></a>

 **Description**

 The `AWSConfigRemediation-DeleteRDSInstanceSnapshot` runbook deletes the Amazon Relational Database Service (Amazon RDS) instance snapshot you specify. Only snapshots in the `available` state are deleted. This runbook does not support deleting snapshots from Amazon Aurora database instances.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteRDSInstanceSnapshot)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ DbSnapshotId

  Type: String

  Description: (Required) The ID of the snapshot you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `rds:DeleteDBSnapshot`
+  `rds:DescribeDBSnapshots`

 **Document Steps**
+  `aws:executeAwsApi` - Gathers the state of the snapshot specified in the `DbSnapshotId` parameter.
+  `aws:assertAwsResourceProperty` - Confirms the state of the snapshot is `available` .
+  `aws:executeAwsApi` - Deletes the snapshot specified in the `DbSnapshotId` parameter.
+  `aws:executeScript` - Verifies the snapshot has been deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
