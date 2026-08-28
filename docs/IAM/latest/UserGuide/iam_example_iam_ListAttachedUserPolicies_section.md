---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListAttachedUserPolicies_section.html
---

# Use `ListAttachedUserPolicies` with a CLI
<a name="iam_example_iam_ListAttachedUserPolicies_section"></a>

The following code examples show how to use `ListAttachedUserPolicies`.

------
#### [ CLI ]

**AWS CLI**
**To list all managed policies that are attached to the specified user**
This command returns the names and ARNs of the managed policies for the IAM user named `Bob` in the AWS account.

```
aws iam list-attached-user-policies \
    --user-name {{Bob}}
```
Output:

```
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        },
        {
            "PolicyName": "SecurityAudit",
            "PolicyArn": "arn:aws:iam::aws:policy/SecurityAudit"
        }
    ],
    "IsTruncated": false
}
```
For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *AWS IAM User Guide*.
+  For API details, see [ListAttachedUserPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-attached-user-policies.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This command returns the names and ARNs of the managed policies for the IAM user named `Bob` in the AWS account. To see the list of inline policies that are embedded in the IAM user, use the `Get-IAMUserPolicyList` command.**

```
Get-IAMAttachedUserPolicyList -UserName "Bob"
```
**Output:**

```
PolicyArn                                                 PolicyName
---------                                                 ----------
arn:aws:iam::aws:policy/TesterPolicy                      TesterPolicy
```
+  For API details, see [ListAttachedUserPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This command returns the names and ARNs of the managed policies for the IAM user named `Bob` in the AWS account. To see the list of inline policies that are embedded in the IAM user, use the `Get-IAMUserPolicyList` command.**

```
Get-IAMAttachedUserPolicyList -UserName "Bob"
```
**Output:**

```
PolicyArn                                                 PolicyName
---------                                                 ----------
arn:aws:iam::aws:policy/TesterPolicy                      TesterPolicy
```
+  For API details, see [ListAttachedUserPolicies](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
