---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_RevokeOAuth2TokenWithIAM.html
---

# RevokeOAuth2TokenWithIAM
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM"></a>

Revokes an OAuth 2.0 refresh token and its associated token chain.

Implements RFC 7009 (OAuth 2.0 Token Revocation) over a SigV4-authenticated endpoint. Invalidates the specified refresh token so that it can no longer be used to obtain new access tokens.

This operation is idempotent – revoking an already-revoked, expired, or otherwise invalid token returns 200 OK with an empty body. Only refresh tokens (prefix `ASOR`) are accepted.

**Important**
Revoking a refresh token does not invalidate access tokens that were previously issued using that refresh token. Existing access tokens remain valid until they expire (up to 1 hour). To immediately block access, use an IAM policy with `aws:SignInSessionArn` to deny the specific session.

## Request Syntax
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM_RequestSyntax"></a>

```
POST /v1/revoke?x-amz-client-auth-method=iam HTTP/1.1
Content-type: application/json

{
   "token": "{{string}}"
}
```

## URI Request Parameters
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [token](#API_dataplane-signin_RevokeOAuth2TokenWithIAM_RequestSyntax) **   <a name="signin-dataplane-signin_RevokeOAuth2TokenWithIAM-request-token"></a>
The refresh token to revoke. Must be a refresh token issued by AWS Sign-In (prefix `ASOR`). Access tokens are not accepted for revocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `ASOR[A-Za-z0-9+/=_\-]+`
Required: Yes

## Response Syntax
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM_Errors"></a>

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
<a name="API_dataplane-signin_RevokeOAuth2TokenWithIAM_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/RevokeOAuth2TokenWithIAM)
