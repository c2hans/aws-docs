---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/api-reference.html
---

# API Reference
<a name="api-reference"></a>

This section provides a complete reference for the Spatial Data Management on AWS REST API (version 2025-04-18). The API provides comprehensive spatial data organization, storage, and collaboration capabilities. You can organize spatial assets into libraries and projects, manage access controls, and integrate with external data sources through connectors.

**Important**
All endpoints in this reference use the `/iam` path prefix and require AWS IAM (Signature Version 4) authentication. For setup instructions, see [API Authentication](api-authentication.md).

## Base URL
<a name="api-base-url"></a>

The API base URL is available from the `SpatialDataManagementApiEndpoint` parameter in AWS Systems Manager Parameter Store, or from the AWS CloudFormation stack outputs after deployment. All endpoints below are relative to this base URL and are prefixed with `/iam`.

## Libraries
<a name="api-libraries"></a>

### GET `/iam/libraries`
<a name="listlibraries"></a>

 **Operation ID:** `ListLibraries`

Retrieves a paginated list of all libraries accessible to the authenticated user. Libraries are organizational containers that hold projects, assets, and templates. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `libraries`  | Array of [Library](#schema-library)  | List of libraries accessible to the user |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}`
<a name="getlibrary"></a>

 **Operation ID:** `GetLibrary`

Retrieves detailed information about a specific library. Returns library metadata including storage configuration, creation details, and access permissions.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `libraryName`  | String | — |
|  `storageConfig`  | Object | S3 storage configuration defining where library data is stored |
|  `storageConfig.defaultS3BucketName`  | String | Default S3 bucket name for library storage |
|  `storageConfig.defaultRootS3Prefix`  | String | Default root S3 prefix for organizing library data |
|  `solutionVersion`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Projects
<a name="api-projects"></a>

### GET `/iam/libraries/{libraryId}/projects`
<a name="listprojects"></a>

 **Operation ID:** `ListProjects`

Retrieves a paginated list of projects resources. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `principalId`  | query | String | No | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `projects`  | Array of [Project](#schema-project)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/projects`
<a name="createproject"></a>

 **Operation ID:** `CreateProject`

Creates a new project resource with the specified configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `projectName`  | String | Yes | — |
|  `projectConfig`  | Object | No | Configuration settings for project. |
|  `projectConfig.name`  | String | No | — |
|  `projectConfig.permittedTemplateIds`  | Array of String | No | — |
|  `projectConfig.description`  | String | No | — |
|  `projectConfig.thumbnailHash`  | String | No | — |
|  `projectConfig.allowNonTemplatedAssets`  | Boolean | No | — |
|  `projectConfig.s3BucketName`  | String | No | — |
|  `projectConfig.rootPrefix`  | String | No | — |
|  `projectConfig.latitude`  | Number | No | — |
|  `projectConfig.longitude`  | Number | No | — |
|  `projectConfig.place`  | String | No | — |
|  `projectConfig.metadata`  | Object | No | — |
|  `projectThumbnailObjectKey`  | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `projectId`  | String | — |
|  `projectName`  | String | — |
|  `assetCount`  | Number | — |
|  `fileCount`  | Number | — |
|  `totalSize`  | Number | — |
|  `s3BucketName`  | String | — |
|  `rootPrefix`  | String | — |
|  `manifestPrefix`  | String | — |
|  `thumbnailObjectKey`  | String | — |
|  `thumbnailUrl`  | String | — |
|  `permittedTemplateIds`  | Array of String | — |
|  `allowNonTemplatedAssets`  | Boolean | — |
|  `description`  | String | — |
|  `metadataAttributes`  | Array of [MetadataAttribute](#schema-metadataattribute)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}`
<a name="getproject"></a>

 **Operation ID:** `GetProject`

Retrieves detailed information about a specific project resource.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `projectId`  | String | — |
|  `projectName`  | String | — |
|  `assetCount`  | Number | — |
|  `fileCount`  | Number | — |
|  `totalSize`  | Number | — |
|  `s3BucketName`  | String | — |
|  `rootPrefix`  | String | — |
|  `manifestPrefix`  | String | — |
|  `thumbnailObjectKey`  | String | — |
|  `thumbnailUrl`  | String | — |
|  `permittedTemplateIds`  | Array of String | — |
|  `allowNonTemplatedAssets`  | Boolean | — |
|  `description`  | String | — |
|  `metadataAttributes`  | Array of [MetadataAttribute](#schema-metadataattribute)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### PUT `/iam/libraries/{libraryId}/projects/{projectId}`
<a name="updateproject"></a>

 **Operation ID:** `UpdateProject`

Updates an existing project resource configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `projectName`  | String | No | — |
|  `projectConfig`  | Object | No | Configuration settings for project. |
|  `projectConfig.name`  | String | No | — |
|  `projectConfig.permittedTemplateIds`  | Array of String | No | — |
|  `projectConfig.description`  | String | No | — |
|  `projectConfig.thumbnailHash`  | String | No | — |
|  `projectConfig.allowNonTemplatedAssets`  | Boolean | No | — |
|  `projectConfig.s3BucketName`  | String | No | — |
|  `projectConfig.rootPrefix`  | String | No | — |
|  `projectConfig.latitude`  | Number | No | — |
|  `projectConfig.longitude`  | Number | No | — |
|  `projectConfig.place`  | String | No | — |
|  `projectConfig.metadata`  | Object | No | — |
|  `projectThumbnailObjectKey`  | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `projectId`  | String | — |
|  `projectName`  | String | — |
|  `assetCount`  | Number | — |
|  `fileCount`  | Number | — |
|  `totalSize`  | Number | — |
|  `s3BucketName`  | String | — |
|  `rootPrefix`  | String | — |
|  `manifestPrefix`  | String | — |
|  `thumbnailObjectKey`  | String | — |
|  `thumbnailUrl`  | String | — |
|  `permittedTemplateIds`  | Array of String | — |
|  `allowNonTemplatedAssets`  | Boolean | — |
|  `description`  | String | — |
|  `metadataAttributes`  | Array of [MetadataAttribute](#schema-metadataattribute)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### DELETE `/iam/libraries/{libraryId}/projects/{projectId}`
<a name="deleteproject"></a>

 **Operation ID:** `DeleteProject`

Deletes a project resource and all its associated data. This operation is irreversible.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/asset-templates/{templateId}/connectors/{connectorId}/resources`
<a name="getconnectorresourcesviaassettemplateproject"></a>

 **Operation ID:** `GetConnectorResourcesViaAssetTemplateProject`

Retrieves connector resources via an asset template with project membership validation.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `resources`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/projects/{projectId}/asset-templates/{templateId}/connectors/{connectorId}/verify`
<a name="verifyprojectconnectorrelationship"></a>

 **Operation ID:** `VerifyProjectConnectorRelationship`

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `result`  | Boolean | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets`
<a name="listassets"></a>

 **Operation ID:** `ListAssets`

Retrieves a paginated list of assets resources. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `assetName`  | query | String | No | — |
|  `assetState`  | query |  [AssetState](#schema-assetstate)  | No | — |
|  `statusCode`  | query |  [ResourceStatus](#schema-resourcestatus)  | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `assets`  | Array of [Asset](#schema-asset)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/projects/{projectId}/assets`
<a name="createasset"></a>

 **Operation ID:** `CreateAsset`

Creates a new asset resource with the specified configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetName`  | String | Yes | — |
|  `assetId`  | String | Yes | — |
|  `manifestHash`  | String | No | — |
|  `manifestObjectKey`  | String | No | — |
|  `sourceAsset`  | Object | No | — |
|  `sourceAsset.assetId`  | String | Yes | — |
|  `sourceAsset.projectId`  | String | Yes | — |
|  `sourceAsset.libraryId`  | String | Yes | — |
|  `mergeAssets`  | Array of [AssetReference](#schema-assetreference)  | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `assetId`  | String | — |
|  `assetName`  | String | — |
|  `projectId`  | String | — |
|  `libraryId`  | String | — |
|  `assetState`  |  [AssetState](#schema-assetstate)  | — |
|  `fileCount`  | Number | — |
|  `totalSize`  | Number | — |
|  `thumbnailUrl`  | String | — |
|  `thumbnailFileId`  | String | — |
|  `thumbnailObjectKey`  | String | — |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | — |
|  `manifestHash`  | String | — |
|  `statusCode`  |  [ResourceStatus](#schema-resourcestatus)  | — |
|  `statusMessage`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}`
<a name="getasset"></a>

 **Operation ID:** `GetAsset`

Retrieves detailed information about a specific asset resource.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `assetId`  | String | — |
|  `assetName`  | String | — |
|  `projectId`  | String | — |
|  `libraryId`  | String | — |
|  `assetState`  |  [AssetState](#schema-assetstate)  | — |
|  `fileCount`  | Number | — |
|  `totalSize`  | Number | — |
|  `thumbnailUrl`  | String | — |
|  `thumbnailFileId`  | String | — |
|  `thumbnailObjectKey`  | String | — |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | — |
|  `manifestHash`  | String | — |
|  `statusCode`  |  [ResourceStatus](#schema-resourcestatus)  | — |
|  `statusMessage`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### PUT `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}`
<a name="updateasset"></a>

 **Operation ID:** `UpdateAsset`

Updates an existing asset resource configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `uploadState`  |  [UploadState](#schema-uploadstate)  | No | — |
|  `assetState`  |  [UserUpdatableAssetState](#schema-userupdatableassetstate)  | No | — |
|  `manifestHash`  | String | No | — |
|  `manifestObjectKey`  | String | No | — |
|  `activeVersionId`  | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `assetId`  | String | — |
|  `assetName`  | String | — |
|  `projectId`  | String | — |
|  `libraryId`  | String | — |
|  `assetState`  |  [AssetState](#schema-assetstate)  | — |
|  `fileCount`  | Number | — |
|  `totalSize`  | Number | — |
|  `thumbnailUrl`  | String | — |
|  `thumbnailFileId`  | String | — |
|  `thumbnailObjectKey`  | String | — |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | — |
|  `manifestHash`  | String | — |
|  `statusCode`  |  [ResourceStatus](#schema-resourcestatus)  | — |
|  `statusMessage`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### DELETE `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}`
<a name="deleteasset"></a>

 **Operation ID:** `DeleteAsset`

Deletes an asset resource and all its associated data. This operation is irreversible.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `force`  | query | Boolean | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `assetState`  |  [AssetState](#schema-assetstate)  | — |
|  `message`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/asset-templates/{templateId}/connectors/{connectorId}/resources`
<a name="getconnectorresourcesviaasset"></a>

 **Operation ID:** `GetConnectorResourcesViaAsset`

Retrieves connector resources in the context of an asset, enabling server-side resolution of asset and file metadata for variable substitution.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `resourceType`  | query | String | Yes | — |
|  `fileId`  | query | String | No | Pattern: `^file-[a-fA-F0-9]{32}$`  |
|  `fileIds`  | query | String | No | Comma-separated list of file IDs. When provided, metadata from all files is merged (e.g. lumidb\_id values combined for multi-file queries). |
|  `aabb`  | query | String | No | JSON-encoded axis-aligned bounding box for spatial filtering. Passed through to the connector as a boundary parameter. |
|  `params`  | query | String | No | Optional JSON-encoded parameters for truly dynamic values (e.g., tile URI) that cannot be resolved from metadata. |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `resources`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/asset-templates/{templateId}/connectors/{connectorId}/trigger`
<a name="triggerconnectoronasset"></a>

 **Operation ID:** `TriggerConnectorOnAsset`

Triggers a connector on asset processing or validation workflow.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `fileId`  | query | String | No | Unique identifier for the file |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `result`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/asset-templates/{templateId}/connectors/{connectorId}/verify`
<a name="verifyassetconnectorrelationship"></a>

 **Operation ID:** `VerifyAssetConnectorRelationship`

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `fileId`  | query | String | No | Pattern: `^file-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `result`  | Boolean | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/attributes`
<a name="listassetattributes"></a>

 **Operation ID:** `ListAssetAttributes`

Retrieves a paginated list of asset attributes. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/connectors/{connectorId}/trigger`
<a name="triggerconnectoronassetdirect"></a>

 **Operation ID:** `TriggerConnectorOnAssetDirect`

Triggers a connector on asset (direct) processing or validation workflow.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `fileId`  | query | String | No | Unique identifier for the file |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `result`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/credentials`
<a name="getassetcredentials"></a>

 **Operation ID:** `GetAssetCredentials`

Retrieves detailed information about asset credentials.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `operation`  | query |  [AccessRequestOperation](#schema-accessrequestoperation)  | Yes | — |
|  `location`  | query |  [AssetAccessLocation](#schema-assetaccesslocation)  | Yes | — |
|  `requestType`  | query |  [CredentialVendingRequestType](#schema-credentialvendingrequesttype)  | No | — |
|  `expirationDuration`  | query | Number | No | — |
|  `fileInfo`  | query | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `credentials`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/files`
<a name="listfiles"></a>

 **Operation ID:** `ListFiles`

Retrieves a paginated list of files resources. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `root`  | query | String | No | — |
|  `includeHiddenFiles`  | query | Boolean | No | — |
|  `includePreviews`  | query | Boolean | No | — |
|  `includeLocations`  | query | Boolean | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `files`  | Array of [File](#schema-file)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/files/{fileIdOrPathId}`
<a name="getfile"></a>

 **Operation ID:** `GetFile`

Retrieves detailed information about a specific file resource.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `fileIdOrPathId`  | path | String | Yes | Pattern: `^(file\|path)-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `fileId`  | String | — |
|  `pathId`  | String | — |
|  `assetId`  | String | — |
|  `path`  | String | — |
|  `mtime`  | Number | — |
|  `addedAt`  | Number | — |
|  `size`  | Number | — |
|  `objectKey`  | String | — |
|  `hash`  | String | — |
|  `state`  |  [FileState](#schema-filestate)  | — |
|  `analysisState`  |  [AnalysisState](#schema-analysisstate)  | — |
|  `connectorInvocationSummary`  | Object | Summary of connector invocation states for a resource. Cached on the resource record for efficient list-view rendering. Extensible: future releases may add byDirection or byConnectorId breakdowns. |
|  `connectorInvocationSummary.total`  | Number | — |
|  `connectorInvocationSummary.succeeded`  | Number | — |
|  `connectorInvocationSummary.failed`  | Number | — |
|  `connectorInvocationSummary.inProgress`  | Number | — |
|  `connectorInvocationSummary.queued`  | Number | — |
|  `connectorInvocationSummary.waiting`  | Number | — |
|  `connectorInvocationSummary.blocked`  | Number | — |
|  `connectorInvocationSummary.notApplicable`  | Number | — |
|  `hasAttributeSuggestions`  | Boolean | — |
|  `versionId`  | String | — |
|  `suggestedMetadataAttributes`  | Array of [Attribute](#schema-attribute)  | — |
|  `metadataAttributes`  | Array of [Attribute](#schema-attribute)  | — |
|  `location`  | Object | — |
|  `location.latitude`  | Number | — |
|  `location.longitude`  | Number | — |
|  `location.place`  | String | — |
|  `location.geoJson`  | String | — |
|  `location.aabb`  | String | — |
|  `url`  | String | — |
|  `previews`  | Array of [FilePreview](#schema-filepreview)  | — |
|  `connectorInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/files/{fileIdOrPathId}/content`
<a name="getfilecontent"></a>

 **Operation ID:** `GetFileContent`

Retrieves the content of a specific file.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `fileIdOrPathId`  | path | String | Yes | Pattern: `^(file\|path)-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/files/{fileIdOrPathId}/versions`
<a name="listfileversions"></a>

 **Operation ID:** `ListFileVersions`

Retrieves a paginated list of file versions. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `fileIdOrPathId`  | path | String | Yes | Pattern: `^(file\|path)-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `versions`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/files/{fileIdOrPathId}/versions/{versionId}`
<a name="getfileversion"></a>

 **Operation ID:** `GetFileVersion`

Retrieves detailed information about a specific file version.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `fileIdOrPathId`  | path | String | Yes | Pattern: `^(file\|path)-[a-fA-F0-9]{32}$`  |
|  `versionId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}-version-[1-9][0-9]*$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `fileId`  | String | — |
|  `pathId`  | String | — |
|  `assetId`  | String | — |
|  `path`  | String | — |
|  `mtime`  | Number | — |
|  `addedAt`  | Number | — |
|  `size`  | Number | — |
|  `objectKey`  | String | — |
|  `hash`  | String | — |
|  `state`  |  [FileState](#schema-filestate)  | — |
|  `analysisState`  |  [AnalysisState](#schema-analysisstate)  | — |
|  `connectorInvocationSummary`  | Object | Summary of connector invocation states for a resource. Cached on the resource record for efficient list-view rendering. Extensible: future releases may add byDirection or byConnectorId breakdowns. |
|  `connectorInvocationSummary.total`  | Number | — |
|  `connectorInvocationSummary.succeeded`  | Number | — |
|  `connectorInvocationSummary.failed`  | Number | — |
|  `connectorInvocationSummary.inProgress`  | Number | — |
|  `connectorInvocationSummary.queued`  | Number | — |
|  `connectorInvocationSummary.waiting`  | Number | — |
|  `connectorInvocationSummary.blocked`  | Number | — |
|  `connectorInvocationSummary.notApplicable`  | Number | — |
|  `hasAttributeSuggestions`  | Boolean | — |
|  `versionId`  | String | — |
|  `suggestedMetadataAttributes`  | Array of [Attribute](#schema-attribute)  | — |
|  `metadataAttributes`  | Array of [Attribute](#schema-attribute)  | — |
|  `location`  | Object | — |
|  `location.latitude`  | Number | — |
|  `location.longitude`  | Number | — |
|  `location.place`  | String | — |
|  `location.geoJson`  | String | — |
|  `location.aabb`  | String | — |
|  `url`  | String | — |
|  `previews`  | Array of [FilePreview](#schema-filepreview)  | — |
|  `connectorInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/suggested-attributes`
<a name="listassetsuggestedattributes"></a>

 **Operation ID:** `ListAssetSuggestedAttributes`

Retrieves a paginated list of asset suggested attributes. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `suggestions`  | Array of [FileTypeSuggestion](#schema-filetypesuggestion)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/versions`
<a name="listassetversions"></a>

 **Operation ID:** `ListAssetVersions`

Retrieves a paginated list of asset versions. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `versions`  | Array of [AssetVersion](#schema-assetversion)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/assets/{assetId}/versions/{versionId}/files`
<a name="listfilesforassetversion"></a>

 **Operation ID:** `ListFilesForAssetVersion`

Retrieves a paginated list of files for an asset version. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `assetId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}$`  |
|  `versionId`  | path | String | Yes | Pattern: `^asset-[a-fA-F0-9]{32}-version-[1-9][0-9]*$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `root`  | query | String | No | — |
|  `includeHiddenFiles`  | query | Boolean | No | — |
|  `includePreviews`  | query | Boolean | No | — |
|  `includeLocations`  | query | Boolean | No | — |
|  `includeChanges`  | query | Boolean | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `files`  | Array of [File](#schema-file)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/projects/{projectId}/connectors/{connectorId}/trigger`
<a name="triggerconnectoronprojectdirect"></a>

 **Operation ID:** `TriggerConnectorOnProjectDirect`

Triggers a connector on project (direct) processing or validation workflow.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `result`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/credentials`
<a name="getprojectcredentials"></a>

 **Operation ID:** `GetProjectCredentials`

Retrieves project credentials.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `operation`  | query |  [ProjectAccessOperation](#schema-projectaccessoperation)  | Yes | — |
|  `location`  | query |  [ProjectAccessLocation](#schema-projectaccesslocation)  | Yes | — |
|  `requestType`  | query |  [CredentialVendingRequestType](#schema-credentialvendingrequesttype)  | No | — |
|  `expirationDuration`  | query | Number | No | — |
|  `fileInfo`  | query | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `credentials`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/known-attributes`
<a name="getprojectknownattributes"></a>

 **Operation ID:** `GetProjectKnownAttributes`

Retrieves the known attributes for a specific project.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `attributes`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/members`
<a name="listprojectmembers"></a>

 **Operation ID:** `ListProjectMembers`

Retrieves a paginated list of project members. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | — |
|  `nextToken`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `parameterName`  | String | — |
|  `parameterValue`  | String | — |
|  `allowedValues`  | Array of String | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/members/{principalId}`
<a name="getprojectmember"></a>

 **Operation ID:** `GetProjectMember`

Retrieves detailed information about a specific project member.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `parameterName`  | String | — |
|  `parameterValue`  | String | — |
|  `allowedValues`  | Array of String | — |

### POST `/iam/libraries/{libraryId}/projects/{projectId}/members/{principalId}`
<a name="addprojectmember"></a>

 **Operation ID:** `AddProjectMember`

Adds a new member to the project with specified access level. Members can be users or groups with roles: OWNER, MANAGER, CONTRIBUTOR, or VIEWER.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### PUT `/iam/libraries/{libraryId}/projects/{projectId}/members/{principalId}`
<a name="updateprojectmember"></a>

 **Operation ID:** `UpdateProjectMember`

Updates an existing project member configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### DELETE `/iam/libraries/{libraryId}/projects/{projectId}/members/{principalId}`
<a name="deleteprojectmember"></a>

 **Operation ID:** `DeleteProjectMember`

Deletes a project member resource and all its associated data. This operation is irreversible.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### GET `/iam/libraries/{libraryId}/projects/{projectId}/permissions`
<a name="getprojectpermissions"></a>

 **Operation ID:** `GetProjectPermissions`

Retrieves project permissions.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `permissions`  | Array of String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Assets
<a name="api-assets"></a>

### GET `/iam/libraries/{libraryId}/assets`
<a name="listlibraryassets"></a>

 **Operation ID:** `ListLibraryAssets`

Retrieves a paginated list of library assets. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `assetState`  | query |  [AssetState](#schema-assetstate)  | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `assets`  | Array of [Asset](#schema-asset)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Asset Templates
<a name="api-asset-templates"></a>

### GET `/iam/libraries/{libraryId}/asset-templates`
<a name="listassettemplates"></a>

 **Operation ID:** `ListAssetTemplates`

Retrieves a paginated list of assettemplates resources. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `permittedConnectorIds`  | query | String | No | — |
|  `preview`  | query | Boolean | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `templates`  | Array of [AssetTemplateMinimal](#schema-assettemplateminimal)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/asset-templates`
<a name="createassettemplate"></a>

 **Operation ID:** `CreateAssetTemplate`

Creates a new assettemplate resource with the specified configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetTemplateConfig`  | Object | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `assetTemplateId`  | String | — |
|  `assetTemplateName`  | String | — |
|  `assetTemplateConfig`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/asset-templates/{templateId}`
<a name="getassettemplate"></a>

 **Operation ID:** `GetAssetTemplate`

Retrieves detailed information about a specific assettemplate resource.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `assetTemplateId`  | String | — |
|  `assetTemplateName`  | String | — |
|  `assetTemplateConfig`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### PUT `/iam/libraries/{libraryId}/asset-templates/{templateId}`
<a name="updateassettemplate"></a>

 **Operation ID:** `UpdateAssetTemplate`

Updates an existing assettemplate resource configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetTemplateConfig`  | Object | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `assetTemplateId`  | String | — |
|  `assetTemplateName`  | String | — |
|  `assetTemplateConfig`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### DELETE `/iam/libraries/{libraryId}/asset-templates/{templateId}`
<a name="deleteassettemplate"></a>

 **Operation ID:** `DeleteAssetTemplate`

Deletes an asset template resource and all its associated data. This operation is irreversible.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/asset-templates/{templateId}/assets`
<a name="listassettemplateassets"></a>

 **Operation ID:** `ListAssetTemplateAssets`

Retrieves a paginated list of asset template assets. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `projectId`  | query | String | No | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `assets`  | Object | — |
|  `hiddenAssetsCount`  | Number | — |
|  `totalAssetsCount`  | Number | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/asset-templates/{templateId}/connectors/{connectorId}/resources`
<a name="getconnectorresourcesviaassettemplate"></a>

 **Operation ID:** `GetConnectorResourcesViaAssetTemplate`

Retrieves connector resources via an asset template.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `resources`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/asset-templates/{templateId}/members`
<a name="listassettemplatemembers"></a>

 **Operation ID:** `ListAssetTemplateMembers`

Retrieves a paginated list of asset template members. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | — |
|  `nextToken`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/asset-templates/{templateId}/members/{principalId}`
<a name="getassettemplatemember"></a>

 **Operation ID:** `GetAssetTemplateMember`

Retrieves detailed information about a specific asset template member.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/asset-templates/{templateId}/members/{principalId}`
<a name="addassettemplatemember"></a>

 **Operation ID:** `AddAssetTemplateMember`

Adds a new member to the assettemplate with specified access level. Members can be users or groups with roles: OWNER, MANAGER, CONTRIBUTOR, or VIEWER.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### PUT `/iam/libraries/{libraryId}/asset-templates/{templateId}/members/{principalId}`
<a name="updateassettemplatemember"></a>

 **Operation ID:** `UpdateAssetTemplateMember`

Updates an existing asset template member configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### DELETE `/iam/libraries/{libraryId}/asset-templates/{templateId}/members/{principalId}`
<a name="deleteassettemplatemember"></a>

 **Operation ID:** `DeleteAssetTemplateMember`

Deletes an asset template member resource and all its associated data. This operation is irreversible.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/asset-templates/{templateId}/permissions`
<a name="getassettemplatepermissions"></a>

 **Operation ID:** `GetAssetTemplatePermissions`

Retrieves asset template permissions.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `permissions`  | Array of String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/asset-templates/{templateId}/project-associations`
<a name="listassettemplateprojectassociations"></a>

 **Operation ID:** `ListAssetTemplateProjectAssociations`

Retrieves a paginated list of asset template project associations. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `associations`  | Array of [ProjectAssociationDetail](#schema-projectassociationdetail)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### PUT `/iam/libraries/{libraryId}/asset-templates/{templateId}/project-associations/{projectId}`
<a name="updateassettemplateprojectassociation"></a>

 **Operation ID:** `UpdateAssetTemplateProjectAssociation`

Updates an existing asset template project association configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |
|  `projectId`  | path | String | Yes | Pattern: `^project-[a-fA-F0-9]{32}(-[a-fA-F0-9]{32})?$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `associationType`  |  [AssociationType](#schema-associationtype)  | — |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | — |
|  `requestedBy`  | String | — |
|  `requestedAt`  | Number | — |
|  `reviewedBy`  | String | — |
|  `reviewedAt`  | Number | — |
|  `sourceResourceId`  | String | — |
|  `targetResourceId`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Connectors
<a name="api-connectors"></a>

### GET `/iam/libraries/{libraryId}/connectors`
<a name="listconnectors"></a>

 **Operation ID:** `ListConnectors`

Retrieves a paginated list of connectors resources. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `direction`  | query |  [ConnectorDirection](#schema-connectordirection)  | No | — |
|  `providingResourceType`  | query | String | No | — |
|  `enabled`  | query | Boolean | No | — |
|  `default`  | query | Boolean | No | — |
|  `supportsExistingResource`  | query | Boolean | No | — |
|  `principalId`  | query | String | No | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `connectors`  | Array of [ConnectorMinimal](#schema-connectorminimal)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/connectors`
<a name="createconnector"></a>

 **Operation ID:** `CreateConnector`

Creates a new connector resource with the specified configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `connectorConfig`  | Object | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `connectorId`  | String | — |
|  `connectorName`  | String | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | — |
|  `enabled`  | Boolean | — |
|  `default`  | Boolean | — |
|  `connectorConfig`  | Object | — |
|  `recentInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/connectors/{connectorId}`
<a name="getconnector"></a>

 **Operation ID:** `GetConnector`

Retrieves detailed information about a specific connector resource.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `connectorId`  | String | — |
|  `connectorName`  | String | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | — |
|  `enabled`  | Boolean | — |
|  `default`  | Boolean | — |
|  `connectorConfig`  | Object | — |
|  `recentInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### PUT `/iam/libraries/{libraryId}/connectors/{connectorId}`
<a name="updateconnector"></a>

 **Operation ID:** `UpdateConnector`

Updates an existing connector resource configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `connectorName`  | String | Yes | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | Yes | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | Yes | — |
|  `enabled`  | Boolean | Yes | — |
|  `connectorConfig`  | Object | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `libraryId`  | String | — |
|  `connectorId`  | String | — |
|  `connectorName`  | String | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | — |
|  `enabled`  | Boolean | — |
|  `default`  | Boolean | — |
|  `connectorConfig`  | Object | — |
|  `recentInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### DELETE `/iam/libraries/{libraryId}/connectors/{connectorId}`
<a name="deleteconnector"></a>

 **Operation ID:** `DeleteConnector`

Deletes a connector resource and all its associated data. This operation is irreversible.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/connectors/{connectorId}/asset-template-associations`
<a name="listconnectorassettemplateassociations"></a>

 **Operation ID:** `ListConnectorAssetTemplateAssociations`

Retrieves a paginated list of connector asset template associations. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `associations`  | Array of [AssetTemplateAssociationDetail](#schema-assettemplateassociationdetail)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### PUT `/iam/libraries/{libraryId}/connectors/{connectorId}/asset-template-associations/{templateId}`
<a name="updateconnectorassettemplateassociation"></a>

 **Operation ID:** `UpdateConnectorAssetTemplateAssociation`

Updates an existing connector asset template association configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `templateId`  | path | String | Yes | Pattern: `^template-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `associationType`  |  [AssociationType](#schema-associationtype)  | — |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | — |
|  `requestedBy`  | String | — |
|  `requestedAt`  | Number | — |
|  `reviewedBy`  | String | — |
|  `reviewedAt`  | Number | — |
|  `sourceResourceId`  | String | — |
|  `targetResourceId`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### GET `/iam/libraries/{libraryId}/connectors/{connectorId}/members`
<a name="listconnectormembers"></a>

 **Operation ID:** `ListConnectorMembers`

Retrieves a paginated list of connector members. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | — |
|  `nextToken`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `parameterName`  | String | — |
|  `parameterValue`  | String | — |
|  `allowedValues`  | Array of String | — |

### GET `/iam/libraries/{libraryId}/connectors/{connectorId}/members/{principalId}`
<a name="getconnectormember"></a>

 **Operation ID:** `GetConnectorMember`

Retrieves detailed information about a specific connector member.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `parameterName`  | String | — |
|  `parameterValue`  | String | — |
|  `allowedValues`  | Array of String | — |

### POST `/iam/libraries/{libraryId}/connectors/{connectorId}/members/{principalId}`
<a name="addconnectormember"></a>

 **Operation ID:** `AddConnectorMember`

Adds a new member to the connector with specified access level. Members can be users or groups with roles: OWNER, MANAGER, CONTRIBUTOR, or VIEWER.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### PUT `/iam/libraries/{libraryId}/connectors/{connectorId}/members/{principalId}`
<a name="updateconnectormember"></a>

 **Operation ID:** `UpdateConnectorMember`

Updates an existing connector member configuration.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### DELETE `/iam/libraries/{libraryId}/connectors/{connectorId}/members/{principalId}`
<a name="deleteconnectormember"></a>

 **Operation ID:** `DeleteConnectorMember`

Deletes a connector member resource and all its associated data. This operation is irreversible.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### GET `/iam/libraries/{libraryId}/connectors/{connectorId}/permissions`
<a name="getconnectorpermissions"></a>

 **Operation ID:** `GetConnectorPermissions`

Retrieves connector permissions.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `permissions`  | Array of String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/connectors/{connectorId}/resources`
<a name="getconnectorresources"></a>

 **Operation ID:** `GetConnectorResources`

Retrieves detailed information about connector resources.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `connectorId`  | path | String | Yes | Pattern: `^connector-[a-fA-F0-9]{32}$`  |
|  `resourceType`  | query | String | No | — |
|  `attributeName`  | query | String | No | — |
|  `params`  | query | String | No | Optional JSON-encoded parameters passed through to the connector for proxy resource requests (e.g., tileset/tile fetching). |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `resources`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Available Asset Templates
<a name="api-available-asset-templates"></a>

### GET `/iam/libraries/{libraryId}/available-asset-templates`
<a name="listavailableassettemplates"></a>

 **Operation ID:** `ListAvailableAssetTemplates`

Retrieves a paginated list of available asset templates. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `permittedConnectorIds`  | query | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `templates`  | Array of [AssetTemplateMinimal](#schema-assettemplateminimal)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Available Connectors
<a name="api-available-connectors"></a>

### GET `/iam/libraries/{libraryId}/available-connectors`
<a name="listavailableconnectors"></a>

 **Operation ID:** `ListAvailableConnectors`

Retrieves a paginated list of available connectors. Results are sorted by creation date in descending order.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |
|  `direction`  | query |  [ConnectorDirection](#schema-connectordirection)  | No | — |
|  `providingResourceType`  | query | String | No | — |
|  `enabled`  | query | Boolean | No | — |
|  `default`  | query | Boolean | No | — |
|  `supportsExistingResource`  | query | Boolean | No | — |
|  `principalId`  | query | String | No | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `connectors`  | Array of [ConnectorMinimal](#schema-connectorminimal)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Members
<a name="api-members"></a>

### GET `/iam/libraries/{libraryId}/members`
<a name="listlibrarymembers"></a>

 **Operation ID:** `ListLibraryMembers`

Retrieves a paginated list of all members with access to the library. Includes member details such as principal ID, type, and membership level.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | — |
|  `nextToken`  | String | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### GET `/iam/libraries/{libraryId}/members/{principalId}`
<a name="getlibrarymember"></a>

 **Operation ID:** `GetLibraryMember`

Retrieves detailed information about a specific library member. Returns the member’s access level and metadata.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Principal identifier (user or group ID) Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |
|  `principalType`  | query |  [PrincipalType](#schema-principaltype)  | No | Type of principal (USER or GROUP) |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### POST `/iam/libraries/{libraryId}/members/{principalId}`
<a name="addlibrarymember"></a>

 **Operation ID:** `AddLibraryMember`

Adds a new member to a library with specified access level. Members can be users or groups with roles: OWNER, MANAGER, CONTRIBUTOR, or VIEWER. Only library OWNERS and MANAGERS can add new members.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |
|  `errorCode`  | String | — |
|  `context`  | Object | — |

### PUT `/iam/libraries/{libraryId}/members/{principalId}`
<a name="updatelibrarymember"></a>

 **Operation ID:** `UpdateLibraryMember`

Updates the membership level of an existing library member. Can change roles between OWNER, MANAGER, CONTRIBUTOR, and VIEWER.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Principal identifier to update Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `createdAt`  | Number | — |
|  `updatedAt`  | Number | — |
|  `createdBy`  | String | — |
|  `updatedBy`  | String | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | — |
|  `principalId`  | String | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

### DELETE `/iam/libraries/{libraryId}/members/{principalId}`
<a name="deletelibrarymember"></a>

 **Operation ID:** `DeleteLibraryMember`

Removes a member’s access to the library. The member will no longer be able to access any resources within this library.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `principalId`  | path | String | Yes | Principal identifier to remove Pattern: `^(arn:aws:[a-zA-Z0-9-]+:[a-zA-Z0-9-]:[0-9]:[a-zA-Z0-9-/:.]+\|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\|system\|[a-zA-Z0-9+=,.@-]+)$`  |

 **Responses**

 `200`
Success

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Permissions
<a name="api-permissions"></a>

### GET `/iam/libraries/{libraryId}/permissions`
<a name="getlibrarypermissions"></a>

 **Operation ID:** `GetLibraryPermissions`

Retrieves the permission structure for a library. Shows what actions the current user can perform on this library resource.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `permissions`  | Array of String | Permission structure showing allowed actions |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Search Assets
<a name="api-search-assets"></a>

### POST `/iam/libraries/{libraryId}/search-assets`
<a name="searchassets"></a>

 **Operation ID:** `SearchAssets`

Searches for assets using flexible query criteria. Supports filtering and pagination.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `searchPattern`  | String | No | — |
|  `searchFilters`  | Array of [PropertyFilter](#schema-propertyfilter)  | No | — |
|  `size`  | Number | No | — |
|  `from`  | Number | No | — |
|  `sort`  | String | No | — |
|  `sortDescending`  | Boolean | No | — |
|  `logicalOperator`  | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `assets`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Search Files
<a name="api-search-files"></a>

### POST `/iam/libraries/{libraryId}/search-files`
<a name="searchfiles"></a>

 **Operation ID:** `SearchFiles`

Searches for files using flexible query criteria. Supports filtering and pagination.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `searchPattern`  | String | No | — |
|  `searchFilters`  | Array of [PropertyFilter](#schema-propertyfilter)  | No | — |
|  `size`  | Number | No | — |
|  `from`  | Number | No | — |
|  `sort`  | String | No | — |
|  `sortDescending`  | Boolean | No | — |
|  `logicalOperator`  | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `files`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Audit Event Queries
<a name="api-audit-event-queries"></a>

### POST `/iam/libraries/{libraryId}/audit-event-queries`
<a name="queryauditevents"></a>

 **Operation ID:** `QueryAuditEvents`

Queries audit events with specified filters and time ranges.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |
|  `maxResults`  | query | Number | No | Maximum number of results to return per page |
|  `nextToken`  | query | String | No | Pagination token from a previous response |

 **Request Body**

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `filters`  | Array of [AuditFilter](#schema-auditfilter)  | No | — |
|  `operation`  | String | No | — |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `nextToken`  | String | — |
|  `columns`  | Array of String | — |
|  `rows`  | Array of Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Known Attributes
<a name="api-known-attributes"></a>

### GET `/iam/libraries/{libraryId}/known-attributes`
<a name="getallprojectknownattributes"></a>

 **Operation ID:** `GetAllProjectKnownAttributes`

Retrieves all known attributes across projects in a library.

 **Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
|  `libraryId`  | path | String | Yes | Pattern: `^library-[a-fA-F0-9]{32}$`  |

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `attributes`  | Object | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Personas
<a name="api-personas"></a>

### GET `/iam/personas`
<a name="getpersonas"></a>

 **Operation ID:** `GetPersonas`

Retrieves the list of available personas.

 **Responses**

 `200`
Success

| Property | Type | Description |
| --- | --- | --- |
|  `personas`  | Array of [Persona](#schema-persona)  | — |

 `400`
Bad request. The request was invalid or cannot be served.

| Property | Type | Description |
| --- | --- | --- |
|  `message`  | String | — |

## Enumerations
<a name="api-enumerations"></a>

The API uses the following enumeration types:

### AccessRequestOperation
<a name="schema-accessrequestoperation"></a>

Type: `string`

Allowed values:
+  `read`
+  `write`

### AnalysisState
<a name="schema-analysisstate"></a>

Type: `string`

Allowed values:
+  `SUCCEEDED`
+  `FAILED`
+  `PENDING`
+  `IN_PROGRESS`

### AssetAccessLocation
<a name="schema-assetaccesslocation"></a>

Type: `string`

Allowed values:
+  `manifest`
+  `data`
+  `manifest_and_data`

### AssetState
<a name="schema-assetstate"></a>

Type: `string`

Allowed values:
+  `DRAFT`
+  `REVIEWED`
+  `READY`
+  `PENDING_DELETE`
+  `PENDING_CREATE`
+  `UPLOADING`

### AssociationStatus
<a name="schema-associationstatus"></a>

Type: `string`

Allowed values:
+  `PENDING`
+  `APPROVED`
+  `DENIED`
+  `REVOKED`

### AssociationType
<a name="schema-associationtype"></a>

Type: `string`

Allowed values:
+  `PROJECT_TEMPLATE`
+  `TEMPLATE_CONNECTOR`

### ConnectorDirection
<a name="schema-connectordirection"></a>

Type: `string`

Allowed values:
+  `derive`
+  `publish`
+  `bidirectional`
+  `exchange`

### ConnectorType
<a name="schema-connectortype"></a>

Type: `string`

Allowed values:
+  `opensearch`
+  `stac`
+  `synchronization`
+  `lambda`
+  `eventbridge`
+  `DeadlineCloud`
+  `rest`
+  `RESTApi`
+  `S3Csv`
+  `S3`
+  `s3`
+  `deadlineCloud`
+  `deadlineJob`
+  `dynamodb`
+  `DDB`

### CredentialVendingRequestType
<a name="schema-credentialvendingrequesttype"></a>

Type: `string`

Allowed values:
+  `user`

### FileState
<a name="schema-filestate"></a>

Type: `string`

Allowed values:
+  `READY`
+  `PENDING`
+  `PROCESSING`
+  `ERROR`
+  `UPLOADING`

### FilterOperator
<a name="schema-filteroperator"></a>

Type: `string`

Allowed values:
+  `eq`
+  `ne`
+  `lt`
+  `lte`
+  `gt`
+  `gte`
+  `like`
+  `not_contains`
+  `starts_with`
+  `not_starts_with`
+  `geo`

### MembershipLevel
<a name="schema-membershiplevel"></a>

Type: `string`

Allowed values:
+  `VIEWER`
+  `CONTRIBUTOR`
+  `MANAGER`
+  `OWNER`

### PrincipalType
<a name="schema-principaltype"></a>

Type: `string`

Allowed values:
+  `USER`
+  `GROUP`

### ProjectAccessLocation
<a name="schema-projectaccesslocation"></a>

Type: `string`

Allowed values:
+  `data`

### ProjectAccessOperation
<a name="schema-projectaccessoperation"></a>

Type: `string`

Allowed values:
+  `write`

### ResourceId
<a name="schema-resourceid"></a>

Type: `string`

### ResourceStatus
<a name="schema-resourcestatus"></a>

Type: `string`

Allowed values:
+  `READY`
+  `UPLOADING`
+  `ANALYZING`
+  `DELETED`
+  `PENDING_CREATE`
+  `CREATE_FAILED`
+  `UPDATE_FAILED`
+  `UPLOAD_FAILED`

### UploadState
<a name="schema-uploadstate"></a>

Type: `string`

Allowed values:
+  `UPLOAD_INITIATED`
+  `UPLOADING`
+  `PAUSED`
+  `CANCELED`
+  `CANCELING`
+  `COMPLETE`

### UserUpdatableAssetState
<a name="schema-userupdatableassetstate"></a>

Type: `string`

Allowed values:
+  `DRAFT`
+  `READY`
+  `DELETED`
+  `REVIEWED`

## Data types
<a name="api-data-types"></a>

The API uses the following complex data types:

### AddAssetTemplateMemberRequestContent
<a name="schema-addassettemplatememberrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

### AddAssetTemplateMemberResponseContent
<a name="schema-addassettemplatememberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### AddConnectorMemberRequestContent
<a name="schema-addconnectormemberrequestcontent"></a>

Context information for connector operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

### AddConnectorMemberResponseContent
<a name="schema-addconnectormemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### AddLibraryMemberRequestContent
<a name="schema-addlibrarymemberrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

### AddLibraryMemberResponseContent
<a name="schema-addlibrarymemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### AddProjectMemberRequestContent
<a name="schema-addprojectmemberrequestcontent"></a>

Context information for project operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |

### AddProjectMemberResponseContent
<a name="schema-addprojectmemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### Asset
<a name="schema-asset"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `assetName`  | String | Yes | — |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetState`  |  [AssetState](#schema-assetstate)  | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `thumbnailUrl`  | String | No | — |
|  `thumbnailFileId`  | String | No | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `statusCode`  |  [ResourceStatus](#schema-resourcestatus)  | No | — |
|  `statusMessage`  | String | No | — |

### AssetReference
<a name="schema-assetreference"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `libraryId`  | String | Yes | Unique identifier for the library |

### AssetTemplateAssociationDetail
<a name="schema-assettemplateassociationdetail"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `associationType`  |  [AssociationType](#schema-associationtype)  | Yes | — |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |
|  `requestedBy`  | String | Yes | — |
|  `requestedAt`  | Number | Yes | — |
|  `reviewedBy`  | String | No | — |
|  `reviewedAt`  | Number | No | — |
|  `sourceResourceId`  | String | Yes | — |
|  `targetResourceId`  | String | Yes | — |
|  `assetTemplateId`  | String | No | — |
|  `assetTemplateName`  | String | No | — |
|  `assetTemplateCreatedAt`  | Number | No | — |

### AssetTemplateMinimal
<a name="schema-assettemplateminimal"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetTemplateId`  | String | Yes | — |
|  `assetTemplateName`  | String | Yes | — |
|  `permittedConnectorIds`  | Array of String | No | — |
|  `allowedFileTypes`  | Array of String | No | — |
|  `allowAdditionalFileTypes`  | Boolean | No | — |

### AssetVersion
<a name="schema-assetversion"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `versionId`  | String | Yes | Unique identifier for the asset version |
|  `createdAt`  | Number | Yes | — |
|  `createdBy`  | String | No | — |
|  `hash`  | String | No | — |
|  `eventCorrelationId`  | String | No | — |

### Attribute
<a name="schema-attribute"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `name`  | String | Yes | — |
|  `value`  | Object | Yes | — |
|  `source`  | String | No | — |
|  `type`  | String | No | — |

### AttributeSuggestion
<a name="schema-attributesuggestion"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `attribute`  | String | Yes | — |
|  `presence`  | Number | Yes | — |
|  `example`  | String | Yes | — |

### AuditFilter
<a name="schema-auditfilter"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `field`  | String | Yes | — |
|  `operator`  | String | Yes | — |
|  `value`  | String | Yes | — |

### ConflictExceptionResponseContent
<a name="schema-conflictexceptionresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `message`  | String | Yes | — |
|  `errorCode`  | String | No | — |
|  `context`  | Object | No | — |

### ConnectorInvocationDetail
<a name="schema-connectorinvocationdetail"></a>

A single connector invocation record returned in GetFile / GetFileVersion responses.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `connectorInvocationId`  | String | Yes | — |
|  `connectorId`  | String | Yes | Unique identifier for the connector |
|  `resourceId`  | String | Yes | — |
|  `status`  | String | Yes | — |
|  `createdAt`  | Number | No | — |
|  `lastStatusChangeAt`  | Number | No | — |
|  `eventCorrelationId`  | String | No | — |
|  `eventTriggeredBy`  | String | No | — |
|  `eventType`  | String | No | — |
|  `triggerResourceType`  | String | No | — |
|  `dependsOn`  | Array of String | No | — |
|  `waitingOn`  | Array of String | No | — |
|  `blockedBy`  | Array of String | No | — |

### ConnectorInvocationSummary
<a name="schema-connectorinvocationsummary"></a>

Summary of connector invocation states for a resource. Cached on the resource record for efficient list-view rendering. Extensible: future releases may add byDirection or byConnectorId breakdowns.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `total`  | Number | Yes | — |
|  `succeeded`  | Number | Yes | — |
|  `failed`  | Number | Yes | — |
|  `inProgress`  | Number | Yes | — |
|  `queued`  | Number | Yes | — |
|  `waiting`  | Number | Yes | — |
|  `blocked`  | Number | Yes | — |
|  `notApplicable`  | Number | Yes | — |

### ConnectorMinimal
<a name="schema-connectorminimal"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `connectorId`  | String | Yes | Unique identifier for the connector |
|  `connectorName`  | String | Yes | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | Yes | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | Yes | — |
|  `enabled`  | Boolean | Yes | — |
|  `connectorConfig`  | Object | No | — |

### CreateAssetRequestContent
<a name="schema-createassetrequestcontent"></a>

Context information for project operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetName`  | String | Yes | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `manifestHash`  | String | No | — |
|  `manifestObjectKey`  | String | No | — |
|  `sourceAsset`  |  [AssetReference](#schema-assetreference)  | No | — |
|  `mergeAssets`  | Array of [AssetReference](#schema-assetreference)  | No | — |

### CreateAssetResponseContent
<a name="schema-createassetresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `assetName`  | String | Yes | — |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetState`  |  [AssetState](#schema-assetstate)  | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `thumbnailUrl`  | String | No | — |
|  `thumbnailFileId`  | String | No | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `manifestHash`  | String | No | — |
|  `statusCode`  |  [ResourceStatus](#schema-resourcestatus)  | No | — |
|  `statusMessage`  | String | No | — |

### CreateAssetTemplateRequestContent
<a name="schema-createassettemplaterequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetTemplateConfig`  | Object | Yes | — |

### CreateAssetTemplateResponseContent
<a name="schema-createassettemplateresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetTemplateId`  | String | Yes | — |
|  `assetTemplateName`  | String | Yes | — |
|  `assetTemplateConfig`  | Object | Yes | — |

### CreateConnectorRequestContent
<a name="schema-createconnectorrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `connectorConfig`  | Object | Yes | — |

### CreateConnectorResponseContent
<a name="schema-createconnectorresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `connectorId`  | String | Yes | Unique identifier for the connector |
|  `connectorName`  | String | Yes | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | Yes | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | Yes | — |
|  `enabled`  | Boolean | Yes | — |
|  `default`  | Boolean | Yes | — |
|  `connectorConfig`  | Object | Yes | — |
|  `recentInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | No | — |

### CreateProjectRequestContent
<a name="schema-createprojectrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `projectName`  | String | Yes | — |
|  `projectConfig`  |  [ProjectConfig](#schema-projectconfig)  | No | — |
|  `projectThumbnailObjectKey`  | String | No | — |

### CreateProjectResponseContent
<a name="schema-createprojectresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `projectName`  | String | Yes | — |
|  `assetCount`  | Number | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `s3BucketName`  | String | Yes | — |
|  `rootPrefix`  | String | Yes | — |
|  `manifestPrefix`  | String | Yes | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `thumbnailUrl`  | String | No | — |
|  `permittedTemplateIds`  | Array of String | No | — |
|  `allowNonTemplatedAssets`  | Boolean | Yes | — |
|  `description`  | String | No | — |
|  `metadataAttributes`  | Array of [MetadataAttribute](#schema-metadataattribute)  | No | — |

### DeleteAssetResponseContent
<a name="schema-deleteassetresponsecontent"></a>

Response data for DeleteAsset operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetState`  |  [AssetState](#schema-assetstate)  | Yes | — |
|  `message`  | String | No | — |

### File
<a name="schema-file"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `fileId`  | String | Yes | Unique identifier for the file |
|  `pathId`  | String | Yes | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `path`  | String | Yes | — |
|  `mtime`  | Number | Yes | — |
|  `addedAt`  | Number | No | — |
|  `size`  | Number | Yes | — |
|  `objectKey`  | String | Yes | — |
|  `hash`  | String | Yes | — |
|  `state`  |  [FileState](#schema-filestate)  | Yes | — |
|  `analysisState`  |  [AnalysisState](#schema-analysisstate)  | No | — |
|  `connectorInvocationSummary`  |  [ConnectorInvocationSummary](#schema-connectorinvocationsummary)  | No | — |
|  `hasAttributeSuggestions`  | Boolean | Yes | — |
|  `versionId`  | String | No | Unique identifier for the asset version |
|  `suggestedMetadataAttributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `metadataAttributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `location`  |  [Location](#schema-location)  | No | — |
|  `url`  | String | No | — |
|  `previews`  | Array of [FilePreview](#schema-filepreview)  | No | — |
|  `connectorInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | No | — |

### FilePreview
<a name="schema-filepreview"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `previewUrl`  | String | Yes | — |
|  `previewType`  | String | Yes | — |
|  `fileId`  | String | No | Unique identifier for the file |

### FileTypeSuggestion
<a name="schema-filetypesuggestion"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `fileType`  | String | Yes | — |
|  `count`  | Number | Yes | — |
|  `suggestions`  | Array of [AttributeSuggestion](#schema-attributesuggestion)  | Yes | — |

### ForbiddenExceptionResponseContent
<a name="schema-forbiddenexceptionresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `message`  | String | Yes | — |

### GetAllProjectKnownAttributesResponseContent
<a name="schema-getallprojectknownattributesresponsecontent"></a>

Response data for GetAllProjectKnownAttributes operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `attributes`  | Object | Yes | — |

### GetAssetCredentialsResponseContent
<a name="schema-getassetcredentialsresponsecontent"></a>

Response data for GetAssetCredentials operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `credentials`  | Object | Yes | — |

### GetAssetResponseContent
<a name="schema-getassetresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `assetName`  | String | Yes | — |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetState`  |  [AssetState](#schema-assetstate)  | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `thumbnailUrl`  | String | No | — |
|  `thumbnailFileId`  | String | No | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `manifestHash`  | String | No | — |
|  `statusCode`  |  [ResourceStatus](#schema-resourcestatus)  | No | — |
|  `statusMessage`  | String | No | — |

### GetAssetTemplateMemberResponseContent
<a name="schema-getassettemplatememberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### GetAssetTemplatePermissionsResponseContent
<a name="schema-getassettemplatepermissionsresponsecontent"></a>

Response data for GetAssetTemplatePermissions operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `permissions`  | Array of String | Yes | — |

### GetAssetTemplateResponseContent
<a name="schema-getassettemplateresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetTemplateId`  | String | Yes | — |
|  `assetTemplateName`  | String | Yes | — |
|  `assetTemplateConfig`  | Object | Yes | — |

### GetConnectorMemberResponseContent
<a name="schema-getconnectormemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### GetConnectorPermissionsResponseContent
<a name="schema-getconnectorpermissionsresponsecontent"></a>

Response data for GetConnectorPermissions operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `permissions`  | Array of String | Yes | — |

### GetConnectorResourcesResponseContent
<a name="schema-getconnectorresourcesresponsecontent"></a>

Response data for GetConnectorResources operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `resources`  | Object | Yes | — |

### GetConnectorResourcesViaAssetResponseContent
<a name="schema-getconnectorresourcesviaassetresponsecontent"></a>

Response data for GetConnectorResourcesViaAsset operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `resources`  | Object | Yes | — |

### GetConnectorResourcesViaAssetTemplateProjectResponseContent
<a name="schema-getconnectorresourcesviaassettemplateprojectresponsecontent"></a>

Response data for GetConnectorResourcesViaAssetTemplateProject operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `resources`  | Object | Yes | — |

### GetConnectorResourcesViaAssetTemplateResponseContent
<a name="schema-getconnectorresourcesviaassettemplateresponsecontent"></a>

Response data for GetConnectorResourcesViaAssetTemplate operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `resources`  | Object | Yes | — |

### GetConnectorResponseContent
<a name="schema-getconnectorresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `connectorId`  | String | Yes | Unique identifier for the connector |
|  `connectorName`  | String | Yes | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | Yes | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | Yes | — |
|  `enabled`  | Boolean | Yes | — |
|  `default`  | Boolean | Yes | — |
|  `connectorConfig`  | Object | Yes | — |
|  `recentInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | No | — |

### GetFileResponseContent
<a name="schema-getfileresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `fileId`  | String | Yes | Unique identifier for the file |
|  `pathId`  | String | Yes | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `path`  | String | Yes | — |
|  `mtime`  | Number | Yes | — |
|  `addedAt`  | Number | No | — |
|  `size`  | Number | Yes | — |
|  `objectKey`  | String | Yes | — |
|  `hash`  | String | Yes | — |
|  `state`  |  [FileState](#schema-filestate)  | Yes | — |
|  `analysisState`  |  [AnalysisState](#schema-analysisstate)  | No | — |
|  `connectorInvocationSummary`  |  [ConnectorInvocationSummary](#schema-connectorinvocationsummary)  | No | — |
|  `hasAttributeSuggestions`  | Boolean | Yes | — |
|  `versionId`  | String | No | Unique identifier for the asset version |
|  `suggestedMetadataAttributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `metadataAttributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `location`  |  [Location](#schema-location)  | No | — |
|  `url`  | String | No | — |
|  `previews`  | Array of [FilePreview](#schema-filepreview)  | No | — |
|  `connectorInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | No | — |

### GetFileVersionResponseContent
<a name="schema-getfileversionresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `fileId`  | String | Yes | Unique identifier for the file |
|  `pathId`  | String | Yes | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `path`  | String | Yes | — |
|  `mtime`  | Number | Yes | — |
|  `addedAt`  | Number | No | — |
|  `size`  | Number | Yes | — |
|  `objectKey`  | String | Yes | — |
|  `hash`  | String | Yes | — |
|  `state`  |  [FileState](#schema-filestate)  | Yes | — |
|  `analysisState`  |  [AnalysisState](#schema-analysisstate)  | No | — |
|  `connectorInvocationSummary`  |  [ConnectorInvocationSummary](#schema-connectorinvocationsummary)  | No | — |
|  `hasAttributeSuggestions`  | Boolean | Yes | — |
|  `versionId`  | String | No | Unique identifier for the asset version |
|  `suggestedMetadataAttributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `metadataAttributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `location`  |  [Location](#schema-location)  | No | — |
|  `url`  | String | No | — |
|  `previews`  | Array of [FilePreview](#schema-filepreview)  | No | — |
|  `connectorInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | No | — |

### GetLibraryMemberResponseContent
<a name="schema-getlibrarymemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### GetLibraryPermissionsResponseContent
<a name="schema-getlibrarypermissionsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `permissions`  | Array of String | Yes | Permission structure showing allowed actions |

### GetLibraryResponseContent
<a name="schema-getlibraryresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `libraryName`  | String | Yes | — |
|  `storageConfig`  |  [StorageConfig](#schema-storageconfig)  | Yes | — |
|  `solutionVersion`  | String | No | — |

### GetPersonasResponseContent
<a name="schema-getpersonasresponsecontent"></a>

Response data for GetPersonas operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `personas`  | Array of [Persona](#schema-persona)  | Yes | — |

### GetProjectCredentialsResponseContent
<a name="schema-getprojectcredentialsresponsecontent"></a>

Response data for GetProjectCredentials operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `credentials`  | Object | Yes | — |

### GetProjectKnownAttributesResponseContent
<a name="schema-getprojectknownattributesresponsecontent"></a>

Response data for GetProjectKnownAttributes operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `attributes`  | Object | Yes | — |

### GetProjectMemberResponseContent
<a name="schema-getprojectmemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### GetProjectPermissionsResponseContent
<a name="schema-getprojectpermissionsresponsecontent"></a>

Response data for GetProjectPermissions operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `permissions`  | Array of String | Yes | — |

### GetProjectResponseContent
<a name="schema-getprojectresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `projectName`  | String | Yes | — |
|  `assetCount`  | Number | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `s3BucketName`  | String | Yes | — |
|  `rootPrefix`  | String | Yes | — |
|  `manifestPrefix`  | String | Yes | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `thumbnailUrl`  | String | No | — |
|  `permittedTemplateIds`  | Array of String | No | — |
|  `allowNonTemplatedAssets`  | Boolean | Yes | — |
|  `description`  | String | No | — |
|  `metadataAttributes`  | Array of [MetadataAttribute](#schema-metadataattribute)  | No | — |

### InvalidParameterValueExceptionResponseContent
<a name="schema-invalidparametervalueexceptionresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `message`  | String | Yes | — |
|  `parameterName`  | String | No | — |
|  `parameterValue`  | String | No | — |
|  `allowedValues`  | Array of String | No | — |

### Library
<a name="schema-library"></a>

Represents a library resource that serves as an organizational container for projects, assets, and templates. Libraries define storage configuration and access controls.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `libraryName`  | String | Yes | Human-readable name of the library |
|  `storageConfig`  |  [StorageConfig](#schema-storageconfig)  | Yes | — |

### ListAssetAttributesResponseContent
<a name="schema-listassetattributesresponsecontent"></a>

Response data for ListAssetAttributes operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | Yes | — |

### ListAssetSuggestedAttributesResponseContent
<a name="schema-listassetsuggestedattributesresponsecontent"></a>

Response data for ListAssetSuggestedAttributes operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `suggestions`  | Array of [FileTypeSuggestion](#schema-filetypesuggestion)  | Yes | — |

### ListAssetTemplateAssetsResponseContent
<a name="schema-listassettemplateassetsresponsecontent"></a>

Response data for ListAssetTemplateAssets operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assets`  | Object | Yes | — |
|  `hiddenAssetsCount`  | Number | No | — |
|  `totalAssetsCount`  | Number | No | — |

### ListAssetTemplateMembersResponseContent
<a name="schema-listassettemplatemembersresponsecontent"></a>

Response data for ListMembers operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | Yes | — |
|  `nextToken`  | String | No | Pagination token from a previous response |

### ListAssetTemplateProjectAssociationsResponseContent
<a name="schema-listassettemplateprojectassociationsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `associations`  | Array of [ProjectAssociationDetail](#schema-projectassociationdetail)  | Yes | — |

### ListAssetTemplatesResponseContent
<a name="schema-listassettemplatesresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `templates`  | Array of [AssetTemplateMinimal](#schema-assettemplateminimal)  | Yes | — |

### ListAssetVersionsResponseContent
<a name="schema-listassetversionsresponsecontent"></a>

Response data for ListAssetVersions operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `versions`  | Array of [AssetVersion](#schema-assetversion)  | Yes | — |

### ListAssetsResponseContent
<a name="schema-listassetsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `assets`  | Array of [Asset](#schema-asset)  | Yes | — |

### ListAvailableAssetTemplatesResponseContent
<a name="schema-listavailableassettemplatesresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `templates`  | Array of [AssetTemplateMinimal](#schema-assettemplateminimal)  | Yes | — |

### ListAvailableConnectorsResponseContent
<a name="schema-listavailableconnectorsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `connectors`  | Array of [ConnectorMinimal](#schema-connectorminimal)  | Yes | — |

### ListConnectorAssetTemplateAssociationsResponseContent
<a name="schema-listconnectorassettemplateassociationsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `associations`  | Array of [AssetTemplateAssociationDetail](#schema-assettemplateassociationdetail)  | Yes | — |

### ListConnectorMembersResponseContent
<a name="schema-listconnectormembersresponsecontent"></a>

Response data for ListMembers operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | Yes | — |
|  `nextToken`  | String | No | Pagination token from a previous response |

### ListConnectorsResponseContent
<a name="schema-listconnectorsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `connectors`  | Array of [ConnectorMinimal](#schema-connectorminimal)  | Yes | — |

### ListFileVersionsResponseContent
<a name="schema-listfileversionsresponsecontent"></a>

Response data for ListFileVersions operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `versions`  | Object | Yes | — |

### ListFilesForAssetVersionResponseContent
<a name="schema-listfilesforassetversionresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `files`  | Array of [File](#schema-file)  | Yes | — |

### ListFilesResponseContent
<a name="schema-listfilesresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `files`  | Array of [File](#schema-file)  | Yes | — |

### ListLibrariesResponseContent
<a name="schema-listlibrariesresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `libraries`  | Array of [Library](#schema-library)  | Yes | List of libraries accessible to the user |

### ListLibraryAssetsResponseContent
<a name="schema-listlibraryassetsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `assets`  | Array of [Asset](#schema-asset)  | Yes | — |

### ListLibraryMembersResponseContent
<a name="schema-listlibrarymembersresponsecontent"></a>

Response data for ListMembers operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | Yes | — |
|  `nextToken`  | String | No | Pagination token from a previous response |

### ListProjectMembersResponseContent
<a name="schema-listprojectmembersresponsecontent"></a>

Response data for ListMembers operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `members`  | Array of [Member](#schema-member)  | Yes | — |
|  `nextToken`  | String | No | Pagination token from a previous response |

### ListProjectsResponseContent
<a name="schema-listprojectsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `projects`  | Array of [Project](#schema-project)  | Yes | — |

### Location
<a name="schema-location"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `latitude`  | Number | No | — |
|  `longitude`  | Number | No | — |
|  `place`  | String | No | — |
|  `geoJson`  | String | No | — |
|  `aabb`  | String | No | — |

### Member
<a name="schema-member"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### MetadataAttribute
<a name="schema-metadataattribute"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `attribute`  | String | Yes | — |
|  `value`  | String | Yes | — |

### Persona
<a name="schema-persona"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `resourceType`  | String | Yes | — |
|  `persona`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |
|  `resourcePermissions`  | Array of [ResourcePermissions](#schema-resourcepermissions)  | Yes | — |

### Project
<a name="schema-project"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `projectName`  | String | Yes | — |
|  `assetCount`  | Number | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `s3BucketName`  | String | Yes | — |
|  `rootPrefix`  | String | Yes | — |
|  `manifestPrefix`  | String | Yes | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `thumbnailUrl`  | String | No | — |
|  `permittedTemplateIds`  | Array of String | No | — |
|  `allowNonTemplatedAssets`  | Boolean | Yes | — |
|  `description`  | String | No | — |
|  `metadataAttributes`  | Array of [MetadataAttribute](#schema-metadataattribute)  | No | — |

### ProjectAssociationDetail
<a name="schema-projectassociationdetail"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `associationType`  |  [AssociationType](#schema-associationtype)  | Yes | — |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |
|  `requestedBy`  | String | Yes | — |
|  `requestedAt`  | Number | Yes | — |
|  `reviewedBy`  | String | No | — |
|  `reviewedAt`  | Number | No | — |
|  `sourceResourceId`  | String | Yes | — |
|  `targetResourceId`  | String | Yes | — |
|  `projectId`  | String | No | Unique identifier for the project |
|  `projectName`  | String | No | — |
|  `projectDescription`  | String | No | — |
|  `projectAssetCount`  | Number | No | — |
|  `projectCreatedAt`  | Number | No | — |

### ProjectConfig
<a name="schema-projectconfig"></a>

Configuration settings for project.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `name`  | String | No | — |
|  `permittedTemplateIds`  | Array of String | No | — |
|  `description`  | String | No | — |
|  `thumbnailHash`  | String | No | — |
|  `allowNonTemplatedAssets`  | Boolean | No | — |
|  `s3BucketName`  | String | No | — |
|  `rootPrefix`  | String | No | — |
|  `latitude`  | Number | No | — |
|  `longitude`  | Number | No | — |
|  `place`  | String | No | — |
|  `metadata`  | Object | No | — |

### PropertyFilter
<a name="schema-propertyfilter"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `key`  | String | Yes | — |
|  `operator`  |  [FilterOperator](#schema-filteroperator)  | Yes | — |
|  `stringValue`  | String | No | — |
|  `numberValue`  | Number | No | — |

### QueryAuditEventsRequestContent
<a name="schema-queryauditeventsrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `filters`  | Array of [AuditFilter](#schema-auditfilter)  | No | — |
|  `operation`  | String | No | — |

### QueryAuditEventsResponseContent
<a name="schema-queryauditeventsresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `nextToken`  | String | No | Pagination token from a previous response |
|  `columns`  | Array of String | No | — |
|  `rows`  | Array of Object | No | — |

### ResourcePermissions
<a name="schema-resourcepermissions"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `resourceType`  | String | Yes | — |
|  `permissions`  | Array of String | Yes | — |

### SearchAssetsRequestContent
<a name="schema-searchassetsrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `searchPattern`  | String | No | — |
|  `searchFilters`  | Array of [PropertyFilter](#schema-propertyfilter)  | No | — |
|  `size`  | Number | No | — |
|  `from`  | Number | No | — |
|  `sort`  | String | No | — |
|  `sortDescending`  | Boolean | No | — |
|  `logicalOperator`  | String | No | — |

### SearchAssetsResponseContent
<a name="schema-searchassetsresponsecontent"></a>

Response data for SearchAssets operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assets`  | Object | Yes | — |

### SearchFilesRequestContent
<a name="schema-searchfilesrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `searchPattern`  | String | No | — |
|  `searchFilters`  | Array of [PropertyFilter](#schema-propertyfilter)  | No | — |
|  `size`  | Number | No | — |
|  `from`  | Number | No | — |
|  `sort`  | String | No | — |
|  `sortDescending`  | Boolean | No | — |
|  `logicalOperator`  | String | No | — |

### SearchFilesResponseContent
<a name="schema-searchfilesresponsecontent"></a>

Response data for SearchFiles operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `files`  | Object | Yes | — |

### StorageConfig
<a name="schema-storageconfig"></a>

S3 storage configuration defining where library data is stored

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `defaultS3BucketName`  | String | Yes | Default S3 bucket name for library storage |
|  `defaultRootS3Prefix`  | String | Yes | Default root S3 prefix for organizing library data |

### TriggerConnectorOnAssetDirectResponseContent
<a name="schema-triggerconnectoronassetdirectresponsecontent"></a>

Response data for TriggerConnectorOnAssetDirect operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `result`  | String | Yes | — |

### TriggerConnectorOnAssetResponseContent
<a name="schema-triggerconnectoronassetresponsecontent"></a>

Response data for TriggerConnectorOnAsset operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `result`  | String | Yes | — |

### TriggerConnectorOnProjectDirectResponseContent
<a name="schema-triggerconnectoronprojectdirectresponsecontent"></a>

Response data for TriggerConnectorOnProjectDirect operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `result`  | String | Yes | — |

### UpdateAssetRequestContent
<a name="schema-updateassetrequestcontent"></a>

Context information for project operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `uploadState`  |  [UploadState](#schema-uploadstate)  | No | — |
|  `assetState`  |  [UserUpdatableAssetState](#schema-userupdatableassetstate)  | No | — |
|  `manifestHash`  | String | No | — |
|  `manifestObjectKey`  | String | No | — |
|  `activeVersionId`  | String | No | — |

### UpdateAssetResponseContent
<a name="schema-updateassetresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `assetId`  | String | Yes | Unique identifier for the asset |
|  `assetName`  | String | Yes | — |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetState`  |  [AssetState](#schema-assetstate)  | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `thumbnailUrl`  | String | No | — |
|  `thumbnailFileId`  | String | No | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `attributes`  | Array of [Attribute](#schema-attribute)  | No | — |
|  `manifestHash`  | String | No | — |
|  `statusCode`  |  [ResourceStatus](#schema-resourcestatus)  | No | — |
|  `statusMessage`  | String | No | — |

### UpdateAssetTemplateMemberRequestContent
<a name="schema-updateassettemplatememberrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateAssetTemplateMemberResponseContent
<a name="schema-updateassettemplatememberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateAssetTemplateProjectAssociationRequestContent
<a name="schema-updateassettemplateprojectassociationrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |

### UpdateAssetTemplateProjectAssociationResponseContent
<a name="schema-updateassettemplateprojectassociationresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `associationType`  |  [AssociationType](#schema-associationtype)  | Yes | — |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |
|  `requestedBy`  | String | Yes | — |
|  `requestedAt`  | Number | Yes | — |
|  `reviewedBy`  | String | No | — |
|  `reviewedAt`  | Number | No | — |
|  `sourceResourceId`  | String | Yes | — |
|  `targetResourceId`  | String | Yes | — |

### UpdateAssetTemplateRequestContent
<a name="schema-updateassettemplaterequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `assetTemplateConfig`  | Object | Yes | — |

### UpdateAssetTemplateResponseContent
<a name="schema-updateassettemplateresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `assetTemplateId`  | String | Yes | — |
|  `assetTemplateName`  | String | Yes | — |
|  `assetTemplateConfig`  | Object | Yes | — |

### UpdateConnectorAssetTemplateAssociationRequestContent
<a name="schema-updateconnectorassettemplateassociationrequestcontent"></a>

Context information for connector operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |

### UpdateConnectorAssetTemplateAssociationResponseContent
<a name="schema-updateconnectorassettemplateassociationresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `associationType`  |  [AssociationType](#schema-associationtype)  | Yes | — |
|  `status`  |  [AssociationStatus](#schema-associationstatus)  | Yes | — |
|  `requestedBy`  | String | Yes | — |
|  `requestedAt`  | Number | Yes | — |
|  `reviewedBy`  | String | No | — |
|  `reviewedAt`  | Number | No | — |
|  `sourceResourceId`  | String | Yes | — |
|  `targetResourceId`  | String | Yes | — |

### UpdateConnectorMemberRequestContent
<a name="schema-updateconnectormemberrequestcontent"></a>

Context information for connector operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateConnectorMemberResponseContent
<a name="schema-updateconnectormemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateConnectorRequestContent
<a name="schema-updateconnectorrequestcontent"></a>

Context information for connector operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `connectorName`  | String | Yes | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | Yes | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | Yes | — |
|  `enabled`  | Boolean | Yes | — |
|  `connectorConfig`  | Object | Yes | — |

### UpdateConnectorResponseContent
<a name="schema-updateconnectorresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `connectorId`  | String | Yes | Unique identifier for the connector |
|  `connectorName`  | String | Yes | — |
|  `connectorType`  |  [ConnectorType](#schema-connectortype)  | Yes | — |
|  `direction`  |  [ConnectorDirection](#schema-connectordirection)  | Yes | — |
|  `enabled`  | Boolean | Yes | — |
|  `default`  | Boolean | Yes | — |
|  `connectorConfig`  | Object | Yes | — |
|  `recentInvocations`  | Array of [ConnectorInvocationDetail](#schema-connectorinvocationdetail)  | No | — |

### UpdateLibraryMemberRequestContent
<a name="schema-updatelibrarymemberrequestcontent"></a>

Context information for library operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateLibraryMemberResponseContent
<a name="schema-updatelibrarymemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateProjectMemberRequestContent
<a name="schema-updateprojectmemberrequestcontent"></a>

Context information for project operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateProjectMemberResponseContent
<a name="schema-updateprojectmemberresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `resourceId`  |  [ResourceId](#schema-resourceid)  | Yes | — |
|  `principalId`  | String | Yes | Identifier of the IAM principal (user, role, or group) |
|  `principalType`  |  [PrincipalType](#schema-principaltype)  | Yes | — |
|  `membershipLevel`  |  [MembershipLevel](#schema-membershiplevel)  | Yes | — |

### UpdateProjectRequestContent
<a name="schema-updateprojectrequestcontent"></a>

Context information for project operations.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `projectName`  | String | No | — |
|  `projectConfig`  |  [ProjectConfig](#schema-projectconfig)  | No | — |
|  `projectThumbnailObjectKey`  | String | No | — |

### UpdateProjectResponseContent
<a name="schema-updateprojectresponsecontent"></a>

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `createdAt`  | Number | Yes | — |
|  `updatedAt`  | Number | No | — |
|  `createdBy`  | String | Yes | — |
|  `updatedBy`  | String | No | — |
|  `libraryId`  | String | Yes | Unique identifier for the library |
|  `projectId`  | String | Yes | Unique identifier for the project |
|  `projectName`  | String | Yes | — |
|  `assetCount`  | Number | Yes | — |
|  `fileCount`  | Number | Yes | — |
|  `totalSize`  | Number | Yes | — |
|  `s3BucketName`  | String | Yes | — |
|  `rootPrefix`  | String | Yes | — |
|  `manifestPrefix`  | String | Yes | — |
|  `thumbnailObjectKey`  | String | No | — |
|  `thumbnailUrl`  | String | No | — |
|  `permittedTemplateIds`  | Array of String | No | — |
|  `allowNonTemplatedAssets`  | Boolean | Yes | — |
|  `description`  | String | No | — |
|  `metadataAttributes`  | Array of [MetadataAttribute](#schema-metadataattribute)  | No | — |

### VerifyAssetConnectorRelationshipResponseContent
<a name="schema-verifyassetconnectorrelationshipresponsecontent"></a>

Response data for VerifyAssetConnectorRelationship operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `result`  | Boolean | Yes | — |

### VerifyProjectConnectorRelationshipResponseContent
<a name="schema-verifyprojectconnectorrelationshipresponsecontent"></a>

Response data for VerifyProjectConnectorRelationship operation.

| Property | Type | Required | Description |
| --- | --- | --- | --- |
|  `result`  | Boolean | Yes | — |

## Error Responses
<a name="api-error-responses"></a>

All API operations may return the following error responses:

 `400`
Bad request. The request was invalid or cannot be served.

 `403`
Forbidden. The authenticated user does not have permission.

 `409`
Conflict. The request conflicts with the current state of the resource.

 `500`
Internal server error.
