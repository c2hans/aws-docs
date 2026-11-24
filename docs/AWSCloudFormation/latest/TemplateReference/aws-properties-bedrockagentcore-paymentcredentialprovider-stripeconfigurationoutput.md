---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider StripeConfigurationOutput

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-description"></a>The `StripeConfigurationOutput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-syntax.json"></a>

```json
{
  "[PublishableKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-publishablekey)" : {{String}},
  "[RestrictedKeyArn](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeyarn)" : {{SecretInfo}},
  "[RestrictedKeyJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeyjsonkey)" : {{String}},
  "[RestrictedKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeysource)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-syntax.yaml"></a>

```yaml
  [PublishableKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-publishablekey): {{String}}
  [RestrictedKeyArn](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeyarn): {{
    SecretInfo}}
  [RestrictedKeyJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeyjsonkey): {{String}}
  [RestrictedKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeysource): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-properties"></a>

`PublishableKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-publishablekey"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^pk_(live|test)_[A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedKeyArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeyarn"></a>
Property description not available.
*Required*: Yes
*Type*: [SecretInfo](aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedKeyJsonKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeyjsonkey"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedKeySource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeconfigurationoutput-restrictedkeysource"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
