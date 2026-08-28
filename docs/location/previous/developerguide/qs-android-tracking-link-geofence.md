---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-link-geofence.html
---

# Tutorial: Link a tracker to a geofence collection
<a name="qs-android-tracking-link-geofence"></a>

To link a tracker to a geofence collection you can use either the console, API, or CLI. The following procedures walk you through each option.

Link a tracker resource to a geofence collection using the Amazon Location Service console:

1.  Open the Amazon Location console.

1.  In the left navigation pane, choose **Trackers**.

1.  Under **Device Trackers**, select the name link of the target tracker.

1.  Under **Linked Geofence Collections**, choose **Link Geofence Collection**.

1.  In the **Linked Geofence Collection window**, select a geofence collection from the dropdown menu.

1.  Choose **Link**.

1.  After you link the tracker resource, it will be assigned an Active status.

Link a tracker resource to a geofence collection using the Amazon Location APIs:

Use the `AsssociateTrackerConsumer` operation from the Amazon Location Trackers APIs. The following example uses an API request that associates an `ExampleTracker` with a geofence collection using its Amazon Resource Name (ARN).

```
        POST /tracking/v0/trackers/ExampleTracker/consumers
        Content-type: application/json
        {
           "ConsumerArn": "arn:aws:geo:us-west-2:123456789012:geofence-collection/{{GOECOLLECTION_NAME}}"
            }
```

Link a tracker resource to a geofence collection using AWS CLI commands:

Use the `associate-tracker-consumer ` command. The following example uses an AWS CLI to create a geofence collection called `{{GOECOLLECTION_NAME}}`.

```
aws location \
associate-tracker-consumer \
    --consumer-arn "arn:aws:geo:us-west-2:123456789012:geofence-collection/{{GOECOLLECTION_NAME}}" \
    --tracker-name "ExampleTracker"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
