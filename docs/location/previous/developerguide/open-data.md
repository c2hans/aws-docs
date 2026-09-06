---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/open-data.html
---

# Open Data
<a name="open-data"></a>

Amazon Location Service provides access to open source map data via the Open Data provider. Open Data provides global basemaps built from the [Daylight map distribution](https://daylightmap.org) of [OpenStreetMap (OSM)](https://www.openstreetmap.org/), [Natural Earth](https://www.naturalearthdata.com/), and other open data sources. The maps provided are designed to support different applications and use cases, including logistics and delivery, and data visualization in web and mobile environments. With over a million map makers, the OSM community updates hundreds of thousands of features per day. Amazon Location Service regularly incorporates these edits.

For additional capability information, see [Open Data](https://aws.amazon.com/location/data-providers/open-data/) on *Amazon Location Service data providers*.

**Topics**
+ [Open Data map styles](#open-data-map-styles)
+ [Coverage: Open Data](#open-data-places-coverage)
+ [Terms of use and data attribution: Open Data](#open-data-terms)
+ [Error reporting and contributing to Open Data](#open-data-support)

## Open Data map styles
<a name="open-data-map-styles"></a>

Amazon Location Service supports the following map styles when [creating a map resource](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html):

Open Data map styles support alternate [Political views](map-concepts.md#political-views).

------
#### [ Open Data Standard Light ]

**Open Data Standard Light**

![Street map showing Cambridge Street area with numbered routes including Route 28 and Route 3.](http://docs.aws.amazon.com/location/previous/developerguide/images/VectorOpenDataStandardLight.png)

**Map style name**: `VectorOpenDataStandardLight`

This provides a detailed basemap for the world in a light map style, suitable for website and mobile application use. This includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.

This basemap is based on the OSM [Daylight map distribution](https://daylightmap.org) compiled from OpenStreetMap (OSM) contributors. The OSM community includes over 1.8 million contributors who update more than 500,000 features daily. Amazon Location Service incorporates these edits on a regular basis.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Amazon Ember Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Regular,Noto Sans Regular
+ Amazon Ember Medium,Noto Sans Medium
+ Amazon Ember Regular Italic,Noto Sans Italic
+ Amazon Ember Regular,Noto Sans Regular
+ Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold
+ Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold
+ Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular
+ Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium

**Note**
The fonts used by `VectorOpenDataStandardLight` are combined fonts that use `Amazon Ember` for most glyphs but `Noto Sans` for glyphs unsupported by `Amazon Ember`.

------
#### [ Open Data Standard Dark ]

**Open Data Standard Dark**

![Map showing street layout of downtown area with Charles River, major roads, and landmarks.](http://docs.aws.amazon.com/location/previous/developerguide/images/VectorOpenDataStandardDark.png)

**Map style name**: `VectorOpenDataStandardDark`

This is a dark-themed map style that provides a detailed basemap for the world, suitable for website and mobile application use. This includes highways, major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.

This basemap is based on the OSM [Daylight map distribution](https://daylightmap.org) compiled from OpenStreetMap (OSM) contributors. The OSM community includes over 1.8 million contributors who update more than 500,000 features daily. Amazon Location Service incorporates these edits on a regular basis.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Amazon Ember Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Regular,Noto Sans Regular
+ Amazon Ember Medium,Noto Sans Medium
+ Amazon Ember Regular Italic,Noto Sans Italic
+ Amazon Ember Regular,Noto Sans Regular
+ Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold
+ Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold
+ Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular
+ Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium

**Note**
The fonts used by `VectorOpenDataStandardDark` are combined fonts that use `Amazon Ember` for most glyphs but `Noto Sans` for glyphs unsupported by `Amazon Ember`.

------
#### [ Open Data Visualization Light ]

**Open Data Visualization Light**

![Street map showing Cambridge Street area with surrounding roads and landmarks.](http://docs.aws.amazon.com/location/previous/developerguide/images/VectorOpenDataVisualizationLight.png)

**Map style name**: `VectorOpenDataVisualizationLight`

This is a light-themed style with muted colors and fewer features that aids in understanding overlaid data.

This basemap is based on the OSM [Daylight map distribution](https://daylightmap.org) compiled from OpenStreetMap (OSM) contributors. The OSM community includes over 1.8 million contributors who update more than 500,000 features daily. Amazon Location Service incorporates these edits on a regular basis.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Amazon Ember Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Regular,Noto Sans Regular
+ Amazon Ember Medium,Noto Sans Medium
+ Amazon Ember Regular Italic,Noto Sans Italic
+ Amazon Ember Regular,Noto Sans Regular
+ Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold
+ Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold
+ Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular
+ Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium

**Note**
The fonts used by `VectorOpenDataVisualizationLight` are combined fonts that use `Amazon Ember` for most glyphs but `Noto Sans` for glyphs unsupported by `Amazon Ember`.

------
#### [ Open Data Visualization Dark ]

**Open Data Visualization Dark**

![Dark-themed map showing street layout of downtown area with labeled roads and landmarks.](http://docs.aws.amazon.com/location/previous/developerguide/images/VectorOpenDataVisualizationDark.png)

**Map style name**: `VectorOpenDataVisualizationDark`

This is a dark-themed style with muted colors and fewer features that aids in understanding overlaid data.

This basemap is based on the OSM [Daylight map distribution](https://daylightmap.org) compiled from OpenStreetMap (OSM) contributors. The OSM community includes over 1.8 million contributors who update more than 500,000 features daily. Amazon Location Service incorporates these edits on a regular basis.

**Fonts**

Amazon Location serves fonts using `[GetMapGlyphs](https://docs.aws.amazon.com/location-maps/latest/APIReference/API_GetMapGlyphs.html#API_GetMapGlyphs_RequestSyntax)`. The following are available font stacks for this map:
+ Amazon Ember Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Regular,Noto Sans Regular
+ Amazon Ember Medium,Noto Sans Medium
+ Amazon Ember Regular Italic,Noto Sans Italic
+ Amazon Ember Regular,Noto Sans Regular
+ Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold
+ Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold
+ Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular
+ Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular
+ Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium

**Note**
The fonts used by `VectorOpenDataVisualizationDark` are combined fonts that use `Amazon Ember` for most glyphs but `Noto Sans` for glyphs unsupported by `Amazon Ember`.

------

## Coverage: Open Data
<a name="open-data-places-coverage"></a>

Open Data includes maps with global coverage for rendering with an [Amazon Location Service map resource](map-concepts.md).

**Note**
Open Data is for use with Amazon Location Service map resources only. You can't use Open Data as a data provider to support queries for geocoding, reverse geocoding, and searches, or to support queries to calculate a route.

## Terms of use and data attribution: Open Data
<a name="open-data-terms"></a>

Before you use Open Data, be sure you can comply with all applicable legal requirements, including license terms applicable to Open Data and AWS.

For more information about the AWS requirements, see [AWS Service Terms](https://aws.amazon.com/service-terms/).

For information about Open Data attribution guidelines, see OpenStreetMap's [Copyright and License](https://www.openstreetmap.org/copyright) and OpenStreetMap's [Licence/Attribution Guidelines](https://wiki.osmfoundation.org/wiki/Licence/Attribution_Guidelines).

## Error reporting and contributing to Open Data
<a name="open-data-support"></a>

OpenStreetMap (OSM) and Natural Earth are community-driven open data projects. If you encounter a problem with the data, you can report the errors or directly contribute fixes or suggestions.
+ To report an error or offer a suggestion in OSM, you can create a *note* on the map. This is a comment on the map that assists contributors in making fixes to the map. You create notes through the [OpenStreetMap website](https://openstreetmap.org/). For more information about notes, see [Notes](https://wiki.openstreetmap.org/wiki/Notes) in the *OpenStreetMap wiki*.
+ For more information about contributing directly to OpenStreetMap, including adding locations and fixing errors, see [Contribute map data](https://wiki.openstreetmap.org/wiki/Contribute_map_data) in the *OpenStreetMap wiki*.
+ To submit a correction request for data in Natural Earth, you can submit an issue through the [Natural Earth website](https://www.naturalearthdata.com/issues/).

**Note**
Correcting errors in OpenStreetMap can happen quickly, however, it can take time for corrections to appear in the Daylight map distribution of the OSM data that is used by the Open Data provider. The [Daylight Map Distribution](https://daylightmap.org) website provides more information about the process. Additionally, Amazon Location Service updates the map data used in Amazon Location Service approximately monthly.
