---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/HERE.html
---

# HERE Technologies
<a name="HERE"></a>

Amazon Location Service uses HERE Technologies’ location services to help AWS customers use maps, geocode, and calculate routes effectively. HERE's location data offers a location-centric platform that's open, secure, and private. By selecting HERE location data, you are selecting accurate, fresh, and robust data that's deployed natively on the AWS Cloud.

For additional capability information, see [HERE](https://aws.amazon.com/location/data-providers/here-technologies/) on *Amazon Location Service data providers*.

**Topics**
+ [HERE map styles](#HERE-map-styles)
+ [Coverage: HERE](#HERE-places-coverage)
+ [Terms of use and data attribution: HERE](#HERE-terms)
+ [Error reporting to HERE](#HERE-support)

## HERE map styles
<a name="HERE-map-styles"></a>

Amazon Location Service supports the following HERE map styles when [creating a map resource](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html):

**Note**
HERE map styles that are not listed in this section are currently not supported.

------
#### [ HERE Explore ]

**HERE Explore**

![Map showing Boston area including Beacon Hill, Cambridge Street, and waterways with street labels.](https://docs.aws.amazon.com/location/previous/developerguide/images/StyleVectorHere.png)

**Map style name**: `VectorHereExplore`

**HERE Explore**

A detailed, neutral base map of the world. The street map includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries. Includes a fully designed map of Japan.

Fonts

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Fira GO Italic
+ Fira GO Regular
+ Fira GO Bold
+ Noto Sans CJK JP Light
+ Noto Sans CJK JP Regular
+ Noto Sans CJK JP Bold

------
#### [ HERE Imagery ]

**HERE Imagery**

![](https://docs.aws.amazon.com/location/previous/developerguide/images/here_satellite_raster.png)

**Map style name**: `RasterHereExploreSatellite`

**HERE Imagery**

HERE Imagery provides high resolution satellite imagery with global coverage.

------
#### [ HERE Hybrid ]

**HERE Hybrid**

![](https://docs.aws.amazon.com/location/previous/developerguide/images/here_satellite_hybrid.png)

**Map style name**: `HybridHereExploreSatellite`

**HERE Hybrid**

HERE Hybrid style displays the road network, street names, and city labels over satellite imagery. This style overlays two map tiles: the satellite image (raster tile) in the background and the road network and labels (vector tile) on top. This style will automatically retrieve both the raster and vector tiles required to render the map.

**Note**
Hybrid styles use both vector and raster tiles when rendering the map that you see. This means that more tiles are retrieved than when using either vector or raster tiles alone. Your charges will include all tiles retrieved.

Fonts

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Fira GO Italic
+ Fira GO Regular
+ Fira GO Bold
+ Noto Sans CJK JP Light
+ Noto Sans CJK JP Regular
+ Noto Sans CJK JP Bold

------
#### [ HERE Contrast (Berlin) ]

**HERE Contrast (Berlin)**

![Map of Boston showing streets, waterways, and neighborhoods with major roads highlighted in yellow.](https://docs.aws.amazon.com/location/previous/developerguide/images/HERE_contrast_2000x1200.png)

**Map style name**: `VectorHereContrast`

**HERE Contrast (Berlin)**

A detailed base map of the world that blends 3D and 2D rendering. The high contrast street map includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.

Fonts

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Fira GO Regular
+ Fira GO Bold

**Note**
This style was renamed from `VectorHereBerlin` (HERE Berlin maps). `VectorHereBerlin` is deprecated, but will continue to work in applications that use it.

------
#### [ HERE Explore Truck ]

**HERE Explore Truck**

![Map of Boston showing purple highway routes with red circular truck restriction icons at various locations.](https://docs.aws.amazon.com/location/previous/developerguide/images/StyleVectorHereTruck.png)

**Map style name**: `VectorHereExploreTruck`

**HERE Explore Truck**

A detailed, neutral base map of the world. The street map builds on top of the HERE Explore style, and highlights track restrictions and attributes (including width, height, and HAZMAT) with symbols and icons, to support use cases within transport and logistics.

Fonts

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Fira GO Italic
+ Fira GO Regular
+ Fira GO Bold
+ Noto Sans CJK JP Light
+ Noto Sans CJK JP Regular
+ Noto Sans CJK JP Bold

------

For additional information about map data quality in different regions of the world, see [HERE map coverage](https://developer.here.com/documentation/map-tile/dev_guide/topics/coverage-information.html).

## Coverage: HERE
<a name="HERE-places-coverage"></a>

You can use HERE as a data provider to support queries for geocoding, reverse geocoding, and searches when you [create a place index resource](https://docs.aws.amazon.com/location/previous/developerguide/places-prerequisites.html#create-place-index-resource), or to support queries to calculate a route when you [create a route calculator resource](https://docs.aws.amazon.com/location/previous/developerguide/routes-prerequisites.html#create-route-calculator-resource).

HERE provides different levels of data quality in different regions of the world. For additional information about coverage in your region of interest, see the following:
+ [HERE geocoding coverage](https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html)
+ [HERE car routing coverage](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/coverage/car-routing.html)
+ [HERE truck routing coverage](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/coverage/truck-routing.html)

## Terms of use and data attribution: HERE
<a name="HERE-terms"></a>

Before you use HERE data, be sure you can comply with all applicable legal requirements, including license terms applicable to HERE and AWS. Because of licensing limitations, you may not use HERE to store geocoding results for locations in Japan.

For information about the AWS requirements, see [AWS Service Terms](https://aws.amazon.com/service-terms/).

For additional information about HERE's attribution guidelines, see Section 2 of HERE Technologies' [Supplier Terms Applicable to Location and Other Content](https://legal.here.com/en-gb/terms/general-content-supplier-terms-and-notices).

## Error reporting to HERE
<a name="HERE-support"></a>

To report map errors and discrepancies to HERE, go to [https://www.here.com/contact](https://www.here.com/contact) and choose **Report a map error**.
