---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedCapacityOptions.html
---

# ReservedCapacityOptions
<a name="API_ReservedCapacityOptions"></a>

Defines EC2 Fleet preferences for utilizing reserved capacity when `DefaultTargetCapacityType` is set to `reserved-capacity`. EC2 Fleet can fulfill reserved capacity using On-Demand Capacity Reservations, Capacity Blocks for ML, and interruptible Capacity Reservations.

## Contents
<a name="API_ReservedCapacityOptions_Contents"></a>

 ** allocationStrategy **
The strategy that determines the order in which EC2 Fleet launches instances across the reservation types that you specify. The only supported value is `prioritized`, which launches instances in the priority order that you specify in your launch template overrides. If you don't specify an allocation strategy, instances are launched in a random order.
Type: String
Valid Values: `prioritized`
Required: No

 ** ReservationTypeSet.N **
The types of Capacity Reservations used for fulfilling the EC2 Fleet request.
Type: Array of strings
Valid Values: `on-demand-capacity-reservation | capacity-block | interruptible-capacity-reservation`
Required: No

 ** reservedCapacityFallbackOptions **
The fallback behavior for the EC2 Fleet when there is not enough reserved capacity available to meet the target capacity.
Type: [ReservedCapacityFallbackOptions](API_ReservedCapacityFallbackOptions.md) object
Required: No

## See Also
<a name="API_ReservedCapacityOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedCapacityOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedCapacityOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedCapacityOptions)
