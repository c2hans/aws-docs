---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AutoScalingGroup.html
---

# AutoScalingGroup
<a name="API_AutoScalingGroup"></a>

Describes an Auto Scaling group.

## Contents
<a name="API_AutoScalingGroup_Contents"></a>

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** AvailabilityZones.member.N **
One or more Availability Zones for the Auto Scaling group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** CreatedTime **
The date and time the Auto Scaling group was created.
Type: Timestamp
Required: Yes

 ** DefaultCooldown **
The duration of the default cooldown period, in seconds, for the Auto Scaling group.
Type: Integer
Required: Yes

 ** DesiredCapacity **
The desired size of the Auto Scaling group.
Type: Integer
Required: Yes

 ** HealthCheckType **
One or more comma-separated health check types for the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** MaxSize **
The maximum size of the Auto Scaling group.
Type: Integer
Required: Yes

 ** MinSize **
The minimum size of the Auto Scaling group.
Type: Integer
Required: Yes

 ** AutoScalingGroupARN **
The Amazon Resource Name (ARN) of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AvailabilityZoneDistribution **
The EC2 instance capacity distribution across Availability Zones for the Auto Scaling group.
Type: [AvailabilityZoneDistribution](API_AvailabilityZoneDistribution.md) object
Required: No

 ** AvailabilityZoneIds.member.N **
 The Availability Zone IDs where the Auto Scaling group can launch instances.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AvailabilityZoneImpairmentPolicy **
The Availability Zone impairment policy for the Auto Scaling group.
Type: [AvailabilityZoneImpairmentPolicy](API_AvailabilityZoneImpairmentPolicy.md) object
Required: No

 ** CapacityRebalance **
Indicates whether Capacity Rebalancing is enabled.
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

 ** DefaultInstanceWarmup **
The duration of the default EC2 instance warmup time, in seconds, for the Auto Scaling group.
Type: Integer
Required: No

 ** DeletionProtection **
The deletion protection setting for the Auto Scaling group.
Type: String
Valid Values: `none | prevent-force-deletion | prevent-all-deletion`
Required: No

 ** DesiredCapacityType **
The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports `DesiredCapacityType` for attribute-based instance type selection only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** EnabledMetrics.member.N **
The metrics enabled for the Auto Scaling group.
Type: Array of [EnabledMetric](API_EnabledMetric.md) objects
Required: No

 ** HealthCheckGracePeriod **
The duration of the health check grace period, in seconds, for the Auto Scaling group.
Type: Integer
Required: No

 ** InstanceLifecyclePolicy **
The instance lifecycle policy for the Auto Scaling group.
Type: [InstanceLifecyclePolicy](API_InstanceLifecyclePolicy.md) object
Required: No

 ** InstanceMaintenancePolicy **
An instance maintenance policy.
Type: [InstanceMaintenancePolicy](API_InstanceMaintenancePolicy.md) object
Required: No

 ** Instances.member.N **
The EC2 instances associated with the Auto Scaling group.
Type: Array of [Instance](API_Instance.md) objects
Required: No

 ** LaunchConfigurationName **
The name of the associated launch configuration for the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LaunchTemplate **
The launch template for the Auto Scaling group.
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object
Required: No

 ** LoadBalancerNames.member.N **
One or more load balancers associated with the group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MaxInstanceLifetime **
The maximum amount of time, in seconds, that an EC2 instance can be in service for the Auto Scaling group.
Type: Integer
Required: No

 ** MixedInstancesPolicy **
The mixed instances policy for the group.
Type: [MixedInstancesPolicy](API_MixedInstancesPolicy.md) object
Required: No

 ** NewInstancesProtectedFromScaleIn **
Indicates whether newly launched EC2 instances are protected from termination when scaling in for the Auto Scaling group.
 For more information about preventing instances from terminating on scale in, see [Use instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 ** Operator **
The entity that manages the Auto Scaling group, if applicable. When set, only the designated operator can make changes to the group configuration.
Type: [Operator](API_Operator.md) object
Required: No

 ** PlacementGroup **
The name of the placement group into which to launch EC2 instances for the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** PredictedCapacity **
The predicted capacity of the group when it has a predictive scaling policy.
Type: Integer
Required: No

 ** ServiceLinkedRoleARN **
The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Status **
The current state of the Auto Scaling group when the [DeleteAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteAutoScalingGroup.html) operation is in progress.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** SuspendedProcesses.member.N **
The suspended processes associated with the Auto Scaling group.
Type: Array of [SuspendedProcess](API_SuspendedProcess.md) objects
Required: No

 ** Tags.member.N **
The tags for the Auto Scaling group.
Type: Array of [TagDescription](API_TagDescription.md) objects
Required: No

 ** TargetGroupARNs.member.N **
The Amazon Resource Names (ARN) of the target groups for your load balancer.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** TerminationPolicies.member.N **
The termination policies for the Auto Scaling group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** TrafficSources.member.N **
The traffic sources associated with this Auto Scaling group.
Type: Array of [TrafficSourceIdentifier](API_TrafficSourceIdentifier.md) objects
Required: No

 ** VPCZoneIdentifier **
One or more comma-separated subnet IDs for the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** WarmPoolConfiguration **
The warm pool for the group.
Type: [WarmPoolConfiguration](API_WarmPoolConfiguration.md) object
Required: No

 ** WarmPoolSize **
The current size of the warm pool.
Type: Integer
Required: No

## See Also
<a name="API_AutoScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AutoScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AutoScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AutoScalingGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
