---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-storage-backendenvironmentname.html
---

# Backend appId Storage backendEnvironmentName
<a name="backend-appid-storage-backendenvironmentname"></a>

Update a storage resource in your Amplify app backend.

## URI
<a name="backend-appid-storage-backendenvironmentname-url"></a>

`/prod/backend/{{appId}}/storage/{{backendEnvironmentName}}`

## HTTP methods
<a name="backend-appid-storage-backendenvironmentname-http-methods"></a>

### POST
<a name="backend-appid-storage-backendenvironmentnamepost"></a>

**Operation ID:** `UpdateBackendStorage`

Updates an existing backend storage resource.

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
<a name="backend-appid-storage-backendenvironmentnameoptions"></a>

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
<a name="backend-appid-storage-backendenvironmentname-schemas"></a>

### Request bodies
<a name="backend-appid-storage-backendenvironmentname-request-examples"></a>

#### POST schema
<a name="backend-appid-storage-backendenvironmentname-request-body-post-example"></a>

```
{
  "resourceConfig": {
    "permissions": {
      "authenticated": [
        enum
      ],
      "unAuthenticated": [
        enum
      ]
    },
    "serviceName": enum
  },
  "resourceName": "string"
}
```

### Response bodies
<a name="backend-appid-storage-backendenvironmentname-response-examples"></a>

#### BackendStorageRespObj schema
<a name="backend-appid-storage-backendenvironmentname-response-body-backendstoragerespobj-example"></a>

```
{
  "jobId": "string",
  "appId": "string",
  "backendEnvironmentName": "string",
  "status": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-storage-backendenvironmentname-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-storage-backendenvironmentname-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-storage-backendenvironmentname-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-storage-backendenvironmentname-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-storage-backendenvironmentname-properties"></a>

### BackendStoragePermissions
<a name="backend-appid-storage-backendenvironmentname-model-backendstoragepermissions"></a>

Describes the read, write, and delete permissions users have against your storage S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authenticated | Array of type string<br />Values: `READ \| CREATE_AND_UPDATE \| DELETE` | True | Lists all authenticated user read, write, and delete permissions for your S3 bucket. |
| unAuthenticated | Array of type string<br />Values: `READ \| CREATE_AND_UPDATE \| DELETE` | False | Lists all unauthenticated user read, write, and delete permissions for your S3 bucket. |

### BackendStorageRespObj
<a name="backend-appid-storage-backendenvironmentname-model-backendstoragerespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| jobId | string | True | The ID for the job. |
| status | string | True | The current status of the request. |

### BadRequestException
<a name="backend-appid-storage-backendenvironmentname-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-storage-backendenvironmentname-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-storage-backendenvironmentname-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-storage-backendenvironmentname-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

### UpdateBackendStorageReqObj
<a name="backend-appid-storage-backendenvironmentname-model-updatebackendstoragereqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceConfig | [UpdateBackendStorageResourceConfig](#backend-appid-storage-backendenvironmentname-model-updatebackendstorageresourceconfig) | True | The resource configuration for updating backend storage. |
| resourceName | string | True | The name of the storage resource. |

### UpdateBackendStorageResourceConfig
<a name="backend-appid-storage-backendenvironmentname-model-updatebackendstorageresourceconfig"></a>

The resource configuration for updating backend storage.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| permissions | [BackendStoragePermissions](#backend-appid-storage-backendenvironmentname-model-backendstoragepermissions) | True | The authorization configuration for the storage S3 bucket. |
| serviceName | string<br />Values: `S3` | True | The name of the storage service. |

## See also
<a name="backend-appid-storage-backendenvironmentname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateBackendStorage
<a name="UpdateBackendStorage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/UpdateBackendStorage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/UpdateBackendStorage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify Admin UI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify-admin-ui` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
