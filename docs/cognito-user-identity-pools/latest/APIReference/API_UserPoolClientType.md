---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolClientType.html
---

# UserPoolClientType
<a name="API_UserPoolClientType"></a>

The configuration of a user pool client.

This data type is a request parameter of [CreateUserPoolClient](API_CreateUserPoolClient.md) and [UpdateUserPoolClient](API_UpdateUserPoolClient.md), and a response parameter of [DescribeUserPoolClient](API_DescribeUserPoolClient.md).

## Contents
<a name="API_UserPoolClientType_Contents"></a>

 ** AccessTokenValidity **   <a name="CognitoUserPools-Type-UserPoolClientType-AccessTokenValidity"></a>
The access token time limit. After this limit expires, your user can't use their access token. To specify the time unit for `AccessTokenValidity` as `seconds`, `minutes`, `hours`, or `days`, set a `TokenValidityUnits` value in your API request.
For example, when you set `AccessTokenValidity` to `10` and `TokenValidityUnits` to `hours`, your user can authorize access with their access token for 10 hours.
The default time unit for `AccessTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.
If you don't specify otherwise in the configuration of your app client, your access tokens are valid for one hour.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

 ** AllowedOAuthFlows **   <a name="CognitoUserPools-Type-UserPoolClientType-AllowedOAuthFlows"></a>
The OAuth grant types that you want your app client to generate. To create an app client that generates client credentials grants, you must add `client_credentials` as the only allowed OAuth flow.
code
Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the `/oauth2/token` endpoint.
implicit
Issue the access token (and, optionally, ID token, based on scopes) directly to your user.
client\_credentials
Issue the access token from the `/oauth2/token` endpoint directly to a non-person user using a combination of the client ID and client secret.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `code | implicit | client_credentials`
Required: No

 ** AllowedOAuthFlowsUserPoolClient **   <a name="CognitoUserPools-Type-UserPoolClientType-AllowedOAuthFlowsUserPoolClient"></a>
Set to `true` to use OAuth 2.0 authorization server features in your app client.
This parameter must have a value of `true` before you can configure the following features in your app client.
+  `CallBackURLs`: Callback URLs.
+  `LogoutURLs`: Sign-out redirect URLs.
+  `AllowedOAuthScopes`: OAuth 2.0 scopes.
+  `AllowedOAuthFlows`: Support for authorization code, implicit, and client credentials OAuth 2.0 grants.
To use authorization server features, configure one of these features in the Amazon Cognito console or set `AllowedOAuthFlowsUserPoolClient` to `true` in a `CreateUserPoolClient` or `UpdateUserPoolClient` API request. If you don't set a value for `AllowedOAuthFlowsUserPoolClient` in a request with the AWS CLI or SDKs, it defaults to `false`. When `false`, only SDK-based API sign-in is permitted.
Type: Boolean
Required: No

 ** AllowedOAuthScopes **   <a name="CognitoUserPools-Type-UserPoolClientType-AllowedOAuthScopes"></a>
The OAuth 2.0 scopes that you want your app client to support. Can include standard OAuth scopes like `phone`, `email`, `openid`, and `profile`. Can also include the `aws.cognito.signin.user.admin` scope that authorizes user profile self-service operations and custom scopes from resource servers.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** AnalyticsConfiguration **   <a name="CognitoUserPools-Type-UserPoolClientType-AnalyticsConfiguration"></a>
The user pool analytics configuration for collecting metrics and sending them to your Amazon Pinpoint campaign.
In AWS Regions where Amazon Pinpoint isn't available, user pools only support sending events to Amazon Pinpoint projects in AWS Region us-east-1. In Regions where Amazon Pinpoint is available, user pools support sending events to Amazon Pinpoint projects within that same Region.
Type: [AnalyticsConfigurationType](API_AnalyticsConfigurationType.md) object
Required: No

 ** AuthSessionValidity **   <a name="CognitoUserPools-Type-UserPoolClientType-AuthSessionValidity"></a>
Amazon Cognito creates a session token for each API request in an authentication flow. `AuthSessionValidity` is the duration, in minutes, of that session token. Your user pool native user must respond to each authentication challenge before the session expires.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 15.
Required: No

 ** CallbackURLs **   <a name="CognitoUserPools-Type-UserPoolClientType-CallbackURLs"></a>
A list of allowed redirect (callback) URLs for the IdPs.
A redirect URI must:
+ Be an absolute URI.
+ Be registered with the authorization server.
+ Not include a fragment component.
See [OAuth 2.0 - Redirection Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
Amazon Cognito requires HTTPS over HTTP for callback URLs to `http://localhost`, `http://127.0.0.1` and `http://[::1]`. These callback URLs are for testing purposes only. You can specify custom TCP ports for your callback URLs.
App callback URLs such as myapp://example are also supported.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** ClientId **   <a name="CognitoUserPools-Type-UserPoolClientType-ClientId"></a>
The ID of the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: No

 ** ClientName **   <a name="CognitoUserPools-Type-UserPoolClientType-ClientName"></a>
The name of the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: No

 ** ClientSecret **   <a name="CognitoUserPools-Type-UserPoolClientType-ClientSecret"></a>
The app client secret.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 64.
Pattern: `[\w+]+`
Required: No

 ** CreationDate **   <a name="CognitoUserPools-Type-UserPoolClientType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** DefaultRedirectURI **   <a name="CognitoUserPools-Type-UserPoolClientType-DefaultRedirectURI"></a>
The default redirect URI. Must be in the `CallbackURLs` list.
A redirect URI must:
+ Be an absolute URI.
+ Be registered with the authorization server.
+ Not include a fragment component.
See [OAuth 2.0 - Redirection Endpoint](https://tools.ietf.org/html/rfc6749#section-3.1.2).
Amazon Cognito requires HTTPS over HTTP for callback URLs to `http://localhost`, `http://127.0.0.1` and `http://[::1]`. These callback URLs are for testing purposes only. You can specify custom TCP ports for your callback URLs.
App callback URLs such as myapp://example are also supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** EnablePropagateAdditionalUserContextData **   <a name="CognitoUserPools-Type-UserPoolClientType-EnablePropagateAdditionalUserContextData"></a>
When `EnablePropagateAdditionalUserContextData` is true, Amazon Cognito accepts an `IpAddress` value that you send in the `UserContextData` parameter. The `UserContextData` parameter sends information to Amazon Cognito threat protection for risk analysis. You can send `UserContextData` when you sign in Amazon Cognito native users with the `InitiateAuth` and `RespondToAuthChallenge` API operations.
When `EnablePropagateAdditionalUserContextData` is false, you can't send your user's source IP address to Amazon Cognito threat protection with unauthenticated API operations. `EnablePropagateAdditionalUserContextData` doesn't affect whether you can send a source IP address in a `ContextData` parameter with the authenticated API operations `AdminInitiateAuth` and `AdminRespondToAuthChallenge`.
You can only activate `EnablePropagateAdditionalUserContextData` in an app client that has a client secret. For more information about propagation of user context data, see [Adding user device and session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint).
Type: Boolean
Required: No

 ** EnableTokenRevocation **   <a name="CognitoUserPools-Type-UserPoolClientType-EnableTokenRevocation"></a>
Indicates whether token revocation is activated for the user pool client. When you create a new user pool client, token revocation is activated by default.
For more information about revoking tokens, see [RevokeToken](API_RevokeToken.md).
Type: Boolean
Required: No

 ** ExplicitAuthFlows **   <a name="CognitoUserPools-Type-UserPoolClientType-ExplicitAuthFlows"></a>
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

 ** IdTokenValidity **   <a name="CognitoUserPools-Type-UserPoolClientType-IdTokenValidity"></a>
The ID token time limit. After this limit expires, your user can't use their ID token. To specify the time unit for `IdTokenValidity` as `seconds`, `minutes`, `hours`, or `days`, set a `TokenValidityUnits` value in your API request.
For example, when you set `IdTokenValidity` as `10` and `TokenValidityUnits` as `hours`, your user can authenticate their session with their ID token for 10 hours.
The default time unit for `IdTokenValidity` in an API request is hours. *Valid range* is displayed below in seconds.
If you don't specify otherwise in the configuration of your app client, your ID tokens are valid for one hour.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-UserPoolClientType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** LogoutURLs **   <a name="CognitoUserPools-Type-UserPoolClientType-LogoutURLs"></a>
A list of allowed logout URLs for the IdPs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** PreventUserExistenceErrors **   <a name="CognitoUserPools-Type-UserPoolClientType-PreventUserExistenceErrors"></a>
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

 ** ReadAttributes **   <a name="CognitoUserPools-Type-UserPoolClientType-ReadAttributes"></a>
The list of user attributes that you want your app client to have read access to. After your user authenticates in your app, their access token authorizes them to read their own attribute value for any attribute in this list.
An example of this kind of activity is when your user selects a link to view their profile information. Your app makes a [GetUser](API_GetUser.md) API request to retrieve and display your user's profile data.
When you don't specify the `ReadAttributes` for your app client, your app can read the values of `email_verified`, `phone_number_verified`, and the standard attributes of your user pool. When your user pool app client has read access to these default attributes, `ReadAttributes` doesn't return any information. Amazon Cognito only populates `ReadAttributes` in the API response if you have specified your own custom set of read attributes.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** RefreshTokenRotation **   <a name="CognitoUserPools-Type-UserPoolClientType-RefreshTokenRotation"></a>
The configuration of your app client for refresh token rotation. When enabled, your app client issues new ID, access, and refresh tokens when users renew their sessions with refresh tokens. When disabled, token refresh issues only ID and access tokens.
Refresh token rotation must be completed with [GetTokensFromRefreshToken](API_GetTokensFromRefreshToken.md). With refresh token rotation disabled, you can complete token refresh with `GetTokensFromRefreshToken` and with `REFRESH_TOKEN_AUTH` in [InitiateAuth:AuthFlow](API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthFlow) and [AdminInitiateAuth:AuthFlow](API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-AuthFlow).
Type: [RefreshTokenRotationType](API_RefreshTokenRotationType.md) object
Required: No

 ** RefreshTokenValidity **   <a name="CognitoUserPools-Type-UserPoolClientType-RefreshTokenValidity"></a>
The refresh token time limit. After this limit expires, your user can't use their refresh token. To specify the time unit for `RefreshTokenValidity` as `seconds`, `minutes`, `hours`, or `days`, set a `TokenValidityUnits` value in your API request.
For example, when you set `RefreshTokenValidity` as `10` and `TokenValidityUnits` as `days`, your user can refresh their session and retrieve new access and ID tokens for 10 days.
The default time unit for `RefreshTokenValidity` in an API request is days. You can't set `RefreshTokenValidity` to 0. If you do, Amazon Cognito overrides the value with the default value of 30 days. *Valid range* is displayed below in seconds.
If you don't specify otherwise in the configuration of your app client, your refresh tokens are valid for 30 days.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 315360000.
Required: No

 ** SupportedIdentityProviders **   <a name="CognitoUserPools-Type-UserPoolClientType-SupportedIdentityProviders"></a>
A list of provider names for the identity providers (IdPs) that are supported on this client. The following are supported: `COGNITO`, `Facebook`, `Google`, `SignInWithApple`, and `LoginWithAmazon`. You can also specify the names that you configured for the SAML and OIDC IdPs in your user pool, for example `MySAMLIdP` or `MyOIDCIdP`.
This parameter sets the IdPs that [managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html) will display on the login page for your app client. The removal of `COGNITO` from this list doesn't prevent authentication operations for local users with the user pools API in an AWS SDK. The only way to prevent SDK-based authentication is to block access with a [AWS WAF rule](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: No

 ** TokenValidityUnits **   <a name="CognitoUserPools-Type-UserPoolClientType-TokenValidityUnits"></a>
The time units that, with `IdTokenValidity`, `AccessTokenValidity`, and `RefreshTokenValidity`, set and display the duration of ID, access, and refresh tokens for an app client. You can assign a separate token validity unit to each type of token.
Type: [TokenValidityUnitsType](API_TokenValidityUnitsType.md) object
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-UserPoolClientType-UserPoolId"></a>
The ID of the user pool associated with the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

 ** WriteAttributes **   <a name="CognitoUserPools-Type-UserPoolClientType-WriteAttributes"></a>
The list of user attributes that you want your app client to have write access to. After your user authenticates in your app, their access token authorizes them to set or modify their own attribute value for any attribute in this list.
An example of this kind of activity is when you present your user with a form to update their profile information and they change their last name. Your app then makes an [UpdateUserAttributes](API_UpdateUserAttributes.md) API request and sets `family_name` to the new value.
When you don't specify the `WriteAttributes` for your app client, your app can write the values of the Standard attributes of your user pool. When your user pool has write access to these default attributes, `WriteAttributes` doesn't return any information. Amazon Cognito only populates `WriteAttributes` in the API response if you have specified your own custom set of write attributes.
If your app client allows users to sign in through an IdP, this array must include all attributes that you have mapped to IdP attributes. Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If your app client does not have write access to a mapped attribute, Amazon Cognito throws an error when it tries to update the attribute. For more information, see [Specifying IdP Attribute Mappings for Your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_UserPoolClientType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolClientType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolClientType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolClientType)
