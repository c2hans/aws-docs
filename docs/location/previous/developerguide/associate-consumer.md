---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/associate-consumer.html
---

# Tutorial: Link a tracker to a geofence collection in Amazon Location
<a name="associate-consumer"></a>

Now that you have a geofence collection and a tracker, you can link them together so that location updates are automatically evaluated against all of your geofences. If you don’t want to evaluate all location updates, or alternatively, if you aren't storing some of your locations in a tracker resource, you can [evaluate device positions against geofences](https://docs.aws.amazon.com/location/previous/developerguide/evaluate-geofences.html) on demand.

When device positions are evaluated against geofences, events are generated. You can set an action to these events. For more information about actions that you can set for geofence events, see [Reacting to Amazon Location Service events with Amazon EventBridge](https://docs.aws.amazon.com/location/previous/developerguide/location-events.html).

An Amazon Location event includes the attributes of the device position update that generates it and some attributes of the geofence that is entered or exited. For more information about the data included in a geofence event, see [Amazon EventBridge event examples for Amazon Location Service](location-events.md#example-event).

The following examples link a tracker resource to a geofence collection using the console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To link a tracker resource to a geofence collection using the Amazon Location Service console**

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. In the left navigation pane, choose **Trackers**.

1. Under **Device trackers**, select the name link of the target tracker.

1. Under **Linked Geofence Collections**, choose **Link Geofence Collection**.

1. In the **Linked Geofence Collection** window, select a geofence collection from the dropdown menu.

1. Choose **Link**.

After you link the tracker resource, it will be assigned an **Active** status.

------
#### [ API ]

**To link a tracker resource to a geofence collection using the Amazon Location APIs**

Use the `[AsssociateTrackerConsumer](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_AssociateTrackerConsumer.html)` operation from the Amazon Location Trackers APIs.

The following example uses an API request that associates {{ExampleTracker}} with a geofence collection using its [Amazon Resource Name ](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)(ARN).

```
POST /tracking/v0/trackers/{{ExampleTracker}}/consumers
Content-type: application/json

{
   "ConsumerArn": "arn:aws:geo:us-west-2:123456789012:geofence-collection/{{ExampleGeofenceCollection}}"
}
```

------
#### [ AWS CLI ]

**To link a tracker resource to a geofence collection using AWS CLI commands**

Use the `[associate-tracker-consumer](https://docs.aws.amazon.com/cli/latest/reference/location/associate-tracker-consumer.html)` command.

The following example uses an AWS CLI to create a geofence collection called {{ExampleGeofenceCollection}}.

```
aws location \
    associate-tracker-consumer \
        --consumer-arn "arn:aws:geo:us-west-2:123456789012:geofence-collection/{{ExampleGeofenceCollection}}" \
        --tracker-name "{{{{ExampleTracker}}}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
