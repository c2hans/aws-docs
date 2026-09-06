---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_CompleteLifecycleAction_section.html
---

# Use `CompleteLifecycleAction` with a CLI
<a name="example_auto-scaling_CompleteLifecycleAction_section"></a>

The following code examples show how to use `CompleteLifecycleAction`.

------
#### [ CLI ]

**AWS CLI**
**To complete the lifecycle action**
This example notifies Amazon EC2 Auto Scaling that the specified lifecycle action is complete so that it can finish launching or terminating the instance.

```
aws autoscaling complete-lifecycle-action \
    --lifecycle-hook-name {{my-launch-hook}} \
    --auto-scaling-group-name {{my-asg}} \
    --lifecycle-action-result {{CONTINUE}} \
    --lifecycle-action-token {{bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635}}
```
This command produces no output.
For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [CompleteLifecycleAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/complete-lifecycle-action.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example completes the specified lifecycle action.**

```
Complete-ASLifecycleAction -LifecycleHookName myLifecycleHook -AutoScalingGroupName my-asg -LifecycleActionResult CONTINUE -LifecycleActionToken bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635
```
+  For API details, see [CompleteLifecycleAction](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example completes the specified lifecycle action.**

```
Complete-ASLifecycleAction -LifecycleHookName myLifecycleHook -AutoScalingGroupName my-asg -LifecycleActionResult CONTINUE -LifecycleActionToken bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635
```
+  For API details, see [CompleteLifecycleAction](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
