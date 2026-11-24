---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider StripeConfigurationInput

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-description"></a>The `StripeConfigurationInput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-syntax.json"></a>

```json
{
  "[PublishableKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-publishablekey)" : {{String}},
  "[RestrictedKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkey)" : {{String}},
  "[RestrictedKeyConfig](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkeyconfig)" : {{SecretReference}},
  "[RestrictedKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkeysource)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-syntax.yaml"></a>

```yaml
  [PublishableKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-publishablekey): {{String}}
  [RestrictedKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkey): {{String}}
  [RestrictedKeyConfig](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkeyconfig): {{
    SecretReference}}
  [RestrictedKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkeysource): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-properties"></a>

`PublishableKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-publishablekey"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^pk_(live|test)_[A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkey"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_]*$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedKeyConfig`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkeyconfig"></a>
Property description not available.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-paymentcredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedKeySource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationinput-restrictedkeysource"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
