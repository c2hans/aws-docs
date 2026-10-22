---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCapacityReservation.html
---

# CreateDBCapacityReservation
<a name="API_CreateDBCapacityReservation"></a>

Creates a DB capacity reservation. A DB capacity reservation reserves compute and memory capacity for DB instances of one DB instance class and one database engine. Amazon RDS reserves that capacity in each Availability Zone that you specify.

Amazon RDS reserves the same amount of capacity in every Availability Zone in the request. You set that amount with `CapacityPerAvailabilityZone`, and you set the Availability Zones with `AvailabilityZones`. The total reserved capacity is `CapacityPerAvailabilityZone` multiplied by the number of Availability Zones.

Specify `StartDate` and `CommitmentDuration` together to create a future-dated reservation. A future-dated reservation reserves capacity for a period that starts later. Amazon RDS holds that capacity for the length of the commitment.

A future-dated reservation has the following additional constraints:
+  `DBInstanceClass` must be a `db.c`, `db.m`, `db.r`, `db.t`, or `db.x` DB instance class. The letter after `db.` gives the DB instance class family. For example, `db.x2g.xlarge` qualifies, and `db.z1d.xlarge` doesn't.
+ If `DBInstanceClass` is a `db.m` or `db.r` DB instance class, it must be from generation 7 or later. The digit after the family letter gives the generation. For example, `db.m7g.xlarge` qualifies, and `db.m5.xlarge` doesn't. A `db.c`, `db.t`, or `db.x` DB instance class has no generation requirement.
+ The reserved capacity must total at least 32 vCPUs in each Availability Zone. Multiply `CapacityPerAvailabilityZone` by the number of vCPUs of the DB instance class. The product must be 32 or more.
+  `CommitmentDuration` must be at least 14 days. For a `db.x` DB instance class, it must be at least 84 days.
+  `StartDate` must be from 5 to 120 days in the future.

Therefore, a DB instance class with 2 vCPUs needs a `CapacityPerAvailabilityZone` of 16 or more, a class with 4 vCPUs needs 8 or more, a class with 8 vCPUs needs 4 or more, and a class with 16 vCPUs needs 2 or more. For the number of vCPUs of each DB instance class, see [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.

**Note**
You can't modify a future-dated reservation before it starts. You can't cancel a future-dated reservation in the `scheduled` state. You can't cancel a reservation in the `active` state during its capacity commitment. Therefore, you can't cancel a future-dated reservation from the time that Amazon RDS schedules it until the commitment ends.

## Request Parameters
<a name="API_CreateDBCapacityReservation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AvailabilityZones.AvailabilityZone.N**
A list of Availability Zones for the reservation.
You can't change the Availability Zones of a reservation after you create it. Reserved capacity in an Availability Zone that no DB instance uses stays unused.
Constraints:
+ Must specify one or more Availability Zones.
+ Each Availability Zone can appear only once.
+ Each Availability Zone must be in the AWS Region of the request.
+ Each Availability Zone must have capacity for the requested DB instance class.
+ Must include two or more Availability Zones to use the reservation for a Multi-AZ DB instance.
+ A DB instance can use reserved capacity only in an Availability Zone that its DB subnet group covers.
Example: `us-east-1a`
Type: Array of strings
Required: Yes

 ** CapacityPerAvailabilityZone **
The number of DB instances to reserve in each Availability Zone that you list in `AvailabilityZones`. Amazon RDS reserves this number of DB instances in every listed Availability Zone.
A Single-AZ DB instance uses one unit of reserved capacity, in one Availability Zone. A Multi-AZ DB instance is one DB instance, and it uses one unit of reserved capacity in each of two Availability Zones. Therefore, a Multi-AZ DB instance uses two units in total. A read replica uses one unit of reserved capacity, in the same way as any other DB instance.
Amazon RDS reserves capacity in each Availability Zone separately. Reserved capacity in one Availability Zone can't serve a DB instance in another Availability Zone. A request for a DB instance fails when the Availability Zone of the DB instance has no available capacity.
Therefore, set this value to the number of DB instances that you want to run at the same time in one Availability Zone. Don't set it to the number that you want in total.
This value multiplied by the number of Availability Zones counts against the DB instances quota for your AWS account in the AWS Region. Your existing DB instances, and the unused capacity of your other reservations, count against the same quota.
To find the value of the DB instances quota, see [Quotas and constraints for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html) in the *Amazon RDS User Guide*.
Constraints:
+ Minimum 1.
Type: Integer
Required: Yes

 ** DBCapacityReservationName **
The name of the DB capacity reservation. This name must be unique for your AWS account in the AWS Region.
Constraints:
+ Must contain from 1 to 63 lowercase letters, digits, or hyphens.
+ First character must be a lowercase letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
+ Can't contain more than 16 groups of characters separated by hyphens.
+ Can't begin with `dbcr-`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z](?:-?[a-z0-9]+){0,15}`
Required: Yes

 ** DBInstanceClass **
The compute and memory capacity to reserve, for example `db.m5.large`. Not all DB instance classes are available in all AWS Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.
Constraints:
+ Must be a DB instance class that the specified `Engine` supports.
+ For RDS for Oracle with `LicenseModel` set to `license-included`, some DB instance classes aren't supported. Either choose a supported DB instance class, or set `LicenseModel` to `bring-your-own-license`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `db\.[0-9a-z]{2,6}\.[0-9a-z\.]{4,20}`
Required: Yes

 ** Engine **
The database engine to reserve capacity for.
Valid Values: `aurora-mysql` \| `aurora-postgresql` \| `mysql` \| `postgres` \| `mariadb` \| `oracle-ee` \| `oracle-ee-cdb` \| `oracle-se2` \| `oracle-se2-cdb` \| `sqlserver-ee` \| `sqlserver-se` \| `sqlserver-web` \| `sqlserver-ex` \| `sqlserver-dev-ee` \| `sqlserver-dev-se` \| `db2-ae` \| `db2-ce` \| `db2-se`
The Developer Edition engines `sqlserver-dev-ee` and `sqlserver-dev-se` support no Multi-AZ DB instance and no read replica. Therefore, a reservation for either engine serves Single-AZ DB instances only.
Type: String
Required: Yes

 ** CommitmentDuration **
The length of the capacity commitment that you request for a future-dated reservation, in seconds. Amazon RDS measures this length from `StartDate`.
Amazon RDS can grant a shorter capacity commitment than you request. Therefore, read `CommitmentEndDate` in `CommitmentInfo` for the commitment that Amazon RDS granted.
The commitment doesn't end the reservation. Specify `EndDate` to set an expiration date. You can't cancel a reservation in the `active` state during the commitment.
Constraints:
+ Minimum 1209600, which is 14 days. For a `db.x` DB instance class, such as `db.x2g.xlarge`, the minimum is 7257600, which is 84 days.
+ Must be less than 315576000, which is 10 years.
+ You must also specify `StartDate`.
Example: `2592000`
Type: Long
Required: No

 ** EndDate **
The date and time when the reservation expires, in Universal Coordinated Time (UTC). If you don't specify a value, the reservation doesn't expire.
To change the expiration of an existing reservation, use `ModifyDBCapacityReservation`. That operation takes `EndDateType` along with `EndDate`.
Constraints:
+ Must be a date and time in the future.
+ For a future-dated reservation, must be at or after `StartDate` plus `CommitmentDuration`. For example, a reservation that starts on 2026-12-01 with a 30-day commitment can't expire before 2026-12-31. To reserve capacity for one calendar month, set `CommitmentDuration` to 30 days or fewer, not to the length of the month.
Example: `2026-12-31T23:59:59Z`
Type: Timestamp
Required: No

 ** LicenseModel **
The license model to reserve capacity for. Specify this parameter only for RDS for Microsoft SQL Server Enterprise Edition, Standard Edition, and Developer Edition, for RDS for Oracle, or for RDS for Db2 Standard Edition and Advanced Edition. Amazon RDS rejects the request for any other engine. This includes Amazon Aurora, the Web and Express editions of RDS for Microsoft SQL Server, and RDS for Db2 Community Edition.
Valid Values:
+ RDS for Microsoft SQL Server Enterprise Edition and Standard Edition - `license-included | bring-your-own-media`
+ RDS for Microsoft SQL Server Developer Edition - `bring-your-own-license`
+ RDS for Oracle - `bring-your-own-license | license-included`
+ RDS for Db2 Standard Edition and Advanced Edition - `bring-your-own-license | marketplace-license`
A DB instance launches into the reservation only when the license model of the DB instance matches the license model of the reservation. For a reservation that holds no license model, Amazon RDS applies no license model check at launch.
For RDS for Microsoft SQL Server Enterprise Edition and Standard Edition, if you don't specify a value, Amazon RDS uses `license-included`.
For RDS for Microsoft SQL Server Developer Edition, if you don't specify a value, Amazon RDS uses `bring-your-own-license`. That is the only license model that these engines accept, and Amazon RDS rejects any other value.
For RDS for Oracle, if you don't specify a value, Amazon RDS uses the only orderable license model for the DB instance class. If more than one license model is orderable, you must specify one.
For RDS for Db2 Standard Edition and Advanced Edition, if you don't specify a value, Amazon RDS uses `bring-your-own-license`. To reserve capacity for Db2 DB instances that you license through AWS Marketplace, specify `marketplace-license`.
For RDS for Oracle, the license models that you can reserve depend on the engine and the DB instance class. RDS for Oracle Enterprise Edition doesn't support `license-included`.
Type: String
Required: No

 ** StartDate **
The date and time when the reservation starts, in Universal Coordinated Time (UTC). Specify this parameter to create a future-dated reservation. If you don't specify a value, the reservation starts immediately.
A reservation that starts later always carries a capacity commitment. Therefore, a request that specifies `StartDate` must also meet every constraint of a future-dated reservation, including the minimum reserved capacity in each Availability Zone.
Constraints:
+ Must be from 5 to 120 days in the future.
+ You must also specify `CommitmentDuration`.
Example: `2026-12-01T00:00:00Z`
Type: Timestamp
Required: No

 **Tags.Tag.N**
Tags to assign to the DB capacity reservation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateDBCapacityReservation_ResponseElements"></a>

The following element is returned by the service.

 ** DBCapacityReservation **
Contains the details of the newly created DB capacity reservation.
Type: [DBCapacityReservation](API_DBCapacityReservation.md) object

## Errors
<a name="API_CreateDBCapacityReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBCapacityReservationAlreadyExists **
You already have a DB capacity reservation with the given name. Choose a different name for the new reservation, or use the existing reservation.
HTTP Status Code: 400

 ** DBCapacityReservationUnsupported **
The specified configuration isn't supported for DB capacity reservations.
HTTP Status Code: 400

 ** InstanceQuotaExceeded **
The request would result in the user exceeding the allowed number of DB instances.
HTTP Status Code: 400

 ** InsufficientDBInstanceCapacity **
The specified DB instance class isn't available in the specified Availability Zone.
HTTP Status Code: 400

## See Also
<a name="API_CreateDBCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBCapacityReservation)
