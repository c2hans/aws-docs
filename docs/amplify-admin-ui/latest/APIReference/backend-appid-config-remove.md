---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-config-remove.html
---

# Backend appId Config Remove
<a name="backend-appid-config-remove"></a>

A configuration object that contains the authentication resources required for a user to access the Amplify Admin UI.

## URI
<a name="backend-appid-config-remove-url"></a>

`/prod/backend/{{appId}}/config/remove`

## HTTP methods
<a name="backend-appid-config-remove-http-methods"></a>

### POST
<a name="backend-appid-config-removepost"></a>

**Operation ID:** `RemoveBackendConfig`

Removes the AWS resources required to access the Amplify Admin UI.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RemoveBackendConfigRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-config-removeoptions"></a>

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
<a name="backend-appid-config-remove-schemas"></a>

### Response bodies
<a name="backend-appid-config-remove-response-examples"></a>

#### RemoveBackendConfigRespObj schema
<a name="backend-appid-config-remove-response-body-removebackendconfigrespobj-example"></a>

```
{
  "error": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-config-remove-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-config-remove-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-config-remove-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-config-remove-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-config-remove-properties"></a>

### BadRequestException
<a name="backend-appid-config-remove-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-config-remove-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-config-remove-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-config-remove-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

### RemoveBackendConfigRespObj
<a name="backend-appid-config-remove-model-removebackendconfigrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| error | string | False | If the request fails, this error is returned. |

## See also
<a name="backend-appid-config-remove-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RemoveBackendConfig
<a name="RemoveBackendConfig-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/RemoveBackendConfig)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/RemoveBackendConfig)
