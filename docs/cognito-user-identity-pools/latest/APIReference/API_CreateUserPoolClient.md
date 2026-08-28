---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html
---

# CreateUserPoolClient
<a name="API_CreateUserPoolClient"></a>

Creates an app client in a user pool. This operation sets basic and advanced configuration options.

You can create an app client in the Amazon Cognito console to your preferences and use the output of [DescribeUserPoolClient](API_DescribeUserPoolClient.md) to generate requests from that baseline.

New app clients activate token revocation by default. For more information about revoking tokens, see [RevokeToken](API_RevokeToken.md).

Unlike app clients created in the console, Amazon Cognito doesn't automatically assign a branding style to app clients that you configure with this API operation. Managed login and classic hosted UI pages aren't available for your client until after you apply a branding style.

Apply a branding style with the [CreateManagedLoginBranding](API_CreateManagedLoginBranding.md) operation. For more information, see [Managed login branding](https://docs.aws.amazon.com/cognito/latest/developerguide/managed-login-branding.html).

**Important**
If you don't provide a value for an attribute, Amazon Cognito sets it to its default value.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_CreateUserPoolClient_RequestSyntax"></a>

```
{
   "AccessTokenValidity": {{number}},
   "AllowedOAuthFlows": [ "{{string}}" ],
   "AllowedOAuthFlowsUserPoolClient": {{boolean}},
   "AllowedOAuthScopes": [ "{{string}}" ],
   "AnalyticsConfiguration": {
      "ApplicationArn": "{{string}}",
      "ApplicationId": "{{string}}",
      "ExternalId": "{{string}}",
      "RoleArn": "{{string}}",
      "UserDataShared": {{boolean}}
   },
   "AuthSessionValidity": {{number}},
   "CallbackURLs": [ "{{string}}" ],
   "ClientName": "{{string}}",
   "ClientSecret": "{{string}}",
   "DefaultRedirectURI": "{{string}}",
   "EnablePropagateAdditionalUserContextData": {{boolean}},
   "EnableTokenRevocation": {{boolean}},
   "ExplicitAuthFlows": [ "{{string}}" ],
   "GenerateSecret": {{boolean}},
   "IdTokenValidity": {{number}},
   "LogoutURLs": [ "{{string}}" ],
   "PreventUserExistenceErrors": "{{string}}",
   "ReadAttributes": [ "{{string}}" ],
   "RefreshTokenRotation": {
      "Feature": "{{string}}",
      "RetryGracePeriodSeconds": {{number}}
   },
   "RefreshTokenValidity": {{number}},
   "SupportedIdentityProviders": [ "{{string}}" ],
   "TokenValidityUnits": {
      "AccessToken": "{{string}}",
      "IdToken": "{{string}}",
      "RefreshToken": "{{string}}"
   },
   "UserPoolId": "{{string}}",
   "WriteAttributes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CreateUserPoolClient_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessTokenValidity](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-AccessTokenValidity"></a>
The access token time limit. After this limit expires, your user can't use their access token. To specify the time unit for `AccessTokenValidity` as `seconds`, `minutes`, `hours`, or `days`, set a `TokenValidityUnits` value in your API request.
For example, when you set `AccessTokenValidity` to `10` and `TokenValidityUnits` to `hours`, your user can authorize access with their access token for 10 hours.
The default time unit for `AccessTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.
If you don't specify otherwise in the configuration of your app client, your access tokens are valid for one hour.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

 ** [AllowedOAuthFlows](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-AllowedOAuthFlows"></a>
The OAuth grant types that you want your app client to generate for clients in managed login authentication. To create an app client that generates client credentials grants, you must add `client_credentials` as the only allowed OAuth flow.
code
Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the `/oauth2/token` endpoint.
implicit
Issue the access token, and the ID token when scopes like `openid` and `profile` are requested, directly to your user.
client\_credentials
Issue the access token from the `/oauth2/token` endpoint directly to a non-person user, authorized by a combination of the client ID and client secret.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `code | implicit | client_credentials`
Required: No

 ** [AllowedOAuthFlowsUserPoolClient](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-AllowedOAuthFlowsUserPoolClient"></a>
Set to `true` to use OAuth 2.0 authorization server features in your app client.
This parameter must have a value of `true` before you can configure the following features in your app client.
+  `CallBackURLs`: Callback URLs.
+  `LogoutURLs`: Sign-out redirect URLs.
+  `AllowedOAuthScopes`: OAuth 2.0 scopes.
+  `AllowedOAuthFlows`: Support for authorization code, implicit, and client credentials OAuth 2.0 grants.
To use authorization server features, configure one of these features in the Amazon Cognito console or set `AllowedOAuthFlowsUserPoolClient` to `true` in a `CreateUserPoolClient` or `UpdateUserPoolClient` API request. If you don't set a value for `AllowedOAuthFlowsUserPoolClient` in a request with the AWS CLI or SDKs, it defaults to `false`. When `false`, only SDK-based API sign-in is permitted.
Type: Boolean
Required: No

 ** [AllowedOAuthScopes](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-AllowedOAuthScopes"></a>
The OAuth, OpenID Connect (OIDC), and custom scopes that you want to permit your app client to authorize access with. Scopes govern access control to user pool self-service API operations, user data from the `userInfo` endpoint, and third-party APIs. Scope values include `phone`, `email`, `openid`, and `profile`. The `aws.cognito.signin.user.admin` scope authorizes user self-service operations. Custom scopes with resource servers authorize access to external APIs.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** [AnalyticsConfiguration](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-AnalyticsConfiguration"></a>
The user pool analytics configuration for collecting metrics and sending them to your Amazon Pinpoint campaign.
In AWS Regions where Amazon Pinpoint isn't available, user pools might not have access to analytics or might be configurable with campaigns in the US East (N. Virginia) Region. For more information, see [Using Amazon Pinpoint analytics](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html).
Type: [AnalyticsConfigurationType](API_AnalyticsConfigurationType.md) object
Required: No

 ** [AuthSessionValidity](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-AuthSessionValidity"></a>
Amazon Cognito creates a session token for each API request in an authentication flow. `AuthSessionValidity` is the duration, in minutes, of that session token. Your user pool native user must respond to each authentication challenge before the session expires.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 15.
Required: No

 ** [CallbackURLs](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-CallbackURLs"></a>
A list of allowed redirect, or callback, URLs for managed login authentication. These URLs are the paths where you want to send your users' browsers after they complete authentication with managed login or a third-party IdP. Typically, callback URLs are the home of an application that uses OAuth or OIDC libraries to process authentication outcomes.
A redirect URI must meet the following requirements:
+ Be an absolute URI.
+ Be registered with the authorization server. Amazon Cognito doesn't accept authorization requests with `redirect_uri` values that aren't in the list of `CallbackURLs` that you provide in this parameter.
+ Not include a fragment component.
See [OAuth 2.0 - Redirection Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
Amazon Cognito requires HTTPS over HTTP except for callback URLs to `http://localhost`, `http://127.0.0.1` and `http://[::1]`. These callback URLs are for testing purposes only. You can specify custom TCP ports for your callback URLs.
App callback URLs such as `myapp://example` are also supported.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** [ClientName](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-ClientName"></a>
A friendly name for the app client that you want to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: Yes

 ** [ClientSecret](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-ClientSecret"></a>
A custom client secret that you want to use for the app client. You cannot specify both GenerateSecret as true and provide a ClientSecret value.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 64.
Pattern: `[\w+]+`
Required: No

 ** [DefaultRedirectURI](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-DefaultRedirectURI"></a>
The default redirect URI. In app clients with one assigned IdP, replaces `redirect_uri` in authentication requests. Must be in the `CallbackURLs` list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** [EnablePropagateAdditionalUserContextData](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-EnablePropagateAdditionalUserContextData"></a>
When `true`, your application can include additional `UserContextData` in authentication requests. This data includes the IP address, and contributes to analysis by threat protection features. For more information about propagation of user context data, see [Adding session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint). If you don’t include this parameter, you can't send the source IP address to Amazon Cognito threat protection features. You can only activate `EnablePropagateAdditionalUserContextData` in an app client that has a client secret.
Type: Boolean
Required: No

 ** [EnableTokenRevocation](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-EnableTokenRevocation"></a>
Activates or deactivates [token revocation](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html) in the target app client.
Revoke tokens with [RevokeToken](API_RevokeToken.md).
If you don't include this parameter, token revocation is automatically activated for the new user pool client.
Type: Boolean
Required: No

 ** [ExplicitAuthFlows](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-ExplicitAuthFlows"></a>
The [authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html) that you want your user pool client to support. For each app client in your user pool, you can sign in your users with any combination of one or more flows, including with a user name and Secure Remote Password (SRP), a user name and password, or a custom authentication process that you define with Lambda functions.
If you don't specify a value for `ExplicitAuthFlows`, your app client supports `ALLOW_REFRESH_TOKEN_AUTH`, `ALLOW_USER_SRP_AUTH`, and `ALLOW_CUSTOM_AUTH`.
The values for authentication flow options include the following.
+  `ALLOW_USER_AUTH`: Enable selection-based sign-in with `USER_AUTH`. This setting covers username-password, secure remote password (SRP), passwordless, and passkey authentication. This authentiation flow can do username-password and SRP authentication without other `ExplicitAuthFlows` permitting them. For example users can complete an SRP challenge through `USER_AUTH` without the flow `USER_SRP_AUTH` being active for the app client. This flow doesn't include `CUSTOM_AUTH`.

  To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
+  `ALLOW_ADMIN_USER_PASSWORD_AUTH`: Enable admin based user password authentication flow `ADMIN_USER_PASSWORD_AUTH`. This setting replaces the `ADMIN_NO_SRP_AUTH` setting. With this authentication flow, your app passes a user name and password to Amazon Cognito in the request, instead of using the Secure Remote Password (SRP) protocol to securely transmit the password.
+  `ALLOW_CUSTOM_AUTH`: Enable Lambda trigger based authentication.
+  `ALLOW_USER_PASSWORD_AUTH`: Enable user password-based authentication. In this flow, Amazon Cognito receives the password in the request instead of using the SRP protocol to verify passwords.
+  `ALLOW_USER_SRP_AUTH`: Enable SRP-based authentication.
+  `ALLOW_REFRESH_TOKEN_AUTH`: Enable authflow to refresh tokens.
In some environments, you will see the values `ADMIN_NO_SRP_AUTH`, `CUSTOM_AUTH_FLOW_ONLY`, or `USER_PASSWORD_AUTH`. You can't assign these legacy `ExplicitAuthFlows` values to user pool clients at the same time as values that begin with `ALLOW_`, like `ALLOW_USER_SRP_AUTH`.
Type: Array of strings
Valid Values: `ADMIN_NO_SRP_AUTH | CUSTOM_AUTH_FLOW_ONLY | USER_PASSWORD_AUTH | ALLOW_ADMIN_USER_PASSWORD_AUTH | ALLOW_CUSTOM_AUTH | ALLOW_USER_PASSWORD_AUTH | ALLOW_USER_SRP_AUTH | ALLOW_REFRESH_TOKEN_AUTH | ALLOW_USER_AUTH`
Required: No

 ** [GenerateSecret](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-GenerateSecret"></a>
When `true`, generates a client secret for the app client. Client secrets are used with server-side and machine-to-machine applications. Client secrets are automatically generated; you can't specify a secret value. For more information, see [App client types](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html#user-pool-settings-client-app-client-types).
Type: Boolean
Required: No

 ** [IdTokenValidity](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-IdTokenValidity"></a>
The ID token time limit. After this limit expires, your user can't use their ID token. To specify the time unit for `IdTokenValidity` as `seconds`, `minutes`, `hours`, or `days`, set a `TokenValidityUnits` value in your API request.
For example, when you set `IdTokenValidity` as `10` and `TokenValidityUnits` as `hours`, your user can authenticate their session with their ID token for 10 hours.
The default time unit for `IdTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.
If you don't specify otherwise in the configuration of your app client, your ID tokens are valid for one hour.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

 ** [LogoutURLs](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-LogoutURLs"></a>
A list of allowed logout URLs for managed login authentication. When you pass `logout_uri` and `client_id` parameters to `/logout`, Amazon Cognito signs out your user and redirects them to the logout URL. This parameter describes the URLs that you want to be the permitted targets of `logout_uri`. A typical use of these URLs is when a user selects "Sign out" and you redirect them to your public homepage. For more information, see [Logout endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/logout-endpoint.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** [PreventUserExistenceErrors](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-PreventUserExistenceErrors"></a>
When `ENABLED`, suppresses messages that might indicate a valid user exists when someone attempts sign-in. This parameters sets your preference for the errors and responses that you want Amazon Cognito APIs to return during authentication, account confirmation, and password recovery when the user doesn't exist in the user pool. When set to `ENABLED` and the user doesn't exist, authentication returns an error indicating either the username or password was incorrect. Account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to `LEGACY`, those APIs return a `UserNotFoundException` exception if the user doesn't exist in the user pool.
Defaults to `LEGACY`.
This setting affects the behavior of the following API operations.
+  [AdminInitiateAuth](API_AdminInitiateAuth.md)
+  [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md)
+  [InitiateAuth](API_InitiateAuth.md)
+  [RespondToAuthChallenge](API_RespondToAuthChallenge.md)
+  [ForgotPassword](API_ForgotPassword.md)
+  [ConfirmForgotPassword](API_ConfirmForgotPassword.md)
+  [ConfirmSignUp](API_ConfirmSignUp.md)
+  [ResendConfirmationCode](API_ResendConfirmationCode.md)
Type: String
Valid Values: `LEGACY | ENABLED`
Required: No

 ** [ReadAttributes](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-ReadAttributes"></a>
The list of user attributes that you want your app client to have read access to. After your user authenticates in your app, their access token authorizes them to read their own attribute value for any attribute in this list.
An example of this kind of activity is when your user selects a link to view their profile information. Your app makes a [GetUser](API_GetUser.md) API request to retrieve and display your user's profile data.
When you don't specify the `ReadAttributes` for your app client, your app can read the values of `email_verified`, `phone_number_verified`, and the standard attributes of your user pool. When your user pool app client has read access to these default attributes, `ReadAttributes` doesn't return any information. Amazon Cognito only populates `ReadAttributes` in the API response if you have specified your own custom set of read attributes.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [RefreshTokenRotation](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-RefreshTokenRotation"></a>
The configuration of your app client for refresh token rotation. When enabled, your app client issues new ID, access, and refresh tokens when users renew their sessions with refresh tokens. When disabled, token refresh issues only ID and access tokens.
Refresh token rotation must be completed with [GetTokensFromRefreshToken](API_GetTokensFromRefreshToken.md). With refresh token rotation disabled, you can complete token refresh with `GetTokensFromRefreshToken` and with `REFRESH_TOKEN_AUTH` in [InitiateAuth:AuthFlow](API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthFlow) and [AdminInitiateAuth:AuthFlow](API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-AuthFlow).
Type: [RefreshTokenRotationType](API_RefreshTokenRotationType.md) object
Required: No

 ** [RefreshTokenValidity](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-RefreshTokenValidity"></a>
The refresh token time limit. After this limit expires, your user can't use their refresh token. To specify the time unit for `RefreshTokenValidity` as `seconds`, `minutes`, `hours`, or `days`, set a `TokenValidityUnits` value in your API request.
For example, when you set `RefreshTokenValidity` as `10` and `TokenValidityUnits` as `days`, your user can refresh their session and retrieve new access and ID tokens for 10 days.
The default time unit for `RefreshTokenValidity` in an API request is days. You can't set `RefreshTokenValidity` to 0. If you do, Amazon Cognito overrides the value with the default value of 30 days. *Valid range* is displayed below in seconds.
If you don't specify otherwise in the configuration of your app client, your refresh tokens are valid for 30 days.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 315360000.
Required: No

 ** [SupportedIdentityProviders](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-SupportedIdentityProviders"></a>
A list of provider names for the identity providers (IdPs) that are supported on this client. The following are supported: `COGNITO`, `Facebook`, `Google`, `SignInWithApple`, and `LoginWithAmazon`. You can also specify the names that you configured for the SAML and OIDC IdPs in your user pool, for example `MySAMLIdP` or `MyOIDCIdP`.
This parameter sets the IdPs that [managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html) will display on the login page for your app client. The removal of `COGNITO` from this list doesn't prevent authentication operations for local users with the user pools API in an AWS SDK. The only way to prevent SDK-based authentication is to block access with a [AWS WAF rule](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: No

 ** [TokenValidityUnits](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-TokenValidityUnits"></a>
The units that validity times are represented in. The default unit for refresh tokens is days, and the default for ID and access tokens are hours.
Type: [TokenValidityUnitsType](API_TokenValidityUnitsType.md) object
Required: No

 ** [UserPoolId](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-UserPoolId"></a>
The ID of the user pool where you want to create an app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

 ** [WriteAttributes](#API_CreateUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-request-WriteAttributes"></a>
The list of user attributes that you want your app client to have write access to. After your user authenticates in your app, their access token authorizes them to set or modify their own attribute value for any attribute in this list.
An example of this kind of activity is when you present your user with a form to update their profile information and they change their last name. Your app then makes an [UpdateUserAttributes](API_UpdateUserAttributes.md) API request and sets `family_name` to the new value.
When you don't specify the `WriteAttributes` for your app client, your app can write the values of the Standard attributes of your user pool. When your user pool has write access to these default attributes, `WriteAttributes` doesn't return any information. Amazon Cognito only populates `WriteAttributes` in the API response if you have specified your own custom set of write attributes.
If your app client allows users to sign in through an IdP, this array must include all attributes that you have mapped to IdP attributes. Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If your app client does not have write access to a mapped attribute, Amazon Cognito throws an error when it tries to update the attribute. For more information, see [Specifying IdP Attribute Mappings for Your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_CreateUserPoolClient_ResponseSyntax"></a>

```
{
   "UserPoolClient": {
      "AccessTokenValidity": number,
      "AllowedOAuthFlows": [ "string" ],
      "AllowedOAuthFlowsUserPoolClient": boolean,
      "AllowedOAuthScopes": [ "string" ],
      "AnalyticsConfiguration": {
         "ApplicationArn": "string",
         "ApplicationId": "string",
         "ExternalId": "string",
         "RoleArn": "string",
         "UserDataShared": boolean
      },
      "AuthSessionValidity": number,
      "CallbackURLs": [ "string" ],
      "ClientId": "string",
      "ClientName": "string",
      "ClientSecret": "string",
      "CreationDate": number,
      "DefaultRedirectURI": "string",
      "EnablePropagateAdditionalUserContextData": boolean,
      "EnableTokenRevocation": boolean,
      "ExplicitAuthFlows": [ "string" ],
      "IdTokenValidity": number,
      "LastModifiedDate": number,
      "LogoutURLs": [ "string" ],
      "PreventUserExistenceErrors": "string",
      "ReadAttributes": [ "string" ],
      "RefreshTokenRotation": {
         "Feature": "string",
         "RetryGracePeriodSeconds": number
      },
      "RefreshTokenValidity": number,
      "SupportedIdentityProviders": [ "string" ],
      "TokenValidityUnits": {
         "AccessToken": "string",
         "IdToken": "string",
         "RefreshToken": "string"
      },
      "UserPoolId": "string",
      "WriteAttributes": [ "string" ]
   }
}
```

## Response Elements
<a name="API_CreateUserPoolClient_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserPoolClient](#API_CreateUserPoolClient_ResponseSyntax) **   <a name="CognitoUserPools-CreateUserPoolClient-response-UserPoolClient"></a>
The details of the new app client.
Type: [UserPoolClientType](API_UserPoolClientType.md) object

## Errors
<a name="API_CreateUserPoolClient_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature you attempted to configure isn't available in your current feature plan.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidOAuthFlowException **
This exception is thrown when the specified OAuth flow is not valid.
HTTP Status Code: 400

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** ScopeDoesNotExistException **
This exception is thrown when the specified scope doesn't exist.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_CreateUserPoolClient_Examples"></a>

### Example
<a name="API_CreateUserPoolClient_Example_1"></a>

The following example creates an app client with all configurable properties set to an example value. The resulting user pool client connects to an analytics client, allows sign-in with username and password, and has two external identity providers associated with it.

#### Sample Request
<a name="API_CreateUserPoolClient_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateUserPoolClient
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "AccessTokenValidity": 6,
    "AllowedOAuthFlows": [
        "code"
    ],
    "AllowedOAuthFlowsUserPoolClient": true,
    "AllowedOAuthScopes": [
        "aws.cognito.signin.user.admin",
        "openid"
    ],
    "AnalyticsConfiguration": {
        "ApplicationId": "d70b2ba36a8c4dc5a04a0451a31a1e12",
        "ExternalId": "my-external-id",
        "RoleArn": "arn:aws:iam::123456789012:role/test-cognitouserpool-role",
        "UserDataShared": true
    },
    "CallbackURLs": [
        "https://example.com",
        "http://localhost",
        "myapp://example"
    ],
    "ClientName": "my-test-app-client",
    "DefaultRedirectURI": "https://example.com",
    "ExplicitAuthFlows": [
        "ALLOW_USER_AUTH",
        "ALLOW_ADMIN_USER_PASSWORD_AUTH",
        "ALLOW_USER_PASSWORD_AUTH",
        "ALLOW_REFRESH_TOKEN_AUTH"
    ],
    "GenerateSecret": true,
    "IdTokenValidity": 6,
    "LogoutURLs": [
        "https://example.com/logout"
    ],
    "PreventUserExistenceErrors": "ENABLED",
    "ReadAttributes": [
        "email",
        "address",
        "preferred_username"
    ],
    "RefreshTokenValidity": 6,
    "SupportedIdentityProviders": [
        "SignInWithApple",
        "MySSO"
    ],
    "TokenValidityUnits": {
        "AccessToken": "hours",
        "IdToken": "minutes",
        "RefreshToken": "days"
    },
    "UserPoolId": "us-east-1_EXAMPLE",
    "WriteAttributes": [
        "family_name",
        "email"
    ]
}
```

#### Sample Response
<a name="API_CreateUserPoolClient_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
      "UserPoolClient": {
        "AccessTokenValidity": 6,
        "AllowedOAuthFlows": [
          "code"
        ],
        "AllowedOAuthFlowsUserPoolClient": true,
        "AllowedOAuthScopes": [
          "aws.cognito.signin.user.admin",
          "openid"
        ],
        "AnalyticsConfiguration": {
          "ApplicationId": "d70b2ba36a8c4dc5a04a0451a31a1e12",
          "ExternalId": "my-external-id",
          "RoleArn": "arn:aws:iam::123456789012:role/test-cognitouserpool-role",
          "UserDataShared": true
        },
        "AuthSessionValidity": 3,
        "CallbackURLs": [
          "https://example.com",
          "http://localhost",
          "myapp://example"
        ],
        "ClientId": "1example23456789",
        "ClientName": "my-test-app-client",
        "ClientSecret": "13ka4h7u28d9oo44tqpq9djqsfvhvu8rk4d2ighvpu0k8fj1c2r9",
        "CreationDate": 1689885426.107,
        "DefaultRedirectURI": "https://example.com",
        "EnablePropagateAdditionalUserContextData": false,
        "EnableTokenRevocation": true,
        "ExplicitAuthFlows": [
          "ALLOW_USER_AUTH",
          "ALLOW_USER_PASSWORD_AUTH",
          "ALLOW_ADMIN_USER_PASSWORD_AUTH",
          "ALLOW_REFRESH_TOKEN_AUTH"
        ],
        "IdTokenValidity": 6,
        "LastModifiedDate": 1689885426.107,
        "LogoutURLs": [
          "https://example.com/logout"
        ],
        "PreventUserExistenceErrors": "ENABLED",
        "ReadAttributes": [
          "address",
          "preferred_username",
          "email"
        ],
        "RefreshTokenValidity": 6,
        "SupportedIdentityProviders": [
          "SignInWithApple",
          "MySSO"
        ],
        "TokenValidityUnits": {
          "AccessToken": "hours",
          "IdToken": "minutes",
          "RefreshToken": "days"
        },
        "UserPoolId": "us-east-1_EXAMPLE",
        "WriteAttributes": [
          "family_name",
          "email"
        ]
      }
}
```

## See Also
<a name="API_CreateUserPoolClient_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CreateUserPoolClient)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CreateUserPoolClient)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
