---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DcrConfigurationType.html
---

# DcrConfigurationType

The dynamic client registration configuration for a user pool. Dynamic client registration lets applications register their own app clients at runtime through the registration endpoint of your user pool domain. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

Applications register app clients at the `/oauth2/register` endpoint of your user pool domain. In authenticated registration, the application sends an access token from your user pool that has the `aws.cognito/dcr/register` scope. In open registration, the application doesn't send a token.

When you include this configuration in an `UpdateUserPool` request, Amazon Cognito replaces the existing configuration with the one that you provide.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_DcrConfigurationType_Contents"></a>

 ** AllowedScopes **   <a name="CognitoUserPools-Type-DcrConfigurationType-AllowedScopes"></a>
The scopes that an app client created through dynamic client registration can request, in addition to the standard OpenID Connect (OIDC) scopes. You can include custom scopes from your resource servers and `aws.cognito.signin.user.admin`. Registered app clients can request the OIDC scopes `openid`, `email`, `phone`, and `profile` without listing them here. If you don't set this value, registered app clients can request only the OIDC scopes. A registered app client can't request the `aws.cognito/dcr/register` scope, even if you include it in this list.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** AuthenticatedGrantTypes **   <a name="CognitoUserPools-Type-DcrConfigurationType-AuthenticatedGrantTypes"></a>
The OAuth grant types that an app client created through authenticated registration can request. If you don't set this value, authenticated registration permits the `code` and `client_credentials` grant types. If you set an empty list, Amazon Cognito rejects authenticated registration requests. Dynamic client registration supports the following values. Amazon Cognito accepts `implicit` in this list but ignores it.
code
Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the `/oauth2/token` endpoint.
client\_credentials
Issue the access token from the `/oauth2/token` endpoint directly to a non-person user using a combination of the client ID and client secret.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `code | implicit | client_credentials`
Required: No

 ** EnableStatus **   <a name="CognitoUserPools-Type-DcrConfigurationType-EnableStatus"></a>
Specifies whether dynamic client registration is turned on for the user pool. If you provide a dynamic client registration configuration without this value, Amazon Cognito turns dynamic client registration on.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** OpenDcrEnabled **   <a name="CognitoUserPools-Type-DcrConfigurationType-OpenDcrEnabled"></a>
Specifies whether open registration is turned on. When open registration is on, applications can register app clients without an initial access token. The default value is `false`.
Type: Boolean
Required: No

 ** OpenDcrGrantTypes **   <a name="CognitoUserPools-Type-DcrConfigurationType-OpenDcrGrantTypes"></a>
The OAuth grant types that an app client created through open registration can request. If you don't set this value, open registration permits only the `code` grant type. If you set an empty list, Amazon Cognito rejects open registration requests. If you add `client_credentials`, anyone can register an app client that requests machine-to-machine (M2M) access tokens, and you pay for the M2M token requests that those app clients make. Dynamic client registration supports the following values. Amazon Cognito accepts `implicit` in this list but ignores it.
code
Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the `/oauth2/token` endpoint.
client\_credentials
Issue the access token from the `/oauth2/token` endpoint directly to a non-person user using a combination of the client ID and client secret.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `code | implicit | client_credentials`
Required: No

## See Also
<a name="API_DcrConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DcrConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DcrConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DcrConfigurationType)
