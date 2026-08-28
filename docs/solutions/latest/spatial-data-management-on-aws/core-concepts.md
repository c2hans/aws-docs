---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/core-concepts.html
---

# Core Concepts
<a name="core-concepts"></a>

This section introduces the fundamental concepts of the Spatial Data Management on AWS solution, explaining what the solution does and how resources are organized.

## What is Spatial Data Management on AWS?
<a name="what-is-spatial-data-management-on-aws"></a>

Spatial Data Management on AWS is a solution for managing large-scale spatial data assets such as point clouds, 3D models, and geospatial imagery. It provides:
+  **Centralized Storage** – Secure storage and organization of spatial data in Amazon Simple Storage Service (Amazon S3)
+  **Metadata Management** – Rich metadata and search capabilities for spatial assets
+  **Access Control** – Fine-grained permissions for users and teams
+  **Integration** – Connectors for external systems and workflows
+  **Versioning** – Complete version history for all assets

## Resource Model
<a name="resource-model"></a>

The Spatial Data Management on AWS solution organizes resources in a hierarchical structure:

![Resource model diagram](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/resource-hierarchy.svg)

## Key Resources
<a name="key-resources"></a>

The solution uses the following resource types:

 **Libraries**

Libraries provide secure boundaries and permission management for managing primary resources — Projects, Asset templates, and Connectors — which in turn help manage Assets. Each library defines S3 configuration and serves as a top-level organizational container for related spatial data.

 **Projects**

Projects logically group related assets and serve as the primary permission boundary. Each project can use configurable templates to enforce consistent metadata and structure across its assets.

 **Assets**

Assets are versioned collections of files and folders that represent a logical unit of spatial data. Each asset includes a manifest defining its structure and metadata.

 **Asset Templates**

Asset templates define structure requirements using JSON Schema validation, ensuring consistent organization of files and metadata. Templates also control which connectors can interact with assets of a specific type.

 **Files**

Files represent individual data items stored using content-addressable storage, enabling automatic deduplication across versions and assets. Each file maintains its own metadata while being efficiently shared across the system.

 **Connectors**

Connectors enable configuration-driven integration between the solution and external systems. They support multiple integration patterns including Content Derivers, Publishers, and Bi-directional synchronization.

## Next Steps
<a name="_next-steps"></a>

Now that you understand the core concepts, you can proceed with deploying and configuring the solution:
+  [Plan your deployment](plan-your-deployment.md) – Review deployment considerations and prerequisites
+  [Deploy the solution](deploy-the-solution.md) – Deploy the solution to your AWS account

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
