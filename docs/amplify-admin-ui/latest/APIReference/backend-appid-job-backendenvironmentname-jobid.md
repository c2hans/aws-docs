---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-job-backendenvironmentname-jobid.html
---

# Backend appId Job backendEnvironmentName jobId
<a name="backend-appid-job-backendenvironmentname-jobid"></a>

Jobs perform backend API actions on your behalf based on your choices in the Amplify Admin UI. The actions that the jobs perform depend on the underlying API request sent from the Amplify Admin UI.

This resource is associated with the `GetBackendJob` and `UpdateBackendJob` operations.

## URI
<a name="backend-appid-job-backendenvironmentname-jobid-url"></a>

`/prod/backend/{{appId}}/job/{{backendEnvironmentName}}/{{jobId}}`

## HTTP methods
<a name="backend-appid-job-backendenvironmentname-jobid-http-methods"></a>

### GET
<a name="backend-appid-job-backendenvironmentname-jobidget"></a>

**Operation ID:** `GetBackendJob`

Returns information about a specific job.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |
| {{jobId}} | String | True | The ID for the job. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BackendJobRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### POST
<a name="backend-appid-job-backendenvironmentname-jobidpost"></a>

**Operation ID:** `UpdateBackendJob`

Updates a specific job.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |
| {{jobId}} | String | True | The ID for the job. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BackendJobRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-job-backendenvironmentname-jobidoptions"></a>

Enables CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |
| {{jobId}} | String | True | The ID for the job. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="backend-appid-job-backendenvironmentname-jobid-schemas"></a>

### Request bodies
<a name="backend-appid-job-backendenvironmentname-jobid-request-examples"></a>

#### POST schema
<a name="backend-appid-job-backendenvironmentname-jobid-request-body-post-example"></a>

```
{
  "operation": "string",
  "status": "string"
}
```

### Response bodies
<a name="backend-appid-job-backendenvironmentname-jobid-response-examples"></a>

#### BackendJobRespObj schema
<a name="backend-appid-job-backendenvironmentname-jobid-response-body-backendjobrespobj-example"></a>

```
{
  "jobId": "string",
  "createTime": "string",
  "appId": "string",
  "updateTime": "string",
  "error": "string",
  "operation": "string",
  "backendEnvironmentName": "string",
  "status": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-job-backendenvironmentname-jobid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-job-backendenvironmentname-jobid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-job-backendenvironmentname-jobid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-job-backendenvironmentname-jobid-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-job-backendenvironmentname-jobid-properties"></a>

### BackendJobReqObj
<a name="backend-appid-job-backendenvironmentname-jobid-model-backendjobreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| operation | string | False | Filters the list of response objects to include only those with the specified operation name. |
| status | string | False | Filters the list of response objects to include only those with the specified status. |

### BackendJobRespObj
<a name="backend-appid-job-backendenvironmentname-jobid-model-backendjobrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| createTime | string | False | The time when the job was created. |
| error | string | False | If the request fails, this error is returned. |
| jobId | string | False | The ID for the job. |
| operation | string | False | The name of the operation. |
| status | string | False | The current status of the request. |
| updateTime | string | False | The time when the job was last updated. |

### BadRequestException
<a name="backend-appid-job-backendenvironmentname-jobid-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-job-backendenvironmentname-jobid-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-job-backendenvironmentname-jobid-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-job-backendenvironmentname-jobid-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-job-backendenvironmentname-jobid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBackendJob
<a name="GetBackendJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/GetBackendJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/GetBackendJob)

### UpdateBackendJob
<a name="UpdateBackendJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/UpdateBackendJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/UpdateBackendJob)
