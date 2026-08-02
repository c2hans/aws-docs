---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteLaunchConfiguration_section.html
---

# Use `DeleteLaunchConfiguration` with a CLI
<a name="example_auto-scaling_DeleteLaunchConfiguration_section"></a>

The following code examples show how to use `DeleteLaunchConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**To delete a launch configuration**
This example deletes the specified launch configuration.

```
aws autoscaling delete-launch-configuration \
    --launch-configuration-name {{my-launch-config}}
```
This command produces no output.
For more information, see [Deleting your Auto Scaling infrastructure](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DeleteLaunchConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-launch-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified launch configuration if it is not attached to an Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASLaunchConfiguration -LaunchConfigurationName my-lc
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASLaunchConfiguration (DeleteLaunchConfiguration)" on Target "my-lc".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASLaunchConfiguration -LaunchConfigurationName my-lc -Force
```
+  For API details, see [DeleteLaunchConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified launch configuration if it is not attached to an Auto Scaling group. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASLaunchConfiguration -LaunchConfigurationName my-lc
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASLaunchConfiguration (DeleteLaunchConfiguration)" on Target "my-lc".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASLaunchConfiguration -LaunchConfigurationName my-lc -Force
```
+  For API details, see [DeleteLaunchConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
