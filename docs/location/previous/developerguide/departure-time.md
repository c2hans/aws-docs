---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html
---

# Departure time with Amazon Location
<a name="departure-time"></a>

By default, when you call `CalculateRoute` or `CalculateRouteMatrix`, if you don't provide a departure time in the request, the calculated routes reflects optimal traffic conditions.

You can set a specific a departure time to use live and predictive traffic conditions from your chosen data provider, by using one of the following options:
+ `DepartNow` – When set to {{true}}, it uses live traffic conditions to calculate the fastest travel path.
+ `DepartureTime` – When provided, it uses predictive and known traffic conditions for the requested time. Defined in the following [format](https://www.iso.org/iso-8601-date-and-time-format.html): `YYYY-MM-DDThh:mm:ss.sssZ`.

**Example**
The following `[CalculateRoute](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CalculateRoute.html)` request sets the departure time to July 2, 2024, at 12:15:20 UTC.

```
POST /routes/v0/calculators/ExampleCalculator/calculate/route
Content-type: application/json
{
   "DeparturePosition": [-122.7565,49.0021],
   "DestinationPosition": [-122.3394, 47.6159],
   "WaypointPositions":[
        [-122.1884,48.0936],
        [-122.3493,47.6205]
    ]
    "IncludeLegGeometry": true,
    "DepartureTime": {{2024-07-02T12:15:20.000Z}},
}
```
