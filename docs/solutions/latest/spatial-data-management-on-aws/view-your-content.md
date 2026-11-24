---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/view-your-content.html
---

# View and inspect your content

The Spatial Data Portal opens many spatial file formats directly in your browser. You can inspect, measure, and review point clouds, 3D models, maps, tables, images, video, and text where they are stored. Downloading a file to check that it is the right one is slow, costly, and unnecessary. For many formats the Portal reads only the part of the file that is on screen, so you can explore a very large file without moving it. You can also compare files side by side and layer map files on one map.

## What Viewing Is For
<a name="view-for-what"></a>

Spatial files are large, and you rarely need all of one. In a cloud workflow, content is used where it is stored, by people and by connectors. Viewing lets you answer a question about content in place, and you download a file only when a tool outside SDMA needs a copy.

| You want to | Use |
| --- | --- |
| Confirm that a capture is the one you expect | The **Panorama**, **Image**, and **Point cloud** views of one file. See [See One File Several Ways](#view-several-views). |
| Check coverage, noise, or gaps in a scan | The point cloud viewer, colored by intensity, elevation, or classification. See [Point Clouds](#view-point-clouds). |
| See what changed between two versions of a file, or two captures of one place |  **Compare**, with synchronized views. See [Compare versions and files](compare-files.md). |
| See imagery and vector data together, in place |  **Layer maps**. See [Layer maps](layer-maps.md). |
| Check whether a model’s output makes sense | The findings that a connector run draws over the scan, with the thresholds that the run used. See [Findings from a Connector Run](#view-findings). |
| Review a scene or a building model | The 3D model viewer, which opens USD scenes and IFC models. See [3D Models](#view-3d-models). |
| Review a table of results | The table viewer for Parquet, CSV, and TSV files. See [Tables and Text](#view-tables-text). |
| Show someone a preview without giving them access to the file | Server-generated thumbnails and previews, which Viewers can see. See [Who Can Open Files](#view-who-can-open). |

## File Types You Can View
<a name="view-file-types"></a>

The Portal chooses a viewer from the file type.

| Kind | File types | Viewer |
| --- | --- | --- |
| Point clouds | COPC (`.copc.laz`), LAS, LAZ, E57, PLY, PCD, XYZ, PTS | 3D point cloud viewer |
| Gaussian splats |  `.splat`, `.ksplat`, `.spz`, and 3D Gaussian splatting (3DGS) or SuperSplat compressed PLY | 3D splat viewer |
| 3D models | GLB, glTF, OBJ, FBX, 3MF, DAE, STL, IFC, IFCZIP, 3DM (Rhinoceros), USD, USDA, USDC, USDZ | 3D model viewer |
| Maps | GeoTIFF and Cloud Optimized GeoTIFF, GeoJSON, KML, GPX, Shapefile, GeoParquet | Map viewer |
| Tables | Parquet, CSV, TSV | Table viewer |
| Documents and text | PDF, Markdown, JSON, JSON Lines, XML, YAML, log files, plain text, and common script, source, and configuration files | Document and text viewer |
| Images | JPG, PNG, GIF, WebP, BMP, AVIF, SVG, and panoramas | Image and panorama viewer |
| Video and audio | MP4, M4V, MOV, WebM; MP3, WAV, M4A, AAC, FLAC, OGG, Opus, AIFF | Video and audio player |

## See One File Several Ways
<a name="view-several-views"></a>

A single file can open in more than one view. When you upload a file, SDMA can generate other representations of it, and connectors can add more. The file viewer shows a tab for every view of the file at the top left, so you can move between them without leaving the file.

For example, an E57 laser scan of a facility can offer these views:

| View | What it shows |
| --- | --- |
|  **Panorama**  | A 360-degree panorama that SDMA generated from the scan on upload. Drag to look around the scan position. |
|  **Image**  | The photographs that the scanner stored in the file, extracted on upload. A strip of thumbnails switches between them. |
|  **Video**  | A video that SDMA generated from the scan’s intensity data. |
|  **Point cloud**  | The scan itself, streamed into the 3D point cloud viewer. |

![File viewer for an E57 scan with the four view tabs at the top left and the panorama view open](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/view-e57-panorama.png)

Use the views together to answer different questions about the same capture:
+  **Confirm you have the right scan** – The panorama and photographs show where the scanner stood and what it saw, in seconds, before anything large loads.
+  **Check scan quality** – The intensity video and the point cloud show gaps, shadows, and noise.
+  **Find something in the scene** – Look around the panorama, then switch to the point cloud to measure it.
+  **Share what was captured** – Send a link to the panorama or a photograph to someone who does not need the full point cloud.

Connectors can add views of their own, for example a COPC copy of a LAS or LAZ file, or a preview image of a model.

## Open a File
<a name="view-open-file"></a>
+ In the asset’s **Files** tab, select a file and choose **View**.
+ In search results or on a file card, choose the file.
+ Select several point cloud files and choose **View in 3D** to see them together in one scene.

The viewer shows the file with a details panel beside it. The panel has the file’s attributes, derived content, connected resources, and version history.

## Inspect Without Downloading
<a name="view-without-downloading"></a>

How a file opens depends on its format.

 **The Portal reads only what is on screen.**
+ COPC point clouds are read in place with range requests.
+ Point clouds that a connector has tiled stream as level-of-detail tiles.
+ GeoTIFF files are read by the byte ranges that the current view needs. If a connector has made a Cloud Optimized GeoTIFF copy, the Portal uses it.
+ Parquet files show a table read from the file footer and the first 500 rows.
+ Large text files load in 2 MB pieces.
+ E57 files without tiles or a COPC copy stream in order, and you can pause loading.
+ Video and audio stream from their signed links.

 **Your browser loads the file to draw it.** This applies to 3D models, PLY and splat files, and map files such as GeoJSON, KML, GPX, and Shapefile. The Portal does not save a copy to your computer.
+ Large files ask before they load, because the browser reads the whole file into memory. 3D models, PLY files, and splats ask above 300 MB. IFC models ask above 150 MB, and zipped IFC models above 30 MB, because IFC builds geometry several times the size of the file. A single E57 file asks above 2 GB. A PLY file over 2 GB does not open.
+ A LAS or LAZ file with no tiles and no COPC copy displays a message that says so, and offers to run content derivation.
+ If a GeoTIFF is too costly to stream, uses an encoding the browser cannot decode, or comes from a server that does not support range requests, the viewer displays a message that explains why, and offers other ways to see the file.

**Note**
To save a file to your computer, use **Download**. In the desktop application, **Download** opens the download dialog. In a browser, the same button reads **Download copy**.

## Who Can Open Files
<a name="view-who-can-open"></a>

Opening a file in a viewer needs more than metadata access.
+  **Consumers, Contributors, Managers, and Owners** of the project can open files in the viewers.
+  **Viewers** see file names, attributes, and server-generated thumbnails and previews. They cannot open file contents in a viewer, compare files, or use layer maps.

For permission details, see [Access Management](access-control.md).

## Controls That Every Viewer Shares
<a name="view-controls"></a>
+  **Views** – When a file has more than one view, the tabs at the top left switch between them. See [See One File Several Ways](#view-several-views).
+  **Fit** – Press `F` to fit the view to the file.
+  **Full screen** – Every viewer has a full screen button.
+  **Shortcuts** – Press `?` to list the keyboard shortcuts for the viewer you are using.
+  **Settings** – App settings sets defaults for 3D display, such as background, up axis, and auto-rotate. For more information, see [App Settings](edit-assets-in-the-portal.md#app-settings).

## Point Clouds
<a name="view-point-clouds"></a>

The point cloud viewer draws a scan in your browser, where it is stored. In the following example, an E57 scan of an industrial facility is colored by RGB. The toolbar is at the top right. Its first item is a badge that reads **LOD tiles**, so the scan streams as level-of-detail tiles that a connector made. The counter at the bottom right shows how many points have loaded. The tabs at the top left switch to the file’s other views, and the **RGB** color control sits below them. In the toolbar, after the badge, the **Top**, **Front**, **Side**, and **Iso** buttons jump to preset camera angles.

![Point cloud viewer showing an E57 scan of an industrial facility under a blue sky with the view tabs and the LOD tiles badge and the camera preset buttons](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/view-point-cloud.png)

+  **Color by** – RGB, elevation, intensity, classification, return number, or flight line. A legend shows the colors.
+  **Classification** – A panel shows and hides classes, for all 256 classification codes. When you color by class, the panel is the legend.
+  **Point limit and pause** – For COPC and E57 files, set how many points to draw and pause loading.
+  **Tools** – Measure, zoom to a box, crop, point size, edge darkening, height shading, sky, guides, and field of view.
+  **Ground coordinates** – The coordinate under the cursor appears in the file’s own coordinate reference system.
+  **Merged view** – Select several LAS, LAZ, COPC, or E57 files and choose **View in 3D** to see them in one scene. The merged view needs a connector that serves tiles for the asset. See [Sending Content to an External Analysis Service and Viewing It in SDMA](connector-patterns.md#pattern-external-analysis).

## Findings from a Connector Run
<a name="view-findings"></a>

A connector that detects or measures things in a scan can write its results as GeoJSON and describe how to draw them. When you open the source point cloud, the viewer draws those results over the scan. For how a connector declares this, see [Drawing a Run’s Findings in the Viewer](connector-configuration.md#output-presentation).

In the following example, a connector reconstructed the conductors in a power line corridor and measured how close the trees come to them. The panel on the left is titled **Corridor findings**. Each layer in it is one kind of finding: **Conductors**, **Tree clearance**, **Fall-in risk** for trees tall enough to strike a conductor, **Needs review**, and **Utility poles**. The **Tree clearance** layer has a slider and preset buttons for its clearance zones, and its legend lists Zone 1 at 1.50 m and Zone 2 at 3.00 m, the values this run used. The scan is point cloud data from the Tokyo Metropolitan Government, licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). It is converted for viewing and shown as rendered in the Spatial Data Portal.

![Point cloud viewer with a Corridor findings panel on the left and the findings drawn over a scan of a residential area](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/view-findings.png)

+  **A panel with the connector’s title.** The panel has a switch to show the findings, and a note that they were derived from this content, so you can tell them apart from the file’s own points.
+  **Layers.** Each layer, for example detected objects, can be shown or hidden. A layer can be colored by comparing a property, such as a score, with thresholds.
+  **A slider and presets.** A layer can offer a slider that keeps the features within a value, such as a minimum score. Preset buttons jump to the thresholds that the run used.
+  **A legend.** The legend lists each threshold with the value from the run that produced the file. A threshold that the run did not record is not drawn, and the panel says so.
+  **Which run made it.** The panel footer shows **Config version**, the connector version that the run used. The thresholds are the run’s own, so a result from an earlier run keeps its meaning after the connector changes.
+  **Details.** Choose a finding to see its properties.

Findings appear only when the connector’s output declares a presentation, and the run recorded it. Use the findings to check a model before you trust its attributes. If the findings do not match what you see in the scan, look at the run that produced them.

## 3D Models
<a name="view-3d-models"></a>

The 3D model viewer opens a model where it is stored. In the following example, a USD robot arm opens with its **Joints** panel. To pose the arm, turn on **Joints** under **Scene** in **View settings**, then drag a slider. **Reset** returns the arm to the pose in the file. The robot arm is the SO-ARM101 model from NVIDIA’s [Sim-to-Real SO-101 Workshop](https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop) on the GitHub website, licensed [Apache 2.0](https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop/blob/main/LICENSE).

![3D model viewer showing a posed USD robot arm with a Joints panel on the left that has a slider for each joint](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/view-usd-model.png)

+  **Lighting and display** – Controls for environment, exposure, light rotation, and ground shadow. Models with Phong or Lambert materials are lit the same way as glTF models.
+  **Section and crop** – Cut the model with a section plane across an axis, and use the crop box.
+  **IFC** – Choose an element to see its properties. Isolate or hide elements, show or hide them by kind and building story, and cut a plan at a story.
+  **Rhino 3DM** – Meshes with no render material take the color that Rhino displays. A file saved with no render meshes tells you how to save it again.
+  **USD** – Opens USD, USDA, USDC, and USDZ scenes, including NVIDIA Isaac Sim robots. The viewer reads the layers, materials, and textures that a scene names. It poses robot joints, plays animation, and lets you choose variants.
+  **OBJ and glTF** – The viewer finds material files, buffers, and textures by their path in the asset.

**Note**
A 3D model can name other files, such as textures, materials, buffers, and USD layers. The viewer finds them in two places:
 **In the same asset.** A path such as `textures/steel.png` is read from the model’s folder in the asset. Upload the files into the asset and keep their folders.
 **At a web address.** A full `https://` address goes to your browser, and the Portal’s content security policy (CSP) decides whether it loads. A file at an address that the policy does not allow does not load. An address that a browser cannot fetch, such as `omniverse://`, does not load either.
A USD scene lists the files that it could not find in the note at the top left of the viewer.

## Maps
<a name="view-maps"></a>
+  **GeoTIFF** – Imagery is placed by its georeferencing. A **Display** panel offers band choice, stretch presets, and opacity. A TIFF with no georeferencing opens in pixel space.
+  **GeoJSON, KML, and GPX** – Open on a map. Choose **Map** or **Text** to switch views. Choose a feature to see its properties.
+  **Shapefile** – Opens with its `.dbf` attributes and `.prj` projection, which the Portal reads from the same folder.
+  **GeoParquet** – Opens on a map.
+  **Base map** – A switch at the bottom right changes the base map.

To show several map files together, see [Layer maps](layer-maps.md).

## Tables and Text
<a name="view-tables-text"></a>
+  **Parquet** – Shows a table built from the file footer and the first 500 rows.
+  **CSV and TSV** – Open as tables.
+  **Text and JSON** – Support find, line links, folding, and format. JSON opens formatted.
+  **Markdown** – Renders as a document.

## Video, Audio, and Images
<a name="view-media"></a>
+ Video and audio use one shared playback bar.
+ Any video frame can be saved as a PNG.
+ To play a folder of images as video, see [Play a Folder of Images as Video](compare-files.md#compare-image-folders).

## Next Steps
<a name="view-next"></a>
+  [Edit assets in the Portal](edit-assets-in-the-portal.md) – Change an asset’s files and attributes.
