---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_OnDemandOptionsRequest.html
---

# OnDemandOptionsRequest
<a name="API_OnDemandOptionsRequest"></a>

Describes the configuration of On-Demand Instances in an EC2 Fleet.

## Contents
<a name="API_OnDemandOptionsRequest_Contents"></a>

 ** AllocationStrategy **
The strategy that determines the order of the launch template overrides to use in fulfilling On-Demand capacity.
 `lowest-price` - EC2 Fleet uses price to determine the order, launching the lowest price first.
 `prioritized` - EC2 Fleet uses the priority that you assigned to each launch template override, launching the highest priority first.
Default: `lowest-price`
Type: String
Valid Values: `lowest-price | prioritized`
Required: No

 ** CapacityReservationOptions **
The strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.
Supported only for fleets of type `instant`.
Type: [CapacityReservationOptionsRequest](API_CapacityReservationOptionsRequest.md) object
Required: No

 ** MaxTotalPrice **
The maximum amount per hour for On-Demand Instances that you're willing to pay.
If your fleet includes T instances that are configured as `unlimited`, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `MaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `MaxTotalPrice`. For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** MinTargetCapacity **
The minimum target capacity for On-Demand Instances in the fleet. If this minimum capacity isn't reached, no instances are launched.
Constraints: Maximum value of `1000`. Supported only for fleets of type `instant`.
At least one of the following must be specified: `SingleAvailabilityZone` \| `SingleInstanceType`
Type: Integer
Required: No

 ** SingleAvailabilityZone **
Indicates that the fleet launches all On-Demand Instances into a single Availability Zone.
Supported only for fleets of type `instant`.
Type: Boolean
Required: No

 ** SingleInstanceType **
Indicates that the fleet uses a single instance type to launch all On-Demand Instances in the fleet.
Supported only for fleets of type `instant`.
Type: Boolean
Required: No

## See Also
<a name="API_OnDemandOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/OnDemandOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/OnDemandOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/OnDemandOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
