---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/manage-retained-instances.html
---

# Manage retained instances
<a name="manage-retained-instances"></a>

 Monitor and control Amazon EC2 instances that have been moved to a retained state. Use CloudWatch metrics to track retained instances, then manually terminate retained instances after completing your custom actions.

 Retained instances do not count toward your Amazon EC2 Auto Scaling group's desired capacity. When an instance enters a retained state, Auto Scaling launches a replacement instance to maintain the desired capacity. For example, suppose your Auto Scaling group has a desired capacity of 10. When an instance enters the `Terminating:Retained` state, Auto Scaling launches a replacement instance to maintain the desired capacity of 10. You now have 11 running instances in total: 10 in your active group plus 1 retained instance. Standard Amazon EC2 charges for all 11 instances will apply until you manually terminate the retained instance.

## Instance lifecycle states of retained instances
<a name="instance-lifecyle-states-of-retained-instances"></a>

 Understand how instances transition through lifecycle states when instance lifecycle policies are used. Instances follow a specific path from normal termination through retention to final termination.

*When retention is triggered, instances transition through these states:*

1. `Terminating` - Normal termination begins

1. `Terminating:Wait` - Lifecycle hook executes

1. `Terminating:Proceed` - Lifecycle actions wrap up (whether they succeeded or failed)

1. `Terminating:Retained` - Hook fails, instance retained for manual intervention

Warm pool instances take different lifecycle state paths depending on the scenario:

*Instances scaling back into the warm pool:*

1. `Warmed:Pending` - Normal warm pool transition begins

1. `Warmed:Pending:Wait` - Lifecycle hook executes

1. `Warmed:Pending:Proceed` - Lifecycle actions wrap up (whether they succeeded or failed)

1. `Warmed:Pending:Retained` - Hook fails, instance retained for manual intervention

*Instances being terminated from the warm pool:*

1. `Warmed:Terminating` - Normal termination begins

1. `Warmed:Terminating:Wait` - Lifecycle hook executes

1. `Warmed:Terminating:Proceed` - Lifecycle actions wrap up (whether they succeeded or failed)

1. `Warmed:Terminating:Retained` - Hook fails, instance retained for manual intervention

## Monitor retained instances
<a name="monitor-retained-instances"></a>

 Because retained Amazon EC2 instances incur costs and require manual intervention, monitoring them is essential. Amazon EC2 Auto Scaling provides several CloudWatch metrics to track retained instances.

Enable group metrics to track retained instances:

```
aws autoscaling enable-metrics-collection \
--auto-scaling-group-name {{my-asg}} \
--metrics {{GroupTerminatingRetainedInstances}}
```

The available metrics are:
+  `GroupTerminatingRetainedInstances` shows the number of instances in the `Terminating:Retained` state.
+  `GroupTerminatingRetainedCapacity` shows the capacity units represented by instances in the `Terminating:Retained` state.
+  `WarmPoolTerminatingRetainedCapacity` tracks retained instances terminating from the warm pool.
+  `WarmPoolPendingRetainedCapacity` tracks retained instances returning to the warm pool.

 You can also check your Amazon EC2 Auto Scaling group's scaling activities to understand why instances were retained. Look for termination activities with `StatusCode: Cancelled` and status reason messages indicating lifecycle hook failures:

```
aws autoscaling describe-scaling-activities \
--auto-scaling-group-name {{my-asg}}
```

 We recommend creating CloudWatch alarms on these metrics to alert you when instances enter a retained state. This helps you track cost implications and ensures you don't forget to clean up instances that require manual intervention.

## Terminate retained instances
<a name="terminate-retained-instances"></a>

After completing your custom actions, terminate your retained instances by calling the [ TerminateInstanceInAutoScalingGroup ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TerminateInstanceInAutoScalingGroup.html) API:

```
aws autoscaling terminate-instance-in-auto-scaling-group \
--instance-id {{i-1234567890abcdef0}} \
--no-should-decrement-desired-capacity
```
