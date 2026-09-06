---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TrustedTokenIssuerConfiguration.html
---

# TrustedTokenIssuerConfiguration
<a name="API_TrustedTokenIssuerConfiguration"></a>

A structure that describes the configuration of a trusted token issuer. The structure and available settings are determined by the type of the trusted token issuer.

## Contents
<a name="API_TrustedTokenIssuerConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** OidcJwtConfiguration **   <a name="singlesignon-Type-TrustedTokenIssuerConfiguration-OidcJwtConfiguration"></a>
A structure that describes the settings for a trusted token issuer that works with OpenID Connect (OIDC) by using JSON Web Tokens (JWT).
Type: [OidcJwtConfiguration](API_OidcJwtConfiguration.md) object
Required: No

## See Also
<a name="API_TrustedTokenIssuerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/TrustedTokenIssuerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/TrustedTokenIssuerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/TrustedTokenIssuerConfiguration)
