---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_AttachInstances_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AttachInstances` with a CLI
<a name="auto-scaling_example_auto-scaling_AttachInstances_section"></a>

The following code examples show how to use `AttachInstances`.

------
#### [ CLI ]

**AWS CLI**
**To attach an instance to an Auto Scaling group**
This example attaches the specified instance to the specified Auto Scaling group.

```
aws autoscaling attach-instances \
    --instance-ids {{i-061c63c5eb45f0416}} \
    --auto-scaling-group-name {{my-asg}}
```
This command produces no output.
+  For API details, see [AttachInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-instances.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example attaches the specified instance to the specified Auto Scaling group. Auto Scaling automatically increases the desired capacity of the Auto Scaling group.**

```
Mount-ASInstance -InstanceId i-93633f9b -AutoScalingGroupName my-asg
```
+  For API details, see [AttachInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example attaches the specified instance to the specified Auto Scaling group. Auto Scaling automatically increases the desired capacity of the Auto Scaling group.**

```
Mount-ASInstance -InstanceId i-93633f9b -AutoScalingGroupName my-asg
```
+  For API details, see [AttachInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
