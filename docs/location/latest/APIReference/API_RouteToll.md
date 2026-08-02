---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteToll.html
---

# RouteToll
<a name="API_RouteToll"></a>

Provides details about toll information along a route, including the payment sites, applicable toll rates, toll systems, and the country associated with the toll collection.

## Contents
<a name="API_RouteToll_Contents"></a>

 ** PaymentSites **   <a name="location-Type-RouteToll-PaymentSites"></a>
Locations or sites where the toll fare is collected.
Type: Array of [RouteTollPaymentSite](API_RouteTollPaymentSite.md) objects
Required: Yes

 ** Rates **   <a name="location-Type-RouteToll-Rates"></a>
Toll rates that need to be paid to travel this leg of the route.
Type: Array of [RouteTollRate](API_RouteTollRate.md) objects
Required: Yes

 ** Systems **   <a name="location-Type-RouteToll-Systems"></a>
Toll systems are authorities that collect payments for the toll.
Type: Array of integers
Required: Yes

 ** Country **   <a name="location-Type-RouteToll-Country"></a>
The alpha-2 or alpha-3 character code for the country.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`
Required: No

## See Also
<a name="API_RouteToll_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteToll)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteToll)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteToll)
