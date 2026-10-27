---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2TokenResponseBody.html
---

# CreateOAuth2TokenResponseBody
<a name="API_dataplane-signin_CreateOAuth2TokenResponseBody"></a>

The response body for an OAuth 2.0 token request. The fields returned depend on the `grant_type`. The authorization code flow returns `refresh_token` and `id_token`. The refresh token flow omits `id_token`.

**Note**
 AWS CLI and AWS SDK clients use `application/json` as the content type and receive a camelCase response. The `accessToken` field is an object containing `accessKeyId`, `secretAccessKey`, and `sessionToken` rather than an opaque Bearer token.

## Contents
<a name="API_dataplane-signin_CreateOAuth2TokenResponseBody_Contents"></a>

 ** access\_token **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenResponseBody-access_token"></a>
The access token issued by the authorization server. This is an opaque Bearer token. Use it as a `Bearer` token in the `Authorization` header when calling the target resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** expires\_in **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenResponseBody-expires_in"></a>
The number of seconds until the access token expires. Maximum value is 900 seconds (15 minutes).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.
Required: Yes

 ** refresh\_token **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenResponseBody-refresh_token"></a>
A refresh token that can be used to obtain new access tokens without re-authenticating.
A new refresh token is issued each time. Always refresh using the most recently issued token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** token\_type **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenResponseBody-token_type"></a>
The type of token issued. Value is `Bearer` as defined in RFC 6749 §5.1.
Type: String
Required: Yes

 ** id\_token **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenResponseBody-id_token"></a>
A JSON Web Token (JWT) containing user identity claims. Present only when `grant_type=authorization_code`. Not included in refresh token responses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_dataplane-signin_CreateOAuth2TokenResponseBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/CreateOAuth2TokenResponseBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/CreateOAuth2TokenResponseBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/CreateOAuth2TokenResponseBody)
