---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/gracefully-handle-instance-termination.html
---

# Design your applications to gracefully handle instance termination
<a name="gracefully-handle-instance-termination"></a>

 This topic describes features that you can use to prevent your Amazon EC2 Auto Scaling group from terminating Amazon EC2 instances that aren't yet ready to terminate. By default, Auto Scaling has no visibility into the applications running on your instances. It can terminate instances before your application is able to gracefully shut down or complete its assigned jobs. These features give your application time to complete in-progress work, transfer state, or perform cleanup before instance terminations. You can use them individually or in combination depending on your application's requirements.

 These features are particularly useful for stateful workloads, where each instance in your fleet holds different data, jobs, or state than other instances. Terminating stateful instances without graceful shutdown could result in long-running jobs restarting from the beginning, reduced data redundancy or data loss, and interrupted in-progress transactions or computations. To gracefully shut down a stateful instance, its workload should be either drained (completing all currently assigned jobs) or transferred (moving jobs, data, or configuration to another active instance).

**Topics**
+ [Termination lifecycle hooks](#gracefully-handle-instance-termination-lifecycle-hooks)
+ [Instance scale-in protection](#gracefully-handle-instance-termination-scale-in-protection)
+ [Custom termination policy](#gracefully-handle-instance-termination-custom-termination-policy)
+ [Instance lifecycle policy](#gracefully-handle-instance-termination-instance-lifecycle-policy)
+ [Suspend terminations altogether](#gracefully-handle-instance-termination-suspend-terminate)
+ [Limitations](#gracefully-handle-instance-termination-limitations)
+ [Example scenarios](#gracefully-handle-instance-termination-examples)

## Termination lifecycle hooks
<a name="gracefully-handle-instance-termination-lifecycle-hooks"></a>

 A termination lifecycle hook extends the life of your Amazon EC2 instance that's already selected for termination. It provides extra time to complete in-progress work currently assigned to the instance, or to save progress and transfer the work to another instance.

 For many workloads, a termination lifecycle hook may be enough to gracefully shut down an application on an instance that's selected for termination. This is a best-effort approach and can't be used to prevent termination if a termination lifecycle action is abandoned. If your workload has a low tolerance for termination lifecycle action failures, configure [ instance lifecycle policies ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html) in combination with your termination lifecycle hooks to retain instances.

 To use a termination lifecycle hook, you need to know when an instance is selected for termination. You have two ways to know this:

| Option | Description | Best used for | Link to documentation |
| --- | --- | --- | --- |
| Inside the instance |  The Instance Metadata Service (IMDS) is a secure endpoint that you can poll for the status of an instance directly from the instance. If the metadata comes back with Terminated, then your instance is scheduled to be terminated.  |  Applications where you must perform an action on the instance before the instance is terminated.  |  [ Retrieve the target lifecycle state ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/retrieving-target-lifecycle-state-through-imds.html)  |
| Outside the instance |  When an instance is terminating, an event notification is generated. You can create rules using Amazon EventBridge, Amazon SQS, Amazon SNS, or AWS Lambda to capture these events, and invoke a response such as with a Lambda function.  |  Applications that need to take action outside of the instance.  |  [ Configure a notification target ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/prepare-for-lifecycle-notifications.html#lifecycle-hook-notification-target)  |

 To use a lifecycle hook, you also need to know when your instance is ready to be fully terminated. Amazon EC2 Auto Scaling will not terminate the instance until it receives a [ CompleteLifecycleAction ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html) API call or the timeout elapses, whichever happens first.

 By default, an instance can continue running for one hour (heartbeat timeout) due to a termination lifecycle hook. You can configure the default timeout if one hour is not enough time to complete the lifecycle action. When a lifecycle action is in progress, you can extend the timeout with [ RecordLifecycleActionHeartbeat ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RecordLifecycleActionHeartbeat.html) API calls.

 For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](lifecycle-hooks.md).

## Instance scale-in protection
<a name="gracefully-handle-instance-termination-scale-in-protection"></a>

 You can use instance scale-in protection to control which instances are selected for termination during scale-in events, especially to prevent an instance that is actively processing a long-running job from being terminated. For example, when running containerized workloads, it's common to want to protect all instances and remove protection only for instances with no current or scheduled tasks. Instances can continue polling for new jobs and re-enable protection when there are new jobs assigned.

 You can enable scale-in protection at the Auto Scaling group level and instance level. When you enable scale-in protection at the Auto Scaling group level, only new instances are protected when they're created. For existing instances, you can enable protection individually.

 Applications can set protection either from the instances themselves, or from a centralized control plane that manages whether each instance is terminable. We recommend the centralized approach for large fleets or when protection needs to be toggled frequently, as it allows you to batch calls to [ SetInstanceProtection ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SetInstanceProtection.html) and avoid API throttling issues.

 For more information, see [Use instance scale-in protection to control instance termination](ec2-auto-scaling-instance-protection.md).

## Custom termination policy
<a name="gracefully-handle-instance-termination-custom-termination-policy"></a>

 Like instance scale-in protection, a custom termination policy helps you prevent your Amazon EC2 Auto Scaling group from terminating specific EC2 instances. Unhealthy instances can still be terminated regardless of your custom termination policy.

 Your Auto Scaling group uses a default termination policy to determine which Amazon EC2 instances it terminates first. If you want more control over which instances terminate first, you can implement a custom termination policy using a Lambda function. Auto Scaling calls this function whenever it needs to select an instance for termination, and will only terminate instances that the function returns. If the function errors, times out, or returns an empty list, Auto Scaling doesn't terminate any instances unless the instance is unhealthy.

 A custom termination policy is useful when your application can identify which instances are idle or safe to terminate. This typically requires a control plane that tracks workload across the group.

 For more information, see [Create a custom termination policy with Lambda](lambda-custom-termination-policy.md).

## Instance lifecycle policy
<a name="gracefully-handle-instance-termination-instance-lifecycle-policy"></a>

 Instance lifecycle policies provide protection against Amazon EC2 Auto Scaling terminations when a termination lifecycle action is abandoned. Unlike lifecycle hooks alone, instance lifecycle policies are designed to ensure that instances move to a retained state when graceful shutdown procedures don't complete successfully.

 When Auto Scaling selects an instance for termination, your configured termination lifecycle hooks are invoked and your application begins graceful shutdown procedures. If the termination lifecycle actions complete successfully with `CONTINUE`, the instance terminates normally. However, if a termination lifecycle action is abandoned for any reason, the instance lifecycle policy moves the instance to a retained state rather than terminating it. Retained instances don't count toward your Auto Scaling group's desired capacity, so replacement instances are launched automatically. You will incur standard Amazon EC2 charges for both the retained instance and its replacement until you manually terminate the retained instance using the [ TerminateInstanceInAutoScalingGroup ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TerminateInstanceInAutoScalingGroup.html) API.

 To use this feature, you must configure both an instance lifecycle policy with the `TerminateHookAbandon` retention trigger set to `retain`, as well as at least one termination lifecycle hook. Because retained instances incur ongoing Amazon EC2 costs and require manual action, monitoring is critical. You should enable CloudWatch metrics like `GroupTerminatingRetainedInstances` and create CloudWatch alarms to alert you when instances enter retained states.

 For more information, see [Control instance retention with instance lifecycle policies](instance-lifecycle-policy.md).

## Suspend terminations altogether
<a name="gracefully-handle-instance-termination-suspend-terminate"></a>

 If you require complete control over all EC2 instance terminations within your Amazon EC2 Auto Scaling group, suspend the `Terminate` process. We only recommend using this option if the above options do not offer you the control you need for your service. By calling [ SuspendProcesses ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendProcesses.html) to suspend the `Terminate` process, you prevent Auto Scaling from attempting terminations for any reason, except those initiated by a user request to the [ TerminateInstanceInAutoScalingGroup ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TerminateInstanceInAutoScalingGroup.html) API.

 For more information, see [Suspend and resume Amazon EC2 Auto Scaling processes](as-suspend-resume-processes.md).

## Limitations
<a name="gracefully-handle-instance-termination-limitations"></a>

**Important**
 When designing your application on Amazon EC2 Auto Scaling to gracefully handle instance terminations, keep the following limitations in mind.

### Unhealthy instances bypass some protections
<a name="gracefully-handle-instance-termination-unhealthy-bypass"></a>

 If an instance is unhealthy, Amazon EC2 Auto Scaling will start terminating it even if you have custom termination policies or scale-in protection in place. The only way to prevent replacement of unhealthy instances by Auto Scaling is to suspend the `HealthCheck`, `ReplaceUnhealthy`, or `Terminate` process. You can use lifecycle hooks and an instance lifecycle policy to allow the application to shut down gracefully or copy any data that you need to recover before the unhealthy instance is terminated.

| Feature | Controls healthy instances | Controls unhealthy instances |
| --- | --- | --- |
| Custom termination policies | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/negative_icon.png) No |
| Scale-in protection | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/negative_icon.png) No |
|  Suspend HealthCheck, ReplaceUnhealthy, or Terminate process  | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes |
| Lifecycle hooks | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes |
| Instance lifecycle policy | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes | ![](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/success_icon.png) Yes |

### Lifecycle hooks alone do not guarantee graceful shutdown
<a name="gracefully-handle-instance-termination-hooks-no-guarantee"></a>

 By default, termination lifecycle hooks operate on a best-effort basis. If a termination lifecycle action is abandoned, Amazon EC2 Auto Scaling proceeds with terminating the instance immediately. You can combine termination lifecycle hooks with an instance lifecycle policy to retain instances when termination lifecycle actions are abandoned. With this combination:
+  Your termination lifecycle hooks attempt to gracefully shut down your application after Auto Scaling triggers an instance termination and the draining from any configured Elastic Load Balancing load balancers complete.
+  If a termination lifecycle action is abandoned for any reason, the instance moves to a retained state instead of being terminated.
+  The retained instance stays in its current Amazon EC2 state, allowing you to manually complete your shutdown procedures or investigate the failure.
+  You can manually terminate retained instances by calling the [ TerminateInstanceInAutoScalingGroup ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TerminateInstanceInAutoScalingGroup.html) API after completing the necessary actions.

 For more information, see [Control instance retention with instance lifecycle policies](instance-lifecycle-policy.md).

### Certain instance market options can be interrupted with limited notice
<a name="gracefully-handle-instance-termination-spot-interruptions"></a>

 If you use instance market options such as Spot Instances and interruptible capacity reservations in your Auto Scaling group, Amazon EC2 can interrupt and reclaim your instances at any time. These interruptions bypass all Amazon EC2 Auto Scaling protection mechanisms, including:
+ Termination lifecycle hooks
+ Instance scale-in protection
+ Custom termination policies
+ Instance lifecycle policies
+ Suspended processes

 When a Spot Instance receives an interruption notice, you have approximately two minutes to perform graceful shutdown tasks. While you can use termination lifecycle hooks to respond to Spot Instance interruptions, the instance will be forcibly terminated at the end of the two-minute window, even if the lifecycle hook is still in progress. Instance lifecycle policies also can't prevent Spot Instance interruptions.

 For more information about handling Spot Instance interruptions, see [ Spot Instance interruptions ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html) and [ Best practices for Amazon EC2 Spot ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) in the *Amazon EC2 User Guide*.

### Direct Amazon EC2 terminations bypass all protections
<a name="gracefully-handle-instance-termination-direct-ec2-api"></a>

 If you terminate an instance in your Auto Scaling group with the Amazon EC2 [ TerminateInstances ](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html) API directly, the termination bypasses all Amazon EC2 Auto Scaling protection mechanisms.

 To terminate instances in your Auto Scaling group while respecting your configured protections, use the [ TerminateInstanceInAutoScalingGroup ](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TerminateInstanceInAutoScalingGroup.html) API instead.

## Example scenarios
<a name="gracefully-handle-instance-termination-examples"></a>

 When you use Amazon EC2 Auto Scaling, you can choose how much fleet management Auto Scaling handles on your behalf versus how much direct control you retain over EC2 instance termination decisions. The more sensitive your workload is to instance terminations, the more control you may want to retain. The following examples describe workloads with different tolerance levels and the recommended configurations:

### Example 1: Distributed database nodes (Low tolerance)
<a name="gracefully-handle-instance-termination-example-database"></a>

 You run a distributed database where each EC2 instance holds a partition of your data with a replication factor of 3. Losing multiple instances that hold replicas of the same partition could cause data loss or make that partition unavailable.

 **Challenge:** Auto Scaling might terminate instances faster than data can be re-replicated to other nodes, and terminations might reduce your capacity below what's needed to maintain your replication factor.

Consider the following configurations:
+  Enable [ instance scale-in protection ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) on all database instances; remove it programmatically only after confirming data is safely replicated elsewhere.
+  Configure [ termination lifecycle hooks ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) with extended timeouts in combination with an instance lifecycle policy to allow data transfer to complete.
+  Set an [ instance maintenance policy ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html) with a minimum healthy percentage of 100% to maintain your required capacity.

### Example 2: Long-running job processing (Medium tolerance)
<a name="gracefully-handle-instance-termination-example-job-processing"></a>

 You have an Amazon SQS queue that collects incoming messages for long-running jobs. When a new message arrives, an EC2 instance retrieves the message and starts a job that takes 3 hours to process. As the queue grows, Auto Scaling adds instances based on your scaling policies. As the queue shrinks, Auto Scaling terminates instances.

 **Challenge:** Auto Scaling might terminate an instance that is 3 hours into processing a job rather than an idle instance. The job can be restarted on another instance, but you lose significant progress.

Consider the following configurations:
+  Configure a [ custom termination policy ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lambda-custom-termination-policy.html) that prioritizes terminating idle instances first.
+  Use [ termination lifecycle hooks ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) to allow in-progress jobs to complete.
+  Enable [ instance scale-in protection ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) programmatically when an instance starts a job, and remove it when the job completes.

### Example 3: Worker fleet for test environments (High tolerance)
<a name="gracefully-handle-instance-termination-example-test"></a>

 You run a fleet of EC2 instances that execute automated tests, CI/CD pipeline jobs, or development workloads. These worker instances pull tasks from a queue, and test results can be regenerated if a job fails.

 **Challenge:** Test jobs may be interrupted during scale-in events, but since tests can be retried without impact, you want to optimize for cost and simplicity rather than zero-interruption availability.

Consider the following configurations:
+  Use [ termination lifecycle hooks ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) to allow in-flight requests to complete.
+  Consider using [ Spot Instances ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) with capacity-optimized allocation strategy to further reduce costs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
