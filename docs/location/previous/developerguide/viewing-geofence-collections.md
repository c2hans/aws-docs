---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/viewing-geofence-collections.html
---

# Tutorial: List your geofence collection resources
<a name="viewing-geofence-collections"></a>

You can view your geofence collection list using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To view a list of geofence collections using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Geofence collections** from the left navigation pane.

1. View a list of your geofence collections under **My geofence collections**.

------
#### [ API ]

Use the `[ListGeofenceCollections](https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofenceCollections.html)` operation from the Amazon Location Geofences APIs.

The following example is an API request to get a list of geofence collections in the AWS account.

```
POST /geofencing/v0/list-collections
```

The following is an example response for `ListGeofenceCollections`:

```
{
    "Entries": [
    {
        "CollectionName": "{{ExampleCollection}}",
        "CreateTime": 2020-09-30T22:59:34.142Z,
        "Description": "string",
        "UpdateTime": 2020-09-30T23:59:34.142Z
    },
    "NextToken": "1234-5678-9012"
}
```

------
#### [ CLI ]

Use the `[list-geofence-collections](https://docs.aws.amazon.com/cli/latest/reference/location/list-geofence-collections.html)` command.

The following example is an AWS CLI to get a list of geofence collections in the AWS account.

```
aws location list-geofence-collections
```

------
