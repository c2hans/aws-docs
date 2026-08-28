---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ResetInstanceAttribute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ResetInstanceAttribute` with a CLI
<a name="ec2_example_ec2_ResetInstanceAttribute_section"></a>

The following code examples show how to use `ResetInstanceAttribute`.

------
#### [ CLI ]

**AWS CLI**
**To reset the sourceDestCheck attribute**
This example resets the `sourceDestCheck` attribute of the specified instance. The instance must be in a VPC. If the command succeeds, no output is returned.
Command:

```
aws ec2 reset-instance-attribute --instance-id {{i-1234567890abcdef0}} --attribute {{sourceDestCheck}}
```
**To reset the kernel attribute**
This example resets the `kernel` attribute of the specified instance. The instance must be in the `stopped` state. If the command succeeds, no output is returned.
Command:

```
aws ec2 reset-instance-attribute --instance-id {{i-1234567890abcdef0}} --attribute {{kernel}}
```
**To reset the ramdisk attribute**
This example resets the `ramdisk` attribute of the specified instance. The instance must be in the `stopped` state. If the command succeeds, no output is returned.
Command:

```
aws ec2 reset-instance-attribute --instance-id {{i-1234567890abcdef0}} --attribute {{ramdisk}}
```
+  For API details, see [ResetInstanceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-instance-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example resets the 'sriovNetSupport' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport
```
**Example 2: This example resets the 'ebsOptimized' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized
```
**Example 3: This example resets the 'sourceDestCheck' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sourceDestCheck
```
**Example 4: This example resets the 'disableApiTermination' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination
```
**Example 5: This example resets the 'instanceInitiatedShutdownBehavior' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior
```
+  For API details, see [ResetInstanceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example resets the 'sriovNetSupport' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport
```
**Example 2: This example resets the 'ebsOptimized' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized
```
**Example 3: This example resets the 'sourceDestCheck' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sourceDestCheck
```
**Example 4: This example resets the 'disableApiTermination' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination
```
**Example 5: This example resets the 'instanceInitiatedShutdownBehavior' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior
```
+  For API details, see [ResetInstanceAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
