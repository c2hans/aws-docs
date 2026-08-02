---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/update-auto-scaling-group.html
---

# Update an Auto Scaling group
<a name="update-auto-scaling-group"></a>

You can update most of your Auto Scaling group's details. You can't update the name of an Auto Scaling group or change its AWS Region.

**To update an Auto Scaling group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Choose your Auto Scaling group to display information about the group, with tabs for **Details**, **Activity**, **Automatic scaling**, **Instance management**, **Monitoring**, and **Instance refresh**.

1. Choose the tabs for the configuration areas that you're interested in and update the settings as needed. For each setting that you edit, choose **Update** to save your changes to the Auto Scaling group's configuration.
   + **Details** tab

     These are the general settings for your Auto Scaling group. You can edit and manage these in the same way as during Auto Scaling group creation.

     The **Advanced configurations** section has some options that are not available when creating the group such as [termination policies](ec2-auto-scaling-termination-policies.md), [cooldown](ec2-auto-scaling-scaling-cooldowns.md), [suspended processes](as-suspend-resume-processes.md), and [maximum instance lifetime](asg-max-instance-lifetime.md). You can also view, but not edit the placement group and [service-linked role](autoscaling-service-linked-role.md) of the Auto Scaling group.
   + **Integrations** tab
     + **Load balancing** – [Elastic Load Balancing ](autoscaling-load-balancer.md)

       If the group is associated with Elastic Load Balancing resources, see [Add an Availability ZoneRemove an Availability Zone](as-add-az-console.md) before changing Availability Zones. Some restrictions on the load balancer might prevent you from applying changes to your group's Availability Zones to your load balancer's Availability Zones.
     + **VPC Lattice integration options** – [VPC Lattice](ec2-auto-scaling-vpc-lattice.md)
     + **ARC zonal shift** – [Auto Scaling group zonal shift](ec2-auto-scaling-zonal-shift.md)
   + **Automatic scaling** tab
     + **Dynamic scaling policies** – [Dynamic scaling policies](as-scale-based-on-demand.md)
     + **Predictive scaling policies** – [Predictive scaling policies](ec2-auto-scaling-predictive-scaling.md)
     + **Scheduled actions** – [Scheduled actions](ec2-auto-scaling-scheduled-scaling.md)
   + **Instance management** tab
     + **Lifecycle hooks** – [Lifecycle hooks](lifecycle-hooks.md)
     + **Warm pool** – [Warm pools](ec2-auto-scaling-warm-pools.md)
   + **Activity** tab
     + **Activity notifications** – [Amazon SNS notifications](ec2-auto-scaling-sns-notifications.md)
   + **Monitoring** tab
     + There is just a single option in this tab, which lets you enable or disable [CloudWatch group metrics collection](ec2-auto-scaling-metrics.md).

**To update an Auto Scaling group using the command line**

You can use one of the following commands:
+ [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) (AWS CLI)
+ [Update-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)

## Update Auto Scaling instances
<a name="update-auto-scaling-instances"></a>

If you associate a new launch template or launch configuration with an Auto Scaling group, all new instances will get the updated configuration. Existing instances continue to run with the configuration that they were originally launched with. To apply your changes to existing instances, you have the following options:
+ Start an instance refresh to replace the older instances. For more information, see [Use an instance refresh to update instances in an Auto Scaling group](asg-instance-refresh.md).
+ Wait for scaling activities to gradually replace older instances with newer instances based on your [termination policies](as-instance-termination.md).
+ Manually terminate them so that they are replaced by your Auto Scaling group.

**Note**
You can change the following instance attributes by specifying them as part of the launch template or launch configuration:
Amazon Machine Image (AMI)
block devices
key pair
instance type
security groups
user data
monitoring
IAM instance profile
placement tenancy
kernel
ramdisk
whether the instance has a public IP address
the Availability Zone distribution strategy

## Auto Scaling group allocation strategy and capacity changes
<a name="update-mixed-instance-groups"></a>

When you change an Auto Scaling group allocation strategy, existing instances are not replaced. Any new instances that are launched because of scale out events will follow the new allocation strategy. Any future scale in events will follow the [termination policy](ec2-auto-scaling-termination-policies.md) and use the new allocation strategy if the termination policy is set to `Default` or `AllocationStrategy`. For example, if you change the allocation strategy from `lowest-price` to `price-capacity-optimized`, there might not be any instance terminations, but any new instances will be launched with the new allocation strategy. Instance type changes do not affect existing instances.

When you change certain parameters such as the [OnDemandBaseCapacity](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstancesDistribution.html) or the [OnDemandPercentageAboveBaseCapacity](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstancesDistribution.html), Auto Scaling will automatically rebalance if the percentage of On-Demand Instances and Spot Instances do not match the new specifications. For example, suppose an Auto Scaling group has the `OnDemandPercentageAboveBaseCapacity` set to 50 percent On-Demand Instances and 50 percent Spot Instances. Then, the `OnDemandPercentageAboveBaseCapacity` is increased to 100 percent On-Demand Instances. The Auto Scaling group will proactively rebalance by launching new On-Demand Instances and terminating Spot Instances. The [instance maintenance policy](instance-maintenance-policy-overview-and-considerations.md) that you defined determines the order of the launch and termination activities.
