---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/route-concepts.html
---

# Routes (V1) concepts
<a name="route-concepts"></a>

**Important**
**This page documents the previous Routes API (V1) and is only for existing applications.** The Routes V2 API is the latest version and is recommended for all new applications; see the [latest Routes Developer Guide](https://docs.aws.amazon.com//location/latest/developerguide/routes.html). The latest API is `CalculateRoutes` (plural, under the `geo-routes` namespace, exposed as `@aws-sdk/client-geo-routes` for JavaScript and `boto3.client('geo-routes')` for Python). The `CalculateRoute`, `CalculateRouteMatrix`, and `RouteCalculator` resources described below are previous-generation and only for existing applications.

This section provides an overview of the concepts around routing using Amazon Location Service.

**Note**
For information about how to use route resources in practice, see [Calculating routes using Amazon Location Service](calculating-routes.md).

## Route calculator resources
<a name="routes-overview"></a>

Route calculator resources allow you to find routes and estimate travel time based on up-to-date road network and live traffic information from your chosen data provider.

You can use the Routes APIs to build features that allow your application to request the travel time, distance, and geometry of the route between any two locations. You can also use the Routes API to request travel time and distance between a set of departures and destinations in a single request to calculate a matrix.

**Note**
For new code, use the latest `CalculateRoutes` operation under `geo-routes` instead of creating a route calculator resource. See the [latest Routes Developer Guide](https://docs.aws.amazon.com//location/latest/developerguide/routes.html).

The following shows you how to create and use a route calculator resource:

![User selecting route points, SDK box in center, and map showing calculated route path.](http://docs.aws.amazon.com/location/previous/developerguide/images/illustration-route.PNG)

1. First, you create a route calculator resource in your AWS account by selecting a data provider.

1. You can then select and install the SDK that matches your development environment and applications.

1. Start using the Amazon Location Routes APIs . For more information about how to use the routing APIs, see the topic on [Calculating routes using Amazon Location Service](calculating-routes.md).

1. You can then integrate monitoring using services such as Amazon CloudWatch and AWS CloudTrail. For more information see, [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).

## Calculating a route
<a name="route-concepts-calc-route"></a>

An Amazon Location route calculator resource provides an action called `CalculateRoute` that you can use to create a route between two geographic locations (the *departure* and the *destination*). In the latest API, this operation is `CalculateRoutes` (plural) under `geo-routes` and does not require a route calculator resource. The calculated route includes the geometry for drawing the route on a map, plus the overall time and distance of the route.

**Using waypoints**

When you are creating your route request, you can add additional waypoints to the route. These are points between the departure and the destination that act as stops along the route. The route will be calculated through each of the waypoints specified. The route from one point in the request to the next is called a `Leg`. Each leg includes a distance, time, and the geometry for that part of the route.

**Note**
The waypoints are routed in the order given in the request. They are not re-ordered for the shortest path. See the [Planning routes](#route-concepts-plan-routes)section for information on finding the shortest path.

You can include up to 25 waypoints in a single request to calculate a route.

**Traffic and departure time**

The Amazon Location Service takes traffic into account when calculating a route. The trafffic that it considers is based on the time that you specify. You can specify to depart now, or you can provide a specific time that you want to leave, which will affect the route result by adjusting for traffic at the specified time.

**Note**
You can calculate the arrival time using the departure time and route response time, to estimate the arrival of a driver, for example.

If you want Amazon Location to not take traffic into account, then do not specify a departure time and do not specify depart now. This will calculate a route that assumes the best traffic conditions for the route.

**Travel mode options**

You can set the travel mode when calculating a route using Amazon Location Service. The default travel mode is *car*, but you can alternately select either *truck* or *walking*.

If you specify either car or truck mode, you can specific additional options, as well.

For **car mode**, you can specify that you wish to avoid toll roads or ferries. This will attempt to avoid ferries and toll roads, but will still route along them, if they are the only way to get to the destination.

For **truck mode**, you can also avoid ferries and toll roads, but additionally, you can specify the size and weight of the truck, to avoid routes that will not accommodate the truck.

## Planning routes
<a name="route-concepts-plan-routes"></a>

You can use Amazon Location Service to create inputs to your route planning and optimization software. You can create route results, including travel time and travel distance, for routes between a set of departure positions and a set of destination positions. This is called creating a route *matrix*.

**Note**
There are many varying scenarios that route planning and optimization software can solve. For example, planning software can use the set of times and distances between points to calculate the shortest path that stops at each point, providing an efficient route for a single driver. Alternatively, planning software can be used to split stops between multiple trucks, providing efficiencies across a fleet, or to make sure that each customer is visited within the time frame that they require. Amazon Location provides the routing functions in an efficient way to allow the planning software to complete it's task.

For example, given departure positions A and B, and destination positions X and Y, Amazon Location Service will return travel time and travel distance for routes from A to X, A to Y, B to X, and B to Y.

As with calculating a single route, you can calculate the routes with different modes of transportation, avoidances, and traffic conditions. For example, you can specify that the vehicle is a truck that is 35 feet long, and the route calculated will use those restrictions to determine the travel time and travel distance. You can't include waypoints in a route matrix calculation.

The number of results returned (and routes calculated) is the number of departure positions multiplied by the number of destination positions. You are charged for each route calculated, not each request to the service, so a route matrix with 10 departures and 10 destinations will be billed as 100 routes.

## Route terminology
<a name="routing-components"></a>

**Route calculator resource**
An AWS resource that enables you to estimate travel time, distance, and plot routes on a map with traffic and road network data sourced from your chosen data provider.
Using route calculator resources, you calculate routes for different modes of transportation, detours, and traffic conditions.

**Route**
A route contains details used when traveling along a path from the departure position, waypoint positions, and destination position.
Examples of details in a route include:
+ The distance from one position to another position.
+ The time it takes to travel from one position to the next position.
+ The LineString geometry representing the path of the route.
For more information about routes, see the [response syntax for the CalculateRoute operation](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CalculateRoute.html) in the *Amazon Location Service Routes API reference*.
For new code, see the [latest `CalculateRoutes` operation](https://docs.aws.amazon.com//geo-routes/latest/APIReference/API_CalculateRoutes.html) under `geo-routes`.

**Route matrix**
A list of routes, from a set of departure positions to a set of destination positions. Useful as inputs into route planning or optimization software.
For more information about calculating a route matrix, see the [syntax for the CalculateRouteMatrix operation](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CalculateRouteMatrix.html) in the *Amazon Location Service Routes API reference*.
The latest API exposes the equivalent operation as [`CalculateRouteMatrix` under `geo-routes`](https://docs.aws.amazon.com//geo-routes/latest/APIReference/API_CalculateRouteMatrix.html), which does not require a route calculator resource.

**`LineString` geometry**
An Amazon Location route consists of one or more legs (a route from one waypoint to another within the overall route). The geometry of each leg is a polyline represented as a `LineString`. A `LineString` is an ordered array of positions that can be used to plot a route on a map.
The following is an example of a `LineString` with three points:

```
[
    {{[-122.7565,49.0021]}},
    {{[-122.3394,47.6159]}},
    {{[-122.1082,45.8371]}}
]
```

**Waypoint**
Waypoints are intermediate positions that act as stops along a route between the departure position and destination position. The stopover order on the route follows the order that you provide the waypoint positions in the request.

**Leg**
A single leg is the journey from one position to another position. If the positions aren't located on a road, they're moved to the nearest road. The number of legs in a route is one less than the total number of positions.
A route with no waypoints consists of a single leg, from the departure position to the destination. A route with 1 waypoint consists of 2 legs, from the departure position to the waypoint, and then from the waypoint to the destination.

**Step**
A step is a subsection of a leg. Each step provides summary information for that step in the leg.
