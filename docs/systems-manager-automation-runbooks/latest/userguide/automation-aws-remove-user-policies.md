---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-remove-user-policies.html
---

# `AWSConfigRemediation-RemoveUserPolicies`
<a name="automation-aws-remove-user-policies"></a>

 **Description**

 The `AWSConfigRemediation-RemoveUserPolicies` runbook deletes the AWS Identity and Access Management (IAM) inline policies and detaches any managed policies attached to the user you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-RemoveUserPolicies)

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
+ IAMUserID

  Type: String

  Description: (Required) The ID of the user you want to remove policies from.
+ PolicyType

  Type: String

  Valid values: All \| Inline \| Managed

  Default: All

  Description: (Required) The type of IAM policies you want to remove from the user.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `iam:DeleteUserPolicy`
+  `iam:DetachUserPolicy`
+  `iam:ListAttachedUserPolicies`
+  `iam:ListUserPolicies`
+  `iam:ListUsers`

 **Document Steps**
+  `aws:executeScript` - Deletes and detaches IAM policies from the user you specify in the `IAMUserID` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
