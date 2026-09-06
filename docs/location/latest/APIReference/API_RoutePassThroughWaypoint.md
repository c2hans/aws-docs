---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePassThroughWaypoint.html
---

# RoutePassThroughWaypoint
<a name="API_RoutePassThroughWaypoint"></a>

If the waypoint should be treated as a stop. If yes, the route is split up into different legs around the stop.

## Contents
<a name="API_RoutePassThroughWaypoint_Contents"></a>

 ** Place **   <a name="location-Type-RoutePassThroughWaypoint-Place"></a>
Place details corresponding to the pass-through waypoint.
Type: [RoutePassThroughPlace](API_RoutePassThroughPlace.md) object
Required: Yes

 ** GeometryOffset **   <a name="location-Type-RoutePassThroughWaypoint-GeometryOffset"></a>
Offset in the leg geometry corresponding to the start of this step.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RoutePassThroughWaypoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoutePassThroughWaypoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoutePassThroughWaypoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoutePassThroughWaypoint)
