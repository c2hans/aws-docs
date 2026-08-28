---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-redshift-encrypt.html
---

# `AWSConfigRemediation-EnableRedshiftClusterEncryption`
<a name="automation-aws-enable-redshift-encrypt"></a>

 **Description**

 The `AWSConfigRemediation-EnableRedshiftClusterEncryption` runbook enables encryption on the Amazon Redshift cluster you specify using an AWS Key Management Service (AWS KMS) customer managed key. This runbook should only be used as a baseline to ensure that your Amazon Redshift clusters are encrypted according to minimum recommended security best practices. We recommend encrypting multiple clusters with different customer managed keys. This runbook cannot change the AWS KMS customer managed key used on an already encrypted cluster. To change the AWS KMS customer managed key used to encrypt a cluster, you must first disable encryption on the cluster.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableRedshiftClusterEncryption)

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

  Description: (Required) The unique identifier of the cluster you want to enable encryption on.
+ KMSKeyARN

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS KMS customer managed key you want to use to encrypt the cluster's data.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `redshift:DescribeClusters`
+  `redshift:ModifyCluster`

 **Document Steps**
+  `aws:executeAwsApi` - Enables encryption on the Amazon Redshift cluster specified in the `ClusterIdentifier` parameter.
+  `aws:assertAwsResourceProperty` - Verifies encryption has been enabled on the cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
