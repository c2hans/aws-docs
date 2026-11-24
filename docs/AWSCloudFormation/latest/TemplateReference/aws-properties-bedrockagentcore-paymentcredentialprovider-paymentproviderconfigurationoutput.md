---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider PaymentProviderConfigurationOutput

Provider configuration output, containing the Amazon Resource Names (ARNs) of the secrets that store the credentials. Raw credential values aren't returned.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-syntax.json"></a>

```json
{
  "[AmazonPayConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-amazonpayconfiguration)" : {{AmazonPayConfigurationOutput}},
  "[CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-coinbasecdpconfiguration)" : {{CoinbaseCdpConfigurationOutput}},
  "[PayPalConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-paypalconfiguration)" : {{PayPalConfigurationOutput}},
  "[StripeConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeconfiguration)" : {{StripeConfigurationOutput}},
  "[StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeprivyconfiguration)" : {{StripePrivyConfigurationOutput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-syntax.yaml"></a>

```yaml
  [AmazonPayConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-amazonpayconfiguration): {{
    AmazonPayConfigurationOutput}}
  [CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-coinbasecdpconfiguration): {{
    CoinbaseCdpConfigurationOutput}}
  [PayPalConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-paypalconfiguration): {{
    PayPalConfigurationOutput}}
  [StripeConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeconfiguration): {{
    StripeConfigurationOutput}}
  [StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeprivyconfiguration): {{
    StripePrivyConfigurationOutput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-properties"></a>

`AmazonPayConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-amazonpayconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [AmazonPayConfigurationOutput](aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CoinbaseCdpConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-coinbasecdpconfiguration"></a>
Coinbase CDP configuration output, containing the Amazon Resource Names (ARNs) of the secrets that store the credentials.
*Required*: No
*Type*: [CoinbaseCdpConfigurationOutput](aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PayPalConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-paypalconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [PayPalConfigurationOutput](aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripeConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [StripeConfigurationOutput](aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripePrivyConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeprivyconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [StripePrivyConfigurationOutput](aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
