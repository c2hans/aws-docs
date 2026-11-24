---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider PayPalConfigurationOutput

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-description"></a>The `PayPalConfigurationOutput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-syntax.json"></a>

```json
{
  "[ClientId](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientid)" : {{String}},
  "[ClientSecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretarn)" : {{SecretInfo}},
  "[ClientSecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretjsonkey)" : {{String}},
  "[ClientSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretsource)" : {{String}},
  "[Environment](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-environment)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-syntax.yaml"></a>

```yaml
  [ClientId](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientid): {{String}}
  [ClientSecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretarn): {{
    SecretInfo}}
  [ClientSecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretjsonkey): {{String}}
  [ClientSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretsource): {{String}}
  [Environment](#cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-environment): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-properties"></a>

`ClientId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretarn"></a>
Property description not available.
*Required*: Yes
*Type*: [SecretInfo](aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretJsonKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretjsonkey"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-clientsecretsource"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Environment`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-paypalconfigurationoutput-environment"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `LIVE | SANDBOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
