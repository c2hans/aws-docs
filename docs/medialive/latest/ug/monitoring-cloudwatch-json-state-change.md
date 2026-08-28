---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/monitoring-cloudwatch-json-state-change.html
---

# JSON for a state change event
<a name="monitoring-cloudwatch-json-state-change"></a>

Events that are based on a change of state in a [channel or multiplex](monitor-activity-types-channel.md) are identified by their `detail-type` property:
+ `MediaLive Channel State Change` for a channel
+ `MediaLive Multiplex State Change` for a multiplex.

**Example**

Following is an example of the JSON payload for a state change event. Note the `detail-type` in line 3.

```
{
    "version": "0",
    "id": "fbcbbbe3-2541-d4a3-d819-x39f522a8ce",
    "detail-type": "MediaLive Channel State Change",
    "source": "aws.medialive",
    "account": "111122223333",
    "time": "2023-03-08T18:40:59Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:medialive:us-west-2:111122223333:channel:283886"
    ],
    "detail": {
        "channel_arn": "arn:aws:medialive:us-west-2:111122223333:channel:123456",
        "state": "DELETED",
        "message": "Deleted channel",
        "pipelines_running_count": 0
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
