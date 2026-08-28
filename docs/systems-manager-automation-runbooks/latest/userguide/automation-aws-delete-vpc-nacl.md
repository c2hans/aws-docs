---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-vpc-nacl.html
---

# `AWSConfigRemediation-DeleteUnusedVPCNetworkACL`
<a name="automation-aws-delete-vpc-nacl"></a>

 **Description**

 The `AWSConfigRemediation-DeleteUnusedVPCNetworkACL` runbook deletes a network access control list (ACL) that is not associated with a subnet.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteUnusedVPCNetworkACL)

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
+ NetworkAclId

  Type: String

  Description: (Required) The ID of the network ACL that you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `ec2:DeleteNetworkAcl`
+  `ec2:DescribeNetworkAcls`

 **Document Steps**
+  `aws:executeAwsApi` - Deletes the network ACL specified in the `NetworkAclId` parameter.
+  `aws:executeScript` - Confirms the network ACL specified in the `NetworkAclId` parameter was deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
