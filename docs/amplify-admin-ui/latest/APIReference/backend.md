---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend.html
---

# Backend
<a name="backend"></a>

All Amplify apps have a backend. The backend has settings and configurations for data storage, security, and other important logic that your app's users don't see. The easiest way to manage your Amplify app backend is using the Amplify Admin UI for your app.

## URI
<a name="backend-url"></a>

`/prod/backend`

## HTTP methods
<a name="backend-http-methods"></a>

### POST
<a name="backendpost"></a>

**Operation ID:** `CreateBackend`

This operation creates a backend for an Amplify app. Backends are automatically created at the time of app creation.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateBackendRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backendoptions"></a>

Enables CORS by returning the correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="backend-schemas"></a>

### Request bodies
<a name="backend-request-examples"></a>

#### POST schema
<a name="backend-request-body-post-example"></a>

```
{
  "resourceConfig": {
  },
  "appName": "string",
  "appId": "string",
  "resourceName": "string",
  "backendEnvironmentName": "string"
}
```

### Response bodies
<a name="backend-response-examples"></a>

#### CreateBackendRespObj schema
<a name="backend-response-body-createbackendrespobj-example"></a>

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
<a name="backend-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-properties"></a>

### BadRequestException
<a name="backend-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### CreateBackendReqObj
<a name="backend-model-createbackendreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| appName | string | True | The name of the app. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| resourceConfig | object | False | The resource configuration for creating a backend. |
| resourceName | string | False | The name of the resource. |

### CreateBackendRespObj
<a name="backend-model-createbackendrespobj"></a>

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
<a name="backend-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateBackend
<a name="CreateBackend-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/CreateBackend)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/CreateBackend)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify Admin UI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify-admin-ui` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
