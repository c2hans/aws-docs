---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ModifyVolumeAttribute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyVolumeAttribute` with a CLI
<a name="ec2_example_ec2_ModifyVolumeAttribute_section"></a>

The following code examples show how to use `ModifyVolumeAttribute`.

------
#### [ CLI ]

**AWS CLI**
**To modify a volume attribute**
This example sets the `autoEnableIo` attribute of the volume with the ID `vol-1234567890abcdef0` to `true`. If the command succeeds, no output is returned.
Command:

```
aws ec2 modify-volume-attribute --volume-id {{vol-1234567890abcdef0}} --auto-enable-io
```
+  For API details, see [ModifyVolumeAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example modifies the specified attribute of the specified volume. I/O operations for the volume are automatically resumed after being suspended due to potentially inconsistent data.**

```
Edit-EC2VolumeAttribute -VolumeId vol-12345678 -AutoEnableIO $true
```
+  For API details, see [ModifyVolumeAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example modifies the specified attribute of the specified volume. I/O operations for the volume are automatically resumed after being suspended due to potentially inconsistent data.**

```
Edit-EC2VolumeAttribute -VolumeId vol-12345678 -AutoEnableIO $true
```
+  For API details, see [ModifyVolumeAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
