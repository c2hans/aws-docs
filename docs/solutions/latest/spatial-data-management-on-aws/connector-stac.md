---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-stac.html
---

# Publishing to STAC with the REST API connector
<a name="connector-stac"></a>

This guide shows how to use the REST API connector to publish SDMA asset metadata as [STAC (SpatioTemporal Asset Catalog)](https://stacspec.org/) Items to a STAC-compliant API. STAC connectors are not a separate connector type — they are REST API connectors configured with field mappings that construct STAC Items and triggers that target STAC collection endpoints.

Use this pattern to integrate with geoportal platforms or any STAC-compliant catalog. When assets are created, updated, or deleted in SDMA, the connector automatically publishes, updates, or removes the corresponding STAC Items.

## How it works
<a name="stac-how-it-works"></a>

The connector maps SDMA asset metadata to the STAC Item specification using field mappings, then publishes the result to STAC collection endpoints using REST steps:
+  **Create** — When an asset is created (or on demand), the connector POSTs a STAC Item to the collection.
+  **Update** — When an asset is updated, the connector DELETEs the existing item, polls until the deletion is confirmed, then POSTs the updated item. This delete-wait-recreate pattern avoids conflicts with STAC APIs that reject duplicate IDs.
+  **Delete** — When an asset is deleted, the connector DELETEs the STAC Item.

The connector also supports **resource discovery** — it queries the STAC API’s `/collections` endpoint so users can select a target collection when linking a project in the Spatial Data Portal.

## Prerequisites
<a name="stac-prerequisites"></a>

1. Deploy or have access to a STAC-compliant API endpoint (for example, a geoportal instance).

1. Create a STAC collection in the target catalog to receive items.

1. Store API credentials in AWS Secrets Manager (for Basic auth, use `username` and `password` keys).

1. Create an IAM role:
   +  **Role name** must start with `SpatialDataManagementContentPublisher-` (for example, `SpatialDataManagementContentPublisher-STAC`).
   +  **Trust policy** must allow the SDMA solution account to assume it.
   +  **Permissions policy** must grant `secretsmanager:GetSecretValue` on the credentials secret.

## Create this connector
<a name="stac-create"></a>

1. In the Spatial Data Portal, go to **Library settings** > **Connectors**.

1. Choose the **Publish content** tab.

1. Choose **Create publisher**.

1. Enter a connector name.

1. For **Connector type**, select **REST API**.

1. Paste the connector configuration JSON (see [Full configuration](#stac-full-configuration)) into the JSON editor.

1. Choose **Create**.

**Note**
STAC connectors use the REST API connector type. The STAC-specific behavior comes entirely from the configuration — the field mappings construct STAC Items and the triggers target STAC API endpoints.

## Associate a project with a STAC collection
<a name="stac-collection-linking"></a>

The connector publishes items to a specific STAC collection. To link a project to a collection:

1. When creating or editing a project, choose the STAC connector from the connected resources list.

1. Select the target STAC collection from the dropdown. The connector queries your STAC API’s `/collections` endpoint to populate this list.

1. Save the project.

The selected collection ID is stored as the `stac_collection_id` metadata attribute on the project. The connector’s triggers use this value in URL paths — for example, `POST /stac/collections/${project.metadataAttributes.stac_collection_id}/items`.

## Full configuration
<a name="stac-full-configuration"></a>

The following is a complete, working STAC connector configuration. Replace the placeholder values with your environment-specific values.

```
{
  "resources": {
    "project": {
      "discover": {
        "responseListField": "collections",
        "path": "/stac/collections",
        "fieldMapping": {
          "project.stac_collection_id": "id"
        },
        "method": "GET",
        "valueField": "id",
        "labelField": "id"
      },
      "display": {
        "displayId": {
          "name": "Collection name",
          "value": "${project.metadataAttributes.stac_collection_id}"
        },
        "connectedResourceName": "collection"
      }
    }
  },
  "restConfig": {
    "apiBase": "http://<STAC_API_HOST>:<PORT>/geoportal",
    "authProvider": "basic_auth",
    "securityConfig": {
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-STAC",
      "password": "${secret.password}",
      "type": "BasicAuth",
      "secretArn": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret:<SECRET_NAME>",
      "username": "${secret.username}"
    }
  },
  "fieldMappings": [
    { "source": "asset.assetId", "target": "id" },
    { "source": "asset.assetName", "target": "title" },
    { "source": "asset.geoLocation.lon", "target": "geometry.coordinates[0]" },
    { "source": "asset.geoLocation.lat", "target": "geometry.coordinates[1]" },
    { "source": "geoJson:asset.geoLocation", "target": "bbox" },
    { "source": "literal:Point", "target": "geometry.type" },
    { "source": "asset.assetName", "target": "properties.title" },
    { "source": "system.timestamp", "target": "properties.datetime" },
    { "source": "project.projectId", "target": "properties.sdmaProjectId" },
    { "source": "asset.assetId", "target": "properties.sdmaAssetId" },
    { "source": "literal:", "target": "properties.sdmaTemplateId" },
    { "source": "literal:[]", "target": "links" },
    { "source": "asset.metadataAttributes", "target": "properties.tags" },
    { "source": "literal:Feature", "target": "type" },
    { "source": "project.metadataAttributes.stac_collection_id", "target": "collection" },
    { "source": "asset.files[*].path", "target": "assets[${file.path}].title" },
    { "source": "asset.files[*].size", "target": "assets[${file.path}].x:size" },
    { "source": "asset.files[*].mtime", "target": "assets[${file.path}].x:mtime" },
    { "source": "asset.files[*].type", "target": "assets[${file.path}].x:type" },
    { "source": "asset.files[*].path", "target": "assets[${file.path}].x:path" },
    { "source": "asset.files[*].geoLocation.lon", "target": "assets[${file.path}].x:geometry.coordinates[0]" },
    { "source": "asset.files[*].geoLocation.lat", "target": "assets[${file.path}].x:geometry.coordinates[1]" },
    { "source": "literal:Point", "target": "assets[${file.path}].x:geometry.type" },
    { "source": "asset.files[*].metadataAttributes", "target": "assets[${file.path}].x:metadataAttributes" },
    { "source": "asset.files[*].contentUrl", "target": "assets[${file.path}].href" },
    { "source": "asset.files[*].type", "target": "assets[${file.path}].type" },
    { "source": "literal:data", "target": "assets[${file.path}].roles[0]" }
  ],
  "triggers": [
    {
      "description": "Create STAC item on asset creation",
      "resources": ["asset"],
      "events": ["create", "onDemand"],
      "steps": [{
        "method": "POST",
        "path": "/stac/collections/${project.metadataAttributes.stac_collection_id}/items"
      }]
    },
    {
      "description": "Update STAC item (delete, wait, recreate)",
      "resources": ["asset"],
      "events": ["update"],
      "steps": [
        {
          "method": "DELETE",
          "path": "/stac/collections/${project.metadataAttributes.stac_collection_id}/items?ids=${asset.assetId}"
        },
        {
          "method": "GET",
          "path": "/stac/collections/${project.metadataAttributes.stac_collection_id}/items/${asset.assetId}",
          "sleepTime": 1,
          "retryCount": 10,
          "successConditions": {
            "expectSuccess": false,
            "responseMatch": { "error": "not found" }
          }
        },
        {
          "method": "POST",
          "path": "/stac/collections/${project.metadataAttributes.stac_collection_id}/items"
        }
      ]
    },
    {
      "description": "Delete STAC item on asset deletion",
      "resources": ["asset"],
      "events": ["delete"],
      "steps": [{
        "method": "DELETE",
        "path": "/stac/collections/${project.metadataAttributes.stac_collection_id}/items?ids=${asset.assetId}"
      }]
    }
  ]
}
```

## Understanding the field mappings
<a name="stac-field-mappings"></a>

The field mappings construct a STAC Item from SDMA asset metadata. The key patterns:

### Core STAC Item fields
<a name="_core-stac-item-fields"></a>

| STAC field | Source | Notes |
| --- | --- | --- |
|  `id`  |  `asset.assetId`  | Unique identifier for the STAC Item. |
|  `type`  |  `literal:Feature`  | Required by the STAC spec. |
|  `collection`  |  `project.metadataAttributes.stac_collection_id`  | Links the item to the collection selected during project setup. |
|  `geometry.type`  |  `literal:Point`  | Point geometry from the asset’s geolocation. |
|  `geometry.coordinates`  |  `asset.geoLocation.lon`, `asset.geoLocation.lat`  | Longitude and latitude. |
|  `bbox`  |  `geoJson:asset.geoLocation`  | Bounding box computed from the geolocation using the `geoJson:` prefix. |
|  `properties.datetime`  |  `system.timestamp`  | Publication timestamp. |
|  `properties.title`  |  `asset.assetName`  | Human-readable title. |
|  `properties.tags`  |  `asset.metadataAttributes`  | All asset metadata attributes as a tags object. |

### Per-file asset entries
<a name="_per-file-asset-entries"></a>

The `assets[${file.path}]` pattern iterates over all files in the SDMA asset and creates a STAC asset entry for each one:

| STAC asset field | Source |
| --- | --- |
|  `href`  |  `asset.files[*].contentUrl` — Download URL for the file. |
|  `title`  |  `asset.files[*].path` — Original file path. |
|  `type`  |  `literal:application/json` — Media type. |
|  `roles[0]`  |  `literal:data` — STAC asset role. |
|  `x:size`  |  `asset.files[*].size` — File size. |
|  `x:mtime`  |  `asset.files[*].mtime` — Last modified time. |
|  `x:geometry`  |  `asset.files[*].geoLocation` — Per-file geolocation. |
|  `x:metadataAttributes`  |  `asset.files[*].metadataAttributes` — Per-file metadata. |

Fields prefixed with `x:` are STAC extension properties — custom fields that carry SDMA-specific metadata into the catalog.

## The update pattern
<a name="stac-update-pattern"></a>

The update trigger uses a three-step delete-wait-recreate pattern because many STAC APIs reject POST requests when an item with the same ID already exists:

1.  **DELETE** the existing item by ID.

1.  **GET** the item with `retryCount: 10` and `sleepTime: 1`, using `expectSuccess: false` with `responseMatch: { "error": "not found" }`. This polls until the deletion is confirmed — the step succeeds when the API returns a "not found" error.

1.  **POST** the updated item.

This pattern is reusable for any REST API that doesn’t support idempotent PUT operations. See [connected resources](connector-rest-api.md#rest-connected-resources) in the REST API connector documentation for more on multi-step patterns.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
