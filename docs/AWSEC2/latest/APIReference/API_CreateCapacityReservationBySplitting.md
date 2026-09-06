---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservationBySplitting.html
---

# CreateCapacityReservationBySplitting
<a name="API_CreateCapacityReservationBySplitting"></a>

 Create a new Capacity Reservation by splitting the capacity of the source Capacity Reservation. The new Capacity Reservation will have the same attributes as the source Capacity Reservation except for tags. The source Capacity Reservation must be `active` and owned by your AWS account.

## Request Parameters
<a name="API_CreateCapacityReservationBySplitting_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceCount**
 The number of instances to split from the source Capacity Reservation.
Type: Integer
Required: Yes

 **SourceCapacityReservationId**
 The ID of the Capacity Reservation from which you want to split the capacity.
Type: String
Required: Yes

 **TagSpecification.N**
 The tags to apply to the new Capacity Reservation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateCapacityReservationBySplitting_ResponseElements"></a>

The following elements are returned by the service.

 **destinationCapacityReservation**
 Information about the destination Capacity Reservation.
Type: [CapacityReservation](API_CapacityReservation.md) object

 **instanceCount**
 The number of instances in the new Capacity Reservation. The number of instances in the source Capacity Reservation was reduced by this amount.
Type: Integer

 **requestId**
The ID of the request.
Type: String

 **sourceCapacityReservation**
 Information about the source Capacity Reservation.
Type: [CapacityReservation](API_CapacityReservation.md) object

## Errors
<a name="API_CreateCapacityReservationBySplitting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateCapacityReservationBySplitting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateCapacityReservationBySplitting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateCapacityReservationBySplitting)
