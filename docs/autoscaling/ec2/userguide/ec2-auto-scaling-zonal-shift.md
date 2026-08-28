---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html
---

# Auto Scaling group zonal shift
<a name="ec2-auto-scaling-zonal-shift"></a>

Zonal shift is a capability in the Amazon Application Recovery Controller (ARC). With zonal shift, you can quickly recover from application impairments in an Availability Zone with a single action. When you enable zonal shift for an Auto Scaling group, the group is registered with the ARC zonal shift service. Then, you can start a zonal shift using the AWS Management Console, AWS CLI, or API and the Auto Scaling group treats the Availability Zone with an active zonal shift as impaired.

## Auto Scaling group zonal shift concepts
<a name="asg-zonal-shift-concepts"></a>

Before proceeding, make sure that you are familiar with the following core concepts related to the integration with ARC zonal shift.

**ARC zonal shift**
Auto Scaling can register Auto Scaling groups with ARC zonal shift when you enable this feature. After registration, you can view your resources with the [ARC `ListManagedResources`](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html) API. For more information, see [Zonal shift in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.

**Availability Zone rebalancing**
Auto Scaling attempts to keep capacity in each Availability Zone balanced. When an imbalance occurs between Availability Zones, Auto Scaling automatically attempts to fix the imbalance. For more information, see [Instance distribution](auto-scaling-benefits.md#AutoScalingBehavior.Rebalancing).

**Dynamic scaling**
Dynamic scaling scales the desired capacity of your Auto Scaling group based on metrics that you choose with scaling policies. For more information, see [Dynamic scaling for Amazon EC2 Auto Scaling](as-scale-based-on-demand.md).

**Health checks**
Auto Scaling periodically checks the health status of all instances within an Auto Scaling group to make sure they're running and in good condition. When an unhealthy instance is detected, Auto Scaling marks it for replacement. For more information, see [Health checks for instances in an Auto Scaling group](ec2-auto-scaling-health-checks.md).

**Instance refresh**
You can use an instance refresh to update the instances in your Auto Scaling group. After an instance refresh is started, Auto Scaling attempts to replace all instances in your Auto Scaling group. For more information, see [Use an instance refresh to update instances in an Auto Scaling group](asg-instance-refresh.md).

**Prescaled**
You can tolerate the loss of a single Availability Zone because you have enough capacity in the remaining Availability Zones for your application.

**Scaling out**
When you increase the desired capacity of an Auto Scaling group, Auto Scaling attempts to launch additional instances to meet the new desired capacity. By default, Auto Scaling launches instance in a balanced way to maintain equal capacity across each enabled Availability Zone in an Auto Scaling group.

## How zonal shift works for Auto Scaling groups
<a name="asg-zonal-shift-how-it-works"></a>

Suppose you have an Auto Scaling group with the following Availability Zones:
+ `us-east-1a`
+ `us-east-1b`
+ `us-east-1c`

You have zonal shift enabled in all Availability Zones and notice failures in `us-east-1a` so you trigger a zonal shift. The following behaviors occur when a zonal shift is triggered in `us-east-1a`.
+ **Scaling out** – Auto Scaling will launch all new capacity requests in the healthy Availability Zones (`us-east-1b` and `us-east-1c`).
+ **Dynamic scaling** – Auto Scaling will block scaling policies from decreasing desired capacity in all Availability Zones. Auto Scaling will not block scaling policies from increasing desired capacity in all Availability Zones.
+ **Instance refreshes** – Auto Scaling will extend the timeout for any instance refresh process that is delayed while a zonal shift is active.

The following table describes the health check behavior for each option when a zonal shift is triggered in `us-east-1a`.

| Impaired Availability Zone health check behavior selection | Health check behavior |
| --- | --- |
| Replace unhealthy | Instances that appear unhealthy will be replaced in all Availability Zones (`us-east-1a`, `us-east-1b`, and `us-east-1c`). |
| Ignore unhealthy | Instances that appear unhealthy will be replaced in `us-east-1b` and `us-east-1c`. Instances will not be replaced in the Availability Zone with the active zonal shift (`us-east-1a`). |

## Best practices for using zonal shift
<a name="asg-zonal-shift-best-practices"></a>

To maintain high availability for your applications when using zonal shift, we recommend the following best practices:
+ Monitor EventBridge notifications to determine when there is an ongoing Availability Zone impairment event. For more information, see [Use EventBridge to handle Auto Scaling events](automating-ec2-auto-scaling-with-eventbridge.md).
+ Use scaling policies with appropriate thresholds to make sure that you have enough capacity to tolerate the loss of an Availability Zone.
+ Set an instance maintenance policy with a minimum healthy percentage of 100. With this setting, Auto Scaling waits for a new instance to be ready to use before terminating an unhealthy instance.

For prescaled customers, we also recommend the following:
+ Select **Ignore unhealthy** as the health check behavior for the impaired Availability Zone because you don't need to replace the unhealthy instance during the impairment event.
+ Use zonal autoshift in ARC for your Auto Scaling groups. The zonal autoshift capability in ARC allows AWS to shift traffic for a resource away from an Availability Zone when AWS detects an impairment in an Availability Zone. For more information, see [Zonal autoshift in ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.html) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.

For customers with cross-zone disabled load balancers, we also recommend the following:
+ Use **balanced only** for your Availability Zone distribution.
+ If you are using zonal shift on both Auto Scaling groups and load balancers, cancel the zonal shift on your Auto Scaling group first. Then, wait for capacity to balance across all Availability Zones before canceling the zonal shift on the load balancer.
+ Due to the possibility for imbalanced capacity when you enable zonal shift and use a cross-zone disabled load balancer, Auto Scaling includes an extra validation step. If you are following best practices, you can acknowledge this possibility by selecting the AWS Management Console checkbox or using the `skip-zonal-shift-validation` flag in `CreateAutoScalingGroup`, `UpdateAutoScalingGroup`, or `AttachTrafficSources`.

For more information about using zonal shift with Auto Scaling groups, see the AWS Compute Blog [Using zonal shift with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/using-zonal-shift-with-amazon-ec2-auto-scaling/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
