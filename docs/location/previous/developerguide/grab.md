---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/grab.html
---

# GrabMaps
<a name="grab"></a>

Grab is the largest delivery organization in Southeast Asia, with millions of driver partners and customers. Their subsidiary, [GrabMaps](https://www.grab.com/sg/business/maps/), creates up-to-date mapping data in those countries/regions for their own use, and others. Amazon Location Service uses GrabMaps' location services to help AWS customers use maps, geocode, and calculate routes effectively. GrabMaps' location services are built to provide high-quality, authoritative, and ready-to-use location data, specifically for southeast Asian countries.

For information about additional capability, see [GrabMaps](https://aws.amazon.com/location/data-providers/grabmaps/) on *Amazon Location Service data providers*.

**Important**
Grab provides maps only for southeast Asia, and is available only in the Asia Pacific (Singapore) Region (ap-southeast-1). For more information, see [Countries/regions and area covered](#grab-coverage-area).

**Topics**
+ [Grab map styles](#grab-map-styles)
+ [Coverage: Grab](#grab-places-coverage)
+ [Countries/regions and area covered](#grab-coverage-area)
+ [Terms of use and data attribution: Grab](#grab-terms)
+ [Error reporting for GrabMaps data](#grab-support)

## Grab map styles
<a name="grab-map-styles"></a>

Amazon Location Service supports the following Grab map styles when [creating a map resource](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html):

**Note**
Grab map styles that are not listed in this section are currently not supported.

------
#### [ Grab Standard Light Map ]

**Grab Standard Light Map**

![An image of Grab's standard light map style.](https://docs.aws.amazon.com/location/previous/developerguide/images/VectorGrabMonoStreet.png)

**Map style name**: `VectorGrabStandardLight`

Grab's standard basemap with detailed land use coloring, area names, roads, landmarks, and points of interest covering Southeast Asia.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Noto Sans Regular
+ Noto Sans Medium
+ Noto Sans Bold

------
#### [ Grab Standard Dark Map ]

**Grab Standard Dark Map**

![An image of Grab's standard dark map style.](https://docs.aws.amazon.com/location/previous/developerguide/images/VectorGrabDarkStreet.png)

**Map style name**: `VectorGrabStandardDark`

Grab's dark variation of their standard basemap, with detailed land use coloring, area names, roads, landmarks, and points of interest covering Southeast Asia.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Noto Sans Regular
+ Noto Sans Medium
+ Noto Sans Bold

------

## Coverage: Grab
<a name="grab-places-coverage"></a>

You can use Grab as a data provider to support queries for geocoding, reverse geocoding, and searches when you [create a place index resource](https://docs.aws.amazon.com/location/previous/developerguide/places-prerequisites.html#create-place-index-resource), or to support queries to calculate a route when you [create a route calculator resource](https://docs.aws.amazon.com/location/previous/developerguide/routes-prerequisites.html#create-route-calculator-resource).

## Countries/regions and area covered
<a name="grab-coverage-area"></a>

Grab provides maps only for southeast Asia, and is only available in the Asia Pacific (Singapore) Region (`ap-southeast-1`).

Grab provides detailed data for the following countries/regions:
+ Malaysia
+ Philippines
+ Thailand
+ Singapore
+ Vietnam
+ Indonesia
+ Myanmar
+ Cambodia

**Note**
Outside of these areas, the Amazon Location Service resources created with Grab as a data provider will not provide any results. This includes search results or routes.

The maps from Grab are within the following boundaries:
+ **South** – Latitude -21.943045533438166
+ **West** – Longitude 90.0
+ **North** – Latitude 31.952162238024968
+ **East** – Longitude 146.25

For zoom levels 1–4, Grab includes global coverage. For zoom levels 5 and below, map tiles are provided only within this bounded box.

**Note**
Outside of this bounded box, the Amazon Location Service map resources created with Grab as a data provider will not return map tiles. To avoid seeing 404 errors in your application, you can limit the map with a bounding box, as described in [Setting extents for a map using MapLibre](setting-map-extents.md).

### Grab routing travel modes
<a name="grab-travel-mode-routes"></a>

For routing, Grab provides **car** and **motorcycle** routing for all of the previously listed countries/regions.

Grab does not support **truck** routing.

For **bicycle** and **walking** routes, Grab supports the following cities:.
+ Singapore
+ Jakarta
+ Manila
+ Klang Valley
+ Bangkok
+ Ho Chi Minh City
+ Hanoi

## Terms of use and data attribution: Grab
<a name="grab-terms"></a>

When using Grab's data, you must comply with all applicable legal requirements, including license terms applicable to Grab and AWS.

For more information about the AWS requirements, see [AWS Service Terms](https://aws.amazon.com/service-terms/).

For information about GrabMaps' attribution guidelines, see Section 9.23 of Grab's [Data Attributions and Terms of Use](https://www.grab.com/sg/terms-policies/transport-delivery-logistics/).

## Error reporting for GrabMaps data
<a name="grab-support"></a>

If you encounter a problem with the data from GrabMaps, and want to report errors or discrepancies, [contact AWS technical support](https://support.console.aws.amazon.com/support/home#/case/create?issueType=customer-service).
