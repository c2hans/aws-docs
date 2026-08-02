---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HostReservation.html
---

# HostReservation
<a name="API_HostReservation"></a>

Details about the Dedicated Host Reservation and associated Dedicated Hosts.

## Contents
<a name="API_HostReservation_Contents"></a>

 ** count **
The number of Dedicated Hosts the reservation is associated with.
Type: Integer
Required: No

 ** currencyCode **
The currency in which the `upfrontPrice` and `hourlyPrice` amounts are specified. At this time, the only supported currency is `USD`.
Type: String
Valid Values: `USD`
Required: No

 ** duration **
The length of the reservation's term, specified in seconds. Can be `31536000 (1 year)` \| `94608000 (3 years)`.
Type: Integer
Required: No

 ** end **
The date and time that the reservation ends.
Type: Timestamp
Required: No

 ** HostIdSet.N **
The IDs of the Dedicated Hosts associated with the reservation.
Type: Array of strings
Required: No

 ** hostReservationId **
The ID of the reservation that specifies the associated Dedicated Hosts.
Type: String
Required: No

 ** hourlyPrice **
The hourly price of the reservation.
Type: String
Required: No

 ** instanceFamily **
The instance family of the Dedicated Host Reservation. The instance family on the Dedicated Host must be the same in order for it to benefit from the reservation.
Type: String
Required: No

 ** offeringId **
The ID of the reservation. This remains the same regardless of which Dedicated Hosts are associated with it.
Type: String
Required: No

 ** paymentOption **
The payment option selected for this reservation.
Type: String
Valid Values: `AllUpfront | PartialUpfront | NoUpfront`
Required: No

 ** start **
The date and time that the reservation started.
Type: Timestamp
Required: No

 ** state **
The state of the reservation.
Type: String
Valid Values: `active | expired | cancelled | scheduled | pending | failed | delayed | unsupported | payment-pending | payment-failed | retired`
Required: No

 ** TagSet.N **
Any tags assigned to the Dedicated Host Reservation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** upfrontPrice **
The upfront price of the reservation.
Type: String
Required: No

## See Also
<a name="API_HostReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/HostReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/HostReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/HostReservation)
