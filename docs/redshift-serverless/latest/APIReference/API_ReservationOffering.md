---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ReservationOffering.html
---

# ReservationOffering
<a name="API_ReservationOffering"></a>

The class of offering for the reservation. The offering class determines the payment schedule for the reservation.

## Contents
<a name="API_ReservationOffering_Contents"></a>

 ** currencyCode **   <a name="redshiftserverless-Type-ReservationOffering-currencyCode"></a>
The currency code for the offering.
Type: String
Required: No

 ** duration **   <a name="redshiftserverless-Type-ReservationOffering-duration"></a>
The duration, in seconds, for which the reservation reserves the RPUs.
Type: Integer
Required: No

 ** hourlyCharge **   <a name="redshiftserverless-Type-ReservationOffering-hourlyCharge"></a>
The rate you are charged for each hour the reservation is active.
Type: Double
Required: No

 ** offeringId **   <a name="redshiftserverless-Type-ReservationOffering-offeringId"></a>
The offering identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** offeringType **   <a name="redshiftserverless-Type-ReservationOffering-offeringType"></a>
Determines the payment schedule for the reservation.
Type: String
Valid Values: `ALL_UPFRONT | NO_UPFRONT`
Required: No

 ** upfrontCharge **   <a name="redshiftserverless-Type-ReservationOffering-upfrontCharge"></a>
The up-front price you are charged for the reservation.
Type: Double
Required: No

## See Also
<a name="API_ReservationOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ReservationOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ReservationOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ReservationOffering)
