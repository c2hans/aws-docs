---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_JwtIssuerInput.html
---

# JwtIssuerInput

A trusted issuer in the JWT configuration.

## Contents
<a name="API_JwtIssuerInput_Contents"></a>

 ** audiences **   <a name="apigw-Type-JwtIssuerInput-audiences"></a>
The audiences that the issuer can issue tokens for. None can be empty. The token's `aud` claim must contain at least one of these values.
Type: Array of strings
Required: Yes

 ** issuer **   <a name="apigw-Type-JwtIssuerInput-issuer"></a>
The OpenID Connect (OIDC) issuer URL. The value must be an absolute `https` URL that includes a host and has no user information, query, or fragment. It must exactly match the `iss` claim of the token, and the issuer's OIDC discovery document must name this exact issuer.
Type: String
Required: Yes

 ** additionalClaims **   <a name="apigw-Type-JwtIssuerInput-additionalClaims"></a>
The additional claim rules for this issuer. Claim names must be unique within the issuer.
Type: Array of [JwtAdditionalClaim](API_JwtAdditionalClaim.md) objects
Required: No

## See Also
<a name="API_JwtIssuerInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/JwtIssuerInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/JwtIssuerInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/JwtIssuerInput)
