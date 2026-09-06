---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/capacity-reservation-create-asg-procedure.html
---

# Configure your Auto Scaling group to launch instances with Capacity Reservations
<a name="capacity-reservation-create-asg-procedure"></a>

To configure your Auto Scaling group to launch instances with Amazon EC2 Capacity Reservations and Capacity Blocks for ML, choose the procedure that matches your approach:
+ For On-Demand Capacity Reservations, see [Use a Capacity Reservation specification](#use-a-capacity-reservation-specification).
+ For Capacity Blocks or interruptible Capacity Reservations, see [Target Capacity Blocks or interruptible Capacity Reservations from a launch template](#target-capacity-blocks-or-interruptible-capacity-reservations-from-a-launch-template).
+ For mixing multiple reservation types (for example, On-Demand Capacity Reservations and Capacity Blocks) in the same Auto Scaling group, see [Use Distribution Segments to target multiple Capacity Reservation types](use-distribution-segments.md).
+ For background on Capacity Reservation targeting options and behavior, see [Target Capacity Reservations from your Auto Scaling group](target-capacity-reservations.md).

## Use a Capacity Reservation specification
<a name="use-a-capacity-reservation-specification"></a>

Use one of the following methods to configure a Capacity Reservation specification when you create a new Auto Scaling group.

------
#### [ Console ]

**To configure a Capacity Reservation specification on a new group (console)**

1. Follow the steps in [Create an Auto Scaling group using the Amazon EC2 launch wizard](create-asg-ec2-wizard.md), up to step 2.

1. On the **Choose instance launch options** page, under **Additional capacity settings**, choose a Capacity Reservation preference. Optionally, choose a Capacity Reservation target. For more information, see [Capacity Reservation preference](target-capacity-reservations.md#asg-capacity-reservation-preference) and [Capacity Reservation target](target-capacity-reservations.md#capacity-reservation-target).

1. Continue with the remaining steps of the wizard.

------
#### [ AWS CLI ]

Add the `--capacity-reservation-specification` parameter to the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command. The parameter accepts a preference and an optional target. For details, see [Capacity Reservation preference](target-capacity-reservations.md#asg-capacity-reservation-preference) and [Capacity Reservation target](target-capacity-reservations.md#capacity-reservation-target).

The following example creates an Auto Scaling group with a preference of `capacity-reservations-only` and a specific Capacity Reservation as the target.

```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --launch-template LaunchTemplateName={{my-launch-template}} \
    --min-size {{1}} --max-size {{10}} --desired-capacity {{5}} \
    --vpc-zone-identifier "{{subnet-abc1234a}},{{subnet-abc1234b}}" \
    --capacity-reservation-specification '{
        "CapacityReservationPreference": "capacity-reservations-only",
        "CapacityReservationTarget": {
            "CapacityReservationIds": ["{{cr-1234567890abcdef1}}"]
        }
    }'
```

------

### Update an existing Auto Scaling group
<a name="update-an-existing-auto-scaling-group"></a>

To change the Capacity Reservation specification on an existing Auto Scaling group, use one of the following methods.

------
#### [ Console ]

**To change the Capacity Reservation specification on an existing group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. From the navigation bar at the top, choose the AWS Region where your Auto Scaling group is located.

1. Select the check box next to your Auto Scaling group. A split pane opens at the bottom of the page.

1. On the **Details** tab, under **Capacity Reservation preference**, choose **Edit**.

1. Choose a Capacity Reservation preference and, optionally, a Capacity Reservation target.

1. Choose **Update**.

------
#### [ AWS CLI ]

Add the `--capacity-reservation-specification` parameter to the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

The following example updates an Auto Scaling group to use a Capacity Reservation Resource Group as the target with a preference of `capacity-reservations-first`.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --capacity-reservation-specification '{
        "CapacityReservationPreference": "capacity-reservations-first",
        "CapacityReservationTarget": {
            "CapacityReservationResourceGroupArns": ["{{arn:aws:resource-groups:us-east-1:123456789012:group/my-cr-group}}"]
        }
    }'
```

------

## Target Capacity Blocks or interruptible Capacity Reservations from a launch template
<a name="target-capacity-blocks-or-interruptible-capacity-reservations-from-a-launch-template"></a>

You can consume Capacity Blocks or interruptible Capacity Reservations from your Auto Scaling group using launch-template-based targeting. This approach requires setting the market type on your launch template and specifying the Capacity Reservation ID as the target on your Auto Scaling group.

If your Auto Scaling group uses a mixed instances policy, we recommend using distribution segments instead, which lets you configure Capacity Reservations in one place on the Auto Scaling group. Launch-template-based targeting is required if your Auto Scaling group uses a single instance type.

### Configure a launch template
<a name="configure-a-launch-template-for-capacity-reservations"></a>

In your launch template, set the following:
+ Set the instance market type (`InstanceMarketOptions.MarketType`) to `capacity-block` for a Capacity Block, or `interruptible-capacity-reservation` for an interruptible Capacity Reservation.
+ Set the Capacity Reservation target (`CapacityReservationSpecification.CapacityReservationTarget.CapacityReservationId`) to the Capacity Reservation ID.

The following example uses the [create-launch-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template.html) command to create a launch template that targets a Capacity Block. For an interruptible Capacity Reservation, replace the `MarketType` value with `interruptible-capacity-reservation`.

```
aws ec2 create-launch-template \
    --launch-template-name {{my-cr-launch-template}} \
    --launch-template-data '{
        "ImageId": "{{ami-0abcdef1234567890}}",
        "InstanceType": "{{p5.48xlarge}}",
        "InstanceMarketOptions": {
            "MarketType": "capacity-block"
        },
        "CapacityReservationSpecification": {
            "CapacityReservationTarget": {
                "CapacityReservationId": "{{cr-1234567890abcdef1}}"
            }
        }
    }'
```

For information about creating a launch template, see [Launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

### Create an Auto Scaling group
<a name="create-an-auto-scaling-group-for-capacity-reservations"></a>

Create an Auto Scaling group that uses the launch template. The Auto Scaling group must be configured with a subnet in the same Availability Zone as your Capacity Reservation.

The following example creates an Auto Scaling group that uses the launch template created in the previous step.

```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name {{my-cr-asg}} \
    --launch-template LaunchTemplateName={{my-cr-launch-template}} \
    --min-size {{0}} --max-size {{4}} --desired-capacity {{4}} \
    --vpc-zone-identifier "{{subnet-abc1234a}}"
```

For more information, see [Create Auto Scaling groups using launch templates](create-auto-scaling-groups-launch-template.md).

### Operational guidelines
<a name="capacity-reservation-launch-template-operational-guidelines"></a>

Consider the following operational guidelines when using launch template–based targeting.
+ **Launch template version** – Point your Auto Scaling group to a specific launch template version instead of the `$Default` or `$Latest` version. This ensures consistency for the duration of the reservation.
+ **Instance replacement** – When a Capacity Block expires or an interruptible Capacity Reservation is reclaimed, Amazon EC2 terminates the instances running in it. The Auto Scaling health checker detects the termination and attempts to launch a replacement instance in the same manner as for any instance that fails a health check. Scaling activities for these terminations show *taken out of service in response to an Amazon EC2 health check that indicated it had been terminated or stopped*.
+ **For Capacity Blocks** – Scale in your Auto Scaling group to zero more than 30 minutes before the Capacity Block reservation end time. Amazon EC2 begins terminating any remaining instances 30 minutes before the end time. Use scheduled scaling to scale out at the reservation start and scale in before the end. Add lifecycle hooks as needed to gracefully shut down your application before the forced termination window.
+ **For interruptible Capacity Reservations** – Instances can be terminated with a 2-minute notice when the capacity owner reclaims capacity. Design your applications to handle graceful shutdowns. Amazon EC2 sends notifications 2 minutes before termination, and you can set up custom automation to respond to these notifications.

### Override Capacity Reservation settings at the Auto Scaling group level
<a name="override-capacity-reservation-settings-at-the-group-level"></a>

You can set a Capacity Reservation preference and target on your Auto Scaling group to override the settings in your launch template. For more information about the Capacity Reservation specification, see [Target Capacity Reservations from your Auto Scaling group](target-capacity-reservations.md).

### Considerations
<a name="launch-template-targeting-considerations"></a>
+ **Mixed instances policies** – Launch-template-based targeting of Capacity Blocks or interruptible Capacity Reservations is not supported with mixed instances policies. To use these reservation types with a mixed instances policy, see [Use Distribution Segments to target multiple Capacity Reservation types](use-distribution-segments.md).
+ **Warm pools** – Warm pools are not supported when your launch template targets a Capacity Block or an interruptible Capacity Reservation.
+ **One Capacity Reservation type per launch template** – A launch template can target only one Capacity Reservation type. To target multiple Capacity Reservation types in one Auto Scaling group, use distribution segments.
