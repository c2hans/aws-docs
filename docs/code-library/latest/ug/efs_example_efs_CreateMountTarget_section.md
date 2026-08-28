---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/efs_example_efs_CreateMountTarget_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateMountTarget` with a CLI
<a name="efs_example_efs_CreateMountTarget_section"></a>

The following code examples show how to use `CreateMountTarget`.

------
#### [ CLI ]

**AWS CLI**
**To create a mount target**
The following `create-mount-target` example creates a mount target for the specified file system.

```
aws efs create-mount-target \
    --file-system-id {{fs-c7a0456e}} \
    --subnet-id {{subnet-02bf4c428bexample}} \
    --security-groups {{sg-068f739363example}}
```
Output:

```
{
    "OwnerId": "123456789012",
    "MountTargetId": "fsmt-f9a14450",
    "FileSystemId": "fs-c7a0456e",
    "SubnetId": "subnet-02bf4c428bexample",
    "LifeCycleState": "creating",
    "IpAddress": "10.0.1.24",
    "NetworkInterfaceId": "eni-02d542216aexample",
    "AvailabilityZoneId": "use2-az2",
    "AvailabilityZoneName": "us-east-2b",
    "VpcId": "vpc-0123456789abcdef0"
}
```
For more information, see [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html) in the *Amazon Elastic File System User Guide*.
+  For API details, see [CreateMountTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-mount-target.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

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

**Tools for PowerShell V5**
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
+  For API details, see [CreateMountTarget](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
