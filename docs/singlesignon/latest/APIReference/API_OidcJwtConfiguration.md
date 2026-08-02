---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_OidcJwtConfiguration.html
---

# OidcJwtConfiguration
<a name="API_OidcJwtConfiguration"></a>

A structure that describes configuration settings for a trusted token issuer that supports OpenID Connect (OIDC) and JSON Web Tokens (JWTs).

## Contents
<a name="API_OidcJwtConfiguration_Contents"></a>

 ** ClaimAttributePath **   <a name="singlesignon-Type-OidcJwtConfiguration-ClaimAttributePath"></a>
The path of the source attribute in the JWT from the trusted token issuer. The attribute mapped by this JMESPath expression is compared against the attribute mapped by `IdentityStoreAttributePath` when a trusted token issuer token is exchanged for an IAM Identity Center token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\p{L}+(?:(\.|\_)\p{L}+){0,2}`
Required: Yes

 ** IdentityStoreAttributePath **   <a name="singlesignon-Type-OidcJwtConfiguration-IdentityStoreAttributePath"></a>
The path of the destination attribute in a JWT from IAM Identity Center. The attribute mapped by this JMESPath expression is compared against the attribute mapped by `ClaimAttributePath` when a trusted token issuer token is exchanged for an IAM Identity Center token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\p{L}+(?:\.\p{L}+){0,2}`
Required: Yes

 ** IssuerUrl **   <a name="singlesignon-Type-OidcJwtConfiguration-IssuerUrl"></a>
The URL that IAM Identity Center uses for OpenID Discovery. OpenID Discovery is used to obtain the information required to verify the tokens that the trusted token issuer generates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https?:\/\/[-a-zA-Z0-9+&@\/%=~_|!:,.;]*[-a-zA-Z0-9+&@\/%=~_|]`
Required: Yes

 ** JwksRetrievalOption **   <a name="singlesignon-Type-OidcJwtConfiguration-JwksRetrievalOption"></a>
The method that the trusted token issuer can use to retrieve the JSON Web Key Set used to verify a JWT.
Type: String
Valid Values: `OPEN_ID_DISCOVERY`
Required: Yes

## See Also
<a name="API_OidcJwtConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/OidcJwtConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/OidcJwtConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/OidcJwtConfiguration)
