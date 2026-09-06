---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-deadline-cloud.html
---

# Create and transform content with AWS Deadline Cloud
<a name="connector-deadline-cloud"></a>

The AWS Deadline Cloud connector submits compute jobs to [AWS Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/what-is-deadline-cloud.html).

Use this connector when your assets need real compute power. Deadline Cloud jobs run on managed compute with access to GPUs, large local disks, and the third-party or licensed software your workflows depend on. Examples include CAD converters, point cloud processors, rendering engines, geospatial analysis tools, and AI/ML inference models. Format conversion, 3D rendering, spatial tiling, quality analysis, metadata extraction, and custom processing pipelines all run asynchronously at whatever scale Deadline Cloud provides. The results come back into SDMA as governed derived files and metadata with full provenance.

You define jobs using [Open Job Description](https://github.com/OpenJobDescription/openjd-specifications), an open specification for portable batch processing jobs. You write a job template that describes what to run. SDMA submits it to Deadline Cloud with the right parameters and file attachments, and Deadline Cloud executes it in an isolated compute environment.

SDMA acts as an orchestrator and ingestion endpoint. It submits job configuration to Deadline Cloud, observes job lifecycle events, and ingests declared allow listed outputs back into the governed asset content. All job execution occurs within Deadline Cloud’s isolated compute environment — SDMA does not execute customer code.

The Deadline Cloud connector uses the `deadlineJob` step type. Unlike other step types that execute synchronously within the connector invocation, `deadlineJob` steps are asynchronous. SDMA submits the job and then receives completion notifications through EventBridge lifecycle events.

**Important**
Deadline Cloud connectors execute the job templates you provide. SDMA does not validate or inspect job logic — that responsibility falls on the customer side of the shared responsibility model. Deadline Cloud provides its own execution isolation, IAM model, and job lifecycle management. Test job templates thoroughly in a non-production environment before enabling them.

## How it works
<a name="deadline-how-it-works"></a>

When a trigger fires, the Deadline Cloud connector performs the following steps:

1. If a singular template is configured, SDMA loads the job template from the configured SDMA template asset.

1. Resolves parameters using `${variable}` substitution from resource metadata, then converts them to the Deadline Cloud parameter format.

1. Builds job attachments by assembling manifests for the triggering asset, the template asset, and any additional assets.

1. Submits the job to Deadline Cloud via the [CreateJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateJob.html) API using the configured farm and queue.

1. Records the job ID in the connector invocation for correlation.

1. When the job completes, Deadline Cloud emits an EventBridge lifecycle event.

1. SDMA processes the completion event, updates the connector invocation status, and ingests any declared outputs back into the asset.

## Open Job Description
<a name="deadline-openjd"></a>

 [Open Job Description](https://github.com/OpenJobDescription/openjd-specifications) is a flexible open specification for defining batch processing jobs that are portable between different scheduling system deployments. The specification originated in the context of render farms and visual compute use cases, but applies more broadly to any batch processing workload. Deadline Cloud uses Open Job Description as the syntax for its job templates.

Open Job Description matters for SDMA because it provides a declarative, portable, and auditable way to define processing jobs. Rather than writing code that calls AWS APIs directly, you write a job template that describes the work. The template declares what parameters it takes, what scripts to run, what files it needs, and where to write outputs. Because the template is declarative, you can review, version, and inspect it without reading implementation code. SDMA handles the submission, file attachment, and result ingestion around that template. This means you can test the same job template locally using the [Open Job Description CLI](https://github.com/OpenJobDescription/openjd-cli), iterate on it independently of SDMA, and version it as an asset within SDMA alongside the scripts and resources it depends on.

### Key concepts
<a name="_key-concepts"></a>

A job template defines the runtime environment and the processes that run as part of a Deadline Cloud job. You can write job templates in YAML (`template.yaml`) or JSON (`template.json`). A job template contains:
+  **Parameters** — Input values that make a template reusable across different jobs. Open Job Description supports `STRING`, `INT`, `FLOAT`, and `PATH` parameter types. `PATH` parameters can declare `objectType` (`FILE` or `DIRECTORY`) and `dataFlow` (`IN`, `OUT`, `INOUT`) to control how [job attachments](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle.html) handle files.
+  **Steps** — Define the scripts that run on workers. Each step has one or more tasks. Steps can declare dependencies on other steps and specify host requirements such as minimum memory.
+  **Tasks** — A unit of work sent to a worker. A task combines a step’s script with specific parameter values (for example, a frame number). The job is complete when all tasks in all steps are complete.
+  **Environments** — Set up and tear down instructions shared by multiple steps or tasks, such as activating a software environment or starting a background service.
+  **Embedded files** — Script content defined inline in the template. The runtime expands variable references (using `{{Param.Name}}` and `{{Task.Param.Name}}` syntax) before writing the content to disk for execution.

For a full introduction to job template authoring, see [Job template elements for job bundles](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-template.html) in the Deadline Cloud Developer Guide. The Open Job Description specification repository provides deeper guides: [How Jobs Are Constructed](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Constructed), [How Jobs Are Run](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run), and the [Introduction to Creating a Job](https://github.com/OpenJobDescription/openjd-specifications/wiki/Introduction-to-Creating-a-Job) tutorial. The [Template Schemas](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas) reference provides the formal specification for all template elements.

For details on how SDMA assembles job bundles and maps configuration to Open Job Description concepts, see [Job template configuration](#deadline-template-modes) and [Configuration fields](#deadline-config-fields).

## Walkthrough: TIF to Cloud-Optimized GeoTIFF conversion
<a name="deadline-walkthrough"></a>

This walkthrough shows how to set up a Deadline Cloud connector that automatically converts uploaded GeoTIFF files to Cloud-Optimized GeoTIFF (COG) format. When a `.tif` file is uploaded to an asset, the connector submits a job that runs a Python conversion script on Deadline Cloud workers and writes the COG back as a derived file.

### Step 1: Create the IAM role
<a name="_step-1-create-the-iam-role"></a>

Create an IAM role that SDMA can assume to submit jobs to your Deadline Cloud farm. The role needs:
+  **Role name** must start with `SpatialDataManagementContentDerivation-` (for example, `SpatialDataManagementContentDerivation-CogConversion`).
+  **Trust policy** must allow the SDMA solution account to assume it:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "<CONNECTOR_INVOCATION_ROLE_ARN>",
          "<ASYNC_CONNECTOR_INVOCATION_ROLE_ARN>"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

\+ Replace `<CONNECTOR_INVOCATION_ROLE_ARN>` and `<ASYNC_CONNECTOR_INVOCATION_ROLE_ARN>` with the execution role ARNs of the connector invocation Lambda functions in your SDMA deployment.

\+ If you have AWS CLI access, you can find these values by running:

\+

```
aws lambda get-function \
  --function-name SpatialDataManagement-ConnectorInvocationFunction \
  --query 'Configuration.Role' --output text

aws lambda get-function \
  --function-name SpatialDataManagement-ConnectorInvocationAsyncFunction \
  --query 'Configuration.Role' --output text
```

\+ Alternatively, in the [Lambda console](https://console.aws.amazon.com/lambda/), open the `SpatialDataManagement-ConnectorInvocationFunction` and `SpatialDataManagement-ConnectorInvocationAsyncFunction` functions and find the role name for each under **Configuration** > **Permissions**. Use these names to construct the full ARNs (for example, `arn:aws:iam::<ACCOUNT_ID>:role/<CONNECTOR_INVOCATION_ROLE_NAME>`).
+  **Permissions policy** must grant access to Deadline Cloud job submission and status queries on your farm and queue:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "deadline:CreateJob",
        "deadline:GetJob",
        "deadline:GetQueue"
      ],
      "Resource": [
        "arn:aws:deadline:<REGION>:<ACCOUNT_ID>:farm/<FARM_ID>",
        "arn:aws:deadline:<REGION>:<ACCOUNT_ID>:farm/<FARM_ID>/queue/<QUEUE_ID>",
        "arn:aws:deadline:<REGION>:<ACCOUNT_ID>:farm/<FARM_ID>/queue/<QUEUE_ID>/job/*"
      ]
    }
  ]
}
```

### Step 2: Upload the job template and scripts
<a name="_step-2-upload-the-job-template-and-scripts"></a>

Create a project and asset in SDMA to hold your job template and any supporting scripts. This asset becomes the template asset that the connector references. Take care with project access — anyone who can modify this asset can change what the connector executes.

Upload the following files to the asset:

 ** `template.yaml` ** — the Open Job Description job template:

```
specificationVersion: 'jobtemplate-2023-09'
name: TIF to COG Conversion
description: |
  Converts a GeoTIFF file to Cloud-Optimized GeoTIFF (COG) format.
  The conversion script lives in scripts/convert_to_cog.py within the
  template asset bundle.

parameterDefinitions:
  - name: InputFile
    type: PATH
    objectType: FILE
    dataFlow: IN
  - name: WorkspacePath
    type: PATH
    objectType: DIRECTORY
    dataFlow: OUT
    default: workspace
  - name: BundlePath
    description: >
      Injected by SDMA in bundle mode. Points to the root of the template
      asset on the worker filesystem. Scripts live under this path.
    type: PATH
    objectType: DIRECTORY
    dataFlow: IN
  - name: SdmaConnectorInvocationId
    type: STRING
  - name: SdmaEventCorrelationId
    type: STRING
  - name: OriginalFilePath
    type: STRING
  - name: InputObjectKey
    type: STRING
  - name: OverviewLevels
    type: STRING
    default: "2,4,8,16,32"
  - name: Compression
    type: STRING
    default: "deflate"
  - name: CondaPackages
    type: STRING
    default: python=3.11 rasterio gdal numpy

steps:
  - name: ConvertToCog
    script:
      actions:
        onRun:
          command: python
          args:
            - '{{Param.BundlePath}}/scripts/convert_to_cog.py'
            - '{{Param.InputFile}}'
            - '{{Param.WorkspacePath}}'
            - '{{Param.OverviewLevels}}'
            - '{{Param.Compression}}'
```

 ** `scripts/convert_to_cog.py` ** — the conversion script (runs on the Deadline Cloud worker):

```
# Reads input TIF, builds overviews, writes COG to output directory.
# Uses rasterio/GDAL — install via CondaPackages in the job template.
import sys, os, rasterio

input_path, output_dir = sys.argv[1], sys.argv[2]
overview_levels, compression = sys.argv[3], sys.argv[4]

# ... your COG conversion logic here ...
# Write output to: os.path.join(output_dir, f"{basename}_cog.tif")
```

The script receives its arguments from the job template’s `{{Param.*}}` references. It reads the input file from the path SDMA staged and writes the COG to the output directory. Deadline Cloud’s job attachments system then uploads the result to S3 for SDMA to ingest and store in the asset.

### Step 3: Create the connector
<a name="_step-3-create-the-connector"></a>

In the Spatial Data Portal, go to **Library settings** > **Content** > **Connectors** > **Derive content** > **Create deriver**. Select **AWS Deadline Cloud** as the connector type and paste the following configuration:

```
{
  "deadlineConfig": {
    "farmId": "<FARM_ID>",
    "queueId": "<QUEUE_ID>",
    "templateAsset": {
      "assetId": "<TEMPLATE_ASSET_ID>"
    },
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-CogConversion"
    }
  },
  "triggers": [
    {
      "description": "Convert uploaded TIF files to Cloud-Optimized GeoTIFF",
      "resources": ["file"],
      "events": ["upload"],
      "filter": {
        "fileExtensionFilter": ".tif"
      },
      "deadlineJob": {
        "template": "template.yaml",
        "parameters": {
          "OverviewLevels": "2,4,8,16,32",
          "Compression": "deflate"
        },
        "output": {
          "derivedFiles": [
            { "filter": { "fileExtensionFilter": ".tif" } }
          ]
        }
      }
    }
  ]
}
```

### Step 4: Approve the connector on a template
<a name="_step-4-approve-the-connector-on-a-template"></a>

In the Spatial Data Portal, go to **Library settings** > **Content** > **Asset templates** and modify the template that governs your GeoTIFF assets to include the connector. From that point on, the connector automatically converts every `.tif` file uploaded to an asset under that template to COG format. SDMA writes the COG back as a derived file with provenance linking it to the job that produced it.

### What happens at runtime
<a name="_what-happens-at-runtime"></a>

1. A user uploads a `.tif` file to an asset.

1. SDMA matches the upload event against the connector’s trigger (resource: `file`, event: `upload`, filter: `.tif`).

1. SDMA submits a Deadline Cloud job with the template from the template asset, the input file staged to the worker, and the configured parameters.

1. The Deadline Cloud worker runs `convert_to_cog.py`, which reads the input TIF, builds overviews, and writes a COG to the output directory.

1. When the job completes, Deadline Cloud emits an EventBridge lifecycle event.

1. SDMA reads the job’s output manifest, matches the `.tif` output against the declared `derivedFiles` filter, and ingests the COG as a derived file on the asset.

1. The derived file fires a `derivationComplete` event, which downstream connectors (for example, a publish connector) can react to.

## Getting started
<a name="deadline-getting-started"></a>

The [Walkthrough: TIF to Cloud-Optimized GeoTIFF conversion](#deadline-walkthrough) walks through each of these steps in detail. At a high level:

1.  **Deadline Cloud farm and queue** — Use the defaults SDMA deploys, or create your own. The queue’s job attachments must point to the SDMA CAS bucket — see [Deadline Cloud infrastructure](#deadline-infrastructure).

1.  **IAM role** — Create a role starting with `SpatialDataManagementContentDerivation-` that the SDMA solution account can assume. Grant `deadline:CreateJob`, `deadline:GetJob`, and `deadline:GetQueue` on your farm and queue. See [Step 1](#deadline-walkthrough) for the trust and permissions policies.

1.  **Job template** — Write an Open Job Description template and upload it (with any supporting scripts) as an SDMA asset. See [Open Job Description](#deadline-openjd) for the key concepts and [Required parameters](#deadline-required-parameters) for the parameters SDMA auto-injects.

1.  **Connector configuration** — In the Spatial Data Portal, go to **Library settings** > **Content** > **Connectors** > **Derive content** > **Create deriver**. Select **AWS Deadline Cloud**, paste your configuration JSON, and create.

1.  **Template approval** — Add the connector ID to the `permittedConnectorIds` list on the asset template that should trigger jobs.

## Job template configuration
<a name="deadline-template-modes"></a>

SDMA loads job templates from SDMA assets and supports two template configuration modes.

A [job bundle](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle.html) groups a job template with additional files and directories that the job needs. When SDMA submits a Deadline Cloud job, it assembles a job bundle automatically according to the connector configuration, including:
+ The **triggering asset** (the SDMA asset that caused the connector to fire) — SDMA attaches it as a job attachment, giving the job read access to the asset’s files.
+ The **template asset** (the SDMA asset containing the job template and any supporting files it might need) — SDMA attaches it so the job can access scripts, configuration files, or other resources stored alongside the template.
+ Any **additional assets** configured in the connector are also attached.

Deadline Cloud is directly compatible with SDMA’s content-addressable storage (CAS). When configuring Deadline Cloud, you grant access to the S3 bucket and prefix containing SDMA’s CAS. When running jobs, Deadline Cloud loads asset content onto its workers seamlessly using manifest references — no transfer step is necessary because the files are already in S3. Deadline Cloud writes job outputs back to CAS, and SDMA ingests them into the governed asset record if they match predefined output filters.

### Template asset mode (recommended)
<a name="_template-asset-mode-recommended"></a>

Use the `templateAsset` block to reference an SDMA asset containing the job template and any supporting files. SDMA attaches the entire asset to the Deadline Cloud job as a job attachment, so the template can reference scripts, configuration files, or other resources stored alongside it.

```
"deadlineConfig": {
  "farmId": "farm-a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
  "queueId": "queue-d4e5f6a7b8c9d0e1f2a3b4c5d6a7b8c9",
  "templateAsset": {
    "assetId": "asset-7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d",
    "projectId": "project-0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"
  },
  "securityConfig": {
    "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-MyJob",
    "type": "AssumeRole"
  }
}
```
+  `templateAsset.assetId` — The SDMA asset containing the job template. Supports `${variable}` substitution.
+  `templateAsset.projectId` — (Optional) The project containing the template asset. Defaults to the triggering asset’s project if omitted.

In this mode, SDMA builds a multi-manifest job attachment with stable mount paths:
+ The triggering asset is mounted at `/sdma/assets/<assetId>`.
+ The template asset is mounted at `/sdma/assets/<templateAssetId>`.
+ Additional assets (if configured) are mounted at their specified `rootPath`.

These mount paths are deterministic, so your job template can reference files at known locations using the auto-injected `PATH` parameters (`InputFile`, `WorkspacePath`, `BundlePath`).

### Simple mode
<a name="_simple-mode"></a>

Use `templateProjectId` and `templateAssetId` to reference the template asset directly. This mode uses a single-manifest attachment with the asset’s original root path.

```
"deadlineConfig": {
  "farmId": "farm-a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
  "queueId": "queue-d4e5f6a7b8c9d0e1f2a3b4c5d6a7b8c9",
  "templateProjectId": "project-0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d",
  "templateAssetId": "asset-7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d",
  "securityConfig": {
    "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-MyJob",
    "type": "AssumeRole"
  }
}
```

**Note**
Template asset mode and simple mode are mutually exclusive. Use template asset mode for new connectors — it provides stable mount paths and supports multi-asset jobs.

## Required parameters
<a name="deadline-required-parameters"></a>

Any job template used with an SDMA Deadline Cloud connector must declare the following parameters. SDMA auto-injects values for these at submission time. Your template does not need to use all of them in its scripts, but it must declare them so that Deadline Cloud accepts the values SDMA provides.

```
parameterDefinitions:
  - name: InputFile
    type: PATH
    objectType: FILE
    dataFlow: IN
  - name: WorkspacePath
    type: PATH
    objectType: DIRECTORY
    dataFlow: OUT
    default: workspace
  - name: BundlePath
    type: PATH
    objectType: DIRECTORY
    dataFlow: IN
  - name: SdmaConnectorInvocationId
    type: STRING
  - name: SdmaEventCorrelationId
    type: STRING
  - name: OriginalFilePath
    type: STRING
  - name: InputObjectKey
    type: STRING
```

 `InputFile`, `WorkspacePath`, and `BundlePath` are `PATH` parameters. They tell the job where to find the source file, where to write outputs, and where the template bundle is mounted on the worker’s local filesystem. The remaining `STRING` parameters carry SDMA context — asset identity, project identity, connector correlation, and the S3 object key of the input file. SDMA uses these to correlate job completion and output ingestion back to the correct asset and connector invocation.

**Important**
If your job template omits any of these parameter declarations, Deadline Cloud rejects the job at submission time because SDMA always passes values for all of them.

## Job parameters
<a name="deadline-parameters"></a>

The `parameters` block in the trigger-level `deadlineJob` configuration passes values for the parameters declared in your job template. Parameter values support `${variable}` substitution from SDMA resource metadata.

```
"deadlineJob": {
  "template": "processing/template.yaml",
  "parameters": {
    "OutputFormat": "glb",
    "Quality": "high",
    "TileSize": "${asset.metadataAttributes.tileSize}:number"
  }
}
```

SDMA passes these values to the Deadline Cloud [CreateJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateJob.html) API, and they become available in your job template via `{{Param.OutputFormat}}`, `{{Param.Quality}}`, and `{{Param.TileSize}}` variable references.

### Parameter type annotations
<a name="_parameter-type-annotations"></a>

Open Job Description job templates declare parameter types (`STRING`, `INT`, `FLOAT`, `PATH`), and the Deadline Cloud CreateJob API expects parameter values in a typed format. SDMA connector parameter values are strings by default. Use a postfix `:type` annotation to declare the Deadline Cloud wire type:

| Suffix | Deadline Cloud format | Example |
| --- | --- | --- |
|  `:string` (default) |  `{"string": "value"}`  |  `"high"` or `"high:string"`  |
|  `:number`  |  `{"float": 256.0}`  |  `"${asset.metadataAttributes.tileSize}:number"`  |
|  `:path`  |  `{"path": "/path/to/file"}`  |  `"/sdma/assets/${asset.assetId}/input.e57:path"`  |

Use `:number` for parameters declared as `INT` or `FLOAT` in the job template. Use `:path` for parameters declared as `PATH`.

SDMA treats colons that are not a recognized type suffix as literal characters. For example, `s3://bucket/key` is unaffected because `//bucket/key` is not a recognized suffix.

## Output configuration
<a name="deadline-outputs"></a>

The `output` block in the trigger-level `deadlineJob` configuration declares which files produced by the job are eligible for ingestion into SDMA. SDMA uses a fail-closed approach — only files matching a declared output filter are ingested. SDMA ignores undeclared outputs.

The job template writes job outputs to the `WorkspacePath` directory. When the job completes, Deadline Cloud’s job attachments system uploads the output files to S3, and SDMA reads the output manifest to determine which files to ingest.

```
"deadlineJob": {
  "template": "conversion/template.yaml",
  "output": {
    "derivedFiles": [
      {
        "filter": { "fileExtensionFilter": ".glb" },
        "preview": true
      },
      {
        "filter": { "fileExtensionFilter": ".stp" }
      }
    ]
  }
}
```

### Output types
<a name="_output-types"></a>

| Type | Description |
| --- | --- |
|  `derivedFiles`  | Files produced by the job are ingested as derived content associated with the triggering file. Each entry specifies a `filter` to match output files by extension or pattern. Set `preview` to `true` to mark matched files as preview content (for example, thumbnails or 3D previews). |
|  `files`  | Output files are inserted directly into the asset as regular files. |
|  `metadataAttributes`  | A JSON metadata file produced by the job is parsed and its fields are applied as metadata attributes on the asset or file. Use `fieldMappings` to control how fields from the metadata file map to SDMA metadata attributes. |

### Output filters
<a name="_output-filters"></a>

Each output entry uses a `filter` block to match files. The filter supports the same fields as trigger-level filters:
+  `fileExtensionFilter` — Match files by extension (for example, `.glb`, `.json`).
+  `fileNameRegex` — Match files by a regex pattern against the filename.
+  `pathRegex` — Match files by a regex pattern against the full path.
+  `minFileSizeMB` / `maxFileSizeMB` — Match files by size.

**Important**
If no output filters are configured, SDMA does not ingest any job outputs. This is a deliberate safety measure — you must explicitly declare which output types are expected.

### Metadata attribute output with field mappings
<a name="_metadata-attribute-output-with-field-mappings"></a>

The `metadataAttributes` output type lets a Deadline Cloud job write structured metadata back to the asset record. The job produces a JSON file (typically named `spatial_data_mgmt_metadata.json`) in the output directory. When that file matches the `metadataAttributes` filter, SDMA parses it and writes the values as confirmed metadata attributes — bypassing the suggestion/review workflow that applies to built-in metadata extraction.

Use `fieldMappings` to control where SDMA writes each field from the JSON file. Mappings with `asset. ` targets write to asset-level metadata attributes. Mappings with `file.` targets write to file-level metadata attributes on the triggering file. SDMA flattens any fields in the JSON that a field mapping does not cover and writes them to file-level metadata by default.

The following example shows a connector that runs a quality analysis job and writes results to both asset-level and file-level metadata:

```
"deadlineJob": {
  "template": "quality-analysis/template.yaml",
  "output": {
    "metadataAttributes": {
      "filter": { "fileExtensionFilter": ".json" },
      "fieldMappings": [
        { "source": "overallScore", "target": "asset.qualityScore" },
        { "source": "bundleProcessed", "target": "asset.bundleProcessed" },
        { "source": "inputQuality", "target": "file.inputQuality" }
      ]
    },
    "derivedFiles": [
      { "filter": { "fileExtensionFilter": ".dat" } }
    ]
  }
}
```

If the job produces the following `spatial_data_mgmt_metadata.json`:

```
{
  "overallScore": 0.94,
  "bundleProcessed": true,
  "inputQuality": "high",
  "resolution": "4096x4096"
}
```

SDMA processes it as follows:
+  `overallScore` → written to `asset.qualityScore` (asset-level metadata attribute) because the mapping target starts with `asset.`.
+  `bundleProcessed` → written to `asset.bundleProcessed` (asset-level) for the same reason.
+  `inputQuality` → written to `file.inputQuality` (file-level metadata attribute on the triggering file) because the mapping target starts with `file.`.
+  `resolution` → not covered by any field mapping, so SDMA flattens it and writes it to file-level metadata by default.

SDMA removes asset-level attributes that map to `asset.*` targets from the raw metadata before file-level flattening, so they do not appear in both places.

When a field mapping targets an attribute that already exists (at either level), SDMA updates the existing value rather than duplicating it. This means re-running a connector on the same asset merges new results into the existing metadata rather than replacing it entirely.

**Note**
Without a `metadataAttributes` filter, SDMA still processes `spatial_data_mgmt_metadata.json` files by filename convention, but writes the values as suggestions rather than confirmed attributes. The `metadataAttributes` filter is what promotes the output to confirmed, connector-directed metadata.

## Additional assets
<a name="deadline-additional-assets"></a>

In template asset mode, you can attach additional SDMA assets to the job as extra job attachments. Use this when a job needs access to shared libraries, reference data, or other assets beyond the triggering asset and the template.

```
"deadlineConfig": {
  "farmId": "farm-a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6",
  "queueId": "queue-d4e5f6a7b8c9d0e1f2a3b4c5d6a7b8c9",
  "templateAsset": {
    "assetId": "asset-e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
  },
  "additionalAssets": [
    {
      "assetId": "asset-b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1",
      "rootPath": "/sdma/libs"
    }
  ],
  "securityConfig": { "..." }
}
```
+  `assetId` — The SDMA asset to attach. Supports `${variable}` substitution.
+  `rootPath` — The mount path for this asset in the Deadline Cloud worker environment. If omitted, defaults to `/sdma/assets/<assetId>`.

**Note**
SDMA currently resolves additional assets from the triggering asset’s project. SDMA accepts the `projectId` field for forward compatibility but does not yet use it for cross-project resolution.

## More configuration examples
<a name="deadline-more-examples"></a>

### As a step in a multi-step connector
<a name="_as-a-step-in-a-multi-step-connector"></a>

You can also use the `deadlineJob` step type within the trigger\+steps model for multi-step workflows:

```
"triggers": [
  {
    "resources": ["file"],
    "events": ["upload"],
    "steps": [
      {
        "stepType": "deadlineJob",
        "template": "processing/template.yaml",
        "parameters": {
          "ModelId": "${file.metadataAttributes.modelId}"
        },
        "output": {
          "derivedFiles": [
            { "filter": { "fileExtensionFilter": ".glb" }, "preview": true }
          ]
        }
      }
    ]
  }
]
```

## Deadline Cloud infrastructure
<a name="deadline-infrastructure"></a>

### Farms, queues, and fleets
<a name="_farms-queues-and-fleets"></a>

Deadline Cloud organizes compute resources into [farms, queues, and fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/how-it-works.html). A farm is the top-level container. Queues hold submitted jobs and manage scheduling. Fleets provide the compute workers that execute jobs. For a full overview of these concepts, see [Concepts and terminology](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/concepts-terminology.html) in the Deadline Cloud Developer Guide.

When you deploy SDMA, the deployment creates a Deadline Cloud farm, a default [service-managed fleet](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html), and a default queue. You can use these default resources for custom processing jobs, but you are not required to. You can create additional queues and fleets tailored to your processing needs.

Fleets can be elastic, scaling workers up and down based on job demand. [Service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html) run on AWS-managed infrastructure with a range of instance type and operating system choices. [Customer-managed fleets](https://aws.amazon.com/blogs/media/leveraging-aws-deadline-clouds-customer-managed-fleets/) run on instances in your own AWS account, giving you full control over the compute environment — useful when jobs require specific software, GPU types, or licensing configurations. Tailor your fleet configuration to the processing workloads your connectors will run.

**Note**
Although Deadline Cloud lazy-loads content from S3 (only fetching files when the job references them), workers still need sufficient local disk space to hold the files during processing. Choose a root volume size large enough to comfortably accommodate the largest files or collection of files you expect to process.

**Important**
The Deadline Cloud [queue](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/queues.html) used by a connector must have its [job attachments configuration](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/storage-job-attachments.html) set to the same S3 bucket and root prefix as SDMA’s content-addressable storage. The queue’s IAM role must also have permission to read from and write to that bucket and prefix. Without this, Deadline Cloud cannot access asset content or write outputs back to SDMA.

### Software and dependencies
<a name="_software-and-dependencies"></a>

Deadline Cloud uses [queue environments](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs.html) to configure the software available to jobs. The default queue environment uses the [conda](https://docs.conda.io/en/latest/) package manager to install software into an isolated virtual environment for each session.

Job templates declare their dependencies using the `CondaPackages` parameter — a space-separated list of conda package specifications (for example, `python=3.11 pillow numpy tifffile zarr`). The queue environment installs these packages before the job runs. Packages can come from:
+ The `deadline-cloud` channel — Deadline Cloud provides a curated set of rendering and content creation applications (such as Blender, Autodesk Maya, and others). For a list of available packages, see [Software licensing for service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-licensing.html).
+ The [conda-forge](https://conda-forge.org/) channel — a community-maintained collection of open-source packages. To use conda-forge packages, set the `CondaChannels` parameter in your job template to include `conda-forge`.
+ Custom S3-hosted channels — for applications not available on public channels, you can [create a conda channel in Amazon S3](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/configure-jobs-s3-channel.html) and [build your own conda packages](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/conda-package.html). Add the S3 channel URL to the queue environment’s `CondaChannels` default so it is available to all jobs in that queue.

### Licensed software
<a name="_licensed-software"></a>

Deadline Cloud supports two approaches for using licensed software in jobs:
+  **Usage-based licensing (UBL)** — Deadline Cloud provides [usage-based licensing](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-licensing.html) for commonly used rendering applications on service-managed fleets. Deadline Cloud automatically licenses supported applications when they run — you do not need to configure or maintain a license server.
+  **Bring your own license (BYOL)** — If you have existing license agreements or need software not covered by UBL, you can [connect service-managed fleets to your own license server](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-byol.html). For customer-managed fleets, you have full control over the licensing configuration since the workers run in your own account.

Management of licensed software, runtime environments, and containers is outside SDMA’s scope. SDMA submits job configuration to Deadline Cloud; the queue environment and fleet configuration determine the software environment.

## Step types
<a name="deadline-step-types"></a>

The Deadline Cloud connector supports the following step type.

| Step type | Description |
| --- | --- |
|  `deadlineJob`  | Submits a job to Deadline Cloud using an Open Job Description job template. The job runs asynchronously in Deadline Cloud’s isolated compute environment. SDMA monitors completion through EventBridge lifecycle events and ingests declared outputs. |

## Configuration fields
<a name="deadline-config-fields"></a>

### How SDMA maps to Open Job Description
<a name="_how-sdma-maps-to-open-job-description"></a>

When SDMA submits a job, it maps connector configuration to Open Job Description concepts as follows:

| SDMA concept | Open Job Description equivalent |
| --- | --- |
|  `deadlineJob.template`  | The job template file (for example, `template.yaml`) |
|  `deadlineJob.parameters`  | Values for the job template’s declared parameters, passed via the Deadline Cloud [CreateJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateJob.html) API |
|  `deadlineConfig.templateAsset`  | The job bundle’s supporting files, attached as a manifest |
|  `deadlineConfig.additionalAssets`  | Additional input manifests attached to the job |
| Auto-injected parameters (for example, `InputFile`, `WorkspacePath`) |  `PATH`-typed parameters that reference the worker’s local mount paths |

### Connector-level fields (`deadlineConfig`)
<a name="_connector-level-fields-deadlineconfig"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `deadlineConfig.farmId`  | Yes | Deadline Cloud farm ID. Format: `farm-<32 hex characters>`. |
|  `deadlineConfig.queueId`  | Yes | Deadline Cloud queue ID. Format: `queue-<32 hex characters>`. |
|  `deadlineConfig.securityConfig`  | Yes | Authentication configuration. Must use `AssumeRole` type. |
|  `deadlineConfig.templateAsset.assetId`  | Yes (template asset mode) | SDMA asset containing the job template. Supports `${variable}` substitution. |
|  `deadlineConfig.templateAsset.projectId`  | No | Project containing the template asset. Defaults to the triggering asset’s project. |
|  `deadlineConfig.templateProjectId`  | Yes (simple mode) | Project ID for the template asset. Mutually exclusive with `templateAsset`. |
|  `deadlineConfig.templateAssetId`  | Yes (simple mode) | Asset ID for the template asset. Mutually exclusive with `templateAsset`. |
|  `deadlineConfig.additionalAssets`  | No | Array of additional SDMA assets to attach to the job as job attachments. Each entry requires `assetId`. `rootPath` is optional (defaults to `/sdma/assets/<assetId>`). |
|  `deadlineConfig.maxRetriesPerTask`  | No | Per-task retry limit passed to Deadline Cloud. Defaults to `1`. |
|  `deadlineConfig.maxFailedTasksCount`  | No | Maximum failed tasks before the job is cancelled. If omitted, the Deadline Cloud default applies. |
|  `deadlineConfig.deadlineMonitorUrl`  | No | Base URL for Deadline Cloud Monitor. Used to generate a direct link to the job in the Spatial Data Portal if required. |

### Trigger-level fields (`deadlineJob`)
<a name="_trigger-level-fields-deadlinejob"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `deadlineJob.template`  | Yes | Path to the job template file within the template asset (for example, `template.yaml` or `processing/template.yaml`). Supports YAML and JSON formats. |
|  `deadlineJob.parameters`  | No | Values for the job template’s declared parameters. Values support `${variable}` substitution and `:type` annotations (`:string`, `:number`, `:path`). |
|  `deadlineJob.output`  | No | Output configuration declaring which job outputs are eligible for ingestion. |
|  `deadlineJob.output.derivedFiles`  | No | Array of derived file output declarations. Each entry has a `filter` and optional `preview` flag. |
|  `deadlineJob.output.files`  | No | Array of regular file output declarations. Each entry has a `filter`. |
|  `deadlineJob.output.metadataAttributes`  | No | Metadata output declaration with a `filter` and optional `fieldMappings`. |

## Job completion and output ingestion
<a name="deadline-completion"></a>

When a Deadline Cloud job completes, the following occurs:

1. Deadline Cloud emits an EventBridge lifecycle event with the job status.

1. SDMA correlates the event to the originating connector invocation using the `SdmaConnectorInvocationId` parameter embedded in the job.

1. If the job succeeded, SDMA reads the job’s output manifest from S3.

1. SDMA checks each output file against the connector’s declared output filters and skips files that do not match any filter.

1. SDMA ingests matching files into the asset as derived files, regular files, or metadata attributes based on the output configuration.

1. SDMA updates the connector invocation status to `SUCCEEDED` or `FAILED`.

1. If the job was triggered by a file event, SDMA publishes a `derivationComplete` event on the triggering file, which can activate downstream connector triggers.

## Security model
<a name="deadline-security"></a>

The Deadline Cloud connector follows the same security model as other SDMA connectors, with additional considerations for compute workloads.

### IAM role
<a name="_iam-role"></a>

SDMA uses the IAM role specified in `deadlineConfig.securityConfig.assumeRoleArn` for all Deadline Cloud API calls (job submission, status queries). This role must:
+ Start with `SpatialDataManagementContentDerivation-`.
+ Have permissions to create and query jobs on the specified farm and queue.
+ Be assumable by the SDMA solution account.

### Shared responsibility
<a name="_shared-responsibility"></a>

SDMA submits job configuration to Deadline Cloud but does not execute, sandbox, or inspect job logic. The security of what a job does is the customer’s responsibility:
+  **Job templates** — You control what the job does. SDMA does not validate job template logic. Deadline Cloud provides its own [security model](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security.html) for job execution.
+  **IAM role permissions** — The role you provide determines what AWS resources the job can access. Scope it to least privilege.
+  **Runtime dependencies** — Management of containers, licensed software, or runtime environments is outside SDMA’s scope. See the Deadline Cloud documentation on [workloads](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/what-is-a-deadline-cloud-workload.html) for guidance on configuring worker environments.
+  **Fleet configuration** — You manage Deadline Cloud farm and queue sizing, concurrency limits, and cost controls in your Deadline Cloud configuration.

### Output ingestion safety
<a name="_output-ingestion-safety"></a>

SDMA enforces strict output ingestion controls:
+ SDMA ingests only files matching a declared output filter.
+ SDMA only accepts outputs when correlated to a known, active connector invocation.
+ SDMA ignores events that cannot be correlated to a known invocation.
+ If the connector configuration cannot be loaded or has no output filters, SDMA does not ingest any outputs (fail-closed).

## Error handling
<a name="deadline-error-handling"></a>

The following table describes common Deadline Cloud connector errors and their resolution.

| Phase | Error | Resolution |
| --- | --- | --- |
| Submission |  `AccessDeniedException`  | The assumed IAM role does not have permission to create jobs on the specified farm and queue. Verify the role’s permissions policy. |
| Submission | Template asset not found | The configured `templateAsset.assetId` or `templateAssetId` does not exist. Verify the asset ID and project ID. |
| Submission | Template file not found | The `template` path does not match any file in the template asset. Verify the path (for example, `template.yaml` or `processing/template.yaml`). |
| Submission | Missing `farmId` or `queueId`  | The `deadlineConfig` is missing required Deadline Cloud identifiers. Verify the connector configuration. |
| Execution | Job `FAILED`  | The Deadline Cloud job failed during execution. Check the job logs in Deadline Cloud Monitor for details. Common causes include missing dependencies, incorrect `PATH` parameter values, or script errors in the job template. |
| Completion | Invocation not found | The `SdmaConnectorInvocationId` in the job parameters does not match any active invocation. The completion event is ignored. |
| Output | No output filters configured | SDMA skips all outputs. Add `derivedFiles`, `files`, or `metadataAttributes` entries to the `output` block. |
| Output | File extension not in allowlist | The output file’s extension does not match any declared filter. Add the appropriate `fileExtensionFilter` to the `output` block. |

If a Deadline Cloud connector repeatedly fails, the connector’s failure policy (if configured) may automatically disable the connector to prevent runaway resubmission. See [Failure policy](connector-configuration.md#failure-policy) in the connectors overview.

## Further reading
<a name="deadline-further-reading"></a>
+  [Open Job Description specification](https://github.com/OpenJobDescription/openjd-specifications) — The specification repository, including the formal template schemas and design documentation.
+  [How Jobs Are Constructed](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Constructed) — Open Job Description guide explaining job template structure, parameters, steps, tasks, and environments.
+  [How Jobs Are Run](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run) — Open Job Description guide explaining sessions, embedded files, variable expansion, and the job execution lifecycle.
+  [Introduction to Creating a Job](https://github.com/OpenJobDescription/openjd-specifications/wiki/Introduction-to-Creating-a-Job) — Step-by-step Open Job Description tutorial from shell scripts to production-ready job templates.
+  [Open Job Description sample templates](https://github.com/OpenJobDescription/openjd-specifications/tree/mainline/samples) — Example job templates in the specification repository.
+  [Deadline Cloud sample job bundles](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles) — Complete job bundle examples for Deadline Cloud.
+  [Job bundles](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle.html) — Deadline Cloud Developer Guide documentation on job bundles and job attachments.
+  [Job template elements](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-template.html) — Deadline Cloud Developer Guide reference for job template syntax.
+  [Deadline Cloud jobs](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deadline-cloud-jobs.html) — Deadline Cloud User Guide overview of jobs, steps, tasks, and priorities.
+  [Deadline Cloud security](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/security.html) — Deadline Cloud security model and shared responsibility documentation.
