---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.html
---

# UpdateIdentityProvider
<a name="API_UpdateIdentityProvider"></a>

Modifies the configuration and trust relationship between a third-party identity provider (IdP) and a user pool. Amazon Cognito accepts sign-in with third-party identity providers through managed login and OIDC relying-party libraries. For more information, see [Third-party IdP sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_UpdateIdentityProvider_RequestSyntax"></a>

```
{
   "AttributeMapping": {
      "{{string}}" : "{{string}}"
   },
   "IdpIdentifiers": [ "{{string}}" ],
   "ProviderDetails": {
      "{{string}}" : "{{string}}"
   },
   "ProviderName": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateIdentityProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributeMapping](#API_UpdateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-UpdateIdentityProvider-request-AttributeMapping"></a>
A mapping of IdP attributes to standard and custom user pool attributes. Specify a user pool attribute as the key of the key-value pair, and the IdP attribute claim name as the value.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [IdpIdentifiers](#API_UpdateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-UpdateIdentityProvider-request-IdpIdentifiers"></a>
An array of IdP identifiers, for example `"IdPIdentifiers": [ "MyIdP", "MyIdP2" ]`. Identifiers are friendly names that you can pass in the `idp_identifier` query parameter of requests to the [Authorize endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html) to silently redirect to sign-in with the associated IdP. Identifiers in a domain format also enable the use of [email-address matching with SAML providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managing-saml-idp-naming.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[\w\s+=.@-]+`
Required: No

 ** [ProviderDetails](#API_UpdateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-UpdateIdentityProvider-request-ProviderDetails"></a>
The scopes, URLs, and identifiers for your external identity provider. The following examples describe the provider detail keys for each IdP type. These values and their schema are subject to change. Social IdP `authorize_scopes` values must match the values listed here.
OpenID Connect (OIDC)
Amazon Cognito accepts the following elements when it can't discover endpoint URLs from `oidc_issuer`: `attributes_url`, `authorize_url`, `jwks_uri`, `token_url`.
Create or update request: `"ProviderDetails": { "attributes_request_method": "GET", "attributes_url": "https://auth.example.com/userInfo", "authorize_scopes": "openid profile email", "authorize_url": "https://auth.example.com/authorize", "client_id": "1example23456789", "client_secret": "provider-app-client-secret", "jwks_uri": "https://auth.example.com/.well-known/jwks.json", "oidc_issuer": "https://auth.example.com", "token_url": "https://example.com/token" }`
Describe response: `"ProviderDetails": { "attributes_request_method": "GET", "attributes_url": "https://auth.example.com/userInfo", "attributes_url_add_attributes": "false", "authorize_scopes": "openid profile email", "authorize_url": "https://auth.example.com/authorize", "client_id": "1example23456789", "client_secret": "provider-app-client-secret", "jwks_uri": "https://auth.example.com/.well-known/jwks.json", "oidc_issuer": "https://auth.example.com", "token_url": "https://example.com/token" }`
SAML
Create or update request with Metadata URL: `"ProviderDetails": { "IDPInit": "true", "IDPSignout": "true", "EncryptedResponses" : "true", "MetadataURL": "https://auth.example.com/sso/saml/metadata", "RequestSigningAlgorithm": "rsa-sha256" }`
Create or update request with Metadata file: `"ProviderDetails": { "IDPInit": "true", "IDPSignout": "true", "EncryptedResponses" : "true", "MetadataFile": "[metadata XML]", "RequestSigningAlgorithm": "rsa-sha256" }`
The value of `MetadataFile` must be the plaintext metadata document with all quote (") characters escaped by backslashes.
Describe response: `"ProviderDetails": { "IDPInit": "true", "IDPSignout": "true", "EncryptedResponses" : "true", "ActiveEncryptionCertificate": "[certificate]", "MetadataURL": "https://auth.example.com/sso/saml/metadata", "RequestSigningAlgorithm": "rsa-sha256", "SLORedirectBindingURI": "https://auth.example.com/slo/saml", "SSORedirectBindingURI": "https://auth.example.com/sso/saml" }`
LoginWithAmazon
Create or update request: `"ProviderDetails": { "authorize_scopes": "profile postal_code", "client_id": "amzn1.application-oa2-client.1example23456789", "client_secret": "provider-app-client-secret"`
Describe response: `"ProviderDetails": { "attributes_url": "https://api.amazon.com/user/profile", "attributes_url_add_attributes": "false", "authorize_scopes": "profile postal_code", "authorize_url": "https://www.amazon.com/ap/oa", "client_id": "amzn1.application-oa2-client.1example23456789", "client_secret": "provider-app-client-secret", "token_request_method": "POST", "token_url": "https://api.amazon.com/auth/o2/token" }`
Google
Create or update request: `"ProviderDetails": { "authorize_scopes": "email profile openid", "client_id": "1example23456789.apps.googleusercontent.com", "client_secret": "provider-app-client-secret" }`
Describe response: `"ProviderDetails": { "attributes_url": "https://people.googleapis.com/v1/people/me?personFields=", "attributes_url_add_attributes": "true", "authorize_scopes": "email profile openid", "authorize_url": "https://accounts.google.com/o/oauth2/v2/auth", "client_id": "1example23456789.apps.googleusercontent.com", "client_secret": "provider-app-client-secret", "oidc_issuer": "https://accounts.google.com", "token_request_method": "POST", "token_url": "https://www.googleapis.com/oauth2/v4/token" }`
SignInWithApple
Create or update request: `"ProviderDetails": { "authorize_scopes": "email name", "client_id": "com.example.cognito", "private_key": "1EXAMPLE", "key_id": "2EXAMPLE", "team_id": "3EXAMPLE" }`
Describe response: `"ProviderDetails": { "attributes_url_add_attributes": "false", "authorize_scopes": "email name", "authorize_url": "https://appleid.apple.com/auth/authorize", "client_id": "com.example.cognito", "key_id": "1EXAMPLE", "oidc_issuer": "https://appleid.apple.com", "team_id": "2EXAMPLE", "token_request_method": "POST", "token_url": "https://appleid.apple.com/auth/token" }`
Facebook
Create or update request: `"ProviderDetails": { "api_version": "v17.0", "authorize_scopes": "public_profile, email", "client_id": "1example23456789", "client_secret": "provider-app-client-secret" }`
Describe response: `"ProviderDetails": { "api_version": "v17.0", "attributes_url": "https://graph.facebook.com/v17.0/me?fields=", "attributes_url_add_attributes": "true", "authorize_scopes": "public_profile, email", "authorize_url": "https://www.facebook.com/v17.0/dialog/oauth", "client_id": "1example23456789", "client_secret": "provider-app-client-secret", "token_request_method": "GET", "token_url": "https://graph.facebook.com/v17.0/oauth/access_token" }`
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [ProviderName](#API_UpdateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-UpdateIdentityProvider-request-ProviderName"></a>
The name of the IdP that you want to update. You can pass the identity provider name in the `identity_provider` query parameter of requests to the [Authorize endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html) to silently redirect to sign-in with the associated IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
Required: Yes

 ** [UserPoolId](#API_UpdateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-UpdateIdentityProvider-request-UserPoolId"></a>
The Id of the user pool where you want to update your IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_UpdateIdentityProvider_ResponseSyntax"></a>

```
{
   "IdentityProvider": {
      "AttributeMapping": {
         "string" : "string"
      },
      "CreationDate": number,
      "IdpIdentifiers": [ "string" ],
      "LastModifiedDate": number,
      "ProviderDetails": {
         "string" : "string"
      },
      "ProviderName": "string",
      "ProviderType": "string",
      "UserPoolId": "string"
   }
}
```

## Response Elements
<a name="API_UpdateIdentityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProvider](#API_UpdateIdentityProvider_ResponseSyntax) **   <a name="CognitoUserPools-UpdateIdentityProvider-response-IdentityProvider"></a>
The identity provider details.
Type: [IdentityProviderType](API_IdentityProviderType.md) object

## Errors
<a name="API_UpdateIdentityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
This exception is thrown if two or more modifications are happening concurrently.
 ** message **
The message provided when the concurrent exception is thrown.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UnsupportedIdentityProviderException **
This exception is thrown when the specified identifier isn't supported.
HTTP Status Code: 400

## Examples
<a name="API_UpdateIdentityProvider_Examples"></a>

### Example
<a name="API_UpdateIdentityProvider_Example_1"></a>

The following example request updates an OIDC identity provider. Note that this request sets a manual configuration of the OIDC service endpoints. If the `oidc_issuer` URL has a `.well-known/openid-configuration` endpoint, you can specify `oidc_issuer` alone and auto-discover the remaining endpoints.

#### Sample Request
<a name="API_UpdateIdentityProvider_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.UpdateIdentityProvider
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "AttributeMapping": {
            "email": "idp_email",
            "email_verified": "idp_email_verified",
            "username": "sub"
        },
        "CreationDate": 1.701129701653E9,
        "IdpIdentifiers": [
            "corp",
            "dev"
        ],
        "LastModifiedDate": 1.701129701653E9,
        "ProviderDetails": {
            "attributes_request_method": "GET",
            "attributes_url": "https://example.com/userInfo",
            "attributes_url_add_attributes": "false",
            "authorize_scopes": "openid profile",
            "authorize_url": "https://example.com/authorize",
            "client_id": "idpexampleclient123",
            "client_secret": "idpexamplesecret456",
            "jwks_uri": "https://example.com/.well-known/jwks.json",
            "oidc_issuer": "https://example.com",
            "token_url": "https://example.com/token"
        },
        "ProviderName": "MyOIDCIdP",
        "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdateIdentityProvider_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "IdentityProvider": {
        "AttributeMapping": {
            "email": "idp_email",
            "email_verified": "idp_email_verified",
            "username": "sub"
        },
        "CreationDate": 1701129701.653,
        "IdpIdentifiers": [
            "corp",
            "dev"
        ],
        "LastModifiedDate": 1736444278.211,
        "ProviderDetails": {
            "attributes_request_method": "GET",
            "attributes_url": "https://example.com/userInfo",
            "attributes_url_add_attributes": "false",
            "authorize_scopes": "openid profile",
            "authorize_url": "https://example.com/authorize",
            "client_id": "idpexampleclient123",
            "client_secret": "idpexamplesecret456",
            "jwks_uri": "https://example.com/.well-known/jwks.json",
            "oidc_issuer": "https://example.com",
            "token_url": "https://example.com/token"
        },
        "ProviderName": "MyOIDCIdP",
        "ProviderType": "OIDC",
        "UserPoolId": "us-west-2_EXAMPLE"
    }
}
```

## See Also
<a name="API_UpdateIdentityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/UpdateIdentityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UpdateIdentityProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
