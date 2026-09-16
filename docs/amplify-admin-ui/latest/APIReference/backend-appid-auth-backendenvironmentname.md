---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-auth-backendenvironmentname.html
---

# Backend appId Auth backendEnvironmentName
<a name="backend-appid-auth-backendenvironmentname"></a>

The authentication and authorization settings from your Amplify project.

## URI
<a name="backend-appid-auth-backendenvironmentname-url"></a>

`/prod/backend/{{appId}}/auth/{{backendEnvironmentName}}`

## HTTP methods
<a name="backend-appid-auth-backendenvironmentname-http-methods"></a>

### POST
<a name="backend-appid-auth-backendenvironmentnamepost"></a>

**Operation ID:** `UpdateBackendAuth`

Updates an existing backend authentication resource.

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
<a name="backend-appid-auth-backendenvironmentnameoptions"></a>

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
<a name="backend-appid-auth-backendenvironmentname-schemas"></a>

### Request bodies
<a name="backend-appid-auth-backendenvironmentname-request-examples"></a>

#### POST schema
<a name="backend-appid-auth-backendenvironmentname-request-body-post-example"></a>

```
{
  "resourceConfig": {
    "userPoolConfigs": {
      "forgotPassword": {
        "smsSettings": {
          "smsMessage": "string"
        },
        "deliveryMethod": enum,
        "emailSettings": {
          "emailMessage": "string",
          "emailSubject": "string"
        }
      },
      "passwordPolicy": {
        "minimumLength": number,
        "additionalConstraints": [
          enum
        ]
      },
      "mfa": {
        "MFAMode": enum,
        "settings": {
        }
      },
      "oAuth": {
        "redirectSignOutURIs": [
          "string"
        ],
        "domainPrefix": "string",
        "redirectSignInURIs": [
          "string"
        ],
        "oAuthScopes": [
          enum
        ],
        "socialProviderSettings": {
        },
        "oAuthGrantType": enum
      },
      "verificationMessage": {
        "smsSettings": {
          "smsMessage": "string"
        },
        "deliveryMethod": enum,
        "emailSettings": {
          "emailMessage": "string",
          "emailSubject": "string"
        }
      }
    },
    "authResources": enum,
    "service": enum,
    "identityPoolConfigs": {
      "unauthenticatedLogin": boolean
    }
  },
  "resourceName": "string"
}
```

### Response bodies
<a name="backend-appid-auth-backendenvironmentname-response-examples"></a>

#### BackendAuthRespObj schema
<a name="backend-appid-auth-backendenvironmentname-response-body-backendauthrespobj-example"></a>

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
<a name="backend-appid-auth-backendenvironmentname-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-auth-backendenvironmentname-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-auth-backendenvironmentname-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-auth-backendenvironmentname-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-auth-backendenvironmentname-properties"></a>

### BackendAuthRespObj
<a name="backend-appid-auth-backendenvironmentname-model-backendauthrespobj"></a>

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
<a name="backend-appid-auth-backendenvironmentname-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### DeliveryMethod
<a name="backend-appid-auth-backendenvironmentname-model-deliverymethod"></a>

The type of verification message to send.
+ `EMAIL`
+ `SMS`

### EmailSettings
<a name="backend-appid-auth-backendenvironmentname-model-emailsettings"></a>

The settings for the email message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| emailMessage | string | False | The contents of the email message. |
| emailSubject | string | False | The contents of the subject line of the email message. |

### InternalServiceException
<a name="backend-appid-auth-backendenvironmentname-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-auth-backendenvironmentname-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-auth-backendenvironmentname-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

### SmsSettings
<a name="backend-appid-auth-backendenvironmentname-model-smssettings"></a>

The settings for the SMS message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| smsMessage | string | False | The contents of the SMS message. |

### UpdateBackendAuthForgotPasswordConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthforgotpasswordconfig"></a>

**(DEPRECATED)** Describes the forgot password policy for authenticating into the Amplify app.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryMethod | [DeliveryMethod](#backend-appid-auth-backendenvironmentname-model-deliverymethod) | False | **(DEPRECATED)** Describes which mode to use (either SMS or email) to deliver messages to app users that want to recover their password. |
| emailSettings | [EmailSettings](#backend-appid-auth-backendenvironmentname-model-emailsettings) | False | **(DEPRECATED)** The configuration for the email sent when an app user forgets their password. |
| smsSettings | [SmsSettings](#backend-appid-auth-backendenvironmentname-model-smssettings) | False | **(DEPRECATED)** The configuration for the SMS message sent when an Amplify app user forgets their password. |

### UpdateBackendAuthIdentityPoolConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthidentitypoolconfig"></a>

Describes the authorization configuration for the Amazon Cognito identity pool, provisioned as a part of your auth resource in the Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| unauthenticatedLogin | boolean | False | A boolean value that can be set to allow or disallow guest-level authorization into your Amplify app. |

### UpdateBackendAuthMFAConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthmfaconfig"></a>

Updates the multi-factor authentication (MFA) configuration for the backend of your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| MFAMode | string<br />Values: `ON \| OFF \| OPTIONAL` | False | The MFA mode for the backend of your Amplify project. |
| settings | object | False | The settings of your MFA configuration for the backend of your Amplify project. |

### UpdateBackendAuthOAuthConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthoauthconfig"></a>

The OAuth configurations for authenticating users into your Amplify app.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainPrefix | string | False | The Amazon Cognito domain prefix used to create a hosted UI for authentication. |
| oAuthGrantType | string<br />Values: `CODE \| IMPLICIT` | False | The OAuth grant type to allow app users to authenticate from your Amplify app. |
| oAuthScopes | Array of type string<br />Values: `PHONE \| EMAIL \| OPENID \| PROFILE \| AWS_COGNITO_SIGNIN_USER_ADMIN` | False | The list of OAuth-related flows that can allow users to authenticate from your Amplify app. |
| redirectSignInURIs | Array of type string | False | Redirect URLs that OAuth uses when a user signs in to an Amplify app. |
| redirectSignOutURIs | Array of type string | False | Redirect URLs that OAuth uses when a user signs out of an Amplify app. |
| socialProviderSettings | object | False | Describes third-party social federation configurations for allowing your users to sign in with OAuth. |

### UpdateBackendAuthPasswordPolicyConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthpasswordpolicyconfig"></a>

Describes the password policy for your Amazon Cognito user pool configured as a part of your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalConstraints | Array of type string<br />Values: `REQUIRE_DIGIT \| REQUIRE_LOWERCASE \| REQUIRE_SYMBOL \| REQUIRE_UPPERCASE` | False | Describes additional constraints on password requirements to sign in to the auth resource, configured as a part of your Amplify project. |
| minimumLength | number | False | Describes the minimum length of the password required to sign in to the auth resource, configured as a part of your Amplify project. |

### UpdateBackendAuthReqObj
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceConfig | [UpdateBackendAuthResourceConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthresourceconfig) | True | The resource configuration for this request object. |
| resourceName | string | True | The name of this resource. |

### UpdateBackendAuthResourceConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthresourceconfig"></a>

Defines the resource configuration when updating an authentication resource in your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authResources | string<br />Values: `USER_POOL_ONLY \| IDENTITY_POOL_AND_USER_POOL` | True | Defines the service name to use when configuring an authentication resource in your Amplify project. |
| identityPoolConfigs | [UpdateBackendAuthIdentityPoolConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthidentitypoolconfig) | False | Describes the authorization configuration for the Amazon Cognito identity pool, provisioned as a part of your auth resource in the Amplify project. |
| service | string<br />Values: `COGNITO` | True | Defines the service name to use when configuring an authentication resource in your Amplify project. |
| userPoolConfigs | [UpdateBackendAuthUserPoolConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthuserpoolconfig) | True | Describes the authentication configuration for the Amazon Cognito user pool, provisioned as a part of your auth resource in the Amplify project. |

### UpdateBackendAuthUserPoolConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthuserpoolconfig"></a>

Describes the Amazon Cognito user pool configuration for the authorization resource to be configured for your Amplify project on an update.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| forgotPassword | [UpdateBackendAuthForgotPasswordConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthforgotpasswordconfig) | False | **(DEPRECATED)** Describes the forgot password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.  |
| mfa | [UpdateBackendAuthMFAConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthmfaconfig) | False | Describes whether to apply multi-factor authentication policies for your Amazon Cognito user pool configured as a part of your Amplify project. |
| oAuth | [UpdateBackendAuthOAuthConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthoauthconfig) | False | Describes the OAuth policy and rules for your Amazon Cognito user pool, configured as a part of your Amplify project. |
| passwordPolicy | [UpdateBackendAuthPasswordPolicyConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthpasswordpolicyconfig) | False | Describes the password policy for your Amazon Cognito user pool, configured as a part of your Amplify project. |
| verificationMessage | [UpdateBackendAuthVerificationMessageConfig](#backend-appid-auth-backendenvironmentname-model-updatebackendauthverificationmessageconfig) | False | Describes the email or SMS verification message for your Amazon Cognito user pool, configured as a part of your Amplify project. |

### UpdateBackendAuthVerificationMessageConfig
<a name="backend-appid-auth-backendenvironmentname-model-updatebackendauthverificationmessageconfig"></a>

Updates the configuration of the email or SMS message for the auth resource configured for your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryMethod | [DeliveryMethod](#backend-appid-auth-backendenvironmentname-model-deliverymethod) | True | The type of verification message to send. |
| emailSettings | [EmailSettings](#backend-appid-auth-backendenvironmentname-model-emailsettings) | False | The settings for the email message. |
| smsSettings | [SmsSettings](#backend-appid-auth-backendenvironmentname-model-smssettings) | False | The settings for the SMS message. |

## See also
<a name="backend-appid-auth-backendenvironmentname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateBackendAuth
<a name="UpdateBackendAuth-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/UpdateBackendAuth)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/UpdateBackendAuth)
