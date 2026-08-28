---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationOptionsRequest.html
---

# CapacityReservationOptionsRequest
<a name="API_CapacityReservationOptionsRequest"></a>

Describes the strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.

**Note**
This strategy can only be used if the EC2 Fleet is of type `instant`.

For more information about Capacity Reservations, see [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*. For examples of using Capacity Reservations in an EC2 Fleet, see [EC2 Fleet example configurations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-examples.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_CapacityReservationOptionsRequest_Contents"></a>

 ** UsageStrategy **
Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.
If you specify `use-capacity-reservations-first`, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (`lowest-price` or `prioritized`) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (`lowest-price` or `prioritized`).
If you do not specify a value, the fleet fulfils the On-Demand capacity according to the chosen On-Demand allocation strategy.
Type: String
Valid Values: `use-capacity-reservations-first`
Required: No

## See Also
<a name="API_CapacityReservationOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
