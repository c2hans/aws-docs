---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-managewindowsservice.html
---

# `AWSSupport-ManageWindowsService`
<a name="automation-awssupport-managewindowsservice"></a>

 **Description**

The `AWSSupport-ManageWindowsService` runbook enables you to stop, start, restart, pause, or disable any Windows service on the target instance.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ManageWindowsService)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ InstanceId

  Type: String

  Description: (Required) The ID of the managed instance to manage the services of.
+ ServiceAction

  Type: String

  Valid values: Check \| Restart \| Force-Restart \| Start \| Stop \| Force-Stop \| Pause

  Default: Check

  Description: (Required) An action to apply to the Windows service. Note that `Force-Restart` and `Force-Stop` can be used to restart and to stop a service that has dependent services.
+ StartupType

  Type: String

  Valid values: Check \| Auto \| Demand \| Disabled \| DelayedAutoStart

  Default: Check

  Description: (Required) A startup type to apply to the Windows service.
+ WindowsServiceName

  Type: String

  Description: (Required) A valid Windows service name.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.

It is recommended that the EC2 instance receiving the command has an IAM role with the **AmazonSSMManagedInstanceCore** Amazon managed policy attached. The user must have at least **ssm:StartAutomationExecution** and **ssm:SendCommand** to run the automation and send the command to the instance, plus **ssm:GetAutomationExecution** to be able to read the automation output.

 **Document Steps**

`aws:runCommand` - Run the PowerShell script to apply the desired configuration to the Windows service on the target instance.

 **Outputs**

manageWindowsService.Output

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
