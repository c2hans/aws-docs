---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-set-iam-policy.html
---

# `AWSConfigRemediation-SetIAMPasswordPolicy`
<a name="automation-aws-set-iam-policy"></a>

 **Description**

 The `AWSConfigRemediation-SetIAMPasswordPolicy` runbook sets the AWS Identity and Access Management (IAM) user password policy for your AWS account.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-SetIAMPasswordPolicy)

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
+ AllowUsersToChangePassword

  Type: Boolean

  Default: false

   Description: (Optional) If set to `true` , all IAM users in your AWS account can use the AWS Management Console to change their passwords.
+ HardExpiry

  Type: Boolean

  Default: false

   Description: (Optional) If set to `true` , IAM users are prevented from resetting their passwords after their password expires.
+ MaxPasswordAge

  Type: Integer

  Default: 0

  Description: (Optional) The number of days an IAM user's password is valid.
+ MinimumPasswordLength

  Type: Integer

  Default: 6

  Description: (Optional) The minimum number of characters an IAM user's password can be.
+ PasswordReusePrevention

  Type: Integer

  Default: 0

  Description: (Optional) The number of previous passwords that an IAM user is prevented from reusing.
+ RequireLowercaseCharacters

  Type: Boolean

  Default: false

   Description: (Optional) If set to `true` , an IAM user's password must contain a lowercase character from the ISO basic Latin alphabet (a to z).
+ RequireNumbers

  Type: Boolean

  Default: false

   Description: (Optional) If set to `true` , an IAM user's password must contain a numeric character (0-9).
+ RequireSymbols

  Type: Boolean

  Default: false

   Description: (Optional) If set to `true` , an IAM user's password must contain a non-alphanumeric character (\! @ \# $ % ^ \* ( ) \_ \+ - = [ ] { } \| ').
+ RequireUppercaseCharacters

  Type: Boolean

  Default: false

   Description: (Optional) If set to `true` , an IAM user's password must contain an uppercase character from the ISO basic Latin alphabet (A to Z).

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `iam:GetAccountPasswordPolicy`
+  `iam:UpdateAccountPasswordPolicy`

 **Document Steps**
+  `aws:executeScript` - Sets the IAM user password policy based on the values you specify for the runbook parameters for your AWS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
