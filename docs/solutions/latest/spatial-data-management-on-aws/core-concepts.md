---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/core-concepts.html
---

# Core Concepts

This section introduces the fundamental concepts of the Spatial Data Management on AWS solution, explaining what the solution does and how resources are organized.

## What Is Spatial Data Management on AWS?
<a name="what-is-spatial-data-management-on-aws"></a>

Spatial Data Management on AWS is a solution for managing large-scale spatial data assets such as point clouds, 3D models, and geospatial imagery. It provides:
+  **Versioned assets** – Each dataset is an asset with a complete version history. Metadata and derived files are recorded on the version they describe.
+  **Lineage** – Derived files and assets record what they were made from.
+  **Metadata Management** – Rich metadata, validated by asset templates, with full-text and geospatial search
+  **Access Control** – Fine-grained permissions for users and teams
+  **Governed integration** – Connectors, configured rather than coded, and approved for each asset template

## Why Each Resource Exists
<a name="why-each-resource"></a>

SDMA keeps one governed record at the center of your work. The tools and services around it read from the asset record and write their results back to it. For the reasoning, see [One Governed Record for Spatial Content](governed-hub.md). The following table starts from what you want to do.

| You want to | Use | Why |
| --- | --- | --- |
| Keep a dataset’s files, metadata, derived content, and history together | An **asset**  | The asset is the unit of record. Every change is a new version, so a result stays with the data it came from. |
| Make every capture declare the same attributes, use the same folders, and hold only the right file types | An **asset template**  | A template is a contract. Anything that reads the asset, such as a person, a script, or a training job, can rely on it. |
| Decide who can see, change, or download content |  **Projects** and permission levels | The project is the permission boundary for its assets. |
| Transform files, run a model, enrich metadata, or publish to another application or system | A **connector**  | A connector declares the external work as configuration. It is approved for each kind of asset, and every run is recorded. |
| Check content before you use it | The **viewers**  | You can inspect, compare, and layer content in the browser. For many formats, the Portal reads only what is on screen. |
| Know what made a result |  **Provenance and run records**  | Derived files and new assets record what they came from. Each run records the connector version, parameters, and attribute values that it wrote. |

A connector acts on a resource only after three approvals. The library defines and approves the connector, a template lists it, and a project uses the template. Default connectors are the exception. They need only the library’s approval, because they reach only resources that SDMA deploys: its AWS Deadline Cloud farm and Amazon OpenSearch Serverless.

Each level belongs to a different group of people, so the people who define integrations, asset standards, and projects each control their own part.

## Resource Model
<a name="resource-model"></a>

The Spatial Data Management on AWS solution organizes resources in a hierarchical structure:

![Resource model diagram](https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/resource-hierarchy.svg)

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

Asset templates define structure requirements using JSON Schema validation, ensuring consistent organization of files and metadata. Templates also control which connectors can interact with assets of a specific type. For more information, see [Asset templates](asset-templates.md).

 **Files**

Files represent individual data items stored using content-addressable storage, enabling automatic deduplication across versions and assets. Each file maintains its own metadata while being efficiently shared across the system.

 **Connectors**

Connectors integrate SDMA with external systems through configuration rather than code. A connector can publish content outward, derive content and metadata inward, or do both.

A single connector can run a multi-step workflow. Its steps call REST APIs, AWS Lambda functions, AWS Deadline Cloud jobs, Amazon S3, and Amazon EventBridge in sequence, and pass values from one step to the next. For example, one connector can start a model training job, wait hours for it to finish without holding compute, and register the trained model as a new asset with its evaluation results. Steps can also run once for each file in an asset, so one connector can send every file to an external system and turn each result into an asset of its own.

Connectors act on assets, not on storage. An asset is a versioned, template-validated, permissioned record. It represents content in SDMA’s content store.

A connector reads asset versions and writes its results back as new versions, metadata, derived files, and new assets. Each result is traceable to the run that produced it. Every change to an asset is a lifecycle event, so connectors also compose through the asset record: one connector’s output is another’s trigger. For more information about connectors, see [Connectors](connectors.md).

## Next Steps
<a name="_next-steps"></a>

Now that you understand the core concepts, you can proceed with deploying and configuring the solution:
+  [Plan Your Deployment](plan-your-deployment.md) – Review deployment considerations and prerequisites
+  [Deploy the Solution](deploy-the-solution.md) – Deploy the solution to your AWS account
