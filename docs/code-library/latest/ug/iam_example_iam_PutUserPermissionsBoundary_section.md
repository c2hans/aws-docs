---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_PutUserPermissionsBoundary_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutUserPermissionsBoundary` with a CLI
<a name="iam_example_iam_PutUserPermissionsBoundary_section"></a>

The following code examples show how to use `PutUserPermissionsBoundary`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To apply a permissions boundary based on a custom policy to an IAM user**
The following `put-user-permissions-boundary` example applies a custom policy named `intern-boundary` as the permissions boundary for the specified IAM user.

```
aws iam put-user-permissions-boundary \
    --permissions-boundary {{arn:aws:iam::123456789012:policy/intern-boundary}} \
    --user-name {{intern}}
```
This command produces no output.
**Example 2: To apply a permissions boundary based on an AWS managed policy to an IAM user**
The following `put-user-permissions-boundary` example applies the AWS managed pollicy named `PowerUserAccess` as the permissions boundary for the specified IAM user.

```
aws iam put-user-permissions-boundary \
    --permissions-boundary {{arn:aws:iam::aws:policy/PowerUserAccess}} \
    --user-name {{developer}}
```
This command produces no output.
For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *AWS IAM User Guide*.
+  For API details, see [PutUserPermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-permissions-boundary.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example shows how to set the Permission boundary for the user. You can set AWS Managed policies or Custom policies as permission boundary. **

```
Set-IAMUserPermissionsBoundary -UserName joe -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary
```
+  For API details, see [PutUserPermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example shows how to set the Permission boundary for the user. You can set AWS Managed policies or Custom policies as permission boundary. **

```
Set-IAMUserPermissionsBoundary -UserName joe -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary
```
+  For API details, see [PutUserPermissionsBoundary](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
