---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_OptimizeWaypoints.html
---

# OptimizeWaypoints
<a name="API_OptimizeWaypoints"></a>

 `OptimizeWaypoints` calculates the optimal order to travel between a set of waypoints to minimize either the travel time or the distance travelled during the journey, based on road network restrictions and the traffic pattern data.

For more information, see [Optimize waypoints](https://docs.aws.amazon.com/location/latest/developerguide/actions-optimize-waypoints.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_OptimizeWaypoints_RequestSyntax"></a>

```
POST /v2/optimize-waypoints?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "Avoid": {
      "Areas": [
         {
            "Geometry": {
               "BoundingBox": [ {{number}} ]
            }
         }
      ],
      "CarShuttleTrains": {{boolean}},
      "ControlledAccessHighways": {{boolean}},
      "DirtRoads": {{boolean}},
      "Ferries": {{boolean}},
      "TollRoads": {{boolean}},
      "Tunnels": {{boolean}},
      "UTurns": {{boolean}}
   },
   "Clustering": {
      "Algorithm": "{{string}}",
      "DrivingDistanceOptions": {
         "DrivingDistance": {{number}}
      }
   },
   "DepartureTime": "{{string}}",
   "Destination": [ {{number}} ],
   "DestinationOptions": {
      "AccessHours": {
         "From": {
            "DayOfWeek": "{{string}}",
            "TimeOfDay": "{{string}}"
         },
         "To": {
            "DayOfWeek": "{{string}}",
            "TimeOfDay": "{{string}}"
         }
      },
      "AppointmentTime": "{{string}}",
      "Heading": {{number}},
      "Id": "{{string}}",
      "ServiceDuration": {{number}},
      "SideOfStreet": {
         "Position": [ {{number}} ],
         "UseWith": "{{string}}"
      }
   },
   "Driver": {
      "RestCycles": {
         "LongCycle": {
            "RestDuration": {{number}},
            "WorkDuration": {{number}}
         },
         "ShortCycle": {
            "RestDuration": {{number}},
            "WorkDuration": {{number}}
         }
      },
      "RestProfile": {
         "Profile": "{{string}}"
      },
      "TreatServiceTimeAs": "{{string}}"
   },
   "Exclude": {
      "Countries": [ "{{string}}" ]
   },
   "OptimizeSequencingFor": "{{string}}",
   "Origin": [ {{number}} ],
   "OriginOptions": {
      "Id": "{{string}}"
   },
   "Traffic": {
      "Usage": "{{string}}"
   },
   "TravelMode": "{{string}}",
   "TravelModeOptions": {
      "Pedestrian": {
         "Speed": {{number}}
      },
      "Truck": {
         "GrossWeight": {{number}},
         "HazardousCargos": [ "{{string}}" ],
         "Height": {{number}},
         "Length": {{number}},
         "Trailer": {
            "TrailerCount": {{number}}
         },
         "TruckType": "{{string}}",
         "TunnelRestrictionCode": "{{string}}",
         "WeightPerAxle": {{number}},
         "Width": {{number}}
      }
   },
   "Waypoints": [
      {
         "AccessHours": {
            "From": {
               "DayOfWeek": "{{string}}",
               "TimeOfDay": "{{string}}"
            },
            "To": {
               "DayOfWeek": "{{string}}",
               "TimeOfDay": "{{string}}"
            }
         },
         "AppointmentTime": "{{string}}",
         "Before": [ {{number}} ],
         "Heading": {{number}},
         "Id": "{{string}}",
         "Position": [ {{number}} ],
         "ServiceDuration": {{number}},
         "SideOfStreet": {
            "Position": [ {{number}} ],
            "UseWith": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_OptimizeWaypoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_OptimizeWaypoints_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Avoid](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Avoid"></a>
Features that are avoided. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, this setting is ignored.
Type: [WaypointOptimizationAvoidanceOptions](API_WaypointOptimizationAvoidanceOptions.md) object
Required: No

 ** [Clustering](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Clustering"></a>
Clustering allows you to specify how nearby waypoints can be clustered to improve the optimized sequence.
Type: [WaypointOptimizationClusteringOptions](API_WaypointOptimizationClusteringOptions.md) object
Required: No

 ** [DepartureTime](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-DepartureTime"></a>
Departure time from the waypoint.
Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** [Destination](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Destination"></a>
The final position for the route in the World Geodetic System (WGS 84) format: `[longitude, latitude]`.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** [DestinationOptions](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-DestinationOptions"></a>
Destination related options.
Type: [WaypointOptimizationDestinationOptions](API_WaypointOptimizationDestinationOptions.md) object
Required: No

 ** [Driver](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Driver"></a>
Driver related options.
Type: [WaypointOptimizationDriverOptions](API_WaypointOptimizationDriverOptions.md) object
Required: No

 ** [Exclude](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Exclude"></a>
Features to be strictly excluded while calculating the route.
Type: [WaypointOptimizationExclusionOptions](API_WaypointOptimizationExclusionOptions.md) object
Required: No

 ** [OptimizeSequencingFor](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-OptimizeSequencingFor"></a>
Specifies the optimization criteria for the calculated sequence.
Default value: `FastestRoute`.
Type: String
Valid Values: `FastestRoute | ShortestRoute`
Required: No

 ** [Origin](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Origin"></a>
The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** [OriginOptions](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-OriginOptions"></a>
Origin related options.
Type: [WaypointOptimizationOriginOptions](API_WaypointOptimizationOriginOptions.md) object
Required: No

 ** [Traffic](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Traffic"></a>
Traffic-related options.
Type: [WaypointOptimizationTrafficOptions](API_WaypointOptimizationTrafficOptions.md) object
Required: No

 ** [TravelMode](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-TravelMode"></a>
Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.
Default value: `Car`
Type: String
Valid Values: `Car | Pedestrian | Scooter | Truck`
Required: No

 ** [TravelModeOptions](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-TravelModeOptions"></a>
Travel mode related options for the provided travel mode.
Type: [WaypointOptimizationTravelModeOptions](API_WaypointOptimizationTravelModeOptions.md) object
Required: No

 ** [Waypoints](#API_OptimizeWaypoints_RequestSyntax) **   <a name="location-OptimizeWaypoints-request-Waypoints"></a>
List of waypoints between the `Origin` and `Destination`, in World Geodetic System (WGS 84) format: [longitude, latitude].
The maximum number of waypoints allowed per request:
+ Maximum 50 waypoints per request
+ Maximum 20 waypoints when using constraints (`AccessHours`, `AppointmentTime`, `ServiceDuration`, `Heading`, `SideOfStreet`, `Before`)
Type: Array of [WaypointOptimizationWaypoint](API_WaypointOptimizationWaypoint.md) objects
Required: No

## Response Syntax
<a name="API_OptimizeWaypoints_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "Connections": [
      {
         "Distance": number,
         "From": "string",
         "RestDuration": number,
         "To": "string",
         "TravelDuration": number,
         "WaitDuration": number
      }
   ],
   "Distance": number,
   "Duration": number,
   "ImpedingWaypoints": [
      {
         "FailedConstraints": [
            {
               "Constraint": "string",
               "Reason": "string"
            }
         ],
         "Id": "string",
         "Position": [ number ]
      }
   ],
   "OptimizedWaypoints": [
      {
         "ArrivalTime": "string",
         "ClusterIndex": number,
         "DepartureTime": "string",
         "Id": "string",
         "Position": [ number ]
      }
   ],
   "TimeBreakdown": {
      "RestDuration": number,
      "ServiceDuration": number,
      "TravelDuration": number,
      "WaitDuration": number
   }
}
```

## Response Elements
<a name="API_OptimizeWaypoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_OptimizeWaypoints_ResponseSyntax) **   <a name="location-OptimizeWaypoints-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.

The following data is returned in JSON format by the service.

 ** [Connections](#API_OptimizeWaypoints_ResponseSyntax) **   <a name="location-OptimizeWaypoints-response-Connections"></a>
Details about the connection from one waypoint to the next, within the optimized sequence.
Type: Array of [WaypointOptimizationConnection](API_WaypointOptimizationConnection.md) objects

 ** [Distance](#API_OptimizeWaypoints_ResponseSyntax) **   <a name="location-OptimizeWaypoints-response-Distance"></a>
Overall distance to travel the whole sequence.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.

 ** [Duration](#API_OptimizeWaypoints_ResponseSyntax) **   <a name="location-OptimizeWaypoints-response-Duration"></a>
Overall duration to travel the whole sequence.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.

 ** [ImpedingWaypoints](#API_OptimizeWaypoints_ResponseSyntax) **   <a name="location-OptimizeWaypoints-response-ImpedingWaypoints"></a>
Returns waypoints that caused the optimization problem to fail, and the constraints that were unsatisfied leading to the failure.
Type: Array of [WaypointOptimizationImpedingWaypoint](API_WaypointOptimizationImpedingWaypoint.md) objects

 ** [OptimizedWaypoints](#API_OptimizeWaypoints_ResponseSyntax) **   <a name="location-OptimizeWaypoints-response-OptimizedWaypoints"></a>
Waypoints in the order of the optimized sequence.
Type: Array of [WaypointOptimizationOptimizedWaypoint](API_WaypointOptimizationOptimizedWaypoint.md) objects

 ** [TimeBreakdown](#API_OptimizeWaypoints_ResponseSyntax) **   <a name="location-OptimizeWaypoints-response-TimeBreakdown"></a>
Time breakdown for the sequence.
Type: [WaypointOptimizationTimeBreakdown](API_WaypointOptimizationTimeBreakdown.md) object

## Errors
<a name="API_OptimizeWaypoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_OptimizeWaypoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-routes-2020-11-19/OptimizeWaypoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/OptimizeWaypoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
