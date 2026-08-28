---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/monitoring-cloudwatch-json-alert.html
---

# JSON for an alert event
<a name="monitoring-cloudwatch-json-alert"></a>

Events that are based on [alerts](monitor-activity-types-alerts-channels.md) are identified by their `detail-type` property:
+ `MediaLive Channel Alert` for a channel
+ `MediaLive Multiplex Alert` for a multiplex.

**Example**

Following is an example of the JSON payload for an alert event. Note the `detail-type` in line 3.

```
{
    "version": "0",
    "id": "154769fb-9f7c-32a1-6822-26fppppe5a58",
    "detail-type": "MediaLive Channel Alert",
    "source": "aws.medialive",
    "account": "111122223333",
    "time": "2023-03-08T18:14:25Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:medialive:us-west-2:111122223333:channel:123456"
    ],
    "detail": {
        "alarm_state": "CLEARED",
        "alarm_id": "7ad616bd389832yue90aab1324bffab5b834a",
        "alert_type": "Failed to Create Output File or Socket",
        "pipeline": "0",
        "channel_arn": "arn:aws:medialive:us-west-2:111122223333:channel:123456",
        "message": "MPEGTS muxer for mediaID [1] unable to open output or stream [https://{{<path>}}]."
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
