---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DeleteNotificationConfiguration_section.html
---

# Use `DeleteNotificationConfiguration` with a CLI
<a name="example_auto-scaling_DeleteNotificationConfiguration_section"></a>

The following code examples show how to use `DeleteNotificationConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**To delete an Auto Scaling notification**
This example deletes the specified notification from the specified Auto Scaling group.

```
aws autoscaling delete-notification-configuration \
    --auto-scaling-group-name {{my-asg}} \
    --topic-arn {{arn:aws:sns:us-west-2:123456789012:my-sns-topic}}
```
This command produces no output.
For more information, see [Delete the notification configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html#delete-settingupnotifications) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DeleteNotificationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-notification-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified notification action. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASNotificationConfiguration -AutoScalingGroupName my-asg -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASNotificationConfiguration (DeleteNotificationConfiguration)" on Target
"arn:aws:sns:us-west-2:123456789012:my-topic".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASNotificationConfiguration -AutoScalingGroupName my-asg -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic" -Force
```
+  For API details, see [DeleteNotificationConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified notification action. You are prompted for confirmation before the operation proceeds.**

```
Remove-ASNotificationConfiguration -AutoScalingGroupName my-asg -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ASNotificationConfiguration (DeleteNotificationConfiguration)" on Target
"arn:aws:sns:us-west-2:123456789012:my-topic".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: If you specify the Force parameter, you are not prompted for confirmation before the operation proceeds.**

```
Remove-ASNotificationConfiguration -AutoScalingGroupName my-asg -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic" -Force
```
+  For API details, see [DeleteNotificationConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
