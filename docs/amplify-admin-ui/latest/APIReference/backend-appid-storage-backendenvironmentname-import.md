---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-storage-backendenvironmentname-import.html
---

# Backend appId Storage backendEnvironmentName Import
<a name="backend-appid-storage-backendenvironmentname-import"></a>

Import a storage resource into your Amplify app backend.

## URI
<a name="backend-appid-storage-backendenvironmentname-import-url"></a>

`/prod/backend/{{appId}}/storage/{{backendEnvironmentName}}/import`

## HTTP methods
<a name="backend-appid-storage-backendenvironmentname-import-http-methods"></a>

### POST
<a name="backend-appid-storage-backendenvironmentname-importpost"></a>

**Operation ID:** `ImportBackendStorage`

Imports an existing backend storage resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BackendStorageRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-storage-backendenvironmentname-importoptions"></a>

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
<a name="backend-appid-storage-backendenvironmentname-import-schemas"></a>

### Request bodies
<a name="backend-appid-storage-backendenvironmentname-import-request-examples"></a>

#### POST schema
<a name="backend-appid-storage-backendenvironmentname-import-request-body-post-example"></a>

```
{
  "bucketName": "string",
  "serviceName": enum
}
```

### Response bodies
<a name="backend-appid-storage-backendenvironmentname-import-response-examples"></a>

#### BackendStorageRespObj schema
<a name="backend-appid-storage-backendenvironmentname-import-response-body-backendstoragerespobj-example"></a>

```
{
  "jobId": "string",
  "appId": "string",
  "backendEnvironmentName": "string",
  "status": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-storage-backendenvironmentname-import-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-storage-backendenvironmentname-import-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-storage-backendenvironmentname-import-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-storage-backendenvironmentname-import-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-storage-backendenvironmentname-import-properties"></a>

### BackendStorageRespObj
<a name="backend-appid-storage-backendenvironmentname-import-model-backendstoragerespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| jobId | string | True | The ID for the job. |
| status | string | True | The current status of the request. |

### BadRequestException
<a name="backend-appid-storage-backendenvironmentname-import-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### ImportBackendStorageReqObj
<a name="backend-appid-storage-backendenvironmentname-import-model-importbackendstoragereqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketName | string | False | The name of the S3 bucket. |
| serviceName | string<br />Values: `S3` | True | The name of the storage service. |

### InternalServiceException
<a name="backend-appid-storage-backendenvironmentname-import-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-storage-backendenvironmentname-import-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-storage-backendenvironmentname-import-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-storage-backendenvironmentname-import-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ImportBackendStorage
<a name="ImportBackendStorage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/ImportBackendStorage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/ImportBackendStorage)
