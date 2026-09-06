---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-distribution-segments.html
---

# Use Distribution Segments to target multiple Capacity Reservation types
<a name="use-distribution-segments"></a>

Use distribution segments to configure your Auto Scaling group to consume multiple Capacity Reservation types – On-Demand Capacity Reservations, Capacity Blocks for ML, and interruptible Capacity Reservations – with priority ordering. You target these reservation types by pointing your Auto Scaling group at a Capacity Reservation Resource Group that contains a mix of different Capacity Reservations.

When you configure distribution segments, Auto Scaling launches instances across the reservation types in the priority order you specify, with optional fallback to On-Demand capacity.

## How Auto Scaling distributes instances across market options
<a name="how-auto-scaling-distributes-instances-across-market-options"></a>

Auto Scaling distributes launched instances across different market options based on your mixed instances policy configuration.

### On-Demand and Spot distribution
<a name="on-demand-and-spot-distribution"></a>

You can distribute instances between On-Demand and Spot capacity using the `OnDemandBaseCapacity` and `OnDemandPercentageAboveBaseCapacity` fields on your mixed instances policy. The following example launches the first 2 instances as On-Demand, then 25 percent of the remaining instances as On-Demand and the remaining as Spot:

```
{
    "InstancesDistribution": {
        "OnDemandBaseCapacity": {{2}},
        "OnDemandPercentageAboveBaseCapacity": {{25}}
    }
}
```

### Distribution with distribution segments
<a name="distribution-with-distribution-segments"></a>

A distribution segment is a configuration on your Auto Scaling group that contains a list of capacity types to prioritize in order. distribution segments are set on the `DistributionSegments` field of your mixed instances policy.

Auto Scaling currently supports only one distribution segment per Auto Scaling group. All Auto Scaling group capacity is distributed across the target capacity types (`TargetCapacityTypes`) in that segment.

The valid values for `TargetCapacityTypes` are:
+ `on-demand-capacity-reservation` – On-Demand Capacity Reservations
+ `capacity-block` – Capacity Blocks for ML
+ `interruptible-capacity-reservation` – interruptible Capacity Reservations
+ `on-demand` – On-Demand capacity

The order of the list determines how Auto Scaling distributes launched instances. Auto Scaling attempts to consume capacity in the order in which the types are listed. When a particular capacity type is unavailable, Auto Scaling skips that type and moves on to the next one.

The following example launches instances as On-Demand Capacity Reservation-backed first, then as Capacity Block-backed, then as interruptible Capacity Reservation-backed, and finally as On-Demand if reserved capacity is insufficient:

```
{
    "InstancesDistribution": {
        "DistributionSegments": [
            {
                "TargetCapacityTypes": [
                    "on-demand-capacity-reservation",
                    "capacity-block",
                    "interruptible-capacity-reservation",
                    "on-demand"
                ]
            }
        ]
    }
}
```

If you include `on-demand` in the list, Auto Scaling falls back to On-Demand capacity when reserved capacity is unavailable. If you omit `on-demand`, instances fail to launch when reserved capacity is unavailable. If you include `on-demand`, it must be the last entry in the list.

**Note**
Spot capacity is not supported as a target capacity type at this time.

## Prerequisites
<a name="distribution-segments-prerequisites"></a>

Before you can configure distribution segments on your Auto Scaling group, you must create the Capacity Reservations that you want to consume and the Capacity Reservation Resource Group that contains them.

To create a Capacity Reservation, see one of the following in the *Amazon EC2 User Guide*:
+ [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html) – for On-Demand Capacity Reservations
+ [Find and purchase Capacity Blocks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-purchase.html) – for Capacity Blocks
+ [Interruptible Capacity Reservations for capacity owners](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html#capacity-owner-considerations) – for interruptible Capacity Reservations

To create a Capacity Reservation Resource Group that contains a mix of different Capacity Reservations, see [Capacity Reservation Resource Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cr-group.html) in the *Amazon EC2 User Guide*.

## Configure your Auto Scaling group to use distribution segments
<a name="configure-distribution-segments"></a>

To configure your Auto Scaling group to use distribution segments, add them to your mixed instances policy and set the Capacity Reservation Resource Group ARN as the target on your Capacity Reservation specification.

Auto Scaling attempts to launch instances in the priority order of the capacity types, and within each capacity type, in the order of instance types listed in your launch template `Overrides`.

------
#### [ Console ]

**To configure distribution segments on a new group (console)**

1. Follow the steps in [Create an Auto Scaling group using the Amazon EC2 launch wizard](create-asg-ec2-wizard.md), up to step 2.

1. On the **Choose instance launch options** page, under **Instance type requirements**, choose **Override launch template**, and then choose **Override launch template for distribution segments**.

1. Under **Instance distribution options**, choose **Distribution segments**.

1. For **Select target Capacity Reservation type**, select the Capacity Reservation types to include in this distribution segment. Make sure that your Capacity Reservation Resource Group contains the reservation types that you select.

1. Under **Order target Capacity Reservation types**, drag the types into the priority order that you want. Auto Scaling launches instances into Capacity Reservations in this order. If you selected **On-Demand instances**, it must be last.

1. Under **Additional capacity settings**, for **Capacity Reservation target**, choose **Specify Capacity Reservation Resource Group (Target by ARN)**, and then choose the ARN of your Capacity Reservation Resource Group.

1. Continue with the remaining steps of the wizard.

------
#### [ AWS CLI ]

Use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to create a new Auto Scaling group with distribution segments.

The following example uses a priority order of On-Demand Capacity Reservations first, then Capacity Blocks, then interruptible Capacity Reservations, then On-Demand.

```
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --min-size {{0}} --max-size {{10}} --desired-capacity {{5}} \
    --vpc-zone-identifier "{{subnet-abc1234a}}" \
    --mixed-instances-policy '{
        "LaunchTemplate": {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{my-launch-template}}"
            },
            "Overrides": [
                {"InstanceType": "{{m5.24xlarge}}"},
                {"InstanceType": "{{p5.48xlarge}}"}
            ]
        },
        "InstancesDistribution": {
            "OnDemandAllocationStrategy": "prioritized",
            "DistributionSegments": [
                {
                    "TargetCapacityTypes": [
                        "on-demand-capacity-reservation",
                        "capacity-block",
                        "interruptible-capacity-reservation",
                        "on-demand"
                    ]
                }
            ]
        }
    }' \
    --capacity-reservation-specification '{
        "CapacityReservationTarget": {
            "CapacityReservationResourceGroupArns": [
                "{{arn:aws:resource-groups:us-east-1:123456789012:group/my-crg}}"
            ]
        }
    }'
```

------

## Migrate to and from distribution segments
<a name="migrate-distribution-segments"></a>

You can migrate an existing Auto Scaling group to use distribution segments, and migrate back to a standard configuration when needed. In all migration scenarios, existing instances continue running. New launches follow the updated configuration.

### Migrate a mixed instances group to use distribution segments
<a name="migrate-to-distribution-segments"></a>

To migrate an existing mixed instances group to use distribution segments, use one of the following methods. Auto Scaling automatically clears `OnDemandBaseCapacity` and `OnDemandPercentageAboveBaseCapacity` when you add distribution segments.

------
#### [ Console ]

**To migrate an existing group to distribution segments (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. From the navigation bar at the top, choose the AWS Region where your Auto Scaling group is located.

1. Choose the name of your Auto Scaling group to open its details page.

1. In the **Instance type requirements** section, choose **Edit**.

1. Under **Instance type requirements**, choose **Override launch template**, and then choose **Override launch template for distribution segments**.

1. Under **Instance distribution options**, choose **Distribution segments**.

1. For **Select target Capacity Reservation type**, select the Capacity Reservation types to include in this distribution segment. Make sure that your Capacity Reservation Resource Group contains the reservation types that you select.

1. Under **Order target Capacity Reservation types**, drag the types into the priority order that you want. If you selected **On-Demand instances**, it must be last.

1. Choose **Update**.

To set the Capacity Reservation Resource Group as the target for an existing group, see [Update an existing Auto Scaling group](capacity-reservation-create-asg-procedure.md#update-an-existing-auto-scaling-group).

------
#### [ AWS CLI ]

Use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command to add distribution segments to your mixed instances policy and set the Capacity Reservation Resource Group ARN as the target.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --mixed-instances-policy '{
        "InstancesDistribution": {
            "DistributionSegments": [
                {
                    "TargetCapacityTypes": [
                        "on-demand-capacity-reservation",
                        "capacity-block",
                        "interruptible-capacity-reservation",
                        "on-demand"
                    ]
                }
            ]
        }
    }' \
    --capacity-reservation-specification '{
        "CapacityReservationPreference": "default",
        "CapacityReservationTarget": {
            "CapacityReservationResourceGroupArns": [
                "{{arn:aws:resource-groups:us-east-1:123456789012:group/my-crg}}"
            ]
        }
    }'
```

------

### Migrate away from distribution segments
<a name="migrate-away-from-distribution-segments"></a>

To migrate back to a standard mixed instances group, use one of the following methods.

------
#### [ Console ]

**To remove distribution segments from a group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. From the navigation bar at the top, choose the AWS Region where your Auto Scaling group is located.

1. Choose the name of your Auto Scaling group to open its details page.

1. In the **Instance type requirements** section, choose **Edit**.

1. Under **Instance type requirements**, choose **Reset to launch template**. This removes the launch template overrides, which clears the mixed instances policy and the distribution segments along with it.

1. Choose **Update**.

------
#### [ AWS CLI ]

Use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command to set `OnDemandBaseCapacity` or `OnDemandPercentageAboveBaseCapacity`. Auto Scaling automatically clears distribution segments when you set the legacy fields.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --mixed-instances-policy '{
        "InstancesDistribution": {
            "OnDemandBaseCapacity": {{2}},
            "OnDemandPercentageAboveBaseCapacity": {{25}}
        }
    }' \
    --capacity-reservation-specification '{
        "CapacityReservationPreference": "capacity-reservations-first"
    }'
```

Alternatively, you can clear distribution segments explicitly by setting `DistributionSegments` to an empty list.

If you want to switch to using a launch template on your Auto Scaling group without a mixed instances policy, use the `update-auto-scaling-group` command with a top-level launch template. Auto Scaling clears the mixed instances policy when you provide a top-level launch template.

```
aws autoscaling update-auto-scaling-group \
    --auto-scaling-group-name {{my-asg}} \
    --launch-template LaunchTemplateName={{my-launch-template}} \
    --capacity-reservation-specification '{
        "CapacityReservationPreference": "capacity-reservations-first"
    }'
```

------

**Note**
You can also migrate to and from distribution segments using an instance refresh with the `--desired-configuration` parameter.

## Scale-in behavior with distribution segments
<a name="scale-in-distribution-segments"></a>

When your Auto Scaling group scales in, Auto Scaling terminates instances in the opposite order of your `TargetCapacityTypes`. On-Demand instances are terminated first, followed by instances of the lowest-priority capacity type, and so on up to the highest-priority capacity type.

For example, with `TargetCapacityTypes` set to `["on-demand-capacity-reservation", "capacity-block", "interruptible-capacity-reservation", "on-demand"]`, Auto Scaling terminates instances in the following order during scale in:

1. On-Demand

1. interruptible Capacity Reservation-backed

1. Capacity Block-backed

1. On-Demand Capacity Reservation-backed

If you update your distribution segments to remove a reservation type, existing instances of that removed type are terminated before any instance whose type is still in the list.

## Considerations
<a name="distribution-segments-considerations"></a>
+ **Capacity Reservation preference** – Only `default` is supported when configuring distribution segments. For more information, see [Capacity Reservation preference](target-capacity-reservations.md#asg-capacity-reservation-preference).
+ **On-Demand allocation strategy** – Only `prioritized` is supported when you configure distribution segments.
+ **Warm pools** – Warm pools are not supported with distribution segments.
+ **Spot capacity** – Spot capacity is not supported as a target capacity type in distribution segments.
