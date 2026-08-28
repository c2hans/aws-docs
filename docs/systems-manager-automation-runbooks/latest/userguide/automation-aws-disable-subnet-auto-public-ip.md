---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disable-subnet-auto-public-ip.html
---

# `AWSConfigRemediation-DisableSubnetAutoAssignPublicIP`
<a name="automation-aws-disable-subnet-auto-public-ip"></a>

 **Description**

 The `AWSConfigRemediation-DisableSubnetAutoAssignPublicIP` runbook disables the IPv4 public addressing attribute for the subnet you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DisableSubnetAutoAssignPublicIP)

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
+ SubnetId

  Type: String

  Description: (Required) The ID of the subnet that you want to disable the auto-assign public IPv4 address attribute on.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `ec2:DescribeSubnets`
+  `ec2:ModifySubnetAttribute`

 **Document Steps**
+  `aws:executeAwsApi` - Disables the auto-assign public IPv4 address attribute for the subnet you specified in the `SubnetId` parameter.
+  `aws:assertAwsResourceProperty` - Verifies the attribute has been disabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
