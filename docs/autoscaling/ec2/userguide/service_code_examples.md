---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/service_code_examples.html
---

# Code examples for Auto Scaling using AWS SDKs
<a name="service_code_examples"></a>

The following code examples show how to use Auto Scaling with an AWS software development kit (SDK).

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

**Contents**
+ [Basics](service_code_examples_basics.md)
  + [Hello Auto Scaling](example_auto-scaling_Hello_section.md)
  + [Learn the basics](example_auto-scaling_Scenario_GroupsAndInstances_section.md)
  + [Actions](service_code_examples_actions.md)
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
+ [Scenarios](service_code_examples_scenarios.md)
  + [Build and manage a resilient service](example_cross_ResilientService_section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
