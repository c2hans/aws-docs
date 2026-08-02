---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/geofence-an-area.html
---

# Geofencing an area of interest using Amazon Location
<a name="geofence-an-area"></a>

A geofencing application evaluates a tracked device’s position relative to previously registered areas of interest. This enables actions to be taken based on position updates. For example, you can initiate an event that prompts a notification when a customer who ordered coffee on their mobile app is near a store.

**Note**
For an overview of geofencing and tracker concepts, see [Learn about geofences and trackers in Amazon Location Service](geofence-tracker-concepts.md).

This section of the guide provides step-by-step instructions for creating a geofencing application using Amazon Location Service.

Overview of steps

1. Add geofences around areas of interest and store them in a geofence collection resource.

1. Start tracking your target devices and store the device location history in a tracker resource.

1. Link your tracker resource to your geofence collection resource so that device location updates are automatically evaluated against all your geofences.

1. You can evaluate device positions directly against your geofence collection resources if you don’t want to use Amazon Location Trackers to keep your devices’ location history.

After you implement your geofencing solution, your geofence collection resource emits the following events:
+ `ENTER` — A tracked device enters a geofence within a geofence collection.
+ `EXIT` — A tracked device exits a geofence within a geofence collection.

You can use Amazon EventBridge to react to events by routing them elsewhere.

As an alternative to sending updates via the Amazon Location Service APIs from each device, you can use MQTT to send device updates.

The following topics describe these steps and alternatives in detail.

**Topics**
+ [Add geofences with Amazon Location](add-geofences.md)
+ [Start tracking with Amazon Location](start-tracking.md)
+ [Tutorial: Link a tracker to a geofence collection in Amazon Location](associate-consumer.md)
+ [Evaluate device positions against geofences in Amazon Location](evaluate-geofences.md)
+ [Tutorial: Verify device positions with Amazon Location](verify-device-positions.md)
+ [Reacting to Amazon Location Service events with Amazon EventBridge](location-events.md)
+ [Track with AWS IoT, MQTT, with Amazon Location Service](tracking-using-mqtt.md)
+ [Manage geofence collection resources with Amazon Location](managing-geofence-collections.md)
+ [Manage tracker resources with Amazon Location](managing-trackers.md)
+ [Sample Geofencing and Tracking mobile application](geofence-tracking-tutorials.md)
