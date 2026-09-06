---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentConnector PaymentCredentialProviderConfiguration
<a name="aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration"></a>

Configuration for a payment credential provider that stores authentication credentials for a payment provider.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration-syntax.json"></a>

```
{
  "[CredentialProviderArn](#cfn-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration-credentialproviderarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration-syntax.yaml"></a>

```
  [CredentialProviderArn](#cfn-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration-credentialproviderarn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration-properties"></a>

`CredentialProviderArn`  <a name="cfn-bedrockagentcore-paymentconnector-paymentcredentialproviderconfiguration-credentialproviderarn"></a>
The Amazon Resource Name (ARN) of the credential provider that stores the authentication credentials for the payment provider.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
