---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider PaymentProviderConfigurationInput
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput"></a>

Provider configuration input containing credentials for creation and update operations. Credentials are stored as secrets in AWS Secrets Manager.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-syntax.json"></a>

```
{
  "[CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-coinbasecdpconfiguration)" : {{CoinbaseCdpConfigurationInput}},
  "[StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeprivyconfiguration)" : {{StripePrivyConfigurationInput}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-syntax.yaml"></a>

```
  [CoinbaseCdpConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-coinbasecdpconfiguration): {{
    CoinbaseCdpConfigurationInput}}
  [StripePrivyConfiguration](#cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeprivyconfiguration): {{
    StripePrivyConfigurationInput}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-properties"></a>

`CoinbaseCdpConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-coinbasecdpconfiguration"></a>
Coinbase CDP configuration input, containing API credentials.
*Required*: No
*Type*: [CoinbaseCdpConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StripePrivyConfiguration`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paymentproviderconfigurationinput-stripeprivyconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [StripePrivyConfigurationInput](aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
