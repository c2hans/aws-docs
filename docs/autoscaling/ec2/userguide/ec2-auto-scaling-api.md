---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-api.html
---

# Working with the Amazon EC2 Auto Scaling APIs
<a name="ec2-auto-scaling-api"></a>

The API for Amazon EC2 Auto Scaling is the protocol-level interface for Amazon EC2 Auto Scaling. When using the API, you must format every HTTPS request correctly and add a valid digital signature to every request. For more information, see the [ Amazon EC2 Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/Welcome.html).

The Amazon EC2 Auto Scaling API includes the following API actions:

**Account Limits**
+ [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html)

**Auto Scaling Groups**
+ [AttachLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancers.html)
+ [AttachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html)
+ [CreateAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html)
+ [DeleteAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteAutoScalingGroup.html)
+ [DescribeAutoScalingGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html)
+ [DescribeLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancers.html)
+ [DescribeLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLoadBalancerTargetGroups.html)
+ [DetachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html)
+ [DetachLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancers.html)
+ [UpdateAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_UpdateAutoScalingGroup.html)

**Auto Scaling Instances**
+ [AttachInstances](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachInstances.html)
+ [DescribeAutoScalingInstances](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingInstances.html)
+ [DetachInstances](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachInstances.html)
+ [SetInstanceHealth](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SetInstanceHealth.html)
+ [SetInstanceProtection](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SetInstanceProtection.html)
+ [TerminateInstanceInAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TerminateInstanceInAutoScalingGroup.html)

**Instance Refreshes**
+ [CancelInstanceRefresh](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CancelInstanceRefresh.html)
+ [DescribeInstanceRefreshes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html)
+ [RollbackInstanceRefresh](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackInstanceRefresh.html)
+ [StartInstanceRefresh](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_StartInstanceRefresh.html)

**Launch Configurations**
+ [CreateLaunchConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateLaunchConfiguration.html)
+ [DeleteLaunchConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteLaunchConfiguration.html)
+ [DescribeLaunchConfigurations](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLaunchConfigurations.html)

**Lifecycle Hooks**
+ [CompleteLifecycleAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html)
+ [DeleteLifecycleHook](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteLifecycleHook.html)
+ [DescribeLifecycleHooks](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHooks.html)
+ [DescribeLifecycleHookTypes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHookTypes.html)
+ [PutLifecycleHook](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutLifecycleHook.html)
+ [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RecordLifecycleActionHeartbeat.html)

**Monitoring**
+ [DeleteNotificationConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteNotificationConfiguration.html)
+ [DescribeAutoScalingNotificationTypes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingNotificationTypes.html)
+ [DescribeMetricCollectionTypes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeMetricCollectionTypes.html)
+ [DescribeNotificationConfigurations](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeNotificationConfigurations.html)
+ [DisableMetricsCollection](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DisableMetricsCollection.html)
+ [EnableMetricsCollection](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html)
+ [PutNotificationConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutNotificationConfiguration.html)

**Scaling**
+ [DeletePolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeletePolicy.html)
+ [DescribeAdjustmentTypes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAdjustmentTypes.html)
+ [DescribePolicies](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html)
+ [DescribeScalingActivities](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html)
+ [DescribeScalingProcessTypes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingProcessTypes.html)
+ [DescribeTerminationPolicyTypes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTerminationPolicyTypes.html)
+ [ExecutePolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ExecutePolicy.html)
+ [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html)
+ [ResumeProcesses](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html)
+ [SetDesiredCapacity](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SetDesiredCapacity.html)
+ [SuspendProcesses](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendProcesses.html)

**Scheduled Scaling**
+ [BatchDeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BatchDeleteScheduledAction.html)
+ [BatchPutScheduledUpdateGroupAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BatchPutScheduledUpdateGroupAction.html)
+ [DeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteScheduledAction.html)
+ [DescribeScheduledActions](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScheduledActions.html)
+ [PutScheduledUpdateGroupAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScheduledUpdateGroupAction.html)

**Standby State**
+ [EnterStandby](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnterStandby.html)
+ [ExitStandby](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ExitStandby.html)

**Tags**
+ [CreateOrUpdateTags](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateOrUpdateTags.html)
+ [DeleteTags](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteTags.html)
+ [DescribeTags](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTags.html)

**Warm Pools**
+ [PutWarmPool](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutWarmPool.html)
+ [DescribeWarmPool](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html)
+ [DeleteWarmPool](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteWarmPool.html)
