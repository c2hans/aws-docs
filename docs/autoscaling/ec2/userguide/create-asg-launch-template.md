---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html
---

# Create an Auto Scaling group using a launch template
<a name="create-asg-launch-template"></a>

When you create an Auto Scaling group, you must specify the necessary information to configure the Amazon EC2 instances, the Availability Zones and VPC subnets for the instances, the desired capacity, and the minimum and maximum capacity limits.

To configure Amazon EC2 instances that are launched by your Auto Scaling group, you can specify a launch template or a launch configuration. The following procedure demonstrates how to create an Auto Scaling group using a launch template.

**Prerequisites**
+ You must have created a launch template. For more information, see [Create a launch template for an Auto Scaling group](create-launch-template.md).

**To create an Auto Scaling group using a launch template (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the same AWS Region that you used when you created the launch template.

1. Choose **Create an Auto Scaling group**.

1. On the **Choose launch template or configuration** page, do the following:

   1. For **Auto Scaling group name**, enter a name for your Auto Scaling group.

   1. For **Launch template**, choose an existing launch template.

   1. For **Launch template version**, choose whether the Auto Scaling group uses the default, the latest, or a specific version of the launch template when scaling out.

   1. Verify that your launch template supports all of the options that you are planning to use, and then choose **Next**.

1. On the **Choose instance launch options** page, if you're not using multiple instance types, you can skip the **Instance type requirements** section to use the EC2 instance type that is specified in the launch template.

   To use multiple instance types, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).

1. Under **Network**, for **VPC**, choose a VPC. The Auto Scaling group must be created in the same VPC as the security group you specified in your launch template.

1. For **Availability Zones and subnets**, choose one or more subnets in the specified VPC. Use subnets in multiple Availability Zones for high availability. For more information, see [Considerations when choosing VPC subnets](asg-in-vpc.md#as-vpc-considerations).

1. For **Availability Zone distribution**, select a distribution strategy. For more information, see [Auto Scaling group Availability Zone distribution](ec2-auto-scaling-availability-zone-balanced.md).

1. If you created a launch template with an instance type specified, then you can continue to the next step to create an Auto Scaling group that uses the instance type in the launch template.

   Alternatively, you can choose the **Override launch template** option if no instance type is specified in your launch template or if you want to use multiple instance types for auto scaling. For more information, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).

1. Choose **Next** to continue to the next step.

   Or, you can accept the rest of the defaults, and choose **Skip to review**.

1. (Optional) On the **Integrate with other services** page, configure the following options, and then choose **Next**:

   1. For **Load balancing**, choose whether to attach your Auto Scaling group to a load balancer. For more information, see [Elastic Load Balancing](autoscaling-load-balancer.md).

   1. For **VPC Lattice integration options**, choose whether to use VPC Lattice. For more information, see [Manage traffic flow with a VPC Lattice target group](ec2-auto-scaling-vpc-lattice.md).

   1. For **Amazon Application Recovery Controller (ARC) zonal shift**, select the checkbox to enable zonal shift. For more information, see [Auto Scaling group zonal shift](ec2-auto-scaling-zonal-shift.md).

      1. If you enable zonal shift, for **Health check behavior**, select Ignore unhealthy or Replace unhealthy. For more information, see [How zonal shift works for Auto Scaling groups](ec2-auto-scaling-zonal-shift.md#asg-zonal-shift-how-it-works).

   1. Under **Health checks**, for **Additional health check types**, select **Turn on Amazon EBS health checks**. For more information, see [Monitor Auto Scaling instances with impaired Amazon EBS volumes using health checks](monitor-and-replace-instances-with-impaired-ebs-volumes.md).

   1. For **Health check grace period**, enter the amount of time, in seconds. This amount of time is how long Amazon EC2 Auto Scaling needs to wait before checking the health status of an instance after it enters the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

1. (Optional) On the **Configure group size and scaling** page, configure the following options, and then choose **Next**:

   1. Under **Group size**, for **Desired capacity**, enter the initial number of instances to launch.

   1. Under **Scaling**, **Scaling limits**, if your new value for **Desired capacity** is greater than **Min desired capacity** and **Max desired capacity**, the **Max desired capacity** is automatically increased to the new desired capacity value. You can change these limits as needed. For more information, see [Set scaling limits for your Auto Scaling group](asg-capacity-limits.md).

   1. For **Automatic scaling**, choose whether you want to create a target tracking scaling policy. You can also create this policy after your create your Auto Scaling group.

      If you choose **Target tracking scaling policy**, follow the directions in [Create a target tracking scaling policy](policy_creating.md) to create the policy.

   1. Under **Instance maintenance policy**, choose whether you want to create an instance maintenance policy. You can also create this policy after your create your Auto Scaling group. Follow the directions in [Set an instance maintenance policy](set-instance-maintenance-policy.md) to create the policy.

   1. Under **Additional capacity settings**, **Capacity Reservation preference**, choose whether you want to use a Capacity Reservation preference. For more information, see [Use Capacity Reservations in your Auto Scaling group](use-ec2-capacity-reservations.md).

   1. Under **Additional settings**, **Instance scale-in protection**, choose whether to enable instance scale-in protection. For more information, see [Use instance scale-in protection to control instance termination](ec2-auto-scaling-instance-protection.md).

   1. For **Monitoring**, choose whether to enable CloudWatch group metrics collection. These metrics provide measurements that can be indicators of a potential issue, such as number of terminating instances or number of pending instances. For more information, see [Monitor CloudWatch metrics for your Auto Scaling groups and instances](ec2-auto-scaling-cloudwatch-monitoring.md).

   1. For **default instance warmup**, select this option and choose the warmup time for your application. If you are creating an Auto Scaling group that has a scaling policy, the default instance warmup feature improves the Amazon CloudWatch metrics used for dynamic scaling. For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

1. (Optional) On the **Add notifications** page, configure the notification, and then choose **Next**. For more information, see [Amazon SNS notification options for Amazon EC2 Auto Scaling](ec2-auto-scaling-sns-notifications.md).

1. (Optional) On the **Add tags** page, choose **Add tag**, provide a tag key and value for each tag, and then choose **Next**. For more information, see [Tag Auto Scaling groups and instances](ec2-auto-scaling-tagging.md).

1. On the **Review** page, choose **Create Auto Scaling group**.

**To create an Auto Scaling group using the command line**

You can use one of the following commands:
+ [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) (AWS CLI)
+ [New-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)
