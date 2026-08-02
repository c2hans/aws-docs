---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DescribeAutoScalingNotificationTypes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeAutoScalingNotificationTypes` with a CLI
<a name="auto-scaling_example_auto-scaling_DescribeAutoScalingNotificationTypes_section"></a>

The following code examples show how to use `DescribeAutoScalingNotificationTypes`.

------
#### [ CLI ]

**AWS CLI**
**To describe the available notification types**
This example describes the available notification types.

```
aws autoscaling describe-auto-scaling-notification-types
```
Output:

```
{
    "AutoScalingNotificationTypes": [
        "autoscaling:EC2_INSTANCE_LAUNCH",
        "autoscaling:EC2_INSTANCE_LAUNCH_ERROR",
        "autoscaling:EC2_INSTANCE_TERMINATE",
        "autoscaling:EC2_INSTANCE_TERMINATE_ERROR",
        "autoscaling:TEST_NOTIFICATION"
    ]
}
```
For more information, see [Getting Amazon SNS notifications when your Auto Scaling group scales](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DescribeAutoScalingNotificationTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-notification-types.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the notification types that are supported by Auto Scaling.**

```
Get-ASAutoScalingNotificationType
```
**Output:**

```
autoscaling:EC2_INSTANCE_LAUNCH
autoscaling:EC2_INSTANCE_LAUNCH_ERROR
autoscaling:EC2_INSTANCE_TERMINATE
autoscaling:EC2_INSTANCE_TERMINATE_ERROR
autoscaling:TEST_NOTIFICATION
```
+  For API details, see [DescribeAutoScalingNotificationTypes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the notification types that are supported by Auto Scaling.**

```
Get-ASAutoScalingNotificationType
```
**Output:**

```
autoscaling:EC2_INSTANCE_LAUNCH
autoscaling:EC2_INSTANCE_LAUNCH_ERROR
autoscaling:EC2_INSTANCE_TERMINATE
autoscaling:EC2_INSTANCE_TERMINATE_ERROR
autoscaling:TEST_NOTIFICATION
```
+  For API details, see [DescribeAutoScalingNotificationTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
