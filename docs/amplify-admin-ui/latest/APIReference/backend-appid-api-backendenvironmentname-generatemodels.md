---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-api-backendenvironmentname-generatemodels.html
---

# Backend appId Api backendEnvironmentName GenerateModels
<a name="backend-appid-api-backendenvironmentname-generatemodels"></a>

The generated datastore models for your Amplify app. Web clients can consume these to use the datastore.

## URI
<a name="backend-appid-api-backendenvironmentname-generatemodels-url"></a>

`/prod/backend/{{appId}}/api/{{backendEnvironmentName}}/generateModels`

## HTTP methods
<a name="backend-appid-api-backendenvironmentname-generatemodels-http-methods"></a>

### POST
<a name="backend-appid-api-backendenvironmentname-generatemodelspost"></a>

**Operation ID:** `GenerateBackendAPIModels`

Generates a model schema for an existing backend API resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BackendAPICodegenRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-api-backendenvironmentname-generatemodelsoptions"></a>

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
<a name="backend-appid-api-backendenvironmentname-generatemodels-schemas"></a>

### Request bodies
<a name="backend-appid-api-backendenvironmentname-generatemodels-request-examples"></a>

#### POST schema
<a name="backend-appid-api-backendenvironmentname-generatemodels-request-body-post-example"></a>

```
{
  "resourceName": "string"
}
```

### Response bodies
<a name="backend-appid-api-backendenvironmentname-generatemodels-response-examples"></a>

#### BackendAPICodegenRespObj schema
<a name="backend-appid-api-backendenvironmentname-generatemodels-response-body-backendapicodegenrespobj-example"></a>

```
{
  "jobId": "string",
  "appId": "string",
  "error": "string",
  "operation": "string",
  "backendEnvironmentName": "string",
  "status": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-api-backendenvironmentname-generatemodels-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-api-backendenvironmentname-generatemodels-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-api-backendenvironmentname-generatemodels-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-api-backendenvironmentname-generatemodels-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-api-backendenvironmentname-generatemodels-properties"></a>

### BackendAPICodegenReqObj
<a name="backend-appid-api-backendenvironmentname-generatemodels-model-backendapicodegenreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceName | string | True | The name of this resource. |

### BackendAPICodegenRespObj
<a name="backend-appid-api-backendenvironmentname-generatemodels-model-backendapicodegenrespobj"></a>

The response object sent when a backend is created.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| error | string | False | If the request fails, this error is returned. |
| jobId | string | False | The ID for the job. |
| operation | string | False | The name of the operation. |
| status | string | False | The current status of the request. |

### BadRequestException
<a name="backend-appid-api-backendenvironmentname-generatemodels-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-api-backendenvironmentname-generatemodels-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-api-backendenvironmentname-generatemodels-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-api-backendenvironmentname-generatemodels-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-api-backendenvironmentname-generatemodels-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GenerateBackendAPIModels
<a name="GenerateBackendAPIModels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/GenerateBackendAPIModels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/GenerateBackendAPIModels)
