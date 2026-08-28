---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/delete-geofence.html
---

# Tutorial: Delete geofences
<a name="delete-geofence"></a>

You can delete geofences from a geofence collection using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To delete a geofence using the Amazon Location console**

**Warning**
This operation deletes the resource permanently.

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Geofence collections** from the left navigation pane.

1. Under **My geofence collection**, select the name link of the target geofence collection.

1. Under **Geofences**, select the target geofence.

1. Choose **Delete geofence**.

------
#### [ API ]

Use the `[BatchDeleteGeofence](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchDeleteGeofence.html)` operation from the Amazon Location Geofences APIs.

The following example is an API request to delete geofences from the geofence collection {{ExampleCollection}}.

```
POST /geofencing/v0/collections/{{ExampleCollection}}/delete-geofences
Content-type: application/json

{
   "GeofenceIds": [ "{{ExampleGeofence11}}" ]
}
```

The following is an example success response for `[BatchDeleteGeofence](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchDeleteGeofence.html)`.

```
HTTP/1.1 200
```

------
#### [ CLI ]

Use the `[batch-delete-geofence](https://docs.aws.amazon.com/cli/latest/reference/location/batch-delete-geofence.html)` command.

The following example is an AWS CLI command to delete geofences from the geofence collection {{ExampleCollection}}.

```
aws location batch-delete-geofence \
    --collection-name "{{ExampleCollection}}" \
    --geofence-ids "{{ExampleGeofence11}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
