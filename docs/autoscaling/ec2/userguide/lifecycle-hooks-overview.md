---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks-overview.html
---

# How lifecycle hooks work in Auto Scaling groups
<a name="lifecycle-hooks-overview"></a>

An Amazon EC2 instance transitions through different states from the time it launches until it is terminated. You can create custom actions for your Auto Scaling group to act when an instance transitions into a wait state due to a lifecycle hook.

The following illustration shows the transitions between Auto Scaling instance states when you use lifecycle hooks for scale out and scale in.

![The transitions between Auto Scaling instance states when you use lifecycle hooks for scale out and scale in.](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/how-lifecycle-hooks-work.png)

As shown in the preceding diagram:

1. The Auto Scaling group responds to a scale-out event and begins launching an instance.

1. The lifecycle hook puts the instance into a wait state (`Pending:Wait`) and then performs a custom action.

   The instance remains in a wait state until you either complete the lifecycle action, or the timeout period ends. By default, the instance remains in a wait state for one hour, and then the Auto Scaling group continues the launch process (`Pending:Proceed`). If you need more time, you can restart the timeout period by recording a heartbeat. If you complete the lifecycle action when the custom action has completed and the timeout period hasn't expired yet, the period ends and the Auto Scaling group continues the launch process.

1. The instance enters the `InService` state and the health check grace period starts. However, before the instance reaches the `InService` state, if the Auto Scaling group is associated with an Elastic Load Balancing load balancer, the instance is registered with the load balancer, and the load balancer starts checking its health. After the health check grace period ends, Amazon EC2 Auto Scaling begins checking the health state of the instance.

1. The Auto Scaling group responds to a scale-in event and begins terminating an instance. If the Auto Scaling group is being used with Elastic Load Balancing, the terminating instance is first deregistered from the load balancer. If connection draining is enabled for the load balancer, the instance stops accepting new connections and waits for existing connections to drain before completing the deregistration process.

1. The lifecycle hook puts the instance into a wait state (`Terminating:Wait`) and then performs a custom action.

   The instance remains in a wait state either until you complete the lifecycle action, or until the timeout period ends (one hour by default). After you complete the lifecycle hook or the timeout period expires, the instance transitions to the next state (`Terminating:Proceed`).

1. The instance is terminated.

**Important**
Instances in a warm pool also have their own lifecycle with corresponding wait states, as described in [Lifecycle state transitions for instances in a warm pool](warm-pool-instance-lifecycle.md#lifecycle-state-transitions).

## Lifecycle state transitions for instances undergoing root volume replacement
<a name="rvr-lifecycle-state-transitions"></a>

The following diagram shows the transition between Auto Scaling instance states when you use lifecycle hooks for replace root volume:

![The transitions between Auto Scaling instance states when you use lifecycle hooks for replace root volume.](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/root-volume-replacement-lifecycle-states.png)

As shown in the preceding diagram:

1. Auto Scaling group responds to an instance refresh and selects an instance for root volume replacement. The instance enters the `ReplacingRootVolume` state. If the instance is registered with a load balancer it is deregistered from the load balancer.

1. The lifecycle hook puts the instance into a wait state (`ReplacingRootVolume:Wait`) and then performs a custom action. The instance remains in a wait state until you either complete the lifecycle action, or the timeout period ends. If you complete the lifecycle action when the custom action has completed and the timeout period hasn't expired yet, the period ends and the Auto Scaling group continues the root volume replacement process.

1. The instance completes its root volume replacement and enters the `RootVolumeReplaced` state.

1. The instance enters the `Pending` state.

1. The lifecycle hook puts the instance into a wait state (`Pending:Wait`) and then performs a custom action. The instance remains in a wait state either until you complete the lifecycle action, or until the timeout period ends. After you complete the lifecycle hook or the timeout period expires, the instance transitions to the next state (`Pending:Proceed`).

1. The instance enters the `InService` state. However, before the instance reaches the `InService` state, if the Auto Scaling group is associated with an Elastic Load Balancing load balancer, the instance is registered with the load balancer.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
