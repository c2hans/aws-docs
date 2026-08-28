---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-startec2instance.html
---

# `AWS-StartEC2Instance`
<a name="automation-aws-startec2instance"></a>

**Description**

Start one or more Amazon Elastic Compute Cloud (Amazon EC2) instances.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-StartEC2Instance)

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

  Type: StringList

  Description: (Required) EC2 instances to start.
+ FailOnUnexpectedStopped

  Type: Boolean

  Default: True

  Description: (Optional) If set to true, the automation fails if the instance transitions to a stopped state during the start operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
