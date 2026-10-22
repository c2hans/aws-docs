---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBCapacityReservation.html
---

# DBCapacityReservation
<a name="API_DBCapacityReservation"></a>

Contains the details of a DB capacity reservation.

This data type is used as a response element in the following operations:
+  `CancelDBCapacityReservation`
+  `CreateDBCapacityReservation`
+  `DescribeDBCapacityReservations`
+  `ModifyDBCapacityReservation`

## Contents
<a name="API_DBCapacityReservation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailableCapacityPerAvailabilityZoneList.AvailableCapacityPerAvailabilityZone.N **
The unused capacity of the reservation, reported for each Availability Zone of the reservation. Each entry names one Availability Zone, and it reports the number of DB instances that remain available in that Availability Zone.
Amazon RDS reports available capacity only for a reservation that is in the `active` state and not past its end date. Otherwise, each entry reports an available capacity of `0`. A future-dated reservation that hasn't started reports `0`, and a reservation that Amazon RDS is modifying reports `0`.
A reservation reports the `pending` state while Amazon RDS modifies it. Therefore, a reservation in the `active` state that reports no available capacity has no unused capacity.
Type: Array of [AvailableCapacityPerAvailabilityZone](API_AvailableCapacityPerAvailabilityZone.md) objects
Required: No

 ** CommitmentInfo **
The capacity commitment of the reservation. Amazon RDS returns this object only for a future-dated reservation.
Type: [DBCapacityReservationCommitmentInfo](API_DBCapacityReservationCommitmentInfo.md) object
Required: No

 ** CreateDate **
The date and time when the reservation was created, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

 ** DBCapacityReservationArn **
The Amazon Resource Name (ARN) of the DB capacity reservation.
Type: String
Required: No

 ** DBCapacityReservationIdentifier **
The unique identifier of the DB capacity reservation. The identifier has the prefix `dbcr-`. Every other DB capacity reservation operation takes this identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z](?:-?[a-z0-9]+){0,15}`
Required: No

 ** DBCapacityReservationName **
The name that you specified for the DB capacity reservation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z](?:-?[a-z0-9]+){0,15}`
Required: No

 ** DBInstanceClass **
The DB instance class for the reserved capacity. You specify this value when you create the reservation, and you can't change it afterward.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `db\.[0-9a-z]{2,6}\.[0-9a-z\.]{4,20}`
Required: No

 ** EndDate **
The date and time when the reservation expires, in Universal Coordinated Time (UTC). Amazon RDS doesn't return this value if the reservation doesn't expire.
A DB instance that uses the reservation keeps running after the reservation expires. It continues on unreserved capacity, and Amazon RDS doesn't stop it or modify it. However, Amazon RDS no longer reserves capacity for the DB instance. Amazon RDS might later move the DB instance to different hardware, for example during hardware maintenance. That move can fail when the AWS Region has insufficient capacity for the DB instance class.
Type: Timestamp
Required: No

 ** Engine **
The database engine for the reserved capacity. You specify this value when you create the reservation, and you can't change it afterward.
Type: String
Required: No

 ** LicenseModel **
The license model for the reserved capacity. Amazon RDS returns this value only for a reservation that reserves capacity for a specific license model. Amazon RDS doesn't return this value for a reservation whose database engine doesn't support a license model.
A DB instance launches into the reservation only when the license model of the DB instance matches this value. For a reservation that holds no license model, Amazon RDS applies no license model check at launch.
Valid Values:
+ RDS for Microsoft SQL Server Enterprise Edition and Standard Edition - `license-included | bring-your-own-media`
+ RDS for Microsoft SQL Server Developer Edition - `bring-your-own-license`
+ RDS for Oracle - `bring-your-own-license | license-included`
+ RDS for Db2 Standard Edition and Advanced Edition - `bring-your-own-license | marketplace-license`
For RDS for Db2 Standard Edition and Advanced Edition, a reservation created without a license model holds `bring-your-own-license`.
Type: String
Required: No

 ** ReservedCapacityPerAvailabilityZone **
The number of DB instances that Amazon RDS reserves in each Availability Zone of the reservation. This value matches the `CapacityPerAvailabilityZone` parameter of the request. The total reserved capacity is this value multiplied by the number of Availability Zones of the reservation.
Type: Integer
Required: No

 ** StartDate **
The date and time when a future-dated reservation starts, in Universal Coordinated Time (UTC). Amazon RDS doesn't return this value for a reservation that started immediately.
Type: Timestamp
Required: No

 ** State **
The current state of the DB capacity reservation. A DB instance can use the reservation in the `active` state only.
Valid Values:
+  `active` - Amazon RDS holds the reserved capacity, and a DB instance can use it.
+  `pending` - The reservation isn't ready to use yet. Amazon RDS is creating the reserved capacity, or it is applying a requested modification.
+  `assessing` - Amazon RDS is evaluating the request for a future-dated reservation.
+  `scheduled` - Amazon RDS accepted a future-dated reservation, and the reservation is waiting for its start date.
+  `delayed` - Amazon RDS couldn't provide the reserved capacity of a future-dated reservation by its start date.
+  `unsupported` - Amazon RDS can't fulfill the future-dated reservation as requested.
+  `expired` - The reservation passed its end date. Amazon RDS releases the reserved capacity.
+  `cancelled` - You cancelled the reservation, and Amazon RDS released the reserved capacity.
+  `failed` - Amazon RDS couldn't reserve the capacity.
The values `assessing`, `scheduled`, `delayed`, and `unsupported` apply to a future-dated reservation only.
Type: String
Valid Values: `active | expired | cancelled | pending | failed | assessing | scheduled | delayed | unsupported`
Required: No

 ** TagList.Tag.N **
The tags associated with the DB capacity reservation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_DBCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBCapacityReservation)
