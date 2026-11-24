---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/layer-maps.html
---

# Layer maps

A layer map shows several files from an asset on one map. Use it to see an orthophoto and its boundaries together.

In the following example, building outlines that a connector produced are drawn over aerial imagery of Zurich. The layers panel lists the base map, the two layers, and the asset’s other files. A card shows the attributes of the selected building. The aerial imagery is swissIMAGE from the Federal Office of Topography swisstopo.

![Layer map of Zurich with building outlines drawn over aerial imagery plus a layers panel on the right and a card for the selected building](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/layer-map-zurich.png)

 *Aerial imagery: swissIMAGE, Federal Office of Topography swisstopo. For the terms of use, see [Terms of use for free geodata and geoservices on the swisstopo website](https://www.swisstopo.admin.ch/en/terms-of-use-free-geodata-and-geoservices).*

Layers need the same access as the file viewers: Consumers and above. For details, see [Who Can Open Files](view-your-content.md#view-who-can-open).

## What Can Be a Layer
<a name="layer-file-types"></a>

| Layer type | Files |
| --- | --- |
| Raster | GeoTIFF and Cloud Optimized GeoTIFF |
| Vector | GeoJSON, KML, GPX, Shapefile (with its `.dbf` and `.prj` files), GeoParquet |

Point clouds are not layers. To see a point cloud, open it in the point cloud viewer. See [Point Clouds](view-your-content.md#view-point-clouds).

## Open a Layer Map
<a name="layer-open"></a>
+  **In the asset.** Open the asset’s **Files** tab and choose the **Map** view. The map has a layers panel above the layers button. The panel lists the base map, the layers, and the asset’s files that can become layers.
+  **In a full-page map.** Select one or more map files and choose **Open in layers view**, from the **Files** header or the file menu. The map opens in the file viewer. You can also open it from the Map view’s tools, the file page header, and the selection card on the Explore map.

Choose **Close** to return to where you opened the layers view.

## Work with Layers
<a name="layer-manage"></a>

Each layer has these controls:
+ Show and hide.
+ Opacity.
+ Color.
+ Order, by dragging or with the arrows. The top layer draws over the others.
+ Zoom to the layer.
+ Retry, if the layer failed to load.
+ Remove.
+ A details button that opens the file’s details.

Other tools:
+  **Find files.** The file filter in the layers panel searches the whole asset, even when the asset is only partly listed.
+  **Groups.** **Add all** adds every file the filter lists as one group, named for the filter. A group shows, hides, fades, moves, zooms, and is removed as one, and it expands to list its files. A layer moves past a whole group, and a file in a group moves only within that group.
+  **Inspect features.** Choose a feature to see its attributes. Choose a file outline to open a card that lets you show the file on the map, zoom to it, or open it.
+  **Measure.** The measure tool gives distance and area.
+  **Labels.** File names sit on their outlines.

## Style Layers
<a name="layer-styling"></a>
+  **Vector layers.** A vector layer uses the file’s own colors when it has them. You can also use one color, a color for each value of an attribute, or graduated classes.
+  **Raster layers.** A raster layer has the same **Bands** and **Stretch** controls as the GeoTIFF viewer. The part of the raster that is on screen is sharpened, two rasters at a time.

## Limits
<a name="layer-limits"></a>
+ A map holds up to 50 layers, and up to 8 of them can be rasters.
+ A hidden layer loads only when you show it.
+ A vector file over 10 MB shows its size before it loads.

## Share a Layer Map
<a name="layer-share"></a>

The layers, their order, their settings, and their groups are in the page address. Send the link to share the map with someone who has access to the asset.

## Files with a Location
<a name="layer-locations"></a>

An asset or file that has a latitude and longitude, but no outline, shows as a pin on the project’s assets map and on the asset’s files map.
