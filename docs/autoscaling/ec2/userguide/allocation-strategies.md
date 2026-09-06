---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html
---

# Allocation strategies for multiple instance types
<a name="allocation-strategies"></a>

When you use multiple instance types, you manage how Amazon EC2 Auto Scaling fulfills your On-Demand and Spot capacities from the possible instance types. To do this, you specify allocation strategies.

To review the best practices for a mixed instances group, see [Setup overview for creating a mixed instances group](mixed-instances-groups-set-up-overview.md).

**Topics**
+ [Spot Instances](#spot-allocation-strategy)
+ [On-Demand Instances](#on-demand-allocation-strategy)
+ [How the allocation strategies work with weights](#lowest-price-allocation-strategy)

## Spot Instances
<a name="spot-allocation-strategy"></a>

Amazon EC2 Auto Scaling provides the following allocation strategies for Spot Instances:

`price-capacity-optimized` (recommended)
The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price.
We recommend this strategy when you're getting started. For more information, see [Introducing the price-capacity-optimized allocation strategy for EC2 Spot Instances](https://aws.amazon.com/blogs/compute/introducing-price-capacity-optimized-allocation-strategy-for-ec2-spot-instances/) in the AWS blog.

`capacity-optimized`
Amazon EC2 Auto Scaling requests your Spot Instance from the pool with optimal capacity for the number of instances that are launching.
With Spot Instances, the pricing changes slowly over time based on long-term trends in supply and demand. However, capacity fluctuates in real time. The `capacity-optimized` strategy automatically launches Spot Instances into the most available pools by looking at real-time capacity data and predicting which are the most available. This helps to minimize possible disruptions for workloads that might have a higher cost of interruption associated with restarting work and checkpointing. To give certain instance types a higher chance of launching first, use `capacity-optimized-prioritized`.

`capacity-optimized-prioritized`
You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling honors the instance type priorities on a best-effort basis but optimizes for capacity first. This is a good option for workloads where the possibility of disruption must be minimized, but the preference for certain instance types matters, too. If the On-Demand allocation strategy is set to `prioritized`, the same priority is applied when fulfilling On-Demand capacity.

`lowest-price` (not recommended)
We don't recommend the `lowest-price` strategy because it has the highest risk of interruption for your Spot Instances.
Amazon EC2 Auto Scaling requests your Spot Instances using the lowest priced pools within an Availability Zone, across the N number of Spot pools that you specify for the **Lowest priced pools** setting. For example, if you specify four instance types and four Availability Zones, your Auto Scaling group can access up to 16 Spot pools. (Four in each Availability Zone.) If you specify two Spot pools (N=2) for the allocation strategy, your Auto Scaling group can draw on the two lowest priced pools per Availability Zone to fulfill your Spot capacity.
The `lowest-price` strategy is only available when using the AWS CLI.
Amazon EC2 Auto Scaling makes an effort to draw Spot Instances from the N number of pools that you specify. However, if a pool runs out of Spot capacity before fulfilling your desired capacity, Amazon EC2 Auto Scaling continues to fulfill your request by drawing from the next lowest priced pool. To meet your desired capacity, you might receive Spot Instances from more pools than your specified N number. Likewise, if most of the pools have no Spot capacity, you might receive your full desired capacity from fewer pools than your specified N number.

**Note**
If you configure your Spot Instances to launch with [AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) turned on, you are charged an additional hourly usage fee that is equivalent to 10% of the [On-Demand hourly rate](https://aws.amazon.com/ec2/pricing/on-demand/) of the selected instance type. If the allocation strategy uses price as an input, Amazon EC2 Auto Scaling does not include this additional fee; only the Spot price is used.

## On-Demand Instances
<a name="on-demand-allocation-strategy"></a>

Amazon EC2 Auto Scaling provides the following allocation strategies that can be used for On-Demand Instances:

`lowest-price`
Amazon EC2 Auto Scaling automatically deploys the lowest priced instance type in each Availability Zone based on the current On-Demand price.
To meet your desired capacity, you might receive On-Demand Instances of more than one instance type in each Availability Zone. This depends on how much capacity you request.

`prioritized`
When fulfilling On-Demand capacity, Amazon EC2 Auto Scaling determines which instance type to use first based on the order of instance types in the list of launch template overrides. For example, let's say that you specify three launch template overrides in the following order: `c5.large`, `c4.large`, and `c3.large`. When your On-Demand Instances launch, the Auto Scaling group fulfills On-Demand capacity in the following order: `c5.large`, `c4.large`, and then `c3.large`.
Consider the following when managing the priority order of your On-Demand Instances:
+ You can pay for usage upfront to get significant discounts for On-Demand Instances by using Savings Plans or Reserved Instances. For more information, see the [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/) page.
+ With Reserved Instances, your discounted rate of the regular On-Demand Instance pricing applies if Amazon EC2 Auto Scaling launches matching instance types. Therefore, if you have unused Reserved Instances for `c4.large`, you can set the instance type priority to give the highest priority for your Reserved Instances to a `c4.large` instance type. When a `c4.large` instance launches, you receive the Reserved Instance pricing.
+ With Savings Plans, your discounted rate of the regular On-Demand Instance pricing applies when using Amazon EC2 Instance Savings Plans or Compute Savings Plans. With Savings Plans, you have more flexibility when prioritizing your instance types. As long as you use instance types that are covered by your Savings Plans, you can set them in any priority order. You can also occasionally change the entire order of your instance types, while still receiving the Savings Plans discounted rate. For more information about Savings Plans, see the [Savings Plans User Guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/).

## How the allocation strategies work with weights
<a name="lowest-price-allocation-strategy"></a>

When you specify the `WeightedCapacity` parameter in your overrides (or `"DesiredCapacityType": "vcpu"` or `"DesiredCapacityType": "memory-mib"` at the group level), the allocation strategies work exactly like they do for other Auto Scaling groups.

Suppose you have an Auto Scaling group with several instance types that have varying amounts of vCPUs. You use `lowest-price` for your Spot and On-Demand allocation strategies. If you choose to assign weights based on the vCPU count of each instance type, Amazon EC2 Auto Scaling launches whichever instance types have the lowest price per your assigned weight values (for example, per vCPU) at the time of fulfillment. If it's a Spot Instance, then this means the lowest Spot price per vCPU. If it's an On-Demand Instance, then this means the lowest On-Demand price per vCPU.

 For more information, see [Configure an Auto Scaling group to use instance weights](ec2-auto-scaling-mixed-instances-groups-instance-weighting.md).
