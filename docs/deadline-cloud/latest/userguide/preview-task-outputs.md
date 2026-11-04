---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/preview-task-outputs.html
---

# Preview task outputs in the job monitor
<a name="preview-task-outputs"></a>

The **Task outputs** panel shows the output files of the task that you select in the **Tasks** list. The panel previews images, text, video, audio, 3D meshes, and point clouds, so you can check what a task produced without downloading its files or leaving the job monitor.

**To preview the outputs of a task**

1. Follow the steps in [View and manage job details in Deadline Cloud](view-a-job.md) to view a list of jobs.

1. Choose the **Add panel** tile that follows the last panel on the page. In **Add a panel**, choose **Task outputs**. You only need to add the panel once. For more information, see [Customize the panels in the job monitor](customize-job-monitor-panels.md).

1. Select a job in the **Jobs** list, a step in the **Steps** list, and a task in the **Tasks** list. The panel lists the output files of the task and previews the first image or video. If the task has no image or video output, the panel opens the first file.

1. (Optional) To preview a different file, choose it in the **Files** tree.

The panel shows a message instead of files in the following cases:
+ **No task selected** appears until you select a task in the **Tasks** list.
+ **Multiple jobs selected**, **Multiple steps selected**, or **Multiple tasks selected** appears when you select more than one job, step, or task. The panel previews the outputs of one task at a time.
+ **No outputs** appears when the task hasn't uploaded any output files yet.

## Browsing and saving output files
<a name="preview-task-outputs-browse"></a>

The panel shows the **Files** tree on the left and a preview of the selected file on the right. To give the preview more room, choose the **Hide file tree** icon in the upper left of the panel. To show the tree again, choose **Show file tree**.

From the panel, you can do the following:
+ To step through the files in the order of the tree, choose **Previous preview** or **Next preview** under the preview. Between the two buttons, the panel shows the position of the file in the list, such as **4 of 6**. You can also select the preview and press the left arrow or right arrow key. The buttons and keys also stop at files that can't be previewed, such as EXR images. For these files, the panel shows the file name and a message that a preview isn't available.
+ To save the selected file, choose the download icon next to the file name.
+ To save all of the task's output files, choose **Download all outputs** in the panel header.
+ To open the task's outputs in the attachments browser in a new browser tab, choose **Open in full view** in the panel header. The attachments browser adds filtering, file details, and a full-screen preview. For more information, see [Browsing job attachments in Deadline Cloud](browse-job-attachments.md).

## Viewing 3D meshes and point clouds
<a name="preview-task-outputs-3d"></a>

The panel previews meshes and point clouds in GLB, glTF, OBJ, STL, PLY, and PCD format, and USD scenes in USDZ format. In the 3D view, drag to orbit, scroll to zoom, and right-drag to pan.

In the following image, the panel previews an OBJ file of a cube. The **Files** tree and the **Properties** panel are on the left, and the 3D view is on the right. The zoom, **Reset view**, **Save snapshot as PNG**, download, and **View settings** controls are in a row at the top of the panel, next to the file name.

![The zoom, Reset view, snapshot, download, and View settings controls appear at the top of the panel, next to the file name.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-task-outputs-mesh.png)

For GLB, glTF, OBJ, STL, PLY, and PCD files, the following controls next to the file name act on the view:
+ **Zoom out** and **Zoom in** change the zoom level, which is shown between the two buttons. To reset the zoom to 100%, choose the zoom level.
+ **Reset view** fits the content to the view again.
+ **Save snapshot as PNG** saves the current view as a PNG image with the same name as the file.

To change how the file is drawn, choose the **View settings** icon. The settings that appear depend on whether the file contains a mesh or a point cloud. A PLY file can contain either one, so the panel checks the file's contents instead of its extension. The settings stay in effect as you step between the files of the selected task.

The following table lists the view settings and the files that each one applies to.

| Setting | Applies to | Description |
| --- | --- | --- |
| Show wireframe | Meshes | Draws surfaces as the edges of their triangles. |
| Point size | Point clouds | Scales the size of each point, from 0.25 to 4 times the size that the monitor chooses for the point cloud. |
| Up axis | Point clouds | Sets the axis of the file that points up: Y up, Y down, or Z up. Mesh formats define their own up axis. |
| Background | Meshes and point clouds | Sets the color behind the content. To return to the default color, choose Reset to default. |
| Show grid | Meshes and point clouds | Draws a floor grid under the content. |
| Show axes | Meshes and point clouds | Draws the X, Y, and Z axes of the file through the content. |

USDZ files open in the 3D view without the zoom, **Reset view**, snapshot, and view settings controls. Under the view, the panel shows the scene's up axis, its meters per unit, and the number of prims in the scene.

If a file is too large to preview, or the monitor can't read it, the panel shows a message in place of the view. To open the file in other software, save it with the download icon.

## Viewing the properties of a mesh or point cloud
<a name="preview-task-outputs-properties"></a>

When you preview a GLB, glTF, OBJ, STL, PLY, or PCD file, the **Properties** panel under the **Files** tree describes the file. The panel shows the following properties:
+ **Format**: the file format, such as **Wavefront OBJ** or **Point Cloud Data**.
+ **Objects**: the number of objects in the file.
+ **Vertices**: the number of vertices. Shown for meshes only.
+ **Triangles**: the number of triangles. Shown when the file contains triangles.
+ **Points**: the number of points. Shown when the file contains a point cloud.
+ **Materials**: the number of materials.
+ **Vertex colors**: **Yes** when the file stores a color for each vertex or point.
+ **Animations**: the number of animations. Shown when the file contains animations.

In the following image, the panel previews a PLY point cloud. The **Files** tree is on the left with the **Properties** panel under it, and the point cloud is in the 3D view on the right. The **Properties** panel lists each property name with its value next to it: **Format** is PLY, **Objects** is 1, **Points** is 240, **Materials** is 1, and **Vertex colors** is **Yes**.

![The Properties panel lists a PLY format, 1 object, 240 points, 1 material, and vertex colors.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-task-outputs-point-cloud.png)

When you hide the file tree, the **Properties** panel is hidden too. Under the view, the panel then shows the number of triangles and objects in a mesh, or the number of points in a point cloud.

The full-screen preview in the attachments browser also shows the **Properties** panel, next to the view. For more information, see [Previewing files](browse-job-attachments.md#browse-job-attachments-preview).
