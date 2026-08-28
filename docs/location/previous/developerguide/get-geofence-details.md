---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/get-geofence-details.html
---

# Tutorial: Get geofence details
<a name="get-geofence-details"></a>

You can get the details of a specific geofence, such as the create time, update time, geometry, and status, from a geofence collection using the Amazon Location console, AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To view the status of a geofence using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. Choose **Geofence collections** from the left navigation pane.

1. Under **My geofence collection**, select the name link of the target geofence collection.

1. Under **Geofences**, you’ll be able to view the status of your geofences.

------
#### [ API ]

Use the `[GetGeofence](https://docs.aws.amazon.com/location/previous/APIReference/API_GetGeofence.html)` operation from the Amazon Location Geofences APIs.

The following example is an API request to get the geofence details from a geofence collection {{ExampleCollection}}.

```
GET /geofencing/v0/collections/{{ExampleCollection}}/geofences/{{ExampleGeofence1}}
```

The following is an example response for `GetGeofence`:

```
{
   "CreateTime": 2020-09-30T22:59:34.142Z,
   "GeofenceId": "{{ExampleGeofence1}}",
   "Geometry": {
      "Polygon": [
          [-1,-1],
          [1,-1],
          [0,1],
          [-1,-1]
      ]
   },
   "Status": "ACTIVE",
   "UpdateTime": 2020-09-30T23:59:34.142Z
}
```

------
#### [ CLI ]

Use the `[get-geofence](https://docs.aws.amazon.com/cli/latest/reference/location/get-geofence.html)` command.

The following example is an AWS CLI to get the geofence collection details for {{ExampleCollection}}.

```
aws location get-geofence \
    --collection-name "{{ExampleCollection}}" \
    --geofence-id "{{ExampleGeofence1}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
