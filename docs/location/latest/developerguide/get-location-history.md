---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/get-location-history.html
---

# Get a device's location history from a tracker
<a name="get-location-history"></a>

 Your Amazon Location tracker resource maintains the location history of all your tracked devices for a period of 30 days. You can retrieve device location history, including all associated metadata, from your tracker resource. The following examples use the AWS CLI, or the Amazon Location APIs.

------
#### [ API ]

**To get the device location history from a tracker using the Amazon Location APIs**

Use the `[GetDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePositionHistory.html)` operation from the Amazon Location Trackers APIs.

The following example uses an API URI request to get the device location history of {{ExampleDevice}} from a tracker called {{ExampleTracker}} starting from `19:05:07` (inclusive) and ends at `19:20:07` (exclusive) on `2020–10–02`.

```
POST /tracking/v0/trackers/{{ExampleTracker}}/devices/{{ExampleDevice}}/list-positions
Content-type: application/json
{
  "StartTimeInclusive": "2020-10-02T19:05:07.327Z",
  "EndTimeExclusive": "2020-10-02T19:20:07.327Z"
}
```

------
#### [ AWS CLI ]

**To get the device location history from a tracker using AWS CLI commands**

Use the `[get-device-position-history](https://docs.aws.amazon.com/cli/latest/reference/location/get-device-position-history.html)` command.

The following example uses an AWS CLI to get the device location history of {{ExampleDevice}} from a tracker called {{ExampleTracker}} starting from `19:05:07` (inclusive) and ends at `19:20:07` (exclusive) on `2020–10–02`.

```
aws location \
    get-device-position-history \
        --device-id "{{ExampleDevice}}" \
        --start-time-inclusive "2020-10-02T19:05:07.327Z" \
        --end-time-exclusive "2020-10-02T19:20:07.327Z" \
        --tracker-name "{{{{ExampleTracker}}}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
