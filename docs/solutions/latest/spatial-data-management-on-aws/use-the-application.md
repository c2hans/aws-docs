---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/use-the-application.html
---

# User Guide

This section provides information about permissions, common tasks, and access methods for working with the solution.

## Understand Your Permissions
<a name="understand-your-permissions"></a>

Your ability to perform actions depends on the permission level assigned to you on a resource. For data resources, permissions are assigned at the Library or Project level. Connectors and Asset Templates under the Library are also controlled by permissions at the resource level.
+  **Owner** – You can create, update, delete resources, and manage access for other users
+  **Manager** – You can create, update resources, and manage access for other users
+  **Contributor** – You can create and update resources but cannot manage access
+  **Consumer** (Projects only) – You can view and download files but cannot create or modify resources
+  **Viewer** – You can only view resource metadata (read-only access, no file downloads on Projects)

To check your current permissions:

1. Navigate to the Library, Project, or Asset you want to access

1. Your permission level is displayed in the resource details or access management section

## Common User Tasks
<a name="common-user-tasks"></a>

Depending on your permission level, you can perform the following tasks:

 **All Users (Viewer and above):**
+ Browse the default library, projects, and assets you have access to
+ Explore projects, assets, and located files on a map
+ Search for assets using metadata or geospatial queries
+ View asset details and metadata

 **Consumers and above:**
+ Open files in the Portal’s viewers, compare files, and layer maps (see [View and inspect your content](view-your-content.md))
+ Download asset files

 **Contributors and above:**
+ Upload new assets
+ Update asset metadata
+ Create new projects (if you have permissions on the parent library)
+ Organize assets within projects

 **Managers and Owners:**
+ Assign permissions to other users
+ Create and modify asset templates
+ Configure connectors for external systems
+ Manage project settings and structure

## Access Methods
<a name="access-methods"></a>

You can interact with Spatial Data Management on AWS through multiple interfaces:

 **Web Portal (Browser):**
+ Best for: Browsing, searching, and one-off asset creation and uploads
+ Capabilities: Create and modify assets, upload files (up to 5,000 files per asset, 50 GB total, 20 GB per file, 3 simultaneous operations), and download files
+ Access: Use the portal URL provided by your administrator

 **Desktop Application:**
+ Best for: Routine or large-scale upload and download operations
+ Capabilities: Full file management plus all web portal features
+ Setup: See [Client setup](client-setup.md) for installation instructions

 **Command-Line Interface (CLI) and Python SDK:**
+ Best for: Automation, scripting, and batch operations
+ Capabilities: Programmatic access to all features
+ Setup: See [Client setup](client-setup.md) for installation instructions

 **API:**
+ Best for: Custom integrations and application development
+ Capabilities: Programmatic access to solution features
+ Access: Use the API endpoint from your deployment

## Learn More
<a name="learn-more"></a>

For detailed walkthroughs of solution functionality, see [Upload Your First Asset](upload-first-asset.md). This guide covers creating projects, uploading assets, managing metadata, and using key features.

To work with your content in the Spatial Data Portal, see:
+  [View and inspect your content](view-your-content.md) – Open point clouds, 3D models, maps, tables, images, and video in your browser, where they are stored.
  +  [Compare versions and files](compare-files.md) – Compare versions of a file, or different files in an asset.
  +  [Layer maps](layer-maps.md) – Show GeoTIFF, vector, and point cloud files together on one map.
+  [Edit assets in the Portal](edit-assets-in-the-portal.md) – Add, move, rename, and remove files, and save the changes as one version.
+  [Asset templates](asset-templates.md) – Set the rules that assets of one kind follow.

## Get Help
<a name="get-help"></a>

If you need assistance:
+ Contact your Library Owner or administrator for permission-related issues
+ Refer to the in-app help documentation (choose the **?** icon in the portal)
+ For technical issues, contact your IT Administrator
