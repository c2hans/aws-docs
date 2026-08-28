---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/delete-geofence-collection.html
---

# Tutorial: Delete a geofence collection
<a name="delete-geofence-collection"></a>

You can delete a geofence collection from your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To delete a geofence collection using the Amazon Location console**

**Warning**
This operation deletes the resource permanently.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Geofence collections** from the left navigation pane.

1. Under **My geofence collection**, select the target geofence collection.

1. Choose **Delete geofence collection**.

------
#### [ API ]

Use the `[DeleteGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteGeofenceCollection.html)` operation from the Amazon Location APIs.

The following example is an API request to delete the geofence collection {{ExampleCollection}}.

```
DELETE /geofencing/v0/collections/{{ExampleCollection}}
```

The following is an example response for `DeleteGeofenceCollection`:

```
HTTP/1.1 200
```

------
#### [ CLI ]

Use the `[delete-geofence-collection](https://docs.aws.amazon.com/cli/latest/reference/location/delete-geofence-collection.html)` command.

The following example is an AWS CLI command to delete the geofence collection {{ExampleCollection}}.

```
aws location delete-geofence-collection \
    --collection-name "{{ExampleCollection}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
