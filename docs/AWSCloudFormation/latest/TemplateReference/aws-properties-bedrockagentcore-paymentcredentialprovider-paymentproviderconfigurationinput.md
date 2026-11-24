---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider PaymentProviderConfigurationInput

Provider configuration input containing credentials for creation and update operations. Credentials are stored as secrets in AWS Secrets Manager.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-syntax.json"></a>

```json
{
  "[AmazonPayConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-amazonpayconfiguration)" : {{AmazonPayConfigurationInput}},
  "[CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-coinbasecdpconfiguration)" : {{CoinbaseCdpConfigurationInput}},
  "[PayPalConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-paypalconfiguration)" : {{PayPalConfigurationInput}},
  "[StripeConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeconfiguration)" : {{StripeConfigurationInput}},
  "[StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeprivyconfiguration)" : {{StripePrivyConfigurationInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-syntax.yaml"></a>

```yaml
  [AmazonPayConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-amazonpayconfiguration): {{
    AmazonPayConfigurationInput}}
  [CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-coinbasecdpconfiguration): {{
    CoinbaseCdpConfigurationInput}}
  [PayPalConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-paypalconfiguration): {{
    PayPalConfigurationInput}}
  [StripeConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeconfiguration): {{
    StripeConfigurationInput}}
  [StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeprivyconfiguration): {{
    StripePrivyConfigurationInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-properties"></a>

`AmazonPayConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-amazonpayconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [AmazonPayConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CoinbaseCdpConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-coinbasecdpconfiguration"></a>
Coinbase CDP configuration input, containing API credentials.
*Required*: No
*Type*: [CoinbaseCdpConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PayPalConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-paypalconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [PayPalConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripeConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [StripeConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripePrivyConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeprivyconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [StripePrivyConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
