---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DeleteLifecycleHook_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteLifecycleHook` with a CLI
<a name="auto-scaling_example_auto-scaling_DeleteLifecycleHook_section"></a>

The following code examples show how to use `DeleteLifecycleHook`.

------
#### [ CLI ]

**AWS CLI**
**To delete a lifecycle hook**
This example deletes the specified lifecycle hook.

```
aws autoscaling delete-lifecycle-hook \
    --lifecycle-hook-name {{my-lifecycle-hook}} \
    --auto-scaling-group-name {{my-asg}}
```
This command produces no output.
+  For API details, see [DeleteLifecycleHook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-lifecycle-hook.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified lifecycle hook for the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASLifecycleHook (DeleteLifecycleHook)" on Target "myLifecycleHook".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook -Force
```
+  For API details, see [DeleteLifecycleHook](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified lifecycle hook for the specified Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASLifecycleHook (DeleteLifecycleHook)" on Target "myLifecycleHook".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName myLifecycleHook -Force
```
+  For API details, see [DeleteLifecycleHook](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
