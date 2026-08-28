---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_IdentityProvider.html
---

# IdentityProvider
<a name="API_IdentityProvider"></a>

The identity provider.

## Contents
<a name="API_IdentityProvider_Contents"></a>

 ** identityProviderArn **   <a name="workspacesweb-Type-IdentityProvider-identityProviderArn"></a>
The ARN of the identity provider.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36}){2,}`
Required: Yes

 ** identityProviderDetails **   <a name="workspacesweb-Type-IdentityProvider-identityProviderDetails"></a>
The identity provider details. The following list describes the provider detail keys for each identity provider type.
+ For Google and Login with Amazon:
  +  `client_id`
  +  `client_secret`
  +  `authorize_scopes`
+ For Facebook:
  +  `client_id`
  +  `client_secret`
  +  `authorize_scopes`
  +  `api_version`
+ For Sign in with Apple:
  +  `client_id`
  +  `team_id`
  +  `key_id`
  +  `private_key`
  +  `authorize_scopes`
+ For OIDC providers:
  +  `client_id`
  +  `client_secret`
  +  `attributes_request_method`
  +  `oidc_issuer`
  +  `authorize_scopes`
  +  `authorize_url` *if not available from discovery URL specified by oidc\_issuer key*
  +  `token_url` *if not available from discovery URL specified by oidc\_issuer key*
  +  `attributes_url` *if not available from discovery URL specified by oidc\_issuer key*
  +  `jwks_uri` *if not available from discovery URL specified by oidc\_issuer key*
+ For SAML providers:
  +  `MetadataFile` OR `MetadataURL`
  +  `IDPSignout` (boolean) *optional*
  +  `IDPInit` (boolean) *optional*
  +  `RequestSigningAlgorithm` (string) *optional* - Only accepts `rsa-sha256`
  +  `EncryptedResponses` (boolean) *optional*
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Pattern: `[\s\S]*`
Required: No

 ** identityProviderName **   <a name="workspacesweb-Type-IdentityProvider-identityProviderName"></a>
The identity provider name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^_][\p{L}\p{M}\p{S}\p{N}\p{P}][^_]+`
Required: No

 ** identityProviderType **   <a name="workspacesweb-Type-IdentityProvider-identityProviderType"></a>
The identity provider type.
Type: String
Valid Values: `SAML | Facebook | Google | LoginWithAmazon | SignInWithApple | OIDC`
Required: No

## See Also
<a name="API_IdentityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/IdentityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/IdentityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/IdentityProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
