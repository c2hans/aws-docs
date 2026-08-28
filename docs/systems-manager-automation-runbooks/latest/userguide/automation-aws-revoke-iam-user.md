---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-revoke-iam-user.html
---

# `AWSConfigRemediation-RevokeUnusedIAMUserCredentials`
<a name="automation-aws-revoke-iam-user"></a>

 **Description**

 The `AWSConfigRemediation-RevokeUnusedIAMUserCredentials` runbook revokes unused AWS Identity and Access Management (IAM) passwords and active access keys. This runbook also deactivates expired access keys, and deletes expired login profiles. AWS Config must be enabled in the AWS Region where you run this automation.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-RevokeUnusedIAMUserCredentials)

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

  Description: (Required) The ID of the IAM resource you want to revoke unused credentials from.
+ MaxCredentialUsageAge

  Type: String

  Default: 90

  Description: (Required) The number of days within which the credential must have been used.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `config:ListDiscoveredResources`
+  `iam:DeleteAccessKey`
+  `iam:DeleteLoginProfile`
+  `iam:GetAccessKeyLastUsed`
+  `iam:GetLoginProfile`
+  `iam:GetUser`
+  `iam:ListAccessKeys`
+  `iam:UpdateAccessKey`

 **Document Steps**
+  `aws:executeScript` - Revokes IAM credentials for the user specified in the `IAMResourceId` parameter. Expired access keys are deactivated, and expired login profiles are deleted.

**Note**
Make sure to configure the `MaxCredentialUsageAge`parameter of this remediation action to match the `maxAccessKeyAge` parameter of the AWS Config rule you use to trigger this action: [access-keys-rotated](https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
