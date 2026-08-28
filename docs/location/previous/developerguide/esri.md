---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/esri.html
---

# Esri
<a name="esri"></a>

Amazon Location Service uses Esri's location services to help AWS customers to use maps, geocode, and calculate routes effectively. Esri’s location services are built with high-quality, authoritative, and ready-to-use location data, curated by expert teams of cartographers, geographers, and demographers.

For additional capability information, see [Esri](https://aws.amazon.com/location/data-providers/esri/) on *Amazon Location Service data providers*.

**Topics**
+ [Esri map styles](#esri-map-styles)
+ [Coverage: Esri](#esri-places-coverage)
+ [Terms of use and data attribution: Esri](#esri-terms)
+ [Error reporting to Esri](#esri-support)

## Esri map styles
<a name="esri-map-styles"></a>

Amazon Location Service supports the following Esri map styles when [creating a map resource](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html).

**Note**
Esri map styles that are not listed in this section are not supported.

The Esri vector styles support alternate [Political views](map-concepts.md#political-views).

------
#### [ Esri Navigation ]

**Esri Navigation**

![Map showing Boston neighborhoods including Beacon Hill, East Cambridge, and waterfront areas.](http://docs.aws.amazon.com/location/previous/developerguide/images/EsriNav.png)

**Map style name**: `VectorEsriNavigation`

This map provides a detailed basemap for the world symbolized with a custom navigation map style that's designed for use during the day in mobile devices.

This comprehensive street map includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries. The vector tile layer in this map is built using the same data sources used for the World Street Map and other Esri basemaps. Enable the `POI` layer by setting it in [CustomLayers](https://docs.aws.amazon.com/location/previous/APIReference/API_MapConfiguration.html) to leverage the additional places data.

For more information, see [Esri World Navigation](https://www.arcgis.com/home/item.html?id=63c47b7177f946b49902c24129b87252) on the Esri website.

**Note**
The`VectorEsriNavigation` map pictured above has the `POI` layer enabled.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Arial Italic
+ Arial Regular
+ Arial Bold
+ Arial Unicode MS Bold
+ Arial Unicode MS Regular

------
#### [ Esri Imagery ]

**Esri Imagery**

![](http://docs.aws.amazon.com/location/previous/developerguide/images/EsriImagery.png)

**Map style name**: `RasterEsriImagery`

This map provides one meter or better satellite and aerial imagery in many parts of the world and lower resolution satellite imagery worldwide.

The map includes 15m imagery at small and mid-scales (\~1:591M down to \~1:72k) and 2.5m SPOT Imagery (\~1:288k to \~1:72k) for the world. The map features 0.5m resolution imagery in the continental United States and parts of Western Europe from Maxar. This map features additional Maxar submeter imagery in many parts of the world. In other parts of the world, the GIS User Community has contributed imagery at different resolutions. In select communities, very high-resolution imagery (down to 0.03m) is available down to \~1:280 scale.

For more information, see [Esri World Imagery](https://www.arcgis.com/home/item.html?id=10df2279f9684e4a9f6a7f08febac2a9) on the Esri website.

------
#### [ Esri Light ]

**Esri Light**

![Map of Boston showing Beacon Hill neighborhood with MBTA stations and major streets.](http://docs.aws.amazon.com/location/previous/developerguide/images/EsriWorldTopo.png)

**Map style name**: `VectorEsriTopographic`

This provides a detailed basemap for the world symbolized with a classic Esri map style. This includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.

This basemap is compiled from a variety of authoritative sources from several data providers, including the US Geological Survey (USGS), US Environmental Protection Agency (EPA), US National Park Service (NPS), Food and Agriculture Organization of the United Nations (FAO), Department of Natural Resources Canada (NRCAN), HERE, and Esri. Data for select areas is sourced from OpenStreetMap contributors. Additionally, data is provided by the GIS community.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Noto Sans Italic
+ Noto Sans Regular
+ Noto Sans Bold
+ Noto Serif Regular
+ Roboto Condensed Light Italic

------
#### [ Esri Light Gray Canvas ]

**Esri Light Gray Canvas**

![Map of Boston area showing streets, neighborhoods, and landmarks in grayscale.](http://docs.aws.amazon.com/location/previous/developerguide/images/EsriLightGray.png)

**Map style name**: `VectorEsriLightGrayCanvas`

This map provides a detailed basemap for the world symbolized with a light gray, neutral background style with minimal colors, labels, and features that's designed to draw attention to your thematic content.

This vector tile layer is built using the same data sources used for the Light Gray Canvas and other Esri basemaps. The map includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.

For more information, see [Esri Light Gray Canvas](https://www.arcgis.com/home/item.html?id=c7e86d018d2945799cdc8e3dfbe30b43) on the Esri website.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Ubuntu Italic
+ Ubuntu Regular
+ Ubuntu Light
+ Ubuntu Bold

------
#### [ Esri Street Map ]

**Esri Street Map**

![Map showing Beacon Hill neighborhood with MBTA stations and surrounding Boston areas.](http://docs.aws.amazon.com/location/previous/developerguide/images/EsriStreet.png)

**Map style name**: `VectorEsriStreets`

This map provides a detailed basemap for the world symbolized with a custom navigation map style that's designed for use during the day in mobile devices.

This comprehensive street map includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries. It also includes a richer set of places, such as shops, services, restaurants, attractions, and other points of interest. The vector tile layer in this map is built using the same data sources used for the World Street Map and other Esri basemaps.

For more information, see [Esri World Street](https://www.arcgis.com/home/item.html?id=de26a3cf4cc9451298ea173c4b324736) on the Esri website.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Arial Italic
+ Arial Regular
+ Arial Bold
+ Arial Unicode MS Bold
+ Arial Unicode MS Regular

------
#### [ Esri Dark Gray Canvas ]

**Esri Dark Gray Canvas**

![Map of Boston area showing neighborhoods, streets, and landmarks in dark gray style.](http://docs.aws.amazon.com/location/previous/developerguide/images/EsriDarkGray.png)

**Map style name**: `VectorEsriDarkGrayCanvas`

This map provides a detailed vector basemap for the world symbolized with a dark gray, neutral background style with minimal colors, labels, and features that's designed to draw attention to your thematic content.

This map includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries. The vector tile layers in this map are built using the same data sources used for the Dark Gray Canvas raster map and other Esri basemaps.

For more information, see [ Esri Dark Gray Canvas](https://www.arcgis.com/home/item.html?id=94521475e86b48f1ad2a21b2ea272d7a) on the Esri website.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Ubuntu Medium Italic
+ Ubuntu Medium
+ Ubuntu Italic
+ Ubuntu Regular
+ Ubuntu Bold

------

## Coverage: Esri
<a name="esri-places-coverage"></a>

You can use Esri as a data provider to support queries for geocoding, reverse geocoding, and searches when you [create a place index resource](https://docs.aws.amazon.com/location/previous/developerguide/places-prerequisites.html#create-place-index-resource), or to support queries to calculate a route when you [create a route calculator resource](https://docs.aws.amazon.com/location/previous/developerguide/routes-prerequisites.html#create-route-calculator-resource).

Esri provides different levels of data quality in different regions of the world. For additional information about coverage in your region of interest, see:
+ [Esri details on geocoding coverage](https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm)
+ [Esri details on street networks and traffic coverage](https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm)

## Terms of use and data attribution: Esri
<a name="esri-terms"></a>

Before you use Esri's data, be sure you can comply with all applicable legal requirements, including license terms applicable to Esri and AWS.

For more information about the AWS requirements, see [AWS Service Terms](https://aws.amazon.com/service-terms/).

For information about Esri's attribution guidelines, see Esri's [Data Attributions and Terms of Use](https://www.esri.com/en-us/legal/terms/data-attributions).

## Error reporting to Esri
<a name="esri-support"></a>

If you encounter a problem with the data and want to report errors and discrepancies to Esri, follow Esri's technical support article for [How to: Provide feedback on basemaps and geocoding](https://support.esri.com/en/technical-article/000011831).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
