---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/efs_example_efs_DeleteMountTarget_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteMountTarget` with a CLI
<a name="efs_example_efs_DeleteMountTarget_section"></a>

The following code examples show how to use `DeleteMountTarget`.

------
#### [ CLI ]

**AWS CLI**
**To delete a mount target**
The following `delete-mount-target` example deletes the specified mount target.

```
aws efs delete-mount-target \
    --mount-target-id {{fsmt-f9a14450}}
```
This command produces no output.
For more information, see [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html) in the *Amazon Elastic File System User Guide*.
+  For API details, see [DeleteMountTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-mount-target.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Deletes the specified mount target. You are prompted for confirmation before the operation proceeds. To suppress the prompt use the `-Force` switch. Note that this operation forcibly breaks any mounts of the file system via the target - you may want to consider unmounting the file system before running this command, if feasible.**

```
Remove-EFSMountTarget -MountTargetId fsmt-1a2b3c4d
```
+  For API details, see [DeleteMountTarget](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Deletes the specified mount target. You are prompted for confirmation before the operation proceeds. To suppress the prompt use the `-Force` switch. Note that this operation forcibly breaks any mounts of the file system via the target - you may want to consider unmounting the file system before running this command, if feasible.**

```
Remove-EFSMountTarget -MountTargetId fsmt-1a2b3c4d
```
+  For API details, see [DeleteMountTarget](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
