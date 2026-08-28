---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/efs_example_efs_CreateFileSystem_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateFileSystem` with a CLI
<a name="efs_example_efs_CreateFileSystem_section"></a>

The following code examples show how to use `CreateFileSystem`.

------
#### [ CLI ]

**AWS CLI**
**To create an encrypted file system**
The following `create-file-system` example creates an encrypted file system using the default CMK. It also adds the tag `Name=my-file-system`.

```
aws efs create-file-system \
    --performance-mode {{generalPurpose}} \
    --throughput-mode {{bursting}} \
    --encrypted \
    --tags {{Key=Name,Value=my-file-system}}
```
Output:

```
{
    "OwnerId": "123456789012",
    "CreationToken": "console-d7f56c5f-e433-41ca-8307-9d9c0example",
    "FileSystemId": "fs-c7a0456e",
    "FileSystemArn": "arn:aws:elasticfilesystem:us-west-2:123456789012:file-system/fs-48499b4d",
    "CreationTime": 1595286880.0,
    "LifeCycleState": "creating",
    "Name": "my-file-system",
    "NumberOfMountTargets": 0,
    "SizeInBytes": {
        "Value": 0,
        "ValueInIA": 0,
        "ValueInStandard": 0
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
```
For more information, see [Creating Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html) in the *Amazon Elastic File System User Guide*.
+  For API details, see [CreateFileSystem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

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

**Tools for PowerShell V5**
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
+  For API details, see [CreateFileSystem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
