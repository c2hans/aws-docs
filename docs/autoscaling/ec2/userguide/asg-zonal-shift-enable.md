---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-zonal-shift-enable.html
---

# Enable zonal shift using the AWS Management Console or the AWS CLI
<a name="asg-zonal-shift-enable"></a>

To enable zonal shift, use one of the following methods.

------
#### [ Console ]

**To enable zonal shift on a new group (console)**

1. Follow the instructions in [Create an Auto Scaling group using a launch template](create-asg-launch-template.md) and complete each step in the procedure, up to step 10.

1. On the **Integrate with other services** page, for **Application Recovery Controller (ARC) zonal shift**, select the checkbox to enable zonal shift.

1. For **Health check behavior**, choose Ignore unhealthy or Replace unhealthy. For more information, see [How zonal shift works for Auto Scaling groups](ec2-auto-scaling-zonal-shift.md#asg-zonal-shift-how-it-works).

1. Continue with the steps in [Create an Auto Scaling group using a launch template](create-asg-launch-template.md).

------
#### [ AWS CLI ]

**To enable zonal shift on a new group (AWS CLI)**
Add the `--availability-zone-impairment-policy` parameter to the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command.

The `--availability-zone-impairment-policy` parameter has two options:
+ **ZonalShiftEnabled** – If set to `true`, Auto Scaling registers the Auto Scaling group with ARC zonal shift and you can [start, update, or cancel a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html) on the ARC console. If set to `false`, Auto Scaling deregisters the Auto Scaling group from ARC zonal shift. You must already have zonal shift enabled to set to `false`.
+ **ImpairedZoneHealthCheckBehavior** – If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see [How zonal shift works for Auto Scaling groups](ec2-auto-scaling-zonal-shift.md#asg-zonal-shift-how-it-works).

The following example enables zonal shift on a new Auto Scaling group named `{{my-asg}}`.

```
aws autoscaling create-auto-scaling-group \
  --launch-template LaunchTemplateName={{my-launch-template}},Version='{{1}}' \
  --auto-scaling-group-name {{my-asg}} \
  --min-size {{1}} \
  --max-size {{10}} \
  --desired-capacity {{5}} \
  --availability-zones {{us-east-1a}} {{us-east-1b}} {{us-east-1c}} \
  --availability-zone-impairment-policy '{
      "ZonalShiftEnabled": {{true}},
      "ImpairedZoneHealthCheckBehavior": {{IgnoreUnhealthy}}
    }'
```

------

------
#### [ Console ]

**To enable zonal shift on an existing group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Integrations** tab, under **Application Recovery Controller (ARC) zonal shift**, choose **Edit**.

1. Select the checkbox to enable zonal shift.

1. For **Health check behavior**, choose Ignore unhealthy or Replace unhealthy. For more information, see [How zonal shift works for Auto Scaling groups](ec2-auto-scaling-zonal-shift.md#asg-zonal-shift-how-it-works).

1. Choose **Update**.

------
#### [ AWS CLI ]

**To enable zonal shift on an existing group (AWS CLI)**
Add the `--availability-zone-impairment-policy` parameter to the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

The `--availability-zone-impairment-policy` parameter has two options:
+ **ZonalShiftEnabled** – If set to `true`, Auto Scaling registers the Auto Scaling group with ARC zonal shift and you can [start, update, or cancel a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html) on the ARC console. If set to `false`, Auto Scaling deregisters the Auto Scaling group from ARC zonal shift. You must already have zonal shift enabled to set to `false`.
+ **ImpairedZoneHealthCheckBehavior** – If set to `replace-unhealthy`, unhealthy instances will be replaced in the Availability Zone with the active zonal shift. If set to `ignore-unhealthy`, unhealthy instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see [How zonal shift works for Auto Scaling groups](ec2-auto-scaling-zonal-shift.md#asg-zonal-shift-how-it-works).

The following example enables zonal shift on the specified Auto Scaling group.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --availability-zone-impairment-policy '{
      "ZonalShiftEnabled": {{true}},
      "ImpairedZoneHealthCheckBehavior": {{IgnoreUnhealthy}}
    }'
```

------
