---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-configuration.html
---

# Create an Auto Scaling group using a launch configuration
<a name="create-asg-launch-configuration"></a>

**Important**
We provide information about launch configurations for customers who have not yet migrated from launch configurations to launch templates. For information about migrating your Auto Scaling groups to launch templates, see [Migrate your Auto Scaling groups to launch templates](migrate-to-launch-templates.md).

When you create an Auto Scaling group, you must specify the necessary information to configure the Amazon EC2 instances, the Availability Zones and VPC subnets for the instances, the desired capacity, and the minimum and maximum capacity limits.

The following procedure demonstrates how to create an Auto Scaling group using a launch configuration. You cannot modify a launch configuration after it is created, but you can replace the launch configuration for an Auto Scaling group. For more information, see [Change the launch configuration for an Auto Scaling group](change-launch-config.md).

**Prerequisites**
+ You must have created a launch configuration. For more information, see [Create a launch configuration](create-launch-config.md).

**To create an Auto Scaling group using a launch configuration (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the same AWS Region that you used when you created the launch configuration.

1. Choose **Create an Auto Scaling group**.

1. On the **Choose launch template or configuration** page, for **Auto Scaling group name**, enter a name for your Auto Scaling group.

1. To choose a launch configuration, do the following:

   1. For **Launch template**, choose **Switch to launch configuration**.

   1. For **Launch configuration**, choose an existing launch configuration.

   1. Verify that your launch configuration supports all of the options that you are planning to use, and then choose **Next**.

1. On the **Configure instance launch options** page, under **Network**, for **VPC**, choose a VPC. The Auto Scaling group must be created in the same VPC as the security group you specified in your launch configuration.

1. For **Availability Zones and subnets**, choose one or more subnets in the specified VPC. Use subnets in multiple Availability Zones for high availability. For more information, see [Considerations when choosing VPC subnets](asg-in-vpc.md#as-vpc-considerations).

1. Choose **Next**.

   Or, you can accept the rest of the defaults, and choose **Skip to review**.

1. (Optional) On the **Configure advanced options** page, configure the following options, and then choose **Next**:

   1. (Optional) For **Health checks**, **Additional health check types**, select **Turn on Amazon EBS health checks**. For more information, see [Monitor Auto Scaling instances with impaired Amazon EBS volumes using health checks](monitor-and-replace-instances-with-impaired-ebs-volumes.md).

   1. (Optional) For **Health check grace period**, enter the amount of time, in seconds. This amount of time is how long Amazon EC2 Auto Scaling needs to wait before checking the health status of an instance after it enters the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

   1. Under **Additional settings**, **Monitoring**, choose whether to enable CloudWatch group metrics collection. These metrics provide measurements that can be indicators of a potential issue, such as number of terminating instances or number of pending instances. For more information, see [Monitor CloudWatch metrics for your Auto Scaling groups and instances](ec2-auto-scaling-cloudwatch-monitoring.md).

   1. For **Enable default instance warmup**, select this option and choose the warmup time for your application. If you are creating an Auto Scaling group that has a scaling policy, the default instance warmup feature improves the Amazon CloudWatch metrics used for dynamic scaling. For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

1. (Optional) On the **Configure group size and scaling policies** page, configure the following options, and then choose **Next**:

   1. Under **Group size**, for **Desired capacity**, enter the initial number of instances to launch.

   1. In the **Scaling** section, under **Scaling limits**, if your new value for **Desired capacity** is greater than **Min desired capacity** and **Max desired capacity**, the **Max desired capacity** is automatically increased to the new desired capacity value. You can change these limits as needed. For more information, see [Set scaling limits for your Auto Scaling group](asg-capacity-limits.md).

   1. For **Automatic scaling**, choose whether you want to create a target tracking scaling policy. You can also create this policy after your create your Auto Scaling group.

      If you choose **Target tracking scaling policy**, follow the directions in [Create a target tracking scaling policy](policy_creating.md) to create the policy.

   1. For **Instance maintenance policy**, choose whether you want to create an instance maintenance policy. You can also create this policy after your create your Auto Scaling group. Follow the directions in [Set an instance maintenance policy](set-instance-maintenance-policy.md) to create the policy.

   1. Under **Instance scale-in protection**, choose whether to enable instance scale-in protection. For more information, see [Use instance scale-in protection to control instance termination](ec2-auto-scaling-instance-protection.md).

1. (Optional) To receive notifications, for **Add notification**, configure the notification, and then choose **Next**. For more information, see [Amazon SNS notification options for Amazon EC2 Auto Scaling](ec2-auto-scaling-sns-notifications.md).

1. (Optional) To add tags, choose **Add tag**, provide a tag key and value for each tag, and then choose **Next**. For more information, see [Tag Auto Scaling groups and instances](ec2-auto-scaling-tagging.md).

1. On the **Review** page, choose **Create Auto Scaling group**.

**To create an Auto Scaling group using the command line**

You can use one of the following commands:
+ [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) (AWS CLI)
+ [New-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)
