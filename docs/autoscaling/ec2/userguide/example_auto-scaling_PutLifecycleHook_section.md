---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_PutLifecycleHook_section.html
---

# Use `PutLifecycleHook` with a CLI
<a name="example_auto-scaling_PutLifecycleHook_section"></a>

The following code examples show how to use `PutLifecycleHook`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To create a lifecycle hook**
This example creates a lifecycle hook that will invoke on any newly launched instances, with a timeout of 4800 seconds. This is useful for keeping the instances in a wait state until the user data scripts have finished, or for invoking an AWS Lambda function using EventBridge.

```
aws autoscaling put-lifecycle-hook \
    --auto-scaling-group-name {{my-asg}} \
    --lifecycle-hook-name {{my-launch-hook}} \
    --lifecycle-transition {{autoscaling:EC2_INSTANCE_LAUNCHING}} \
    --heartbeat-timeout {{4800}}
```
This command produces no output. If a lifecycle hook with the same name already exists, it will be overwritten by the new lifecycle hook.
For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 2: To send an Amazon SNS email message to notify you of instance state transitions**
This example creates a lifecycle hook with the Amazon SNS topic and IAM role to use to receive notification at instance launch.

```
aws autoscaling put-lifecycle-hook \
    --auto-scaling-group-name {{my-asg}} \
    --lifecycle-hook-name {{my-launch-hook}} \
    --lifecycle-transition {{autoscaling:EC2_INSTANCE_LAUNCHING}} \
    --notification-target-arn {{arn:aws:sns:us-west-2:123456789012:my-sns-topic}} \
    --role-arn {{arn:aws:iam::123456789012:role/my-auto-scaling-role}}
```
This command produces no output.
For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 3: To publish a message to an Amazon SQS queue**
This example creates a lifecycle hook that publishes a message with metadata to the specified Amazon SQS queue.

```
aws autoscaling put-lifecycle-hook \
    --auto-scaling-group-name {{my-asg}} \
    --lifecycle-hook-name {{my-launch-hook}} \
    --lifecycle-transition {{autoscaling:EC2_INSTANCE_LAUNCHING}} \
    --notification-target-arn {{arn:aws:sqs:us-west-2:123456789012:my-sqs-queue}} \
    --role-arn {{arn:aws:iam::123456789012:role/my-notification-role}} \
    --notification-metadata {{"SQS message metadata"}}
```
This command produces no output.
For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [PutLifecycleHook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds the specified lifecycle hook to the specified Auto Scaling group.**

```
Write-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName "myLifecycleHook" -LifecycleTransition "autoscaling:EC2_INSTANCE_LAUNCHING" -NotificationTargetARN "arn:aws:sns:us-west-2:123456789012:my-sns-topic" -RoleARN "arn:aws:iam::123456789012:role/my-iam-role"
```
+  For API details, see [PutLifecycleHook](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds the specified lifecycle hook to the specified Auto Scaling group.**

```
Write-ASLifecycleHook -AutoScalingGroupName my-asg -LifecycleHookName "myLifecycleHook" -LifecycleTransition "autoscaling:EC2_INSTANCE_LAUNCHING" -NotificationTargetARN "arn:aws:sns:us-west-2:123456789012:my-sns-topic" -RoleARN "arn:aws:iam::123456789012:role/my-iam-role"
```
+  For API details, see [PutLifecycleHook](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
