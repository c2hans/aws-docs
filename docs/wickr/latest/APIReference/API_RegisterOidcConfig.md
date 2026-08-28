---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_RegisterOidcConfig.html
---

# RegisterOidcConfig
<a name="API_RegisterOidcConfig"></a>

Registers and saves an OpenID Connect (OIDC) configuration for a Wickr network, enabling Single Sign-On (SSO) authentication through an identity provider.

## Request Syntax
<a name="API_RegisterOidcConfig_RequestSyntax"></a>

```
POST /networks/{{networkId}}/oidc/save HTTP/1.1
Content-type: application/json

{
   "companyId": "{{string}}",
   "customUsername": "{{string}}",
   "extraAuthParams": "{{string}}",
   "issuer": "{{string}}",
   "scopes": "{{string}}",
   "secret": "{{string}}",
   "ssoTokenBufferMinutes": {{number}},
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterOidcConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-uri-networkId"></a>
The ID of the Wickr network for which OIDC will be configured.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_RegisterOidcConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [companyId](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-companyId"></a>
Custom identifier your end users will use to sign in with SSO.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [issuer](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-issuer"></a>
The issuer URL of the OIDC provider (e.g., 'https://login.example.com').
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [scopes](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-scopes"></a>
The OAuth scopes to request from the OIDC provider (e.g., 'openid profile email').
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [customUsername](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-customUsername"></a>
A custom field mapping to extract the username from the OIDC token (optional).
The customUsername is only required if you use something other than email as the username field.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** [extraAuthParams](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-extraAuthParams"></a>
Additional authentication parameters to include in the OIDC flow (optional).
Type: String
Pattern: `[\S\s]*`
Required: No

 ** [secret](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-secret"></a>
The client secret for authenticating with the OIDC provider (optional).
Type: String
Pattern: `[\S\s]*`
Required: No

 ** [ssoTokenBufferMinutes](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-ssoTokenBufferMinutes"></a>
The buffer time in minutes before the SSO token expires to refresh it (optional).
Type: Integer
Required: No

 ** [userId](#API_RegisterOidcConfig_RequestSyntax) **   <a name="wickr-RegisterOidcConfig-request-userId"></a>
Unique identifier provided by your identity provider to authenticate the access request. Also referred to as clientID.
Type: String
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_RegisterOidcConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
}
```

## Response Elements
<a name="API_RegisterOidcConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [companyId](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-companyId"></a>
Custom identifier your end users will use to sign in with SSO.
Type: String
Pattern: `[\S\s]*`

 ** [issuer](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-issuer"></a>
The issuer URL of the OIDC provider.
Type: String
Pattern: `[\S\s]*`

 ** [scopes](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-scopes"></a>
The OAuth scopes configured for the application.
Type: String
Pattern: `[\S\s]*`

 ** [applicationId](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-applicationId"></a>
The unique identifier for the registered OIDC application.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [applicationName](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-applicationName"></a>
The name of the registered OIDC application.
Type: String
Pattern: `[\S\s]*`

 ** [caCertificate](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-caCertificate"></a>
The CA certificate used for secure communication with the OIDC provider.
Type: String
Pattern: `[\S\s]*`

 ** [clientId](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-clientId"></a>
The OAuth client ID assigned to the application.
Type: String
Pattern: `[\S\s]*`

 ** [clientSecret](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-clientSecret"></a>
The OAuth client secret for the application.
Type: String
Pattern: `[\S\s]*`

 ** [customUsername](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-customUsername"></a>
The custom field mapping used for extracting the username.
Type: String
Pattern: `[\S\s]*`

 ** [extraAuthParams](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-extraAuthParams"></a>
The additional authentication parameters configured for the OIDC flow.
Type: String
Pattern: `[\S\s]*`

 ** [redirectUrl](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-redirectUrl"></a>
The redirect URL configured for the OAuth flow.
Type: String
Pattern: `[\S\s]*`

 ** [secret](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-secret"></a>
The client secret for authenticating with the OIDC provider.
Type: String
Pattern: `[\S\s]*`

 ** [ssoTokenBufferMinutes](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-ssoTokenBufferMinutes"></a>
The buffer time in minutes before the SSO token expires.
Type: Integer

 ** [userId](#API_RegisterOidcConfig_ResponseSyntax) **   <a name="wickr-RegisterOidcConfig-response-userId"></a>
The claim field being used as the user identifier.
Type: String
Pattern: `[\S\s]*`

## Errors
<a name="API_RegisterOidcConfig_Errors"></a>

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
<a name="API_RegisterOidcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/RegisterOidcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/RegisterOidcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
