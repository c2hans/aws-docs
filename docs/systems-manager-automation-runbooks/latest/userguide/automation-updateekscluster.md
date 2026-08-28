---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-updateekscluster.html
---

# `AWS-UpdateEKSCluster`
<a name="automation-updateekscluster"></a>

 **Description**

 The `AWS-UpdateEKSCluster` runbook helps you update your Amazon Elastic Kubernetes Service (Amazon EKS) cluster to the Kubernetes version that you want to use.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateEKSCluster)

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
+ ClusterName

  Type: String

  Description: (Required) The name of your Amazon EKS cluster.
+ Version

  Type: String

  Description: (Required) The Kubernetes version that you want to update your cluster to.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `eks:DescribeUpdate`
+  `eks:UpdateClusterVersion`

 **Document Steps**
+  `aws:executeAwsApi` - Updates the Kubernetes version that is used by your Amazon EKS cluster.
+  `aws:waitForAwsResourceProperty` - Waits for the update status to be `Successful`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
