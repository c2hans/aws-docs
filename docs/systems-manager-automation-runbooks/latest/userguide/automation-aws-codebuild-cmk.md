---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-codebuild-cmk.html
---

# `AWSConfigRemediation-ConfigureCodeBuildProjectWithKMSCMK`
<a name="automation-aws-codebuild-cmk"></a>

 **Description**

 The `AWSConfigRemediation-ConfigureCodeBuildProjectWithKMSCMK` runbook encrypts an AWS CodeBuild (CodeBuild) project's build artifacts using the AWS Key Management Service (AWS KMS) customer managed key you specify. AWS Config must be enabled in the AWS Region where you run this automation.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-ConfigureCodeBuildProjectWithKMSCMK)

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
+ KMSKeyId

  Type: String

   Description: (Required) The Amazon Resource Name (ARN) of the AWS KMS customer managed key you want to use to encrypt the CodeBuild project you specify in the `ProjectId` parameter.
+ ProjectId

  Type: String

  Description: (Required) The ID of the CodeBuild project whose build artifacts you want to encrypt.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `codebuild:BatchGetProjects`
+  `codebuild:UpdateProject`
+  `config:GetResourceConfigHistory`

 **Document Steps**
+  `aws:executeAwsApi` - Gathers the CodeBuild project name from the project ID.
+  `aws:executeAwsApi` - Enables encryption on the CodeBuild project you specify in the `ProjectId` parameter.
+  `aws:assertAwsResourceProperty` - Verifies that encryption has been enabled on the CodeBuild project.

 **Outputs**

 UpdateLambdaConfig.UpdateFunctionConfigurationResponse - Response from the `UpdateFunctionConfiguration` API call.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
