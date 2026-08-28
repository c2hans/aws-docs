---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_DeleteRolePermissionsBoundary_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteRolePermissionsBoundary` with a CLI
<a name="iam_example_iam_DeleteRolePermissionsBoundary_section"></a>

The following code examples show how to use `DeleteRolePermissionsBoundary`.

------
#### [ CLI ]

**AWS CLI**
**To delete a permissions boundary from an IAM role**
The following `delete-role-permissions-boundary` example deletes the permissions boundary for the specified IAM role. To apply a permissions boundary to a role, use the `put-role-permissions-boundary` command.

```
aws iam delete-role-permissions-boundary \
    --role-name {{lambda-application-role}}
```
This command produces no output.
For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *AWS IAM User Guide*.
+  For API details, see [DeleteRolePermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-permissions-boundary.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example shows how to remove the permission boundary attached to an IAM role.**

```
Remove-IAMRolePermissionsBoundary -RoleName MyRoleName
```
+  For API details, see [DeleteRolePermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example shows how to remove the permission boundary attached to an IAM role.**

```
Remove-IAMRolePermissionsBoundary -RoleName MyRoleName
```
+  For API details, see [DeleteRolePermissionsBoundary](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
