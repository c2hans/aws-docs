---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedCapacityOptionsRequest.html
---

# ReservedCapacityOptionsRequest
<a name="API_ReservedCapacityOptionsRequest"></a>

Defines EC2 Fleet preferences for utilizing reserved capacity when `DefaultTargetCapacityType` is set to `reserved-capacity`. EC2 Fleet can fulfill reserved capacity using On-Demand Capacity Reservations, Capacity Blocks for ML, and interruptible Capacity Reservations.

**Note**
This configuration can only be used if the EC2 Fleet is of type `instant`.

When you specify `ReservedCapacityOptions`, you must also set `DefaultTargetCapacityType` to `reserved-capacity` in the `TargetCapacitySpecification`.

For more information about interruptible Capacity Reservations, see [Launch instances into an interruptible Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-launch-instances-interruptible-cr-walkthrough.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_ReservedCapacityOptionsRequest_Contents"></a>

 ** AllocationStrategy **
The strategy that determines the order in which EC2 Fleet launches instances across the reservation types that you specify. The only supported value is `prioritized`, which launches instances in the priority order that you specify in your launch template overrides. If you don't specify an allocation strategy, instances are launched in a random order.
Type: String
Valid Values: `prioritized`
Required: No

 ** CapacityReservationTarget **
The Capacity Reservations or Capacity Reservation Resource Groups to use for fulfilling the EC2 Fleet request. You can specify Capacity Reservation IDs or a Capacity Reservation Resource Group ARN, but not both.
Type: [FleetCapacityReservationTargetRequest](API_FleetCapacityReservationTargetRequest.md) object
Required: No

 ** ReservationType.N **
The types of Capacity Reservations to use for fulfilling the EC2 Fleet request. This is an ordered list: EC2 Fleet attempts to launch instances into each Capacity Reservation type in the order that you specify them before moving on to the next type.
Type: Array of strings
Valid Values: `on-demand-capacity-reservation | capacity-block | interruptible-capacity-reservation`
Required: No

 ** ReservedCapacityFallbackOptions **
The fallback behavior for the EC2 Fleet when there is not enough reserved capacity available to meet the target capacity. This member takes a `ReservedCapacityFallbackOptionsRequest` structure, in which you set `MarketTypes` to the instance purchasing options to fall back to.
Type: [ReservedCapacityFallbackOptionsRequest](API_ReservedCapacityFallbackOptionsRequest.md) object
Required: No

## See Also
<a name="API_ReservedCapacityOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedCapacityOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedCapacityOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedCapacityOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
