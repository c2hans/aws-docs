---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-capacity-blocks.html
---

# Use Capacity Blocks for machine learning workloads
<a name="launch-template-capacity-blocks"></a>

Capacity Blocks help you reserve highly sought-after GPU instances on a future date to support your short-duration, machine learning (ML) workloads.

For an overview of Capacity Blocks and how they work, see [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) in the *Amazon EC2 User Guide*.

To start using Capacity Blocks, you create a capacity reservation in a specific Availability Zone. Capacity Blocks are delivered as `targeted` capacity reservations in a single Availability Zone. When you create your launch template, specify the Capacity Block's reservation ID and instance type. Then, update your Auto Scaling group to use the launch template you created and the Capacity Block's Availability Zone. When your Capacity Block reservation begins, use scheduled scaling to launch the same number of instances as your Capacity Block reservation.

**Important**
Capacity Blocks are only available for certain Amazon EC2 instance types and AWS Regions. For more information, see [Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-using.html#capacity-blocks-prerequisites) in the *Amazon EC2 User Guide*.

**Topics**
+ [Operational guidelines](#capacity-blocks-operational-guidelines)
+ [Specify a Capacity Block in your launch template](#specify-a-capacity-block-in-your-launch-template)
+ [Limitations](#capacity-blocks-limitations)
+ [Related resources](#capacity-blocks-related-resources)

## Operational guidelines
<a name="capacity-blocks-operational-guidelines"></a>

The following are basic operational guidelines that you should follow when using a Capacity Block with an Auto Scaling group.
+ Scale in your Auto Scaling group to zero more than 30 minutes before the Capacity Block reservation end time. Amazon EC2 will terminate any instances that are still running 30 minutes before the end time of the Capacity Block.
+ We recommend that you use scheduled scaling to scale out (add instances) and scale in (remove instances) at the appropriate reservation times. For more information, see [Scheduled scaling for Amazon EC2 Auto Scaling](ec2-auto-scaling-scheduled-scaling.md).
+ Add lifecycle hooks as needed to perform a graceful shutdown of your application inside the instances when scaling in. Leave enough time for the lifecycle action to complete *before* Amazon EC2 starts forcibly terminating your instances 30 minutes before the Capacity Block reservation end time. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](lifecycle-hooks.md).
+ Make sure that the Auto Scaling group points to the correct version of the launch template for the entire duration of the reservation. We recommend pointing to a specific version of the launch template instead of the `$Default` or `$Latest` version.

**Note**
If you leave a Capacity Block instance running until the end of the reservation and Amazon EC2 reclaims it, the scaling activities for your Auto Scaling group state that it was "`taken out of service in response to an EC2 health check that indicated it had been terminated or stopped`", even though it was purposely reclaimed at the end of the Capacity Block. Similarly, Amazon EC2 Auto Scaling will attempt to replace the instance in the same manner as it does for any instance that fails a health check. For more information, see [Health checks for instances in an Auto Scaling group](ec2-auto-scaling-health-checks.md).

## Specify a Capacity Block in your launch template
<a name="specify-a-capacity-block-in-your-launch-template"></a>

To create a launch template that targets a specific Capacity Block for your Auto Scaling group, use one of the following methods:

------
#### [ Console ]

**To specify a Capacity Block in your launch template (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the top navigation bar, select the AWS Region where you created your Capacity Block.

1. On the navigation pane, under **Instances**, choose **Launch Templates**.

1. Choose **Create launch template**, and create the launch template. Include the ID of the Amazon Machine Image (AMI), the instance type, and any other launch template settings as needed.

1. Expand the **Advanced details** section to view the advanced settings.

1. For **Purchasing option**, choose **Capacity Blocks**.

1. For **Capacity reservation**, choose **Target by ID**, and then for **Capacity reservation - Target by ID**, choose the capacity reservation ID of an existing Capacity Block.

1. When you have finished, choose **Create launch template**.

   For help creating an Auto Scaling group with a launch template, see [Create an Auto Scaling group using a launch template](create-asg-launch-template.md).

------
#### [ AWS CLI ]

**To specify a Capacity Block in your launch template (AWS CLI)**
Use the following [create-launch-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template.html) command to create a launch template that specifies an existing Capacity Block reservation ID. Replace each {{user input placeholder}} with your own information.

```
aws ec2 create-launch-template --launch-template-name {{my-template-for-capacity-block}}  \
  --version-description {{AutoScalingVersion1}} --region {{us-east-2}} \
  --launch-template-data file://config.json
```

**Tip**
If this command throws an error, make sure that you have updated the AWS CLI locally to the latest version.

Contents of `config.json`.

```
{
    "ImageId": "{{ami-04d5cc9b88example}}",
    "InstanceType": "{{p4d.24xlarge}}",
    "SecurityGroupIds": [
        "{{sg-903004f88example}}"
    ],
    "KeyName": "{{MyKeyPair}}",
    "InstanceMarketOptions": {
        "MarketType": "capacity-block"
    },
    "CapacityReservationSpecification": {
        "CapacityReservationTarget": {
            "CapacityReservationId": "{{cr-02168da1478b509e0}}"
        }
    }
}
```

The following is example output.

```
{
    "LaunchTemplate": {
        "LaunchTemplateId": "lt-068f72b724example",
        "LaunchTemplateName": "my-template-for-capacity-block",
        "CreateTime": "2023-10-27T15:12:44.000Z",
        "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
        "DefaultVersionNumber": 1,
        "LatestVersionNumber": 1
    }
}
```

You can use the following [describe-launch-template-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-template-versions.html) command to verify the Capacity Block reservation ID associated with the launch template.

```
aws ec2 describe-launch-template-versions --launch-template-names {{my-template-for-capacity-block}} \
  --region us-east-2
```

The following is example output for a launch template that specifies a Capacity Block reservation.

```
{
    "LaunchTemplateVersions": [
        {
            "LaunchTemplateId": "lt-068f72b724example",
            "LaunchTemplateName": "my-template-for-capacity-block",
            "VersionNumber": 1,
            "CreateTime": "2023-10-27T15:12:44.000Z",
            "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
            "DefaultVersion": true,
            "LaunchTemplateData": {
                "ImageId": "ami-04d5cc9b88example",
                "InstanceType": "p5.48xlarge",
                "SecurityGroupIds": [
                    "sg-903004f88example"
                ],
                "KeyName": "MyKeyPair",
                "InstanceMarketOptions": {
                    "MarketType": "capacity-block"
                },
                "CapacityReservationSpecification": {
                    "CapacityReservationTarget": {
                        "CapacityReservationId": "cr-02168da1478b509e0"
                    }
                }
            }
        }
    ]
}
```

------

## Limitations
<a name="capacity-blocks-limitations"></a>
+ Support for Capacity Blocks is only available if your Auto Scaling group has a compatible configuration. Mixed instances groups and warm pools are not supported.
+ You can only target one Capacity Block at a time.

## Related resources
<a name="capacity-blocks-related-resources"></a>
+ For the prerequisites and recommendations for using P5 Instances, see [Get started with P5 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/p5-instances-started.html) in the *Amazon EC2 User Guide*.
+ Amazon EKS supports using Capacity Blocks to support your short duration, machine learning (ML) workloads on Amazon EKS clusters. For more information, see [Capacity Blocks for ML](https://docs.aws.amazon.com/eks/latest/userguide/capacity-blocks.html) in the **Amazon EKS User Guide**.
+ You can use Capacity Blocks with supported instance types and Regions. However, On-Demand Capacity Reservations provide flexibility to reserve capacity for other instances types and Regions. For a tutorial that shows you how to use the On-Demand Capacity Reservation option, see [Reserve capacity in specific Availability Zones with Capacity Reservations](use-ec2-capacity-reservations.md).
