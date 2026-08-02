---
source_url: https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups-id.html
---

# Packaging\_groups id
<a name="packaging_groups-id"></a>

## URI
<a name="packaging_groups-id-url"></a>

`/packaging_groups/{{id}}`

## HTTP methods
<a name="packaging_groups-id-http-methods"></a>

### GET
<a name="packaging_groups-idget"></a>

**Operation ID:** `DescribePackagingGroup`

Provides details about a packaging group.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you're working on. |

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

### PUT
<a name="packaging_groups-idput"></a>

**Operation ID:** `UpdatePackagingGroup`

Updates a specific packaging group.

You can't change the `id` attribute or any other system-generated attributes.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | Identifier for the object that you're working on. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PackagingGroup |  `200 OK` response<br />The packaging group is updated successfully. |
| 403 | None |  `403 Forbidden` response<br />AWS Elemental MediaPackage cannot authorize the request, possibly due to insufficient authentication credentials. |
| 404 | None |  `404 Not Found` response<br />AWS Elemental MediaPackage did not find a representation of the target resource. |
| 422 | None |  `422 Unprocessable Entity` response<br />AWS Elemental MediaPackage could not process the instructions in the body of the request. |
| 429 | None |  `429 Too Many Requests` response<br />One of these two error conditions:<br />Too many requests have been sent in a given amount of time.<br />Your account has exceeded the quota allotted for the resource that you're creating. |
| 500 | None |  `500 Internal Server Error` response<br />An unexpected condition prevented AWS Elemental MediaPackage from fulfilling the request. |
| 503 | None |  `Service unavailable` response<br />AWS Elemental MediaPackage can't currently complete the request, usually because of a temporary overload or maintenance. |

### DELETE
<a name="packaging_groups-iddelete"></a>

**Operation ID:** `DeletePackagingGroup`

Permanently deletes a packaging group.

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
<a name="packaging_groups-idoptions"></a>

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
<a name="packaging_groups-id-schemas"></a>

### Request bodies
<a name="packaging_groups-id-request-examples"></a>

#### PUT schema
<a name="packaging_groups-id-request-body-put-example"></a>

```
{
  "authorization": {
    "cdnIdentifierSecret": "string",
    "secretsRoleArn": "string"
  }
}
```

### Response bodies
<a name="packaging_groups-id-response-examples"></a>

#### PackagingGroup schema
<a name="packaging_groups-id-response-body-packaginggroup-example"></a>

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
<a name="packaging_groups-id-properties"></a>

### Authorization
<a name="packaging_groups-id-model-authorization"></a>

Parameters for enabling CDN authorization.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cdnIdentifierSecret | string | True | The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that's used for CDN authorization. |
| secretsRoleArn | string | True | The ARN for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager. |

### EgressAccessLogs
<a name="packaging_groups-id-model-egressaccesslogs"></a>

Configures egress access logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| logGroupName | string | False | Sets a custom Amazon CloudWatch log group name for egress logs. If a log group name isn't specified, the default name is used: `/aws/MediaPackage/EgressAccessLogs`. |

### PackagingGroup
<a name="packaging_groups-id-model-packaginggroup"></a>

Parameters for a packaging group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| approximateAssetCount | integer | False | The approximate number of assets in a packaging group. The number is approximate because the count is not updated immediately after adding or removing assets. |
| arn | string | False | The ARN for the packaging group. You can get this from the response to any request to the packaging group. |
| authorization | [Authorization](#packaging_groups-id-model-authorization) | False | Parameters for CDN authorization. |
| createdAt | string | False | The date and time the PackagingGroup was created. |
| domainName | string | False | The fully qualified domain name for assets in the PackagingGroup. |
| egressAccessLogs | [EgressAccessLogs](#packaging_groups-id-model-egressaccesslogs) | False | The configuration parameters for egress access logging. |
| id | string | False | Unique identifier that you assign to the packaging group. |
| tags | [Tags](#packaging_groups-id-model-tags) | False | The tags to assign to the packaging group. |

### PackagingGroupUpdateParameters
<a name="packaging_groups-id-model-packaginggroupupdateparameters"></a>

Parameters used to update a MediaPackage packaging group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#packaging_groups-id-model-authorization) | False | Parameters for CDN authorization. |

### Tags
<a name="packaging_groups-id-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |
