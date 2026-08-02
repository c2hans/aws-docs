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
+  `stepType` – The type of step to execute (for publish connectors).
+  `steps` – One or more step configurations to execute in order.

### Supported resources
<a name="trigger-resources"></a>

The following resource types can activate a trigger.

| Resource | Description |
| --- | --- |
|  `project`  | Triggered when a project is created, updated, or deleted. Project-scoped triggers can produce assets via the `assets` output target without requiring a triggering asset. |
|  `asset`  | Triggered when an asset is created, updated, or deleted. |
|  `file`  | Triggered when a file within an asset is processed. |
|  `derivedFile`  | Triggered when a derived file (produced by a previous connector or processing job) is created. This is the primary mechanism for chaining connectors. A Deadline Cloud job that produces a `.glb` preview file fires a `derivedFile` event that a downstream publish connector can react to. |

### Supported events
<a name="trigger-events"></a>

The following events can activate a trigger.

| Event | Description |
| --- | --- |
|  `create`  | A resource is created. |
|  `update`  | A resource is updated. |
|  `delete`  | A resource is deleted. |
|  `upload`  | A file is added to or updated within an asset. |
|  `uploadComplete`  | All files in an asset have finished uploading and the asset is ready. |
|  `derivationComplete`  | A derivation or processing job for a file has completed. Use this to chain connectors — for example, triggering a publish after a Deadline Cloud job finishes. |
|  `onDemand`  | Manually triggered by a user from the Spatial Data Portal or via the API. |

A single trigger can match multiple resources and events. For example, a trigger with `"resources": ["asset"], "events": ["create", "update"]` fires on both asset creation and update.

### Ordering connectors with dependsOn
<a name="trigger-dependencies"></a>

When one connector’s work must complete before another connector runs, use `dependsOn` on the downstream trigger. This orders connector execution within the same lifecycle context — the set of work that a single upstream event triggers.

```
"triggers": [
  {
    "description": "Publish to catalog after quality analysis completes",
    "resources": ["asset"],
    "events": ["derivationComplete"],
    "dependsOn": ["<quality-analysis-connector-id>"],
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

For most compositions, you do not need `dependsOn`. Connectors compose naturally through the asset record. One connector produces a derived file or updates metadata, and another connector triggers on that lifecycle event. Use `dependsOn` only when you need explicit ordering within the same lifecycle context that the asset record alone does not provide.

## Output routing
<a name="output-routing"></a>

When a step completes — whether a REST call, a Lambda invocation, or a Deadline Cloud job — you can route the results back into the asset record. Use an `output` block to do this. Output routing is how connectors write results back to SDMA as governed metadata, derived files, or both.

Output routing works uniformly across all step types. The same `output` block works on REST steps, Lambda steps, and Deadline Cloud jobs. For Deadline Cloud, place the `output` block inside the `deadlineJob` configuration on the trigger (see [Create and transform content with AWS Deadline Cloud](connector-deadline-cloud.md)). The vocabulary is identical regardless of which step type produced the result.

The `output` block supports the following routing targets:

| Target | Description |
| --- | --- |
|  `metadataAttributes`  | Writes response fields to asset or file metadata attributes. Contains a `fieldMappings` array that maps fields from the step response to SDMA metadata paths. Use this to write summary values — counts, scores, timestamps, identifiers — that you want to be searchable, displayable, and available for downstream triggers. |
|  `derivedFiles`  | Ingests files that the step wrote to S3, attaching them as derived files on the asset. Each entry specifies a `filter` to match output files by extension or pattern. Each ingested derived file fires a `derivationComplete` lifecycle event that can trigger downstream connectors. |
|  `files`  | Ingests files as top-level files on the asset (without a derived-from relationship). Each entry specifies a `filter`. |
|  `assets`  | Creates new assets in the project from envelope files the step produced. Each entry specifies an `allowedTemplateIds` list and an optional `filter` to match output files. Only valid on triggers with `"resources": ["project"]`. |

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

Mappings with `asset. ` targets write to asset-level metadata. Mappings with `file.` targets write to file-level metadata on the triggering file. An optional `filter` on `metadataAttributes` narrows which files' attributes the connector processes.

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

Any trigger that declares an `output` block with `metadataAttributes`, `derivedFiles`, or `files` makes the connector asset-content-scoped, which means you must approve it through the template authorization chain. The `assets` target additionally requires that the connector is approved on each template ID listed in `allowedTemplateIds`.

### Creating assets from connector output
<a name="_creating-assets-from-connector-output"></a>

The `assets` target lets a connector create new assets in the project. This is used with project-scoped triggers — typically a Deadline Cloud job that produces one or more assets without an originating asset.

Each entry in the `assets` array specifies which templates the connector is allowed to create assets under, and an optional filter to identify envelope files in the step output:

```
"output": {
  "assets": [
    {
      "allowedTemplateIds": ["<TEMPLATE_ID>"],
      "filter": { "fileExtensionFilter": ".json" }
    }
  ]
}
```

The connector’s step output must contain asset envelopes — JSON objects with:
+  `idempotencyKey` – A unique key per asset to enable deduplication across retries.
+  `templateId` – Must be listed in `allowedTemplateIds`.
+  `name` – The asset name.
+  `metadataAttributes` – (Optional) Metadata to set on the created asset.
+  `manifest` – (Optional) File manifest for the asset.

SDMA validates that the triggering user has at least Contributor membership in the project before creating the asset. Each created asset fires a standard `create` lifecycle event.

The `assets` output target is only eligible on triggers with `"resources": ["project"]`. Declaring it on asset-scoped or file-scoped triggers causes a validation error at connector creation time.

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
|  `geoJson:`  | Extracts a GeoJSON bounding box from a location field (for example, `geoJson:asset.geoLocation`). |
|  `literal:`  | Uses a literal string value (for example, `literal:Feature`, `literal:Point`). |

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

Without a type suffix, SDMA stores values as strings. Use type coercion when the external system returns values that you want to search or filter as numbers, dates, booleans, or lists in SDMA

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

 `$temp.*` variables work anywhere that `${variable}` substitution is supported: step paths, query parameters, body templates, and field mapping sources.

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
  "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-MyRole"
}
```

API key in a header:

```
"securityConfig": {
  "type": "ApiKey",
  "apiKeyLocation": "header",
  "headerName": "X-API-Key",
  "secretArn": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret:<SECRET_NAME>",
  "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-MyRole"
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
  "secretArn": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret:<SECRET_NAME>",
  "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-MyRole"
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
+  `responseListField` — JSON path to the array of results in the API response.
+  `labelField` / `valueField` — Which fields from each result to use as the display label and stored value.
+  `fieldMappings` — Maps selected resource fields to metadata attribute names on the project using the canonical `[{source, target}]` array form. When a user selects a resource, SDMA stores these as metadata attributes on the resource.
+  `pagination` — Optional. Supports `offset` pagination with configurable page size and maximum pages.

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
+  `connectedResourceName` — Label for this connected resource type.
+  `displayId` — The name and value template for the ID shown in the Spatial Data Portal.
+  `deepLinkUrl` — URL template that links to the external resource. Supports `${variable}` substitution.

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
+  **Standard path** — dot-notation path into SDMA metadata, for example `asset.assetName` or `project.projectId`.
+  **Literal string** — prefix with `literal:` to set a static string value, for example `literal:Feature` or `literal:data`.
+  **Literal array** — `literal:` with a JSON array, for example `literal:["data"]` or `literal:["thumbnail","overview"]`.
+  **Literal object** — `literal:` with a JSON object, for example `literal:{"format":"GeoTIFF","compression":"deflate"}`.
+  **File download URL** — use `file.contentUrl` or `asset.files[].contentUrl ` to generate an SDMA API-routed file download URL. Use `file.presignedUrl` or `asset.files[` to generate a direct S3 presigned URL for the file content. SDMA computes both at execution time from the file hash and asset context.
+  **GeoJSON bounding box** — prefix with `geoJson:` to convert a geometry field to a `[minX, minY, maxX, maxY]` bounding box, for example `geoJson:asset.geoLocation`.
+  **Timestamp** — use `system.timestamp` to insert the current UTC timestamp in ISO 8601 format.
+  **Array iteration** — use `[] ` to iterate over arrays, for example `asset.files[` or `asset.files[*].size`.

Supported target types:
+  **Flat field** — for example `id` or `assetName`.
+  **Nested path** — dot-separated path that creates nested objects, for example `properties.title`.
+  **Array index** — sets a specific position in an array, for example `geometry.coordinates[0]`.
+  **Dynamic dictionary key** — use `${variable}` inside brackets to create dictionary entries keyed by a field value, for example `assets[${file.path}].href`.

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
|  `stepType`  | No | Default step type for all steps in this trigger. One of: `rest`, `lambdaInvoke`, `eventBridgePutEvents`, `s3PutObject`, `s3DeleteObject`, `deadlineJob`. |
|  `steps`  | Yes | Array of step objects to execute when the trigger fires. |
|  `filter`  | No | Optional filter to restrict which files activate the trigger. Supports `fileExtensionFilter` (for example, `.laz`), `fileNameRegex` (regex against filename), `pathRegex` (regex against full path), `minFileSizeMB`, and `maxFileSizeMB`. |
|  `output`  | No | Output routing configuration for the trigger. The eligible output targets depend on the trigger’s `resources` scope: `metadataAttributes` (project, asset, file, derivedFile), `derivedFiles` (asset, file, derivedFile), `files` (asset only), `assets` (project only). |

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
  +  `WAITING` – The invocation is waiting for an upstream connector to complete (see `dependsOn` in trigger configuration).
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
