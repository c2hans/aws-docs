---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_StopWorkspaces_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `StopWorkspaces` with a CLI
<a name="workspaces_example_workspaces_StopWorkspaces_section"></a>

The following code examples show how to use `StopWorkspaces`.

------
#### [ CLI ]

**AWS CLI**
**To stop an AutoStop WorkSpace**
The following `stop-workspaces` example stops the specified WorkSpace. The WorkSpace must have a running mode of `AutoStop`.

```
aws workspaces stop-workspaces \
    --stop-workspace-requests {{WorkspaceId=ws-dk1xzr417}}
```
Output:

```
{
    "FailedRequests": []
}
```
For more information, see [Stop and start an AutoStop WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html#stop-start-workspace) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [StopWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/stop-workspaces.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Stops multiple WorkSpaces.**

```
Stop-WKSWorkspace -WorkspaceId "ws-1a2b3c4d5","ws-6a7b8c9d0"
```
**Example 2: Retrieves the collection of all your WorkSpaces and pipes the IDs to the -WorkSpaceId parameter of Stop-WKSWorkspace causing the WorkSpaces to be stopped.**

```
Get-WKSWorkspaces | Stop-WKSWorkspace
```
**Example 3: This example shows how to pass StopRequest objects defining the WorkSpaces to be stopped.**

```
$arrRequest = @()
$request1 = New-Object Amazon.WorkSpaces.Model.StopRequest
$request1.WorkspaceId = 'ws-12345678'
$arrRequest += $request1
$request2 = New-Object Amazon.WorkSpaces.Model.StopRequest
$request2.WorkspaceId = 'ws-abcdefgh'
$arrRequest += $request2
Stop-WKSWorkspace -Request $arrRequest
```
+  For API details, see [StopWorkspaces](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Stops multiple WorkSpaces.**

```
Stop-WKSWorkspace -WorkspaceId "ws-1a2b3c4d5","ws-6a7b8c9d0"
```
**Example 2: Retrieves the collection of all your WorkSpaces and pipes the IDs to the -WorkSpaceId parameter of Stop-WKSWorkspace causing the WorkSpaces to be stopped.**

```
Get-WKSWorkspaces | Stop-WKSWorkspace
```
**Example 3: This example shows how to pass StopRequest objects defining the WorkSpaces to be stopped.**

```
$arrRequest = @()
$request1 = New-Object Amazon.WorkSpaces.Model.StopRequest
$request1.WorkspaceId = 'ws-12345678'
$arrRequest += $request1
$request2 = New-Object Amazon.WorkSpaces.Model.StopRequest
$request2.WorkspaceId = 'ws-abcdefgh'
$arrRequest += $request2
Stop-WKSWorkspace -Request $arrRequest
```
+  For API details, see [StopWorkspaces](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
