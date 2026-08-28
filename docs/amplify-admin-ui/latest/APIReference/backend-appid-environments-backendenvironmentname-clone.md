---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-environments-backendenvironmentname-clone.html
---

# Backend appId Environments backendEnvironmentName Clone
<a name="backend-appid-environments-backendenvironmentname-clone"></a>

A clone of an existing environment in your Amplify project.

## URI
<a name="backend-appid-environments-backendenvironmentname-clone-url"></a>

`/prod/backend/{{appId}}/environments/{{backendEnvironmentName}}/clone`

## HTTP methods
<a name="backend-appid-environments-backendenvironmentname-clone-http-methods"></a>

### POST
<a name="backend-appid-environments-backendenvironmentname-clonepost"></a>

**Operation ID:** `CloneBackend`

This operation clones an existing backend.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CloneBackendRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-environments-backendenvironmentname-cloneoptions"></a>

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
<a name="backend-appid-environments-backendenvironmentname-clone-schemas"></a>

### Request bodies
<a name="backend-appid-environments-backendenvironmentname-clone-request-examples"></a>

#### POST schema
<a name="backend-appid-environments-backendenvironmentname-clone-request-body-post-example"></a>

```
{
  "targetEnvironmentName": "string"
}
```

### Response bodies
<a name="backend-appid-environments-backendenvironmentname-clone-response-examples"></a>

#### CloneBackendRespObj schema
<a name="backend-appid-environments-backendenvironmentname-clone-response-body-clonebackendrespobj-example"></a>

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
<a name="backend-appid-environments-backendenvironmentname-clone-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-environments-backendenvironmentname-clone-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-environments-backendenvironmentname-clone-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-environments-backendenvironmentname-clone-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-environments-backendenvironmentname-clone-properties"></a>

### BadRequestException
<a name="backend-appid-environments-backendenvironmentname-clone-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### CloneBackendReqObj
<a name="backend-appid-environments-backendenvironmentname-clone-model-clonebackendreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| targetEnvironmentName | string | True | The name of the destination backend environment to be created. |

### CloneBackendRespObj
<a name="backend-appid-environments-backendenvironmentname-clone-model-clonebackendrespobj"></a>

The response object sent when a backend is created.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| error | string | False | If the request fails, this error is returned. |
| jobId | string | False | The ID for the job. |
| operation | string | False | The name of the operation. |
| status | string | False | The current status of the request. |

### InternalServiceException
<a name="backend-appid-environments-backendenvironmentname-clone-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-environments-backendenvironmentname-clone-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-environments-backendenvironmentname-clone-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-environments-backendenvironmentname-clone-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CloneBackend
<a name="CloneBackend-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/CloneBackend)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/CloneBackend)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify Admin UI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify-admin-ui` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
