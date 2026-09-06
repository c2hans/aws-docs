---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_IdentityProviderSummary.html
---

# IdentityProviderSummary
<a name="API_IdentityProviderSummary"></a>

The summary of the identity provider.

## Contents
<a name="API_IdentityProviderSummary_Contents"></a>

 ** identityProviderArn **   <a name="workspacesweb-Type-IdentityProviderSummary-identityProviderArn"></a>
The ARN of the identity provider.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36}){2,}`
Required: Yes

 ** identityProviderName **   <a name="workspacesweb-Type-IdentityProviderSummary-identityProviderName"></a>
The identity provider name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^_][\p{L}\p{M}\p{S}\p{N}\p{P}][^_]+`
Required: No

 ** identityProviderType **   <a name="workspacesweb-Type-IdentityProviderSummary-identityProviderType"></a>
The identity provider type.
Type: String
Valid Values: `SAML | Facebook | Google | LoginWithAmazon | SignInWithApple | OIDC`
Required: No

## See Also
<a name="API_IdentityProviderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/IdentityProviderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/IdentityProviderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/IdentityProviderSummary)
