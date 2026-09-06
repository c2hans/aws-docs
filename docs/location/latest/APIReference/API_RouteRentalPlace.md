---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRentalPlace.html
---

# RouteRentalPlace
<a name="API_RouteRentalPlace"></a>

Place details corresponding to the arrival or departure.

## Contents
<a name="API_RouteRentalPlace_Contents"></a>

 ** Position **   <a name="location-Type-RouteRentalPlace-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: Yes

 ** AccessPointDetails **   <a name="location-Type-RouteRentalPlace-AccessPointDetails"></a>
Details of the access point.
Type: [RouteAccessPointDetails](API_RouteAccessPointDetails.md) object
Required: No

 ** Name **   <a name="location-Type-RouteRentalPlace-Name"></a>
The name of the place.
Type: String
Required: No

 ** OriginalPosition **   <a name="location-Type-RouteRentalPlace-OriginalPosition"></a>
Position provided in the request.
Type: Array of doubles
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: No

 ** StationDetails **   <a name="location-Type-RouteRentalPlace-StationDetails"></a>
Details about the station.
Type: [RouteStationDetails](API_RouteStationDetails.md) object
Required: No

 ** Type **   <a name="location-Type-RouteRentalPlace-Type"></a>
The type of the place.
Type: String
Valid Values: `AccessPoint | DockingStation | ParkingLot | Station`
Required: No

 ** WaypointIndex **   <a name="location-Type-RouteRentalPlace-WaypointIndex"></a>
Index of the waypoint in the request.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RouteRentalPlace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteRentalPlace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteRentalPlace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteRentalPlace)
