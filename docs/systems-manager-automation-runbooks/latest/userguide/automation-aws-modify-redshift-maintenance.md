---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-redshift-maintenance.html
---

# `AWSConfigRemediation-ModifyRedshiftClusterMaintenanceSettings`
<a name="automation-aws-modify-redshift-maintenance"></a>

 **Description**

 The `AWSConfigRemediation-ModifyRedshiftClusterMaintenanceSettings` runbook modifies the maintenance settings for the Amazon Redshift cluster you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-ModifyRedshiftClusterMaintenanceSettings)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AllowVersionUpgrade

  Type: Boolean

   Description: (Required) If set to `true` , major version upgrades are applied automatically to the cluster during the maintenance window.
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ AutomatedSnapshotRetentionPeriod

  Type: Integer

  Valid values: 1-35

  Description: (Required) The number of days automated snapshots are retained.
+ ClusterIdentifier

  Type: String

  Description: (Required) The unique identifier of the cluster you want to enable enhanced VPC routing on.
+ PreferredMaintenanceWindow

  Type: String

  Description: (Required) The weekly time range (in UTC) during which system maintenance can occur.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `redshift:DescribeClusters`
+  `redshift:ModifyCluster`

 **Document Steps**
+  `aws:executeAwsApi` - Modifies the maintenance settings for the cluster specified in the `ClusterIdentifier` parameter.
+  `aws:assertAwsResourceProperty` - Confirms the modified maintenance settings were configured for the cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
