---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-auth-backendenvironmentname-import.html
---

# Backend appId Auth backendEnvironmentName Import
<a name="backend-appid-auth-backendenvironmentname-import"></a>

Imports an existing backend authentication resource.

## URI
<a name="backend-appid-auth-backendenvironmentname-import-url"></a>

`/prod/backend/{{appId}}/auth/{{backendEnvironmentName}}/import`

## HTTP methods
<a name="backend-appid-auth-backendenvironmentname-import-http-methods"></a>

### POST
<a name="backend-appid-auth-backendenvironmentname-importpost"></a>

**Operation ID:** `ImportBackendAuth`

Imports an existing backend authentication resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BackendAuthRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-auth-backendenvironmentname-importoptions"></a>

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
<a name="backend-appid-auth-backendenvironmentname-import-schemas"></a>

### Request bodies
<a name="backend-appid-auth-backendenvironmentname-import-request-examples"></a>

#### POST schema
<a name="backend-appid-auth-backendenvironmentname-import-request-body-post-example"></a>

```
{
  "webClientId": "string",
  "nativeClientId": "string",
  "identityPoolId": "string",
  "userPoolId": "string"
}
```

### Response bodies
<a name="backend-appid-auth-backendenvironmentname-import-response-examples"></a>

#### BackendAuthRespObj schema
<a name="backend-appid-auth-backendenvironmentname-import-response-body-backendauthrespobj-example"></a>

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
<a name="backend-appid-auth-backendenvironmentname-import-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-auth-backendenvironmentname-import-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-auth-backendenvironmentname-import-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-auth-backendenvironmentname-import-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-auth-backendenvironmentname-import-properties"></a>

### BackendAuthRespObj
<a name="backend-appid-auth-backendenvironmentname-import-model-backendauthrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| error | string | False | If the request fails, this error is returned. |
| jobId | string | False | The ID for the job. |
| operation | string | False | The name of the operation. |
| status | string | False | The current status of the request. |

### BadRequestException
<a name="backend-appid-auth-backendenvironmentname-import-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### ImportBackendAuthReqObj
<a name="backend-appid-auth-backendenvironmentname-import-model-importbackendauthreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| identityPoolId | string | False | The ID of the Amazon Cognito identity pool. |
| nativeClientId | string | True | The ID of the Amazon Cognito native client. |
| userPoolId | string | True | The ID of the Amazon Cognito user pool. |
| webClientId | string | True | The ID of the Amazon Cognito web client. |

### InternalServiceException
<a name="backend-appid-auth-backendenvironmentname-import-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-auth-backendenvironmentname-import-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-auth-backendenvironmentname-import-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-auth-backendenvironmentname-import-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ImportBackendAuth
<a name="ImportBackendAuth-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/ImportBackendAuth)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/ImportBackendAuth)
