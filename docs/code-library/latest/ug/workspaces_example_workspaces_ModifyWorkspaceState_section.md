---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_ModifyWorkspaceState_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyWorkspaceState` with a CLI
<a name="workspaces_example_workspaces_ModifyWorkspaceState_section"></a>

The following code examples show how to use `ModifyWorkspaceState`.

------
#### [ CLI ]

**AWS CLI**
**To modify the state of a WorkSpace**
The following `modify-workspace-state` example sets the state of the specified WorkSpace to `ADMIN_MAINTENANCE`.

```
aws workspaces modify-workspace-state \
    --workspace-id {{ws-dk1xzr417}} \
    --workspace-state {{ADMIN_MAINTENANCE}}
```
This command produces no output.
For more information, see [WorkSpace maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [ModifyWorkspaceState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-state.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This sample changes the state of the specified Workspace to Available**

```
Edit-WKSWorkspaceState -WorkspaceId ws-w361s100v -Region us-west-2 -WorkspaceState AVAILABLE
```
+  For API details, see [ModifyWorkspaceState](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This sample changes the state of the specified Workspace to Available**

```
Edit-WKSWorkspaceState -WorkspaceId ws-w361s100v -Region us-west-2 -WorkspaceState AVAILABLE
```
+  For API details, see [ModifyWorkspaceState](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
