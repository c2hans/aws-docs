---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_RegisterOidcConfigTest.html
---

# RegisterOidcConfigTest
<a name="API_RegisterOidcConfigTest"></a>

Tests an OpenID Connect (OIDC) configuration for a Wickr network by validating the connection to the identity provider and retrieving its supported capabilities.

## Request Syntax
<a name="API_RegisterOidcConfigTest_RequestSyntax"></a>

```
POST /networks/{{networkId}}/oidc/test HTTP/1.1
Content-type: application/json

{
   "certificate": "{{string}}",
   "extraAuthParams": "{{string}}",
   "issuer": "{{string}}",
   "scopes": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterOidcConfigTest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_RegisterOidcConfigTest_RequestSyntax) **   <a name="wickr-RegisterOidcConfigTest-request-uri-networkId"></a>
The ID of the Wickr network for which the OIDC configuration will be tested.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_RegisterOidcConfigTest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [issuer](#API_RegisterOidcConfigTest_RequestSyntax) **   <a name="wickr-RegisterOidcConfigTest-request-issuer"></a>
The issuer URL of the OIDC provider to test.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [scopes](#API_RegisterOidcConfigTest_RequestSyntax) **   <a name="wickr-RegisterOidcConfigTest-request-scopes"></a>
The OAuth scopes to test with the OIDC provider.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [certificate](#API_RegisterOidcConfigTest_RequestSyntax) **   <a name="wickr-RegisterOidcConfigTest-request-certificate"></a>
The CA certificate for secure communication with the OIDC provider (optional).
Type: String
Pattern: `[\S\s]*`
Required: No

 ** [extraAuthParams](#API_RegisterOidcConfigTest_RequestSyntax) **   <a name="wickr-RegisterOidcConfigTest-request-extraAuthParams"></a>
Additional authentication parameters to include in the test (optional).
Type: String
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_RegisterOidcConfigTest_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizationEndpoint": "string",
   "endSessionEndpoint": "string",
   "grantTypesSupported": [ "string" ],
   "issuer": "string",
   "logoutEndpoint": "string",
   "microsoftMultiRefreshToken": boolean,
   "responseTypesSupported": [ "string" ],
   "revocationEndpoint": "string",
   "scopesSupported": [ "string" ],
   "tokenEndpoint": "string",
   "tokenEndpointAuthMethodsSupported": [ "string" ],
   "userinfoEndpoint": "string"
}
```

## Response Elements
<a name="API_RegisterOidcConfigTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizationEndpoint](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-authorizationEndpoint"></a>
The authorization endpoint URL discovered from the OIDC provider.
Type: String
Pattern: `[\S\s]*`

 ** [endSessionEndpoint](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-endSessionEndpoint"></a>
The end session endpoint URL for logging out users from the OIDC provider.
Type: String
Pattern: `[\S\s]*`

 ** [grantTypesSupported](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-grantTypesSupported"></a>
The OAuth grant types supported by the OIDC provider.
Type: Array of strings
Pattern: `[\S\s]*`

 ** [issuer](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-issuer"></a>
The issuer URL confirmed by the OIDC provider.
Type: String
Pattern: `[\S\s]*`

 ** [logoutEndpoint](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-logoutEndpoint"></a>
The logout endpoint URL for terminating user sessions.
Type: String
Pattern: `[\S\s]*`

 ** [microsoftMultiRefreshToken](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-microsoftMultiRefreshToken"></a>
Indicates whether the provider supports Microsoft multi-refresh tokens.
Type: Boolean

 ** [responseTypesSupported](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-responseTypesSupported"></a>
The OAuth response types supported by the OIDC provider.
Type: Array of strings
Pattern: `[\S\s]*`

 ** [revocationEndpoint](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-revocationEndpoint"></a>
The token revocation endpoint URL for invalidating tokens.
Type: String
Pattern: `[\S\s]*`

 ** [scopesSupported](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-scopesSupported"></a>
The OAuth scopes supported by the OIDC provider.
Type: Array of strings
Pattern: `[\S\s]*`

 ** [tokenEndpoint](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-tokenEndpoint"></a>
The token endpoint URL discovered from the OIDC provider.
Type: String
Pattern: `[\S\s]*`

 ** [tokenEndpointAuthMethodsSupported](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-tokenEndpointAuthMethodsSupported"></a>
The authentication methods supported by the token endpoint.
Type: Array of strings
Pattern: `[\S\s]*`

 ** [userinfoEndpoint](#API_RegisterOidcConfigTest_ResponseSyntax) **   <a name="wickr-RegisterOidcConfigTest-response-userinfoEndpoint"></a>
The user info endpoint URL discovered from the OIDC provider.
Type: String
Pattern: `[\S\s]*`

## Errors
<a name="API_RegisterOidcConfigTest_Errors"></a>

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
<a name="API_RegisterOidcConfigTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/RegisterOidcConfigTest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/RegisterOidcConfigTest)
