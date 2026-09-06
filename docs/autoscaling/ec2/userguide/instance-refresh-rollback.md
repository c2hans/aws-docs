---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-rollback.html
---

# Undo changes with a manual or auto rollback
<a name="instance-refresh-rollback"></a>

You can roll back an instance refresh that is still in progress. You can't roll it back after it's finished. You can, however, update your Auto Scaling group again by starting a new instance refresh.

When rolling back, Amazon EC2 Auto Scaling replaces the instances that have been deployed so far. The new instances match the configuration that you last saved on the Auto Scaling group before starting the instance refresh.

Amazon EC2 Auto Scaling provides the following ways to roll back:
+ Manual rollback: You start a rollback manually to reverse what was deployed up to the rollback point.
+ Auto rollback: Amazon EC2 Auto Scaling automatically reverses what was deployed if the instance refresh fails for some reason or if any CloudWatch alarms you specify go into the `ALARM` state.

**Topics**
+ [Considerations](#instance-refresh-rollback-considerations)
+ [Manually start a rollback](#instance-refresh-manual-rollback)
+ [Start an instance refresh with auto rollback](#instance-refresh-using-auto-rollback)

## Considerations
<a name="instance-refresh-rollback-considerations"></a>

The following considerations apply when using a rollback:
+ The rollback option is only available if you specify a desired configuration as part of starting an instance refresh.
+ You can only roll back to a previous version of a launch template if the version is a specific numbered version. The rollback option is not available if the Auto Scaling group is configured to use the `$Latest` or `$Default` launch template version.
+ You also cannot roll back to a launch template that is configured to use an AMI alias from the AWS Systems Manager Parameter Store.
+ The configuration that you last saved on the Auto Scaling group must be in a stable state. If it's not in a stable state, the rollback workflow will still occur, but it will eventually fail. Until you resolve the issue, the Auto Scaling group might be in a failed state where it can no longer launch instances successfully. This might impact the availability of the service or application.

## Manually start a rollback
<a name="instance-refresh-manual-rollback"></a>

------
#### [ Console ]

**To manually start a rollback of an instance refresh (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

1. On the **Instance refresh** tab, in **Active instance refresh**, choose **Actions**, **Start rollback**.

1. When prompted for confirmation, choose **Confirm**.

------
#### [ AWS CLI ]

**To manually start a rollback of an instance refresh (AWS CLI)**
Use the [rollback-instance-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/rollback-instance-refresh.html) command from the AWS CLI and provide the Auto Scaling group name.

```
aws autoscaling rollback-instance-refresh --auto-scaling-group-name {{my-asg}}
```

Example output:

```
{
    "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b"
}
```

**Tip**
If this command throws an error, make sure that you have updated the AWS CLI locally to the latest version.

------

## Start an instance refresh with auto rollback
<a name="instance-refresh-using-auto-rollback"></a>

Using the auto rollback feature, you can automatically roll back the instance refresh when it fails, such as when there are errors or a specified Amazon CloudWatch alarm goes into the `ALARM` state.

If you enable auto rollback, and there are errors while replacing instances, the instance refresh attempts to complete all replacements for one hour before it fails and rolls back. These errors are usually caused by things like EC2 launch failures, misconfigured health checks, or not ignoring or allowing the termination of instances that are in `Standby` state or protected from scale in.

Specifying CloudWatch alarms is optional. To specify an alarm, you first need to create it. You can specify metric alarms and composite alarms. For information about creating the alarm, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). Using Elastic Load Balancing metrics as an example, if you use an Application Load Balancer, you could use the `HTTPCode_ELB_5XX_Count` and `HTTPCode_ELB_4XX_Count` metrics.

**Considerations**
+ If you specify a CloudWatch alarm but do not enable auto rollback, and the alarm state goes to `ALARM`, the instance refresh fails without rolling back.
+ You can choose a maximum of 10 alarms when you start an instance refresh.
+ When choosing a CloudWatch alarm, the alarm must be in a compatible state. If the alarm state is `INSUFFICIENT_DATA` or `ALARM`, you receive an error when you try to start the instance refresh.
+ When creating an alarm for Amazon EC2 Auto Scaling to use, the alarm should include how to treat missing data points. If a metric is frequently missing data points by design, the state of the alarm is `INSUFFICIENT_DATA` during those periods. When this happens, Amazon EC2 Auto Scaling cannot replace instances until new data points are found. To force the alarm to maintain the previous `ALARM` or `OK` state, you could choose to ignore missing data instead. For more information, see [Configuring how alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data) in the *Amazon CloudWatch User Guide*.

------
#### [ Console ]

**To start an instance refresh with auto rollback (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

1. On the **Instance refresh** tab, in **Active instance refresh**, choose **Start instance refresh**.

1. Follow the [Start an instance refresh (console)](start-instance-refresh.md#start-instance-refresh-console) procedure and configure your instance refresh settings as needed.

1. (Optional) Under **Refresh settings**, for **CloudWatch alarm**, choose **Enable CloudWatch alarms**, and then choose one or more alarms to identify any issues and fail the operation if an alarm goes into the `ALARM` state.

1. Under **Rollback settings**, choose **Enable auto rollback** to automatically roll back a failed instance refresh to the configuration that you last saved on the Auto Scaling group before starting the instance refresh.

1. Review your selections, and then choose **Start instance refresh**.

------
#### [ AWS CLI ]

**To start an instance refresh with auto rollback (AWS CLI)**
Use the [start-instance-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/start-instance-refresh.html) command and specify `true` for the `AutoRollback` option in the `Preferences`.

The following example shows how to start an instance refresh that will automatically roll back if something fails. Replace the {{`italicized`}} parameter values with your own.

```
aws autoscaling start-instance-refresh --cli-input-json file://config.json
```

Contents of `config.json`.

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "DesiredConfiguration": {
{{      "LaunchTemplate": {
          "LaunchTemplateName": "my-launch-template",
          "Version": "1"
       }}}
    },
    "Preferences": {
      "AutoRollback": true
    }
}
```

Alternatively, to automatically roll back when the instance refresh fails or when a specified CloudWatch alarm is in the `ALARM` state, specify the `AlarmSpecification` option in the `Preferences` and provide the alarm name, as in the following example. Replace the {{`italicized`}} parameter values with your own.

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "DesiredConfiguration": {
{{      "LaunchTemplate": {
          "LaunchTemplateName": "my-launch-template",
          "Version": "1"
       }}}
    },
    "Preferences": {
      "AutoRollback": true,
      "AlarmSpecification": { "Alarms": [ "{{my-alarm}}" ] }
    }
}
```

If successful, the command returns output similar to the following.

```
{
  "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b"
}
```

**Tip**
If this command throws an error, make sure that you have updated the AWS CLI locally to the latest version.

------
