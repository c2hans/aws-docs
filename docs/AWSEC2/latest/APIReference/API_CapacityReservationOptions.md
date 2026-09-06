---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationOptions.html
---

# CapacityReservationOptions
<a name="API_CapacityReservationOptions"></a>

Describes the strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.

**Note**
This strategy can only be used if the EC2 Fleet is of type `instant`.

For more information about Capacity Reservations, see [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*. For examples of using Capacity Reservations in an EC2 Fleet, see [EC2 Fleet example configurations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-examples.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_CapacityReservationOptions_Contents"></a>

 ** usageStrategy **
Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.
If you specify `use-capacity-reservations-first`, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (`lowest-price` or `prioritized`) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (`lowest-price` or `prioritized`).
If you do not specify a value, the fleet fulfils the On-Demand capacity according to the chosen On-Demand allocation strategy.
Type: String
Valid Values: `use-capacity-reservations-first`
Required: No

## See Also
<a name="API_CapacityReservationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationOptions)
