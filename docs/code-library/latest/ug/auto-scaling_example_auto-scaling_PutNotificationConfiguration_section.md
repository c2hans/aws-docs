---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_PutNotificationConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutNotificationConfiguration` with a CLI
<a name="auto-scaling_example_auto-scaling_PutNotificationConfiguration_section"></a>

The following code examples show how to use `PutNotificationConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**To add a notification**
This example adds the specified notification to the specified Auto Scaling group.

```
aws autoscaling put-notification-configuration \
    --auto-scaling-group-name {{my-asg}} \
    --topic-arn {{arn:aws:sns:us-west-2:123456789012:my-sns-topic}} \
    --notification-type {{autoscaling:TEST_NOTIFICATION}}
```
This command produces no output.
For more information, see [Getting Amazon SNS notifications when your Auto Scaling group scales](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html#as-configure-asg-for-sns) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [PutNotificationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-notification-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example configures the specified Auto Scaling group to send a notification to the specified SNS topic when it launches EC2 instances.**

```
Write-ASNotificationConfiguration -AutoScalingGroupName my-asg -NotificationType "autoscaling:EC2_INSTANCE_LAUNCH" -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
**Example 2: This example configures the specified Auto Scaling group to send a notification to the specified SNS topic when it launches or terminates EC2 instances.**

```
Write-ASNotificationConfiguration -AutoScalingGroupName my-asg -NotificationType @("autoscaling:EC2_INSTANCE_LAUNCH", "autoscaling:EC2_INSTANCE_TERMINATE") -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
+  For API details, see [PutNotificationConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example configures the specified Auto Scaling group to send a notification to the specified SNS topic when it launches EC2 instances.**

```
Write-ASNotificationConfiguration -AutoScalingGroupName my-asg -NotificationType "autoscaling:EC2_INSTANCE_LAUNCH" -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
**Example 2: This example configures the specified Auto Scaling group to send a notification to the specified SNS topic when it launches or terminates EC2 instances.**

```
Write-ASNotificationConfiguration -AutoScalingGroupName my-asg -NotificationType @("autoscaling:EC2_INSTANCE_LAUNCH", "autoscaling:EC2_INSTANCE_TERMINATE") -TopicARN "arn:aws:sns:us-west-2:123456789012:my-topic"
```
+  For API details, see [PutNotificationConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
