---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/efs_example_efs_DescribeFileSystems_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeFileSystems` with a CLI
<a name="efs_example_efs_DescribeFileSystems_section"></a>

The following code examples show how to use `DescribeFileSystems`.

------
#### [ CLI ]

**AWS CLI**
**To describe a file system**
The following `describe-file-systems` example describes the specified file system.

```
aws efs describe-file-systems \
    --file-system-id {{fs-c7a0456e}}
```
Output:

```
{
    "FileSystems": [
        {
            "OwnerId": "123456789012",
            "CreationToken": "console-d7f56c5f-e433-41ca-8307-9d9c0example",
            "FileSystemId": "fs-c7a0456e",
            "FileSystemArn": "arn:aws:elasticfilesystem:us-west-2:123456789012:file-system/fs-48499b4d",
            "CreationTime": 1595286880.0,
            "LifeCycleState": "available",
            "Name": "my-file-system",
            "NumberOfMountTargets": 3,
            "SizeInBytes": {
                "Value": 6144,
                "Timestamp": 1600991437.0,
                "ValueInIA": 0,
                "ValueInStandard": 6144
            },
            "PerformanceMode": "generalPurpose",
            "Encrypted": true,
            "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/a59b3472-e62c-42e4-adcf-30d92example",
            "ThroughputMode": "bursting",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "my-file-system"
                }
            ]
        }
    ]
}
```
For more information, see [Managing Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/managing.html) in the *Amazon Elastic File System User Guide*.
+  For API details, see [DescribeFileSystems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-file-systems.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

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

**Tools for PowerShell V5**
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
+  For API details, see [DescribeFileSystems](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
