---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_JwtIssuer.html
---

# JwtIssuer

A trusted issuer in the returned JWT configuration.

## Contents
<a name="API_JwtIssuer_Contents"></a>

 ** additionalClaims **   <a name="apigw-Type-JwtIssuer-additionalClaims"></a>
The additional claim rules configured for this issuer.
Type: Array of [JwtAdditionalClaim](API_JwtAdditionalClaim.md) objects
Required: No

 ** audiences **   <a name="apigw-Type-JwtIssuer-audiences"></a>
The audiences that the issuer can issue tokens for.
Type: Array of strings
Required: No

 ** issuer **   <a name="apigw-Type-JwtIssuer-issuer"></a>
The OpenID Connect (OIDC) issuer URL.
Type: String
Required: No

 ** jwksUri **   <a name="apigw-Type-JwtIssuer-jwksUri"></a>
The JSON Web Key Set (JWKS) URI that API Gateway resolved from the issuer's OpenID Connect discovery document. This value is read-only and cannot be set.
Type: String
Required: No

## See Also
<a name="API_JwtIssuer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/JwtIssuer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/JwtIssuer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/JwtIssuer)
