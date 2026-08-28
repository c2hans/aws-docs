---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider PaymentProviderConfigurationOutput
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput"></a>

Provider configuration output, containing the Amazon Resource Names (ARNs) of the secrets that store the credentials. Raw credential values aren't returned.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-syntax.json"></a>

```
{
  "[CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-coinbasecdpconfiguration)" : {{CoinbaseCdpConfigurationOutput}},
  "[StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeprivyconfiguration)" : {{StripePrivyConfigurationOutput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-syntax.yaml"></a>

```
  [CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-coinbasecdpconfiguration): {{
    CoinbaseCdpConfigurationOutput}}
  [StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeprivyconfiguration): {{
    StripePrivyConfigurationOutput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-properties"></a>

`CoinbaseCdpConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-coinbasecdpconfiguration"></a>
Coinbase CDP configuration output, containing the Amazon Resource Names (ARNs) of the secrets that store the credentials.
*Required*: No
*Type*: [CoinbaseCdpConfigurationOutput](aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripePrivyConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationoutput-stripeprivyconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [StripePrivyConfigurationOutput](aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
