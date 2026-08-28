---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html
---

# CalculateRoute
<a name="API_CalculateRoute"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to [`CalculateRoutes`](/location/latest/APIReference/API_CalculateRoutes.html) or [`CalculateIsolines`](/location/latest/APIReference/API_CalculateIsolines.html) unless you require Grab data.
 `CalculateRoute` is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `CalculateRoutes` operation gives better results for point-to-point routing, while the version 2 `CalculateIsolines` operation adds support for calculating service areas and travel time envelopes.
If you are using an AWS SDK or the AWS CLI, note that the Routes API version 2 is found under `geo-routes` or `geo_routes`, not under `location`.
Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.

 [Calculates a route](https://docs.aws.amazon.com/location/previous/developerguide/calculate-route.html) given the following required parameters: `DeparturePosition` and `DestinationPosition`. Requires that you first [create a route calculator resource](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html).

By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating the route.

Additional options include:
+  [Specifying a departure time](https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html) using either `DepartureTime` or `DepartNow`. This calculates a route based on predictive traffic data at the given time.
**Note**
You can't specify both `DepartureTime` and `DepartNow` in a single request. Specifying both parameters returns a validation error.
+  [Specifying a travel mode](https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html) using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in `CarModeOptions` if traveling by `Car`, or `TruckModeOptions` if traveling by `Truck`.
**Note**
If you specify `walking` for the travel mode and your data provider is Esri, the start and destination must be within 40km.

## Request Syntax
<a name="API_CalculateRoute_RequestSyntax"></a>

```
POST /routes/v0/calculators/{{CalculatorName}}/calculate/route?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "ArrivalTime": "{{string}}",
   "CarModeOptions": {
      "AvoidFerries": {{boolean}},
      "AvoidTolls": {{boolean}}
   },
   "DepartNow": {{boolean}},
   "DeparturePosition": [ {{number}} ],
   "DepartureTime": "{{string}}",
   "DestinationPosition": [ {{number}} ],
   "DistanceUnit": "{{string}}",
   "IncludeLegGeometry": {{boolean}},
   "OptimizeFor": "{{string}}",
   "TravelMode": "{{string}}",
   "TruckModeOptions": {
      "AvoidFerries": {{boolean}},
      "AvoidTolls": {{boolean}},
      "Dimensions": {
         "Height": {{number}},
         "Length": {{number}},
         "Unit": "{{string}}",
         "Width": {{number}}
      },
      "Weight": {
         "Total": {{number}},
         "Unit": "{{string}}"
      }
   },
   "WaypointPositions": [
      [ {{number}} ]
   ]
}
```

## URI Request Parameters
<a name="API_CalculateRoute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CalculatorName](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-uri-CalculatorName"></a>
The name of the route calculator resource that you want to use to calculate the route.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [Key](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_CalculateRoute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ArrivalTime](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-ArrivalTime"></a>
Specifies the desired time of arrival. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.
ArrivalTime is not supported Esri.
Type: Timestamp
Required: No

 ** [CarModeOptions](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-CarModeOptions"></a>
Specifies route preferences when traveling by `Car`, such as avoiding routes that use ferries or tolls.
Requirements: `TravelMode` must be specified as `Car`.
Type: [CalculateRouteCarModeOptions](API_CalculateRouteCarModeOptions.md) object
Required: No

 ** [DepartNow](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-DepartNow"></a>
Sets the time of departure as the current time. Uses the current time to calculate a route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.
Default Value: `false`
Valid Values: `false` \| `true`
Type: Boolean
Required: No

 ** [DeparturePosition](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-DeparturePosition"></a>
The start position for the route. Defined in [World Geodetic System (WGS 84)](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format: `[longitude, latitude]`.
+ For example, `[-123.115, 49.285]`
If you specify a departure that's not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html). If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a `400 RoutesValidationException` error.
Valid Values: `[-180 to 180,-90 to 90]`
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** [DepartureTime](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-DepartureTime"></a>
Specifies the desired time of departure. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.
+ In [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`. For example, `2020–07-2T12:15:20.000Z+01:00`
Type: Timestamp
Required: No

 ** [DestinationPosition](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-DestinationPosition"></a>
The finish position for the route. Defined in [World Geodetic System (WGS 84)](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format: `[longitude, latitude]`.
+  For example, `[-122.339, 47.615]`
If you specify a destination that's not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html).
Valid Values: `[-180 to 180,-90 to 90]`
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** [DistanceUnit](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-DistanceUnit"></a>
Set the unit system to specify the distance.
Default Value: `Kilometers`
Type: String
Valid Values: `Kilometers | Miles`
Required: No

 ** [IncludeLegGeometry](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-IncludeLegGeometry"></a>
Set to include the geometry details in the result for each path between a pair of positions.
Default Value: `false`
Valid Values: `false` \| `true`
Type: Boolean
Required: No

 ** [OptimizeFor](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-OptimizeFor"></a>
Specifies the distance to optimize for when calculating a route.
Type: String
Valid Values: `FastestRoute | ShortestRoute`
Required: No

 ** [TravelMode](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-TravelMode"></a>
Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. You can choose `Car`, `Truck`, `Walking`, `Bicycle` or `Motorcycle` as options for the `TravelMode`.
 `Bicycle` and `Motorcycle` are only valid when using Grab as a data provider, and only within Southeast Asia.
 `Truck` is not available for Grab.
For more details on the using Grab for routing, including areas of coverage, see [GrabMaps](https://docs.aws.amazon.com/location/previous/developerguide/grab.html) in the *Amazon Location Service Developer Guide*.
The `TravelMode` you specify also determines how you specify route preferences:
+ If traveling by `Car` use the `CarModeOptions` parameter.
+ If traveling by `Truck` use the `TruckModeOptions` parameter.
Default Value: `Car`
Type: String
Valid Values: `Car | Truck | Walking | Bicycle | Motorcycle`
Required: No

 ** [TruckModeOptions](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-TruckModeOptions"></a>
Specifies route preferences when traveling by `Truck`, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.
Requirements: `TravelMode` must be specified as `Truck`.
Type: [CalculateRouteTruckModeOptions](API_CalculateRouteTruckModeOptions.md) object
Required: No

 ** [WaypointPositions](#API_CalculateRoute_RequestSyntax) **   <a name="location-CalculateRoute-request-WaypointPositions"></a>
Specifies an ordered list of up to 23 intermediate positions to include along a route between the departure position and destination position.
+ For example, from the `DeparturePosition` `[-123.115, 49.285]`, the route follows the order that the waypoint positions are given `[[-122.757, 49.0021],[-122.349, 47.620]]`
If you specify a waypoint position that's not located on a road, Amazon Location [moves the position to the nearest road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html).
Specifying more than 23 waypoints returns a `400 ValidationException` error.
If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a `400 RoutesValidationException` error.
Valid Values: `[-180 to 180,-90 to 90]`
Type: Array of arrays of doubles
Array Members: Minimum number of 0 items. Maximum number of 23 items.
Array Members: Fixed number of 2 items.
Required: No

## Response Syntax
<a name="API_CalculateRoute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Legs": [
      {
         "Distance": number,
         "DurationSeconds": number,
         "EndPosition": [ number ],
         "Geometry": {
            "LineString": [
               [ number ]
            ]
         },
         "StartPosition": [ number ],
         "Steps": [
            {
               "Distance": number,
               "DurationSeconds": number,
               "EndPosition": [ number ],
               "GeometryOffset": number,
               "StartPosition": [ number ]
            }
         ]
      }
   ],
   "Summary": {
      "DataSource": "string",
      "Distance": number,
      "DistanceUnit": "string",
      "DurationSeconds": number,
      "RouteBBox": [ number ]
   }
}
```

## Response Elements
<a name="API_CalculateRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Legs](#API_CalculateRoute_ResponseSyntax) **   <a name="location-CalculateRoute-response-Legs"></a>
Contains details about each path between a pair of positions included along a route such as: `StartPosition`, `EndPosition`, `Distance`, `DurationSeconds`, `Geometry`, and `Steps`. The number of legs returned corresponds to one fewer than the total number of positions in the request.
For example, a route with a departure position and destination position returns one leg with the positions [snapped to a nearby road](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html):
+ The `StartPosition` is the departure position.
+ The `EndPosition` is the destination position.
A route with a waypoint between the departure and destination position returns two legs with the positions snapped to a nearby road:
+ Leg 1: The `StartPosition` is the departure position . The `EndPosition` is the waypoint positon.
+ Leg 2: The `StartPosition` is the waypoint position. The `EndPosition` is the destination position.
Type: Array of [Leg](API_Leg.md) objects

 ** [Summary](#API_CalculateRoute_ResponseSyntax) **   <a name="location-CalculateRoute-response-Summary"></a>
Contains information about the whole route, such as: `RouteBBox`, `DataSource`, `Distance`, `DistanceUnit`, and `DurationSeconds`.
Type: [CalculateRouteSummary](API_CalculateRouteSummary.md) object

## Errors
<a name="API_CalculateRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_CalculateRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/CalculateRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/CalculateRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CalculateRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/CalculateRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CalculateRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/CalculateRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/CalculateRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/CalculateRoute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/CalculateRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CalculateRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
