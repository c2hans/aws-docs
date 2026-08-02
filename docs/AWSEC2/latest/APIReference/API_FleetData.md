---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetData.html
---

# FleetData
<a name="API_FleetData"></a>

Describes an EC2 Fleet.

## Contents
<a name="API_FleetData_Contents"></a>

 ** activityStatus **
The progress of the EC2 Fleet.
For fleets of type `instant`, the status is `fulfilled` after all requests are placed, regardless of whether target capacity is met (this is the only possible status for `instant` fleets).
For fleets of type `request` or `maintain`, the status is `pending_fulfillment` after all requests are placed, `fulfilled` when the fleet size meets or exceeds target capacity, `pending_termination` while instances are terminating when fleet size is decreased, and `error` if there's an error.
Type: String
Valid Values: `error | pending_fulfillment | pending_termination | fulfilled`
Required: No

 ** clientToken **
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Constraints: Maximum 64 ASCII characters
Type: String
Required: No

 ** context **
Reserved.
Type: String
Required: No

 ** createTime **
The creation date and time of the EC2 Fleet.
Type: Timestamp
Required: No

 ** ErrorSet.N **
Information about the instances that could not be launched by the fleet. Valid only when **Type** is set to `instant`.
Type: Array of [DescribeFleetError](API_DescribeFleetError.md) objects
Required: No

 ** excessCapacityTerminationPolicy **
Indicates whether running instances should be terminated if the target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.
Supported only for fleets of type `maintain`.
Type: String
Valid Values: `no-termination | termination`
Required: No

 ** fleetId **
The ID of the EC2 Fleet.
Type: String
Required: No

 ** FleetInstanceSet.N **
Information about the instances that were launched by the fleet. Valid only when **Type** is set to `instant`.
Type: Array of [DescribeFleetsInstances](API_DescribeFleetsInstances.md) objects
Required: No

 ** fleetState **
The state of the EC2 Fleet.
Type: String
Valid Values: `submitted | active | deleted | failed | deleted_running | deleted_terminating | modifying`
Required: No

 ** fulfilledCapacity **
The number of units fulfilled by this request compared to the set target capacity.
Type: Double
Required: No

 ** fulfilledOnDemandCapacity **
The number of units fulfilled by this request compared to the set target On-Demand capacity.
Type: Double
Required: No

 ** LaunchTemplateConfigs.N **
The launch template and overrides.
Type: Array of [FleetLaunchTemplateConfig](API_FleetLaunchTemplateConfig.md) objects
Required: No

 ** onDemandOptions **
The allocation strategy of On-Demand Instances in an EC2 Fleet.
Type: [OnDemandOptions](API_OnDemandOptions.md) object
Required: No

 ** replaceUnhealthyInstances **
Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type `maintain`. For more information, see [EC2 Fleet health checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks) in the *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 ** reservedCapacityOptions **
Defines EC2 Fleet preferences for utilizing reserved capacity when DefaultTargetCapacityType is set to `reserved-capacity`.
Type: [ReservedCapacityOptions](API_ReservedCapacityOptions.md) object
Required: No

 ** spotOptions **
The configuration of Spot Instances in an EC2 Fleet.
Type: [SpotOptions](API_SpotOptions.md) object
Required: No

 ** TagSet.N **
The tags for an EC2 Fleet resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** targetCapacitySpecification **
The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is `maintain`, you can specify a target capacity of 0 and add capacity later.
Type: [TargetCapacitySpecification](API_TargetCapacitySpecification.md) object
Required: No

 ** terminateInstancesWithExpiration **
Indicates whether running instances should be terminated when the EC2 Fleet expires.
Type: Boolean
Required: No

 ** type **
The type of request. Indicates whether the EC2 Fleet only `requests` the target capacity, or also attempts to `maintain` it. If you request a certain target capacity, EC2 Fleet only places the required requests; it does not attempt to replenish instances if capacity is diminished, and it does not submit requests in alternative capacity pools if capacity is unavailable. To maintain a certain target capacity, EC2 Fleet places the required requests to meet this target capacity. It also automatically replenishes any interrupted Spot Instances. Default: `maintain`.
Type: String
Valid Values: `request | maintain | instant`
Required: No

 ** validFrom **
The start date and time of the request, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z). The default is to start fulfilling the request immediately.
Type: Timestamp
Required: No

 ** validUntil **
The end date and time of the request, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z). At this point, no new instance requests are placed or able to fulfill the request. The default end date is 7 days from the current date.
Type: Timestamp
Required: No

## See Also
<a name="API_FleetData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FleetData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FleetData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FleetData)
