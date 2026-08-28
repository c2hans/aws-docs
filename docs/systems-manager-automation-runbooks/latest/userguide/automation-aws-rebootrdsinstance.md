---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-rebootrdsinstance.html
---

# `AWS-RebootRdsInstance`
<a name="automation-aws-rebootrdsinstance"></a>

 **Description**

 The `AWS-RebootRdsInstance` runbook reboots an Amazon Relational Database Service (Amazon RDS) DB instance if it isn't already rebooting.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-RebootRdsInstance)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ InstanceId

  Type: String

  Description: (Required) The ID of the Amazon RDS DB instance that you want to reboot.

 **Document Steps**

RebootInstance - Reboots the DB instance if it is not already rebooting.

WaitForAvailableState - Waits for the DB instance to complete the reboot process.

 **Outputs**

This automation has no outputs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
