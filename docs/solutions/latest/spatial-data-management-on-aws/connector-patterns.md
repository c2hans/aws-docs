---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-patterns.html
---

# Connector patterns for models and pipelines
<a name="connector-patterns"></a>

This topic describes patterns for training and running machine learning models, and for multi-stage processing pipelines, with connectors. The models and pipelines can work on any spatial content, such as point clouds, imagery, 3D models, or sensor recordings. Each pattern uses only the connector features described in [Connector configuration](connector-configuration.md), [Working with wait steps](connector-wait.md), and [Create and transform content with AWS Deadline Cloud](connector-deadline-cloud.md). Together, they show how several connectors, each approved and versioned independently, build one governed result on an asset.

Filters, `output` blocks, `${…​}` variables, `$temp` values, and type suffixes such as `:number` work the same way for every connector type. For more information, see [Trigger filters](connector-configuration.md#trigger-filters), [Output routing](connector-configuration.md#output-routing), [Variable substitution](connector-configuration.md#variable-substitution), [Intermediate state with $temp variables](connector-configuration.md#temp-variables), and [Type coercion](connector-configuration.md#type-coercion).

## Running inference on an Amazon SageMaker asynchronous endpoint
<a name="pattern-sagemaker-async"></a>

An Amazon SageMaker asynchronous inference endpoint suits models that take minutes to run on large inputs, such as point clouds or imagery. You send the endpoint the Amazon S3 location of a request. The endpoint returns at once with the locations where it will write the result and, if the request fails, an error. For more information, see [Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) in the *Amazon SageMaker AI Developer Guide*. A connector expresses this in three steps:

1. An `s3PutObject` step writes the request document to Amazon S3.

1. A `rest` step calls the endpoint’s `async-invocations` operation and captures the two locations from the response headers into `$temp` variables.

1. A `wait` step polls for the result at the captured output location, and fails at once if the error appears at the captured failure location.

### Example – segment a point cloud with a SageMaker asynchronous endpoint
<a name="_example-segment-a-point-cloud-with-a-sagemaker-asynchronous-endpoint"></a>

The following connector runs a segmentation model on each uploaded `.las` file. It ingests the model’s output point cloud as a derived file and records the model’s summary on the source file.

```
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
          "path": "/endpoints/<endpoint-name>/async-invocations",
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
                { "source": "model.modelVersion", "target": "file.metadataAttributes.segmentationModelVersion" },
                { "source": "processing.elapsedSeconds", "target": "file.metadataAttributes.segmentationSeconds:number" },
                { "source": "model.modelVersion", "target": "derivedFile.metadataAttributes.modelVersion" }
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
|  `rest`  | Calls the endpoint. SDMA signs the request with Signature Version 4 for SageMaker, because the host name contains `sagemaker`. SageMaker returns the output and failure locations in response headers, not in the body. A `responseFieldMapping` source of `responseHeaders.<header-name>`, in lowercase, captures a response header. |
|  `wait`  | Polls for the summary file at `$temp.outputLocation`. It reads that file as the source for `fieldMappings`, and ingests the `.laz` files under the job prefix as derived files. If the endpoint writes an error to `$temp.failureLocation` first, the wait fails at once with the error as its reason. |

Passing the run’s ID as `X-Amzn-SageMaker-InferenceId` lets you match an endpoint’s logs to the connector invocation.

This connector is configuration only. There is no function to write or deploy between SDMA and the endpoint: SDMA signs the call, waits for the result without holding compute, and ingests the output.

### Permissions
<a name="_permissions"></a>

The connector’s role must allow `sagemaker:InvokeEndpointAsync` on the endpoint. It must also allow `s3:PutObject` for the request, and `s3:GetObject` and `s3:ListBucket` for the result and error locations. The endpoint’s own execution role reads the request and input file, and writes the result. For more information about connector roles, see [IAM role naming](connector-configuration.md#security-role-naming).

## Recording which model produced a result
<a name="pattern-model-provenance"></a>

When a model’s output becomes part of an asset, record which model produced it. Then anyone who reads the result, later or in another system, can tell how it was made.

Two features make this simple:
+  **A parameter for the model version.** Declare a parameter such as `modelVersion` with a `default`. Pass it to the model in the request, and map it back from the model’s response. Someone who runs the connector on demand can choose another version. For more information, see [Trigger parameters](connector-configuration.md#trigger-parameters).
+  **Separate targets for facts about the input and facts about the output.** A field mapping target that starts with `file.` writes to the file that matched the trigger. A target that starts with `derivedFile.` writes to the derived files the step produced.

| Target | Lands on | Use it for |
| --- | --- | --- |
|  `file.metadataAttributes.<name>`  | The source file | Facts about the source, such as how many points of each class it contains |
|  `derivedFile.metadataAttributes.<name>`  | Each derived file the step ingested | Facts about the output, such as which model version made it |

Facts about an output belong on the output. If you record the model version only on the source file, the next run against that file, perhaps with another model, overwrites it. On the derived file, the version stays with the result it describes.

## Example – a multi-model pipeline
<a name="pattern-pipeline"></a>

A pipeline turns one upload into a result that no single model produces. Build each stage as its own connector, and let the stages compose through the asset record: each stage’s derived file raises an `upload` event that starts the next.

The following example analyzes a point cloud in five stages. Stage 1 has a `file` trigger on `upload`. Stages 2 to 5 each have a `derivedFile` trigger on `upload`, and match only the file the previous stage produced, using `fileNameRegex`. For more information, see [Chaining connectors](connector-configuration.md#chaining-connectors).

| Stage | Runs on | Matches | Produces |
| --- | --- | --- | --- |
| 1. Semantic segmentation | SageMaker asynchronous endpoint | An uploaded `.las` file |  `segmented.laz`, with a class for each point |
| 2. Format conversion | AWS Deadline Cloud |  `segmented.laz`  |  `segmented.copc.laz`, a streamable preview |
| 3. Filter | AWS Deadline Cloud |  `segmented.copc.laz`  |  `vegetation.laz`, only the points stage 4 needs |
| 4. Instance segmentation | SageMaker asynchronous endpoint |  `vegetation.laz`  | An instance point cloud, one ID for each object |
| 5. Fusion | AWS Deadline Cloud | The instance point cloud | A report that combines stages 1 and 4 with terrain data from another connector |

```
upload .las ──> 1 segmentation ──> 2 conversion ──> 3 filter ──> 4 instances ──> 5 fusion
                     │                 │                │              │              │
                     └─────────────────┴── derived files of the .las ──┴──────────────┘
```

Patterns that make the pipeline work:
+  **Keep every stage’s output beside the source.** Stages 2 to 5 each match a derived file, and declare their output with `siblingDerivedFiles` rather than `derivedFiles`. All stages' outputs then sit side by side as derived files of the original `.las`, rather than in a chain nested five levels deep. For more information, see [Placing derived files alongside their source](connector-configuration.md#sibling-derived-files).
+  **Order stages that read more than their trigger.** A stage that reads outputs other than the one that matched it can declare `dependsOn` for the connectors that produce them. For more information, see [Ordering connectors with dependsOn](connector-configuration.md#trigger-dependencies).
+  **Write the result as metadata, too.** The fusion stage maps counts and measurements from its report into `derivedFile.metadataAttributes`, so you can search for and filter the result without opening it.
+  **Approve each stage separately.** Each connector is approved on the asset template, so you can change, turn off, or reuse one stage without touching the others.
+  **Connect stages with configuration, not code.** The models and job scripts are your code, but the connectors that run them, pass outputs between them, and record their results are configuration. Adding or reordering a stage is a connector change, not a deployment.

### Reading earlier stages' outputs in a job
<a name="pattern-reading-earlier-outputs"></a>

A fusion stage needs more than the file that matched its trigger. In the example, stage 5 matches the instance point cloud, but it also needs the stage 1 segmentation and a terrain model from another connector.

An AWS Deadline Cloud job receives these without extra configuration. SDMA attaches the triggering asset to the job, and the files staged on the worker include the derived files that earlier connectors added to that asset. The file that matched the trigger is also passed in the `InputFile` parameter.

Find the other inputs by name or pattern, not by a fixed path. The layout of derived files on the worker is not part of the connector contract, so a path that works today might not work after an update. For example, a job script can search the staged files:

```
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

## Training a model and registering it as an asset
<a name="pattern-train-register"></a>

Training is long-running work that consumes one asset, a dataset, and produces another, a trained model. A connector can start the training, wait for it without holding compute, and register the trained model as a new asset in the project, with the run’s metrics as its metadata. The trained model is then a governed asset like any other: versioned, permissioned, and available to the next connector, such as an evaluation or deployment step.

### Example – train a model with an Amazon SageMaker pipeline
<a name="_example-train-a-model-with-an-amazon-sagemaker-pipeline"></a>

The following connector starts an Amazon SageMaker pipeline on a dataset asset that the caller names. The pipeline writes the trained model’s files and a completion summary to Amazon S3. When the summary appears, SDMA creates the model asset. For more information about pipelines, see [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) in the *Amazon SageMaker AI Developer Guide*.

```
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

The trigger is on the project, so the caller names the dataset with a parameter, and the new asset carries `dataset_asset_id` as metadata. For more information about inline assets, see [Inline assets from a wait step](connector-configuration.md#inline-assets-from-wait).

The connector’s role must allow `sagemaker:StartPipelineExecution` on the pipeline, and `s3:PutObject`, `s3:GetObject`, and `s3:ListBucket` on the bucket. The pipeline’s own role reads the dataset and writes the outputs.

This connector is configuration only. The training code lives in the SageMaker pipeline, and SDMA starts it, waits for it, and registers its result without any code of its own.

## Choosing where each stage runs
<a name="pattern-placement"></a>

A pipeline can mix step types, so put each stage where its software already runs.

| Run the stage on | When |
| --- | --- |
| An Amazon SageMaker endpoint | The stage is model inference that needs GPUs, and the model is packaged as an endpoint. |
| AWS Deadline Cloud | The stage needs specific software, large local disks, or the outputs of several earlier stages. Examples are format conversion, filtering, and fusion. |
| AWS Lambda | The stage is short custom code that fits within the AWS Lambda limits. |
| A `rest` step | The stage is a call to an external service you already run. |

For example, a segmentation model’s container might not include a point cloud library. Rather than add that library to the model container, a short AWS Deadline Cloud stage converts the model’s output. Each stage stays small, and each runs where its tools are.
