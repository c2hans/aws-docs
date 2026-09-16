---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/calculate-route.html
---

# Calculate a route with Amazon Location
<a name="calculate-route"></a>

You can use Amazon Location Service to calculate routes between an origin and a destination, with up to 23 waypoints along the route, for different modes of transportation, avoidances, and traffic conditions.

**Note**
You must first create a route calculator resource and set up authentication for your requests to Amazon Location. For more information, see [Prerequisites for calculating routes using Amazon Location](routes-prerequisites.md).

## Start calculating routes
<a name="start-calculate-route"></a>

Submit a simple request by using the `[CalculateRoute](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html)` operation. A simple request contains the following required fields:

**Note**
In the latest API, this operation is `[CalculateRoutes](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html)` (plural) under `geo-routes`, which takes `Origin` and `Destination` instead of `DeparturePosition` and `DestinationPosition`, and does not require a route calculator resource.
+ `DeparturePosition` – The starting position for which to calculate the route from. Defined as `[longitude, latitude]`
+ `DestinationPosition` – The end position to which to calculate the route. Defined as `[longitude, latitude]`.

**Note**
If you specify a departure or destination position that's not located on a road, Amazon Location [moves the position to the nearest road](snap-to-nearby-road.md).

You can optionally specify [waypoints](#waypoints), a [departure time](departure-time.md), and a [ travel mode](travel-mode.md) in your request.

You can use the AWS CLI or the Amazon Location APIs.

------
#### [ API ]

The following example is a `CalculateRoute` request using the route calculator resource {{ExampleCalculator}}. The request specifies calculating a route from a departure position [{{-122.7565}}, {{49.0021}}] to a destination position [{{-122.3394}}, {{47.6159}}].

```
POST /routes/v0/calculators/{{ExampleCalculator}}/calculate/route
Content-type: application/json
{
   "DeparturePosition": [{{-122.7565}},{{49.0021}}],
   "DestinationPosition": [{{-122.3394}}, {{47.6159}}]
}
```

------
#### [ AWS CLI ]

The following example is a `calculate-route` command using the route calculator resource {{ExampleCalculator}}. The request specifies calculating a route from a departure position [{{-122.7565}}, {{49.0021}}] to a destination position [{{-122.3394}}, {{47.6159}}].

```
aws location \
    calculate-route \
        --calculator-name {{ExampleCalculator}} \
        --departure-position {{-122.7565}} {{49.0021}} \
        --destination-position {{-122.3394}} {{47.6159}}
```

------

By default, the response returns `Distance` in kilometers. You can change the unit of measurement to miles using the following optional parameter:
+ `DistanceUnit` – Specifies the unit system to use for the distance results.

**Example**

```
POST /routes/v0/calculators/ExampleCalculator/calculate/route
Content-type: application/json
{
   "DeparturePosition": [-122.7565,49.0021],
   "DestinationPosition": [-122.3394, 47.6159],
   "DistanceUnit": "{{Miles}}"
}
```

## Setting waypoints
<a name="waypoints"></a>

When calculating a route, you can specify up to 23 intermediate stopover points between the departure position and the destination position using waypoint positions.
+ `WaypointPositions` – Specifies an ordered list of intermediate positions to include along a route between the departure position and destination position.
**Note**
If you specify a waypoint position that's not located on a road, Amazon Location moves the position to the nearest road.

**Example**
The following `[CalculateRoute](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html)` request calculates a route with 2 waypoints:
+ The departure position is [-122.7565, 49.0021], and the destination position is [-122.3394, 47.6159].
+ For the request parameter `WaypointPositions`:
  + The first stop over position is [{{-122.1884, 48.0936}}].
  + The second stop over position is [{{-122.3493, 47.6205}}].
+ To include the leg linestring geometry between these two waypoints, set the following optional parameter to {{true}}:
  + `IncludeLegGeometry` – Includes the geometry of each path between a pair of positions in the response.

```
POST /routes/v0/calculators/ExampleCalculator/calculate/route
Content-type: application/json
{
   "DeparturePosition": [-122.7565,49.0021],
   "DestinationPosition": [-122.3394, 47.6159],
   "WaypointPositions":[
        [{{-122.1884,48.0936}}],
        [{{-122.3493,47.6205}}]
    ],
   "IncludeLegGeometry": {{true}}
}
```

## Example response
<a name="example-response-calculate-route"></a>

The following is an example request with the corresponding response when calling the `[CalculateRoute](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html)` operation from the Amazon Location Routes API with the `IncludeLegGeometry` set to {{true}}, which includes the linestring geometry of each path between a pair of positions in the response.

------
#### [ Example request ]

```
POST /routes/v0/calculators/ExampleCalculator/calculate/route
Content-type: application/json
{
   "DeparturePosition": [{{-122.7565}},{{49.0021}}],
   "DestinationPosition": [{{-122.3394}}, {{47.6159}}],
   "IncludeLegGeometry": true
}
```

------
#### [ Example response ]

```
{
   "Legs": [
      {
         "Distance": 178.5,
         "DurationSeconds": 6480,
         "EndPosition": [-122.3394,47.6159],
         "Geometry": {
            "LineString": [
               [{{-122.7565,49.0021}}],
               [{{-122.3394,47.6159}}]
            ]
         },
         "StartPosition": [-122.7565,49.0021],
         "Steps": [
            {
               "Distance": 178.5,
               "DurationSeconds": 6480,
               "EndPosition": [-122.3394,47.6159],
               "GeometryOffset": 0,
               "StartPosition": [-122.7565,49.0021]
            }
         ]
      }
   ],
   "Summary": {
      "DataSource": "Esri",
      "Distance": 178.5,
      "DistanceUnit": "Kilometers",
      "DurationSeconds": 6480,
      "RouteBBox": [
        -122.7565,49.0021,
        -122.3394,47.6159
    ]
   }
}
```

------
