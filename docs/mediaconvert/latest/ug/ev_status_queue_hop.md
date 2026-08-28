---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/ev_status_queue_hop.html
---

# Events with QUEUE\_HOP status
<a name="ev_status_queue_hop"></a>

MediaConvert sends the `QUEUE_HOP` event when a job hops queues. It contains the ARNs for both queues and the job's priority within the queues.

Both `priority` and `previousPriority` will be the same unless the queue hopping configuration specifies a new priority to give to the job as it hops queues.

The following JSON is an example event containing the `QUEUE_HOP` status for a job.

```
{
    "version": "0",
    "id": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "detail-type": "MediaConvert Job State Change",
    "source": "aws.mediaconvert",
    "account": "111122223333",
    "time": "2018-01-07T23:35:20Z",
    "region": "us-west-2",
    "resources": ["arn:aws:mediaconvert:us-west-2:111122223333:jobs/1515368087458-qnoxtd"],
    "detail": {
        "timestamp": 1515368120764,
        "accountId": "111122223333",
        "queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default",
        "previousQueue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Alternate",
        "priority": 0,
        "previousPriority": 0,
        "jobId": "1515368087458-qnoxtd",
        "status": "QUEUE_HOP",
        "userMetadata": {}
    }
}
```

You can use the following sample JSON to create an EventBridge event pattern for jobs with a status of `QUEUE_HOP`.

```
{
    "source": ["aws.mediaconvert"],
    "detail-type": ["MediaConvert Job State Change"],
    "detail": {
        "status": ["QUEUE_HOP"]
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
