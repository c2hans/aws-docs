---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotOptionsRequest.html
---

# SpotOptionsRequest
<a name="API_SpotOptionsRequest"></a>

Describes the configuration of Spot Instances in an EC2 Fleet request.

## Contents
<a name="API_SpotOptionsRequest_Contents"></a>

 ** AllocationStrategy **
The strategy that determines how to allocate the target Spot Instance capacity across the Spot Instance pools specified by the EC2 Fleet launch configuration. For more information, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html) in the *Amazon EC2 User Guide*.
price-capacity-optimized (recommended)
EC2 Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. EC2 Fleet then requests Spot Instances from the lowest priced of these pools.
capacity-optimized
EC2 Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. To give certain instance types a higher chance of launching first, use `capacity-optimized-prioritized`. Set a priority for each instance type by using the `Priority` parameter for `LaunchTemplateOverrides`. You can assign the same priority to different `LaunchTemplateOverrides`. EC2 implements the priorities on a best-effort basis, but optimizes for capacity first. `capacity-optimized-prioritized` is supported only if your EC2 Fleet uses a launch template. Note that if the On-Demand `AllocationStrategy` is set to `prioritized`, the same priority is applied when fulfilling On-Demand capacity.
diversified
EC2 Fleet requests instances from all of the Spot Instance pools that you specify.
lowest-price (not recommended)
We don't recommend the `lowest-price` allocation strategy because it has the highest risk of interruption for your Spot Instances.
EC2 Fleet requests instances from the lowest priced Spot Instance pool that has available capacity. If the lowest priced pool doesn't have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, EC2 Fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.
Default: `lowest-price`
Type: String
Valid Values: `lowest-price | diversified | capacity-optimized | capacity-optimized-prioritized | price-capacity-optimized`
Required: No

 ** InstanceInterruptionBehavior **
The behavior when a Spot Instance is interrupted.
Default: `terminate`
Type: String
Valid Values: `hibernate | stop | terminate`
Required: No

 ** InstancePoolsToUseCount **
The number of Spot pools across which to allocate your target Spot capacity. Supported only when Spot `AllocationStrategy` is set to `lowest-price`. EC2 Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.
Note that EC2 Fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, EC2 Fleet will continue to fulfill your request by drawing from the next cheapest pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.
Type: Integer
Required: No

 ** MaintenanceStrategies **
The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.
Type: [FleetSpotMaintenanceStrategiesRequest](API_FleetSpotMaintenanceStrategiesRequest.md) object
Required: No

 ** MaxTotalPrice **
The maximum amount per hour for Spot Instances that you're willing to pay. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.
If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.
If your fleet includes T instances that are configured as `unlimited`, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `MaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `MaxTotalPrice`. For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** MinTargetCapacity **
The minimum target capacity for Spot Instances in the fleet. If this minimum capacity isn't reached, no instances are launched.
Constraints: Maximum value of `1000`. Supported only for fleets of type `instant`.
At least one of the following must be specified: `SingleAvailabilityZone` \| `SingleInstanceType`
Type: Integer
Required: No

 ** SingleAvailabilityZone **
Indicates that the fleet launches all Spot Instances into a single Availability Zone.
Supported only for fleets of type `instant`.
Type: Boolean
Required: No

 ** SingleInstanceType **
Indicates that the fleet uses a single instance type to launch all Spot Instances in the fleet.
Supported only for fleets of type `instant`.
Type: Boolean
Required: No

## See Also
<a name="API_SpotOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SpotOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SpotOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SpotOptionsRequest)
