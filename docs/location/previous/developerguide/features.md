---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/features.html
---

# Key features in Amazon Location
<a name="features"></a>

**Note**
We released a new version of the Places, Maps, and Routes APIs, see the updated [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html) for revised information and new topics, such as [Geofences](https://docs.aws.amazon.com/location/latest/developerguide/geofences.html) and [Trackers](https://docs.aws.amazon.com/location/latest/developerguide/trackers.html).

Amazon Location offers a comprehensive set of features to enhance your location-based applications and services. This page provides an overview of the key capabilities available, including interactive maps, geocoding for address conversion, geofencing to monitor spatial boundaries, device tracking for asset management, and routing algorithms for optimized travel planning. Leveraging these features, you can build rich, location-aware experiences tailored to your specific use cases, whether it's delivering real-time location intelligence, enabling location-based services, or optimizing logistics and transportation operations.

Amazon Location provides the following features:

**Maps**
Amazon Location Service Maps lets you visualize location information and is the foundations of many location-based service capabilities. Amazon Location Service provides map tiles of different styles sourced from global location data providers Esri, Grab, and HERE, as well Open data maps.

**Places**
Amazon Location Service Places lets you integrate search functionality into your application, convert addresses into geographic coordinates in latitude and longitude (geocoding), and convert a coordinate into a street address (reverse geocoding). Amazon Location Service sources high-quality geospatial data from Esri, Grab, and HERE to support Places functions.

**Routing**
Amazon Location Service Routes lets you find routes and estimate travel time based on up-to-date roadway and live traffic information. Build features that allow your application to request the travel time, distance, and directions between any two locations. Calculate the time and distance for a matrix of routes to use in route planning.

**Geofencing**
Amazon Location Service Geofences lets you give your application the ability to detect and act when a device enters or exits a deﬁned geographical boundary known as a geofence. Automatically send an entry or exit event to Amazon EventBridge when a geofence breach is detected. This lets you initiate downstream actions such as sending a notiﬁcation to a target.

**Trackers**
Amazon Location Service Trackers lets you retrieve the current and historical location of devices that are running your tracking-enabled application. You can also link trackers with Amazon Location Service geofences to evaluate location updates from your devices against your geofences automatically. Trackers can help you reduce costs by filtering position updates that haven't moved before storing or evaluating them against geofences.
When you use trackers, sensitive location information on your tracked devices does not leave your AWS account. This helps protect sensitive information from third parties, protect user privacy, and reduce security risks.
