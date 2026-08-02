---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_ModifyWorkspaceProperties_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyWorkspaceProperties` with a CLI
<a name="workspaces_example_workspaces_ModifyWorkspaceProperties_section"></a>

The following code examples show how to use `ModifyWorkspaceProperties`.

------
#### [ CLI ]

**AWS CLI**
**To modify the running mode of a WorkSpace**
The following `modify-workspace-properties` example sets the running mode of the specified WorkSpace to `AUTO_STOP`.

```
aws workspaces modify-workspace-properties \
    --workspace-id {{ws-dk1xzr417}} \
    --workspace-properties {{RunningMode=AUTO_STOP}}
```
This command produces no output.
For more information, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [ModifyWorkspaceProperties](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-properties.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This Sample changes the Workspace Running Mode Property to Auto Stop for the specified Workspace**

```
Edit-WKSWorkspaceProperty -WorkspaceId ws-w361s100v -Region us-west-2 -WorkspaceProperties_RunningMode AUTO_STOP
```
+  For API details, see [ModifyWorkspaceProperties](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This Sample changes the Workspace Running Mode Property to Auto Stop for the specified Workspace**

```
Edit-WKSWorkspaceProperty -WorkspaceId ws-w361s100v -Region us-west-2 -WorkspaceProperties_RunningMode AUTO_STOP
```
+  For API details, see [ModifyWorkspaceProperties](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
