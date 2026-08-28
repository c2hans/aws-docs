---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/concepts-traffic-awareness.html
---

# Traffic awareness
<a name="concepts-traffic-awareness"></a>

Determines the type of traffic-related information used during route calculation. Flow traffic represents congestion, excluding long-term incident-related congestion. The accuracy of flow traffic data decreases over time, making historical traffic data more reliable for past events.

| Parameter | Description | Routes | Routes Matrix | Isoline | Optimize Waypoint | Snap To Road |
| --- | --- | --- | --- | --- | --- | --- |
| Usage | Enable or disable traffic data during route calculation. When enabled, if `DepartureTime`, `ArrivalTime`, or `DepartNow` are not provided, only long-term closures will be considered. Otherwise, if a time is provided, all traffic data is taken into account. | Yes | Yes | Yes | Yes | No |
| FlowEventThresholdOverride | Duration in seconds for which a flow traffic event is considered valid. While valid, flow traffic data will be used over historical traffic data. | Yes | Yes | Yes | No | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
