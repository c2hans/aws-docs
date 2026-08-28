---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DeleteVolume_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteVolume` with a CLI
<a name="ec2_example_ec2_DeleteVolume_section"></a>

The following code examples show how to use `DeleteVolume`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Creating and managing block storage volumes](ec2_example_ec2_GettingStarted_020_section.md)
+  [Working with block storage encryption, snapshots, and volume initialization](ec2_example_ec2_GettingStarted_022_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a volume**
This example command deletes an available volume with the volume ID of `vol-049df61146c4d7901`. If the command succeeds, no output is returned.
Command:

```
aws ec2 delete-volume --volume-id {{vol-049df61146c4d7901}}
```
+  For API details, see [DeleteVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-volume.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example detaches the specified volume. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2Volume -VolumeId vol-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Volume (DeleteVolume)" on target "vol-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVolume](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example detaches the specified volume. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2Volume -VolumeId vol-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Volume (DeleteVolume)" on target "vol-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteVolume](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
