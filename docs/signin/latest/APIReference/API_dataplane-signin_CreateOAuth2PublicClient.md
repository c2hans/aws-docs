---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2PublicClient.html
---

# CreateOAuth2PublicClient
<a name="API_dataplane-signin_CreateOAuth2PublicClient"></a>

Dynamically registers an OAuth 2.0 public client for use with AWS Sign-In.

Implements RFC 7591 (OAuth 2.0 Dynamic Client Registration) for MCP-compatible agents. Only redirect URIs matching the allowlisted patterns are accepted during registration.

Registered clients receive an ARN in the format `arn:aws:signin:{region}::external-client/dcr/{uuid}`. Client registrations have a 90-day lifetime.

## Request Syntax
<a name="API_dataplane-signin_CreateOAuth2PublicClient_RequestSyntax"></a>

```
POST /v1/register HTTP/1.1
Content-type: application/json

{
   "grant\_types": [ "{{string}}" ],
   "redirect\_uris": [ "{{string}}" ],
   "response\_types": [ "{{string}}" ],
   "token\_endpoint\_auth\_method": "{{string}}"
}
```

## URI Request Parameters
<a name="API_dataplane-signin_CreateOAuth2PublicClient_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_dataplane-signin_CreateOAuth2PublicClient_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [grant\_types](#API_dataplane-signin_CreateOAuth2PublicClient_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-request-grant_types"></a>
The grant types that this client will use. Supported values: `authorization_code`, `refresh_token`. Defaults to both if omitted. The `client_credentials` grant type is not supported. The `refresh_token` grant type cannot be specified alone without `authorization_code`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [redirect\_uris](#API_dataplane-signin_CreateOAuth2PublicClient_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-request-redirect_uris"></a>
The redirect URIs that this client will use for OAuth callbacks. Only redirect URIs matching the allowlisted patterns are accepted. Maximum of 10 URIs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [response\_types](#API_dataplane-signin_CreateOAuth2PublicClient_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-request-response_types"></a>
The response types that this client will use. Only `code` is supported. Defaults to `["code"]` if omitted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [token\_endpoint\_auth\_method](#API_dataplane-signin_CreateOAuth2PublicClient_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-request-token_endpoint_auth_method"></a>
The client authentication method for the token endpoint. Only `none` is supported (public clients). Defaults to `none` if omitted.
Type: String
Pattern: `none`
Required: No

## Response Syntax
<a name="API_dataplane-signin_CreateOAuth2PublicClient_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "client\_id": "string",
   "client\_id\_issued\_at": number,
   "grant\_types": [ "string" ],
   "redirect\_uris": [ "string" ],
   "response\_types": [ "string" ],
   "token\_endpoint\_auth\_method": "string"
}
```

## Response Elements
<a name="API_dataplane-signin_CreateOAuth2PublicClient_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [client\_id](#API_dataplane-signin_CreateOAuth2PublicClient_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-response-client_id"></a>
The unique client identifier (ARN) assigned to this client. Format: `arn:aws:signin:{region}::external-client/dcr/{uuid}`.
Type: String

 ** [client\_id\_issued\_at](#API_dataplane-signin_CreateOAuth2PublicClient_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-response-client_id_issued_at"></a>
The time at which the client identifier was issued, as a NumericDate (Unix epoch seconds).
Type: Long

 ** [grant\_types](#API_dataplane-signin_CreateOAuth2PublicClient_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-response-grant_types"></a>
The grant types registered for this client.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [redirect\_uris](#API_dataplane-signin_CreateOAuth2PublicClient_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-response-redirect_uris"></a>
The redirect URIs registered for this client.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [response\_types](#API_dataplane-signin_CreateOAuth2PublicClient_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-response-response_types"></a>
The response types registered for this client.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [token\_endpoint\_auth\_method](#API_dataplane-signin_CreateOAuth2PublicClient_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2PublicClient-response-token_endpoint_auth_method"></a>
The client authentication method. Always `none` for public clients.
Type: String
Pattern: `none`

## Errors
<a name="API_dataplane-signin_CreateOAuth2PublicClient_Errors"></a>

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
<a name="API_dataplane-signin_CreateOAuth2PublicClient_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/CreateOAuth2PublicClient)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/CreateOAuth2PublicClient)
