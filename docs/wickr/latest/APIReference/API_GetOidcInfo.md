---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetOidcInfo.html
---

# GetOidcInfo
<a name="API_GetOidcInfo"></a>

Retrieves the OpenID Connect (OIDC) configuration for a Wickr network, including SSO settings and optional token information if access token parameters are provided.

## Request Syntax
<a name="API_GetOidcInfo_RequestSyntax"></a>

```
GET /networks/{{networkId}}/oidc?certificate={{certificate}}&clientId={{clientId}}&clientSecret={{clientSecret}}&code={{code}}&codeVerifier={{codeVerifier}}&grantType={{grantType}}&redirectUri={{redirectUri}}&url={{url}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOidcInfo_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificate](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-certificate"></a>
The CA certificate for secure communication with the OIDC provider (optional).
Pattern: `[\S\s]*`

 ** [clientId](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-clientId"></a>
The OAuth client ID for retrieving access tokens (optional).
Pattern: `[\S\s]*`

 ** [clientSecret](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-clientSecret"></a>
The OAuth client secret for retrieving access tokens (optional).
Pattern: `[\S\s]*`

 ** [code](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-code"></a>
The authorization code for retrieving access tokens (optional).
Pattern: `[\S\s]*`

 ** [codeVerifier](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-codeVerifier"></a>
The PKCE code verifier for enhanced security in the OAuth flow (optional).
Pattern: `[\S\s]*`

 ** [grantType](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-grantType"></a>
The OAuth grant type for retrieving access tokens (optional).
Pattern: `[\S\s]*`

 ** [networkId](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-networkId"></a>
The ID of the Wickr network whose OIDC configuration will be retrieved.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

 ** [redirectUri](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-redirectUri"></a>
The redirect URI for the OAuth flow (optional).
Pattern: `[\S\s]*`

 ** [url](#API_GetOidcInfo_RequestSyntax) **   <a name="wickr-GetOidcInfo-request-uri-url"></a>
The URL for the OIDC provider (optional).
Pattern: `[\S\s]*`

## Request Body
<a name="API_GetOidcInfo_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOidcInfo_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "openidConnectInfo": {
      "applicationId": number,
      "applicationName": "string",
      "caCertificate": "string",
      "clientId": "string",
      "clientSecret": "string",
      "companyId": "string",
      "customUsername": "string",
      "extraAuthParams": "string",
      "issuer": "string",
      "redirectUrl": "string",
      "scopes": "string",
      "secret": "string",
      "ssoTokenBufferMinutes": number,
      "userId": "string"
   },
   "tokenInfo": {
      "accessToken": "string",
      "codeChallenge": "string",
      "codeVerifier": "string",
      "expiresIn": number,
      "idToken": "string",
      "refreshToken": "string",
      "tokenType": "string"
   }
}
```

## Response Elements
<a name="API_GetOidcInfo_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [openidConnectInfo](#API_GetOidcInfo_ResponseSyntax) **   <a name="wickr-GetOidcInfo-response-openidConnectInfo"></a>
The OpenID Connect configuration information for the network, including issuer, client ID, scopes, and other SSO settings.
Type: [OidcConfigInfo](API_OidcConfigInfo.md) object

 ** [tokenInfo](#API_GetOidcInfo_ResponseSyntax) **   <a name="wickr-GetOidcInfo-response-tokenInfo"></a>
OAuth token information including access token, refresh token, and expiration details (only present if token parameters were provided in the request).
Type: [OidcTokenInfo](API_OidcTokenInfo.md) object

## Errors
<a name="API_GetOidcInfo_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [BadRequestError](API_BadRequestError.md)
The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.
 ** message **
A detailed message explaining what was wrong with the request and how to correct it.
HTTP Status Code: 400

 [ForbiddenError](API_ForbiddenError.md)
Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.
 ** message **
A message explaining why access was denied and what permissions are required.
HTTP Status Code: 403

 [InternalServerError](API_InternalServerError.md)
An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact AWS Support.
 ** message **
A message describing the internal server error that occurred.
HTTP Status Code: 500

 [RateLimitError](API_RateLimitError.md)
The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.
 ** message **
A message indicating that the rate limit was exceeded and suggesting when to retry.
HTTP Status Code: 429

 [ResourceNotFoundError](API_ResourceNotFoundError.md)
The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.
 ** message **
A message identifying which resource was not found.
HTTP Status Code: 404

 [UnauthorizedError](API_UnauthorizedError.md)
The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.
 ** message **
A message explaining why the authentication failed.
HTTP Status Code: 401

 [ValidationError](API_ValidationError.md)
One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.
 ** message **
A message describing the validation error error that occurred.
 ** reasons **
A list of validation error details, where each item identifies a specific field that failed validation and explains the reason for the failure.
HTTP Status Code: 422

## See Also
<a name="API_GetOidcInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/GetOidcInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/GetOidcInfo)
