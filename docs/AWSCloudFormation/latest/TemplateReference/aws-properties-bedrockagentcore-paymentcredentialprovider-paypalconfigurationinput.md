---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider PayPalConfigurationInput

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-description"></a>The `PayPalConfigurationInput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-syntax.json"></a>

```json
{
  "[ClientId](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientid)" : {{String}},
  "[ClientSecret](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecret)" : {{String}},
  "[ClientSecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecretconfig)" : {{SecretReference}},
  "[ClientSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecretsource)" : {{String}},
  "[Environment](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-environment)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-syntax.yaml"></a>

```yaml
  [ClientId](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientid): {{String}}
  [ClientSecret](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecret): {{String}}
  [ClientSecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecretconfig): {{
    SecretReference}}
  [ClientSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecretsource): {{String}}
  [Environment](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-environment): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-properties"></a>

`ClientId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecret"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9+/=\-_]*$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretConfig`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecretconfig"></a>
Property description not available.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-paymentcredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-clientsecretsource"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationinput-environment"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `LIVE | SANDBOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
