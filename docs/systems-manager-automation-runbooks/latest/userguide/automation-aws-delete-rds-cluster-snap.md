---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-rds-cluster-snap.html
---

# `AWSConfigRemediation-DeleteRDSClusterSnapshot`
<a name="automation-aws-delete-rds-cluster-snap"></a>

 **Description**

 The `AWSConfigRemediation-DeleteRDSClusterSnapshot` runbook deletes the given Amazon Relational Database Service (Amazon RDS) cluster snapshot.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteRDSClusterSnapshot)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ DBClusterSnapshotId

  Type: String

  Description: (Required) The Amazon RDS cluster snapshot identifier to be deleted.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `rds:DeleteDBClusterSnapshot`
+  `rds:DescribeDBClusterSnapshots`

 **Document Steps**
+  `aws:branch` - Checks if the cluster snapshot is in the `available` state. If it is not available, the flow ends.
+  `aws:executeAwsApi` - Deletes the given Amazon RDS cluster snapshot using the database (DB) cluster snapshot identifier.
+  `aws:executeScript` - Verifies that the given Amazon RDS cluster snapshot was deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
