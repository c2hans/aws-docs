---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteWaypoint.html
---

# RouteWaypoint
<a name="API_RouteWaypoint"></a>

Waypoint between the Origin and Destination.

## Contents
<a name="API_RouteWaypoint_Contents"></a>

 ** Position **   <a name="location-Type-RouteWaypoint-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** AvoidActionsForDistance **   <a name="location-Type-RouteWaypoint-AvoidActionsForDistance"></a>
 Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Long
Valid Range: Maximum value of 2000.
Required: No

 ** AvoidUTurns **   <a name="location-Type-RouteWaypoint-AvoidUTurns"></a>
 Avoid U-turns for calculation on highways and motorways. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** Heading **   <a name="location-Type-RouteWaypoint-Heading"></a>
 GPS Heading at the position. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Matching **   <a name="location-Type-RouteWaypoint-Matching"></a>
 Options to configure matching the provided position to the road network. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteMatchingOptions](API_RouteMatchingOptions.md) object
Required: No

 ** PassThrough **   <a name="location-Type-RouteWaypoint-PassThrough"></a>
 If the waypoint should not be treated as a stop. If yes, the waypoint is passed through and doesn't split the route into different legs. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** SideOfStreet **   <a name="location-Type-RouteWaypoint-SideOfStreet"></a>
 Options to configure matching the provided position to a side of the street. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteSideOfStreetOptions](API_RouteSideOfStreetOptions.md) object
Required: No

 ** StopDuration **   <a name="location-Type-RouteWaypoint-StopDuration"></a>
 Duration of the stop. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
 **Unit**: `seconds`
Type: Long
Valid Range: Maximum value of 49999.
Required: No

## See Also
<a name="API_RouteWaypoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteWaypoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteWaypoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteWaypoint)
