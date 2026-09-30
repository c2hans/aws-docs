---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservationDateChangeQuote.html
---

# CreateCapacityReservationDateChangeQuote
<a name="API_CreateCapacityReservationDateChangeQuote"></a>

Generates a quote for changing the start date of a future-dated Capacity Reservation that has not yet been delivered. The quote includes the new start date, the resulting commitment end date, and a quote ID. Pass the quote ID to `ModifyCapacityReservation` to apply the change.

The cumulative pushout across all changes is limited to 30 days from the Capacity Reservation's original start date. Quotes are valid for 24 hours, and always expire at least one hour before the start date.

## Request Parameters
<a name="API_CreateCapacityReservationDateChangeQuote_RequestParameters"></a>

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

 **NewStartDate**
The requested new start date for the Capacity Reservation, in the ISO8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`). The new start date must be later than the current start date and within the cumulative 30-day pushout limit.
Type: Timestamp
Required: Yes

 **TagSpecification.N**
The tags to apply to the date change quote.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateCapacityReservationDateChangeQuote_ResponseElements"></a>

The following elements are returned by the service.

 **capacityReservationModificationQuote**
Information about the Capacity Reservation date change quote.
Type: [CapacityReservationModificationQuote](API_CapacityReservationModificationQuote.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateCapacityReservationDateChangeQuote_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateCapacityReservationDateChangeQuote_Examples"></a>

### Example
<a name="API_CreateCapacityReservationDateChangeQuote_Example_1"></a>

This example generates a quote for moving the start date of a future-dated Capacity Reservation to October 15, 2026.

#### Sample Request
<a name="API_CreateCapacityReservationDateChangeQuote_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateCapacityReservationDateChangeQuote
&CapacityReservationId=cr-1234567890abcdef0
&NewStartDate=2026-10-15T00:00:00.000Z
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateCapacityReservationDateChangeQuote_Example_1_Response"></a>

```
<CreateCapacityReservationDateChangeQuoteResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityReservationModificationQuote>
        <capacityReservationModificationQuoteId>crmq-123456789abcdefgh</capacityReservationModificationQuoteId>
        <capacityReservationId>cr-1234567890abcdef0</capacityReservationId>
        <createTime>2026-09-18T10:15:00.000Z</createTime>
        <expirationTime>2026-09-19T10:15:00.000Z</expirationTime>
        <quoteState>active</quoteState>
        <currentConfiguration>
            <instanceCount>20</instanceCount>
            <reservationState>scheduled</reservationState>
            <startDate>2026-10-01T00:00:00.000Z</startDate>
            <originalStartDate>2026-09-15T00:00:00.000Z</originalStartDate>
        </currentConfiguration>
        <modificationTerms>
            <reservationUpdate>
                <newStartDate>2026-10-15T00:00:00.000Z</newStartDate>
                <newCommitmentEndDate>2026-11-14T00:00:00.000Z</newCommitmentEndDate>
                <newCommitmentDuration>2592000</newCommitmentDuration>
            </reservationUpdate>
        </modificationTerms>
    </capacityReservationModificationQuote>
</CreateCapacityReservationDateChangeQuoteResponse>
```

## See Also
<a name="API_CreateCapacityReservationDateChangeQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateCapacityReservationDateChangeQuote)
