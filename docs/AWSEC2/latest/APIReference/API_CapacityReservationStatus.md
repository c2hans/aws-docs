---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationStatus.html
---

# CapacityReservationStatus
<a name="API_CapacityReservationStatus"></a>

Describes the availability of capacity for a Capacity Reservation.

## Contents
<a name="API_CapacityReservationStatus_Contents"></a>

 ** capacityReservationId **
The ID of the Capacity Reservation.
Type: String
Required: No

 ** totalAvailableCapacity **
The remaining capacity. Indicates the amount of resources that can be launched into the Capacity Reservation.
Type: Integer
Required: No

 ** totalCapacity **
The combined amount of `Available` and `Unavailable` capacity in the Capacity Reservation.
Type: Integer
Required: No

 ** totalUnavailableCapacity **
The used capacity. Indicates that the capacity is in use by resources that are running in the Capacity Reservation.
Type: Integer
Required: No

## See Also
<a name="API_CapacityReservationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationStatus)
