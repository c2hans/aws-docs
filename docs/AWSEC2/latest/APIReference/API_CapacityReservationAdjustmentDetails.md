---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationAdjustmentDetails.html
---

# CapacityReservationAdjustmentDetails
<a name="API_CapacityReservationAdjustmentDetails"></a>

Describes the configuration that a Capacity Reservation will have after a pending adjustment is applied.

## Contents
<a name="API_CapacityReservationAdjustmentDetails_Contents"></a>

 ** commitmentDuration **
The commitment duration, in seconds, that the Capacity Reservation will have after the adjustment.
Type: Long
Required: No

 ** commitmentEndDate **
The date and time at which the commitment duration will expire after the adjustment.
Type: Timestamp
Required: No

 ** endDate **
The end date that the Capacity Reservation will have after the adjustment.
Type: Timestamp
Required: No

 ** endDateType **
Indicates the way in which the Capacity Reservation will end after the adjustment. Possible values are:
+  `unlimited` - The Capacity Reservation remains active until you explicitly cancel it.
+  `limited` - The Capacity Reservation expires automatically at the date and time given by `endDate`.
Type: String
Required: No

 ** startDate **
The start date that the Capacity Reservation will have after the adjustment.
Type: Timestamp
Required: No

## See Also
<a name="API_CapacityReservationAdjustmentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationAdjustmentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationAdjustmentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationAdjustmentDetails)
