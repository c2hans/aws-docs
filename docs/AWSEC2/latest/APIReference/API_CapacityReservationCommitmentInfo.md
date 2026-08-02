---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationCommitmentInfo.html
---

# CapacityReservationCommitmentInfo
<a name="API_CapacityReservationCommitmentInfo"></a>

Information about your commitment for a future-dated Capacity Reservation.

## Contents
<a name="API_CapacityReservationCommitmentInfo_Contents"></a>

 ** commitmentEndDate **
The date and time at which the commitment duration expires, in the ISO8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`). You can't decrease the instance count or cancel the Capacity Reservation before this date and time.
Type: Timestamp
Required: No

 ** committedInstanceCount **
The instance capacity that you committed to when you requested the future-dated Capacity Reservation.
Type: Integer
Required: No

## See Also
<a name="API_CapacityReservationCommitmentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationCommitmentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationCommitmentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationCommitmentInfo)
