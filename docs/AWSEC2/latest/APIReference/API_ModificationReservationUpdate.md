---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModificationReservationUpdate.html
---

# ModificationReservationUpdate
<a name="API_ModificationReservationUpdate"></a>

Describes the changes that a Capacity Reservation modification quote will apply to a Capacity Reservation.

## Contents
<a name="API_ModificationReservationUpdate_Contents"></a>

 ** newCommitmentDuration **
The commitment duration, in seconds, that the Capacity Reservation will have after the modification.
Type: Integer
Required: No

 ** newCommitmentEndDate **
The date and time at which the commitment duration will expire after the modification, in the ISO8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp
Required: No

 ** newStartDate **
The start date that the Capacity Reservation will have after the modification, in the ISO8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp
Required: No

## See Also
<a name="API_ModificationReservationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModificationReservationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModificationReservationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModificationReservationUpdate)
