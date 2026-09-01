---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connectors-overview.html
---

# Connectors overview
<a name="connectors-overview"></a>

Spatial assets become more valuable when they work with the applications your teams already use — geospatial platforms, rendering services, quality analysis tools, and publishing catalogs. Connectors are how SDMA leverages those external applications and services to transform, enrich, and interoperate with your content — and how those systems reach back in, governed by SDMA.

A connector can submit a compute job that converts a CAD file into a reviewable 3D format and writes the result back as a derived file. It can call an inference service that classifies imagery and writes quality scores into the asset record. It can look up metadata from a database or CSV and apply it across hundreds of files in one operation. It can publish structured metadata to a geospatial catalog, a data lake, or a project management system every time an asset changes. It can do several of these things in one governed contract.

A domain expert or administrator defines this once — what transforms to run, how to assess file quality, what metadata to enrich from which sources, where to publish — and attaches those connectors to a template. From that point on, every asset created under that template gets the benefit automatically. Files are converted, metadata is enriched, quality is assessed, and external systems are updated as content arrives. The people uploading and working with assets do not need to know how any of this works. They see governed, enriched, publication-ready assets from the moment of ingestion.

Connectors work through configuration, not code. You declare what should happen, when, with what data, under what credentials, and SDMA handles execution, security, failure policy, and audit. Every invocation is tracked. Every result flows back through the asset record with provenance. Connectors are governed through an explicit authorization chain: a connector is created and approved at the library level, a template author requests and approves which connectors are permitted for that class of assets, and a project uses that template. A connector does nothing until it is explicitly approved at each level. This means the people who define integrations, the people who define asset standards, and the people who create projects each control their own part of the chain.

With connectors, you can:
+  **Transform and derive content.** Submit compute jobs to AWS Deadline Cloud that convert file formats, generate thumbnails, extract spatial properties, or run custom processing pipelines that leverage your existing licensed software. Results come back as derived files and metadata on the asset — governed, versioned, and traceable to the job that produced them.
+  **Enrich metadata from external sources.** Look up values from S3 files, DynamoDB tables, or REST APIs and write them as metadata attributes on assets or files. Match external records to SDMA resources by filename, ID, or any field. Enrich in bulk on upload or on demand.
+  **Publish to external systems.** Push metadata to REST APIs, write to S3, invoke Lambda functions, or send events to EventBridge when assets are created, updated, or deleted. Keep external systems in sync with your asset record.
+  **Integrate with external applications.** Maintain a governed relationship with an external application that spans both directions — create external records on project creation, enrich metadata from the external catalog, and publish derived content back. One connector, one set of credentials, one failure policy.
+  **Expose external resources for guided workflows.** List available resources from a connected application — projects, collections, models — so users can select and link them during template authoring without leaving the Spatial Data Portal.
+  **Chain connectors through the asset record.** When one connector produces a derived file or updates metadata, that change is a lifecycle event that can trigger other connectors. A format conversion connector can feed a quality analysis connector, which can feed a publishing connector — each governed independently, composing through the asset record without referencing each other.
+  **Wait for long-running external work.** A `wait` step suspends a trigger until an external job completes — whether that is a point-cloud import, a render, an inference job, or a third-party review. SDMA polls the external system on an interval, or the external system calls back when done. Results flow back into the asset automatically, and remaining steps resume. No running compute is held while waiting.

**Important**
Connectors execute the configuration you provide. SDMA validates the structure and security credentials of a connector, but does not evaluate the business logic of the configuration. For example, if a connector is configured to produce malformed data or send metadata to an unintended destination, SDMA executes those actions as configured. Test connector configurations thoroughly in a non-production environment before enabling them.

## How connectors work
<a name="how-connectors-work"></a>

SDMA provides a small set of integration primitives — REST, S3, Deadline Cloud, Lambda, EventBridge — that connect your assets with the outside world. Each primitive can produce new content and bring it into SDMA (derive), or send content outward to external systems (publish). For a simple, single action — push metadata to an API, look up values from a CSV, submit a compute job — use a single-step publisher or deriver. When you need more, compose those same primitives into multi-step workflows within a single trigger. The primitives are the same either way.

A connector is a governed composition of five surfaces:
+  **Resource surface** – What external resources can be discovered, validated, and displayed. Not all connectors need this — it is for connectors that expose selectable values or linked external identities.
+  **Mapping surface** – How values move between SDMA and the external system. Field mappings transform resource metadata into the structure the external system expects, and can route external response values back into SDMA metadata.
+  **Execution surface** – What triggers exist, what events they match, and what steps run. SDMA has two execution models: the lookup-derivation model for bulk metadata enrichment, and the trigger\+steps model for step-composed workflows and publishing.
+  **Security surface** – How the connector authenticates, what secrets it uses, and what IAM roles it assumes.
+  **Operational surface** – How failures are handled, what policy disables runaway behavior, and what invocation state is visible for troubleshooting.

### Execution flow
<a name="_execution-flow"></a>

When a resource event occurs (for example, an asset is created or a file upload completes):

1. SDMA evaluates all connectors associated with the asset’s template.

1. For each connector, SDMA matches the event against the connector’s triggers. SDMA skips any connector with no matching trigger for the current event — attachment does not imply execution.

1. Every trigger whose resource type, event, and filters match the current event executes independently, each producing its own invocation record.

1. For triggers with a `dependsOn` list, SDMA checks whether the upstream connectors have completed within the same lifecycle context before dispatching.

1. Each trigger’s steps execute in order, sharing intermediate state through `$temp.*` variables. If a step is a `wait` step, the trigger suspends until a terminal verdict arrives — subsequent steps do not execute until the wait resolves successfully. A wait holds no running compute while pending.

1. SDMA routes results back to the asset record through output routing — as metadata attributes, derived files, or both.

1. Derived files and metadata updates re-enter SDMA as lifecycle events, which can trigger downstream connectors. This is how connectors compose through the asset record without needing to reference each other directly.

### Connector directions
<a name="_connector-directions"></a>

Every connector declares a direction that describes which way content flows across the integration boundary: outward (publish), inward (derive), or both (integration connectors using the `bidirectional` direction).

#### Publishers
<a name="_publishers"></a>

A publish connector sends content from SDMA to an external system. It runs when a lifecycle event matches a trigger — for example, when an asset is created or a file upload completes.

A publisher can be a single operation (one REST call, one S3 write, one EventBridge event) or a composed sequence of steps that together accomplish the publication. In a multi-step publisher, steps execute in order and share intermediate state through `$temp.*` variables. For example, a publisher might create a record in an external system, capture the returned ID, then use that ID to upload file content in a second step.

Each step type is a reusable primitive. The same `rest` step type that powers a simple single-step publisher also participates in multi-step compositions alongside `s3PutObject`, `lambdaInvoke`, `eventBridgePutEvents`, `deadlineJob`, and `wait` steps.

Publisher step configuration and field mappings support `${variable}` substitution against resource metadata, invocation parameters, and built-in invocation fields—see [Invocation built-in variables](connector-configuration.md#invocation-variables) in [Connector configuration](connector-configuration.md).

#### Derivers
<a name="_derivers"></a>

A derive connector brings new content, reference data, or capability into SDMA. Derivers fill one or more of three roles:
+  **Content transformation and production.** The connector executes work against an external system — a compute job, an API call, or an inference request. It routes the result back into the asset record as metadata attributes, derived files, or both. A Deadline Cloud job that converts a CAD file to a reviewable 3D format is a content producer. So is a REST call that runs quality analysis and writes scores back to the asset. Content producers can be single-step or multi-step, and they use the same step types and composition model as publishers.
+  **Metadata lookup and enrichment.** The connector fetches records from an external data source (an S3 CSV file, a DynamoDB table, or a REST API). It matches records to SDMA files or assets by a key field and writes the matched values as metadata attributes. This is the lookup-derivation model — designed for bulk enrichment where many files need metadata from the same external source.
+  **Resource provision.** The connector exposes external resources that users can browse and select — available projects in a connected application, collections in a catalog, models in a library. Users link selected resources to SDMA projects or assets, and subsequent triggers can reference them. A connector that provides resources does not need lifecycle triggers — its value is in what it exposes, not in what it executes on events.

A single derive connector can fill multiple roles. A connector integrating with a geospatial platform might provide resources for project linking at authoring time and enrich file metadata from the platform’s catalog on upload. It can also submit compute jobs for spatial analysis — all through one governed contract.

#### Integration connectors
<a name="_integration-connectors"></a>

An integration connector combines publish and derive roles in a single governed contract. Set the direction to `bidirectional` when the external system has a deep relationship with SDMA that spans both directions.

Integration connectors are multi-step and potentially bidirectional. They can compose operations across both directions — deriving content inward and publishing content outward — in a single governed contract. For example, a connector integrating with an external CAD management system might:
+ Provide resources so users can discover and link external models during template authoring.
+ Enrich file metadata from the external catalog when matching records are found.
+ Create external records when SDMA projects are created.
+ Upload derived content back to the external system when processing completes.

One connector, one set of credentials, one failure policy, one governance boundary — multiple roles across both directions.

#### How directions compose in multi-step integrations
<a name="_how-directions-compose-in-multi-step-integrations"></a>

Directions describe which way content flows. Step types describe what each operation does. These are independent axes. A derive connector uses the same `rest` step type a publisher uses. The difference is that the deriver routes results back into the asset record through output routing, while the publisher sends content outward.

Multi-step triggers can combine operations that feel like both directions. A trigger might call an external API to create a job (outward), poll for completion (outward), fetch the results (inward), and write metadata back to the asset (inward). All of these run in one trigger and SDMA tracks them as one invocation. The connector’s declared direction describes the overall intent; the steps describe the mechanics.

When one connector’s output needs to feed another connector’s input, composition happens through the asset record. A derive connector that produces a derived file creates a lifecycle event. A publish connector with a trigger on `derivationComplete` picks up that event and publishes the result. The two connectors do not reference each other — they compose through what they produce and consume in the asset record.

## Supported connector types
<a name="supported-connector-types"></a>

A connector’s type identifies the external system it connects to. Each type is a multi-purpose primitive — the same type can publish content outward, derive metadata inward, expose resources for discovery, and participate as a step in multi-step workflows. The type determines the protocol and authentication model; the direction, triggers, and configuration determine what the connector does with it.

### AWS Deadline Cloud
<a name="_aws-deadline-cloud"></a>

Step type: `deadlineJob`

 **Roles:** content transformation, derived file production, metadata derivation from job output.

Submits batch processing jobs to AWS Deadline Cloud using Open Job Description templates. Jobs run on managed compute with access to GPUs, large local disks, and the third-party or licensed software your workflows depend on. Examples include CAD converters, point cloud processors, rendering engines, geospatial analysis tools, and AI/ML inference models. Format conversion, 3D rendering, spatial tiling, quality analysis, metadata extraction, and custom processing pipelines all run asynchronously at whatever scale Deadline Cloud provides. Results come back as derived files and metadata attributes on the asset, with full provenance linking the output to the job that produced it.

Deadline Cloud is the compute platform of choice for connector-driven transformation work. SDMA stores Open Job Description templates as governed assets. The combination of these templates with SDMA’s correlation and output routing means compute jobs are auditable, repeatable, and governed through the same template chain as every other connector.

For configuration details, see [Create and transform content with AWS Deadline Cloud](connector-deadline-cloud.md).

### REST API
<a name="_rest-api"></a>

Step type: `rest`

 **Roles:** publish metadata to external APIs, derive metadata from external APIs, expose external resources for discovery and linking, content production through API calls, multi-step orchestration.

The most versatile connector type. A REST connector can call any HTTP endpoint — external project management systems, geospatial platforms, inference services, catalog APIs, or any system with a REST interface. It supports all HTTP methods (GET, POST, PUT, PATCH, DELETE), session initialization for stateful protocols, SIGv4 signing for AWS service endpoints, and binary file upload.

As a publisher, it sends asset metadata to external systems. As a deriver, it calls external APIs and writes results back as metadata or derived files. As a resource provider, it exposes external resources for discovery and linking in the Spatial Data Portal. As a step in a multi-step trigger, it composes with other step types. A single REST connector can fill several of these roles in one governed contract.

For configuration details, see [Working with REST APIs](connector-rest-api.md).

### Amazon S3
<a name="_amazon-s3"></a>

Step types: `s3PutObject`, `s3DeleteObject`

 **Roles:** publish structured metadata to S3, derive metadata from S3 files (CSV, JSON), expose S3-hosted reference data for resource provision.

An S3 connector can write structured JSON metadata to a bucket on asset events (publish role). It can read a CSV or JSON file from S3 and match records to SDMA files for bulk metadata enrichment (lookup role through `s3Lookup`). It can also serve values from an S3-hosted file as selectable options during template authoring (resource provision role).

For configuration details, see [Amazon S3 connector](connector-s3.md). For the lookup role, see [Metadata lookup and enrichment](connector-derivation.md).

### Amazon S3 Import
<a name="_amazon-s3-import"></a>

Step types: `casPutObject`, `deadlineJob`

 **Roles:** Import files from external S3 buckets into SDMA as managed assets.

The Amazon S3 Import connector browses a source S3 bucket (same-account or cross-account), and you can select files in the Spatial Data Portal to import them into SDMA via an AWS Deadline Cloud job. Files are integrity-verified during transfer. This connector is purpose-built for bringing existing S3-hosted data into SDMA without re-uploading through the browser.

For configuration details, see [Importing files from Amazon S3](connector-s3-import.md).

### Amazon DynamoDB
<a name="_amazon-dynamodb"></a>

Step type: n/a (used through the lookup-derivation model)

 **Roles:** derive metadata from DynamoDB tables, expose DynamoDB-hosted reference data for resource provision.

A DynamoDB connector performs single-record lookups by partition key and writes the result as metadata attributes on matched files or assets (lookup role via `dynamodbLookup`). It can also serve values from a DynamoDB table as selectable options during template authoring (resource provision role). DynamoDB connectors are well suited for per-file enrichment where each file maps to a single record in an external table.

For configuration details, see [Metadata lookup and enrichment](connector-derivation.md).

### AWS Lambda
<a name="_aws-lambda"></a>

Step type: `lambdaInvoke`

 **Roles:** content production, custom processing, publish via code.

A Lambda connector invokes a function with resource metadata as the payload. Use this type when the integration requires custom code — transformations, validations, or processing logic that cannot be expressed through the declarative configuration of other step types. Lambda connectors can also route results back into the asset record through output routing, making them content producers as well as publishers.

For configuration details, see [AWS Lambda connector](connector-lambda.md).

### Amazon EventBridge
<a name="_amazon-eventbridge"></a>

Step type: `eventBridgePutEvents`

 **Roles:** publish events to downstream consumers.

An EventBridge connector publishes events to a custom event bus when asset lifecycle events occur. Use this type to fan out resource events to multiple downstream consumers through EventBridge rules — for example, notifying external systems, triggering workflows in other AWS accounts, or feeding event-driven architectures.

For configuration details, see [Amazon EventBridge connector](connector-eventbridge.md).

### STAC API
<a name="_stac-api"></a>

Step type: `rest` (specialized)

 **Roles:** publish asset metadata as STAC Items to geoportal APIs.

A STAC connector maps SDMA assets to the STAC Item specification — geometry, bounding box, temporal properties, and per-file asset entries — and publishes them to a STAC-compliant geoportal API. This is a specialized application of the REST connector type, purpose-built for geospatial catalog interoperability.

For configuration details, see [Publishing to STAC with the REST API connector](connector-stac.md).

### Composable step types
<a name="composable-step-types"></a>

Each connector type is also a reusable step type. Step types are composable — a single trigger can combine steps of different types to build multi-step workflows. For example, a trigger can write metadata to Amazon S3, then invoke a Lambda function to post-process it, and finally publish an event to EventBridge:

```
"triggers": [{
  "resources": ["asset"],
  "events": ["create"],
  "steps": [
    {
      "stepType": "s3PutObject",
      "s3Config": { "objectKey": "raw/${asset.assetId}.json" }
    },
    {
      "stepType": "lambdaInvoke",
      "lambdaConfig": { "functionArn": "arn:aws:lambda:us-west-2:123456789012:function:post-process" }
    },
    {
      "stepType": "eventBridgePutEvents",
      "eventBridgeConfig": { "eventBusArn": "arn:aws:events:us-west-2:123456789012:event-bus/my-bus", "source": "sdma", "detailType": "AssetPublished" }
    }
  ]
}]
```

The `deadlineJob` step type can also participate in multi-step triggers, enabling workflows that combine synchronous steps (REST calls, S3 writes) with asynchronous compute jobs.

This composability means you do not need a separate connector for each destination. A single connector can orchestrate a complete workflow by combining different step types in a single trigger.

## Connectors, templates, and projects
<a name="connector-blast-radius"></a>

SDMA uses a three-level relationship between connectors, asset templates, and projects to control which connectors can run and on which resources.

### How the relationship works
<a name="_how-the-relationship-works"></a>

1.  **Connectors** are created at the library level. A connector defines the integration logic (field mappings, triggers, steps) and security credentials.

1.  **Asset templates** define the structure and rules for assets. Each template has a `permittedConnectorIds` list that controls which connectors are approved for assets created from that template.

1.  **Projects** use asset templates. When an asset is created in a project, only connectors approved by the asset’s template are triggered.

This means:
+ A connector does nothing until it is explicitly added to a template’s `permittedConnectorIds` list.
+ Different templates can approve different connectors, so teams can control which integrations apply to their asset types.
+ Removing a connector ID from a template immediately stops that connector from firing for new events on assets using that template.

### Limiting blast radius
<a name="_limiting-blast-radius"></a>

This three-level model limits the blast radius of any single connector:

| Control | Effect |
| --- | --- |
| IAM role permissions | Restricts what AWS resources the connector can access. Scope the role to specific buckets, functions, or event buses. |
| Template approval | Restricts which asset types trigger the connector. A connector not listed in a template’s `permittedConnectorIds` is never invoked for assets of that type. |
| Trigger filters | Restricts which specific events and resources activate the connector. A trigger with `"events": ["create"]` does not fire on updates or deletes. |
| Payload field filtering | Restricts which metadata fields are sent to the external system. Use `payload.fields` to include only the fields the external system needs. |
| Failure policy | Automatically disables a connector after repeated failures, preventing runaway error loops. |

**Important**
SDMA executes connector configurations as defined. To reduce risk, scope IAM roles to the minimum required permissions, test configurations with non-production data, and review trigger filters before enabling a connector.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
