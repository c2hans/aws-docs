---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AwsBillingX402PaymentOutput.html
---

# AwsBillingX402PaymentOutput

The output of an AWS Billing x402 payment.

## Contents
<a name="API_AwsBillingX402PaymentOutput_Contents"></a>

 ** paymentToken **   <a name="BedrockAgentCore-Type-AwsBillingX402PaymentOutput-paymentToken"></a>
The payment token, a signed JSON Web Token (JWT). Include it when you retry your request to the seller. Treat the payment token as a credential: don't log or share it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-AwsBillingX402PaymentOutput-version"></a>
The x402 protocol version. This is the same value as the `version` in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`
Required: Yes

## See Also
<a name="API_AwsBillingX402PaymentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AwsBillingX402PaymentOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AwsBillingX402PaymentOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AwsBillingX402PaymentOutput)
