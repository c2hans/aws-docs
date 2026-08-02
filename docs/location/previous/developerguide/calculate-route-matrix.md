---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html
---

# Route planning with a route matrix in Amazon Location
<a name="calculate-route-matrix"></a>

You can use Amazon Location Service to create inputs to your route planning and optimization software. You can create route results, including travel time and travel distance, for routes between a set of departure positions and a set of destination positions.

For example, given departure positions A and B, and destination positions X and Y, Amazon Location Service will return travel time and travel distance for routes from A to X, A to Y, B to X, and B to Y.

You can calculate the routes with different modes of transportation, avoidances, and traffic conditions. For example, you can specify that the vehicle is a truck that is 35 feet long, and the route calculated will use those restrictions to determine the travel time and travel distance.

The number of results returned (and routes calculated) is the number of departure positions multiplied by the number of destination positions. You are charged for each route calculated, not each request to the service, so a route matrix with 10 departures and 10 destinations will be billed as 100 routes.

## Calculating a route matrix
<a name="calc-route-matrix-howto"></a>

You can calculate a matrix of routes between a set of departure positions and a set of destination positions. The route results will include travel time and travel distance.

**Prerequisite**
+ You must first create a route calculator resource and set up authentication for your requests to Amazon Location. For more information, see [Prerequisites for calculating routes using Amazon Location](routes-prerequisites.md).

Submit a request by using the `[CalculateRouteMatrix](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CalculateRouteMatrix.html)` operation. A minimal request contains the following required fields:
+ `DeparturePositions` – The set of starting positions for which to calculate the routes. Defined as an array of `[longitude, latitude]`
+ `DestinationPositions` – The set of end positions for which to calculate the routes. Defined as an array of `[longitude, latitude]`.

**Note**
If you specify a departure or destination position that's not located on a road, Amazon Location [moves the position to the nearest road](snap-to-nearby-road.md).

You can optionally specify a [departure time](departure-time.md), and a [ travel mode](travel-mode.md) in your request.

You can use the AWS CLI or the Amazon Location APIs.

------
#### [ API ]

The following example is a `CalculateRouteMatrix` request using the route calculator resource {{ExampleCalculator}}. The request specifies calculating the matrix of routes from departure positions [{{-122.7565}}, {{49.0021 }}] and [{{-122.2014}}, {{47.6101}}] to destination positions [{{-122.3394}}, {{47.6159 }}] and [{{-122.4813}}, {{48.7511}}].

```
POST /routes/v0/calculators/{{ExampleCalculator}}/calculate/route-matrix
Content-type: application/json
{
   "DeparturePositions": [
       [{{-122.7565}},{{49.0021}}],
       [{{-122.2014}},{{47.6101}}]
   ],
   "DestinationPositions": [
       [{{-122.3394}}, {{47.6159}}],
       [{{-122.4813}},{{48.7511}}]
   ]
}
```

------
#### [ AWS CLI ]

The following example is a `calculate-route-matrix` command using the route calculator resource {{ExampleCalculator}}. The request specifies calculating the matrix of routes from departure positions [{{-122.7565}}, {{49.0021 }}] and [{{-122.2014}}, {{47.6101}}] to destination positions [{{-122.3394}}, {{47.6159 }}] and [{{-122.4813}}, {{48.7511}}].

```
aws location \
    calculate-route-matrix \
        --calculator-name {{ExampleCalculator}} \
        --departure-positions "[{{[-122.7565,49.0021],[-122.2014,47.6101]}}]" \
	    --destination-positions "[{{[-122.3394,47.6159],[-122.4813,48.7511]}}]"
```

------

By default, the response returns `Distance` in kilometers. You can change the unit of measurement to miles using the following optional parameter:
+ `DistanceUnit` – Specifies the unit system to use for the distance results.

**Example**

```
POST /routes/v0/calculators/{{ExampleCalculator}}/calculate/route-matrix
Content-type: application/json
{
   "DeparturePositions": [
       [{{-122.7565}},{{49.0021}}],
       [{{-122.2014}},{{47.6101}}]
   ],
   "DestinationPositions": [
       [{{-122.3394}}, {{47.6159}}],
       [{{-122.4813}},{{48.7511}}]
   ],
   "DistanceUnit": "{{Miles}}"
}
```

## Restrictions on departure and destination positions
<a name="matrix-routing-position-limits"></a>

When calculating a route matrix, there are restrictions on the departure and destination positions. These restrictions vary depending on the provider used by the `RouteCalculator` resource.

****

| Limitation | Esri | Grab | HERE |
| --- | --- | --- | --- |
| Number of positions | Up to 10 departure positions and 10 destination positions. | Up to 350 departure positions and 350 destination positions. | Up to 350 departure positions and 350 destination positions.<br />For longer routes, additional restrictions apply. See the [ section](#matrix-routing-longer-routes). |
| Distance between positions | Any pair of departure and destination positions must be within 400 km of each other (40km for walking routes). |  | All departure and destination positions must fall within a 180 km diameter circle.<br />For longer routes, additional restrictions apply. See the [ section](#matrix-routing-longer-routes). |
| Route length | Routes will not be completed if the total travel time for the route is over 400 minutes. |  | Routes that deviate more than 10 km outside a circle around the departure and destination points will not be calculated.<br />For longer routes, additional restrictions apply. See the [ section](#matrix-routing-longer-routes). |
| Regions | Calculating a route matrix is not supported in Korea. | Available in Southeast Asia. For a list of supported countries/regions and more information, see [Countries/regions and area covered](grab.md#grab-coverage-area). | No additional restrictions. |

### Longer route planning
<a name="matrix-routing-longer-routes"></a>

Calculating a matrix of route results is useful for efficient route planning, but the calculation can take some time. All of the Amazon Location Service data providers put limitations on the number of routes or the distance of the routes that can be calculated. For example, HERE allows creating routes between 350 departure and destination positions, but those positions must fall within a 180km circle. What if you want to plan with longer routes?

You can calculate a matrix of routes with unrestricted lengths for a smaller numbers of routes, using, a `RouteCalculator` with HERE as the data provider. This does not change the way that you call the `[CalculateRouteMatrix](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteMatrix.html)` API, Amazon Location simply allows longer routes when you meet the requirements.

The requirements for longer length route calculations are:
+ The `RouteCalculator` must use the HERE data provider.
+ The number of departure positions must not be greater than 15.
+ The total number of routes to calculate must not be greater than 100.
+ Long distance routing is not allowed for truck routing with toll avoidances when the routes are greater than 1,000 km. This combination is slower to calculate, and can cause the call to time out. You can calculate these routes individually with the [CalculateRoute](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html) operation.

If your call does not meet these requirements (for example, you are requesting 150 route calculations in a single call), then `CalculateRouteMatrix` will revert to only allowing the shorter route rules. You can then calculate the routes, as long as the positions are within a 180km circle.

When calculating longer routes, keep these points in mind:
+ Longer routes can take longer to calculate, even longer than the maximum time for Amazon Location APIs. If you get frequent timeouts with specific routes, you can try a smaller number of routes in each call to `CalculateRouteMatrix`.
+ If you add more destination or departure positions to your `CalculateRouteMatrix` request, the operation can switch into the more restricted mode, and you can get an error for a route that can be calculated without issue when there are fewer routes to create. In this case, reduce the number of destination or departure positions, and make multiple requests to get the full set of route calculations that you need.

## Example response
<a name="example-response-route-matrix"></a>

The following is an example request with the corresponding response when calling the `[CalculateRouteMatrix](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CalculateRouteMatrix.html)` operation from the Amazon Location Routes API.

------
#### [ Example request ]

```
POST /routes/v0/calculators/{{ExampleCalculator}}/calculate/route-matrix
Content-type: application/json
{
   "DeparturePositions": [
       [{{-122.7565}},{{49.0021}}],
       [{{-122.2014}},{{47.6101}}]
   ],
   "DestinationPositions": [
       [{{-122.3394}}, {{47.6159}}],
       [{{-122.4813}},{{48.7511}}]
   ]
}
```

------
#### [ Example response ]

```
{
    "RouteMatrix": [
        [
            {
                "Distance": 178.764,
                "DurationSeconds": 7565
            },
            {
                "Distance": 39.795,
                "DurationSeconds": 1955
            }
        ],
        [
            {
                "Distance": 15.31,
                "DurationSeconds": 1217
            },
            {
                "Distance": 142.506,
                "DurationSeconds": 6279
            }
        ]
    ],
    "Summary": {
        "DataSource": "Here",
        "RouteCount": 4,
        "ErrorCount": 0,
        "DistanceUnit": "Kilometers"
    }
}
```

------
