---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationCancellationQuote.html
---

# CapacityReservationCancellationQuote
<a name="API_CapacityReservationCancellationQuote"></a>

Describes a Capacity Reservation cancellation quote, which provides the cancellation terms for cancelling a future-dated Capacity Reservation during its commitment duration.

## Contents
<a name="API_CapacityReservationCancellationQuote_Contents"></a>

 ** CancellationTermSet.N **
The cancellation terms associated with the quote, including the fee type and charge details.
Type: Array of [CancellationTerms](API_CancellationTerms.md) objects
Required: No

 ** capacityReservationCancellationQuoteId **
The ID of the cancellation quote.
Type: String
Required: No

 ** capacityReservationId **
The ID of the Capacity Reservation associated with the cancellation quote.
Type: String
Required: No

 ** createTime **
The date and time at which the cancellation quote was created.
Type: Timestamp
Required: No

 ** currentConfiguration **
The current configuration of the Capacity Reservation.
Type: [CapacityReservationConfiguration](API_CapacityReservationConfiguration.md) object
Required: No

 ** expirationTime **
The date and time at which the cancellation quote expires.
Type: Timestamp
Required: No

 ** quoteState **
The state of the cancellation quote. Possible values include `pending`, `active`, and `expired`.
Type: String
Valid Values: `pending | active | expired`
Required: No

 ** TagSet.N **
The tags assigned to the cancellation quote.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_CapacityReservationCancellationQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationCancellationQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationCancellationQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationCancellationQuote)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
