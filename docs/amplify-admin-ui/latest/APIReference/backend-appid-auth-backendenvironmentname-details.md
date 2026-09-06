---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-auth-backendenvironmentname-details.html
---

# Backend appId Auth backendEnvironmentName Details
<a name="backend-appid-auth-backendenvironmentname-details"></a>

The authentication and authorization settings from your Amplify project.

## URI
<a name="backend-appid-auth-backendenvironmentname-details-url"></a>

`/prod/backend/{{appId}}/auth/{{backendEnvironmentName}}/details`

## HTTP methods
<a name="backend-appid-auth-backendenvironmentname-details-http-methods"></a>

### POST
<a name="backend-appid-auth-backendenvironmentname-detailspost"></a>

**Operation ID:** `GetBackendAuth`

Gets a backend auth details.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetBackendAuthRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-auth-backendenvironmentname-detailsoptions"></a>

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
<a name="backend-appid-auth-backendenvironmentname-details-schemas"></a>

### Request bodies
<a name="backend-appid-auth-backendenvironmentname-details-request-examples"></a>

#### POST schema
<a name="backend-appid-auth-backendenvironmentname-details-request-body-post-example"></a>

```
{
  "resourceName": "string"
}
```

### Response bodies
<a name="backend-appid-auth-backendenvironmentname-details-response-examples"></a>

#### GetBackendAuthRespObj schema
<a name="backend-appid-auth-backendenvironmentname-details-response-body-getbackendauthrespobj-example"></a>

```
{
  "resourceConfig": {
    "userPoolConfigs": {
      "userPoolName": "string",
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
      "requiredSignUpAttributes": [
        enum
      ],
      "mfa": {
        "MFAMode": enum,
        "settings": {
        }
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
      "signInMethod": enum
    },
    "authResources": enum,
    "service": enum,
    "identityPoolConfigs": {
      "identityPoolName": "string",
      "unauthenticatedLogin": boolean
    }
  },
  "appId": "string",
  "resourceName": "string",
  "error": "string",
  "backendEnvironmentName": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-auth-backendenvironmentname-details-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-auth-backendenvironmentname-details-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-auth-backendenvironmentname-details-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-auth-backendenvironmentname-details-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-auth-backendenvironmentname-details-properties"></a>

### BadRequestException
<a name="backend-appid-auth-backendenvironmentname-details-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### CreateBackendAuthForgotPasswordConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthforgotpasswordconfig"></a>

**(DEPRECATED)** Describes the forgot password policy for authenticating into the Amplify app.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryMethod | [DeliveryMethod](#backend-appid-auth-backendenvironmentname-details-model-deliverymethod) | True | **(DEPRECATED)** Describes which mode to use (either SMS or email) to deliver messages to app users who want to recover their password. |
| emailSettings | [EmailSettings](#backend-appid-auth-backendenvironmentname-details-model-emailsettings) | False | **(DEPRECATED)** The configuration for the email sent when an app user forgets their password. |
| smsSettings | [SmsSettings](#backend-appid-auth-backendenvironmentname-details-model-smssettings) | False | **(DEPRECATED)** The configuration for the SMS message sent when an app user forgets their password. |

### CreateBackendAuthIdentityPoolConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthidentitypoolconfig"></a>

Describes authorization configurations for the auth resources, configured as a part of your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| identityPoolName | string | True | Name of the Amazon Cognito identity pool used for authorization. |
| unauthenticatedLogin | boolean | True | Set to true or false based on whether you want to enable guest authorization to your Amplify app. |

### CreateBackendAuthMFAConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthmfaconfig"></a>

Describes whether to apply multi-factor authentication policies for your Amazon Cognito user pool configured as a part of your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| MFAMode | string<br />Values: `ON \| OFF \| OPTIONAL` | True | Describes whether MFA should be [`ON`, `OFF`, or `OPTIONAL`] for authentication in your Amplify project. |
| settings | object | False | Describes the configuration settings and methods for your Amplify app users to use MFA. |

### CreateBackendAuthOAuthConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthoauthconfig"></a>

Creates the OAuth configuration for your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainPrefix | string | False | The domain prefix for your Amplify app. |
| oAuthGrantType | string<br />Values: `CODE \| IMPLICIT` | True | The OAuth grant type that you use to allow app users to authenticate from your Amplify app. |
| oAuthScopes | Array of type string<br />Values: `PHONE \| EMAIL \| OPENID \| PROFILE \| AWS_COGNITO_SIGNIN_USER_ADMIN` | True | List of OAuth-related flows used to allow your app users to authenticate from your Amplify app. |
| redirectSignInURIs | Array of type string | True | The redirected URI for signing in to your Amplify app. |
| redirectSignOutURIs | Array of type string | True | Redirect URLs that OAuth uses when a user signs out of an Amplify app. |
| socialProviderSettings | object | False | The settings for using social providers to access your Amplify app. |

### CreateBackendAuthPasswordPolicyConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthpasswordpolicyconfig"></a>

The password policy configuration for the backend to your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| additionalConstraints | Array of type string<br />Values: `REQUIRE_DIGIT \| REQUIRE_LOWERCASE \| REQUIRE_SYMBOL \| REQUIRE_UPPERCASE` | False | Additional constraints for the password used to access the backend of your Amplify project. |
| minimumLength | number | True | The minimum length of the password used to access the backend of your Amplify project. |

### CreateBackendAuthResourceConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthresourceconfig"></a>

Defines the resource configuration when creating an auth resource in your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authResources | string<br />Values: `USER_POOL_ONLY \| IDENTITY_POOL_AND_USER_POOL` | True | Defines whether you want to configure only authentication or both authentication and authorization settings. |
| identityPoolConfigs | [CreateBackendAuthIdentityPoolConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthidentitypoolconfig) | False | Describes the authorization configuration for the Amazon Cognito identity pool, provisioned as a part of your auth resource in the Amplify project. |
| service | string<br />Values: `COGNITO` | True | Defines the service name to use when configuring an authentication resource in your Amplify project. |
| userPoolConfigs | [CreateBackendAuthUserPoolConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthuserpoolconfig) | True | Describes authentication configuration for the Amazon Cognito user pool, provisioned as a part of your auth resource in the Amplify project. |

### CreateBackendAuthUserPoolConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthuserpoolconfig"></a>

Describes the Amazon Cognito user pool configuration for the auth resource to be configured for your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| forgotPassword | [CreateBackendAuthForgotPasswordConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthforgotpasswordconfig) | False | **(DEPRECATED)** Describes the forgotten password policy for your Amazon Cognito user pool, configured as a part of your Amplify project. |
| mfa | [CreateBackendAuthMFAConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthmfaconfig) | False | Describes whether to apply multi-factor authentication policies for your Amazon Cognito user pool configured as a part of your Amplify project. |
| oAuth | [CreateBackendAuthOAuthConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthoauthconfig) | False | Describes the OAuth policy and rules for your Amazon Cognito user pool, configured as a part of your Amplify project. |
| passwordPolicy | [CreateBackendAuthPasswordPolicyConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthpasswordpolicyconfig) | False | Describes the password policy for your Amazon Cognito user pool, configured as a part of your Amplify project. |
| requiredSignUpAttributes | Array of type string<br />Values: `ADDRESS \| BIRTHDATE \| EMAIL \| FAMILY_NAME \| GENDER \| GIVEN_NAME \| LOCALE \| MIDDLE_NAME \| NAME \| NICKNAME \| PHONE_NUMBER \| PICTURE \| PREFERRED_USERNAME \| PROFILE \| UPDATED_AT \| WEBSITE \| ZONE_INFO` | True | The required attributes to sign up new users in the user pool. |
| signInMethod | string<br />Values: `EMAIL \| EMAIL_AND_PHONE_NUMBER \| PHONE_NUMBER \| USERNAME` | True | Describes the sign-in methods that your Amplify app users use to log in using the Amazon Cognito user pool, configured as a part of your Amplify project. |
| userPoolName | string | True | The Amazon Cognito user pool name. |
| verificationMessage | [CreateBackendAuthVerificationMessageConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthverificationmessageconfig) | False | Describes the email or SMS verification message for your Amazon Cognito user pool, configured as a part of your Amplify project. |

### CreateBackendAuthVerificationMessageConfig
<a name="backend-appid-auth-backendenvironmentname-details-model-createbackendauthverificationmessageconfig"></a>

Creates an email or SMS verification message for the auth resource configured for your Amplify project.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryMethod | [DeliveryMethod](#backend-appid-auth-backendenvironmentname-details-model-deliverymethod) | True | The type of verification message to send. |
| emailSettings | [EmailSettings](#backend-appid-auth-backendenvironmentname-details-model-emailsettings) | False | The settings for the email message. |
| smsSettings | [SmsSettings](#backend-appid-auth-backendenvironmentname-details-model-smssettings) | False | The settings for the SMS message. |

### DeliveryMethod
<a name="backend-appid-auth-backendenvironmentname-details-model-deliverymethod"></a>

The type of verification message to send.
+ `EMAIL`
+ `SMS`

### EmailSettings
<a name="backend-appid-auth-backendenvironmentname-details-model-emailsettings"></a>

The settings for the email message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| emailMessage | string | False | The contents of the email message. |
| emailSubject | string | False | The contents of the subject line of the email message. |

### GetBackendAuthReqObj
<a name="backend-appid-auth-backendenvironmentname-details-model-getbackendauthreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceName | string | True | The name of this resource. |

### GetBackendAuthRespObj
<a name="backend-appid-auth-backendenvironmentname-details-model-getbackendauthrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| error | string | False | If the request fails, this error is returned. |
| resourceConfig | [CreateBackendAuthResourceConfig](#backend-appid-auth-backendenvironmentname-details-model-createbackendauthresourceconfig) | False | The resource configuration for authorization requests to the backend of your Amplify project. |
| resourceName | string | False | The name of this resource. |

### InternalServiceException
<a name="backend-appid-auth-backendenvironmentname-details-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-auth-backendenvironmentname-details-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-auth-backendenvironmentname-details-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

### SmsSettings
<a name="backend-appid-auth-backendenvironmentname-details-model-smssettings"></a>

The settings for the SMS message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| smsMessage | string | False | The contents of the SMS message. |

## See also
<a name="backend-appid-auth-backendenvironmentname-details-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBackendAuth
<a name="GetBackendAuth-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/GetBackendAuth)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/GetBackendAuth)
