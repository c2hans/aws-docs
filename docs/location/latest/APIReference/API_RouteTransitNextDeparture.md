---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitNextDeparture.html
---

# RouteTransitNextDeparture
<a name="API_RouteTransitNextDeparture"></a>

Details about the next available departure for the transit service.

## Contents
<a name="API_RouteTransitNextDeparture_Contents"></a>

 ** Time **   <a name="location-Type-RouteTransitNextDeparture-Time"></a>
The departure time.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: Yes

 ** Delay **   <a name="location-Type-RouteTransitNextDeparture-Delay"></a>
The delay from the scheduled departure time.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** PlatformName **   <a name="location-Type-RouteTransitNextDeparture-PlatformName"></a>
Platform name or number for the departure.
Type: String
Required: No

 ** Status **   <a name="location-Type-RouteTransitNextDeparture-Status"></a>
The status of the departure.
Type: String
Valid Values: `Added | Cancelled | Replaced | Scheduled`
Required: No

 ** Transport **   <a name="location-Type-RouteTransitNextDeparture-Transport"></a>
Transport mode details for this departure.
Type: [RouteTransitTransportModeDetails](API_RouteTransitTransportModeDetails.md) object
Required: No

## See Also
<a name="API_RouteTransitNextDeparture_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitNextDeparture)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitNextDeparture)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitNextDeparture)
