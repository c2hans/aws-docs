---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DeleteNotificationConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteNotificationConfiguration` with a CLI
<a name="auto-scaling_example_auto-scaling_DeleteNotificationConfiguration_section"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
