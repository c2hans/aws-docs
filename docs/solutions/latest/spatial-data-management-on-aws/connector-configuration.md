---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-configuration.html
---

# Connector configuration
<a name="connector-configuration"></a>

## Triggers
<a name="_triggers"></a>

Triggers define which resource events activate the connector. Each trigger specifies:
+  `resources` – The resource types to match.
+  `events` – The event types to match.
+  `filter` – (Optional) Which files and metadata the trigger matches. See [Trigger filters](#trigger-filters).
+  `stepType` – The type of step to execute (for publish connectors).
+  `steps` – One or more step configurations to execute in order.
+  `applyTo` – (Optional) Runs the steps per file or batch. See [Running steps per file](#trigger-apply-to).
+  `parameterDefinitions` – (Optional) Parameters for on-demand runs. See [Trigger parameters](#trigger-parameters).

### Supported resources
<a name="trigger-resources"></a>

The following resource types can activate a trigger.

| Resource | Description |
| --- | --- |
|  `project`  | Triggered when a project is created, updated, or deleted. Project-scoped triggers can produce assets via the `assets` output target without requiring a triggering asset. |
|  `asset`  | Triggered when an asset is created, updated, or deleted. |
|  `file`  | Triggered when a file within an asset is processed. |
|  `derivedFile`  | Triggered when a connector or processing job adds a derived file. With the `upload` event, this is the primary way to chain connectors. For example, an AWS Deadline Cloud job produces a `.glb` preview file, and a publish connector with a `derivedFile` trigger on `upload` publishes it. For more information, see [Chaining connectors](#chaining-connectors). |

### Supported events
<a name="trigger-events"></a>

The following events can activate a trigger.

| Event | Description |
| --- | --- |
|  `create`  | A resource is created. |
|  `update`  | A resource is updated. |
|  `delete`  | A resource is deleted. |
|  `upload`  | A file is added to or updated within an asset. On a `derivedFile` trigger, a connector or processing job added the derived file. |
|  `uploadComplete`  | All files in an asset have finished uploading and the asset is ready. |
|  `derivationComplete`  | A connector run that started from a file succeeded. The event is raised once, on that file, and not on the derived files the run produced. Use it to act on the source file after processing finishes, for example to mark it as processed. To act on the derived files, use `upload` on a `derivedFile` trigger instead. |
|  `onDemand`  | Manually triggered by a user from the Spatial Data Portal or via the API. |

A single trigger can match multiple resources and events. For example, a trigger with `"resources": ["asset"], "events": ["create", "update"]` matches both asset creation and update.

### Trigger filters
<a name="trigger-filters"></a>

A `filter` narrows which events a trigger matches. Filter keys combine with AND, so every key must match. Spatial Data Management on AWS (SDMA) checks the file dimensions first, then metadata. SDMA tests metadata only on files that already passed the dimension check.

#### File dimensions
<a name="_file-dimensions"></a>

Use the following keys to run a trigger only on the files it cares about, such as new `.laz` files or files under a size limit.

| Key | Matches |
| --- | --- |
|  `fileExtensionFilter`  | Matches files with this extension, for example `.laz`. |
|  `fileNameRegex`  | Matches files whose name matches this regular expression, anchored at the start. |
|  `pathRegex`  | Matches files whose full path matches this regular expression, anchored at the start. |
|  `minFileSizeMB` / `maxFileSizeMB`  | Matches files within this size range, in megabytes. |
|  `changeState`  | Matches files that the triggering version `added` or `modified`, compared with the version immediately before it. |

On an asset trigger, `changeState` matches only if at least one file matches. A metadata-only update changes no files. As a result, a connector’s own metadata write-back doesn’t match a `changeState` trigger.

#### Metadata conditions
<a name="_metadata-conditions"></a>

Use `project`, `asset`, or `file` to test metadata attributes on the resource. Each takes a `metadataAttributes` object that maps attribute names to conditions. A bare value tests for equality. An object applies one or more operators, all of which must hold.

The following JSON filter combines a file dimension with asset and file metadata conditions.

```
"filter": {
  "fileExtensionFilter": ".tif",
  "asset": {
    "metadataAttributes": {
      "region": "emea",
      "qcStatus": { "$in": ["approved", "reviewed"] }
    }
  },
  "file": {
    "metadataAttributes": {
      "resolutionCm": { "$lte": 10 },
      "tags": { "$contains": "orthophoto" }
    }
  }
}
```

This trigger matches `.tif` files with a resolution of 10 cm or better and an `orthophoto` tag. The files must also be in assets whose `region` is `emea` and whose `qcStatus` is `approved` or `reviewed`.

| Operator | Holds when |
| --- | --- |
|  `$eq` / `$ne`  | The value equals / does not equal the given value. |
|  `$in`  | A single-valued attribute equals one of the listed values. |
|  `$contains`  | A list-valued attribute contains the given value, or at least one of the listed values. |
|  `$gt`, `$gte`, `$lt`, `$lte`  | The value is greater than, at least, less than, or at most the given value. |
|  `$exists`  |  `true`: the attribute is present. `false`: it is absent. |
|  `$regex`  | The value matches the regular expression anywhere (not anchored, unlike `fileNameRegex` and `pathRegex`). Maximum 512 characters. |

Within one evaluation, project and asset conditions give the same result for every file. SDMA checks file conditions file by file.

### Trigger parameters
<a name="trigger-parameters"></a>

A trigger can declare the parameters a caller supplies when running it on demand, with `parameterDefinitions`. SDMA validates the caller’s values before the trigger runs, and steps read them as `${parameters.<name>}`.

The following JSON declares three parameters.

```
"parameterDefinitions": {
  "outputFormat": {
    "type": "string",
    "allowedValues": ["glb", "usdz"],
    "default": "glb",
    "description": "Format to convert to"
  },
  "lodLevels": {
    "type": "number",
    "multipleValues": true,
    "minItems": 1,
    "maxItems": 4,
    "min": 0,
    "max": 8
  },
  "notifyEmail": { "type": "string", "required": true }
}
```

| Field | Meaning |
| --- | --- |
|  `type`  | Required. `string`, `number`, `boolean`, or `date`. |
|  `multipleValues`  | When `true`, the parameter takes a list of values of that type. |
|  `required`  | When `true`, the caller must supply the parameter. Cannot be combined with `default`. |
|  `default`  | The value used when the caller leaves the parameter out. Must match the type and constraints. |
|  `allowedValues`  | The only values accepted. |
|  `min` / `max`  | Bounds for a number. |
|  `minItems` / `maxItems`  | Bounds on the number of values, when `multipleValues` is `true`. |
|  `description`  | Shown to users who run the connector. |

Parameter names start with a letter and contain only letters, digits, and underscores. Callers pass values in the `parameters` field of the trigger API, or through the Spatial Data Portal.

### Running steps per file
<a name="trigger-apply-to"></a>

By default, a trigger’s steps run once for the resource whose event matched. Add `applyTo` to run them once for each file or derived file instead, or once for each batch of files. For example, a Deadline Cloud trigger with `applyTo` submits one job for each matching file, and a REST trigger with `"batchSize": 100` sends files to an API 100 at a time.

The following JSON shows an `applyTo` block.

```
"applyTo": {
  "resource": "file",
  "scope": "all",
  "batchSize": 100,
  "concurrency": 4,
  "onError": "record-and-continue"
}
```

In this example, each run of the steps receives up to 100 files (`batchSize`), and up to four runs happen at the same time (`concurrency`). The steps see one item as `file` (or `derivedFile`), or a batch as `files` (or `derivedFiles`).

 `onError` sets what happens when a run fails:
+  `fail`, the default, stops the fan-out at the first failed run.
+  `record-and-continue` records the failure and runs the remaining items. After `circuitBreakerThreshold` failures in a row (default `5`), the fan-out stops anyway.

Either way, the invocation ends `FAILED` if any run failed, and it records how many items or batches succeeded and failed. For every field, how filters apply to the iteration, and a worked example that writes results back to each file, see [Processing changed files and writing results back](connector-fan-out-write-back.md).

### Chaining connectors
<a name="chaining-connectors"></a>

The recommended way to chain connectors is through the asset record. One connector adds a derived file. That raises an event, and the next connector’s trigger matches it. Each connector is configured and approved on its own, so you can change or turn off one stage without changing the others.

A connector can also name another connector with `dependsOn`. That makes it wait for the other connector, but it couples the two, and it does not start a run by itself (see [Ordering connectors with dependsOn](#trigger-dependencies)).

Choose the event by what the next connector should act on.

| The next connector acts on | Trigger | Raised |
| --- | --- | --- |
| A derived file the previous connector produced |  `"resources": ["derivedFile"]`, `"events": ["upload"]`  | Once for each derived file, when it is added |
| The file a run started from, after the run succeeded |  `"resources": ["file"]` or `["derivedFile"]`, `"events": ["derivationComplete"]`  | Once for each successful run that started from that file |
| The asset, after its metadata changed |  `"resources": ["asset"]`, `"events": ["update"]`  | When the asset is updated |

The following trigger is the second stage of a pipeline. The first stage writes `segmented.laz` as a derived file. This trigger matches only that file, by name, and converts it:

```
"triggers": [
  {
    "resources": ["derivedFile"],
    "events": ["upload"],
    "filter": {
      "fileExtensionFilter": ".laz",
      "fileNameRegex": ".*segmented\\.laz$"
    },
    "deadlineJob": {
      "template": "copc/template.yaml",
      "output": {
        "siblingDerivedFiles": [
          { "filter": { "fileExtensionFilter": ".copc.laz" }, "preview": true }
        ]
      }
    }
  }
]
```

Follow these practices when you chain connectors:
+  **Match each stage’s input by name.** Give each stage’s output a distinctive name, and match it with `fileNameRegex`. A filter on the extension alone can match outputs of other stages, too.
+  **Keep a chain’s outputs beside the original.** A stage that matches a derived file can declare its output with `siblingDerivedFiles`, so all stages' outputs sit side by side under the original file (see [Placing derived files alongside their source](#sibling-derived-files)).
+  **Prefer the asset record to `dependsOn`.** A stage that matches its input file already waits for that file to exist. Use `dependsOn` only when a stage also reads outputs it did not start from, such as a fusion stage that needs a terrain model (see [Ordering connectors with dependsOn](#trigger-dependencies)).
+  **Expect a depth limit.** By default, SDMA follows up to five connector-produced hops from one upload. Further derived files are kept, but they start no more connectors. This stops a connector that matches its own output from running forever.
+  **Chain on `upload`, not `derivationComplete`.** A run started by `derivationComplete` does not raise `derivationComplete` again, so a chain built on that event stops after one hop.

For a five-stage example, see [Example – a multi-model pipeline](connector-patterns.md#pattern-pipeline).

### Ordering connectors with dependsOn
<a name="trigger-dependencies"></a>

When one connector’s work must complete before another connector runs, use `dependsOn` on the downstream trigger. This orders connector execution within the same lifecycle context — the set of work that a single upstream event triggers.

```
"triggers": [
  {
    "description": "Fuse instance results with the terrain model",
    "resources": ["derivedFile"],
    "events": ["upload"],
    "filter": { "fileNameRegex": ".*instance.*\\.ply$" },
    "dependsOn": ["<terrain-connector-id>"],
    "steps": [{ ... }]
  }
]
```

 `dependsOn` takes a list of connector IDs. SDMA evaluates the status of each listed connector within the current lifecycle before dispatching:
+ If all upstream connectors have succeeded (or were not applicable because no trigger matched), the downstream connector is queued normally.
+ If any upstream connector has failed, the downstream connector is marked as `DEPENDENCY_BLOCKED` and does not execute.
+ If upstream connectors are still running, the downstream connector waits until they reach a terminal state.

Rules:
+ Dependencies apply only within a single lifecycle context. A connector does not wait on unrelated invocations from other events.
+ Upstream connectors must be in the same library and must share at least one template association with the dependent connector.
+  `dependsOn` is for ordering between connectors, not a general-purpose workflow mechanism. For ordering within a single connector, use multi-step triggers.

For most chains, you do not need `dependsOn`, because each stage starts only when its input exists (see [Chaining connectors](#chaining-connectors)). Use `dependsOn` only when a stage also needs outputs other than the one that started it.

## Output routing
<a name="output-routing"></a>

When a step completes — whether a REST call, a Lambda invocation, or a Deadline Cloud job — you can route the results back into the asset record. Use an `output` block to do this. Output routing is how connectors write results back to SDMA as governed metadata, derived files, or both.

Output routing works uniformly across all step types. The same `output` block works on REST steps, Lambda steps, and Deadline Cloud jobs. For Deadline Cloud, place the `output` block inside the `deadlineJob` configuration on the trigger (see [Create and transform content with AWS Deadline Cloud](connector-deadline-cloud.md)). The vocabulary is identical regardless of which step type produced the result.

The `output` block supports the following routing targets:

| Target | Description |
| --- | --- |
|  `metadataAttributes`  | Writes response fields to asset or file metadata attributes. Contains a `fieldMappings` array that maps fields from the step response to SDMA metadata paths. Use this to write summary values — counts, scores, timestamps, identifiers — that you want to be searchable, displayable, and available for downstream triggers. |
|  `derivedFiles`  | Ingests files that the step wrote to S3, attaching them as derived files on the asset. Each entry specifies a `filter` to match output files by extension or pattern. Each ingested derived file raises an `upload` event on the `derivedFile` resource, which can start the next connector (see [Chaining connectors](#chaining-connectors)). |
|  `siblingDerivedFiles`  | Ingests files as derived files of the same file the triggering derived file belongs to, alongside it rather than beneath it. Same entry shape as `derivedFiles`. Only valid on triggers with `"resources": ["derivedFile"]`. See [Placing derived files alongside their source](#sibling-derived-files). |
|  `files`  | Ingests files as top-level files on the asset (without a derived-from relationship). Each entry specifies a `filter`. |
|  `assets`  | Creates new assets in the project. Each entry specifies an `assetTemplateIds` list, and either a `filter` that matches envelope files the step produced or, on a `wait` step, one inline asset. Valid on triggers with `"resources": ["project"]` or `"resources": ["asset"]`. On an asset trigger, SDMA records lineage from each new asset back to the triggering asset. See [Creating assets from connector output](#creating-assets). |

### Routing metadata with fieldMappings
<a name="_routing-metadata-with-fieldmappings"></a>

The `metadataAttributes` target uses `fieldMappings` to control which response fields to write and where to write them. Each mapping has a `source` (a field in the step response) and a `target` (an SDMA metadata path). Use `:type` suffixes on targets to store values as typed metadata (see [Type coercion](#type-coercion)).

```
"output": {
  "metadataAttributes": {
    "fieldMappings": [
      { "source": "overallScore", "target": "asset.metadataAttributes.qualityScore:number" },
      { "source": "classification", "target": "asset.metadataAttributes.classification" },
      { "source": "processedAt", "target": "asset.metadataAttributes.lastProcessed:date" }
    ]
  }
}
```

Mappings with `asset. ` targets write to asset-level metadata. Mappings with `file.` targets write to file-level metadata on the triggering file. Mappings with `derivedFile.*` targets write to each derived file the step ingested, so a fact about an output, such as the model version that made it, stays with that output. For more information, see [Recording which model produced a result](connector-patterns.md#pattern-model-provenance). An optional `filter` on `metadataAttributes` narrows which files' attributes the connector processes.

The `metadataAttributes` target also supports an optional `uri` field. When present, SDMA reads the JSON file at that S3 location as the source for `fieldMappings` instead of using the step’s response body directly. This is used with output-driven `wait` steps (see [Working with wait steps](connector-wait.md)): SDMA watches S3 for the file to appear, then reads and maps its contents.

```
"metadataAttributes": {
  "uri": "s3://amzn-s3-demo-bucket/results/${invocation.id}/",
  "filter": { "fileNameRegex": ".*_summary\\.json$" },
  "fieldMappings": [
    { "source": "score", "target": "asset.metadataAttributes.qualityScore:number" }
  ]
}
```

### Combining metadata and derived files
<a name="_combining-metadata-and-derived-files"></a>

A single `output` block can route to multiple targets. This is the canonical pattern when a step produces both summary metadata (for search and display) and detailed output files (for downstream processing or review).

```
"output": {
  "metadataAttributes": {
    "fieldMappings": [
      { "source": "score", "target": "asset.metadataAttributes.qualityScore:number" },
      { "source": "status", "target": "asset.metadataAttributes.analysisStatus" }
    ]
  },
  "derivedFiles": [
    { "filter": { "fileExtensionFilter": ".json" } },
    { "filter": { "fileExtensionFilter": ".glb" }, "preview": true }
  ]
}
```

In this example, the step writes quality scores into asset metadata and ingests `.json` detail files and `.glb` preview files as derived files. The `preview: true` flag marks matched files as preview content in the Spatial Data Portal.

Adding an `output` block does not change how a connector is approved, and you do not change its resources or any other part of its definition. Like every connector, it runs on an asset only when the asset’s template approves it. For the `assets` target, you also need to approve the connector on each template ID listed in `assetTemplateIds`, because it creates assets under those templates. For more information about approving a connector on a template, see [Connector to Asset Template Association](access-control.md#connector-to-asset-template-association).

### Placing derived files alongside their source
<a name="sibling-derived-files"></a>

 `derivedFiles` places output beneath the file that triggered the step. That is right when the output is a child of that file. Sometimes the output is instead another representation of the same original.

For example, an orthophoto `site.tif` has a derived shapefile `site.zip`. A connector converts `site.zip` to GeoJSON. The GeoJSON describes the orthophoto just as the shapefile does, so you place it next to `site.zip`, under `site.tif`, not under `site.zip`. The following JSON configuration declares this with `siblingDerivedFiles` on a trigger on `derivedFile`:

```
"output": {
  "siblingDerivedFiles": [
    { "filter": { "fileExtensionFilter": ".geojson" }, "preview": true }
  ]
}
```

SDMA records the output as derived from the same file as the triggering derived file. SDMA resolves only one level up, so each connector in a chain can independently choose where its output belongs.

### Creating assets from connector output
<a name="creating-assets"></a>

The `assets` target lets a connector create new assets in the project. Use it on a project trigger, for example a Deadline Cloud job that produces assets without an originating asset. You can also use it on an asset trigger, to turn each result of processing an asset into an asset of its own (see [Lineage from an asset trigger](#asset-lineage)).

A step declares new assets in one of two ways:
+  **Envelope files.** The step writes JSON files that describe the assets, and a `filter` selects them.
+  **An inline asset.** A `wait` step describes one asset directly in its `output` block. See [Inline assets from a wait step](#inline-assets-from-wait).

#### Envelope files
<a name="_envelope-files"></a>

Each entry in the `assets` array specifies which templates the connector is allowed to create assets under, and a filter that identifies envelope files in the step output.

```
"output": {
  "assets": [
    {
      "assetTemplateIds": ["<template-id>"],
      "filter": { "fileExtensionFilter": ".json" }
    }
  ]
}
```

Replace `<template-id>` with the ID of the asset template to create assets under.

The connector’s step output must contain asset envelopes — JSON objects with:
+  `idempotencyKey` – A unique key per asset to enable deduplication across retries.
+  `templateId` – Must be listed in `assetTemplateIds`.
+  `name` – The asset name.
+  `metadataAttributes` – (Optional) Metadata to set on the created asset.
+  `manifest` – (Optional) File manifest for the asset.

Before creating the asset, SDMA checks that the user whose event started the run has at least Contributor membership in the project (see [Contributor](access-control.md#contributor)). Each created asset raises a standard `create` lifecycle event (see [Supported events](#trigger-events)).

SDMA combines `idempotencyKey` with the connector invocation ID. A retry within one run does not create a duplicate, but running the connector again creates new assets.

The `assets` output target is valid on project and asset triggers. Declaring it on a file or derived file trigger causes a validation error when you create the connector.

#### Inline assets from a wait step
<a name="inline-assets-from-wait"></a>

A `wait` step has no output files of its own to filter. Instead, its `assets` entry describes the asset to create when the wait completes. Every `${…​}` expression resolves at that point, including `$temp` values the wait captures with `responseFieldMapping` (see [Capturing values from the result](connector-wait.md#wait-capture)).

```
{
  "stepType": "wait",
  "wait": {
    "timeoutSeconds": 21600,
    "poll": { "type": "output", "intervalSeconds": 60 }
  },
  "responseFieldMapping": [
    { "source": "eval_action_mae", "target": "$temp.actionMae" }
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
        "metadataAttributes": { "action_mae": "${$temp.actionMae:number}" },
        "files": [
          { "path": "checkpoint/model.safetensors", "s3Uri": "s3://amzn-s3-demo-bucket/runs/${parameters.connectorInvocationId}/checkpoint/model.safetensors" },
          { "path": "config/training_run.json", "s3Uri": "s3://amzn-s3-demo-bucket/runs/${parameters.connectorInvocationId}/config/training_run.json" }
        ]
      }
    ]
  }
}
```

| Field | Required | Description |
| --- | --- | --- |
|  `assetTemplateIds`  | Yes | The templates this entry may create assets under. |
|  `templateId`  | Yes | The template for the new asset. Must be listed in `assetTemplateIds`. |
|  `name`  | Yes | The new asset’s name. |
|  `idempotencyKey`  | Yes | Prevents a duplicate when SDMA retries within one run. |
|  `metadataAttributes`  | No | Metadata to set on the new asset, subject to the template’s schema. |
|  `files`  | No | The new asset’s files. Each entry has a `path` and an `s3Uri`. SDMA copies each object into the project’s content store and computes its hash and size. |
|  `manifest`  | No | The new asset’s files as an asset-creation manifest. A path entry can give `s3Uri` instead of `hash`, `size`, and `mtime`. Use `files` or `manifest`, not both. |

 `templateId`, `name`, and `idempotencyKey` must be given together. An inline asset cannot also declare a `filter`.

#### Lineage from an asset trigger
<a name="asset-lineage"></a>

When a trigger on an asset creates new assets, SDMA records where each new asset came from. This *lineage* is what allows an asset trigger to create assets outside the asset that matched.

SDMA builds lineage from what it bound for the run, never from the connector configuration or a producer’s response. It writes one `derivedFrom` edge on the history event of the new asset’s first version:

```
"lineage": [
  {
    "kind": "derivedFrom",
    "at": 1793724699,
    "derivedBy": {
      "connectorId": "connector-<id>",
      "connectorInvocationId": "connector-invocation-<id>",
      "eventCorrelationId": "<event-correlation-id>",
      "triggeringUserId": "<user-id>"
    },
    "sources": [
      { "assetId": "asset-<id>", "assetVersionId": "<version-id>" }
    ],
    "files": [
      {
        "target": { "path": "clip01.mp4", "hash": "<new-file-hash>" },
        "sources": [ { "assetId": "asset-<id>", "path": "clip01.mp4", "hash": "<source-file-hash>" } ]
      }
    ]
  }
]
```

| Field | Meaning |
| --- | --- |
|  `derivedBy`  | The connector and the run that created the asset, and the user whose event started it. |
|  `sources`  | The source asset and the version the run read. |
|  `files`  | For a run that processed one source file: each new file, and the source file it came from. |

SDMA owns lineage. On every update, it restores lineage from the previous version, so a client cannot remove, change, or invent it. If you write a client that reads lineage, keep edges whose `kind` you do not recognize. SDMA also records the source asset IDs and the run on the asset’s record, and the source asset and file hash on each file’s record, for lookup.

### Ingesting derived files from an external S3 location
<a name="_ingesting-derived-files-from-an-external-s3-location"></a>

When a step writes output files to S3 and returns the location in its response, you can use `${response.*}` expressions in the `uri` field of a `derivedFiles` entry to ingest those files without hardcoding paths.

The `uri` field supports two forms depending on whether `filter` is present:
+  **S3 object form** (no `filter`) – Ingests a single object at the resolved S3 URI.
+  **S3 prefix form** (with `filter`) – Lists objects under the resolved S3 URI prefix and ingests those matching the filter.

Example — ingest `.png` files from a location returned by a Lambda step:

```
"output": {
  "derivedFiles": [
    {
      "filter": { "fileExtensionFilter": ".png" },
      "uri": "${response.outputLocation}"
    }
  ]
}
```

In this example, the Lambda function returns `{"outputLocation": "s3://my-bucket/renders/job-123/"}` in its response payload. SDMA lists objects under that prefix, filters for `.png` files, copies them into the managed content store, and attaches them as derived files on the asset.

You can also reference a single file directly:

```
"output": {
  "derivedFiles": [
    {
      "uri": "${response.thumbnailUrl}"
    }
  ]
}
```

Supported fields on each `derivedFiles` entry:

| Field | Form | Description |
| --- | --- | --- |
|  `uri`  | Both | S3 URI or S3 URI prefix. Supports `${response.*}` variable substitution. |
|  `filter`  | Prefix only | Narrows which objects under the prefix are ingested. Supports `fileExtensionFilter`, `fileNameRegex`, `minFileSizeMB`, and `maxFileSizeMB`. |
|  `hash`  | In-bucket only | xxh128 hash (32 hex chars). When present, indicates the file is already at the canonical SDMA key — no copy is performed. |
|  `path`  | All | Override the display path for the derived file. |
|  `securityConfig`  | Object and prefix | Per-entry IAM role to assume when reading from the source bucket. Use when the source bucket is in a different account. |

The `uri` and `hash` forms are mutually exclusive. When `hash` is present, SDMA assumes the bytes are already in the managed content store at the canonical key.

## Field mappings
<a name="field-mappings"></a>

Field mappings transform resource metadata into the format expected by the external system. Each mapping specifies a `source` field from the resource metadata and a `target` field name for the output.

```
"fieldMappings": [
  { "source": "project.projectId", "target": "projectId" },
  { "source": "asset.assetName", "target": "name" },
  { "source": "geoJson:asset.geoLocation", "target": "bbox" }
]
```

### Source field prefixes
<a name="field-mapping-source-prefixes"></a>

Source fields must use a resource prefix or a special prefix:

| Prefix | Description |
| --- | --- |
|  `project.`  | Project metadata field (for example, `project.projectId`). |
|  `asset.`  | Asset metadata field (for example, `asset.assetName`, `asset.geoLocation`). |
|  `file.`  | File metadata field (for example, `file.path`, `file.metadataAttributes`). |
|  `system.`  | System-generated field (for example, `system.timestamp`). |
|  `parameters.`  | A parameter supplied when the connector was invoked (for example, `parameters.notifyEmail`). Available only while a trigger is executing. |
|  `invocation.`  | Built-in fields for the current connector invocation: `invocation.id` and `invocation.callbackUrl`. Available only while a trigger is executing. |
|  `geoJson:`  | Extracts a GeoJSON bounding box from a location field (for example, `geoJson:asset.geoLocation`). |
|  `literal:`  | Uses a literal string value (for example, `literal:Feature`, `literal:Point`). |
|  `interpolate:`  | Substitutes one or more `${variable}` expressions inside a static string template (for example, `interpolate:Run ${invocation.id} completed for ${asset.assetName}`). |

**Note**
Flat field references like `projectId` are not allowed. Always use the fully qualified form `project.projectId` to avoid ambiguity.

### Array iteration
<a name="field-mapping-array-iteration"></a>

Field mappings support iterating over arrays using the `[*]` syntax. For example, to map each file in an asset:

```
{ "source": "asset.files[*].path", "target": "assets[${file.path}].title" }
```

This creates one output entry per file, using the file path as the key.

You can define field mappings at the connector level as a default and override them per step when different events require different output shapes.

### Correlate mapping
<a name="correlate-mapping"></a>

When a step response contains a collection (object or array) whose entries correspond to individual files on the asset, use a `correlate` block on a `fieldMapping` to write per-file metadata by matching each response entry to an existing file.

```
"metadataAttributes": {
  "fieldMappings": [
    {
      "source": "tables.${asset.metadataAttributes.table_name}.file_metadata[*]",
      "target": "file.metadataAttributes.external_id:string",
      "correlate": {
        "responseField": "stripExtension:original_filename",
        "resourceField": "file.hash"
      }
    }
  ]
}
```

In this example, the response contains a collection of file metadata entries keyed by identifier. For each entry, SDMA strips the file extension from `original_filename`, matches the result against the `file.hash` of existing files on the asset, and writes the entry’s key as the `external_id` metadata attribute on the matched file.

| Field | Required | Description |
| --- | --- | --- |
|  `responseField`  | Yes | Path within each response entry whose value identifies the file. Supports prefix transforms in canonical form: `stripExtension:field_name`, `basename:field_name`, `tolower:field_name`. |
|  `resourceField`  | Yes | SDMA file field to match against. Supported values: `file.hash`, `file.path`. |
|  `valueField`  | No | Field within each response entry whose value is written to the matched file’s target attribute. Required for list-shaped source collections. For dict-shaped (object) collections, the entry key is used when `valueField` is omitted. |

**Note**
For list-shaped source collections (arrays), `valueField` is required. Without it, there is no meaningful identifier to write and the entry is skipped. For dict-shaped collections (objects), the entry key serves as the default value.

## Payload fields
<a name="payload-fields"></a>

For publish connectors, the `payload.fields` array selects which mapped field names to include in the output. If you omit it, the connector includes all mapped fields. This gives you explicit control over what data the connector sends to the external system.

```
"payload": {
  "format": "json",
  "fields": ["projectId", "assetId", "name"]
}
```

## Variable substitution
<a name="variable-substitution"></a>

Many configuration fields support `${variable}` substitution using resource metadata values. You can use variable substitution in:
+ Step paths (for example, REST API paths, S3 object keys)
+ Request body templates (the `body` field on a step — an alternative to field-mapping-based payload construction)
+ Query parameters
+ Security configuration fields (for example, `${secret.username}`)
+ Field mapping sources
+ Output routing field mappings

Examples:
+  `assets/${project.projectId}/${asset.assetId}.json` resolves to `assets/proj-abc123/asset-def456.json`
+  `${asset.metadataAttributes.customField}` resolves to the value of a custom metadata attribute
+  `${secret.password}` resolves to a value from the referenced Secrets Manager secret

### Invocation built-in variables
<a name="invocation-variables"></a>

SDMA injects the following variables at trigger execution time. They are available in step paths, body templates, output `uri` fields, field mapping sources, and anywhere else that supports `${variable}` substitution.

| Variable | Description |
| --- | --- |
|  `${eventName}`  | The lifecycle event that matched the trigger (for example, `create`, `uploadComplete`, `onDemand`). |
|  `${invocation.id}`  | The connector invocation ID for the current execution. Use this to construct unique output paths (for example, an S3 prefix per invocation). |
|  `${invocation.callbackUrl}`  | The fully-qualified URL a third party should call to resolve a `wait` step’s external completion. Resolves to the `UpdateConnectorInvocation` endpoint for this invocation. Empty if the API endpoint cannot be resolved. |
|  `${parameters.connectorInvocationId}`  | The connector invocation ID, which SDMA adds to the parameters of every run. You do not declare it in `parameterDefinitions`. When steps wait for each file in an `applyTo` fan-out, each file runs in its own invocation, so the value differs for each file. Use it for unique Amazon S3 paths and idempotency keys. |
|  `${parameters.<name>}`  | A validated parameter supplied when the connector was invoked (for example, `${parameters.notifyEmail}`). The value resolves to an empty string if the parameter was not supplied or the invocation record could not be loaded. |

The caller supplies parameters when triggering a connector through the API (the `parameters` field on `TriggerConnectorOnAsset` or `TriggerConnectorOnProject`). With these parameters, connector configurations can reference truly dynamic, per-invocation values that metadata alone cannot provide.

To mix variables into a mostly-static string in a field mapping source, use the `interpolate:` prefix. For example: `interpolate:Run ${invocation.id} completed for ${asset.assetName}`. You must use this prefix when the source is not a single `${variable}` expression.

### Type coercion
<a name="type-coercion"></a>

When you need to store a value as a specific metadata type, append a `:type` suffix to the target path or to an expression inside `${…​}`:
+  **On a target path** — declares the intended metadata type: `asset.metadataAttributes.surveyDate:date`, `asset.metadataAttributes.score:number`, `asset.metadataAttributes.approved:boolean`.
+  **Inside an expression** — coerces the expression result before mapping: `${response.site_codes:numberList}`, `${response.tags:stringList}`.

Supported type suffixes: `string`, `number`, `boolean`, `date`, `stringList`, `numberList`.

Example:

```
{
  "source": "response.survey_date",
  "target": "asset.metadataAttributes.surveyDate:date"
}
```

```
{
  "source": "${response.site_codes:numberList}",
  "target": "asset.metadataAttributes.siteCodes:numberList"
}
```

Without a type suffix, SDMA stores values as strings. Use type coercion when the external system returns values that you want to search or filter as numbers, dates, booleans, or lists in SDMA.

## Intermediate state with $temp variables
<a name="temp-variables"></a>

In multi-step triggers, steps often need to pass values to subsequent steps — for example, capturing an ID from a creation response and using it in a follow-up request. The `$temp.*` namespace provides this intermediate state.

Use `responseFieldMapping` on a step to capture response values into `$temp.*` variables:

```
"steps": [
  {
    "description": "Create external record",
    "method": "POST",
    "path": "/api/records",
    "body": { "name": "${asset.assetName}" },
    "responseFieldMapping": [
      { "source": "id", "target": "$temp.recordId" },
      { "source": "status", "target": "$temp.status" }
    ]
  },
  {
    "description": "Upload file content to the new record",
    "method": "PUT",
    "path": "/api/records/${$temp.recordId}/content",
    "bodyFromFile": { "contentType": "application/octet-stream" }
  }
]
```

 `$temp.*` variables apply only to a single trigger execution. SDMA does not share them across triggers or across connectors. Each trigger invocation starts with an empty `$temp` namespace.

 `$temp.*` variables work anywhere that `${variable}` substitution is supported: step paths, query parameters, body templates, field mapping sources, and output `uri` fields.

A `rest` step can also capture a response header. Use the source `responseHeaders.<header-name>`, with the header name in lowercase. This is how a step captures where an asynchronous API will write its result, as in [Running inference on an Amazon SageMaker asynchronous endpoint](connector-patterns.md#pattern-sagemaker-async).

```
"responseFieldMapping": [
  { "source": "responseHeaders.x-amzn-sagemaker-outputlocation", "target": "$temp.outputLocation" }
]
```

**Note**
 `$temp.*` variables captured before a `wait` step are preserved across the wait and available to steps that resume after the wait resolves. SDMA persists them alongside the wait state, so a multi-hour wait does not lose intermediate context.

## Security configuration
<a name="security-configuration"></a>

Connectors authenticate with external systems using a `securityConfig` block. SDMA supports the following authentication types:

| Type | Description |
| --- | --- |
|  `AssumeRole`  | Assumes an IAM role to access AWS resources. Requires `assumeRoleArn`. |
|  `ApiKey`  | Sends an API key in a header, query parameter, or cookie. Requires `secretArn` and `apiKeyLocation`. Supports optional `headerName` and `apiKeyPrefix` (for example, `Bearer`). |
|  `TokenAuth`  | Fetches a token from an OAuth/token endpoint and includes it in requests. Requires `tokenEndpoint`, `tokenMethod`, `headerName`, `tokenResponseField`, and `secretArn`. |
|  `BasicAuth`  | Sends HTTP Basic authentication credentials. Requires `secretArn`. SDMA resolves the username and password from the secret using `${secret.username}` and `${secret.password}`. |

### IAM role naming
<a name="security-role-naming"></a>

IAM roles used by connectors must follow a naming convention:
+  **Publish connectors** – Role name must start with `SpatialDataManagementContentPublisher-`
+  **Derive connectors** – Role name must start with `SpatialDataManagementContentDerivation-`

SDMA validates the role name prefix and tests role assumption when you create the connector. If the role cannot be assumed, connector creation fails with a validation error.

### Examples
<a name="security-config-example"></a>

The following examples show different authentication configurations.

IAM role assumption:

```
"securityConfig": {
  "type": "AssumeRole",
  "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-MyRole"
}
```

API key in a header:

```
"securityConfig": {
  "type": "ApiKey",
  "apiKeyLocation": "header",
  "headerName": "X-API-Key",
  "secretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>",
  "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-MyRole"
}
```

Token-based authentication (OAuth 2.0):

```
"securityConfig": {
  "type": "TokenAuth",
  "tokenEndpoint": "https://auth.example.com/oauth/token",
  "tokenMethod": "POST",
  "headerName": "Authorization",
  "tokenPrefix": "Bearer",
  "tokenResponseField": "access_token",
  "tokenRequestBody": {
    "grant_type": "client_credentials"
  },
  "secretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>",
  "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-MyRole"
}
```

## Connected resources
<a name="connected-resources"></a>

Some connectors need to associate a project with an external resource — for example, a STAC collection or an external project identifier. The optional `resources` block in the connector configuration defines how SDMA discovers, validates, and displays these external resources.

Each resource type (`project`, `asset`, `file`) can define three sub-configurations:

| Sub-config | Purpose |
| --- | --- |
|  `discover`  | Calls an external API to list available resources. SDMA presents the results as a selectable list when you create or edit the resource. |
|  `validate`  | Calls an external API to verify the selected resource exists. Checks the response status code against `successCriteria`. |
|  `display`  | Controls how the connected resource appears in the Spatial Data Portal — the resource label, the ID field shown, and a deep link URL to the external system. |

### Discovery configuration
<a name="_discovery-configuration"></a>

The following example shows how to configure resource discovery.

```
"resources": {
  "project": {
    "discover": {
      "description": "List external resources",
      "method": "GET",
      "path": "/api/resources",
      "type": "rest",
      "responseListField": "items",
      "labelField": "name",
      "valueField": "id",
      "fieldMappings": [
        { "source": "id", "target": "external_id" }
      ],
      "pagination": {
        "type": "offset",
        "offsetParam": "offset",
        "limitParam": "limit",
        "pageSize": 100,
        "maxPages": 10
      }
    }
  }
}
```
+  `responseListField` – The JSON path to the array of results in the API response.
+  `labelField` / `valueField` – The fields from each result to use as the display label and the stored value.
+  `fieldMappings` – Maps selected resource fields to metadata attribute names on the project, in the canonical `[{source, target}]` array form. When a user selects a resource, SDMA stores these as metadata attributes on the resource.
+  `pagination` – (Optional) Configures `offset` pagination, with a page size and a maximum number of pages.
+  `rawResponse` – (Optional) Specifies whether to return the external API’s JSON response as is, without extracting a list. Defaults to `false`.
+  `responseFormat` – (Optional) Configures APIs that return bytes rather than JSON, such as image tiles. Set `type` to `binary`. With `encoding: "base64"` (the default), SDMA returns the bytes base64-encoded inside JSON. With `encoding: "passthrough"`, SDMA returns the bytes directly with the `mediaType` you declare, which is then required.
+  `encodedQueryParam` – (Optional) Configures APIs that take a JSON document as a single encoded query parameter. Set `param` to the parameter name, `encoding` to `base64json`, and `template` to the JSON document, which supports `${variable}` substitution. Add `:intArray` to an expression that resolves to a comma-separated list, such as `${file[*].metadataAttributes.externalId:intArray}`, to send it as an array of integers.
+  `async` – (Optional) Declares that the operation returns before its work completes, so the caller polls or receives a callback for the result.

Discovery operations can also read values from the request. A client passes them as a JSON object in the `params` query parameter of the `GetConnectorResources` operation, and the operation references them as `${params.<name>}`.

#### Example – serving tiles through a connector
<a name="_example-serving-tiles-through-a-connector"></a>

A viewer can load a large point cloud or map progressively, one tile at a time. Two discovery operations let a connector serve those tiles from an external service, without exposing the service’s credentials to the viewer:

```
"resources": {
  "tileset": {
    "discover": {
      "type": "rest",
      "method": "GET",
      "path": "/api/tileset",
      "description": "Fetch the tileset hierarchy for the asset's files.",
      "encodedQueryParam": {
        "param": "p",
        "encoding": "base64json",
        "template": {
          "ids": "${file[*].metadataAttributes.externalId:intArray}",
          "boundary": "${params.boundary}"
        }
      },
      "rawResponse": true
    }
  },
  "tile": {
    "discover": {
      "type": "rest",
      "method": "GET",
      "path": "/api/tiles/${params.uri}",
      "description": "Fetch one tile by its content URI from the tileset.",
      "responseFormat": { "type": "binary", "encoding": "passthrough", "mediaType": "application/octet-stream" }
    }
  }
}
```
+ The `tileset` operation sends the external service the IDs of the asset’s files, as recorded by an earlier connector run, and returns the service’s tileset document unchanged.
+ The `tile` operation fetches each tile the viewer asks for, and returns its bytes directly.

### Validation configuration
<a name="_validation-configuration"></a>

The following example shows how to configure resource validation.

```
"validate": {
  "description": "Verify resource exists",
  "type": "rest",
  "method": "GET",
  "path": "/api/resources/${external_id}",
  "successCriteria": {
    "statusCodes": [200]
  }
}
```

### Display configuration
<a name="_display-configuration"></a>

The following example shows how to configure the display of connected resources in the Spatial Data Portal.

```
"display": {
  "connectedResourceName": "External resource",
  "displayId": {
    "name": "Resource ID",
    "value": "${external_id}"
  },
  "deepLinkUrl": "https://example.com/resources/${external_id}"
}
```
+  `connectedResourceName` – The label for this connected resource type.
+  `displayId` – The name and value template for the ID shown in the Spatial Data Portal.
+  `deepLinkUrl` – The URL template that links to the external resource. Supports `${variable}` substitution.

## Setting up a connector
<a name="connector-setup"></a>

To create a connector in the Spatial Data Portal:

1. Sign in to the Spatial Data Portal and navigate to **Library settings**.

1. In the **Connectors** section, choose the tab for the connector direction:
   +  **Publish content** — for publish connectors that send data to external systems.
   +  **Derive content** — for derive connectors that enrich metadata, transform content, or expose external resources.

1. Choose **Create publisher** or **Create deriver**.

1. Enter a connector name (5–128 characters, letters, numbers, spaces, hyphens, and underscores).

1. Select the connector type from the dropdown. The available types depend on the direction — for example, Deadline Cloud and metadata import types appear under **Derive content**.

1. Paste the connector configuration JSON into the JSON editor. See the individual connector type pages for configuration details.

1. Choose **Create**.

For integration connectors that combine publish and derive roles, set the `direction` to `bidirectional` in the connector configuration.

After creating the connector, associate it with an asset template by adding the connector ID to the template’s `permittedConnectorIds` list. A connector does nothing until you explicitly approve it on a template. Only approved connectors trigger for assets created under that template. For more on how connectors, templates, and projects relate, see [Connectors, templates, and projects](connectors-overview.md#connector-blast-radius).

**Important**
SDMA validates the connector configuration on creation. Validation includes:
Configuration structure — the connector JSON must conform to the expected structure described in [Connector configuration reference](#connector-config-reference).
IAM role assumption test — SDMA attempts to assume the configured role. If the role’s trust policy does not allow assumption, creation fails.
Role name prefix check — the role must start with `SpatialDataManagementContentPublisher-` (publish connectors) or `SpatialDataManagementContentDerivation-` (derive connectors).
Configuration size limit — the connector config must not exceed 350 KB.

## Connector configuration reference
<a name="connector-config-reference"></a>

Every connector configuration is a JSON object with the following top-level structure:

```
{
  "direction": "publish",
  "connectorType": "RESTApi | S3 | lambda | eventbridge | ...",
  "enabled": true,
  "connectorConfig": {
    "securityConfig": { ... },
    "fieldMappings": [ ... ],
    "triggers": [ ... ]
  }
}
```

The `connectorConfig` object contains the connector-specific settings described below.

### Security configuration
<a name="_security-configuration"></a>

Every connector requires a `securityConfig` that tells SDMA how to authenticate with the target service.

| Field | Required | Description |
| --- | --- | --- |
|  `type`  | Yes | Authentication method. One of `AssumeRole`, `ApiKey`, `TokenAuth`, or `BasicAuth`. |
|  `assumeRoleArn`  | Yes (for `AssumeRole`) | ARN of the IAM role to assume. The role’s trust policy must allow SDMA to assume it. |
|  `secretArn`  | Yes (for `ApiKey`, `TokenAuth`, `BasicAuth`) | ARN of the Secrets Manager secret containing the credential. |
|  `apiKeyLocation`  | Yes (for `ApiKey`) | Where to send the key: `header`, `query`, or `cookie`. |
|  `headerName`  | No | Custom header name for API key or token authentication. |
|  `tokenEndpoint`  | Yes (for `TokenAuth`) | URL to request an access token from. |

### Field mappings
<a name="_field-mappings"></a>

Field mappings transform SDMA resource metadata into the structure expected by the target system. Define them at the connector level (shared by all triggers) or at the step level (overrides connector-level mappings).

Each mapping has a `source` and a `target`:

```
"fieldMappings": [
  { "source": "asset.assetName", "target": "properties.title" },
  { "source": "project.projectId", "target": "properties.projectId" },
  { "source": "literal:Feature", "target": "type" },
  { "source": "asset.files[*].size", "target": "files[${file.path}].size" }
]
```

Supported source types:
+  **Standard path** – dot-notation path into SDMA metadata, for example `asset.assetName` or `project.projectId`.
+  **Literal string** – prefix with `literal:` to set a static string value, for example `literal:Feature` or `literal:data`.
+  **Literal array** – `literal:` with a JSON array, for example `literal:["data"]` or `literal:["thumbnail","overview"]`.
+  **Literal object** – `literal:` with a JSON object, for example `literal:{"format":"GeoTIFF","compression":"deflate"}`.
+  **File download URL** – use `file.contentUrl` or `asset.files[].contentUrl ` to generate an SDMA API-routed file download URL. Use `file.presignedUrl` or `asset.files[` to generate a direct S3 presigned URL for the file content. Use `file.s3Uri` or `asset.files[*].s3Uri` for the `s3://bucket/key` location of the file content, for a service that reads the file directly from Amazon S3 with its own role. SDMA computes all three at execution time from the file hash and asset context.
+  **GeoJSON bounding box** – prefix with `geoJson:` to convert a geometry field to a `[minX, minY, maxX, maxY]` bounding box, for example `geoJson:asset.geoLocation`.
+  **Timestamp** – use `system.timestamp` to insert the current UTC timestamp in ISO 8601 format.
+  **Invocation parameter** – use `parameters.<name>` to reference a parameter supplied when the connector was invoked, for example `parameters.connectorInvocationId`. Available only while a trigger is executing (see [Invocation built-in variables](#invocation-variables)).
+  **Invocation built-ins** – use `invocation.id` or `invocation.callbackUrl` to reference the current connector invocation. Available only while a trigger is executing (see [Invocation built-in variables](#invocation-variables)).
+  **String interpolation** – prefix with `interpolate:` to substitute one or more `${variable}` expressions inside a static string template, for example `interpolate:Run ${invocation.id} completed for ${asset.assetName}`.
+  **Array iteration** – use `[] ` to iterate over arrays, for example `asset.files[` or `asset.files[*].size`.

Supported target types:
+  **Flat field** – for example `id` or `assetName`.
+  **Nested path** – dot-separated path that creates nested objects, for example `properties.title`.
+  **Array index** – sets a specific position in an array, for example `geometry.coordinates[0]`.
+  **Dynamic dictionary key** – use `${variable}` inside brackets to create dictionary entries keyed by a field value, for example `assets[${file.path}].href`.

### Triggers
<a name="_triggers-2"></a>

Triggers define when and how the connector runs. Each trigger specifies which resources and events activate it, and what steps to execute.

```
"triggers": [
  {
    "description": "On asset creation, publish metadata to S3.",
    "resources": ["asset"],
    "events": ["create", "onDemand"],
    "stepType": "s3PutObject",
    "steps": [{ ... }]
  }
]
```

| Field | Required | Description |
| --- | --- | --- |
|  `resources`  | Yes | Which resource types activate this trigger. One or more of: `project`, `asset`, `file`, `derivedFile`. |
|  `events`  | Yes | Which events activate this trigger. One or more of: `create`, `update`, `delete`, `upload`, `uploadComplete`, `derivationComplete`, `onDemand`. |
|  `stepType`  | No | Default step type for all steps in this trigger. One of: `rest`, `lambdaInvoke`, `eventBridgePutEvents`, `s3PutObject`, `s3DeleteObject`, `deadlineJob`, `wait`. |
|  `steps`  | Yes | Array of step objects to execute when the trigger matches. |
|  `filter`  | No | Restricts which events the trigger matches, by file dimensions (`fileExtensionFilter`, `fileNameRegex`, `pathRegex`, `minFileSizeMB`, and `maxFileSizeMB`), by `changeState`, and by project, asset, or file metadata. See [Trigger filters](#trigger-filters). |
|  `applyTo`  | No | Runs the steps once for each file, derived file, or batch, instead of once for the triggering resource. See [Running steps per file](#trigger-apply-to). |
|  `parameterDefinitions`  | No | Declares the parameters a caller supplies when running the trigger on demand. See [Trigger parameters](#trigger-parameters). |
|  `dependsOn`  | No | Lists connector IDs that must finish first within the same lifecycle context. See [Ordering connectors with dependsOn](#trigger-dependencies). |
|  `derivation`  | No | Makes the trigger a metadata lookup (`s3Lookup`, `restLookup`, `dynamodbLookup`). See [Metadata lookup and enrichment](connector-derivation.md). |
|  `deadlineJob`  | No | Specifies the Deadline Cloud job template, parameters, and output for the trigger. See [Create and transform content with AWS Deadline Cloud](connector-deadline-cloud.md). |
|  `output`  | No | Specifies the output routing configuration for the trigger. The valid targets depend on the trigger’s `resources`, as the following list shows. See [Output routing](#output-routing). |

Each output target is valid only on triggers with certain `resources`:
+  `metadataAttributes` – `project`, `asset`, `file`, `derivedFile`
+  `derivedFiles` – `asset`, `file`, `derivedFile`
+  `siblingDerivedFiles` – `derivedFile` only
+  `files` – `asset` only
+  `assets` – `project`, `asset` (with lineage)

### Steps
<a name="_steps"></a>

Each step defines a single action. The step type determines which fields are relevant.

| Step type | Description |
| --- | --- |
|  `rest`  | Makes an HTTP request. Configure `method`, `path`, `headers`, `queryParams`, and `body`. |
|  `lambdaInvoke`  | Invokes an AWS Lambda function. Configure `lambdaConfig.functionArn`. |
|  `eventBridgePutEvents`  | Sends an event to Amazon EventBridge. Configure `eventBridgeConfig.eventBusArn`, `source`, and `detailType`. |
|  `s3PutObject`  | Writes a JSON object to Amazon S3. Configure `s3Config.objectKey` and optionally `s3Config.bucketName`. |
|  `s3DeleteObject`  | Deletes an object from Amazon S3. Configure `s3Config.objectKey` and optionally `s3Config.bucketName`. |
|  `deadlineJob`  | Submits a batch processing job to AWS Deadline Cloud. Configure `deadlineConfig` at the connector level and `deadlineJob` (template, parameters, output) at the trigger level. |
|  `wait`  | Pauses the trigger while an asynchronous task completes, then resumes the remaining steps. Configure a `wait` block with exactly one of `poll` (SDMA periodically checks whether the task is done — either by querying an HTTP endpoint or by watching for output files in S3) or `externalCompletion` (waiting for a callback from the external system). No running compute is held while waiting. See [Working with wait steps](connector-wait.md). |

Common step fields:
+  `s3Config` — for S3 steps, set `objectKey` (supports `${variable}` interpolation) and optionally `bucketName` to override the connector-level bucket.
+  `payload.fields` — array of top-level field names to include in the output. The connector writes only these fields and excludes all others.
+  `fieldMappings` — step-level field mappings that override the connector-level mappings.
+  `securityConfig` — step-level security config that overrides the connector-level config.
+  `onError` — set to `fail` (default) or `record-and-continue`.

## Failure policy
<a name="failure-policy"></a>

Connectors support a failure policy that automatically disables the connector when too many failures occur within a time window. Configure this at the connector level:

```
"failurePolicy": {
  "maxFailures": 5,
  "windowMinutes": 10,
  "onExceeded": "disable"
}
```
+  `maxFailures` – Number of failures within the time window before the policy action triggers. Defaults to `5`.
+  `windowMinutes` – Rolling time window (in minutes) for counting failures. If the window expires without reaching the threshold, the failure count resets. Defaults to `10`.
+  `onExceeded` – Action to take when failures exceed the threshold. Currently only `disable` is supported.

When failures exceed the threshold, SDMA sets the connector status to `FAILURE_COUNT_EXCEEDED` and disables it. Re-enable the connector manually after resolving the underlying issue.

## Error handling
<a name="error-handling"></a>

SDMA automatically records connector invocation results. Each invocation tracks:
+  **Status** – One of the following:
  +  `QUEUED` – The invocation is queued for execution.
  +  `IN_PROGRESS` – The invocation is currently executing.
  +  `SUCCEEDED` – The invocation completed successfully.
  +  `FAILED` – The invocation failed during execution.
  +  `NOT_APPLICABLE` – The connector was attached but no trigger matched the event, so no work was performed.
  +  `WAITING` – The invocation is suspended. This occurs when a trigger executes a `wait` step with `externalCompletion` and is blocked until a third party posts its result via `UpdateConnectorInvocation`, or when the invocation is waiting for an upstream connector to complete (see `dependsOn` in trigger configuration).
  +  `DEPENDENCY_BLOCKED` – An upstream connector that this invocation depends on has failed, so this invocation was not executed.
+  **Exception details** – Error message, type, and context for failed invocations

Steps support per-step error handling by using the `onError` field:
+  `fail` (default) – Stop execution and mark the invocation as failed.
+  `record-and-continue` – Record the error and continue to the next step. Use this in multi-step triggers when a step is non-critical. For example, a notification step should not block the rest of the workflow if the notification service is temporarily unavailable.

For multi-step triggers, the `sleepTime` and `retryCount` fields on individual steps control retry behavior. Use the `successConditions` block to define custom success criteria (for example, waiting for a resource to be deleted before proceeding).

In multi-step connectors, error handling interacts with step composition. If a step with `onError: fail` fails, SDMA marks the entire invocation as failed and does not execute subsequent steps. If a step with `onError: record-and-continue` fails, SDMA records the error but continues to the next step. The invocation status reflects the overall outcome — `SUCCEEDED` if all steps completed (even if some recorded errors), `FAILED` if any `fail`-mode step failed.

## Security model
<a name="connector-security"></a>

SDMA enforces multiple layers of security to isolate connector execution and limit the impact of misconfiguration.

### Network isolation
<a name="_network-isolation"></a>

Connector step execution runs in isolated AWS Lambda functions within the SDMA deployment account. These functions:
+ Execute in a private VPC with no direct inbound internet access.
+ Access external services only through configured IAM roles and security credentials.
+ Do not share execution context, memory, or temporary storage between connectors or between invocations.

Each connector invocation is an independent, stateless execution. A failure or misconfiguration in one connector does not affect other connectors or the core SDMA service.

### IAM role isolation
<a name="_iam-role-isolation"></a>

Every connector authenticates with external services through a dedicated IAM role that you create and control in your own AWS account. SDMA enforces the following constraints:
+  **Role name prefix** — The role must start with `SpatialDataManagementContentPublisher-` (publish connectors) or `SpatialDataManagementContentDerivation-` (derive connectors). SDMA rejects roles that do not match the expected prefix for the connector direction.
+  **Assumption test on creation** — SDMA attempts to assume the role when you create the connector. If the trust policy does not permit assumption, creation fails.
+  **Least privilege** — The role’s permissions policy determines exactly what the connector can do. SDMA does not grant any additional permissions beyond what the role allows.

You control the blast radius of each connector by scoping the IAM role’s permissions. For example, you can restrict an S3 connector role to a single bucket and prefix, preventing the connector from accessing any other resources in your account.

### Credential management
<a name="_credential-management"></a>

For connectors that use API keys, tokens, or basic authentication, you store credentials in AWS Secrets Manager. SDMA retrieves credentials at execution time and does not cache or persist them. The connector’s IAM role must have permission to read the specific secret.
