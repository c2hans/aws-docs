---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_RecordLifecycleActionHeartbeat_section.html
---

# Use `RecordLifecycleActionHeartbeat` with a CLI
<a name="example_auto-scaling_RecordLifecycleActionHeartbeat_section"></a>

The following code examples show how to use `RecordLifecycleActionHeartbeat`.

------
#### [ CLI ]

**AWS CLI**
**To record a lifecycle action heartbeat**
This example records a lifecycle action heartbeat to keep the instance in a pending state.

```
aws autoscaling record-lifecycle-action-heartbeat \
    --lifecycle-hook-name {{my-launch-hook}} \
    --auto-scaling-group-name {{my-asg}} \
    --lifecycle-action-token {{bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635}}
```
This command produces no output.
For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [RecordLifecycleActionHeartbeat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/record-lifecycle-action-heartbeat.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example records a heartbeat for the specified lifecycle action. This keeps the instance in a pending state until you complete the custom action.**

```
Write-ASLifecycleActionHeartbeat -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook -LifecycleActionToken bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635
```
+  For API details, see [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example records a heartbeat for the specified lifecycle action. This keeps the instance in a pending state until you complete the custom action.**

```
Write-ASLifecycleActionHeartbeat -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook -LifecycleActionToken bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635
```
+  For API details, see [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
