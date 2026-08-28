---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/location-regions.html
---

# Amazon Location regions and endpoints
<a name="location-regions"></a>

**Note**
We released a new version of the Places, Maps, and Routes APIs, see the updated [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html) for revised information and new topics, such as [Geofences](https://docs.aws.amazon.com/location/latest/developerguide/geofences.html) and [Trackers](https://docs.aws.amazon.com/location/latest/developerguide/trackers.html).

Amazon Location Service is available across multiple AWS regions globally. This page lists the regions where the service is currently deployed and operational. It provides information to help you determine the most suitable region for your applications and workloads. The guide covers any potential variations or limitations in feature availability across regions. This information is crucial for making informed decisions regarding deployment locations, ensuring compliance with data residency requirements, and optimizing performance based on the proximity to end-users or operational centers.

## Regions
<a name="available-regions"></a>

Amazon Location is available in the following AWS Regions:

| Region Name | Region | Endpoint | Protocol |
| --- | --- | --- | --- |
| US East (Ohio) | us-east-2 |  geo.us-east-2.amazonaws.com  | HTTPS |
| US East (N. Virginia) | us-east-1 |  geo.us-east-1.amazonaws.com  | HTTPS |
| US West (Oregon) | us-west-2 |  geo.us-west-2.amazonaws.com  | HTTPS |
| Asia Pacific (Malaysia) | ap-southeast-5 |  geo.ap-southeast-5.amazonaws.com  | HTTPS |
| Asia Pacific (Mumbai) | ap-south-1 |  geo.ap-south-1.amazonaws.com  | HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 |  geo.ap-southeast-1.amazonaws.com  | HTTPS |
| Asia Pacific (Sydney) | ap-southeast-2 |  geo.ap-southeast-2.amazonaws.com  | HTTPS |
| Asia Pacific (Tokyo) | ap-northeast-1 |  geo.ap-northeast-1.amazonaws.com  | HTTPS |
| Canada (Central) | ca-central-1 |  geo.ca-central-1.amazonaws.com  | HTTPS |
| Europe (Frankfurt) | eu-central-1 |  geo.eu-central-1.amazonaws.com  | HTTPS |
| Europe (Ireland) | eu-west-1 |  geo.eu-west-1.amazonaws.com  | HTTPS |
| Europe (London) | eu-west-2 |  geo.eu-west-2.amazonaws.com  | HTTPS |
| Europe (Spain) | eu-south-2 |  geo.eu-south-2.amazonaws.com  | HTTPS |
| Europe (Stockholm) | eu-north-1 |  geo.eu-north-1.amazonaws.com  | HTTPS |
| South America (São Paulo) | sa-east-1 |  geo.sa-east-1.amazonaws.com  | HTTPS |
|  AWS GovCloud (US-West) | us-gov-west-1 |  geo.us-gov-west-1.amazonaws.com <br /> geo-fips.us-gov-west-1.amazonaws.com  | HTTPS<br />HTTPS |

**Note**
For more information about how to use the endpoints in this table, see the following section.

## Endpoints
<a name="service-code"></a>

The general syntax for an Amazon Location regional endpoint is as follows:

```
protocol://{{service-code}}.geo.{{region-code}}.amazonaws.com
```

Within this syntax, Amazon Location uses the following service codes:

| Service | Service code |
| --- | --- |
| Amazon Location Maps | maps |
| Amazon Location Places | places |
| Amazon Location Geofences | geofencing |
| Amazon Location Trackers | tracking |
| Amazon Location Routes | routes |

For example, the regional endpoint for Amazon Location Maps for US East (N. Virginia) would be: https://{{maps}}.geo.{{us-east-1}}.amazonaws.com.

## API operation Endpoints
<a name="service-code-control-plane"></a>

The syntax for an Amazon Location Service control plane endpoint is as follows:

```
protocol://cp.{{service-code}}.geo.{{region-code}}.amazonaws.com
```

The control plane actions for Amazon Location Service are:

| Service | Endpoint | API operation |
| --- | --- | --- |
| Amazon Location Maps | https://cp.maps.geo.{{region}}.amazonaws.com | [CreateMap](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateMap.html)<br />[DeleteMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteMap.html)<br />[DescribeMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeMap.html)<br />[ListMaps](https://docs.aws.amazon.com/location/previous/APIReference/API_ListMaps.html)<br />[UpdateMap](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateMap.html) |
| Amazon Location Places | https://cp.places.geo.{{region}}.amazonaws.com | [CreatePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_CreatePlaceIndex.html)<br />[DeletePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_DeletePlaceIndex.html)<br />[DescribePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribePlaceIndex.html)<br />[ListPlaceIndexes](https://docs.aws.amazon.com/location/previous/APIReference/API_ListPlaceIndexes.html)<br />[UpdatePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdatePlaceIndex.html) |
| Amazon Location Geofences | https://cp.geofencing.geo.{{region}}.amazonaws.com | [CreateGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateGeofenceCollection.html)<br />[DeleteGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteGeofenceCollection.html)<br />[DescribeGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeGeofenceCollection.html)<br />[ListGeofenceCollections](https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofenceCollections.html)<br />[UpdateGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateGeofenceCollection.html) |
| Amazon Location Trackers | https://cp.tracking.geo.{{region}}.amazonaws.com | [CreateTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateTracker.html)<br />[DeleteTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteTracker.html)<br />[DescribeTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeTracker.html)<br />[UpdateTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateTracker.html)<br />[ListTrackers](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateGeofenceCollection.html)<br />[AssociateTrackerConsumer](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateGeofenceCollection.html)<br />[DisassociateTrackerConsumer](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteGeofenceCollection.html)<br />[ListTrackerConsumers](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeGeofenceCollection.html) |
| Amazon Location Routes | https://cp.routes.geo.{{region}}.amazonaws.com | [CreateRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_CreatePlaceIndex.html)<br />[DeleteRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DeletePlaceIndex.html)<br />[DescribeRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribePlaceIndex.html)<br />[ListRouteCalculators](https://docs.aws.amazon.com/location/previous/APIReference/API_ListPlaceIndexes.html)<br />[UpdateRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdatePlaceIndex.html) |
| Amazon Location Metadata | https://cp.metadata.geo.{{region}}.amazonaws.com | [CreateKey](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateKey.html)<br />[DeleteKey](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteKey.html)<br />[DescribeKey](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeKey.html)<br />[ListKeys](https://docs.aws.amazon.com/location/previous/APIReference/API_ListKeys.html)<br />[UpdateKey](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateKey.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
