---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/workspaces_example_workspaces_DescribeWorkspaces_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeWorkspaces` with a CLI
<a name="workspaces_example_workspaces_DescribeWorkspaces_section"></a>

The following code examples show how to use `DescribeWorkspaces`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Creating and managing personal virtual desktops](workspaces_example_workspaces_GettingStarted_035_section.md)

------
#### [ CLI ]

**AWS CLI**
**To describe a WorkSpace**
The following `describe-workspaces` example describes the specified WorkSpace.

```
aws workspaces describe-workspaces \
    --workspace-ids {{ws-dk1xzr417}}
```
Output:

```
{
    "Workspaces": [
        {
            "WorkspaceId": "ws-dk1xzr417",
            "DirectoryId": "d-926722edaf",
            "UserName": "Mary",
            "IpAddress": "172.16.0.175",
            "State": "STOPPED",
            "BundleId": "wsb-0zsvgp8fc",
            "SubnetId": "subnet-500d5819",
            "ComputerName": "WSAMZN-RBSLTTD9",
            "WorkspaceProperties": {
                "RunningMode": "AUTO_STOP",
                "RunningModeAutoStopTimeoutInMinutes": 60,
                "RootVolumeSizeGib": 80,
                "UserVolumeSizeGib": 10,
                "ComputeTypeName": "VALUE"
            },
            "ModificationStates": []
        }
    ]
}
```
For more information, see [Administer your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-workspaces.html) in the *Amazon WorkSpaces Administration Guide*.
+  For API details, see [DescribeWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [DescribeWorkspaces](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
