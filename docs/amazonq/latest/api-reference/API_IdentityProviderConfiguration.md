---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_IdentityProviderConfiguration.html
---

# IdentityProviderConfiguration
<a name="API_IdentityProviderConfiguration"></a>

Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

## Contents
<a name="API_IdentityProviderConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** openIDConnectConfiguration **   <a name="qbusiness-Type-IdentityProviderConfiguration-openIDConnectConfiguration"></a>
Information about the OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
Type: [OpenIDConnectProviderConfiguration](API_OpenIDConnectProviderConfiguration.md) object
Required: No

 ** samlConfiguration **   <a name="qbusiness-Type-IdentityProviderConfiguration-samlConfiguration"></a>
Information about the SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
Type: [SamlProviderConfiguration](API_SamlProviderConfiguration.md) object
Required: No

## See Also
<a name="API_IdentityProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/IdentityProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/IdentityProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/IdentityProviderConfiguration)
