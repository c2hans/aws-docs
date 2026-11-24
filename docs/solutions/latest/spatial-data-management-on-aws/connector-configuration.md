---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-configuration.html
---

# Connector Configuration

## Triggers
<a name="_triggers"></a>

Triggers define which resource events activate the connector. Each trigger specifies:
+  `resources` – The resource types to match.
+  `events` – The event types to match.
+  `filter` – (Optional) Which files and metadata the trigger matches. See [Trigger Filters](#trigger-filters).
+  `stepType` – The type of step to execute (for publish connectors).
+  `steps` – One or more step configurations to execute in order.
+  `applyTo` – (Optional) Runs the steps per file or batch. See [Running Steps per File](#trigger-apply-to).
+  `parameterDefinitions` – (Optional) Parameters for on-demand runs. See [Trigger Parameters](#trigger-parameters).

### Supported Resources
<a name="trigger-resources"></a>

The following resource types can activate a trigger.

| Resource | Description |
| --- | --- |
|  `project`  | Triggered when a project is created, updated, or deleted. Project-scoped triggers can produce assets via the `assets` output target without requiring a triggering asset. |
|  `asset`  | Triggered when an asset is created, updated, or deleted. |
|  `file`  | Triggered when a file within an asset is processed. |
|  `derivedFile`  | Triggered when a connector or processing job adds a derived file. With the `upload` event, this is the primary way to chain connectors. For example, an AWS Deadline Cloud job produces a `.glb` preview file, and a publish connector with a `derivedFile` trigger on `upload` publishes it. For more information, see [Chaining Connectors](#chaining-connectors). |

### Supported Events
<a name="trigger-events"></a>

The following events can activate a trigger.

| Event | Description |
| --- | --- |
|  `create`  | A resource is created. |
|  `update`  | A resource is updated. |
|  `delete`  | A resource is deleted. |
|  `upload`  | A file is added to or updated within an asset. On a `derivedFile` trigger, a connector or processing job added the derived file. |
|  `uploadComplete`  | All files in an asset have finished uploading and the asset is ready. |
|  `derivationComplete`  | Connector processing finished. On a `file` or `derivedFile`, it is raised once for the file, when a connector run that started from it succeeded, and not on the derived files the run produced. On an `asset`, it is raised once, when every derive connector run that the same upload or update started has ended, including runs that those runs started, and at least one succeeded. Use the file event to react to each result, for example to mark the file as processed. Use the asset event to act on the version’s final state, for example to publish the asset’s results. To act on the derived files, use `upload` on a `derivedFile` trigger instead. SDMA delivers the asset event at least once, so a consumer must handle a repeat. |
|  `onDemand`  | Manually triggered by a user from the Spatial Data Portal or through the API. The trigger runs on the project, asset, or files that the user starts it from. See [Running a Trigger on Demand](#trigger-on-demand). |

A single trigger can match multiple resources and events. For example, a trigger with `"resources": ["asset"], "events": ["create", "update"]` matches both asset creation and update.

### Running a Trigger on Demand
<a name="trigger-on-demand"></a>

The `onDemand` event runs when a user invokes the connector, from the Spatial Data Portal or through the API. Unlike lifecycle events, nothing in the content raises it, so the resource that the trigger runs on is the one you invoke the connector upon.

| You start the connector from | The trigger must name | API operation |
| --- | --- | --- |
| A project: **Run content derivation on project**  |  `project`  |  `TriggerConnectorOnProjectDirect`  |
| An asset: **Run content derivation on asset**, **Publish asset**, or one or more assets selected in a project |  `asset`  |  `TriggerConnectorOnAsset` or `TriggerConnectorOnAssetDirect`  |
| One or more files selected in an asset: **Run content derivation** or **Publish files**  |  `file`, or `derivedFile` for a derived file | The same asset operation, once for each file, with that file in the `fileId` query parameter |

A connector runs only if one of its triggers names that resource in `resources`, includes `onDemand` in `events`, and has a filter that matches. A trigger can name several resources. For example, `"resources": ["asset", "file"]` makes the same trigger available at both levels.

The Portal lists connectors by direction. A derive connector appears under **Run content derivation**, a publish connector under **Publish**, and a bidirectional connector under both.

The following connector has a trigger for each level. Each one runs only when the connector is started from that level.

```json
"triggers": [
  { "resources": ["project"], "events": ["onDemand"], "steps": [ ... ] },
  { "resources": ["asset"], "events": ["onDemand"], "steps": [ ... ] },
  {
    "resources": ["file"],
    "events": ["onDemand"],
    "filter": { "fileExtensionFilter": ".laz" },
    "steps": [ ... ]
  }
]
```

#### What to Expect
<a name="trigger-on-demand-rules"></a>
+  **Starting at the project level runs only project triggers.** SDMA does not also run the connector on the project’s assets.
+  **Starting at the asset level also tries the files.** When you start a connector on an asset, SDMA runs the asset triggers on the asset. If the connector also has `file` triggers, SDMA then checks every file in the asset, except SDMA’s own system files and derived files, and runs the trigger on each file that its filter matches. To run on one file, select the file and start the connector from the file.
+  **Derived files are separate.** A derived file matches `derivedFile` triggers, not `file` triggers, and starting a connector on the asset skips it. To run a `derivedFile` trigger, select the derived file and invoke the connector from it.
+  **Trying to invoke a connector with no matching trigger for a resource type does nothing.** No invocation is recorded. The Portal lists only connectors that have a trigger for where you are. If you invoke one that has none, it displays a message that none of its triggers match.
+  **Every matching trigger runs.** If two triggers on the connector match, both run in the same invocation. Only one of them can declare `parameterDefinitions`. See [Trigger Parameters](#trigger-parameters).
+  **The connector must be usable.** It must be enabled, and it must be a default connector or be approved on a template. For a project, the template must be one that the project uses. For an asset, it must be the asset’s template.
+  **An on-demand run does not wait for `dependsOn`.** The run starts at once, even when the connector’s trigger lists connectors that it normally waits for.
+  **Parameters come from the caller.** SDMA checks the values against the `parameterDefinitions` of the trigger that matches. When an event starts a trigger instead, each parameter takes its default. See [Trigger Parameters](#trigger-parameters).

### Trigger Filters
<a name="trigger-filters"></a>

A `filter` narrows which events a trigger matches. Filter keys combine with AND, so every key must match. Spatial Data Management on AWS (SDMA) checks the file dimensions first, then metadata. SDMA tests metadata only on files that already passed the dimension check.

#### File Dimensions
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

#### Metadata Conditions
<a name="_metadata-conditions"></a>

Use `project`, `asset`, or `file` to test metadata attributes on the resource. Each takes a `metadataAttributes` object that maps attribute names to conditions. A bare value tests for equality. An object applies one or more operators, all of which must hold.

The following JSON filter combines a file dimension with asset and file metadata conditions.

```json
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

### Trigger Parameters
<a name="trigger-parameters"></a>

A trigger can declare parameters with `parameterDefinitions`. A caller supplies the values when running the trigger on demand. When an event starts the trigger, SDMA uses each parameter’s `default`. SDMA validates the values before the trigger runs, records them on the run, and steps read them as `${parameters.<name>}`.

The following JSON declares three parameters.

```json
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
|  `type`  | Required. `string`, `number`, `boolean`, `date`, or `file`. A `file` value names an SDMA file as `project-<id>/asset-<id>/file-<id>`. That name identifies one stored object permanently, so a `file` parameter pins the exact bytes. A path or an asset version is not accepted. |
|  `displayName`  | A label, up to 128 characters, that the Portal shows in place of the parameter name. |
|  `modelIdentity`  | Marks the parameter as the identity of the model that the trigger runs. See [Naming the Model a Trigger Runs](#trigger-model-identity). |
|  `multipleValues`  | When `true`, the parameter takes a list of values of that type. |
|  `required`  | When `true`, the caller must supply the parameter. Cannot be combined with `default`. |
|  `default`  | The value used when the caller leaves the parameter out. Must match the type and constraints. |
|  `allowedValues`  | The only values accepted. |
|  `min` / `max`  | Bounds for a number. |
|  `minItems` / `maxItems`  | Bounds on the number of values, when `multipleValues` is `true`. |
|  `description`  | Shown to users who run the connector. |

Parameter names start with a letter and contain only letters, digits, and underscores. Callers pass values in the `parameters` field of the trigger API, or through the Spatial Data Portal.

SDMA enforces these rules, so that a run always has the values it needs:
+  **A trigger that runs on an event cannot require a parameter.** Nothing supplies the value when an event starts the trigger. When you save a connector with a `required` parameter on a trigger whose `events` include anything other than `onDemand`, SDMA rejects it. Give the parameter a `default` instead.
+  **Defaults apply to every run.** A parameter with a `default` takes that value when a caller omits it, and when an event starts the trigger.
+  **One parameterized trigger matches at a time.** If two triggers that declare `parameterDefinitions` match the same resource, SDMA rejects the dispatch, because the run’s parameters would be ambiguous.
+  **A run that declares parameters needs them recorded.** If a run’s parameters cannot be read, the run fails instead of continuing with empty values.

#### Naming the Model a Trigger Runs
<a name="trigger-model-identity"></a>

When a trigger runs a model, mark the parameter that identifies it with `modelIdentity`. The run records the value, and the **Content flow** tab of the template names the model on the connector’s card. A trigger can have at most one such parameter, and it cannot take multiple values.

|  `modelIdentity`  | Parameter `type`  | The parameter holds |
| --- | --- | --- |
|  `file`  |  `file`  | The SDMA file that holds the model. Because a `file` value pins exact bytes, the run records exactly which model it used. |
|  `sagemakerEndpoint`  |  `string`  | The name of the Amazon SageMaker endpoint that the trigger’s requests use. |
|  `external`  |  `string`  | Any other reference to the model, such as a version label or a registry identifier in another system. |

The following parameters declare a model that is an SDMA file and a confidence threshold:

```json
"parameterDefinitions": {
  "model": {
    "type": "file",
    "modelIdentity": "file",
    "displayName": "Detection model",
    "required": true
  },
  "minScore": {
    "type": "number",
    "displayName": "Minimum score",
    "min": 0,
    "max": 1,
    "default": 0.5
  }
}
```

This trigger runs only on demand, because it requires `model`. For a pattern that records the model on the result, see [Recording Which Model Produced a Result](connector-patterns.md#pattern-model-provenance).

### Running Steps per File
<a name="trigger-apply-to"></a>

By default, a trigger’s steps run once for the resource whose event matched. Add `applyTo` to run them once for each file or derived file instead, or once for each batch of files. For example, a Deadline Cloud trigger with `applyTo` submits one job for each matching file, and a REST trigger with `"batchSize": 100` sends files to an API 100 at a time.

The following JSON shows an `applyTo` block.

```json
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

Either way, the invocation ends `FAILED` if any run failed, and it records how many items or batches succeeded and failed. For every field, how filters apply to the iteration, and a worked example that writes results back to each file, see [Processing Changed Files and Writing Results Back](connector-fan-out-write-back.md).

### Chaining Connectors
<a name="chaining-connectors"></a>

The recommended way to chain connectors is through the asset record. One connector adds a derived file. That raises an event, and the next connector’s trigger matches it. Each connector is configured and approved on its own, so you can change or turn off one stage without changing the others.

A connector can also name another connector with `dependsOn`. That makes it wait for the other connector, but it couples the two, and it does not start a run by itself (see [Ordering Connectors with dependsOn](#trigger-dependencies)).

Choose the event by what the next connector should act on.

| The next connector acts on | Trigger | Raised |
| --- | --- | --- |
| A derived file the previous connector produced |  `"resources": ["derivedFile"]`, `"events": ["upload"]`  | Once for each derived file, when it is added |
| The file a run started from, after the run succeeded |  `"resources": ["file"]` or `["derivedFile"]`, `"events": ["derivationComplete"]`  | Once for each successful run that started from that file |
| The asset, after its metadata changed |  `"resources": ["asset"]`, `"events": ["update"]`  | When the asset is updated |
| The asset, after all its derive connectors finished |  `"resources": ["asset"]`, `"events": ["derivationComplete"]`  | Once, after the last derive connector run that the same event started has ended, if at least one succeeded |

The following trigger is the second stage of a pipeline. The first stage writes `segmented.laz` as a derived file. This trigger matches only that file, by name, and converts it:

```json
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
+  **Keep a chain’s outputs beside the original.** A stage that matches a derived file can declare its output with `siblingDerivedFiles`, so all stages' outputs sit side by side under the original file (see [Placing Derived Files Alongside Their Source](#sibling-derived-files)).
+  **Prefer the asset record to `dependsOn`.** A stage that matches its input file already waits for that file to exist. Use `dependsOn` only when a stage also reads outputs it did not start from, such as a fusion stage that needs a terrain model (see [Ordering Connectors with dependsOn](#trigger-dependencies)).
+  **Expect a depth limit.** By default, SDMA follows up to five connector-produced hops from one upload. Further derived files are kept, but they start no more connectors. This stops a connector that matches its own output from running forever.
+  **Chain on `upload`, not `derivationComplete`.** A run started by `derivationComplete` does not raise `derivationComplete` again, so a chain built on that event stops after one hop. A run that `derivationComplete` starts also runs after the asset event, so the asset event does not wait for it. To include a later stage, start it from the derived files.

For a five-stage example, see [Example – A Multi-Model Pipeline](connector-patterns.md#pattern-pipeline).

### Ordering Connectors with dependsOn
<a name="trigger-dependencies"></a>

When one connector’s work must complete before another connector runs, use `dependsOn` on the downstream trigger. This orders connector execution within the same lifecycle context — the set of work that a single upstream event triggers.

```json
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

For most chains, you do not need `dependsOn`, because each stage starts only when its input exists (see [Chaining Connectors](#chaining-connectors)). Use `dependsOn` only when a stage also needs outputs other than the one that started it.

## Output Routing
<a name="output-routing"></a>

When a step completes — whether a REST call, a Lambda invocation, or a Deadline Cloud job — you can route the results back into the asset record. Use an `output` block to do this. Output routing is how connectors write results back to SDMA as governed metadata, derived files, or both.

Output routing works uniformly across all step types. The same `output` block works on REST steps, Lambda steps, and Deadline Cloud jobs. For Deadline Cloud, place the `output` block inside the `deadlineJob` configuration on the trigger (see [Create and Transform Content with AWS Deadline Cloud](connector-deadline-cloud.md)). The vocabulary is identical regardless of which step type produced the result.

The `output` block supports the following routing targets:

| Target | Description |
| --- | --- |
|  `metadataAttributes`  | Writes response fields to asset or file metadata attributes. Contains a `fieldMappings` array that maps fields from the step response to SDMA metadata paths. Use this to write summary values — counts, scores, timestamps, identifiers — that you want to be searchable, displayable, and available for downstream triggers. |
|  `derivedFiles`  | Ingests files that the step wrote to S3, attaching them as derived files on the asset. Each entry specifies a `filter` to match output files by extension or pattern. Each ingested derived file raises an `upload` event on the `derivedFile` resource, which can start the next connector (see [Chaining Connectors](#chaining-connectors)). |
|  `siblingDerivedFiles`  | Ingests files as derived files of the same file the triggering derived file belongs to, alongside it rather than beneath it. Same entry shape as `derivedFiles`. Only valid on triggers with `"resources": ["derivedFile"]`. See [Placing Derived Files Alongside Their Source](#sibling-derived-files). |
|  `files`  | Ingests files as top-level files on the asset (without a derived-from relationship). Each entry specifies a `filter`. |
|  `assets`  | Creates new assets in the project. Each entry specifies an `assetTemplateIds` list, and either a `filter` that matches envelope files the step produced or, on a `wait` step, one inline asset. Valid on triggers with `"resources": ["project"]` or `"resources": ["asset"]`. On an asset trigger, SDMA records lineage from each new asset back to the triggering asset. See [Creating Assets from Connector Output](#creating-assets). |

### Routing Metadata with fieldMappings
<a name="_routing-metadata-with-fieldmappings"></a>

The `metadataAttributes` target uses `fieldMappings` to control which response fields to write and where to write them. Each mapping has a `source` (a field in the step response) and a `target` (an SDMA metadata path). Use `:type` suffixes on targets to store values as typed metadata (see [Type Coercion](#type-coercion)).

```json
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

Mappings with `asset. ` targets write to asset-level metadata. Mappings with `file.` targets write to file-level metadata on the triggering file. Mappings with `derivedFile.*` targets write to each derived file the step ingested, so a fact about an output, such as the model version that made it, stays with that output. For more information, see [Recording Which Model Produced a Result](connector-patterns.md#pattern-model-provenance). An optional `filter` on `metadataAttributes` narrows which files' attributes the connector processes.

The `metadataAttributes` target also supports an optional `uri` field. When present, SDMA reads the JSON file at that S3 location as the source for `fieldMappings` instead of using the step’s response body directly. This is used with output-driven `wait` steps (see [Working with Wait Steps](connector-wait.md)): SDMA watches S3 for the file to appear, then reads and maps its contents.

```json
"metadataAttributes": {
  "uri": "s3://amzn-s3-demo-bucket/results/${invocation.id}/",
  "filter": { "fileNameRegex": ".*_summary\\.json$" },
  "fieldMappings": [
    { "source": "score", "target": "asset.metadataAttributes.qualityScore:number" }
  ]
}
```

### Saying What a Value Means
<a name="field-mapping-role"></a>

Add `role` to a field mapping in an `output` block to say what the value means to a person who reads it.

|  `role`  | Use it for |
| --- | --- |
|  `provenance`  | Where the result came from, or the rules it was produced under. For example, the model version, or the source coordinate system. |
|  `finding`  | A result that the run produced. For example, a count of detections. |

```json
"fieldMappings": [
  { "source": "model.version", "target": "derivedFile.metadataAttributes.modelVersion", "role": "provenance" },
  { "source": "detections", "target": "file.metadataAttributes.detectionCount:number", "role": "finding" }
]
```

 `role` does not change where SDMA writes the value. It is part of the record. When a run writes an attribute, SDMA records the connector run as the attribute’s source, with the role you declared. An accepted attribute suggestion records the run that proposed it, with the role `suggestion`. A person who sees the value can tell that a run wrote it and what it stands for, instead of reading it as something a person typed. The value is still the connector’s claim, and SDMA does not vouch for it.

The **Content flow** tab of an asset template groups the attributes on each connector’s card by role. See [See How Content Flows Through the Connectors](asset-templates.md#template-content-flow).

When a person edits a file’s attributes, an attribute whose value is unchanged keeps the source that SDMA recorded. A new or changed value is recorded as the person’s own.

### Combining Metadata and Derived Files
<a name="_combining-metadata-and-derived-files"></a>

A single `output` block can route to multiple targets. This is the canonical pattern when a step produces both summary metadata (for search and display) and detailed output files (for downstream processing or review).

```json
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

### Drawing a Run’s Findings in the Viewer
<a name="output-presentation"></a>

A connector that detects or measures things can tell the Portal how to draw the result. Add a `presentation` block to a `derivedFiles` or `siblingDerivedFiles` entry that produces GeoJSON. When someone opens the source point cloud, the point cloud viewer draws the GeoJSON over it. See [Findings from a Connector Run](view-your-content.md#view-findings).

```json
"derivedFiles": [
  {
    "filter": { "fileExtensionFilter": ".geojson" },
    "presentation": {
      "title": "Detections",
      "thresholds": [
        { "id": "confident", "label": "Confident", "parameter": "minScore", "direction": "atOrAbove", "color": "#2e7d32" }
      ],
      "layers": [
        {
          "id": "objects",
          "label": "Objects",
          "visible": true,
          "colorBy": { "property": "score", "thresholds": ["confident"] },
          "draw": { "box": { "property": "box", "style": "outline" } },
          "fields": ["class", "score"],
          "summary": "{count} of {total} objects"
        }
      ]
    }
  }
]
```

| Field | Meaning |
| --- | --- |
|  `title`  | The heading that the viewer shows. The default is `Findings`. |
|  `thresholds`  | Up to eight values that layers color and filter features by. Each has an `id` and a `parameter`, which is the trigger parameter whose value the run recorded. `direction` is `atOrBelow` or `atOrAbove`, and `color` is `#rrggbb`. If the run recorded no number for the parameter, the threshold has no value. |
|  `layers`  | One or more groups of features that are drawn alike. A layer needs a `color`, or `colorBy`, which colors features by comparing a feature property with thresholds that have the same direction. |
| layer `color`  | One `#rrggbb` color for every feature in the layer. Use it instead of `colorBy` when the layer is not colored by thresholds. |
| layer `filter`  | The property values that a feature must hold to be in the layer. |
| layer `measure`  | A slider that keeps the features within a value of one property. It has `property`, `min`, `max`, `presets` (threshold IDs the slider can jump to), and `default` (the preset the slider starts at). `label`, `unit`, and `labelCount` are optional. |
| layer `draw`  | How to draw each feature. `box` names a property that holds a center, a size, and `yaw_deg`, and draws it as a `solid` or `outline` box. `segment` names a property that holds a line to draw. |
| layer `fields`  | The feature properties that the panel lists when someone selects a feature. |
| layer `summary`  | A line under the layer. The placeholders `{count}`, `{total}`, `{measure}`, and `{min}` are filled in. |
| layer `visible`  | Whether the layer is shown when the viewer opens. |

The viewer draws the thresholds with the values that the run used, not today’s connector configuration. SDMA records on each derived file the connector version, the parameter values, and which output entry produced the file, so the file always carries the presentation of the run that made it. Files from runs that did not record these values have no presentation, and the viewer draws nothing for them.

### Placing Derived Files Alongside Their Source
<a name="sibling-derived-files"></a>

 `derivedFiles` places output beneath the file that triggered the step. That is right when the output is a child of that file. Sometimes the output is instead another representation of the same original.

For example, an orthophoto `site.tif` has a derived shapefile `site.zip`. A connector converts `site.zip` to GeoJSON. The GeoJSON describes the orthophoto just as the shapefile does, so you place it next to `site.zip`, under `site.tif`, not under `site.zip`. The following JSON configuration declares this with `siblingDerivedFiles` on a trigger on `derivedFile`:

```json
"output": {
  "siblingDerivedFiles": [
    { "filter": { "fileExtensionFilter": ".geojson" }, "preview": true }
  ]
}
```

SDMA records the output as derived from the same file as the triggering derived file. SDMA resolves only one level up, so each connector in a chain can independently choose where its output belongs.

### Creating Assets from Connector Output
<a name="creating-assets"></a>

The `assets` target lets a connector create new assets in the project. Use it on a project trigger, for example a Deadline Cloud job that produces assets without an originating asset. You can also use it on an asset trigger, to turn each result of processing an asset into an asset of its own (see [Lineage from an Asset Trigger](#asset-lineage)).

A step declares new assets in one of two ways:
+  **Envelope files.** The step writes JSON files that describe the assets, and a `filter` selects them.
+  **An inline asset.** A `wait` step describes one asset directly in its `output` block. See [Inline Assets from a Wait Step](#inline-assets-from-wait).

#### Envelope Files
<a name="_envelope-files"></a>

Each entry in the `assets` array specifies which templates the connector is allowed to create assets under, and a filter that identifies envelope files in the step output.

```json
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

Before creating the asset, SDMA checks that the user whose event started the run has at least Contributor membership in the project (see [Contributor](access-control.md#contributor)). Each created asset raises a standard `create` lifecycle event (see [Supported Events](#trigger-events)).

SDMA combines `idempotencyKey` with the connector invocation ID. A retry within one run does not create a duplicate, but running the connector again creates new assets.

The `assets` output target is valid on project and asset triggers. Declaring it on a file or derived file trigger causes a validation error when you create the connector.

#### Inline Assets from a Wait Step
<a name="inline-assets-from-wait"></a>

A `wait` step has no output files of its own to filter. Instead, its `assets` entry describes the asset to create when the wait completes. Every `${…​}` expression resolves at that point, including `$temp` values the wait captures with `responseFieldMapping` (see [Capturing Values from the Result](connector-wait.md#wait-capture)).

```json
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
|  `manifest`  | No | The new asset’s files as an asset-creation manifest. A path entry can give `s3Uri` instead of `hash`, `size`, and `mtime`. It can also give `s3Uri` together with a `hash`, and SDMA checks the hash while it copies. Use `files` or `manifest`, not both. |

 `templateId`, `name`, and `idempotencyKey` must be given together. An inline asset cannot also declare a `filter`.

#### Lineage from an Asset Trigger
<a name="asset-lineage"></a>

When a trigger on an asset creates new assets, SDMA records where each new asset came from. This *lineage* is what allows an asset trigger to create assets outside the asset that matched.

SDMA builds lineage from what it bound for the run, never from the connector configuration or a producer’s response. It writes one `derivedFrom` edge on the history event of the new asset’s first version:

```json
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

### Ingesting Derived Files from an External S3 Location
<a name="_ingesting-derived-files-from-an-external-s3-location"></a>

When a step writes output files to S3 and returns the location in its response, you can use `${response.*}` expressions in the `uri` field of a `derivedFiles` entry to ingest those files without hardcoding paths.

The `uri` field supports two forms depending on whether `filter` is present:
+  **S3 object form** (no `filter`) – Ingests a single object at the resolved S3 URI.
+  **S3 prefix form** (with `filter`) – Lists objects under the resolved S3 URI prefix and ingests those matching the filter.

Example — ingest `.png` files from a location returned by a Lambda step:

```json
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

```json
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

Give a `uri` or a `hash`. If an entry gives both, SDMA uses the `hash` and ignores the `uri`. With `hash`, SDMA assumes the bytes are already in the managed content store at the canonical key. An asset manifest path entry is different: it can give both `s3Uri` and `hash`, and SDMA checks the hash while it copies.

#### Size Limits for Ingested Files
<a name="output-size-limits"></a>

SDMA stores each file in its content-addressable storage under the file’s hash, and the whole run must finish within the 15-minute function limit. How large a file can be depends on whether its hash is already known:
+  **Already in the managed bucket, with its `hash`.** The entry gives the `hash` of a file that is already at its canonical key. SDMA copies nothing, so there is no size limit.
+  **An S3 object in an asset manifest, with its `hash`.** A manifest path entry can give both `s3Uri` and `hash`. SDMA checks the hash while it copies. The object can be up to 25 GiB, with or without an assumed role.
+  **An S3 object, without a `hash`.** SDMA must hash the object before it can store it. The object can be up to 25 GiB. If the source needs a role that SDMA assumes, the limit is 12 GiB.

SDMA rejects an entry over a limit with the reason `HashSizeExceeded`, and reports the size and the limit. The 15-minute limit covers the whole output, so a run with many large objects can still time out. Split the objects across several runs.

When the entry gives a `hash`, or the source needs an assumed role, SDMA checks the bytes that it stores. If the object changed, SDMA rejects the entry and stores nothing, with the reason `HashMismatch` or `SourceChangedDuringRead`. Otherwise, make sure the producer has stopped writing before the run ends.

## Field Mappings
<a name="field-mappings"></a>

Field mappings transform resource metadata into the format expected by the external system. Each mapping specifies a `source` field from the resource metadata and a `target` field name for the output.

```json
"fieldMappings": [
  { "source": "project.projectId", "target": "projectId" },
  { "source": "asset.assetName", "target": "name" },
  { "source": "geoJson:asset.geoLocation", "target": "bbox" }
]
```

### Source Field Prefixes
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

### Array Iteration
<a name="field-mapping-array-iteration"></a>

Field mappings support iterating over arrays using the `[*]` syntax. For example, to map each file in an asset:

```json
{ "source": "asset.files[*].path", "target": "assets[${file.path}].title" }
```

This creates one output entry per file, using the file path as the key.

You can define field mappings at the connector level as a default and override them per step when different events require different output shapes.

### Correlate Mapping
<a name="correlate-mapping"></a>

When a step response contains a collection (object or array) whose entries correspond to individual files on the asset, use a `correlate` block on a `fieldMapping` to write per-file metadata by matching each response entry to an existing file.

```json
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

## Payload Fields
<a name="payload-fields"></a>

For publish connectors, the `payload.fields` array selects which mapped field names to include in the output. If you omit it, the connector includes all mapped fields. This gives you explicit control over what data the connector sends to the external system.

```json
"payload": {
  "format": "json",
  "fields": ["projectId", "assetId", "name"]
}
```

## Variable Substitution
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

### Invocation Built-In Variables
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

### Type Coercion
<a name="type-coercion"></a>

When you need to store a value as a specific metadata type, append a `:type` suffix to the target path or to an expression inside `${…​}`:
+  **On a target path** — declares the intended metadata type: `asset.metadataAttributes.surveyDate:date`, `asset.metadataAttributes.score:number`, `asset.metadataAttributes.approved:boolean`.
+  **Inside an expression** — coerces the expression result before mapping: `${response.site_codes:numberList}`, `${response.tags:stringList}`.

Supported type suffixes: `string`, `number`, `boolean`, `date`, `stringList`, `numberList`.

Example:

```json
{
  "source": "response.survey_date",
  "target": "asset.metadataAttributes.surveyDate:date"
}
```

```json
{
  "source": "${response.site_codes:numberList}",
  "target": "asset.metadataAttributes.siteCodes:numberList"
}
```

Without a type suffix, SDMA stores values as strings. Use type coercion when the external system returns values that you want to search or filter as numbers, dates, booleans, or lists in SDMA.

## Intermediate State with $temp Variables
<a name="temp-variables"></a>

In multi-step triggers, steps often need to pass values to subsequent steps — for example, capturing an ID from a creation response and using it in a follow-up request. The `$temp.*` namespace provides this intermediate state.

Use `responseFieldMapping` on a step to capture response values into `$temp.*` variables:

```json
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

A `rest` step can also capture a response header. Use the source `responseHeaders.<header-name>`, with the header name in lowercase. This is how a step captures where an asynchronous API will write its result, as in [Running Inference on an Amazon SageMaker Asynchronous Endpoint](connector-patterns.md#pattern-sagemaker-async).

```json
"responseFieldMapping": [
  { "source": "responseHeaders.x-amzn-sagemaker-outputlocation", "target": "$temp.outputLocation" }
]
```

**Note**
 `$temp.*` variables captured before a `wait` step are preserved across the wait and available to steps that resume after the wait resolves. SDMA persists them alongside the wait state, so a multi-hour wait does not lose intermediate context.

## Security Configuration
<a name="security-configuration"></a>

Connectors authenticate with external systems using a `securityConfig` block. SDMA supports the following authentication types:

| Type | Description |
| --- | --- |
|  `AssumeRole`  | Assumes an IAM role to access AWS resources. Requires `assumeRoleArn`. |
|  `ApiKey`  | Sends an API key in a header, query parameter, or cookie. Requires `secretArn` and `apiKeyLocation`. Supports optional `headerName` and `apiKeyPrefix` (for example, `Bearer`). |
|  `TokenAuth`  | Fetches a token from an OAuth/token endpoint and includes it in requests. Requires `tokenEndpoint`, `tokenMethod`, `headerName`, `tokenResponseField`, and `secretArn`. |
|  `BasicAuth`  | Sends HTTP Basic authentication credentials. Requires `secretArn`. SDMA resolves the username and password from the secret using `${secret.username}` and `${secret.password}`. |

### IAM Role Naming
<a name="security-role-naming"></a>

IAM roles used by connectors must follow a naming convention:
+  **Publish connectors** – Role name must start with `SpatialDataManagementContentPublisher-`
+  **Derive connectors** – Role name must start with `SpatialDataManagementContentDerivation-`

SDMA validates the role name prefix and tests role assumption when you save the connector. The test runs as the SDMA connector invocation role, which is the role that assumes your role when the connector runs. If a role cannot be assumed, SDMA does not save the connector. The error lists each role and names the connector invocation role to add to that role’s trust policy.

### Examples
<a name="security-config-example"></a>

The following examples show different authentication configurations.

IAM role assumption:

```json
"securityConfig": {
  "type": "AssumeRole",
  "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-MyRole"
}
```

API key in a header:

```json
"securityConfig": {
  "type": "ApiKey",
  "apiKeyLocation": "header",
  "headerName": "X-API-Key",
  "secretArn": "arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>",
  "assumeRoleArn": "arn:aws:iam::<account-id>:role/SpatialDataManagementContentPublisher-MyRole"
}
```

Token-based authentication (OAuth 2.0):

```json
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

## Connected Resources
<a name="connected-resources"></a>

Some connectors need to associate a project with an external resource — for example, a STAC collection or an external project identifier. The optional `resources` block in the connector configuration defines how SDMA discovers, validates, and displays these external resources.

Each resource type (`project`, `asset`, `file`) can define three sub-configurations:

| Sub-config | Purpose |
| --- | --- |
|  `discover`  | Calls an external API to list available resources. SDMA presents the results as a selectable list when you create or edit the resource. |
|  `validate`  | Calls an external API to verify the selected resource exists. Checks the response status code against `successCriteria`. |
|  `display`  | Controls how the connected resource appears in the Spatial Data Portal — the resource label, the ID field shown, and a deep link URL to the external system. |

### Discovery Configuration
<a name="_discovery-configuration"></a>

The following example shows how to configure resource discovery.

```json
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

#### Example – Serving Tiles Through a Connector
<a name="_example-serving-tiles-through-a-connector"></a>

A viewer can load a large point cloud or map progressively, one tile at a time. Two discovery operations let a connector serve those tiles from an external service, without exposing the service’s credentials to the viewer:

```json
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

For a complete connector that imports the files into the service and then serves them as tiles, see [Sending Content to an External Analysis Service and Viewing It in SDMA](connector-patterns.md#pattern-external-analysis).

### Validation Configuration
<a name="_validation-configuration"></a>

The following example shows how to configure resource validation.

```json
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

### Display Configuration
<a name="_display-configuration"></a>

The following example shows how to configure the display of connected resources in the Spatial Data Portal.

```json
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

## Setting Up a Connector
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

After creating the connector, associate it with an asset template by adding the connector ID to the template’s `permittedConnectorIds` list. A connector does nothing until you explicitly approve it on a template. Only approved connectors trigger for assets created under that template. For more on how connectors, templates, and projects relate, see [Connectors, Templates, and Projects](connectors-overview.md#connector-blast-radius).

**Important**
SDMA validates the connector configuration on creation. Validation includes:
Configuration structure — the connector JSON must conform to the expected structure described in [Connector Configuration Reference](#connector-config-reference).
IAM role assumption test — SDMA attempts to assume every role named in the configuration’s `securityConfig` blocks. If a role’s trust policy does not allow the connector invocation role to assume it, the connector is not saved, and the error names the role to trust.
Role name prefix check — the role must start with `SpatialDataManagementContentPublisher-` (publish connectors) or `SpatialDataManagementContentDerivation-` (derive connectors).
Configuration size limit — the connector config must not exceed 350 KB.

## Connector Configuration Reference
<a name="connector-config-reference"></a>

Every connector configuration is a JSON object with the following top-level structure:

```json
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

### Description
<a name="connector-description"></a>

A connector can have an optional `description` of up to 1,024 characters. The Spatial Data Portal shows it in connector lists, in the connector picker on a template, and in search.

Set it as a top-level `description` in the request, or as `description` in `connectorConfig`. If you set both, the top-level value is used. SDMA keeps the two in step, so a configuration you copy to another library keeps its description. When you update a connector and leave out the description, the stored description stays. To remove it, send an empty string. Asset templates have the same optional `description`.

### Security Configuration
<a name="_security-configuration"></a>

Every connector requires a `securityConfig` that tells SDMA how to authenticate with the target service.

| Field | Required | Description |
| --- | --- | --- |
|  `type`  | Yes | Authentication method. One of `AssumeRole`, `ApiKey`, `TokenAuth`, or `BasicAuth`. |
|  `assumeRoleArn`  | Yes (for `AssumeRole`) | ARN of the IAM role to assume. The role’s trust policy must allow the SDMA connector invocation role to assume it. If it does not, the error you receive when you save the connector names that role. |
|  `secretArn`  | Yes (for `ApiKey`, `TokenAuth`, `BasicAuth`) | ARN of the Secrets Manager secret containing the credential. |
|  `apiKeyLocation`  | Yes (for `ApiKey`) | Where to send the key: `header`, `query`, or `cookie`. |
|  `headerName`  | No | Custom header name for API key or token authentication. |
|  `tokenEndpoint`  | Yes (for `TokenAuth`) | URL to request an access token from. |

### Field Mappings
<a name="_field-mappings"></a>

Field mappings transform SDMA resource metadata into the structure expected by the target system. Define them at the connector level (shared by all triggers) or at the step level (overrides connector-level mappings).

Each mapping has a `source` and a `target`:

```json
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
+  **Invocation parameter** – use `parameters.<name>` to reference a parameter supplied when the connector was invoked, for example `parameters.connectorInvocationId`. Available only while a trigger is executing (see [Invocation Built-In Variables](#invocation-variables)).
+  **Invocation built-ins** – use `invocation.id` or `invocation.callbackUrl` to reference the current connector invocation. Available only while a trigger is executing (see [Invocation Built-In Variables](#invocation-variables)).
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

```json
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
|  `filter`  | No | Restricts which events the trigger matches, by file dimensions (`fileExtensionFilter`, `fileNameRegex`, `pathRegex`, `minFileSizeMB`, and `maxFileSizeMB`), by `changeState`, and by project, asset, or file metadata. See [Trigger Filters](#trigger-filters). |
|  `applyTo`  | No | Runs the steps once for each file, derived file, or batch, instead of once for the triggering resource. See [Running Steps per File](#trigger-apply-to). |
|  `parameterDefinitions`  | No | Declares the parameters a caller supplies when running the trigger on demand. See [Trigger Parameters](#trigger-parameters). |
|  `dependsOn`  | No | Lists connector IDs that must finish first within the same lifecycle context. See [Ordering Connectors with dependsOn](#trigger-dependencies). |
|  `derivation`  | No | Makes the trigger a metadata lookup (`s3Lookup`, `restLookup`, `dynamodbLookup`). See [Metadata Lookup and Enrichment](connector-derivation.md). |
|  `deadlineJob`  | No | Specifies the Deadline Cloud job template, parameters, and output for the trigger. See [Create and Transform Content with AWS Deadline Cloud](connector-deadline-cloud.md). |
|  `output`  | No | Specifies the output routing configuration for the trigger. The valid targets depend on the trigger’s `resources`, as the following list shows. See [Output Routing](#output-routing). |

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
|  `wait`  | Pauses the trigger while an asynchronous task completes, then resumes the remaining steps. Configure a `wait` block with exactly one of `poll` (SDMA periodically checks whether the task is done — either by querying an HTTP endpoint or by watching for output files in S3) or `externalCompletion` (waiting for a callback from the external system). No running compute is held while waiting. See [Working with Wait Steps](connector-wait.md). |

Common step fields:
+  `s3Config` — for S3 steps, set `objectKey` (supports `${variable}` interpolation) and optionally `bucketName` to override the connector-level bucket.
+  `payload.fields` — array of top-level field names to include in the output. The connector writes only these fields and excludes all others.
+  `fieldMappings` — step-level field mappings that override the connector-level mappings.
+  `securityConfig` — step-level security config that overrides the connector-level config.
+  `onError` — set to `fail` (default) or `record-and-continue`.

## Failure Policy
<a name="failure-policy"></a>

Connectors support a failure policy that automatically disables the connector when too many failures occur within a time window. Configure this at the connector level:

```json
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

## Error Handling
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
+  **Connector version** – The version of the connector that ran, returned as `connectorVersionId`. A run uses the version it was dispatched with for its whole life, including wait steps, per-file child runs, and output ingestion, so an edit to the connector during a run does not mix two configurations. Use the version to tell apart runs made before and after you changed the connector. If a run’s version cannot be loaded, the run fails. A connector that has no saved versions runs its current configuration. Runs from before this field was recorded have no value.
+  **Parameters** – The values the run used, with defaults applied. See [Trigger Parameters](#trigger-parameters).
+  **Exception details** – Error message, type, and context for failed invocations

Each derived file also records the run that produced it, and the `output` entry that produced it. The entry is recorded as a JSON pointer into the connector version that ran, for example `/triggers/0/deadlineJob/output/siblingDerivedFiles/1`. A file that no entry claims records no entry.

Steps support per-step error handling by using the `onError` field:
+  `fail` (default) – Stop execution and mark the invocation as failed.
+  `record-and-continue` – Record the error and continue to the next step. Use this in multi-step triggers when a step is non-critical. For example, a notification step should not block the rest of the workflow if the notification service is temporarily unavailable.

For multi-step triggers, the `sleepTime` and `retryCount` fields on individual steps control retry behavior. Use the `successConditions` block to define custom success criteria (for example, waiting for a resource to be deleted before proceeding).

In multi-step connectors, error handling interacts with step composition. If a step with `onError: fail` fails, SDMA marks the entire invocation as failed and does not execute subsequent steps. If a step with `onError: record-and-continue` fails, SDMA records the error but continues to the next step. The invocation status reflects the overall outcome — `SUCCEEDED` if all steps completed (even if some recorded errors), `FAILED` if any `fail`-mode step failed.

## Security Model
<a name="connector-security"></a>

SDMA enforces multiple layers of security to isolate connector execution and limit the impact of misconfiguration.

### Network Isolation
<a name="_network-isolation"></a>

Connector step execution runs in isolated AWS Lambda functions within the SDMA deployment account. These functions:
+ Execute in a private VPC with no direct inbound internet access.
+ Access external services only through configured IAM roles and security credentials.
+ Do not share execution context, memory, or temporary storage between connectors or between invocations.

Each connector invocation is an independent, stateless execution. A failure or misconfiguration in one connector does not affect other connectors or the core SDMA service.

### IAM Role Isolation
<a name="_iam-role-isolation"></a>

Every connector authenticates with external services through a dedicated IAM role that you create and control in your own AWS account. SDMA enforces the following constraints:
+  **Role name prefix** — The role must start with `SpatialDataManagementContentPublisher-` (publish connectors) or `SpatialDataManagementContentDerivation-` (derive connectors). SDMA rejects roles that do not match the expected prefix for the connector direction.
+  **Assumption test on save** — SDMA attempts to assume each role when you save the connector. If a trust policy does not permit assumption by the connector invocation role, the connector is not saved.
+  **Least privilege** — The role’s permissions policy determines exactly what the connector can do. SDMA does not grant any additional permissions beyond what the role allows.

You control the blast radius of each connector by scoping the IAM role’s permissions. For example, you can restrict an S3 connector role to a single bucket and prefix, preventing the connector from accessing any other resources in your account.

### Credential Management
<a name="_credential-management"></a>

For connectors that use API keys, tokens, or basic authentication, you store credentials in AWS Secrets Manager. SDMA retrieves credentials at execution time and does not cache or persist them. The connector’s IAM role must have permission to read the specific secret.
