---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-redshift-enhanced-routing.html
---

# `AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting`
<a name="automation-aws-enable-redshift-enhanced-routing"></a>

 **Description**

 The `AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting` runbook enables enhanced virtual private cloud (VPC) routing for the Amazon Redshift cluster you specify. For information about enhanced VPC routing, see [Amazon Redshift enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/gsg/enhanced-vpc-routing.html) in the *Amazon Redshift Management Guide* .

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting)

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

  Description: (Required) The unique identifier of the cluster you want to enable enhanced VPC routing on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `redshift:DescribeClusters`
+  `redshift:ModifyCluster`

 **Document Steps**
+  `aws:executeAwsApi` - Enables enhanced VPC routing on the cluster specified in the `ClusterIdentifier` parameter.
+  `assertAwsResourceProperty` - Confirms enhanced VPC routing was enabled on the cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
