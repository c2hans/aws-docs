---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-fan-out-write-back.html
---

# Processing changed files and writing results back
<a name="connector-fan-out-write-back"></a>

A common integration sends the files an asset version changed to an external system. It then records what that system returned on each file. For example, a publishing service returns a publish ID for every file it accepts, and you want each file in SDMA to carry its own publish ID.

SDMA supports this with one trigger that combines four ideas:
+  **Change filter** (`changeState`) – Limits the connector to the files the version added or modified.
+  **Fan-out** (`applyTo`) – Runs the steps for each file, or for each batch of files, rather than once for the whole asset.
+  **Request mapping** (`fieldMappings` and `payload.fields`) – Shapes what the external system receives.
+  **Correlate write-back** (`output` with `correlate`) – Matches each entry in the response to the file it describes and writes the value onto that file.

The external system only has to answer the request. It does not call back into SDMA, and it does not need SDMA credentials. SDMA writes the results itself.

Filters, `output` blocks, and `${…​}` variables work the same way for every connector type. For more information, see [Trigger filters](connector-configuration.md#trigger-filters), [Output routing](connector-configuration.md#output-routing), and [Variable substitution](connector-configuration.md#variable-substitution).

## Example – Publishing changed files and writing back publish IDs
<a name="fan-out-example"></a>

The following connector publishes changed files through an AWS Lambda function in batches of up to 500, and writes each returned publish ID to the matching file’s `publishId` attribute:

```
{
  "schemaVersion": "1.0.0",
  "name": "Publish changed files",
  "description": "Sends the files each version changed to a publishing service and records the publish ID it returns on each file.",
  "securityConfig": {
    "type": "AssumeRole",
    "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-<suffix>"
  },
  "lambdaConfig": {
    "region": "<region>",
    "functionArn": "arn:aws:lambda:<region>:<account-id>:function:<publish-function>"
  },
  "fieldMappings": [
    { "source": "asset.assetId", "target": "Asset ID" },
    { "source": "files[*].objectKey", "target": "S3 Objects[*].Asset Key" },
    { "source": "files[*].hash", "target": "S3 Objects[*].File Hash" }
  ],
  "triggers": [
    {
      "description": "Publish changed files and write each publish ID back to its file.",
      "resources": ["asset"],
      "events": ["create", "update"],
      "filter": {
        "changeState": ["added", "modified"]
      },
      "applyTo": {
        "resource": "file",
        "scope": "all",
        "filter": {
          "changeState": ["added", "modified"]
        },
        "batchSize": 500,
        "onError": "record-and-continue"
      },
      "steps": [
        {
          "stepType": "lambdaInvoke",
          "payload": {
            "fields": ["Asset ID", "S3 Objects"]
          },
          "output": {
            "metadataAttributes": {
              "fieldMappings": [
                {
                  "source": "publishedFiles[*]",
                  "target": "file.metadataAttributes.publishId:string",
                  "correlate": {
                    "responseField": "file_hash",
                    "resourceField": "file.hash",
                    "valueField": "publishId"
                  }
                }
              ]
            }
          }
        }
      ]
    }
  ]
}
```

The sections below explain each part.

## Selecting the files a version changed
<a name="fan-out-change-filter"></a>

 `changeState` compares the triggering version with the version immediately before it. Each file is `added` (new in this version), `modified` (same path, different content), or neither. The example accepts `added` and `modified`, so unchanged files are left alone.

The filter appears twice, and each copy has its own job:

| Where | What it does |
| --- | --- |
|  `filter` on the trigger | Decides **whether the trigger matches the event**. On an asset trigger, it matches only if at least one file does. |
|  `filter` on `applyTo`  | Decides **which files the steps run over**. |

If you leave out `applyTo.filter`, the steps run over the files the trigger filter matched. The example states both so the intent is visible in the configuration.

Because the trigger matches only when files changed, an update that changes only metadata does not run the connector. This includes the connector’s own write-back, so the connector does not trigger itself.

**Important**
 `changeState` looks back one version only. Suppose a version’s publish failed, and a later version is created before you re-run it. The later version’s change set then excludes the files from the failed version, and the connector skips them. To catch up, add a second trigger on `onDemand` without the `changeState` filter, so a manual run covers every file.

## Running the steps for each file or batch
<a name="fan-out-apply-to"></a>

Use `applyTo` when you need a separate result for each file, or when the external system accepts files one at a time or in groups. Without `applyTo`, a trigger’s steps run once for the whole asset. With `applyTo`, they run once for each item in a collection.

| Field | Meaning |
| --- | --- |
|  `resource`  | The collection to iterate: `file` or `derivedFile`. |
|  `scope`  | Which members of the collection to consider. Only `all` is supported. |
|  `filter`  | Which members the steps run over. For more information, see the preceding section. |
|  `batchSize`  | How many items each run of the steps receives. Defaults to `1`. |
|  `concurrency`  | How many runs of the steps happen at the same time. Defaults to `1`, maximum `16`. |
|  `onError`  | What happens when one run fails: `fail` (default) stops the fan-out, `record-and-continue` records the failure and moves on. |
|  `circuitBreakerThreshold`  | With `record-and-continue`, the number of consecutive failures that stops the fan-out. Defaults to `5`. |

### What a step sees
<a name="_what-a-step-sees"></a>

With `batchSize` of `1`, each run of the steps receives one file under the name `file`. Your mappings then use `file.hash`, `file.path`, and so on.

With `batchSize` greater than `1`, each run receives a list of files under the plural name `files`. Your mappings then use `files[].hash `. The example maps `files[` and `files[*].hash` because each function call receives up to 500 files.

Batching suits a service that accepts many files in each request. A changed version of 2,000 files becomes four calls instead of 2,000.

### How runs are recorded
<a name="fan-out-invocations"></a>

A fan-out records one parent invocation for the trigger, and one child invocation for each file.

| Invocation | Recorded on | What it holds in `context`  |
| --- | --- | --- |
| Parent | The resource whose event matched, such as the asset | Counters for the whole fan-out |
| Child | The file the item is |  `parentInvocationId`, the parent’s ID, and `applyToItemIndex`, the file’s position in the collection |

Each file therefore shows its own run in the file’s connector invocations, in the Spatial Data Portal and in the `connectorInvocations` field of `GetFile`. A child invocation has the same `eventCorrelationId` as its parent. With batching, each file in a batch still has its own child, and the files in one batch share that batch’s outcome.

The parent’s counters depend on batching:

| Batching | Counters |
| --- | --- |
|  `batchSize` of `1`  |  `applyToTotalItems`, `applyToSucceededItems`, `applyToFailedItems`  |
|  `batchSize` greater than `1`  |  `applyToBatchSize`, `applyToTotalBatches`, `applyToSucceededBatches`, `applyToFailedBatches`, `applyToTotalItems`  |

The parent ends `SUCCEEDED` only if every item or batch succeeded. Otherwise, it ends `FAILED`, and the counters show how many failed. With `record-and-continue`, a failed batch does not stop the others. If the circuit breaker stops the fan-out, the parent’s `context` also includes `applyToCircuitBreakerTripped`, and items that never ran count as failed.

When the steps include a `wait`, the parent stays `IN_PROGRESS` until every child that started has finished. For more information, see [Steps that wait for each file](#fan-out-wait).

### Steps that wait for each file
<a name="fan-out-wait"></a>

When the steps include a `wait`, each file runs as its own connector invocation. Each one sends its request, waits for its own result, and resumes independently. No compute is held while the files wait.

The same pattern applies to any collection of files that each needs its own long-running job, such as video clips, scenes to render, or 3D models to optimize. For example, a connector can send each `.mp4` in an asset to an external processing system, wait for each processed file to appear in Amazon S3, and create a new asset from each result:

```
{
  "resources": ["asset"],
  "events": ["onDemand"],
  "filter": { "fileExtensionFilter": ".mp4" },
  "applyTo": { "resource": "file", "scope": "all", "concurrency": 4, "onError": "record-and-continue" },
  "steps": [
    {
      "stepType": "s3PutObject",
      "s3Config": { "objectKey": "requests/${parameters.connectorInvocationId}/${file.hash}/request.json" }
    },
    {
      "stepType": "wait",
      "wait": {
        "timeoutSeconds": 3600,
        "poll": { "type": "output", "intervalSeconds": 30 },
        "failure": { "uri": "s3://amzn-s3-demo-bucket/errors/${parameters.connectorInvocationId}/${file.hash}" }
      },
      "output": {
        "assets": [
          {
            "assetTemplateIds": ["<processed-template-id>"],
            "templateId": "<processed-template-id>",
            "name": "${asset.assetName} - processed - ${file.hash}",
            "idempotencyKey": "${file.hash}",
            "files": [
              { "path": "${file.path}", "s3Uri": "s3://amzn-s3-demo-bucket/outputs/${parameters.connectorInvocationId}/${file.hash}/output.mp4" }
            ]
          }
        ]
      }
    }
  ]
}
```

Here `${parameters.connectorInvocationId}` is the ID of the run, and `${file.hash}` tells the files apart, so every file gets its own request and output paths. `${file.hash}` alone would not be enough: a later run would find the earlier output already in place. Each new asset records lineage back to the source asset and the `.mp4` it came from (see [Lineage from an asset trigger](connector-configuration.md#asset-lineage)).

How this differs from steps that do not wait:

|  | Steps without a `wait`  | Steps with a `wait`  |
| --- | --- | --- |
| Where items run | Together, in one invocation | Each in its own invocation |
|  `concurrency`  | Items processed at the same time | Items in flight at the same time, including those waiting |
| How long it can take | Bounded by one invocation’s time limit | Each item can wait up to its `timeoutSeconds`  |
| When the trigger’s invocation ends | When its steps finish | When every item’s invocation has finished |

With a `wait`, these are not supported: `batchSize` greater than `1`, `source`, `wait.externalCompletion`, and writing metadata back to the triggering asset.

**Note**
An item’s invocation that stops before its wait is saved — for example, because its function was stopped — leaves the trigger’s invocation `IN_PROGRESS`. This is the same behavior as a single `wait` step, but such an item also holds one of the `concurrency` slots.

## Shaping the request
<a name="fan-out-request"></a>

The connector-level `fieldMappings` build the request body. Each mapping copies a value from SDMA into a named field:
+  `asset.assetId` becomes `Asset ID`.
+ Each file’s `objectKey` and `hash` become one entry in the `S3 Objects` list, as `Asset Key` and `File Hash`.

 `payload.fields` on the step chooses which mapped fields are sent. Here, both `Asset ID` and `S3 Objects` are sent. For a batch of two files, the following JSON shows the request body the Lambda function receives:

```
{
  "Asset ID": "asset-<id>",
  "S3 Objects": [
    { "Asset Key": "<object-key-1>", "File Hash": "<hash-1>" },
    { "Asset Key": "<object-key-2>", "File Hash": "<hash-2>" }
  ]
}
```

Field names can contain spaces, so you can match the external system’s own field names exactly.

## Writing results back to each file
<a name="fan-out-correlate"></a>

The function’s response describes the files it handled, but not in SDMA’s terms. A correlate mapping connects the two. The following JSON shows an example response returned by the function:

```
{
  "publishedFiles": [
    { "file_hash": "<hash-1>", "publishId": "pub-001" },
    { "file_hash": "<hash-2>", "publishId": "pub-002" }
  ]
}
```

The following table explains each part of the mapping.

| Part | Meaning |
| --- | --- |
|  `source: publishedFiles[*]`  | Go through each entry in the `publishedFiles` list. |
|  `correlate.responseField: file_hash`  | In each entry, `file_hash` says which file the entry is about. |
|  `correlate.resourceField: file.hash`  | Match that value against each file’s hash. |
|  `correlate.valueField: publishId`  | Take the entry’s `publishId` as the value to write. |
|  `target: file.metadataAttributes.publishId:string`  | Write it to the matched file’s `publishId` attribute, as a string. |

So the file with hash `<hash-1>` gets `publishId` `pub-001`, and the file with hash `<hash-2>` gets `pub-002`. SDMA skips an entry that matches no file. SDMA leaves a file unchanged if the response does not mention it.

Matching on `file.hash` is reliable because the request sent each file’s hash, and the function echoes it back. You can match on `file.path` instead if the external system works with paths.

For more information about correlate options, see [Correlate mapping](connector-configuration.md#correlate-mapping).

## Why write back through output routing
<a name="fan-out-why-output"></a>

You can write results back to an asset in two ways, and both are supported:
+  **Declaratively**, by giving the step an `output` block, as in the example. SDMA writes the values.
+  **Directly**, by having the external system or your function call the SDMA API or SDK (for example, `UpdateAsset`) with its own credentials.

Direct writes are a good fit for systems that act on their own schedule, such as an editing tool or a nightly job. When the values come back as the **result of a connector step**, output routing is usually the better choice. This is because of how SDMA versions assets.

### How versions relate to writes
<a name="_how-versions-relate-to-writes"></a>

An asset’s history is a list of versions. Each version records a consistent state of the asset: its files and its metadata at one moment.

Metadata and derived content are only meaningful alongside the content they describe. A publish ID, a quality score, or a converted preview belongs to the files it was produced from. Output routing keeps them together: what a connector run writes is carried with the content version it relates to. Direct writes cannot do this, because each write is a separate change that creates a version of its own.
+ Each direct update is its own change. It adds a new version to the asset’s history, and it raises an `update` event that other connectors subscribed to `update` respond to.
+ Writes made through output routing belong to the connector run that produced them. SDMA coalesces them, so everything one run writes lands together on the asset instead of as a series of separate changes. Metadata a run writes joins the current version. Files a run adds form exactly one new version, however many steps or batches produced them.

Consider a version that changes 2,000 files, published in batches of 500. The following table compares how each kind of write behaves in that case.

|  | Written through output routing | Written directly through the API or SDK |
| --- | --- | --- |
| Writes to the asset | Grouped by SDMA; batches are written together under the asset’s lock | One for each call your code makes, each separate |
| Asset history | The publish IDs join the current version | Each call adds a version |
|  `update` events | One, after the asset’s connector runs finish | One for each call, so subscribed connectors run each time |
| Link to the run | Counted on the connector invocation that wrote it | Recorded against the caller’s identity |
| Partial failure | A batch counts as succeeded only once its write-back is saved, so the counters stay true | Your code tracks which calls succeeded |
| Credentials | None needed by the external system | The writer needs SDMA access |

In short, output routing keeps metadata and derived content with the content version they describe, and keeps the asset’s history about what **people and processes changed** rather than each step of how a connector reported back. Reviewers see one coherent version, downstream connectors react once, and every value can be traced to the run that wrote it.

**Tip**
If your function already calls the SDK to write results back, you can usually move that logic into the response instead. Return the values in the function’s response, add an `output` block with a correlate mapping, and remove the SDK call. The function becomes simpler, and it no longer needs SDMA credentials.

Output routing works the same way for every step type that returns a response, including `rest` and `lambdaInvoke` steps, and for Deadline Cloud jobs. For more information about output routing, see [Output routing](connector-configuration.md#output-routing).

## Writing the Lambda function
<a name="fan-out-lambda-contract"></a>

The function in this example must do only three things:

1. Read `Asset ID` and the `S3 Objects` list from the event.

1. Do its work for each file. Read file content, if needed, by the `Asset Key` in the asset’s bucket.

1. Return a `publishedFiles` list with one entry for each file it handled, each carrying the `file_hash` it received and the value to record.

The following Python code example shows a minimal Lambda handler:

```
import logging

logger = logging.getLogger()

def handler(event, context):
    published = []
    for obj in event["S3 Objects"]:
        try:
            publish_id = publish(event["Asset ID"], obj["Asset Key"])  # your logic
        except Exception:
            # Leave the file out so it keeps its previous value.
            logger.exception("Failed to publish %s", obj["Asset Key"])
            continue
        published.append({"file_hash": obj["File Hash"], "publishId": publish_id})
    return {"publishedFiles": published}
```

Leave a file out of `publishedFiles` if the function could not handle it. That file keeps its previous value, and the next run that includes it can try again.

The connector’s role must allow `lambda:InvokeFunction` on the function. For more information about the role setup, see [AWS Lambda connector](connector-lambda.md).

## Considerations
<a name="fan-out-considerations"></a>
+  **Batch size.** Choose a `batchSize` the external system can handle in one request, within the Lambda function’s time and payload limits.
+  **Failures.** With `record-and-continue`, one failed batch does not stop the rest. Use `fail` when a partial result is worse than none.
+  **Approving the connector.** Because the trigger writes to file metadata, approve the connector on the asset template, as for any connector with an `output` block. For more information, see [Connectors, templates, and projects](connectors-overview.md#connector-blast-radius).
