---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationWaypoint.html
---

# WaypointOptimizationWaypoint
<a name="API_WaypointOptimizationWaypoint"></a>

Waypoint between the Origin and Destination.

## Contents
<a name="API_WaypointOptimizationWaypoint_Contents"></a>

 ** Position **   <a name="location-Type-WaypointOptimizationWaypoint-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** AccessHours **   <a name="location-Type-WaypointOptimizationWaypoint-AccessHours"></a>
Access hours corresponding to when a waypoint can be visited.
Type: [WaypointOptimizationAccessHours](API_WaypointOptimizationAccessHours.md) object
Required: No

 ** AppointmentTime **   <a name="location-Type-WaypointOptimizationWaypoint-AppointmentTime"></a>
Appointment time at the waypoint.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** Before **   <a name="location-Type-WaypointOptimizationWaypoint-Before"></a>
Constraint defining what waypoints are to be visited after this waypoint.
Type: Array of integers
Required: No

 ** Heading **   <a name="location-Type-WaypointOptimizationWaypoint-Heading"></a>
GPS Heading at the position.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Id **   <a name="location-Type-WaypointOptimizationWaypoint-Id"></a>
The waypoint Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^,;!]+`
Required: No

 ** ServiceDuration **   <a name="location-Type-WaypointOptimizationWaypoint-ServiceDuration"></a>
Service time spent at the waypoint. At an appointment, the service time should be the appointment duration.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** SideOfStreet **   <a name="location-Type-WaypointOptimizationWaypoint-SideOfStreet"></a>
Options to configure matching the provided position to a side of the street.
Type: [WaypointOptimizationSideOfStreetOptions](API_WaypointOptimizationSideOfStreetOptions.md) object
Required: No

## See Also
<a name="API_WaypointOptimizationWaypoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationWaypoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationWaypoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationWaypoint)
