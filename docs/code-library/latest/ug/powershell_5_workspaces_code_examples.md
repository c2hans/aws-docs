---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_workspaces_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# WorkSpaces examples using Tools for PowerShell V5
<a name="powershell_5_workspaces_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with WorkSpaces.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Approve-WKSIpRule`
<a name="workspaces_AuthorizeIpRules_powershell_5_topic"></a>

The following code example shows how to use `Approve-WKSIpRule`.

**Tools for PowerShell V5**
**Example 1: This sample adds rules to an existing IP Group**

```
$Rule = @(
@{IPRule = "10.1.0.0/0"; RuleDesc = "First Rule Added"},
@{IPRule = "10.2.0.0/0"; RuleDesc = "Second Rule Added"}
)

Approve-WKSIpRule -GroupId wsipg-abcnx2fcw -UserRule $Rule
```
+  For API details, see [AuthorizeIpRules](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Copy-WKSWorkspaceImage`
<a name="workspaces_CopyWorkspaceImage_powershell_5_topic"></a>

The following code example shows how to use `Copy-WKSWorkspaceImage`.

**Tools for PowerShell V5**
**Example 1: This sample copies workspace Image with specified ID from us-west-2 to the current region with the name "CopiedImageTest"**

```
Copy-WKSWorkspaceImage -Name CopiedImageTest -SourceRegion us-west-2 -SourceImageId wsi-djfoedhw6
```
**Output:**

```
wsi-456abaqfe
```
+  For API details, see [CopyWorkspaceImage](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Edit-WKSClientProperty`
<a name="workspaces_ModifyClientProperties_powershell_5_topic"></a>

The following code example shows how to use `Edit-WKSClientProperty`.

**Tools for PowerShell V5**
**Example 1: This sample enables Reconnection for the Workspaces Client**

```
Edit-WKSClientProperty -Region us-west-2 -ClientProperties_ReconnectEnabled "ENABLED" -ResourceId d-123414a369
```
+  For API details, see [ModifyClientProperties](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Edit-WKSSelfServicePermission`
<a name="workspaces_ModifySelfservicePermissions_powershell_5_topic"></a>

The following code example shows how to use `Edit-WKSSelfServicePermission`.

**Tools for PowerShell V5**
**Example 1: This sample enables self service permissions to Change compute type and Increase Volume Size for the specified Directory**

```
Edit-WKSSelfservicePermission -Region us-west-2 -ResourceId d-123454a369 -SelfservicePermissions_ChangeComputeType ENABLED -SelfservicePermissions_IncreaseVolumeSize ENABLED
```
+  For API details, see [ModifySelfservicePermissions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Edit-WKSWorkspaceAccessProperty`
<a name="workspaces_ModifyWorkspaceAccessProperties_powershell_5_topic"></a>

The following code example shows how to use `Edit-WKSWorkspaceAccessProperty`.

**Tools for PowerShell V5**
**Example 1: This sample enables Workspace access on Android and Chrome OS for the specified Directory**

```
Edit-WKSWorkspaceAccessProperty -Region us-west-2 -ResourceId d-123454a369 -WorkspaceAccessProperties_DeviceTypeAndroid ALLOW -WorkspaceAccessProperties_DeviceTypeChromeOs ALLOW
```
+  For API details, see [ModifyWorkspaceAccessProperties](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Edit-WKSWorkspaceCreationProperty`
<a name="workspaces_ModifyWorkspaceCreationProperties_powershell_5_topic"></a>

The following code example shows how to use `Edit-WKSWorkspaceCreationProperty`.

**Tools for PowerShell V5**
**Example 1: This sample enables Internet Access and Maintenance Mode to true as default values while creating a Workspace**

```
Edit-WKSWorkspaceCreationProperty -Region us-west-2 -ResourceId d-123454a369 -WorkspaceCreationProperties_EnableInternetAccess $true -WorkspaceCreationProperties_EnableMaintenanceMode $true
```
+  For API details, see [ModifyWorkspaceCreationProperties](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Edit-WKSWorkspaceProperty`
<a name="workspaces_ModifyWorkspaceProperties_powershell_5_topic"></a>

The following code example shows how to use `Edit-WKSWorkspaceProperty`.

**Tools for PowerShell V5**
**Example 1: This Sample changes the Workspace Running Mode Property to Auto Stop for the specified Workspace**

```
Edit-WKSWorkspaceProperty -WorkspaceId ws-w361s100v -Region us-west-2 -WorkspaceProperties_RunningMode AUTO_STOP
```
+  For API details, see [ModifyWorkspaceProperties](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Edit-WKSWorkspaceState`
<a name="workspaces_ModifyWorkspaceState_powershell_5_topic"></a>

The following code example shows how to use `Edit-WKSWorkspaceState`.

**Tools for PowerShell V5**
**Example 1: This sample changes the state of the specified Workspace to Available**

```
Edit-WKSWorkspaceState -WorkspaceId ws-w361s100v -Region us-west-2 -WorkspaceState AVAILABLE
```
+  For API details, see [ModifyWorkspaceState](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSClientProperty`
<a name="workspaces_DescribeClientProperties_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSClientProperty`.

**Tools for PowerShell V5**
**Example 1: This sample gets the Client Properties of the Workspace Client for the specified Directory**

```
Get-WKSClientProperty -ResourceId d-223562a123
```
+  For API details, see [DescribeClientProperties](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSIpGroup`
<a name="workspaces_DescribeIpGroups_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSIpGroup`.

**Tools for PowerShell V5**
**Example 1: This sample gets the details of the specified IP Group in the specified region**

```
Get-WKSIpGroup -Region us-east-1 -GroupId wsipg-8m1234v45
```
**Output:**

```
GroupDesc GroupId         GroupName UserRules
--------- -------         --------- ---------
          wsipg-8m1234v45 TestGroup {Amazon.WorkSpaces.Model.IpRuleItem, Amazon.WorkSpaces.Model.IpRuleItem}
```
+  For API details, see [DescribeIpGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSTag`
<a name="workspaces_DescribeTags_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSTag`.

**Tools for PowerShell V5**
**Example 1: This Sample fetches tag for the given Workspace**

```
Get-WKSTag -WorkspaceId ws-w361s234r -Region us-west-2
```
**Output:**

```
Key         Value
---         -----
auto-delete no
purpose     Workbench
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSWorkspace`
<a name="workspaces_DescribeWorkspaces_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSWorkspace`.

**Tools for PowerShell V5**
**Example 1: Retrieves details of all your WorkSpaces to the pipeline.**

```
Get-WKSWorkspace
```
**Output:**

```
BundleId                    : wsb-1a2b3c4d
ComputerName                :
DirectoryId                 : d-1a2b3c4d
ErrorCode                   :
ErrorMessage                :
IpAddress                   :
RootVolumeEncryptionEnabled : False
State                       : PENDING
SubnetId                    :
UserName                    : myuser
UserVolumeEncryptionEnabled : False
VolumeEncryptionKey         :
WorkspaceId                 : ws-1a2b3c4d
WorkspaceProperties         : Amazon.WorkSpaces.Model.WorkspaceProperties
```
**Example 2: This command shows the values of child properties of `WorkSpaceProperties` for a workspace in the `us-west-2` region. For more information about the child properties of `WorkSpaceProperties`, see https://docs.aws.amazon.com/workspaces/latest/api/API\_WorkspaceProperties.html.**

```
(Get-WKSWorkspace -Region us-west-2 -WorkSpaceId ws-xdaf7hc9s).WorkspaceProperties
```
**Output:**

```
        ComputeTypeName                     : STANDARD
        RootVolumeSizeGib                   : 80
        RunningMode                         : AUTO_STOP
        RunningModeAutoStopTimeoutInMinutes : 60
        UserVolumeSizeGib                   : 50
```
**Example 3: This command shows the value of the child property `RootVolumeSizeGib` of `WorkSpaceProperties` for a workspace in the `us-west-2` region. The root volume size, in GiB, is 80.**

```
(Get-WKSWorkspace -Region us-west-2 -WorkSpaceId ws-xdaf7hc9s).WorkspaceProperties.RootVolumeSizeGib
```
**Output:**

```
        80
```
+  For API details, see [DescribeWorkspaces](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSWorkspaceBundle`
<a name="workspaces_DescribeWorkspaceBundles_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSWorkspaceBundle`.

**Tools for PowerShell V5**
**Example 1: This sample fetches details of all the Workspace bundles in the current region**

```
Get-WKSWorkspaceBundle
```
**Output:**

```
BundleId        : wsb-sfhdgv342
ComputeType     : Amazon.WorkSpaces.Model.ComputeType
Description     : This bundle is custom
ImageId         : wsi-235aeqges
LastUpdatedTime : 12/26/2019 06:44:07
Name            : CustomBundleTest
Owner           : 233816212345
RootStorage     : Amazon.WorkSpaces.Model.RootStorage
UserStorage     : Amazon.WorkSpaces.Model.UserStorage
```
+  For API details, see [DescribeWorkspaceBundles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSWorkspaceDirectory`
<a name="workspaces_DescribeWorkspaceDirectories_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSWorkspaceDirectory`.

**Tools for PowerShell V5**
**Example 1: This sample lists the directory details for registered directories**

```
Get-WKSWorkspaceDirectory
```
**Output:**

```
Alias                       : TestWorkspace
CustomerUserName            : Administrator
DirectoryId                 : d-123414a369
DirectoryName               : TestDirectory.com
DirectoryType               : MicrosoftAD
DnsIpAddresses              : {172.31.43.45, 172.31.2.97}
IamRoleId                   : arn:aws:iam::761234567801:role/workspaces_RoleDefault
IpGroupIds                  : {}
RegistrationCode            : WSpdx+4RRT43
SelfservicePermissions      : Amazon.WorkSpaces.Model.SelfservicePermissions
State                       : REGISTERED
SubnetIds                   : {subnet-1m3m7b43, subnet-ard11aba}
Tenancy                     : SHARED
WorkspaceAccessProperties   : Amazon.WorkSpaces.Model.WorkspaceAccessProperties
WorkspaceCreationProperties : Amazon.WorkSpaces.Model.DefaultWorkspaceCreationProperties
WorkspaceSecurityGroupId    : sg-0ed2441234a123c43
```
+  For API details, see [DescribeWorkspaceDirectories](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSWorkspaceImage`
<a name="workspaces_DescribeWorkspaceImages_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSWorkspaceImage`.

**Tools for PowerShell V5**
**Example 1: This sample fetches all the details of all images in the region**

```
Get-WKSWorkspaceImage
```
**Output:**

```
Description     :This image is copied from another image
ErrorCode       :
ErrorMessage    :
ImageId         : wsi-345ahdjgo
Name            : CopiedImageTest
OperatingSystem : Amazon.WorkSpaces.Model.OperatingSystem
RequiredTenancy : DEFAULT
State           : AVAILABLE
```
+  For API details, see [DescribeWorkspaceImages](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSWorkspaceSnapshot`
<a name="workspaces_DescribeWorkspaceSnapshots_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSWorkspaceSnapshot`.

**Tools for PowerShell V5**
**Example 1: This sample shows the timestamp of the most recent snapshot created for the specified Workspace**

```
Get-WKSWorkspaceSnapshot -WorkspaceId ws-w361s100v
```
**Output:**

```
RebuildSnapshots                   RestoreSnapshots
----------------                   ----------------
{Amazon.WorkSpaces.Model.Snapshot} {Amazon.WorkSpaces.Model.Snapshot}
```
+  For API details, see [DescribeWorkspaceSnapshots](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-WKSWorkspacesConnectionStatus`
<a name="workspaces_DescribeWorkspacesConnectionStatus_powershell_5_topic"></a>

The following code example shows how to use `Get-WKSWorkspacesConnectionStatus`.

**Tools for PowerShell V5**
**Example 1: This sample fetches the connection status for the specified Workspace**

```
Get-WKSWorkspacesConnectionStatus -WorkspaceId ws-w123s234r
```
+  For API details, see [DescribeWorkspacesConnectionStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-WKSIpGroup`
<a name="workspaces_CreateIpGroup_powershell_5_topic"></a>

The following code example shows how to use `New-WKSIpGroup`.

**Tools for PowerShell V5**
**Example 1: This sample creates an empty Ip group named FreshEmptyIpGroup**

```
New-WKSIpGroup -GroupName "FreshNewIPGroup"
```
**Output:**

```
wsipg-w45rty4ty
```
+  For API details, see [CreateIpGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-WKSTag`
<a name="workspaces_CreateTags_powershell_5_topic"></a>

The following code example shows how to use `New-WKSTag`.

**Tools for PowerShell V5**
**Example 1: This example adds a new tag to a workspace named `ws-wsname`. The tag has a key of "Name", and a key value of `AWS_Workspace`.**

```
$tag = New-Object Amazon.WorkSpaces.Model.Tag
$tag.Key = "Name"
$tag.Value = "AWS_Workspace"
New-WKSTag -Region us-west-2 -WorkspaceId ws-wsname -Tag $tag
```
**Example 2: This example adds multiple tags to a workspace named `ws-wsname`. One tag has a key of "Name" and a key value of `AWS_Workspace`; the other tag has a tag key of "Stage" and a key value of "Test".**

```
$tag = New-Object Amazon.WorkSpaces.Model.Tag
$tag.Key = "Name"
$tag.Value = "AWS_Workspace"

$tag2 = New-Object Amazon.WorkSpaces.Model.Tag
$tag2.Key = "Stage"
$tag2.Value = "Test"
New-WKSTag -Region us-west-2 -WorkspaceId ws-wsname -Tag $tag,$tag2
```
+  For API details, see [CreateTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-WKSWorkspace`
<a name="workspaces_CreateWorkspaces_powershell_5_topic"></a>

The following code example shows how to use `New-WKSWorkspace`.

**Tools for PowerShell V5**
**Example 1: Create a WorkSpace for the supplied bundle, directory, and user.**

```
New-WKSWorkspace -Workspace @{"BundleID" = "wsb-1a2b3c4d"; "DirectoryId" = "d-1a2b3c4d"; "UserName" = "USERNAME"}
```
**Example 2: This example creates multiple WorkSpaces**

```
New-WKSWorkspace -Workspace @{"BundleID" = "wsb-1a2b3c4d"; "DirectoryId" = "d-1a2b3c4d"; "UserName" = "USERNAME_1"},@{"BundleID" = "wsb-1a2b3c4d"; "DirectoryId" = "d-1a2b3c4d"; "UserName" = "USERNAME_2"}
```
+  For API details, see [CreateWorkspaces](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-WKSIpGroup`
<a name="workspaces_AssociateIpGroups_powershell_5_topic"></a>

The following code example shows how to use `Register-WKSIpGroup`.

**Tools for PowerShell V5**
**Example 1: This sample registers the specified IP Group with the specified Directory**

```
Register-WKSIpGroup -GroupId wsipg-23ahsdres -DirectoryId d-123412e123
```
+  For API details, see [AssociateIpGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-WKSWorkspaceDirectory`
<a name="workspaces_RegisterWorkspaceDirectory_powershell_5_topic"></a>

The following code example shows how to use `Register-WKSWorkspaceDirectory`.

**Tools for PowerShell V5**
**Example 1: This sample registers the specified directory for Workspaces Service**

```
Register-WKSWorkspaceDirectory -DirectoryId d-123412a123 -EnableWorkDoc $false
```
+  For API details, see [RegisterWorkspaceDirectory](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-WKSIpGroup`
<a name="workspaces_DeleteIpGroup_powershell_5_topic"></a>

The following code example shows how to use `Remove-WKSIpGroup`.

**Tools for PowerShell V5**
**Example 1: This sample deletes the specified IP Group**

```
Remove-WKSIpGroup -GroupId wsipg-32fhgtred
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-WKSIpGroup (DeleteIpGroup)" on target "wsipg-32fhgtred".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteIpGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-WKSTag`
<a name="workspaces_DeleteTags_powershell_5_topic"></a>

The following code example shows how to use `Remove-WKSTag`.

**Tools for PowerShell V5**
**Example 1: This sample removes the tag associated with the Workspace**

```
Remove-WKSTag -ResourceId ws-w10b3abcd -TagKey "Type"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-WKSTag (DeleteTags)" on target "ws-w10b3abcd".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-WKSWorkspace`
<a name="workspaces_TerminateWorkspaces_powershell_5_topic"></a>

The following code example shows how to use `Remove-WKSWorkspace`.

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

### `Reset-WKSWorkspace`
<a name="workspaces_RebuildWorkspaces_powershell_5_topic"></a>

The following code example shows how to use `Reset-WKSWorkspace`.

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

### `Restart-WKSWorkspace`
<a name="workspaces_RebootWorkspaces_powershell_5_topic"></a>

The following code example shows how to use `Restart-WKSWorkspace`.

**Tools for PowerShell V5**
**Example 1: Reboots the specified WorkSpace.**

```
Restart-WKSWorkspace -WorkspaceId "ws-1a2b3c4d"
```
**Example 2: Reboots multiple WorkSpaces.**

```
Restart-WKSWorkspace -WorkspaceId "ws-1a2b3c4d","ws-5a6b7c8d"
```
**Example 3: Retrieves the collection of all your WorkSpaces and pipes the IDs to the -WorkSpaceId parameter of Restart-WKSWorkspace, causing the WorkSpaces to be restarted.**

```
Get-WKSWorkspaces | Restart-WKSWorkspace
```
+  For API details, see [RebootWorkspaces](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Stop-WKSWorkspace`
<a name="workspaces_StopWorkspaces_powershell_5_topic"></a>

The following code example shows how to use `Stop-WKSWorkspace`.

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

### `Unregister-WKSIpGroup`
<a name="workspaces_DisassociateIpGroups_powershell_5_topic"></a>

The following code example shows how to use `Unregister-WKSIpGroup`.

**Tools for PowerShell V5**
**Example 1: This sample unregisters the specified IP Group from the specified Directory**

```
Unregister-WKSIpGroup -GroupId wsipg-12abcdphq -DirectoryId d-123454b123
```
+  For API details, see [DisassociateIpGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
