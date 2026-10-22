---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCapacityReservation.html
---

# ModifyDBCapacityReservation
<a name="API_ModifyDBCapacityReservation"></a>

Modifies a DB capacity reservation. You can change the reserved capacity in each Availability Zone of the reservation, and you can change the end date of the reservation. You can't change the Availability Zones of an existing reservation.

The reservation must be in the `active` state. A future-dated reservation that hasn't started isn't modifiable, and neither is a reservation that Amazon RDS is already modifying.

You must specify `CapacityPerAvailabilityZone`, `EndDateType`, or `EndDate`. A request that specifies none of the three changes nothing, and Amazon RDS rejects it.

## Request Parameters
<a name="API_ModifyDBCapacityReservation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBCapacityReservationIdentifier **
The identifier or the name of the DB capacity reservation to modify. You can specify the identifier, which has the prefix `dbcr-`, or the reservation name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z](?:-?[a-z0-9]+){0,15}`
Required: Yes

 ** CapacityPerAvailabilityZone **
The new number of DB instances to reserve in each Availability Zone of the reservation. Amazon RDS applies this number to every Availability Zone of the reservation.
An increase reserves more capacity at the time of the request, so it can fail when the AWS Region has insufficient capacity.
This value multiplied by the number of Availability Zones counts against the DB instances quota for your AWS account in the AWS Region. Amazon RDS checks the quota only when you increase the value.
Constraints:
+ Minimum 1.
+ Can't be less than the highest number of DB instances that use the reservation in any single Availability Zone of the reservation. That number includes a DB instance that holds a unit of reserved capacity for a pending modification. To find that number for an Availability Zone, subtract `AvailableCapacity` from `ReservedCapacityPerAvailabilityZone`.
+ During a capacity commitment, can't be less than `CommittedCapacityPerAvailabilityZone`.
Type: Integer
Required: No

 ** EndDate **
The new end date for the reservation, in Universal Coordinated Time (UTC). Required when `EndDateType` is `limited`. Don't specify a value when `EndDateType` is `unlimited`.
When you specify `EndDate`, you must also specify `EndDateType`.
Constraints:
+ Must be a date and time in the future.
+ During a capacity commitment, must be at or after `CommitmentEndDate`.
Type: Timestamp
Required: No

 ** EndDateType **
The end date type for the reservation.
Valid Values:
+  `limited` - The reservation has a specific end date. You must also specify `EndDate`.
+  `unlimited` - The reservation doesn't expire. Don't specify `EndDate`.
Type: String
Valid Values: `unlimited | limited`
Required: No

## Response Elements
<a name="API_ModifyDBCapacityReservation_ResponseElements"></a>

The following element is returned by the service.

 ** DBCapacityReservation **
Contains the details of the modified DB capacity reservation.
Type: [DBCapacityReservation](API_DBCapacityReservation.md) object

## Errors
<a name="API_ModifyDBCapacityReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBCapacityReservationNotFound **
 `DBCapacityReservationIdentifier` doesn't refer to an existing DB capacity reservation.
HTTP Status Code: 404

 ** InstanceQuotaExceeded **
The request would result in the user exceeding the allowed number of DB instances.
HTTP Status Code: 400

 ** InsufficientDBInstanceCapacity **
The specified DB instance class isn't available in the specified Availability Zone.
HTTP Status Code: 400

 ** InvalidDBCapacityReservationState **
The DB capacity reservation isn't in a valid state.
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBCapacityReservation)
