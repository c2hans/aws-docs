---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_EnableVolumeIo_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `EnableVolumeIo` with a CLI
<a name="ec2_example_ec2_EnableVolumeIo_section"></a>

The following code examples show how to use `EnableVolumeIo`.

------
#### [ CLI ]

**AWS CLI**
**To enable I/O for a volume**
This example enables I/O on volume `vol-1234567890abcdef0`.
Command:

```
aws ec2 enable-volume-io --volume-id {{vol-1234567890abcdef0}}
```
Output:

```
{
  "Return": true
}
```
+  For API details, see [EnableVolumeIo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-volume-io.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example enables I/O operations for the specified volume, if I/O operations were disabled.**

```
Enable-EC2VolumeIO -VolumeId vol-12345678
```
+  For API details, see [EnableVolumeIo](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example enables I/O operations for the specified volume, if I/O operations were disabled.**

```
Enable-EC2VolumeIO -VolumeId vol-12345678
```
+  For API details, see [EnableVolumeIo](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
