---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_OidcTokenInfo.html
---

# OidcTokenInfo
<a name="API_OidcTokenInfo"></a>

Contains OAuth token information returned from the identity provider, including access tokens, ID tokens, and PKCE parameters used for secure authentication.

## Contents
<a name="API_OidcTokenInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accessToken **   <a name="wickr-Type-OidcTokenInfo-accessToken"></a>
The OAuth access token that can be used to access protected resources on behalf of the authenticated user.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** codeChallenge **   <a name="wickr-Type-OidcTokenInfo-codeChallenge"></a>
The PKCE code challenge, a transformed version of the code verifier sent during the authorization request for verification.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** codeVerifier **   <a name="wickr-Type-OidcTokenInfo-codeVerifier"></a>
The PKCE (Proof Key for Code Exchange) code verifier, a cryptographically random string used to enhance security in the OAuth flow.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** expiresIn **   <a name="wickr-Type-OidcTokenInfo-expiresIn"></a>
The lifetime of the access token in seconds, indicating when the token will expire and need to be refreshed.
Type: Long
Required: No

 ** idToken **   <a name="wickr-Type-OidcTokenInfo-idToken"></a>
The OpenID Connect ID token containing user identity information and authentication context as a signed JWT.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** refreshToken **   <a name="wickr-Type-OidcTokenInfo-refreshToken"></a>
The OAuth refresh token that can be used to obtain new access tokens without requiring the user to re-authenticate.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** tokenType **   <a name="wickr-Type-OidcTokenInfo-tokenType"></a>
The type of access token issued, typically 'Bearer', which indicates how the token should be used in API requests.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_OidcTokenInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/OidcTokenInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/OidcTokenInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/OidcTokenInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
