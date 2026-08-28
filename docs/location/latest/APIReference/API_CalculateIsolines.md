---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateIsolines.html
---

# CalculateIsolines
<a name="API_CalculateIsolines"></a>

Calculates areas that can be reached within specified time or distance thresholds from a given point. For example, you can use this operation to determine the area within a 30-minute drive of a store location, find neighborhoods within walking distance of a school, or identify delivery zones based on drive time.

Isolines (also known as isochrones for time-based calculations) are useful for various applications including:
+ Service area visualization - Show customers the area you can serve within promised delivery times
+ Site selection - Analyze potential business locations based on population within travel distance
+ Site selection - Determine areas that can be reached within specified response times

**Note**
Route preferences such as avoiding toll roads or ferries are treated as preferences rather than absolute restrictions. If a viable route cannot be calculated while honoring all preferences, some may be ignored.

For more information, see [Calculate isolines](https://docs.aws.amazon.com/location/latest/developerguide/calculate-isolines.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_CalculateIsolines_RequestSyntax"></a>

```
POST /v2/isolines?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "Allow": {
      "Hot": {{boolean}},
      "Hov": {{boolean}}
   },
   "ArrivalTime": "{{string}}",
   "Avoid": {
      "Areas": [
         {
            "Except": [
               {
                  "BoundingBox": [ {{number}} ],
                  "Corridor": {
                     "LineString": [
                        [ {{number}} ]
                     ],
                     "Radius": {{number}}
                  },
                  "Polygon": [
                     [
                        [ {{number}} ]
                     ]
                  ],
                  "PolylineCorridor": {
                     "Polyline": "{{string}}",
                     "Radius": {{number}}
                  },
                  "PolylinePolygon": [ "{{string}}" ]
               }
            ],
            "Geometry": {
               "BoundingBox": [ {{number}} ],
               "Corridor": {
                  "LineString": [
                     [ {{number}} ]
                  ],
                  "Radius": {{number}}
               },
               "Polygon": [
                  [
                     [ {{number}} ]
                  ]
               ],
               "PolylineCorridor": {
                  "Polyline": "{{string}}",
                  "Radius": {{number}}
               },
               "PolylinePolygon": [ "{{string}}" ]
            }
         }
      ],
      "CarShuttleTrains": {{boolean}},
      "ControlledAccessHighways": {{boolean}},
      "DirtRoads": {{boolean}},
      "Ferries": {{boolean}},
      "SeasonalClosure": {{boolean}},
      "TollRoads": {{boolean}},
      "TollTransponders": {{boolean}},
      "TruckRoadTypes": [ "{{string}}" ],
      "Tunnels": {{boolean}},
      "UTurns": {{boolean}},
      "ZoneCategories": [
         {
            "Category": "{{string}}"
         }
      ]
   },
   "DepartNow": {{boolean}},
   "DepartureTime": "{{string}}",
   "Destination": [ {{number}} ],
   "DestinationOptions": {
      "AvoidActionsForDistance": {{number}},
      "Heading": {{number}},
      "Matching": {
         "NameHint": "{{string}}",
         "OnRoadThreshold": {{number}},
         "Radius": {{number}},
         "Strategy": "{{string}}"
      },
      "SideOfStreet": {
         "Position": [ {{number}} ],
         "UseWith": "{{string}}"
      }
   },
   "IsolineGeometryFormat": "{{string}}",
   "IsolineGranularity": {
      "MaxPoints": {{number}},
      "MaxResolution": {{number}}
   },
   "OptimizeIsolineFor": "{{string}}",
   "OptimizeRoutingFor": "{{string}}",
   "Origin": [ {{number}} ],
   "OriginOptions": {
      "AvoidActionsForDistance": {{number}},
      "Heading": {{number}},
      "Matching": {
         "NameHint": "{{string}}",
         "OnRoadThreshold": {{number}},
         "Radius": {{number}},
         "Strategy": "{{string}}"
      },
      "SideOfStreet": {
         "Position": [ {{number}} ],
         "UseWith": "{{string}}"
      }
   },
   "Thresholds": {
      "Distance": [ {{number}} ],
      "Time": [ {{number}} ]
   },
   "Traffic": {
      "FlowEventThresholdOverride": {{number}},
      "Usage": "{{string}}"
   },
   "TravelMode": "{{string}}",
   "TravelModeOptions": {
      "Car": {
         "EngineType": "{{string}}",
         "LicensePlate": {
            "LastCharacter": "{{string}}"
         },
         "MaxSpeed": {{number}},
         "Occupancy": {{number}}
      },
      "Scooter": {
         "EngineType": "{{string}}",
         "LicensePlate": {
            "LastCharacter": "{{string}}"
         },
         "MaxSpeed": {{number}},
         "Occupancy": {{number}}
      },
      "Truck": {
         "AxleCount": {{number}},
         "EngineType": "{{string}}",
         "GrossWeight": {{number}},
         "HazardousCargos": [ "{{string}}" ],
         "Height": {{number}},
         "HeightAboveFirstAxle": {{number}},
         "KpraLength": {{number}},
         "Length": {{number}},
         "LicensePlate": {
            "LastCharacter": "{{string}}"
         },
         "MaxSpeed": {{number}},
         "Occupancy": {{number}},
         "PayloadCapacity": {{number}},
         "TireCount": {{number}},
         "Trailer": {
            "AxleCount": {{number}},
            "TrailerCount": {{number}}
         },
         "TruckType": "{{string}}",
         "TunnelRestrictionCode": "{{string}}",
         "WeightPerAxle": {{number}},
         "WeightPerAxleGroup": {
            "Quad": {{number}},
            "Quint": {{number}},
            "Single": {{number}},
            "Tandem": {{number}},
            "Triple": {{number}}
         },
         "Width": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_CalculateIsolines_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-uri-Key"></a>
An Amazon Location Service API Key with access to this action. If omitted, the request must be signed using Signature Version 4.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_CalculateIsolines_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Allow](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-Allow"></a>
Enables special road types or features that should be considered for routing even if they might be restricted by default for the selected travel mode. These include high-occupancy vehicle and toll lanes.
Type: [IsolineAllowOptions](API_IsolineAllowOptions.md) object
Required: No

 ** [ArrivalTime](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-ArrivalTime"></a>
Determine areas from which `Destination` can be reached by this time, taking into account predicted traffic conditions and working backward to account for congestion patterns. This attribute cannot be used together with `DepartureTime` or `DepartNow`. Specified as an ISO-8601 timestamp with timezone offset.
Time format: `YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** [Avoid](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-Avoid"></a>
Specifies road types, features, or areas to avoid (if possible) when calculating reachable areas. These are treated as preferences rather than strict constraints—if a route cannot be calculated without using an avoided feature, that avoidance preference may be ignored.
Type: [IsolineAvoidanceOptions](API_IsolineAvoidanceOptions.md) object
Required: No

 ** [DepartNow](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-DepartNow"></a>
When true, uses the current time as the departure time and takes current traffic conditions into account. This attribute cannot be used together with `DepartureTime` or `ArrivalTime`.
Type: Boolean
Required: No

 ** [DepartureTime](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-DepartureTime"></a>
Determine areas that can be reached when departing at this time, taking into account predicted traffic conditions. This attribute cannot be used together with `ArrivalTime` or `DepartNow`. Specified as an ISO-8601 timestamp with timezone offset.
Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** [Destination](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-Destination"></a>
An optional destination point, specified as `[longitude, latitude]` coordinates. When provided, the service calculates areas from which this destination can be reached within the specified thresholds. This reverses the usual isoline calculation to show areas that could reach your location, rather than areas you could reach from your location. Either `Origin` or `Destination` must be provided.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** [DestinationOptions](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-DestinationOptions"></a>
Options that control how the destination point is matched to the road network and how routes can approach it. These options help improve travel time accuracy by accounting for real-world access to the destination.
Type: [IsolineDestinationOptions](API_IsolineDestinationOptions.md) object
Required: No

 ** [IsolineGeometryFormat](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-IsolineGeometryFormat"></a>
The format of the returned IsolineGeometry.
Default value:`FlexiblePolyline`
Type: String
Valid Values: `FlexiblePolyline | Simple`
Required: No

 ** [IsolineGranularity](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-IsolineGranularity"></a>
Controls the detail level of the generated isolines. Higher granularity produces smoother shapes but requires more processing time and results in larger responses.
Type: [IsolineGranularityOptions](API_IsolineGranularityOptions.md) object
Required: No

 ** [OptimizeIsolineFor](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-OptimizeIsolineFor"></a>
Controls the trade-off between calculation speed and isoline precision. Choose ` FastCalculation` for quicker results with less detail, `AccurateCalculation` for more precise results, or `BalancedCalculation` for a middle ground.
Default value: `BalancedCalculation`
Type: String
Valid Values: `AccurateCalculation | BalancedCalculation | FastCalculation`
Required: No

 ** [OptimizeRoutingFor](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-OptimizeRoutingFor"></a>
Determines whether routes prioritize shortest travel time (`FastestRoute`) or shortest physical distance (`ShortestRoute`) when calculating reachable areas.
Default value: `FastestRoute`
Type: String
Valid Values: `FastestRoute | ShortestRoute`
Required: No

 ** [Origin](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-Origin"></a>
The starting point for isoline calculations, specified as `[longitude, latitude]` coordinates. For example, this could be a store location, service center, or any point from which you want to calculate reachable areas. Either `Origin` or `Destination` must be provided.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** [OriginOptions](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-OriginOptions"></a>
Options that control how the origin point is matched to the road network and how routes can depart from it. These options help improve travel time accuracy by accounting for real-world access from the origin.
Type: [IsolineOriginOptions](API_IsolineOriginOptions.md) object
Required: No

 ** [Thresholds](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-Thresholds"></a>
The distance or time thresholds used to determine reachable areas. You can specify up to five thresholds (which all must be the same type) to calculate multiple isolines in a single request. For example, to determine the areas that are reachable within 10 and 20 minutes of the origin, specify time thresholds of 600 and 1200 seconds.
You incur a calculation charge for each threshold. Using a large number of thresholds in a request can lead to unexpected charges. For more information, see [Routes pricing](https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html) in the *Amazon Location Service Developer Guide*.
Type: [IsolineThresholds](API_IsolineThresholds.md) object
Required: Yes

 ** [Traffic](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-Traffic"></a>
Configures how real-time and historical traffic data affects isoline calculations. Traffic patterns can significantly impact reachable areas, especially during peak hours.
Type: [IsolineTrafficOptions](API_IsolineTrafficOptions.md) object
Required: No

 ** [TravelMode](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-TravelMode"></a>
The mode of transportation to use for calculations. This affects which road types or features can be used, estimated speed, and the traffic levels that are applied.
+  `Car`—Standard passenger vehicle routing using roads accessible to cars
+  `Pedestrian`—Walking routes using pedestrian paths, sidewalks, and crossings
+  `Scooter`—Light two-wheeled vehicle routing using roads and paths accessible to scooters
+  `Truck`—Commercial truck routing considering vehicle dimensions, weight restrictions, and hazardous material regulations
The mode `Scooter` also applies to motorcycles; set this to `Scooter` when calculating isolines for motorcycles.
Default value: `Car`
Type: String
Valid Values: `Car | Pedestrian | Scooter | Truck`
Required: No

 ** [TravelModeOptions](#API_CalculateIsolines_RequestSyntax) **   <a name="location-CalculateIsolines-request-TravelModeOptions"></a>
Additional attributes that refine how reachable areas are calculated based on specific vehicle characteristics. These options help produce more accurate results by accounting for real-world constraints and capabilities.
For example:
+ For trucks (`Truck`), specify dimensions, weight limits, and hazardous cargo restrictions to ensure isolines only include roads that can physically and legally accommodate the vehicle
+ For cars (`Car`), set maximum speed capabilities or indicate high-occupancy vehicle eligibility to better estimate reachable areas
+ For scooters (`Scooter`), specify engine type and speed limitations to more accurately model their travel capabilities
Without these options, calculations use default assumptions that may not match your specific use case.
Type: [IsolineTravelModeOptions](API_IsolineTravelModeOptions.md) object
Required: No

## Response Syntax
<a name="API_CalculateIsolines_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "ArrivalTime": "string",
   "DepartureTime": "string",
   "IsolineGeometryFormat": "string",
   "Isolines": [
      {
         "Connections": [
            {
               "FromPolygonIndex": number,
               "Geometry": {
                  "LineString": [
                     [ number ]
                  ],
                  "Polyline": "string"
               },
               "ToPolygonIndex": number
            }
         ],
         "DistanceThreshold": number,
         "Geometries": [
            {
               "Polygon": [
                  [
                     [ number ]
                  ]
               ],
               "PolylinePolygon": [ "string" ]
            }
         ],
         "TimeThreshold": number
      }
   ],
   "SnappedDestination": [ number ],
   "SnappedOrigin": [ number ]
}
```

## Response Elements
<a name="API_CalculateIsolines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_CalculateIsolines_ResponseSyntax) **   <a name="location-CalculateIsolines-response-PricingBucket"></a>
The pricing bucket applied to this calculation. Different buckets apply based on the travel mode and thresholds used.

The following data is returned in JSON format by the service.

 ** [ArrivalTime](#API_CalculateIsolines_ResponseSyntax) **   <a name="location-CalculateIsolines-response-ArrivalTime"></a>
Time of arrival at the destination, used for traffic calculations. This attribute is returned only if the `Destination` and `ArrivalTime` attributes were provided in the request.
Time format: `YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`

 ** [DepartureTime](#API_CalculateIsolines_ResponseSyntax) **   <a name="location-CalculateIsolines-response-DepartureTime"></a>
Time of departure from the origin, used for traffic calculations. This attribute is returned when `Origin` was provided in the request and either a specific departure time was requested (`DepartureTime`) or `DepartNow` was set to true.
Time format: `YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`

 ** [IsolineGeometryFormat](#API_CalculateIsolines_ResponseSyntax) **   <a name="location-CalculateIsolines-response-IsolineGeometryFormat"></a>
The format of the returned geometries, matching the format specified in the request. Either ` FlexiblePolyline` for compact encoding or `Simple` for GeoJSON-compatible coordinates.
Default value:`FlexiblePolyline`
Type: String
Valid Values: `FlexiblePolyline | Simple`

 ** [Isolines](#API_CalculateIsolines_ResponseSyntax) **   <a name="location-CalculateIsolines-response-Isolines"></a>
Reachable areas, or isolines, for each threshold specified in the request.
Type: Array of [Isoline](API_Isoline.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [SnappedDestination](#API_CalculateIsolines_ResponseSyntax) **   <a name="location-CalculateIsolines-response-SnappedDestination"></a>
The actual point on the road network used for calculations, which may differ from the requested destination if `Destination` was not directly on a road.
Type: Array of doubles
Array Members: Fixed number of 2 items.

 ** [SnappedOrigin](#API_CalculateIsolines_ResponseSyntax) **   <a name="location-CalculateIsolines-response-SnappedOrigin"></a>
The actual point on the road network used for calculations, which may differ from the requested origin if `Origin` was not directly on a road.
Type: Array of doubles
Array Members: Fixed number of 2 items.

## Errors
<a name="API_CalculateIsolines_Errors"></a>

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
<a name="API_CalculateIsolines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-routes-2020-11-19/CalculateIsolines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/CalculateIsolines)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
