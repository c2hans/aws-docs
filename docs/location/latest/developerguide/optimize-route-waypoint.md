---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/optimize-route-waypoint.html
---

# Optimize route and waypoint sequence
<a name="optimize-route-waypoint"></a>

## Optimize routing
<a name="optimize-routing"></a>

Optimization criteria for when calculating a route. This can either be the fastest route measured by time or the shortest route measured by distance.

| Option | Description | Measurement |
| --- | --- | --- |
| Fastest Route | Calculate the fastest route, focusing on minimizing travel time. This takes into account traffic conditions, road speed limits, and other factors. | Time |
| Shortest Route | Calculate the shortest route, minimizing the distance traveled. This is often used when distance is the key factor, such as reducing fuel costs or emissions. | Distance |

## Optimize waypoint
<a name="optimize-waypoint"></a>

Optimization criteria for sequencing waypoints in a route.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
