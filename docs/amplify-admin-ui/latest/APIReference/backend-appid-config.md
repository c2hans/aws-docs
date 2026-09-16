---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-config.html
---

# Backend appId Config
<a name="backend-appid-config"></a>

A configuration object that contains the authentication resources required for a user to access the Amplify Admin UI.

## URI
<a name="backend-appid-config-url"></a>

`/prod/backend/{{appId}}/config`

## HTTP methods
<a name="backend-appid-config-http-methods"></a>

### POST
<a name="backend-appid-configpost"></a>

**Operation ID:** `CreateBackendConfig`

Creates a config object for a backend.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateBackendConfigRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-configoptions"></a>

Enables CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="backend-appid-config-schemas"></a>

### Request bodies
<a name="backend-appid-config-request-examples"></a>

#### POST schema
<a name="backend-appid-config-request-body-post-example"></a>

```
{
  "backendManagerAppId": "string"
}
```

### Response bodies
<a name="backend-appid-config-response-examples"></a>

#### CreateBackendConfigRespObj schema
<a name="backend-appid-config-response-body-createbackendconfigrespobj-example"></a>

```
{
  "jobId": "string",
  "appId": "string",
  "backendEnvironmentName": "string",
  "status": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-config-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-config-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-config-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-config-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-config-properties"></a>

### BadRequestException
<a name="backend-appid-config-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### CreateBackendConfigReqObj
<a name="backend-appid-config-model-createbackendconfigreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| backendManagerAppId | string | False | The app ID for the backend manager. |

### CreateBackendConfigRespObj
<a name="backend-appid-config-model-createbackendconfigrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | False | The name of the backend environment. |
| jobId | string | False | The ID for the job. |
| status | string | False | The current status of the request. |

### InternalServiceException
<a name="backend-appid-config-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-config-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-config-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-config-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateBackendConfig
<a name="CreateBackendConfig-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/CreateBackendConfig)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/CreateBackendConfig)
