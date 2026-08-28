---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-iam-policy.html
---

# `AWSConfigRemediation-DeleteUnusedIAMPolicy`
<a name="automation-aws-delete-iam-policy"></a>

 **Description**

 The `AWSConfigRemediation-DeleteUnusedIAMPolicy` runbook deletes an AWS Identity and Access Management (IAM) policy that is not attached to any users, groups, or roles.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteUnusedIAMPolicy)

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
+ IAMResourceId

  Type: String

  Description: (Required) The resource identifier of the IAM policy that you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `config:GetResourceConfigHistory`
+  `config:ListDiscoveredResources`
+  `iam:DeletePolicy`
+  `iam:DeletePolicyVersion`
+  `iam:GetPolicy`
+  `iam:ListEntitiesForPolicy`
+  `iam:ListPolicyVersions`

 **Document Steps**
+  `aws:executeScript` - Deletes the policy you specify in the `IAMResourceId` parameter, and verifies the policy was deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
