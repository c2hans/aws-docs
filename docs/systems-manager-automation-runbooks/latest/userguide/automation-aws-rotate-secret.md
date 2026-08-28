---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-rotate-secret.html
---

# `AWSConfigRemediation-RotateSecret`
<a name="automation-aws-rotate-secret"></a>

 **Description**

 The `AWSConfigRemediation-RotateSecret` runbook rotates a secret stored in AWS Secrets Manager.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-RotateSecret)

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
+ RotationInterval

  Type: Interval

  Valid values: 1-365

  Description: (Required) The number of days between rotations of the secret.
+ RotationLambdaArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Lambda funtion that can rotate the secret.
+ SecretId

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the secret you want to rotate.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `lambda:InvokeFunction`
+  `secretsmanager:DescribeSecret`
+  `secretsmanager:RotateSecret`

 **Document Steps**
+  `aws:executeAwsApi` - Rotates the secret you specify in the `SecretId` parameter.
+  `aws:executeScript` - Verifies rotation has been enabled on the secret.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
