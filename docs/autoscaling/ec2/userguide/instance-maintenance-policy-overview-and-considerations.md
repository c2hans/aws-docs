---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-maintenance-policy-overview-and-considerations.html
---

# Instance maintenance policy for Auto Scaling group
<a name="instance-maintenance-policy-overview-and-considerations"></a>

This topic provides an overview of the options available and describes what to consider when you create an instance maintenance policy.

**Topics**
+ [Overview](#instance-maintenance-policy-overview)
+ [Core concepts](#instance-maintenance-policy-core-concepts)
+ [Instance warmup](#instance-maintenance-policy-instance-warm-up)
+ [Health check grace period](#instance-maintenance-policy-health-check-grace-period)
+ [Scale your Auto Scaling group](#instance-maintenance-policy-scaling-limits)
+ [Example scenarios](#instance-maintenance-policy-scenarios)

## Overview
<a name="instance-maintenance-policy-overview"></a>

When you create an instance maintenance policy for your Auto Scaling group, the policy affects Amazon EC2 Auto Scaling events that cause instances to be replaced. This results in more consistent replacement behaviors within the same Auto Scaling group. It also lets you optimize your group for availability or cost depending on your needs.

In the console, the following configuration options are available:
+ **Launch before terminating** – A new instance must be provisioned first before an existing instance can be terminated. This approach is a good choice for applications that favor availability over cost savings.
+ **Terminate and launch** – New instances are provisioned at the same time your existing instances are terminated. This approach is a good choice for applications that favor cost savings over availability. It's also a good choice for applications that should not launch more capacity than is currently available, even when replacing instances.
+ **Custom policy** – This option lets you set up your policy with a custom minimum and maximum range for the amount of capacity that you want available when replacing instances. This approach can help you achieve the right balance between cost and availability.

The default for an Auto Scaling group is to not have an instance maintenance policy, which causes it to respond to instance maintenance events with the default behaviors. The default behaviors are described in the following table.

**Instance maintenance event default behaviors**

|  Event  |  Description  |  Default behavior  |
| --- | --- | --- |
| Health check failure | Happens automatically when instances fail their health checks. Amazon EC2 Auto Scaling replaces instances that fail their health checks. To understand the causes of health check failures, see [Health checks for instances in an Auto Scaling group](ec2-auto-scaling-health-checks.md). | Terminate and launch. |
| Instance refresh | Happens when you start an instance refresh. Depending on your configuration, an instance refresh replaces instances one at a time, several at a time, or all at once. For more information, see [Use an instance refresh to update instances in an Auto Scaling group](asg-instance-refresh.md). | Terminate and launch. |
| Maximum instance lifetime | Happens automatically when instances reach the maximum instance lifetime that you specify for your Auto Scaling group. Amazon EC2 Auto Scaling replaces instances that reach their maximum instance lifetime. For more information, see [Replace Auto Scaling instances based on maximum instance lifetime](asg-max-instance-lifetime.md). | Terminate and launch. |
| Rebalancing | Happens automatically if there are underlying changes that cause the group to become unbalanced. Amazon EC2 Auto Scaling rebalances the group in the following situations:+  An Availability Zone that previously had insufficient capacity recovers, or you add or remove an Availability Zone from the group. When this happens, your Auto Scaling group tries to evenly balance itself across Availability Zones. For more information, see [Rebalancing activities](auto-scaling-benefits.md#AutoScalingBehavior.InstanceUsage).  <br />+  You enable Capacity Rebalancing on your Auto Scaling group, and it tries to launch new Spot Instances before existing ones are interrupted as the availability of Spot Instances changes. For more information, see [Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances](ec2-auto-scaling-capacity-rebalancing.md). <br />+  You update your Auto Scaling group, and it gradually replaces instances to match the new purchasing options that you chose when updating a mixed instances policy. For more information, see [Update an Auto Scaling group](update-auto-scaling-group.md).  | Launch before terminating.<br />Amazon EC2 Auto Scaling can exceed your group's size limits by up to 10 percent of its *maximum capacity*. However, if you're using Capacity Rebalancing, it can only exceed these limits by up to 10 percent of the *desired capacity*. |

Amazon EC2 Auto Scaling will continue to default to terminate and launch in the following situations. Therefore, when one of these situations occur, your group's capacity might be less than the lower threshold of your instance maintenance policy.
+ When an instance terminates unexpectedly, for example, because of human action. Amazon EC2 Auto Scaling immediately replaces instances that are no longer running. For more information, see [Amazon EC2 health checks](health-checks-overview.md#instance-health-detection).
+ When Amazon EC2 reboots, stops, or retires an instance as part of a scheduled event before Amazon EC2 Auto Scaling can launch the replacement instance. For more information about these events, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html) in the *Amazon EC2 User Guide*.
+ When the Amazon EC2 Spot Service initiates a Spot Instance interruption and a Spot Instance is then forcibly terminated.

With Spot Instances, if you enabled Capacity Rebalancing on your Auto Scaling group, then the instance might already have a pending instance from a different Spot pool that we launched before we initiated the Spot interruption. For details about how Capacity Rebalancing works, see [Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances](ec2-auto-scaling-capacity-rebalancing.md).

However, because Spot Instances are not guaranteed to remain available and can be terminated with a two-minute Spot Instance interruption notice, your instance maintenance policy's lower threshold can be exceeded if instances are interrupted before your new instances have launched.

## Core concepts
<a name="instance-maintenance-policy-core-concepts"></a>

Before you get started, familiarize yourself with the following core concepts and terms:

**Desired capacity**
The *desired capacity* is the capacity of the Auto Scaling group at the time of creation. It is also the capacity the group attempts to maintain when there are no scaling conditions attached to the group.

**Instance maintenance policy**
An *instance maintenance policy* controls whether an instance is provisioned first before an existing instance is terminated for instance maintenance events. It also determines how far below and over your desired capacity your Auto Scaling group might go to replace multiple instances at the same time.

**Maximum healthy percentage**
The *maximum healthy percentage* is the percentage of its desired capacity that your Auto Scaling group can increase to when replacing instances. It represents the maximum percentage of the group that can be in service and healthy, or pending, to support your workload. In the console, you can set the maximum healthy percentage when you use either the **Launch before terminating** option or the **Custom policy** option. The valid values are 100–200 percent.

**Minimum healthy percentage**
The *minimum healthy percentage* is the percentage of the desired capacity to keep in service, healthy, and ready to use to support your workload when replacing instances. An instance is considered healthy and ready to use after it successfully completes its first health check and the specified warmup time passes. In the console, you can set the minimum healthy percentage when you use either the **Terminate and launch** option or the **Custom policy** option. The valid values are 0–100 percent.
To replace instances faster, you can specify a low minimum healthy percentage. However, if there aren't enough healthy instances running, it can reduce availability. We recommend selecting a reasonable value to maintain availability in situations where multiple instances will be replaced.

## Instance warmup
<a name="instance-maintenance-policy-instance-warm-up"></a>

If your instances need time to initialize after they enter the `InService` state, enable the default instance warmup for your Auto Scaling group. With the default instance warmup, you can prevent instances from being counted toward the minimum healthy percentage before they are ready. This ensures that Amazon EC2 Auto Scaling considers how long it takes to have enough capacity in place to support the workload before it terminates existing instances.

As an added benefit, you can improve the Amazon CloudWatch metrics used for dynamic scaling when you enable the default instance warmup. If your Auto Scaling group has any scaling policies, when the group scales out, it uses the same default warmup period to prevent instances from being counted toward CloudWatch metrics before they have finished initializing.

For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

## Health check grace period
<a name="instance-maintenance-policy-health-check-grace-period"></a>

Amazon EC2 Auto Scaling determines whether an instance is healthy based on the status of the health checks that your Auto Scaling group uses. For more information, see [Health checks for instances in an Auto Scaling group](ec2-auto-scaling-health-checks.md).

To make sure that these health checks start as soon as possible, don't set the group's health check grace period too high, but high enough for your Elastic Load Balancing health checks to determine whether a target is available to handle requests. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

## Scale your Auto Scaling group
<a name="instance-maintenance-policy-scaling-limits"></a>

An instance maintenance policy only applies to instance maintenance events and doesn't prevent the group from being manually or automatically scaled.

When there are scaling policies or scheduled actions attached to your Auto Scaling group, they can run in parallel while instance maintenance events are occurring. In which case, they could increase or decrease the group's desired capacity but only within the scaling limits that you defined. For more information about these limits, see [Set scaling limits for your Auto Scaling group](asg-capacity-limits.md).

## Example scenarios
<a name="instance-maintenance-policy-scenarios"></a>

In a typical scenario, your instance maintenance policy and desired capacity might look something like this:
+ Minimum healthy percentage = 90 percent
+ Maximum healthy percentage = 120 percent
+ Desired capacity = 100

During any instance maintenance event, your Auto Scaling group might have as few as 90 instances and as many as 120. After the event, the group goes back to having 100 instances.

When you use an instance maintenance policy with an Auto Scaling group that has a warm pool, the minimum and maximum healthy percentages are applied separately to the Auto Scaling group and the warm pool.

For example, assume this is your configuration:
+ Minimum healthy percentage = 90 percent
+ Maximum healthy percentage = 120 percent
+ Desired capacity = 100
+ Warm pool size = 10

If you start an instance refresh to recycle the group's instances, Amazon EC2 Auto Scaling replaces instances in the Auto Scaling group first, and then instances in the warm pool. While Amazon EC2 Auto Scaling is still working on replacing instances in the Auto Scaling group, the group might have as few as 90 instances and as many as 120. After finishing with the group, Amazon EC2 Auto Scaling can work on replacing instances in the warm pool. While this is happening, the warm pool might have as few as 9 instances and as many as 12.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
