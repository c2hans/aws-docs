---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/step-scaling-create-scale-in-policy.html
---

# Create a step scaling policy for scale in
<a name="step-scaling-create-scale-in-policy"></a>

To create a step scaling policy for scale in for your Auto Scaling group, use one of the following methods:

------
#### [ Console ]

**Step 1: Create a CloudWatch alarm for the metric low threshold**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. If necessary, change the Region. From the navigation bar, select the Region where your Auto Scaling group resides.

1. In the navigation pane, choose **Alarms, All alarms** and then choose **Create alarm**.

1. Choose **Select metric**.

1. On the **All metrics** tab, choose **EC2**, **By Auto Scaling Group**, and enter the Auto Scaling group's name in the search field. Then, select `CPUUtilization` and choose **Select metric**. The **Specify metric and conditions** page appears, showing a graph and other information about the metric.

1. For **Period**, choose the evaluation period for the alarm, for example, 1 minute. When evaluating the alarm, each period is aggregated into one data point.
**Note**
A shorter period creates a more sensitive alarm.

1. Under **Conditions**, do the following:
   + For **Threshold type**, choose **Static**.
   + For **Whenever `CPUUtilization` is**, specify whether you want the value of the metric to be less than or less than or equal to the threshold to breach the alarm. Then, under **than**, enter the threshold value that you want to breach the alarm.
**Important**
For an alarm to use with a scale in policy (metric low), make sure you do not choose greater than or greater than or equal to the threshold.

1. Under **Additional configuration**, do the following:
   + For **Datapoints to alarm**, enter the number of data points (evaluation periods) during which the metric value must meet the threshold conditions for the alarm. For example, two consecutive periods of 5 minutes would take 10 minutes to invoke the alarm state.
   + For **Missing data treatment**, choose **Treat missing data as bad (breaching threshold)**. For more information, see [Configuring how CloudWatch alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data) in the *Amazon CloudWatch User Guide*.

1. Choose **Next**.

   The **Configure actions** page appears.

1. Under **Notification**, select an Amazon SNS topic to notify when the alarm is in `ALARM` state, `OK` state, or `INSUFFICIENT_DATA` state.

   To have the alarm send multiple notifications for the same alarm state or for different alarm states, choose **Add notification**.

   To have the alarm not send notifications, choose **Remove**.

1. You can leave the other sections of the **Configure actions** page empty. Leaving the other sections empty creates an alarm without associating it to a scaling policy. You can then associate the alarm with a scaling policy from the Amazon EC2 Auto Scaling console.

1. Choose **Next**.

1. Enter a name (for example, `Step-Scaling-AlarmLow-RemoveCapacity`) and, optionally, a description for the alarm, and then choose **Next**.

1. Choose **Create alarm**.

Use the following procedure to continue where you left off after creating your CloudWatch alarm.

**Step 2: Create a step scaling policy for scale in**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. Verify that the scaling limits are appropriately set. For example, if your group's desired capacity is already at its minimum, you need to specify a new minimum in order to scale in. For more information, see [Set scaling limits for your Auto Scaling group](asg-capacity-limits.md).

1. On the **Automatic scaling** tab, in **Dynamic scaling policies**, choose **Create dynamic scaling policy**.

1. For **Policy type**, choose **Step scaling**, and then specify a name for the policy.

1. For **CloudWatch alarm**, choose your alarm. If you haven't already created an alarm, choose **Create a CloudWatch alarm** and complete step 4 through step 14 in the previous procedure to create an alarm.

1. Specify the change in the current group size that this policy will make when executed using **Take the action**. You can remove a specific number of instances or a percentage of the existing group size, or set the group to an exact size.

   For example, to create a scale in policy that decreases the capacity of the group by two instances, choose `Remove`, enter `2` in the next field, and then choose `capacity units`. By default, the upper bound for this step adjustment is the alarm threshold and the lower bound is negative (-) infinity.

1. To add another step, choose **Add step** and then define the amount by which to scale and the lower and upper bounds of the step relative to the alarm threshold.

1. Choose **Create**.

------
#### [ AWS CLI ]

To create a step scaling policy for scale in (decrease capacity), you can use the following example commands. Replace each {{user input placeholder}} with your own information.

When you use the AWS CLI, you first create a step scaling policy that provides instructions to Amazon EC2 Auto Scaling about how to scale in when a metric's value is decreasing. Then, you create the alarm by identifying the metric to watch, defining the metric low threshold and other details for the alarms, and associating the alarm with the scaling policy.

**Step 1: Create a policy for scale in**
Use the following [put-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scaling-policy.html) command to create a step scaling policy named `my-step-scale-in-policy`, with an adjustment type of `ChangeInCapacity` that decreases the capacity of the group by 2 instances when the associated CloudWatch alarm breaches the metric low threshold value.

```
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name {{my-asg}}  \
  --policy-name {{my-step-scale-in-policy}} \
  --policy-type StepScaling \
  --adjustment-type ChangeInCapacity \
  --step-adjustments MetricIntervalUpperBound={{0.0}},ScalingAdjustment={{-2}}
```

Record the policy's Amazon Resource Name (ARN). You need it to create the CloudWatch alarm for the policy.

```
{
    "PolicyARN": "arn:aws:autoscaling:{{region}}:{{123456789012}}:scalingPolicy:{{ac542982-cbeb-4294-891c-a5a941dfa787}}:autoScalingGroupName/{{my-asg}}:policyName/{{my-step-scale-out-policy}}
}
```

**Step 2: Create a CloudWatch alarm for the metric low threshold**
Use the following CloudWatch [put-metric-alarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html) command to create an alarm that decreases the size of the Auto Scaling group based on average CPU threshold value of 40 percent for at least two consecutive evaluation periods of two minutes. To use your own custom metric, specify its name in `--metric-name` and its namespace in `--namespace`.

```
aws cloudwatch put-metric-alarm --alarm-name {{Step-Scaling-AlarmLow-RemoveCapacity}} \
  --metric-name {{CPUUtilization}} --namespace {{AWS/EC2}} --statistic Average \
  --period {{120}} --evaluation-periods {{2}} --threshold {{40}} \
  --comparison-operator LessThanOrEqualToThreshold \
  --dimensions "Name=AutoScalingGroupName,Value={{my-asg}}" \
  --alarm-actions {{PolicyARN}}
```

------
