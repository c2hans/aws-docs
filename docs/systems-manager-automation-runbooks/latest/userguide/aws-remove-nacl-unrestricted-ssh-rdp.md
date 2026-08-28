---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-remove-nacl-unrestricted-ssh-rdp.html
---

# `AWS-RemoveNetworkACLUnrestrictedSSHRDP`
<a name="aws-remove-nacl-unrestricted-ssh-rdp"></a>

 **Description**

 The `AWS-RemoveNetworkACLUnrestrictedSSHRDP` runbook removes all network access control list (ACL) rules from the specified network ACL that allow ingress traffic from all source addresses to default SSH and RDP ports. Rules that include port ranges that overlap with the default SSH and RDP ports aren't removed.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-RemoveNetworkACLUnrestrictedSSHRDP)

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
+ NetworkAclId

  Type: String

  Description: (Required) The ID of the network ACL that you want to remove unrestricted rules that allow ingress traffic from all source addresses to default SSH and RDP ports.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `ec2:DeleteNetworkAclEntry`
+  `ec2:DescribeNetworkAcls`

 **Document Steps**
+  `aws:executeScript` - Removes all ingress rules that allow traffic from all source addresses from the security group you specified in the `SecurityGroupId` parameter.

 **Outputs**

RemoveNaclEntriesAndVerify.VerificationMessage - Verification messages of the successfully deleted network ACL rules.

RemoveNaclEntriesAndVerify.RulesDeletedAndApiResponses - The network ACL rules that were deleted, and the `DeleteNetworkAclEntry` API operation responses.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
