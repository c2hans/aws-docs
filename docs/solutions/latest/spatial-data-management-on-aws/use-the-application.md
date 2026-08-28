---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/use-the-application.html
---

# User guide
<a name="use-the-application"></a>

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
+ Search for assets using metadata or geospatial queries
+ View asset details and metadata

 **Consumers and above:**
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

## Learn more
<a name="learn-more"></a>

For detailed walkthroughs of solution functionality, see [Upload your first asset](upload-first-asset.md). This guide covers creating projects, uploading assets, managing metadata, and using key features.

## Get Help
<a name="get-help"></a>

If you need assistance:
+ Contact your Library Owner or administrator for permission-related issues
+ Refer to the in-app help documentation (choose the **?** icon in the portal)
+ For technical issues, contact your IT Administrator

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
