---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationOptimizedWaypoint.html
---

# WaypointOptimizationOptimizedWaypoint
<a name="API_WaypointOptimizationOptimizedWaypoint"></a>

The optimized waypoint.

## Contents
<a name="API_WaypointOptimizationOptimizedWaypoint_Contents"></a>

 ** DepartureTime **   <a name="location-Type-WaypointOptimizationOptimizedWaypoint-DepartureTime"></a>
Estimated time of departure from the origin.
Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: Yes

 ** Id **   <a name="location-Type-WaypointOptimizationOptimizedWaypoint-Id"></a>
The waypoint Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^,;!]+`
Required: Yes

 ** Position **   <a name="location-Type-WaypointOptimizationOptimizedWaypoint-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** ArrivalTime **   <a name="location-Type-WaypointOptimizationOptimizedWaypoint-ArrivalTime"></a>
Estimated time of arrival at the destination.
Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** ClusterIndex **   <a name="location-Type-WaypointOptimizationOptimizedWaypoint-ClusterIndex"></a>
Index of the cluster the waypoint is associated with. The index is included in the response only if clustering was performed while processing the request.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_WaypointOptimizationOptimizedWaypoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationOptimizedWaypoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationOptimizedWaypoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationOptimizedWaypoint)
