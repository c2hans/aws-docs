---
source_url: https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups.html
---

# Packaging\_groups
<a name="packaging_groups"></a>

## URI
<a name="packaging_groups-url"></a>

`/packaging_groups`

## HTTP methods
<a name="packaging_groups-http-methods"></a>

### GET
<a name="packaging_groupsget"></a>

**Operation ID:** `ListPackagingGroups`

Lists packaging groups that match a set of filters that you define.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | Pagination token. Use this token to request the next page of record results. |
| maxResults | String | False | Upper bound on number of records to return. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PackagingGroupList |  `200 OK` response<br />The list of tags is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### POST
<a name="packaging_groupspost"></a>

**Operation ID:** `CreatePackagingGroup`

Creates a packaging group.

The packaging group holds one or more packaging configurations. When you create an asset, you specify the packaging group associated with the asset. The asset has playback endpoints for each packaging configuration within the group.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PackagingGroup |  `200 OK` response<br />The list of tags is returned successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### OPTIONS
<a name="packaging_groupsoptions"></a>

Enable cross-origin resource sharing (CORS) by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None |  `200 OK` response<br />The list of tags is returned successfully. |

## Schemas
<a name="packaging_groups-schemas"></a>

### Request bodies
<a name="packaging_groups-request-examples"></a>

#### POST schema
<a name="packaging_groups-request-body-post-example"></a>

```
{
  "authorization": {
    "cdnIdentifierSecret": "string",
    "secretsRoleArn": "string"
  },
  "egressAccessLogs": {
    "logGroupName": "string"
  },
  "id": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="packaging_groups-response-examples"></a>

#### PackagingGroupList schema
<a name="packaging_groups-response-body-packaginggrouplist-example"></a>

```
{
  "nextToken": "string",
  "packagingGroups": [
    {
      "authorization": {
        "cdnIdentifierSecret": "string",
        "secretsRoleArn": "string"
      },
      "createdAt": "string",
      "domainName": "string",
      "egressAccessLogs": {
        "logGroupName": "string"
      },
      "id": "string",
      "arn": "string",
      "approximateAssetCount": integer,
      "tags": {
      }
    }
  ]
}
```

#### PackagingGroup schema
<a name="packaging_groups-response-body-packaginggroup-example"></a>

```
{
  "authorization": {
    "cdnIdentifierSecret": "string",
    "secretsRoleArn": "string"
  },
  "createdAt": "string",
  "domainName": "string",
  "egressAccessLogs": {
    "logGroupName": "string"
  },
  "id": "string",
  "arn": "string",
  "approximateAssetCount": integer,
  "tags": {
  }
}
```

## Properties
<a name="packaging_groups-properties"></a>

### Authorization
<a name="packaging_groups-model-authorization"></a>

Parameters for enabling CDN authorization.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cdnIdentifierSecret | string | True | The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that's used for CDN authorization. |
| secretsRoleArn | string | True | The ARN for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager. |

### EgressAccessLogs
<a name="packaging_groups-model-egressaccesslogs"></a>

Configures egress access logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| logGroupName | string | False | Sets a custom Amazon CloudWatch log group name for egress logs. If a log group name isn't specified, the default name is used: `/aws/MediaPackage/EgressAccessLogs`. |

### PackagingGroup
<a name="packaging_groups-model-packaginggroup"></a>

Parameters for a packaging group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| approximateAssetCount | integer | False | The approximate number of assets in a packaging group. The number is approximate because the count is not updated immediately after adding or removing assets. |
| arn | string | False | The ARN for the packaging group. You can get this from the response to any request to the packaging group. |
| authorization | [Authorization](#packaging_groups-model-authorization) | False | Parameters for CDN authorization. |
| createdAt | string | False | The date and time the PackagingGroup was created. |
| domainName | string | False | The fully qualified domain name for assets in the PackagingGroup. |
| egressAccessLogs | [EgressAccessLogs](#packaging_groups-model-egressaccesslogs) | False | The configuration parameters for egress access logging. |
| id | string | False | Unique identifier that you assign to the packaging group. |
| tags | [Tags](#packaging_groups-model-tags) | False | The tags to assign to the packaging group. |

### PackagingGroupCreateParameters
<a name="packaging_groups-model-packaginggroupcreateparameters"></a>

Parameters for creating a packaging group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#packaging_groups-model-authorization) | False | Parameters for CDN authorization. |
| egressAccessLogs | [EgressAccessLogs](#packaging_groups-model-egressaccesslogs) | False | The configuration parameters for egress access logging. |
| id | string | True | Unique identifier that you assign to the packaging group. |
| tags | [Tags](#packaging_groups-model-tags) | False | The tags to assign to the packaging group. |

### PackagingGroupList
<a name="packaging_groups-model-packaginggrouplist"></a>

A collection of PackagingGroup records.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Pagination token. Use this token to request the next page of packaging groups results. |
| packagingGroups | Array of type [PackagingGroup](#packaging_groups-model-packaginggroup) | False | A list of PackagingGroup records that are configured on this account in this AWS Region. |

### Tags
<a name="packaging_groups-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |
