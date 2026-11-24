---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-patterns.html
---

# Connector Patterns for Models and Pipelines

This topic describes patterns for training and running machine learning models, and for multi-stage processing pipelines, with connectors. The models and pipelines can work on any spatial content, such as point clouds, imagery, 3D models, or sensor recordings. Each pattern uses only the connector features described in [Connector Configuration](connector-configuration.md), [Working with Wait Steps](connector-wait.md), and [Create and Transform Content with AWS Deadline Cloud](connector-deadline-cloud.md). Together, they show how several connectors, each approved and versioned independently, build one governed result on an asset.

Filters, `output` blocks, `${…​}` variables, `$temp` values, and type suffixes such as `:number` work the same way for every connector type. For more information, see [Trigger Filters](connector-configuration.md#trigger-filters), [Output Routing](connector-configuration.md#output-routing), [Variable Substitution](connector-configuration.md#variable-substitution), [Intermediate State with $temp Variables](connector-configuration.md#temp-variables), and [Type Coercion](connector-configuration.md#type-coercion).

## Running Inference on an Amazon SageMaker Asynchronous Endpoint
<a name="pattern-sagemaker-async"></a>

An Amazon SageMaker asynchronous inference endpoint suits models that take minutes to run on large inputs, such as point clouds or imagery. You send the endpoint the Amazon S3 location of a request. The endpoint returns at once with the locations where it will write the result and, if the request fails, an error. For more information, see [Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) in the *Amazon SageMaker AI Developer Guide*. A connector expresses this in three steps:

1. An `s3PutObject` step writes the request document to Amazon S3.

1. A `rest` step calls the endpoint’s `async-invocations` operation and captures the two locations from the response headers into `$temp` variables.

1. A `wait` step polls for the result at the captured output location, and fails at once if the error appears at the captured failure location.

### Example – Segment a Point Cloud with an Amazon SageMaker Asynchronous Endpoint
<a name="_example-segment-a-point-cloud-with-an-amazon-sagemaker-asynchronous-endpoint"></a>

The following connector runs a segmentation model on each uploaded `.las` file. It ingests the model’s output point cloud as a derived file and records the model’s summary on the source file.

```json
{
  "schemaVersion": "1.0.0",
  "name": "Point cloud segmentation (SageMaker async)",
  "defaultStepConfig": {
    "stepType": "rest",
    "restConfig": {
      "apiBase": "https://runtime.sagemaker.<region>.amazonaws.com",
      "securityConfig": {
        "type": "AssumeRole",
        "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentDerivation-SageMaker"
      }
    }
  },
  "s3Config": {
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentDerivation-SageMaker"
    }
  },
  "triggers": [
    {
      "resources": ["file"],
      "events": ["upload", "onDemand"],
      "filter": { "fileExtensionFilter": ".las" },
      "parameterDefinitions": {
        "endpoint": {
          "type": "string",
          "modelIdentity": "sagemakerEndpoint",
          "allowedValues": ["<endpoint-name>"],
          "default": "<endpoint-name>",
          "displayName": "Model endpoint",
          "description": "SageMaker endpoint that runs the model."
        },
        "modelVersion": {
          "type": "string",
          "default": "segmentation-v2",
          "description": "Model label recorded on the results."
        }
      },
      "steps": [
        {
          "stepType": "s3PutObject",
          "description": "Stage the inference request.",
          "s3Config": {
            "bucketName": "amzn-s3-demo-bucket",
            "objectKey": "requests/${parameters.connectorInvocationId}/request.json"
          },
          "fieldMappings": [
            { "source": "file.s3Uri", "target": "input.s3Uri" }
          ],
          "body": {
            "requestId": "${parameters.connectorInvocationId}",
            "model": { "modelVersion": "${parameters.modelVersion}" },
            "output": { "s3Prefix": "s3://amzn-s3-demo-bucket/jobs/${parameters.connectorInvocationId}/" }
          }
        },
        {
          "stepType": "rest",
          "description": "Start the asynchronous inference.",
          "method": "POST",
          "path": "/endpoints/${parameters.endpoint}/async-invocations",
          "headers": {
            "X-Amzn-SageMaker-ContentType": "application/json",
            "X-Amzn-SageMaker-InferenceId": "${parameters.connectorInvocationId}",
            "X-Amzn-SageMaker-InputLocation": "s3://amzn-s3-demo-bucket/requests/${parameters.connectorInvocationId}/request.json",
            "X-Amzn-SageMaker-InvocationTimeoutSeconds": "1800"
          },
          "responseFieldMapping": [
            { "source": "responseHeaders.x-amzn-sagemaker-outputlocation", "target": "$temp.outputLocation" },
            { "source": "responseHeaders.x-amzn-sagemaker-failurelocation", "target": "$temp.failureLocation" }
          ]
        },
        {
          "stepType": "wait",
          "description": "Wait for the result, and ingest it.",
          "wait": {
            "timeoutSeconds": 1800,
            "poll": { "type": "output", "intervalSeconds": 15 },
            "failure": { "uri": "${$temp.failureLocation}" }
          },
          "output": {
            "metadataAttributes": {
              "uri": "${$temp.outputLocation}",
              "filter": { "fileNameRegex": ".*\\.out$" },
              "fieldMappings": [
                { "role": "provenance", "source": "model.modelVersion", "target": "file.metadataAttributes.segmentationModelVersion" },
                { "source": "processing.elapsedSeconds", "target": "file.metadataAttributes.segmentationSeconds:number" },
                { "role": "provenance", "source": "model.modelVersion", "target": "derivedFile.metadataAttributes.modelVersion" }
              ]
            },
            "derivedFiles": [
              {
                "uri": "s3://amzn-s3-demo-bucket/jobs/${parameters.connectorInvocationId}",
                "filter": { "fileExtensionFilter": ".laz" },
                "preview": true
              }
            ]
          }
        }
      ]
    }
  ]
}
```

Replace `<region>`, `<account-id>`, and `<endpoint-name>` with your values, and `amzn-s3-demo-bucket` with the bucket the endpoint reads and writes.

How the steps work together:

| Step | What it does |
| --- | --- |
|  `s3PutObject`  | Writes the request document. `file.s3Uri` gives the endpoint the Amazon S3 location of the uploaded file, so the endpoint reads the file in place. The request and output paths include the run’s ID, so each run is separate. |
|  `rest`  | Calls the endpoint. SDMA signs the request with Signature Version 4 for SageMaker, in the Region that the host name names. SageMaker returns the output and failure locations in response headers, not in the body. A `responseFieldMapping` source of `responseHeaders.<header-name>`, in lowercase, captures a response header. |
|  `wait`  | Polls for the summary file at `$temp.outputLocation`. It reads that file as the source for `fieldMappings`, and ingests the `.laz` files under the job prefix as derived files. If the endpoint writes an error to `$temp.failureLocation` first, the wait fails at once with the error as its reason. |

Passing the run’s ID as `X-Amzn-SageMaker-InferenceId` lets you match an endpoint’s logs to the connector invocation.

The `endpoint` parameter pins the model. It has one allowed value, and the call’s path uses it, so the connector can only run the endpoint it names. `modelIdentity` tells SDMA that this parameter is the model, so each run records which endpoint it called, and the template’s **Content flow** tab names it on the connector’s card. Someone who runs the connector on demand cannot pick an endpoint that is not in `allowedValues`. To run another model, replace the allowed value, or add one to let callers choose between them. Either is a change to the connector itself, and every run records the connector version it ran with. For more information, see [Naming the Model a Trigger Runs](connector-configuration.md#trigger-model-identity).

This connector is configuration only. There is no function to write or deploy between SDMA and the endpoint: SDMA signs the call, waits for the result without holding compute, and ingests the output.

### Permissions
<a name="_permissions"></a>

The connector’s role must allow `sagemaker:InvokeEndpointAsync` on the endpoint. It must also allow `s3:PutObject` for the request, and `s3:GetObject` and `s3:ListBucket` for the result and error locations. The endpoint’s own execution role reads the request and input file, and writes the result. For more information about connector roles, see [IAM Role Naming](connector-configuration.md#security-role-naming).

## Recording Which Model Produced a Result
<a name="pattern-model-provenance"></a>

When a model’s output becomes part of an asset, record which model produced it. Then anyone who reads the result, later or in another system, can tell how it was made.

Four features make this simple:
+  **A parameter for the model.** Declare a parameter such as `modelVersion` with a `default`. Pass it to the model in the request, and map it back from the model’s response. Someone who runs the connector on demand can choose another version. For more information, see [Trigger Parameters](connector-configuration.md#trigger-parameters).
+  **A declared model identity.** Mark the parameter that names the model with `modelIdentity`, so that SDMA and the Portal know which parameter identifies the model. When the model is a file in SDMA, make the parameter type `file`. The run then pins the exact stored bytes of the model, not a name that someone can later point at something else. See [Naming the Model a Trigger Runs](connector-configuration.md#trigger-model-identity).
+  **Separate targets for facts about the input and facts about the output.** A field mapping target that starts with `file.` writes to the file that matched the trigger. A target that starts with `derivedFile.` writes to the derived files the step produced.
+  **A role for each value.** Mark mappings that record where a result came from with `"role": "provenance"`, and mappings that record what the run found with `"role": "finding"`. SDMA records which run wrote each value, with its role. See [Saying What a Value Means](connector-configuration.md#field-mapping-role).

Every run also records the connector version and the parameter values that it ran with. To answer which model produced a result, read the derived file’s attributes, and the invocation that produced it.

| Target | Lands on | Use it for |
| --- | --- | --- |
|  `file.metadataAttributes.<name>`  | The source file | Facts about the source, such as how many points of each class it contains |
|  `derivedFile.metadataAttributes.<name>`  | Each derived file the step ingested | Facts about the output, such as which model version made it |

Facts about an output belong on the output. If you record the model version only on the source file, the next run against that file, perhaps with another model, overwrites it. On the derived file, the version stays with the result it describes.

## Example – A Multi-Model Pipeline
<a name="pattern-pipeline"></a>

A pipeline turns one upload into a result that no single model produces. Build each stage as its own connector, and let the stages compose through the asset record: each stage’s derived file raises an `upload` event that starts the next.

The following example analyzes a point cloud in five stages. Stage 1 has a `file` trigger on `upload`. Stages 2 to 5 each have a `derivedFile` trigger on `upload`, and match only the file the previous stage produced, using `fileNameRegex`. For more information, see [Chaining Connectors](connector-configuration.md#chaining-connectors).

| Stage | Runs on | Matches | Produces |
| --- | --- | --- | --- |
| 1. Semantic segmentation | SageMaker asynchronous endpoint | An uploaded `.las` file |  `segmented.laz`, with a class for each point |
| 2. Format conversion | AWS Deadline Cloud |  `segmented.laz`  |  `segmented.copc.laz`, a streamable preview |
| 3. Filter | AWS Deadline Cloud |  `segmented.copc.laz`  |  `vegetation.laz`, only the points stage 4 needs |
| 4. Instance segmentation | SageMaker asynchronous endpoint |  `vegetation.laz`  | An instance point cloud, one ID for each object |
| 5. Fusion | AWS Deadline Cloud | The instance point cloud | A report that combines stages 1 and 4 with terrain data from another connector |

```text
upload .las ──> 1 segmentation ──> 2 conversion ──> 3 filter ──> 4 instances ──> 5 fusion
                     │                 │                │              │              │
                     └─────────────────┴── derived files of the .las ──┴──────────────┘
```

Patterns that make the pipeline work:
+  **Keep every stage’s output beside the source.** Stages 2 to 5 each match a derived file, and declare their output with `siblingDerivedFiles` rather than `derivedFiles`. All stages' outputs then sit side by side as derived files of the original `.las`, rather than in a chain nested five levels deep. For more information, see [Placing Derived Files Alongside Their Source](connector-configuration.md#sibling-derived-files).
+  **Order stages that read more than their trigger.** A stage that reads outputs other than the one that matched it can declare `dependsOn` for the connectors that produce them. For more information, see [Ordering Connectors with dependsOn](connector-configuration.md#trigger-dependencies).
+  **Write the result as metadata, too.** The fusion stage maps counts and measurements from its report into `derivedFile.metadataAttributes`, so you can search for and filter the result without opening it. For a complete fusion stage, see [Example – An Inspection Stage Whose Findings Use the Run’s Own Thresholds](#pattern-inspection-findings).
+  **Approve each stage separately.** Each connector is approved on the asset template, so you can change, turn off, or reuse one stage without touching the others.
+  **Connect stages with configuration, not code.** The models and job scripts are your code, but the connectors that run them, pass outputs between them, and record their results are configuration. Adding or reordering a stage is a connector change, not a deployment.

### Reading Earlier Stages' Outputs in a Job
<a name="pattern-reading-earlier-outputs"></a>

A fusion stage needs more than the file that matched its trigger. In the example, stage 5 matches the instance point cloud, but it also needs the stage 1 segmentation and a terrain model from another connector.

An AWS Deadline Cloud job receives these without extra configuration. SDMA attaches the triggering asset to the job, and the files staged on the worker include the derived files that earlier connectors added to that asset. The file that matched the trigger is also passed in the `InputFile` parameter.

Find the other inputs by name or pattern, not by a fixed path. The layout of derived files on the worker is not part of the connector contract, so a path that works today might not work after an update. For example, a job script can search the staged files:

```python
import subprocess

def find(pattern):
    """Return staged files whose names match a pattern, such as '*.tif'."""
    result = subprocess.run(
        ["find", ".", "-type", "f", "-iname", pattern],
        capture_output=True, text=True, check=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]

segmentation = [p for p in find("*.laz") if "segmented" in p and "vegetation" not in p]
terrain = [p for p in find("*.tif") if "dtm" in p.lower()]
```

Give each stage’s output a distinctive name, such as `segmented.laz` or `dtm.tif`, so later stages can find it reliably. Declare `dependsOn` for any stage whose output the job reads but that did not produce the trigger file, so that output exists before the job starts.

### Example – An Inspection Stage Whose Findings Use the Run’s Own Thresholds
<a name="pattern-inspection-findings"></a>

The last stage of a pipeline is often the one people act on. In a power line corridor, for example, it measures how close each tree comes to the conductors and flags the trees that break a clearance rule. The rule is a setting, such as 1.5 meters, and a reviewer needs to know which setting produced the result they are looking at.

The following connector is stage 5 of the example pipeline. It runs one AWS Deadline Cloud job, and a single run setting does three jobs:
+  **It drives the job.** The two clearance zones are trigger parameters, and the job receives them as job parameters.
+  **It is recorded on the run.** SDMA records the parameter values with the run, and each output records the run that made it.
+  **It draws the result.** The viewer’s thresholds, slider presets, and colors come from the values that the run used, not from today’s configuration. If someone later changes the default, earlier results still draw with the values that produced them.

The job writes three outputs, each for a different audience:

| Output | For | How the connector declares it |
| --- | --- | --- |
|  `.geojson`  | People reviewing the result in the point cloud viewer | A sibling derived file with a `presentation` block. See [Drawing a Run’s Findings in the Viewer](connector-configuration.md#output-presentation). |
|  `.gpkg`  | GIS tools and work-order systems | A sibling derived file |
|  `.json` report | Search, filters, and dashboards | Counts and measurements mapped to attributes, each with a `role`. See [Saying What a Value Means](connector-configuration.md#field-mapping-role). |

```json
{
  "schemaVersion": "1.0.0",
  "name": "Vegetation encroachment audit",
  "description": "Measure each tree's clearance to the reconstructed conductors, flag trees that break the clearance zones, and write the findings for review, for GIS, and as searchable attributes.",
  "deadlineConfig": {
    "farmId": "<farm-id>",
    "queueId": "<queue-id>",
    "templateProjectId": "<template-project-id>",
    "templateAssetId": "<template-asset-id>",
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentDerivation-Inspection"
    }
  },
  "triggers": [
    {
      "description": "Audit tree clearance when the instance point cloud arrives.",
      "resources": ["derivedFile"],
      "events": ["upload", "onDemand"],
      "filter": { "fileExtensionFilter": ".ply", "fileNameRegex": ".*instance.*" },
      "dependsOn": ["<segmentation-connector-id>", "<terrain-connector-id>"],
      "parameterDefinitions": {
        "Zone1ClearanceMeters": {
          "type": "number",
          "default": 1.5,
          "displayName": "Zone 1 clearance (m)",
          "description": "Clearance at or below which a tree is a Zone 1 violation.",
          "required": false
        },
        "Zone2ClearanceMeters": {
          "type": "number",
          "default": 3,
          "displayName": "Zone 2 clearance (m)",
          "description": "Clearance at or below which a tree is a Zone 2 grow-in risk.",
          "required": false
        }
      },
      "deadlineJob": {
        "template": "encroachment_template.yaml",
        "parameters": {
          "Standard": "<your clearance standard>",
          "Zone1ClearanceMeters": "${parameters.Zone1ClearanceMeters}",
          "Zone2ClearanceMeters": "${parameters.Zone2ClearanceMeters}"
        },
        "output": {
          "metadataAttributes": {
            "filter": { "fileExtensionFilter": ".json" },
            "fieldMappings": [
              { "role": "finding", "source": "detections.tree.count", "target": "derivedFile.metadataAttributes.assessedTreeCount:number" },
              { "role": "finding", "source": "detections.encroachment.count", "target": "derivedFile.metadataAttributes.encroachmentCount:number" },
              { "role": "finding", "source": "detections.zone1Violation.count", "target": "derivedFile.metadataAttributes.zone1ViolationCount:number" },
              { "role": "finding", "source": "detections.fallInRisk.count", "target": "derivedFile.metadataAttributes.fallInRiskCount:number" },
              { "role": "finding", "source": "detections.needsReview.count", "target": "derivedFile.metadataAttributes.needsReviewCount:number" },
              { "role": "finding", "source": "processing.worstClearanceMeters", "target": "derivedFile.metadataAttributes.worstClearanceM:number" },
              { "role": "provenance", "source": "standard", "target": "derivedFile.metadataAttributes.clearanceStandard" },
              { "role": "provenance", "source": "sourceModels", "target": "derivedFile.metadataAttributes.sourceModels" }
            ]
          },
          "siblingDerivedFiles": [
            { "filter": { "fileExtensionFilter": ".gpkg" } },
            {
              "filter": { "fileExtensionFilter": ".geojson" },
              "preview": true,
              "presentation": {
                "title": "Corridor findings",
                "thresholds": [
                  { "id": "zone1", "label": "Zone 1", "parameter": "Zone1ClearanceMeters", "direction": "atOrBelow", "color": "#ff3b30" },
                  { "id": "zone2", "label": "Zone 2", "parameter": "Zone2ClearanceMeters", "direction": "atOrBelow", "color": "#ff9f0a" }
                ],
                "layers": [
                  {
                    "id": "conductors",
                    "label": "Conductors",
                    "visible": true,
                    "filter": { "properties": { "feature_type": "conductor_span" } },
                    "colorBy": { "property": "vertex_clearance_m", "thresholds": ["zone1", "zone2"] },
                    "fields": ["span_id", "min_clearance_m", "sag_m"],
                    "summary": "{count} spans reconstructed from detected wires"
                  },
                  {
                    "id": "tree-clearance",
                    "label": "Tree clearance",
                    "visible": true,
                    "filter": { "properties": { "feature_type": "tree" } },
                    "colorBy": { "property": "clearance_m", "thresholds": ["zone1", "zone2"] },
                    "draw": { "box": { "property": "bbox_3d", "style": "solid" }, "segment": "clearance_segment" },
                    "measure": {
                      "property": "clearance_m",
                      "label": "Closer than",
                      "unit": "m",
                      "min": 0,
                      "max": 5,
                      "labelCount": 5,
                      "presets": ["zone1", "zone2"],
                      "default": "zone1"
                    },
                    "fields": ["tree_id", "clearance_m", "height_m"],
                    "summary": "{count} of {total} trees within {measure} · closest {min}"
                  },
                  {
                    "id": "fall-in",
                    "label": "Fall-in risk",
                    "visible": false,
                    "color": "#bf5af2",
                    "filter": { "properties": { "feature_type": "tree", "fall_in_risk": true } },
                    "draw": { "box": { "property": "bbox_3d", "style": "outline" }, "segment": "strike_segment" },
                    "summary": "{count} trees tall enough to strike a conductor"
                  },
                  {
                    "id": "needs-review",
                    "label": "Needs review",
                    "visible": false,
                    "color": "#64d2ff",
                    "filter": { "properties": { "feature_type": "tree", "needs_review": true } },
                    "draw": { "box": { "property": "bbox_3d", "style": "outline" } },
                    "summary": "{count} findings where observed and reconstructed wires disagree"
                  },
                  {
                    "id": "poles",
                    "label": "Utility poles",
                    "visible": false,
                    "color": "#d1d1d6",
                    "filter": { "properties": { "feature_type": "pole", "supports_conductor": true } },
                    "draw": { "segment": "pole_segment" },
                    "summary": "{count} poles carrying a conductor"
                  }
                ]
              }
            }
          ]
        }
      }
    }
  ]
}
```

Replace `<farm-id>`, `<queue-id>`, `<template-project-id>`, `<template-asset-id>`, `<account-id>`, and the two connector IDs with your values, and `<your clearance standard>` with the rule your program follows.

How the parts work together:

| Part | What it does |
| --- | --- |
|  `filter` and `dependsOn`  | The stage starts on the instance point cloud from stage 4. It also reads the segmentation from stage 1 and a terrain model from another connector, so it waits for both. See [Reading Earlier Stages' Outputs in a Job](#pattern-reading-earlier-outputs). |
|  `parameterDefinitions`  | Declares the two clearance zones. An event run uses the defaults. A reviewer can run the stage on demand with other values to see how the result changes, and each run keeps its own values. |
|  `deadlineJob.parameters`  | Passes the zones to the job with `${parameters.<name>}`, along with fixed settings such as the standard. |
|  `metadataAttributes`  | Maps counts and the worst clearance from the report to typed attributes marked `finding`, so you can search for corridors with Zone 1 violations. `clearanceStandard` and `sourceModels` are marked `provenance`. The report lists the models whose outputs the job combined, so the final result names every model upstream. |
|  `.geojson` with `presentation`  | Draws five layers from one file. Each layer selects features by `feature_type`. Boxes show each tree, and segments show the line from a tree to the nearest conductor. The **Tree clearance** slider jumps to the run’s Zone 1 and Zone 2 values. |
|  `.gpkg`  | Carries the same findings for GIS tools, with no presentation. |

All the outputs are sibling derived files, so they sit next to the earlier stages' outputs under the original scan. For how the viewer draws the result, see [Findings from a Connector Run](view-your-content.md#view-findings).

## Training a Model and Registering It as an Asset
<a name="pattern-train-register"></a>

Training is long-running work that consumes one asset, a dataset, and produces another, a trained model. A connector can start the training, wait for it without holding compute, and register the trained model as a new asset in the project, with the run’s metrics as its metadata. The trained model is then a governed asset like any other: versioned, permissioned, and available to the next connector, such as an evaluation or deployment step.

### Example – Train a Model with an Amazon SageMaker Pipeline
<a name="_example-train-a-model-with-an-amazon-sagemaker-pipeline"></a>

The following connector starts an Amazon SageMaker pipeline on a dataset asset that the caller names. The pipeline writes the trained model’s files and a completion summary to Amazon S3. When the summary appears, SDMA creates the model asset. For more information about pipelines, see [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) in the *Amazon SageMaker AI Developer Guide*.

```json
{
  "schemaVersion": "1.0.0",
  "name": "Train a model",
  "restConfig": {
    "apiBase": "https://api.sagemaker.<region>.amazonaws.com",
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentDerivation-Training"
    }
  },
  "s3Config": {
    "securityConfig": {
      "type": "AssumeRole",
      "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentDerivation-Training"
    }
  },
  "triggers": [
    {
      "resources": ["project"],
      "events": ["onDemand"],
      "parameterDefinitions": {
        "datasetAssetId": { "type": "string", "required": true, "description": "Dataset asset to train on." },
        "newAssetName": { "type": "string", "required": true, "description": "Name for the trained model asset." },
        "maxSteps": { "type": "string", "default": "1000", "description": "Training steps." }
      },
      "steps": [
        {
          "stepType": "s3PutObject",
          "description": "Record the run's parameters beside its outputs.",
          "s3Config": {
            "bucketName": "amzn-s3-demo-bucket",
            "objectKey": "runs/${parameters.connectorInvocationId}/request.json"
          },
          "body": {
            "datasetAssetId": "${parameters.datasetAssetId}",
            "maxSteps": "${parameters.maxSteps}",
            "output": { "s3Prefix": "s3://amzn-s3-demo-bucket/runs/${parameters.connectorInvocationId}/" }
          }
        },
        {
          "stepType": "rest",
          "description": "Start the training pipeline.",
          "method": "POST",
          "path": "/",
          "headers": {
            "Content-Type": "application/x-amz-json-1.1",
            "X-Amz-Target": "SageMaker.StartPipelineExecution"
          },
          "body": {
            "PipelineName": "<pipeline-name>",
            "ClientRequestToken": "${parameters.connectorInvocationId}",
            "PipelineParameters": [
              { "Name": "DatasetAssetId", "Value": "${parameters.datasetAssetId}" },
              { "Name": "RunId", "Value": "${parameters.connectorInvocationId}" },
              { "Name": "MaxSteps", "Value": "${parameters.maxSteps}" }
            ]
          },
          "responseFieldMapping": [
            { "source": "PipelineExecutionArn", "target": "$temp.executionArn" }
          ]
        },
        {
          "stepType": "wait",
          "description": "Wait for the completion summary, then register the trained model.",
          "wait": {
            "timeoutSeconds": 21600,
            "poll": { "type": "output", "intervalSeconds": 60 },
            "failure": { "uri": "s3://amzn-s3-demo-bucket/runs/${parameters.connectorInvocationId}/_FAILED.json" }
          },
          "responseFieldMapping": [
            { "source": "eval_score", "target": "$temp.evalScore" },
            { "source": "training_seconds", "target": "$temp.trainingSeconds" }
          ],
          "output": {
            "metadataAttributes": {
              "uri": "s3://amzn-s3-demo-bucket/runs/${parameters.connectorInvocationId}/_COMPLETE.json"
            },
            "assets": [
              {
                "assetTemplateIds": ["<model-template-id>"],
                "templateId": "<model-template-id>",
                "name": "${parameters.newAssetName}",
                "idempotencyKey": "${parameters.connectorInvocationId}",
                "metadataAttributes": {
                  "dataset_asset_id": "${parameters.datasetAssetId}",
                  "eval_score": "${$temp.evalScore:number}",
                  "training_seconds": "${$temp.trainingSeconds:number}"
                },
                "files": [
                  { "path": "model/model.safetensors", "s3Uri": "s3://amzn-s3-demo-bucket/runs/${parameters.connectorInvocationId}/model/model.safetensors" },
                  { "path": "config/training_run.json", "s3Uri": "s3://amzn-s3-demo-bucket/runs/${parameters.connectorInvocationId}/config/training_run.json" }
                ]
              }
            ]
          }
        }
      ]
    }
  ]
}
```

Replace `<region>`, `<account-id>`, `<pipeline-name>`, and `<model-template-id>` with your values.

How the steps work together:

| Step | What it does |
| --- | --- |
|  `s3PutObject`  | Records the run’s parameters beside its outputs, so anyone can see later how the model was trained. |
|  `rest`  | Calls the SageMaker `StartPipelineExecution` API, signed with Signature Version 4. The run’s ID is the `ClientRequestToken`, so a retry does not start a second run. |
|  `wait`  | Waits up to six hours for the completion summary, and fails at once if the pipeline writes `_FAILED.json` instead. It captures the metrics from the summary into `$temp`, then creates the model asset with those metrics as typed metadata and the pipeline’s output files as the asset’s files. |

The trigger is on the project, so the caller names the dataset with a parameter, and the new asset carries `dataset_asset_id` as metadata. For more information about inline assets, see [Inline Assets from a Wait Step](connector-configuration.md#inline-assets-from-wait).

The connector’s role must allow `sagemaker:StartPipelineExecution` on the pipeline, and `s3:PutObject`, `s3:GetObject`, and `s3:ListBucket` on the bucket. The pipeline’s own role reads the dataset and writes the outputs.

This connector is configuration only. The training code lives in the SageMaker pipeline, and SDMA starts it, waits for it, and registers its result without any code of its own.

## Sending Content to an External Analysis Service and Viewing It in SDMA
<a name="pattern-external-analysis"></a>

Some teams analyze point clouds in an external service, such as a point cloud database or an analytics platform. The service needs the files, and people still want to view the results in SDMA, next to the asset’s other content. One connector does both:
+  **A trigger sends the content out.** When an upload completes, the connector gives the service short-lived links to the asset’s files, waits for the import to finish, and writes the service’s ID for each file back to that file as an attribute. Only this approved connector sends the content, and the run is recorded on the asset.
+  **Two resources read it back, under SDMA access control.** The `tileset` and `tile` discovery operations fetch level-of-detail tiles from the service. The viewer asks SDMA for each tile, in the context of the asset, and never calls the service itself. So SDMA checks every request like any other read of the asset: only people who can open the asset see its tiles, and only through a connector approved on the asset’s template. The service’s credentials stay in SDMA. The point cloud viewer streams the tiles and shows the **LOD tiles** badge.

Because the `tileset` operation sends the IDs of all the files it is asked for, the service can return them as one tileset. That is how you view several point cloud files together in one scene. In the Spatial Data Portal, select several point cloud files and choose **View in 3D**. For more information, see [Point Clouds](view-your-content.md#view-point-clouds).

### Example – Import Point Clouds into an External Service and Stream Them Back as Tiles
<a name="_example-import-point-clouds-into-an-external-service-and-stream-them-back-as-tiles"></a>

The following connector imports the asset’s point cloud files when an upload completes. The asset’s `table_name` attribute names where the service stores them, and its `proj` attribute gives their coordinate reference system.

```json
{
  "schemaVersion": "1.0.0",
  "name": "External point cloud service (import and tiles)",
  "description": "Import point cloud files into an external service on upload, wait for the import to finish, then write each file's external ID back to the file. Stream the files back to the viewer as tiles.",
  "defaultStepConfig": {
    "stepType": "rest",
    "restConfig": {
      "apiBase": "https://api.example.com",
      "securityConfig": {
        "type": "ApiKey",
        "apiKeyLocation": "header",
        "headerName": "Authorization",
        "apiKeyPrefix": "apikey",
        "secretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>",
        "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-Proxy"
      }
    }
  },
  "triggers": [
    {
      "description": "Import point cloud files into the external service when an upload completes.",
      "resources": ["asset"],
      "events": ["uploadComplete", "onDemand"],
      "steps": [
        {
          "stepType": "rest",
          "method": "POST",
          "path": "/api/tables/import",
          "description": "Send the import request with a link to each file.",
          "fieldMappings": [
            { "source": "asset.metadataAttributes.table_name", "target": "table_name" },
            { "source": "asset.metadataAttributes.proj", "target": "table_proj" },
            { "source": "asset.files[*].presignedUrl", "target": "inputs[*].src" },
            { "source": "asset.metadataAttributes.proj", "target": "inputs[*].proj" }
          ],
          "responseFieldMapping": [
            { "source": "table_version", "target": "$temp.table_version" }
          ]
        },
        {
          "stepType": "wait",
          "description": "Poll the import status until the import is ready.",
          "wait": {
            "timeoutSeconds": 7200,
            "poll": {
              "method": "GET",
              "path": "/api/tables/import_status/${$temp.table_version}",
              "intervalSeconds": 30,
              "successWhen": { "status": "ready" },
              "failureWhen": { "status": "failed" }
            }
          }
        },
        {
          "stepType": "rest",
          "method": "POST",
          "path": "/api/query_metadata",
          "description": "Fetch each file's metadata and write its external ID back to the file.",
          "body": {
            "table_names": ["${asset.metadataAttributes.table_name}"],
            "boundary": null,
            "boundary_proj": null,
            "meta_filter": null,
            "classification_filter": null
          },
          "output": {
            "metadataAttributes": {
              "fieldMappings": [
                {
                  "source": "tables.${asset.metadataAttributes.table_name}.file_metadata[*]",
                  "target": "file.metadataAttributes.externalId:string",
                  "correlate": {
                    "resourceField": "file.hash",
                    "responseField": "stripExtension:original_filename"
                  }
                }
              ]
            }
          }
        }
      ]
    }
  ],
  "resources": {
    "tileset": {
      "discover": {
        "type": "rest",
        "method": "GET",
        "path": "/api/tables/3d_tileset",
        "description": "Fetch the tileset hierarchy for progressive point cloud loading.",
        "encodedQueryParam": {
          "param": "p",
          "encoding": "base64json",
          "template": {
            "meta_filter": "${file[*].metadataAttributes.externalId:intArray}",
            "table_name": "${asset.metadataAttributes.table_name}",
            "output_proj": "${asset.metadataAttributes.proj}",
            "boundary": "${params.boundary}",
            "boundary_proj": "${asset.metadataAttributes.proj}",
            "classification_filter": null
          }
        },
        "rawResponse": true
      }
    },
    "tile": {
      "discover": {
        "type": "rest",
        "method": "GET",
        "path": "/api/tables/${params.uri}",
        "description": "Fetch one tile by its content URI from the tileset.",
        "queryParams": { "format": "threejs" },
        "responseFormat": {
          "type": "binary",
          "encoding": "passthrough",
          "mediaType": "application/octet-stream"
        }
      }
    }
  }
}
```

Replace `<region>`, `<account-id>`, and `<secret-name>` with your values, and `api.example.com` and the paths with your service’s API.

How the parts work together:

| Part | What it does |
| --- | --- |
| Import `rest` step | Sends the service a link to each of the asset’s files, and captures the import’s version in `$temp`. |
|  `wait` step | Polls the import status every 30 seconds for up to two hours. It fails at once if the service reports a `failed` status. |
| Metadata `rest` step | Reads the service’s record of each file. The service names each file after the link it read, which is the file’s content hash, so `correlate` matches each record to its SDMA file and writes `externalId` to that file. |
|  `tileset` resource | Sends the service the `externalId` of each file the viewer asks for, and the box the viewer is looking at. It returns the service’s tileset unchanged. |
|  `tile` resource | Fetches each tile the viewer asks for, and returns its bytes directly. |

For more information about the two resource operations, see [Connector Configuration](connector-configuration.md).

## Choosing Where Each Stage Runs
<a name="pattern-placement"></a>

A pipeline can mix step types, so put each stage where its software already runs.

| Run the stage on | When |
| --- | --- |
| An Amazon SageMaker endpoint | The stage is model inference that needs GPUs, and the model is packaged as an endpoint. |
| AWS Deadline Cloud | The stage needs specific software, large local disks, or the outputs of several earlier stages. Examples are format conversion, filtering, and fusion. |
| AWS Lambda | The stage is short custom code that fits within the AWS Lambda limits. |
| A `rest` step | The stage is a call to an external service you already run. |

For example, a segmentation model’s container might not include a point cloud library. Rather than add that library to the model container, a short AWS Deadline Cloud stage converts the model’s output. Each stage stays small, and each runs where its tools are.
