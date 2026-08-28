---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-cb-keys.html
---

# `AWSConfigRemediation-DeleteAccessKeysFromCodeBuildProject`
<a name="automation-aws-delete-cb-keys"></a>

 **Description**

 The `AWSConfigRemediation-DeleteAccessKeysFromCodeBuildProject` runbook deletes the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables from the AWS CodeBuild (CodeBuild) project you specify. AWS Config must be enabled in the AWS Region where you run this automation.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteAccessKeysFromCodeBuildProject)

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
+ ResourceId

  Type: String

  Description: (Required) The ID of the CodeBuild project whose access key environment variables you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `config:GetResourceConfigHistory`
+  `codebuild:BatchGetProjects`
+  `codebuild:UpdateProject`

 **Document Steps**
+  `aws:executeScript` - Deletes the access key environment variables for the CodeBuild project specified in the `ResourceId` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
