---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-config-update.html
---

# Backend appId Config Update
<a name="backend-appid-config-update"></a>

A configuration object that contains the authentication resources required for a user to access the Amplify Admin UI.

## URI
<a name="backend-appid-config-update-url"></a>

`/prod/backend/{{appId}}/config/update`

## HTTP methods
<a name="backend-appid-config-update-http-methods"></a>

### POST
<a name="backend-appid-config-updatepost"></a>

**Operation ID:** `UpdateBackendConfig`

Updates the AWS resources required to access the Amplify Admin UI.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BackendConfigRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-config-updateoptions"></a>

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
<a name="backend-appid-config-update-schemas"></a>

### Request bodies
<a name="backend-appid-config-update-request-examples"></a>

#### POST schema
<a name="backend-appid-config-update-request-body-post-example"></a>

```
{
  "loginAuthConfig": {
    "aws_user_pools_id": "string",
    "aws_cognito_identity_pool_id": "string",
    "aws_cognito_region": "string",
    "aws_user_pools_web_client_id": "string"
  }
}
```

### Response bodies
<a name="backend-appid-config-update-response-examples"></a>

#### BackendConfigRespObj schema
<a name="backend-appid-config-update-response-body-backendconfigrespobj-example"></a>

```
{
  "backendManagerAppId": "string",
  "loginAuthConfig": {
    "aws_user_pools_id": "string",
    "aws_cognito_identity_pool_id": "string",
    "aws_cognito_region": "string",
    "aws_user_pools_web_client_id": "string"
  },
  "appId": "string",
  "error": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-config-update-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-config-update-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-config-update-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-config-update-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-config-update-properties"></a>

### BackendConfigRespObj
<a name="backend-appid-config-update-model-backendconfigrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | False | The app ID. |
| backendManagerAppId | string | False | The app ID for the backend manager. |
| error | string | False | If the request fails, this error is returned. |
| loginAuthConfig | [LoginAuthConfigReqObj](#backend-appid-config-update-model-loginauthconfigreqobj) | False | Describes the Amazon Cognito configurations for the Admin UI auth resource to log in with. |

### BadRequestException
<a name="backend-appid-config-update-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-config-update-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-config-update-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### LoginAuthConfigReqObj
<a name="backend-appid-config-update-model-loginauthconfigreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| aws\_cognito\_identity\_pool\_id | string | False | The Amazon Cognito identity pool ID used for the Amplify Admin UI login authorization. |
| aws\_cognito\_region | string | False | The AWS Region for the Amplify Admin UI login. |
| aws\_user\_pools\_id | string | False | The Amazon Cognito user pool ID used for Amplify Admin UI login authentication. |
| aws\_user\_pools\_web\_client\_id | string | False | The web client ID for the Amazon Cognito user pools. |

### NotFoundException
<a name="backend-appid-config-update-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

### UpdateBackendConfigReqObj
<a name="backend-appid-config-update-model-updatebackendconfigreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| loginAuthConfig | [LoginAuthConfigReqObj](#backend-appid-config-update-model-loginauthconfigreqobj) | False | Describes the Amazon Cognito configuration for Admin UI access. |

## See also
<a name="backend-appid-config-update-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateBackendConfig
<a name="UpdateBackendConfig-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/UpdateBackendConfig)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/UpdateBackendConfig)
