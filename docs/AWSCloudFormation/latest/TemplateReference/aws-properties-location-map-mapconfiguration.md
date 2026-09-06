---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-map-mapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::Map MapConfiguration
<a name="aws-properties-location-map-mapconfiguration"></a>

Specifies the map tile style selected from an available provider.

## Syntax
<a name="aws-properties-location-map-mapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-map-mapconfiguration-syntax.json"></a>

```
{
  "[CustomLayers](#cfn-location-map-mapconfiguration-customlayers)" : {{[ String, ... ]}},
  "[PoliticalView](#cfn-location-map-mapconfiguration-politicalview)" : {{String}},
  "[Style](#cfn-location-map-mapconfiguration-style)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-map-mapconfiguration-syntax.yaml"></a>

```
  [CustomLayers](#cfn-location-map-mapconfiguration-customlayers): {{
    - String}}
  [PoliticalView](#cfn-location-map-mapconfiguration-politicalview): {{String}}
  [Style](#cfn-location-map-mapconfiguration-style): {{String}}
```

## Properties
<a name="aws-properties-location-map-mapconfiguration-properties"></a>

`CustomLayers`  <a name="cfn-location-map-mapconfiguration-customlayers"></a>
Specifies the custom layers for the style. Leave unset to not enable any custom layer, or, for styles that support custom layers, you can enable layer(s), such as the `POI` layer for the VectorEsriNavigation style.
Currenlty only `VectorEsriNavigation` supports CustomLayers. For more information, see [Custom Layers](https://docs.aws.amazon.com/location/latest/developerguide/map-concepts.html#map-custom-layers).
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PoliticalView`  <a name="cfn-location-map-mapconfiguration-politicalview"></a>
Specifies the map political view selected from an available data provider.
*Required*: No
*Type*: String
*Pattern*: `^[A-Z]{3}$`
*Minimum*: `3`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Style`  <a name="cfn-location-map-mapconfiguration-style"></a>
Specifies the map style selected from an available data provider.
Valid [Esri map styles](https://docs.aws.amazon.com/location/previous/developerguide/esri.html):
+ `VectorEsriDarkGrayCanvas` – The Esri Dark Gray Canvas map style. A vector basemap with a dark gray, neutral background with minimal colors, labels, and features that's designed to draw attention to your thematic content.
+ `RasterEsriImagery` – The Esri Imagery map style. A raster basemap that provides one meter or better satellite and aerial imagery in many parts of the world and lower resolution satellite imagery worldwide.
+ `VectorEsriLightGrayCanvas` – The Esri Light Gray Canvas map style, which provides a detailed vector basemap with a light gray, neutral background style with minimal colors, labels, and features that's designed to draw attention to your thematic content.
+ `VectorEsriTopographic` – The Esri Light map style, which provides a detailed vector basemap with a classic Esri map style.
+ `VectorEsriStreets` – The Esri Street Map style, which provides a detailed vector basemap for the world symbolized with a classic Esri street map style. The vector tile layer is similar in content and style to the World Street Map raster map.
+ `VectorEsriNavigation` – The Esri Navigation map style, which provides a detailed basemap for the world symbolized with a custom navigation map style that's designed for use during the day in mobile devices.
Valid [HERE Technologies map styles](https://docs.aws.amazon.com/location/previous/developerguide/HERE.html):
+ `VectorHereContrast` – The HERE Contrast (Berlin) map style is a high contrast detailed base map of the world that blends 3D and 2D rendering.
**Note**
The `VectorHereContrast` style has been renamed from `VectorHereBerlin`. `VectorHereBerlin` has been deprecated, but will continue to work in applications that use it.
+ `VectorHereExplore` – A default HERE map style containing a neutral, global map and its features including roads, buildings, landmarks, and water features. It also now includes a fully designed map of Japan.
+ `VectorHereExploreTruck` – A global map containing truck restrictions and attributes (e.g. width / height / HAZMAT) symbolized with highlighted segments and icons on top of HERE Explore to support use cases within transport and logistics.
+ `RasterHereExploreSatellite` – A global map containing high resolution satellite imagery.
+ `HybridHereExploreSatellite` – A global map displaying the road network, street names, and city labels over satellite imagery. This style will automatically retrieve both raster and vector tiles, and your charges will be based on total tiles retrieved.
**Note**
Hybrid styles use both vector and raster tiles when rendering the map that you see. This means that more tiles are retrieved than when using either vector or raster tiles alone. Your charges will include all tiles retrieved.
Valid [GrabMaps map styles](https://docs.aws.amazon.com/location/previous/developerguide/grab.html):
+ `VectorGrabStandardLight` – The Grab Standard Light map style provides a basemap with detailed land use coloring, area names, roads, landmarks, and points of interest covering Southeast Asia.
+ `VectorGrabStandardDark` – The Grab Standard Dark map style provides a dark variation of the standard basemap covering Southeast Asia.
Grab provides maps only for countries in Southeast Asia, and is only available in the Asia Pacific (Singapore) Region (`ap-southeast-1`). For more information, see [GrabMaps countries and area covered](https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area).
Valid [Open Data map styles](https://docs.aws.amazon.com/location/previous/developerguide/open-data.html):
+ `VectorOpenDataStandardLight` – The Open Data Standard Light map style provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.
+ `VectorOpenDataStandardDark` – Open Data Standard Dark is a dark-themed map style that provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.
+ `VectorOpenDataVisualizationLight` – The Open Data Visualization Light map style is a light-themed style with muted colors and fewer features that aids in understanding overlaid data.
+ `VectorOpenDataVisualizationDark` – The Open Data Visualization Dark map style is a dark-themed style with muted colors and fewer features that aids in understanding overlaid data.
*Required*: Yes
*Type*: String
*Pattern*: `^[-._\w]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
