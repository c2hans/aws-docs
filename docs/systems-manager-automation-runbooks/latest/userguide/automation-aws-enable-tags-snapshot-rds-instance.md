---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-tags-snapshot-rds-instance.html
---

# `AWSConfigRemediation-EnableCopyTagsToSnapshotOnRDSDBInstance`
<a name="automation-aws-enable-tags-snapshot-rds-instance"></a>

 **Description**

 The `AWSConfigRemediation-EnableCopyTagsToSnapshotOnRDSDBInstance` runbook enables the `CopyTagsToSnapshot` setting on the Amazon Relational Database Service (Amazon RDS) instance you specify. Enabling this setting copies all tags from the DB instance to snapshots of the DB instance. The default is not to copy them. AWS Config must be enabled in the AWS Region where you run this automation.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCopyTagsToSnapshotOnRDSDBInstance)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ ApplyImmediately

  Type: Boolean

  Default: false

   Description: (Optional) If you specify `true` for this parameter, the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the DB instance.
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ DbiResourceId

  Type: String

   Description: (Required) The resource identifier for the DB instance you want to enable the `CopyTagsToSnapshot` setting on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `config:GetResourceConfigHistory`
+  `rds:DescribeDBInstances`
+  `rds:ModifyDBInstance`

 **Document Steps**
+  `aws:executeAwsApi` - Gathers the DB instance identifier from the DB instance resource identifier.
+  `aws:assertAwsResourceProperty` - Confirms the DB instance is in an `AVAILABLE` state.
+  `aws:executeAwsApi` - Enables the `CopyTagsToSnapshot` setting on your DB instance.
+  `aws:assertAwsResourceProperty` - Confirms the `CopyTagsToSnapshot` setting is enabled on your DB instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
