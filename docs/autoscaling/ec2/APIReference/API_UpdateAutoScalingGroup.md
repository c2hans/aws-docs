---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_UpdateAutoScalingGroup.html
---

# UpdateAutoScalingGroup
<a name="API_UpdateAutoScalingGroup"></a>

 **We strongly recommend that all Auto Scaling groups use launch templates to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.**

Updates the configuration for the specified Auto Scaling group.

To update an Auto Scaling group, specify the name of the group and the property that you want to change. Any properties that you don't specify are not changed by this update request. The new settings take effect on any scaling activities after this call returns.

If you associate a new launch configuration or template with an Auto Scaling group, all new instances will get the updated configuration. Existing instances continue to run with the configuration that they were originally launched with. When you update a group to specify a mixed instances policy instead of a launch configuration or template, existing instances may be replaced to match the new purchasing options that you specified in the policy. For example, if the group currently has 100% On-Demand capacity and the policy specifies 50% Spot capacity, this means that half of your instances will be gradually terminated and relaunched as Spot Instances. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that updating your group does not compromise the performance or availability of your application.

Note the following about changing `DesiredCapacity`, `MaxSize`, or `MinSize`:
+ If a scale-in activity occurs as a result of a new `DesiredCapacity` value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate.
+ If you specify a new value for `MinSize` without specifying a value for `DesiredCapacity`, and the new `MinSize` is larger than the current size of the group, this sets the group's `DesiredCapacity` to the new `MinSize` value.
+ If you specify a new value for `MaxSize` without specifying a value for `DesiredCapacity`, and the new `MaxSize` is smaller than the current size of the group, this sets the group's `DesiredCapacity` to the new `MaxSize` value.

To see which properties have been set, call the [DescribeAutoScalingGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html) API. To view the scaling policies for an Auto Scaling group, call the [DescribePolicies](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribePolicies.html) API. If the group has scaling policies, you can update them by calling the [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html) API.

## Request Parameters
<a name="API_UpdateAutoScalingGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** AvailabilityZoneDistribution **
 The instance capacity distribution across Availability Zones.
Type: [AvailabilityZoneDistribution](API_AvailabilityZoneDistribution.md) object
Required: No

 **AvailabilityZoneIds.member.N**
 A list of Availability Zone IDs for the Auto Scaling group. You cannot specify both AvailabilityZones and AvailabilityZoneIds in the same request.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AvailabilityZoneImpairmentPolicy **
 The policy for Availability Zone impairment.
Type: [AvailabilityZoneImpairmentPolicy](API_AvailabilityZoneImpairmentPolicy.md) object
Required: No

 **AvailabilityZones.member.N**
One or more Availability Zones for the group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** CapacityRebalance **
Enables or disables Capacity Rebalancing. If Capacity Rebalancing is disabled, proactive replacement of at-risk Spot Instances does not occur. For more information, see [Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html) in the *Amazon EC2 Auto Scaling User Guide*.
To suspend rebalancing across Availability Zones, use the [SuspendProcesses](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendedProcess.html) API.
Type: Boolean
Required: No

 ** CapacityReservationSpecification **
 The capacity reservation specification for the Auto Scaling group.
Type: [CapacityReservationSpecification](API_CapacityReservationSpecification.md) object
Required: No

 ** Context **
Reserved.
Type: String
Required: No

 ** DefaultCooldown **
 *Only needed if you use simple scaling policies.*
The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see [Scaling cooldowns for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-cooldowns.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Integer
Required: No

 ** DefaultInstanceWarmup **
The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the `InService` state.
During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see [Set the default instance warmup for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html) in the *Amazon EC2 Auto Scaling User Guide*.
To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, *even if it is set to 0 seconds*. To remove a value that you previously set, include the property but specify `-1` for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of `0` or other nominal value.
Type: Integer
Required: No

 ** DeletionProtection **
 The deletion protection setting for the Auto Scaling group. This setting helps safeguard your Auto Scaling group and its instances by controlling whether the `DeleteAutoScalingGroup` operation is allowed. When deletion protection is enabled, users cannot delete the Auto Scaling group according to the specified protection level until the setting is changed back to a less restrictive level.
 The valid values are `none`, `prevent-force-deletion`, and `prevent-all-deletion`.
 Default: `none`
 For more information, see [ Configure deletion protection for your Amazon EC2 Auto Scaling resources](https://docs.aws.amazon.com/autoscaling/ec2/userguide/resource-deletion-protection.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Valid Values: `none | prevent-force-deletion | prevent-all-deletion`
Required: No

 ** DesiredCapacity **
The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.
Type: Integer
Required: No

 ** DesiredCapacityType **
The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports `DesiredCapacityType` for attribute-based instance type selection only. For more information, see [Create a mixed instances group using attribute-based instance type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.html) in the *Amazon EC2 Auto Scaling User Guide*.
By default, Amazon EC2 Auto Scaling specifies `units`, which translates into number of instances.
Valid values: `units` \| `vcpu` \| `memory-mib`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** HealthCheckGracePeriod **
The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Integer
Required: No

 ** HealthCheckType **
A comma-separated value string of one or more health check types.
The valid values are `EC2`, `EBS`, `ELB`, and `VPC_LATTICE`. `EC2` is the default health check and cannot be disabled. For more information, see [Health checks for instances in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html) in the *Amazon EC2 Auto Scaling User Guide*.
Only specify `EC2` if you must clear a value that was previously set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** InstanceLifecyclePolicy **
 The instance lifecycle policy for the Auto Scaling group. This policy controls instance behavior when an instance transitions through its lifecycle states. Configure retention triggers to specify when instances should move to a `Retained` state instead of automatic termination.
For more information, see [ Control instance retention with instance lifecycle policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: [InstanceLifecyclePolicy](API_InstanceLifecyclePolicy.md) object
Required: No

 ** InstanceMaintenancePolicy **
An instance maintenance policy. For more information, see [Set instance maintenance policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: [InstanceMaintenancePolicy](API_InstanceMaintenancePolicy.md) object
Required: No

 ** LaunchConfigurationName **
The name of the launch configuration. If you specify `LaunchConfigurationName` in your update request, you can't specify `LaunchTemplate` or `MixedInstancesPolicy`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LaunchTemplate **
The launch template and version to use to specify the updates. If you specify `LaunchTemplate` in your update request, you can't specify `LaunchConfigurationName` or `MixedInstancesPolicy`.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object
Required: No

 ** MaxInstanceLifetime **
The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). To clear a previously set value, specify a new value of 0. For more information, see [Replacing Auto Scaling instances based on maximum instance lifetime](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Integer
Required: No

 ** MaxSize **
The maximum size of the Auto Scaling group.
With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above `MaxSize` to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above `MaxSize` by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).
Type: Integer
Required: No

 ** MinSize **
The minimum size of the Auto Scaling group.
Type: Integer
Required: No

 ** MixedInstancesPolicy **
The mixed instances policy. For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) in the *Amazon EC2 Auto Scaling User Guide*.
You can remove the Distribution Segments configuration by specifying `OnDemandBaseCapacity` or `OnDemandPercentageAboveBaseCapacity`. You can also remove it explicitly by specifying an empty list for `DistributionSegments`.
Type: [MixedInstancesPolicy](API_MixedInstancesPolicy.md) object
Required: No

 ** NewInstancesProtectedFromScaleIn **
Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see [Use instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 ** PlacementGroup **
The name of an existing placement group into which to launch your instances. To remove the placement group setting, pass an empty string for `placement-group`. For more information about placement groups, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.
A *cluster* placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ServiceLinkedRoleARN **
The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf. For more information, see [Service-linked roles](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** SkipZonalShiftValidation **
 If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify `true`. For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 **TerminationPolicies.member.N**
A policy or a list of policies that are used to select the instances to terminate. The policies are executed in the order that you list them. For more information, see [Configure termination policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html) in the *Amazon EC2 Auto Scaling User Guide*.
Valid values: `Default` \| `AllocationStrategy` \| `ClosestToNextInstanceHour` \| `NewestInstance` \| `OldestInstance` \| `OldestLaunchConfiguration` \| `OldestLaunchTemplate` \| `arn:aws:lambda:region:account-id:function:my-function:my-alias`
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** VPCZoneIdentifier **
A comma-separated list of subnet IDs for a virtual private cloud (VPC). If you specify `VPCZoneIdentifier` with `AvailabilityZones`, the subnets that you specify must reside in those Availability Zones.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Errors
<a name="API_UpdateAutoScalingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ScalingActivityInProgress **
The operation can't be performed because there are scaling activities in progress.
 ** message **

HTTP Status Code: 400

 ** ServiceLinkedRoleFailure **
The service-linked role is not yet ready for use.
HTTP Status Code: 500

## Examples
<a name="API_UpdateAutoScalingGroup_Examples"></a>

### Example 1: Update the health check settings of an existing Auto Scaling group
<a name="API_UpdateAutoScalingGroup_Example_1"></a>

This example updates the health check settings for the Auto Scaling group `my-asg`.

#### Sample Request
<a name="API_UpdateAutoScalingGroup_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=UpdateAutoScalingGroup
&AutoScalingGroupName=my-asg
&HealthCheckType=ELB
&HealthCheckGracePeriod=300
&Version=2011-01-01
&AUTHPARAMS
```

### Example 2: Update the VPC subnets of an existing Auto Scaling group
<a name="API_UpdateAutoScalingGroup_Example_2"></a>

This example updates the VPC subnets for the Auto Scaling group `my-asg`.

#### Sample Request
<a name="API_UpdateAutoScalingGroup_Example_2_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=UpdateAutoScalingGroup
&AutoScalingGroupName=my-asg
&VPCZoneIdentifier=subnet-057fa0918fEXAMPLE%2Csubnet-610acd08EXAMPLE%2Csubnet-530fc83aEXAMPLE
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_UpdateAutoScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/UpdateAutoScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/UpdateAutoScalingGroup)
