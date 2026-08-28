---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html
---

# CreateAutoScalingGroup
<a name="API_CreateAutoScalingGroup"></a>

 **We strongly recommend using a launch template when calling this operation to ensure full functionality for Amazon EC2 Auto Scaling and Amazon EC2.**

Creates an Auto Scaling group with the specified name and attributes.

If you exceed your maximum limit of Auto Scaling groups, the call fails. To query this limit, call the [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html) API. For information about updating this limit, see [Quotas for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html) in the *Amazon EC2 Auto Scaling User Guide*.

If you're new to Amazon EC2 Auto Scaling, see the introductory tutorials in [Get started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.

Every Auto Scaling group has three size properties (`DesiredCapacity`, `MaxSize`, and `MinSize`). Usually, you set these sizes based on a specific number of instances. However, if you configure a mixed instances policy that defines weights for the instance types, you must specify these sizes with the same units that you use for weighting instances.

## Request Parameters
<a name="API_CreateAutoScalingGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group. This name must be unique per Region per account.
The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters.
You cannot use a colon (:) in the name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** AvailabilityZoneDistribution **
The instance capacity distribution across Availability Zones.
Type: [AvailabilityZoneDistribution](API_AvailabilityZoneDistribution.md) object
Required: No

 **AvailabilityZoneIds.member.N**
 A list of Availability Zone IDs where the Auto Scaling group can launch instances. You cannot specify both AvailabilityZones and AvailabilityZoneIds in the same request.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AvailabilityZoneImpairmentPolicy **
 The policy for Availability Zone impairment.
Type: [AvailabilityZoneImpairmentPolicy](API_AvailabilityZoneImpairmentPolicy.md) object
Required: No

 **AvailabilityZones.member.N**
A list of Availability Zones where instances in the Auto Scaling group can be created. Used for launching into the default VPC subnet in each Availability Zone when not using the `VPCZoneIdentifier` property, or for attaching a network interface when an existing network interface ID is specified in a launch template.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** CapacityRebalance **
Indicates whether Capacity Rebalancing is enabled. Otherwise, Capacity Rebalancing is disabled. When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of interruption. After launching a new instance, it then terminates an old instance. For more information, see [Use Capacity Rebalancing to handle Amazon EC2 Spot Interruptions](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html) in the in the *Amazon EC2 Auto Scaling User Guide*.
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
Default: `300` seconds
Type: Integer
Required: No

 ** DefaultInstanceWarmup **
The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the `InService` state.
During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see [Set the default instance warmup for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html) in the *Amazon EC2 Auto Scaling User Guide*.
To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, *even if it is set to 0 seconds*. To remove a value that you previously set, include the property but specify `-1` for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of `0` or other nominal value.
Default: None
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
The desired capacity is the initial capacity of the Auto Scaling group at the time of its creation and the capacity it attempts to maintain. It can scale beyond this capacity if you configure auto scaling. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity, the default is the minimum size of the group.
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
Default: `0` seconds
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

 ** InstanceId **
The ID of the instance used to base the launch configuration on. If specified, Amazon EC2 Auto Scaling uses the configuration values from the specified instance to create a new launch configuration. To get the instance ID, use the Amazon EC2 [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) API operation. For more information, see [Create an Auto Scaling group using parameters from an existing instance](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-from-instance.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** InstanceLifecyclePolicy **
 The instance lifecycle policy for the Auto Scaling group. This policy controls instance behavior when an instance transitions through its lifecycle states. Configure retention triggers to specify when instances should move to a `Retained` state instead of automatic termination.
For more information, see [ Control instance retention with instance lifecycle policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.
Instances in a Retained state will continue to incur standard EC2 charges until terminated.
Type: [InstanceLifecyclePolicy](API_InstanceLifecyclePolicy.md) object
Required: No

 ** InstanceMaintenancePolicy **
An instance maintenance policy. For more information, see [Set instance maintenance policy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: [InstanceMaintenancePolicy](API_InstanceMaintenancePolicy.md) object
Required: No

 ** LaunchConfigurationName **
The name of the launch configuration to use to launch instances.
Conditional: You must specify either a launch template (`LaunchTemplate` or `MixedInstancesPolicy`) or a launch configuration (`LaunchConfigurationName` or `InstanceId`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LaunchTemplate **
Information used to specify the launch template and version to use to launch instances.
Conditional: You must specify either a launch template (`LaunchTemplate` or `MixedInstancesPolicy`) or a launch configuration (`LaunchConfigurationName` or `InstanceId`).
The launch template that is specified must be configured for use with an Auto Scaling group. For more information, see [Create a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object
Required: No

 **LifecycleHookSpecificationList.member.N**
One or more lifecycle hooks to add to the Auto Scaling group before instances are launched.
Type: Array of [LifecycleHookSpecification](API_LifecycleHookSpecification.md) objects
Required: No

 **LoadBalancerNames.member.N**
A list of Classic Load Balancers associated with this Auto Scaling group. For Application Load Balancers, Network Load Balancers, and Gateway Load Balancers, specify the `TargetGroupARNs` property instead.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MaxInstanceLifetime **
The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). For more information, see [Replace Auto Scaling instances based on maximum instance lifetime](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Integer
Required: No

 ** MaxSize **
The maximum size of the group.
With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above `MaxSize` to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above `MaxSize` by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).
Type: Integer
Required: Yes

 ** MinSize **
The minimum size of the group.
Type: Integer
Required: Yes

 ** MixedInstancesPolicy **
The mixed instances policy.
The policy includes properties that define how the Auto Scaling group distributes capacity across purchase options and how it allocates instance types to fulfill the capacity. The policy also includes properties that specify the instance configuration, including the launch template and instance types. The policy can also include a weight for each instance type and different launch templates for certain instance types. For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) in the *Amazon EC2 Auto Scaling User Guide*. To learn how to prioritize multiple capacity types, see [Use Distribution Segments to target multiple capacity types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-distribution-segments.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: [MixedInstancesPolicy](API_MixedInstancesPolicy.md) object
Required: No

 ** NewInstancesProtectedFromScaleIn **
Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see [Use instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 ** Operator **
The entity that manages the Auto Scaling group. If you specify this parameter, Amazon EC2 Auto Scaling passes the operator identity to EC2 for instance launches and only allows the designated operator to make changes to the Auto Scaling group. All mutating API calls from non-operator callers are rejected with an `AccessDenied` exception.
Type: [Operator](API_Operator.md) object
Required: No

 ** PlacementGroup **
The name of the placement group into which to launch your instances. For more information, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.
A *cluster* placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ServiceLinkedRoleARN **
The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS service on your behalf. By default, Amazon EC2 Auto Scaling uses a service-linked role named `AWSServiceRoleForAutoScaling`, which it creates if it does not exist. For more information, see [Service-linked roles](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** SkipZonalShiftValidation **
 If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify `true`. For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 **Tags.member.N**
One or more tags. You can tag your Auto Scaling group and propagate the tags to the Amazon EC2 instances it launches. Tags are not propagated to Amazon EBS volumes. To add tags to Amazon EBS volumes, specify the tags in a launch template but use caution. If the launch template specifies an instance tag with a key that is also specified for the Auto Scaling group, Amazon EC2 Auto Scaling overrides the value of that instance tag with the value specified by the Auto Scaling group. For more information, see [Tag Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 **TargetGroupARNs.member.N**
The Amazon Resource Names (ARN) of the Elastic Load Balancing target groups to associate with the Auto Scaling group. Instances are registered as targets with the target groups. The target groups receive incoming traffic and route requests to one or more registered targets. For more information, see [Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **TerminationPolicies.member.N**
A policy or a list of policies that are used to select the instance to terminate. These policies are executed in the order that you list them. For more information, see [Configure termination policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html) in the *Amazon EC2 Auto Scaling User Guide*.
Valid values: `Default` \| `AllocationStrategy` \| `ClosestToNextInstanceHour` \| `NewestInstance` \| `OldestInstance` \| `OldestLaunchConfiguration` \| `OldestLaunchTemplate` \| `arn:aws:lambda:region:account-id:function:my-function:my-alias`
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **TrafficSources.member.N**
The list of traffic sources to attach to this Auto Scaling group. You can use any of the following as traffic sources for an Auto Scaling group: Classic Load Balancer, Application Load Balancer, Gateway Load Balancer, Network Load Balancer, and VPC Lattice.
Type: Array of [TrafficSourceIdentifier](API_TrafficSourceIdentifier.md) objects
Required: No

 ** VPCZoneIdentifier **
A comma-separated list of subnet IDs for a virtual private cloud (VPC) where instances in the Auto Scaling group can be created. If you specify `VPCZoneIdentifier` with `AvailabilityZones`, the subnets that you specify must reside in those Availability Zones.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Errors
<a name="API_CreateAutoScalingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
You already have an Auto Scaling group or launch configuration with this name.
 ** message **

HTTP Status Code: 400

 ** LimitExceeded **
You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html).
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ServiceLinkedRoleFailure **
The service-linked role is not yet ready for use.
HTTP Status Code: 500

## Examples
<a name="API_CreateAutoScalingGroup_Examples"></a>

### Example
<a name="API_CreateAutoScalingGroup_Example_1"></a>

This example illustrates one usage of CreateAutoScalingGroup.

#### Sample Request
<a name="API_CreateAutoScalingGroup_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=CreateAutoScalingGroup
&AutoScalingGroupName=my-asg
&VPCZoneIdentifier=subnet-057fa0918fEXAMPLE%2Csubnet-610acd08EXAMPLE
&MinSize=2
&MaxSize=10
&DesiredCapacity=2
&LoadBalancerNames.member.1=my-loadbalancer
&HealthCheckType=ELB
&HealthCheckGracePeriod=120
&LaunchConfigurationName=my-lc
&MaxInstanceLifetime=2592000
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateAutoScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/CreateAutoScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CreateAutoScalingGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
