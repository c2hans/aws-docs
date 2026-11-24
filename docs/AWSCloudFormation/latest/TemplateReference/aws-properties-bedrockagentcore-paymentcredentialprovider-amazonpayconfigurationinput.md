---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider AmazonPayConfigurationInput

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-description"></a>The `AmazonPayConfigurationInput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-syntax.json"></a>

```json
{
  "[AmazonPayRegion](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-amazonpayregion)" : {{String}},
  "[AuthorizationToken](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtoken)" : {{String}},
  "[AuthorizationTokenConfig](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtokenconfig)" : {{SecretReference}},
  "[AuthorizationTokenSource](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtokensource)" : {{String}},
  "[Environment](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-environment)" : {{String}},
  "[MerchantId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-merchantid)" : {{String}},
  "[StoreId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-storeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-syntax.yaml"></a>

```yaml
  [AmazonPayRegion](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-amazonpayregion): {{String}}
  [AuthorizationToken](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtoken): {{String}}
  [AuthorizationTokenConfig](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtokenconfig): {{
    SecretReference}}
  [AuthorizationTokenSource](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtokensource): {{String}}
  [Environment](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-environment): {{String}}
  [MerchantId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-merchantid): {{String}}
  [StoreId](#cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-storeid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-properties"></a>

`AmazonPayRegion`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-amazonpayregion"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NA | EU | JP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthorizationToken`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtoken"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9+/=._\-]*$`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationTokenConfig`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtokenconfig"></a>
Property description not available.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-paymentcredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationTokenSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-authorizationtokensource"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-environment"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `LIVE | SANDBOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MerchantId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-merchantid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StoreId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-amazonpayconfigurationinput-storeid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
