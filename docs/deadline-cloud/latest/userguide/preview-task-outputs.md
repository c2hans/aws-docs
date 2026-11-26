---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/preview-task-outputs.html
---

# Preview task outputs in the job monitor

The **Task outputs** panel shows the output files of the task that you select in the **Tasks** list. The panel previews images, text, tables, logs, video, audio, and 3D files, so you can check what a task produced without downloading its files or leaving the job monitor.

To try the panel with sample data, open the [demo compositing job](https://_demo.us-east-1.deadlinecloud.amazonaws.com/us-west-2/farms/farm-94d29d9475dd814529b87a52f20ff9cb/queues/queue-b5fb7c92ae42326d3851bab4b0568d97?jobId=job-1cf313e2991e74375006ea6092c5a2ed&stepId=step-ed81a8594ee0f700b2f915af2582cc26&taskId=task-ed81a8594ee0f700b2f915af2582cc26-0&demo=moonrise), and then add the **Task outputs** panel.

**To preview the outputs of a task**

1. Follow the steps in [View and manage job details in Deadline Cloud](view-a-job.md) to view a list of jobs.

1. Choose the **Add panel** tile that follows the last panel on the page. In **Add a panel**, choose **Task outputs**. You only need to add the panel once. For more information, see [Customize the panels in the job monitor](customize-job-monitor-panels.md).

1. Select a job in the **Jobs** list, a step in the **Steps** list, and a task in the **Tasks** list. The panel previews the first image or video among the output files of the task. If the task has no image or video output, the panel opens the first file.

1. (Optional) To preview a different file, choose **Show file tree**, and then select the file in the **Files** tree. You can also choose **Next preview** under the preview.

The panel shows a message instead of files in the following cases:
+ **No task selected** appears until you select a task in the **Tasks** list.
+ **Multiple jobs selected**, **Multiple steps selected**, or **Multiple tasks selected** appears when you select more than one job, step, or task. The panel previews the outputs of one task at a time.
+ **No outputs** appears when the task hasn't uploaded any output files yet.

## Browsing and saving output files
<a name="preview-task-outputs-browse"></a>

The panel shows a preview of the selected file. The **Files** tree is hidden when the panel opens. To show the tree on the left of the preview, choose the **Show file tree** icon in the upper left of the panel. To give the preview more room again, choose **Hide file tree**.

For a mesh, a point cloud, or a robot description in Unified Robot Description Format (URDF), a **Properties** panel appears under the **Files** tree. At most one of the two is open at a time, so that the open one has the height of the column. To open the other one, choose its heading. When you choose a file in the tree, the tree stays open. Hiding the file tree also hides the **Properties** panel.

From the panel, you can do the following:
+ To step through the files in the order of the tree, choose **Previous preview** or **Next preview** under the preview. Between the two buttons, the panel shows the position of the file in the list, such as **4 of 6**. You can also select the preview and press the left arrow or right arrow key. The buttons and keys also stop at files that can't be previewed, such as EXR images. For these files, the panel shows the file name and a message that a preview isn't available. A video or audio file that your browser can't play shows a similar message.
+ To save the selected file, choose the download icon next to the file name.
+ To save all of the task's output files, choose **Download all outputs** in the panel header.
+ To open the task's outputs in the attachments browser, choose **Open in full view** in the panel header. In a browser, the attachments browser opens in a new tab. In the Deadline Cloud monitor desktop application, it opens in the application. The attachments browser adds filtering, file details, and a full-screen preview. For more information, see [Browsing job attachments in Deadline Cloud](browse-job-attachments.md).

## Viewing 3D meshes and point clouds
<a name="preview-task-outputs-3d"></a>

The panel previews meshes and point clouds in GLB, glTF, OBJ, STL, PLY, and PCD format, and Universal Scene Description (USD) scenes in USD, USDA, USDC, and USDZ format. It also previews robot descriptions in URDF format. For more information about URDF files, see [Viewing and posing a URDF robot](#preview-task-outputs-urdf).

In the following image, the panel previews an OBJ file of a cube. The **Files** tree is open on the left, with the closed **Properties** panel under it, and the 3D view is on the right. The zoom, **Reset view**, **Save snapshot as PNG**, download, **Show controls**, and **View settings** controls are in a row at the top of the panel, next to the file name. The axis indicator is in the lower-right corner of the 3D view.

![Cube previewed in the Task outputs panel, with the Files tree open and the view controls next to the file name.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-task-outputs-mesh.png)

The buttons next to the file name zoom the view and fit the content to the view again. They also save the current view as a PNG image and list the mouse controls. The axis indicator in the 3D view shows the X, Y, and Z axes of the file as the camera sees them.

To change how the file is drawn, choose the **View settings** icon. The settings that appear depend on whether the file contains a mesh, a point cloud, or a USD scene. A PLY file can contain either one, so the panel checks the file's contents instead of its extension. The settings stay in effect as you step between the files of the selected task.

The following table lists the view settings and the files that each one applies to.

| Setting | Applies to | Description |
| --- | --- | --- |
| Show wireframe | Meshes and USD scenes | Draws surfaces as the edges of their triangles. |
| Ambient light | Meshes and USD scenes | Sets the strength of the light that reaches every surface evenly. |
| Directional light | Meshes and USD scenes | Sets the strength of the light that shines from one direction and shades the surfaces. |
| Light direction | Meshes and USD scenes | Turns the directional light around the vertical axis. |
| Point size | Point clouds | Scales the size of each point. |
| Up axis | Point clouds | Sets which axis of the file points up. Mesh formats define their own up axis. |
| Background | Meshes, point clouds, and USD scenes | Sets the color behind the content. To return to the default color, choose Reset to default. |
| Show grid | Meshes, point clouds, and USD scenes | Draws a floor grid under the content. |
| Show axes | Meshes, point clouds, and USD scenes | Draws the X, Y, and Z axes of the file through the content. |
| Show bounding box | Meshes, point clouds, and USD scenes | Draws a box around the whole model. |

USD scenes have the same view buttons and settings, except **Point size** and **Up axis**, because a USD scene sets its own up axis. They do not have the axis indicator or the **Show controls** icon.

Under the view, the panel shows the scene's up axis, its meters per unit, and the number of prims in the scene.

A USD, USDA, or USDC file shows only the geometry that it defines itself. The files that it refers to are not part of the attachment. When the file refers to other files, the panel says so: it shows **Showing this file only** under the view, or, when the file has no geometry of its own, it shows a message in place of the view.

If a file is too large to preview, or the monitor can't read it, the panel shows a message in place of the view. To open the file in other software, save it with the download icon.

## Viewing the properties of a mesh or point cloud
<a name="preview-task-outputs-properties"></a>

When you preview a GLB, glTF, OBJ, STL, PLY, or PCD file, the **Properties** panel under the **Files** tree describes the file. To open it, choose **Properties**. If the file tree is hidden, first choose **Show file tree**. The **Files** tree closes while the panel is open. To return to the tree, choose **Files**. The panel shows the following properties:
+ **Format**: the file format, such as **Wavefront OBJ** or **Point Cloud Data**.
+ **Objects**: the number of objects in the file.
+ **Vertices**: the number of vertices. Shown for meshes only.
+ **Triangles**: the number of triangles. Shown when the file contains triangles.
+ **Points**: the number of points. Shown when the file contains a point cloud.
+ **Size (X × Y × Z)**: the size of the model along each axis. Shown when the model has a size.
+ **Materials**: the number of materials.
+ **Vertex colors**: **Yes** when the file stores a color for each vertex or point.
+ **Animations**: the number of animations. Shown when the file contains animations.

In the following image, the panel previews a PLY point cloud. The **Properties** panel is open on the left, under the closed **Files** tree, and the point cloud is in the 3D view on the right. The **Properties** panel lists each property name with its value next to it: **Format** is PLY, **Objects** is 1, **Points** is 240, **Size (X × Y × Z)** is 2.7 × 0.7 × 2.7, **Materials** is 1, and **Vertex colors** is **Yes**.

![A PLY point cloud in the Task outputs panel. The Properties panel lists a PLY format, 1 object, 240 points, a size of 2.7 by 0.7 by 2.7, 1 material, and vertex colors.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-task-outputs-point-cloud.png)

When you hide the file tree, the **Properties** panel is hidden too. Under the view, the panel then shows the number of triangles and objects in a mesh, or the number of points in a point cloud.

The full-screen preview in the attachments browser also shows the **Properties** panel, next to the view. For more information, see [Previewing files](browse-job-attachments.md#browse-job-attachments-preview).

## Viewing and posing a URDF robot
<a name="preview-task-outputs-urdf"></a>

The **Task outputs** panel previews robot descriptions in Unified Robot Description Format (URDF). Use the preview to check a robot that a job produced, and how its joints move, without downloading its files. The panel draws each link of the robot from the visual geometry in the file. That geometry includes the boxes, cylinders, and spheres that the file defines, and the STL, OBJ, and PLY meshes that the file refers to. The panel doesn't draw collision geometry. The robot starts in its rest pose, the pose that the file defines.

To try the URDF preview with sample data, open the [demo compositing job](https://_demo.us-east-1.deadlinecloud.amazonaws.com/us-west-2/farms/farm-94d29d9475dd814529b87a52f20ff9cb/queues/queue-b5fb7c92ae42326d3851bab4b0568d97?jobId=job-1cf313e2991e74375006ea6092c5a2ed&stepId=step-ed81a8594ee0f700b2f915af2582cc26&taskId=task-ed81a8594ee0f700b2f915af2582cc26-0&demo=moonrise), add the **Task outputs** panel, show the file tree, and choose `rover.urdf`.

The panel looks for each mesh among the task's outputs, under the same root folder as the URDF file. A relative path is resolved from the folder of the URDF file, and a `package://` path is resolved to a folder with that package name. When a mesh isn't among the task's outputs, the panel also looks in the job's input files under the same root folder. The panel doesn't read URLs, absolute paths, or paths that lead outside the root folder.

When the panel can't draw every mesh, the **Properties** panel shows **Showing {{found}} of {{total}} meshes** and the reasons, with how many meshes each one affects. For example, a mesh might not be in the job's attachments, or it might be in a format that the panel doesn't draw, such as Collada (DAE). When the file tree is hidden, the notice appears under the view instead. To see the notice while the file tree is open, choose **Properties**. To show every mesh, add the meshes to the job's attachments as STL, OBJ, or PLY files. To open the robot in other software, save it with the download icon.

For a URDF file, the **Properties** panel adds the following properties to the properties of a mesh:
+ **Robot**: the name of the robot. Shown when the file names the robot.
+ **Links**: the number of links.
+ **Joints**: the number of joints.
+ **Meshes**: the number of meshes that the panel drew out of the meshes that the file refers to, such as **3 of 3**. Shown when the file refers to meshes.

To check how the robot moves, pose its joints in the **Joint positions** panel. Posing the robot doesn't change the file.

**To pose a robot**

1. In the **Files** tree, select a URDF file. If the tree is hidden, first choose **Show file tree**.

1. In the row of buttons next to the file name, choose the **Joint positions** icon. The **Joint positions** panel opens over the 3D view, with one row for each joint that you can move.

1. In the row of a joint, drag its slider or enter a value in its box to move the joint. Revolute and continuous joints turn in degrees, and prismatic joints slide in meters. The label of each joint shows its unit, such as **shoulder (°)**.

1. (Optional) To see what a joint moves, point to its row or select its box. The 3D view outlines the links that the joint carries.

1. (Optional) To return a joint to its rest position, choose the reset icon in its row. To return every joint, choose **Reset pose**.

In the following image, the file tree is hidden and the **Joint positions** panel is open on the left of the 3D view of a rover. The shoulder joint is at 60 degrees and the pan joint at -45 degrees. The shoulder joint's box has focus, so the 3D view outlines the arm that the shoulder joint moves.

![Rover in the Task outputs panel, posed in the Joint positions panel, with its arm outlined.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-task-outputs-urdf.png)

Each slider covers the limits that the file sets for its joint, and always includes zero. A continuous joint, and a revolute joint without a `limit` element, turn a full circle. A prismatic joint without usable limits has no slider. A joint that mimics another joint usually has no slider of its own and moves with the joint that it follows. Fixed, floating, and planar joints don't have a slider. When a robot has more than 10 joints that you can move, enter part of a joint name in **Find joints** to list only the matching joints.

The **Joint positions** panel stays open while you turn the view and as you step between files. To move the panel out of the way, choose **Move panel to the other side**, or drag it by its handle. To close the panel, choose the close icon or press Esc.

The **Task outputs** panel previews URDF files of up to 8 MB. It draws up to 256 mesh files, with up to 64 MB of meshes in all. When a robot refers to more, the panel draws the meshes that fit and lists the rest as left out. When a robot has more than 2,000 links, or more geometry than the panel can draw, the panel shows a message in place of the view.

## Viewing data and log files
<a name="preview-task-outputs-data"></a>

The panel opens the following data and log files in viewers of their own:
+ CSV, TSV, and JSON Lines (JSONL and NDJSON) files appear as a table. The table shows the first rows and columns of the file. To read the file as plain text instead, choose **Text** for **View** in the view settings. For a JSON Lines file, a message at the top of the preview lists the lines that aren't valid JSON, and the table leaves those lines out.
+ Parquet files appear as a table of the first rows, with the data type of each column under its name. The full-screen preview also lists the schema of the file and the software that wrote it.
+ JSON files appear as formatted text. To explore the file as an expandable tree, choose **Tree** for **View** in the view settings. If the file isn't valid JSON, the panel shows the raw text and the line and column where parsing stopped.
+ YAML files appear with highlighting. If the file has a syntax error, the panel shows the line and column of the first error.
+ Log files appear with line numbers, and errors and warnings are colored. To show only the lines with errors and warnings, turn on **Show errors and warnings only** in the view settings. A very large log shows its first and last lines, and the panel says how many lines it leaves out.

If a file is larger than the viewer can read, the panel shows the start of the file, or a message that the file is too large to preview, and suggests that you save the file to view all of it.
