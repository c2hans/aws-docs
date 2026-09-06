---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/service_code_examples_actions.html
---

# Actions for Auto Scaling using AWS SDKs
<a name="service_code_examples_actions"></a>

The following code examples demonstrate how to perform individual Auto Scaling actions with AWS SDKs. Each example includes a link to GitHub, where you can find instructions for setting up and running the code.

These excerpts call the Auto Scaling API and are code excerpts from larger programs that must be run in context. You can see actions in context in [Scenarios for Auto Scaling using AWS SDKs](service_code_examples_scenarios.md).

 The following examples include only the most commonly used actions. For a complete list, see the [Amazon EC2 Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/Welcome.html).

**Topics**
+ [`AttachInstances`](example_auto-scaling_AttachInstances_section.md)
+ [`AttachLoadBalancerTargetGroups`](example_auto-scaling_AttachLoadBalancerTargetGroups_section.md)
+ [`AttachLoadBalancers`](example_auto-scaling_AttachLoadBalancers_section.md)
+ [`CompleteLifecycleAction`](example_auto-scaling_CompleteLifecycleAction_section.md)
+ [`CreateAutoScalingGroup`](example_auto-scaling_CreateAutoScalingGroup_section.md)
+ [`CreateLaunchConfiguration`](example_auto-scaling_CreateLaunchConfiguration_section.md)
+ [`CreateOrUpdateTags`](example_auto-scaling_CreateOrUpdateTags_section.md)
+ [`DeleteAutoScalingGroup`](example_auto-scaling_DeleteAutoScalingGroup_section.md)
+ [`DeleteLaunchConfiguration`](example_auto-scaling_DeleteLaunchConfiguration_section.md)
+ [`DeleteLifecycleHook`](example_auto-scaling_DeleteLifecycleHook_section.md)
+ [`DeleteNotificationConfiguration`](example_auto-scaling_DeleteNotificationConfiguration_section.md)
+ [`DeletePolicy`](example_auto-scaling_DeletePolicy_section.md)
+ [`DeleteScheduledAction`](example_auto-scaling_DeleteScheduledAction_section.md)
+ [`DeleteTags`](example_auto-scaling_DeleteTags_section.md)
+ [`DescribeAccountLimits`](example_auto-scaling_DescribeAccountLimits_section.md)
+ [`DescribeAdjustmentTypes`](example_auto-scaling_DescribeAdjustmentTypes_section.md)
+ [`DescribeAutoScalingGroups`](example_auto-scaling_DescribeAutoScalingGroups_section.md)
+ [`DescribeAutoScalingInstances`](example_auto-scaling_DescribeAutoScalingInstances_section.md)
+ [`DescribeAutoScalingNotificationTypes`](example_auto-scaling_DescribeAutoScalingNotificationTypes_section.md)
+ [`DescribeLaunchConfigurations`](example_auto-scaling_DescribeLaunchConfigurations_section.md)
+ [`DescribeLifecycleHookTypes`](example_auto-scaling_DescribeLifecycleHookTypes_section.md)
+ [`DescribeLifecycleHooks`](example_auto-scaling_DescribeLifecycleHooks_section.md)
+ [`DescribeLoadBalancers`](example_auto-scaling_DescribeLoadBalancers_section.md)
+ [`DescribeMetricCollectionTypes`](example_auto-scaling_DescribeMetricCollectionTypes_section.md)
+ [`DescribeNotificationConfigurations`](example_auto-scaling_DescribeNotificationConfigurations_section.md)
+ [`DescribePolicies`](example_auto-scaling_DescribePolicies_section.md)
+ [`DescribeScalingActivities`](example_auto-scaling_DescribeScalingActivities_section.md)
+ [`DescribeScalingProcessTypes`](example_auto-scaling_DescribeScalingProcessTypes_section.md)
+ [`DescribeScheduledActions`](example_auto-scaling_DescribeScheduledActions_section.md)
+ [`DescribeTags`](example_auto-scaling_DescribeTags_section.md)
+ [`DescribeTerminationPolicyTypes`](example_auto-scaling_DescribeTerminationPolicyTypes_section.md)
+ [`DetachInstances`](example_auto-scaling_DetachInstances_section.md)
+ [`DetachLoadBalancers`](example_auto-scaling_DetachLoadBalancers_section.md)
+ [`DisableMetricsCollection`](example_auto-scaling_DisableMetricsCollection_section.md)
+ [`EnableMetricsCollection`](example_auto-scaling_EnableMetricsCollection_section.md)
+ [`EnterStandby`](example_auto-scaling_EnterStandby_section.md)
+ [`ExecutePolicy`](example_auto-scaling_ExecutePolicy_section.md)
+ [`ExitStandby`](example_auto-scaling_ExitStandby_section.md)
+ [`PutLifecycleHook`](example_auto-scaling_PutLifecycleHook_section.md)
+ [`PutNotificationConfiguration`](example_auto-scaling_PutNotificationConfiguration_section.md)
+ [`PutScalingPolicy`](example_auto-scaling_PutScalingPolicy_section.md)
+ [`PutScheduledUpdateGroupAction`](example_auto-scaling_PutScheduledUpdateGroupAction_section.md)
+ [`RecordLifecycleActionHeartbeat`](example_auto-scaling_RecordLifecycleActionHeartbeat_section.md)
+ [`ResumeProcesses`](example_auto-scaling_ResumeProcesses_section.md)
+ [`SetDesiredCapacity`](example_auto-scaling_SetDesiredCapacity_section.md)
+ [`SetInstanceHealth`](example_auto-scaling_SetInstanceHealth_section.md)
+ [`SetInstanceProtection`](example_auto-scaling_SetInstanceProtection_section.md)
+ [`SuspendProcesses`](example_auto-scaling_SuspendProcesses_section.md)
+ [`TerminateInstanceInAutoScalingGroup`](example_auto-scaling_TerminateInstanceInAutoScalingGroup_section.md)
+ [`UpdateAutoScalingGroup`](example_auto-scaling_UpdateAutoScalingGroup_section.md)
