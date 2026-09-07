---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/geofence-overview.html
---

# Learn about geofences in Amazon Location Service
<a name="geofence-overview"></a>

Geofence collection resources allow you to store and manage geofences—virtual boundaries on a map. You can evaluate locations against a geofence collection resource and get notifications when the location update crosses the boundary of any of the geofences in the geofence collection.

The following shows you how to create and use geofence collection resources:

![Workflow showing clicking a polygon, adding and positioning it, then messaging on mobile device.](https://docs.aws.amazon.com/location/previous/developerguide/images/illustration-geofence.PNG)

1. Create a geofence collection resource in your AWS account.

1. Add geofences to that collection. You can do so by either using the geofence upload tool on the Amazon Location console, or by using the Amazon Location Geofences API. For more information about available options, see [Accessing Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/how-to-access.html).

   Geofences can either be defined by a polygon or by a circle. Use a polygon to find when a device enters a specific area. Use a circle to find when a device comes within a certain distance (radius) of a point.

1. You can start evaluating locations against all your geofences. When a location update crosses the boundaries of one or more geofences, your geofence collection resource emits one of the following geofence event types on Amazon EventBridge:
   + ****ENTER**** – One event is generated for each geofence where the location update crosses its boundary by entering it.
   + ****EXIT**** – One event is generated for each geofence where the location update crosses its boundary by exiting it.

   For more information, see [Reacting to Amazon Location Service events with Amazon EventBridge](location-events.md). You can also integrate monitoring using services such as Amazon CloudWatch and AWS CloudTrail. For more information see, [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).

For example, if you are tracking a fleet of trucks, and you want to get notified when a truck comes within a certain area of any of your warehouses. You can create a geofence for the area around each warehouse. Then, when the trucks send you updated locations, you can use Amazon Location Service to evaluate those positions and see if a truck has entered (or exited) one of the geofence areas.

**Note**
Your are billed by the number of geofence collections you evaluate against. Your bill is not affected by the number of geofences in each collection. Since each geofence collection may contain up to 50,000 geofences, you may want to combine your geofences into fewer collections, where possible, to reduce your cost of geofence evaluations. The events generated will include the ID of the individual geofence in the collection, as well as the ID of the collection.

## Geofence events
<a name="geofence-events-concepts"></a>

Locations for positions you are monitoring are referenced by an ID called a `DeviceId` (and the positions are referred to as device positions). You can send a list of device positions to evaluate directly to the geofence collection resource, or you can use a tracker. See the next section for more information on trackers.

You receive events (via Amazon EventBridge) only when a device enters or exits a geofence, not for every position change. This means that you will typically receive events and have to respond to them much less frequently than every device position update.

**Note**
For the first location evaluation for a specific `DeviceID`, it is assumed that the device was previously not in any geofences. So the first update will generate an `ENTER` event, if inside a geofence in the collection, and no event if not.

In order to calculate whether a device has entered or exited a geofence, Amazon Location Service must keep previous position state for the device. This position state is stored for 30 days. After 30 days without an update for a device, a new location update will be treated as the first position update.

## Geofence terminology
<a name="geofence-components"></a>

**Geofence Collection**
Contains zero or more geofences. It is capable of geofence monitoring by emitting Entry and Exit events, when requested, to evaluate a device position against its geofences.

**Geofence**
A polygon or circle geometry that defines a virtual boundary on a map.

**Polygon geometry**
An Amazon Location geofence is a virtual boundary for a geographical area and is represented as a polygon geometry or as a circle.
A circle is a point with a distance around it. Use a circle when you want to be notified if a device is within a certain distance of a location.
A polygon is an array composed of 1 or more linear rings. Use a polygon when you want to define a specific boundary for device notifications. A linear ring is an array of four or more vertices, where the first and last vertex are the same to form a closed boundary. Each vertex is a 2-dimensional point of the form {{[longitude, latitude]}}, where the units of longitude and latitude are degrees. The vertices must be listed in counter-clockwise order around the polygon.
Amazon Location Service doesn't support polygons with more than one ring. This includes holes, islands or multipolygons. Amazon Location also doesn't support polygons that are wound clockwise, or that cross the antimeridian.
The following is an example of a single linear external ring:

```
[
  [
    [-5.716667, -15.933333],
    [-14.416667, -7.933333],
    [-12.316667, -37.066667],
    [-5.716667, -15.933333]
  ]
]
```
