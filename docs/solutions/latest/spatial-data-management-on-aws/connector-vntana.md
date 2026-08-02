---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-vntana.html
---

# Integrating with VNTANA for 3D optimization
<a name="connector-vntana"></a>

 [VNTANA](https://aws.amazon.com/marketplace/pp/prodview-ooio3bidshgy4), available on AWS Marketplace, provides automated 3D model optimization — converting CAD files into web-ready formats like glTF/GLB, USDZ, FBX, and generating thumbnails, all through a containerized processing pipeline. The VNTANA connector for SDMA brings this capability directly into your governed asset workflow. The connector uses SDMA’s [connector framework](connectors.md) and runs processing jobs through [AWS Deadline Cloud](connector-deadline-cloud.md).

When a CAD file (`.zip`, `.stp`, `.stl`, or other supported formats) is uploaded to an asset, the VNTANA connector automatically submits a processing job through Deadline Cloud. VNTANA’s optimization engine runs in an ECS container controlled by Deadline Cloud workers, converts the source CAD into multiple output formats, and writes the results back as derived files on the asset — with previews, thumbnails, and format variants all governed, versioned, and traceable to the job that produced them.

This means a template author can define once that "all CAD uploads in this project get optimized by VNTANA" — and every asset created under that template gets web-ready 3D previews, format conversions, and thumbnails automatically from the moment of ingestion. No manual processing, no separate tools, no ungoverned side channels.

## How it works
<a name="vntana-how-it-works"></a>

The VNTANA connector uses a Deadline-to-ECS bridge pattern:

1. SDMA fires the connector when a matching file is uploaded.

1. The connector submits a Deadline Cloud job that launches a VNTANA container as an ECS task.

1. The VNTANA container reads the source CAD file, runs optimization and conversion, and writes output files (`.glb`, `.usdz`, `.fbx`, `.png`, `.html`) to the job’s output directory.

1. Deadline Cloud uploads the outputs to S3 and SDMA ingests the declared output files as derived files on the asset.

1. GLB and other preview-capable formats are marked as previews, making them immediately viewable in the Spatial Data Portal.

## Setup and installation
<a name="vntana-setup"></a>

VNTANA provides an open-source CDK package that deploys the ECS infrastructure, staging buckets, and connector configuration into your SDMA account. The full installation guide — including IAM role setup, stack deployment, connector registration, and template wiring — is available at:

 [VNTANA Connector Quickstart Guide](https://github.com/VNTANA-3D/modelops-cdk/blob/main/docs/install/quickstart.md)

The quickstart covers:
+ Gathering your SDMA deployment values (farm ID, queue ID, VPC, bucket ARNs).
+ Deploying the VNTANA CDK stack with the ECS task definition and Deadline Cloud queue integration.
+ Registering the connector in SDMA and wiring it to an asset template.
+ Verifying end-to-end by uploading a CAD file and watching the job complete.

## What the connector looks like
<a name="vntana-connector-shape"></a>

The VNTANA quickstart generates the connector configuration automatically. You do not need to write it by hand. The generated connector has the following shape:
+  **Direction:** `derive` — content flows inward from VNTANA’s processing pipeline back into SDMA.
+  **Connector type:** Deadline Cloud — jobs are submitted to your SDMA-managed Deadline Cloud farm.
+  **One trigger per input format** — for example, `.zip` for zipped CAD assemblies, `.stl` and `.stp`/`.step` for individual CAD files. Each trigger fires on `upload` and `onDemand` events.
+  **Output declarations** — each trigger declares `derivedFiles` filters for the output formats VNTANA produces: `.glb`, `.usdz`, `.fbx`, `.zip` (re-packaged archive), `.png` (thumbnail), and `.html` (viewer).
+  **ECS bridge parameters** — the Deadline job template launches a VNTANA container as an ECS task, passing cluster ARN, task definition, subnets, security groups, and the pipeline configuration as job parameters.

The connector produces multiple derived files from a single upload — GLB as the primary web-ready 3D format, plus USDZ, FBX, PNG, and HTML as additional format variants and previews. All outputs are governed through the same template chain and traceable to the VNTANA processing job that produced them.
