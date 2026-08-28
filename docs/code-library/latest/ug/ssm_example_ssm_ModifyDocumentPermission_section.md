---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_ModifyDocumentPermission_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyDocumentPermission` with a CLI
<a name="ssm_example_ssm_ModifyDocumentPermission_section"></a>

The following code examples show how to use `ModifyDocumentPermission`.

------
#### [ CLI ]

**AWS CLI**
**To modify document permissions**
The following `modify-document-permission` example shares a Systems Manager document publicly.

```
aws ssm modify-document-permission \
    --name {{"Example"}} \
    --permission-type {{"Share"}} \
    --account-ids-to-add {{"All"}}
```
This command produces no output.
For more information, see [Share a Systems Manager Document](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-how-to-share.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [ModifyDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/modify-document-permission.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds "share" permissions to all accounts for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScript" -PermissionType "Share" -AccountIdsToAdd all
```
**Example 2: This example adds "share" permissions to a specific account for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScriptNew" -PermissionType "Share" -AccountIdsToAdd "123456789012"
```
+  For API details, see [ModifyDocumentPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds "share" permissions to all accounts for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScript" -PermissionType "Share" -AccountIdsToAdd all
```
**Example 2: This example adds "share" permissions to a specific account for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScriptNew" -PermissionType "Share" -AccountIdsToAdd "123456789012"
```
+  For API details, see [ModifyDocumentPermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
