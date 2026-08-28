---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/start-tracking.html
---

# Start tracking with Amazon Location
<a name="start-tracking"></a>

This section guides you through building a tracking application that captures device locations.

**Topics**
+ [Create a tracker](#start-create-tracker)
+ [Authenticating your requests](#tracking-identity-pool)
+ [Update your tracker with a device position](#send-location-updates)
+ [Get a device's location history from a tracker](#get-location-history)
+ [List your device positions](#list-device-positions)

## Create a tracker
<a name="start-create-tracker"></a>

Create a tracker resource to store and process position updates from your devices. You can use the Amazon Location Service console, the AWS CLI, or the Amazon Location APIs.

Each position update stored in your tracker resources can include a measure of position accuracy, and up to three fields of metadata about the position or device that you want to store. The metadata is stored as key-value pairs, and can store information such as speed, direction, tire pressure, or engine temperature.

Trackers filter position updates as they are received. This reduces visual noise in your device paths (called *jitter*), and reduces the number of false geofence entry and exit events. This also helps manage costs by reducing the number of geofence evaluations initiated.

Trackers offer three position filtering options to help manage costs and reduce jitter in your location updates.
+ **Accuracy-based** – *Use with any device that provides an accuracy measurement. Most mobile devices provide this information.* The accuracy of each position measurement is affected by many environmental factors, including GPS satellite reception, landscape, and the proximity of Wi-Fi and Bluetooth devices. Most devices, including most mobile devices, can provide an estimate of the accuracy of the measurement along with the measurement. With `AccuracyBased` filtering, Amazon Location ignores location updates if the device moved less than the measured accuracy. For example, if two consecutive updates from a device have an accuracy range of 5 m and 10 m, Amazon Location ignores the second update if the device has moved less than 15 m. Amazon Location neither evaluates ignored updates against geofences, nor stores them.

   When accuracy is not provided, it is treated as zero, and the measurement is considered perfectly accurate.
**Note**
You can also use accuracy-based filtering to remove all filtering. If you select accuracy-based filtering, but override all accuracy data to zero, or omit the accuracy entirely, then Amazon Location will not filter out any updates.
+ **Distance-based** – *Use when your devices do not provide an accuracy measurement, but you still want to take advantage of filtering to reduce jitter and manage costs.* `DistanceBased` filtering ignores location updates in which devices have moved less than 30 m (98.4 ft). When you use `DistanceBased` position filtering, Amazon Location neither evaluates these ignored updates against geofences nor stores the updates.

  The accuracy of most mobile devices, including the average accuracy of iOS and Android devices, is within 15 m. In most applications, `DistanceBased` filtering can reduce the effect of location inaccuracies when displaying device trajectory on a map, and the bouncing effect of multiple consecutive entry and exit events when devices are near the border of a geofence. It can also help reduce the cost of your application, by making fewer calls to evaluate against linked geofences or retrieve device positions.
+ **Time-based** – (default) *Use when your devices send position updates very frequently (more than once every 30 seconds), and you want to achieve near real-time geofence evaluations without storing every update. *In `TimeBased` filtering, every location update is evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID.

**Note**
Be mindful of the costs of your tracking application when deciding your filtering method and the frequency of position updates. You are billed for every location update and once for evaluating the position update against each linked geofence collection. For example, when using time-based filtering, if your tracker is linked to two geofence collections, every position update will count as one location update request and two geofence collection evaluations. If you are reporting position updates every 5 seconds for your devices and using time-based filtering, you will be billed for 720 location updates and 1,440 geofence evaluations per hour for each device.
Your bill is not affected by the number of geofences in each collection. Since each geofence collection may contain up to 50,000 geofences, you may want to combine your geofences into fewer collections, where possible, to reduce your cost of geofence evaluations.

By default, you will get EventBridge events each time a tracked device enters or exits a linked geofence. For more information, see [Tutorial: Link a tracker to a geofence collection in Amazon Location](associate-consumer.md).

You can enable events for all filtered position updates for a tracker resource. For more information, see [Enable update events for a tracker](location-events.md#enable-update-events).

**Note**
If you wish to encrypt your data using your own AWS KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this Bounding Polygon Queries feature, a representation of your device positions will not be encrypted using the your AWS KMS managed key. However, the exact device position is still encrypted using your managed key.
You can choose to opt-in to the Bounding Polygon Queries feature by setting the `KmsKeyEnableGeospatialQueries` parameter to true when creating or updating a Tracker.

------
#### [ Console ]

**To create a tracker using the Amazon Location console**

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. In the left navigation pane, choose **Trackers**.

1. Choose **Create tracker**.

1. Fill the following fields:
   + ****Name **** – Enter a unique name. For example, {{ExampleTracker}}. Maximum 100 characters. Valid entries include alphanumeric characters, hyphens, periods, and underscores.
   + ****Description** ** – Enter an optional description.

1. Under **Position filtering**, choose the option that best fits how you intend to use your tracker resource. If you do not set **Position filtering**, the default setting is `TimeBased`. For more information, see [Learn about trackers in Amazon Location Service](tracking-overview.md) in this guide, and `[PositionFiltering](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_CreateTracker.html#locationtrackers-CreateTracker-request-PositionFiltering)` in the Amazon Location Service Trackers API Reference.

1. (Optional) Under **Tags**, enter a tag **Key** and **Value**. This adds a tag your new geofence collection. For more information, see [Tagging your resources](tagging.md).

1. (Optional) Under **Customer managed key encryption**, you can choose to **Add a customer managed key**. This adds a symmetric customer managed key that you create, own, and manage over the default AWS owned encryption. For more information, see [Encrypting data at rest](encryption-at-rest.md).

1. (Optional) Under **KmsKeyEnableGeospatialQueries**, you can choose to enable **Geospatial Queries**. This allows you use the Bounding Polygon Queries feature, while encrypting your data using a customer AWS KMS managed key.
**Note**
When you use the Bounding Polygon Queries feature a representation of your device positions is not be encrypted using the your AWS KMS managed key. However, the exact device position is still encrypted using your managed key.

1. (Optional) Under **EventBridge configuration**, you can choose to enable EventBridge events for filtered position updates. This will send an event each time a position update for a device in this tracker meets the position filtering evaluation.

1. Choose **Create tracker**.

------
#### [ API ]

**To create a tracker by using the Amazon Location APIs**

Use the `[CreateTracker](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_CreateTracker.html)` operation from the Amazon Location Trackers APIs.

The following example uses an API request to create a tracker called {{ExampleTracker}}. The tracker resource is associated with a [customer managed AWS KMS key to encrypt customer data](encryption-at-rest.md), and does not [enable position updates in EventBridge](location-events.md#enable-update-events).

```
POST /tracking/v0/trackers
Content-type: application/json

{

   "TrackerName": "ExampleTracker",
   "Description": "string",
   "KmsKeyEnableGeospatialQueries": false,
   "EventBridgeEnabled": false,
   "KmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
   "PositionFiltering": "AccuracyBased",
   "Tags": {
      "string" : "string"
   }
}
```

**Create a tracker with `KmsKeyEnableGeospatialQueries` enabled**

The following example has the parameter `KmsKeyEnableGeospatialQueries` set to true. This allows you use the Bounding Polygon Queries feature, while encrypting your data using a customer AWS KMS managed key.

For information on using the Bounding Polygon Queries feature, see [List your device positions](#list-device-positions)

**Note**
When you use the Bounding Polygon Queries feature a representation of your device positions is not be encrypted using the your AWS KMS managed key. However, the exact device position is still encrypted using your managed key.

```
POST /tracking/v0/trackers
Content-type: application/json

{

   "TrackerName": "{{ExampleTracker}}",
   "Description": "string",
   "KmsKeyEnableGeospatialQueries": true,
   "EventBridgeEnabled": false,
   "KmsKeyId": "{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
   "PositionFiltering": "{{AccuracyBased}}",
   "Tags": {
      "string" : "string"
   }
}
```

------
#### [ AWS CLI ]

**To create a tracker using AWS CLI commands**

Use the `[create-tracker](https://docs.aws.amazon.com/cli/latest/reference/location/create-tracker.html)` command.

The following example uses the AWS CLI to create a tracker called {{ExampleTracker}}. The tracker resource is associated with a [customer managed AWS KMS key to encrypt customer data](encryption-at-rest.md), and does not [enable position updates in EventBridge](location-events.md#enable-update-events).

```
aws location \
  create-tracker \
  --tracker-name "{{{{ExampleTracker}}}}" \
  --position-filtering "{{AccuracyBased}}" \
  --event-bridge-enabled false \
  --kms-key-enable-geospatial-queries false \
  --kms-key-id "{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
```

**Create a tracker with `KmsKeyEnableGeospatialQueries` enabled**

The following example has the parameter `KmsKeyEnableGeospatialQueries` set to true. This allows you use the Bounding Polygon Queries feature, while encrypting your data using a customer AWS KMS managed key.

For information on using the Bounding Polygon Queries feature, see [List your device positions](#list-device-positions)

**Note**
When you use the Bounding Polygon Queries feature a representation of your device positions is not be encrypted using the your AWS KMS managed key. However, the exact device position is still encrypted using your managed key.

```
aws location \
  create-tracker \
  --tracker-name "{{{{ExampleTracker}}}}" \
  --position-filtering "{{AccuracyBased}}" \
  --event-bridge-enabled false \
  --kms-key-enable-geospatial-queries true \
  --kms-key-id "{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
```

------

**Note**
Billing depends on your usage. You may incur fees for the use of other AWS services. For more information, see [Amazon Location Service pricing](https://aws.amazon.com/location/pricing/).

You can edit the **Description**, **Position filtering**, and **EventBridge configuration** after the tracker is created by choosing **Edit tracker**.

## Authenticating your requests
<a name="tracking-identity-pool"></a>

Once you create a tracker resource and you're ready to begin evaluating device positions against geofences, choose how you would authenticate your requests:
+ To explore ways you can access the services, see [Accessing Amazon Location Service](how-to-access.md).
+ If you want to publish device positions with unauthenticated requests,you may want to use Amazon Cognito.

  **Example**

  The following example shows using an Amazon Cognito identity pool for authorization, using [AWS JavaScript SDK v3](https://aws.amazon.com/sdk-for-javascript/), and the Amazon Location [JavaScript Authentication helper](loc-sdk-auth.md).

  ```
  import { LocationClient, BatchUpdateDevicePositionCommand } from "@aws-sdk/client-location";
  import { withIdentityPoolId } from "@aws/amazon-location-utilities-auth-helper";

  // Unauthenticated identity pool you created
  const identityPoolId = "{{us-east-1:1234abcd-5678-9012-abcd-sample-id}}";

  // Create an authentication helper instance using credentials from Cognito
  const authHelper = await withIdentityPoolId(identityPoolId);

  const client = new LocationClient({
    region: "{{us-east-1}}", // The region containing both the identity pool and tracker resource
    ...authHelper.getLocationClientConfig(), // Provides configuration required to make requests to Amazon Location
  });

  const input = {
    TrackerName: "{{ExampleTracker}}",
    Updates: [
      {
        DeviceId: "{{ExampleDevice-1}}",
        Position: [-123.4567, 45.6789],
        SampleTime: new Date("2020-10-02T19:09:07.327Z"),
      },
      {
        DeviceId: "{{ExampleDevice-2}}",
        Position: [-123.123, 45.123],
        SampleTime: new Date("2020-10-02T19:10:32Z"),
      },
    ],
  };

  const command = new BatchUpdateDevicePositionCommand(input);

  // Send device position updates
  const response = await client.send(command);
  ```

## Update your tracker with a device position
<a name="send-location-updates"></a>

To track your devices, you can post device position updates to your tracker. You can later retrieve these device positions or the device position history from your tracker resource.

Each position update must include the device ID, a timestamp , and a position. You may optionally include other metadata, including accuracy and up to 3 key-value pairs for your own use.

If your tracker is linked to one or more geofence collections, updates will be evaluated against those geofences (following the filtering rules that you specified for the tracker). If a device breaches a geofenced area (by moving from inside the area to outside, or vice versa), you will receive events in EventBridge. These `ENTER` or `EXIT` events include the position update details, including the device ID, the timestamp, and any associated metadata.

**Note**
For more information about position filtering, see [Create a tracker](#start-create-tracker).
For more information about geofence events, see [Reacting to Amazon Location Service events with Amazon EventBridge](location-events.md).

Use either of these methods to send device updates:
+ [Send MQTT updates](https://docs.aws.amazon.com/location/previous/developerguide/tracking-using-mqtt.html) to an AWS IoT Core resource and link it to your tracker resource.
+ Send location updates using the Amazon Location Trackers API, by using the AWS CLI, or the Amazon Location APIs. You can use the [AWS SDKs](location-actions.md) to call the APIs from your iOS or Android application.

------
#### [ API ]

**To send a position update using the Amazon Location APIs**

Use the `[BatchUpdateDevicePosition](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_BatchUpdateDevicePosition.html)` operation from the Amazon Location Trackers APIs.

The following example uses an API request to post a device position update for {{ExampleDevice}} to a tracker {{ExampleTracker}}.

```
POST /tracking/v0/trackers/{{ExampleTracker}}/positions
Content-type: application/json
{
 "Updates": [
    {
    "DeviceId": "1",
    "Position": [
   -123.12245146162303, 49.27521118043802
    ],
    "SampleTime": "2022-10-24T19:09:07.327Z",
     "PositionProperties": {
            "name" : "device1"
         },
         "Accuracy": {
            "Horizontal": 10
         }
    },

    {
    "DeviceId": "2",
    "Position": [
   -123.1230104928471, 49.27752402723152
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "3",
    "Position": [
    -123.12325592118916, 49.27340530543111
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "4",
    "Position": [
    -123.11958813096311, 49.27774641063121
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "5",
    "Position": [
    -123.1277418058896, 49.2765989015285
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "6",
    "Position": [
   -123.11964267059481, 49.274188155916534
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    }
    ]
}
```

------
#### [ AWS CLI ]

**To send a position update using AWS CLI commands**

Use the `[batch-update-device-position](https://docs.aws.amazon.com/cli/latest/reference/location/batch-update-device-position.html)` command.

The following example uses an AWS CLI to post a device position update for {{ExampleDevice-1}} and {{ExampleDevice-2}} to a tracker {{ExampleTracker}}.

```
aws location batch-update-device-position \
--tracker-name ExampleTracker \
--updates '[{"DeviceId":"ExampleDevice-1","Position":[-123.123,47.123],"SampleTime":"2021-11-30T21:47:25.149Z"},{"DeviceId":"ExampleDevice-2","Position":[-123.123,47.123],"SampleTime":"2021-11-30T21:47:25.149Z","Accuracy":{"Horizontal":10.30},"PositionProperties":{"field1":"value1","field2":"value2"}}]'
```

------

## Get a device's location history from a tracker
<a name="get-location-history"></a>

 Your Amazon Location tracker resource maintains the location history of all your tracked devices for a period of 30 days. You can retrieve device location history, including all associated metadata, from your tracker resource. The following examples use the AWS CLI, or the Amazon Location APIs.

------
#### [ API ]

**To get the device location history from a tracker using the Amazon Location APIs**

Use the `[GetDevicePositionHistory](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_GetDevicePositionHistory.html)` operation from the Amazon Location Trackers APIs.

The following example uses an API URI request to get the device location history of {{ExampleDevice}} from a tracker called {{ExampleTracker}} starting from `19:05:07` (inclusive) and ends at `19:20:07` (exclusive) on `2020–10–02`.

```
POST /tracking/v0/trackers/{{ExampleTracker}}/devices/{{ExampleDevice}}/list-positions
Content-type: application/json
{
  "StartTimeInclusive": "2020-10-02T19:05:07.327Z",
  "EndTimeExclusive": "2020-10-02T19:20:07.327Z"
}
```

------
#### [ AWS CLI ]

**To get the device location history from a tracker using AWS CLI commands**

Use the `[get-device-position-history](https://docs.aws.amazon.com/cli/latest/reference/location/get-device-position-history.html)` command.

The following example uses an AWS CLI to get the device location history of {{ExampleDevice}} from a tracker called {{ExampleTracker}} starting from `19:05:07` (inclusive) and ends at `19:20:07` (exclusive) on `2020–10–02`.

```
aws location \
    get-device-position-history \
        --device-id "{{ExampleDevice}}" \
        --start-time-inclusive "2020-10-02T19:05:07.327Z" \
        --end-time-exclusive "2020-10-02T19:20:07.327Z" \
        --tracker-name "{{{{ExampleTracker}}}}"
```

------

## List your device positions
<a name="list-device-positions"></a>

You can view a list device positions for a tracker using the AWS CLI, or the Amazon Location APIs, with the ListDevicePositions API. When you call the ListDevicePositions API, a list of the latest positions for all devices associated with a given tracker is returned. By default this API returns 100 of the latest device positions per page of results for a given tracker. To only return devices within a specific region use the `FilterGeometry` parameter to create a Bounding Polygon Query. This way when you call ListDevicePositions, only devices inside the polygon will be returned.

**Note**
If you wish to encrypt your data using your own AWS KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this feature, a representation of your device positions will not be encrypted using the your AWS KMS managed key. The exact device position, however; is still encrypted using your managed key.
You can choose to opt-in to the Bounding Polygon Queries feature. This is done by setting the `KmsKeyEnableGeospatialQueries` parameter to true when creating or updating a Tracker.

------
#### [ API ]

Use the `[ListDevicePositions](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_ListDevicePositions.html)` operation from the Amazon Location Trackers APIs.

The following example is an API request to get a list of device positions in polygonal area, using the optional parameter `[FilterGeometry](https://docs.aws.amazon.com/)`. The example returns 3 device locations present in the area defined by the `Polygon` array.

```
POST /tracking/v0/trackers/{{TrackerName}}/list-positions HTTP/1.1
Content-type: application/json

{
   "FilterGeometry": {
        "Polygon": [
          [
            [
              -123.12003339442259,
              49.27425121147397
            ],
            [
              -123.1176984148229,
              49.277063620879744
            ],
            [
              -123.12389509145294,
              49.277954183760926
            ],
            [
              -123.12755921328647,
              49.27554025235713
            ],
            [
              -123.12330236586217,
              49.27211836076236
            ],
            [
              -123.12003339442259,
              49.27425121147397
            ]
          ]
        ]
    },
   "MaxResults": 3,
   "NextToken": "1234-5678-9012"
}
```

The following is an example response for `[ListDevicePositions](https://docs.aws.amazon.com/location-trackers/latest/APIReference/API_ListDevicePositions.html)`:

```
{
    "Entries": [
        {
            "DeviceId": "1",
            "SampleTime": "2022-10-24T19:09:07.327Z",
            "Position": [
                -123.12245146162303,
                49.27521118043802
            ],
            "Accuracy": {
                "Horizontal": 10
            },
            "PositionProperties": {
                "name": "device1"
            }
        },
        {
            "DeviceId": "3",
            "SampleTime": "2022-10-02T19:09:07.327Z",
            "Position": [
                -123.12325592118916,
                49.27340530543111
            ]
        },
        {
            "DeviceId": "2",
            "SampleTime": "2022-10-02T19:09:07.327Z",
            "Position": [
                -123.1230104928471,
                49.27752402723152
            ]
        }
    ],
   "NextToken": "1234-5678-9012"
}
```

------
#### [ CLI ]

Use the `[list-trackers](https://docs.aws.amazon.com/cli/latest/reference/location/list-trackers.html)` command.

The following example is an AWS CLI to get a list of devices in a polygonal area.

```
aws location list-device-positions TODO: add arguments add props for filter geo
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
