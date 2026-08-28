---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_fsx_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Amazon FSx examples using Tools for PowerShell V5
<a name="powershell_fsx_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon FSx.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-FSXResourceTag`
<a name="fsx_TagResource_powershell_topic"></a>

The following code example shows how to use `Add-FSXResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example adds tags to the given resource.**

```
Add-FSXResourceTag -ResourceARN "arn:aws:fsx:eu-west-1:123456789012:file-system/fs-01cd23bc4bdf5678a" -Tag @{Key="Users";Value="Test"}
```
**Output:**

```
arn:aws:fsx:eu-west-1:123456789012:file-system/fs-01cd23bc4bdf5678a
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-FSXBackup`
<a name="fsx_DescribeBackups_powershell_topic"></a>

The following code example shows how to use `Get-FSXBackup`.

**Tools for PowerShell V5**
**Example 1: This example fetches backups created since yesterday for the given file system id.**

```
Get-FSXBackup -Filter @{Name="file-system-id";Values=$fsx.FileSystemId} | Where-Object CreationTime -gt (Get-Date).AddDays(-1)
```
**Output:**

```
BackupId        : backup-01dac234e56782bcc
CreationTime    : 6/14/2019 3:35:14 AM
FailureDetails  :
FileSystem      : Amazon.FSx.Model.FileSystem
KmsKeyId        : arn:aws:kms:eu-west-1:123456789012:key/f1af23c4-1b23-1bde-a1f1-e1234c5af123
Lifecycle       : AVAILABLE
ProgressPercent : 100
ResourceARN     : arn:aws:fsx:eu-west-1:123456789012:backup/backup-01dac234e56782bcc
Tags            : {}
Type            : AUTOMATIC
```
+  For API details, see [DescribeBackups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-FSXFileSystem`
<a name="fsx_DescribeFileSystems_powershell_topic"></a>

The following code example shows how to use `Get-FSXFileSystem`.

**Tools for PowerShell V5**
**Example 1: This example returns the description of given filesystemId.**

```
Get-FSXFileSystem -FileSystemId fs-01cd23bc4bdf5678a
```
**Output:**

```
CreationTime         : 1/17/2019 9:55:30 AM
DNSName              : fs-01cd23bc4bdf5678a.ktmsad.local
FailureDetails       :
FileSystemId         : fs-01cd23bc4bdf5678a
FileSystemType       : WINDOWS
KmsKeyId             : arn:aws:kms:eu-west-1:123456789012:key/f1af23c4-5b67-8bde-a9f0-e1234c5af678
Lifecycle            : AVAILABLE
LustreConfiguration  :
NetworkInterfaceIds  : {eni-07d1dda1322b7e209}
OwnerId              : 123456789012
ResourceARN          : arn:aws:fsx:eu-west-1:123456789012:file-system/fs-01cd23bc4bdf5678a
StorageCapacity      : 300
SubnetIds            : {subnet-7d123456}
Tags                 : {FSx-Service}
VpcId                : vpc-41cf2b3f
WindowsConfiguration : Amazon.FSx.Model.WindowsFileSystemConfiguration
```
+  For API details, see [DescribeFileSystems](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-FSXResourceTagList`
<a name="fsx_ListTagsForResource_powershell_topic"></a>

The following code example shows how to use `Get-FSXResourceTagList`.

**Tools for PowerShell V5**
**Example 1: This example lists tags for provided resource arn.**

```
Get-FSXResourceTagList -ResourceARN $fsx.ResourceARN
```
**Output:**

```
Key         Value
---         -----
FSx-Service Windows
Users       Dev
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-FSXBackup`
<a name="fsx_CreateBackup_powershell_topic"></a>

The following code example shows how to use `New-FSXBackup`.

**Tools for PowerShell V5**
**Example 1: This example creates a back up of the given file system.**

```
New-FSXBackup -FileSystemId fs-0b1fac2345623456ba
```
**Output:**

```
BackupId        : backup-0b1fac2345623456ba
CreationTime    : 6/14/2019 5:37:17 PM
FailureDetails  :
FileSystem      : Amazon.FSx.Model.FileSystem
KmsKeyId        : arn:aws:kms:eu-west-1:123456789012:key/f1af23c4-1b23-1bde-a1f3-e1234c5af678
Lifecycle       : CREATING
ProgressPercent : 0
ResourceARN     : arn:aws:fsx:eu-west-1:123456789012:backup/backup-0b1fac2345623456ba
Tags            : {}
Type            : USER_INITIATED
```
+  For API details, see [CreateBackup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-FSXFileSystem`
<a name="fsx_CreateFileSystem_powershell_topic"></a>

The following code example shows how to use `New-FSXFileSystem`.

**Tools for PowerShell V5**
**Example 1: This example creates a new 300GB Windows file system, permitting access from the specified subnet, that supports throughput up to 8 megabytes per second. The new file system is automatically joined to the specified Microsoft Active Directory.**

```
New-FSXFileSystem -FileSystemType WINDOWS -StorageCapacity 300 -SubnetId subnet-1a2b3c4d5e6f -WindowsConfiguration @{ThroughputCapacity=8;ActiveDirectoryId='d-1a2b3c4d'}
```
**Output:**

```
CreationTime         : 12/10/2018 6:06:59 PM
DNSName              : fs-abcdef01234567890.example.com
FailureDetails       :
FileSystemId         : fs-abcdef01234567890
FileSystemType       : WINDOWS
KmsKeyId             : arn:aws:kms:us-west-2:123456789012:key/a1234567-252c-45e9-afaa-123456789abc
Lifecycle            : CREATING
LustreConfiguration  :
NetworkInterfaceIds  : {}
OwnerId              : 123456789012
ResourceARN          : arn:aws:fsx:us-west-2:123456789012:file-system/fs-abcdef01234567890
StorageCapacity      : 300
SubnetIds            : {subnet-1a2b3c4d5e6f}
Tags                 : {}
VpcId                : vpc-1a2b3c4d5e6f
WindowsConfiguration : Amazon.FSx.Model.WindowsFileSystemConfiguration
```
+  For API details, see [CreateFileSystem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-FSXFileSystemFromBackup`
<a name="fsx_CreateFileSystemFromBackup_powershell_topic"></a>

The following code example shows how to use `New-FSXFileSystemFromBackup`.

**Tools for PowerShell V5**
**Example 1: This exmaple creates new Amazon FSx file system from an existing Amazon FSx for Windows File Server backup.**

```
New-FSXFileSystemFromBackup -BackupId $backupID -Tag @{Key="tag:Name";Value="from-manual-backup"} -SubnetId $SubnetID -SecurityGroupId $SG_ID -WindowsConfiguration @{ThroughputCapacity=8;ActiveDirectoryId=$DirectoryID}
```
**Output:**

```
CreationTime         : 8/8/2019 12:59:58 PM
DNSName              : fs-012ff34e56789120.ktmsad.local
FailureDetails       :
FileSystemId         : fs-012ff34e56789120
FileSystemType       : WINDOWS
KmsKeyId             : arn:aws:kms:eu-west-1:123456789012:key/f1af23c4-5b67-1bde-a2f3-e4567c8a9321
Lifecycle            : CREATING
LustreConfiguration  :
NetworkInterfaceIds  : {}
OwnerId              : 933303704102
ResourceARN          : arn:aws:fsx:eu-west-1:123456789012:file-system/fs-012ff34e56789120
StorageCapacity      : 300
SubnetIds            : {subnet-fa1ae23c}
Tags                 : {tag:Name}
VpcId                : vpc-12cf3b4f
WindowsConfiguration : Amazon.FSx.Model.WindowsFileSystemConfiguration
```
+  For API details, see [CreateFileSystemFromBackup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-FSXBackup`
<a name="fsx_DeleteBackup_powershell_topic"></a>

The following code example shows how to use `Remove-FSXBackup`.

**Tools for PowerShell V5**
**Example 1: This example removes the given backup-id.**

```
Remove-FSXBackup -BackupId $backupID
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-FSXBackup (DeleteBackup)" on target "backup-0bbca1e2345678e12".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

BackupId                 Lifecycle
--------                 ---------
backup-0bbca1e2345678e12 DELETED
```
+  For API details, see [DeleteBackup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-FSXFileSystem`
<a name="fsx_DeleteFileSystem_powershell_topic"></a>

The following code example shows how to use `Remove-FSXFileSystem`.

**Tools for PowerShell V5**
**Example 1: This example removes the given FSX file system ID.**

```
Remove-FSXFileSystem -FileSystemId fs-012ff34e567890120
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-FSXFileSystem (DeleteFileSystem)" on target "fs-012ff34e567890120".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

FileSystemId         Lifecycle WindowsResponse
------------         --------- ---------------
fs-012ff34e567890120 DELETING  Amazon.FSx.Model.DeleteFileSystemWindowsResponse
```
+  For API details, see [DeleteFileSystem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-FSXResourceTag`
<a name="fsx_UntagResource_powershell_topic"></a>

The following code example shows how to use `Remove-FSXResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example removes the resource tag for the given FSX file system resource ARN.**

```
Remove-FSXResourceTag -ResourceARN $FSX.ResourceARN -TagKey Users
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-FSXResourceTag (UntagResource)" on target "arn:aws:fsx:eu-west-1:933303704102:file-system/fs-07cd45bc6bdf2674a".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-FSXFileSystem`
<a name="fsx_UpdateFileSystem_powershell_topic"></a>

The following code example shows how to use `Update-FSXFileSystem`.

**Tools for PowerShell V5**
**Example 1: This example updates the FSX file system automatic backup retention days via UpdateFileSystemWindowsConfiguration.**

```
$UpdateFSXWinConfig = [Amazon.FSx.Model.UpdateFileSystemWindowsConfiguration]::new()
	$UpdateFSXWinConfig.AutomaticBackupRetentionDays = 35
	Update-FSXFileSystem -FileSystemId $FSX.FileSystemId -WindowsConfiguration $UpdateFSXWinConfig
```
**Output:**

```
CreationTime         : 1/17/2019 9:55:30 AM
DNSName              : fs-01cd23bc4bdf5678a.ktmsad.local
FailureDetails       :
FileSystemId         : fs-01cd23bc4bdf5678a
FileSystemType       : WINDOWS
KmsKeyId             : arn:aws:kms:eu-west-1:123456789012:key/f1af23c4-1b23-1bde-a1f2-e1234c5af678
Lifecycle            : AVAILABLE
LustreConfiguration  :
NetworkInterfaceIds  : {eni-01cd23bc4bdf5678a}
OwnerId              : 933303704102
ResourceARN          : arn:aws:fsx:eu-west-1:933303704102:file-system/fs-07cd45bc6bdf2674a
StorageCapacity      : 300
SubnetIds            : {subnet-1d234567}
Tags                 : {FSx-Service}
VpcId                : vpc-23cf4b5f
WindowsConfiguration : Amazon.FSx.Model.WindowsFileSystemConfiguration
```
+  For API details, see [UpdateFileSystem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
