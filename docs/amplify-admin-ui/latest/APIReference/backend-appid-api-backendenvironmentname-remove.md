---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-api-backendenvironmentname-remove.html
---

# Backend appId Api backendEnvironmentName Remove
<a name="backend-appid-api-backendenvironmentname-remove"></a>

The data model from your Amplify project.

## URI
<a name="backend-appid-api-backendenvironmentname-remove-url"></a>

`/prod/backend/{{appId}}/api/{{backendEnvironmentName}}/remove`

## HTTP methods
<a name="backend-appid-api-backendenvironmentname-remove-http-methods"></a>

### POST
<a name="backend-appid-api-backendenvironmentname-removepost"></a>

**Operation ID:** `DeleteBackendAPI`

Deletes an existing backend API resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BackendAPIRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-api-backendenvironmentname-removeoptions"></a>

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
<a name="backend-appid-api-backendenvironmentname-remove-schemas"></a>

### Request bodies
<a name="backend-appid-api-backendenvironmentname-remove-request-examples"></a>

#### POST schema
<a name="backend-appid-api-backendenvironmentname-remove-request-body-post-example"></a>

```
{
  "resourceConfig": {
    "apiName": "string",
    "defaultAuthType": {
      "mode": enum,
      "settings": {
        "openIDProviderName": "string",
        "expirationTime": number,
        "openIDIatTTL": "string",
        "description": "string",
        "openIDAuthTTL": "string",
        "openIDClientId": "string",
        "openIDIssueURL": "string",
        "cognitoUserPoolId": "string"
      }
    },
    "transformSchema": "string",
    "service": "string",
    "additionalAuthTypes": [
      {
        "mode": enum,
        "settings": {
          "openIDProviderName": "string",
          "expirationTime": number,
          "openIDIatTTL": "string",
          "description": "string",
          "openIDAuthTTL": "string",
          "openIDClientId": "string",
          "openIDIssueURL": "string",
          "cognitoUserPoolId": "string"
        }
      }
    ],
    "conflictResolution": {
      "resolutionStrategy": enum
    }
  },
  "resourceName": "string"
}
```

### Response bodies
<a name="backend-appid-api-backendenvironmentname-remove-response-examples"></a>

#### BackendAPIRespObj schema
<a name="backend-appid-api-backendenvironmentname-remove-response-body-backendapirespobj-example"></a>

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
<a name="backend-appid-api-backendenvironmentname-remove-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-api-backendenvironmentname-remove-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-api-backendenvironmentname-remove-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-api-backendenvironmentname-remove-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-api-backendenvironmentname-remove-properties"></a>

### BackendAPIAppSyncAuthSettings
<a name="backend-appid-api-backendenvironmentname-remove-model-backendapiappsyncauthsettings"></a>

The authentication settings for accessing provisioned data models in your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cognitoUserPoolId | string | False | The Amazon Cognito user pool ID, if Amazon Cognito was used as an authentication setting to access your data models. |
| description | string | False | The API key description for `API_KEY`, if it was used as an authentication mechanism to access your data models. |
| expirationTime | number | False | The API key expiration time for `API_KEY`, if it was used as an authentication mechanism to access your data models. |
| openIDAuthTTL | string | False | The expiry time for the `OpenID` authentication mechanism. |
| openIDClientId | string | False | The `clientID` for `openID`, if `openID` was used as an authentication setting to access your data models. |
| openIDIatTTL | string | False | The expiry time for the `OpenID` authentication mechanism. |
| openIDIssueURL | string | False | The `openID` issuer URL, if `openID` was used as an authentication setting to access your data models. |
| openIDProviderName | string | False | The OpenID provider name, if OpenID was used as an authentication mechanism to access your data models. |

### BackendAPIAuthType
<a name="backend-appid-api-backendenvironmentname-remove-model-backendapiauthtype"></a>

Describes the auth types for your configured data models.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mode | string<br />Values: `API_KEY \| AWS_IAM \| AMAZON_COGNITO_USER_POOLS \| OPENID_CONNECT` | False | Describes the authentication mode. |
| settings | [BackendAPIAppSyncAuthSettings](#backend-appid-api-backendenvironmentname-remove-model-backendapiappsyncauthsettings) | False | Describes settings for the authentication mode. |

### BackendAPIConflictResolution
<a name="backend-appid-api-backendenvironmentname-remove-model-backendapiconflictresolution"></a>

Describes the conflict resolution configuration for your data model configured in your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resolutionStrategy | string<br />Values: `OPTIMISTIC_CONCURRENCY \| LAMBDA \| AUTOMERGE \| NONE` | False | The strategy for conflict resolution. |

### BackendAPIReqObj
<a name="backend-appid-api-backendenvironmentname-remove-model-backendapireqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceConfig | [BackendAPIResourceConfig](#backend-appid-api-backendenvironmentname-remove-model-backendapiresourceconfig) | False | Defines the resource configuration for the data model in your Amplify project. |
| resourceName | string | True | The name of this resource. |

### BackendAPIResourceConfig
<a name="backend-appid-api-backendenvironmentname-remove-model-backendapiresourceconfig"></a>

The resource config for the data model, configured as a part of the Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalAuthTypes | Array of type [BackendAPIAuthType](#backend-appid-api-backendenvironmentname-remove-model-backendapiauthtype) | False | Additional authentication methods used to interact with your data models. |
| apiName | string | False | The API name used to interact with the data model, configured as a part of your Amplify project. |
| conflictResolution | [BackendAPIConflictResolution](#backend-appid-api-backendenvironmentname-remove-model-backendapiconflictresolution) | False | The conflict resolution strategy for your data stored in the data models. |
| defaultAuthType | [BackendAPIAuthType](#backend-appid-api-backendenvironmentname-remove-model-backendapiauthtype) | False | The default authentication type for interacting with the configured data models in your Amplify project. |
| service | string | False | The service used to provision and interact with the data model. |
| transformSchema | string | False | The definition of the data model in the annotated transform of the GraphQL schema. |

### BackendAPIRespObj
<a name="backend-appid-api-backendenvironmentname-remove-model-backendapirespobj"></a>

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
<a name="backend-appid-api-backendenvironmentname-remove-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-api-backendenvironmentname-remove-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-api-backendenvironmentname-remove-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-api-backendenvironmentname-remove-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-api-backendenvironmentname-remove-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteBackendAPI
<a name="DeleteBackendAPI-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/DeleteBackendAPI)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/DeleteBackendAPI)
