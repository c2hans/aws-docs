---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_IntrospectOAuth2TokenWithIAM.html
---

# IntrospectOAuth2TokenWithIAM
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM"></a>

Inspects the metadata and active state of an OAuth 2.0 access token or refresh token.

Implements RFC 7662 (OAuth 2.0 Token Introspection) over a SigV4-authenticated endpoint. Returns the claims associated with a token issued by AWS Sign-In. It inspects the metadata of a token issued by AWS Sign-In and returns the claims associated with it.

When the supplied token is unknown, expired, revoked, malformed, or owned by a different account, the response contains only `{"active": false}` with all other claims omitted.

## Request Syntax
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM_RequestSyntax"></a>

```
POST /v1/introspect?x-amz-client-auth-method=iam HTTP/1.1
Content-type: application/json

{
   "token": "{{string}}",
   "token\_type\_hint": "{{string}}"
}
```

## URI Request Parameters
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [token](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_RequestSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-request-token"></a>
The string value of the token to introspect. Can be an access token or a refresh token issued by AWS Sign-In.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `ASO[AR][A-Za-z0-9+/=_\-]+`
Required: Yes

 ** [token\_type\_hint](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_RequestSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-request-token_type_hint"></a>
An optional hint about the type of the token submitted for introspection per RFC 7662. The server checks both token types regardless of the hint provided. Allowed values: `access_token`, `refresh_token`.
Type: String
Pattern: `(access_token|refresh_token)`
Required: No

## Response Syntax
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "account\_id": "string",
   "active": boolean,
   "aud": "string",
   "client\_id": "string",
   "exp": number,
   "iat": number,
   "iss": "string",
   "jti": "string",
   "nbf": number,
   "resource": "string",
   "signin\_session": "string",
   "sub": "string",
   "token\_type": "string",
   "user\_id": "string"
}
```

## Response Elements
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [account\_id](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-account_id"></a>
12-digit AWS account ID of the token's subject principal.
Type: String
Pattern: `[0-9]{12}`

 ** [active](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-active"></a>
Indicates whether the token is currently active. Returns `true` only when the token is valid, has not expired, has not been revoked, and belongs to the caller's account.
Type: Boolean

 ** [aud](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-aud"></a>
Audience of the token: the OAuth resource the token is scoped to. Omitted for refresh tokens.
Type: String

 ** [client\_id](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-client_id"></a>
Client identifier for the OAuth 2.0 client that requested the token.
Type: String

 ** [exp](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-exp"></a>
Token expiration time as a NumericDate (Unix epoch seconds).
Type: Long

 ** [iat](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-iat"></a>
Token issuance time as a NumericDate (Unix epoch seconds).
Type: Long

 ** [iss](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-iss"></a>
Issuer of the token. Always `signin.amazonaws.com` for AWS Sign-In.
Type: String

 ** [jti](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-jti"></a>
Unique identifier for the token.
Type: String

 ** [nbf](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-nbf"></a>
Token "not before" time as a NumericDate (Unix epoch seconds).
Type: Long

 ** [resource](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-resource"></a>
The OAuth resource the token is scoped to. Only present for refresh token introspection.
Type: String

 ** [signin\_session](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-signin_session"></a>
 AWS Sign-In session ARN bound to the token, of the form `arn:aws:signin:{region}:{account}:session/{uuid}`.
Type: String

 ** [sub](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-sub"></a>
Subject of the token: the IAM principal Amazon Resource Name (ARN). For assumed-role sessions, this is the session ARN.
Type: String

 ** [token\_type](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-token_type"></a>
Indicates which kind of token was introspected. One of `access_token` or `refresh_token`.
Type: String
Pattern: `(access_token|refresh_token)`

 ** [user\_id](#API_dataplane-signin_IntrospectOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_IntrospectOAuth2TokenWithIAM-response-user_id"></a>
User identifier matching the `UserId` field from `sts:GetCallerIdentity` for the token's subject principal.
Type: String

## Errors
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM_Errors"></a>

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
<a name="API_dataplane-signin_IntrospectOAuth2TokenWithIAM_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/IntrospectOAuth2TokenWithIAM)
