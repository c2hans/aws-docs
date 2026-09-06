---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-storage-backendenvironmentname-details.html
---

# Backend appId Storage backendEnvironmentName Details
<a name="backend-appid-storage-backendenvironmentname-details"></a>

Get the details for a storage resource in your Amplify app backend.

## URI
<a name="backend-appid-storage-backendenvironmentname-details-url"></a>

`/prod/backend/{{appId}}/storage/{{backendEnvironmentName}}/details`

## HTTP methods
<a name="backend-appid-storage-backendenvironmentname-details-http-methods"></a>

### POST
<a name="backend-appid-storage-backendenvironmentname-detailspost"></a>

**Operation ID:** `GetBackendStorage`

Gets details for a backend storage resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetBackendStorageRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-storage-backendenvironmentname-detailsoptions"></a>

Enables CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="backend-appid-storage-backendenvironmentname-details-schemas"></a>

### Request bodies
<a name="backend-appid-storage-backendenvironmentname-details-request-examples"></a>

#### POST schema
<a name="backend-appid-storage-backendenvironmentname-details-request-body-post-example"></a>

```
{
  "resourceName": "string"
}
```

### Response bodies
<a name="backend-appid-storage-backendenvironmentname-details-response-examples"></a>

#### GetBackendStorageRespObj schema
<a name="backend-appid-storage-backendenvironmentname-details-response-body-getbackendstoragerespobj-example"></a>

```
{
  "resourceConfig": {
    "bucketName": "string",
    "permissions": {
      "authenticated": [
        enum
      ],
      "unAuthenticated": [
        enum
      ]
    },
    "imported": boolean,
    "serviceName": enum
  },
  "appId": "string",
  "resourceName": "string",
  "backendEnvironmentName": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-storage-backendenvironmentname-details-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-storage-backendenvironmentname-details-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-storage-backendenvironmentname-details-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-storage-backendenvironmentname-details-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-storage-backendenvironmentname-details-properties"></a>

### BackendStoragePermissions
<a name="backend-appid-storage-backendenvironmentname-details-model-backendstoragepermissions"></a>

Describes the read, write, and delete permissions users have against your storage S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authenticated | Array of type string<br />Values: `READ \| CREATE_AND_UPDATE \| DELETE` | True | Lists all authenticated user read, write, and delete permissions for your S3 bucket. |
| unAuthenticated | Array of type string<br />Values: `READ \| CREATE_AND_UPDATE \| DELETE` | False | Lists all unauthenticated user read, write, and delete permissions for your S3 bucket. |

### BadRequestException
<a name="backend-appid-storage-backendenvironmentname-details-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### GetBackendStorageReqObj
<a name="backend-appid-storage-backendenvironmentname-details-model-getbackendstoragereqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceName | string | True | The name of the storage resource. |

### GetBackendStorageResourceConfig
<a name="backend-appid-storage-backendenvironmentname-details-model-getbackendstorageresourceconfig"></a>

The details for a backend storage resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketName | string | False | The name of the S3 bucket. |
| imported | boolean | True | Returns `True` if the storage resource has been imported. |
| permissions | [BackendStoragePermissions](#backend-appid-storage-backendenvironmentname-details-model-backendstoragepermissions) | False | The authorization configuration for the storage S3 bucket. |
| serviceName | string<br />Values: `S3` | True | The name of the storage service. |

### GetBackendStorageRespObj
<a name="backend-appid-storage-backendenvironmentname-details-model-getbackendstoragerespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| resourceConfig | [GetBackendStorageResourceConfig](#backend-appid-storage-backendenvironmentname-details-model-getbackendstorageresourceconfig) | False | The resource configuration for the backend storage resource. |
| resourceName | string | False | The name of the storage resource. |

### InternalServiceException
<a name="backend-appid-storage-backendenvironmentname-details-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-storage-backendenvironmentname-details-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-storage-backendenvironmentname-details-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-storage-backendenvironmentname-details-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBackendStorage
<a name="GetBackendStorage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/GetBackendStorage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/GetBackendStorage)
