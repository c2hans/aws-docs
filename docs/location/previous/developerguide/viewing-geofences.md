---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/viewing-geofences.html
---

# Tutorial: List stored geofences
<a name="viewing-geofences"></a>

You can list geofences stored in a specified geofence collection using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To view a list of geofences using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Geofence collections** from the left navigation pane.

1. Under **My geofence collection**, select the name link of the target geofence collection.

1. View geofences in the geofence collection under **Geofences**

------
#### [ API ]

Use the `[ListGeofences](https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofences.html)` operation from the Amazon Location Geofences APIs.

The following example is an API request to get a list of geofences stored in the geofence collection {{ExampleCollection}}.

```
POST /geofencing/v0/collections/{{ExampleCollection}}/list-geofences
```

The following is an example response for `ListGeofences`:

```
{
   "Entries": [
      {
         "CreateTime": 2020-09-30T22:59:34.142Z,
         "GeofenceId": "geofence-1",
         "Geometry": {
             "Polygon": [
                 [-5.716667, -15.933333,
                 [-14.416667, -7.933333],
                 [-12.316667, -37.066667],
                 [-5.716667, -15.933333]
             ]
         },
         "Status": "ACTIVE",
         "UpdateTime": 2020-09-30T23:59:34.142Z
      }
   ],
   "NextToken": "1234-5678-9012"
}
```

------
#### [ CLI ]

Use the `[list-geofences](https://docs.aws.amazon.com/cli/latest/reference/location/list-geofences.html)` command.

The following example is an AWS CLI to get a list of geofences stored in the geofence collection {{ExampleCollection}}.

```
aws location list-geofences \
    --collection-name "{{ExampleCollection}}"
```

------
