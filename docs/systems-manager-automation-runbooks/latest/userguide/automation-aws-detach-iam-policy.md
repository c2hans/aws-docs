---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-detach-iam-policy.html
---

# `AWSConfigRemediation-DetachIAMPolicy`
<a name="automation-aws-detach-iam-policy"></a>

 **Description**

 The `AWSConfigRemediation-DetachIAMPolicy` runbook detaches the AWS Identity and Access Management (IAM) policy you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DetachIAMPolicy)

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

  Description: (Required) The ID of the IAM policy you want to detach.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `config:GetResourceConfigHistory`
+  `config:ListDiscoveredResources`
+  `iam:DetachGroupPolicy`
+  `iam:DetachRolePolicy`
+  `iam:DetachUserPolicy`
+  `iam:GetPolicy`
+  `iam:ListEntitiesForPolicy`

 **Document Steps**
+  `aws:executeScript` - Detaches the IAM policy from all resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
