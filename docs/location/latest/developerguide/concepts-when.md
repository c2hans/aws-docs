---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/concepts-when.html
---

# When (departure and arrival)
<a name="concepts-when"></a>

Specifies the time for route calculation. The time not only determines the timestamps for departure and arrival but also influences the traffic data to be used.

| Parameter | Description | Routes | Routes Matrix | Isoline | Optimize Waypoint | Snap To Road |
| --- | --- | --- | --- | --- | --- | --- |
| Departure Time | Time of departure from the Origin. If neither arrival nor departure time is provided, dynamic traffic information is not used, and only free-flow speeds based on historical traffic are applied. | Yes | Yes | Yes | Yes | No |
| Depart Now | Uses the current time as the time of departure from the Origin. | Yes | Yes | Yes | No | No |
| Arrival Time | Time of arrival at the destination. If neither arrival nor departure time is provided, dynamic traffic information is not used, and only free-flow speeds based on historical traffic are applied. | Yes | No | Yes | No | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
