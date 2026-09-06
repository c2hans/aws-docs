---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelCapacityReservation.html
---

# CancelCapacityReservation
<a name="API_CancelCapacityReservation"></a>

Cancels the specified Capacity Reservation, releases the reserved capacity, and changes the Capacity Reservation's state to `cancelled`.

You can cancel a Capacity Reservation that is in the following states:
+  `assessing`
+  `scheduled` — requires a cancellation quote. Use `CreateCapacityReservationCancellationQuote` to generate a quote, then pass the quote ID with `ApplyCancellationCharges` set to `commitment-wind-down`. The cancellation charge depends on how close the reservation is to its start date.
+  `active` and there is no commitment duration or the commitment duration has elapsed.
+  `active` during the commitment duration — requires a cancellation quote. Use `CreateCapacityReservationCancellationQuote` to generate a quote, then pass the quote ID with `ApplyCancellationCharges` set to `commitment-wind-down`. The Capacity Reservation transitions to `cancelling` while charges are applied.
+  `delayed` — the commitment duration is waived, so no cancellation charge applies.

**Note**
You can't modify or cancel a Capacity Block. For more information, see [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html).

Instances running in the reserved capacity continue running until you stop them. Stopped instances that target the Capacity Reservation can no longer launch. Modify these instances to either target a different Capacity Reservation, launch On-Demand Instance capacity, or run in any open Capacity Reservation that has matching attributes and sufficient capacity.

## Request Parameters
<a name="API_CancelCapacityReservation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ApplyCancellationCharges**
Specifies the cancellation charge type to apply when cancelling a future-dated Capacity Reservation during its commitment duration. Possible values include `commitment-wind-down`, which continues billing for the remaining commitment duration without delivering capacity.
Type: String
Valid Values: `commitment-wind-down`
Required: No

 **CapacityReservationId**
The ID of the Capacity Reservation to be cancelled.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **QuoteId**
The ID of the cancellation quote to use for the cancellation. You can generate a cancellation quote by using the `CreateCapacityReservationCancellationQuote` action. The cancellation quote must be in an `active` state.
Type: String
Required: No

## Response Elements
<a name="API_CancelCapacityReservation_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_CancelCapacityReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CancelCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CancelCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelCapacityReservation)
