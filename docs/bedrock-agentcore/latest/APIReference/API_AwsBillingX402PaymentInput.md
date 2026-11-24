---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_AwsBillingX402PaymentInput.html
---

# AwsBillingX402PaymentInput

The input for an AWS Billing x402 payment. The payment pays an AWS Marketplace seller's x402 (HTTP 402) payment requirement and is billed to the AWS account that owns the payment manager, through the payment manager's AWS Billing payment connector.

## Contents
<a name="API_AwsBillingX402PaymentInput_Contents"></a>

 ** payload **   <a name="BedrockAgentCore-Type-AwsBillingX402PaymentInput-payload"></a>
The seller's x402 payment requirement for AWS Billing, passed unchanged as a JSON object. The service reads the seller-signed quote token from `extra.quoteToken` and returns a `ValidationException` if it is missing or invalid. Any change to the quote token invalidates its signature.
Type: JSON value
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-AwsBillingX402PaymentInput-version"></a>
The x402 protocol version of the seller's HTTP 402 response, from its `x402Version` field. For example, `2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`
Required: Yes

 ** options **   <a name="BedrockAgentCore-Type-AwsBillingX402PaymentInput-options"></a>
Optional settings for the AWS Billing payment.
Type: [AwsBillingPaymentOptions](API_AwsBillingPaymentOptions.md) object
Required: No

## See Also
<a name="API_AwsBillingX402PaymentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AwsBillingX402PaymentInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AwsBillingX402PaymentInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AwsBillingX402PaymentInput)
