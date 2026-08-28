---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/close-security-group.html
---

# `AWS-CloseSecurityGroup`
<a name="close-security-group"></a>

 **Description**

This runbook removes all ingress and egress rules from the security group you specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CloseSecurityGroup)

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
+ SecurityGroupId

  Type: String

  Description: (Required) The ID of the security group you want to close.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeSecurityGroups`
+ `ec2:RevokeSecurityGroupEgress`
+ `ec2:RevokeSecurityGroupIngress`

**Document Steps**
+ `aws:executeScript` - Removes all ingress and egress rules from the security group you specify in the `SecurityGroupId` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
