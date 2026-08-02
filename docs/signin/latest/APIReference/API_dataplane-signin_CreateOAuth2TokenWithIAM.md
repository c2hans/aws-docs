---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2TokenWithIAM.html
---

# CreateOAuth2TokenWithIAM
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM"></a>

Exchanges client credentials for an OAuth 2.0 access token scoped to a resource, which you can use to access AWS services from applications.

Implements the OAuth 2.0 client credentials grant. Applications authenticate to the token endpoint using SigV4 signing, and AWS Sign-In returns a short-lived OAuth access token (JWT) scoped to the requested resource.

The returned access token is a Bearer token per the OAuth 2.0 specification. The token is a JSON Web Token (JWT). Token lifetime is the minimum of the caller's session validity and 1 hour (3600 seconds).

## Request Syntax
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM_RequestSyntax"></a>

```
POST /v1/token?x-amz-client-auth-method=iam HTTP/1.1
Content-type: application/json

{
   "grant\_type": "{{string}}",
   "resource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [grant\_type](#API_dataplane-signin_CreateOAuth2TokenWithIAM_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithIAM-request-grant_type"></a>
The OAuth 2.0 grant type. Must be `client_credentials`.
Type: String
Pattern: `client_credentials`
Required: Yes

 ** [resource](#API_dataplane-signin_CreateOAuth2TokenWithIAM_RequestSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithIAM-request-resource"></a>
The OAuth resource for which the access token is requested. This identifies the target service that the token grants access to. To scope the access token down to the specific resource, the resource parameter is mandated under RFC 8707 (Resource Indicators for OAuth 2.0).
When using a dynamically registered client (DCR), the resource parameter is required.
Example: `aws-mcp.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "access\_token": "string",
   "expires\_in": number,
   "token\_type": "string"
}
```

## Response Elements
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [access\_token](#API_dataplane-signin_CreateOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithIAM-response-access_token"></a>
JWT access token containing principal identity, resource scope, and session metadata. Use this token as a Bearer token when accessing the target resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [expires\_in](#API_dataplane-signin_CreateOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithIAM-response-expires_in"></a>
Token lifetime in seconds. Value is the minimum of the caller's session validity and 1 hour (3600 seconds).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.

 ** [token\_type](#API_dataplane-signin_CreateOAuth2TokenWithIAM_ResponseSyntax) **   <a name="signin-dataplane-signin_CreateOAuth2TokenWithIAM-response-token_type"></a>
Always `Bearer` per OAuth 2.0 specification.
Type: String
Pattern: `Bearer`

## Errors
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM_Errors"></a>

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
<a name="API_dataplane-signin_CreateOAuth2TokenWithIAM_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/CreateOAuth2TokenWithIAM)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/CreateOAuth2TokenWithIAM)
