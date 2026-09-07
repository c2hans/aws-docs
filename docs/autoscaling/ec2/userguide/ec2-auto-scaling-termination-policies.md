---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html
---

# Configure termination policies for Amazon EC2 Auto Scaling
<a name="ec2-auto-scaling-termination-policies"></a>

A termination policy provides the criteria that Amazon EC2 Auto Scaling follows to terminate instances in a specific order. By default, Amazon EC2 Auto Scaling uses a termination policy that's designed to terminate instances that are using outdated configurations first. You can change the termination policy to control which instances are most important to terminate first.

When Amazon EC2 Auto Scaling terminates instances, it tries to maintain balance across the Availability Zones that are enabled for your Auto Scaling group. Maintaining Zonal balance takes precedence over the termination policy. If one Availability Zone has more instances than others, Amazon EC2 Auto Scaling applies the termination policy to the imbalanced zone first. If the Availability Zones are balanced, it applies the termination policy across all Zones.

**Topics**
+ [How the default termination policy works](#default-termination-policy)
+ [Default termination policy and mixed instances groups](#default-termination-policy-mixed-instances-groups)
+ [Predefined termination policies](#predefined-termination-policies)
+ [Change the termination policy for an Auto Scaling group](custom-termination-policy.md)

**Note**
Amazon EC2 Auto Scaling applies termination policies only to instances that are not considered unhealthy by the Auto Scaling group. As a result, instances marked as unhealthy by Auto Scaling health checks will bypass termination policy evaluation.
For more information, see [Design your applications to gracefully handle instance termination](gracefully-handle-instance-termination.md).

## How the default termination policy works
<a name="default-termination-policy"></a>

When Amazon EC2 Auto Scaling needs to terminate an instance, it first identifies which Availability Zone (or Zones) has the most instances and at least one instance that is not protected from scale in. Then, it proceeds to evaluate unprotected instances within the identified Availability Zone as follows:

**Instances that use outdated configurations**
+ **For groups that use a launch template** – Determine whether any of the instances use outdated configurations, prioritizing in this order:

  1. First, check for instances launched with a launch configuration.

  1. Then, check for instances launched using a different launch template instead of the current launch template.

  1. Finally, check for instances using the oldest version of the current launch template.
+ **For groups that use a launch configuration** – Determine whether any of the instances use the oldest launch configuration.

If no instances with outdated configurations are found, or there are multiple instances to choose from, Amazon EC2 Auto Scaling considers the next criteria of instances approaching their next billing hour.

**Instances approaching next billing hour**
Determine whether any of the instances that meet the previous criteria are closest to the next billing hour. If multiple instances are equally close, terminate one at random. This helps you maximize the use of your instances that are billed hourly. However, most EC2 usage is now billed per second, so this optimization provides less benefit. For more information, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).

The following flow diagram illustrates how the default termination policy works for groups that use a launch template.

![A flowchart showing how an Auto Scaling group uses the default termination policy to terminate instances.](https://docs.aws.amazon.com/autoscaling/ec2/userguide/images/termination-policy-default-flowchart-diagram.png)

## Default termination policy and mixed instances groups
<a name="default-termination-policy-mixed-instances-groups"></a>

Amazon EC2 Auto Scaling applies additional criteria when terminating instances in [mixed instances groups](ec2-auto-scaling-mixed-instances-groups.md).

When Amazon EC2 Auto Scaling needs to terminate an instance, it first identifies which purchase option (Spot or On-Demand) should be terminated based on the settings of the group. This makes sure that the group trends toward the specified ratio of Spot and On-Demand instances over time.

It then applies the termination policy independently within each Availability Zone. It determines which Spot or On-Demand Instance in which Availability Zone to terminate to keep the Availability Zones balanced. The same logic applies to a mixed instances group with weights defined for the instance types.

Within each zone, the default termination policy works as follows to determine which unprotected instance within the identified purchase option can be terminated:

1. Determine whether any of the instances can be terminated to improve alignment with the specified [allocation strategy](allocation-strategies.md) for the Auto Scaling group. If no instances are identified for optimization, or there are multiple instances to choose from, the evaluation continues.

1. Determine whether any of the instances use outdated configurations, prioritizing in this order:

   1. First, check for instances launched with a launch configuration.

   1. Then, check for instances launched using a different launch template instead of the current launch template.

   1. Finally, check for instances using the oldest version of the current launch template.

   If no instances with outdated configurations are found, or there are multiple instances to choose from, the evaluation continues.

1. Determine whether any of the instances are closest to the next billing hour. If multiple instances are equally close, choose one at random.

## Predefined termination policies
<a name="predefined-termination-policies"></a>

You choose from the following predefined termination policies:
+ **`Default`** – Terminate instances according to the default termination policy.
+ **`AllocationStrategy`** – Terminate instances in the Auto Scaling group to align the remaining instances to the allocation strategy for the type of instance that is terminating (either a Spot Instance or an On-Demand Instance). This policy is useful when your preferred instance types have changed. If the Spot allocation strategy is `lowest-price`, you can gradually rebalance the distribution of Spot Instances across your N lowest priced Spot pools. If the Spot allocation strategy is `capacity-optimized`, you can gradually rebalance the distribution of Spot Instances across Spot pools where there is more available Spot capacity. You can also gradually replace On-Demand Instances of a lower priority type with On-Demand Instances of a higher priority type.
+ **`OldestLaunchTemplate`** – Terminate instances that have the oldest launch template. With this policy, instances that use the noncurrent launch template are terminated first, followed by instances that use the oldest version of the current launch template. This policy is useful when you're updating a group and phasing out the instances from a previous configuration.
+ **`OldestLaunchConfiguration`** – Terminate instances that have the oldest launch configuration. This policy is useful when you're updating a group and phasing out the instances from a previous configuration. With this policy, instances that use the noncurrent launch configuration are terminated first.
+ **`ClosestToNextInstanceHour`** – Terminate instances that are closest to the next billing hour. This policy helps you maximize the use of your instances that have an hourly charge.
+ **`NewestInstance`** – Terminate the newest instance in the group. This policy is useful when you're testing a new launch configuration but don't want to keep it in production.
+ **`OldestInstance`** – Terminate the oldest instance in the group. This option is useful when you're upgrading the instances in the Auto Scaling group to a new EC2 instance type. You can gradually replace instances of the old type with instances of the new type.
**Note**
Amazon EC2 Auto Scaling always balances instances across Availability Zones first, regardless of which termination policy is used. As a result, you might encounter situations in which some newer instances are terminated before older instances. For example, when there is a more recently added Availability Zone, or when one Availability Zone has more instances than the other Availability Zones that are used by the group.
