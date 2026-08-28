---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/data-provider-features.html
---

# Features by data provider
<a name="data-provider-features"></a>

This section describes the features available in Amazon Location Service, categorized by data provider.

The following table provides a high-level overview of the features.

| Data provider | Geographical coverage | Feature coverage | AWS Region |
| --- | --- | --- | --- |
| Esri | Global | Maps, Places, Routes | [All Regions](location-regions.md#available-regions) where Amazon Location is available. |
| Grab | [Southeast Asia](grab.md#grab-coverage-area) | Maps, Places, Routes | Asia Pacific (Singapore), ap-southeast-1, only. |
| HERE | Global | Maps, Places, Routes | [All Regions](location-regions.md#available-regions) where Amazon Location is available. |
| Open Data | Global | Maps | [All Regions](location-regions.md#available-regions) where Amazon Location is available. |

The following tabs show details within each feature area.

------
#### [ Map Features ]

The following table shows the map features by data provider. For more information about map concepts, see [Learn about Maps resources in Amazon Location Service](map-concepts.md).

| Data provider | Supported map types | Vector zoom levels | Raster zoom levels |
| --- | --- | --- | --- |
| Esri | Vector<br />Raster (imagery)<br />For more information, see [Esri map styles](esri.md#esri-map-styles). | 0-15 | 0-23 |
| Grab | Vector<br />([Southeast Asia](grab.md#grab-coverage-area) only)<br />For more information, see [Grab map styles](grab.md#grab-map-styles). | 0-14 | none |
| HERE | Vector<br />Raster (imagery)<br />Hybrid<br />For more information, see [HERE map styles](HERE.md#HERE-map-styles). | 1-17 | 0-19 |
| Open Data | Vector<br />For more information, see [Open Data map styles](open-data.md#open-data-map-styles). | 0-15 | none |

**Note**
Zoom levels represent the maximum and minimum settings, as defined in each provider's APIs. Different areas of the map may have different maximums; for example, ocean tiles may have fewer detailed zoom levels than areas in major cities.
MapLibre (and other map rendering engines) allow you to set minimum and maximum zoom levels, and will also honor the data provider zoom levels in an area, so you do not have to write code to handle these discrepancies.

------
#### [ Places and Search ]

The following table shows the place and search features by data provider. For more information about place concepts, see [Learn about Places search in Amazon Location Service](places-concepts.md).

| Data provider | Geocoding | Reverse Geocoding | Autocomplete | GetPlace |
| --- | --- | --- | --- | --- |
| Esri | All features, except:<br />*   PlaceId* | All features, except:<br />*   TimeZone*<br />*   PlaceId* | All features | All features |
| Grab | All features, except:<br />*   unit type *<br />   Categories not supported | All features | All features | All features, except:<br />*   unit type*<br />*   SubMunicipality* |
| HERE | All features, except:<br />*   unit number*<br />*   unit type*<br />*   relevance*<br />   Additional [limitations on filtering](category-filtering.md#filter-limitations) | All features | All features | All features, except:<br />*   unit number*<br />*   unit type*<br />*   SubMunicipality* |
| Open Data | Not supported | Not supported | Not supported | Only supports:<br />*   SubMunicipality* |

------
#### [ Route features ]

The following table shows the route features by data provider. For more information about route concepts, see [Routes (V1) concepts](route-concepts.md). For more detailed descriptions of route matrix limitations, see [Restrictions on departure and destination positions](calculate-route-matrix.md#matrix-routing-position-limits).

| Data provider | Travel modes | Calculate route | Route matrix |
| --- | --- | --- | --- |
| Esri | Car, Truck, Walking | Departure and destination must be within 400 km of each other. The total travel time can't be more than 400 minutes.<br />ArrivalTime is not supported. | Up to 10 departure and destination positions. <br />Not supported in Korea.<br />All departure and destination pairs must be within 400 km of each other. |
| Grab | Car, Motorcycle.<br />Walking and Bicycle in [selected cities](grab.md#grab-travel-mode-routes). | No distance limits. | Up to 350 departure and destination positions. |
| HERE | Car, Truck, Walking | No distance limit. Routes that go more than 10 km outside a circle around the departure and destination positions will not be calculated. | Up to 350 departure and destination positions.<br />All departure and destination positions must fall with a 180 km circle.<br />Longer routes are supported, with [additional restrictions](calculate-route-matrix.md#matrix-routing-longer-routes). |
| Open Data | Not supported | Not supported | Not supported |

------

Each data provider gathers and produces data in different ways. You can learn more about their coverage areas in the following topics:
+ [Coverage: Esri](esri.md#esri-places-coverage)
+ [Coverage: Grab](grab.md#grab-places-coverage)
+ [Coverage: HERE](HERE.md#HERE-places-coverage)
+ [Coverage: Open Data](open-data.md#open-data-places-coverage)

If you encounter a problem with the data and want to report an error to the data provider, see the following topics:
+ [Error reporting to Esri](esri.md#esri-support)
+ [Error reporting for GrabMaps data](grab.md#grab-support)
+ [Error reporting to HERE](HERE.md#HERE-support)
+ [Error reporting and contributing to Open Data](open-data.md#open-data-support)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
