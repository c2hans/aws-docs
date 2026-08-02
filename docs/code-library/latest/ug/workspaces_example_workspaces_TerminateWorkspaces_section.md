---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_TerminateWorkspaces_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `TerminateWorkspaces` with a CLI
<a name="workspaces_example_workspaces_TerminateWorkspaces_section"></a>

The following code examples show how to use `TerminateWorkspaces`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Creating and managing personal virtual desktops](workspaces_example_workspaces_GettingStarted_035_section.md)

------
#### [ CLI ]

**AWS CLI**
**To terminate a WorkSpace**
The following `terminate-workspaces` example terminates the specified workspace.

```
aws workspaces terminate-workspaces \
    --terminate-workspace-requests {{ws-dk1xzr417}}
```
Output:

```
{
    "FailedRequests": []
}
```
For more information, see [Delete a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [TerminateWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/terminate-workspaces.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Terminates multiple WorkSpaces. use of the -Force switch stops the cmdlet from prompting for confirmation.**

```
Remove-WKSWorkspace -WorkspaceId "ws-1a2b3c4d5","ws-6a7b8c9d0" -Force
```
**Example 2: Retrieves the collection of all your WorkSpaces and pipes the IDs to the -WorkSpaceId parameter of Remove-WKSWorkspace, terminating all of the WorkSpaces. The cmdlet will prompt before each WorkSpace is terminated. To suppress the confirmation prompt add the -Force switch.**

```
Get-WKSWorkspaces | Remove-WKSWorkspace
```
**Example 3: This example shows how to pass TerminateRequest objects defining the WorkSpaces to be terminated. The cmdlet will prompt for confirmation before proceeding, unless the -Force switch parameter is also specified.**

```
$arrRequest = @()
$request1 = New-Object Amazon.WorkSpaces.Model.TerminateRequest
$request1.WorkspaceId = 'ws-12345678'
$arrRequest += $request1
$request2 = New-Object Amazon.WorkSpaces.Model.TerminateRequest
$request2.WorkspaceId = 'ws-abcdefgh'
$arrRequest += $request2
Remove-WKSWorkspace -Request $arrRequest
```
+  For API details, see [TerminateWorkspaces](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Terminates multiple WorkSpaces. use of the -Force switch stops the cmdlet from prompting for confirmation.**

```
Remove-WKSWorkspace -WorkspaceId "ws-1a2b3c4d5","ws-6a7b8c9d0" -Force
```
**Example 2: Retrieves the collection of all your WorkSpaces and pipes the IDs to the -WorkSpaceId parameter of Remove-WKSWorkspace, terminating all of the WorkSpaces. The cmdlet will prompt before each WorkSpace is terminated. To suppress the confirmation prompt add the -Force switch.**

```
Get-WKSWorkspaces | Remove-WKSWorkspace
```
**Example 3: This example shows how to pass TerminateRequest objects defining the WorkSpaces to be terminated. The cmdlet will prompt for confirmation before proceeding, unless the -Force switch parameter is also specified.**

```
$arrRequest = @()
$request1 = New-Object Amazon.WorkSpaces.Model.TerminateRequest
$request1.WorkspaceId = 'ws-12345678'
$arrRequest += $request1
$request2 = New-Object Amazon.WorkSpaces.Model.TerminateRequest
$request2.WorkspaceId = 'ws-abcdefgh'
$arrRequest += $request2
Remove-WKSWorkspace -Request $arrRequest
```
+  For API details, see [TerminateWorkspaces](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
