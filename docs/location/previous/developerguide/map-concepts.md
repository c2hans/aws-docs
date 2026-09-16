---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/map-concepts.html
---

# Maps (V1) concepts
<a name="map-concepts"></a>

**Important**
**This page documents the previous Maps API (V1). Use it only for existing applications.** The Maps V2 API is the latest version. Use it for all new applications; see the latest [Amazon Location Service Maps](https://docs.aws.amazon.com/location/latest/developerguide/maps.html) developer guide.
The latest operations are `GetTile`, `GetStyleDescriptor`, `GetStaticMap`, `GetSprites`, and `GetGlyphs`. These operations are under the `geo-maps` namespace. They are exposed as `@aws-sdk/client-geo-maps` for JavaScript and `boto3.client('geo-maps')` for Python.
The `GetMapTile`, `GetMapStyleDescriptor`, and `Map` resources described below are previous-generation. Use them only for existing applications.

The Amazon Location Service *Map* resource gives you access to the underlying basemap data for a map. You use the Map resource with a map rendering library to add an interactive map to your application. You can add other functionality to your map, such as markers (or pins), routes, and polygon areas, as needed for your application.

**Note**
For information about how to use map resources in practice, see [Using Maps (V1) in your application](using-maps.md).

The following is an overview of how to create and use map resources:

![](https://docs.aws.amazon.com/location/previous/developerguide/images/illustration-maps.PNG)

1. You create a map resource in your AWS account by selecting a map style from a data provider.

1. You can then select and install the SDK that matches your development environment and applications. For more information about available options, see the topic about [Accessing Amazon Location](how-to-access.md).

1. To display a map in your application, combine a map resource with a rendering library, such as Amplify, MapLibre, or Tangram. For more information. see [Using maps](using-maps.md) in this guide.

1. You can then integrate monitoring by using services, such as Amazon CloudWatch and AWS CloudTrail with Amazon Location. For more information see, [Monitor Amazon Location Service with Amazon CloudWatch](monitoring-using-cloudwatch.md) and [Log and monitor with AWS CloudTrail](logging-using-cloudtrail.md).

## Map styles
<a name="map-style-concepts"></a>

When you create a map resource, you must choose a map style for that resource. Map styles define the look of the rendered map. For example, the following image shows the same data provider with two different styles from different map resources in Amazon Location. One style is a typical road style, based on the vector data in the map. The other includes raster data showing satellite imagery. The style may change as you zoom in or out on the map, but typically styles have a consistent theme. It's possible to override parts or all of the style information before passing it to the map rendering library.

![An image showing the same area of the world, drawn with two different styles: a road style and a satellite imagery style.](https://docs.aws.amazon.com/location/previous/developerguide/images/map-styles-concepts.png)

## Political views
<a name="political-views"></a>

Certain maps styles in Amazon Location Service support additional political views.

**Note**
The political view must be used in compliance with applicable laws, including those laws about mapping of the country or region where the maps, images, and other data and third-party content which you access through Amazon Location Service is made available.

The following map styles support an India (IND) political view.
+ [Esri map styles](esri.md#esri-map-styles):
  + Esri Navigation
  + Esri Light
  + Esri Street Map
  + Esri Dark Gray Canvas
  + Esri Light Gray Canvas
+ [Open Data map styles](open-data.md#open-data-map-styles):
  + Open Data Standard Light
  + Open Data Standard Dark
  + Open Data Visualization Light
  + Open Data Visualization Dark

In the Amazon Location Service console, you can filter the styles shown to just show the styles that support the India political view.

## Custom Layers
<a name="map-custom-layers"></a>

A custom layer is an additional layer you can enable for a map style. Currently only the VectorEsriNavigation map style supports the `POI` custom layer.

When you enable the `POI` custom layer it adds a richer set of places, such as shops, services, restaurants, attractions, and other points of interest to your map. By default, the custom layer is `unset`. For more information see, [MapConfiguration](https://docs.aws.amazon.com/location/previous/APIReference/API_MapConfiguration.html) in the Location API reference.

## Map rendering
<a name="map-rendering-concepts"></a>

To render a map in your application, you will typically use a map rendering library. There are several common options for libraries to use:
+ **MapLibre** – MapLibre is an open source library specifically for rendering interactive maps, and is the preferred method of rendering maps from Amazon Location Service. MapLibre includes the ability to render raster and vector data from a data source (such as an Amazon Location map resource). You can extend MapLibre to draw your own data on the map.
+ **Amplify** – Amplify is an open source framework for building applications for the web, iOS, Android, and more. If your application uses Amplify, then you can extend it to include Amazon Location functionality. Amplify includes libraries specifically for creating Amazon Location based applications, including rendering maps. Amplify uses MapLibre to render the map, but provides additional functionality that is specific to Amazon Location Service to make it more efficient to use, and also adding search and other functionality.
+ **Tangram** – Tangram is an alternative open source library that renders interactive maps, similar to MapLibre.

The map rendering library pulls data from Amazon Location Service at runtime, rendering the map data based on the map resource you select. The map resource defines the data provider and map style that will be used.

**Note**
For new code, request tiles with the latest [`GetTile`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html) operation and styles with [`GetStyleDescriptor`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStyleDescriptor.html), under `geo-maps`. These do not require a map resource, and the latest API also adds [`GetStaticMap`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStaticMap.html) for server-rendered map images. See the latest [Amazon Location Service Maps](https://docs.aws.amazon.com/location/latest/developerguide/maps.html) developer guide.

The following image shows how the map resource is used in Amazon Location Service along with a map rendering library to create the final map.

![An image showing a user creating a map resource in Amazon Location Service and an app using that resource to get map data and render a map.](https://docs.aws.amazon.com/location/previous/developerguide/images/RenderMapInApp.png)

1. You create a map resource in Amazon Location Service, using the AWS Management Console or AWS CLI. This defines the data provider and the map style that you want to use.

1. Your application includes a map rendering library. You give the map rendering library the name of the map resource to use. The map rendering library pulls data and style information for that map resource from Amazon Location and renders the map on screen.

## Maps terminology
<a name="map-components"></a>

**Map resource**
Allows you to access map data from a selected provider. Use the map resource to fetch map tiles that contain map data and a style descriptor to specify how features render on a map.
The latest API has no map resource. Tiles and style descriptors are requested directly with `GetTile` and `GetStyleDescriptor` under `geo-maps`. See the latest [Amazon Location Service Maps](https://docs.aws.amazon.com/location/latest/developerguide/maps.html) developer guide.

**Basemap**
Provides geographic context to your map, which is stored as vector tile layers. Tile layers include geographical context such as street names, buildings, and land use for visual reference.

**Vector**
Vector data is shape data made up of points, lines, and polygons. It is often used to store and display roads, locations, and areas on a map. A vector shape can also be used as icons for markers on a map.

**Raster**
Raster data is image data, made up of a grid, usually of colors. It is often used to store and display a representation of continuous data on maps, such as terrain, satellite imagery, or heat maps. Raster images can also be used as images or icons.

**Map Style**
Vector data does not inherently include information about how to draw the layers of data to create the final map. A map style defines color and other style information for the data to define how it will look when rendered. Map resources include style information for the map.
Amazon Location Service provides styles following the [Mapbox GL style specification](https://docs.mapbox.com/mapbox-gl-js/style-spec/).

**Vector tile **
A tile format that stores map data using vector shapes. This data results in a map that can adjust to the display resolution, and selectively render features in a number of ways, while maintaining a small file size for optimal performance.
Supported vector file format: Mapbox Vector Tiles (MVT).

**Glyph file**
A binary file containing encoded Unicode characters. Used by a map renderer to display labels.

**Sprite file**
A Portable Network Graphic (PNG) image file that contains small raster images, with location descriptions in a JSON file. Used by a map renderer to render icons or textures on a map.
