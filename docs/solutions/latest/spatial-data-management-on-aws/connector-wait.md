---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-wait.html
---

# Working with wait steps
<a name="connector-wait"></a>

Many integrations take real time to respond. A point-cloud import can run for minutes, an inference job might take an hour, and an external review might not come back until someone acts on it. A `wait` step lets a connector start that kind of work, pause until it finishes, and then act on the result — all without holding any running compute while the external work is in progress.

Use a wait step when you need a connector trigger to block on an external outcome before continuing. A wait of a few seconds and a wait of several hours cost the same.

## How wait steps work
<a name="wait-overview"></a>

A typical pattern is: start a job, wait for it to finish, then write the results back.

1. A preceding step starts the external work (for example, posting an import request) and captures identifiers into `$temp.*` variables.

1. The `wait` step suspends the trigger. SDMA persists everything the remaining steps will need — captured variables, the steps themselves, and the rules for deciding when the external work is done.

1. While the trigger is suspended, no compute is running. The invocation sits in `IN_PROGRESS` (if SDMA is polling) or `WAITING` (if the external system will call back).

1. When the external work finishes, SDMA evaluates the result against the configured success and failure patterns.

1. On success, SDMA applies any output routing on the wait step (writing metadata or ingesting files) and resumes the remaining steps with the preserved context.

1. On failure or timeout, the invocation is marked `FAILED` and the remaining steps do not run.

## Result sources
<a name="wait-result-sources"></a>

A wait step needs to know when the external work is done. There are two ways this can happen, and you choose the one that fits the integration:

| Source | When to use |
| --- | --- |
|  `poll`  | The external system exposes a status endpoint. SDMA checks it on an interval you configure and decides the outcome from the response. |
|  `externalCompletion`  | The external system supports callbacks or webhooks. You give it the invocation’s callback URL, and it posts the result back to SDMA when it is done. |

Each wait step must declare exactly one of these. Declaring both is a validation error — SDMA needs a single, unambiguous path to a result.

## Wait step configuration
<a name="wait-configuration"></a>

```
{
  "stepType": "wait",
  "description": "Wait for import job to finish",
  "wait": {
    "timeoutSeconds": 7200,
    "poll": { ... }
  },
  "output": { ... }
}
```

The `wait` block is a sibling of `stepType` and `output` on the step object. It contains the result source configuration:

| Field | Type | Default | Description |
| --- | --- | --- | --- |
|  `timeoutSeconds`  | integer | 7200 | Maximum seconds to wait for a result before failing the step. Minimum 10, maximum 86400 (24 hours). |
|  `poll`  | object | — | Polling result source. Mutually exclusive with `externalCompletion`. |
|  `externalCompletion`  | object | — | External-completion result source. Mutually exclusive with `poll`. |

## Polling result source
<a name="wait-polling"></a>

With a polling wait, SDMA checks for the result on an interval you configure. There are two polling modes:
+  **REST polling** (`type: "rest"`, the default) — SDMA issues an HTTP request to a status endpoint and evaluates the response against the patterns you declare (`successWhen` and `failureWhen`). If neither matches, it checks again later.
+  **Output polling** (`type: "output"`) — SDMA checks whether the step’s declared output files have appeared in S3. When all declared targets are present, the wait resolves. See [Output-driven wait](#wait-output-driven) for details.

Choose REST polling when the external system exposes a status endpoint. Choose output polling when the external system writes its results to S3 and has no status API (or when you want to wait on the actual output rather than a status flag).

### Poll configuration
<a name="_poll-configuration"></a>

| Field | Type | Default | Description |
| --- | --- | --- | --- |
|  `type`  | string |  `rest`  | How to check for the result. `rest` polls an HTTP endpoint. `output` watches S3 for the step’s declared output (see [Output-driven wait](#wait-output-driven)). |
|  `intervalSeconds`  | integer | 30 | Seconds between polls. Minimum 10, maximum 3600. |
|  `method`  | string |  `GET`  | HTTP method for the poll request. Only applies when `type` is `rest`. |
|  `path`  | string | — | URL path to poll. Supports `${…​}` variable substitution. Required when `type` is `rest`. |
|  `successWhen`  | pattern | — | Pattern that means the external work succeeded. Required when `type` is `rest`. See [Result classifier patterns](#wait-classifier). |
|  `failureWhen`  | pattern | — | Pattern that means the external work failed. Optional. If omitted, only `successWhen` is checked and non-matching responses trigger the next poll. Only applies when `type` is `rest`. |
|  `headers`  | object | — | Additional HTTP headers for the poll request. Only applies when `type` is `rest`. |
|  `body`  | object | — | Request body template for POST polls. Supports `${…​}` variable substitution. Only applies when `type` is `rest`. |
|  `queryParams`  | object | — | Query parameters for the poll request. Only applies when `type` is `rest`. |

### REST polling example
<a name="_rest-polling-example"></a>

A connector that starts an import via a REST POST, captures the job version, then polls a status endpoint until the import is ready:

```
{
  "triggers": [
    {
      "description": "Import point cloud files and wait for completion.",
      "resources": ["asset"],
      "events": ["uploadComplete"],
      "steps": [
        {
          "description": "POST import manifest to external API.",
          "stepType": "rest",
          "method": "POST",
          "path": "/api/tables/import",
          "fieldMappings": [
            { "source": "asset.files[*].presignedUrl", "target": "inputs[*].src" }
          ],
          "responseFieldMapping": [
            { "source": "table_version", "target": "$temp.table_version" }
          ]
        },
        {
          "description": "Wait for the import to be ready, polling the status endpoint.",
          "stepType": "wait",
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
          "description": "Fetch results and write metadata back to the asset.",
          "stepType": "rest",
          "method": "POST",
          "path": "/api/query_metadata",
          "output": {
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
          }
        }
      ]
    }
  ]
}
```

In this example:

1. The first step starts an import job and captures the `table_version` into `$temp`.

1. The wait step polls every 30 seconds until `{"status": "ready"}` appears in the response or 2 hours elapse.

1. Once the wait resolves successfully, the third step runs — fetching per-file metadata and writing it back to individual files using a correlate mapping.

### Output polling example
<a name="_output-polling-example"></a>

A connector that invokes an inference service, then waits for the results to appear in S3:

```
{
  "triggers": [
    {
      "description": "Run inference and wait for output files.",
      "resources": ["asset"],
      "events": ["uploadComplete"],
      "steps": [
        {
          "description": "Submit inference request.",
          "stepType": "rest",
          "method": "POST",
          "path": "/v1/inference",
          "body": { "input": "${asset.files[0].presignedUrl}" }
        },
        {
          "description": "Wait for results to land in S3.",
          "stepType": "wait",
          "wait": {
            "timeoutSeconds": 3600,
            "poll": {
              "type": "output",
              "intervalSeconds": 30
            }
          },
          "output": {
            "metadataAttributes": {
              "uri": "s3://results-bucket/jobs/${invocation.id}/",
              "filter": { "fileNameRegex": ".*_summary\\.json$" },
              "fieldMappings": [
                { "source": "score", "target": "asset.metadataAttributes.qualityScore:number" }
              ]
            },
            "derivedFiles": [
              {
                "uri": "s3://results-bucket/jobs/${invocation.id}/",
                "filter": { "fileExtensionFilter": ".geojson" }
              }
            ]
          }
        }
      ]
    }
  ]
}
```

In this example:

1. The first step submits an inference request. The external service writes its output to S3 when it finishes.

1. The wait step checks S3 every 30 seconds. It completes when both a `_summary.json` file and a `.geojson` file appear under the invocation prefix.

1. On completion, SDMA reads the summary JSON and maps `score` to asset metadata, then ingests the `.geojson` files as derived files.

No `successWhen` or `failureWhen` is needed — the presence of the declared output files is the success signal. See [Output-driven wait](#wait-output-driven) for the full reference.

## External completion result source
<a name="wait-external-completion"></a>

With an external-completion wait, SDMA suspends the trigger and waits for the external system to call back. The third party calls the `UpdateConnectorInvocation` API endpoint with a freeform JSON body when it is done. SDMA evaluates that body using the same `successWhen` / `failureWhen` patterns.

### External completion configuration
<a name="_external-completion-configuration"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `successWhen`  | Yes | Pattern that means the external work succeeded. |
|  `failureWhen`  | No | Pattern that means the external work failed. If the posted body matches neither pattern, SDMA marks the invocation as `FAILED` — the third party should only post when it has a final result. |

### External completion example
<a name="_external-completion-example"></a>

A connector that starts an external quality review, passes the callback URL, and writes the review results back as asset metadata when the external system posts its decision:

```
{
  "triggers": [
    {
      "description": "Start a review and wait for the external system to post results.",
      "resources": ["asset"],
      "events": ["onDemand"],
      "steps": [
        {
          "description": "Submit asset for review and pass the callback URL.",
          "stepType": "rest",
          "method": "POST",
          "path": "/api/reviews",
          "body": {
            "assetId": "${asset.assetId}",
            "callbackUrl": "${invocation.callbackUrl}"
          },
          "responseFieldMapping": [
            { "source": "reviewId", "target": "$temp.reviewId" }
          ]
        },
        {
          "description": "Wait for the review platform to post its decision.",
          "stepType": "wait",
          "wait": {
            "externalCompletion": {
              "successWhen": { "status": "complete" },
              "failureWhen": { "status": "failed" }
            },
            "timeoutSeconds": 86400
          },
          "output": {
            "metadataAttributes": {
              "fieldMappings": [
                { "source": "score", "target": "asset.metadataAttributes.reviewScore:number" },
                { "source": "reviewer", "target": "asset.metadataAttributes.reviewedBy" },
                { "source": "comments", "target": "asset.metadataAttributes.reviewComments" }
              ]
            }
          }
        }
      ]
    }
  ]
}
```

When the external review platform finishes, it sends a PUT request to the callback URL with a body like:

```
{
  "status": "complete",
  "score": 92,
  "reviewer": "jane@example.com",
  "comments": "Geometry validated, no issues found."
}
```

SDMA evaluates `{"status": "complete"}` against `successWhen` — it matches (subset match ignores extra fields). SDMA then applies the `output` block: it maps `score`, `reviewer`, and `comments` from the posted body into asset metadata attributes. Remaining steps (if any) resume with the preserved `$temp` context.

The callback URL for the current invocation is available as `${invocation.callbackUrl}` in any step configuration field that supports variable substitution. The preceding REST step passes it to the external system so it knows where to post the result.

## Result classifier patterns
<a name="wait-classifier"></a>

The `successWhen` and `failureWhen` fields accept a pattern that SDMA matches against the response body (for polling) or the posted body (for external completion). These patterns describe what "success" and "failure" look like in the external system’s response.

### Pattern semantics
<a name="_pattern-semantics"></a>

| Shape | Match rule |
| --- | --- |
| Object |  **Subset match.** Every field listed in the pattern must be present in the response and must match recursively. Extra fields in the response are ignored. |
| Array |  **Any-of.** The response matches the array pattern if it matches any element in the array. |
| Scalar (string, number, boolean) |  **Exact equality.** Numbers compare numerically. Strings compare exactly (case-sensitive). |

The special key `$status` matches the HTTP status code of the poll response (not a body field). It is only meaningful for polling waits.

### Pattern examples
<a name="_pattern-examples"></a>

Simple field match — succeeds when the response contains `"status": "ready"` (extra fields are ignored):

```
"successWhen": { "status": "ready" }
```

Nested subset match — succeeds when `result.state` is `"DONE"` and `errorCount` is `0`:

```
"successWhen": { "result": { "state": "DONE" }, "errorCount": 0 }
```

Any-of — succeeds if the response matches either pattern:

```
"successWhen": [
  { "status": "succeeded" },
  { "status": "complete" }
]
```

HTTP status match — fails on a 404 regardless of body content:

```
"failureWhen": { "$status": 404 }
```

Combined status and body — succeeds only when both HTTP 200 and body field match:

```
"successWhen": { "$status": 200, "result": { "state": "DONE" } }
```

### Tie-breaking
<a name="_tie-breaking"></a>

If the response matches both `successWhen` and `failureWhen`, success wins. Design patterns so they are mutually exclusive to avoid ambiguity.

## Output-driven wait
<a name="wait-output-driven"></a>

An output-driven wait (`poll.type: "output"`) completes when the step’s declared `output` targets are available in S3, rather than polling an HTTP endpoint. Use this when the external system writes results to S3 and you want SDMA to detect and ingest them automatically.

With this mode, SDMA periodically checks S3 for the declared output files. When all targets are present, the wait resolves successfully and SDMA routes the output through the standard output router.

### Configuration
<a name="_configuration"></a>

Set `poll.type` to `"output"` and declare an `output` block with at least one S3-backed target (a `uri` on `metadataAttributes`, `derivedFiles`, or `files`):

```
{
  "stepType": "wait",
  "description": "Wait for inference results to appear in S3.",
  "wait": {
    "timeoutSeconds": 7200,
    "poll": {
      "type": "output",
      "intervalSeconds": 30
    }
  },
  "output": {
    "metadataAttributes": {
      "uri": "s3://results-bucket/jobs/${invocation.id}/",
      "filter": { "fileNameRegex": ".*_summary\\.json$" },
      "fieldMappings": [
        { "source": "polygonCount", "target": "asset.metadataAttributes.polygonCount:number" }
      ]
    },
    "derivedFiles": [
      {
        "uri": "s3://results-bucket/jobs/${invocation.id}/",
        "filter": { "fileExtensionFilter": ".zip" }
      }
    ]
  }
}
```

In this example:
+ SDMA polls S3 every 30 seconds.
+ The wait completes when both a `_summary.json` file and a `.zip` file exist under the invocation prefix.
+ On completion, SDMA reads the summary JSON and maps `polygonCount` to asset metadata, then ingests the `.zip` files as derived files.

### Completion rule
<a name="_completion-rule"></a>

Output-driven wait uses an **all targets present** rule: every S3-backed target declared in the step’s `output` block must be available before the wait resolves. If `metadataAttributes.uri` is declared, it serves as both the completion signal and the data source that `fieldMappings` map from.

### Requirements
<a name="_requirements"></a>
+ The `output` block must declare at least one S3-backed target with a `uri`. A wait step with `poll.type: "output"` and no `uri` in any output target is a validation error — there would be nothing to wait for.
+ The `path`, `method`, `successWhen`, and `failureWhen` fields do not apply in output mode. Only `type`, `intervalSeconds`, and `timeoutSeconds` are relevant.

## Timeout behavior
<a name="wait-timeout"></a>

If `timeoutSeconds` elapses without a result, SDMA marks the invocation as `FAILED`. Remaining steps do not execute. The poll schedule (if any) is deleted.

Choose a timeout that exceeds the expected duration of the external work by a comfortable margin. For jobs that may take hours, values up to 86400 (24 hours) are supported.

## Resume semantics
<a name="wait-resume"></a>

When a wait resolves successfully:

1. SDMA applies the wait step’s `output` routing (metadata attributes, derived files, or both) using the response body as the data source.

1. SDMA resumes the remaining steps in the trigger. All `$temp.*` variables captured before the wait are available to resumed steps.

1. If a resumed step initiates another wait, the trigger suspends again — multiple waits in a single trigger are supported (though uncommon).

## Error handling
<a name="wait-error-handling"></a>

A wait step has three failure modes:
+  **Timeout** — `timeoutSeconds` elapsed without a successful result. The invocation is marked `FAILED`.
+  **Failure pattern matched** — the response matched `failureWhen`. The invocation is marked `FAILED`.
+  **Unmatched body (external completion only)** — the posted body matched neither `successWhen` nor `failureWhen`. The invocation is marked `FAILED`. For external completion, the third party should only post when it has a final outcome; an unmatched body means the contract was not followed.

In all three cases, no output routing runs and remaining steps do not execute. The invocation record captures the reason.

For REST polling, a response that matches neither pattern is **not** a failure — it means "still in progress" and SDMA schedules the next poll. Only an explicit `failureWhen` match or a timeout ends a polling wait as `FAILED`.

### Interaction with `onError`
<a name="_interaction-with-onerror"></a>

The `onError` field (`fail` or `record-and-continue`) is not supported on the wait step itself. A wait step always fails the invocation on any of the three failure modes above — there is no option to continue past a failed wait.

However, `onError` works normally on steps that run **after** a successful wait. If the trigger resumes and a subsequent step fails:
+ With `onError: fail` (the default) — the invocation is marked `FAILED` and no further steps run.
+ With `onError: record-and-continue` — the error is recorded and the next step executes.

This means a trigger like **[rest → wait → rest (record-and-continue) → rest]** behaves as you would expect: if the third step fails, it is recorded but the fourth step still runs.

## Providing the callback URL to external systems
<a name="wait-callback-url"></a>

For external-completion waits, the third party needs to know the URL to call. SDMA makes this available as `${invocation.callbackUrl}`. A common pattern is to pass it in a preceding REST step:

```
"steps": [
  {
    "description": "Start external review and pass the callback URL.",
    "stepType": "rest",
    "method": "POST",
    "path": "/api/reviews",
    "body": {
      "assetId": "${asset.assetId}",
      "callbackUrl": "${invocation.callbackUrl}"
    }
  },
  {
    "description": "Wait for the review to complete.",
    "stepType": "wait",
    "wait": {
      "externalCompletion": {
        "successWhen": { "decision": "approved" },
        "failureWhen": { "decision": "rejected" }
      },
      "timeoutSeconds": 86400
    }
  }
]
```

The external system stores the callback URL and, when the review is done, sends a PUT request to that URL with a body like `{"decision": "approved", "reviewer": "[jane@example.com](mailto:jane@example.com)"}`.

## Considerations
<a name="wait-limitations"></a>
+ A wait step can only appear in a multi-step trigger (the `steps` array). It cannot be used as a single-step trigger via the top-level `stepType` shorthand.
+ The maximum `timeoutSeconds` is 86400 (24 hours). For longer waits, consider breaking the integration into separate triggers that compose through the asset record.
+ Concurrent termination is handled safely: if both a poll and an external callback race to terminate the same invocation, only the first writer succeeds. The second is silently discarded.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
