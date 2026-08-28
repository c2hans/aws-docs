---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetRequestConfigData.html
---

# SpotFleetRequestConfigData
<a name="API_SpotFleetRequestConfigData"></a>

Describes the configuration of a Spot Fleet request.

## Contents
<a name="API_SpotFleetRequestConfigData_Contents"></a>

 ** IamFleetRole ** (request), ** iamFleetRole ** (response)
The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that grants the Spot Fleet the permission to request, launch, terminate, and tag instances on your behalf. For more information, see [Spot Fleet prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-requests.html#spot-fleet-prerequisites) in the *Amazon EC2 User Guide*. Spot Fleet can terminate Spot Instances on your behalf when you cancel its Spot Fleet request using [CancelSpotFleetRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests) or when the Spot Fleet request expires, if you set `TerminateInstancesWithExpiration`.
Type: String
Required: Yes

 ** TargetCapacity ** (request), ** targetCapacity ** (response)
The number of units to request for the Spot Fleet. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is `maintain`, you can specify a target capacity of 0 and add capacity later.
Type: Integer
Required: Yes

 ** AllocationStrategy ** (request), ** allocationStrategy ** (response)
The strategy that determines how to allocate the target Spot Instance capacity across the Spot Instance pools specified by the Spot Fleet launch configuration. For more information, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html) in the *Amazon EC2 User Guide*.
priceCapacityOptimized (recommended)
Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. Spot Fleet then requests Spot Instances from the lowest priced of these pools.
capacityOptimized
Spot Fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. To give certain instance types a higher chance of launching first, use `capacityOptimizedPrioritized`. Set a priority for each instance type by using the `Priority` parameter for `LaunchTemplateOverrides`. You can assign the same priority to different `LaunchTemplateOverrides`. EC2 implements the priorities on a best-effort basis, but optimizes for capacity first. `capacityOptimizedPrioritized` is supported only if your Spot Fleet uses a launch template. Note that if the `OnDemandAllocationStrategy` is set to `prioritized`, the same priority is applied when fulfilling On-Demand capacity.
diversified
Spot Fleet requests instances from all of the Spot Instance pools that you specify.
lowestPrice (not recommended)
We don't recommend the `lowestPrice` allocation strategy because it has the highest risk of interruption for your Spot Instances.
Spot Fleet requests instances from the lowest priced Spot Instance pool that has available capacity. If the lowest priced pool doesn't have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, Spot Fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.
Default: `lowestPrice`
Type: String
Valid Values: `lowestPrice | diversified | capacityOptimized | capacityOptimizedPrioritized | priceCapacityOptimized`
Required: No

 ** ClientToken ** (request), ** clientToken ** (response)
A unique, case-sensitive identifier that you provide to ensure the idempotency of your listings. This helps to avoid duplicate listings. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 ** Context ** (request), ** context ** (response)
Reserved.
Type: String
Required: No

 ** ExcessCapacityTerminationPolicy ** (request), ** excessCapacityTerminationPolicy ** (response)
Indicates whether running instances should be terminated if you decrease the target capacity of the Spot Fleet request below the current size of the Spot Fleet.
Supported only for fleets of type `maintain`.
Type: String
Valid Values: `noTermination | default`
Required: No

 ** FulfilledCapacity ** (request), ** fulfilledCapacity ** (response)
The number of units fulfilled by this request compared to the set target capacity. You cannot set this value.
Type: Double
Required: No

 ** InstanceInterruptionBehavior ** (request), ** instanceInterruptionBehavior ** (response)
The behavior when a Spot Instance is interrupted. The default is `terminate`.
Type: String
Valid Values: `hibernate | stop | terminate`
Required: No

 ** InstancePoolsToUseCount ** (request), ** instancePoolsToUseCount ** (response)
The number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot **AllocationStrategy** is set to `lowest-price`. Spot Fleet selects the cheapest Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.
Note that Spot Fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, Spot Fleet will continue to fulfill your request by drawing from the next cheapest pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.
Type: Integer
Required: No

 ** LaunchSpecifications.N **
The launch specifications for the Spot Fleet request. If you specify `LaunchSpecifications`, you can't specify `LaunchTemplateConfigs`. If you include On-Demand capacity in your request, you must use `LaunchTemplateConfigs`.
If an AMI specified in a launch specification is deregistered or disabled, no new instances can be launched from the AMI. For fleets of type `maintain`, the target capacity will not be maintained.
Type: Array of [SpotFleetLaunchSpecification](API_SpotFleetLaunchSpecification.md) objects
Required: No

 ** LaunchTemplateConfigs.N **
The launch template and overrides. If you specify `LaunchTemplateConfigs`, you can't specify `LaunchSpecifications`. If you include On-Demand capacity in your request, you must use `LaunchTemplateConfigs`.
Type: Array of [LaunchTemplateConfig](API_LaunchTemplateConfig.md) objects
Required: No

 ** LoadBalancersConfig ** (request), ** loadBalancersConfig ** (response)
One or more Classic Load Balancers and target groups to attach to the Spot Fleet request. Spot Fleet registers the running Spot Instances with the specified Classic Load Balancers and target groups.
With Network Load Balancers, Spot Fleet cannot register instances that have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1.
Type: [LoadBalancersConfig](API_LoadBalancersConfig.md) object
Required: No

 ** OnDemandAllocationStrategy ** (request), ** onDemandAllocationStrategy ** (response)
The order of the launch template overrides to use in fulfilling On-Demand capacity. If you specify `lowestPrice`, Spot Fleet uses price to determine the order, launching the lowest price first. If you specify `prioritized`, Spot Fleet uses the priority that you assign to each Spot Fleet launch template override, launching the highest priority first. If you do not specify a value, Spot Fleet defaults to `lowestPrice`.
Type: String
Valid Values: `lowestPrice | prioritized`
Required: No

 ** OnDemandFulfilledCapacity ** (request), ** onDemandFulfilledCapacity ** (response)
The number of On-Demand units fulfilled by this request compared to the set target On-Demand capacity.
Type: Double
Required: No

 ** OnDemandMaxTotalPrice ** (request), ** onDemandMaxTotalPrice ** (response)
The maximum amount per hour for On-Demand Instances that you're willing to pay. You can use the `onDemandMaxTotalPrice` parameter, the `spotMaxTotalPrice` parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity.
If your fleet includes T instances that are configured as `unlimited`, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `onDemandMaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `onDemandMaxTotalPrice`. For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** OnDemandTargetCapacity ** (request), ** onDemandTargetCapacity ** (response)
The number of On-Demand units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is `maintain`, you can specify a target capacity of 0 and add capacity later.
Type: Integer
Required: No

 ** ReplaceUnhealthyInstances ** (request), ** replaceUnhealthyInstances ** (response)
Indicates whether Spot Fleet should replace unhealthy instances.
Type: Boolean
Required: No

 ** SpotMaintenanceStrategies ** (request), ** spotMaintenanceStrategies ** (response)
The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.
Type: [SpotMaintenanceStrategies](API_SpotMaintenanceStrategies.md) object
Required: No

 ** SpotMaxTotalPrice ** (request), ** spotMaxTotalPrice ** (response)
The maximum amount per hour for Spot Instances that you're willing to pay. You can use the `spotMaxTotalPrice` parameter, the `onDemandMaxTotalPrice` parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, Spot Fleet will launch instances until it reaches the maximum amount you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity.
If your fleet includes T instances that are configured as `unlimited`, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `spotMaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `spotMaxTotalPrice`. For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** SpotPrice ** (request), ** spotPrice ** (response)
The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.
If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.
Type: String
Required: No

 ** TagSpecification.N **
The key-value pair for tagging the Spot Fleet request on creation. The value for `ResourceType` must be `spot-fleet-request`, otherwise the Spot Fleet request fails. To tag instances at launch, specify the tags in the [launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template) (valid only if you use `LaunchTemplateConfigs`) or in the ` [SpotFleetTagSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetTagSpecification.html) ` (valid only if you use `LaunchSpecifications`). For information about tagging after launch, see [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources).
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 ** TargetCapacityUnitType ** (request), ** targetCapacityUnitType ** (response)
The unit for the target capacity. You can specify this parameter only when using attribute-based instance type selection.
Default: `units` (the number of instances)
Type: String
Valid Values: `vcpu | memory-mib | units`
Required: No

 ** TerminateInstancesWithExpiration ** (request), ** terminateInstancesWithExpiration ** (response)
Indicates whether running Spot Instances are terminated when the Spot Fleet request expires.
Type: Boolean
Required: No

 ** Type ** (request), ** type ** (response)
The type of request. Indicates whether the Spot Fleet only requests the target capacity or also attempts to maintain it. When this value is `request`, the Spot Fleet only places the required requests. It does not attempt to replenish Spot Instances if capacity is diminished, nor does it submit requests in alternative Spot pools if capacity is not available. When this value is `maintain`, the Spot Fleet maintains the target capacity. The Spot Fleet places the required requests to meet capacity and automatically replenishes any interrupted instances. Default: `maintain`. `instant` is listed but is not used by Spot Fleet.
Type: String
Valid Values: `request | maintain | instant`
Required: No

 ** ValidFrom ** (request), ** validFrom ** (response)
The start date and time of the request, in UTC format (*YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z). By default, Amazon EC2 starts fulfilling the request immediately.
Type: Timestamp
Required: No

 ** ValidUntil ** (request), ** validUntil ** (response)
The end date and time of the request, in UTC format (*YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z). After the end date and time, no new Spot Instance requests are placed or able to fulfill the request. If no value is specified, the Spot Fleet request remains until you cancel it.
Type: Timestamp
Required: No

## See Also
<a name="API_SpotFleetRequestConfigData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SpotFleetRequestConfigData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SpotFleetRequestConfigData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SpotFleetRequestConfigData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
