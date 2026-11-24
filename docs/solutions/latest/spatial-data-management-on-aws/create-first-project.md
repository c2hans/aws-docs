---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/create-first-project.html
---

# Create Your First Project

Projects organize related assets within the library. Create a project before uploading assets.

<a name="projects-page"></a>The **Projects** page lists the projects that you can see:
+  **Browse projects** shows each project as a card, with its name, description, number of assets, size, and when it was last opened. Use the grid and list buttons to change the layout, and **Sort by** to change the order.
+  **Explore map** shows the projects that have a location on a map.
+ The search box finds projects. It also takes you to other pages, so you can type the name of anything you want to open.
+  **Create** starts a new project.

  1. Launch the Spatial Data Management desktop application

  1. Sign in with your Library Owner or Contributor credentials

  1. From the sidebar, open **Projects**

  1. On the **Projects** page, choose **Create**

  1. On **Define your project** (step 1 of 3), leave **Create a brand new project** selected, and enter the project details:
     +  **Project name** – Enter a descriptive name (for example, `Site Survey 2026`)
     +  **Description** (optional) – Provide context about the project purpose
     +  **Thumbnail** (optional) – Choose an image in PNG, JPEG, JPG, WebP, or AVIF format, smaller than 10 MB
     +  **Location** (optional) – Choose **This project has a specific geographic location** to enable map-based discovery. Search for a place or enter latitude and longitude, and move the marker on the map to refine the position. You can also choose **This project has no geographic location** or **This project has a geometry**

  1. Choose **Next**.

  1. On **Configure your project’s content** (step 2 of 3), choose what the project can use. You can leave both lists empty. If you are creating your first project, there may be no connectors or asset templates yet, and you can add them later:
     +  **Connections** – Under **Use**, select the connectors that the project integrates with, to derive or publish content. Use **Find connectors** to search the list. For more information, see [Connectors](connectors.md).
     +  **Asset templates** – Choose the asset templates that the project permits. If you select a connector, also choose at least one template that supports it. **Allow assets that don’t use any template** controls whether assets in the project can skip a template. For more information, see [Asset templates](asset-templates.md).

  1. Choose **Next**.

  1. On **Review and create your project** (step 3 of 3), check the project details, location, and attributes. Choose **Edit** to go back and change them.

  1. Choose **Create project**.

Your project is now ready to receive assets.

![Create project wizard step 1 of 3: Define your project](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/create-project-define-step.png)
