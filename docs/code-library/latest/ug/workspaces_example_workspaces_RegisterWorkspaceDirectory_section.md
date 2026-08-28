---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_RegisterWorkspaceDirectory_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RegisterWorkspaceDirectory` with a CLI
<a name="workspaces_example_workspaces_RegisterWorkspaceDirectory_section"></a>

The following code examples show how to use `RegisterWorkspaceDirectory`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Creating and managing personal virtual desktops](workspaces_example_workspaces_GettingStarted_035_section.md)

------
#### [ CLI ]

**AWS CLI**
**To register a directory**
The following `register-workspace-directory` example registers the specified directory for use with Amazon WorkSpaces.

```
aws workspaces register-workspace-directory \
    --directory-id {{d-926722edaf}}
```
This command produces no output.
For more information, see [Register an existing AWS Directory Service directory with WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [RegisterWorkspaceDirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/register-workspace-directory.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This sample registers the specified directory for Workspaces Service**

```
Register-WKSWorkspaceDirectory -DirectoryId d-123412a123 -EnableWorkDoc $false
```
+  For API details, see [RegisterWorkspaceDirectory](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This sample registers the specified directory for Workspaces Service**

```
Register-WKSWorkspaceDirectory -DirectoryId d-123412a123 -EnableWorkDoc $false
```
+  For API details, see [RegisterWorkspaceDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
