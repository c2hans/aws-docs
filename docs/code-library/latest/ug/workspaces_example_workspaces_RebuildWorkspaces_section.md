---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_RebuildWorkspaces_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RebuildWorkspaces` with a CLI
<a name="workspaces_example_workspaces_RebuildWorkspaces_section"></a>

The following code examples show how to use `RebuildWorkspaces`.

------
#### [ CLI ]

**AWS CLI**
**To rebuild a WorkSpace**
The following `rebuild-workspaces` example rebuilds the specified WorkSpace.

```
aws workspaces rebuild-workspaces \
    --rebuild-workspace-requests {{ws-dk1xzr417}}
```
Output:

```
{
    "FailedRequests": []
}
```
For more information, see [Rebuild a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/rebuild-workspace.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [RebuildWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/rebuild-workspaces.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Rebuilds the specified WorkSpace.**

```
Reset-WKSWorkspace -WorkspaceId "ws-1a2b3c4d"
```
**Example 2: Retrieves the collection of all your WorkSpaces and pipes the IDs to the -WorkSpaceId parameter of Reset-WKSWorkspace, causing the WorkSpaces to be rebuilt.**

```
Get-WKSWorkspaces | Reset-WKSWorkspace
```
+  For API details, see [RebuildWorkspaces](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Rebuilds the specified WorkSpace.**

```
Reset-WKSWorkspace -WorkspaceId "ws-1a2b3c4d"
```
**Example 2: Retrieves the collection of all your WorkSpaces and pipes the IDs to the -WorkSpaceId parameter of Reset-WKSWorkspace, causing the WorkSpaces to be rebuilt.**

```
Get-WKSWorkspaces | Reset-WKSWorkspace
```
+  For API details, see [RebuildWorkspaces](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
