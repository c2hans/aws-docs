---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html
---

# Positions not located on a road in Amazon Location
<a name="snap-to-nearby-road"></a>

When using `CalculateRoute` or `CalculateRouteMatrix`, if you specify a departure, destination, or waypoint position that's not located on a road Amazon Location moves the position to a nearby road.

The following `[CalculateRoute](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CalculateRoute.html)` request specifies a departure position and destination position that's not located on a road:

```
POST /routes/v0/calculators/{{ExampleCalculator}}/calculate/route
Content-type: application/json
{
   "DeparturePosition": [{{-123.128014, 49.298472}}],
   "DestinationPosition": [{{-123.134701, 49. 294315}}]
}
```

The resulting response returns a position that's snapped to a nearby road:

```
{
   "Legs": [
      {
         "StartPosition": [{{-123.12815, 49.29717}}],
         "EndPosition":   [{{-123.13375, 49.2926}}],
         "Distance": 4.223,
         "DurationSeconds": 697,
         "Steps": [
            {
               "StartPosition": [ -123.12815, 49.29717 ],
               "EndPosition":   [ -123.12806, 49.29707 ],
               "Distance": 0.013,
               "DurationSeconds": 8
            },
            {
               "StartPosition": [ -123.12806, 49.29707 ],
               "EndPosition":   [ -123.1288, 49.29659 ],
               "Distance": 0.082,
               "DurationSeconds": 36
            },
            {
               "StartPosition": [ -123.1288, 49.29659 ],
               "EndPosition":   [ -123.12021, 49.29853 ],
               "Distance": 0.742,
               "DurationSeconds": 128
            },
            {
               "StartPosition": [ -123.12021, 49.29853 ],
               "EndPosition":   [ -123.1201, 49.29959 ],
               "Distance": 0.131,
               "DurationSeconds": 26
            },
            {
               "StartPosition": [ -123.1201, 49.29959 ],
               "EndPosition":   [ -123.13562, 49.30681 ],
               "Distance": 1.47,
               "DurationSeconds": 238
            },
            {
               "StartPosition": [ -123.13562, 49.30681 ],
               "EndPosition":   [ -123.13693, 49.30615 ],
               "Distance": 0.121,
               "DurationSeconds": 28
            },
            {
               "StartPosition": [ -123.13693, 49.30615 ],
               "EndPosition":   [ -123.13598, 49.29755 ],
               "Distance": 0.97,
               "DurationSeconds": 156
            },
            {
               "StartPosition": [ -123.13598, 49.29755 ],
               "EndPosition":   [ -123.13688, 49.29717 ],
               "Distance": 0.085,
               "DurationSeconds": 15
            },
            {
               "StartPosition": [ -123.13688, 49.29717 ],
               "EndPosition":   [ -123.13375, 49.2926 ],
               "Distance": 0.609,
               "DurationSeconds": 62
            }
         ]
      }
   ],
   "Summary": {
      "RouteBBox": [ -123.13693, 49.2926, -123.1201, 49.30681 ],
      "DataSource": "Here",
      "Distance": 4.223,
      "DurationSeconds": 697,
      "DistanceUnit": "Kilometers"
   }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
