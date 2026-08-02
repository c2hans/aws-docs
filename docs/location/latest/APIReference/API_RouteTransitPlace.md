---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitPlace.html
---

# RouteTransitPlace
<a name="API_RouteTransitPlace"></a>

Place details corresponding to the arrival or departure.

## Contents
<a name="API_RouteTransitPlace_Contents"></a>

 ** Position **   <a name="location-Type-RouteTransitPlace-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: Yes

 ** Name **   <a name="location-Type-RouteTransitPlace-Name"></a>
The name of the place.
Type: String
Required: No

 ** OriginalPosition **   <a name="location-Type-RouteTransitPlace-OriginalPosition"></a>
Position provided in the request.
Type: Array of doubles
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: No

 ** StationDetails **   <a name="location-Type-RouteTransitPlace-StationDetails"></a>
Details about the station.
Type: [RouteStationDetails](API_RouteStationDetails.md) object
Required: No

 ** Type **   <a name="location-Type-RouteTransitPlace-Type"></a>
The type of the place.
Type: String
Valid Values: `Station`
Required: No

 ** WaypointIndex **   <a name="location-Type-RouteTransitPlace-WaypointIndex"></a>
Index of the waypoint in the request.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RouteTransitPlace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitPlace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitPlace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitPlace)
