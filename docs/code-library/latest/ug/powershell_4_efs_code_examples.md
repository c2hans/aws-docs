---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_efs_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon EFS examples using Tools for PowerShell V4
<a name="powershell_4_efs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Amazon EFS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Edit-EFSMountTargetSecurityGroup`
<a name="efs_ModifyMountTargetSecurityGroups_powershell_4_topic"></a>

The following code example shows how to use `Edit-EFSMountTargetSecurityGroup`.

**Tools for PowerShell V4**
**Example 1: Updates the security groups in effect for the specified mount target. Up to 5 may be specified, in the format "sg-xxxxxxxx".**

```
Edit-EFSMountTargetSecurityGroup -MountTargetId fsmt-1a2b3c4d -SecurityGroup sg-group1,sg-group3
```
+  For API details, see [ModifyMountTargetSecurityGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EFSFileSystem`
<a name="efs_DescribeFileSystems_powershell_4_topic"></a>

The following code example shows how to use `Get-EFSFileSystem`.

**Tools for PowerShell V4**
**Example 1: Returns the collection of all file systems owned by the caller's account in the region.**

```
Get-EFSFileSystem
```
**Output:**

```
CreationTime         : 5/26/2015 4:02:38 PM
CreationToken        : 1a2bff54-85e0-4747-bd95-7bc172c4f555
FileSystemId         : fs-1a2b3c4d
LifeCycleState       : available
Name                 :
NumberOfMountTargets : 0
OwnerId              : 123456789012
SizeInBytes          : Amazon.ElasticFileSystem.Model.FileSystemSize

CreationTime         : 5/26/2015 4:06:23 PM
CreationToken        : 2b4daa14-85e0-4747-bd95-7bc172c4f555
FileSystemId         : fs-4d3c2b1a
...
```
**Example 2: Returns the details of the specified file system.**

```
Get-EFSFileSystem -FileSystemId fs-1a2b3c4d
```
**Example 3: Returns the details of a file system using the idempotency creation token that was specified at the time the file system was created.**

```
Get-EFSFileSystem -CreationToken 1a2bff54-85e0-4747-bd95-7bc172c4f555
```
+  For API details, see [DescribeFileSystems](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EFSMountTarget`
<a name="efs_DescribeMountTargets_powershell_4_topic"></a>

The following code example shows how to use `Get-EFSMountTarget`.

**Tools for PowerShell V4**
**Example 1: Returns the collection of mount targets associated with the specified file system.**

```
Get-EFSMountTarget -FileSystemId fs-1a2b3c4d
```
**Output:**

```
FileSystemId       : fs-1a2b3c4d
IpAddress          : 10.0.0.131
LifeCycleState     : available
MountTargetId      : fsmt-1a2b3c4d
NetworkInterfaceId : eni-1a2b3c4d
OwnerId            : 123456789012
SubnetId           : subnet-1a2b3c4d
```
+  For API details, see [DescribeMountTargets](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EFSMountTargetSecurityGroup`
<a name="efs_DescribeMountTargetSecurityGroups_powershell_4_topic"></a>

The following code example shows how to use `Get-EFSMountTargetSecurityGroup`.

**Tools for PowerShell V4**
**Example 1: Returns the ids of the security groups currently assigned to the network interface associated with the mount target.**

```
Get-EFSMountTargetSecurityGroup -MountTargetId fsmt-1a2b3c4d
```
**Output:**

```
sg-1a2b3c4d
```
+  For API details, see [DescribeMountTargetSecurityGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-EFSTag`
<a name="efs_DescribeTags_powershell_4_topic"></a>

The following code example shows how to use `Get-EFSTag`.

**Tools for PowerShell V4**
**Example 1: Returns the collection of tags currently associated with the specified file system.**

```
Get-EFSTag -FileSystemId fs-1a2b3c4d
```
**Output:**

```
Key         Value
---         -----
Name        My File System
tagkey1     tagvalue1
tagkey2     tagvalue2
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EFSFileSystem`
<a name="efs_CreateFileSystem_powershell_4_topic"></a>

The following code example shows how to use `New-EFSFileSystem`.

**Tools for PowerShell V4**
**Example 1: Creates a new, empty file system. The token used to ensure idempotent creation will be generated automatically and can be accessed from the `CreationToken` member of the returned object.**

```
New-EFSFileSystem
```
**Output:**

```
CreationTime         : 5/26/2015 4:02:38 PM
CreationToken        : 1a2bff54-85e0-4747-bd95-7bc172c4f555
FileSystemId         : fs-1a2b3c4d
LifeCycleState       : creating
Name                 :
NumberOfMountTargets : 0
OwnerId              : 123456789012
SizeInBytes          : Amazon.ElasticFileSystem.Model.FileSystemSize
```
**Example 2: Creates a new, empty file system using a custom token to ensure idempotent creation.**

```
New-EFSFileSystem -CreationToken "MyUniqueToken"
```
+  For API details, see [CreateFileSystem](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EFSMountTarget`
<a name="efs_CreateMountTarget_powershell_4_topic"></a>

The following code example shows how to use `New-EFSMountTarget`.

**Tools for PowerShell V4**
**Example 1: Creates a new mount target for a file system. The specified subnet will be used determine the Virtual Private Cloud (VPC) that the mount target will be created in and the IP address that will be auto-assigned (from the address range of the subnet). The assigned IP address can be used to then mount this file system on an Amazon EC2 instance. As no security groups were specified the network interface created for the target is associated with the default security group for the subnet's VPC.**

```
New-EFSMountTarget -FileSystemId fs-1a2b3c4d -SubnetId subnet-1a2b3c4d
```
**Output:**

```
FileSystemId       : fs-1a2b3c4d
IpAddress          : 10.0.0.131
LifeCycleState     : creating
MountTargetId      : fsmt-1a2b3c4d
NetworkInterfaceId : eni-1a2b3c4d
OwnerId            : 123456789012
SubnetId           : subnet-1a2b3c4d
```
**Example 2: Creates a new mount target for the specified file system with auto-assigned IP address. The network interface created for the mount target is associated with the specified security groups (up to 5, in the format "sg-xxxxxxxx", may be specified).**

```
New-EFSMountTarget -FileSystemId fs-1a2b3c4d -SubnetId subnet-1a2b3c4d -SecurityGroup sg-group1,sg-group2,sg-group3
```
**Example 3: Creates a new mount target for the specified file system with the specified IP address.**

```
New-EFSMountTarget -FileSystemId fs-1a2b3c4d -SubnetId subnet-1a2b3c4d -IpAddress 10.0.0.131
```
+  For API details, see [CreateMountTarget](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-EFSTag`
<a name="efs_CreateTags_powershell_4_topic"></a>

The following code example shows how to use `New-EFSTag`.

**Tools for PowerShell V4**
**Example 1: Applies the collection of tags to the specified file system. If a tag with key specified already exists on the file system the value of the tag is updated.**

```
New-EFSTag -FileSystemId fs-1a2b3c4d -Tag @{Key="tagkey1";Value="tagvalue1"},@{Key="tagkey2";Value="tagvalue2"}
```
**Example 2: Sets the name tag for the specified file system. This value is returned along with other file system details when the Get-EFSFileSystem cmdlet is used.**

```
New-EFSTag -FileSystemId fs-1a2b3c4d -Tag @{Key="Name";Value="My File System"}
```
+  For API details, see [CreateTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EFSFileSystem`
<a name="efs_DeleteFileSystem_powershell_4_topic"></a>

The following code example shows how to use `Remove-EFSFileSystem`.

**Tools for PowerShell V4**
**Example 1: Deletes the specified file system that is no longer in use (if the file system has mount targets they must be removed first). You are prompted for confirmation before the cmdlet proceeds - to suppress confirmation, use the `-Force` switch.**

```
Remove-EFSFileSystem -FileSystemId fs-1a2b3c4d
```
+  For API details, see [DeleteFileSystem](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EFSMountTarget`
<a name="efs_DeleteMountTarget_powershell_4_topic"></a>

The following code example shows how to use `Remove-EFSMountTarget`.

**Tools for PowerShell V4**
**Example 1: Deletes the specified mount target. You are prompted for confirmation before the operation proceeds. To suppress the prompt use the `-Force` switch. Note that this operation forcibly breaks any mounts of the file system via the target - you may want to consider unmounting the file system before running this command, if feasible.**

```
Remove-EFSMountTarget -MountTargetId fsmt-1a2b3c4d
```
+  For API details, see [DeleteMountTarget](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Remove-EFSTag`
<a name="efs_DeleteTags_powershell_4_topic"></a>

The following code example shows how to use `Remove-EFSTag`.

**Tools for PowerShell V4**
**Example 1: Deletes the collection of one or more tags from a file system. You are prompted for confirmation before the cmdlet proceeds - to suppress confirmation, use the `-Force` switch.**

```
Remove-EFSTag -FileSystemId fs-1a2b3c4d -TagKey "tagkey1","tagkey2"
```
+  For API details, see [DeleteTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
