---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-interruptible-capacity-reservations.html
---

# Interruptible Capacity Reservations with EC2 Auto Scaling
<a name="asg-interruptible-capacity-reservations"></a>

Interruptible Capacity Reservations represent spare capacity lent to you by On-Demand Capacity Reservation owners within your AWS organization. These reservations are suitable for interruptible workloads because the capacity owner can reclaim the capacity at any time with a 2-minute interruption notice, after which the instances are terminated. For an overview of Interruptible Capacity Reservations and how they work, see [ Interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html) in the *Amazon EC2 User Guide*.

To get started, you create an interruptible reservation by allocating unused capacity from any On-Demand Capacity Reservation within your account. Next, you create your launch template, specify the interruptible capacity reservation ID and the appropriate market type. Finally, create your Auto Scaling group to use the launch template you created.

**Note**
Mixed instances groups are not supported with interruptible capacity reservations.
The interruptible Capacity Reservations appear in your account with a new attribute `interruptible` set to `true`.

**Topics**
+ [Operational guidelines](#operational-guidelines)
+ [Specify an Interruptible Capacity Reservation in your launch template](#specify-interruptible-cr)
+ [Limitations](#limitations)
+ [Related resources](#related-resources)

## Operational guidelines
<a name="operational-guidelines"></a>

The following are basic operational guidelines that you should follow when using Interruptible Capacity Reservations with an Auto Scaling group.
+ Instances launched from interruptible capacity reservations can be terminated with a 2-minute notice when the capacity is reclaimed. Design your applications to handle graceful shutdowns.
+ Amazon EC2 sends EventBridge notifications 2 minutes before terminating instances. While Auto Scaling doesn't automatically react to these events, you can set up custom automation to respond to interruption notices.
+ When instances are terminated due to capacity reclamation, Auto Scaling's health checker will detect the termination and automatically launch replacement instances according to your group's configuration.
+ Point to a specific version of the launch template instead of the `$Default` or `$Latest` version to ensure consistency.

**Note**
When an interruptible capacity reservation instance is reclaimed, the scaling activities for your Auto Scaling group will state: `taken out of service in response to an Amazon EC2 health check that indicated it had been terminated or stopped`. Auto Scaling will attempt to replace the instance in the same manner as it does for any instance that fails a health check.

## Specify an Interruptible Capacity Reservation in your launch template
<a name="specify-interruptible-cr"></a>

To create a launch template that targets a specific Interruptible Capacity Reservation for your Auto Scaling group, use one of the following methods:

------
#### [ Console ]

**To specify an Interruptible Capacity Reservation in your launch template (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the top navigation bar, select the AWS Region where you have your interruptible capacity reservation.

1. On the navigation pane, under **Instances**, choose **Launch Templates**.

1. Choose **Create launch template**, and create the launch template. Include the ID of the AMI, the instance type, and any other launch template settings as needed.

1. Expand the **Advanced details** section to view the advanced settings.

1. For **Purchasing option**, choose **Interruptible Capacity Reservation**.

1. For **Capacity Reservation**, choose **Target by ID**, and then for **Capacity Reservation - Target by ID**, choose the capacity reservation ID of an existing interruptible capacity reservation.

1. When you have finished, choose **Create launch template**.

For help creating an Auto Scaling group with a launch template, see [Create an Auto Scaling group using a launch template](create-asg-launch-template.md).

------
#### [ AWS CLI ]

**To specify an Interruptible Capacity Reservation in your launch template (AWS CLI)**
Use the following [create-launch-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template.html) command to create a launch template that specifies an existing interruptible capacity reservation ID. Replace each user input placeholder with your own information.

```
aws ec2 create-launch-template --launch-template-name {{my-template-for-interruptible-cr}} \
  --version-description {{AutoScalingVersion1}} --region {{us-east-2}} \
  --launch-template-data {{file://config.json}}
```

**Tip**
If this command throws an error, make sure that you have updated the AWS CLI locally to the latest version.

Contents of `config.json`:

```
{
    "ImageId": "ami-04d5cc9b88example",
    "InstanceType": "t3.nano",
    "SecurityGroupIds": [
        "sg-903004f88example"
    ],
    "KeyName": "MyKeyPair",
    "InstanceMarketOptions": {
        "MarketType": "interruptible-capacity-reservation"
    },
    "CapacityReservationSpecification": {
        "CapacityReservationTarget": {
            "CapacityReservationId": "cr-02168da1478b509e0"
        }
    }
}
```

The following is example output:

```
{
    "LaunchTemplate": {
        "LaunchTemplateId": "lt-068f72b724example",
        "LaunchTemplateName": "my-template-for-interruptible-cr",
        "CreateTime": "2023-10-27T15:12:44.000Z",
        "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
        "DefaultVersionNumber": 1,
        "LatestVersionNumber": 1
    }
}
```

You can use the following [describe-launch-template-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-template-versions.html) command to verify the interruptible capacity reservation ID associated with the launch template:

```
aws ec2 describe-launch-template-versions --launch-template-names {{my-template-for-interruptible-cr}} \
  --region {{us-east-2}}
```

------

**Auto Scaling group level configuration**
You can optionally specify capacity reservation settings at the Auto Scaling group level to override the launch template settings:
+ **Capacity Reservation preference**: Only `capacity-reservations-only` is supported for interruptible capacity reservations. The `capacity-reservations-first` preference is not supported.
+ **Target specification**: You can specify a different interruptible capacity reservation ID at the group level to override the launch template setting.

## Limitations
<a name="limitations"></a>
+ Mixed instances policies are not supported with interruptible capacity reservations.
+ You must specify the correct market type (`interruptible-capacity-reservation`) in your launch template along with the capacity reservation ID.

## Related resources
<a name="related-resources"></a>
+ For information about creating and managing interruptible capacity reservations, see [Interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html) in the *Amazon EC2 User Guide*.
+ For general information about using capacity reservations with Auto Scaling, see [Reserve capacity in specific Availability Zones with Capacity Reservations](use-ec2-capacity-reservations.md).
+ For information about Auto Scaling group health checks, see [Health checks for instances in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html).
