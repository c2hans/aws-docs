---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentconnector-credentialsproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentConnector CredentialsProviderConfiguration
<a name="aws-properties-bedrockagentcore-paymentconnector-credentialsproviderconfiguration"></a>

The credential provider configuration for a payment connector. Specifies the payment provider type and its associated credential provider.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-syntax.json"></a>

```
{
  "[CoinbaseCDP](#cfn-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-coinbasecdp)" : {{PaymentCredentialProviderConfiguration}},
  "[StripePrivy](#cfn-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-stripeprivy)" : {{PaymentCredentialProviderConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-syntax.yaml"></a>

```
  [CoinbaseCDP](#cfn-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-coinbasecdp): {{
    PaymentCredentialProviderConfiguration}}
  [StripePrivy](#cfn-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-stripeprivy): {{
    PaymentCredentialProviderConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-properties"></a>

`CoinbaseCDP`  <a name="cfn-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-coinbasecdp"></a>
The credential provider configuration for a Coinbase CDP payment connector.
*Required*: No
*Type*: [PaymentCredentialProviderConfiguration](aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripePrivy`  <a name="cfn-bedrockagentcore-paymentconnector-credentialsproviderconfiguration-stripeprivy"></a>
The credential provider configuration for a Stripe Privy payment connector.
*Required*: No
*Type*: [PaymentCredentialProviderConfiguration](aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
