---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CancelDBCapacityReservation.html
---

# CancelDBCapacityReservation
<a name="API_CancelDBCapacityReservation"></a>

Cancels a DB capacity reservation. Amazon RDS changes the state of the reservation to `cancelled` and stops reporting available capacity for it. Amazon RDS then releases the reserved capacity.

A DB instance that uses the reservation keeps running. It continues on unreserved capacity, and Amazon RDS doesn't stop it or modify it. However, Amazon RDS no longer reserves capacity for the DB instance. If Amazon RDS later moves the DB instance to different hardware, for example during hardware maintenance, that move can fail when the AWS Region has insufficient capacity for the DB instance class.

You can't cancel a reservation in the `active` state during a capacity commitment. The response of `DescribeDBCapacityReservations` reports the end of the commitment in `CommitmentInfo`.

Constraints:
+ The reservation must be in the `active`, `assessing`, or `delayed` state.
+ The reservation must not be past its end date.

## Request Parameters
<a name="API_CancelDBCapacityReservation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBCapacityReservationIdentifier **
The identifier or the name of the DB capacity reservation to cancel. You can specify the identifier, which has the prefix `dbcr-`, or the reservation name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z](?:-?[a-z0-9]+){0,15}`
Required: Yes

## Response Elements
<a name="API_CancelDBCapacityReservation_ResponseElements"></a>

The following element is returned by the service.

 ** DBCapacityReservation **
Contains the details of the canceled DB capacity reservation.
Type: [DBCapacityReservation](API_DBCapacityReservation.md) object

## Errors
<a name="API_CancelDBCapacityReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBCapacityReservationNotFound **
 `DBCapacityReservationIdentifier` doesn't refer to an existing DB capacity reservation.
HTTP Status Code: 404

 ** InvalidDBCapacityReservationState **
The DB capacity reservation isn't in a valid state.
HTTP Status Code: 400

## See Also
<a name="API_CancelDBCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CancelDBCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CancelDBCapacityReservation)
