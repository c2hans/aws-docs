---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-iam-group.html
---

# `AWSConfigRemediation-DeleteUnusedIAMGroup`
<a name="automation-aws-delete-iam-group"></a>

 **Description**

 The `AWSConfigRemediation-DeleteUnusedIAMGroup` runbook deletes an IAM group that does not contain any users.

 The `AWSConfigRemediation-DeleteUnusedIAMGroup` runbook deletes an IAM group that does not contain any users.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteUnusedIAMGroup)

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
+ GroupName

  Type: String

  Description: (Required) The name of the IAM group that you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `iam:DeleteGroup`
+  `iam:DeleteGroupPolicy`
+  `iam:DetachGroupPolicy`

 **Document Steps**
+  `aws:executeScript` - Removes managed and inline IAM policies attached to the target IAM group, and then deletes the IAM group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
