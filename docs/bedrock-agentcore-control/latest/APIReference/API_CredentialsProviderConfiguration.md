---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CredentialsProviderConfiguration.html
---

# CredentialsProviderConfiguration

The configuration for a payment connector. Specifies the payment provider type and either its associated credential provider or, for an AWS Billing payment connector, its billing configuration.

## Contents
<a name="API_CredentialsProviderConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsBilling **   <a name="bedrockagentcorecontrol-Type-CredentialsProviderConfiguration-awsBilling"></a>
The configuration for an AWS Billing payment connector. The service sets this configuration when it creates the connector and returns it in responses. Don't specify it when you create an AWS Billing payment connector.
Type: [AwsBillingConnectorConfiguration](API_AwsBillingConnectorConfiguration.md) object
Required: No

 ** coinbaseCDP **   <a name="bedrockagentcorecontrol-Type-CredentialsProviderConfiguration-coinbaseCDP"></a>
The credential provider configuration for a Coinbase CDP payment connector.
Type: [PaymentCredentialProviderConfiguration](API_PaymentCredentialProviderConfiguration.md) object
Required: No

 ** stripePrivy **   <a name="bedrockagentcorecontrol-Type-CredentialsProviderConfiguration-stripePrivy"></a>
The credential provider configuration for a Stripe Privy payment connector.
Type: [PaymentCredentialProviderConfiguration](API_PaymentCredentialProviderConfiguration.md) object
Required: No

## See Also
<a name="API_CredentialsProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CredentialsProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CredentialsProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CredentialsProviderConfiguration)
