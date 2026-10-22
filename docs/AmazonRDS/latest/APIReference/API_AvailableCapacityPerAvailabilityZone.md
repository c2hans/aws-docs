---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AvailableCapacityPerAvailabilityZone.html
---

# AvailableCapacityPerAvailabilityZone
<a name="API_AvailableCapacityPerAvailabilityZone"></a>

Contains the unused capacity of a DB capacity reservation in one Availability Zone.

This data type is used as a response element in the following operations:
+  `CancelDBCapacityReservation`
+  `CreateDBCapacityReservation`
+  `DescribeDBCapacityReservations`
+  `ModifyDBCapacityReservation`

## Contents
<a name="API_AvailableCapacityPerAvailabilityZone_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityZone **
The name of the Availability Zone.
Type: String
Required: No

 ** AvailableCapacity **
The number of DB instances that remain available in this Availability Zone. Amazon RDS decreases this value when a DB instance takes a unit of reserved capacity in this Availability Zone, and it increases this value when a DB instance releases that unit.
A DB instance with a pending modification also holds a unit of reserved capacity. A DB instance has a pending modification when Amazon RDS accepts a change to the DB instance and applies that change later, during the maintenance window. Amazon RDS holds the unit from the time that it accepts the request. To find a DB instance with a pending modification, check `PendingModifiedValues` in the response of `DescribeDBInstances`.
Amazon RDS reports available capacity only for a reservation that is in the `active` state and not past its end date. Otherwise, this value is `0`.
Type: Integer
Required: No

## See Also
<a name="API_AvailableCapacityPerAvailabilityZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AvailableCapacityPerAvailabilityZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AvailableCapacityPerAvailabilityZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AvailableCapacityPerAvailabilityZone)
