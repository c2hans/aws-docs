---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html
---

# CalculateRoutes
<a name="API_CalculateRoutes"></a>

 `CalculateRoutes` computes routes given the following required parameters: `Origin` and `Destination`.

For more information, see [Calculate routes](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_CalculateRoutes_RequestSyntax"></a>

```
POST /v2/routes?key={{Key}} HTTP/1.1
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
      "AvoidUTurns": {{boolean}},
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
      },
      "StopDuration": {{number}}
   },
   "Driver": {
      "Schedule": [
         {
            "DriveDuration": {{number}},
            "RestDuration": {{number}}
         }
      ]
   },
   "Exclude": {
      "Countries": [ "{{string}}" ]
   },
   "InstructionsMeasurementSystem": "{{string}}",
   "Languages": [ "{{string}}" ],
   "LegAdditionalFeatures": [ "{{string}}" ],
   "LegGeometryFormat": "{{string}}",
   "MaxAlternatives": {{number}},
   "OptimizeRoutingFor": "{{string}}",
   "Origin": [ {{number}} ],
   "OriginOptions": {
      "AvoidActionsForDistance": {{number}},
      "AvoidUTurns": {{boolean}},
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
   "SpanAdditionalFeatures": [ "{{string}}" ],
   "Tolls": {
      "AllTransponders": {{boolean}},
      "AllVignettes": {{boolean}},
      "Currency": "{{string}}",
      "EmissionType": {
         "Co2EmissionClass": "{{string}}",
         "Type": "{{string}}"
      },
      "VehicleCategory": "{{string}}"
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
      "Intermodal": {
         "AccessibilityAttributes": [ "{{string}}" ],
         "MaxTransfers": {{number}},
         "Pedestrian": {
            "MaxDistance": {{number}},
            "Speed": {{number}}
         },
         "Rental": {
            "AllowedModes": [ "{{string}}" ],
            "EnabledFor": [ "{{string}}" ],
            "ExcludedModes": [ "{{string}}" ]
         },
         "Taxi": {
            "AllowedModes": [ "{{string}}" ],
            "EnabledFor": [ "{{string}}" ],
            "ExcludedModes": [ "{{string}}" ]
         },
         "Transit": {
            "AllowedModes": [ "{{string}}" ],
            "EnabledFor": [ "{{string}}" ],
            "ExcludedModes": [ "{{string}}" ]
         },
         "Vehicle": {
            "AllowedModes": [ "{{string}}" ],
            "EnabledFor": [ "{{string}}" ],
            "ExcludedModes": [ "{{string}}" ]
         }
      },
      "Pedestrian": {
         "Speed": {{number}}
      },
      "Scooter": {
         "EngineType": "{{string}}",
         "LicensePlate": {
            "LastCharacter": "{{string}}"
         },
         "MaxSpeed": {{number}},
         "Occupancy": {{number}}
      },
      "Transit": {
         "AccessibilityAttributes": [ "{{string}}" ],
         "AllowedModes": [ "{{string}}" ],
         "ExcludedModes": [ "{{string}}" ],
         "MaxTransfers": {{number}},
         "Pedestrian": {
            "MaxDistance": {{number}},
            "Speed": {{number}}
         }
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
   },
   "TravelStepType": "{{string}}",
   "Waypoints": [
      {
         "AvoidActionsForDistance": {{number}},
         "AvoidUTurns": {{boolean}},
         "Heading": {{number}},
         "Matching": {
            "NameHint": "{{string}}",
            "OnRoadThreshold": {{number}},
            "Radius": {{number}},
            "Strategy": "{{string}}"
         },
         "PassThrough": {{boolean}},
         "Position": [ {{number}} ],
         "SideOfStreet": {
            "Position": [ {{number}} ],
            "UseWith": "{{string}}"
         },
         "StopDuration": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_CalculateRoutes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_CalculateRoutes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Allow](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Allow"></a>
 Features that are allowed while calculating a route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteAllowOptions](API_RouteAllowOptions.md) object
Required: No

 ** [ArrivalTime](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-ArrivalTime"></a>
 Time of arrival at the destination. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** [Avoid](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Avoid"></a>
 Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `ControlledAccessHighways`, `Ferries`, and `TollRoads`
Type: [RouteAvoidanceOptions](API_RouteAvoidanceOptions.md) object
Required: No

 ** [DepartNow](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-DepartNow"></a>
Uses the current time as the time of departure.
Type: Boolean
Required: No

 ** [DepartureTime](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-DepartureTime"></a>
Time of departure from the origin.
Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** [Destination](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Destination"></a>
The final position for the route. In the World Geodetic System (WGS 84) format: `[longitude, latitude]`.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** [DestinationOptions](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-DestinationOptions"></a>
 Destination related options. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteDestinationOptions](API_RouteDestinationOptions.md) object
Required: No

 ** [Driver](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Driver"></a>
 Driver related options. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteDriverOptions](API_RouteDriverOptions.md) object
Required: No

 ** [Exclude](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Exclude"></a>
 Features to be strictly excluded while calculating the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteExclusionOptions](API_RouteExclusionOptions.md) object
Required: No

 ** [InstructionsMeasurementSystem](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-InstructionsMeasurementSystem"></a>
Measurement system to be used for instructions within steps in the response.
Type: String
Valid Values: `Metric | Imperial`
Required: No

 ** [Languages](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Languages"></a>
 List of languages for instructions within steps in the response. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Instructions in the requested language are returned only if they are available.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [LegAdditionalFeatures](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-LegAdditionalFeatures"></a>
 A list of optional additional parameters such as timezone that can be requested for each result. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `PassThroughWaypoints`, `Summary`, and `TravelStepInstructions`
+  `Elevation`: Retrieves the elevation information for each location.
+  `Incidents`: Provides information on traffic incidents along the route.
+  `PassThroughWaypoints`: Indicates waypoints that are passed through without stopping.
+  `Summary`: Returns a summary of the route, including distance and duration.
+  `Tolls`: Supplies toll cost information along the route.
+  `TravelStepInstructions`: Provides step-by-step instructions for travel along the route.
+  `TruckRoadTypes`: Returns information about road types suitable for trucks.
+  `TypicalDuration`: Gives typical travel duration based on historical data.
+  `Zones`: Specifies the time zone information for each waypoint.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 12 items.
Valid Values: `Elevation | Incidents | PassThroughWaypoints | Summary | Tolls | TravelStepInstructions | TruckRoadTypes | TypicalDuration | Zones | Bookings | IntermediateStops | NextDepartures`
Required: No

 ** [LegGeometryFormat](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-LegGeometryFormat"></a>
Specifies the format of the geometry returned for each leg of the route. You can choose between two different geometry encoding formats.
 `FlexiblePolyline`: A compact and precise encoding format for the leg geometry. For more information on the format, see the GitHub repository for [https://github.com/aws-geospatial/polyline](https://github.com/aws-geospatial/polyline).
 `Simple`: A less compact encoding, which is easier to decode but may be less precise and result in larger payloads.
Type: String
Valid Values: `FlexiblePolyline | Simple`
Required: No

 ** [MaxAlternatives](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-MaxAlternatives"></a>
Maximum number of alternative routes to be provided in the response, if available. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only up to 3 alternative routes.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 5.
Required: No

 ** [OptimizeRoutingFor](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-OptimizeRoutingFor"></a>
Controls the trade-off between achieving the shortest travel time (`FastestRoute`) and achieving the shortest physical distance ((`ShortestRoute`) when calculating each route in the matrix.
Default value: `FastestRoute`
Type: String
Valid Values: `FastestRoute | ShortestRoute`
Required: No

 ** [Origin](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Origin"></a>
The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** [OriginOptions](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-OriginOptions"></a>
 Specifies how the origin point should be matched to the road network and any routing constraints that apply when the traveler is departing the origin. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteOriginOptions](API_RouteOriginOptions.md) object
Required: No

 ** [SpanAdditionalFeatures](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-SpanAdditionalFeatures"></a>
 A list of optional features such as `SpeedLimit` that can be requested for a Span. A span is a section of a Leg for which the requested features have the same values. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 24 items.
Valid Values: `BestCaseDuration | CarAccess | Country | Distance | Duration | DynamicSpeed | FunctionalClassification | Gates | Incidents | Names | Notices | PedestrianAccess | RailwayCrossings | Region | RoadAttributes | RouteNumbers | ScooterAccess | SpeedLimit | TollSystems | TruckAccess | TruckRoadTypes | TypicalDuration | Zones | Consumption`
Required: No

 ** [Tolls](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Tolls"></a>
 Toll related options. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteTollOptions](API_RouteTollOptions.md) object
Required: No

 ** [Traffic](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Traffic"></a>
 Traffic related options. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteTrafficOptions](API_RouteTrafficOptions.md) object
Required: No

 ** [TravelMode](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-TravelMode"></a>
 Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `Car`, `Pedestrian`, and `Scooter` values.
Default value: `Car`
Type: String
Valid Values: `Car | Pedestrian | Scooter | Truck | Intermodal | Transit`
Required: No

 ** [TravelModeOptions](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-TravelModeOptions"></a>
 Travel mode related options for the provided travel mode. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `Car` and `Pedestrian` travel mode options.
Type: [RouteTravelModeOptions](API_RouteTravelModeOptions.md) object
Required: No

 ** [TravelStepType](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-TravelStepType"></a>
Type of step returned by the response. `Default` provides basic steps intended for web based applications. `TurnByTurn` provides detailed instructions with more granularity intended for a turn based navigation system. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions `Default` does not return any steps.
Type: String
Valid Values: `Default | TurnByTurn`
Required: No

 ** [Waypoints](#API_CalculateRoutes_RequestSyntax) **   <a name="location-CalculateRoutes-request-Waypoints"></a>
 List of waypoints between the Origin and Destination. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions max length is `100`.
Max length: `23`
Type: Array of [RouteWaypoint](API_RouteWaypoint.md) objects
Required: No

## Response Syntax
<a name="API_CalculateRoutes_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "LegGeometryFormat": "string",
   "Notices": [
      {
         "Code": "string",
         "Impact": "string"
      }
   ],
   "Routes": [
      {
         "Legs": [
            {
               "FerryLegDetails": {
                  "AfterTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "Arrival": {
                     "Place": {
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "BeforeTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "Departure": {
                     "Place": {
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Notices": [
                     {
                        "Code": "string",
                        "Impact": "string"
                     }
                  ],
                  "PassThroughWaypoints": [
                     {
                        "GeometryOffset": number,
                        "Place": {
                           "OriginalPosition": [ number ],
                           "Position": [ number ],
                           "WaypointIndex": number
                        }
                     }
                  ],
                  "RouteName": "string",
                  "Spans": [
                     {
                        "Country": "string",
                        "Distance": number,
                        "Duration": number,
                        "GeometryOffset": number,
                        "Names": [
                           {
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "Region": "string"
                     }
                  ],
                  "Summary": {
                     "Overview": {
                        "Distance": number,
                        "Duration": number
                     },
                     "TravelOnly": {
                        "Duration": number
                     }
                  },
                  "TravelSteps": [
                     {
                        "Distance": number,
                        "Duration": number,
                        "GeometryOffset": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ]
               },
               "Geometry": {
                  "LineString": [
                     [ number ]
                  ],
                  "Polyline": "string"
               },
               "Language": "string",
               "PedestrianLegDetails": {
                  "AfterTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "Arrival": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "SideOfStreet": "string",
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Departure": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "SideOfStreet": "string",
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Notices": [
                     {
                        "Code": "string",
                        "Impact": "string"
                     }
                  ],
                  "PassThroughWaypoints": [
                     {
                        "GeometryOffset": number,
                        "Place": {
                           "OriginalPosition": [ number ],
                           "Position": [ number ],
                           "WaypointIndex": number
                        }
                     }
                  ],
                  "Spans": [
                     {
                        "BestCaseDuration": number,
                        "Country": "string",
                        "Distance": number,
                        "Duration": number,
                        "DynamicSpeed": {
                           "BestCaseSpeed": number,
                           "TurnDuration": number,
                           "TypicalSpeed": number
                        },
                        "FunctionalClassification": number,
                        "GeometryOffset": number,
                        "Incidents": [ number ],
                        "Names": [
                           {
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "PedestrianAccess": [ "string" ],
                        "Region": "string",
                        "RoadAttributes": [ "string" ],
                        "RouteNumbers": [
                           {
                              "Direction": "string",
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "SpeedLimit": {
                           "MaxSpeed": number,
                           "Unlimited": boolean
                        },
                        "TypicalDuration": number
                     }
                  ],
                  "Summary": {
                     "Overview": {
                        "Distance": number,
                        "Duration": number
                     },
                     "TravelOnly": {
                        "Duration": number
                     }
                  },
                  "TravelSteps": [
                     {
                        "ContinueStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "CurrentRoad": {
                           "RoadName": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RouteNumber": [
                              {
                                 "Direction": "string",
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Towards": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Type": "string"
                        },
                        "Distance": number,
                        "Duration": number,
                        "ExitNumber": [
                           {
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "GeometryOffset": number,
                        "Instruction": "string",
                        "KeepStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "NextRoad": {
                           "RoadName": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RouteNumber": [
                              {
                                 "Direction": "string",
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Towards": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Type": "string"
                        },
                        "RoundaboutEnterStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RoundaboutExitStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RelativeExit": number,
                           "RoundaboutAngle": number,
                           "SteeringDirection": "string"
                        },
                        "RoundaboutPassStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "Signpost": {
                           "Labels": [
                              {
                                 "RouteNumber": {
                                    "Direction": "string",
                                    "Language": "string",
                                    "Value": "string"
                                 },
                                 "Text": {
                                    "Language": "string",
                                    "Value": "string"
                                 }
                              }
                           ]
                        },
                        "TurnStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "Type": "string"
                     }
                  ]
               },
               "RentalLegDetails": {
                  "AfterTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "Agency": {
                     "Name": "string",
                     "Url": "string"
                  },
                  "Arrival": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Attributions": [
                     {
                        "AttributionType": "string",
                        "WebLink": {
                           "AnchorText": "string",
                           "Description": "string",
                           "DeviceType": "string",
                           "Url": "string"
                        }
                     }
                  ],
                  "BeforeTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "BookingWebLinks": [
                     {
                        "AnchorText": "string",
                        "Description": "string",
                        "DeviceType": "string",
                        "Url": "string"
                     }
                  ],
                  "Departure": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Summary": {
                     "Overview": {
                        "Distance": number,
                        "Duration": number
                     },
                     "TravelOnly": {
                        "Duration": number
                     }
                  },
                  "Transport": {
                     "AvailableSeats": number,
                     "Category": "string",
                     "Color": "string",
                     "Engine": "string",
                     "LicensePlate": "string",
                     "Mode": "string",
                     "Model": "string",
                     "Name": "string",
                     "TextColor": "string"
                  },
                  "TravelSteps": [
                     {
                        "ContinueStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "Distance": number,
                        "Duration": number,
                        "ExitStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RelativeExit": number,
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "GeometryOffset": number,
                        "Instruction": "string",
                        "KeepStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RampStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RoundaboutEnterStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RoundaboutExitStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RelativeExit": number,
                           "RoundaboutAngle": number,
                           "SteeringDirection": "string"
                        },
                        "RoundaboutPassStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "TurnStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "Type": "string",
                        "UTurnStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        }
                     }
                  ]
               },
               "TaxiLegDetails": {
                  "AfterTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "Agency": {
                     "Name": "string",
                     "Url": "string"
                  },
                  "Arrival": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Attributions": [
                     {
                        "AttributionType": "string",
                        "WebLink": {
                           "AnchorText": "string",
                           "Description": "string",
                           "DeviceType": "string",
                           "Url": "string"
                        }
                     }
                  ],
                  "BeforeTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "BookingWebLinks": [
                     {
                        "AnchorText": "string",
                        "Description": "string",
                        "DeviceType": "string",
                        "Url": "string"
                     }
                  ],
                  "Departure": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Notices": [
                     {
                        "Code": "string",
                        "Impact": "string"
                     }
                  ],
                  "Summary": {
                     "Overview": {
                        "Distance": number,
                        "Duration": number
                     },
                     "TravelOnly": {
                        "Duration": number
                     }
                  },
                  "Transport": {
                     "AvailableSeats": number,
                     "Category": "string",
                     "Color": "string",
                     "Engine": "string",
                     "LicensePlate": "string",
                     "Mode": "string",
                     "Model": "string",
                     "Name": "string",
                     "TextColor": "string"
                  },
                  "TravelSteps": [
                     {
                        "ContinueStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "Distance": number,
                        "Duration": number,
                        "ExitStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RelativeExit": number,
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "GeometryOffset": number,
                        "Instruction": "string",
                        "KeepStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RampStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RoundaboutEnterStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RoundaboutExitStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RelativeExit": number,
                           "RoundaboutAngle": number,
                           "SteeringDirection": "string"
                        },
                        "RoundaboutPassStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "TurnStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "Type": "string",
                        "UTurnStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        }
                     }
                  ]
               },
               "TransitLegDetails": {
                  "AfterTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "Agency": {
                     "Name": "string",
                     "Url": "string"
                  },
                  "Arrival": {
                     "Delay": number,
                     "Place": {
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Status": "string",
                     "Time": "string"
                  },
                  "Attributions": [
                     {
                        "AttributionType": "string",
                        "WebLink": {
                           "AnchorText": "string",
                           "Description": "string",
                           "DeviceType": "string",
                           "Url": "string"
                        }
                     }
                  ],
                  "BeforeTravelSteps": [
                     {
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "BookingWebLinks": [
                     {
                        "AnchorText": "string",
                        "Description": "string",
                        "DeviceType": "string",
                        "Url": "string"
                     }
                  ],
                  "Departure": {
                     "Delay": number,
                     "Place": {
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Status": "string",
                     "Time": "string"
                  },
                  "Incidents": [
                     {
                        "Description": "string",
                        "Effect": "string",
                        "EndTime": "string",
                        "StartTime": "string",
                        "Type": "string",
                        "Url": "string"
                     }
                  ],
                  "IntermediateStops": [
                     {
                        "Attributes": [ "string" ],
                        "Departure": {
                           "Delay": number,
                           "Place": {
                              "Name": "string",
                              "OriginalPosition": [ number ],
                              "Position": [ number ],
                              "StationDetails": {
                                 "Accessibility": {
                                    "Wheelchair": "string"
                                 },
                                 "PlatformName": "string",
                                 "ShortName": "string"
                              },
                              "Type": "string",
                              "WaypointIndex": number
                           },
                           "Status": "string",
                           "Time": "string"
                        },
                        "Duration": number,
                        "GeometryOffset": number,
                        "Transport": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "Color": "string",
                           "Headsign": "string",
                           "LongRouteName": "string",
                           "Mode": "string",
                           "RouteName": "string",
                           "ShortRouteName": "string",
                           "TextColor": "string"
                        }
                     }
                  ],
                  "NextDepartures": [
                     {
                        "Delay": number,
                        "PlatformName": "string",
                        "Status": "string",
                        "Time": "string",
                        "Transport": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "Color": "string",
                           "Headsign": "string",
                           "LongRouteName": "string",
                           "Mode": "string",
                           "RouteName": "string",
                           "ShortRouteName": "string",
                           "TextColor": "string"
                        }
                     }
                  ],
                  "Notices": [
                     {
                        "Code": "string",
                        "Impact": "string"
                     }
                  ],
                  "PassThroughWaypoints": [
                     {
                        "GeometryOffset": number,
                        "Place": {
                           "OriginalPosition": [ number ],
                           "Position": [ number ],
                           "WaypointIndex": number
                        }
                     }
                  ],
                  "Spans": [
                     {
                        "Country": "string",
                        "Distance": number,
                        "Duration": number,
                        "GeometryOffset": number,
                        "Names": [
                           {
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "Region": "string"
                     }
                  ],
                  "Summary": {
                     "Overview": {
                        "Distance": number,
                        "Duration": number
                     },
                     "TravelOnly": {
                        "Duration": number
                     }
                  },
                  "Transport": {
                     "Accessibility": {
                        "Wheelchair": "string"
                     },
                     "Color": "string",
                     "Headsign": "string",
                     "LongRouteName": "string",
                     "Mode": "string",
                     "RouteName": "string",
                     "ShortRouteName": "string",
                     "TextColor": "string"
                  },
                  "TravelSteps": [
                     {
                        "Distance": number,
                        "Duration": number,
                        "GeometryOffset": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ]
               },
               "TravelMode": "string",
               "Type": "string",
               "VehicleLegDetails": {
                  "AfterTravelSteps": [
                     {
                        "ChargeStepDetails": {
                           "ArrivalCharge": number,
                           "ConsumablePower": number,
                           "DesiredCharge": number
                        },
                        "Duration": number,
                        "Instruction": "string",
                        "Type": "string"
                     }
                  ],
                  "Arrival": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "SideOfStreet": "string",
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Departure": {
                     "Place": {
                        "AccessPointDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           }
                        },
                        "Name": "string",
                        "OriginalPosition": [ number ],
                        "Position": [ number ],
                        "SideOfStreet": "string",
                        "StationDetails": {
                           "Accessibility": {
                              "Wheelchair": "string"
                           },
                           "PlatformName": "string",
                           "ShortName": "string"
                        },
                        "Type": "string",
                        "WaypointIndex": number
                     },
                     "Time": "string"
                  },
                  "Incidents": [
                     {
                        "Description": "string",
                        "EndTime": "string",
                        "Severity": "string",
                        "StartTime": "string",
                        "Type": "string"
                     }
                  ],
                  "Notices": [
                     {
                        "Code": "string",
                        "Details": [
                           {
                              "Title": "string",
                              "ViolatedConstraints": {
                                 "AllHazardsRestricted": boolean,
                                 "AxleCount": {
                                    "Max": number,
                                    "Min": number
                                 },
                                 "HazardousCargos": [ "string" ],
                                 "MaxHeight": number,
                                 "MaxKpraLength": number,
                                 "MaxLength": number,
                                 "MaxPayloadCapacity": number,
                                 "MaxWeight": {
                                    "Type": "string",
                                    "Value": number
                                 },
                                 "MaxWeightPerAxle": number,
                                 "MaxWeightPerAxleGroup": {
                                    "Quad": number,
                                    "Quint": number,
                                    "Single": number,
                                    "Tandem": number,
                                    "Triple": number
                                 },
                                 "MaxWidth": number,
                                 "Occupancy": {
                                    "Max": number,
                                    "Min": number
                                 },
                                 "RestrictedTimes": "string",
                                 "TimeDependent": boolean,
                                 "TrailerCount": {
                                    "Max": number,
                                    "Min": number
                                 },
                                 "TravelMode": boolean,
                                 "TruckRoadType": "string",
                                 "TruckType": "string",
                                 "TunnelRestrictionCode": "string"
                              }
                           }
                        ],
                        "Impact": "string"
                     }
                  ],
                  "PassThroughWaypoints": [
                     {
                        "GeometryOffset": number,
                        "Place": {
                           "OriginalPosition": [ number ],
                           "Position": [ number ],
                           "WaypointIndex": number
                        }
                     }
                  ],
                  "Spans": [
                     {
                        "BestCaseDuration": number,
                        "CarAccess": [ "string" ],
                        "Country": "string",
                        "Distance": number,
                        "Duration": number,
                        "DynamicSpeed": {
                           "BestCaseSpeed": number,
                           "TurnDuration": number,
                           "TypicalSpeed": number
                        },
                        "FunctionalClassification": number,
                        "Gate": "string",
                        "GeometryOffset": number,
                        "Incidents": [ number ],
                        "Names": [
                           {
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "Notices": [ number ],
                        "RailwayCrossing": "string",
                        "Region": "string",
                        "RoadAttributes": [ "string" ],
                        "RouteNumbers": [
                           {
                              "Direction": "string",
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "ScooterAccess": [ "string" ],
                        "SpeedLimit": {
                           "MaxSpeed": number,
                           "Unlimited": boolean
                        },
                        "TollSystems": [ number ],
                        "TruckAccess": [ "string" ],
                        "TruckRoadTypes": [ number ],
                        "TypicalDuration": number,
                        "Zones": [ number ]
                     }
                  ],
                  "Summary": {
                     "Overview": {
                        "BestCaseDuration": number,
                        "Distance": number,
                        "Duration": number,
                        "TypicalDuration": number
                     },
                     "TravelOnly": {
                        "BestCaseDuration": number,
                        "Duration": number,
                        "TypicalDuration": number
                     }
                  },
                  "Tolls": [
                     {
                        "Country": "string",
                        "PaymentSites": [
                           {
                              "Name": "string",
                              "Position": [ number ]
                           }
                        ],
                        "Rates": [
                           {
                              "ApplicableTimes": "string",
                              "ConvertedPrice": {
                                 "Currency": "string",
                                 "Estimate": boolean,
                                 "PerDuration": number,
                                 "Range": boolean,
                                 "RangeValue": {
                                    "Max": number,
                                    "Min": number
                                 },
                                 "Value": number
                              },
                              "Id": "string",
                              "LocalPrice": {
                                 "Currency": "string",
                                 "Estimate": boolean,
                                 "PerDuration": number,
                                 "Range": boolean,
                                 "RangeValue": {
                                    "Max": number,
                                    "Min": number
                                 },
                                 "Value": number
                              },
                              "Name": "string",
                              "Pass": {
                                 "IncludesReturnTrip": boolean,
                                 "SeniorPass": boolean,
                                 "TransferCount": number,
                                 "TripCount": number,
                                 "ValidityPeriod": {
                                    "Period": "string",
                                    "PeriodCount": number
                                 }
                              },
                              "PaymentMethods": [ "string" ],
                              "Transponders": [
                                 {
                                    "SystemName": "string"
                                 }
                              ]
                           }
                        ],
                        "Systems": [ number ]
                     }
                  ],
                  "TollSystems": [
                     {
                        "Name": "string"
                     }
                  ],
                  "TravelSteps": [
                     {
                        "ContinueHighwayStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "ContinueStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ]
                        },
                        "CurrentRoad": {
                           "RoadName": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RouteNumber": [
                              {
                                 "Direction": "string",
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Towards": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Type": "string"
                        },
                        "Distance": number,
                        "Duration": number,
                        "EnterHighwayStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "ExitNumber": [
                           {
                              "Language": "string",
                              "Value": "string"
                           }
                        ],
                        "ExitStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RelativeExit": number,
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "GeometryOffset": number,
                        "Instruction": "string",
                        "KeepStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "NextRoad": {
                           "RoadName": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RouteNumber": [
                              {
                                 "Direction": "string",
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Towards": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "Type": "string"
                        },
                        "RampStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RoundaboutEnterStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "RoundaboutExitStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "RelativeExit": number,
                           "RoundaboutAngle": number,
                           "SteeringDirection": "string"
                        },
                        "RoundaboutPassStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "Signpost": {
                           "Labels": [
                              {
                                 "RouteNumber": {
                                    "Direction": "string",
                                    "Language": "string",
                                    "Value": "string"
                                 },
                                 "Text": {
                                    "Language": "string",
                                    "Value": "string"
                                 }
                              }
                           ]
                        },
                        "TurnStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        },
                        "Type": "string",
                        "UTurnStepDetails": {
                           "Intersection": [
                              {
                                 "Language": "string",
                                 "Value": "string"
                              }
                           ],
                           "SteeringDirection": "string",
                           "TurnAngle": number,
                           "TurnIntensity": "string"
                        }
                     }
                  ],
                  "TruckRoadTypes": [ "string" ],
                  "Zones": [
                     {
                        "Category": "string",
                        "Name": "string"
                     }
                  ]
               }
            }
         ],
         "MajorRoadLabels": [
            {
               "RoadName": {
                  "Language": "string",
                  "Value": "string"
               },
               "RouteNumber": {
                  "Direction": "string",
                  "Language": "string",
                  "Value": "string"
               }
            }
         ],
         "Summary": {
            "Distance": number,
            "Duration": number,
            "Tolls": {
               "Total": {
                  "Currency": "string",
                  "Estimate": boolean,
                  "Range": boolean,
                  "RangeValue": {
                     "Max": number,
                     "Min": number
                  },
                  "Value": number
               }
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_CalculateRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_CalculateRoutes_ResponseSyntax) **   <a name="location-CalculateRoutes-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.

The following data is returned in JSON format by the service.

 ** [LegGeometryFormat](#API_CalculateRoutes_ResponseSyntax) **   <a name="location-CalculateRoutes-response-LegGeometryFormat"></a>
Specifies the format of the geometry returned for each leg of the route.
Type: String
Valid Values: `FlexiblePolyline | Simple`

 ** [Notices](#API_CalculateRoutes_ResponseSyntax) **   <a name="location-CalculateRoutes-response-Notices"></a>
 Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteResponseNotice](API_RouteResponseNotice.md) objects

 ** [Routes](#API_CalculateRoutes_ResponseSyntax) **   <a name="location-CalculateRoutes-response-Routes"></a>
The path from the origin to the destination.
Type: Array of [Route](API_Route.md) objects

## Errors
<a name="API_CalculateRoutes_Errors"></a>

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
<a name="API_CalculateRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-routes-2020-11-19/CalculateRoutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/CalculateRoutes)
