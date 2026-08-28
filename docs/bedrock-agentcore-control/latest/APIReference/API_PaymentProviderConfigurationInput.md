---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_PaymentProviderConfigurationInput.html
---

# PaymentProviderConfigurationInput
<a name="API_PaymentProviderConfigurationInput"></a>

Provider configuration input — contains secrets for creation and update. Varies by vendor type.

## Contents
<a name="API_PaymentProviderConfigurationInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** coinbaseCdpConfiguration **   <a name="bedrockagentcorecontrol-Type-PaymentProviderConfigurationInput-coinbaseCdpConfiguration"></a>
The Coinbase CDP configuration.
Type: [CoinbaseCdpConfigurationInput](API_CoinbaseCdpConfigurationInput.md) object
Required: No

 ** stripePrivyConfiguration **   <a name="bedrockagentcorecontrol-Type-PaymentProviderConfigurationInput-stripePrivyConfiguration"></a>
The Stripe Privy configuration.
Type: [StripePrivyConfigurationInput](API_StripePrivyConfigurationInput.md) object
Required: No

## See Also
<a name="API_PaymentProviderConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PaymentProviderConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PaymentProviderConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PaymentProviderConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
