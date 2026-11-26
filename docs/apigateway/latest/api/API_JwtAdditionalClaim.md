---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_JwtAdditionalClaim.html
---

# JwtAdditionalClaim

An additional claim rule for an issuer.

## Contents
<a name="API_JwtAdditionalClaim_Contents"></a>

 ** claimName **   <a name="apigw-Type-JwtAdditionalClaim-claimName"></a>
The name of the claim to check. The value cannot be empty and cannot be `iss`, `aud`, `exp`, `nbf`, `iat`, `scope`, or `scp`.
Type: String
Required: Yes

 ** format **   <a name="apigw-Type-JwtAdditionalClaim-format"></a>
The format of the claim value. The only valid value is `SINGLE_STRING`.
Type: String
Valid Values: `SINGLE_STRING`
Required: Yes

 ** expectedValues **   <a name="apigw-Type-JwtAdditionalClaim-expectedValues"></a>
The accepted value for the claim. The value cannot be empty. When a value is specified, the claim must match it exactly, and the match is case-sensitive. When no value is specified, the claim only has to be present.
Type: Array of strings
Required: No

 ** required **   <a name="apigw-Type-JwtAdditionalClaim-required"></a>
Specifies whether the claim must be present in the token. Defaults to `false`. When `true`, the token must contain the claim.
Type: Boolean
Required: No

## See Also
<a name="API_JwtAdditionalClaim_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/JwtAdditionalClaim)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/JwtAdditionalClaim)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/JwtAdditionalClaim)
