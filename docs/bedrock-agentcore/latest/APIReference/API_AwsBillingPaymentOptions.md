---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AwsBillingPaymentOptions.html
---

# AwsBillingPaymentOptions

Optional settings for an AWS Billing payment.

## Contents
<a name="API_AwsBillingPaymentOptions_Contents"></a>

 ** dpopJwk **   <a name="BedrockAgentCore-Type-AwsBillingPaymentOptions-dpopJwk"></a>
The agent's public key for Demonstrating Proof of Possession (DPoP), as described in RFC 9449. If you specify a key, the payment token is bound to it, and the seller can verify that the token is presented by the holder of the matching private key. If you don't specify a key, the payment token isn't bound to a key.
Type: [DpopJwk](API_DpopJwk.md) object
Required: No

## See Also
<a name="API_AwsBillingPaymentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AwsBillingPaymentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AwsBillingPaymentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AwsBillingPaymentOptions)
