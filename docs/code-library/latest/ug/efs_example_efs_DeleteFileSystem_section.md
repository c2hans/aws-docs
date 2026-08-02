---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/efs_example_efs_DeleteFileSystem_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteFileSystem` with a CLI
<a name="efs_example_efs_DeleteFileSystem_section"></a>

The following code examples show how to use `DeleteFileSystem`.

------
#### [ CLI ]

**AWS CLI**
**To delete a file system**
The following `delete-file-system` example deletes the specified file system.

```
aws efs delete-file-system \
    --file-system-id {{fs-c7a0456e}}
```
This command produces no output.
For more information, see [Deleting an Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/delete-efs-fs.html) in the *Amazon Elastic File System User Guide*.
+  For API details, see [DeleteFileSystem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-file-system.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Deletes the specified file system that is no longer in use (if the file system has mount targets they must be removed first). You are prompted for confirmation before the cmdlet proceeds - to suppress confirmation, use the `-Force` switch.**

```
Remove-EFSFileSystem -FileSystemId fs-1a2b3c4d
```
+  For API details, see [DeleteFileSystem](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Deletes the specified file system that is no longer in use (if the file system has mount targets they must be removed first). You are prompted for confirmation before the cmdlet proceeds - to suppress confirmation, use the `-Force` switch.**

```
Remove-EFSFileSystem -FileSystemId fs-1a2b3c4d
```
+  For API details, see [DeleteFileSystem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
