---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/solution-overview.html
---

# Spatial Data Management on AWS

Spatial Data Management on AWS (SDMA) stores, views, governs, and processes spatial, 2D, and 3D content in your own AWS account. That content includes point clouds, 3D models and scenes, computer-aided design (CAD) and building information modeling (BIM) files, Gaussian splats, maps, imagery, and video. SDMA connects it to the applications, processing jobs, and models you already use, and records what each one did.

## What Is Spatial Data Management on AWS?
<a name="what-is-spatial-data-management-on-aws"></a>

Managing spatial data at scale presents significant challenges due to storage, compute, and security requirements. With costly data acquisition and creation, organizations need robust processes to track, integrate, and leverage spatial assets across use cases. Spatial Data Management on AWS provides a comprehensive solution to store, manage, and connect your spatial data as a single source of truth. Deploy the solution in your AWS account and use the pre-built client application to improve efficiency of your spatial workflows.

Each dataset, such as a LiDAR survey, a site model, or a capture session, is an asset: a versioned, permissioned record of its files and metadata. Previews, converted formats, model outputs, and measurements are added to the version they came from, so you can always tell what was made from what. Connectors link assets to the applications, processing jobs, and models you already use, through configuration that an administrator approves for each asset type.

You can work with SDMA in four ways:

| Interface | Best for |
| --- | --- |
|  **Spatial Data Portal**  | A web application for browsing, searching, and viewing content in the browser, editing attributes, and managing templates, connectors, and access. See [Use the Solution](use-the-solution.md). |
|  **Desktop application**  | Everything the Spatial Data Portal does, plus uploading and downloading large captures and whole folders on Windows, macOS, and Linux. See [Client setup](client-setup.md). |
|  **CLI and Python SDK**  | Scripts, bulk operations, and automation. See [Client setup](client-setup.md). |
|  **REST API**  | Custom applications and integrations. See [API Reference](api-reference.md). |

 **Topics**
+  [One Governed Record for Spatial Content](governed-hub.md)
+  [Example: From Captured Data to a Deployed Model](capture-to-model-workflow.md)
+  [Benefits](benefits.md)
+  [Use Cases](use-cases.md)
+  [Architecture Overview](architecture-overview.md)
+  [Core Concepts](core-concepts.md)
+  [Plan Your Deployment](plan-your-deployment.md)
+  [Deploy the Solution](deploy-the-solution.md)
