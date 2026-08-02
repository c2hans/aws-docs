---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-checkpoints-console-cli.html
---

# Enable checkpoints using the using the AWS Management Console or AWS CLI
<a name="enable-checkpoints-console-cli"></a>

You can use the AWS Management Console or AWS CLI to enable checkpoints.

## Enable checkpoints (console)
<a name="enable-checkpoints-console"></a>

You can enable checkpoints before starting an instance refresh to replace instances using an incremental or phased approach. This provides additional time for verification.

**To start an instance refresh that uses checkpoints**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up at the bottom of the **Auto Scaling groups** page.

1. On the **Instance refresh** tab, in **Active instance refresh**, choose **Start instance refresh**.

1. On the **Start instance refresh** page, enter the values for **Minimum healthy percentage** and **Instance warmup**.

1. Select the **Enable checkpoints** check box.

   This displays a box where you can define the percentage threshold for the first checkpoint.

1. For **Proceed until \_\_\_\_ % of the group is refreshed**, enter a number (1–100). This sets the percentage for the first checkpoint.

1. To add another checkpoint, choose **Add checkpoint** and then define the percentage for the next checkpoint.

1. To specify how long Amazon EC2 Auto Scaling waits after a checkpoint is reached, update the fields in **Wait for `1` `hour` between checkpoints**. The time unit can be hours, minutes, or seconds.

1. If you are finished with your instance refresh selections, choose **Start instance refresh**.

## Enable checkpoints (AWS CLI)
<a name="enable-checkpoints-cli"></a>

To start an instance refresh with checkpoints enabled using the AWS CLI, you need a configuration file that defines the following parameters:
+ `CheckpointPercentages`: Specifies threshold values for the percentage of instances to be replaced. These threshold values provide the checkpoints. When the percentage of instances that are replaced and warmed up reaches one of the specified thresholds, the operation waits for a specified period of time. You specify the number of seconds to wait in `CheckpointDelay`. When the specified period of time has passed, the instance refresh continues until it reaches the next checkpoint (if applicable).
+ `CheckpointDelay`: Specifies the amount of time, in seconds, to wait after a checkpoint is reached before continuing. Choose a time period that provides enough time to perform your verifications.

The last value shown in the `CheckpointPercentages` array describes the percentage of the Auto Scaling group that needs to be successfully replaced. The operation transitions to `Successful` after this percentage is successfully replaced and each instance is considered to have finished initializing.

**To create multiple checkpoints**
To create multiple checkpoints, use the following example [start-instance-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/start-instance-refresh.html) command. This example configures an instance refresh that initially refreshes one percent of the Auto Scaling group. After waiting 10 minutes, it then refreshes the next 19 percent and waits another 10 minutes. Finally, it refreshes the rest of the group before concluding the operation.

```
aws autoscaling start-instance-refresh --cli-input-json file://config.json
```

Contents of `config.json`:

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "Preferences": {
      "InstanceWarmup": {{60}},
      "MinHealthyPercentage": {{80}},
      "CheckpointPercentages": [{{1,20,100}}],
      "CheckpointDelay": {{600}}
    }
}
```

**To create a single checkpoint**
To create a single checkpoint, use the following example [start-instance-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/start-instance-refresh.html) command. This example configures an instance refresh that initially refreshes 20 percent of the Auto Scaling group. After waiting 10 minutes, it then refreshes the rest of the group before concluding the operation.

```
aws autoscaling start-instance-refresh --cli-input-json file://config.json
```

Contents of `config.json`:

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "Preferences": {
      "InstanceWarmup": {{60}},
      "MinHealthyPercentage": {{80}},
      "CheckpointPercentages": [{{20,100}}],
      "CheckpointDelay": {{600}}
    }
}
```

**To partially refresh the Auto Scaling group**
To replace only a portion of your Auto Scaling group and then stop completely, use the following example [start-instance-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/start-instance-refresh.html) command. This example configures an instance refresh that initially refreshes one percent of the Auto Scaling group. After waiting 10 minutes, it then refreshes the next 19 percent before concluding the operation.

```
aws autoscaling start-instance-refresh --cli-input-json file://config.json
```

Contents of `config.json`:

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "Preferences": {
      "InstanceWarmup": {{60}},
      "MinHealthyPercentage": {{80}},
      "CheckpointPercentages": [{{1,20}}],
      "CheckpointDelay": {{600}}
    }
}
```
