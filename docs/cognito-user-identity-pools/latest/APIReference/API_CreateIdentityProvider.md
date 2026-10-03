---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html
---

# CreateIdentityProvider
<a name="API_CreateIdentityProvider"></a>

Adds a configuration and trust relationship between a third-party identity provider (IdP) and a user pool. Amazon Cognito accepts sign-in with third-party identity providers through managed login and OIDC relying-party libraries. For more information, see [Third-party IdP sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_CreateIdentityProvider_RequestSyntax"></a>

```
{
   "AcrMapping": {
      "{{string}}" : "{{string}}"
   },
   "AttributeMapping": {
      "{{string}}" : "{{string}}"
   },
   "IdpIdentifiers": [ "{{string}}" ],
   "ProviderDetails": {
      "{{string}}" : "{{string}}"
   },
   "ProviderName": "{{string}}",
   "ProviderType": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateIdentityProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcrMapping](#API_CreateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-request-AcrMapping"></a>
A mapping between the authentication context class reference (ACR) levels of your user pool and the ACR values of the external OpenID Connect (OIDC) identity provider (IdP). The map is keyed by level, from `Level1` through `Level4`, and each value is the ACR value that the IdP uses for the corresponding level. Amazon Cognito uses this mapping to translate a requested user pool ACR level to the value that the IdP expects, and to map an ACR value that the IdP returns back to a user pool level. When the IdP returns an ACR value that isn't mapped, Amazon Cognito resolves it to the lowest level. Only OIDC IdPs support ACR mapping.
Setting `AcrMapping` is available in all feature plans. It isn't restricted to the Essentials or Plus feature plan.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 4 items.
Key Pattern: `Level[1-4]`
Value Length Constraints: Minimum length of 1. Maximum length of 64.
Value Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: No

 ** [AttributeMapping](#API_CreateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-request-AttributeMapping"></a>
A mapping of IdP attributes to standard and custom user pool attributes. Specify a user pool attribute as the key of the key-value pair, and the IdP attribute claim name as the value.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [IdpIdentifiers](#API_CreateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-request-IdpIdentifiers"></a>
An array of IdP identifiers, for example `"IdPIdentifiers": [ "MyIdP", "MyIdP2" ]`. Identifiers are friendly names that you can pass in the `idp_identifier` query parameter of requests to the [Authorize endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html) to silently redirect to sign-in with the associated IdP. Identifiers in a domain format also enable the use of [email-address matching with SAML providers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managing-saml-idp-naming.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[\w\s+=.@-]+`
Required: No

 ** [ProviderDetails](#API_CreateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-request-ProviderDetails"></a>
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
Required: Yes

 ** [ProviderName](#API_CreateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-request-ProviderName"></a>
The name that you want to assign to the IdP. You can pass the identity provider name in the `identity_provider` query parameter of requests to the [Authorize endpoint](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html) to silently redirect to sign-in with the associated IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^_\p{Z}][\p{L}\p{M}\p{S}\p{N}\p{P}][^_\p{Z}]+`
Required: Yes

 ** [ProviderType](#API_CreateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-request-ProviderType"></a>
The type of IdP that you want to add. Amazon Cognito supports OIDC, SAML 2.0, Login With Amazon, Sign In With Apple, Google, and Facebook IdPs.
Type: String
Valid Values: `SAML | Facebook | Google | LoginWithAmazon | SignInWithApple | OIDC`
Required: Yes

 ** [UserPoolId](#API_CreateIdentityProvider_RequestSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-request-UserPoolId"></a>
The Id of the user pool where you want to create an IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_CreateIdentityProvider_ResponseSyntax"></a>

```
{
   "IdentityProvider": {
      "AcrMapping": {
         "string" : "string"
      },
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
<a name="API_CreateIdentityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityProvider](#API_CreateIdentityProvider_ResponseSyntax) **   <a name="CognitoUserPools-CreateIdentityProvider-response-IdentityProvider"></a>
The details of the new user pool IdP.
Type: [IdentityProviderType](API_IdentityProviderType.md) object

## Errors
<a name="API_CreateIdentityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateProviderException **
This exception is thrown when the provider is already supported by the user pool.
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

## Examples
<a name="API_CreateIdentityProvider_Examples"></a>

### Example
<a name="API_CreateIdentityProvider_Example_1"></a>

This request adds a SAML IdP named `MySAMLIdP` to a user pool. The IdP is identified by a static `MetadataFile` in this request. Note the escape characters before the double-quotes in the metadata XML. You can also add a dynamic metadata source with `MetadataURL`. The SAML provider supports single logout (SLO) and provides the SLO endpoint in the metadata. Additionally, the SAML provider supports IdP-initiated SAML and encrypted responses.

#### Sample Request
<a name="API_CreateIdentityProvider_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateIdentityProvider
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "AttributeMapping": {
      "email" : "idp_email",
      "email_verified" : "idp_email_verified"
   },
   "IdpIdentifiers": [ "platform" ],
   "ProviderDetails": {
      "MetadataFile": "<md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"http://www.example.com/saml\"><md:IDPSSODescriptor WantAuthnRequestsSigned=\"false\" protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"><md:KeyDescriptor use=\"signing\"><ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><ds:X509Data><ds:X509Certificate>CERTIFICATE_DATA</ds:X509Certificate></ds:X509Data></ds:KeyInfo></md:KeyDescriptor><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://example.com/slo/saml\"/><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://example.com/slo/saml\"/><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://example.com/sso/saml\"/><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://example.com/sso/saml\"/></md:IDPSSODescriptor></md:EntityDescriptor>",
      "IDPSignout" : "true",
      "RequestSigningAlgorithm" : "rsa-sha256",
      "EncryptedResponses" : "true",
      "IDPInit" : "true"
   },
   "ProviderName": "MySAMLIdP",
   "ProviderType": "SAML",
   "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateIdentityProvider_Example_1_Response"></a>

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
		   "email_verified": "idp_email_verified"
		},
		"CreationDate": 1701128513.249,
		"IdpIdentifiers": [
		   "example.com"
		],
		"LastModifiedDate": 1701128513.249,
		"ProviderDetails": {
           "MetadataFile": "<md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"http://www.example.com/saml\"><md:IDPSSODescriptor WantAuthnRequestsSigned=\"false\" protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"><md:KeyDescriptor use=\"signing\"><ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><ds:X509Data><ds:X509Certificate>CERTIFICATE_DATA</ds:X509Certificate></ds:X509Data></ds:KeyInfo></md:KeyDescriptor><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://example.com/slo/saml\"/><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://example.com/slo/saml\"/><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://example.com/sso/saml\"/><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://example.com/sso/saml\"/></md:IDPSSODescriptor></md:EntityDescriptor>",
           "IDPSignout" : "true",
           "RequestSigningAlgorithm" : "rsa-sha256",
           "EncryptedResponses" : "true",
           "IDPInit" : "true"
		},
		"ProviderName": "MySAMLIdP",
		"ProviderType": "SAML",
		"UserPoolId": "us-east-1_EXAMPLE"
	}
}
```

### Example
<a name="API_CreateIdentityProvider_Example_2"></a>

This request adds an OIDC IdP named `MyOIDCIdP` to a user pool. In this request, we have chosen not to discover the issuer endpoints with `oidc_issuer` but instead to enter them manually.

#### Sample Request
<a name="API_CreateIdentityProvider_Example_2_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateIdentityProvider
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
   "AttributeMapping": {
      "email" : "idp_email",
      "email_verified" : "idp_email_verified"
   },
   "IdpIdentifiers": [ "station" ],
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
   "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateIdentityProvider_Example_2_Response"></a>

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
			"station"
		],
		"LastModifiedDate": 1701129701.653,
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
		"UserPoolId": "us-east-1_EXAMPLE"
	}
}
```

## See Also
<a name="API_CreateIdentityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CreateIdentityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CreateIdentityProvider)
