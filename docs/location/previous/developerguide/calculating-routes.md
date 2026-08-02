---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/calculating-routes.html
---

# Calculating routes using Amazon Location Service
<a name="calculating-routes"></a>

**Note**
We released a new version of the Routes API, see the updated [Routes Developer Guide](https://docs.aws.amazon.com//location/latest/developerguide/routes.html) or [Routes API](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html) for revised information.

Amazon Location lets you select a data provider for calculating a route by creating and configuring a route calculator resource.

You can use the route calculator resource to [calculate a route](calculate-route.md) given specific parameters using the AWS SDK, or the REST API endpoints. Use this route calculator resource to calculate routes between an origin, a destination and up to 23 waypoints for different modes of transportation, avoidances, and traffic conditions.

You can also use the route calculator resource to create inputs for your route planning algorithms or products by [calculating a route matrix](calculate-route-matrix.md). Calculate the travel time and travel distance between a set of departure positions and a set of destination positions. Route planning software can use that time and distance data to optimize a route or a set of routes; for example, if you are planning multiple delivery routes, and want to find the best route and time for each stop. You can calculate a matrix of routes for different modes of transportation, avoidances, and traffic conditions.

**Note**
For an overview of routing concepts, see [Routes (V1) concepts](route-concepts.md).

**Topics**
+ [Prerequisites for calculating routes using Amazon Location](routes-prerequisites.md)
+ [Calculate a route with Amazon Location](calculate-route.md)
+ [Route planning with a route matrix in Amazon Location](calculate-route-matrix.md)
+ [Positions not located on a road in Amazon Location](snap-to-nearby-road.md)
+ [Departure time with Amazon Location](departure-time.md)
+ [Travel mode with Amazon Location](travel-mode.md)
+ [Managing your route calculator resources with Amazon Location](managing-route-calculators.md)
