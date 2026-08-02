---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/understand-how-suspending-processes-affects-other-processes.html
---

# How suspended processes affect other processes
<a name="understand-how-suspending-processes-affects-other-processes"></a>

The following sections describe what happens when different processes are suspended individually.

**Topics**
+ [`Launch` is suspended](#launch-is-suspended)
+ [`Terminate` is suspended](#terminate-is-suspended)
+ [`AddToLoadBalancer` is suspended](#addtoloadbalancer-is-suspended)
+ [`AlarmNotification` is suspended](#alarmnotification-is-suspended)
+ [`AZRebalance` is suspended](#azrebalance-is-suspended)
+ [`HealthCheck` is suspended](#healthcheck-is-suspended)
+ [`InstanceRefresh` is suspended](#instancerefresh-is-suspended)
+ [`ReplaceUnhealthy` is suspended](#replaceunhealthy-is-suspended)
+ [`ScheduledActions` is suspended](#scheduledactions-is-suspended)
+ [Additional considerations](#other-considerations)

## `Launch` is suspended
<a name="launch-is-suspended"></a>
+ `AlarmNotification` is still active, but your Auto Scaling group can't initiate scale-out activities for alarms that are in breach.
+ `ScheduledActions` is active, but your Auto Scaling group can't initiate scale-out activities for any scheduled actions that occur.
+ `AZRebalance` stops rebalancing the group.
+ `ReplaceUnhealthy` continues to terminate unhealthy instances, but does not launch replacements. When you resume the `Launch` process, Amazon EC2 Auto Scaling immediately replaces any instances that it terminated during the time that `Launch` was suspended.
+ `InstanceRefresh` does not replace instances.

## `Terminate` is suspended
<a name="terminate-is-suspended"></a>
+ `AlarmNotification` is still active, but your Auto Scaling group can't initiate scale in activities for alarms that are in breach.
+ `ScheduledActions` is active, but your Auto Scaling group can't initiate scale in activities for any scheduled actions that occur.
+ `AZRebalance` is still active but does not function properly. It can launch new instances without terminating the old ones. This could cause your Auto Scaling group to grow up to 10 percent larger than its maximum size, because this is allowed temporarily during rebalancing activities. Your Auto Scaling group could remain above its maximum size until you resume the `Terminate` process.
+ `ReplaceUnhealthy` is inactive but not `HealthCheck`. When `Terminate` resumes, the `ReplaceUnhealthy` process immediately starts running. If any instances were marked as unhealthy while `Terminate` was suspended, they are immediately replaced.
+ `InstanceRefresh` does not replace instances.

## `AddToLoadBalancer` is suspended
<a name="addtoloadbalancer-is-suspended"></a>
+ Amazon EC2 Auto Scaling launches the instances but does not add them to the load balancer target group or Classic Load Balancer. When you resume the `AddToLoadBalancer` process, it resumes adding instances to the load balancer when they are launched. However, it does not add the instances that were launched while this process was suspended. You must register those instances manually.

## `AlarmNotification` is suspended
<a name="alarmnotification-is-suspended"></a>
+ Amazon EC2 Auto Scaling does not invoke scaling policies when a CloudWatch alarm threshold is in breach. When you resume `AlarmNotification`, Amazon EC2 Auto Scaling considers policies with alarm thresholds that are currently in breach.

## `AZRebalance` is suspended
<a name="azrebalance-is-suspended"></a>
+ Amazon EC2 Auto Scaling does not attempt to redistribute instances after certain events. However, if a scale-out or scale in event occurs, the scaling process still tries to balance the Availability Zones. For example, during scale out, it launches instances in the Availability Zone with the fewest instances. If the group becomes unbalanced while `AZRebalance` is suspended and you resume it, Amazon EC2 Auto Scaling attempts to rebalance the group. It first calls `Launch` and then `Terminate`.
+ Warm pools are not affected when `AZRebalance` is suspended.

## `HealthCheck` is suspended
<a name="healthcheck-is-suspended"></a>
+ Amazon EC2 Auto Scaling stops marking instances unhealthy as a result of EC2 and Elastic Load Balancing health checks. Your custom health checks continue to function properly. After you suspend `HealthCheck`, if you need to, you can manually set the health state of instances in your group and have `ReplaceUnhealthy` replace them.

## `InstanceRefresh` is suspended
<a name="instancerefresh-is-suspended"></a>
+ Amazon EC2 Auto Scaling stops replacing instances as a result of an instance refresh. If there is an instance refresh in progress, this pauses the operation without canceling it.

## `ReplaceUnhealthy` is suspended
<a name="replaceunhealthy-is-suspended"></a>
+ Amazon EC2 Auto Scaling stops replacing instances that are marked as unhealthy. Instances that fail EC2 or Elastic Load Balancing health checks are still marked as unhealthy. As soon as you resume the `ReplaceUnhealthy` process, Amazon EC2 Auto Scaling replaces instances that were marked unhealthy while this process was suspended. The `ReplaceUnhealthy` process calls `Terminate` first and then `Launch`.

## `ScheduledActions` is suspended
<a name="scheduledactions-is-suspended"></a>
+ Amazon EC2 Auto Scaling does not run scheduled actions that are scheduled to run during the suspension period. When you resume `ScheduledActions`, Amazon EC2 Auto Scaling only considers scheduled actions whose scheduled time has not yet passed.

## Additional considerations
<a name="other-considerations"></a>

In addition, when `Launch` or `Terminate` are suspended, the following features might not function correctly:
+ **Maximum instance lifetime** – When `Launch` or `Terminate` are suspended, the maximum instance lifetime feature can't replace any instances.
+ **Spot Instance interruptions** – If `Terminate` is suspended and your Auto Scaling group has Spot Instances, they can still terminate in the event that Spot capacity is no longer available. While `Launch` is suspended, Amazon EC2 Auto Scaling can't launch replacement instances from another Spot Instance pool or from the same Spot Instance pool when it is available again.
+ **Capacity Rebalancing** – If `Terminate` is suspended and you use Capacity Rebalancing to handle Spot Instance interruptions, the Amazon EC2 Spot service can still terminate instances in the event that Spot capacity is no longer available. If `Launch` is suspended, Amazon EC2 Auto Scaling can't launch replacement instances from another Spot Instance pool or from the same Spot Instance pool when it is available again.
+ **Attaching and detaching instances ** – When `Launch` and `Terminate` are suspended, you can detach instances that are attached to your Auto Scaling group, but while `Launch` is suspended, you can't attach new instances to the group.
+ **Standby instances** – When `Launch` and `Terminate` are suspended, you can put an instance in the `Standby` state, but while `Launch` is suspended, you can't return an instance in the `Standby` state to service.
