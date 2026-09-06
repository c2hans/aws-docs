---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for Auto Scaling using AWS SDKs
<a name="auto-scaling_code_examples"></a>

The following code examples show you how to use Amazon EC2 Auto Scaling with an AWS software development kit (SDK).

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

**More resources**
+  **[ Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)** – More information about Auto Scaling.
+ **[Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/Welcome.html)** – Details about all available Auto Scaling actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23ec2-auto-scaling)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](auto-scaling_code_examples_basics.md)
  + [Hello Auto Scaling](auto-scaling_example_auto-scaling_Hello_section.md)
  + [Learn the basics](auto-scaling_example_auto-scaling_Scenario_GroupsAndInstances_section.md)
  + [Actions](auto-scaling_code_examples_actions.md)
    + [`AttachInstances`](auto-scaling_example_auto-scaling_AttachInstances_section.md)
    + [`AttachLoadBalancerTargetGroups`](auto-scaling_example_auto-scaling_AttachLoadBalancerTargetGroups_section.md)
    + [`AttachLoadBalancers`](auto-scaling_example_auto-scaling_AttachLoadBalancers_section.md)
    + [`CompleteLifecycleAction`](auto-scaling_example_auto-scaling_CompleteLifecycleAction_section.md)
    + [`CreateAutoScalingGroup`](auto-scaling_example_auto-scaling_CreateAutoScalingGroup_section.md)
    + [`CreateLaunchConfiguration`](auto-scaling_example_auto-scaling_CreateLaunchConfiguration_section.md)
    + [`CreateOrUpdateTags`](auto-scaling_example_auto-scaling_CreateOrUpdateTags_section.md)
    + [`DeleteAutoScalingGroup`](auto-scaling_example_auto-scaling_DeleteAutoScalingGroup_section.md)
    + [`DeleteLaunchConfiguration`](auto-scaling_example_auto-scaling_DeleteLaunchConfiguration_section.md)
    + [`DeleteLifecycleHook`](auto-scaling_example_auto-scaling_DeleteLifecycleHook_section.md)
    + [`DeleteNotificationConfiguration`](auto-scaling_example_auto-scaling_DeleteNotificationConfiguration_section.md)
    + [`DeletePolicy`](auto-scaling_example_auto-scaling_DeletePolicy_section.md)
    + [`DeleteScheduledAction`](auto-scaling_example_auto-scaling_DeleteScheduledAction_section.md)
    + [`DeleteTags`](auto-scaling_example_auto-scaling_DeleteTags_section.md)
    + [`DescribeAccountLimits`](auto-scaling_example_auto-scaling_DescribeAccountLimits_section.md)
    + [`DescribeAdjustmentTypes`](auto-scaling_example_auto-scaling_DescribeAdjustmentTypes_section.md)
    + [`DescribeAutoScalingGroups`](auto-scaling_example_auto-scaling_DescribeAutoScalingGroups_section.md)
    + [`DescribeAutoScalingInstances`](auto-scaling_example_auto-scaling_DescribeAutoScalingInstances_section.md)
    + [`DescribeAutoScalingNotificationTypes`](auto-scaling_example_auto-scaling_DescribeAutoScalingNotificationTypes_section.md)
    + [`DescribeLaunchConfigurations`](auto-scaling_example_auto-scaling_DescribeLaunchConfigurations_section.md)
    + [`DescribeLifecycleHookTypes`](auto-scaling_example_auto-scaling_DescribeLifecycleHookTypes_section.md)
    + [`DescribeLifecycleHooks`](auto-scaling_example_auto-scaling_DescribeLifecycleHooks_section.md)
    + [`DescribeLoadBalancers`](auto-scaling_example_auto-scaling_DescribeLoadBalancers_section.md)
    + [`DescribeMetricCollectionTypes`](auto-scaling_example_auto-scaling_DescribeMetricCollectionTypes_section.md)
    + [`DescribeNotificationConfigurations`](auto-scaling_example_auto-scaling_DescribeNotificationConfigurations_section.md)
    + [`DescribePolicies`](auto-scaling_example_auto-scaling_DescribePolicies_section.md)
    + [`DescribeScalingActivities`](auto-scaling_example_auto-scaling_DescribeScalingActivities_section.md)
    + [`DescribeScalingProcessTypes`](auto-scaling_example_auto-scaling_DescribeScalingProcessTypes_section.md)
    + [`DescribeScheduledActions`](auto-scaling_example_auto-scaling_DescribeScheduledActions_section.md)
    + [`DescribeTags`](auto-scaling_example_auto-scaling_DescribeTags_section.md)
    + [`DescribeTerminationPolicyTypes`](auto-scaling_example_auto-scaling_DescribeTerminationPolicyTypes_section.md)
    + [`DetachInstances`](auto-scaling_example_auto-scaling_DetachInstances_section.md)
    + [`DetachLoadBalancers`](auto-scaling_example_auto-scaling_DetachLoadBalancers_section.md)
    + [`DisableMetricsCollection`](auto-scaling_example_auto-scaling_DisableMetricsCollection_section.md)
    + [`EnableMetricsCollection`](auto-scaling_example_auto-scaling_EnableMetricsCollection_section.md)
    + [`EnterStandby`](auto-scaling_example_auto-scaling_EnterStandby_section.md)
    + [`ExecutePolicy`](auto-scaling_example_auto-scaling_ExecutePolicy_section.md)
    + [`ExitStandby`](auto-scaling_example_auto-scaling_ExitStandby_section.md)
    + [`PutLifecycleHook`](auto-scaling_example_auto-scaling_PutLifecycleHook_section.md)
    + [`PutNotificationConfiguration`](auto-scaling_example_auto-scaling_PutNotificationConfiguration_section.md)
    + [`PutScalingPolicy`](auto-scaling_example_auto-scaling_PutScalingPolicy_section.md)
    + [`PutScheduledUpdateGroupAction`](auto-scaling_example_auto-scaling_PutScheduledUpdateGroupAction_section.md)
    + [`RecordLifecycleActionHeartbeat`](auto-scaling_example_auto-scaling_RecordLifecycleActionHeartbeat_section.md)
    + [`ResumeProcesses`](auto-scaling_example_auto-scaling_ResumeProcesses_section.md)
    + [`SetDesiredCapacity`](auto-scaling_example_auto-scaling_SetDesiredCapacity_section.md)
    + [`SetInstanceHealth`](auto-scaling_example_auto-scaling_SetInstanceHealth_section.md)
    + [`SetInstanceProtection`](auto-scaling_example_auto-scaling_SetInstanceProtection_section.md)
    + [`SuspendProcesses`](auto-scaling_example_auto-scaling_SuspendProcesses_section.md)
    + [`TerminateInstanceInAutoScalingGroup`](auto-scaling_example_auto-scaling_TerminateInstanceInAutoScalingGroup_section.md)
    + [`UpdateAutoScalingGroup`](auto-scaling_example_auto-scaling_UpdateAutoScalingGroup_section.md)
+ [Scenarios](auto-scaling_code_examples_scenarios.md)
  + [Build and manage a resilient service](auto-scaling_example_cross_ResilientService_section.md)
