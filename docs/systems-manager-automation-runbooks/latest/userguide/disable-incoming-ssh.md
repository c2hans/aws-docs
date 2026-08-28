---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/disable-incoming-ssh.html
---

# `AWS-DisableIncomingSSHOnPort22`
<a name="disable-incoming-ssh"></a>

**Description**

The `AWS-DisableIncomingSSHOnPort22` runbook removes rules that allow unrestricted incoming SSH traffic on TCP port 22 for security groups.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DisableIncomingSSHOnPort22)

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
+ SecurityGroupIds

  Type: String

  Description: (Required) A comma separated list of the IDs of the security groups you want to restrict SSH traffic for.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeSecurityGroups`
+ `ec2:RevokeSecurityGroupIngress`

**Document Steps**
+ `aws:executeAwsApi` - Removes all rules allowing incoming SSH traffic on TCP port 22 from the security groups you specify in the `SecurityGroupIds` parameter.

**Outputs**

DisableIncomingSSHTemplate.RestrictedSecurityGroupIds - A list of the IDs of the security groups that had inbound SSH rules removed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
