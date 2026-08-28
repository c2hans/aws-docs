---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/disassociate-tracker.html
---

# Tutorial: Disconnect a tracker from a geofence collection
<a name="disassociate-tracker"></a>

You can disconnect a tracker from a geofence collection using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To disassociate a tracker from an associated geofence collection using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Trackers** from the left navigation pane.

1. Under **My trackers**, select the name link of the target tracker.

1. Under **Linked Geofence Collections**, select a geofence collection with a **Linked** status.

1. Choose **Unlink**.

------
#### [ API ]

Use the `[DisassociateTrackerConsumer](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_DisassociateTrackerConsumer.html)` operation from the Amazon Location Trackers APIs.

The following example is an API request to disassociate a tracker from an associated geofence collection.

```
DELETE /tracking/v0/trackers/{{ExampleTracker}}/consumers/arn:aws:geo:us-west-2:123456789012:geofence-collection/ExampleCollection
```

The following is an example response for `[DisassociateTrackerConsumer](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_DisassociateTrackerConsumer.html)`:

```
HTTP/1.1 200
```

------
#### [ CLI ]

Use the `[disassociate-tracker-consumer](https://docs.aws.amazon.com/cli/latest/reference/location/disassociate-tracker-consumer.html)` command.

The following example is an AWS CLI command to disassociate a tracker from an associated geofence collection.

```
aws location disassociate-tracker-consumer \
    --consumer-arn "arn:aws:geo:us-west-2:123456789012:geofence-collection/ExampleCollection" \
    --tracker-name "{{ExampleTracker}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
