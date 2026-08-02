---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/delete-tracker.html
---

# Tutorial: Delete a tracker with Amazon Location
<a name="delete-tracker"></a>

You can delete a tracker from your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To delete an existing map resource using the Amazon Location console**

**Warning**
This operation deletes the resource permanently. If the tracker resource is in use, you may encounter an error. Make sure that the target resource isn't a dependency for your applications.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Trackers** from the left navigation pane.

1. Under **My trackers**, select the target tracker.

1. Choose **Delete tracker**.

------
#### [ API ]

Use the `[DeleteTracker](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_DeleteTracker.html)` operation from the Amazon Location Tracker APIs.

The following example is an API request to delete the tracker {{ExampleTracker}}.

```
DELETE /tracking/v0/trackers/{{ExampleTracker}}
```

The following is an example response for `[DeleteTracker](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_DeleteTracker.html)`:

```
HTTP/1.1 200
```

------
#### [ CLI ]

Use the `[delete-tracker](https://docs.aws.amazon.com/cli/latest/reference/location/delete-tracker.html)` command.

The following example is an AWS CLI command to delete the tracker {{ExampleTracker}}.

```
aws location delete-tracker \
    --tracker-name "{{ExampleTracker}}"
```

------
