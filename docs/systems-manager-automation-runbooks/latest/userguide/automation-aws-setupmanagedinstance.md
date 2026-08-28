---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-setupmanagedinstance.html
---

# `AWS-SetupManagedInstance`
<a name="automation-aws-setupmanagedinstance"></a>

 **Description**

Configure an instance with an AWS Identity and Access Management (IAM) role for Systems Manager access.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-SetupManagedInstance)

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

  Description: (Required) ID of the EC2 instance to configure
+ LambdaAssumeRole

  Type: String

  Description: (Optional) The ARN of the role that allows Lambda created by Automation to perform the actions on your behalf. If not specified a transient role will be created to run the Lambda function.
+ RoleName

  Type: String

  Default: SSMRoleForManagedInstance

   Description: (Optional) The name of the IAM role for the EC2 instance. If this role does not exist, it will be created. When specifying this value, verify that the role contains the **AmazonSSMManagedInstanceCore** Managed Policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
