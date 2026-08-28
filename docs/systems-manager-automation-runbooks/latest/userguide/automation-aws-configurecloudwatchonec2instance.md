---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configurecloudwatchonec2instance.html
---

# `AWS-ConfigureCloudWatchOnEC2Instance`
<a name="automation-aws-configurecloudwatchonec2instance"></a>

 **Description**

Enable or disable Amazon CloudWatch detailed monitoring on managed instances.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ConfigureCloudWatchOnEC2Instance)

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
+ InstanceId

  Type: String

  Description: (Required) The ID of the Amazon EC2 instance on which you want to enable CloudWatch monitoring.
+ properties

  Type: String

  Description: (Optional) This parameter is not supported. It is listed here for backwards compatibility.
+ status

  Valid values: Enabled \| Disabled

  Description: (Optional) Specifies whether to enable or disable CloudWatch.

  Default: Enabled

 **Document Steps**

configureCloudWatch - Configures CloudWatch on the Amazon EC2 instance with the given status.

 **Outputs**

This automation has no output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
