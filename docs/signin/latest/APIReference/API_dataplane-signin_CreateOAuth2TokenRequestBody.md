---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_CreateOAuth2TokenRequestBody.html
---

# CreateOAuth2TokenRequestBody
<a name="API_dataplane-signin_CreateOAuth2TokenRequestBody"></a>

Input for the `CreateOAuth2Token` operation.

Supports both authorization code and refresh token flows. The flow is determined by the `grant_type` parameter. All field names use snake\_case per RFC 6749.

## Contents
<a name="API_dataplane-signin_CreateOAuth2TokenRequestBody_Contents"></a>

 ** client\_id **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenRequestBody-client_id"></a>
The OAuth 2.0 client identifier. Expected values: `arn:aws:signin:::devtools/same-device`, `arn:aws:signin:::devtools/cross-device`, or `arn:aws:signin:{region}::external-client/dcr/{uuid}` for dynamically registered clients.
Type: String
Pattern: `arn:aws:signin:::devtools/(same-device|cross-device)$|^arn:aws:signin:[^:]*::external-client/dcr/.*`
Required: Yes

 ** grant\_type **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenRequestBody-grant_type"></a>
The OAuth 2.0 grant type. Supported values:
+  `authorization_code` — Exchange an authorization code for tokens.
+  `refresh_token` — Use a refresh token to obtain a new access token.
Type: String
Pattern: `(authorization_code|refresh_token)`
Required: Yes

 ** code **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenRequestBody-code"></a>
The authorization code received from the `/v1/authorize` endpoint. Required when `grant_type=authorization_code`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** code\_verifier **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenRequestBody-code_verifier"></a>
The PKCE code verifier that proves possession of the original code challenge. Required when `grant_type=authorization_code`.
Type: String
Length Constraints: Minimum length of 43. Maximum length of 128.
Pattern: `[A-Za-z0-9\-._~]+`
Required: No

 ** redirect\_uri **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenRequestBody-redirect_uri"></a>
The redirect URI that was used in the original authorization request. Must match exactly. Required when `grant_type=authorization_code`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** refresh\_token **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenRequestBody-refresh_token"></a>
The refresh token issued by a previous token response. Required when `grant_type=refresh_token`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** resource **   <a name="signin-Type-dataplane-signin_CreateOAuth2TokenRequestBody-resource"></a>
The OAuth resource for which the access token is requested ([RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707)). Identifies the target service the token grants access to.
Required for dynamically registered (DCR) clients.
Example: `https://aws-mcp.us-east-1.api.aws/mcp`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_dataplane-signin_CreateOAuth2TokenRequestBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signin-2023-01-01/CreateOAuth2TokenRequestBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signin-2023-01-01/CreateOAuth2TokenRequestBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signin-2023-01-01/CreateOAuth2TokenRequestBody)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sign-In. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
