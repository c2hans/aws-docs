---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservationCancellationQuote.html
---

# CreateCapacityReservationCancellationQuote
<a name="API_CreateCapacityReservationCancellationQuote"></a>

Generates a cancellation quote for a future-dated Capacity Reservation that is within its commitment duration. The quote includes the cancellation terms and a quote ID that you can pass to the `CancelCapacityReservation` action. Cancellation quotes are valid for 24 hours.

## Request Parameters
<a name="API_CreateCapacityReservationCancellationQuote_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityReservationId**
The ID of the Capacity Reservation.
Type: String
Required: Yes

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to apply to the cancellation quote.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateCapacityReservationCancellationQuote_ResponseElements"></a>

The following elements are returned by the service.

 **capacityReservationCancellationQuote**
Information about the Capacity Reservation cancellation quote.
Type: [CapacityReservationCancellationQuote](API_CapacityReservationCancellationQuote.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateCapacityReservationCancellationQuote_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateCapacityReservationCancellationQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateCapacityReservationCancellationQuote)
