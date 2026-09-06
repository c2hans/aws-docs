---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2Token.html
---

# CreateOAuth2Token
<a name="API_dataplane-signin_CreateOAuth2Token"></a>

Exchanges an authorization code or refresh token for an OAuth 2.0 access token and refresh token.

This operation accepts `application/x-www-form-urlencoded` requests ([RFC 6749 §4.1.3](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.3)).

**Important**
 AWS AWS CLI and AWS SDK clients use `application/json` as the content type and receive a camelCase response. The `accessToken` field is an object containing `accessKeyId`, `secretAccessKey`, and `sessionToken` rather than an opaque Bearer JWT string.

## Request Syntax
<a name="API_dataplane-signin_CreateOAuth2Token_RequestSyntax"></a>

```
POST /v1/token HTTP/1.1
Content-type: application/json

{
   "client\_id": "{{string}}",
   "code": "{{string}}",
   "code\_verifier": "{{string}}",
   "grant\_type": "{{string}}",
   "redirect\_uri": "{{string}}",
   "refresh\_token": "{{string}}",
   "resource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_dataplane-signin_CreateOAuth2Token_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_dataplane-signin_CreateOAuth2Token_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [client\_id](#API_dataplane-signin_CreateOAuth2Token_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-request-client_id"></a>
The OAuth 2.0 client identifier. Expected values: `arn:aws:signin:::devtools/same-device`, `arn:aws:signin:::devtools/cross-device`, or `arn:aws:signin:{region}::external-client/dcr/{uuid}` for dynamically registered clients.
Type: String
Pattern: `arn:aws:signin:::devtools/(same-device|cross-device)$|^arn:aws:signin:[^:]*::external-client/dcr/.*`
Required: Yes

 ** [code](#API_dataplane-signin_CreateOAuth2Token_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-request-code"></a>
The authorization code received from the `/v1/authorize` endpoint. Required when `grant_type=authorization_code`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [code\_verifier](#API_dataplane-signin_CreateOAuth2Token_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-request-code_verifier"></a>
The PKCE code verifier that proves possession of the original code challenge. Required when `grant_type=authorization_code`.
Type: String
Length Constraints: Minimum length of 43. Maximum length of 128.
Pattern: `[A-Za-z0-9\-._~]+`
Required: No

 ** [grant\_type](#API_dataplane-signin_CreateOAuth2Token_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-request-grant_type"></a>
The OAuth 2.0 grant type. Supported values:
+  `authorization_code` — Exchange an authorization code for tokens.
+  `refresh_token` — Use a refresh token to obtain a new access token.
Type: String
Pattern: `(authorization_code|refresh_token)`
Required: Yes

 ** [redirect\_uri](#API_dataplane-signin_CreateOAuth2Token_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-request-redirect_uri"></a>
The redirect URI that was used in the original authorization request. Must match exactly. Required when `grant_type=authorization_code`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [refresh\_token](#API_dataplane-signin_CreateOAuth2Token_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-request-refresh_token"></a>
The refresh token issued by a previous token response. Required when `grant_type=refresh_token`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [resource](#API_dataplane-signin_CreateOAuth2Token_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-request-resource"></a>
The OAuth resource for which the access token is requested ([RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707)). Identifies the target service the token grants access to.
Required for dynamically registered (DCR) clients.
Example: `https://aws-mcp.us-east-1.api.aws/mcp`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_dataplane-signin_CreateOAuth2Token_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "access\_token": "string",
   "expires\_in": number,
   "id\_token": "string",
   "refresh\_token": "string",
   "token\_type": "string"
}
```

## Response Elements
<a name="API_dataplane-signin_CreateOAuth2Token_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [access\_token](#API_dataplane-signin_CreateOAuth2Token_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-response-access_token"></a>
The access token issued by the authorization server. This is an opaque Bearer JWT string (prefix `ASOA`). Use as a `Bearer` token in the `Authorization` header when calling the target resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [expires\_in](#API_dataplane-signin_CreateOAuth2Token_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-response-expires_in"></a>
The number of seconds until the access token expires. Maximum value is 900 seconds (15 minutes).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.

 ** [id\_token](#API_dataplane-signin_CreateOAuth2Token_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-response-id_token"></a>
A JSON Web Token (JWT) containing user identity claims. Present only when `grant_type=authorization_code`. Not included in refresh token responses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [refresh\_token](#API_dataplane-signin_CreateOAuth2Token_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-response-refresh_token"></a>
An encrypted refresh token that can be used to obtain new access tokens without re-authenticating. Valid for up to 12 hours.
Each time a refresh token is used, a new refresh token is returned (token rotation). Always use the most recently issued refresh token for subsequent requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [token\_type](#API_dataplane-signin_CreateOAuth2Token_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2Token-response-token_type"></a>
The type of token issued. Value is `Bearer` per RFC 6749 §5.1.
Type: String

## Errors
<a name="API_dataplane-signin_CreateOAuth2Token_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** TooManyRequestsError **
Indicates that the principal has exceeded the limit of requests to this API operation.
HTTP Status Code: 429

 ** ValidationException **
The request failed because it contains a syntax error.
HTTP Status Code: 400

## See Also
<a name="API_dataplane-signin_CreateOAuth2Token_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/CreateOAuth2Token)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/CreateOAuth2Token)
