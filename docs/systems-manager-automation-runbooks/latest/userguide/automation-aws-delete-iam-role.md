---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-iam-role.html
---

# `AWSConfigRemediation-DeleteIAMRole`
<a name="automation-aws-delete-iam-role"></a>

 **Description**

 The `AWSConfigRemediation-DeleteIAMRole` runbook deletes the AWS Identity and Access Management (IAM) role you specify. This automation does not delete instance profiles associated with the IAM role, or service-linked roles.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteIAMRole)

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
+ IAMRoleID

  Type: String

  Description: (Required) The ID of the IAM role you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `iam:DeleteRole`
+  `iam:DeleteRolePolicy`
+  `iam:GetRole`
+  `iam:ListAttachedRolePolicies`
+  `iam:ListInstanceProfilesForRole`
+  `iam:ListRolePolicies`
+  `iam:ListRoles`
+  `iam:RemoveRoleFromInstanceProfile`

 **Document Steps**
+  `aws:executeScript` - Gathers the name of the IAM role you specify in the `IAMRoleID` parameter.
+  `aws:executeScript` - Gathers policies and instance profiles associated with the IAM role.
+  `aws:executeScript` - Deletes attached policies.
+  `aws:executeScript` - Deletes the IAM role and verifies the role has been deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
