---
source_url: https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/assets.html
---

# Assets
<a name="assets"></a>

## URI
<a name="assets-url"></a>

`/assets`

## HTTP methods
<a name="assets-http-methods"></a>

### GET
<a name="assetsget"></a>

**Operation ID:** `ListAssets`

Lists assets that match a set of filters that you define.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| packagingGroupId | String | False | Limits the results to records that are associated with the given packaging group. |
| nextToken | String | False | Pagination token. Use this token to request the next page of record results. |
| maxResults | String | False | Upper bound on number of records to return. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | AssetList |  `200 OK` response<br />The list of tags is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### POST
<a name="assetspost"></a>

**Operation ID:** `CreateAsset`

Creates an asset to ingest VOD content.

Once created, the asset starts ingesting content and generates playback URLs for the packaging configurations associated with it. When ingest is complete, downstream devices request VOD content from AWS Elemental MediaPackage using the appropriate URL.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Asset |  `200 OK` response<br />The list of tags is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="assetsoptions"></a>

Enable cross-origin resource sharing (CORS) by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None |  `200 OK` response<br />The list of tags is returned successfully. |

## Schemas
<a name="assets-schemas"></a>

### Request bodies
<a name="assets-request-examples"></a>

#### POST schema
<a name="assets-request-body-post-example"></a>

```
{
  "packagingGroupId": "string",
  "sourceArn": "string",
  "resourceId": "string",
  "sourceRoleArn": "string",
  "id": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="assets-response-examples"></a>

#### AssetList schema
<a name="assets-response-body-assetlist-example"></a>

```
{
  "assets": [
    {
      "createdAt": "string",
      "packagingGroupId": "string",
      "sourceArn": "string",
      "resourceId": "string",
      "sourceRoleArn": "string",
      "id": "string",
      "arn": "string",
      "tags": {
      }
    }
  ],
  "nextToken": "string"
}
```

#### Asset schema
<a name="assets-response-body-asset-example"></a>

```
{
  "createdAt": "string",
  "packagingGroupId": "string",
  "sourceArn": "string",
  "resourceId": "string",
  "sourceRoleArn": "string",
  "id": "string",
  "arn": "string",
  "egressEndpoints": [
    {
      "packagingConfigurationId": "string",
      "url": "string",
      "status": "string"
    }
  ],
  "tags": {
  }
}
```

## Properties
<a name="assets-properties"></a>

### Asset
<a name="assets-model-asset"></a>

Parameters for an asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) for the asset. You can get this from the response to any request to the asset. |
| createdAt | string | False | The date and time the Asset was initially submitted for Ingest. |
| egressEndpoints | Array of type [EgressEndpoint](#assets-model-egressendpoint) | False | List of playback endpoints that are available for this asset. |
| id | string | False | Unique identifier that you assign to the asset. |
| packagingGroupId | string | False | The ID of the packaging group associated with this asset. |
| resourceId | string | False | Unique identifier for this asset, as it's configured in the key provider service. |
| sourceArn | string | False | The ARN for the source content in Amazon S3. |
| sourceRoleArn | string | False | The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored. Valid format: `arn:aws:iam::{accountID}:role/{name}`  |
| tags | [Tags](#assets-model-tags) | False | The tags to assign to the asset. |

### AssetCreateParameters
<a name="assets-model-assetcreateparameters"></a>

Parameters for creating an asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | True | Unique identifier that you assign to the asset. |
| packagingGroupId | string | True | The ID of the packaging group associated with this asset. |
| resourceId | string | False | Unique identifier for this asset, as it's configured in the key provider service. |
| sourceArn | string | True | The ARN for the source content in Amazon S3.  |
| sourceRoleArn | string | True | The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored. Valid format: `arn:aws:iam::{accountID}:role/{name}`  |
| tags | [Tags](#assets-model-tags) | False | The tags to assign to the asset. |

### AssetList
<a name="assets-model-assetlist"></a>

A collection of Asset records.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| assets | Array of type [AssetShallow](#assets-model-assetshallow) | False | A list of Asset records that are configured on this account in this AWS Region. |
| nextToken | string | False | Pagination token. Use this token to request the next page of assets results. |

### AssetShallow
<a name="assets-model-assetshallow"></a>

Parameters on an asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) for the asset. You can get this from the response to any request to the asset. |
| createdAt | string | False | The date and time the Asset was initially submitted for Ingest. |
| id | string | False | Unique identifier that you assigned to the asset. |
| packagingGroupId | string | False | The ID of the packaging group associated with this asset. |
| resourceId | string | False | Unique identifier for this endpoint, as it's configured in the key provider service. |
| sourceArn | string | False | The ARN for the source content in Amazon S3. |
| sourceRoleArn | string | False | The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored. Valid format: `arn:aws:iam::{accountID}:role/{name}`  |
| tags | [Tags](#assets-model-tags) | False | The tags to assign to the asset. |

### EgressEndpoint
<a name="assets-model-egressendpoint"></a>

The playback endpoint for a packaging configuration on an asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| packagingConfigurationId | string | False | The ID of a packaging configuration that's applied to this asset. |
| status | string | False | The current processing status of the asset used for the packaging configuration. The status can be `QUEUED`, `PROCESSING`, `PLAYABLE`, or `FAILED`. Status information isn't available for most assets ingested before September 30th, 2021. |
| url | string | False | The URL that's used to request content from this endpoint. |

### Tags
<a name="assets-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |
