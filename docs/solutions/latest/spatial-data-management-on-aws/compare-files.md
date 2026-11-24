---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/compare-files.html
---

# Compare versions and files

Compare shows files side by side in the Spatial Data Portal. You can compare two versions of one file, or compare different files in the same asset. Views stay in step, so the same area of a point cloud, map, or image shows in every pane.

## What You Can Use Compare For
<a name="compare-uses"></a>

| Task | What you compare | What tells you the answer |
| --- | --- | --- |
| Pick the best take | Several clips or captures of the same shot | Play them in step, then read the quality attributes a connector recorded, such as sharpness, light level, motion, or quality flags |
| Check a derived file against its source | An original and a connector’s output, such as a LAS file and its COPC copy, a full and a decimated mesh, or a master and a proxy video | Linked views show any detail lost at the same spot, and the details table shows how the size changed, for example "3.2× smaller than the base" |
| Review a change before you approve it | Two versions of one file | What changed in the content and which attributes changed, before you mark the asset reviewed |
| Line up footage from several cameras | Clips from a multi-camera rig or several drones | Time offsets align the clips, and frame stepping finds the exact moment |
| See how a site changed | Surveys or orthophotos captured on different dates | Linked 3D views, or a swipe or overlay of two maps or two images |
| Check a capture run for problems | The captures from one session | Files that stand out in the details table, such as low light, scene cuts, or sparse keyframes, show what to capture again or leave out of a training set |

Compare opens in the file viewer. It needs the same access as the viewers: Consumers and above. For details, see [Who Can Open Files](view-your-content.md#view-who-can-open).

## Compare Versions of a File
<a name="compare-versions"></a>

Use this to see what changed between two versions of one file.

1. In the asset’s **Files** tab, select one file.

1. Choose **Compare versions**.

The comparison opens with the newest version and the version before it. Above the panes, a **Base** and a **Compare** picker choose the two versions, and a swap button between them exchanges the sides. A **Changes** panel lists what changed, such as the size and the file’s attributes, with the attributes that were added, changed, or removed first.

In the following example, version 1 of a 3D model is on the left and version 2 is on the right. Version 2 adds two ducks to the scene. When **Sync views** is on, the two panes stay at the same point in the model as you move around.

![Compare versions view of a 3D model with version 1 on the left showing one duck and version 2 on the right showing three ducks](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/compare-versions-3d.png)

 **Compare versions** is unavailable when the file has only one version. The newest version has no version label in the panes.

## Compare Different Files in an Asset
<a name="compare-different-files"></a>

Use this to compare a source file with something derived from it, two cameras, or two surveys of the same site.

1. In the asset’s **Files** tab, select two to six files that the Portal can open.

1. Choose **Compare files**.

Each file gets a pane and a letter, A to F. Two panes sit side by side, three sit in a row, four sit in two rows of two, and five or six sit in two rows of three.

In the following example, six clips of a robot pick-and-place task are compared. The panes play in step on one playback bar. The details table shows the 11 of 51 attributes that differ, judged against clip A, which is the base. The attributes that differ are **Size**, `bitrateKbps`, `brightnessMean`, `contrastMean`, `fileSizeBytes`, `longestStaticRunFrames`, `motionMean`, `motionP95`, `sharpnessMean`, `sharpnessP05`, and `staticFrameFraction`. For example, the mean motion is 0.199 in clip A and 0.246 in clip B. The robot arm in the clips is the SO-ARM101 model from NVIDIA’s [Sim-to-Real SO-101 Workshop](https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop) on the GitHub website, licensed [Apache 2.0](https://github.com/isaac-sim/Sim-to-Real-SO-101-Workshop/blob/main/LICENSE).

![Compare view with six video panes in two rows of three with a shared playback bar and a details table with one column for each clip](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/compare-six-clips.png)

+  **Change a pane’s file.** Each pane has a dropdown that lists the files in the asset. Files of the same kind are listed first. On a large asset that is only partly loaded, the dropdown searches the whole asset.
+  **Compare a folder with its files.** You can select a folder together with files to compare.
+  **Remove a pane.** Each pane has a remove button.
+  **Placeholders.** Empty panes hold the layout while files load, so one viewer does not start before the others.

### Details Table
<a name="compare-details-table"></a>

When you compare different files, a details table shows one column for each file.
+ Rows that differ come first. Rows that match are hidden until you show them.
+ Choose a column header to make that file the base. Every other column is judged against it.
+ For numbers, a column can show how it differs from the base, for example "27× the base" or "3.2× smaller than the base".

## Keep Views in Step
<a name="compare-sync"></a>

 **Sync views** links the panes. The setting is in the page address, so a link to a comparison opens it in the same state.

When views are linked, these follow each other:
+ 3D cameras for point clouds, tiled point clouds, PLY files, and models. The cameras move in the files' own coordinates.
+ Maps.
+ Images and panoramas.
+ Section planes.

View settings, such as point size or color mode, are shared too.

## Video and Image Sequences
<a name="compare-playback"></a>

Videos and image sequences in a comparison follow one clock.
+ One playback bar plays, pauses, and steps frame by frame for every pane.
+ Each pane can have a time offset, so you can line up videos that did not start together.
+ Each video is corrected to show the exact frame that the clock calls for.
+ In full screen, a linked video keeps its playback bar.

## Compare Maps and Images
<a name="compare-maps"></a>

Two maps, or two images, can be compared as a swipe or as an overlay. Choose **Swipe** to drag a divider across the two. Choose **Overlay** to fade one over the other. Any image can be compared this way, so you can see what changed between two photographs, two orthophotos, or two renders at the same spot.

## Compare Text Files
<a name="compare-text"></a>

Two text files, or two versions of one text file, line up row for row. Changed lines are tinted, and a gap on one side means that the other side has a line the first one does not.
+ The toolbar counts the changes, or the differences when you compare two different files. It says **No changes** or **Identical** when nothing differs.
+ Choose **Next change** and **Previous change**, or press `N` and `P`, to jump between them.
+ When two texts are too different to line up, the viewer says so and shows each one as it is.

## Play a Folder of Images as Video
<a name="compare-image-folders"></a>

A folder of images can play as video. This is useful for frames from a camera.
+ The folder must hold at least two images in a format the browser draws itself: PNG, JPEG, GIF, WebP, BMP, or AVIF.
+ Frames play in name order, with numbers read as numbers. `frame_9` plays before `frame_10`.
+ Use the playback bar to play, pause, and step frame by frame.
+ Any frame can be saved as a PNG.
