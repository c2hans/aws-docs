---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationModificationQuote.html
---

# CapacityReservationModificationQuote
<a name="API_CapacityReservationModificationQuote"></a>

Describes a Capacity Reservation modification quote, which provides the terms for changing the start date or the commitment of a future-dated Capacity Reservation.

## Contents
<a name="API_CapacityReservationModificationQuote_Contents"></a>

 ** capacityReservationId **
The ID of the Capacity Reservation associated with the modification quote.
Type: String
Required: No

 ** capacityReservationModificationQuoteId **
The ID of the modification quote.
Type: String
Required: No

 ** createTime **
The date and time at which the modification quote was created.
Type: Timestamp
Required: No

 ** currentConfiguration **
The configuration that the Capacity Reservation has at the time the quote was generated.
Type: [ModificationQuoteCurrentConfiguration](API_ModificationQuoteCurrentConfiguration.md) object
Required: No

 ** expirationTime **
The date and time at which the modification quote expires.
Type: Timestamp
Required: No

 ** modificationTerms **
The terms of the modification, including the configuration that the Capacity Reservation will have if you accept them by using `ModifyCapacityReservation`.
Type: [ModificationTerms](API_ModificationTerms.md) object
Required: No

 ** quoteState **
The state of the modification quote itself. Possible values are:
+  `active` - The quote can still be used.
+  `expired` - The quote can no longer be used. A quote becomes `expired` at its `expirationTime`.
Type: String
Valid Values: `active | expired`
Required: No

 ** TagSet.N **
The tags assigned to the modification quote.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_CapacityReservationModificationQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationModificationQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationModificationQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationModificationQuote)
