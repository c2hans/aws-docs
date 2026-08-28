---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-rds-instance.html
---

# `AWSConfigRemediation-DeleteRDSInstance`
<a name="automation-aws-delete-rds-instance"></a>

 **Description**

 The `AWSConfigRemediation-DeleteRDSInstance` runbook deletes the Amazon Relational Database Service (Amazon RDS) instance you specify. When you delete a database (DB) instance, all automated backups for that instance are deleted and can't be recovered. Manual DB snapshots are not deleted. If the DB instance you want to delete is in the `failed` , `incompatible-network` , or `incompatible-restore` state, you must set the `SkipFinalSnapshot` parameter to `true` .

**Note**
If the DB instance you want to delete is in an Amazon Aurora DB cluster, the runbook will not delete the DB instance if it is a read replica and the only instance in the DB cluster.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteRDSInstance)

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
+ DbiResourceId

  Type: String

  Description: (Required) The resource identifier for the DB instance you want to delete.
+ SkipFinalSnapshot

  Type: Boolean

  Default: false

   Description: (Optional) If set to `true` , a final snapshot is not created before the DB instance is deleted.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `rds:DeleteDBInstance`
+  `rds:DescribeDBInstances`

 **Document Steps**
+  `aws:executeAwsApi` - Gathers the DB instance name from the value you specify in the `DbiResourceId` parameter.
+  `aws:branch` - Branches based on the value you specify in the `SkipFinalSnapshot` parameter.
+  `aws:executeAwsApi` - Deletes the DB instance you specify in the `DbiResourceId` parameter.
+  `aws:executeAwsApi` - Deletes the DB instance you specify in the `DbiResourceId` parameter after the final snapshot is created.
+  `aws:assertAwsResourceProperty` - Verifies the DB instance was deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
