---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-ecs-container-instance.html
---

# `AWSSupport-TroubleshootECSContainerInstance`
<a name="automation-aws-troubleshoot-ecs-container-instance"></a>

 **Description**

 The `AWSSupport-TroubleshootECSContainerInstance` runbook helps you troubleshoot an Amazon Elastic Compute Cloud (Amazon EC2) instance that fails to register with an Amazon ECS cluster. This automation reviews whether the user data for the instance contains the correct cluster information, whether the instance profile contains the required permissions, and network configuration issues.

**Important**
 To successfully run this automation, the state of your Amazon EC2 instance must be `running` , and the Amazon ECS cluster state must be `ACTIVE` .

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootECSContainerInstance)

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

  Description: (Required) The name of the Amazon ECS cluster that the instance failed to register with.
+ InstanceId

  Type: String

  Description: (Required) The ID of the Amazon EC2 instance you want to troubleshoot.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ec2:DescribeIamInstanceProfileAssociations`
+  `ec2:DescribeInstanceAttribute`
+  `ec2:DescribeInstances`
+  `ec2:DescribeNetworkAcls`
+  `ec2:DescribeRouteTables`
+  `ec2:DescribeSecurityGroups`
+  `ec2:DescribeSubnets`
+  `ec2:DescribeVpcEndpoints`
+  `ec2:DescribeVpcs`
+  `iam:GetInstanceProfile`
+  `iam:GetRole`
+  `iam:SimulateCustomPolicy`
+  `iam:SimulatePrincipalPolicy`

 **Document Steps**

aws:executeScript: Reviews whether the Amazon EC2 instance meets the prerequisites needed to register with an Amazon ECS cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
