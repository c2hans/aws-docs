---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_Leg.html
---

# Leg
<a name="API_Leg"></a>

Contains the calculated route's details for each path between a pair of positions. The number of legs returned corresponds to one fewer than the total number of positions in the request.

For example, a route with a departure position and destination position returns one leg with the positions [snapped to a nearby road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html):
+ The `StartPosition` is the departure position.
+ The `EndPosition` is the destination position.

A route with a waypoint between the departure and destination position returns two legs with the positions snapped to a nearby road:
+ Leg 1: The `StartPosition` is the departure position . The `EndPosition` is the waypoint positon.
+ Leg 2: The `StartPosition` is the waypoint position. The `EndPosition` is the destination position.

## Contents
<a name="API_Leg_Contents"></a>

 ** Distance **   <a name="location-Type-Leg-Distance"></a>
The distance between the leg's `StartPosition` and `EndPosition` along a calculated route.
+ The default measurement is `Kilometers` unless the request specifies a `DistanceUnit` of `Miles`.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** DurationSeconds **   <a name="location-Type-Leg-DurationSeconds"></a>
The estimated travel time between the leg's `StartPosition` and `EndPosition`. The travel mode and departure time that you specify in the request determines the calculated time.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** EndPosition **   <a name="location-Type-Leg-EndPosition"></a>
The terminating position of the leg. Follows the format `[longitude,latitude]`.
If the `EndPosition` isn't located on a road, it's [snapped to a nearby road](https://docs.aws.amazon.com/location/previous/developerguide/nap-to-nearby-road.html).
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** StartPosition **   <a name="location-Type-Leg-StartPosition"></a>
The starting position of the leg. Follows the format `[longitude,latitude]`.
If the `StartPosition` isn't located on a road, it's [snapped to a nearby road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html).
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** Steps **   <a name="location-Type-Leg-Steps"></a>
Contains a list of steps, which represent subsections of a leg. Each step provides instructions for how to move to the next step in the leg such as the step's start position, end position, travel distance, travel duration, and geometry offset.
Type: Array of [Step](API_Step.md) objects
Required: Yes

 ** Geometry **   <a name="location-Type-Leg-Geometry"></a>
Contains the calculated route's path as a linestring geometry.
Type: [LegGeometry](API_LegGeometry.md) object
Required: No

## See Also
<a name="API_Leg_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/Leg)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/Leg)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/Leg)
