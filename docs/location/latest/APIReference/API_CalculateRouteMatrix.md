---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRouteMatrix.html
---

# CalculateRouteMatrix
<a name="API_CalculateRouteMatrix"></a>

 Use `CalculateRouteMatrix` to compute results for all pairs of Origins to Destinations. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destinations positions.

For more information, see [Calculate route matrix](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_CalculateRouteMatrix_RequestSyntax"></a>

```
POST /v2/route-matrix?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "Allow": {
      "Hot": {{boolean}},
      "Hov": {{boolean}}
   },
   "Avoid": {
      "Areas": [
         {
            "Geometry": {
               "BoundingBox": [ {{number}} ],
               "Polygon": [
                  [
                     [ {{number}} ]
                  ]
               ],
               "PolylinePolygon": [ "{{string}}" ]
            }
         }
      ],
      "CarShuttleTrains": {{boolean}},
      "ControlledAccessHighways": {{boolean}},
      "DirtRoads": {{boolean}},
      "Ferries": {{boolean}},
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
   "Destinations": [
      {
         "Options": {
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
         "Position": [ {{number}} ]
      }
   ],
   "Exclude": {
      "Countries": [ "{{string}}" ]
   },
   "OptimizeRoutingFor": "{{string}}",
   "Origins": [
      {
         "Options": {
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
         "Position": [ {{number}} ]
      }
   ],
   "RoutingBoundary": {
      "Geometry": {
         "AutoCircle": {
            "Margin": {{number}},
            "MaxRadius": {{number}}
         },
         "BoundingBox": [ {{number}} ],
         "Circle": {
            "Center": [ {{number}} ],
            "Radius": {{number}}
         },
         "Polygon": [
            [
               [ {{number}} ]
            ]
         ]
      },
      "Unbounded": {{boolean}}
   },
   "Traffic": {
      "FlowEventThresholdOverride": {{number}},
      "Usage": "{{string}}"
   },
   "TravelMode": "{{string}}",
   "TravelModeOptions": {
      "Car": {
         "LicensePlate": {
            "LastCharacter": "{{string}}"
         },
         "MaxSpeed": {{number}},
         "Occupancy": {{number}}
      },
      "Scooter": {
         "LicensePlate": {
            "LastCharacter": "{{string}}"
         },
         "MaxSpeed": {{number}},
         "Occupancy": {{number}}
      },
      "Truck": {
         "AxleCount": {{number}},
         "GrossWeight": {{number}},
         "HazardousCargos": [ "{{string}}" ],
         "Height": {{number}},
         "KpraLength": {{number}},
         "Length": {{number}},
         "LicensePlate": {
            "LastCharacter": "{{string}}"
         },
         "MaxSpeed": {{number}},
         "Occupancy": {{number}},
         "PayloadCapacity": {{number}},
         "Trailer": {
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
<a name="API_CalculateRouteMatrix_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_CalculateRouteMatrix_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Allow](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-Allow"></a>
Features that are allowed while calculating a route.
Type: [RouteMatrixAllowOptions](API_RouteMatrixAllowOptions.md) object
Required: No

 ** [Avoid](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-Avoid"></a>
 Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `TollRoads`, `Ferries`, and `ControlledAccessHighways`.
Type: [RouteMatrixAvoidanceOptions](API_RouteMatrixAvoidanceOptions.md) object
Required: No

 ** [DepartNow](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-DepartNow"></a>
Uses the current time as the time of departure.
Type: Boolean
Required: No

 ** [DepartureTime](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-DepartureTime"></a>
Time of departure from the origin.
Time format:`YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm`
Examples:
 `2020-04-22T17:57:24Z`
 `2020-04-22T17:57:24+02:00`
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** [Destinations](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-Destinations"></a>
List of destinations for the route in World Geodetic System (WGS 84) format: [longitude, latitude].
Route calculations are billed for each origin and destination pair. If you use a large matrix of origins and destinations, your costs will increase accordingly. For more information, see [Routes pricing](https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html) in the *Amazon Location Service Developer Guide*.
The maximum number of destinations depends on the routing boundary configuration:
+ With `RoutingBoundary.Geometry` set: maximum 500 destinations
+ With `RoutingBoundary.Unbounded` set to `true`: maximum 100 destinations
+ For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers in `ap-southeast-1` and `ap-southeast-5`: maximum 350 destinations
The total matrix size (origins × destinations) must not exceed:
+ With `RoutingBoundary.Geometry`: 160,000
+ With `RoutingBoundary.Unbounded`: 100
+ For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers in `ap-southeast-1` and `ap-southeast-5`: 122,500
Type: Array of [RouteMatrixDestination](API_RouteMatrixDestination.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [Exclude](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-Exclude"></a>
 Features to be strictly excluded while calculating the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteMatrixExclusionOptions](API_RouteMatrixExclusionOptions.md) object
Required: No

 ** [OptimizeRoutingFor](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-OptimizeRoutingFor"></a>
Controls the trade-off between finding the shortest travel time (`FastestRoute`) and the shortest distance (`ShortestRoute`) when calculating reachable areas.
Default value: `FastestRoute`
Type: String
Valid Values: `FastestRoute | ShortestRoute`
Required: No

 ** [Origins](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-Origins"></a>
List of origins for the route in World Geodetic System (WGS 84) format: [longitude, latitude].
Route calculations are billed for each origin and destination pair. Using a large amount of Origins in a request can lead you to incur unexpected charges. For more information, see [Routes pricing](https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html) in the *Amazon Location Service Developer Guide*.
The maximum number of origins depends on the routing boundary configuration:
+ With `RoutingBoundary.Geometry` set: maximum 500 origins
+ With `RoutingBoundary.Unbounded` set to `true`: maximum 15 origins
+ For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers in `ap-southeast-1` and `ap-southeast-5`: maximum 350 origins
The total matrix size (origins × destinations) must not exceed:
+ With `RoutingBoundary.Geometry`: 160,000
+ With `RoutingBoundary.Unbounded`: 100
+ For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers in `ap-southeast-1` and `ap-southeast-5`: 122,500
Type: Array of [RouteMatrixOrigin](API_RouteMatrixOrigin.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [RoutingBoundary](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-RoutingBoundary"></a>
 Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `Unbounded` set to `true`.
Default value: `Unbounded set to true`
When `AutoCircle` is set in the request, the response routing boundary will return `Circle` derived from the `AutoCircle` settings.
Type: [RouteMatrixBoundary](API_RouteMatrixBoundary.md) object
Required: No

 ** [Traffic](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-Traffic"></a>
 Traffic related options. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteMatrixTrafficOptions](API_RouteMatrixTrafficOptions.md) object
Required: No

 ** [TravelMode](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-TravelMode"></a>
 Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `Car`, `Pedestrian`, and `Scooter`.
Default value: `Car`
Type: String
Valid Values: `Car | Pedestrian | Scooter | Truck`
Required: No

 ** [TravelModeOptions](#API_CalculateRouteMatrix_RequestSyntax) **   <a name="location-CalculateRouteMatrix-request-TravelModeOptions"></a>
 Travel mode related options for the provided travel mode. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteMatrixTravelModeOptions](API_RouteMatrixTravelModeOptions.md) object
Required: No

## Response Syntax
<a name="API_CalculateRouteMatrix_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "ErrorCount": number,
   "RouteMatrix": [
      [
         {
            "Distance": number,
            "Duration": number,
            "Error": "string"
         }
      ]
   ],
   "RoutingBoundary": {
      "Geometry": {
         "AutoCircle": {
            "Margin": number,
            "MaxRadius": number
         },
         "BoundingBox": [ number ],
         "Circle": {
            "Center": [ number ],
            "Radius": number
         },
         "Polygon": [
            [
               [ number ]
            ]
         ]
      },
      "Unbounded": boolean
   }
}
```

## Response Elements
<a name="API_CalculateRouteMatrix_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.

The following data is returned in JSON format by the service.

 ** [ErrorCount](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-ErrorCount"></a>
The count of error results in the route matrix. If this number is 0, all routes were calculated successfully.
Type: Integer
Valid Range: Minimum value of 0.

 ** [RouteMatrix](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-RouteMatrix"></a>
The calculated route matrix containing the results for all pairs of Origins to Destination positions. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destination positions.
Type: Array of arrays of [RouteMatrixEntry](API_RouteMatrixEntry.md) objects

 ** [RoutingBoundary](#API_CalculateRouteMatrix_ResponseSyntax) **   <a name="location-CalculateRouteMatrix-response-RoutingBoundary"></a>
Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid.
When `AutoCircle` is set in the request, the response routing boundary will return `Circle` derived from the `AutoCircle` settings.
Type: [RouteMatrixBoundary](API_RouteMatrixBoundary.md) object

## Errors
<a name="API_CalculateRouteMatrix_Errors"></a>

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
<a name="API_CalculateRouteMatrix_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-routes-2020-11-19/CalculateRouteMatrix)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/CalculateRouteMatrix)
