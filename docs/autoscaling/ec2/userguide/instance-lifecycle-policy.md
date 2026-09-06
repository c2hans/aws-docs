---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html
---

# Control instance retention with instance lifecycle policies
<a name="instance-lifecycle-policy"></a>

 Instance lifecycle policies provide protection against Amazon EC2 Auto Scaling terminations when a termination lifecycle action is abandoned. Unlike lifecycle hooks alone, instance lifecycle policies are designed to ensure that instances move to a retained state when graceful shutdown procedures don't complete successfully.

## When to use instance lifecycle policies
<a name="when-to-use-instance-lifecycle-policies"></a>

 Use instance lifecycle policies when graceful shutdown of your application is not optional but mandatory and failed shutdowns require manual intervention. Common use cases include:
+  Stateful applications that must complete data persistence before termination.
+  Applications requiring extended draining periods that may exceed the maximum lifecycle hook timeout of 48 hours.
+  Workloads handling sensitive data where failed or incomplete cleanup could result in data loss or corruption.
+  Mission-critical services where abrupt shutdown causes availability impact.

 For more information on how to gracefully handle instance termination, see [Design your applications to gracefully handle instance termination](gracefully-handle-instance-termination.md).

## How instance lifecycle policies work with termination lifecycle hooks
<a name="how-instance-lifecycle-policies-work"></a>

 Instance lifecycle policies work in combination with termination lifecycle hooks, not as a replacement. The process follows several stages:

1.  **Termination lifecycle actions execute.** When Amazon EC2 Auto Scaling selects an instance for termination, your termination lifecycle hooks are invoked and the instance enters the `Terminating:Wait` state to begin executing the termination lifecycle actions.

1.  **Graceful shutdown attempt begins.** Your application, either running on the instance or via a control plane, receives the terminatioin lifecycle action notification and begins graceful shutdown procedures such as draining connections, completing in-progress work, or transferring data.

1.  **Termination lifecycle actions complete.** A termination lifecycle action can complete with `CONTINUE` or `ABANDON` result.

1.  **The instance lifecycle policy evaluates the situation.** Without an instance lifecycle policy configured, the instance proceeds to termination immediately even if the termination lifecycle action was completed with `ABANDON` result. With an instance lifecycle policy configured to retain instances on `TerminateHookAbandon`, the instance moves to a retained state if the termination lifecycle action was completed with `ABANDON` result.

1.  **Retained instances await manual action.** Instances in retained states continue to incur standard Amazon EC2 charges. These instances don't count toward your Auto Scaling group's desired capacity, so Auto Scaling launches replacement instances to maintain the desired size. Auto Scaling features such as instance refresh and max instance lifetime will also ignore retained instances. This allows you to complete cleanup procedures manually, recover data, or investigate why automated shutdown failed before manually terminating the instance.

1.  **Manual termination occurs.** After you complete the necessary actions on the retained instance, you need to call the `TerminateInstanceInAutoScalingGroup` API to terminate the instance.
