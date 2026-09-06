---
source_url: https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/assets-id.html
---

# Assets id
<a name="assets-id"></a>

## URI
<a name="assets-id-url"></a>

`/assets/{{id}}`

## HTTP methods
<a name="assets-id-http-methods"></a>

### GET
<a name="assets-idget"></a>

**Operation ID:** `DescribeAsset`

Provides details about an asset.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you're working on. |

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

### DELETE
<a name="assets-iddelete"></a>

**Operation ID:** `DeleteAsset`

Permanently deletes an asset.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you're working on. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | None |  `202 Accepted` response<br />AWS Elemental MediaPackage accepted the request but has not processed it yet. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="assets-idoptions"></a>

Enable cross-origin resource sharing (CORS) by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you're working on. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None |  `200 OK` response<br />The list of tags is returned successfully. |

## Schemas
<a name="assets-id-schemas"></a>

### Response bodies
<a name="assets-id-response-examples"></a>

#### Asset schema
<a name="assets-id-response-body-asset-example"></a>

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
<a name="assets-id-properties"></a>

### Asset
<a name="assets-id-model-asset"></a>

Parameters for an asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) for the asset. You can get this from the response to any request to the asset. |
| createdAt | string | False | The date and time the Asset was initially submitted for Ingest. |
| egressEndpoints | Array of type [EgressEndpoint](#assets-id-model-egressendpoint) | False | List of playback endpoints that are available for this asset. |
| id | string | False | Unique identifier that you assign to the asset. |
| packagingGroupId | string | False | The ID of the packaging group associated with this asset. |
| resourceId | string | False | Unique identifier for this asset, as it's configured in the key provider service. |
| sourceArn | string | False | The ARN for the source content in Amazon S3. |
| sourceRoleArn | string | False | The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored. Valid format: `arn:aws:iam::{accountID}:role/{name}`  |
| tags | [Tags](#assets-id-model-tags) | False | The tags to assign to the asset. |

### EgressEndpoint
<a name="assets-id-model-egressendpoint"></a>

The playback endpoint for a packaging configuration on an asset.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| packagingConfigurationId | string | False | The ID of a packaging configuration that's applied to this asset. |
| status | string | False | The current processing status of the asset used for the packaging configuration. The status can be `QUEUED`, `PROCESSING`, `PLAYABLE`, or `FAILED`. Status information isn't available for most assets ingested before September 30th, 2021. |
| url | string | False | The URL that's used to request content from this endpoint. |

### Tags
<a name="assets-id-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |
