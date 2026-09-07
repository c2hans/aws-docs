---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tracking-overview.html
---

# Learn about trackers in Amazon Location Service
<a name="tracking-overview"></a>

A tracker stores position updates for a collection of devices. The tracker can be used to query the devices' current location or location history. It stores the updates, but reduces storage space and visual noise by filtering the locations before storing them.

Each position update stored in your tracker resources can include a measure of position accuracy and up to 3 fields of metadata about the position or device that you want to store. The metadata is stored as key-value pairs, and can store information such as speed, direction, tire pressure, or engine temperature.

**Note**
Tracker storage is encrypted with AWS owned keys automatically. You can add another layer of encryption using KMS keys that you manage, to ensure that only you can access your data. For more information, see [Data encryption at rest for Amazon Location Service](encryption-at-rest.md).

Tracker position filtering and storage are useful on their own, but trackers are especially useful when paired with geofences. You can link trackers to one or more of your geofence collection resources, and position updates are evaluated automatically against the geofences in those collections. Proper use of filtering can greatly reduce the costs of your geofence evaluations, as well.

The following diagram shows you how to create and use tracker resources:

![Workflow showing selection of tracker elements, SDK integration, embedding in application, and deployment.](https://docs.aws.amazon.com/location/previous/developerguide/images/illustration-trackers.PNG)

1. First, you create a tracker resource in your AWS account.

1. Next, decide how you send location updates to your tracker resources. Use [AWS SDKs](location-actions.md) to integrate tracking capabilities into your mobile applications. Alternately, you can use MQTT by following step-by-step directions in [tracking using MQTT](tracking-using-mqtt.md).

1. You can now use your tracker resource to record location history and visualize it on a map.

1. You can also link your tracker resource to one or more geofence collections so that every position update sent to your tracker resource is automatically evaluated against all the geofence in all the linked geofence collections. You can link resource on the tracker resource details page of the Amazon Location console or by using the Amazon Location Trackers API.

1. You can then integrate monitoring using services such as Amazon CloudWatch and AWS CloudTrail. For more information see, [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).

## Using trackers with geofences
<a name="trackers-with-geofences-concepts"></a>

Trackers provide additional functionality when paired with geofences. You associate a tracker with a geofence collection, either through the Amazon Location console or the API, to automatically evaluate tracker locations. Each time the tracker receives an updated location, that location will be evaluated against each geofence in the collection, and the appropriate `ENTER` and `EXIT` events are generated in Amazon EventBridge. You can also apply filtering to the tracker, and, depending on the filtering, you can reduce the costs for geofence evaluations by only evaluating meaningful location updates.

If you associate the tracker with a geofence collection after it has already received some position updates, the first position update after association is treated as an initial update for the geofence evaluations. If it is within a geofence, you will receive an `ENTER` event. If it is not within any geofences you will not receive an `EXIT` event, regardless of the previous state.

## Position filtering
<a name="tracker-filtering-concepts"></a>

Trackers can automatically filter the positions that are sent to them. There are several reasons why you might want to filter out some of your device location updates. If you have a system that only sends reports every minute or so, you might want to filter devices by time, storing and evaluating positions only every 30 seconds. Even if you are monitoring more frequently, you might want to filter position updates to clean up the noisiness of GPS hardware. GPS position locations are inherently noisy. Their accuracy is not 100% perfect, so even a device that is stationary appears to be moving around slightly. At low speeds, this *jitter* causes visual clutter and can cause false entry and exit events if the device is near the edge of a geofence.

The position filtering works as position updates are received by a tracker, reducing visual noise in your device paths (jitter), reducing the number of false geofence entry and exit events, and helping manage costs by reducing the number of position updates stored and geofence evaluations triggered.

Trackers offer three position filtering options to help manage costs and reduce jitter in your location updates.
+ **Accuracy-based** – *Use with any device that provides an accuracy measurement. Most GPS and mobile devices provide this information.* The accuracy of each position measurement is affected by many environmental factors, including GPS satellite reception, landscape, and the proximity of wifi and bluetooth devices. Most devices, including most mobile devices, can provide an estimate of the accuracy of the measurement along with the measurement. With `AccuracyBased` filtering, Amazon Location ignores location updates if the device moved less than the measured accuracy. For example, if two consecutive updates from a device have an accuracy range of 5 m and 10 m, Amazon Location ignores the second update if the device has moved less than 15 m. Amazon Location neither evaluates ignored updates against geofences, nor stores them.

  When accuracy is not provided, it is treated as zero, and the measurement is considered perfectly accurate, and no filtering will be applied to the updates.
**Note**
You can use accuracy-based filtering to remove all filtering. If you select accuracy-based filtering, but override all accuracy data to zero, or omit the accuracy entirely, then Amazon Location will not filter out any updates.

  In most scenarios, accuracy-based filtering is a good choice for filtering position updates, providing a balance of tracking location while filtering out unneeded updates, thereby reducing costs.
+ **Distance-based** – *Use when your devices do not provide an accuracy measurement, but you still want to take advantage of filtering to reduce jitter and manage costs.* `DistanceBased` filtering ignores location updates in which devices have moved less than 30 m (98.4 ft). When you use `DistanceBased` position filtering, Amazon Location neither evaluates these ignored updates against geofences nor stores the updates.

  The accuracy of most mobile devices, including the average accuracy of iOS and Android devices, is within 15 m. In most applications, `DistanceBased` filtering can reduce the effect of location inaccuracies when displaying device trajectory on a map, and the bouncing effect of multiple consecutive entry and exit events when devices are near the border of a geofence. It can also help reduce the cost of your application, by making fewer calls to evaluate against linked geofences or retrieve device positions.

  Distance-based filtering is useful if you want to filter, but your device doesn't provide accuracy measurements, or you want to filter out a larger number of updates than with accuracy-based.
+ **Time-based** – (default) *Use when your devices send position updates very frequently (more than once every 30 seconds), and you want to achieve near real-time geofence evaluations without storing every update. *In `TimeBased` filtering, every location update is evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID.

  Time-based filtering is particularly useful when you want to store fewer positions, but want every position update to be evaluated against the associated geofence collections.

**Note**
Be mindful of the costs of your tracking application when deciding your filtering method and the frequency of position updates. You are billed for every location update and once for evaluating the position update against each linked geofence collection. For example, when using time-based filtering, if your tracker is linked to two geofence collections, every position update will count as one location update request and two geofence collection evaluations. If you are reporting position updates every 5 seconds for your devices and using time-based filtering, you will be billed for 720 location updates and 1,440 geofence evaluations per hour for each device.

## Tracker terminology
<a name="tracking-components"></a>

**Tracker resource**
An AWS resource that receives location updates from devices. The tracker resource provides support for location queries, such as current and historic device location. Linking a tracker resource to a geofence collection evaluates location updates against all geofences in the linked geofence collection automatically.

**Position data tracked**
A tracker resource stores information about your devices over time. The information includes a series of position updates, where each update includes location, time, and optional metadata. The metadata can include a position's accuracy, and up to three key-value pairs to help you track key information about each position, such as speed, direction, tire pressure, remaining fuel, or engine temperature of the vehicle you are tracking. Trackers maintain device location history for 30 days.

**Position filtering**
Position filtering can help you control costs and improve the quality of your tracking application by filtering out position updates that don't provide valuable information before the updates are stored or evaluated against geofences.
You can choose `AccuracyBased`, `DistanceBased`, or `TimeBased` filtering. By default, position filtering is set to `TimeBased`.
You can configure position filtering when you create or update tracker resources.

**RFC 3339 timestamp format **
Amazon Location Service Trackers uses the [RFC 3339](https://tools.ietf.org/html/rfc3339) format, which follows the [International Organization for Standardization (ISO) 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format for dates and time.
The format is “YYYY-MM-DDThh:mm:ss.sssZ\+00:00”:
+ `YYYY-MM-DD` — Represents the date format.
+ `T` — Indicates that the time values will follow.
+ `hh:mm:ss.sss` — Represents the time in 24-hour format.
+ `Z` — Indicates that the time zone used is UTC, which can be followed with deviations from the UTC time zone.
+ `+00:00` — Optionally indicate deviations from the UTC time zone. For example, \+01:00 indicates UTC \+ 1 hour.
**Example**
For July 2, 2020, at 12:15:20 in the afternoon, with an adjustment of an additional 1 hour to the UTC time zone.

```
2020-07-02T12:15:20.000Z+01:00
```
