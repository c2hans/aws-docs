---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2TokenWithTokenExchange.html
---

# CreateOAuth2TokenWithTokenExchange
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange"></a>

Exchanges a supported token for an OAuth 2.0 access token scoped to a resource, which you can use to access AWS services from applications.

The issued access token is valid for up to 1 hour (3600 seconds).

## Request Syntax
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestSyntax"></a>

```
POST /v1/token?x-amz-oauth-token-method=token-exchange HTTP/1.1
Content-type: application/json

{
   "grant\_type": "{{string}}",
   "resource": "{{string}}",
   "scope": "{{string}}",
   "subject\_token": "{{string}}",
   "subject\_token\_type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [grant\_type](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-request-grant_type"></a>
The OAuth 2.0 grant type. Currently only supports `urn:ietf:params:oauth:grant-type:token-exchange`.
Type: String
Pattern: `urn:ietf:params:oauth:grant-type:token-exchange`
Required: Yes

 ** [resource](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-request-resource"></a>
The OAuth resource for which the access token is requested. Required when `grant_type=urn:ietf:params:oauth:grant-type:token-exchange`. Example: `glue.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [scope](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-request-scope"></a>
IAM managed policy Amazon Resource Names (ARNs) to apply as session policies that further scope down the permissions of the issued access token, provided as a space-delimited list.
Example: `arn:aws:iam::444455556666:policy/MyPolicy`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [subject\_token](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-request-subject_token"></a>
The subject token that represents the identity of the party on whose behalf the request is made. Required when `grant_type=urn:ietf:params:oauth:grant-type:token-exchange`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 20000.
Required: No

 ** [subject\_token\_type](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-request-subject_token_type"></a>
The token type of the subject token. Currently only supports `urn:ietf:params:oauth:token-type:jwt`. Required when `grant_type=urn:ietf:params:oauth:grant-type:token-exchange`.
Type: String
Pattern: `urn:ietf:params:oauth:token-type:.+`
Required: No

## Response Syntax
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "access\_token": "string",
   "expires\_in": number,
   "issued\_token\_type": "string",
   "token\_type": "string"
}
```

## Response Elements
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [access\_token](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-response-access_token"></a>
Access token containing principal identity, resource scope, and session metadata. Use this token as a Bearer token when accessing the target resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [expires\_in](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-response-expires_in"></a>
Token lifetime in seconds. Value is the minimum of the subject token's validity and 1 hour (3600 seconds).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.

 ** [issued\_token\_type](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-response-issued_token_type"></a>
The token type of the issued token. Always `urn:ietf:params:oauth:token-type:access_token` as defined in RFC 8693 §2.2.1.
Type: String
Pattern: `urn:ietf:params:oauth:token-type:access_token`

 ** [token\_type](#API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithTokenExchange-response-token_type"></a>
The token type. Currently only supports `Bearer` as defined in RFC 6749.
Type: String
Pattern: `Bearer`

## Errors
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request failed because of an internal server error.
HTTP Status Code: 500

 ** InvalidGrantException **
The request failed because the provided grant is invalid or expired.
HTTP Status Code: 400

 ** InvalidScopeException **
The request failed because the requested scope is invalid or exceeds the scope that can be granted.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed because a dependency is temporarily unavailable. You can retry the request.
HTTP Status Code: 503

 ** TooManyRequestsError **
The request failed because you exceeded the request rate limit for this operation.
HTTP Status Code: 429

 ** ValidationException **
The request failed because it contains a malformed, missing, or invalid parameter.
HTTP Status Code: 400

## See Also
<a name="API_dataplane-signin_CreateOAuth2TokenWithTokenExchange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/CreateOAuth2TokenWithTokenExchange)
