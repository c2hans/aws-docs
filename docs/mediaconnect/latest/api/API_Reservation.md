---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Reservation.html
---

# Reservation
<a name="API_Reservation"></a>

 A pricing agreement for a discounted rate for a specific outbound bandwidth that your MediaConnect account will use each month over a specific time period. The discounted rate in the reservation applies to outbound bandwidth for all flows from your account until your account reaches the amount of bandwidth in your reservation. If you use more outbound bandwidth than the agreed upon amount in a single month, the overage is charged at the on-demand rate.

## Contents
<a name="API_Reservation_Contents"></a>

 ** currencyCode **   <a name="mediaconnect-Type-Reservation-currencyCode"></a>
 The type of currency that is used for billing. The currencyCode used for your reservation is US dollars.
Type: String
Required: Yes

 ** duration **   <a name="mediaconnect-Type-Reservation-duration"></a>
 The length of time that this reservation is active. MediaConnect defines this value in the offering.
Type: Integer
Required: Yes

 ** durationUnits **   <a name="mediaconnect-Type-Reservation-durationUnits"></a>
 The unit of measurement for the duration of the reservation. MediaConnect defines this value in the offering.
Type: String
Valid Values: `MONTHS`
Required: Yes

 ** end **   <a name="mediaconnect-Type-Reservation-end"></a>
 The day and time that this reservation expires. This value is calculated based on the start date and time that you set and the offering's duration.
Type: String
Required: Yes

 ** offeringArn **   <a name="mediaconnect-Type-Reservation-offeringArn"></a>
 The Amazon Resource Name (ARN) that MediaConnect assigns to the offering.
Type: String
Required: Yes

 ** offeringDescription **   <a name="mediaconnect-Type-Reservation-offeringDescription"></a>
 A description of the offering. MediaConnect defines this value in the offering.
Type: String
Required: Yes

 ** pricePerUnit **   <a name="mediaconnect-Type-Reservation-pricePerUnit"></a>
 The cost of a single unit. This value, in combination with priceUnits, makes up the rate. MediaConnect defines this value in the offering.
Type: String
Required: Yes

 ** priceUnits **   <a name="mediaconnect-Type-Reservation-priceUnits"></a>
 The unit of measurement that is used for billing. This value, in combination with pricePerUnit, makes up the rate. MediaConnect defines this value in the offering.
Type: String
Valid Values: `HOURLY`
Required: Yes

 ** reservationArn **   <a name="mediaconnect-Type-Reservation-reservationArn"></a>
 The Amazon Resource Name (ARN) that MediaConnect assigns to the reservation when you purchase an offering.
Type: String
Required: Yes

 ** reservationName **   <a name="mediaconnect-Type-Reservation-reservationName"></a>
 The name that you assigned to the reservation when you purchased the offering.
Type: String
Required: Yes

 ** reservationState **   <a name="mediaconnect-Type-Reservation-reservationState"></a>
 The status of your reservation.
Type: String
Valid Values: `ACTIVE | EXPIRED | PROCESSING | CANCELED`
Required: Yes

 ** resourceSpecification **   <a name="mediaconnect-Type-Reservation-resourceSpecification"></a>
 A definition of the amount of outbound bandwidth that you would be reserving if you purchase the offering. MediaConnect defines the values that make up the resourceSpecification in the offering.
Type: [ResourceSpecification](API_ResourceSpecification.md) object
Required: Yes

 ** start **   <a name="mediaconnect-Type-Reservation-start"></a>
 The day and time that the reservation becomes active. You set this value when you purchase the offering.
Type: String
Required: Yes

## See Also
<a name="API_Reservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Reservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Reservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Reservation)
