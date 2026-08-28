---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ResetImageAttribute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ResetImageAttribute` with a CLI
<a name="ec2_example_ec2_ResetImageAttribute_section"></a>

The following code examples show how to use `ResetImageAttribute`.

------
#### [ CLI ]

**AWS CLI**
**To reset the launchPermission attribute**
This example resets the `launchPermission` attribute for the specified AMI to its default value. By default, AMIs are private. If the command succeeds, no output is returned.
Command:

```
aws ec2 reset-image-attribute --image-id {{ami-5731123e}} --attribute {{launchPermission}}
```
+  For API details, see [ResetImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-image-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example resets the 'launchPermission' attribute to its default value. By default, AMIs are private.**

```
Reset-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission
```
+  For API details, see [ResetImageAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example resets the 'launchPermission' attribute to its default value. By default, AMIs are private.**

```
Reset-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission
```
+  For API details, see [ResetImageAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
