---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBCapacityReservationCommitmentInfo.html
---

# DBCapacityReservationCommitmentInfo
<a name="API_DBCapacityReservationCommitmentInfo"></a>

Contains the capacity commitment details of a DB capacity reservation, including the number of committed DB instances in each Availability Zone and the end date of the commitment period. Amazon RDS holds the committed capacity until the commitment ends. Amazon RDS rejects a request to cancel a reservation in the `active` state, and a request to reduce the reserved capacity below the commitment.

This data type is used as a response element in the following operations:
+  `CancelDBCapacityReservation`
+  `CreateDBCapacityReservation`
+  `DescribeDBCapacityReservations`
+  `ModifyDBCapacityReservation`

## Contents
<a name="API_DBCapacityReservationCommitmentInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CommitmentEndDate **
The date and time when the commitment ends, in Universal Coordinated Time (UTC). This date reports the capacity commitment that Amazon RDS granted.
Amazon RDS can grant a shorter capacity commitment than you request in `CommitmentDuration`. Therefore, this date can fall earlier than `StartDate` plus `CommitmentDuration`.
Type: Timestamp
Required: No

 ** CommittedCapacityPerAvailabilityZone **
The number of DB instances that Amazon RDS holds in each Availability Zone of the reservation for the length of the commitment.
Type: Integer
Required: No

## See Also
<a name="API_DBCapacityReservationCommitmentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBCapacityReservationCommitmentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBCapacityReservationCommitmentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBCapacityReservationCommitmentInfo)
