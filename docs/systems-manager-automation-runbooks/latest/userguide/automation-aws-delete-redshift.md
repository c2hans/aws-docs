---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-redshift.html
---

# `AWSConfigRemediation-DeleteRedshiftCluster`
<a name="automation-aws-delete-redshift"></a>

 **Description**

 The `AWSConfigRemediation-DeleteRedshiftCluster` runbook deletes the Amazon Redshift cluster you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteRedshiftCluster)

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
+ ClusterIdentifier

  Type: String

  Description: (Required) The ID of the Amazon Redshift cluster that you want to delete.
+ SkipFinalClusterSnapshot

  Type: Boolean

  Default: false

   Description: (Optional) If set to `false` , the automation creates a snapshot before deleting the Amazon Redshift cluster. If set to `true` , a final cluster snapshot is not created.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `redshift:DeleteCluster`
+  `redshift:DescribeClusters`

 **Document Steps**
+  `aws:branch` - Branches based on the value you specify for the `SkipFinalClusterSnapshot` parameter.
+  `aws:executeAwsApi` - Deletes the Amazon Redshift cluster specified in the `ClusterIdentifier` parameter.
+  `aws:assertAwsResourceProperty` - Verifies the Amazon Redshift cluster has been deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
