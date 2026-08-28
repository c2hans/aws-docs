---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_DeleteAccountPasswordPolicy_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteAccountPasswordPolicy` with a CLI
<a name="iam_example_iam_DeleteAccountPasswordPolicy_section"></a>

The following code examples show how to use `DeleteAccountPasswordPolicy`.

------
#### [ CLI ]

**AWS CLI**
**To delete the current account password policy**
The following `delete-account-password-policy` command removes the password policy for the current account.

```
aws iam delete-account-password-policy
```
This command produces no output.
For more information, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *AWS IAM User Guide*.
+  For API details, see [DeleteAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-account-password-policy.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the password policy for the AWS account and resets all values to their original defaults. If a password policy does not currently exist, the following error message appears: The account policy with name PasswordPolicy cannot be found.**

```
Remove-IAMAccountPasswordPolicy
```
+  For API details, see [DeleteAccountPasswordPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the password policy for the AWS account and resets all values to their original defaults. If a password policy does not currently exist, the following error message appears: The account policy with name PasswordPolicy cannot be found.**

```
Remove-IAMAccountPasswordPolicy
```
+  For API details, see [DeleteAccountPasswordPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
