---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/overview.html
---

# Amazon Location overview
<a name="overview"></a>

Amazon Location Service provides access to location-based functionality and data providers through AWS resources. Amazon Location offers five types of AWS resources, depending on the type of functionality you need. Use the different resources together to create a full location-based application. You can create one or more of these resources by using the Amazon Location console, the Amazon Location APIs, or the SDKs.

![Five Amazon Location Service resource types: Maps , Place indexes, Route calculators, Geofence collections, and Trackers.](http://docs.aws.amazon.com/location/previous/developerguide/images/how-it-works.PNG)

Each resource defines the underlying [data provider](what-is-data-provider.md) to be used (where applicable), and gives access to functionality related to its type.

For example:
+ [Amazon Location Service Maps](map-concepts.md) lets you choose a map from a map provider to use on your mobile or web application.
+ [Amazon Location Service Places](places-concepts.md) lets you choose a data provider for searching for points of interest, completing partial text, geocoding, and reverse geocoding.
+ [Amazon Location Service Routes](route-concepts.md) lets you choose a data provider and find routes and estimate travel time based on up-to-date roadway and live traffic information.
+ [Amazon Location Service Geofences](geofence-tracker-concepts.md) let you define areas of interest as a virtual boundary. You can then evaluate locations against them and get notifications of entry and exit events.
+ [Amazon Location Service Trackers](geofence-tracker-concepts.md) receive location updates from your devices. You can link trackers to geofence collections so that all position updates are automatically evaluated against your geofences.

You can use IAM policies to manage and authorize access to your Amazon Location resources. You can also organize your resources into resource groups to manage and automate tasks as your resource numbers grow. For more information about managing AWS resources, see [What are AWS Resource Groups?](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) In the *AWS Resource Groups User Guide*.

Location is defined by using latitude and longitude coordinates that follow the [World Geodetic System (WGS 84)](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84), commonly used as the standard coordinate reference system for Global Positioning System (GPS) services.

The following sections describe how the components of Amazon Location work.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
