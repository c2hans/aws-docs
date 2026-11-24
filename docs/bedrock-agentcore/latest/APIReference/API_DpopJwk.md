---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DpopJwk.html
---

# DpopJwk

An elliptic curve public key in JSON Web Key (JWK) format, as described in RFC 7518 section 6.2, used to bind a payment token to the agent.

## Contents
<a name="API_DpopJwk_Contents"></a>

 ** crv **   <a name="BedrockAgentCore-Type-DpopJwk-crv"></a>
The elliptic curve of the key.
Type: String
Valid Values: `P-256 | P-384 | P-521`
Required: Yes

 ** kty **   <a name="BedrockAgentCore-Type-DpopJwk-kty"></a>
The key type. The only valid value is `EC`.
Type: String
Valid Values: `EC`
Required: Yes

 ** x **   <a name="BedrockAgentCore-Type-DpopJwk-x"></a>
The x-coordinate of the elliptic curve point, base64url-encoded.
Type: String
Length Constraints: Minimum length of 43. Maximum length of 128.
Required: Yes

 ** y **   <a name="BedrockAgentCore-Type-DpopJwk-y"></a>
The y-coordinate of the elliptic curve point, base64url-encoded.
Type: String
Length Constraints: Minimum length of 43. Maximum length of 128.
Required: Yes

## See Also
<a name="API_DpopJwk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DpopJwk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DpopJwk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DpopJwk)
