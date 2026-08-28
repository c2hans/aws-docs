---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ResetSnapshotAttribute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ResetSnapshotAttribute` with a CLI
<a name="ec2_example_ec2_ResetSnapshotAttribute_section"></a>

The following code examples show how to use `ResetSnapshotAttribute`.

------
#### [ CLI ]

**AWS CLI**
**To reset a snapshot attribute**
This example resets the create volume permissions for snapshot `snap-1234567890abcdef0`. If the command succeeds, no output is returned.
Command:

```
aws ec2 reset-snapshot-attribute --snapshot-id {{snap-1234567890abcdef0}} --attribute {{createVolumePermission}}
```
+  For API details, see [ResetSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-snapshot-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example resets the specified attribute of the specified snapshot.**

```
Reset-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission
```
+  For API details, see [ResetSnapshotAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example resets the specified attribute of the specified snapshot.**

```
Reset-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission
```
+  For API details, see [ResetSnapshotAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
