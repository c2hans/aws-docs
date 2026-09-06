---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstancesDistribution.html
---

# InstancesDistribution
<a name="API_InstancesDistribution"></a>

Use this structure to specify how a mixed instances policy distributes capacity across On-Demand, Spot, and supported Capacity Reservation types, and to specify the allocation strategies that are used to fulfill the capacity.

When you define a mixed instances policy, this structure uses default values for unspecified parameters, except for `SpotMaxPrice`. However, we recommend that you review and customize the other parameters as needed and explicitly specify the allocation strategies. For help choosing allocation strategies, see [Allocation strategies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html) in the *Amazon EC2 Auto Scaling User Guide*.

When you modify `SpotAllocationStrategy`, `SpotInstancePools`, or `SpotMaxPrice` in the [UpdateAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_UpdateAutoScalingGroup.html) API call, this update action does not deploy any changes across the running EC2 instances in the group. Your existing Spot Instances continue to run as long as the maximum price for those instances is higher than the current Spot price. When scaling out occurs, Amazon EC2 Auto Scaling launches instances based on the new settings. When scaling in occurs, Amazon EC2 Auto Scaling terminates instances according to the group's termination policies.

## Contents
<a name="API_InstancesDistribution_Contents"></a>

 ** DistributionSegments.member.N **
The Distribution Segments configuration. Each segment contains an ordered list of capacity types to prioritize.
For more information, see [Use Distribution Segments to target multiple capacity types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-distribution-segments.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Array of [DistributionSegment](API_DistributionSegment.md) objects
Required: No

 ** OnDemandAllocationStrategy **
The allocation strategy to apply to your On-Demand Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.
The following lists the valid values:
lowest-price
Uses price to determine which instance types are the highest priority, launching the lowest priced instance types within an Availability Zone first. This is the default value for Auto Scaling groups that specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html).
prioritized
You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling launches your highest priority instance types first. If all your On-Demand capacity cannot be fulfilled using your highest priority instance type, then Amazon EC2 Auto Scaling launches the remaining capacity using the second priority instance type, and so on. This is the default value for Auto Scaling groups that don't specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) and cannot be used for groups that do.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** OnDemandBaseCapacity **
The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances. This base portion is launched first as your group scales.
This number has the same unit of measurement as the group's desired capacity. If you change the default unit of measurement (number of instances) by specifying weighted capacity values in your launch template overrides list, or by changing the default desired capacity type setting of the group, you must specify this number using the same unit of measurement.
Default: 0
An update to this setting means a gradual replacement of instances to adjust the current On-Demand Instance levels. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the previous ones.
Type: Integer
Required: No

 ** OnDemandPercentageAboveBaseCapacity **
Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond `OnDemandBaseCapacity`. Expressed as a number (for example, 20 specifies 20% On-Demand Instances, 80% Spot Instances). If set to 100, only On-Demand Instances are used.
Default: 100
An update to this setting means a gradual replacement of instances to adjust the current On-Demand and Spot Instance levels for your additional capacity higher than the base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the previous ones.
Type: Integer
Required: No

 ** SpotAllocationStrategy **
The allocation strategy to apply to your Spot Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.
The following lists the valid values:
capacity-optimized
Requests Spot Instances using pools that are optimally chosen based on the available Spot capacity. This strategy has the lowest risk of interruption. To give certain instance types a higher chance of launching first, use `capacity-optimized-prioritized`.
capacity-optimized-prioritized
You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling honors the instance type priorities on a best effort basis but optimizes for capacity first. Note that if the On-Demand allocation strategy is set to `prioritized`, the same priority is applied when fulfilling On-Demand capacity. This is not a valid value for Auto Scaling groups that specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html).
lowest-price
Requests Spot Instances using the lowest priced pools within an Availability Zone, across the number of Spot pools that you specify for the `SpotInstancePools` property. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. This is the default value, but it might lead to high interruption rates because this strategy only considers instance price and not available capacity.
price-capacity-optimized (recommended)
The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** SpotInstancePools **
The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the overrides. Valid only when the `SpotAllocationStrategy` is `lowest-price`. Value must be in the range of 1–20.
Default: 2
Type: Integer
Required: No

 ** SpotMaxPrice **
The maximum price per unit hour that you are willing to pay for a Spot Instance. If your maximum price is lower than the Spot price for the instance types that you selected, your Spot Instances are not launched. We do not recommend specifying a maximum price because it can lead to increased interruptions. When Spot Instances launch, you pay the current Spot price. To remove a maximum price that you previously set, include the property but specify an empty string ("") for the value.
If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify one.
Valid Range: Minimum value of 0.001
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_InstancesDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/InstancesDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/InstancesDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/InstancesDistribution)
