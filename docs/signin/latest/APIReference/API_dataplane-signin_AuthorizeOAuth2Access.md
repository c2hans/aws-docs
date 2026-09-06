---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_AuthorizeOAuth2Access.html
---

# AuthorizeOAuth2Access
<a name="API_dataplane-signin_AuthorizeOAuth2Access"></a>

Grants permission to authenticate through a browser and obtain an OAuth 2.0 authorization code for credential exchange.

## Request Syntax
<a name="API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax"></a>

```
GET /v1/authorize?client_id={{clientId}}&code_challenge={{codeChallenge}}&code_challenge_method={{codeChallengeMethod}}&redirect_uri={{redirectUri}}&resource={{resource}}&response_type={{responseType}}&scope={{scope}}&state={{state}} HTTP/1.1
```

## URI Request Parameters
<a name="API_dataplane-signin_AuthorizeOAuth2Access_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientId](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-clientId"></a>
Client identifier which is unique to authorization server. Expected values: `arn:aws:signin:::devtools/same-device`, `arn:aws:signin:::devtools/cross-device`, or `arn:aws:signin:{region}::external-client/dcr/{uuid}` for dynamically registered clients.
Pattern: `arn:aws:signin:::devtools/(same-device|cross-device)$|^arn:aws:signin:[^:]*::external-client/dcr/.*`
Required: Yes

 ** [codeChallenge](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-codeChallenge"></a>
PKCE code challenge (SHA-256 hash of code verifier). Base64URL encoded, 43-128 characters.
Length Constraints: Minimum length of 43. Maximum length of 128.
Pattern: `[A-Za-z0-9\-._~]+`
Required: Yes

 ** [codeChallengeMethod](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-codeChallengeMethod"></a>
PKCE code challenge method - must be `SHA-256` for AWS CLI.
Pattern: `SHA-256`
Required: Yes

 ** [redirectUri](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-redirectUri"></a>
Redirect URI where authorization code will be sent.
Same-device: `http://127.0.0.1:PORT/oauth/callback`
Cross-device: `https://{region}.signin.aws.amazon.com/v1/sessions/confirmation`
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [resource](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-resource"></a>
The OAuth resource for which the access token is requested. This identifies the target service that the token grants access to. To scope the access token down to the specific resource, the resource parameter is mandated under RFC 8707 (Resource Indicators for OAuth 2.0).
If the client is a dynamically registered (DCR) client, this parameter is required.
Example: `https://aws-mcp.us-east-1.api.aws/mcp`.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [responseType](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-responseType"></a>
OAuth 2.0 response type - must be `code` for authorization code flow.
Pattern: `code`
Required: Yes

 ** [scope](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-scope"></a>
OAuth 2.0 scope parameter - must be `openid` for AWS CLI clients.
Pattern: `openid`

 ** [state](#API_dataplane-signin_AuthorizeOAuth2Access_RequestSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-request-uri-state"></a>
CSRF protection parameter to prevent authorization injection attacks.
Length Constraints: Minimum length of 1. Maximum length of 128.

## Request Body
<a name="API_dataplane-signin_AuthorizeOAuth2Access_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_dataplane-signin_AuthorizeOAuth2Access_ResponseSyntax"></a>

```
HTTP/1.1 302
Location: {{location}}
```

## Response Elements
<a name="API_dataplane-signin_AuthorizeOAuth2Access_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 302 response.

The response returns the following HTTP headers.

 ** [location](#API_dataplane-signin_AuthorizeOAuth2Access_ResponseSyntax) **   <a name="signin-dataplane-signin_AuthorizeOAuth2Access-response-location"></a>
HTTP Location header containing the redirect URI with authorization code and state parameters.
Response format: `{redirect_uri}?code={authorization_code}&state={state_parameter}`
Where:
+  `redirect_uri`: The same URI provided in the authorization request
+  `authorization_code`: A short-lived, single-use code for token exchange
+  `state`: The same state value from the original request (CSRF protection)
Example values:
+  `http://127.0.0.1:PORT/oauth/callback?code=ABC123&state=xyz`
+  `https://{region}.signin.aws.amazon.com/v1/sessions/confirmation?code=DEF456&state=abc`

## Errors
<a name="API_dataplane-signin_AuthorizeOAuth2Access_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request is invalid. Used for OAuth 2.0 request validation errors such as missing required parameters, invalid parameter values, malformed PKCE parameters, or invalid scope values.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** TooManyRequestsError **
Indicates that the principal has exceeded the limit of requests to this API operation.
HTTP Status Code: 429

## See Also
<a name="API_dataplane-signin_AuthorizeOAuth2Access_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/AuthorizeOAuth2Access)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/AuthorizeOAuth2Access)
