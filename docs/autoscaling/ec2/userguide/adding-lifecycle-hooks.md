---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/adding-lifecycle-hooks.html
---

# Add lifecycle hooks to your Auto Scaling group
<a name="adding-lifecycle-hooks"></a>

To put your Auto Scaling instances into a wait state and perform custom actions on them, you can add lifecycle hooks to your Auto Scaling group. Custom actions are performed as the instances launch or before they terminate. Instances remain in a wait state until you either complete the lifecycle action, or the timeout period ends.

After you create an Auto Scaling group from the AWS Management Console, you can add one or more lifecycle hooks to it, up to a total of 50 lifecycle hooks. You can also use the AWS CLI, CloudFormation, or an SDK to add lifecycle hooks to an Auto Scaling group as you are creating it.

By default, when you add a lifecycle hook in the console, Amazon EC2 Auto Scaling sends lifecycle event notifications to Amazon EventBridge. Using EventBridge or a user data script is a recommended best practice. To create a lifecycle hook that sends notifications directly to Amazon SNS, Amazon SQS, or AWS Lambda you can use the [put-lifecycle-hook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html) command, as shown in the examples in this topic.

**Topics**
+ [Add lifecycle hooks (console)](#adding-lifecycle-hooks-console)
+ [Add lifecycle hooks (AWS CLI)](#adding-lifecycle-hooks-aws-cli)

## Add lifecycle hooks (console)
<a name="adding-lifecycle-hooks-console"></a>

Follow these steps to add lifecycle hooks to your Auto Scaling group. To add lifecycle hooks for scaling out (instances launching) and scaling in (instances terminating or returning to a warm pool), you must create two separate hooks.

Before you begin, confirm that you have set up a custom action, as needed, as described in [Prepare to add a lifecycle hook to your Auto Scaling group](prepare-for-lifecycle-notifications.md).

**To add a lifecycle hook for scale out**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group. A split pane opens up in the bottom of the page.

1. On the **Instance management** tab, in **Lifecycle hooks**, choose **Create lifecycle hook**.

1. To define a lifecycle hook for scale out (instances launching), do the following:

   1. For **Lifecycle hook name**, specify a name for the lifecycle hook.

   1. For **Lifecycle transition**, choose **Instance launch**.

   1. For **Heartbeat timeout**, specify the amount of time, in seconds, for instances to remain in a wait state when scaling out before the hook times out. The range is from `30` to `7200` seconds. Setting a long timeout period provides more time for your custom action to complete. Then, if you finish before the timeout period ends, send the [complete-lifecycle-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/complete-lifecycle-action.html) command to allow the instance to proceed to the next state.

   1. For **Default result**, specify the action to take when the lifecycle hook timeout elapses or when an unexpected failure occurs. You can choose to either **CONTINUE** or **ABANDON**.
      + If you choose **CONTINUE**, the Auto Scaling group can proceed with any other lifecycle hooks and then put the instance into service.
      + If you choose **ABANDON**, the Auto Scaling group stops any remaining actions and terminates the instance immediately.

   1. (Optional) For **Notification metadata**, specify other information that you want to include when Amazon EC2 Auto Scaling sends a message to the notification target.

1. Choose **Create**.

**To add a lifecycle hook for scale in**

1. Choose **Create lifecycle hook** to continue where you left off after creating a lifecycle hook for scale out.

1. To define a lifecycle hook for scale in (instances terminating or returning to a warm pool), do the following:

   1. For **Lifecycle hook name**, specify a name for the lifecycle hook.

   1. For **Lifecycle transition**, choose **Instance terminate**.

   1. For **Heartbeat timeout**, specify the amount of time, in seconds, for instances to remain in a wait state when scaling out before the hook times out. We recommend a short timeout period of `30` to `120` seconds, depending on how much time you need to perform any final tasks, such as pulling EC2 logs from CloudWatch.

   1. For **Default result**, specify the action that the Auto Scaling group takes when the timeout elapses or if an unexpected failure occurs. Both **ABANDON** and **CONTINUE** let the instance terminate.
      + If you choose **CONTINUE**, the Auto Scaling group can proceed with any remaining actions, such as other lifecycle hooks, before termination.
      + If you choose **ABANDON**, the Auto Scaling group terminates the instance immediately.

   1. (Optional) For **Notification metadata**, specify other information that you want to include when Amazon EC2 Auto Scaling sends a message to the notification target.

1. Choose **Create**.

## Add lifecycle hooks (AWS CLI)
<a name="adding-lifecycle-hooks-aws-cli"></a>

Create and update lifecycle hooks using the [put-lifecycle-hook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html) command.

To perform an action on scale out, use the following command.

```
aws autoscaling put-lifecycle-hook --lifecycle-hook-name {{my-launch-hook}}  \
  --auto-scaling-group-name {{my-asg}} \
  --lifecycle-transition autoscaling:EC2_INSTANCE_LAUNCHING
```

To perform an action on scale in, use the following command instead.

```
aws autoscaling put-lifecycle-hook --lifecycle-hook-name {{my-termination-hook}}  \
  --auto-scaling-group-name {{my-asg}} \
  --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING
```

To receive notifications using Amazon SNS or Amazon SQS, add the `--notification-target-arn` and `--role-arn` options. To receive notifications using AWS Lambda, add the `--notification-target-arn`.

The following example creates a lifecycle hook that specifies an SNS topic named `{{my-sns-topic}}` as the notification target.

```
aws autoscaling put-lifecycle-hook --lifecycle-hook-name {{my-termination-hook}}  \
  --auto-scaling-group-name {{my-asg}} \
  --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING \
  --notification-target-arn arn:aws:sns:{{region}}:{{123456789012}}:{{my-sns-topic}} \
  --role-arn arn:aws:iam::{{123456789012}}:role/{{my-notification-role}}
```

The topic receives a test notification with the following key-value pair.

```
"Event": "autoscaling:TEST_NOTIFICATION"
```

By default, the [put-lifecycle-hook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html) command creates a lifecycle hook with a heartbeat timeout of `3600` seconds (one hour).

To change the heartbeat timeout for an existing lifecycle hook, add the `--heartbeat-timeout` option, as shown in the following example.

```
aws autoscaling put-lifecycle-hook --lifecycle-hook-name {{my-termination-hook}} \
  --auto-scaling-group-name {{my-asg}} --heartbeat-timeout {{120}}
```

If an instance is already in a wait state, you can prevent the lifecycle hook from timing out by recording a heartbeat, using the [record-lifecycle-action-heartbeat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/record-lifecycle-action-heartbeat.html) CLI command. This extends the timeout period by the timeout value specified when you created the lifecycle hook. If you finish before the timeout period ends, you can send the [complete-lifecycle-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/complete-lifecycle-action.html) CLI command to allow the instance to proceed to the next state. For more information and examples, see [Complete a lifecycle action in an Auto Scaling group](completing-lifecycle-hooks.md).
