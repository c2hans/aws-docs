---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-details.html
---

# Backend appId Details
<a name="backend-appid-details"></a>

Project-level details for your Amplify project.

## URI
<a name="backend-appid-details-url"></a>

`/prod/backend/{{appId}}/details`

## HTTP methods
<a name="backend-appid-details-http-methods"></a>

### POST
<a name="backend-appid-detailspost"></a>

**Operation ID:** `GetBackend`

Provides project-level details for your Amplify UI project.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetBackendRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-detailsoptions"></a>

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
<a name="backend-appid-details-schemas"></a>

### Request bodies
<a name="backend-appid-details-request-examples"></a>

#### POST schema
<a name="backend-appid-details-request-body-post-example"></a>

```
{
  "backendEnvironmentName": "string"
}
```

### Response bodies
<a name="backend-appid-details-response-examples"></a>

#### GetBackendRespObj schema
<a name="backend-appid-details-response-body-getbackendrespobj-example"></a>

```
{
  "appName": "string",
  "appId": "string",
  "backendEnvironmentList": [
    "string"
  ],
  "amplifyFeatureFlags": "string",
  "error": "string",
  "amplifyMetaConfig": "string",
  "backendEnvironmentName": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-details-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-details-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-details-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-details-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-details-properties"></a>

### BadRequestException
<a name="backend-appid-details-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### GetBackendReqObj
<a name="backend-appid-details-model-getbackendreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| backendEnvironmentName | string | False | The name of the backend environment. |

### GetBackendRespObj
<a name="backend-appid-details-model-getbackendrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| amplifyFeatureFlags | string | False | A stringified version of the `cli.json` file for your Amplify project. |
| amplifyMetaConfig | string | False | A stringified version of the current configs for your Amplify project. |
| appId | string | True | The app ID. |
| appName | string | False | The name of the app. |
| backendEnvironmentList | Array of type string | False | A list of backend environments in an array. |
| backendEnvironmentName | string | False | The name of the backend environment. |
| error | string | False | If the request failed, this is the returned error. |

### InternalServiceException
<a name="backend-appid-details-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-details-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-details-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-details-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBackend
<a name="GetBackend-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/GetBackend)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/GetBackend)
