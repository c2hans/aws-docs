---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/get-geofence-collection-details.html
---

# Tutorial: Get geofence collection details
<a name="get-geofence-collection-details"></a>

You can get details about any geofence collection resource in your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

------
#### [ Console ]

**To view the details of a geofence collection using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Geofence collections** from the left navigation pane.

1. Under **My geofence collections**, select the name link of the target geofence collection.

------
#### [ API ]

Use the `[DescribeGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeGeofenceCollection.html)` operation from the Amazon Location Geofences APIs.

The following example is an API request to get the geofence collection details for {{ExampleCollection}}.

```
GET /geofencing/v0/collections/{{ExampleCollection}}
```

The following is an example response for `DescribeGeofenceCollection`:

```
{
    "CollectionArn": "arn:aws:geo:us-west-2:123456789012:geofence-collection/GeofenceCollection",
    "CollectionName": "{{ExampleCollection}}",
    "CreateTime": 2020-09-30T22:59:34.142Z,
    "Description": "string",
    "KmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "Tags": {
        "Tag1" : "Value1"
    },
    "UpdateTime": 2020-09-30T23:59:34.142Z
}
```

------
#### [ CLI ]

Use the `[describe-geofence-collection](https://docs.aws.amazon.com/cli/latest/reference/location/describe-geofence-collection.html)` command.

The following example is an AWS CLI to get the geofence collection details for {{ExampleCollection}}.

```
aws location describe-geofence-collection \
    --collection-name "{{ExampleCollection}}"
```

------
